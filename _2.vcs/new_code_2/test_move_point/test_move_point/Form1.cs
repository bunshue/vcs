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


namespace test_move_point
{
    public partial class Form1 : Form
    {
        //在多點網格移動的小球 ST
        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool flag_dragging = false; // 是否拖拉中
        Pen p = new Pen(Color.Green, 1);
        Point[] pts = new Point[4];

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
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int radius = 10;

            e.Graphics.DrawPolygon(p, pts);

            for (int i = 0; i < 4; i++)
            {
                FillCircle(e.Graphics, pts[i], radius, Color.Red);
            }
        }

        // 檢查是哪一個點被 選到
        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = 0; i < mpList.Count; i++)
            {
                if (mpList[i].CheckSelected(e.X, e.Y))
                {
                    mp_Selected = i;
                    flag_dragging = true;
                    //richTextBox1.Text += "選中 " + i.ToString() + "\n";
                    pts[mp_Selected].X = mpList[mp_Selected].pos.X;
                    pts[mp_Selected].Y = mpList[mp_Selected].pos.Y;
                    //pts[i] = new Point(mpList[i].pos.X, mpList[i].pos.Y); //same

                    richTextBox1.Text += "選中 " + i.ToString() + "\t" + mpList[mp_Selected].pos.ToString() + "\n";

                    break;
                }
            }
        }

        // 更新 被選到的點 的座標
        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                mpList[mp_Selected].Move(e.X, e.Y);

                pts[mp_Selected].X = mpList[mp_Selected].pos.X;
                pts[mp_Selected].Y = mpList[mp_Selected].pos.Y;

                this.Invalidate();
                this.pictureBox3.Invalidate();
            }
        }

        // 解除 被選到的點
        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_dragging == true)
            {
                richTextBox1.Text += "放開 " + mp_Selected.ToString() + "\t" + mpList[mp_Selected].pos.ToString() + "\n";

                mp_Selected = -1;
                flag_dragging = false;
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
