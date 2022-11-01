//演示了OpenGL背面剔除，深度測試，和多邊形模式
#include "GLTools.h"
#include "GLMatrixStack.h"
#include "GLFrame.h"
#include "GLFrustum.h"
#include "GLGeometryTransform.h"

#include <math.h>
#define FREEGLUT_STATIC
#include <GL/glut.h>

////設置角色幀，作為相機
GLFrame             viewFrame;
//使用GLFrustum類來設置透視投影
GLFrustum           viewFrustum;
GLTriangleBatch     torusBatch;
GLMatrixStack       modelViewMatix;
GLMatrixStack       projectionMatrix;
GLGeometryTransform transformPipeline;
GLShaderManager     shaderManager;

//標記：背面剔除、深度測試
int iCull = 0;
int iDepth = 0;

//渲染場景
void RenderScene()
{
    //1.清除窗口和深度緩沖區
    //可以給學員演示一下不清空顏色/深度緩沖區時.渲染會造成什么問題. 殘留數據
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    
    //2.把攝像機矩陣壓入模型矩陣中
    modelViewMatix.PushMatrix(viewFrame);
    
    //3.設置繪圖顏色
    GLfloat vRed[] = { 1.0f, 1.0f, 0.0f, 1.0f };
    
    //4.
    //使用平面著色器
    //參數1：平面著色器
    //參數2：模型視圖投影矩陣
    //參數3：顏色
   // shaderManager.UseStockShader(GLT_SHADER_FLAT, transformPipeline.GetModelViewProjectionMatrix(), vRed);
    
    //使用默認光源著色器
    //通過光源、陰影效果跟提現立體效果
    //參數1：GLT_SHADER_DEFAULT_LIGHT 默認光源著色器
    //參數2：模型視圖矩陣
    //參數3：投影矩陣
    //參數4：基本顏色值
    shaderManager.UseStockShader(GLT_SHADER_DEFAULT_LIGHT, transformPipeline.GetModelViewMatrix(), transformPipeline.GetProjectionMatrix(), vRed);
    
    //5.繪制
    torusBatch.Draw();

    //6.出棧 繪制完成恢復
    modelViewMatix.PopMatrix();
    
    //7.交換緩存區
    glutSwapBuffers();
}

void SetupRC()
{
    //1.設置背景顏色
    glClearColor(0.3f, 0.3f, 0.3f, 1.0f );
    
    //2.初始化著色器管理器
    shaderManager.InitializeStockShaders();
    
    //3.將相機向后移動7個單元：肉眼到物體之間的距離
    viewFrame.MoveForward(7.0);
    
    //4.創建一個甜甜圈
    //參數1：GLTriangleBatch 容器幫助類
    //參數2：外邊緣半徑
    //參數3：內邊緣半徑
    //參數4、5：主半徑和從半徑的細分單元數量
    gltMakeTorus(torusBatch, 1.0f, 0.3f, 52, 26);
    
    //5.點的大小(方便點填充時,肉眼觀察)
    glPointSize(4.0f); 	//設定點的大小, N X N
}

//鍵位設置，通過不同的鍵位對其進行設置
//控制Camera的移動，從而改變視口
void SpecialKeys(int key, int x, int y)
{
    //1.判斷方向
    if(key == GLUT_KEY_UP)
        //2.根據方向調整觀察者位置
        viewFrame.RotateWorld(m3dDegToRad(-5.0), 1.0f, 0.0f, 0.0f);
    
    if(key == GLUT_KEY_DOWN)
        viewFrame.RotateWorld(m3dDegToRad(5.0), 1.0f, 0.0f, 0.0f);
    
    if(key == GLUT_KEY_LEFT)
        viewFrame.RotateWorld(m3dDegToRad(-5.0), 0.0f, 1.0f, 0.0f);
    
    if(key == GLUT_KEY_RIGHT)
        viewFrame.RotateWorld(m3dDegToRad(5.0), 0.0f, 1.0f, 0.0f);
    
    //3.重新刷新
    glutPostRedisplay();
}

//窗口改變
void ChangeSize(int w, int h)
{
    //1.防止h變為0
    if(h == 0)
        h = 1;
    
    //2.設置視口窗口尺寸
    glViewport(0, 0, w, h);
    
    //3.setPerspective函數的參數是一個從頂點方向看去的視場角度（用角度值表示）
    // 設置透視模式，初始化其透視矩陣
    viewFrustum.SetPerspective(35.0f, float(w)/float(h), 1.0f, 100.0f);
    
    //4.把透視矩陣加載到透視矩陣對陣中
    projectionMatrix.LoadMatrix(viewFrustum.GetProjectionMatrix());
    
    //5.初始化渲染管線
    transformPipeline.SetMatrixStacks(modelViewMatix, projectionMatrix);
}



int main(int argc, char* argv[])
{
    gltSetWorkingDirectory(argv[0]);
    
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_STENCIL);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Geometry Test Program");
    glutReshapeFunc(ChangeSize);
    glutSpecialFunc(SpecialKeys);
    glutDisplayFunc(RenderScene);
    
    
    GLenum err = glewInit();
    if (GLEW_OK != err) {
        fprintf(stderr, "GLEW Error: %s\n", glewGetErrorString(err));
        return 1;
    }
    
    SetupRC();
    
    glutMainLoop();
    return 0;
}