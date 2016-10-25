#ifndef UTILITY_HH
#define UTILITY_HH

#include <string>
#include <vector>
#include <iostream>

typedef std::string Cell;
typedef std::vector<Cell> CellRow;
typedef std::vector<CellRow> CellMatrix;

// For reading CSV files
CellMatrix readCSV(std::string const&, char delim);


#endif
