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
    {1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
    {0.0, 0.0, 1.0},		//-z �� ��
    {1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
    {0.0, 1.0, 1.0},		//-x �� Cyan �ѫC
    {1.0, 1.0, 0.0},		//-y �U ��
    {1.0, 0.0, 1.0},		//+x �k Magenta���
    {0.0, 1.0, 0.0},		//+y �W ��
    {1.0, 0.0, 0.0}			//+z �e ��
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
    0, 3, 2, 1,		//��, -z�b
    2, 3, 7, 6,		//�W, +y�b
    0, 4, 7, 3,		//��, -x�b
    1, 2, 6, 5,		//�k, +x�b
    4, 5, 6, 7,		//�e, +z�b
    0, 1, 5, 4		//�U, -y�b
};

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//��U�b�����ਤ��
GLint axis = 0;	//0: ¶x�b����, 1: ¶y�b����, 2: ¶z�b����
GLdouble viewer[] = { 0.0, 0.0, 5.0 }; /* initial viewer location  */

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

double eyex = 0.0f;
double eyey = 0.0f;
double eyez = 0.0f;
double eye_distance = 2.0f;

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
    glEnableClientState(GL_COLOR_ARRAY);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, 0, vertices);		//�q vertices �}�C��_, �C3�I���@��, �@8�ӳ��I
    glColorPointer(3, GL_FLOAT, 0, vertex_color);	//�q vertex_color �}�C��_, �C3�I���@��, �@8���C��, �Ψ�䤤6��
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);	//�q cubeIndices �}�C �̭���X 24 �ӯ��޼�
    //��GL_QUADS�N�O�C4�Ӳզ��@�ӥ|��� => �@6�ӭ�

    //�w����ᤧ�y�жb
    draw_coordinates(1.5f);     //�e�y�жb

    draw_teapot(color_purple, 1.0f, 1.5f);	//�e����

    glColor3f(1.0f, 1.0f, 1.0f);

    for (int i = 0; i < 8; i++)
    {
        glRasterPos3fv((GLfloat*)vertices[i]);
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
    }
    glFlush();  // ����ø�ϩR�O
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

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("�A�ҫ����䪺�X�O%x\t���ɵ��������ƹ��y�ЬO(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //���}����
        glutDestroyWindow(glutGetWindow());
        return;
    case 'x':
        printf("�q ��X�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = eye_distance;
        eyey = 0.0f;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'X':
        printf("�q �tX�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = -eye_distance;
        eyey = 0.0f;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'y': /* positive y-axis */
        printf("�q ��Y�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = eye_distance;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0);
        break;
    case 'Y': /* negative y-axis */
        printf("�q �tY�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = -eye_distance;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
        break;
    case 'z':
        printf("�q ��Z�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = 0.0f;
        eyez = eye_distance;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'Z':
        printf("�q �tZ�b �ѥ~�V����\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = 0.0f;
        eyez = -eye_distance;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
        /*   TBD
    case '+':
        printf("Zoom in\n");
        eye_distance -= 0.02f;
        if (eye_distance < 0.1f)
            eye_distance = 0.1f;
        break;
    case '-':
        printf("Zoom out\n");
        eye_distance += 0.02f;
        if (eye_distance > 5.0f)
            eye_distance = 5.0f;
        break;
        */
    }
    glutPostRedisplay();    //�N��e�������W�аO�A�аO��ݭn�A����ܡC
}

int main(int argc, char** argv)
{
    const char* windowName = "Color Cube";
    const char* message = "�� x X y Y z Z �ѦU�Ӥ�V�h�ݤ��, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    //���O�d
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glEnable(GL_DEPTH_TEST);
    colorcube();

    /* Set initial view to positive x-axis. */
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    printf("�q ��X�b �ѥ~�V����\n");
    eyex = eye_distance;
    gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0); //��X�b

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
