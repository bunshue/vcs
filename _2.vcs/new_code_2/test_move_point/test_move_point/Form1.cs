using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_move_point
{
    public partial class Form1 : Form
    {
        //在多點網格移動的小球 ST
        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        List<int> pathList = new List<int>(); // 小球 在 可移動點動態陣列 的路徑
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Pen myPen = new Pen(Color.Green, 1);  // 
        //int D = 10; // 小球的半徑

        //BallInNet ball; // 
        //在多點網格移動的小球 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int x_st = 100;
            int y_st = 100;
            int w = 400;
            int h = 300;
            Point[] pts = new Point[4];

            pts[0] = new Point(x_st, y_st);
            pts[1] = new Point(x_st + w, y_st);
            pts[2] = new Point(x_st + w, y_st + h);
            pts[3] = new Point(x_st, y_st + h);


            ClassMovingPoint mp;
            mp = new ClassMovingPoint(pts[0], 10, Color.Blue, "p0");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[1], 10, Color.Blue, "p1");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[2], 10, Color.Blue, "p2");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[3], 10, Color.Blue, "p3");
            mpList.Add(mp);

            pathList.Add(0);
            pathList.Add(2);
            pathList.Add(1);
            pathList.Add(3);
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;


            int radius = 10;
            Point pt = new Point();

            for (int i = 0; i < mpList.Count; i++)
            {
                mpList[i].Draw(e.Graphics);
                FillCircle(e.Graphics, mpList[i].pos, radius, Color.Red);
            }

            for (int i = 0; i < mpList.Count - 1; i++)
            {
                for (int j = i + 1; j < mpList.Count; j++)
                {
                    e.Graphics.DrawLine(myPen, mpList[i].pos, mpList[j].pos);
                }
            }

        }

        // 檢查是哪一個點被 選到
        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
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

        // 更新 被選到的點 的座標
        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                mpList[mp_Selected].Move(e.X, e.Y);

                this.Invalidate();
                this.pictureBox3.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            mp_Selected = -1;
            dragging = false;

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
