using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_ScreenCapture3
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

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();//隱藏當前窗體

            Thread.Sleep(200);//讓線程睡眠一段時間，窗體消失需要一點時間

            int width = Screen.PrimaryScreen.Bounds.Width;
            int height = Screen.PrimaryScreen.Bounds.Height;

            Bitmap bmp = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bmp);
            g.CopyFromScreen(0, 0, 0, 0, new Size(width, height));

            FullScreenForm f2 = new FullScreenForm(bmp);
            if (f2.ShowDialog() == DialogResult.OK)
            {
                this.Show();//重新顯示窗體
                pictureBox1.Image = bmp;
            }
        }
    }
}

