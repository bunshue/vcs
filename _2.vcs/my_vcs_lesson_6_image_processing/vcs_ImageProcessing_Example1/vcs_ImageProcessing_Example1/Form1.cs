using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_ImageProcessing_Example1
{
    public partial class Form1 : Form
    {
        //pictureBox0 ST
        string filename0 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_image_processing\vcs_ImageProcessing_Example1\vcs_ImageProcessing_Example1\img\VanGogh.png";
        Bitmap bitmap0;
        Point[] pArr1a = new Point[3];
        Point[] pArr2a = new Point[3];
        SolidBrush brush1a = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        SolidBrush brush2a = new SolidBrush(Color.FromArgb(64, 0, 255, 255));

        int Dx1a = 2;
        int Dx2a = -3;
        //pictureBox0 SP

        //pictureBox1 ST
        string filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_image_processing\vcs_ImageProcessing_Example1\vcs_ImageProcessing_Example1\img\Picasso_01.jpg";
        Bitmap bitmap1;
        Point[] pArr1b = new Point[3];
        Point[] pArr2b = new Point[3];
        SolidBrush brush1b = new SolidBrush(Color.FromArgb(64, 255, 255, 0));
        SolidBrush brush2b = new SolidBrush(Color.FromArgb(64, 0, 255, 255));
        int Dx1b = 2;
        int Dx2b = -3;

        //探照燈的位置
        Point mp1; //  moving point
        bool Selected1 = false;
        int dx1, dy1;

        Point mp2; //  moving point
        bool Selected2 = false;
        int dx2, dy2;
        //pictureBox1 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //pictureBox0 ST
            //this.Size = new Size(900, 700);
            //this.pictureBox_spotlight1.ClientSize = new Size(600, 600);
            bitmap0 = new Bitmap(filename0);
            pArr1a[0] = new Point(450, 600);
            pArr1a[1] = new Point(300 - 70, 0);
            pArr1a[2] = new Point(300 + 70, 0);

            pArr2a[0] = new Point(0, 0);
            pArr2a[1] = new Point(300 - 100, 600);
            pArr2a[2] = new Point(300 + 100, 600);
            //pictureBox0 SP

            //------------------------------------------------------------  # 60個

            //pictureBox1 ST
            //this.Size = new Size(900, 700);
            //this.pictureBox_spotlight1.ClientSize = new Size(600, 600);
            bitmap1 = new Bitmap(filename1);

            //this.Size = new Size(900, 700);
            //this.pictureBox_spotlight2.ClientSize = new Size(600, 600);

            mp1 = new Point(450, 600);
            pArr1b[0] = mp1;
            pArr1b[1] = new Point(300 - 70, 0);
            pArr1b[2] = new Point(300 + 70, 0);

            mp2 = new Point(150, 100);
            pArr2b[0] = new Point(0, 0);
            pArr2b[1] = new Point(300 - 100, 600);
            pArr2b[2] = new Point(300 + 100, 600);

            //pictureBox1 SP

            //------------------------------------------------------------  # 60個


        }

        void show_item_location()
        {
            int W = 640;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label0.Text = "探照燈";
            label1.Text = "探照燈";
            label2.Text = "";
            label3.Text = "";
            richTextBox1.Size = new Size(300, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1840, 940);
            this.Text = "vcs_MousePaint7";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void timer0_Tick(object sender, EventArgs e)
        {
            if (pArr1a[1].X <= 0 || pArr1a[2].X >= 600)
            {
                Dx1a = -Dx1a;
            }
            pArr1a[1].X = pArr1a[1].X + Dx1a;
            pArr1a[2].X = pArr1a[2].X + Dx1a;

            if (pArr2a[1].X <= 0 || pArr2a[2].X >= 600)
            {
                Dx2a = -Dx2a;
            }
            pArr2a[1].X = pArr2a[1].X + Dx2a;
            pArr2a[2].X = pArr2a[2].X + Dx2a;

            this.pictureBox0.Invalidate();
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap0, 0, 0, bitmap0.Width, bitmap0.Height);

            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr1a);
            e.Graphics.FillPath(brush1a, gp);

            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2a);
            e.Graphics.FillPath(brush2a, gp2);
        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (pArr1b[1].X <= 0 || pArr1b[2].X >= 600)
            {
                Dx1b = -Dx1b;
            }
            pArr1b[1].X = pArr1b[1].X + Dx1b;
            pArr1b[2].X = pArr1b[2].X + Dx1b;

            if (pArr2b[1].X <= 0 || pArr2b[2].X >= 600)
            {
                Dx2b = -Dx2b;
            }
            pArr2b[1].X = pArr2b[1].X + Dx2b;
            pArr2b[2].X = pArr2b[2].X + Dx2b;

            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // mp vs e.Location
            double dis = Math.Sqrt((mp1.X - e.X) * (mp1.X - e.X) + (mp1.Y - e.Y) * (mp1.Y - e.Y));
            if (dis <= 10)
            {
                Selected1 = true;
                dx1 = e.X - mp1.X;
                dy1 = e.Y - mp1.Y;
            }

            double dis2 = Math.Sqrt((mp2.X - e.X) * (mp2.X - e.X) + (mp2.Y - e.Y) * (mp2.Y - e.Y));
            if (dis2 <= 10)
            {
                Selected2 = true;
                dx2 = e.X - mp2.X;
                dy2 = e.Y - mp2.Y;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (Selected1 == true)
            {
                mp1.X = e.X - dx1;
                mp1.Y = e.Y - dy1;
            }

            if (Selected2 == true)
            {
                mp2.X = e.X - dx2;
                mp2.Y = e.Y - dy2;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Selected1 = false;
            Selected2 = false;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            e.Graphics.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            pArr1b[0] = mp1;
            GraphicsPath gp = new GraphicsPath();
            gp.AddPolygon(pArr1b);
            e.Graphics.FillPath(brush1b, gp);

            pArr2b[0] = mp2;
            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddPolygon(pArr2b);
            e.Graphics.FillPath(brush2b, gp2);

            e.Graphics.FillEllipse(Brushes.Red, mp1.X - 10, mp1.Y - 10, 20, 20);
            e.Graphics.FillEllipse(Brushes.Red, mp2.X - 10, mp2.Y - 10, 20, 20);
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


