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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetStyle(ControlStyles.Opaque, true);
            Point p = new Point(0, 0);
            Size s = new Size(500, 300);
            //Bounds = new Rectangle(0, 0, 500, 300);
            Bounds = new Rectangle(p, s);//窗體大小及相對於父客體的位置(0,0)
        }

        protected override void OnPaint(PaintEventArgs e)//重定義基類OnPaint()方法
        {
            Graphics g = e.Graphics;
            int y = 0;
            g.FillRectangle(Brushes.White, ClientRectangle);//繪制窗體背景色
            //g.FillRectangle(Brushes.Blue, rect);//墳充一個矩形

            Font f = new Font("微軟正黑體", 30, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(0, y, 400, f.Height);
            string str = "微軟正黑體";
            g.DrawString(str, f, Brushes.Black, rect);
            f.Dispose();
        }




    }
}
