#include "framework.h"
#include "OpenGL.h"

#include "texture.h"
#include "utils.h"

// 導入 OpenGL 的個頭文件 , 必須先導入 windows.h 頭文件之後再導入 opengl 頭文件
#include <gl/GL.h>
#include <gl/GLU.h>

// 鏈接 OpenGL 庫
#pragma comment(lib, "opengl32.lib")
#pragma comment(lib, "glu32.lib")

#define MAX_LOADSTRING 100

// 全局變量:
HINSTANCE hInst;                                // 當前實例
WCHAR szTitle[MAX_LOADSTRING];                  // 標題欄文本
WCHAR szWindowClass[MAX_LOADSTRING];            // 主窗口類名 

// 此代碼模塊中包含的函數的前向聲明:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);

// 窗口設備
// 提取到全局變量中 
HDC dc = NULL;

int APIENTRY wWinMain(_In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance, _In_ LPWSTR lpCmdLine, _In_ int nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: 在此處放置代碼。

    // 初始化全局字符串
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_OPENGL, szWindowClass, MAX_LOADSTRING);

    // 注冊窗口
    MyRegisterClass(hInstance);

    // 執行應用程序初始化:
    // 創建窗口
    if (!InitInstance(hInstance, nCmdShow))
    {
        return FALSE;
    }

    // 下面的邏輯是一個死循環 , 避免讓窗口退出 

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_OPENGL));

    MSG msg;
    // 讀取文件內容
    char* str = (char*)LoadFileContent("C:\\_git\\vcs\\_6.opengl\\OpenGL - master\\test.txt");
    printf("%s\n", str);

    // 只顯示正面 , 不顯示背面
    //glEnable(GL_CULL_FACE);

    // 設置順時針方向 CW : Clock Wind 順時針方向
    // 默認是 GL_CCW : Counter Clock Wind 逆時針方向 
    //glFrontFace(GL_CW);

    // 默認模式, 填充模式 , 如果不設置就默認為填充模式
    //glPolygonMode(GL_FRONT, GL_FILL);

    // 設置線框模式 
    // 設置了該模式後 , 之後的所有圖形都會變成線
    //glPolygonMode(GL_FRONT, GL_LINE);

    // 設置點模式 
    // 設置了該模式後 , 之後的所有圖形都會變成點
    //glPolygonMode(GL_FRONT, GL_POINT);

    // 將方形的點變為圓點
    //glEnable(GL_POINT_SMOOTH);
    //glEnable(GL_BLEND);

    // 設置光源顏色 , 黑色 
    float blackColor[] = { 0.0f, 0.0f, 0.0f, 1.0f };
    float whiteColor[] = { 1.0f, 1.0f, 1.0f, 1.0f };

    // 設置環境光 
    glLightfv(GL_LIGHT0, GL_AMBIENT, whiteColor);

    // 設置漫反射光
    glLightfv(GL_LIGHT0, GL_DIFFUSE, whiteColor);

    // 設置鏡面反射光 
    glLightfv(GL_LIGHT0, GL_SPECULAR, whiteColor);

    // 設置光源位置 , 最後一位設置成 0 代表該光源無限遠
    float lightPosition[] = { 0.0f, 1.0f, 0.0f, 0.0f };
    // 設置光源位置 , y 軸無限遠位置 
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);

    // 設置材質
    float blackMat[] = { 0.0f, 0.0f, 0.0f, 1.0f };
    float greenMat[] = { 0.0f, 1.0f, 0.0f, 1.0f };
    float blueMat[] = { 0.0f, 0.0f, 1.0f, 1.0f };
    float whiteMat[] = { 1.0f, 1.0f, 1.0f, 1.0f };

    // 設置環境光反射材質 , 這里設置為黑色 , 不反射光 , 全都吸收
    glMaterialfv(GL_FRONT, GL_AMBIENT, greenMat);

    // 設置漫反射光反射材質 , 這里設置為黑色 , 不反射光 , 全都吸收
    glMaterialfv(GL_FRONT, GL_DIFFUSE, blueMat);

    // 設置鏡面反射光反射材質 , 這里設置為黑色 , 不反射光 , 全都吸收
    glMaterialfv(GL_FRONT, GL_SPECULAR, blueMat);

    // 啟用光照
    glEnable(GL_LIGHTING);

    // 設置光源 , 0 號光源使用的是默認材質
    glEnable(GL_LIGHT0);

    // 主消息循環:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }

        // 渲染場景

        glLoadIdentity();   //設置單位矩陣

        // 矩陣壓棧 
        //glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??

        // 矩陣縮放
        // 縮放的是下面設置的點的座標
        // 每個參數都影響 x , y , z 分量
        //glScalef(2.0f, 2.0f, 1.0f);

        // 矩陣旋轉
        // glRotatef (GLfloat angle, GLfloat x, GLfloat y, GLfloat z);
        // 第 1 個參數是旋轉角度 , 後面三個參數的值代表是否繞該軸旋轉 , 
        // 如果對應值設置為 1 , 則繞該軸旋轉 
        // 這里設置的是繞 z 軸旋轉 30 度
        //glRotatef(90.0f, 0.0f, 0.0f, 1.0f);

        // 平移變換 
        // 設置 xyz 三個方向平移的值
        //glTranslatef(0.0f, -2.0f, 0.0f);

        // 清除緩沖區 , 
        // 使用之前設置的 glClearColor(1.0, 0.0, 0.0, 1.0) 擦除顏色緩沖區
        // 紅色背景
        glClear(GL_COLOR_BUFFER_BIT);

        // 設置當前的繪製顏色 , 4 個 unsigned byte 
        // 每個顏色的分量占一個字節
        // 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
        // 下面設置的含義是白色, 繪製點的時候, 每次都使用白色繪製
        glColor4ub(255, 255, 255, 255);

        // 設置當前點的大小
        glPointSize(5.0f);

        glLineWidth(5.0f);	//設定線寬

        //glBegin(GL_POINTS);	//繪製點
        //glBegin(GL_LINES);	//繪製線
        //glBegin(GL_LINE_STRIP);//繪製前後連接的點組成的線
        //glBegin(GL_LINE_LOOP); //繪製前後連接的點組成的線 , 并且收尾相連
        //glBegin(GL_TRIANGLES); //繪製多個三角形
        //glBegin(GL_TRIANGLE_STRIP); //繪製 GL_TRIANGLE_STRIP 三角形
        //glBegin(GL_TRIANGLE_FAN);	//繪製三角形扇

        //繪製三角形
        glBegin(GL_TRIANGLES);

        glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
        glColor4ub(255, 0, 0, 255);     //R
        glVertex3f(-1.0f, -0.9f, -2.0f);    //左下

        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 255, 0, 255);     //G
        glVertex3f(1.0f, -0.9f, -2.0f); //右下

        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 0, 255, 255);     //B
        glVertex3f(0.0f, 2.5f, -10.0f); //上

        glEnd();

        // 矩陣出棧 
        //glPopMatrix();

        SwapBuffers(dc);    // 將後緩沖區繪製到前臺
    }
    return (int)msg.wParam;
}

