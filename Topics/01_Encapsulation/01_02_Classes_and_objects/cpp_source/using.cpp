#include <iostream>
#include <string>
using namespace std;

class Clock {

    int hours, minutes, seconds;

public:

    Clock(int h, int m, int s) :
            hours(h), minutes(m), seconds(s) {
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

class Dog: public Animal {
public:
    virtual void sayHi() {
        cout << "Bark Bark!" << endl;
    }
};

class RESTClient {
public:
    RESTClient(string url) {
    }

    string get(string url) {
        return "";

    }

    void post(string url, string data) {
    }
};

class Robot {

    int location;
    double battery;

    void moveLeftLeg() {
    }
    void moveRightLeg() {
    }

public:

    int getLocation() {
        return location;
    }

    void goTo(int loc) {
        location = loc;
        battery = battery - 0.10;
    }

    void goTo2(Robot * that, int location) {
        this->location = location;
    }

    void sayHi() {
        cout << "Beep Beep" << endl;
    }
    double getBatteryLevel() {
        return 0.0;
    }
    void goTo(double lat, double lng) {
        moveLeftLeg();
        moveRightLeg();
    }
};

class Point {
    int x, y;
public:
    int addX(int a) {
        return x + a;
        return this->x + a;
    }
};

int main() {

    Point * p = new Point();
    int a = p->addX(5);

    Point q;
    int b = q.addX(5);

    Robot * bob = new Robot();
    bob->goTo(20);
    int a = bob->getLocation();

    Robot * jan = new Robot();
    jan->goTo(50);
    int b = bob->getLocation();

    Robot * rob = new Robot();
    rob->sayHi();
    double charge = rob->getBatteryLevel();
    cout << charge << endl;
    rob->goTo(34.738, -86.60);

    //rob->moveLeftLeg();

    /*
     RESTClient * client = new RESTClient("https://io.adafruit.com/topher");

     string resp = client->get("/freezer_data");

     client->post("/freezer_data", "-10.5");

     delete client;

     RESTClient client2("https://io.adafruit.com/topher");
     string resp = client2.get("/freezer_data");
     client2.post("/freezer_data", "-10.5");

     cout << "HERE" << endl;
     */
}
