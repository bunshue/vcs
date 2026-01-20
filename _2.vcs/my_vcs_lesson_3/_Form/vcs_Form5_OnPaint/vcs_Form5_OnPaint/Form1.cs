using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form5_OnPaint
{
    public partial class Form1 : Form
    {
        float Cx, Cy, Radius;

        public Form1()
        {
            InitializeComponent();
            SetStyle(ControlStyles.Opaque, true);   //無背景色
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            InitializeCircle();

            SetStyle(ControlStyles.Opaque, true);
            Point p = new Point(0, 0);
            Size s = new Size(500, 300);
            //Bounds = new Rectangle(0, 0, 500, 300);
            Bounds = new Rectangle(p, s);//窗體大小及相對於父客體的位置(0,0)
        }

        private void InitializeCircle()
        {
            Cx = this.ClientSize.Width / 2;
            Cy = this.ClientSize.Height / 2;
            Radius = (float)(Math.Min(Cx, Cy) * 0.8);
            this.Invalidate();
        }

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            int y = 0;
            g.FillRectangle(Brushes.Wheat, ClientRectangle);    //繪制窗體背景色

            //g.FillRectangle(Brushes.Blue, rect);//墳充一個矩形

            Font f = new Font("微軟正黑體", 30, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(0, y, 500, f.Height);
            string str = "重定義基類OnPaint()方法";
            g.DrawString(str, f, Brushes.Black, rect);
            rect.Y += 50;
            g.DrawString("使用Resize()方法", f, Brushes.Black, rect);
            f.Dispose();

            using (Pen pen = new Pen(Color.Red, 1))
            {
                for (y = 0; y <= ClientRectangle.Height; y += ClientRectangle.Height / 12)
                {

                    g.DrawLine(pen, new Point(0, 0), new Point(ClientRectangle.Width, y));
                }
            }
            g.FillEllipse(Brushes.Red, new Rectangle(100, 100, 50, 50));

            // Draw the circle.
            e.Graphics.DrawEllipse(Pens.Blue, Cx - Radius, Cy - Radius, Radius * 2, Radius * 2);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            InitializeCircle();
            this.Invalidate();
        }
    }
}
