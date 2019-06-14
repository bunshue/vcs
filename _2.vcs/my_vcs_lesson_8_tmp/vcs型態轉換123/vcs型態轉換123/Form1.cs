using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs型態轉換123
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str = "this is a lion-mouse";
            richTextBox1.Text += "old string : " + str + "\n";

            byte[] byteArray = System.Text.Encoding.Default.GetBytes(str);
            richTextBox1.Text += "len = " + byteArray.Length.ToString() + ", to byte array\n";
            int i;
            for (i = 0; i < byteArray.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\n";  //多了(char)變成%c
            }
            


        }

        private void button2_Click(object sender, EventArgs e)
        {
            byte[] byteArray = new byte[5] { 0x41, 0x42, 0x43, 0x44, 0x45 };

            string str = System.Text.Encoding.Default.GetString(byteArray);

            richTextBox1.Text += "get string : " + str + "\n";


        }

        private void button3_Click(object sender, EventArgs e)
        {
            byte[] byteData = new byte[5] { 0x01, 0x02, 0x03, 0x04, 0x05 };
            char[] cChar = Encoding.ASCII.GetChars(byteData);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            byte[] byteData = Encoding.Default.GetBytes(cChar);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int dint = 170;
            string strHex = String.Format("{0:X2}", dint);    //X2的2代表若缺0會自動補0，所以沒有2也沒關係
            richTextBox1.Text += "result : " + strHex + "\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            string s2 = "AB";

            //轉換10進位
            int j = 0;
            int result = 0;

            for (int i = 0; i < s2.Length; i++)
            {
                result = result * 16;
                j = s2[i] - 48;
                if (j < 10)
                {
                    result = result + j;
                }
                else
                {
                    result = result + j - 39;
                }
            }
            richTextBox1.Text += "result : " + result.ToString() + "\n";

            //另一種寫法
            //Convert.ToInt32("100", 16);

            richTextBox1.Text += "result : " + Convert.ToInt32("AB", 16).ToString() + "\n";


        }
    }
}



