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

        string str_0 =
            "01110" +
            "10001" +
            "10011" +
            "10101" +
            "11001" +
            "10001" +
            "01110";

        string str_1 =
            "01100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "01110";

        string str_2 =
            "01110" +
            "10001" +
            "00001" +
            "00110" +
            "01000" +
            "10000" +
            "11111";

        string str_8 =
            "01110" +
            "10001" +
            "10001" +
            "01110" +
            "10001" +
            "10001" +
            "01110";

        string str_K =
            "10001" +
            "10010" +
            "10100" +
            "11000" +
            "10100" +
            "10010" +
            "10001";

        string str_L =
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "11111";

        string str_O =
            "01110" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "01110";

        string str_A =
            "00100" +
            "01010" +
            "10001" +
            "10001" +
            "11111" +
            "10001" +
            "10001";

        string str_B =
            "11110" +
            "10001" +
            "10001" +
            "11110" +
            "10001" +
            "10001" +
            "11110";

        string str_C =
            "01110" +
            "10001" +
            "10000" +
            "10000" +
            "10000" +
            "10001" +
            "01110";

        string str_D =
            "11110" +
            "01001" +
            "01001" +
            "01001" +
            "01001" +
            "01001" +
            "11110";

        string str_I =
            "01110" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "01110";

        string str_J =
            "01110" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "10100" +
            "01000";

        string str_M =
            "10001" +
            "11011" +
            "10101" +
            "10001" +
            "10001" +
            "10001" +
            "10001";

        string str_N =
            "10001" +
            "10001" +
            "11001" +
            "10101" +
            "10011" +
            "10001" +
            "10001";

        string str_G =
            "01111" +
            "10000" +
            "10000" +
            "10111" +
            "10001" +
            "10001" +
            "01111";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(BackColor);
            pictureBox1.Image = bitmap1;
            //richTextBox1.Text += "已新建圖檔\n";
            //richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";
        }

        void draw_alphanumeric(string str, int x_st, int y_st, int w, int h)
        {
            bool[,] word = new bool[5, 7];

            word = StringToBool(str);
            //PrintArray(word);

            int ddx = w * 3 / 10;
            int ddy = h * 3 / 10;

            int dx = w + ddx;
            int dy = h + ddy;

            for (int j = 0; j < 7; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    //richTextBox1.Text += "word[" + i.ToString() + ", " + j.ToString() + "] = " + word[i, j].ToString() + "\n";
                    //richTextBox1.Text += word[i, j].ToString() + " ";

                    sb = new SolidBrush(Color.Gray);
                    g.FillRectangle(sb, x_st + i * dx - 2, y_st + j * dy - 2, w + 4, h + 4);

                    if (word[i, j] == true)
                        sb = new SolidBrush(Color.Red);
                    else
                        sb = new SolidBrush(Color.Black);

                    if (word[i, j] == true)
                        g.FillRectangle(sb, x_st + i * dx, y_st + j * dy, w, h);
                }
                //richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            pictureBox1.Image = bitmap1;
            //Application.DoEvents();
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
                //richTextBox1.Text += result[i].ToString() + "\t";

                word[i % 5, i / 5] = result[i];

                //richTextBox1.Text += "word[" + (i % 5).ToString() + ", " + (i / 5).ToString() + "] = " + word[i % 5, i / 5].ToString() + "\n";
            }
            //richTextBox1.Text += "\n";

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

        private void button2_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);
            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);

            int x_st = 20;
            int y_st = 20;

            int w = 20;
            int h = 20;

            int dx = w * 7 + 10;
            int dy = h * 9 + 10;

            draw_alphanumeric(str_2, x_st + dx * 0, y_st + dy * 0, w, h);

            draw_alphanumeric(str_0, x_st + dx * 1, y_st + dy * 0, w, h);

            draw_alphanumeric(str_2, x_st + dx * 2, y_st + dy * 0, w, h);

            draw_alphanumeric(str_1, x_st + dx * 3, y_st + dy * 0, w, h);

            draw_alphanumeric(str_L, x_st + dx * 0, y_st + dy * 1, w, h);

            draw_alphanumeric(str_O, x_st + dx * 1, y_st + dy * 1, w, h);

            draw_alphanumeric(str_A, x_st + dx * 2, y_st + dy * 1, w, h);

            draw_alphanumeric(str_D, x_st + dx * 3, y_st + dy * 1, w, h);

            draw_alphanumeric(str_I, x_st + dx * 0, y_st + dy * 2, w, h);

            draw_alphanumeric(str_N, x_st + dx * 1, y_st + dy * 2, w, h);

            draw_alphanumeric(str_G, x_st + dx * 2, y_st + dy * 2, w, h);

            draw_alphanumeric(str_M, x_st + dx * 3, y_st + dy * 2, w, h);

            //draw_alphanumeric(str_J, x_st + dx * 0, y_st + dy * 3, w, h);
            //draw_alphanumeric(str_K, x_st + dx * 1, y_st + dy * 3, w, h);
            draw_alphanumeric(str_A, x_st + dx * 0, y_st + dy * 3, w, h);
            draw_alphanumeric(str_B, x_st + dx * 1, y_st + dy * 3, w, h);
            draw_alphanumeric(str_C, x_st + dx * 2, y_st + dy * 3, w, h);
            draw_alphanumeric(str_D, x_st + dx * 3, y_st + dy * 3, w, h);
        }


        private void button3_Click(object sender, EventArgs e)
        {
            //draw_alphanumeric("01100001000010000100001000010001110");   //1
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //draw_alphanumeric("01110100010000100110010001000011111");   //2
        }
    }
}

