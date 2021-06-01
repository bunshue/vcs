using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//先移動點

//再移動邊

namespace vcs_Draw_Drag
{
    public partial class Form1 : Form
    {
        int pt_selected = -1;  // 動態陣列 的 第幾個 被選到
        bool flag_dragging = false; // 是否拖拉中
        Pen p1 = new Pen(Color.Green, 1);
        Pen p2 = new Pen(Color.Blue, 1);
        Point[] pts = new Point[4];
        int Epsilon = 100; // 滑鼠 是否 點選到點 的距離 判斷 (避免 開根號)

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int x_st = 50;
            int y_st = 50;
            int w = 300;
            int h = 300;

            pts[0] = new Point(x_st, y_st);
            pts[1] = new Point(x_st + w, y_st);
            pts[2] = new Point(x_st + w, y_st + h);
            pts[3] = new Point(x_st, y_st + h);

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int radius = 10;

            if (flag_dragging == true)
                e.Graphics.DrawPolygon(p1, pts);
            else
                e.Graphics.DrawPolygon(p2, pts);

            for (int i = 0; i < 4; i++)
            {
                FillCircle(e.Graphics, pts[i], radius, Color.Red);
            }
            e.Graphics.DrawString("移動圓點", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(10, 370));
        }

        // 檢查是哪一個點被 選到
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = 0; i < pts.Length; i++)
            {
                if (CheckSelected(pts[i], e.Location) == true)
                {
                    pt_selected = i;
                    flag_dragging = true;
                    pts[pt_selected].X = e.X;
                    pts[pt_selected].Y = e.Y;
                    //richTextBox1.Text += "選中 " + i.ToString() + "\n";
                    break;
                }
                else
                {
                    //richTextBox1.Text += "沒選中\n";
                }
            }
        }

        // 更新 被選到的點 的座標
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                pts[pt_selected].X = e.X;
                pts[pt_selected].Y = e.Y;
                this.pictureBox1.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                pt_selected = -1;
                flag_dragging = false;
                this.pictureBox1.Invalidate();
            }
        }

        // 檢查是否選到這個點
        bool CheckSelected(Point pt1, Point pt2)
        {
            int dist = (pt1.X - pt2.X) * (pt1.X - pt2.X) + (pt1.Y - pt2.Y) * (pt1.Y - pt2.Y);
            if (dist <= Epsilon) // dis 是尚未開根號 的距離
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }
    }
}
