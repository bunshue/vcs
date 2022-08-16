using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ClockF
{
    public partial class Form1 : Form
    {
        const int s_pinlen = 100;//秒針長度
        const int m_pinlen = 75; //分針長度
        const int h_pinlen = 75; //時針長度
        PointF center = new PointF(s_pinlen + 3, s_pinlen + 3);//中心點位置
        SolidBrush sb = new SolidBrush(Color.Black);//時鐘圓心的刷子

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(300, 300);
            timer1_Tick(sender, e);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int h = DateTime.Now.Hour;
            int m = DateTime.Now.Minute;
            int s = DateTime.Now.Second;
            myClock(h, m, s);//調用畫時鐘表的方法
            this.Text = "當前時間:" + DateTime.Now.ToLongTimeString();
        }

        //　　方法AngleToPos是根據角度和百分比計算出一個點的坐標函數,代碼如下:
        PointF AngleToPos(int angle, float percent)
        {
            PointF pos = new PointF();
            double radian = angle * Math.PI / 180;
            pos.Y = center.Y - s_pinlen * percent * (float)Math.Sin(radian);
            pos.X = center.X + s_pinlen * percent * (float)Math.Cos(radian);
            return pos;
        }

        void myClock(int h, int m, int s)
        {
            Pen pDisk = new Pen(Color.Orange, 3);//時鐘背景的筆
            Pen pScale = new Pen(Color.Coral);//刻度的筆
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen myPen = new Pen(Color.Black, 2);
            Point CPoint = new Point(s_pinlen, s_pinlen);
            Point SPoint = new Point((int)(CPoint.X + (Math.Sin(6 * s * Math.PI / 180)) * s_pinlen), (int)(CPoint.Y - (Math.Cos(6 * s * Math.PI / 180)) * s_pinlen));
            Point MPoint = new Point((int)(CPoint.X + (Math.Sin(6 * m * Math.PI / 180)) * m_pinlen), (int)(CPoint.Y - (Math.Cos(6 * m * Math.PI / 180)) * m_pinlen));

            Point HPoint = new Point((int)(CPoint.X + (Math.Sin(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen), (int)(CPoint.Y - (Math.Cos(((30 * h) + (m / 2)) * Math.PI / 180)) * h_pinlen));
            g.FillEllipse(sb, center.X - 8, center.Y - 7, 14, 14);
            g.DrawLine(myPen, CPoint, SPoint);
            myPen = new Pen(Color.Blue, 4);
            g.DrawLine(myPen, CPoint, MPoint);
            myPen = new Pen(Color.Green, 6);
            g.DrawLine(myPen, CPoint, HPoint);
            g.DrawEllipse(pDisk, 1, 1, s_pinlen * 2, s_pinlen * 2);//畫刻度
            for (int i = 0; i < 360; i += 6)
            {
                Pen tempPen = (i % 30 == 0) ? pDisk : pScale;
                PointF qidian = AngleToPos(i, 0.87f);
                PointF zhongdian = AngleToPos(i, 1.0f);
                g.DrawLine(tempPen, qidian, zhongdian);
            }
        }
    }
}

