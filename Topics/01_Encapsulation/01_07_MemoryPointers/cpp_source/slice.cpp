#include <iostream>

using namespace std;

class Point {
public:
    int x, y;
    virtual void speak() {
        cout << "In Point" << endl;
    }
};

class LoudPoint: public Point {
public:
    int volume;
    virtual void speak() {
        cout << "In LoudPoint" << endl;
    }
};

class HoldLoudPoint: public LoudPoint {
public:
    int hold;
    virtual void speak() {
        cout << "In HoldLoudPoint" << endl;
    }
};

class Line {
public:
    Point * start;
    Point * end;
};

class Chart {
public:
    Line axis1;
    Line axis2;
    Line axis3;
};

void pointSpeak(Point p) {
    p.speak();
}

Point doStuff(int a, Point x) {
    return x;
}

int main(int argc, char ** argv) {

    int a, b;
    b = a;
    a = a + b;

    Point x, y;
    y = x;
    x = x + y;

    Point g = doStuff(a, x);

    /*
     HoldLoudPoint h;
     pointSpeak(h);
     Line a;
     Chart b;
     Chart * c = new Chart();
     */
    /*
     Point * common = new Point();
     Line a;
     Line b;
     a.start = common;
     b.start = common;

     a.start->x = 20;
     cout << b.start->x;
     */
}
