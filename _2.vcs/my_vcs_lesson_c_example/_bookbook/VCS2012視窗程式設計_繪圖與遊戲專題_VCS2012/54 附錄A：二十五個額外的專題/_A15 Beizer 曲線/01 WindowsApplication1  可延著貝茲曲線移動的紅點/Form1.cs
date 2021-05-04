// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        List<MovingPoint> mpList = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中
        Pen penRed = new Pen(Color.Red, 3);
        float t = 0;
        float td = 0.01f;

        public Form1()
        {
            InitializeComponent();

            MovingPoint mp; 
            mp = new MovingPoint(new Point(100, 200));
            mpList.Add(mp); // 第一個控制點

            mp = new MovingPoint(new Point(200, 100));
            mpList.Add(mp); // 第二個控制點

            mp = new MovingPoint(new Point(300, 300));
            mpList.Add(mp); // 第三個控制點

            mp = new MovingPoint(new Point(400, 200));
            mpList.Add(mp); // 第四個控制點
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath();  // 圖形路徑物件

            gp.AddBezier(mpList[0].p, mpList[1].p, mpList[2].p, mpList[3].p); // 加入貝茲曲線
            gp.StartFigure(); // 不封閉目前的貝茲曲線 開始新形狀。

            // 加入兩條切線
            gp.AddLine(mpList[0].p, mpList[1].p);
            gp.CloseFigure(); // 封閉目前的圖形

            gp.AddLine(mpList[2].p, mpList[3].p);
            gp.CloseFigure(); // 封閉目前的圖形

            // 加入 左邊 圓形端點
            gp.AddEllipse(mpList[0].p.X - 10, mpList[0].p.Y - 10, 20, 20);
            Rectangle rect1, rect2;
            rect1 = new Rectangle(mpList[1].p.X - 10, mpList[1].p.Y - 10, 20, 20);
            rect2 = new Rectangle(mpList[2].p.X - 10, mpList[2].p.Y - 10, 20, 20);
            gp.AddRectangle(rect1); // 加入 方形控制點
            gp.AddRectangle(rect2); // 加入 方形控制點
            gp.AddEllipse(mpList[3].p.X - 10, mpList[3].p.Y - 10, 20, 20); //加入右邊圓形端點

            PointF pt = BezierFormula(t);
            e.Graphics.FillEllipse(Brushes.Red, pt.X-5, pt.Y-5, 10, 10);

            e.Graphics.DrawPath(Pens.Black, gp);  // 繪出GraphicsPath物件
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            // 端點或控制點 是否被點選到
            for (int i = 0; i <= mpList.Count - 1; i++)
            {
                if (mpList[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected = i;
                    dragging = true;
                    break;
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging) // 移動端點或控制點
            {
                mpList[mp_Selected].Move(e.X, e.Y);
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            // 解除 端點或控制點 的點選狀況
            mp_Selected = -1;
            dragging = false;
        }

        PointF BezierFormula(float t)
        {
            PointF ret = new PointF();

            ret.X = (1 - t) * (1 - t) * (1 - t) * mpList[0].p.X +
                    3 * t * (t - 1) * (t - 1) * mpList[1].p.X +
                    3 * t * t * (1 - t) * mpList[2].p.X +
                    t * t * t * mpList[3].p.X;

            ret.Y = (1 - t) * (1 - t) * (1 - t) * mpList[0].p.Y +
                    3 * t * (t - 1) * (t - 1) * mpList[1].p.Y +
                    3 * t * t * (1 - t) * mpList[2].p.Y +
                    t * t * t * mpList[3].p.Y;

            return ret;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            t = t + td;
            if (t > 1.0f)
            {
                t = 1;
                td = -td;
            }
            else if (t < 0)
            {
                t = 0;
                td = -td;
            }

            this.Invalidate();
        }
    }
}