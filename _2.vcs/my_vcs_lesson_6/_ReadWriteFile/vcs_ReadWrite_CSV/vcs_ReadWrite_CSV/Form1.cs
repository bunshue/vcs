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
        //二維List for string
        List<string[]> MyList = new List<string[]>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MyList.Clear();
        }

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
            string filename = "C:\\______test_files1\\__RW\\_csv\\vcs_ReadWrite_CSV_成績檔.csv";

            Encoding enc = Encoding.GetEncoding("big5"); //設定檔案的編碼
            //一維字串陣列
            string[] readText = File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案

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

                //二, 分割資料, 分割資料後印出 a
                /*
                string[] ss = s.Split(',');         //將一列的資料，以逗號的方式進行資料切割，並將資料放入一個字串陣列
                int len = ss.Length;
                int i;
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

                /*
                //二, 分割資料, 分割資料後印出 b
                var fields = s.Split(new char[] { ',' });
                foreach (var v in fields)
                {
                    richTextBox1.Text += v + "\t";
                }
                richTextBox1.Text += "\n";
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

        private const int LENGTH = 500;
        private const int PICTURE_WIDTH = 500;
        private const int PICTURE_HEIGHT = 500;

        private void button7_Click(object sender, EventArgs e)
        {
            //int k = 0;
            string filename = "C:\\______test_files1\\__RW\\_csv\\vcs_ReadWrite_CSV_F0035CH1.CSV";

            Encoding enc = Encoding.GetEncoding("big5"); //設定檔案的編碼
            string[] readText = File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案

            richTextBox1.Text += "len = " + readText.Length.ToString() + "\n";

            //資料處理
            //double[][] allData = new double[readText.Length][]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            double[,] allData = new double[readText.Length, 2]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            //Point[][] colonPoints = new Point[2][];
            int line = 0; //表第幾行(第幾列，每一列為一個學生的資料)

            foreach (string s in readText)
            {
                //只打印每行資料
                //richTextBox1.Text += s + "\r\n";

                /*
                //切割資料後印出
                string[] ss = s.Split(',');

                richTextBox1.Text += "---" + ss[3] + "---" + ss[4] + "---" + "\r\n";
                */

                //三, 資料處理

                //richTextBox1.Text += s + "\r\n";

                string[] ss = s.Split(','); //將一列的資料，以逗號的方式進行資料切割，並將資料放入一個字串陣列

                allData[line, 0] = double.Parse(ss[3]);
                allData[line, 1] = double.Parse(ss[4]);

                //richTextBox1.Text += allData[line, 0] + "  " + allData[line, 1] + "\r\n";
                line++; //進行下一筆資料的處理
                //資料分別在取出的字串陣列裏，姓名->ss[0], 成績1->ss[1], 成績2->ss[2], 成績3->ss[3], 成績4->ss[4]

                //k++;
                //if (k == LENGTH)
                //break;

            }


            // 實例化圖片方塊
            PictureBox pictureBox1 = new PictureBox();

            pictureBox1.Size = new Size(PICTURE_WIDTH, PICTURE_HEIGHT);

            // 設定圖片方塊參數
            pictureBox1.Left = 10;
            pictureBox1.Top = 10;
            //pictureBox1.Width = 300;
            //pictureBox1.Height = 300;
            pictureBox1.BackColor = Color.Pink;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Location = new Point(this.Width - 550, 0);
            // 將圖片方塊加入表單
            this.Controls.Add(pictureBox1);

            Point[] curvePoints = new Point[LENGTH];    //一維陣列內有 N 個Point

            int i;
            for (i = 0; i < LENGTH; i++)
            {
                curvePoints[i].X = i;
                curvePoints[i].Y = pictureBox1.Height - (int)allData[i * 4, 1] * 10 - 50;

                //curvePoints[i].X = i;
                //curvePoints[i].Y = i;

                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + h / 2);
            }


            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            p = new Pen(Color.Red, 3);
            sb = new SolidBrush(Color.Red);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);

            g.Clear(Color.Gray);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。


            // Draw curve to screen.
            g.DrawCurve(p, curvePoints); //畫曲線


            pictureBox1.Image = bitmap1;




        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\csv_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".csv";

            int aaa = 123;
            int bbb = 456;

            using (var stream = File.CreateText(filename))
            {
                string first = aaa.ToString();
                string second = bbb.ToString();
                string csv = string.Format("{0},{1}\n", first, second);
                //File.WriteAllText(filename, csv);
                stream.WriteLine(csv);
                richTextBox1.Text += "csv : " + csv + "\n";
            }
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files1\\__RW\\_csv\\vcs_ReadWrite_CSV_station.csv";

            Encoding enc = Encoding.GetEncoding("big5"); //設定檔案的編碼
            //一維字串陣列
            string[] readText = File.ReadAllLines(filename, enc); //以指定的編碼方式讀取檔案

            //資料處理
            string[] name = new string[readText.Length];//宣告一個1維字串陣列，來儲存所有的姓名
            //double[][] allData = new double[readText.Length][]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            double[,] allData = new double[readText.Length, 4]; //宣告一個2維double陣列，用來儲存所有的成績資料，第一維的大小是資料的列數(筆數)
            //Point[][] colonPoints = new Point[2][];
            //int line = 0; //表第幾行(第幾列，每一列為一個學生的資料)

            foreach (string s in readText)
            {
                //一, 未分割資料, 只打印每行資料
                richTextBox1.Text += s + "\r\n";

                //二, 分割資料, 分割資料後印出
                /*
                string[] ss = s.Split(',');         //將一列的資料，以逗號的方式進行資料切割，並將資料放入一個字串陣列
                int len = ss.Length;
                int i;
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

                /*
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
                */
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取CSV檔至DataTable 1 有標題\n";
            string filename = @"C:\______test_files\__RW\_csv\vcs_ReadWrite_CSV_成績檔_有標題.csv"; //cvs文件路徑
            DataTable dt = export_csv_to_dataTable(filename, true);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取CSV檔至DataTable 2 無標題\n";
            string filename = @"C:\______test_files\__RW\_csv\vcs_ReadWrite_CSV_成績檔.csv"; //cvs文件路徑
            DataTable dt = export_csv_to_dataTable(filename, false);
        }

        DataTable export_csv_to_dataTable(string filename, bool flag_csv_file_with_title)
        {
            int intColCount = 0;

            DataTable mydt = new DataTable("myTableName");
            DataColumn mydc;
            DataRow mydr;

            string strline;
            string[] aryline;


            StreamReader mysr = new StreamReader(filename, Encoding.Default);    //Windows預設，就是big5

            //因為csv檔沒有標題 所以要另外寫
            if (flag_csv_file_with_title == false)
            {
                mydc = new DataColumn("name");
                mydt.Columns.Add(mydc);
                mydc = new DataColumn("chi");
                mydt.Columns.Add(mydc);
                mydc = new DataColumn("eng");
                mydt.Columns.Add(mydc);
                mydc = new DataColumn("math");
                mydt.Columns.Add(mydc);
                mydc = new DataColumn("science");
                mydt.Columns.Add(mydc);
            }

            while ((strline = mysr.ReadLine()) != null)
            {
                aryline = strline.Split(new char[] { ',' });
                for (int i = 0; i < aryline.Length; i++)
                {
                    richTextBox1.Text += aryline[i] + "-";
                }
                richTextBox1.Text += "\n";


                //若csv檔的第一行是標題 直接把標題讀出來設定為每欄的名稱
                if (flag_csv_file_with_title == true)
                {
                    flag_csv_file_with_title = false;
                    intColCount = aryline.Length;
                    for (int i = 0; i < aryline.Length; i++)
                    {
                        mydc = new DataColumn(aryline[i]);
                        mydt.Columns.Add(mydc);
                    }
                }

                mydr = mydt.NewRow();
                for (int i = 0; i < intColCount; i++)
                {
                    mydr[i] = aryline[i];
                }
                mydt.Rows.Add(mydr);
            }


            richTextBox1.Text += "印出DataTable的內容\n";

            return mydt;
        }
    }
}

