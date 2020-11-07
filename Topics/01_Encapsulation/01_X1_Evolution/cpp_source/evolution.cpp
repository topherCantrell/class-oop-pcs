#include <iostream>
#include <string.h>
using namespace std;

struct Account {
private:
    char name[12];
    char address[20];
    int phone;
    double balance;

public:
    // void chargeAccountFee(Account * this, double fee)
    void chargeFee(double fee) {
        this->balance = this->balance - fee;
        balance = balance - fee;
    }

    void withdraw(double amount) {
    }

    void deposit(double amount) {
    }

};

void chargeAccountFee(Account * acct, double fee) {
    acct->balance = acct->balance - fee;
}

char * getAccountName(Account * acct) {
    return acct->name;
}

void withdrawFromAccount(Account * acct, double amount) {

}

void depositIntoAccount(Account * acct, double amount) {

}

// void setName(Account * acct, char * newName)

int main(int argc, char ** argv) {

    Account jan;
    Account bob;

    jan.withdraw(10.0);
    jan.chargeFee(1.0);
    bob.deposit(10.0);
    bob.chargeFee(1.0);

    strcpy(jan.name, "Jan");
    jan.balance = 50.0;

    chargeAccountFee(&jan, 1.0);
    char * p = getAccountName(&bob);

    withdrawFromAccount(&jan, 10.0);
    chargeAccountFee(&jan, 1.0);

    depositIntoAccount(&bob, 10.0);
    chargeAccountFee(&bob, 1.0);

    cout << p << endl;

    cout << jan.balance;

}
