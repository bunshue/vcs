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

        }

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;
            //e.Graphics.Clear(Color.White);
            e.Graphics.DrawRectangle(Pens.Red, 50, 50, W - 50 * 2, H - 50 * 2);

            Font f = new Font("微軟正黑體", 22, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(100, 100, 500, f.Height);
            string str = "重定義基類OnPaint()方法";
            e.Graphics.DrawString(str, f, Brushes.Black, rect);
            e.Graphics.DrawString("使用Resize()方法", f, Brushes.Black, 100, 150);
            f.Dispose();

            float Cx = this.ClientSize.Width / 2;
            float Cy = this.ClientSize.Height / 2;
            float Radius = (float)(Math.Min(Cx, Cy) * 0.8);
            e.Graphics.DrawEllipse(Pens.Blue, Cx - Radius, Cy - Radius, Radius * 2, Radius * 2);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
