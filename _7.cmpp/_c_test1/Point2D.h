class Point2D { 
public: 
    Point2D() {
        _x = 0;
        _y = 0;
    }
    Point2D(int x, int y) : _x(x), _y(y) {
    }
    int x() {return _x;} 
    int y() {return _y;} 
    void x(int x) {
        _x = x;
    }
    void y(int y) {
        _y = y;
    }
private:
    int _x;
    int _y;
};


