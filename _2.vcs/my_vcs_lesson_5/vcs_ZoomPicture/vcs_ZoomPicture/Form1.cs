using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ZoomPicture
{
    public partial class Form1 : Form
    {
        Graphics g;	//設定一個畫布g
        int ratio = 100;
        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();	//這個視窗，就是畫布
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Image image = Image.FromFile("C:\\______test_vcs\\_case1\\pic2.jpg");
            //pictureBox1.Image = image1;
            int width = image.Width;
            int height = image.Height;
            Bitmap bmp = new Bitmap(image, width * ratio / 100, height * ratio / 100);
            //g.DrawImage(bmp, 50, 50);
            g.DrawImage(bmp, this.ClientSize.Width / 2 - width * ratio / 100 / 2, this.ClientSize.Height / 2 - height * ratio / 100 / 2);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Add:
                    if(ratio < 500)
                        ratio += 10;
                    this.Refresh();
                    break;
                case Keys.Subtract:
                    if (ratio > 10)
                        ratio -= 10;
                    this.Refresh();
                    break;
                default:
                    break;
            }
        }
    }
}
