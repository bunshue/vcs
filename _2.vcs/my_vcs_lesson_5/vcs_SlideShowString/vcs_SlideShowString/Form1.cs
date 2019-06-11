using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SlideShowString
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Bitmap bmp;
        //bool flag_pause = false;
        //int cnt = 0;
        //int total = 100;
        int W;
        int H;

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(1920 - 250, 200);

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);


            timer1_Tick(sender, e);

            this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
        }

        void slide_show_string()
        {
            bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            W = pictureBox1.Width;
            H = pictureBox1.Height;
            int xx;
            int yy;
            for (yy = 0; yy < H; yy++)
            {
                for (xx = 0; xx < W; xx++)
                {
                    bmp.SetPixel(xx, yy, Color.FromArgb(30, 0x11, 0x33, 0x55));
                }
            }

            Graphics g;
            g = Graphics.FromImage(bmp);
            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 24);

            int head;
            int waist;
            int max_width = 0;
            int max_height = 0;

            string string1 = "李清照 醉花陰";
            string string2 = "薄霧濃雲愁永晝，瑞腦銷金獸。";
            string string3 = "佳節又重陽，玉枕紗櫥，半夜涼初透。";
            string string4 = "東籬把酒黃昏後，有暗香盈袖。";
            string string5 = "莫道不銷魂，簾捲西風，人比黃花瘦。";

            System.Drawing.StringFormat drawFormat = new System.Drawing.StringFormat();
            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;


            richTextBox1.Text += "pictureBox W = " + pictureBox1.Width.ToString() + "\t";
            richTextBox1.Text += "H = " + pictureBox1.Height.ToString() + "\n";

            Pen p;
            p = new Pen(Color.Red, 3);

            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height);

            Size sss;

            sss = g.MeasureString(string1, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 150, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            sss = g.MeasureString(string2, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 100, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            sss = g.MeasureString(string3, f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";
            //g.DrawRectangle(p, 50, 50, sss.Height - 1, sss.Width);

            if (max_width < sss.Width)
                max_width = sss.Width;
            if (max_height < sss.Height)
                max_height = sss.Height;

            richTextBox1.Text += "max_width = " + max_width.ToString() + "\t";
            richTextBox1.Text += "max_height = " + max_height.ToString() + "\n";

            if (max_width < pictureBox1.Height)
                head = (pictureBox1.Height - max_width) / 2;
            else
                head = 0;

            if (max_height * 3 < pictureBox1.Width)
                waist = (pictureBox1.Width - max_height * 3) / 4;
            else
                waist = 0;

            richTextBox1.Text += "head = " + head.ToString() + "\t";
            richTextBox1.Text += "waist = " + waist.ToString() + "\n";

            g.DrawString(string1, f, new SolidBrush(Color.Black), 0 + waist * 3 + max_height * 2, head, drawFormat);
            g.DrawString(string2, f, new SolidBrush(Color.Black), 0 + waist * 2 + max_height, head, drawFormat);
            g.DrawString(string3, f, new SolidBrush(Color.Black), 0 + waist, head, drawFormat);


            pictureBox1.Image = bmp;


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            slide_show_string();



        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //Application.Exit();

            /*
            //timer1_Tick(sender, e);
            if (flag_pause == false)
            {
                flag_pause = true;
                timer1.Enabled = false;
            }
            else
            {
                flag_pause = false;
                timer1.Enabled = true;
            }
            */
        }

        //***********************
        private Point mouseOffset;//记录鼠标坐标
        private bool isMouseDown = false;//是否按下鼠标
        //***********************

        #region 移动无边框窗体
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
