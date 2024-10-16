using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for file read/write

using System.Collections; //匯入集合物件      for Hashtable

namespace vcs_test_all_02_Array
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
            x_st = 12;
            y_st = 12;
            dx = 210;
            dy = 48;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);

            button13.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 12);

            button26.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            tb_matrix.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            rtb_matrix.Location = new Point(x_st + dx * 2 + 140, y_st + dy * 10);

            button36.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button40.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button41.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button42.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button44.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button45.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 6 - 100, y_st + dy * 0);
            richTextBox1.Size = new Size(800, 900);

            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 15);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 17);


            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //二維陣列的宣告與使用
            int i, j;
            int[,] gray = new int[3, 8];    //Row = 3, Column = 8

            int ROW = gray.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = gray.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = gray.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "assign value\n";

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    gray[j, i] = i * 10 + j;
                }
            }

            richTextBox1.Text += "print value\n";
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    richTextBox1.Text += gray[j, i].ToString("D2") + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "二維陣列內容\n";
            PrintArray(gray);

            //richTextBox1.Text += "數學的(5,2)位置 要寫gray[2, 5] = " + gray[2, 5].ToString("D2") + "\n";
            richTextBox1.Text += "數學的(5,2)位置 要寫gray[2, 5] = " + gray[2, 5].ToString("D2") + "\n";


            /*
            //三維陣列 測試中
            int[,,] gray2 = new int[5, 3, 8];    //Row = 3, Column = 8

            richTextBox1.Text += "Rank = " + gray2.Rank.ToString() + "\n";

            richTextBox1.Text += "三維陣列內容\n";
            PrintArray(gray2);
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //獲取二維陣列的長度

            int[,] array2D;
            //使用 C# 中的 Array.GetLength() 函式獲取 2D 陣列的寬度和高度
            //使用 C# 中的 Array.GetUpperBound() 函式獲取二維陣列的寬度和高度
            array2D = new int[5, 10];
            Console.WriteLine(array2D.GetLength(0));	//5
            Console.WriteLine(array2D.GetLength(1));	//10

            //使用 C# 中的 Array.GetUpperBound() 函式獲取二維陣列的寬度和高度
            array2D = new int[5, 10];
            Console.WriteLine(array2D.GetUpperBound(0) + 1);	//5
            Console.WriteLine(array2D.GetUpperBound(1) + 1);	//10

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //計算二維陣列所有元素總和
            int[,] array = new int[,] { { 0, 11, 3, 45, 17 }, { 23, 41, 5, 8, 10 }, { 9, 21, 16, 84, 51 } };

            int Total = 0;
            foreach (int element in array)
            {
                Total += element;
            }
            richTextBox1.Text += "此二維陣列的各個元素總和為: " + Total.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //一維陣列用法：
            int[] A = new int[5];
            int[] B = new int[] { 1, 2, 3, 4, 5 };
            int[] C = { 1, 3, 5, 7, 9 };
            int[] myArray = new int[10];
            string[] studentName = new string[100];
            int[] a = new int[5] { 0, 1, 2, 3, 4 };
            Point[] pt = new Point[360];    //一維陣列內有360個Point

            //字串一維陣列
            String[] strings = { "This is a string.", "Hello!", "Nothing.", "Yes.", "randomize" };
            // print out the array of strings
            foreach (var s in strings)
            {
                richTextBox1.Text += "字串\t" + s + "\n";
            }

            richTextBox1.Text += "一維陣列的運算\n";
            int N = 12;
            int[] Values = new int[N];
            Random r = new Random();
            //Values = new int[NumValues];
            for (int i = 0; i < N; i++)
            {
                Values[i] = r.Next(0, 100);
            }

            richTextBox1.Text += "顯示內容\n";
            foreach (var v in Values)
            {
                richTextBox1.Text += v.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "個數 :\t" + Values.Count().ToString() + "\t陣列資料長度\n";
            richTextBox1.Text += "個數 :\t" + Values.Length.ToString() + "\t陣列資料長度\n";
            richTextBox1.Text += "總和 :\t" + Values.Sum().ToString() + "\n";
            richTextBox1.Text += "平均 :\t" + Values.Average().ToString() + "\n";
            richTextBox1.Text += "Max :\t" + Values.Max().ToString() + "\n";
            richTextBox1.Text += "Min :\t" + Values.Min().ToString() + "\n";
            richTextBox1.Text += "Rank :\t" + Values.Rank.ToString() + "\t陣列維度值\n";

            Array.Sort(Values);
            richTextBox1.Text += "排序後\n";
            foreach (var v in Values)
            {
                richTextBox1.Text += v.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            Array.Reverse(Values);
            richTextBox1.Text += "反相後\n";
            foreach (var v in Values)
            {
                richTextBox1.Text += v.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "不定長度一維字串陣列\n";
            string[] Product = new string[] { "火影忍者", "航海王",
 				"史瑞克4", "葉問2", "鋼鐵人2", "偷心大聖PS男", "阿凡達",
 				"半夜鬼上床", "第一次愛上你", "松藥局的兒子們", "老婆，給我飯" };
            richTextBox1.Text += "共有 " + Product.Length.ToString() + " 個項目, 分別是:\n";
            foreach (var s in Product)
            {
                richTextBox1.Text += s.ToString() + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //二維陣列用法：
            int[,] b = new int[2, 3];
            int[,] c = new int[2, 3] { { 1, 2, 3 }, { 4, 5, 6 } };
            int[,] D = new int[3, 3];
            int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[,] myArray = new int[2, 3] { { 1, 2, 3 }, { 4, 5, 6 } };
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //一維陣列宣告：
            int[] A1 = new int[6];
            int[] A2 = new int[10];
            int[] A3 = { 60, 70, 80, 85, 90, 100 };
            int[] Stu_Sum = new int[4];         //學生總成績
            int[] Stu_Average = new int[4];     //學生平均成績
            int[] Subject_Sum = new int[5];     //科目總成績
            int[] Subjcet_Average = new int[5]; //科目平均成績
            Point[] pt = new Point[360];    //一維陣列內有360個Point
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //二維陣列宣告：
            int[,] Stu_Sum = new int[3, 4];         //學生總成績
            int[,] Stu_Average = new int[3, 4];     //學生平均成績
            int[,] Subject_Sum = new int[3, 5];     //科目總成績
            int[,] Subjcet_Average = new int[3, 5]; //科目平均成績
            int[,] Score = new int[,] { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 100 } };

            string[,] person = null;
            person = new string[,] {
                { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
                { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
                };

            int rank = person.Rank; //獲取維度
            int rows = person.GetUpperBound(0) + 1; //獲取指定維度的上限，第0項就是行數 row
            int cols = person.GetUpperBound(1) + 1; //獲取指定維度的上限，第1項就是列數 columns
            int len = person.Length;//獲取整個二維陣列的長度，即所有元 的個數

            int i, j;

            richTextBox1.Text += "維度 rank = " + rank.ToString() + "\n";
            for (i = 0; i < rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (person.GetUpperBound(i) + 1).ToString() + "\n";
            }

            int xx = person.GetUpperBound(0) + 1;
            int yy = person.GetUpperBound(1) + 1;
            //int zz = person.GetUpperBound(2) + 1;
            for (i = 0; i < xx; i++)
            {
                for (j = 0; j < yy; j++)
                {
                    //for (k = 0; k < zz; k++)
                    {
                        //richTextBox1.Text += "第(" + i.ToString() + ", " + j.ToString() + ", " + k.ToString() + ")項\t" + person[i, j, k] + "\n";
                        richTextBox1.Text += "第(" + i.ToString() + ", " + j.ToString() + ")項 " + person[i, j] + "\t";

                    }
                }
                richTextBox1.Text += "\n";
            }



            richTextBox1.Text += "維度 rank = " + rank.ToString() + "\n";
            richTextBox1.Text += "行 rows = " + rows.ToString() + "\n";
            richTextBox1.Text += "列 cols = " + cols.ToString() + "\n";
            richTextBox1.Text += "總長度 len  = " + len.ToString() + "\n";

            int col2 = person.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數

            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";    //3

            int len0 = person.GetLength(0);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int len1 = person.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            richTextBox1.Text += "len0 = " + len0.ToString() + "\n";    //3
            richTextBox1.Text += "len1 = " + len1.ToString() + "\n";    //6


        }

        private void button7_Click(object sender, EventArgs e)
        {
            //三維陣列宣告：
            int[, ,] G = new int[3, 4, 5];

            //三維陣列宣告：
            //int[, ,] Score = { { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 99 } }, { { 77, 88, 66, 77, 66 }, { 65, 66, 88, 55, 77 }, { 70, 88, 56, 88, 88 }, { 80, 90, 95, 99, 99 } }, { { 55, 67, 56, 98, 67 }, { 66, 69, 76, 66, 78 }, { 77, 89, 88, 77, 77 }, { 88, 89, 99, 97, 88 } } };

            //三維陣列宣告：  3Layer X 4Row X 5Column
            int[, ,] Score = {
                              { { 65, 85, 78, 75, 69 },
                                { 66, 55, 52, 92, 47 },
                                { 75, 99, 63, 73, 86 },
                                { 77, 88, 99, 91, 99 } },
                              { { 77, 88, 66, 77, 66 },
                                { 65, 66, 88, 55, 77 },
                                { 70, 88, 56, 88, 88 },
                                { 80, 90, 95, 99, 99 } },
                              { { 55, 67, 56, 98, 67 },
                                { 66, 69, 76, 66, 78 },
                                { 77, 89, 88, 77, 77 },
                                { 88, 89, 99, 97, 88 } }
                              };

            int i, j, k;
            int rank = Score.Rank; //獲取維度
            int rows = Score.GetUpperBound(0) + 1; //獲取指定維度的上限，第0項就是行數 row
            int cols = Score.GetUpperBound(1) + 1; //獲取指定維度的上限，第1項就是列數 columns
            int tttt = Score.GetUpperBound(2) + 1; //獲取指定維度的上限，第1項就是列數 columns
            int len = Score.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "維度 rank = " + rank.ToString() + "\n";
            for (i = 0; i < rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (Score.GetUpperBound(i) + 1).ToString() + "\n";
            }

            int xx = Score.GetUpperBound(0) + 1;
            int yy = Score.GetUpperBound(1) + 1;
            int zz = Score.GetUpperBound(2) + 1;
            for (i = 0; i < xx; i++)
            {
                for (j = 0; j < yy; j++)
                {
                    for (k = 0; k < zz; k++)
                    {
                        richTextBox1.Text += "第(" + i.ToString() + ", " + j.ToString() + ", " + k.ToString() + ")項 " + Score[i, j, k] + "\t";

                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }


            richTextBox1.Text += "行 rows = " + rows.ToString() + "\n";
            richTextBox1.Text += "列 cols = " + cols.ToString() + "\n";
            richTextBox1.Text += "列 cols = " + tttt.ToString() + "\n";
            richTextBox1.Text += "總長度 len  = " + len.ToString() + "\n";

            int col2 = Score.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數

            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";    //3

            int len0 = Score.GetLength(0);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int len1 = Score.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            richTextBox1.Text += "len0 = " + len0.ToString() + "\n";    //3
            richTextBox1.Text += "len1 = " + len1.ToString() + "\n";    //6
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //字串陣列的寫法(一維)：
            string[] atoms = { "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "魔羯座" };

            //字串陣列的寫法(一維)：
            string[] ws = new string[10] { "Acknowledge", "LookDown", "Sad", "Alert", "LookDownBlink", "Search", "Announce", "LookUp", "Think", "Blink" };

            //字串陣列的寫法(二維)：
            String[,] language = new string[3, 6] { { "正中1", "正中2", "正中3", "正中4", "正中5", "正中6" }, { "簡中1", "簡中2", "簡中3", "簡中4", "簡中5", "簡中6" }, { "英語1", "英語2", "英語3", "英語4", "英語5", "英語6" } };

            //字串陣列的寫法(一維)：
            String[] weekday = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = weekday[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            //字串宣告：
            string[] A = new string[10];
            string Temp = "";
            string D1, D2 = "", D3;
            D1 = richTextBox1.Text;
            string[] Stu_Name = { "張三", "李四", "王五", "陳六" };
        }

        private void button9_Click(object sender, EventArgs e)
        {
            int[,] x = { { 2, 3, 2 }, { 5, 6, 1 }, { 4, 6, 2 }, { 4, 6, 3 } };

            //int[, , , ,] y;

            richTextBox1.Text += "len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "rank = " + x.Rank.ToString() + "\n";
            //richTextBox1.Text += "rank = " + y.Rank.ToString() + "\n";


            int[, , ,] dim = new int[2, 5, 3, 7];
            richTextBox1.Text += "rank = " + dim.Rank.ToString() + "\n";

            //int[] num = { { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } } };
            //richTextBox1.Text += "rank = " + num.Rank.ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //this.Size = new Size(1920 *2, 1080 / 1);

            //不規則陣列

            // Declare the array of two elements.
            int[][] arr = new int[3][];

            // Initialize the elements.
            arr[0] = new int[5] { 1, 3, 5, 7, 9 };
            arr[1] = new int[4] { 2, 4, 6, 8 };
            arr[2] = new int[2] { 2, 4 };

            // Display the array elements.
            for (int i = 0; i < arr.Length; i++)
            {
                richTextBox1.Text += "row(" + i.ToString() + "):\tlen = " + arr[i].Length.ToString() + "\t";

                for (int j = 0; j < arr[i].Length; j++)
                {
                    richTextBox1.Text += arr[i][j].ToString() + "_";
                    //System.Console.Write("{0}{1}", arr[i][j], j == (arr[i].Length - 1) ? "" : " ");
                }
                richTextBox1.Text += "\n";
            }
            /*

            int row = arr.Rank;//獲取行數
            int col1 = arr.GetLength(0);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int col2 = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int num1 = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數

            richTextBox1.Text += "row = " + row.ToString() + "\n";
            richTextBox1.Text += "col1 = " + col1.ToString() + "\n";
            richTextBox1.Text += "col2 = " + col2.ToString() + "\n";
            richTextBox1.Text += "num1 = " + num1.ToString() + "\n";
            */
        }

        private void button11_Click(object sender, EventArgs e)
        {
            int i;

            //二維List for string
            List<string[]> steps = new List<string[]>();

            for (i = 0; i < 9; i++)
            {
                steps.Add(new string[] { i.ToString(), ('A' + i).ToString() });
            }

            //steps.Clear();

            if (steps.Count > 0)
                richTextBox1.Text += "共有 " + steps.Count.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < steps.Count; i++)
            {
                int tt = int.Parse(steps[i][1]);
                richTextBox1.Text += "steps[" + i.ToString() + "][0] = " + steps[i][0].ToString() + "\tsteps[" + i.ToString() + "][1] = " + (char)tt + "\n";
            }

            //刪除第N項
            int N;

            N = 1; steps.RemoveAt(N);  //index = N, 刪除第N項

            N = 3; steps.RemoveAt(N);  //index = N, 刪除第N項

            N = 5; steps.RemoveAt(N);  //index = N, 刪除第N項

            if (steps.Count > 0)
                richTextBox1.Text += "共有 " + steps.Count.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < steps.Count; i++)
            {
                int aaa = int.Parse(steps[i][1]);
                richTextBox1.Text += "steps[" + i.ToString() + "][0] = " + steps[i][0].ToString() + "\tsteps[" + i.ToString() + "][1] = " + (char)aaa + "\n";
            }

            /*
            Random r = new Random();
            string result2 = "";
            for (i = 0; i < 5; i++)
            {
                result2 += r.Next(10).ToString() + " ";
            }
            richTextBox1.Text += "取0~10的亂數值：" + result2 + "\n";
            */

            Random r = new Random();

            int[] selected = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int tmp;

            for (i = 0; i < selected.Length; i++)
            {
                int n = r.Next(selected.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }
            richTextBox1.Text += "方法一結果：";
            for (i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < selected.Length; i++)
            {
                selected[i] = i;
            }

            for (i = selected.Length - 1; i > 0; i--)
            {
                int n = r.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }

            richTextBox1.Text += "方法二結果：";
            for (i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string[,] person = null;
            person = new string[,] {
                { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
                { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
                { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
                };

            richTextBox1.Text += "二維陣列內容\n";
            PrintArray(person);
        }

        private const int COLUMNS = 10;
        private const int ROWS = 8;

        int[,] gray = new int[COLUMNS, ROWS];

        //製作二維陣列並存檔
        private void button13_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    //richTextBox1.Text += gray[i, j].ToString() + " ";
                    gray[i, j] = i + j * COLUMNS;
                }
                //richTextBox1.Text += "\n";
            }

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }

            string filename = "my_2d_array." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            StreamWriter sw = File.CreateText(filename);

            //sw.Write(richTextBox1.Text);

            sw.WriteLine(COLUMNS.ToString());
            sw.WriteLine(ROWS.ToString());

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    sw.WriteLine(gray[i, j].ToString());
                }
            }

            // Dispose StreamWriter
            sw.Dispose();
            // Close FileStream
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
        }

        //讀出檔案資料成二維陣列
        private void button14_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int k;
            int M = 0;
            int N = 0;

            string filename = @"C:\_git\vcs\_1.data\______test_files1\my_2d_array.txt";
            String line;
            StreamReader sr;

            i = 0;
            sr = new StreamReader(filename, Encoding.GetEncoding("big5"), true);
            while (!sr.EndOfStream)
            {               // 每次讀取一行，直到檔尾
                line = sr.ReadLine();            // 讀取文字到 line 變數
                if (line.Length > 0)
                {
                    k = int.Parse(line);
                    if (i == 0)
                        M = k;
                    else if (i == 1)
                    {
                        N = k;
                        break;
                    }
                    i++;
                }
            }
            sr.Close();

            richTextBox1.Text += "2D array " + M.ToString() + " X " + N.ToString() + "\n";

            gray = new int[M, N];

            i = 0;
            sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"), true);
            while (!sr.EndOfStream)
            {               // 每次讀取一行，直到檔尾
                line = sr.ReadLine();            // 讀取文字到 line 變數
                if (line.Length > 0)
                {
                    //richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\tlength:" + line.Length.ToString() + "\n";
                    k = int.Parse(line);
                    //richTextBox1.Text += k.ToString() + "\n";
                    if (i == 0)
                        M = k;
                    else if (i == 1)
                        N = k;
                    if (i > 1)
                    {
                        gray[(i - 2) % COLUMNS, (i - 2) / COLUMNS] = k;
                        //richTextBox1.Text += "i = " + ((i - 2) % COLUMNS).ToString() + ", j = " + ((i - 2) / COLUMNS).ToString() + ", k = " + k.ToString() + "\n";

                    }

                    i++;
                }
            }
            sr.Close();

            richTextBox1.Text += "show 2d array:\n";

            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    richTextBox1.Text += gray[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //Array.Copy.
            int i;
            int[] array1 = new int[1000];
            int[] array2 = new int[1000];

            for (i = 0; i < array1.Length; i++)
                array1[i] = i;

            Array.Copy(array1, array2, array1.Length);  //從前array1拷貝長度陣列到後array2，長度array1.Length，會快得多，約7倍快

            richTextBox1.Text += "Array1\t";
            for (i = 0; i < array1.Length; i += 60)
            {
                richTextBox1.Text += array1[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Array2\t";
            for (i = 0; i < array2.Length; i += 60)
            {
                richTextBox1.Text += array2[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //製作data
            int NumValues = 10;
            int[] Values = new int[NumValues];
            // Generate random values.
            Random rand = new Random();
            //Values = new int[NumValues];
            for (int i = 0; i < NumValues; i++)
            {
                Values[i] = rand.Next(0, 100);
            }
            // Sort the values.
            Array.Sort(Values);

            richTextBox1.Text += "原陣列\t";
            PrintArray(Values);

            int target = 30;

            richTextBox1.Text += "Binary Search\ttarget = " + target.ToString() + "\n";

            // Try to find it.
            int index = Array.BinarySearch(Values, target);

            // Select the value.
            if (index >= 0)
            {
                // We found the target. Select it.
                //lstValues.SelectedIndex = index;
                richTextBox1.Text += "Found target, index = " + index.ToString() + "\tvalue = " + Values[index].ToString() + "\n";

            }
            else
            {
                // We didn't find the target. Select a nearby value.
                index = -index;
                if (index >= NumValues)
                    index = NumValues - 1;
                //lstValues.SelectedIndex = index;
                richTextBox1.Text += "No found target, index = " + index.ToString() + "\tvalue = " + Values[index].ToString() + "\n";
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "一維顏色陣列顯示名稱\n";
            Color[] colorSet = { Color.Red, Color.Blue, Color.Green, Color.Gray };
            for (int i = 0; i < 4; i++)
            {
                richTextBox1.Text += colorSet[i].Name.ToString() + "\n";
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {

            String[, ,] items =
            new String[,,] {
            {
            { "A1", "A2", "A3", "☆", "○" },
            { "B1", "B2", "B3", "☆", "○" },
            { "C1", "C2", "C3", "☆", "○" },
            { "D1", "D2", "D3", "☆", "○" }
            }, {
            { "E1", "E2", "E3", "☆", "○" },
            { "F1", "F2", "F3", "☆", "○" },
            { "G1", "G2", "G3", "☆", "○" },
            { "H1", "H2", "H3", "☆", "○" }
            }
            };

            //GetUpperBound(0) 返回數組的第一維的索引上限，GetUpperBound(i)返回數組的i+1維的上限，GetUpperBound(Rank-1)返回數組的最後一維的上限，也就是列數-1

            Console.WriteLine("Items.Rank =" + items.Rank);
            Console.WriteLine("Items.GetUpperBound(0)=" + items.GetUpperBound(0));

            Console.WriteLine("Items.GetUpperBound(1)=" + items.GetUpperBound(1));
            Console.WriteLine("Items.GetUpperBound(2)=" + items.GetUpperBound(items.Rank - 1));

            Console.WriteLine("Items[0, 0, 0]=" + items[0, 0, 0]);
            Console.WriteLine("Items[0, 0, 1]=" + items[0, 0, 1]);
            Console.WriteLine("Items[0, 0, 2]=" + items[0, 0, 2]);
            Console.WriteLine("Items[0, 0, 3]=" + items[0, 0, 3]);
            Console.WriteLine("Items[0, 0, 4]=" + items[0, 0, 4]);


            Console.WriteLine("Items[0, 1, 0]=" + items[0, 1, 0]);
            Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 1]);
            Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 2]);
            Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 3]);

            Console.WriteLine("Items[0, 2, 0]=" + items[0, 1, 4]);

        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "插入排序\n";
            int[] iArrary = new int[] { 1, 13, 3, 6, 10, 55, 98, 2, 87, 12, 34, 75, 33, 47 };
            InsertionSort ii = new InsertionSort();
            ii.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
            {
                richTextBox1.Text += iArrary[m].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "希爾排序\n";
            int[] iArrary = new int[] { 1, 5, 13, 6, 10, 55, 99, 2, 87, 12, 34, 75, 33, 47 };
            ShellSort sh = new ShellSort();
            sh.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
            {
                richTextBox1.Text += iArrary[m].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        class AnimalData
        {
            public string Name_C { get; set; }
            public string Name_E { get; set; }
            public string Name_N { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public DateTime Birthday { get; set; }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //二維陣列排序
            AnimalData[] AnimalDataArray = new AnimalData[]{
            new AnimalData { Name_C = "鼠", Name_E = "mouse", Name_N = "Mickey", Age= 20 , Weight = 5, Birthday = DateTime.Parse("1928/11/18") },
            new AnimalData { Name_C = "牛", Name_E = "bull", Name_N = "Benny", Age= 30 , Weight = 82, Birthday = DateTime.Parse("2000/8/14") },
            new AnimalData { Name_C = "虎", Name_E = "tiger", Name_N = "Eric", Age= 15 , Weight = 55, Birthday = DateTime.Parse("1993/12/13") },
            new AnimalData { Name_C = "兔", Name_E = "rabbit", Name_N = "Cony", Age= 22 , Weight = 12, Birthday = DateTime.Parse("2013/4/17") }
            };

            richTextBox1.Text += "排序前：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Name_C排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Name_C.CompareTo(s2.Name_C);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Name_E排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Name_E.CompareTo(s2.Name_E);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Name_N排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Name_N.CompareTo(s2.Name_N);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Age排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Age.CompareTo(s2.Age);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Weight排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Weight.CompareTo(s2.Weight);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Birthday排序, ";
            Array.Sort(AnimalDataArray, delegate(AnimalData s1, AnimalData s2)
            {
                return s1.Birthday.CompareTo(s2.Birthday);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (AnimalData str in AnimalDataArray)
            {
                richTextBox1.Text += str.Name_C + "\t" + str.Name_E + "\t" + str.Name_N + "\t" + str.Age + "\t" + str.Weight + "\t" + str.Birthday + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            int[] num = { 12, 45, 76, -3, 48, 93 };

            richTextBox1.Text += "原陣列：\n";
            for (int i = 0; i < num.Length; i++)
            {
                richTextBox1.Text += num[i].ToString() + "   ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "原陣列反相：\n";
            Array.Reverse(num);
            for (int i = 0; i < num.Length; i++)
            {
                richTextBox1.Text += num[i].ToString() + "   ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "原陣列排序：\n";
            Array.Sort(num);
            for (int i = 0; i < num.Length; i++)
            {
                richTextBox1.Text += num[i].ToString() + "   ";
            }
            richTextBox1.Text += "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            int[] Scores = new int[] { 89, 65, 31, 89, 92, 46 };
            richTextBox1.Text += "原成績：\t";
            foreach (int s in Scores)
            {
                richTextBox1.Text += s.ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "排列後：\t";
            Array.Sort(Scores);
            foreach (int s in Scores)
            {
                richTextBox1.Text += s.ToString() + "\t";
            }
            richTextBox1.Text += "遞增\n";

            richTextBox1.Text += "排列後：\t";
            Array.Reverse(Scores);
            foreach (int s in Scores)
            {
                richTextBox1.Text += s.ToString() + "\t";
            }
            richTextBox1.Text += "遞減\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "選擇排序\n";
            int[] iArrary = new int[] { 1, 5, 3, 6, 10, 55, 9, 2, 87, 12, 34, 75, 33, 47 };
            SelectionSort ss = new SelectionSort();
            ss.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)
            {
                richTextBox1.Text += iArrary[m].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "氣泡排序\n";
            int[] iArrary = new int[] { 1, 5, 13, 6, 10, 55, 99, 2, 87, 12, 34, 75, 33, 47 };//定義數組
            BubbleSort sh = new BubbleSort();
            sh.Sort(iArrary);
            for (int m = 0; m < iArrary.Length; m++)//輸出結果
            {
                richTextBox1.Text += iArrary[m].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            int[] scores = new int[] { 80, 50, 60, 90, 70 };
            //string[] names = new string[] {"Mary", "Jack", "Tom", "David", "Grace" };  //寫法同下
            string[] names = { "Mary", "Jack", "Tom", "David", "Grace" };

            richTextBox1.Text += "排序前：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + names[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";

            Array.Sort(names, scores);   //以names為準排序，scores跟著
            richTextBox1.Text += "依姓名排序：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + names[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";

            Array.Sort(scores, names);   //以scores為準排序，names跟著
            richTextBox1.Text += "依成績排序：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + names[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //排名次
            int i;
            int j;
            int[] scores = new int[] { 80, 50, 60, 90, 80 };
            int[] scores_new = new int[5];
            int[] rank = new int[5];
            //string[] names = new string[] {"Mary", "Jack", "Tom", "David", "Grace" };  //寫法同下
            string[] names = { "Mary", "Jack", "Tom", "David", "Grace" };

            richTextBox1.Text += "排序前：\n";
            for (i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t" + names[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";

            Array.Copy(scores, scores_new, scores.Length);
            Array.Sort(scores_new);
            Array.Reverse(scores_new);

            int score_last = -1;
            for (i = 0; i < scores_new.Length; i++)
            {
                if (scores_new[i] == score_last)
                    continue;
                else
                    score_last = scores_new[i];

                //richTextBox1.Text += i.ToString() + "\t" + names[i] + "\t" + scores_new[i] + "\n";
                for (j = 0; j < scores_new.Length; j++)
                {
                    if (scores[j] == scores_new[i])
                    {
                        //richTextBox1.Text += "match i = " + i.ToString() + " j = " + j.ToString() + " s = " + scores_new[i].ToString() + "\n";
                        rank[j] = i;
                    }
                }
            }
            richTextBox1.Text += "排名次：\n";
            for (i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t" + names[i] + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button28_Click(object sender, EventArgs e)
        {
            int i; // 宣告 i 為for迴圈計數變數
            // 建立RoleName[0]~RoleName[4]用來存放角色姓名
            string[] RoleName = new string[] { "魯夫", "喬巴", "羅賓", "香吉士", "騙人布" };
            // 建立Money[0]~Money[4] 用來存放角色的懸賞金額
            int[] Money = new int[] { 300000000, 50, 78000000, 77000000, 30000000 };

            richTextBox1.Text += "==草帽海賊團成員(原資料)==\n";
            richTextBox1.Text += "姓名\t懸賞金額\n";
            richTextBox1.Text += "==================\n";
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                richTextBox1.Text += RoleName[i] + "\t" + Money[i].ToString("#,#") + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "==草帽海賊團成員(遞增排序)==\n";
            richTextBox1.Text += "姓名\t懸賞金額\n";
            richTextBox1.Text += "==================\n";
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            // 陣列的GetUpperBound()方法可用來取得某一維度的上限
            // 因此RoleName.GetUpperBound(0) 會傳回 4
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                richTextBox1.Text += RoleName[i] + "\t" + Money[i].ToString("#,#") + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "==草帽海賊團成員(遞減排序)==\n";
            richTextBox1.Text += "姓名\t懸賞金額\n";
            richTextBox1.Text += "==================\n";
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            // 反轉Money陣列，使Money陣列變成遞減排序
            Array.Reverse(Money);
            Array.Reverse(RoleName);    // 反轉RoleName陣列
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                richTextBox1.Text += RoleName[i] + "\t" + Money[i].ToString("#,#") + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            Person[] people =
            {
                new Person() { FirstName="Ben", LastName="Holbrook"},
                new Person() { FirstName="Fred", LastName="Gill"},
                new Person() { FirstName="Ginny", LastName="Franklin"},
                new Person() { FirstName="Cindy", LastName="Carter"},
                new Person() { FirstName="Ann", LastName="Baker"},
                new Person() { FirstName="Jeff", LastName="Ivanova"},
                new Person() { FirstName="Irma", LastName="Archer"},
                new Person() { FirstName="Dan", LastName="Jerico"},
                new Person() { FirstName="Hal", LastName="Evans"},
                new Person() { FirstName="Edwina", LastName="Dolf"},
            };

            richTextBox1.Text += "原陣列\n";
            // Display the people unsorted.
            for (int i = 0; i < people.Length; i++)
            {
                //lstPeople.Items.Add(people[i]);
                richTextBox1.Text += people[i] + "\n";
            }

            richTextBox1.Text += "依名排序\n";
            // Sort the people.
            Array.Sort(people);
            for (int i = 0; i < people.Length; i++)
            {
                //lstSortedPeople.Items.Add(people[i]);
                richTextBox1.Text += people[i] + "\n";
            }

        }

        private void button30_Click(object sender, EventArgs e)
        {
            Person[] people =
            {
                new Person() { FirstName="Ben", LastName="Holbrook"},
                new Person() { FirstName="Fred", LastName="Gill"},
                new Person() { FirstName="Ginny", LastName="Franklin"},
                new Person() { FirstName="Cindy", LastName="Carter"},
                new Person() { FirstName="Ann", LastName="Baker"},
                new Person() { FirstName="Jeff", LastName="Ivanova"},
                new Person() { FirstName="Irma", LastName="Archer"},
                new Person() { FirstName="Dan", LastName="Jerico"},
                new Person() { FirstName="Hal", LastName="Evans"},
                new Person() { FirstName="Edwina", LastName="Dolf"},
            };

            richTextBox1.Text += "原陣列\n";
            // Display the people unsorted.
            for (int i = 0; i < people.Length; i++)
            {
                //lstLastNameFirst.Items.Add(people[i]);
                richTextBox1.Text += people[i] + "\n";
            }

            richTextBox1.Text += "依姓排序\n";
            // Sort the people.
            PersonComparer comparer = new PersonComparer();
            Array.Sort(people, comparer);
            for (int i = 0; i < people.Length; i++)
            {
                //lstSortedLastNameFirst.Items.Add(people[i]);
                richTextBox1.Text += people[i] + "\n";
            }

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {
            //Array環狀右移
            int n = 10;
            // Initialize the list of array_data.
            int[] array_data = new int[n];
            for (int i = 0; i < n; i++)
                array_data[i] = i;
            richTextBox1.Text += "原陣列\n";
            PrintArray(array_data);

            int rr = 1;
            richTextBox1.Text += "rotate r = " + rr.ToString() + "\n";
            RotateArrayR(array_data, rr);     // Rotate the array.
            PrintArray(array_data);

            rr = 3;
            richTextBox1.Text += "rotate r = " + rr.ToString() + "\n";
            RotateArrayR(array_data, rr);     // Rotate the array.
            PrintArray(array_data);

            rr = 11;
            richTextBox1.Text += "rotate r = " + rr.ToString() + "\n";
            RotateArrayR(array_data, rr);     // Rotate the array.
            PrintArray(array_data);

            rr = 28;
            richTextBox1.Text += "rotate r = " + rr.ToString() + "\n";
            RotateArrayR(array_data, rr);     // Rotate the array.
            PrintArray(array_data);

            rr = 31;
            richTextBox1.Text += "rotate r = " + rr.ToString() + "\n";
            RotateArrayR(array_data, rr);     // Rotate the array.
            PrintArray(array_data);
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //Array環狀左移
            int n = 10;
            // Initialize the list of array_data.
            int[] array_data = new int[n];
            for (int i = 0; i < n; i++)
                array_data[i] = i;
            richTextBox1.Text += "原陣列\n";
            PrintArray(array_data);

            int rl = 1;
            richTextBox1.Text += "rotate l = " + rl.ToString() + "\n";
            RotateArrayL(array_data, rl);     // Rotate the array.
            PrintArray(array_data);

            richTextBox1.Text += "rotate l = " + rl.ToString() + "\n";
            RotateArrayL(array_data, rl);     // Rotate the array.
            PrintArray(array_data);

            richTextBox1.Text += "rotate l = " + rl.ToString() + "\n";
            RotateArrayL(array_data, rl);     // Rotate the array.
            PrintArray(array_data);

            richTextBox1.Text += "rotate l = " + rl.ToString() + "\n";
            RotateArrayL(array_data, rl);     // Rotate the array.
            PrintArray(array_data);
        }

        // Rotate to right with offset
        private void RotateArrayR(int[] array_data, int offset)
        {
            offset = offset % array_data.Length;
            if (offset == 0)
                return;
            int[] tmp = new int[offset];
            int i;
            for (i = 0; i < offset; i++)
            {
                tmp[i] = array_data[array_data.Length - offset + i];
            }

            Array.Copy(array_data, 0, array_data, offset, array_data.Length - offset);
            for (i = 0; i < offset; i++)
            {
                array_data[i] = tmp[i];
            }
        }

        // Rotate to left with offset
        private void RotateArrayL(int[] array_data, int offset)
        {
            offset = offset % array_data.Length;
            if (offset == 0)
                return;
            int[] tmp = new int[offset];
            int i;
            for (i = 0; i < offset; i++)
            {
                tmp[i] = array_data[i];
            }

            Array.Copy(array_data, offset, array_data, 0, array_data.Length - offset);
            for (i = 0; i < offset; i++)
            {
                array_data[array_data.Length - 1 - i] = tmp[i];
            }
        }

        private void PrintArray(int[] array_data)
        {
            for (int i = 0; i < array_data.Length; i++)
            {
                if (i == (array_data.Length - 1))
                    richTextBox1.Text += array_data[i].ToString();
                else
                    richTextBox1.Text += array_data[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void PrintArray<T>(T[,] arr)
        {
            richTextBox1.Text += "Rank = " + arr.Rank.ToString() + "\n";

            int ROW = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = arr.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "L0 = " + arr.GetLength(0).ToString() + "\n";  //第0維的長度
            richTextBox1.Text += "L1 = " + arr.GetLength(1).ToString() + "\n";  //第1維的長度

            richTextBox1.Text += "t1 = " + arr.GetLowerBound(0).ToString() + "\n";  //第0維的下限 0
            richTextBox1.Text += "t2 = " + arr.GetLowerBound(1).ToString() + "\n";  //第1維的下限 0
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(0).ToString() + "\n";  //第0維的上限
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(1).ToString() + "\n";  //第1維的上限


            for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
            {
                for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
                {
                    richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void PrintArray<T>(T[, ,] arr)
        {
            int i;
            int rank = arr.Rank;

            richTextBox1.Text += "維度 rank = " + rank.ToString() + "\n";

            for (i = 0; i < rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + arr.GetLength(i).ToString() + "\n";
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (arr.GetUpperBound(i) + 1).ToString() + "\n";
            }

            /*
            int ROW = arr.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = arr.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = arr.Length;//獲取整個二維陣列的長度，即所有元 的個數
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";

            richTextBox1.Text += "t1 = " + arr.GetLowerBound(0).ToString() + "\n";  //第0維的下限 0
            richTextBox1.Text += "t2 = " + arr.GetLowerBound(1).ToString() + "\n";  //第1維的下限 0
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(0).ToString() + "\n";  //第0維的上限
            richTextBox1.Text += "t3 = " + arr.GetUpperBound(1).ToString() + "\n";  //第1維的上限
            */

            for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
            {
                for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
                {
                    //richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
        }


        //解讀一個在TextBox的矩陣 ST
        private void button34_Click(object sender, EventArgs e)
        {
            int num_rows, num_cols;
            richTextBox1.Text += "call LoadArray for arr\n";
            double[,] arr = LoadArray(out num_rows, out num_cols);
            // Display the initial arrays.
            richTextBox1.Text += "PrintArray for arr\n";
            PrintArray(arr);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            int num_rows, num_cols;
            richTextBox1.Text += "call LoadArray for arr\n";
            double[,] arr = LoadArray2(out num_rows, out num_cols);
            // Display the initial arrays.
            richTextBox1.Text += "PrintArray for arr\n";
            PrintArray(arr);
        }

        // Load the augmented array.
        // Column num_cols holds the result values.
        // Column num_cols + 1 will hold the variables' final values after backsolving.
        private double[,] LoadArray(out int num_rows, out int num_cols)
        {
            richTextBox1.Text += "LoadArray ST\n";
            // Build the augmented matrix.
            //string[] value_rows = txtValues.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);

            //string[] coef_rows = rtb_matrix.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);
            string[] coef_rows = tb_matrix.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);

            string[] one_row = coef_rows[0].Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            /*
            richTextBox1.Text += "value_rows\t";
            foreach (string s in value_rows)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";
            */
            richTextBox1.Text += "coef_rows\t";
            foreach (string s in coef_rows)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "one_row\t";
            foreach (string s in one_row)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";

            num_rows = coef_rows.GetUpperBound(0);
            num_cols = one_row.GetUpperBound(0);
            richTextBox1.Text += "num_rows = " + num_rows.ToString() + "\n";
            richTextBox1.Text += "num_cols = " + num_cols.ToString() + "\n";

            double[,] arr = new double[num_rows + 1, num_cols + 1];
            for (int r = 0; r < (num_rows + 1); r++)
            {
                one_row = coef_rows[r].Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                for (int c = 0; c < (num_cols + 1); c++)
                {
                    arr[r, c] = double.Parse(one_row[c]);
                }
                //arr[r, num_cols] = double.Parse(value_rows[r]);
            }

            return arr;
        }

        // Load the augmented array.
        // Column num_cols holds the result values.
        // Column num_cols + 1 will hold the variables' final values after backsolving.
        private double[,] LoadArray2(out int num_rows, out int num_cols)
        {
            richTextBox1.Text += "LoadArray ST\n";
            // Build the augmented matrix.
            //string[] value_rows = txtValues.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);

            string[] coef_rows = rtb_matrix.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);
            //string[] coef_rows = tb_matrix.Text.Split(new string[] { "\r\n" }, StringSplitOptions.RemoveEmptyEntries);

            string[] one_row = coef_rows[0].Split(new string[] { " " }, StringSplitOptions.RemoveEmptyEntries);
            /*
            richTextBox1.Text += "value_rows\t";
            foreach (string s in value_rows)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";
            */
            richTextBox1.Text += "coef_rows\t";
            foreach (string s in coef_rows)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";
            richTextBox1.Text += "one_row\t";
            foreach (string s in one_row)
                richTextBox1.Text += s + " ";
            richTextBox1.Text += "\n";

            num_rows = coef_rows.GetUpperBound(0);
            num_cols = one_row.GetUpperBound(0);
            richTextBox1.Text += "num_rows = " + num_rows.ToString() + "\n";
            richTextBox1.Text += "num_cols = " + num_cols.ToString() + "\n";

            double[,] arr = new double[num_rows + 1, num_cols + 1];
            for (int r = 0; r < (num_rows + 1); r++)
            {
                one_row = coef_rows[r].Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                for (int c = 0; c < (num_cols + 1); c++)
                {
                    //arr[r, c] = double.Parse(one_row[c]);
                }
                //arr[r, num_cols] = double.Parse(value_rows[r]);
            }

            return arr;
        }

        private void PrintArray(double[,] arr)
        {
            richTextBox1.Text += "PrintArray\n";
            for (int r = arr.GetLowerBound(0); r <= arr.GetUpperBound(0); r++)
            {
                for (int c = arr.GetLowerBound(1); c <= arr.GetUpperBound(1); c++)
                {
                    richTextBox1.Text += arr[r, c].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
        //解讀一個在TextBox的矩陣 SP

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "IndexOf的用法\n";

            string[] stu = new string[] { "趙一", "林二", "張三", "李四", "王五" };
            int[] score = new int[] { 95, 100, 100, 92, 100 };

            richTextBox1.Text += "一份成績表, 搜尋100分的學生\t";
            //string msg = "一百分學生：";
            int index = Array.IndexOf(score, 100);   //搜尋第一個滿分學生
            while (index >= 0)                   //當index >= 0繼續迴圈
            {
                richTextBox1.Text += stu[index] + ", ";      // 顯示學生姓名
                index = Array.IndexOf(score, 100, index + 1);  // 從下一筆繼續搜尋
            };
            richTextBox1.Text += "\n";



            //定義學生的學號陣列StuId及姓名陣列StuName
            string[] StuId = new string[] { "8001", "8002", "8003", "8004", "8005" };
            string[] StuName = new string[] { "劉學有", "張杰輪", "周立宏", "王吉吉", "陶得華" };
            richTextBox1.Text += "一份學號與姓名對照表, 搜尋學號為8003的學生\t";

            // 使用Array.IndexOf方法搜尋txtId.Text在StuId陣列中是第幾個元素
            int search_num = Array.IndexOf(StuId, "8003");
            if (search_num != -1)
            {
                //lblMsg.Text = StuName[search_num] + "    歡迎光臨!!";
                richTextBox1.Text += "查到學生:\t" + StuName[search_num] + "\n";
            }
            else
            {
                //lblMsg.Text = "Sorry!   查無此學生!!";
                richTextBox1.Text += "查無此學生\n";
            }


            //song字串陣列存放歌曲名稱
            string[] song = new string[] { "姐姐", "天后", "我的歌聲裡", "東區東區", "勢在必行", "末班車", "一個人想著一個人", "愛你", "阿飛的小蝴蝶", "王妃" };
            //singer字串陣列存放歌手姓名
            string[] singer = new string[] { "謝金燕", "陳勢安", "曲婉婷", "八三夭", "陳勢安", "蕭煌奇", "曾沛慈", "陳芳語", "蕭敬騰", "蕭敬騰" };
            richTextBox1.Text += "一份歌手與專輯的對照表, 搜尋歌手為<陳芳語>的專輯\n";

            string search = "陳芳語"; //取得使用者查詢的歌手姓名
            string msg = "找不到" + search; //預設找不到
            index = Array.IndexOf(singer, search);   //搜尋第一個歌手
            if (index >= 0) //若有找到相符的資料
            {
                msg = "歌手" + "\t" + "歌曲" + Environment.NewLine;
                while (index >= 0)   //當index >= 0繼續迴圈
                {
                    msg += singer[index] + "\t" + song[index] + Environment.NewLine;    //顯示資料內容
                    index = Array.IndexOf(singer, search, index + 1); //從下一筆繼續搜尋
                };
            }
            //txtMsg.Text = msg;  //顯示資料內容
            richTextBox1.Text += msg + "\n";
        }

        private void button37_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "一份歌手與歌曲的對照表, 依排名排序  依歌曲名排序\n";

            //song字串陣列存放歌曲名稱
            string[] song = new string[] { "姐姐", "天后", "我的歌聲裡", "東區東區", "勢在必行", "末班車", "一個人想著一個人", "愛你", "阿飛的小蝴蝶", "王妃" };
            //singer字串陣列存放歌手姓名
            string[] singer = new string[] { "謝金燕", "陳勢安", "曲婉婷", "八三夭", "陳勢安", "蕭煌奇", "曾沛慈", "陳芳語", "蕭敬騰", "蕭敬騰" };
            int[] no = new int[10]; //no整數陣列存放排名

            for (int i = 0; i < no.Length; i++) //設定no陣列的初值
            {
                no[i] = i + 1;
            }

            richTextBox1.Text += "依排名排序\n";
            int[] temp1 = new int[no.Length];//宣告temp整數陣列，大小和no陣列相同
            no.CopyTo(temp1, 0);   //將no陣列的內容複製到temp陣列
            Array.Sort(no, song);   //nog陣列遞增排序，song陣列同步調整
            Array.Sort(temp1, singer);   //temp陣列遞增排序，singer陣列同步調整
            string msg1 = "排名" + "\t" + "歌手" + "\t" + "歌曲" + Environment.NewLine;
            for (int i = 0; i < song.Length; i++)
            {
                msg1 += no[i].ToString() + "\t" + singer[i] + "\t" + song[i] + Environment.NewLine;
            }
            richTextBox1.Text += msg1 + "\n";

            richTextBox1.Text += "依歌曲名排序\n";
            string[] temp2 = new string[song.Length];//宣告temp字串陣列，大小和song陣列相同
            song.CopyTo(temp2, 0);   //將song陣列的內容複製到temp陣列
            Array.Sort(song, no);   //song陣列遞增排序，no陣列同步調整
            Array.Sort(temp2, singer);   //temp陣列遞增排序，singer陣列同步調整
            string msg2 = "排名" + "\t" + "歌手" + "\t" + "歌曲" + Environment.NewLine;
            for (int i = 0; i < song.Length; i++)
            {
                msg2 += no[i].ToString() + "\t" + singer[i] + "\t" + song[i] + Environment.NewLine;
            }
            richTextBox1.Text += msg2 + "\n";
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //Clone的用法
            string[] arr = { "one", "two", "three", "four", "five" };
            string[] arrCloned = arr.Clone() as string[];

            richTextBox1.Text += "原陣列:\t";
            foreach (string s in arr)
            {
                richTextBox1.Text += s + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Clone陣列:\t";
            foreach (string s in arrCloned)
            {
                richTextBox1.Text += s + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //使用 GetBytes() 方法將字串轉換為位元組陣列

            string myString = "This is a string.";
            byte[] byteArray = Encoding.ASCII.GetBytes(myString);
            richTextBox1.Text += "The Byte Array is:\n";
            foreach (byte bytes in byteArray)
            {
                richTextBox1.Text += bytes.ToString() + "\n";
            }
        }

        string[] LunarHolDayName = {
                  "小寒", "大寒", "立春", "雨水",
                  "驚蟄", "春分", "清明", "谷雨",
                  "立夏", "小滿", "芒種", "夏至",
                  "小暑", "大暑", "立秋", "處暑",
                  "白露", "秋分", "寒露", "霜降",
                  "立冬", "小雪", "大雪", "冬至"};

        private void button40_Click(object sender, EventArgs e)
        {
            //陣列宣告範例
            int[] A = new int[5];
            int[] B = new int[] { 1, 2, 3, 4, 5 };
            int[] C = { 1, 3, 5, 7, 9 };
            int[,] D = new int[3, 3];
            int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[, ,] G = new int[3, 4, 5];

            //一維陣列
            int[] myArr = new int[4];	//宣告
            myArr[0] = 1;
            myArr[1] = 2;
            myArr[2] = 3;
            myArr[3] = 4;
            myArr = new int[] { 1, 2, 3, 4 };	//改值

            //三維陣列的寫法：
            int[, ,] myArray = new int[2, 3, 4];

            //鋸齒陣列	//不規則陣列
            char[][] ch = new char[][]
            {
                new char[] {'a','b','c'},
                new char[] {'c','d','e','f','g','h'},
                new char[] {'w','x','y','z'}
            };

            //Color陣列
            System.Drawing.Color[] color1 = new Color[5];
            color1[0] = Color.Brown;
            color1[1] = Color.Azure;
            color1[2] = Color.Chartreuse;
            color1[3] = Color.Cyan;
            color1[4] = Color.Gainsboro;

            //Point陣列
            Point a = new Point(10, 20);    //宣告一個Point變數
            a.X = 30;   //改值
            a.Y = 40;
            a = new Point(35, 45);          //同時更改XY兩個整數屬性的值


            int[] index = new int[4] { 2, 4, 6, 8 };
            int[] a1 = new int[4];
            a1[0] = 5;
            a1[1] = 4;
            a1[2] = 6;
            a1[3] = 2;
            Array.Sort(a1);
            richTextBox1.Text += "\n最大值為：" + a1[3].ToString() + "\n";

            foreach (string str in LunarHolDayName)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
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

        //氣泡排序2 ST

        /*
        1、道理：從數組的第一個地位開端兩兩比擬array[index]和array[index+1]，假如array[index]年夜於array[index+1]則交流array[index]和array[index+1]的地位，止到數組停止;
        從數組的第一個地位開端，反復下面的舉措，止到數組長度減一個地位停止;
        從數組的第一個地位開端，反復下面的舉措，止到數組長度減二個地位停止;
        。。。。
        2、時光龐雜度：O(N²)，停止了(n-1)*(n-2)....=n*(n-1)/2次比擬和約比擬次數一半的交流次數(均況下)，那末依據年夜O表現法時光龐雜度為O(N^2)
        */

        //先樹立一個類，今後把一切排序辦法都放到這個類裡，
        public class SumSort
        {
            //冒泡排序辦法，從小到年夜排，固然許多冒泡排序都是從年夜到小，
            //可是我就想這麼排，你能怎樣著我。
            public void PopSort(int[] list)
            {
                int i, j, temp;  //先界說一下要用的變量
                for (i = 0; i < list.Length - 1; i++)
                {
                    for (j = i + 1; j < list.Length; j++)
                    {
                        if (list[i] > list[j]) //假如第二個小於第一個數
                        {
                            //交流兩個數的地位，在這裡你也能夠零丁寫一個交流辦法，在此挪用就好了
                            temp = list[i]; //把年夜的數放在一個暫時存儲地位
                            list[i] = list[j]; //然後把小的數賦給前一個，包管每趟排序後面的最小
                            list[j] = temp; //然後把暫時地位的誰人年夜數賦給後一個
                        }
                    }
                }
            }
        }

        private void button45_Click(object sender, EventArgs e)
        {
            //氣泡排序2
            int[] arr = { 1, 4, 2, 43, 5, 61, 89, 34, 67, 32, 40 };
            richTextBox1.Text += "原序列:\n";
            for (int i = 0; i < arr.Length; i++)
            {
                richTextBox1.Text += arr[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            //把數據排序類實例化一下，然後挪用辦法。
            //甚麼？還要實例，可我不想實例化怎樣辦？
            //那也沒有關系，把PopSort辦法前加一個static，直接挪用SumSort.PopSort(arr)就行了
            SumSort mysort = new SumSort();
            //來來來，年夜家按高矮排個隊，矮的排後面高的排前面
            mysort.PopSort(arr);
            //真聽話，看看年夜家都排第幾位了
            richTextBox1.Text += "排序後:\n";
            for (int i = 0; i < arr.Length; i++)
            {
                richTextBox1.Text += arr[i].ToString() + "\t";
            }
            Console.WriteLine();
            richTextBox1.Text += "\n";


        }
        //氣泡排序2 SP

        private void array_sort_Click(object sender, EventArgs e)
        {
            //物件陣列測試
            TextBox[] textArray = new TextBox[] { numText1a, numText2a, numText3a, numText4a, numText5a, numText6a, numText7a, numText8a };
            for (int i = 0; i < 8; i++)
            {
                textArray[i].BackColor = SystemColors.Window;
            }
            int[] numArray = new int[8];
            Random rnd = new Random();
            for (int i = 0; i < 8; ++i)
            {
                int num = rnd.Next(1, 50);
                numArray[i] = num;
                textArray[i].Text = num.ToString();
            }
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            timer_sort.Enabled = true;
            startButton.Text = "1";
        }

        private void timer_sort_Tick(object sender, EventArgs e)
        {
            TextBox[] textArray = new TextBox[] { numText1b, numText2b, numText3b, numText4b, numText5b, numText6b, numText7b, numText8b };
            for (int i = 0; i < 8; i++)
                textArray[i].BackColor = SystemColors.Window;

            int check = int.Parse(startButton.Text);
            for (int j = 0; check > (7 - j); j++)
                check -= (7 - j);

            check--;
            textArray[check].BackColor = Color.LightBlue;
            textArray[check + 1].BackColor = Color.LightBlue;
            string tmp;
            if (int.Parse(textArray[check].Text) > int.Parse(textArray[check + 1].Text))
            {
                textArray[check].BackColor = Color.Pink;
                textArray[check + 1].BackColor = Color.Pink;
                tmp = textArray[check + 1].Text;
                textArray[check + 1].Text = textArray[check].Text;
                textArray[check].Text = tmp;
            }

            if (startButton.Text == "28")
            {
                timer_sort.Enabled = false;
                textArray[check].BackColor = SystemColors.Window;
                textArray[check + 1].BackColor = SystemColors.Window;
                startButton.Text = "開始排序";
            }
            else
            {
                startButton.Text = (int.Parse(startButton.Text) + 1).ToString();
            }
        }

        private void stepButton_Click(object sender, EventArgs e)
        {
            TextBox[] textArray = new TextBox[] { numText1c, numText2c, numText3c, numText4c, numText5c, numText6c, numText7c, numText8c };

            if (stepButton.Text == "開始")
            {
                stepButton.Text = "下一步";

                for (int i = 7; i > 0; i--)
                {
                    for (int j = 0; j < i; j++)
                    {
                        if (int.Parse(textArray[j].Text) > int.Parse(textArray[j + 1].Text))
                        {
                            string tmp = textArray[j + 1].Text;
                            textArray[j + 1].Text = textArray[j].Text;
                            textArray[j].Text = tmp;
                        }
                    }
                }
                for (int i = 0; i < 8; i++)
                {
                    textArray[i].BackColor = Color.LightBlue;
                }
                targetText.Enabled = false;
            }
            else
            {
                int i, lowIndex = 0, highIndex = 0;

                for (i = 0; i < 8; i++)
                {
                    if (textArray[i].BackColor == Color.LightBlue)
                    {
                        break;
                    }
                }
                lowIndex = i;

                for (i = 7; i > 0; i--)
                {
                    if (textArray[i].BackColor == Color.LightBlue)
                    {
                        break;
                    }
                }
                highIndex = i;

                for (i = 0; i < 8; i++)
                {
                    textArray[i].BackColor = SystemColors.Window;
                }


                int midIndex = (highIndex + lowIndex) / 2;
                if (textArray[midIndex].Text == targetText.Text)
                {
                    MessageBox.Show("你所指定的數字在索引 " + midIndex + "的位置!");
                    stepButton.Text = "開始";
                    targetText.Enabled = true;
                }
                else
                {
                    if (int.Parse(textArray[midIndex].Text) > int.Parse(targetText.Text))
                    {
                        highIndex = midIndex - 1;
                    }
                    else
                    {
                        lowIndex = midIndex + 1;
                    }

                    if (lowIndex > highIndex)
                    {
                        MessageBox.Show("程式在陣列中沒有找到你所指定的數字!");
                        stepButton.Text = "開始";
                        targetText.Enabled = true;
                    }
                    else
                    {
                        for (i = lowIndex; i <= highIndex; i++)
                        {
                            textArray[i].BackColor = Color.LightBlue;
                        }
                    }
                }
            }
        }
    }

    class Person : IComparable<Person>
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }

        public override string ToString()
        {
            return FirstName + " " + LastName;
        }

        // Compare two Person's names.
        public int CompareTo(Person person)
        {
            return ToString().CompareTo(person.ToString());
        }
    }

    class PersonComparer : IComparer<Person>
    {
        // Compare two Persons.
        public int Compare(Person person1, Person person2)
        {
            string name1 = person1.LastName + "," + person1.FirstName;
            string name2 = person2.LastName + "," + person2.FirstName;
            return name1.CompareTo(name2);
        }
    }
}

