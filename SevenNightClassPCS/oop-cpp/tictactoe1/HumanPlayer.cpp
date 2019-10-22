#include "HumanPlayer.h"

HumanPlayer::HumanPlayer(Board * brd, char tok) {
	board = brd;
	token = tok;
}

HumanPlayer::~HumanPlayer() {
}

int HumanPlayer::getMove() {
	return 0;
}
