using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_all
{
    public partial class Form1 : Form
    {
        private const int BORDER = 20;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int W = 1920;
            int H = 1080;
            int w = 640;
            int h = 480;
            int x_st;
            int y_st;
            int dx;
            int dy;

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(BORDER, BORDER);
            pictureBox1.BackColor = Color.Pink;

            //button
            x_st = 1240;
            y_st = 40;
            dx = 130;
            dy = 50;

            x_st = W / 3 * 2;
            y_st = BORDER;
            w = W / 3 - BORDER;
            h = 480;
            
            tabControl1.Size = new Size(w, h);
            tabControl1.Location = new Point(x_st, y_st);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(w, h);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = BORDER;
            y_st = BORDER;
            w = 100;
            h = 80;
            dx = w + BORDER / 2;
            dy = h + BORDER / 2;
            //第0頁 第0列
            bt_000.Size = new Size(100, 60);
            bt_010.Size = new Size(100, 60);
            bt_020.Size = new Size(100, 60);
            bt_030.Size = new Size(100, 60);
            bt_040.Size = new Size(100, 60);
            bt_000.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_010.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_020.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_030.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_040.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            //第0頁 第1列
            bt_001.Size = new Size(100, 60);
            bt_011.Size = new Size(100, 60);
            bt_021.Size = new Size(100, 60);
            bt_031.Size = new Size(100, 60);
            bt_041.Size = new Size(100, 60);
            bt_001.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_011.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_021.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_031.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_041.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            //第1頁 第0列
            bt_100.Size = new Size(100, 60);
            bt_110.Size = new Size(100, 60);
            bt_120.Size = new Size(100, 60);
            bt_130.Size = new Size(100, 60);
            bt_140.Size = new Size(100, 60);
            bt_100.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_110.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_120.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_130.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_140.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            //第1頁 第1列
            bt_101.Size = new Size(100, 60);
            bt_111.Size = new Size(100, 60);
            bt_121.Size = new Size(100, 60);
            bt_131.Size = new Size(100, 60);
            bt_141.Size = new Size(100, 60);
            bt_101.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_111.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_121.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_131.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_141.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            //第2頁 第0列
            bt_200.Size = new Size(100, 60);
            bt_210.Size = new Size(100, 60);
            bt_220.Size = new Size(100, 60);
            bt_230.Size = new Size(100, 60);
            bt_240.Size = new Size(100, 60);
            bt_200.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_210.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_220.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_230.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_240.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            //第2頁 第1列
            bt_201.Size = new Size(100, 60);
            bt_211.Size = new Size(100, 60);
            bt_221.Size = new Size(100, 60);
            bt_231.Size = new Size(100, 60);
            bt_241.Size = new Size(100, 60);
            bt_201.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_211.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_221.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_231.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_241.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            //第3頁 第0列
            bt_300.Size = new Size(100, 60);
            bt_310.Size = new Size(100, 60);
            bt_320.Size = new Size(100, 60);
            bt_330.Size = new Size(100, 60);
            bt_340.Size = new Size(100, 60);
            bt_300.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_310.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_320.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_330.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_340.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            //第3頁 第1列
            bt_301.Size = new Size(100, 60);
            bt_311.Size = new Size(100, 60);
            bt_321.Size = new Size(100, 60);
            bt_331.Size = new Size(100, 60);
            bt_341.Size = new Size(100, 60);
            bt_301.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_311.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_321.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_331.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_341.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //第0頁
        private void bt_000_Click(object sender, EventArgs e)
        {

        }

        private void bt_010_Click(object sender, EventArgs e)
        {

        }

        private void bt_020_Click(object sender, EventArgs e)
        {

        }

        private void bt_030_Click(object sender, EventArgs e)
        {

        }

        private void bt_040_Click(object sender, EventArgs e)
        {

        }

        private void bt_001_Click(object sender, EventArgs e)
        {

        }

        private void bt_011_Click(object sender, EventArgs e)
        {

        }

        private void bt_021_Click(object sender, EventArgs e)
        {

        }

        private void bt_031_Click(object sender, EventArgs e)
        {

        }

        private void bt_041_Click(object sender, EventArgs e)
        {

        }

        //第1頁
        private void bt_100_Click(object sender, EventArgs e)
        {

        }

        private void bt_110_Click(object sender, EventArgs e)
        {

        }

        private void bt_120_Click(object sender, EventArgs e)
        {

        }

        private void bt_130_Click(object sender, EventArgs e)
        {

        }

        private void bt_140_Click(object sender, EventArgs e)
        {

        }

        private void bt_101_Click(object sender, EventArgs e)
        {

        }

        private void bt_111_Click(object sender, EventArgs e)
        {

        }

        private void bt_121_Click(object sender, EventArgs e)
        {

        }

        private void bt_131_Click(object sender, EventArgs e)
        {

        }

        private void bt_141_Click(object sender, EventArgs e)
        {

        }

        //第2頁
        private void bt_200_Click(object sender, EventArgs e)
        {

        }

        private void bt_210_Click(object sender, EventArgs e)
        {

        }

        private void bt_220_Click(object sender, EventArgs e)
        {

        }

        private void bt_230_Click(object sender, EventArgs e)
        {

        }

        private void bt_240_Click(object sender, EventArgs e)
        {

        }

        private void bt_201_Click(object sender, EventArgs e)
        {

        }

        private void bt_211_Click(object sender, EventArgs e)
        {

        }

        private void bt_221_Click(object sender, EventArgs e)
        {

        }

        private void bt_231_Click(object sender, EventArgs e)
        {

        }

        private void bt_241_Click(object sender, EventArgs e)
        {

        }

        //第3頁
        private void bt_300_Click(object sender, EventArgs e)
        {

        }

        private void bt_310_Click(object sender, EventArgs e)
        {

        }

        private void bt_320_Click(object sender, EventArgs e)
        {

        }

        private void bt_330_Click(object sender, EventArgs e)
        {

        }

        private void bt_340_Click(object sender, EventArgs e)
        {

        }

        private void bt_301_Click(object sender, EventArgs e)
        {

        }

        private void bt_311_Click(object sender, EventArgs e)
        {

        }

        private void bt_321_Click(object sender, EventArgs e)
        {

        }

        private void bt_331_Click(object sender, EventArgs e)
        {

        }

        private void bt_341_Click(object sender, EventArgs e)
        {

        }
    }
}
