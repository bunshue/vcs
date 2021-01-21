using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture4
{
    //本例是實現在Label上按下滑鼠左鍵拖曳的功能 
    public partial class Form1 : Form
    {
        bool isPress = false;
        //判斷是否有按下
        int oldX, oldY;
        //記錄按下的位置

        public Form1()
        {
            InitializeComponent();

            string filename = "C:\\______test_files\\picture1.jpg";
            Bitmap bitmap1;
            bitmap1 = new Bitmap(filename);

            Image img = Image.FromFile(filename);
            label1.Text = "";
            label1.AutoSize = false;
            //關閉自動調整大小
            label1.Width = img.Width;
            label1.Height = img.Height;
            label1.Image = img;
        }

        private void label1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == System.Windows.Forms.MouseButtons.Left)
            {
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
    }
}
