using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinVHScrollBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // ===  表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            // pictureBox1顯示 "無尾熊.jpg"
            pictureBox1.Image = new Bitmap("../../../images/" + "無尾熊.jpg");
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            // 圖片方塊寬度指定給水平捲軸最大值
            hScrollBar1.Maximum = pictureBox1.Width;
            // 圖片方塊寬度指定給水平捲軸的值
            hScrollBar1.Value = pictureBox1.Width;
            // 圖片方塊高度指定給垂直捲軸最大值
            vScrollBar1.Maximum = pictureBox1.Height;
            // 圖片方塊高度指定給垂直捲軸的值
            vScrollBar1.Value = pictureBox1.Height;
            // label1顯示目前水平捲軸與垂直捲軸的值
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       " + "高：" + vScrollBar1.Value.ToString();
        }

        // ===  當vScrollBar1垂直捲軸捲動時會執行此事件
        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // 圖片的高度依目前垂直捲軸的值調整
            pictureBox1.Height = vScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }

        // ===  當hScrollBar1水平捲軸捲動時會執行此事件
        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // 圖片的寬度依目前水平捲軸的值調整
            pictureBox1.Width = hScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }
    }
}
