using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox3
{
    public partial class Form1 : Form
    {
        /*
         * [C#]pictureBox隨滑鼠滾輪滾動改變大小
         * pictureBox的Sizemode屬性設為Zoom
         * 再添加事件
         * this.MouseWheel += new MouseEventHandler(Form1_MouseWheel);
         */


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.MouseWheel += new MouseEventHandler(Form1_MouseWheel);

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
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            pictureBox1.Size = new Size(663, 377);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(930, 200);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(970, 820);
            this.Text = "vcs_PictureBox3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {

        }

        void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            var t = pictureBox1.Size;
            //t.Width += e.Delta;
            //t.Height += e.Delta;
            if (e.Delta > 0)
            {
                t.Width++;
                t.Height++;
            }
            else
            {
                t.Width--;
                t.Height--;
            }
            pictureBox1.Size = t;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            //1. 載入圖檔，由資源檔
            pictureBox1.Image = Resource1.bear;

            //2. picturebox載入一圖
            //pictureBox1.Image = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg"); //載入圖檔，由檔案

            //3. picturebox顯示圖檔
            //Image img = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
            //pictureBox1.Image = img;

            //pictureBox1.Height = 800; 設定圖片高度和寬度
            //pictureBox1.Width = 600;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Height += 10;
            pictureBox1.Width += 10;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Height -= 10;
            pictureBox1.Width -= 10;
        }
    }
}
