using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // for GraphicsPath

namespace WindowsFormsApplication1
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
            GraphicsPath gp = new GraphicsPath(); // 圖形軌跡物件

            //加入 兩條切線
            gp.AddLine(mpList[0].p, mpList[1].p);
            gp.CloseFigure(); // 關閉目前的圖形

            gp.AddLine(mpList[2].p, mpList[3].p);
            gp.CloseFigure(); // 關閉目前的圖形

            //加入 兩個端點 和 兩個控制點
            gp.AddEllipse(mpList[0].p.X - 10, mpList[0].p.Y - 10, 20, 20);
            Rectangle rect1, rect2;
            rect1 = new Rectangle(mpList[1].p.X - 10, mpList[1].p.Y - 10, 20, 20);
            rect2 = new Rectangle(mpList[2].p.X - 10, mpList[2].p.Y - 10, 20, 20);
            gp.AddRectangle(rect1);
            gp.AddRectangle(rect2);
            gp.AddEllipse(mpList[3].p.X - 10, mpList[3].p.Y - 10, 20, 20);

            // 只含貝茲曲線 的 GraphicsPath圖形軌跡物件
            GraphicsPath gp2 = new GraphicsPath(); // 圖形軌跡物件
            gp2.AddBezier(mpList[0].p, mpList[1].p, mpList[2].p, mpList[3].p);
            Region r1 = new Region(gp2); // 新增 區域表面 物件
            e.Graphics.FillRegion(Brushes.Yellow, r1); // 區域表面 繪出

            gp.AddPath(gp2, false); // 將 gp2 加入 gp 中
            e.Graphics.DrawPath(Pens.Black, gp); // 圖形軌跡 繪出
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
    }
}