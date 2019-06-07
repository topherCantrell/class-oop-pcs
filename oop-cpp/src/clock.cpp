
#include <iostream>
using namespace std;

class Clock {

	int hours,minutes,seconds;

public:

	Clock(int h, int m, int s) :
		hours(h),minutes(m),seconds(s) {
	}

	virtual int getHours() {
		return hours;
	}

};

class Animal {
public:
	virtual void sayHi() {
		cout << "I am not a plant." << endl;
	}
};

class Dog : public Animal {
public:
	virtual void sayHi() {
		cout << "Bark Bark!" << endl;
	}
};

int main() {
	Clock c(23,59,59);
	int h = c.getHours();

	Animal * p = new Dog();
	p->sayHi();
}
