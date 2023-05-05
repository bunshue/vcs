using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/* 
加入 ContextMenuStrip
點選屬性/Items/打開集合/MenuItem 按加入
修改Text
*/

namespace vcs_Widget
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_cat\cat1.png";
        string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_png\ladybug.png";

        int nOldWndLeft;
        int nOldWndTop;
        int nClickX;
        int nClickY;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //自製類似widget的桌面小玩意
            this.FormBorderStyle = FormBorderStyle.None;
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份
            this.ShowInTaskbar = false;

            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //檢查滑鼠右鍵
            if (e.Button == MouseButtons.Right)
            {
                // Display the context menu.
                ShowContextMenu(e.Location);
                return;
            }

            //紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
            nOldWndLeft = this.Left;
            nOldWndTop = this.Top;
            nClickX = e.X;
            nClickY = e.Y;
        }

        // Prepare the context menu and display it.
        private void ShowContextMenu(Point location)
        {
            // Display the context menu.
            contextMenuStrip1.Show(pictureBox1, location);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (pictureBox1.Capture == true)        //如果滑鼠按著拖曳  
            {
                //'設定新的視窗位置  
                this.Top = e.Y + nOldWndTop - nClickY;
                this.Left = e.X + nOldWndLeft - nClickX;
                //更新紀錄的視窗位置  
                nOldWndLeft = this.Left;
                nOldWndTop = this.Top;
            }
        }
    }
}

