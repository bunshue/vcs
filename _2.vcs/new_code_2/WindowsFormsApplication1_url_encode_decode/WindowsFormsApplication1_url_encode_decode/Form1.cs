using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1_url_encode_decode
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str1 = "https://ja.wikipedia.org/wiki/和 製 英 語";

            richTextBox1.Text += "原字串(a)\t\t" + str1 + "\n";
            richTextBox1.Text += "原字串空白轉nbsp(b)\t" + str1.SpaceToNbsp() + "\n";

            string str2 = str1.UrlEncode();

            richTextBox1.Text += "原字串特殊符號編碼(c)\t" + str2 + "\n";

            richTextBox1.Text += "(c)再解碼\t\t" + str2.UrlDecode() + "\n";

            richTextBox1.Text += "(b)目前無法解碼\n";
            richTextBox1.Text += "\n";




        }
    }
}
