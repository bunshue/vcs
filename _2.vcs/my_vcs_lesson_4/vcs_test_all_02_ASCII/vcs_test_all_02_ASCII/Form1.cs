using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_02_ASCII
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";

            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int j = 0;
            for (int i = 0x41; i < 0x5B; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t0x" + i.ToString("X2") + "\t" + (char)j + "\n";

            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //string test_string = "ABC可否開啟檔案總管？";
            string test_string = "如果用MysonLink，就要燒錄mega上放的韌體。";
            string test_string2 = "ABCDE";
            /*
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";

            }
            */
            for (int i = 0; i < test_string.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string[i] + "\t" + Convert.ToString(((int)test_string[i]), 16) + "\n";
            }
            for (int i = 0; i < test_string2.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string2[i] + "\t" + Convert.ToString(((int)test_string2[i]), 16) + "\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //string input = "Hello World!";
            string input = "基本運算制作USB启动盘ウィキペディア???世?生?????概?表????";
            char[] values = input.ToCharArray();
            foreach (char letter in values)
            {
                // Get the integral value of the character.
                int value = Convert.ToInt32(letter);
                // Convert the integer value to a hexadecimal value in string form.

                //Console.WriteLine($"Hexadecimal value of {letter} is {value:X}");
                richTextBox1.Text += "Hexadecimal value of " + letter + " is " + value.ToString("X4") + "\n";
            }

        }
    }
}
