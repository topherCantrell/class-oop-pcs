#include <iostream>
#include <stdarg.h>

using namespace std;

// TODO initialize outside the bracket in initializer list. See later this is how you call the super constructor.
// Python requires YOU to call the super constructor if you want it. Show if only base class has constructor.

/*

 gcc -g -c constructors.cpp
 objdump -d -M intel -S constructors.o > t.txt
 notepad t.txt

 */

class Point2 {

    int x = 22;
    int y = 33;

public:

    Point2() :
            x(22), y(33) {
        x = 22;
        y = 33;
    }

    int getX() {
        return x;
    }
};

class Point3 {
public:
    int x;
    int y;

    Point3() {
        x = 44;
        y = 45;
    }

    int getX() {
        return x;
    }

    /*
     Point3(int x, int y) :
     x(x), y(y) {
     cout << "in constructor" << endl;
     }
     */
};

class Point {

    int x;
    int y;
    //string color;

    static int numCreated;

public:

    static int getNumCreated() {
        return Point::numCreated;
    }

    Point() :
            Point(0) {
        cout << Point::numCreated << endl;

    }

    ~Point() {
        cout << "In destructor" << endl;
    }

    Point(int val) :
            Point(val, val) {
    }

    Point(int x, int y, string color = "blue") {
        this->x = x;
        this->y = y;
        //this->color = color;
    }

    Point operator+(int value) {
        Point ret(this->x + value, this->y + value);
        return ret;
    }

    bool operator==(Point other) {
        if (other.x == x && other.y == y) {
            return true;
        }
        return false;
    }

    Point addValueToXandY(int value) {
        Point ret(this->x + value, this->y + value);
        return ret;
    }

    void sayHi(string name) {
        cout << "string " << name << endl;
    }

    int sayHi(int x) {
        cout << "int " << x << endl;
        return 0;
    }

    int sayHi(long int y) {
        cout << "long " << y << endl;
        return 0;
    }

    void sayHi(int x, int y) {
        cout << "two " << x << "," << y << endl;
    }

    void init(int x, int y) {
        this->x = x;
        this->y = y;
    }

    int getX() {
        return x;
    }

    //void setX(int x) {this->x = x;}

};

int Point::numCreated = 0;

int addAll(int n, ...) {
    va_list vl;
    va_start(vl, n);
    int first = va_arg(vl, int);
    int second = va_arg(vl, int);
    va_end(vl);
    return first;
}

int usePoint(Point x) {
    cout << "In use point" << endl;
}

int main(int argc, char **argv) {

    int i = 2;

    i -= -1;

    cout << i << endl;

}
