#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

#include <helper_gl.h>

//#include <GL/glut.h>		//32 bits
#include <GL/freeglut.h>	//64 bits

#define	PI	3.141592654F

#define abs(a, b)	(((a) > (b)) ? (a - b) : (b - a))
#define max(a,b)	((a > b) ? a : b)
#define min(a,b)	((a < b) ? a : b)

//常用的顏色 RGBA四碼
float color_r[] = { 1.0f, 0.0f, 0.0f, 1.0f };
float color_g[] = { 0.0f, 1.0f, 0.0f, 1.0f };
float color_b[] = { 0.0f, 0.0f, 1.0f, 1.0f };
float color_y[] = { 1.0f, 1.0f, 0.0f, 1.0f };
float color_m[] = { 1.0f, 0.0f, 1.0f, 1.0f };	//Magenta, 洋紅色、品紅色、紅紫色
float color_c[] = { 0.0f, 1.0f, 1.0f, 1.0f };	//Cyan, 青色
float color_black[] = { 0.0f, 0.0f, 0.0f, 1.0f };
float color_white[] = { 1.0f, 1.0f, 1.0f, 1.0f };
float color_silver[] = { 0.75f, 0.75f, 0.75f, 1.0f };
float color_gray[] = { 0.5f, 0.5f, 0.5f, 1.0f };
float color_purple[] = { 0.5f, 0.0f, 0.5f, 1.0f };

void draw_coordinates(float len);
void draw_boundary(float* color, float dd);
void draw_teapot(float* color, float width, double size);
void draw_tetrahedron(void);	//畫四面體
void draw_tetrahedron2(void);

void draw_string1(const char* str, float* color, void* font, float x_st, float y_st);	//無陰影
void draw_string1s(std::string str, float* color, void* font, float x_st, float y_st);	//無陰影
void draw_string2(const char* str, float* color, void* font, float x_st, float y_st);	//有陰影

//空心三角形
void draw_triangle(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3);

//實心三角形
void draw_triangle_s(float* color, float x1, float y1, float x2, float y2, float x3, float y3);

void draw_point(float* color, float size, float x_st, float y_st);

//空心矩形, 左下為原點, 向右w, 向上h, 顏色color, 線寬width
void draw_rectangle(float* color, float width, float x_st, float y_st, float w, float h);

//實心矩形, 左下為原點, 向右w, 向上h, 顏色color, 無線寬width
void draw_rectangle_s(float* color, float x_st, float y_st, float w, float h);

//空心四邊形, 左下為原點, 向右w, 向上h, 顏色color, 線寬width
void draw_quad(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4);

//實心四邊形, 左下為原點, 向右w, 向上h, 顏色color, 無線寬width
void draw_quad_s(float* color, float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4);

void reshape0(int w, int h);
void keyboard0(unsigned char key, int x, int y);
void mouse0(int button, int state, int x, int y);
void motion0(int x, int y);