//
//  函數: MyRegisterClass()
//  目標: 注冊窗口類。
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
    // 注冊窗口的結構體
    WNDCLASSEXW wcex;

    // 設置結構體的大小
    wcex.cbSize = sizeof(WNDCLASSEX);
    // 窗口風格 , CS 是 Class Style 縮寫 , VREDRAW 垂直重繪 , HREDRAW 水平重繪
    wcex.style = CS_HREDRAW | CS_VREDRAW;
    // 消息響應函數 , 鼠標點擊窗口 , 或打字字後的回調函數
    wcex.lpfnWndProc = WndProc;
    // 不需要額外的空間
    wcex.cbClsExtra = 0;
    // 不需要額外的空間
    wcex.cbWndExtra = 0;
    // 設置程序的實例, 通過桌面程序入口函數傳入
    wcex.hInstance = hInstance;
    // 生成的程序在文件夾中的樣式 , 可執行程序的圖標
    wcex.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_OPENGL));
    // 設置鼠標光標樣式
    wcex.hCursor = LoadCursor(nullptr, IDC_ARROW);
    // 設置背景
    //wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    // 菜單
    wcex.lpszMenuName = MAKEINTRESOURCEW(IDC_OPENGL);
    // 窗口的唯一標識符
    wcex.lpszClassName = szWindowClass;
    // 設置窗口運行後顯示在右上角的圖標
    wcex.hIconSm = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    // 設置完上述參數後 , 最後調用該方法注冊窗口
    return RegisterClassExW(&wcex);
}

