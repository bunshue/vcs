#include <iostream>

void draw_coordinates(float len);
void draw_boundary(float* color, float dd);
void draw_teapot(float* color, float width, double size);
void draw_tetrahedron(void);	//畫四面體
void draw_tetrahedron2(void);

void draw_string1(const char* str, float* color, void* font, float x_st, float y_st);	//無陰影
void draw_string1s(std::string str, float* color, void* font, float x_st, float y_st);	//無陰影
void draw_string2(const char* str, float* color, void* font, float x_st, float y_st);	//有陰影
void draw_triangle(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3);

void reshape0(int w, int h);
void keyboard0(unsigned char key, int x, int y);
void mouse0(int button, int state, int x, int y);
void motion0(int x, int y);


