using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO; // for StreamWriter, StreamReader

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            StreamWriter outFile = new StreamWriter("myText.txt"); // true 是資料可附加至檔案
            // StreamWriter outFile = new StreamWriter("myText.txt", true); // true 是資料可附加至檔案
            outFile.WriteLine("白日依山盡"); // 寫入一行
            outFile.WriteLine("黃河入海流");
            outFile.WriteLine("欲窮千里目");
            outFile.WriteLine("更上一層樓");
            outFile.Close(); // 關閉檔案
        }

        private void button2_Click(object sender, EventArgs e)
        {
            StreamReader inFile = new StreamReader("myText.txt"); // 開啟檔案
            /*
            String str = inFile.ReadLine(); // 讀出一行

            while (str != null)
            {
                if (textBox1.Text != "")
                    textBox1.Text = textBox1.Text + Environment.NewLine;  // "\r\n"

                textBox1.Text = textBox1.Text + str;
                str = inFile.ReadLine();
            }
             * */

            textBox1.Text = ""; // 文字方塊 先清空
            string str;  // 宣告字串變數
            while (inFile.Peek() != -1) // 傳回下一個可供使用的字元，但不消耗它
            {
                str = inFile.ReadLine(); // 讀出一行 到字串 str

                if (textBox1.Text != "") // 如果不是第一行 就加入 新行字串
                    textBox1.Text = textBox1.Text + Environment.NewLine;  // "\r\n"

                textBox1.Text = textBox1.Text + str;
            }

            inFile.Close(); // 關閉檔案
        }
    }
}