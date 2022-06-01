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

        string snull =
            "00000" +
            "00000" +
            "00000" +
            "00000" +
            "00000" +
            "00000" +
            "00000";

        string scomma =
            "00000" +
            "00000" +
            "00100" +
            "00000" +
            "00100" +
            "00000" +
            "00000";

        string sslash =
            "00000" +
            "00001" +
            "00010" +
            "00100" +
            "01000" +
            "10000" +
            "00000";

        string sbackslash =
            "00000" +
            "10000" +
            "01000" +
            "00100" +
            "00010" +
            "00001" +
            "00000";

        string s0 =
            "01110" +
            "10001" +
            "10011" +
            "10101" +
            "11001" +
            "10001" +
            "01110";

        string s1 =
            "00100" +
            "01100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "01110";

        string s2 =
            "01110" +
            "10001" +
            "00001" +
            "00110" +
            "01000" +
            "10000" +
            "11111";

        string s3 =
            "01110" +
            "10001" +
            "00001" +
            "00110" +
            "00001" +
            "10001" +
            "01110";

        string s4 =
            "00011" +
            "00101" +
            "01001" +
            "10001" +
            "11111" +
            "00001" +
            "00001";

        string s5 =
            "11111" +
            "10000" +
            "11110" +
            "00001" +
            "00001" +
            "10001" +
            "01110";

        string s6 =
            "01110" +
            "10001" +
            "10000" +
            "11110" +
            "10001" +
            "10001" +
            "01110";

        string s7 =
            "11111" +
            "00001" +
            "00010" +
            "00100" +
            "01000" +
            "01000" +
            "01000";

        string s8 =
            "01110" +
            "10001" +
            "10001" +
            "01110" +
            "10001" +
            "10001" +
            "01110";

        string s9 =
            "01110" +
            "10001" +
            "10001" +
            "01111" +
            "00001" +
            "10001" +
            "01110";

        string sA =
            "00100" +
            "01010" +
            "10001" +
            "10001" +
            "11111" +
            "10001" +
            "10001";

        string sB =
            "11110" +
            "10001" +
            "10001" +
            "11110" +
            "10001" +
            "10001" +
            "11110";

        string sC =
            "01110" +
            "10001" +
            "10000" +
            "10000" +
            "10000" +
            "10001" +
            "01110";

        string sD =
            "11110" +
            "01001" +
            "01001" +
            "01001" +
            "01001" +
            "01001" +
            "11110";

        string sE =
            "11111" +
            "10000" +
            "10000" +
            "11110" +
            "10000" +
            "10000" +
            "11111";

        string sF =
            "11111" +
            "10000" +
            "10000" +
            "11110" +
            "10000" +
            "10000" +
            "10000";

        string sG =
            "01110" +
            "10001" +
            "10000" +
            "10000" +
            "10011" +
            "10001" +
            "01110";

        string sH =
            "10001" +
            "10001" +
            "10001" +
            "11111" +
            "10001" +
            "10001" +
            "10001";

        string sI =
            "01110" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "01110";

        string sJ =
            "00111" +
            "00010" +
            "00010" +
            "00010" +
            "10010" +
            "10010" +
            "01100";

        string sK =
            "10001" +
            "10010" +
            "10100" +
            "11000" +
            "10100" +
            "10010" +
            "10001";

        string sL =
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "10000" +
            "11111";

        string sM =
            "10001" +
            "11011" +
            "10101" +
            "10001" +
            "10001" +
            "10001" +
            "10001";

        string sN =
            "10001" +
            "10001" +
            "11001" +
            "10101" +
            "10011" +
            "10001" +
            "10001";

        string sO =
            "01110" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "01110";

        string sP =
            "11110" +
            "10001" +
            "10001" +
            "11110" +
            "10000" +
            "10000" +
            "10000";

        string sQ =
            "01110" +
            "10001" +
            "10001" +
            "10001" +
            "10101" +
            "10010" +
            "01101";

        string sR =
            "11110" +
            "10001" +
            "10001" +
            "11110" +
            "10001" +
            "10001" +
            "10001";

        string sS =
            "01110" +
            "10001" +
            "10000" +
            "01110" +
            "00001" +
            "10001" +
            "01110";

        string sT =
            "11111" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "00100" +
            "00100";

        string sU =
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "01110";

        string sV =
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "01010" +
            "00100";

        string sW =
            "10001" +
            "10001" +
            "10001" +
            "10001" +
            "10101" +
            "10101" +
            "01010";

        string sX =
            "10001" +
            "10001" +
            "01010" +
            "00100" +
            "01010" +
            "10001" +
            "10001";

        string sY =
            "10001" +
            "10001" +
            "01010" +
            "00100" +
            "00100" +
            "00100" +
            "00100";

        string sZ =
            "11111" +
            "00001" +
            "00010" +
            "00100" +
            "01000" +
            "10000" +
            "11111";

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

        string get_alphanumeric_string(char c)
        {
            string result = snull;
            switch (c)
            {
                case ':': result = scomma; break;
                case '0': result = s0; break;
                case '1': result = s1; break;
                case '2': result = s2; break;
                case '3': result = s3; break;
                case '4': result = s4; break;
                case '5': result = s5; break;
                case '6': result = s6; break;
                case '7': result = s7; break;
                case '8': result = s8; break;
                case '9': result = s9; break;
                case 'A': result = sA; break;
                case 'B': result = sB; break;
                case 'C': result = sC; break;
                case 'D': result = sD; break;
                case 'E': result = sE; break;
                case 'F': result = sF; break;
                case 'G': result = sG; break;
                case 'H': result = sH; break;
                case 'I': result = sI; break;
                case 'J': result = sJ; break;
                case 'K': result = sK; break;
                case 'L': result = sL; break;
                case 'M': result = sM; break;
                case 'N': result = sN; break;
                case 'O': result = sO; break;
                case 'P': result = sP; break;
                case 'Q': result = sQ; break;
                case 'R': result = sR; break;
                case 'S': result = sS; break;
                case 'T': result = sT; break;
                case 'U': result = sU; break;
                case 'V': result = sV; break;
                case 'W': result = sW; break;
                case 'X': result = sX; break;
                case 'Y': result = sY; break;
                case 'Z': result = sZ; break;

                default: break;
            }
            return result;
        }

        void draw_alphanumeric(char c, int size, Color forecolor, Color backcolor, int x_st, int y_st)
        {
            string str = get_alphanumeric_string(c);
            draw_alphanumeric0(str, size, forecolor, backcolor, x_st, y_st);
        }

        void draw_alphanumeric0(string str, int size, Color forecolor, Color backcolor, int x_st, int y_st)
        {
            bool[,] word = new bool[5, 7];

            word = StringToBool(str);
            //PrintArray(word);

            int w = size;
            int h = size;

            int ddx = w * 4 / 10;
            int ddy = h * 4 / 10;

            int dx = w + ddx;
            int dy = h + ddy;

            for (int j = 0; j < 7; j++)
            {
                for (int i = 0; i < 5; i++)
                {
                    //richTextBox1.Text += "word[" + i.ToString() + ", " + j.ToString() + "] = " + word[i, j].ToString() + "\n";
                    //richTextBox1.Text += word[i, j].ToString() + " ";

                    sb = new SolidBrush(backcolor);
                    g.FillRectangle(sb, x_st + i * dx - 2, y_st + j * dy - 2, w + 4, h + 4);

                    if (word[i, j] == true)
                        sb = new SolidBrush(forecolor);
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

            int w = 15;
            int h = 15;

            int dx = w * 7 + 10;
            int dy = h * 9 + 20;

            //draw_alphanumeric0(str, size, forecolor, backcolor, x_st, y_st);

            int size = 15;
            Color forecolor = Color.Red;
            Color backcolor = Color.Gray;

            draw_alphanumeric0(s1, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 0);
            draw_alphanumeric0(s2, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 0);
            draw_alphanumeric0(s3, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 0);
            draw_alphanumeric0(s4, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 0);
            draw_alphanumeric0(s5, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 0);

            draw_alphanumeric0(s6, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 1);
            draw_alphanumeric0(s7, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 1);
            draw_alphanumeric0(s8, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 1);
            draw_alphanumeric0(s9, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 1);
            draw_alphanumeric0(s0, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 1);

            draw_alphanumeric0(sA, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 2);
            draw_alphanumeric0(sB, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 2);
            draw_alphanumeric0(sC, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 2);
            draw_alphanumeric0(sD, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 2);
            draw_alphanumeric0(sE, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 2);
            draw_alphanumeric0(sF, size, forecolor, backcolor, x_st + dx * 5, y_st + dy * 2);
            draw_alphanumeric0(sG, size, forecolor, backcolor, x_st + dx * 6, y_st + dy * 2);

            draw_alphanumeric0(sH, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 3);
            draw_alphanumeric0(sI, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 3);
            draw_alphanumeric0(sJ, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 3);
            draw_alphanumeric0(sK, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 3);
            draw_alphanumeric0(sL, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 3);
            draw_alphanumeric0(sM, size, forecolor, backcolor, x_st + dx * 5, y_st + dy * 3);
            draw_alphanumeric0(sN, size, forecolor, backcolor, x_st + dx * 6, y_st + dy * 3);

            draw_alphanumeric0(sO, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 4);
            draw_alphanumeric0(sP, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 4);
            draw_alphanumeric0(sQ, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 4);
            draw_alphanumeric0(sR, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 4);
            draw_alphanumeric0(sS, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 4);
            draw_alphanumeric0(sT, size, forecolor, backcolor, x_st + dx * 5, y_st + dy * 4);
            draw_alphanumeric0(sU, size, forecolor, backcolor, x_st + dx * 6, y_st + dy * 4);

            draw_alphanumeric0(sV, size, forecolor, backcolor, x_st + dx * 0, y_st + dy * 5);
            draw_alphanumeric0(sW, size, forecolor, backcolor, x_st + dx * 1, y_st + dy * 5);
            draw_alphanumeric0(sX, size, forecolor, backcolor, x_st + dx * 2, y_st + dy * 5);
            draw_alphanumeric0(sY, size, forecolor, backcolor, x_st + dx * 3, y_st + dy * 5);
            draw_alphanumeric0(sZ, size, forecolor, backcolor, x_st + dx * 4, y_st + dy * 5);
        }

        void draw_string(string str, int size, Color forecolor, Color backcolor, int x_st, int y_st, int dx)
        {
            int len = str.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + str[i] + "\n";
                draw_alphanumeric(str[i], size, forecolor, backcolor, x_st + dx * i, y_st);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string str = "ABCD";
            int size = 15;
            Color forecolor = Color.Red;
            Color backcolor = Color.Gray;
            int x_st = 20;
            int y_st = 20;
            int dx = size * 7 + 10;

            draw_string(str, size, forecolor, backcolor, x_st, y_st, dx);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string current_time = DateTime.Now.ToString("HH:mm:ss");

            richTextBox1.Text += current_time + "\n";

            int size = 6;
            Color forecolor = Color.Red;
            Color backcolor = Color.Gray;
            int x_st = 600;
            int y_st = 20;
            int dx = size * 7 + 10;

            g.Clear(BackColor);
            draw_string(current_time, size, forecolor, backcolor, x_st, y_st, dx);
        }
    }
}

