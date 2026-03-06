using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1303
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;
            pictureBox1.ClientSize = new Size(bitmap1.Width, bitmap1.Height);
        }

        private void tsslMsg_Click(object sender, EventArgs e)
        {
            pictureBox1.Left = 0;
            timer1.Start();//開始計時
            tsslMsg.Text = "移動圖片";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (pictureBox1.Left < 200)
            {
                //從表單的左邊移動圖片
                pictureBox1.Left += 5;
                tsspShow.Value = pictureBox1.Left;
                //顯示進度列目前進行的狀態
                tsslMsg.Text = String.Concat(tsspShow.Value / 3, " % 已經完成");
            }
            else
            {
                timer1.Stop();
                tsslMsg.Text = "使命已達";
            }
        }
    }
}
