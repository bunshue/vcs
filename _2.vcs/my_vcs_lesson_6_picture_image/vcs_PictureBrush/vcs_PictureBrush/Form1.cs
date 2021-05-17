using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBrush
{
    public partial class Form1 : Form
    {
        Bitmap image;
        TextureBrush textureBrush;
        Pen p;
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics G; // 畫布物件

        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
            image = new Bitmap(filename);
            textureBrush = new TextureBrush(image);
            p = new Pen(textureBrush, 40);
            this.ClientSize = new Size(image.Width, image.Height);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            x = e.X; // 紀錄筆畫的起始點
            y = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 滑鼠的左鍵
            {
                G = this.CreateGraphics();
                G.DrawLine(p, x, y, e.X, e.Y);　// 寫到　buffer

                x = e.X; // 結束點 就是 下一次的 開始點
                y = e.Y;
            }
        }
    }
}

