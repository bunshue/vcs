using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        ClassGrid grid = new ClassGrid();
        int D = 30;  // 格子單位寬
        PointF p1 = new PointF(-10, 10); // 兩點成一直線
        PointF p2 = new PointF(10, -10);
        float A, B, C; // Ax + By + C = 0 直線方程式

        PointF p3 = new PointF(10, 10); // 線外一點
        PointF p4 = new PointF(0, 0);   // 另一側的相對點
        PointF p5 = new PointF(0, 0);   // 中間點 

        Pen myPen = new Pen(Color.Red, 3);

        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Font fn = new Font("Times New Roman", 20);

        public Form1()
        {
            InitializeComponent();
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
            myPen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;

            // 加入三個可移動點
            ClassMovingPoint mp;
            mp = new ClassMovingPoint(p1, this.ClientSize.Width, this.ClientSize.Height, D);
            mpList.Add(mp);

            mp = new ClassMovingPoint(p2, this.ClientSize.Width, this.ClientSize.Height, D);
            mpList.Add(mp);

            mp = new ClassMovingPoint(p3, this.ClientSize.Width, this.ClientSize.Height, D);
            mpList.Add(mp);
        }

        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            {
                D = D + 1;
                if (D > 40) D = 40;
            }
            else if (e.Delta < 0)
            {
                D = D - 1;
                if (D < 10) D = 10;
            }

            foreach (ClassMovingPoint mp in mpList) // 更新 可移動點 物件 的 格子單位寬
                mp.D = D;

            this.Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            grid.Draw(e.Graphics, this.ClientSize.Width, this.ClientSize.Height, D);

            //e.Graphics.DrawLine(Pens.BlueViolet, GetPoint(p1), GetPoint(p2));
            GetABC(p1, p2);
            label9.Text = "<< 直線 >> " + A.ToString() + " X + " + B.ToString() + " Y + " + C.ToString() + " = 0, 斜率： " + Convert.ToString(-A / B);

            // 斜率是 - A / B 或是 (p2.Y - p1.Y) / (p2.X - p1.X)
            //float f1 = -A / B;
            //float f2 = (p2.Y - p1.Y) / (p2.X - p1.X);
            //float f3 = (p1.Y - p2.Y) / (p1.X - p2.X);

            if (B == 0 || Math.Abs(-A / B) > 1.0)
            {
                // 和上下邊界 水平線相切
                e.Graphics.DrawLine(Pens.Blue, GetPoint(GetIntersect(A, B, C, 0, 1, (+this.ClientSize.Height / (2 * D)) + 1)),
                                                     GetPoint(GetIntersect(A, B, C, 0, 1, (-this.ClientSize.Height / (2 * D)) - 1)));
            }
            else
            {
                // 和左右邊界 垂直線相切
                e.Graphics.DrawLine(Pens.Blue, GetPoint(GetIntersect(A, B, C, 1, 0, (+this.ClientSize.Width / (2 * D)) + 1)),
                                                     GetPoint(GetIntersect(A, B, C, 1, 0, (-this.ClientSize.Width / (2 * D)) - 1)));
            }

            // 垂直線的斜率可從 -A/B 得到為 B/A 
            // (p3.Y - y) / (p3.X - x) = B / A 
            // A*(p3.Y - y) = B * (p3.X - x)
            // Bx - Ay + (A*p3.Y - B*p3.X) = 0
            // 假設 對稱點 p4 為 (x y)  則中間點 p5 為 (p3.X + x) / 2, (p3.Y + y) / 2 會經過 Ax + By + C = 0
            // A * ((p3.X + x) / 2) + B * ((p3.Y + y) / 2) + C = 0
            // A * p3.X + Ax + B * p3.Y + By + 2C = 0
            // Ax + By + (A*p3.X+B*p3.Y+2*C) = 0;
            p4 = GetIntersect(B, -A, A * p3.Y - B * p3.X, A, B, A * p3.X + B * p3.Y + 2 * C);
            e.Graphics.DrawLine(myPen, GetPoint(p3), GetPoint(p4));
            label11.Text = "(" + p4.X.ToString() + ", " + p4.Y.ToString() + ")";

            p5.X = (p3.X + p4.X) / 2;
            p5.Y = (p3.Y + p4.Y) / 2;
            label8.Text = "(" + p5.X.ToString() + ", " + p5.Y.ToString() + ")";
            label13.Text = (Math.Sqrt((p5.X - p3.X) * (p5.X - p3.X) + (p5.Y - p3.Y) * (p5.Y - p3.Y))).ToString();

            e.Graphics.FillEllipse(Brushes.Blue, GetRect(p1));
            e.Graphics.FillEllipse(Brushes.RoyalBlue, GetRect(p2));

            e.Graphics.FillEllipse(Brushes.Red, GetRect(p3));
            e.Graphics.FillEllipse(Brushes.Yellow, GetRect(p4));
            e.Graphics.FillEllipse(Brushes.Pink, GetRect(p5));

            e.Graphics.DrawEllipse(Pens.Black, GetRect(p1)); // 可點選移動的點 有外框線
            e.Graphics.DrawEllipse(Pens.Black, GetRect(p2));
            e.Graphics.DrawEllipse(Pens.Black, GetRect(p3));

            e.Graphics.DrawString("p1", fn, Brushes.Black, GetPoint(p1), StringFormat.GenericTypographic);
            e.Graphics.DrawString("p2", fn, Brushes.Black, GetPoint(p2), StringFormat.GenericTypographic);
            e.Graphics.DrawString("p3", fn, Brushes.Black, GetPoint(p3), StringFormat.GenericTypographic);
        }

        // 找到 兩條直線的交叉點 
        // Ax + By + C = 0 和
        // ax + by + c = 0 
        PointF GetIntersect(float A, float B, float C, float a, float b, float c)
        {
            PointF p = new Point(0, 0);
            if ((A == 0 && B == 0) || (a == 0 && b == 0))
            {
                // 其中一條不是 直線
            }
            else if (B == 0 && b == 0)  // 兩條都是 鉛錘線
            {
                // 無交叉點
            }
            else if (A == 0 && a == 0)  // 兩條都是 水平線
            {
                // 無交叉點
            }
            else if (B != 0 && b != 0 && -(A / B) == -(a / b))  // 兩條斜率一樣 是平行線
            {
                // 無交叉點
            }
            else if (B == 0 && b != 0)  // 第一條是 鉛錘線
            {
                p.X = -C / A;
                p.Y = -(a * p.X + c) / b;
            }
            else if (B != 0 && b == 0) // 第二條是 鉛錘線
            {
                p.X = -c / a;
                p.Y = -(A * p.X + C) / B;
            }
            else if (A == 0 && a != 0) // 第一條是 水平線
            {
                p.Y = -C / B;
                p.X = -(b * p.Y + c) / a;
            }
            else if (A != 0 && a == 0) // 第二條是 水平線
            {
                p.Y = -c / b;
                p.X = -(B * p.Y + C) / A;
            }
            else
            {
                p.Y = -(a * C - A * c) / (a * B - A * b);
                p.X = -(B * p.Y + C) / A;
            }

            return p;
        }

        // 由 p1 和 p2 兩點 找到 直線方程式  Ax + By + C = 0
        // Ax + By + C = 0 和
        void GetABC(PointF p1, PointF p2)
        {
            // (X - p2.X)(p1.Y- p2.Y) = (Y-p2.Y)(p1.X-p2.X)

            A = p1.Y - p2.Y;
            B = p2.X - p1.X;
            C = p2.Y * (p1.X - p2.X) - p2.X * (p1.Y - p2.Y);
        }

        // 由 點 算出 視窗座標 
        Point GetPoint(PointF p)
        {
            Point point = new Point();
            point.X = (int)(this.ClientSize.Width / 2 + p.X * D);
            point.Y = (int)(this.ClientSize.Height / 2 - p.Y * D);

            return point;
        }

        // 由 點 算出 矩形視窗座標 
        Rectangle GetRect(PointF p)
        {
            Rectangle rect = new Rectangle();
            rect.X = (int)(this.ClientSize.Width / 2 + p.X * D - D / 2);
            rect.Y = (int)(this.ClientSize.Height / 2 - p.Y * D - D / 2);
            rect.Width = D;
            rect.Height = D;
            return rect;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            foreach (ClassMovingPoint mp in mpList) // 更新 可移動點 物件 的 視窗寬高
            {
                mp.W = this.ClientSize.Width;
                mp.H = this.ClientSize.Height;
            }
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            p1 = new PointF(Convert.ToSingle(textBox1.Text), Convert.ToSingle(textBox2.Text));
            p2 = new PointF(Convert.ToSingle(textBox3.Text), Convert.ToSingle(textBox4.Text));
            p3 = new PointF(Convert.ToSingle(textBox5.Text), Convert.ToSingle(textBox6.Text));

            mpList[0].p = p1;
            mpList[1].p = p2;
            mpList[2].p = p3;

            this.Invalidate();
        }

        // 檢查是哪一個點被 選到
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
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

        // 更新 被選到的點 的 格子座標
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                mpList[mp_Selected].Move(e.X, e.Y);
                if (mp_Selected == 0)
                {
                    p1 = mpList[mp_Selected].p;
                    textBox1.Text = p1.X.ToString();
                    textBox2.Text = p1.Y.ToString();
                }
                else if (mp_Selected == 1)
                {
                    p2 = mpList[mp_Selected].p;
                    textBox3.Text = p2.X.ToString();
                    textBox4.Text = p2.Y.ToString();
                }
                else if (mp_Selected == 2)
                {
                    p3 = mpList[mp_Selected].p;
                    textBox5.Text = p3.X.ToString();
                    textBox6.Text = p3.Y.ToString();
                }
                this.Invalidate();
            }
        }

        // 解除 被選到的點
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            mp_Selected = -1;
            dragging = false;
        }
    }
}