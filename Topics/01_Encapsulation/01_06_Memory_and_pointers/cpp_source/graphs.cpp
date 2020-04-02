#include <iostream>
using namespace std;

class Token {
public:
    char letter;
};

class Board {
public:
    Token ** cells;
};

class HumanPlayer {
public:
    Token * token;
    Board * board;
};

class RandomPlayer {
public:
    Token * token;
    Board * board;
};

class Game {
public:
    Board * board;
    HumanPlayer * player1;
    RandomPlayer * player2;
};

int main2(int argc, char ** argv) {
    Token * tokenX = new Token();
    tokenX->letter = 'X';

    Token * tokenO = new Token();
    tokenO->letter = 'O';

    Token ** tkns = new Token*[9];

    Board * brd = new Board();
    brd->cells = tkns;

    HumanPlayer * p1 = new HumanPlayer();
    p1->token = tokenX;
    p1->board = brd;

    RandomPlayer * p2 = new RandomPlayer();
    p2->token = tokenO;
    p2->board = brd;

    Game * gm = new Game();
    gm->board = brd;
    gm->player1 = p1;
    gm->player2 = p2;

    gm->board->cells[2] = gm->player1->token;
    char t = gm->board->cells[2]->letter;

    cout << t << endl;
    return 0;
}

// int -- 4 bytes each
// virtual table adds 8 bytes
class Point {
public:
    int x;
    int y;
    int data[6];
    virtual void sayHi() {
        cout << "Hi" << endl;
    }
    virtual void doOther() {
    }
};

void print(string p) {
    cout << p << endl;
    return;
}

void getMove() {
    print("What is your move?");
    print("Are you sure?");
    return;
}

void playHuman() {
    print("Ready, human!");
    getMove();
    print("Good move!");
    return;
}

void printInt(char *p) {
    cout << hex << (long long) p << " : ";
    for (int i = 3; i >= 0; --i) {
        int a = (int) (*(p + i)) & 0xFF;
        if (a < 16) {
            cout << "0";
        }
        cout << a;
    }
    cout << endl;
}

void printMemory(char * p, int num) {
    for (int x = 0; x < num; ++x) {
        printInt((char *) (p + x * 4));
    }
}

void frameCheck() {
    int a = 0xBEEF1111;
    int b = 0xBEEF2222;

    printMemory(((char *) &b), 18);
}

int main(int argc, char ** argv) {

    int a = 0xFACE5555;
    int i = 0xFACE1234;
    int b = 0xFACE4444;

//cout << "##" << hex << &a << &i << &b << endl;

    frameCheck();

//playHuman();
    return 0;
}