//
//   函數: InitInstance(HINSTANCE, int)
//   目標: 保存實例句柄并創建主窗口
//   注釋:
//        在此函數中，我們在全局變量中保存實例句柄并
//        創建和顯示主程序窗口。
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
    hInst = hInstance; // 將實例句柄存儲在全局變量中

    // 創建窗口的核心邏輯
    HWND hWnd = CreateWindowW(
        szWindowClass,       // 窗口主類
        szTitle,             // 窗口標題名稱
        WS_OVERLAPPEDWINDOW, // 窗口風格
        100,                // x 座標
        100,                // y 座標
        800,                 // 寬度
        600,                 // 高度
        nullptr,             // 父窗口 
        nullptr,             // 菜單
        hInstance,           // 程序實體
        nullptr);

    // 如果創建失敗 , 直接退出
    if (!hWnd)
    {
        return FALSE;
    }

    // 創建 OpenGL 的渲染上下文

    // 獲取窗口設備 
    dc = GetDC(hWnd);

    // 顏色描述符, 像素格式描述符 , 選取 OpenGL 渲染的像素格式
    PIXELFORMATDESCRIPTOR pfd;

    // 將 PIXELFORMATDESCRIPTOR 結構體清空
    memset(&pfd, 0, sizeof(PIXELFORMATDESCRIPTOR));

    // 填充結構體

    // 設置版本號
    pfd.nVersion = 1;
    // 結構體大小
    pfd.nSize = sizeof(PIXELFORMATDESCRIPTOR);
    // 顏色緩沖區 32 位
    pfd.cColorBits = 32;
    // 深度緩沖區 24 位
    pfd.cDepthBits = 24;
    pfd.cStencilBits = 8;
    // 顏色格式
    pfd.iPixelType = PFD_TYPE_RGBA;
    pfd.iLayerType = PFD_MAIN_PLANE;

    // 分別設置 繪製到桌面窗口 , OpenGL 支持 , 雙緩沖 標志位 
    // 雙緩沖區可以讓畫面更流暢 
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;

    // 選擇像素格式 , 如果返回 -1 , 說明選擇像素格式失敗 , 一般情況下該選擇是成功的 
    int pixelFormat = ChoosePixelFormat(dc, &pfd);

    // 設置像素格式
    SetPixelFormat(dc, pixelFormat, &pfd);

    // 創建 OpenGL 上下文對象 , 注意該操作必須在設置完像素格式後進行操作
    HGLRC rc = wglCreateContext(dc);

    // 設置 OpenGL 上下文對象 , 將 rc 和 dc 作為當前的渲染設備
    wglMakeCurrent(dc, rc);

    // 設置清除緩沖區背景顏色
    // glClearColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
    // 對應的參數是 紅色 , 綠色 , 藍色 , 透明度
    // 這里設置的是紅色
    glClearColor(0.0, 0.0, 0.0, 1.0);   //設置背景顏色 黑色

    // 矩陣環境初始化 , 主要是投影矩陣和模型矩陣 

    // ( 選中投影矩陣 ) 設置矩陣模式 , 告知 GPU 當前要操作的矩陣是投影矩陣
    glMatrixMode(GL_PROJECTION);
    // ( 給投影矩陣設置值 ) 向投影矩陣設置參數
    // 參數一 : 50.0f 是攝像機的視口角度
    // 參數二 : 800.0f / 600.0f 是窗口的寬高比
    // 參數三 : 0.1f , 可視的最近的距離
    // 參數四 : 1000.0f , 可視的最遠距離
    gluPerspective(50.0f, 800.0f / 600.0f, 0.1f, 1000.0f);

    // 上述設置好了攝像機的參數 , 具體的攝像機能看什么東西 , 就需要模型視圖矩陣設置

    // ( 選中模型矩陣 )
    glMatrixMode(GL_MODELVIEW);
    // ( 設置模型矩陣值 ) , 這里設置的是單位矩陣
    glLoadIdentity();   //設置單位矩陣

    // 顯示窗口
    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);

    return TRUE;
}

//
//  函數: WndProc(HWND, UINT, WPARAM, LPARAM)
//  目標: 處理主窗口的消息。
//
//  WM_COMMAND  - 處理應用程序菜單
//  WM_PAINT    - 繪製主窗口
//  WM_DESTROY  - 發送退出消息并返回
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_COMMAND:
    {
        int wmId = LOWORD(wParam);
        // 分析菜單選擇:
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
        // TODO: 在此處添加使用 hdc 的任何繪圖代碼...
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

// “關於”框的消息處理程序。
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


