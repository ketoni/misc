
#include <iostream>
#include <string.h>
#include <unordered_map>
#include <algorithm>

#include "utility.hpp"

// Sorts delimited files (CSV, etc.) by most common word / value.
// Cells are sorted from left to right based on their frequency so that common cells are stored in same column.
// This means blank cells are added to row contents, but the relative order of the rows stay the same
//
// For example, the following input:
//
// 	A	C	B	E
// 	C	A
//	D	B	E	A
// 	F	B	A
// 	D	A	F	C	B	E
//
// 	Would be sorted like:
//
// 	A	B	E	C
// 	A			C
// 	A	B	E		D
// 	A	B				F
// 	A	B	E	C	D	F
//
//	In this example the executable would be called with:
//	freq_sort  "	" file_to_sort
//	Note that the firts argument must be a character. This example uses tab as the delimited, so $"\t" would work too.
//	Third (optional) argument should be a positive integer threshold which filters out coulums with low word frequency.


int main(int argc, char* argv[]) {
	
	if (argc < 3 || argc > 4) {
		std::cerr << "Usage:\tSort delimiter delimited_file [threshold]\n";
		return -1;
	}
	if (strlen(argv[1]) != 1) {
		std::cerr << "Delimiter must be a character\n";
		return -1;
	}
	uint16_t threshold = 1;
	if (argc == 4) {
		threshold = std::stoi(argv[3]);
	}


	CellMatrix matrix = readCSV(argv[2], *argv[1]);
	std::unordered_map<std::string, uint16_t> words;
	
	for (auto& row : matrix) {
		for (auto it = row.begin(); it != row.end(); ) {
			// Remove empty cells
			if (it->empty()) {
				it = row.erase(it);
				continue;
			}
			// Count the frequency of words to a map
			auto ret = words.insert(std::make_pair(*it,1));
			if (!ret.second) {
				ret.first->second++;
			}
			it++;
		}
	}
	
	// Remove all words which frequency is below threshold
	if (threshold > 1) {
		for (auto it = words.begin(); it != words.end(); ) {
			if (it->second < threshold) {
				it = words.erase(it);
			}
			else {
				it++;
			}
		}
	}

	// Create a descending order based on word frequency
	std::vector<uint16_t> order;
	for (auto elem : words) {
		order.push_back(elem.second);
	}
	std::sort(order.begin(), order.end(), std::greater<int>());
	
	// Replace frequencies with corresponding order numbers
	for (auto& elem : words) {
		for (unsigned i = 0; i < order.size(); i++) {
			if (order[i] == elem.second) {
				elem.second = i;
				order[i] = 0;
				break;
			}
		}
	}
	
	// Create a CellMatrix like the one above but with order.size() capacity on each row
	CellMatrix matrix_final;
	matrix_final.assign(matrix.size(), CellRow());
	for (auto& row_final : matrix_final) {
		row_final.assign(order.size(), "");
	}

	// Insert words from matrix to matrix_final using order numbers in 'words' map
	for (unsigned row_idx = 0; row_idx < matrix.size(); row_idx++) {
		for (unsigned cell_idx = 0; cell_idx < matrix[row_idx].size(); cell_idx++) {	
			Cell word = matrix[row_idx][cell_idx];
			auto ret = words.find(word);
			if (ret != words.end()) {
				matrix_final[row_idx][ret->second] = word;
			}	
				
		}
	}
	
	// Output results		
	for (auto& row : matrix_final) {
		for (auto& word	: row) {
			std::cout << word << *argv[1];
		}
		std::cout << "\n";	
	}

	return 0;
}
