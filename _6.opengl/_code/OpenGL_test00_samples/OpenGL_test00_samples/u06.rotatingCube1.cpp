#include "../../Common.h"

// Vertices of the cube, centered at the origin.
//�C3�I���@��
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
//�C3�I���@��
GLfloat vertex_color[][3] =
{
	{1.0, 1.0, 1.0},		//0, ���Ψ� �զ�  XXXX
	{0.0, 0.0, 1.0},		//1, -z �� ��
	{1.0, 1.0, 1.0},		//2, ���Ψ� �զ�  XXXX
	{0.0, 1.0, 1.0},		//3, -x �� Cyan �ѫC
	{1.0, 1.0, 0.0},		//4, -y �U ��
	{1.0, 0.0, 1.0},		//5, +x �k Magenta���
	{0.0, 1.0, 0.0},		//6, +y �W ��
	{1.0, 0.0, 0.0}			//7, +z �e ��
};

// Indices of the vertices to make up the six faces of the cube. �ݭn�Ӷ��� �k�u�¥~�~�i�H
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//��, -z�b ��
	2, 3, 7, 6,		//�W, +y�b ��
	0, 4, 7, 3,		//��, -x�b �ѫC
	1, 2, 6, 5,		//�k, +x�b ���
	4, 5, 6, 7,		//�e, +z�b ��
	0, 1, 5, 4		//�U, -y�b ��
};
//�H��4�I�������C��

// ø�Ϧ^�ը��
void display(void)
{
	//�]�wcubic�����I�P�C��
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);		//�q vertices �}�C��_, �C3�I���@��, �@8�ӳ��I
	glEnableClientState(GL_COLOR_ARRAY);
	glColorPointer(3, GL_FLOAT, 0, vertex_color);	//�q vertex_color �}�C��_, �C3�I���@��, �@8���C��, �Ψ�䤤6��

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);	//�q cubeIndices �}�C �̭���X 24 �ӯ��޼�
	//��GL_QUADS�N�O�C4�Ӳզ��@�ӥ|��� => �@6�ӭ�

	glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
	const char* windowName = "Color Cube";
	const char* message = "�����, �L����, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

	glEnable(GL_DEPTH_TEST);
	
	glShadeModel(GL_FLAT);	//���o�� �ܦ��¦�, �S�o�� �ܦ��m��

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
