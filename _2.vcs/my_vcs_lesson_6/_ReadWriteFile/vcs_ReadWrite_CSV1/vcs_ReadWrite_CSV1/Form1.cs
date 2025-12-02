using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FILE
using System.Drawing.Drawing2D; //for Matrix
using System.Collections;   //for ArrayList
using System.Diagnostics;   //for Debug

//using System.Text.RegularExpressions;

//參考/加入參考/.NET/Microsoft.Office.Interop.Excel
//方案總管 Microsoft.Office.Interop.Excel 右鍵/將內嵌Interop型別改為False

using Excel = Microsoft.Office.Interop.Excel;

// Data from https://covidtracking.com/api

namespace vcs_ReadWrite_CSV1
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
            show_item_location();

            MyList.Clear();

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            button40.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            pictureBox1.Size = new Size(500, 200);
            pictureBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 430);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 210);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1560, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立

            MyList.Add(new string[] { "data111", "data222", DateTime.Now.ToString() });
            MyList.Add(new string[] { "data333", "data444", DateTime.Now.ToString() });
            MyList.Add(new string[] { "data555", "data666", DateTime.Now.ToString() });
            richTextBox1.Text += "添加項目, 目前List共有 " + MyList.Count.ToString() + " 個項目\n";

            //顯示

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

        private void button1_Click(object sender, EventArgs e)
        {
            //List匯出到CSV檔
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

        private void button2_Click(object sender, EventArgs e)
        {
            //製作CSV檔

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

        private void button3_Click(object sender, EventArgs e)
        {
            //讀取CSV檔1_成績單

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_成績檔.csv";

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

        private const int LENGTH = 500;
        private const int PICTURE_WIDTH = 500;
        private const int PICTURE_HEIGHT = 500;

        private void button4_Click(object sender, EventArgs e)
        {
            //讀取CSV檔2_示波器

            //int k = 0;
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_F0035CH1.CSV";

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

        private void button5_Click(object sender, EventArgs e)
        {
            //讀取CSV檔3_火車站
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_station.csv";

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

        private void button6_Click(object sender, EventArgs e)
        {
            MyList.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //讀取CSV檔至DataTable 1
            richTextBox1.Text += "讀取CSV檔至DataTable 1 有標題\n";
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_成績檔_有標題.csv"; //cvs文件路徑
            DataTable dt = export_csv_to_dataTable(filename, true);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //讀取CSV檔至DataTable 2
            richTextBox1.Text += "讀取CSV檔至DataTable 2 無標題\n";
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_成績檔.csv"; //cvs文件路徑
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



        private void button9_Click(object sender, EventArgs e)
        {
            //讀取CSV檔

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_data.csv";

            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案 " + filename + " 不存在，離開。\n";
                return;
            }

            // Get the data.
            string[,] values = LoadCsv2(filename);
            int num_rows = values.GetUpperBound(0) + 1;
            int num_cols = values.GetUpperBound(1) + 1;

            richTextBox1.Text += "共有 " + num_cols.ToString() + " 欄(column)資料\n";
            richTextBox1.Text += "共有 " + num_rows.ToString() + " 列(row)資料\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            richTextBox1.Text += "欄名 : ";
            for (int c = 0; c < num_cols; c++)
            {
                richTextBox1.Text += values[0, c];

                if (c != (num_cols - 1))
                    richTextBox1.Text += "\t";
            }
            richTextBox1.Text += "\n------------------------------------------------------------\n";  // 60個

            for (int r = 1; r < num_rows; r++)
            {
                for (int c = 0; c < num_cols; c++)
                {
                    richTextBox1.Text += values[r, c];

                    if (c != (num_cols - 1))
                        richTextBox1.Text += "\t";
                }
                richTextBox1.Text += "\n------------------------------\n";  // 30個
            }

        }

        // Load a CSV file into an array of rows and columns.
        // Assume there may be blank lines but every line has
        // the same number of fields.
        private string[,] LoadCsv2(string filename)
        {
            // Get the file's text.
            string whole_file = File.ReadAllText(filename);

            // Split into lines.
            whole_file = whole_file.Replace('\n', '\r');
            string[] lines = whole_file.Split(new char[] { '\r' },
                StringSplitOptions.RemoveEmptyEntries);

            // See how many rows and columns there are.
            int num_rows = lines.Length;
            int num_cols = lines[0].Split(',').Length;

            // Allocate the data array.
            string[,] values = new string[num_rows, num_cols];

            // Load the array.
            for (int r = 0; r < num_rows; r++)
            {
                string[] line_r = lines[r].Split(',');
                for (int c = 0; c < num_cols; c++)
                {
                    values[r, c] = line_r[c];
                }
            }

            // Return the values.
            return values;
        }

        object[,] csv_data;

        private int colDate = 1;
        private int colState = 2;
        private int colPositive = 3;
        private int colNegative = 4;
        private int colPending = 5;
        private int colHospitalizedNow = 6;
        private int colHospitalizedTotal = 7;
        private int colIcuNow = 8;
        private int colIcuTotal = 9;
        private int colVentNow = 10;
        private int colVentTotal = 11;
        private int colRecovered = 12;
        private int colDeaths = 17;
        private int colPositiveIncrease = 25;
        private int colHospitalizedIncrease = 24;
        private int colDeathsIncrease = 23;

        private void FindColumns(object[,] fields)
        {
            colDate = FindColumn(fields, "date");
            colState = FindColumn(fields, "state");
            colPositive = FindColumn(fields, "positive");
            colNegative = FindColumn(fields, "negative");
            colPending = FindColumn(fields, "pending");
            colHospitalizedNow = FindColumn(fields, "hospitalizedCurrently");
            colHospitalizedTotal = FindColumn(fields, "hospitalizedCumulative");
            colIcuNow = FindColumn(fields, "inIcuCurrently");
            colIcuTotal = FindColumn(fields, "inIcuCumulative");
            colVentNow = FindColumn(fields, "onVentilatorCurrently");
            colVentTotal = FindColumn(fields, "onVentilatorCumulative");
            colRecovered = FindColumn(fields, "recovered");
            colDeaths = FindColumn(fields, "death");
            colPositiveIncrease = FindColumn(fields, "positiveIncrease");
            colHospitalizedIncrease = FindColumn(fields, "hospitalizedIncrease");
            colDeathsIncrease = FindColumn(fields, "deathIncrease");
        }

        // See which column contains the indicated column header.
        private int FindColumn(object[,] fields, string header)
        {
            for (int i = fields.GetLowerBound(1); i <= fields.GetUpperBound(1); i++)
            {
                if (fields[1, i].ToString().ToLower() == header.ToLower())
                    return i;
            }
            throw new Exception("Cannot find column " + header);
        }

        private object[,] LoadData(string filename)
        {
            // Read the file.
            object[,] fields = LoadCsv(filename);
            return fields;
        }

        // Return a value from the CSV file.
        private int ParseValue(object value)
        {
            if (value == null) return 0;

            int result;
            if (int.TryParse(value.ToString(), out result))
                return result;
            return 0;
        }

        // Load a CSV file into a 1-based array.
        private object[,] LoadCsv(string filename)
        {
            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            //excel_app.Visible = true;

            // Open the workbook read-only.
            //filename = Application.StartupPath + "\\" + filename;
            Excel.Workbook workbook = excel_app.Workbooks.Open(
                filename,
                Type.Missing, true, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing, Type.Missing, Type.Missing,
                Type.Missing, Type.Missing);

            // Get the first worksheet.
            Excel.Worksheet sheet = (Excel.Worksheet)workbook.Sheets[1];

            // Get the used range.
            Excel.Range used_range = sheet.UsedRange;

            // Get the sheet's values.
            object[,] values = (object[,])used_range.Value2;

            // Close the workbook without saving changes.
            workbook.Close(false, Type.Missing, Type.Missing);

            // Close the Excel server.
            excel_app.Quit();

            return values;
        }


        private void button10_Click(object sender, EventArgs e)
        {
            //透過EXCEL讀取CSV檔
            //Load CSV
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_state_data.csv";

            //filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_成績檔.csv";

            richTextBox1.Text += "filename = " + filename + "\n";

            csv_data = LoadData(filename);
        }

        void ShowData(object[,] fields)
        {
            if (fields == null)
            {
                richTextBox1.Text += "無資料\n";
                return;
            }
            else
                richTextBox1.Text += "資料OK\n";

            int i;
            int j;
            int column_st = fields.GetLowerBound(1);
            int column_sp = fields.GetUpperBound(1);
            int num_column = column_sp - column_st + 1;
            int num_row = fields.GetUpperBound(0);

            richTextBox1.Text += "共有 " + num_column.ToString() + " 欄(column)資料\n";
            richTextBox1.Text += "共有 " + num_row.ToString() + " 列(row)資料\n";

            for (i = fields.GetLowerBound(1); i <= fields.GetUpperBound(1); i++)
            {
                richTextBox1.Text += "第一列 第 " + i.ToString() + " 欄 : " + fields[1, i].ToString() + "\n";
            }

            if (num_row > 10)
                num_row = 10;
            for (i = 1; i <= num_row; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (j = column_st; j <= column_sp; j++)
                {
                    if (fields[i, j] == null)
                        richTextBox1.Text += "N.A.";
                    else
                        richTextBox1.Text += fields[i, j].ToString();
                    if (j < column_sp)
                        richTextBox1.Text += "\t";
                }
                richTextBox1.Text += "\n";
            }
            //FindColumns(fields);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //Show CSV
            ShowData(csv_data);
        }

        // Structure to hold price data.
        private struct PriceData
        {
            public DateTime Date;
            public float Price;
            public PriceData(DateTime new_Date, float new_Price)
            {
                Date = new_Date;
                Price = new_Price;
            }
        };

        private void DrawGraph()
        {
            this.Cursor = Cursors.WaitCursor;

            // Load the data.
            List<PriceData> price_data = GetDjiPrices();

            // Graph it.
            DrawGraph(price_data);

            this.Cursor = Cursors.Default;
        }

        // Get the historical prices.
        private List<PriceData> GetDjiPrices()
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\DjiPrices.csv";

            string[] lines = File.ReadAllLines(filename);

            // See which header fields contains Date and Adj Close.
            string[] fields = lines[0].Split(',');
            int date_field = -1, close_field = -1;
            for (int i = 0; i < fields.Length; i++)
            {
                if (fields[i].ToLower() == "adj close")
                    close_field = i;
                else if (fields[i].ToLower() == "date")
                    date_field = i;
            }

            // Process the lines, skipping the header.
            List<PriceData> price_data = new List<PriceData>();
            for (int i = 1; i < lines.Length; i++)
            {
                fields = lines[i].Split(',');
                price_data.Add(new PriceData(
                    DateTime.Parse(fields[date_field]),
                    float.Parse(fields[close_field])));
            }

            // Reverse so the data is in historical order.
            price_data.Reverse();
            return price_data;
        }

        // Draw the graph.
        private void DrawGraph(List<PriceData> price_data)
        {
            // Make the bitmap.
            Bitmap bm = new Bitmap(
                pictureBox1.ClientSize.Width,
                pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Get the largest price.
                var max_query = from PriceData data in price_data select data.Price;
                float max_price = max_query.Max() + 500;

                // Scale and translate the graph.
                float scale_x = pictureBox1.ClientSize.Width / (float)price_data.Count;
                float scale_y = -pictureBox1.ClientSize.Height / max_price;
                gr.ScaleTransform(scale_x, scale_y);
                gr.TranslateTransform(
                    0,
                    pictureBox1.ClientSize.Height,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                using (Pen thin_pen = new Pen(Color.Gray, 0))
                {
                    // Draw the horizontal grid lines.
                    for (int y = 0; y <= max_price; y += 1000)
                    {
                        // Draw the line.
                        gr.DrawLine(thin_pen, 0, y, price_data.Count, y);

                        // Draw the value.
                        if (y > 0)
                            DrawTextAt(gr, y.ToString("C"), 10, y, Color.Blue,
                                StringAlignment.Near, StringAlignment.Far);
                    }

                    // Draw the vertical grid lines.
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int last_year = 0;
                        for (int i = 0; i < price_data.Count; i++)
                        {
                            // See if this is the start of a new year.
                            if (price_data[i].Date.Year > last_year)
                            {
                                last_year = price_data[i].Date.Year;

                                // Draw a line for the year.
                                gr.DrawLine(thin_pen, i, 0, i, 750);

                                // Draw the year number.
                                DrawTextAt(gr, last_year.ToString(), i, 0, Color.Blue,
                                    StringAlignment.Center, StringAlignment.Far);
                            }
                        }
                    }
                }

                // Draw the prices. Make the data points.
                PointF[] points = new PointF[price_data.Count];
                for (int i = 0; i < price_data.Count; i++)
                {
                    points[i] = new PointF(i, price_data[i].Price);
                }

                // Draw the points.
                using (Pen thin_pen = new Pen(Color.Black, 0))
                {
                    gr.DrawLines(thin_pen, points);
                }
            }

            // Display the result.
            pictureBox1.Image = bm;
        }

        // Draw the text at the specified location.
        private void DrawTextAt(Graphics gr, string txt, float x, float y, Color clr, StringAlignment alignment, StringAlignment line_alignment)
        {
            // See where the point is in PictureBox coordinates.
            Matrix old_transformation = gr.Transform;
            PointF[] pt = { new PointF(x, y) };
            gr.Transform.TransformPoints(pt);

            // Reset the transformation.
            gr.ResetTransform();

            // Draw the text.
            using (Font small_font = new Font("Arial", 8))
            {
                using (SolidBrush br = new SolidBrush(clr))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = alignment;
                        string_format.LineAlignment = line_alignment;
                        gr.DrawString(txt, small_font, br, pt[0].X, pt[0].Y, string_format);
                    }
                }
            }

            // Restore the original transformation.
            gr.Transform = old_transformation;
        }

        // The historical prices.
        private List<PriceData> Prices;

        // Investment information.
        private List<PointF[]> Investments;
        private List<string> InvestmentNames;
        private List<Color> InvestmentColors;
        private const float InitialInvestment = 4000;   // The money we start with.
        private const float BaseInterestRate = 0.01f;   // Interest rate for uninvested money.

        private void DrawGraph2()
        {
            this.Cursor = Cursors.WaitCursor;

            // Graph it.
            DrawGraph2(Prices);

            this.Cursor = Cursors.Default;
        }

        // Draw the graph.
        private void DrawGraph2(List<PriceData> price_data)
        {
            // Make the bitmap.
            Bitmap bm = new Bitmap(
                pictureBox1.ClientSize.Width,
                pictureBox1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Get the largest price.
                var max_query = from PriceData data in price_data select data.Price;
                float max_price = max_query.Max() + 500;
                for (int i = 0; i < Investments.Count; i++)
                {
                    var test_query = from PointF pt in Investments[i] select pt.Y;
                    float test_max = test_query.Max() + 500;
                    if (max_price < test_max) max_price = test_max;
                }


                // Scale and translate the graph.
                float scale_x = pictureBox1.ClientSize.Width / (float)price_data.Count;
                float scale_y = -pictureBox1.ClientSize.Height / max_price;
                gr.ScaleTransform(scale_x, scale_y);
                gr.TranslateTransform(
                    0,
                    pictureBox1.ClientSize.Height,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                using (Pen thin_pen = new Pen(Color.Gray, 0))
                {
                    // Draw the horizontal grid lines.
                    for (int y = 0; y <= max_price; y += 1000)
                    {
                        // Draw the line.
                        gr.DrawLine(thin_pen, 0, y, price_data.Count, y);

                        // Draw the value.
                        if (y > 0)
                            DrawTextAt(gr, y.ToString("C"), 10, y, Color.Blue,
                                StringAlignment.Near, StringAlignment.Far);
                    }

                    // Draw the vertical grid lines.
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        int last_year = 0;
                        for (int i = 0; i < price_data.Count; i++)
                        {
                            // See if this is the start of a new year.
                            if (price_data[i].Date.Year > last_year)
                            {
                                last_year = price_data[i].Date.Year;

                                // Draw a line for the year.
                                gr.DrawLine(thin_pen, i, 0, i, 750);

                                // Draw the year number.
                                DrawTextAt(gr, last_year.ToString(), i, 0, Color.Blue,
                                    StringAlignment.Center, StringAlignment.Far);
                            }
                        }
                    }
                }

                //// Draw the prices. Make the data points.
                //PointF[] points = new PointF[price_data.Count];
                //for (int i = 0; i < price_data.Count; i++)
                //{
                //    points[i] = new PointF(i, price_data[i].Price);
                //}

                //// Draw the points.
                //using (Pen thin_pen = new Pen(Color.Black, 0))
                //{
                //    gr.DrawLines(thin_pen, points);
                //}

                // Draw investments.
                float label_y = (int)(max_price / 1000 - 1) * 1000;
                using (Pen thin_pen = new Pen(Color.Red, 0))
                {
                    int num_periods = Investments[0].Length;
                    for (int i = 0; i < Investments.Count; i++)
                    {
                        // Draw the graph for this investment.
                        thin_pen.Color = InvestmentColors[i];
                        gr.DrawLines(thin_pen, Investments[i]);

                        // Draw the investment's name and return.
                        DrawTextAt(gr, InvestmentNames[i], 500,
                            label_y, InvestmentColors[i],
                            StringAlignment.Near, StringAlignment.Far);
                        float end_balance = Investments[i][num_periods - 1].Y;
                        float pct = 100 * (end_balance - InitialInvestment) / InitialInvestment;
                        DrawTextAt(gr, pct.ToString("0.00") + "%", 1700,
                            label_y, InvestmentColors[i],
                            StringAlignment.Near, StringAlignment.Far);
                        label_y -= 1000;
                    }
                }
            }

            // Display the result.
            pictureBox1.Image = bm;
        }

        // Make investments using different strategies.
        private void MakeInvestments()
        {
            // Make room for the results.
            int num_points = Prices.Count;
            Investments = new List<PointF[]>();
            InvestmentNames = new List<string>();
            InvestmentColors = new List<Color>();

            // Strategy: All in at the start.
            StrategyAllIn();

            // Strategy: Fixed interest.
            StrategyInterest(0.05f);

            // Strategy: Fixed amount per period.
            StrategyFixedPerPeriod(100);

            //// Strategy: $100 every time there is a streak of down periods in a row.
            //StrategyDownStreak(2, Color.Orange);

            // Strategy: $100 every time there is a streak of down periods in a row.
            StrategyDownStreak(3, Color.Blue);

            //// Strategy: $100 when down by a given percent.
            //StrategyDownPercent(0.002f, Color.Plum);

            // Strategy: $100 when down by a given percent.
            StrategyDownPercent(0.001f, Color.Purple);

            // Strategy: $100 when down by $10.
            StrategyDownAmount(10, 100, Color.Brown);

            //// Strategy: $100 every time there is a streak of up periods in a row.
            //StrategyUpStreak(2, Color.Orange);

            // Strategy: $100 every time there is a streak of up periods in a row.
            StrategyUpStreak(3, Color.Orange);

            // Make perfect guesses.
            StrategyPerfectGuess(100, Color.Black);
        }

        // Strategy: 5% interest.
        private void StrategyInterest(float interest_rate)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;

            InvestmentNames.Add(interest_rate * 100 + "% interest");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Gray);

            for (int i = 0; i < num_points; i++)
            {
                // If this is a new year, add interest.
                if (i > 0)
                {
                    if (Prices[i].Date.Year > Prices[i - 1].Date.Year)
                    {
                        money_left += money_left * interest_rate;
                    }
                }
                Investments[investment_num][i] = new PointF(i, money_left);
            }
        }

        // Strategy: All in at the start.
        private void StrategyAllIn()
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;

            InvestmentNames.Add("All In");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Red);
            investment_num = Investments.Count - 1;
            float shares = InitialInvestment / Prices[0].Price;
            for (int i = 0; i < num_points; i++)
            {
                Investments[investment_num][i] = new PointF(i, shares * Prices[i].Price);
            }
        }

        // Strategy: $10 per period.
        private void StrategyFixedPerPeriod(float amount)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " per period");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(Color.Green);
            investment_num = Investments.Count - 1;
            for (int i = 0; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);
                BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 every time there is a streak of down periods in a row.
        // The best number depends on the data. For this data, 3 periods works.
        // For data that doesn't include the big drops at the end, 2 works better.
        private void StrategyDownStreak(int num_down, Color clr)
        {
            const float investment_per_period = 100;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " per " + num_down + " down periods");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_down; i++)
            {
                AddBaseInterest(i, ref money_left);
                Investments[investment_num][i] = new PointF(i, money_left);
            }
            for (int i = num_down; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See if the last num_down periods were declines.
                bool all_down = true;
                for (int look_back = 0; look_back < num_down; look_back++)
                {
                    // See if this period was not a decline.
                    if (Prices[i - look_back].Price >= Prices[i - look_back - 1].Price)
                    {
                        all_down = false;
                    }
                }

                // If all periods were declines, invest.
                if (all_down)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 when down by a given percent.
        private void StrategyDownPercent(float target_down_percent, Color clr)
        {
            const float investment_per_period = 10;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " when down by " + target_down_percent * 100 + "%");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            Investments[investment_num][0] = new PointF(0, money_left);
            for (int i = 1; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                float percent_down = (Prices[i - 1].Price - Prices[i].Price) / Prices[i - 1].Price;
                if (percent_down > target_down_percent)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 when down by a given amount.
        private void StrategyDownAmount(float down_amount, float amount, Color clr)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " when down by $" + down_amount);
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            Investments[investment_num][0] = new PointF(0, money_left);
            for (int i = 1; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                float amount_down = Prices[i - 1].Price - Prices[i].Price;
                if (amount_down > down_amount)
                {
                    BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: $100 every time there is a streak of up periods in a row.
        private void StrategyUpStreak(int num_up, Color clr)
        {
            const float investment_per_period = 100;
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + investment_per_period + " per " + num_up + " up periods");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_up; i++)
            {
                AddBaseInterest(i, ref money_left);
                Investments[investment_num][i] = new PointF(i, money_left);
            }
            for (int i = num_up; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See if the last num_up periods were increases.
                bool all_up = true;
                for (int look_back = 0; look_back < num_up; look_back++)
                {
                    // See if this period was not an increase.
                    if (Prices[i - look_back].Price <= Prices[i - look_back - 1].Price)
                    {
                        all_up = false;
                    }
                }
                // If all periods were increases, invest.
                if (all_up)
                {
                    BuyShares(ref money_left, ref shares, investment_per_period, Prices[i].Price);
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // Strategy: Invest whenever the price is about to go up by more than the base interest rate.
        private void StrategyPerfectGuess(float amount, Color clr)
        {
            int investment_num = Investments.Count;
            int num_points = Prices.Count;
            float money_left = InitialInvestment;
            float shares = 0;

            InvestmentNames.Add("$" + amount + " if increase > " + BaseInterestRate * 100 + "%");
            Investments.Add(new PointF[num_points]);
            InvestmentColors.Add(clr);
            investment_num = Investments.Count - 1;
            shares = 0;
            money_left = InitialInvestment;
            for (int i = 0; i < num_points; i++)
            {
                AddBaseInterest(i, ref money_left);

                // See what the increase will be in the next period.
                if (i < num_points - 1)
                {
                    float increase_percent = (Prices[i + 1].Price - Prices[i].Price) / Prices[i].Price;
                    if (increase_percent > BaseInterestRate)
                    {
                        BuyShares(ref money_left, ref shares, amount, Prices[i].Price);
                    }
                }

                Investments[investment_num][i] = new PointF(i, money_left + shares * Prices[i].Price);
            }
        }

        // If it's a new year, add base interest.
        private void AddBaseInterest(int period_number, ref float money_left)
        {
            if (period_number > 0)
            {
                if (Prices[period_number].Date.Year > Prices[period_number - 1].Date.Year)
                {
                    money_left += money_left * BaseInterestRate;
                }
            }
        }

        // Buy shares.
        private void BuyShares(ref float money_left, ref float shares, float investment_per_period, float price)
        {
            if (money_left < investment_per_period)
            {
                shares += money_left / price;
                money_left = 0;
            }
            else
            {
                shares += investment_per_period / price;
                money_left -= investment_per_period;
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //讀取CSV檔, 將資料畫出來
            DrawGraph();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //讀取CSV檔, 將資料畫出來
            // Load the data.
            Prices = GetDjiPrices();

            // Make investments.
            MakeInvestments();

            DrawGraph2();
        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            /* tmp
            // Open the Add Reference dialog. On the COM tab,
            // add a reference to "Microsoft.Office.Interop.Excel"
            using Excel = Microsoft.Office.Interop.Excel;
            */

            //用Excel開啟.CSV檔
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_CSV_F0035CH1.CSV";

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";

            // Get the Excel application object.
            Excel.Application excel_app = new Excel.ApplicationClass();

            // Make Excel visible (optional).
            excel_app.Visible = true;

            // Open the file.
            excel_app.Workbooks.Open(
                filename,                   // Filename
                Type.Missing,
                Type.Missing,
                Excel.XlFileFormat.xlCSV,   // Format
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                ",",                        // Delimiter
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing,
                Type.Missing);

        }

        private void button21_Click(object sender, EventArgs e)
        {
            /*
            用C#寫的讀寫CSV文件，
            用C#寫的讀取CSV文件的源代碼
            CSV文件的格子中包含逗號，引號，換行等，都能輕松讀取，而且可以把數據轉化成DATATABLE格式
            */
            //讀取一CSV檔至DataTable
            //使用 class CsvStreamReader
        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button34_Click(object sender, EventArgs e)
        {

        }

        private void button35_Click(object sender, EventArgs e)
        {

        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void button37_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {

        }

        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        private void button45_Click(object sender, EventArgs e)
        {

        }

        private void button46_Click(object sender, EventArgs e)
        {

        }

        private void button47_Click(object sender, EventArgs e)
        {

        }

        private void button48_Click(object sender, EventArgs e)
        {

        }

        private void button49_Click(object sender, EventArgs e)
        {

        }
    }


    /// <summary>
    ///  <DL>
    ///  <DT><b>讀CSV文件類,讀取指定的CSV文件，可以導出DataTable</b></DT>
    ///   <DD>
    ///    <UL> 
    ///    </UL>
    ///   </DD>
    ///  </DL>
    ///  <Author>yangzhihong</Author>   
    ///  <CreateDate>2006/01/16</CreateDate>
    ///  <Company></Company>
    ///  <Version>1.0</Version>
    /// </summary>

    public class CsvStreamReader
    {
        private ArrayList rowAL;        //行鏈表,CSV文件的每一行就是一個鏈
        private string fileName;       //文件名

        private Encoding encoding;       //編碼

        public CsvStreamReader()
        {
            this.rowAL = new ArrayList();
            this.fileName = "";
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public CsvStreamReader(string fileName)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = Encoding.Default;
            LoadCsvFile();
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public CsvStreamReader(string fileName, Encoding encoding)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = encoding;
            LoadCsvFile();
        }

        /// <summary>
        /// 文件名,包括文件路徑
        /// </summary>
        public string FileName
        {
            set
            {
                this.fileName = value;
                LoadCsvFile();
            }
        }

        /// <summary>
        /// 文件編碼
        /// </summary>

        public Encoding FileEncoding
        {
            set
            {
                this.encoding = value;
            }
        }

        /// <summary>
        /// 獲取行數
        /// </summary>
        public int RowCount
        {
            get
            {
                return this.rowAL.Count;
            }
        }

        /// <summary>
        /// 獲取列數
        /// </summary>
        public int ColCount
        {
            get
            {
                int maxCol;

                maxCol = 0;
                for (int i = 0; i < this.rowAL.Count; i++)
                {
                    ArrayList colAL = (ArrayList)this.rowAL[i];

                    maxCol = (maxCol > colAL.Count) ? maxCol : colAL.Count;
                }

                return maxCol;
            }
        }


        /// <summary>
        /// 獲取某行某列的數據

        /// row:行,row = 1代表第一行

        /// col:列,col = 1代表第一列  
        /// </summary>
        public string this[int row, int col]
        {
            get
            {
                //數據有效性驗證

                CheckRowValid(row);
                CheckColValid(col);
                ArrayList colAL = (ArrayList)this.rowAL[row - 1];

                //如果請求列數據大於當前行的列時,返回空值

                if (colAL.Count < col)
                {
                    return "";
                }

                return colAL[col - 1].ToString();
            }
        }


        /// <summary>
        /// 根據最小行，最大行，最小列，最大列，來生成一個DataTable類型的數據

        /// 行等於1代表第一行

        /// 列等於1代表第一列

        /// maxrow: -1代表最大行
        /// maxcol: -1代表最大列
        /// </summary>
        public DataTable this[int minRow, int maxRow, int minCol, int maxCol]
        {
            get
            {
                //數據有效性驗證

                CheckRowValid(minRow);
                CheckMaxRowValid(maxRow);
                CheckColValid(minCol);
                CheckMaxColValid(maxCol);
                if (maxRow == -1)
                {
                    maxRow = RowCount;
                }
                if (maxCol == -1)
                {
                    maxCol = ColCount;
                }
                if (maxRow < minRow)
                {
                    throw new Exception("最大行數不能小於最小行數");
                }
                if (maxCol < minCol)
                {
                    throw new Exception("最大列數不能小於最小列數");
                }
                DataTable csvDT = new DataTable();
                int i;
                int col;
                int row;

                //增加列

                for (i = minCol; i <= maxCol; i++)
                {
                    csvDT.Columns.Add(i.ToString());
                }
                for (row = minRow; row <= maxRow; row++)
                {
                    DataRow csvDR = csvDT.NewRow();

                    i = 0;
                    for (col = minCol; col <= maxCol; col++)
                    {
                        csvDR[i] = this[row, col];
                        i++;
                    }
                    csvDT.Rows.Add(csvDR);
                }

                return csvDT;
            }
        }


        /// <summary>
        /// 檢查行數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckRowValid(int row)
        {
            if (row <= 0)
            {
                throw new Exception("行數不能小於0");
            }
            if (row > RowCount)
            {
                throw new Exception("沒有當前行的數據");
            }
        }

        /// <summary>
        /// 檢查最大行數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckMaxRowValid(int maxRow)
        {
            if (maxRow <= 0 && maxRow != -1)
            {
                throw new Exception("行數不能等於0或小於-1");
            }
            if (maxRow > RowCount)
            {
                throw new Exception("沒有當前行的數據");
            }
        }

        /// <summary>
        /// 檢查列數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckColValid(int col)
        {
            if (col <= 0)
            {
                throw new Exception("列數不能小於0");
            }
            if (col > ColCount)
            {
                throw new Exception("沒有當前列的數據");
            }
        }

        /// <summary>
        /// 檢查檢查最大列數是否是有效的

        /// </summary>
        /// <param name="col"></param>  
        private void CheckMaxColValid(int maxCol)
        {
            if (maxCol <= 0 && maxCol != -1)
            {
                throw new Exception("列數不能等於0或小於-1");
            }
            if (maxCol > ColCount)
            {
                throw new Exception("沒有當前列的數據");
            }
        }

        /// <summary>
        /// 載入CSV文件
        /// </summary>
        private void LoadCsvFile()
        {
            //對數據的有效性進行驗證

            if (this.fileName == null)
            {
                throw new Exception("請指定要載入的CSV文件名");
            }
            else if (!File.Exists(this.fileName))
            {
                throw new Exception("指定的CSV文件不存在");
            }
            else
            {
            }
            if (this.encoding == null)
            {
                this.encoding = Encoding.Default;
            }

            StreamReader sr = new StreamReader(this.fileName, this.encoding);
            string csvDataLine;

            csvDataLine = "";
            while (true)
            {
                string fileDataLine;

                fileDataLine = sr.ReadLine();
                if (fileDataLine == null)
                {
                    break;
                }
                if (csvDataLine == "")
                {
                    csvDataLine = fileDataLine;//GetDeleteQuotaDataLine(fileDataLine);
                }
                else
                {
                    csvDataLine += "/r/n" + fileDataLine;//GetDeleteQuotaDataLine(fileDataLine);
                }
                //如果包含偶數個引號，說明該行數據中出現回車符或包含逗號
                if (!IfOddQuota(csvDataLine))
                {
                    AddNewDataLine(csvDataLine);
                    csvDataLine = "";
                }
            }
            sr.Close();
            //數據行出現奇數個引號
            if (csvDataLine.Length > 0)
            {
                throw new Exception("CSV文件的格式有錯誤");
            }
        }

        /// <summary>
        /// 獲取兩個連續引號變成單個引號的數據行
        /// </summary>
        /// <param name="fileDataLine">文件數據行</param>
        /// <returns></returns>
        private string GetDeleteQuotaDataLine(string fileDataLine)
        {
            return fileDataLine.Replace("\"\"", "\"");
        }

        /// <summary>
        /// 判斷字符串是否包含奇數個引號
        /// </summary>
        /// <param name="dataLine">數據行</param>
        /// <returns>為奇數時，返回為真；否則返回為假</returns>
        private bool IfOddQuota(string dataLine)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = 0; i < dataLine.Length; i++)
            {
                if (dataLine[i] == '\"')
                {
                    quotaCount++;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 判斷是否以奇數個引號開始

        /// </summary>
        /// <param name="dataCell"></param>
        /// <returns></returns>
        private bool IfOddStartQuota(string dataCell)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = 0; i < dataCell.Length; i++)
            {
                if (dataCell[i] == '\"')
                {
                    quotaCount++;
                }
                else
                {
                    break;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 判斷是否以奇數個引號結尾
        /// </summary>
        /// <param name="dataCell"></param>
        /// <returns></returns>
        private bool IfOddEndQuota(string dataCell)
        {
            int quotaCount;
            bool oddQuota;

            quotaCount = 0;
            for (int i = dataCell.Length - 1; i >= 0; i--)
            {
                if (dataCell[i] == '\"')
                {
                    quotaCount++;
                }
                else
                {
                    break;
                }
            }

            oddQuota = false;
            if (quotaCount % 2 == 1)
            {
                oddQuota = true;
            }

            return oddQuota;
        }

        /// <summary>
        /// 加入新的數據行

        /// </summary>
        /// <param name="newDataLine">新的數據行</param>
        private void AddNewDataLine(string newDataLine)
        {
            Debug.WriteLine("NewLine:" + newDataLine);

            //return;

            ArrayList colAL = new ArrayList();
            string[] dataArray = newDataLine.Split(',');
            bool oddStartQuota;       //是否以奇數個引號開始

            string cellData;

            oddStartQuota = false;
            cellData = "";
            for (int i = 0; i < dataArray.Length; i++)
            {
                if (oddStartQuota)
                {
                    //因為前面用逗號分割,所以要加上逗號
                    cellData += "," + dataArray[i];
                    //是否以奇數個引號結尾
                    if (IfOddEndQuota(dataArray[i]))
                    {
                        colAL.Add(GetHandleData(cellData));
                        oddStartQuota = false;
                        continue;
                    }
                }
                else
                {
                    //是否以奇數個引號開始

                    if (IfOddStartQuota(dataArray[i]))
                    {
                        //是否以奇數個引號結尾,不能是一個雙引號,並且不是奇數個引號

                        if (IfOddEndQuota(dataArray[i]) && dataArray[i].Length > 2 && !IfOddQuota(dataArray[i]))
                        {
                            colAL.Add(GetHandleData(dataArray[i]));
                            oddStartQuota = false;
                            continue;
                        }
                        else
                        {

                            oddStartQuota = true;
                            cellData = dataArray[i];
                            continue;
                        }
                    }
                    else
                    {
                        colAL.Add(GetHandleData(dataArray[i]));
                    }
                }
            }
            if (oddStartQuota)
            {
                throw new Exception("數據格式有問題");
            }
            this.rowAL.Add(colAL);
        }


        /// <summary>
        /// 去掉格子的首尾引號，把雙引號變成單引號

        /// </summary>
        /// <param name="fileCellData"></param>
        /// <returns></returns>
        private string GetHandleData(string fileCellData)
        {
            if (fileCellData == "")
            {
                return "";
            }
            if (IfOddStartQuota(fileCellData))
            {
                if (IfOddEndQuota(fileCellData))
                {
                    return fileCellData.Substring(1, fileCellData.Length - 2).Replace("\"\"", "\""); //去掉首尾引號，然後把雙引號變成單引號
                }
                else
                {
                    throw new Exception("數據引號無法匹配" + fileCellData);
                }
            }
            else
            {
                //考慮形如""    """"      """"""   
                if (fileCellData.Length > 2 && fileCellData[0] == '\"')
                {
                    fileCellData = fileCellData.Substring(1, fileCellData.Length - 2).Replace("\"\"", "\""); //去掉首尾引號，然後把雙引號變成單引號
                }
            }

            return fileCellData;
        }
    }

    /// <summary>
    ///  <DL>
    ///  <DT><b>寫CSV文件類,首先給CSV文件賦值,最後通過Save方法進行保存操作</b></DT>
    ///   <DD>
    ///    <UL> 
    ///    </UL>
    ///   </DD>
    ///  </DL>
    ///  <Author>yangzhihong</Author>   
    ///  <CreateDate>2006/01/16</CreateDate>
    ///  <Company></Company>
    ///  <Version>1.0</Version>
    /// </summary>
    public class CsvStreamWriter
    {
        private ArrayList rowAL;        //行鏈表,CSV文件的每一行就是一個鏈
        private string fileName;       //文件名
        private Encoding encoding;       //編碼

        public CsvStreamWriter()
        {
            this.rowAL = new ArrayList();
            this.fileName = "";
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public CsvStreamWriter(string fileName)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = Encoding.Default;
        }

        /// <summary>
        ///
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public CsvStreamWriter(string fileName, Encoding encoding)
        {
            this.rowAL = new ArrayList();
            this.fileName = fileName;
            this.encoding = encoding;
        }

        /// <summary>
        /// row:行,row = 1代表第一行
        /// col:列,col = 1代表第一列
        /// </summary>
        public string this[int row, int col]
        {
            set
            {
                //對行進行判斷
                if (row <= 0)
                {
                    throw new Exception("行數不能小於0");
                }
                else if (row > this.rowAL.Count) //如果當前列鏈的行數不夠，要補齊
                {
                    for (int i = this.rowAL.Count + 1; i <= row; i++)
                    {
                        this.rowAL.Add(new ArrayList());
                    }
                }
                else
                {
                }
                //對列進行判斷
                if (col <= 0)
                {
                    throw new Exception("列數不能小於0");
                }
                else
                {
                    ArrayList colTempAL = (ArrayList)this.rowAL[row - 1];

                    //擴大長度
                    if (col > colTempAL.Count)
                    {
                        for (int i = colTempAL.Count; i <= col; i++)
                        {
                            colTempAL.Add("");
                        }
                    }
                    this.rowAL[row - 1] = colTempAL;
                }
                //賦值
                ArrayList colAL = (ArrayList)this.rowAL[row - 1];

                colAL[col - 1] = value;
                this.rowAL[row - 1] = colAL;
            }
        }


        /// <summary>
        /// 文件名,包括文件路徑
        /// </summary>
        public string FileName
        {
            set
            {
                this.fileName = value;
            }
        }

        /// <summary>
        /// 文件編碼
        /// </summary>

        public Encoding FileEncoding
        {
            set
            {
                this.encoding = value;
            }
        }

        /// <summary>
        /// 獲取當前最大行
        /// </summary>
        public int CurMaxRow
        {
            get
            {
                return this.rowAL.Count;
            }
        }

        /// <summary>
        /// 獲取最大列
        /// </summary>
        public int CurMaxCol
        {
            get
            {
                int maxCol;

                maxCol = 0;
                for (int i = 0; i < this.rowAL.Count; i++)
                {
                    ArrayList colAL = (ArrayList)this.rowAL[i];

                    maxCol = (maxCol > colAL.Count) ? maxCol : colAL.Count;
                }

                return maxCol;
            }
        }

        /// <summary>
        /// 添加表數據到CSV文件中
        /// </summary>
        /// <param name="dataDT">表數據</param>
        /// <param name="beginCol">從第幾列開始,beginCol = 1代表第一列</param>
        public void AddData(DataTable dataDT, int beginCol)
        {
            if (dataDT == null)
            {
                throw new Exception("需要添加的表數據為空");
            }
            int curMaxRow;

            curMaxRow = this.rowAL.Count;
            for (int i = 0; i < dataDT.Rows.Count; i++)
            {
                for (int j = 0; j < dataDT.Columns.Count; j++)
                {
                    this[curMaxRow + i + 1, beginCol + j] = dataDT.Rows[i][j].ToString();
                }
            }
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        public void Save()
        {
            //對數據的有效性進行判斷
            if (this.fileName == null)
            {
                throw new Exception("缺少文件名");
            }
            else if (File.Exists(this.fileName))
            {
                File.Delete(this.fileName);
            }
            if (this.encoding == null)
            {
                this.encoding = Encoding.Default;
            }
            System.IO.StreamWriter sw = new StreamWriter(this.fileName, false, this.encoding);

            for (int i = 0; i < this.rowAL.Count; i++)
            {
                sw.WriteLine(ConvertToSaveLine((ArrayList)this.rowAL[i]));
            }

            sw.Close();
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        public void Save(string fileName)
        {
            this.fileName = fileName;
            Save();
        }

        /// <summary>
        /// 保存數據,如果當前硬盤中已經存在文件名一樣的文件，將會覆蓋
        /// </summary>
        /// <param name="fileName">文件名,包括文件路徑</param>
        /// <param name="encoding">文件編碼</param>
        public void Save(string fileName, Encoding encoding)
        {
            this.fileName = fileName;
            this.encoding = encoding;
            Save();
        }


        /// <summary>
        /// 轉換成保存行
        /// </summary>
        /// <param name="colAL">一行</param>
        /// <returns></returns>
        private string ConvertToSaveLine(ArrayList colAL)
        {
            string saveLine;

            saveLine = "";
            for (int i = 0; i < colAL.Count; i++)
            {
                saveLine += ConvertToSaveCell(colAL[i].ToString());
                //格子間以逗號分割
                if (i < colAL.Count - 1)
                {
                    saveLine += ",";
                }
            }

            return saveLine;
        }

        /// <summary>
        /// 字符串轉換成CSV中的格子
        /// 雙引號轉換成兩個雙引號，然後首尾各加一個雙引號
        /// 這樣就不需要考慮逗號及換行的問題
        /// </summary>
        /// <param name="cell">格子內容</param>
        /// <returns></returns>
        private string ConvertToSaveCell(string cell)
        {
            cell = cell.Replace("\"", "\"\"");

            return "\"" + cell + "\"";
        }
    }
}





//6060
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


/*  可搬出

*/




