// OpenGL.cpp : 定义应用程序的入口点。
// 窗口程序入口
// 代码提交测试

#include "framework.h"
#include "OpenGL.h"

#include "texture.h"
#include "utils.h"

// 导入 OpenGL 的个头文件 , 必须先导入 windows.h 头文件之后再导入 opengl 头文件
#include <gl/GL.h>
#include <gl/GLU.h>

// 链接 OpenGL 库
#pragma comment(lib, "opengl32.lib")
#pragma comment(lib, "glu32.lib")

#define MAX_LOADSTRING 100

// 全局变量:
HINSTANCE hInst;                                // 当前实例
WCHAR szTitle[MAX_LOADSTRING];                  // 标题栏文本
WCHAR szWindowClass[MAX_LOADSTRING];            // 主窗口类名 

// 此代码模块中包含的函数的前向声明:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);

// 窗口设备
// 提取到全局变量中 
HDC dc = NULL;

int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPWSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: 在此处放置代码。

    // 初始化全局字符串
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_OPENGL, szWindowClass, MAX_LOADSTRING);

    // 注册窗口
    MyRegisterClass(hInstance);

    // 执行应用程序初始化:
    // 创建窗口
    if (!InitInstance (hInstance, nCmdShow))
    {
        return FALSE;
    }

    // 下面的逻辑是一个死循环 , 避免让窗口退出 

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_OPENGL));

    MSG msg;

	// 读取文件内容
	// 绝对路径 : "D:\\002_Project\\006_Visual_Studio\\OpenGL\\OpenGL\\test.txt"
	// Visual Studio 2019 中使用相对路径读取不到文件
	char* str = (char*)LoadFileContent("D:\\002_Project\\006_Visual_Studio\\OpenGL\\OpenGL\\test.txt");
	printf("%s\n", str);


	// 只显示正面 , 不显示背面
	//glEnable(GL_CULL_FACE);

	// 设置顺时针方向 CW : Clock Wind 顺时针方向
	// 默认是 GL_CCW : Counter Clock Wind 逆时针方向 
	//glFrontFace(GL_CW);

	// 默认模式, 填充模式 , 如果不设置就默认为填充模式
	//glPolygonMode(GL_FRONT, GL_FILL);

	// 设置线框模式 
	// 设置了该模式后 , 之后的所有图形都会变成线
	//glPolygonMode(GL_FRONT, GL_LINE);

	// 设置点模式 
	// 设置了该模式后 , 之后的所有图形都会变成点
	//glPolygonMode(GL_FRONT, GL_POINT);

	// 将方形的点变为圆点
	//glEnable(GL_POINT_SMOOTH);
	//glEnable(GL_BLEND);

	// 设置光源颜色 , 黑色 
	float blackColor[] = {0.0f, 0.0f, 0.0f, 1.0f};
	float whiteColor[] = {1.0f, 1.0f, 1.0f, 1.0f};

	// 设置环境光 
	glLightfv(GL_LIGHT0, GL_AMBIENT, whiteColor);

	// 设置漫反射光
	glLightfv(GL_LIGHT0, GL_DIFFUSE, whiteColor);

	// 设置镜面反射光 
	glLightfv(GL_LIGHT0, GL_SPECULAR, whiteColor);

	// 设置光源位置 , 最后一位设置成 0 代表该光源无限远
	float lightPosition[] = { 0.0f, 1.0f, 0.0f, 0.0f };
	// 设置光源位置 , y 轴无限远位置 
	glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);

	// 设置材质
	float blackMat[] = { 0.0f, 0.0f, 0.0f, 1.0f };
	float greenMat[] = { 0.0f, 1.0f, 0.0f, 1.0f };
	float blueMat[] = { 0.0f, 0.0f, 1.0f, 1.0f };
	float whiteMat[] = { 1.0f, 1.0f, 1.0f, 1.0f };

	// 设置环境光反射材质 , 这里设置为黑色 , 不反射光 , 全都吸收
	glMaterialfv(GL_FRONT, GL_AMBIENT, greenMat);

	// 设置漫反射光反射材质 , 这里设置为黑色 , 不反射光 , 全都吸收
	glMaterialfv(GL_FRONT, GL_DIFFUSE, blueMat);

	// 设置镜面反射光反射材质 , 这里设置为黑色 , 不反射光 , 全都吸收
	glMaterialfv(GL_FRONT, GL_SPECULAR, blueMat);


	// 启用光照
	glEnable(GL_LIGHTING);

	// 设置光源 , 0 号光源使用的是默认材质
	glEnable(GL_LIGHT0);

    // 主消息循环:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }

		// 渲染场景

		// 设置单位矩阵
		glLoadIdentity();

		// 矩阵压栈 
		//glPushMatrix();

		// 矩阵缩放
		// 缩放的是下面设置的点的坐标
		// 每个参数都影响 x , y , z 分量
		//glScalef(2.0f, 2.0f, 1.0f);

		// 矩阵旋转
		// glRotatef (GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
		// 第 1 个参数是旋转角度 , 后面三个参数的值代表是否绕该轴旋转 , 
		// 如果对应值设置为 1 , 则绕该轴旋转 
		// 这里设置的是绕 z 轴旋转 30 度
		//glRotatef(90.0f, 0.0f, 0.0f, 1.0f);

		// 平移变换 
		// 设置 xyz 三个方向平移的值
		//glTranslatef(0.0f, -2.0f, 0.0f);

		// 清除缓冲区 , 
		// 使用之前设置的 glClearColor(1.0, 0.0, 0.0, 1.0) 擦除颜色缓冲区
		// 红色背景
		glClear(GL_COLOR_BUFFER_BIT);

        // 设置当前的绘制颜色 , 4 个 unsigned byte 
        // 每个颜色的分量占一个字节
        // 参数数据是 R 红色 G 绿色 B 蓝色 A 透明度
        // 下面设置的含义是白色, 绘制点的时候, 每次都使用白色绘制
        glColor4ub(255, 255, 255, 255);

		// 设置当前点的大小
		glPointSize(5.0f);

		// 设置线的宽度 
		glLineWidth(5.0f);

        //glBegin(GL_POINTS);	// 绘制点
        //glBegin(GL_LINES);	// 绘制线
		//glBegin(GL_LINE_STRIP);// 绘制前后连接的点组成的线
        //glBegin(GL_LINE_LOOP); // 绘制前后连接的点组成的线 , 并且收尾相连
        //glBegin(GL_TRIANGLES); // 绘制多个三角形
        //glBegin(GL_TRIANGLE_STRIP); // 绘制 GL_TRIANGLE_STRIP 三角形
		//glBegin(GL_TRIANGLE_FAN);	// 绘制三角形扇

		// 绘制三角形
        glBegin(GL_TRIANGLES);

		// 设置法线
		glNormal3f(0.0f, -1.0f, 0.0f);

		// 1. 设置白色 , glVertex3f (GLfloat x, GLfloat y, GLfloat z)
		glColor4ub(255, 255, 255, 255);
        glVertex3f(-1.0f, -0.5f, -2.0f);

		// 设置法线
		glNormal3f(0.0f, 1.0f, 0.0f);

		// 2. 设置绿色 
		glColor4ub(0, 255, 0, 255);
		glVertex3f(1.0f, -0.5f, -2.0f);

		// 设置法线
		glNormal3f(0.0f, 1.0f, 0.0f);

		// 3. 设置蓝色
		glColor4ub(0, 0, 255, 255);
		glVertex3f(0.0f, -0.5f, -10.0f);

        // 绘制三角形结束
        glEnd();

		// 矩阵出栈 
		//glPopMatrix();

		// 将后缓冲区绘制到前台
		SwapBuffers(dc);

    }

    return (int) msg.wParam;
}



