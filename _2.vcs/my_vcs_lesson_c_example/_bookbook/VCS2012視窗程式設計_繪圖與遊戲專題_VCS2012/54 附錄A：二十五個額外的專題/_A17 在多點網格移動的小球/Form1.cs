// 作者：鄞永傳老師  xnabook@yahoo.com.tw  2008.12.14
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        List<int> pathList = new List<int>(); // 小球 在 可移動點動態陣列 的路徑
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Pen myPen = new Pen(Color.Green, 1);  // 
        int D = 10; // 小球的半徑

        BallInNet ball; // 

        public Form1()
        {
            InitializeComponent();

            myPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            this.ClientSize = new Size(800, 600);
            // 加入5個可移動點  當作 網格 的個頂點
            Point[] pts = new Point[5];
            int Cx, Cy;
            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;

            double theta = -Math.PI / 2;
            for (int i = 0; i < pts.Length; i++)
            {
                pts[i].X = (int)(Cx + 200 * Math.Cos(theta));
                pts[i].Y = (int)(Cy + 200 * Math.Sin(theta));
                theta = theta + 2* Math.PI / pts.Length;
            }

            ClassMovingPoint mp;
            mp = new ClassMovingPoint(pts[0], 10, Color.Blue, "p0");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[1], 10, Color.Blue, "p1");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[2], 10, Color.Blue, "p2");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[3], 10, Color.Blue, "p3");
            mpList.Add(mp);
            mp = new ClassMovingPoint(pts[4], 10, Color.Blue, "p4");
            mpList.Add(mp);

            pathList.Add(0);
            pathList.Add(2);
            pathList.Add(1);
            pathList.Add(3);
            pathList.Add(4);

            ball = new BallInNet(mpList,pathList,
                5,
                D,
                Color.Red);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            for (int i = 0; i < mpList.Count; i++)
            {
                mpList[i].Draw(e.Graphics);
            }

            for (int i = 0; i < mpList.Count-1; i++)
            {
                for (int j = i+1; j < mpList.Count; j++)
                {
                    e.Graphics.DrawLine(myPen, mpList[i].pos, mpList[j].pos);
                }
            }

            ball.Draw(e.Graphics);
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

        // 更新 被選到的點 的座標
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                mpList[mp_Selected].Move(e.X, e.Y);

                this.Invalidate();
            }
        }

        // 解除 被選到的點
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            mp_Selected = -1;
            dragging = false;
        }
 
        private void timer1_Tick(object sender, EventArgs e)
        {
            ball.Update();
            this.Invalidate();
        }
    }
}