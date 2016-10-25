
#include "utility.hpp"

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdexcept>


/////////////////////////
// readCSV(path):
// 		Reads a CSV file specified by 'path' and returns a matrix of strings, with each string representing a cell.
 
CellMatrix readCSV(std::string const& path, char delim) {
	std::ifstream infile(path);
	if (infile.fail()) {
		throw std::runtime_error("Couldn't open '" + path + "'!\n");
	}
	CellMatrix mat;
	CellRow row;
	Cell cell;
	std::string line;

	while (std::getline(infile, line)) {
		row.clear();
		if (line.find_first_not_of(" \t\n\v") == std::string::npos || line[0] == '#') {
			row.push_back("");
		}
		else {
			std::stringstream linestream(line);
			while (std::getline(linestream, cell, delim)) {
				row.push_back(cell);
			}
		}
		mat.push_back(row);
	}
	return mat;
}

