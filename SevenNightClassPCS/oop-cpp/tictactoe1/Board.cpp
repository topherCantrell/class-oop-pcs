#include "Board.h"

#include <string>
using namespace std;

Board::Board() {
	clearBoard();
}

Board::~Board() {
}

string Board::getStringRepr() {
	// In the OO version, change this to a call on getCell
	string ret = string(1,board[0])+"|"+string(1,board[1])+"|"+string(1,board[2])+"\n";
	ret = ret + "-+-+-\n";
	ret = ret + string(1,board[3])+"|"+string(1,board[4])+"|"+string(1,board[5])+"\n";
	ret = ret + "-+-+-\n";
	ret = ret + string(1,board[6])+"|"+string(1,board[7])+"|"+string(1,board[8]);
	return ret;
}

bool Board::checkThreeInARow(char token) {
	if(board[0]==token && board[1]==token && board[2]==token) return true;
	if(board[3]==token && board[4]==token && board[5]==token) return true;
	if(board[6]==token && board[7]==token && board[8]==token) return true;
	if(board[0]==token && board[3]==token && board[6]==token) return true;
	if(board[1]==token && board[4]==token && board[7]==token) return true;
	if(board[2]==token && board[5]==token && board[8]==token) return true;
	if(board[0]==token && board[4]==token && board[8]==token) return true;
	if(board[2]==token && board[4]==token && board[7]==token) return true;
	return false;
}

char Board::getStatus() {
	if(checkThreeInARow('X')) return 'X';
	if(checkThreeInARow('O')) return 'O';
	for(int x=0;x<9;++x) {
		if(board[x]==' ') return ' ';
	}
	return 'C';
}

char Board::getCell(int cell) {
	return board[cell];
}

void Board::makeMove(int cell, char token) {
	board[cell] = token;
}

void Board::clearBoard() {
	for(int x=0;x<9;++x) {
		board[x] = ' ';
	}
}