//
//  函数: MyRegisterClass()
//
//  目标: 注册窗口类。
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
    // 注册窗口的结构体
    WNDCLASSEXW wcex;

    // 设置结构体的大小
    wcex.cbSize = sizeof(WNDCLASSEX);
    // 窗口风格 , CS 是 Class Style 缩写 , VREDRAW 垂直重绘 , HREDRAW 水平重绘
    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    // 消息响应函数 , 鼠标点击窗口 , 或打字字后的回调函数
    wcex.lpfnWndProc    = WndProc;
    // 不需要额外的空间
    wcex.cbClsExtra     = 0;
    // 不需要额外的空间
    wcex.cbWndExtra     = 0;
    // 设置程序的实例, 通过桌面程序入口函数传入
    wcex.hInstance      = hInstance;
    // 生成的程序在文件夹中的样式 , 可执行程序的图标
    wcex.hIcon          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_OPENGL));
    // 设置鼠标光标样式
    wcex.hCursor        = LoadCursor(nullptr, IDC_ARROW);
    // 设置背景
    //wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    // 菜单
    wcex.lpszMenuName   = MAKEINTRESOURCEW(IDC_OPENGL);
    // 窗口的唯一标识符
    wcex.lpszClassName  = szWindowClass;
    // 设置窗口运行后显示在右上角的图标
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    // 设置完上述参数后 , 最后调用该方法注册窗口
    return RegisterClassExW(&wcex);
}

