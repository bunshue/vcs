using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Queue
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\picture1.jpg";
        string filename2 = @"C:\______test_files\bear.jpg";
        string filename3 = @"C:\______test_files\elephant.jpg";

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            update_queue_count();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第1張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第2張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第3張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (frames.Count > 0)
            {
                try
                {
                    Bitmap bitmap1 = frames.Dequeue();
                    pictureBox_show.Image = bitmap1;
                    richTextBox1.Text += "從Queue中讀出第1張圖, 從頭取\n";
                }
                catch (Exception ex)
                {
                }
            }
            else
            {
                richTextBox1.Text += "無圖可讀\n";
            }
            update_queue_count();
        }

        void update_queue_count()
        {
            label1.Text = "目前Queue中的張數 : " + frames.Count.ToString();
            //richTextBox1.Text += "目前Queue中的張數 : " + frames.Count.ToString() + "\n";
            pictureBox_count.Invalidate();
        }

        private void pictureBox_count_Paint(object sender, PaintEventArgs e)
        {
            int border = 10;    //10 percent
            int W = pictureBox_count.ClientSize.Width;
            int H = pictureBox_count.ClientSize.Height;
            int x_st = W * border / 100;
            int y_st = H * border / 100;
            int w = W * (100 - border * 2) / 100;
            int h = H * (100 - border * 2) / 100;

            int cnt = frames.Count;
            int i = 0;
            int width = 0;

            e.Graphics.Clear(Color.Pink);
            if (cnt == 0)
            {
            }
            else if (cnt <= 10)
            {
                width = w / 10;
                for (i = 0; i < cnt; i++)
                {
                    e.Graphics.FillRectangle(Brushes.Red, x_st + width * i, y_st, width, h);
                    e.Graphics.DrawRectangle(Pens.DarkRed, x_st + width * i, y_st, width, h);
                }

                

            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            frames.Clear();
            richTextBox1.Text += "清除Queue\n";
            update_queue_count();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            Queue<char> q = new Queue<char>();

            q.Enqueue('A');
            q.Enqueue('B');
            q.Enqueue('C');
            q.Enqueue('D');

            richTextBox1.Text += "Current queue: " + "\n";
            foreach (char c in q)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

            q.Enqueue('E');
            q.Enqueue('F');
            richTextBox1.Text += "Current queue: " + "\n";
            foreach (char c in q)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Removing some values " + "\n";
            char ch = (char)q.Dequeue();
            richTextBox1.Text += "The removed value: " + ch + "\n";
            ch = (char)q.Dequeue();
            richTextBox1.Text += "The removed value: " + ch + "\n";

        }
    }
}
