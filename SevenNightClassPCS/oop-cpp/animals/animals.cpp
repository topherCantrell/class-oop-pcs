#include <iostream>
using namespace std;

#include <vector>

class Animal {
public:
    virtual void sayHi() {
        cout << "Should not be here" << endl;
    }
};

class Cat: public Animal {
public:
    virtual void sayHi() {
        cout << "Meow!" << endl;
    }
};

class Dog: public Animal {
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

int main(int argc, char **argv) {

    Dog * dog = new Dog();
    Cat * cat = new Cat();

    dog->sayHi();

    vector<Animal*> zoo;

    zoo.push_back(dog);
    zoo.push_back(cat);

    zoo[0]->sayHi();

    zoo.erase(zoo.begin() + 1);
    zoo.erase(zoo.begin());

    delete dog;
    delete cat;

}
