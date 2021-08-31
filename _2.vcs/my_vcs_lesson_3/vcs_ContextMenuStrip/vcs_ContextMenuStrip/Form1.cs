using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ContextMenuStrip
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\picture1.jpg";

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
            //same
            //Image img = Image.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //pictureBox1.Image = Image.FromFile(filename); //載入圖檔，由檔案

            //same
            //Bitmap bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

            //same
            //Image img = Bitmap.FromFile(filename);
            //pictureBox1.Image = img;

            //same
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            //pictureBox1.Image = bitmap1;

            //same
            pictureBox1.Image = new Bitmap(filename);

            //pictureBox1.ImageLocation = filename;   //可顯示圖片 但無法抓出圖片的相關資訊

            /*
            int width = pictureBox1.Image.Width;
            int height = pictureBox1.Image.Height;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Size = new Size(width, height);
            */

            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;


            this.Text = "在圖上按右鍵測試ContextMenuStrip";
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                contextMenuStrip1.Show(pictureBox1, e.Location);  //顯示ContextMenu
                return;
            }

            //紀錄滑鼠點選時的視窗位置與滑鼠點選位置  
            nOldWndLeft = this.Left;
            nOldWndTop = this.Top;
            nClickX = e.X;
            nClickY = e.Y;
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

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem1.Text + "\n";
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem2.Text + "\n";
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem3.Text + "\n";
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem4.Text + "\n";
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem5.Text + "\n";
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem6.Text + "\n";
        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem7.Text + "\n";
            this.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Visible = false;
            richTextBox1.Visible = false;
            //this.FormBorderStyle = FormBorderStyle.None;
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份
            this.ShowInTaskbar = false;
            //this.StartPosition = FormStartPosition.CenterScreen;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = Color.Black;

            //pictureBox1.Dock = DockStyle..Fill;      //停駐於父容器中
            pictureBox1.Location = new Point((this.Width - pictureBox1.Image.Width) / 2, (this.Height - pictureBox1.Image.Height) / 2);
        }
    }
}

