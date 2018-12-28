#include <iostream>
#include "Point3D.h"

using namespace std;

int main() {
    Point3D p1(1, 3, 4);
    Point3D p2; 

    cout << "p1: (" 
         << p1.x() << ", " 
         << p1.y() << ", " 
         << p1.z() << ")"
         << endl;
 
    p2.x(5);
    p2.y(7);
    p2.z(8);
 
    cout << "p2: (" 
         << p2.x() << ", " 
         << p2.y() << ", " 
         << p2.z() << ")"
         << endl;
 
    return 0;
}

