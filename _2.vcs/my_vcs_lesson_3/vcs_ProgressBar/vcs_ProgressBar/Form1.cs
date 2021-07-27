using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_ProgressBar
{
    public partial class Form1 : Form
    {
        MyProgressBar my_progressBar1;// = new MyProgressBar();
        Label lb;// = new Label();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            my_progressBar1 = new MyProgressBar();
            lb = new Label();

            //MyProgressBar cp = new MyProgressBar();
            my_progressBar1.Parent = progressBar1;
            my_progressBar1.Minimum = 0;//进度条显示最小值
            my_progressBar1.Maximum = 100;//进度条显示最大值
            my_progressBar1.Width = progressBar1.Width;
            my_progressBar1.Height = progressBar1.Height;
            my_progressBar1.BackColor = Color.Red;     //背景色
            //Label l = new Label();
            lb.Parent = my_progressBar1;
            lb.BackColor = Color.Transparent;
            lb.ForeColor = Color.Black;
            //lb.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            lb.TextAlign = System.Drawing.ContentAlignment.BottomRight;
            lb.Width = my_progressBar1.Width;
            lb.Height = my_progressBar1.Height;
        }

        int value = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            progressBar2.Value = value;
            label2.Text = value.ToString();

            my_progressBar1.Value = value;
            my_progressBar1.Invalidate();
            Application.DoEvents();
            lb.Text = my_progressBar1.Value.ToString();

            value += 1;
            if (value > 100)
            {
                value = 0;
            }
        }
    }

    public class MyProgressBar : ProgressBar
    {
        public MyProgressBar()
        {
            base.SetStyle(ControlStyles.UserPaint, true);
        }

        //重寫OnPaint方法
        protected override void OnPaint(PaintEventArgs e)
        {
            int border = 2;
            SolidBrush brush = null;
            Rectangle bounds = new Rectangle(0, 0, base.Width, base.Height);

            //e.Graphics.FillRectangle(new SolidBrush(this.BackColor), 1, 1, bounds.Width, bounds.Height);
            //e.Graphics.FillRectangle(new SolidBrush(Color.Green), 1, 1, bounds.Width, bounds.Height);

            bounds.Height -= border * 2;
            bounds.Width = ((int)(bounds.Width * (((double)base.Value) / ((double)base.Maximum)))) - border * 2;
            brush = new SolidBrush(Color.Yellow); //前景色
            e.Graphics.FillRectangle(brush, border, border, bounds.Width, bounds.Height);

            Font font = new Font("標楷體", (float)16, FontStyle.Regular);
            PointF pt = new PointF(base.Width / 2 - 10, base.Height / 2 - 13);
            e.Graphics.DrawString(base.Value.ToString(), font, Brushes.Black, pt);
        }
    }


}
