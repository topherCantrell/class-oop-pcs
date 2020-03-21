#include <iostream>
#include <memory>
using namespace std;

class Point {
public:
    Point() {
        cout << "Making a point" << endl;
    }
    Point(const Point &other) {
        cout << "Copy constructor" << endl;
    }
    ~Point() {
        cout << "Destroyting a point" << endl;
    }
    int x, y, z;
};

void pointDouble(Point * p) {
    int b = p->x * 2;
    p->x = b;
    p = new Point();
    p->x = 10;
}

void pointDoubleRef(Point &p) {
    int b = p.x * 2;
    p.x = b;
    //p = NULL;
    //p = new Point();

}

void main2(int argc, char **argv) {
    int b = 3;
    Point * a = new Point();
    int c = 4;
    a->x = b;
    a->y = c;
    b = 8;
    pointDouble(a);
    cout << b << endl;
    cout << a->x << endl;
}

Point pointDoubleEm(Point p) {
    cout << "Here A" << endl;
    int b = p.x * 2;
    p.x = b;
    cout << "Here B" << endl;
    Point q;
    cout << "Here C" << endl;
    q.x = 2;
    q.y = 3;
    cout << "Here D" << endl;
    p = q;
    cout << "Here E" << endl;
    return q;
}

int main(int argc, char ** argv) {
    Point a; // Not "Point a();"
    Point b;
    cout << "Here 1" << endl;
    cout << "Here 2" << endl;
    a.x = 10;
    a.y = 20;
    cout << "Here 3" << endl;
    b = pointDoubleEm(a);
    cout << "Here 4" << endl;
    cout << a.x << endl;
    cout << b.x << endl;
}

// GARBAGE collection google "C++ smart pointer circular reference"
// Java/Python handles circular references correctly

class Player {
public:
    Player * companion;
    //std::shared_ptr<Player> companion;
};

/*
 int main2(int argc, char ** argv) {


 std::shared_ptr<Player> jasmine = std::make_shared<Player>();
 std::shared_ptr<Player> albert = std::make_shared<Player>();
 Player * jasmine = new Player();
 Player * albert = new Player();
 jasmine->companion = albert;
 albert->companion = jasmine;


 bool monday = true;

 Point * p = new Point();
 // ...
 p = new Point();
 // or p = NULL;

 Point * p = new Point();
 // ...
 delete p;

 Point * p = new Point();
 Point * q = p;
 // ...
 delete q;
 cout << p->x << endl;

 Point * p = new Point();
 // ...
 if (monday) {
 delete p;
 }


 int b = 3;
 Point a;
 int c = 4;
 a.x = b;
 a.y = c;
 b = 8;
 //pointDoubleRef(a);
 pointDoubleEm(a);
 cout << b << endl;
 cout << a.x << endl;
 }
 */

