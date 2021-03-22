#include <iostream>

using namespace std;

struct Point {
	int x;
	int y;
};

struct Line {
	Point a;
	Point b;
};

struct TTTBoard {
	Line h1;
	Line h2;
	Line v1;
	Line v2;
};

int main(int argc, char **argv) {

	int j = 0xBE025F20;

	Point p;
	p.x = 2;
	p.y = 3;

	Line g;
	g.a.x = 4;
	g.a.y = 5;

	TTTBoard board;
	board.h1.a.x = 3;

	cout << board.h1.a.x << endl;     // 3
	cout << board.h1.a.y << endl;     // garbage
	cout << board.h2.a.x << endl;     // garbage

	cout << sizeof(int) << endl;      // MyPC=4
	cout << sizeof(Point) << endl;    // MyPC=8
	cout << sizeof(Line) << endl;     // MyPC=16
	cout << sizeof(TTTBoard) << endl; //MyPC=64

}
