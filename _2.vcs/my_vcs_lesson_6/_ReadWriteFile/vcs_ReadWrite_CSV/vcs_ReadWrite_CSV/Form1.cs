using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FILE

namespace vcs_ReadWrite_CSV
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            MyList.Clear();
        }

        //二維List for string
        List<string[]> MyList = new List<string[]>();

        private void button1_Click(object sender, EventArgs e)
        {

            MyList.Add(new string[] { "data111", "data222", DateTime.Now.ToString() });
            MyList.Add(new string[] { "data333", "data444", DateTime.Now.ToString() });
            MyList.Add(new string[] { "data555", "data666", DateTime.Now.ToString() });
            richTextBox1.Text += "添加項目, 目前List共有 " + MyList.Count.ToString() + " 個項目\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (MyList.Count > 0)
            {
                richTextBox1.Text += "目前List共有 " + MyList.Count.ToString() + " 個項目, 分別是\n";
                int i;
                for (i = 0; i < MyList.Count; i++)
                {
                    richTextBox1.Text += "MyList[" + i.ToString() + "][0] = " + MyList[i][0].ToString() +
                        " MyList[" + i.ToString() + "][1] = " + MyList[i][1].ToString() +
                        " MyList[" + i.ToString() + "][2] = " + MyList[i][2].ToString() + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "目前List沒有項目\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\csv_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".csv";
            //StreamWriter sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.GetEncoding("UTF-8"));    //指名編碼格式
            StreamWriter sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.UTF8);    //指名編碼格式

            int i;
            string content = "";

            content += "第一欄" + "," + "第二欄" + "," + "時間" + "\n";
            for (i = 0; i < MyList.Count; i++)
            {
                richTextBox1.Text += "MyList[" + i.ToString() + "][0] = " + MyList[i][0].ToString() +
                    " MyList[" + i.ToString() + "][1] = " + MyList[i][1].ToString() +
                    " MyList[" + i.ToString() + "][2] = " + MyList[i][2].ToString() + "\n";
                content += MyList[i][0].ToString() + "," + MyList[i][1].ToString() + "," + MyList[i][2].ToString() + "\n";
            }

            sw.WriteLine(content);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            int len = 0;
            string filename = "C:\\______test_files\\__RW\\_csv\\成績檔.csv";

            Encoding enc = Encoding.GetEncoding("big5"); //設定檔案的編碼
            string[] readText = System.IO.File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案
            foreach (string s in readText)
            {
                //只打印每行資料
                //richTextBox1.Text += s + "\r\n";

                //切割資料後印出
                string[] ss = s.Split(',');
                len = ss.Length;
                for (i = 0; i < len; i++)
                {
                    //richTextBox1.Text += ss[0] + "  " + ss[1] + "  " + ss[2] + "  " + ss[3] + "  " + ss[4] + "\r\n";
                    richTextBox1.Text += ss[i];
                    if (i != (len - 1))
                        richTextBox1.Text += "  ";
                    else
                        richTextBox1.Text += "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            MyList.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int k = 0;
            string filename = "C:\\______test_files\\__RW\\_csv\\F0035CH1.CSV";

            Encoding enc = Encoding.GetEncoding("big5"); //設定檔案的編碼
            string[] readText = System.IO.File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案
            foreach (string s in readText)
            {
                //只打印每行資料
                //richTextBox1.Text += s + "\r\n";

                //切割資料後印出
                string[] ss = s.Split(',');

                richTextBox1.Text += "---" + ss[3] + "---" + ss[4] + "---" + "\r\n";

                k++;
                if (k == 100)
                    break;

            }

        }

    }
}
