using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CutPicture
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Image img = Image.FromFile(@"C:\______test_vcs\picture1.jpg");

            pictureBox_src.Image = img;
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            Bitmap targetbitmap = new Bitmap(pictureBox_dst.Width, pictureBox_dst.Height, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            Graphics g = Graphics.FromImage(targetbitmap);

            int src_x = 0;
            int src_y = 0;

            if (radioButton1.Checked)   //左上
            {
                src_x = 0;
                src_y = 0;
            }
            else if (radioButton2.Checked)  //右上
            {
                src_x = pictureBox_src.Width / 2;
                src_y = 0;
            }
            else if (radioButton3.Checked)  //左下
            {
                src_x = 0;
                src_y = pictureBox_src.Height / 2;
            }
            else if (radioButton4.Checked)  //右下
            {
                src_x = pictureBox_src.Width / 2;
                src_y = pictureBox_src.Height / 2;
            }
            else if (radioButton5.Checked)   //中間
            {
                src_x = pictureBox_src.Width / 4;
                src_y = pictureBox_src.Height / 4;
            }

            //Graphics.DrawImage (Image, Rectangle, Rectangle, GraphicsUnit)
            //四個參數分別是     來源影像 目標區域  來源區域      單位

            g.DrawImage(pictureBox_src.Image,
                new Rectangle(0, 0, pictureBox_src.Width, pictureBox_src.Height),
                new Rectangle(src_x, src_y, pictureBox_src.Width / 2, pictureBox_src.Height / 2), GraphicsUnit.Pixel);

            pictureBox_dst.Image = targetbitmap;
        }
    }
}
