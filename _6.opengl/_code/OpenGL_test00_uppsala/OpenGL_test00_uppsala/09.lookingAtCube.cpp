#include "../../Common.h"

// Vertices of the cube, centered at the origin.
//每3點為一組
GLfloat vertices[][3] =
{
    {-1.0, -1.0, -1.0},		//0
    {1.0, -1.0, -1.0},		//1
    {1.0, 1.0, -1.0},		//2
    {-1.0, 1.0, -1.0},		//3
    {-1.0, -1.0, 1.0},		//4
    {1.0, -1.0, 1.0},		//5
    {1.0, 1.0, 1.0},		//6
    {-1.0, 1.0, 1.0}		//7
};

// Colors of the vertices.
//每3點為一組
GLfloat vertex_color[][3] =
{
	{1.0, 1.0, 1.0},		//0, 未用到 白色  XXXX
	{0.0, 0.0, 1.0},		//1, -z 後 藍
	{1.0, 1.0, 1.0},		//2, 未用到 白色  XXXX
	{0.0, 1.0, 1.0},		//3, -x 左 Cyan 天青
	{1.0, 1.0, 0.0},		//4, -y 下 黃
	{1.0, 0.0, 1.0},		//5, +x 右 Magenta桃紅
	{0.0, 1.0, 0.0},		//6, +y 上 綠
	{1.0, 0.0, 0.0}			//7, +z 前 紅
};

// Indices of the vertices to make up the six faces of the cube. 需要照順序 法線朝外才可以
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//後, -z軸 藍
	2, 3, 7, 6,		//上, +y軸 綠
	0, 4, 7, 3,		//左, -x軸 天青
	1, 2, 6, 5,		//右, +x軸 桃紅
	4, 5, 6, 7,		//前, +z軸 紅
	0, 1, 5, 4		//下, -y軸 黃
};
//以第4點為對應顏色

void display(void)
{
    //設定cubic之頂點與顏色
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, 0, vertices);		//從 vertices 陣列找起, 每3點為一組, 共8個頂點
    glEnableClientState(GL_COLOR_ARRAY);
    glColorPointer(3, GL_FLOAT, 0, vertex_color);	//從 vertex_color 陣列找起, 每3點為一組, 共8種顏色, 用到其中6種

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);	//從 cubeIndices 陣列 裡面找出 24 個索引數
    //用GL_QUADS就是每4個組成一個四邊形 => 共6個面

    //已旋轉後之座標軸
    draw_coordinates(1.5f);     //畫座標軸

    draw_teapot(color_purple, 1.0f, 1.5f);	//畫茶壺

    glColor3f(1.0f, 1.0f, 1.0f);

    for (int i = 0; i < 8; i++)
    {
        glRasterPos3fv((GLfloat*)vertices[i]);
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
    }
    glFlush();  // 執行繪圖命令
}

// This is the reshape callback function. It resets the viewport to the entire window and
// the projection matrix to keep the cube centered in the window.
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
    {
        glOrtho(-2.0, 2.0, -2.0 * (GLfloat)h / (GLfloat)w, 2.0 * (GLfloat)h / (GLfloat)w, 1.0, 5.0);
    }
    else
    {
        glOrtho(-2.0 * (GLfloat)w / (GLfloat)h, 2.0 * (GLfloat)w / (GLfloat)h, -2.0, 2.0, 1.0, 5.0);
    }
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
    const char* windowName = "Color Cube";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    //先保留
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glEnable(GL_DEPTH_TEST);

    /* Set initial view to positive x-axis. */
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
