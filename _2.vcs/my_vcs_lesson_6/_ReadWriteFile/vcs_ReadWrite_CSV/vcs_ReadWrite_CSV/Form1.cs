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
            //一維字串陣列
            string[] readText = System.IO.File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案

            //資料處理
            string[] name = new string[readText.Length];//宣告一個1維字串陣列，來儲存所有的姓名
            //double[][] allData = new double[readText.Length][]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            double[,] allData = new double[readText.Length, 5]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            //Point[][] colonPoints = new Point[2][];
            int line = 0; //表第幾行(第幾列，每一列為一個學生的資料)

            foreach (string s in readText)
            {
                //一, 未分割資料, 只打印每行資料
                //richTextBox1.Text += s + "\r\n";

                //二, 分割資料, 分割資料後印出
                /*
                string[] ss = s.Split(',');         //將一列的資料，以逗號的方式進行資料切割，並將資料放入一個字串陣列
                len = ss.Length;
                for (i = 0; i < len; i++)
                {
                    //richTextBox1.Text += ss[0] + "  " + ss[1] + "  " + ss[2] + "  " + ss[3] + "  " + ss[4] + "\r\n";
                    //資料分別在取出的字串陣列裏，姓名->ss[0], 成績1->ss[1], 成績2->ss[2], 成績3->ss[3], 成績4->ss[4]
                    richTextBox1.Text += ss[i];
                    if (i != (len - 1))
                        richTextBox1.Text += "  ";
                    else
                        richTextBox1.Text += "\n";
                }
                */

                //三, 資料處理
                string[] ss = s.Split(','); //將一列的資料，以逗號的方式進行資料切割，並將資料放入一個字串陣列
                name[line] = ss[0]; //切出來的字串，第0個元素是姓名


                allData[line, 0] = double.Parse(ss[1]);
                allData[line, 1] = double.Parse(ss[2]);
                allData[line, 2] = double.Parse(ss[3]);
                allData[line, 3] = double.Parse(ss[4]);
                allData[line, 4] = allData[line, 0] + allData[line, 1] + allData[line, 2] + allData[line, 3]; //將每個人的成績加起來放在最後一欄

                richTextBox1.Text += name[line] + "  " + allData[line, 0] + "  " + allData[line, 1] + "  " + allData[line, 2] + "  " + allData[line, 3] + "  " + allData[line, 4] + "\r\n";
                line++; //進行下一筆資料的處理
                //資料分別在取出的字串陣列裏，姓名->ss[0], 成績1->ss[1], 成績2->ss[2], 成績3->ss[3], 成績4->ss[4]
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

        private const int PICTURE_WIDTH = 300;
        private const int PICTURE_HEIGHT = 300;

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


            // 實例化圖片方塊
            PictureBox pbx = new PictureBox();

            pbx.Size = new Size(PICTURE_WIDTH, PICTURE_HEIGHT);

            // 設定圖片方塊參數
            pbx.Left = 10;
            pbx.Top = 10;
            //pbx.Width = 300;
            //pbx.Height = 300;
            pbx.BackColor = Color.Pink;
            pbx.SizeMode = PictureBoxSizeMode.Zoom;
            pbx.Location = new Point(this.Width - 350, 0);
            // 將圖片方塊加入表單
            this.Controls.Add(pbx);
        }

    }
}
