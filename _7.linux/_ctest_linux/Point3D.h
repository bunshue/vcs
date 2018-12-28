#include "Point2D.h"

class Point3D : public Point2D { 
public: 
    Point3D() { 
        _z = 0; 
    } 
    Point3D(int x, int y, int z) : Point2D(x, y), _z(z) { 
    } 
    int z() {return _z;}
    void z(int z) {_z = z;}
 
private:
    int _z;
};

