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
        PointF p1 = new PointF(0, 0); // 頂點
        PointF p2 = new PointF(10, 10); // 拋物線 經過此點
        float A, B, C; // y = A(x * x)+ Bx + C  一元二次函數
        float a, b, c; // y = a(x+b)^2 + c

        Pen myPen = new Pen(Color.Red, 3);

        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Font fn = new Font("Times New Roman", 20);

        public Form1()
        {
            InitializeComponent();

            textBox1.Text = p1.X.ToString();
            textBox2.Text = p1.Y.ToString();

            textBox3.Text = p2.X.ToString();
            textBox4.Text = p2.Y.ToString();

            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
            myPen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;

            // 加入 2 個可移動點
            ClassMovingPoint mp;
            mp = new ClassMovingPoint(p1, this.ClientSize.Width, this.ClientSize.Height, D);
            mpList.Add(mp);

            mp = new ClassMovingPoint(p2, this.ClientSize.Width, this.ClientSize.Height, D);
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

            label9.Text = "Y = " + A.ToString() + " X^2 + " + B.ToString() + " * X + " + C.ToString();

            a = A;
            b = B / (2 * a);
            c = (4 * A * C - B * B) / 4 * A;
            label6.Text = "Y = " + a.ToString() + " (X + " + b.ToString() + ")^2 + " + c.ToString();


            PointF p = new PointF(0, 0); // 頂點
            Rectangle rect = new Rectangle();

            p.X = p1.X;
            while (true)
            {
                if (Math.Abs(A) <= 1.0f)
                    p.X = p.X - 0.1f;
                else
                    p.X = p.X - 0.1f / A;
                p.Y = A * p.X * p.X + B * p.X + C;

                rect = GetRect2(p);
                if (rect.Y < 0 || rect.Y > this.ClientSize.Height ||
                    rect.X < 0 || rect.X > this.ClientSize.Width) break;
                e.Graphics.FillEllipse(Brushes.Black, rect);
            }

            p.X = p1.X;
            while (true)
            {
                if (Math.Abs(A) <= 1.0f)
                    p.X = p.X + 0.1f;
                else
                    p.X = p.X + 0.1f / A;
                p.Y = A * p.X * p.X + B * p.X + C;

                rect = GetRect2(p);
                if (rect.Y < 0 || rect.Y > this.ClientSize.Height ||
                    rect.X < 0 || rect.X > this.ClientSize.Width) break;
                e.Graphics.FillEllipse(Brushes.Black, rect);
            }

            e.Graphics.FillEllipse(Brushes.Blue, GetRect(p1));
            e.Graphics.FillEllipse(Brushes.RoyalBlue, GetRect(p2));

            e.Graphics.DrawEllipse(Pens.Black, GetRect(p1)); // 可點選移動的點 有外框線
            e.Graphics.DrawEllipse(Pens.Black, GetRect(p2));


            e.Graphics.DrawString("p1", fn, Brushes.Black, GetPoint(p1), StringFormat.GenericTypographic);
            e.Graphics.DrawString("p2", fn, Brushes.Black, GetPoint(p2), StringFormat.GenericTypographic);
        }

        // 由 p1 和 p2 兩點 找到 y = A(x * x)+ Bx + C  一元二次函數
        void GetABC(PointF p1, PointF p2)
        {
            A = (p2.Y - p1.Y) / (p2.X * p2.X - 2 * p1.X * p2.X + p1.X * p1.X);
            B = -p1.X * 2 * A;
            C = p1.Y + p1.X * p1.X * A;
        }

        // 由 點 算出 視窗座標 
        Point GetPoint(PointF p)
        {
            Point point = new Point();
            point.X = (int)(this.ClientSize.Width / 2 + p.X * D);
            point.Y = (int)(this.ClientSize.Height / 2 - p.Y * D);

            return point;
        }

        // 由 點 算出 矩形視窗座標 ( p1 p2 控制點 使用)
        Rectangle GetRect(PointF p)
        {
            Rectangle rect = new Rectangle();
            rect.X = (int)(this.ClientSize.Width / 2 + p.X * D - D / 2);
            rect.Y = (int)(this.ClientSize.Height / 2 - p.Y * D - D / 2);
            rect.Width = D;
            rect.Height = D;
            return rect;
        }
        // 由 點 算出 矩形視窗座標 (拋物線的軌跡小點使用)
        Rectangle GetRect2(PointF p)
        {
            Rectangle rect = new Rectangle();
            rect.X = (int)(this.ClientSize.Width / 2 + p.X * D - 1);
            rect.Y = (int)(this.ClientSize.Height / 2 - p.Y * D - 1);
            rect.Width = 2;
            rect.Height = 2;
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
            float x, y;

            try
            {
                x = Convert.ToSingle(textBox1.Text);
            }
            catch
            {
                x = 0;
                textBox1.Text = "0";
            }

            try
            {
                y = Convert.ToSingle(textBox2.Text);
            }
            catch
            {
                y = 0;
                textBox2.Text = "0";
            }
            p1 = new PointF(x, y);

            try
            {
                x = Convert.ToSingle(textBox3.Text);
            }
            catch
            {
                x = 0;
                textBox3.Text = "0";
            }

            try
            {
                y = Convert.ToSingle(textBox4.Text);
            }
            catch
            {
                y = 0;
                textBox4.Text = "0";
            }
            p2 = new PointF(x, y);

            mpList[0].p = p1;
            mpList[1].p = p2;

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

                this.Invalidate();
            }
        }

        // 解除 被選到的點
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            mp_Selected = -1;
            dragging = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            float aa, bb, cc;
            try
            {
                aa = Convert.ToSingle(textBox_a.Text);
            }
            catch
            {
                aa = 0;
                textBox_a.Text = "0";
            }

            try
            {
                bb = Convert.ToSingle(textBox_b.Text);
            }
            catch
            {
                bb = 0;
                textBox_b.Text = "0";
            }

            try
            {
                cc = Convert.ToSingle(textBox_c.Text);
            }
            catch
            {
                cc = 0;
                textBox_c.Text = "0";
            }

            p1.X = -bb;
            p1.Y = cc;

            textBox1.Text = (p1.X).ToString();
            textBox2.Text = textBox_c.Text;

            if (p1.X != 0)
                p2.X = 0;
            else
                p2.X = 1;

            p2.Y = Convert.ToSingle(aa * (p2.X + bb) * (p2.X + bb) + cc);

            textBox3.Text = (p2.X).ToString();
            textBox4.Text = textBox_c.Text;

            mpList[0].p = p1;
            mpList[1].p = p2;

            this.Invalidate();
        }
    }
}