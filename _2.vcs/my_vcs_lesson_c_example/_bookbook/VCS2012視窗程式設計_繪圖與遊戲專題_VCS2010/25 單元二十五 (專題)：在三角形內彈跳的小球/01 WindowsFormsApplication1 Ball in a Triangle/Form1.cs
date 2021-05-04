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
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中

        Pen myPen = new Pen(Color.Green, 5);  // 有箭頭的直線筆 當作三角形的邊界
        int D = 10; // 小球的半徑

        BallInATriangle ball; // 在三角形 內的小球物件

        public Form1()
        {
            InitializeComponent();

            myPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            // 加入三個可移動點  當作 三角形 的三個頂點
            ClassMovingPoint mp;
            mp = new ClassMovingPoint(new Point(250, 30), 10, Color.Blue, "p1");
            mpList.Add(mp);
            mp = new ClassMovingPoint(new Point(100, 330), 10, Color.Blue, "p2");
            mpList.Add(mp);
            mp = new ClassMovingPoint(new Point(400, 330), 10, Color.Blue, "p3");
            mpList.Add(mp);

            Point q1 = new Point(300, 300);  // 獨立的一點 當作 小球的座標
            ball = new BallInATriangle(q1,
                new PointF(2, 3),
                D,
                Color.Red);

            isBallInTriangle(); // 小球 是否在三角形內
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            for (int i = 0; i < mpList.Count; i++)
            {
                mpList[i].Draw(e.Graphics);
            }

            e.Graphics.DrawLine(myPen, mpList[0].pos, mpList[1].pos);
            e.Graphics.DrawLine(myPen, mpList[1].pos, mpList[2].pos);
            e.Graphics.DrawLine(myPen, mpList[2].pos, mpList[0].pos);

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
            isBallInTriangle();
        }

        // 小球 是否在 mpList[0].pos, mpList[1].pos, mpList[2].pos 三角形內
        void isBallInTriangle()
        {
            bool ret = G2D_PointAndLine.IsPointInTriangle(mpList[0].pos, mpList[1].pos, mpList[2].pos, ball.position);
            if (ret == true)
                label1.Text = "小球 在 p1 p2 p3 三角形內！ (Inside)";
            else
                label1.Text = "小球 不在 p1 p2 p3 三角形內！ (Outside)";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ball.Update(mpList[0].pos, mpList[1].pos, mpList[2].pos);
            isBallInTriangle();
            this.Invalidate();
        }
    }
}