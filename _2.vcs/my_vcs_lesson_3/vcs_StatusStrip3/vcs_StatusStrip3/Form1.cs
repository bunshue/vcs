using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StatusStrip3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.toolStripStatusLabel3.AutoSize = false;
            this.toolStripProgressBar3.Maximum = 200;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.ClientSize = new Size(bitmap1.Width, bitmap1.Height);
        }

        private void toolStripStatusLabel3_Click(object sender, EventArgs e)
        {
            pictureBox1.Left = 0;
            timer3.Start();//開始計時
            toolStripStatusLabel3.Text = "移動圖片";
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            if (pictureBox1.Left < 200)
            {
                //從表單的左邊移動圖片
                pictureBox1.Left += 5;
                toolStripProgressBar3.Value = pictureBox1.Left;
                //顯示進度列目前進行的狀態
                toolStripStatusLabel3.Text = String.Concat(toolStripProgressBar3.Value / 3, " % 已經完成");
            }
            else
            {
                timer3.Stop();
                toolStripStatusLabel3.Text = "使命已達";
            }


        }

    }
}
