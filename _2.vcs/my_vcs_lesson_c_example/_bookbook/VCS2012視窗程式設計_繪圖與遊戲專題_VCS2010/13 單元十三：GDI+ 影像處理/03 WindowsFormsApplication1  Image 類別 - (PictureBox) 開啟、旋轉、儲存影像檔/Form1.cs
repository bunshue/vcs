using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        Image img; // Image 影像
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            img = Image.FromFile(filename); // 產生一個Image物件
            pictureBox1.BackgroundImage = img;
            // 呈現 影像 的寬高資訊
            label1.Text = "(" + img.Width.ToString() + ", " + img.Height.ToString() + ")";
        }

        // 90 度旋轉按鈕
        private void button2_Click(object sender, EventArgs e)
        {
            img.RotateFlip(RotateFlipType.Rotate90FlipNone); // 影像旋轉90度
            pictureBox1.BackgroundImage = img;
            pictureBox1.Refresh(); // pictureBox1 重畫
        }

    }
}
