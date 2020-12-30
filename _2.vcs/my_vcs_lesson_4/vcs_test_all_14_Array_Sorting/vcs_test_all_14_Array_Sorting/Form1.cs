using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for file read/write

namespace vcs_test_all_14_Array_Sorting
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
            button36.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 12);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //陣列宣告範例
            int[] A = new int[5];
            int[] B = new int[] { 1, 2, 3, 4, 5 };
            int[] C = { 1, 3, 5, 7, 9 };
            int[,] D = new int[3, 3];
            int[,] E = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[,] F = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[, ,] G = new int[3, 4, 5];
            Point[] pt = new Point[360];    //一維陣列內有360個Point
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //一維陣列用法：
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
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //二維陣列用法：
            int[,] b = new int[2, 3];
            int[,] c = new int[2, 3] { { 1, 2, 3 }, { 4, 5, 6 } };
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
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //三維陣列宣告：
            int[, ,] Score = { { { 65, 85, 78, 75, 69 }, { 66, 55, 52, 92, 47 }, { 75, 99, 63, 73, 86 }, { 77, 88, 99, 91, 99 } }, { { 77, 88, 66, 77, 66 }, { 65, 66, 88, 55, 77 }, { 70, 88, 56, 88, 88 }, { 80, 90, 95, 99, 99 } }, { { 55, 67, 56, 98, 67 }, { 66, 69, 76, 66, 78 }, { 77, 89, 88, 77, 77 }, { 88, 89, 99, 97, 88 } } };
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //字串陣列的寫法(一維)：
            string[] atoms = { "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "魔羯座" };

            //字串陣列的寫法(二維)：
            String[,] language = new string[3, 6] { { "正中1", "正中2", "正中3", "正中4", "正中5", "正中6" }, { "簡中1", "簡中2", "簡中3", "簡中4", "簡中5", "簡中6" }, { "英語1", "英語2", "英語3", "英語4", "英語5", "英語6" } };

            //字串陣列的寫法(一維)：
            String[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

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
            //Console.WriteLine(dim.Rank);//結果 4

            //int[] num = { { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } }, { { 5, 6 }, { 7, 8 } } };
            //richTextBox1.Text += "rank = " + num.Rank.ToString() + "\n";
            //Console.WriteLine(num.Rank);//結果 3
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

            string filename = "C:\\______test_files\\my_2d_array.txt";
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

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

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

        }

        private void button25_Click(object sender, EventArgs e)
        {

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

        }

        private void button30_Click(object sender, EventArgs e)
        {

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
    }
}
