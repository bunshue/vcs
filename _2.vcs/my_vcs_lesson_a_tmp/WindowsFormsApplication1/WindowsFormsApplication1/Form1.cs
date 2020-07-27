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
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
            p = new Pen(Color.Red, 2);
            sb = new SolidBrush(Color.Navy);

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[,] x = { { 2, 3, 2 }, { 5, 6, 1 }, { 4, 6, 2 }, { 4, 6, 3 } };

            //int[, , , ,] y;

            richTextBox1.Text += "len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "rank = " + x.Rank.ToString() + "\n";
            //richTextBox1.Text += "rank = " + y.Rank.ToString() + "\n";


            int[, , ,] dim = new int[2, 5, 3, 7];
            richTextBox1.Text += "rank = " + dim.Rank.ToString() + "\n";
            //Console.WriteLine(dim.Rank);//結果 4

            //int[] num = { { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } } };
            //richTextBox1.Text += "rank = " + num.Rank.ToString() + "\n";
            //Console.WriteLine(num.Rank);//結果 3



        }

        private void button2_Click(object sender, EventArgs e)
        {

            //C# 如何產生 GUID?
            //可以直接透過內建方法，產生 GUID

            Guid guid = Guid.NewGuid();
            richTextBox1.Text += "GUID1 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID2 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID3 : " + guid + "\n";


        }

        private void button3_Click(object sender, EventArgs e)
        {
            checkSuperuser chk = new checkSuperuser();
            chk.ShowDialog();
        }
    }


}
