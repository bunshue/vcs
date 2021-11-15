using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RichTextBox8
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

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1100;
            y_st = 10;
            dx = 100;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }


        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int len = richTextBox1.Lines.Length;

            richTextBox2.Text += "richTextBox1 共有 : " + len.ToString() + " 行\n";
            for (i = 0; i < len; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i] + "\tlen = " + richTextBox1.Lines[i].Length.ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //check
            int i;
            int j;
            int len = richTextBox1.Lines.Length;

            richTextBox2.Text += "richTextBox1 共有 : " + len.ToString() + " 行\n";
            for (i = 0; i < (len - 1); i++)
            {
                if (richTextBox1.Lines[i].Length <= 0)
                    continue;

                for (j = (i + 1); j < len; j++)
                {
                    if (richTextBox1.Lines[j].Length <= 0)
                        continue;

                    if (richTextBox1.Lines[i].Trim().Contains(richTextBox1.Lines[j].Trim()))
                    {
                        richTextBox2.Text += "第 " + i.ToString() + " 行 包含 第 " + j.ToString() + " 行\n";
                    }
                    else if (richTextBox1.Lines[j].Trim().Contains(richTextBox1.Lines[i].Trim()))
                    {
                        richTextBox2.Text += "第 " + j.ToString() + " 行 包含 第 " + i.ToString() + " 行\n";
                    }


                }
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Richtextbox 的比例因子 ZoomFactor
            richTextBox1.ZoomFactor = (float)3.2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Richtextbox 的比例因子 ZoomFactor
            richTextBox1.ZoomFactor = (float)1.0;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Font f = new Font("標楷體", 20F, FontStyle.Regular, GraphicsUnit.Point);
            Font f = new Font("標楷體", 20F, FontStyle.Bold, GraphicsUnit.Point);      //粗體


            richTextBox1.Font = f;

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //richTextBox2.Text += "A ";
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //抓 Ctrl + R
            byte asc = Convert.ToByte(e.KeyChar);
            //richTextBox2.Text += "|  " + e.KeyChar.ToString() + "  |  " + asc.ToString() + "  |  " + asc.ToString("X2") + "  |\n";
            if (asc == 18)  //ctrl + A = 1, ctrl + B = 2, ..., ctrl + R = 18
            {
                e.Handled = true;
                richTextBox2.Text += "你按了 ctrl + R\n";
            }

            //抓 Enter 鍵
            if (e.KeyChar == (char)Keys.Enter)
            {
                e.Handled = true;
                richTextBox2.Text += "你按了 Enter\n";
            }
        }
    }
}

