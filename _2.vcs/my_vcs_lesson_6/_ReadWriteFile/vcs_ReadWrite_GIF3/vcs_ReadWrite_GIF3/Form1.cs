using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_GIF3
{
    public partial class Form1 : Form
    {
        static string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\cat.gif";

        Bitmap bitmap = new Bitmap(filename);
        bool current = false;

        public void AnimateImage()
        {
            if (current == false)
            {
                ImageAnimator.Animate(bitmap, new EventHandler(this.OnFrameChanged));
                current = true;
            }
        }

        private void OnFrameChanged(object o, EventArgs e)
        {
            this.Invalidate();
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            AnimateImage();
            ImageAnimator.UpdateFrames();

            e.Graphics.DrawImage(this.bitmap, new Point(0, 0));

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ImageAnimator.StopAnimate(bitmap, new EventHandler(this.OnFrameChanged));//停止
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ImageAnimator.Animate(bitmap, new EventHandler(this.OnFrameChanged));//播放
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}

