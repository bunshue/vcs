using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;//引用命名空間
namespace PlotOnButton
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Bitmap bmp;//實例Bitmap對像
        //打開要繪製的圖片
        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.gif|*.gif|*.jpg|*.jpg|*.bmp|*.bmp";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                bmp = new Bitmap(openFileDialog1.FileName);
                this.Invalidate();
            }
        }//開始繪圖
        private void button1_Paint(object sender, PaintEventArgs e)
        {
            if (bmp != null)
            {
                Graphics g = e.Graphics;
                TextureBrush myBrush = new TextureBrush(bmp);
                g.FillRectangle(myBrush, this.ClientRectangle);

            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void 打開文件ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bmp != null)
            { MessageBox.Show("已經繪圖了"); }
            else
            { MessageBox.Show("還沒有繪圖"); }
        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }

    }
}