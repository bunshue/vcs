using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureSlideShow2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool flag_no_fix_position = false;
        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            switch (cnt)
            {
                case 1: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony01; break;
                case 2: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony02; break;
                case 3: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony03; break;
                case 4: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony04; break;
                case 5: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony05; break;
                case 6: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony06; break;
                case 7: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony07; break;
                case 8: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony08; break;
                case 9: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony09; break;
                //case 10: pictureBox1.Image = vcs_PictureSlideShow2.Properties.Resources.peony10; break;
                default:
                    break;
            }
            if (cnt >= 9)
                cnt = 0;
            pictureBox1.Width = pictureBox1.Image.Width / 8;
            pictureBox1.Height = pictureBox1.Image.Height / 8;
            this.Size = new Size(pictureBox1.Width, pictureBox1.Height);
            if(flag_no_fix_position == false)
                this.Location = new System.Drawing.Point(1920 - pictureBox1.Width, 100);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(1920 - 800, 100);

            this.FormBorderStyle = FormBorderStyle.None;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new System.Drawing.Point(0, 0);
            timer1_Tick(sender, e);
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //Application.Exit();
            timer1_Tick(sender, e);
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
    }
}
