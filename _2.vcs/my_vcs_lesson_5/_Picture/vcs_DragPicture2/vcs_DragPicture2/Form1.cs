using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture2
{
    public partial class Form1 : Form
    {
        bool isPress = false;   //判斷是否有按下
        int oldX, oldY;         //記錄按下的位置

        public Form1()
        {
            InitializeComponent();
            Image image = Image.FromFile("C:\\______test_vcs\\bear.jpg");
            int width = image.Width;
            int height = image.Height;

            this.ClientSize = new Size(width + 200, height + 200);
            //要在Properties.Resources放入圖片
            label1.Text = "";
            label1.AutoSize = false;
            //關閉自動調整大小
            label1.Width = image.Width;
            label1.Height = image.Height;
            label1.Image = image;
            label1.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }

        private void label1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == System.Windows.Forms.MouseButtons.Left)
            {
                label1.Cursor = Cursors.Hand;
                isPress = true;
                oldX = e.X;
                oldY = e.Y;
            }

        }

        private void label1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isPress)
            {
                label1.Left = e.X + (label1.Left - oldX);
                label1.Top = e.Y + (label1.Top - oldY);
                //按下的點，可能在圖上的任一點，所以抓出對應的座標並加回去

            }

        }

        private void label1_MouseUp(object sender, MouseEventArgs e)
        {
            isPress = false;
        }

        private void label1_MouseEnter(object sender, EventArgs e)
        {
            label1.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }

        private void label1_MouseHover(object sender, EventArgs e)
        {
            label1.Cursor = Cursors.Cross;    //移到控件上，改變鼠標
        }
    }
}
