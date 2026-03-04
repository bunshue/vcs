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
        Pen myPen = new Pen(Color.FromArgb(64, 0, 255, 0), 40); // 透明的畫筆
        SolidBrush myBrush = new SolidBrush(Color.FromArgb(64, 0, 0, 255)); // 透明的塗刷
        Image image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            image = Image.FromFile(filename);
            pictureBox1.Image = image;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rectDest = new Rectangle(0, 0, image.Width, image.Height);
            e.Graphics.DrawImage(image, rectDest); // 呈現原圖
            e.Graphics.DrawLine(myPen, 0, 100, image.Width, 100); // 畫出透明的直線
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.pictureBox1.ClientSize.Height / 2;
            e.Graphics.FillEllipse(myBrush, Cx - 100, Cy - 100, 200, 200); // 繪畫出透明的圓形
        }
    }
}
