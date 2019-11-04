#include <iostream>
using namespace std;

class ThingInt {
public:

    int thing;

    void set(int value) {
        thing = value;
    }

    int get() {
        return thing;
    }

    int sum(int other) {
        return thing + other;
    }

};

class ThingFloat {
public:

    float thing;

    void set(float value) {
        thing = value;
    }

    float get() {
        return thing;
    }

    float sum(float other) {
        return thing + other;
    }

};

class ThingStr {
public:

    string thing;

    void set(string value) {
        thing = value;
    }

    string get() {
        return thing;
    }

    string sum(string other) {
        return thing + other;
    }

};

template<class T> class Thing {
public:

    T thing;

    void set(T value) {
        thing = value;
    }

    T get() {
        return thing;
    }

    T sum(T other) {
        return thing + other;
    }

};

int main(int argc, char ** argv) {

    ThingInt i;
    ThingFloat f;
    ThingStr s;

    i.set(15);
    cout << i.sum(20) << endl;

    f.set(3.5);
    cout << f.sum(1.2) << endl;

    s.set("Hello");
    cout << s.sum("World") << endl;

    Thing<int> ti;
    Thing<float> tf;
    Thing<string> ts;

    ti.set(15);
    cout << ti.sum(20) << endl;

    tf.set(3.5);
    cout << tf.sum(1.2) << endl;

    ts.set("Hello");
    cout << ts.sum("World") << endl;

}
