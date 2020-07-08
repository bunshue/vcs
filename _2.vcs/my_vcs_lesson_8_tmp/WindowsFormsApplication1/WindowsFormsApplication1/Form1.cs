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
    //本例是實現在PicLabel上按下滑鼠左鍵拖曳的功能 
    public partial class Form1 : Form
    {
        bool isPress = false;
        //判斷是否有按下
        int oldX, oldY;
        //記錄按下的位置

        public Form1()
        {
            InitializeComponent();

            Image ii = WindowsFormsApplication1.Properties.Resources.picture1;
            //要在Properties.Resources放入圖片
            PicLabel.Text = "";
            PicLabel.AutoSize = false;
            //關閉自動調整大小
            PicLabel.Width = ii.Width;
            PicLabel.Height = ii.Height;
            PicLabel.Image = ii;
        }

        private void PicLabel_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == System.Windows.Forms.MouseButtons.Left)
            {
                isPress = true;
                oldX = e.X;
                oldY = e.Y;
            }
        }

        private void PicLabel_MouseMove(object sender, MouseEventArgs e)
        {
            if (isPress)
            {
                PicLabel.Left = e.X + (PicLabel.Left - oldX);
                PicLabel.Top = e.Y + (PicLabel.Top - oldY);
                //按下的點，可能在圖上的任一點，所以抓出對應的座標並加回去

            }
        }

        private void PicLabel_MouseUp(object sender, MouseEventArgs e)
        {
            isPress = false;

        }
    }
}
