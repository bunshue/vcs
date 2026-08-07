using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for file read/write
using System.Collections;  // 匯入集合物件 for Hashtable

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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            bt_controls_array.Location = new Point(x_st + dx * 4 + 60, y_st + dy * 0);

            groupBox2.Size = new Size(470, 60);
            groupBox2.Location = new Point(x_st + dx * 3, y_st + dy * 2);

            richTextBox1.Size = new Size(470, 480);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 58;
            numText1a.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            numText2a.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            numText3a.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            numText4a.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            numText5a.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            numText6a.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            numText7a.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            numText8a.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            this.Size = new Size(930 + 210, 750);
            this.Text = "vcs_test_all_02_Array";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //整數一維陣列
            int[] myArray1 = new int[5];
            int[] myArray2 = { 1, 2, 3, 4, 5 };

            //整數一維陣列
            int[] A3 = { 75, 66, 60, 70, 80, 85, 90, 100 };
            int[] C = { 1, 3, 5, 7, 9 };
            int[] B = new int[] { 1, 2, 3, 4, 5 };
            int[] a = new int[5] { 0, 1, 2, 3, 4 };
            int[] A = new int[5];
            A[0] = 1;
            A[1] = 2;
            A[2] = 3;
            A[3] = 4;
            A[4] = 5;
            A = new int[] { 1, 9, 4, 5, 8 };	//改值

            richTextBox1.Text += "資料長度 : " + A.Length.ToString() + "\n";
            Array.Sort(A);
            richTextBox1.Text += "排序後 :\n";
            foreach (var v in A)
            {
                richTextBox1.Text += v.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "最大值為 : " + A[4].ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //整數一維陣列
            int[] numArray = new int[8];
            for (int i = 0; i < 8; i++)
            {
                numArray[i] = i;
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //整數一維陣列
            int[] iArrary = new int[] { 1, 5, 13, 6, 10, 55, 99, 2, 87, 12, 34, 75, 33, 47 };
            for (int m = 0; m < iArrary.Length; m++)
            {
                richTextBox1.Text += iArrary[m].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //整數一維陣列
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串一維陣列
            string[] strings2 = new string[10];
            string[] animals1 = { "鼠", "牛", "虎", "兔", "龍" };
            string[] animals2 = new string[] { "鼠", "牛", "虎", "兔", "龍" };
            string[] animals3 = new string[5] { "鼠", "牛", "虎", "兔", "龍" };
            richTextBox1.Text += "共有 " + animals2.Length.ToString() + " 個項目, 分別是:\n";
            foreach (var str in animals1)
            {
                richTextBox1.Text += "字串 : " + str + "\n";
            }

            //字串一維陣列

            string[] names = new string[] { "張三", "李四", "王五" };
            string[] items = new string[] { "螢幕", "滑鼠", "鍵盤" };

            //字串一維陣列
            string[] engNum = new string[] { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串一維陣列
            String[] weekday = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = weekday[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //Color一維陣列
            Color[] colorSet = { Color.Red, Color.Blue, Color.Green, Color.Gray };
            for (int i = 0; i < 4; i++)
            {
                richTextBox1.Text += colorSet[i].Name.ToString() + "\n";
            }

            //Color一維陣列
            Color[] color1 = new Color[5];
            color1[0] = Color.Brown;
            color1[1] = Color.Azure;
            color1[2] = Color.Chartreuse;
            color1[3] = Color.Cyan;
            color1[4] = Color.Gainsboro;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //Point一個點
            Point point = new Point(10, 20);    //宣告一個Point變數
            point.X = 30;   //改值
            point.Y = 40;
            point = new Point(35, 45);          //同時更改XY兩個整數屬性的值

            //Point一維陣列
            Point[] pt = new Point[360];    //一維陣列內有360個Point

            List<Point> Points = new List<Point>();
            Points.Clear();
            int x_st = 570;
            int y_st = 60;
            Points.Add(new Point(x_st, y_st));
            Points.Add(new Point(x_st + 130, y_st));
            Points.Add(new Point(x_st + 130, y_st + 100));
            Points.Add(new Point(x_st + 65, y_st + 150));
            Points.Add(new Point(x_st + 0, y_st + 100));
            Points.Add(new Point(x_st, y_st));

            richTextBox1.Text += "點數 : " + Points.Count.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //二維陣列

            int[,] D = new int[3, 3];
            int[,] E = new int[,]
            {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
            };
            int[,] F = {
                       { 1, 2, 3 },
                       { 4, 5, 6 },
                       { 7, 8, 9 }
                       };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //拜二維陣列 R=3, C=8
            byte[,] newdata = new byte[3, 8];

            //整數二維陣列 R=3, C=8
            int[,] Stu_Sum = new int[3, 8];

            int[,] Score = new int[,]
            {
            { 65, 85, 78, 75, 69 },
            { 66, 55, 52, 92, 47 },
            { 75, 99, 63, 73, 86 },
            { 77, 88, 99, 91, 100 }
            };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //字串二維陣列 R=3, C=6
            string[,] language = new string[3, 6]
            {
            { "正中1", "正中2", "正中3", "正中4", "正中5", "正中6" },
            { "簡中1", "簡中2", "簡中3", "簡中4", "簡中5", "簡中6" },
            { "英語1", "英語2", "英語3", "英語4", "英語5", "英語6" }
            };

            //字串二維陣列 R=3, C=6
            string[,] array2D = new string[,]
            {
            { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
            { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
            { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
            };

            //字串二維陣列 R=5, C=4
            string[,] members = new string[5, 4]
            {
            { "Doraemon", "9/3/2112", "男", "士" },
            { "Dorami", "12/2/2114", "女", "農" },
            { "Mickey", "11/18/1928", "男", "工" },
            { "Benny", "8/14/2000", "男", "商" },
            { "Cony", "4/17/2013", "女", "兵" }
            };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //整數二維陣列 R=2, C=3
            int[,] b = new int[2, 3];
            int[,] c = new int[2, 3]
            {
            { 1, 2, 3 },
            { 4, 5, 6 }
            };

            //整數二維陣列 R=2, C=3
            int[,] myArray = new int[2, 3]
            {
            { 1, 2, 3 },
            { 4, 5, 6 }
            };

            //整數二維陣列 R=3, C=8
            int[,] array2D2 = new int[,]
            {
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算二維陣列所有元素總和
            //整數二維陣列
            int[,] array = new int[,]
            {
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 0, 1, 2, 3, 4, 5, 6, 7 }
            };

            int Total = 0;
            foreach (int element in array)
            {
                Total += element;
            }
            richTextBox1.Text += "此二維陣列的各個元素總和為: " + Total.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲取二維陣列的長度
            //Array.GetLength() 函式獲取 2D 陣列的寬度和高度
            //Array.GetUpperBound() 函式獲取二維陣列的寬度和高度

            /*
            //整數二維陣列
            const int ROWS = 3;
            const int COLUMNS = 8;

            //寫法一
            int[,] array2D = new int[ROWS, COLUMNS]
            {
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 1, 2, 3, 4, 5, 6, 7, 8 },
            { 2, 3, 4, 5, 6, 7, 8, 9 }
            };

            //寫法二
            array2D = new int[,]
            {
            { 0, 1, 2, 3, 4, 5, 6, 7 },
            { 1, 2, 3, 4, 5, 6, 7, 8 },
            { 2, 3, 4, 5, 6, 7, 8, 9 }
            };

            int ROW = array2D.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = array2D.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL
            richTextBox1.Text += "橫列 ROW : " + ROW.ToString() + "\n";
            richTextBox1.Text += "直行 COL : " + COL.ToString() + "\n";

            richTextBox1.Text += "秩 :\t" + array2D.Rank + "\t長度 :\t" + array2D.Length + "\n";  // 獲取維度和整個二維陣列的長度
            for (int i = 0; i < array2D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維 :\t"
                    + array2D.GetLowerBound(i) + " ~ " + array2D.GetUpperBound(i) + "\t長度 :\t" + array2D.GetLength(i) + "\n";
                //                下限                             上限                                     長度
            }

            richTextBox1.Text += "設定數值 :\n";

            //逐一設定 二維陣列
            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    array2D[i, j] = i + j;
                }
            }

            richTextBox1.Text += "二維陣列內容\n";
            PrintArray2D(array2D);
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            //字串二維陣列 R=3, C=6
            string[,] array2D = new string[,]
            {
            { "1", "隋文帝", "541年7月21日", "604年8月13日", "581年3月4日", "604年8月13日"},
            { "2", "隋煬帝", "569年", "618年4月11日", "604年8月21日", "618年4月11日"},
            { "3", "隋恭帝", "605年", "619年9月14日", "617年12月18日", "618年6月18日"},
            };

            int ROW = array2D.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = array2D.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL
            richTextBox1.Text += "橫列 ROW : " + ROW.ToString() + "\n";
            richTextBox1.Text += "直行 COL : " + COL.ToString() + "\n";

            richTextBox1.Text += "秩 :\t" + array2D.Rank + "\t長度 :\t" + array2D.Length + "\n";  // 獲取維度和整個二維陣列的長度
            for (int i = 0; i < array2D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維 :\t"
                    + array2D.GetLowerBound(i) + " ~ " + array2D.GetUpperBound(i) + "\t長度 :\t" + array2D.GetLength(i) + "\n";
                //                下限                             上限                                     長度
            }

            richTextBox1.Text += "二維陣列內容\n";
            PrintArray2D(array2D);

            richTextBox1.Text += "二維陣列內容\n";
            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    richTextBox1.Text += "第(" + i.ToString() + ", " + j.ToString() + ")項 " + array2D[i, j] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //點二維陣列
            //Point二維陣列
            //Point[][] colonPoints = new Point[2][];
            //Point[][] colonPoints = new Point[2][];

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //整數三維陣列
            int[, ,] myArray = new int[2, 3, 4];

            //整數三維陣列宣告：  3Layer X 4Row X 5Column
            //3層 4橫列 5直行
            //LAYER = 3
            //ROW = 4
            //COL = 5
            int[, ,] array3D =
            {
                {
                    { 65, 85, 78, 75, 69 },
                    { 66, 55, 52, 92, 47 },
                    { 75, 99, 63, 73, 86 },
                    { 77, 88, 99, 91, 99 }
                },
                {
                    { 77, 88, 66, 77, 66 },
                    { 65, 66, 88, 55, 77 },
                    { 70, 88, 56, 88, 88 },
                    { 80, 90, 95, 99, 99 }
                },
                {
                    { 55, 67, 56, 98, 67 },
                    { 66, 69, 76, 66, 78 },
                    { 77, 89, 88, 77, 77 },
                    { 88, 89, 99, 97, 88 }
                }
            };

            int LAYER = array3D.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是層數 LAYER
            int ROW = array3D.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是橫列數 ROW
            int COL = array3D.GetUpperBound(2) + 1;  // 取得指定維度的上限，第2項就是直行數 COL
            int zz = array3D.GetUpperBound(2) + 1;  // 取得指定維度的上限，第2項就是直行數 ROW ??

            richTextBox1.Text += "層數 LAYER : " + LAYER.ToString() + "\n";
            richTextBox1.Text += "橫列 ROW : " + ROW.ToString() + "\n";
            richTextBox1.Text += "直行 COL : " + COL.ToString() + "\n";

            richTextBox1.Text += "秩 :\t" + array3D.Rank + "\t長度 :\t" + array3D.Length + "\n";  // 獲取維度和整個二維陣列的長度

            for (int i = 0; i < array3D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (array3D.GetUpperBound(i) + 1).ToString() + "\n";
            }

            for (int i = 0; i < LAYER; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 層 :\n";
                for (int j = 0; j < ROW; j++)
                {
                    richTextBox1.Text += "第 " + i.ToString() + " 列 :\n";
                    for (int k = 0; k < COL; k++)
                    {
                        richTextBox1.Text += "第(" + i.ToString() + ", " + j.ToString() + ", " + k.ToString() + ")項 " + array3D[i, j, k] + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //三維陣列 測試中
            int[, ,] array3Da = new int[5, 3, 8];    //Row = 3, Column = 8

            richTextBox1.Text += "Rank = " + array3Da.Rank.ToString() + "\n";

            richTextBox1.Text += "三維陣列內容\n";
            PrintArray(array3Da);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //多維陣列

            String[, ,] items = new String[,,] {
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

        private void button3_Click(object sender, EventArgs e)
        {
            //鋸齒陣列	//不規則陣列
            char[][] ch = new char[][]
            {
                new char[] {'a','b','c'},
                new char[] {'c','d','e','f','g','h'},
                new char[] {'w','x','y','z'}
            };

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            //秩和維度的上下限

            string[] array1D = new string[] { "鼠", "牛", "虎", "兔", "龍" };

            richTextBox1.Text += "秩 :\t" + array1D.Rank + "\t長度 :\t" + array1D.Length + "\n";  // 獲取維度和整個一維陣列的長度

            for (int i = 0; i < array1D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維 :\t"
                    + array1D.GetLowerBound(i) + " ~ " + array1D.GetUpperBound(i) + "\t長度 :\t" + array1D.GetLength(i) + "\n";
                //                下限                             上限                                     長度
            }

            for (int i = array1D.GetLowerBound(0); i <= array1D.GetUpperBound(0); i++)
            {
                richTextBox1.Text += array1D[i] + "\n";
            }

            //------------------------------------------------------------  # 60個

            int[,] xxx = {
                       { 2, 3, 2 },
                       { 5, 6, 1 },
                       { 4, 6, 2 },
                       { 4, 6, 3 }
                       };

            //int[, , , ,] yyy;

            richTextBox1.Text += "len = " + xxx.Length.ToString() + "\n";
            richTextBox1.Text += "rank = " + xxx.Rank.ToString() + "\n";
            //richTextBox1.Text += "rank = " + yyy.Rank.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int[, , ,] dim = new int[2, 5, 3, 7];
            richTextBox1.Text += "rank = " + dim.Rank.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //int[] num = { { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } } };
            //richTextBox1.Text += "rank = " + num.Rank.ToString() + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            // Array方法

            richTextBox1.Text += "各種Array()方法\n";

            /*
            Array.Sort(Values);
            Array.Reverse(Values);
            Array.Copy(array1, array2, array1.Length);
            Array.BinarySearch(Values, target);
            Array.IndexOf(score, 100);   //搜尋第一個滿分學生
            Array.CreateInstance(typeof(int), 3, 4);
            Array.CreateInstance(typeof(int), 2, 3, 4);
            Array.Resize(ref score, score.Length + 1);    //陣列大小+1
            Array.Copy(array_data, 0, array_data, offset, array_data.Length - offset);
            Array.Copy(array_data, offset, array_data, 0, array_data.Length - offset);
            */

            //------------------------------------------------------------  # 60個

            //一列排序 內建函數1
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //一列排序 內建函數2
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //Array.Copy.
            int[] array1 = new int[1000];
            int[] array2 = new int[1000];

            for (int i = 0; i < array1.Length; i++)
                array1[i] = i;

            Array.Copy(array1, array2, array1.Length);  //從前array1拷貝長度陣列到後array2，長度array1.Length，會快得多，約7倍快

            richTextBox1.Text += "Array1\t";
            for (int i = 0; i < array1.Length; i += 60)
            {
                richTextBox1.Text += array1[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Array2\t";
            for (int i = 0; i < array2.Length; i += 60)
            {
                richTextBox1.Text += array2[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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

            //------------------------------------------------------------  # 60個

            // Array方法

            // 建立一個整數二維陣列 R=3, C=4
            Array myArr2D = Array.CreateInstance(typeof(int), 3, 4);

            int ROW = myArr2D.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = myArr2D.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL
            richTextBox1.Text += "橫列 ROW : " + ROW.ToString() + "\n";
            richTextBox1.Text += "直行 COL : " + COL.ToString() + "\n";

            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    //SetValue 設定資料
                    myArr2D.SetValue((i * 10) + (j * 1), i, j);
                }
            }

            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    //GetValue 取得資料
                    int value = (int)myArr2D.GetValue(i, j);
                    richTextBox1.Text += value + " ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "秩 :\t" + myArr2D.Rank + "\t長度 :\t" + myArr2D.Length + "\n";  // 獲取維度和整個二維陣列的長度
            for (int i = 0; i < myArr2D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維 :\t"
                    + myArr2D.GetLowerBound(i) + " ~ " + myArr2D.GetUpperBound(i) + "\t長度 :\t" + myArr2D.GetLength(i) + "\n";
                //                下限                             上限                                     長度
            }

            richTextBox1.Text += "Array內容\n";
            //TBD

            //------------------------------------------------------------  # 60個

            // 建立一個整數三維陣列
            Array myArr3D = Array.CreateInstance(typeof(int), 2, 3, 4);
            for (int i = 0; i <= myArr3D.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= myArr3D.GetUpperBound(1); j++)
                {
                    for (int k = 0; k <= myArr3D.GetUpperBound(2); k++)
                    {
                        //SetValue 設定資料
                        myArr3D.SetValue((i * 100) + (j * 10) + k, i, j, k);
                    }
                }
            }
            for (int i = 0; i <= myArr3D.GetUpperBound(0); i++)
            {
                for (int j = 0; j <= myArr3D.GetUpperBound(1); j++)
                {
                    for (int k = 0; k <= myArr3D.GetUpperBound(2); k++)
                    {
                        //GetValue 取得資料
                        int value = (int)myArr3D.GetValue(i, j, k);
                        richTextBox1.Text += value + " ";
                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "秩 :\t" + myArr3D.Rank + "\t長度 :\t" + myArr3D.Length + "\n";  // 獲取維度和整個二維陣列的長度
            for (int i = 0; i < myArr3D.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維 :\t"
                    + myArr3D.GetLowerBound(i) + " ~ " + myArr3D.GetUpperBound(i) + "\t長度 :\t" + myArr3D.GetLength(i) + "\n";
                //                下限                             上限                                     長度
            }

            richTextBox1.Text += "Array內容\n";
            //TBD
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void PrintArray1D(int[] array_data)
        {
            for (int i = 0; i < array_data.Length; i++)
            {
                if (i == (array_data.Length - 1))
                {
                    richTextBox1.Text += array_data[i].ToString();
                }
                else
                {
                    richTextBox1.Text += array_data[i].ToString() + " ";
                }
            }
            richTextBox1.Text += "\n";
        }

        private void button8_Click(object sender, EventArgs e)
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
            PrintArray1D(Values);

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

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "IndexOf的用法\n";

            //字串一維陣列
            string[] stu = new string[] { "趙一", "林二", "張三", "李四", "王五" };

            //整數一維陣列
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

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
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

        class AnimalData
        {
            public string Name_C { get; set; }
            public string Name_E { get; set; }
            public string Name_N { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public DateTime Birthday { get; set; }
        }

        private void button11_Click(object sender, EventArgs e)
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

            //二維陣列排序
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

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "一份歌手與歌曲的對照表, 依排名排序  依歌曲名排序\n";

            //song字串陣列存放歌曲名稱
            string[] song = new string[] { "姐姐", "天后", "我的歌聲裡", "東區東區", "勢在必行", "末班車", "一個人想著一個人", "愛你", "阿飛的小蝴蝶", "王妃" };
            //singer字串陣列存放歌手姓名
            string[] singer = new string[] { "謝金燕", "陳勢安", "曲婉婷", "八三夭", "陳勢安", "蕭煌奇", "曾沛慈", "陳芳語", "蕭敬騰", "蕭敬騰" };

            //整數一維陣列
            int[] no = new int[10];  // no整數陣列存放排名

            int i;
            for (i = 0; i < no.Length; i++) //設定no陣列的初值
            {
                no[i] = i + 1;
            }

            richTextBox1.Text += "依排名排序\n";
            //整數一維陣列
            int[] temp1 = new int[no.Length];  // 宣告temp整數陣列，大小和no陣列相同
            no.CopyTo(temp1, 0);   //將no陣列的內容複製到temp陣列
            Array.Sort(no, song);   //nog陣列遞增排序，song陣列同步調整
            Array.Sort(temp1, singer);   //temp陣列遞增排序，singer陣列同步調整
            string msg1 = "排名" + "\t" + "歌手" + "\t" + "歌曲" + Environment.NewLine;
            for (i = 0; i < song.Length; i++)
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
            for (i = 0; i < song.Length; i++)
            {
                msg2 += no[i].ToString() + "\t" + singer[i] + "\t" + song[i] + Environment.NewLine;
            }
            richTextBox1.Text += msg2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //排序
            string[] name = { "王一", "李二", "陳三", "趙四", "馬五" };

            //整數一維陣列
            int[] score = { 78, 80, 50, 96, 69 };

            //整數一維陣列
            int[] rank = new int[5];
            //int i;
            int j;
            for (i = 0; i < 5; i++)
            {
                rank[i] = 1; //先假設名次為1

                // 依序和他人比較，只要有人較高分，其名次即遞增1
                for (j = 0; j < 5; j++)
                {
                    if (score[j] > score[i])
                    {
                        rank[i] += 1;
                    }
                }
            }

            for (i = 0; i < 5; i++)
            {
                richTextBox1.Text += name[i] + "\t第" + rank[i].ToString() + "名\n";
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //二陣列排序
            int[] scores = new int[] { 80, 50, 60, 90, 70 };
            //string[] animals = new string[] {"Mary", "Jack", "Tom", "David", "Grace" };  //寫法同下
            string[] animals = { "Mary", "Jack", "Tom", "David", "Grace" };

            richTextBox1.Text += "排序前：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + animals[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";

            Array.Sort(animals, scores);   //以animals為準排序，scores跟著
            richTextBox1.Text += "依姓名排序：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + animals[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";

            Array.Sort(scores, animals);   //以scores為準排序，animals跟著
            richTextBox1.Text += "依成績排序：\n";
            for (int i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + animals[i] + "\t" + scores[i] + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //二陣列排序2 排名次
            int i; // 宣告 i 為for迴圈計數變數
            // 建立RoleName[0]~RoleName[4]用來存放角色姓名
            string[] RoleName = new string[] { "魯夫", "喬巴", "羅賓", "香吉士", "騙人布" };
            // 建立Money[0]~Money[4] 用來存放角色的懸賞金額

            //整數一維陣列
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

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
            //姓名依名排序
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
            for (int i = 0; i < people.Length; i++)
            {
                richTextBox1.Text += people[i] + "\n";
            }

            richTextBox1.Text += "依名排序\n";
            Array.Sort(people);

            for (int i = 0; i < people.Length; i++)
            {
                richTextBox1.Text += people[i] + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            //排名次
            int i;
            int j;
            //整數一維陣列
            int[] scores = new int[] { 80, 50, 60, 90, 80 };
            int[] scores_new = new int[5];
            int[] rank = new int[5];
            //string[] animals = new string[] {"Mary", "Jack", "Tom", "David", "Grace" };  //寫法同下
            string[] animals = { "Mary", "Jack", "Tom", "David", "Grace" };

            richTextBox1.Text += "排序前：\n";
            for (i = 0; i < scores.Length; i++)
            {
                richTextBox1.Text += (i + 1).ToString() + "\t" + animals[i] + "\t" + scores[i] + "\n";
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

                //richTextBox1.Text += i.ToString() + "\t" + animals[i] + "\t" + scores_new[i] + "\n";
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
                richTextBox1.Text += (i + 1).ToString() + "\t" + animals[i] + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
            }
            richTextBox1.Text += "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
            //Array測試
            int[] total = new int[4];
            int[,] gdp =
            {
            {250872, 259564, 288579, 283280 },
            { 3208572, 3541387, 401368, 4244227},
            { 7804898, 8071281, 8369219, 8643443}
            };

            //GetLength()方法分別取得列(row)和欄(column)的值
            int row = gdp.GetLength(0);
            int column = gdp.GetLength(1);

            //雙層for廻圈，外層for先讀取row數
            for (int outer = 0; outer < row; outer++)
            {
                //內層for讀取column數
                for (int inner = 0; inner < column; inner++)
                {
                    //欄寬14，NO表示含有千位分號但小數位數是零
                    //Write($"{gdp[outer, inner],14:N0}");
                }
                richTextBox1.Text += "\n";
                total[0] += gdp[outer, 0];//101年gdp合計
                total[1] += gdp[outer, 1];//102年gdp合計
                total[2] += gdp[outer, 2];//103年gdp合計
                total[3] += gdp[outer, 3];//104年gdp合計
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < total.Length; i++)
            {
                richTextBox1.Text += total[i] + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //宣告鋸齒陣列為隱含型別
            var subject = new[]
            {
                new[] {"Tomas", "國文", "英文", "計算機概論" },
                new[] {"Mary", "數學", "資料庫"},
                new[] {"Peter", "數學","應用文", "多媒體", "程式設計"}
            };

            //外層for廻圈，取屬性subject.Length為列數
            for (var outer = 0; outer < subject.Length; outer++)
            {
                //內層for廻圈，取屬性subject[outer].Length為欄數
                for (var inner = 0; inner < subject[outer].Length; inner++)
                {
                    //-6表示欄寬為6，負號為靠左對齊
                    //Write($"{subject[outer][inner],-6}");
                }
                //WriteLine();//
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //三維 array
            /*
                        //宣告多維陣列並初始化
                        int[,,] arr3D = new int[2, 2, 3] {
                        { { 1, 2, 3 }, { 12, 14, 16 } },
                        { { 21, 24, 27 }, { 30, 35, 40 } } };

                        //Write("第2個表格，第2列 第2欄 元素：");
                        //WriteLine($"{arr3D[1, 1, 1]}");

                        //GetLength()方法取得多維陣列的Table, Row, Column
                        int table = arr3D.GetLength(0);
                        int row = arr3D.GetLength(1);
                        int column = arr3D.GetLength(2);

                        //Write($"有{table}個表格，");
                        //Write($"是 {row} * {column} 二維表格\n");

                        //3層for廻圈；第一層先讀表格(table)
                        for (int first = 0; first < table; first++)
                        {
                            //WriteLine($"表格 {first + 1} -------");

                            //第二層for廻圈讀列(row)
                            for (int second = 0; second < row; second++)
                            {
                                //第三層for廻圈讀欄(column)
                                for (int thrid = 0; thrid < column; thrid++)
                                {
                                    //依序輸出多維陣列的元素
                                    //Write($"{arr3D[first, second, thrid],3} |");
                                }

                                //WriteLine();   //換行

                            }//end second for-loop

                            //WriteLine();   //換行

                        }//end first for-loop
                    }//end Main()
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            int num = 10;
            double sum = 0;
            double[] tall = new double[num];  // 建立tall倍精確陣列存放每位的身高

            for (int i = 0; i <= tall.GetUpperBound(0); i++)
            {
                Console.Write("請輸入第 {0} 位身高(公分) : ", i + 1);
                tall[i] = double.Parse(Console.ReadLine()); //輸入身高逐一存入陣列  
            }

            foreach (double height in tall)  // 計算總人數身高的加總
                sum += height;   // 將所有陣列元素依序加總指定給sum           

            //richTextBox1.Text +="\n=== " + i.ToString("#") + " 位平均身高:" + (sum / num).ToString("00.00"));// 顯示平均身高
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //宣告陣列並初始化
            int[] number = { 124, 65, 3314, 81, 92, 65 };

            //foreach廻圈讀取陣列元素
            foreach (int item in number)
            {
                //Write($"{item,4} ");
            }
            //WriteLine();//換行

            int first = Array.IndexOf(number, 65);
            //WriteLine($"從前方找65，索引值 {first}");

            int tail = Array.LastIndexOf(number, 65);
            //WriteLine($"從末端找65，索引值 {tail}");

            int unknown = Array.IndexOf(number, 33);
            //WriteLine($"從前方找33，索引值 {unknown}");

            richTextBox1.Text += "------------------------------\n";  // 30個

            string[] ng_reason = new string[] { "無資料", "鏡頭脫落", "影像有黑影", "Ring上有異物", "Ring未組裝好", "Ring裂痕", "LED脫落", "LED不亮", "LED有異物", "漏光", "其他：" };

            //最大值，剛好為陣列索引上限
            int num = ng_reason.GetUpperBound(0);
            richTextBox1.Text += "num = " + num.ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //IEnumerator

            // 宣告並建立含有10個字元的字串陣列
            String[] myAry = new String[10];
            // 設定陣列初值
            myAry[0] = "第三次";
            myAry[1] = "工業革命";
            myAry[2] = "是";
            myAry[3] = "3D 列印";

            // 顯示陣列的內容
            int idx = 0;
            //實作名稱myEnumerator列舉器, 透過GetEnumerator方法來讀取myAry陣列
            // 此時指標指到myAry陣列第一個陣列元素的前面
            IEnumerator myEnumerator = myAry.GetEnumerator();

            Console.WriteLine("myAry 陣列元素內容如下 :\n");
            // 依序透過MoveNext方法指標下移一個項目,current屬性讀取陣列元素
            while ((myEnumerator.MoveNext()) && (myEnumerator.Current != null))
            {
                Console.WriteLine("myAry[{0}] = {1}", idx++, myEnumerator.Current);
            }

            //------------------------------------------------------------  # 60個

        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
            //Array 1
            // 產生一個含有五個陣列元素的整數陣列
            Array ary1D = Array.CreateInstance(typeof(Int32), 5);
            // 設定陣列初值依序為:1,2,3,4,5
            for (int i = ary1D.GetLowerBound(0); i <= ary1D.GetUpperBound(0); i++)
            {
                ary1D.SetValue(i + 1, i);
            }

            // 顯示陣列初值            
            IEnumerator myEnumerator = ary1D.GetEnumerator();
            int k = 0;
            int cols = ary1D.GetLength(ary1D.Rank - 1);
            while (myEnumerator.MoveNext())
            {
                if (k < cols)
                {
                    k++;
                }
                else
                {
                    Console.WriteLine();
                    k = 1;
                }
                Console.Write(" {0}. ary1D[{1}] = {2} \n", k, k, myEnumerator.Current);
            }
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
            //Array 2
            // 產生 2x3 字串陣列並設定初值
            Array ary2D = Array.CreateInstance(typeof(String), 2, 3);

            for (int i = ary2D.GetLowerBound(0); i <= ary2D.GetUpperBound(0); i++)
            {
                for (int j = ary2D.GetLowerBound(1); j <= ary2D.GetUpperBound(1); j++)
                {
                    ary2D.SetValue("註標 " + i + "," + j, i, j);
                }
            }

            // 顯示陣列的資料
            Console.WriteLine(" 二維陣列包含下列資料 :");

            IEnumerator myEnumerator = ary2D.GetEnumerator();

            int r = 0;  // row 列
            int c = 0;  // col 欄

            int cols = ary2D.GetLength(ary2D.Rank - 1);

            while (myEnumerator.MoveNext() && (myEnumerator.Current != null))
            {
                if (r > cols || c >= 3)
                {
                    Console.WriteLine();
                    r++; c = 0;
                }
                Console.Write(" ary2D[{0},{1}]={2} , ", r, c++, myEnumerator.Current);
            }

        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void PrintArray2D<T>(T[,] arr)
        {
            richTextBox1.Text += "秩 :\t" + arr.Rank + "\t長度 :\t" + arr.Length + "\n";  // 獲取維度和整個二維陣列的長度

            int ROW = arr.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = arr.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL
            richTextBox1.Text += "橫列 ROW : " + ROW.ToString() + "\n";
            richTextBox1.Text += "直行 COL : " + COL.ToString() + "\n";

            for (int i = 0; i < ROW; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 列 :\t";
                for (int j = 0; j < COL; j++)
                {
                    richTextBox1.Text += arr[i, j].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void PrintArray<T>(T[, ,] arr)
        {
            richTextBox1.Text += "秩 :\t" + arr.Rank + "\t長度 :\t" + arr.Length + "\n";  // 獲取維度和整個二維陣列的長度
            for (int i = 0; i < arr.Rank; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + arr.GetLength(i).ToString() + "\n";
                richTextBox1.Text += "第 " + i.ToString() + " 維的長度 : " + (arr.GetUpperBound(i) + 1).ToString() + "\n";
            }

            int ROW = arr.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = arr.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL

            for (int i = 0; i < ROW; i++)
            {
                for (int j = 0; j < COL; j++)
                {
                    //richTextBox1.Text += arr[i, j].ToString() + "\t";
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_controls_array_Click(object sender, EventArgs e)
        {
            //把控件做成陣列

            //控件一維陣列
            TextBox[] textArray = new TextBox[] { numText1a, numText2a, numText3a, numText4a, numText5a, numText6a, numText7a, numText8a };

            for (int i = 0; i < 8; i++)
            {
                textArray[i].Multiline = true;
                textArray[i].Size = new Size(48, 32);
                textArray[i].BackColor = Color.Pink;
                textArray[i].Text = i.ToString();
            }

            //------------------------------------------------------------  # 60個

            // 製作一個PictureBox Array

            //控件陣列 宣告
            PictureBox[] pbox = { pictureBox1, pictureBox2, pictureBox3, pictureBox4 }; //same

            /* same
            PictureBox[] pbox = new PictureBox[4];
            //控件陣列 使用
            pbox[0] = this.pictureBox1;
            pbox[1] = this.pictureBox2;
            pbox[2] = this.pictureBox3;
            pbox[3] = this.pictureBox4;
            */
            pbox[0].BackColor = Color.Red;
            pbox[1].BackColor = Color.Green;
            pbox[2].BackColor = Color.Blue;
            pbox[3].BackColor = Color.Yellow;

            // 製作一個CheckBox Array
            //CheckBox[] BreakfastControls, LunchControls, DinnerControls;
            //BreakfastControls = new CheckBox[] { cb00, cb01, cb02 };
            //LunchControls     = new CheckBox[] { cb10, cb11, cb12 };
            //DinnerControls    = new CheckBox[] { cb20, cb21, cb22 };
        }

        //------------------------------------------------------------  # 60個
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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
目前看到的 GetLowerBound(n) 下限都是從0開始 改成0就好

for (int i = myArr2D.GetLowerBound(0); i < ROW; i++)
for (int j = myArr2D.GetLowerBound(1); j < COL; j++)

*/


/*
        //已沒人用
        private void PrintArray2Db(double[,] arr)
        {
            int ROW = arr.GetUpperBound(0) + 1;  // 取得指定維度的上限，第0項就是橫列數 ROW
            int COL = arr.GetUpperBound(1) + 1;  // 取得指定維度的上限，第1項就是直行數 COL

            richTextBox1.Text += "PrintArray\n";
            for (int i = 0; i < ROW; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 列 :\t";
                for (int j = 0; j < COL; j++)
                {
                    richTextBox1.Text += arr[i, j].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

*/

/*
            // 陣列的GetUpperBound()方法可用來取得某一維度的上限
            // 因此RoleName.GetUpperBound(0) 會傳回 4
            for (int i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                //richTextBox1.Text +="{0}\t{1}", RoleName[i], Money[i]);
                richTextBox1.Text += RoleName[i] + "\t" + Money[i].ToString("#,#") + "\n";
            }

6060


Jagged Array
string[][] trans = new string[30][];
trans有30項 每項長度不定 需要動態配置長度
ex:
	trans[5] = new string[10];
	第5項長度10個字串
	trans[5][0] = "aa";
	trans[5][1] = "bb";
	trans[5][2] = "cc";
		:
		:
取得單項長度 trans[5].Length



Point[] pntArr = new Point[3];


*/