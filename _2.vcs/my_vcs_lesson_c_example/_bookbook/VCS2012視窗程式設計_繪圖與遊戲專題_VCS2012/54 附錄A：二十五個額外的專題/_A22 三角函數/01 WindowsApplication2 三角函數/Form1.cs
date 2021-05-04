// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        ClassGridM grid = new ClassGridM();
        int D = 30;  // 格子單位寬
        bool GridDragging = false; // 格子 是否拖拉中
        Point GridDragStartPos = new Point();
        Font fn = new Font("Times New Roman", 20);
        Font fn2 = new Font("標楷體", 12);
        int AngleFrom = 0;
        int AngleTo = 360;
        bool VLine90, VLine180, VLine270, VLine360;

        public Form1()
        {
            InitializeComponent();
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);

        }

        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            {
                D = D + 1;
                if (D > 100) D = 100;
            }
            else if (e.Delta < 0)
            {
                D = D - 1;
                if (D < 5) D = 5;
            }

            this.Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            PointF p = new PointF();
            Point p0 = new Point();
            Point p1 = new Point();

            grid.Draw(e.Graphics, this.ClientSize.Width, this.ClientSize.Height, D);
            // 繪出 兩條 橫線
            e.Graphics.DrawLine(Pens.Violet, GetPoint(-1000, 10), GetPoint(1000, 10));
            e.Graphics.DrawLine(Pens.Violet, GetPoint(-1000, -10), GetPoint(1000, -10));
            e.Graphics.DrawString(" 1", fn, Brushes.Violet, GetPoint(-2, 10.5f), StringFormat.GenericTypographic);
            e.Graphics.DrawString("-1", fn, Brushes.Violet, GetPoint(-2, -9.5f), StringFormat.GenericTypographic);

            // 繪出 度數的直線
            if (VLine90)
            {
                e.Graphics.DrawLine(Pens.Red, GetPoint(9, 20), GetPoint(9, -20));
                e.Graphics.DrawString(" 0.5*pi=90度", fn2, Brushes.Red, GetPoint(9, -20), StringFormat.GenericTypographic);
            }

            if (VLine180)
            {
                e.Graphics.DrawLine(Pens.Red, GetPoint(18, 20), GetPoint(18, -20));
                e.Graphics.DrawString(" pi=180度", fn2, Brushes.Red, GetPoint(18, 20), StringFormat.GenericTypographic);
            }

            if (VLine270)
            {
                e.Graphics.DrawLine(Pens.Red, GetPoint(27, 20), GetPoint(27, -20));
                e.Graphics.DrawString(" 1.5*pi=270度", fn2, Brushes.Red, GetPoint(27, -20), StringFormat.GenericTypographic);
            }

            if (VLine360)
            {
                e.Graphics.DrawLine(Pens.Red, GetPoint(36, 20), GetPoint(36, -20));
                e.Graphics.DrawString(" 2*pi=360度", fn2, Brushes.Red, GetPoint(36, 20), StringFormat.GenericTypographic);
            }
            
            if (checkBox1.Checked) // sin(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (float)Math.Sin(AngleFrom * Math.PI / 180);
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom+1; i <= AngleTo; i++)
                {
                    p.X = i*0.1f;
                    p.Y = 10*(float)Math.Sin(i * Math.PI / 180);
                    p1 = GetPoint(p.X, p.Y);
                    e.Graphics.DrawLine(Pens.Black, p0, p1);
                    p0 = p1;
                }
            }

            if (checkBox2.Checked) // cos(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (float)Math.Cos(AngleFrom * Math.PI / 180);
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom + 1; i <= AngleTo; i++)
                {
                    p.X = i * 0.1f;
                    p.Y = 10 * (float)Math.Cos(i * Math.PI / 180);
                    p1 = GetPoint(p.X, p.Y);
                    e.Graphics.DrawLine(Pens.Blue, p0, p1);
                    p0 = p1;
                }
            }

            if (checkBox3.Checked) // tan(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (float)Math.Tan(AngleFrom * Math.PI / 180);
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom + 1; i <= AngleTo; i++)
                {
                    p.X = i * 0.1f;
                    p.Y = 10 * (float)Math.Tan(i * Math.PI / 180);
                    p1 = GetPoint(p.X, p.Y);

                    if (p0.Y <= 0 && p1.Y >= -this.ClientSize.Height)
                    {
                        // 從 正的無窮大 到 負的無窮大
                    }
                    else
                        e.Graphics.DrawLine(Pens.Brown, p0, p1);
                    p0 = p1;
                }
            }

            if (checkBox4.Checked) // cot(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (1 / (float)Math.Tan(AngleFrom * Math.PI / 180));
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom + 1; i <= AngleTo; i++)
                {
                    p.X = i * 0.1f;
                    p.Y = 10 * (1 / (float)Math.Tan(i * Math.PI / 180));
                    p1 = GetPoint(p.X, p.Y);

                    if (p0.Y >= -this.ClientSize.Height && p1.Y <= 0)
                    {
                        // 從 負的無窮大 到 正的無窮大
                    }
                    else
                    e.Graphics.DrawLine(Pens.Olive, p0, p1);
                    p0 = p1;
                }
            }

            if (checkBox5.Checked) // sec(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (1 / (float)Math.Cos(AngleFrom * Math.PI / 180));
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom + 1; i <= AngleTo; i++)
                {
                    p.X = i * 0.1f;
                    p.Y = 10 * (1 / (float)Math.Cos(i * Math.PI / 180));
                    p1 = GetPoint(p.X, p.Y);

                    if ((p0.Y <= 0 && p1.Y >= -this.ClientSize.Height) ||
                        (p0.Y >= -this.ClientSize.Height && p1.Y <= 0))
                    {
                        // 從 正的無窮大 到 負的無窮大
                        // 從 負的無窮大 到 正的無窮大
                    }
                    else
                      e.Graphics.DrawLine(Pens.BlueViolet, p0, p1);
                    p0 = p1;
                }
            } 

            if (checkBox6.Checked) // csc(θ)
            {
                p.X = AngleFrom * 0.1f;
                p.Y = 10 * (1 / (float)Math.Sin(AngleFrom * Math.PI / 180));
                p0 = GetPoint(p.X, p.Y);

                for (int i = AngleFrom + 1; i <= AngleTo; i++)
                {
                    p.X = i * 0.1f;
                    p.Y = 10 * (1 / (float)Math.Sin(i * Math.PI / 180));
                    p1 = GetPoint(p.X, p.Y);

                    if ((p0.Y <= 0 && p1.Y >= -this.ClientSize.Height) ||
                        (p0.Y >= -this.ClientSize.Height && p1.Y <= 0))
                    {
                        // 從 正的無窮大 到 負的無窮大
                        // 從 負的無窮大 到 正的無窮大
                    }
                    else
                    e.Graphics.DrawLine(Pens.DimGray, p0, p1);
                    p0 = p1;
                }
            }
        }

        // 由 格子座標 的點 算出 視窗座標 的 小點矩形區域 (軌跡小點使用)
        Rectangle GetRect2(PointF p)
        {
            Rectangle rect = new Rectangle();
            rect.X = (int)(this.ClientSize.Width / 2 + p.X * D - 1) + grid.offset.X;

            float temp = this.ClientSize.Height / 2 - p.Y * D - 1 + grid.offset.Y;
            if (temp > 1000) temp = 1000;
            else if (temp < -1000) temp = -1000;
            rect.Y = (int)(temp);  // for tan()

            rect.Width = 2;
            rect.Height = 2;
            return rect;
        }
        //由 格子座標 的點 算出 視窗座標 的點 
        Point GetPoint(float x, float y)
        {
            Point point = new Point();
            point.X = (int)(this.ClientSize.Width / 2 + x * D - 1) + grid.offset.X;
            float temp = (this.ClientSize.Height / 2 - y * D - 1) + grid.offset.Y;
            if (temp > 1000) temp = 1000;
            else if (temp < -1000) temp = -1000;
            point.Y = (int)(temp);
            return point;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            GridDragging = true;
            GridDragStartPos = e.Location;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (GridDragging)
            {
                int dx = (e.X - GridDragStartPos.X);
                int dy = (e.Y - GridDragStartPos.Y);
                grid.AdjustOffset(dx, dy);
                GridDragStartPos = e.Location;
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            GridDragging = false;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            grid.offset = new Point(0, 0);
            this.Invalidate();
        }

        private void checkBox7_CheckedChanged(object sender, EventArgs e)
        {
            VLine90 = !VLine90;
            this.Invalidate();
        }

        private void checkBox8_CheckedChanged(object sender, EventArgs e)
        {
            VLine180 = !VLine180;
            this.Invalidate();
        }

        private void checkBox9_CheckedChanged(object sender, EventArgs e)
        {
            VLine270 = !VLine270;
            this.Invalidate();
        }

        private void checkBox10_CheckedChanged(object sender, EventArgs e)
        {
            VLine360 = !VLine360;
            this.Invalidate();
        }

        private void checkBox11_CheckedChanged(object sender, EventArgs e)
        {
            grid.FrameVisible = !grid.FrameVisible;
            this.Invalidate();
        }

        private void checkBox12_CheckedChanged(object sender, EventArgs e)
        {
            if (!checkBox12.Checked)
            {
                AngleFrom = -720 * 4;
                AngleTo = 720 * 4;
            }
            else
            {
                AngleFrom = 0;
                AngleTo = 360;
            }
            this.Invalidate();
        }
    }
}