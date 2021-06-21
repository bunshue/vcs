using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureSlideShow3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Image bmp;
        bool flag_no_fix_position = false;
        bool flag_pause = false;
        int cnt = 0;
        int total = 100;
        int W;
        int H;

        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;

            int x_st;
            x_st = bmp.Width - 100 - 1 * cnt;
            if (x_st > 0)
            {
                pictureBox1.Image = cropImage(bmp, new Rectangle(x_st, 0, 100, 300));
                GC.Collect();       //回收資源
            }
            else
                timer1.Enabled = false;
            
            //if (cnt >= 20)
              //  cnt = 0;
            /*
            pictureBox1.Width = pictureBox1.Image.Width / 8;
            pictureBox1.Height = pictureBox1.Image.Height / 8;
            this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
            if(flag_no_fix_position == false)
                this.Location = new System.Drawing.Point(1920 - pictureBox1.Width, 100);
            */

        }

        private Image cropImage(Image img, Rectangle cropArea)
        {
            Bitmap bmpImage = new Bitmap(img);
            return bmpImage.Clone(cropArea, bmpImage.PixelFormat);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(1920 - 250, 200);

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);

            bmp = vcs_PictureSlideShow3.Properties.Resources.chingming;

            W = bmp.Width;
            H = bmp.Height;

            pictureBox1.Image = cropImage(bmp, new Rectangle(bmp.Width - 100, 0, 100, 300));
            this.Size = new Size(pictureBox1.Width, pictureBox1.Height);

            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //Application.Exit();
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
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************

        #region 移動無邊框Form
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
                flag_no_fix_position = true;
            }
        }
        #endregion

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            {
                if (timer1.Interval > 5)
                    timer1.Interval -= 5;
            }
            else
                timer1.Interval += 10;
        }
    }
}
