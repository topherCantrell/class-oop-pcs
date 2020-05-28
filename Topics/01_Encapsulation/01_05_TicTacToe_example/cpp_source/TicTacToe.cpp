#include <iostream>
using namespace std;

#include "Board.h"
#include "MrRandom.h"
#include "HumanPlayer.h"

int main(int argc, char ** argv) {

	Board * brd = new Board();
	string r = brd->getStringRepr();
	cout << r << endl;


	delete brd;

}
