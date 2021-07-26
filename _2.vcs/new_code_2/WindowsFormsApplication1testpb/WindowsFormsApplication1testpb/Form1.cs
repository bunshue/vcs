using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace WindowsFormsApplication1testpb
{
    public partial class Form1 : Form
    {
        MyProgressBar cp;// = new MyProgressBar();
        Label lb;// = new Label();

        public Form1()
        {
            InitializeComponent();


        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //progressBar1.ForeColor = Color.Red;
            //progressBar1.BackColor = Color.Green;


            cp = new MyProgressBar();
            lb = new Label();

            //MyProgressBar cp = new MyProgressBar();
            cp.Parent = progressBar1;
            cp.Minimum = 0;//进度条显示最小值
            cp.Maximum = 100;//进度条显示最大值
            cp.Width = progressBar1.Width;
            cp.Height = progressBar1.Height;
            cp.BackColor = Color.Red;     //背景色
            //Label l = new Label();
            lb.Parent = cp;
            lb.BackColor = Color.Transparent;
            lb.ForeColor = Color.Red;
            lb.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            lb.Width = cp.Width;
            lb.Height = cp.Height;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            for (int i = 33; i < 34; i++)
            {

                Thread.Sleep(100);
                cp.Value = i + 1;

                label1.Text = i.ToString();
                label2.Text = (i + 2).ToString();
                //SetProcessValue("aa", i + 1);
                //Font font = new Font("宋体", (float)16, FontStyle.Regular);
                //PointF pt = new PointF(cp.Width / 2 - 10, cp.Height / 2 - 13);
                //cp.CreateGraphics().DrawString(i.ToString(), font, Brushes.Red, pt);
                lb.Text = i.ToString();
                Application.DoEvents();
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //int i = 10;
            //Thread.Sleep(100);
            //cp.Value = i + 1;

            //label1.Text = i.ToString();
            //label2.Text = (i + 2).ToString();
            //SetProcessValue("aa", i + 1);
            //Font font = new Font("宋体", (float)16, FontStyle.Regular);
            //PointF pt = new PointF(cp.Width / 2 - 10, cp.Height / 2 - 13);
            //cp.CreateGraphics().DrawString(i.ToString(), font, Brushes.Red, pt);
            //l.Text = i.ToString();
            //Application.DoEvents();

            cp.Value = 10;
            cp.Invalidate();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            cp.Value = 70;
            cp.Invalidate();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            cp.Value = 30;
            label3.Text = cp.Value.ToString();
            Application.DoEvents(); 
            cp.Invalidate();

            for (int i = 0; i < 7; i++)
            {
                Thread.Sleep(1000);
                cp.Value -= 3;
                label3.Text = cp.Value.ToString();
                Application.DoEvents();
                cp.Invalidate();
            }
            for (int i = 0; i < 7; i++)
            {
                Thread.Sleep(1000);
                cp.Value += 3;
                label3.Text = cp.Value.ToString();
                Application.DoEvents();
                cp.Invalidate();
            }


        }

    }

    public class MyProgressBar : ProgressBar
    {
        public MyProgressBar()
        {
            base.SetStyle(ControlStyles.UserPaint, true);
        }

        //重写OnPaint方法
        protected override void OnPaint(PaintEventArgs e)
        {
            int border = 2;
            SolidBrush brush = null;
            Rectangle bounds = new Rectangle(0, 0, base.Width, base.Height);

            //e.Graphics.FillRectangle(new SolidBrush(this.BackColor), 1, 1, bounds.Width, bounds.Height);

            bounds.Height -= border * 2;
            bounds.Width = ((int)(bounds.Width * (((double)base.Value) / ((double)base.Maximum)))) - border * 2;
            //brush = new SolidBrush(Color.Coral);
            //brush = new SolidBrush(base.ForeColor);

            brush = new SolidBrush(Color.Yellow); //前景色

            e.Graphics.FillRectangle(brush, border, border, bounds.Width, bounds.Height);


        }
    }
}