//
//   函数: InitInstance(HINSTANCE, int)
//
//   目标: 保存实例句柄并创建主窗口
//
//   注释:
//
//        在此函数中，我们在全局变量中保存实例句柄并
//        创建和显示主程序窗口。
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   hInst = hInstance; // 将实例句柄存储在全局变量中

   // 创建窗口的核心逻辑
   HWND hWnd = CreateWindowW(
       szWindowClass,       // 窗口主类
       szTitle,             // 窗口标题名称
       WS_OVERLAPPEDWINDOW, // 窗口风格
       100 ,                // x 坐标
       100 ,                // y 坐标
       800,                 // 宽度
       600,                 // 高度
       nullptr,             // 父窗口 
       nullptr,             // 菜单
       hInstance,           // 程序实体
       nullptr);

   // 如果创建失败 , 直接退出
   if (!hWnd)
   {
      return FALSE;
   }


   // 创建 OpenGL 的渲染上下文

   // 获取窗口设备 
   dc = GetDC(hWnd);

   // 颜色描述符, 像素格式描述符 , 选取 OpenGL 渲染的像素格式
   PIXELFORMATDESCRIPTOR pfd;

   // 将 PIXELFORMATDESCRIPTOR 结构体清空
   memset(&pfd, 0, sizeof(PIXELFORMATDESCRIPTOR));

   // 填充结构体

   // 设置版本号
   pfd.nVersion = 1;
   // 结构体大小
   pfd.nSize = sizeof(PIXELFORMATDESCRIPTOR);
   // 颜色缓冲区 32 位
   pfd.cColorBits = 32;
   // 深度缓冲区 24 位
   pfd.cDepthBits = 24;
   pfd.cStencilBits = 8;
   // 颜色格式
   pfd.iPixelType = PFD_TYPE_RGBA;
   pfd.iLayerType = PFD_MAIN_PLANE;

   // 分别设置 绘制到桌面窗口 , OpenGL 支持 , 双缓冲 标志位 
   // 双缓冲区可以让画面更流畅 
   pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;

   // 选择像素格式 , 如果返回 -1 , 说明选择像素格式失败 , 一般情况下该选择是成功的 
   int pixelFormat = ChoosePixelFormat(dc, &pfd);

   // 设置像素格式
   SetPixelFormat(dc, pixelFormat, &pfd);

   // 创建 OpenGL 上下文对象 , 注意该操作必须在设置完像素格式后进行操作
   HGLRC rc = wglCreateContext(dc);

   // 设置 OpenGL 上下文对象 , 将 rc 和 dc 作为当前的渲染设备
   wglMakeCurrent(dc, rc); 

   // 设置清除缓冲区背景颜色
   // glClearColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
   // 对应的参数是 红色 , 绿色 , 蓝色 , 透明度
   // 这里设置的是红色
   glClearColor(1.0, 0.0, 0.0, 1.0);


   // 矩阵环境初始化 , 主要是投影矩阵和模型矩阵 

   // ( 选中投影矩阵 ) 设置矩阵模式 , 告知 GPU 当前要操作的矩阵是投影矩阵
   glMatrixMode(GL_PROJECTION);
   // ( 给投影矩阵设置值 ) 向投影矩阵设置参数
   // 参数一 : 50.0f 是摄像机的视口角度
   // 参数二 : 800.0f / 600.0f 是窗口的宽高比
   // 参数三 : 0.1f , 可视的最近的距离
   // 参数四 : 1000.0f , 可视的最远距离
   gluPerspective(50.0f, 800.0f / 600.0f, 0.1f, 1000.0f);

   // 上述设置好了摄像机的参数 , 具体的摄像机能看什么东西 , 就需要模型视图矩阵设置

   // ( 选中模型矩阵 )
   glMatrixMode(GL_MODELVIEW);
   // ( 设置模型矩阵值 ) , 这里设置的是单位矩阵
   glLoadIdentity();


   // 显示窗口
   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

//
//  函数: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  目标: 处理主窗口的消息。
//
//  WM_COMMAND  - 处理应用程序菜单
//  WM_PAINT    - 绘制主窗口
//  WM_DESTROY  - 发送退出消息并返回
//
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_COMMAND:
        {
            int wmId = LOWORD(wParam);
            // 分析菜单选择:
            switch (wmId)
            {
            case IDM_ABOUT:
                DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
                break;
            case IDM_EXIT:
                DestroyWindow(hWnd);
                break;
            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;
    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hWnd, &ps);
            // TODO: 在此处添加使用 hdc 的任何绘图代码...
            EndPaint(hWnd, &ps);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// “关于”框的消息处理程序。
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}
