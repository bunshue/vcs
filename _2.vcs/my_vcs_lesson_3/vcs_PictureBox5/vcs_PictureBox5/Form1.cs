using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            Image loadedImage = Image.FromFile(filename);
            pictureBox1.Image = loadedImage;

            //拉動表單大小連帶改變pictureBox大小

            //圖片框PictureBox滿框(Zoom)
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            //圖片框PictureBox跟隨Form改變大小
            pictureBox1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;

            //要先把圖片框PictureBox靠近Form的邊緣
            //C# 控制項跟著視窗自動縮放或維持相對位置  可以使用 Control.Anchor 屬性

            pictureBox1.Dock = DockStyle.Fill;
        }
    }
}
