#include <iostream>
#include <string.h>
using namespace std;

class Robot {

public:

    Robot(string name, int x, int y) {
        cout << "ROBOT " << name << " " << x << " " << y << endl;
    }

    void moveTo(int x, int y) {
        cout << "MOVETO " << x << " " << y << endl;
    }

    void fireLasers(float power) {
        cout << "FIRE " << power << endl;
    }

    float getFuelLevel() {
        cout << "GETFUEL" << endl;
        return 1.0;
    }

};

int main(int argc, char **argv) {

    Robot * rob = new Robot("sue", 20, 30);
    rob->fireLasers(0.5);
    rob->moveTo(5, 5);
    float f = rob->getFuelLevel();
    cout << f << endl;

    Robot r("jan", 100, 200);
    r.fireLasers(1.0);
    r.moveTo(0, 0);
    f = r.getFuelLevel();
    cout << f << endl;

}
