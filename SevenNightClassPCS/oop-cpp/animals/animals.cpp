#include <iostream>
using namespace std;

#include <vector>

class Animal {
public:
	virtual void sayHi() {
		cout << "Should not be here" << endl;
	}
};

class Cat : public Animal {
public:
	virtual void sayHi() {
		cout << "Meow!" << endl;
	}
};

class Dog : public Animal {
public:
	virtual void sayHi() {
		cout << "Woof!" << endl;
	}
};

void speak(Animal an) {
	an.sayHi();
}

void speakPoly(Animal * an) {
	an->sayHi();
}

