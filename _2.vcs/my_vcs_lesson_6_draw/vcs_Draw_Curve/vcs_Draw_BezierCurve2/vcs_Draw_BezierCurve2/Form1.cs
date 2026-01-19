using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_BezierCurve2
{
    public partial class Form1 : Form
    {
        List<MovingPoint> mpList = new List<MovingPoint>(); // 可移動點的動態陣列
        int mp_Selected = -1;  // 動態陣列 的第幾個 被選到
        bool dragging = false; // 是否拖拉中
        Pen penRed = new Pen(Color.Red, 3);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MovingPoint mp;
            mp = new MovingPoint(new Point(100, 200));
            mpList.Add(mp); // 第一個控制點

            mp = new MovingPoint(new Point(200, 100));
            mpList.Add(mp); // 第二個控制點

            mp = new MovingPoint(new Point(300, 300));
            mpList.Add(mp); // 第三個控制點

            mp = new MovingPoint(new Point(400, 200));
            mpList.Add(mp); // 第四個控制點

            mp = new MovingPoint(new Point(500, 100));
            mpList.Add(mp); // 第五個控制點

            mp = new MovingPoint(new Point(600, 300));
            mpList.Add(mp); // 第六個控制點

            mp = new MovingPoint(new Point(700, 200));
            mpList.Add(mp); // 第七個控制點
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point[] mpArray = new Point[7];
            for (int i = 0; i <= mpList.Count - 1; i++)
            {
                mpArray[i] = mpList[i].p;
            }
            e.Graphics.DrawBeziers(penRed, mpArray);

            //繪出切線
            e.Graphics.DrawLine(Pens.Black, mpList[0].p, mpList[1].p);
            e.Graphics.DrawLine(Pens.Black, mpList[2].p, mpList[3].p);

            e.Graphics.DrawLine(Pens.Black, mpList[3].p, mpList[4].p);
            e.Graphics.DrawLine(Pens.Black, mpList[5].p, mpList[6].p);

            //繪出 端點和控制點
            e.Graphics.DrawEllipse(Pens.Black, mpList[0].p.X - 10, mpList[0].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList[1].p.X - 10, mpList[1].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList[2].p.X - 10, mpList[2].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList[3].p.X - 10, mpList[3].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList[4].p.X - 10, mpList[4].p.Y - 10, 20, 20);
            e.Graphics.DrawRectangle(Pens.Black, mpList[5].p.X - 10, mpList[5].p.Y - 10, 20, 20);
            e.Graphics.DrawEllipse(Pens.Black, mpList[6].p.X - 10, mpList[6].p.Y - 10, 20, 20);
        }
    }
}

