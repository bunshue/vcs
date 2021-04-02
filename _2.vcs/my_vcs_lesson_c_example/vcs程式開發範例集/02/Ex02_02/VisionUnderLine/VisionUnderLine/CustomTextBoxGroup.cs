using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;//引用Runtime.InteropServices命名空间
using System.Drawing;//引用Drawing命名空间

namespace VisionUnderLine
{
    class CustomTextBoxGroup:TextBox
    {
        #region 本程序中的变量声明
        public const int WM_PAINT = 0x000F;//该变量标识绘制TextBox控件
        public const int WM_CTLCOLOREDIT = 0x0133;//该变量表示开始编辑TextBox控件的颜色
        #endregion

        #region 本程序中用到的API函数声明
        [DllImport("user32.dll")]
        ///说明：获取整个窗口的设备场景
        ///返回值：执行成功则为窗口设备场景，失败则为0
        ///参数说明：将获取其设备场景的窗口
        ///PS：用完后一定要用ReleaseDC函数释放场景
        public static extern IntPtr GetWindowDC(IntPtr hWnd);
        [DllImport("user32.dll")]
       ///说明：释放由调用GetDC或GetWindowDC函数获取的指定设备场景，它对类或私有设备场景无效
       ///返回值：执行成功返回1，否则，返回0
       ///参数说明：
       ///hWnd：要释放的设备场景相关的窗口句柄
       ///hDC：要释放的设备场景句柄
        public static extern int ReleaseDC(IntPtr hWnd,IntPtr hDC);
        #endregion

        public CustomTextBoxGroup()
        {
            this.Width = 180;//设置控件的宽度
            this.Height = 100;//设置控件的高度
            this.BorderStyle = BorderStyle.None;//设置控件为无边框状态
            this.Top = 60;//设置控件上边缘与其容器工作区上边缘之间的距离
            this.Left = 100;//设置控件左边缘与其容器工作区左边缘之间的距离
        }

        protected override void WndProc(ref Message m)
        {
            base.WndProc(ref m);//处理消息
            switch(m.Msg)//截获有关TextBox控件的绘制信息
            {
                case WM_CTLCOLOREDIT://当开始编辑TextBox控件的颜色时
                    goto case WM_PAINT;//跳转到TextBox控件的绘制
                case WM_PAINT://当开始绘制TextBox控件时
                    IntPtr hDC = GetWindowDC(this.Handle);//获取当前窗口的设备场景
                    if(hDC.ToInt32() != 0)//当此场景存在时
                    {
                        using(Graphics g = Graphics.FromHdc(hDC))//声明一个GDI+绘图图面类对象g所占用的资源
                        {
                            DrawBottomLines(g);//绘制TextBox控件的底端横线
                            g.Dispose();//释放GDI+绘图图面类对象g所占用的资源
                        }
                    }
                    m.Result = IntPtr.Zero;//指定在当前条件下的返回值
                    ReleaseDC(m.HWnd,hDC);//释放指定设备的场景
                    break;
            }
        }

        public void DrawBottomLines(Graphics g)
        {
            Pen p = new Pen(this.BackColor,2);//定义一个用于绘制直线和曲线的对象并设定它的颜色和宽度
            g.DrawRectangle(p,1,1,this.Width - 2,this.Height - 2);//绘制由坐标对、宽度和高度指定的矩形
            p = new Pen(Color.FromArgb(0,0,0),1);//定义一个用于绘制直线和曲线的对象并设定它的颜色和宽度
            g.DrawLine(p,0,this.Height - 1,this.Width,this.Height - 1);//绘制TextBox的底端横线
            p.Dispose();//释放画笔p所占用的资源
        }
    }
}
