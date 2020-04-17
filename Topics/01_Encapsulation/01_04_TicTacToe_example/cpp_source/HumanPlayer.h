#ifndef HUMANPLAYER_H_
#define HUMANPLAYER_H_

#include "Board.h"

class HumanPlayer {

	char token;
	Board * board;

public:

	HumanPlayer(Board * brd, char tok);
	virtual ~HumanPlayer();

	int getMove();
};

#endif /* HUMANPLAYER_H_ */
