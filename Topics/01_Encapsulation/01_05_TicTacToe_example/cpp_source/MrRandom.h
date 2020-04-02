#ifndef MRRANDOM_H_
#define MRRANDOM_H_

#include "Board.h"

class MrRandom {

	char token;
	Board * board;

public:

	MrRandom(Board * brd, char tok);
	virtual ~MrRandom();

	int getMove();
};

#endif /* MRRANDOM_H_ */
