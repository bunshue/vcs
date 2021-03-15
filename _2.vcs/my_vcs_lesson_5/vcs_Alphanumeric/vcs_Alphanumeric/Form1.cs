using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Alphanumeric
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
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            //richTextBox1.Text += "已新建圖檔\n";
            //richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            bool[,] word = new bool[5, 7];

            //word = StringToBool("01110100010000100110010001000011111");     //2
            word = StringToBool("01110100011001110101110011000101110");     //0

            //word = StringToBool("01100001000010000100001000010001110");     //1

            //PrintArray(word);

            int x_st = 200;
            int y_st = 50;
            int w = 30;
            int h = 30;
            int dx = w + 10;
            int dy = h + 10;

            for (int j = 0; j < 7; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    //richTextBox1.Text += "word[" + i.ToString() + ", " + j.ToString() + "] = " + word[i, j].ToString() + "\n";
                    richTextBox1.Text += word[i, j].ToString() + " ";

                    if (word[i, j] == true)
                        sb = new SolidBrush(Color.Red);
                    else
                        sb = new SolidBrush(Color.Black);

                    if (word[i, j] == true)
                        g.FillRectangle(sb, x_st + i * dx, y_st + j * dy, w, h);
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        // Display the array's values in the Console window.
        private void PrintArray<T>(T[,] arr)
        {
            richTextBox1.Text += "AAAAA\n";
            for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
            {
                for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
                {
                    richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        // Convert a string of the form 10100110...
        // into an array of bool.
        private bool[,] StringToBool(string values)
        {
            int len = values.Length;
            bool[] result = new bool[len];
            for (int i = 0; i < len; i++)
            {
                result[i] = (values[i] == '1');
            }

            bool[,] word = new bool[5, 7];

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += result[i].ToString() + "\t";

                word[i % 5, i / 5] = result[i];


                //richTextBox1.Text += "word[" + (i % 5).ToString() + ", " + (i / 5).ToString() + "] = " + word[i % 5, i / 5].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            /*
            for (int j = 0; j < 7; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    //richTextBox1.Text += "word[" + i.ToString() + ", " + j.ToString() + "] = " + word[i, j].ToString() + "\n";
                    richTextBox1.Text += word[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            */

            return word;
        }






    }
}
