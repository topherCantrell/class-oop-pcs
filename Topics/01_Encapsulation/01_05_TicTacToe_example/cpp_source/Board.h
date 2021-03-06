#ifndef BOARD_H_
#define BOARD_H_

#include <string>

class Board {

private:

	char board[9];

	bool checkThreeInARow(char token);

public:

	Board();
	virtual ~Board();

	std::string getStringRepr();

	char getStatus();

	char getCell(int cell);

	void makeMove(int cell, char token);

	void clearBoard();

};

#endif /* BOARD_H_ */
