using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考 http://weisico.com/program/2018/0531/350.html

namespace vcs_Clock1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.DoubleBuffered = true;//避免闪烁  方法一
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;      //定义g为该窗体控件的画布　
            // Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁

            //解决闪烁
            //方法二  占用内存
            //SetStyle(ControlStyles.UserPaint, true);
            //SetStyle(ControlStyles.AllPaintingInWmPaint, true); // 禁止擦除背景.
            //SetStyle(ControlStyles.DoubleBuffer, true); // 双缓冲

            //方法三  占用CPU
            //this.SetStyle(ControlStyles.DoubleBuffer | ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint, true);
            //this.UpdateStyles();
            int r = 100;
            // 绘制数字时钟
            int ss = DateTime.Now.Second;
            int mm = DateTime.Now.Minute;
            int hh = DateTime.Now.Hour;
            this.Text = DateTime.Now.ToString("hh:mm:ss");

            //绘制圆形轮廓
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;//使画出的指针更平滑、高质量
            g.FillEllipse(Brushes.White, 50, 50, 200, 200);
            g.DrawEllipse(new Pen(Color.Red, 2), 46, 46, 208, 208);
            g.DrawEllipse(new Pen(Color.DarkGray, 1), 50, 50, 200, 200);
            //绘制数字刻度
            g.ResetTransform();
            g.TranslateTransform(150, 150);  //重新定位坐标
            Font drawFont = new Font("Arial", 12);
            SolidBrush drawBrush = new SolidBrush(Color.Black);
            //e.Graphics.DrawString("1", drawFont, drawBrush, 30, -70);
            //e.Graphics.DrawString("2", drawFont, drawBrush, 60, -50);
            //e.Graphics.DrawString("5", drawFont, drawBrush, 30, 60);
            //e.Graphics.DrawString("4", drawFont, drawBrush, 65, 30);
            e.Graphics.DrawString("6", drawFont, drawBrush, -7, 70);
            e.Graphics.DrawString("12", drawFont, drawBrush, -9, -80);
            e.Graphics.DrawString("3", drawFont, drawBrush, 70, -7);
            e.Graphics.DrawString("9", drawFont, drawBrush, -80, -7);
            //绘制刻度
            for (int z = 0; z < 60; z++)
            {
                g.ResetTransform();
                g.TranslateTransform(150, 150); //更改坐标原点
                g.RotateTransform(z * 6);  //旋转，每一秒旋转6度 
                if (z % 5 == 0)
                    g.DrawLine(new Pen(Color.Black, 3.0f), r - 12, 0, r - 5, 0);//小时刻度             
                else
                    g.DrawLine(new Pen(Color.Black, 1.5f), r - 8, 0, r - 5, 0);//分钟标准刻度
            }
            //绘制秒针
            g.ResetTransform();    //恢复默认状态
            g.TranslateTransform(150, 150);
            g.RotateTransform(ss * 6 + 270);   //以水平线为x轴，从垂直上方开始旋转，每次旋转6度。     
            Pen secPen = new Pen(Color.Red, 1);
            secPen.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //画线，从圆点开始   
            secPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;//画线，结束于箭头
            g.DrawLine(secPen, 0, 0, 65, 0);//65表示线的长度           
            //绘制分针
            g.ResetTransform();
            g.TranslateTransform(150, 150);
            g.RotateTransform(mm * 6 + 270);
            Pen minPen = new Pen(Color.Blue, 2);
            minPen.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor;
            minPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawLine(minPen, 0, 0, 50, 0);
            //绘制时针
            g.ResetTransform();
            g.TranslateTransform(150, 150);
            g.RotateTransform(hh * 30 + mm * 1 / 2 + 270);
            Pen hourPen = new Pen(Color.Black, 3);
            hourPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawLine(hourPen, 0, 0, 35, 0);      

        }
    }
}
