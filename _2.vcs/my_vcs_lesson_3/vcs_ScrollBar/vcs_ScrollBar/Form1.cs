using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ScrollBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            // pictureBox1顯示圖片
            pictureBox1.Image = new Bitmap(filename);
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

            hScrollBar1.Minimum = 0;
            hScrollBar1.Maximum = pictureBox1.Width;

            vScrollBar1.Minimum = 0;
            vScrollBar1.Maximum = pictureBox1.Height;

            //pictureBox1.Width = 300;
            //pictureBox1.Height = 225;
            //hScrollBar1.Value = 300;
            //vScrollBar1.Value = 225;

            //6060

            panel_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            panel_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            panel_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            panel_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            richTextBox1.Size = new Size(300, 680);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_ScrollBar";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // ===  當vScrollBar1垂直捲軸捲動時會執行此事件
            // 圖片的高度依目前垂直捲軸的值調整
            pictureBox1.Height = vScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // ===  當hScrollBar1水平捲軸捲動時會執行此事件
            // 圖片的寬度依目前水平捲軸的值調整
            pictureBox1.Width = hScrollBar1.Value;
            label1.Text = "寬：" + hScrollBar1.Value.ToString() + "       高：" + vScrollBar1.Value.ToString();
        }

        private void hScrollBar_rgb_Scroll(object sender, ScrollEventArgs e)
        {
            //用水平滾動條調整背景色的實例
            //调用了方法，另外把hScrollBar2的scrooll时间设置成hScrollBar1的scroll事件就行了
            panel_rgb.BackColor = Color.FromArgb(hScrollBar_r.Value, hScrollBar_g.Value, hScrollBar_b.Value);
            tb_r.Text = hScrollBar_r.Value.ToString();
            tb_g.Text = hScrollBar_g.Value.ToString();
            tb_b.Text = hScrollBar_b.Value.ToString();
            panel_r.BackColor = Color.FromArgb(hScrollBar_r.Value, 0, 0);
            panel_g.BackColor = Color.FromArgb(0, hScrollBar_g.Value, 0);
            panel_b.BackColor = Color.FromArgb(0, 0, hScrollBar_b.Value);
        }
    }
}
