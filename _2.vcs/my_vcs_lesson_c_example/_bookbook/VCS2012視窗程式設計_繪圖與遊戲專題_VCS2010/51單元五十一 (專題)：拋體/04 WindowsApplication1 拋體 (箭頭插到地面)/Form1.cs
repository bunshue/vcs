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
        double Theta = -Math.PI / 2;
        Pen MyPen = new Pen(Color.DarkBlue, 10);
        Font fn = new Font("標楷體", 12);

        int x0, y0; // 起初的位置
        int D = 100; // 力道
        ClassCannon b;
        List<ClassCannon> mylist = new List<ClassCannon>();

        bool SpaceUp = true;

        public Form1()
        {
            InitializeComponent();
            MyPen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            MyPen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int w = this.ClientSize.Width;
            int h = this.ClientSize.Height;

            e.Graphics.FillRectangle(Brushes.Black, x0-40, y0-20, 80, 40);

            x0 = 60;
            y0 = h;
            int x1 = x0 + (int)(D * Math.Cos(Theta));
            int y1 = y0 + (int)(D * Math.Sin(Theta));
            e.Graphics.DrawLine(MyPen, x0, y0, x1, y1);

            for (int i = mylist.Count - 1; i >= 0; i--)
            {
                if (mylist[i].x < 0 || mylist[i].x > w ) // 超過左右側 就移除
                    mylist.RemoveAt(i);
                else
                {
                    mylist[i].Draw(e.Graphics);
                    if (mylist[i].y > h)  // 到達下緣就不走了 
                    {
                        mylist[i].alive = false;
                    }
                }
            }

            e.Graphics.DrawString("發射座標 : (" + x0.ToString() + "," + y0.ToString() + ")",
               fn, Brushes.Black, 10, 10, StringFormat.GenericTypographic);

            e.Graphics.DrawString("發射仰角角度 : " + (-Theta * 180 / Math.PI).ToString(),
                fn, Brushes.Black, 10, 30, StringFormat.GenericTypographic);

            e.Graphics.DrawString("發射速度 (力道) : " + D.ToString(),
                fn, Brushes.Black, 10, 50, StringFormat.GenericTypographic);

            if (mylist.Count >= 1)
            {
                int k = mylist.Count - 1;
                e.Graphics.DrawString("拋體目前座標 : (" + mylist[k].x.ToString() + "," + mylist[k].y.ToString() + ")",
                    fn, Brushes.Blue, 10, 70, StringFormat.GenericTypographic);

                e.Graphics.DrawString("(X軸速度, Y軸速度) : (" + mylist[k].vx.ToString() + "," + mylist[k].vy.ToString() + ")",
                    fn, Brushes.Blue, 10, 90, StringFormat.GenericTypographic);

                e.Graphics.DrawString("目前的速度 : " + mylist[k].v.ToString(),
                    fn, Brushes.Blue, 10, 110, StringFormat.GenericTypographic);

                e.Graphics.DrawString("拋射的最大高度 : " + mylist[k].h.ToString(),
                    fn, Brushes.Blue, 10, 130, StringFormat.GenericTypographic);

                e.Graphics.DrawString("拋體在空中停留的時間 : " + mylist[k].T.ToString() + " 秒",
                    fn, Brushes.Blue, 10, 150, StringFormat.GenericTypographic);

                e.Graphics.DrawString("拋射的最遠距離 : " + mylist[k].R.ToString(),
                    fn, Brushes.Blue, 10, 170, StringFormat.GenericTypographic);
            }

        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.A || e.KeyData == Keys.Left)
            {
                Theta = Theta - 0.01;
            }
            else if (e.KeyData == Keys.D || e.KeyData == Keys.Right)
            {
                Theta = Theta + 0.01;
            }
            else if (e.KeyData == Keys.W || e.KeyData == Keys.Up)
            {
                D += 1;
            }
            else if (e.KeyData == Keys.S || e.KeyData == Keys.Down)
            {
                D -= 1;
            }
            else if (e.KeyData == Keys.Space && SpaceUp)
            {
                SpaceUp = false;
                b = new ClassCannon(x0, y0, D, Theta);
                mylist.Add(b);
                timer1.Enabled = true;
            }

            this.Invalidate();
        }


        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                SpaceUp = true;
            }

            if (e.KeyData == Keys.P)
                timer1.Enabled = !timer1.Enabled;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}