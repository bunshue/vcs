using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for BitmapData
using System.Drawing.Drawing2D; //for InterpolationMode
using System.Runtime.InteropServices;   //for Marshal

namespace vcs_ImageProcessingI
{
    public partial class Form1 : Form
    {
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\naruto.jpg";
        string filename = @"C:\_git\vcs\_1.data\______test_files1\ims01.bmp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            reset_pictureBox();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 160 + 10;
            dy = 50 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                filename = openFileDialog1.FileName;
                reset_pictureBox();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
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
            bt_exit.Name = "bt_exit";
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

        void reset_pictureBox()
        {
            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }
    }
}
