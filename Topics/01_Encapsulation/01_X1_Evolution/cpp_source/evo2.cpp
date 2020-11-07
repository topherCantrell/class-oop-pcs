#include <iostream>
#include <string.h>
using namespace std;

class Account {
public:
    char name[12];
    char address[20];
    int phone;
    double balance;

public:
    virtual void chargeFee(double fee) {
        balance = balance - fee;
    }

    virtual void withdraw(double amount) {
        cout << "In Base" << endl;
    }

    virtual void deposit(double amount) {
    }

};

class FeeAccount: public Account {
public:
    virtual void withdraw(double amount) {
        //balance = balance - amount;
        //balance = balance - 1.00;
        cout << "In Fee" << endl;
    }
};

void takeOutEightDollars(Account & account) {

    account.withdraw(8);
    withdraw(account, 8);

}

void sayHiEN() {
    cout << "Hello" << endl;
}

void sayHiSP() {
    cout << "Hola" << endl;
}

class Point {
    //int x, y;
};

class NamePoint: public Point {

};

int main(int argc, char ** argv) {

    //Point * a = new Point();
    //a->x = 4;

    //Point b;
    //b.x = 4;

    // "greet" is a pointer to a function
    // that takes no args and returns
    // nothing.
    //void (*greet)();

    //greet = sayHiEN;

    //greet();

    //greet = sayHiSP;
    //greet();

    Account bob;

    takeOutEightDollars(bob);

    FeeAccount jan;

    takeOutEightDollars(jan);

    //jan.withdraw(5.00);

    //withdraw(&jan, 5.00);

    //double *p = (double *) &jan.phone;
    //cout << *p << endl;

}
