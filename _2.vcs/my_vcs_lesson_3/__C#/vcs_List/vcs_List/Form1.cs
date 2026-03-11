using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;

namespace vcs_List
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

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_List";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //類別List
            List<Person> persons1 = new List<Person>();
            persons1.Add(new Person("张三", "男", 20, 1500));
            persons1.Add(new Person("王成", "男", 32, 3200));
            persons1.Add(new Person("李丽", "女", 19, 1700));
            persons1.Add(new Person("何英", "女", 35, 3600));
            persons1.Add(new Person("何英", "女", 18, 1600));

            //Console.WriteLine("泛型分组如下：");
            richTextBox1.Text += "泛型分组如下：\n";

            var ls = persons1.GroupBy(a => a.Sex).Select(g => (new { sex = g.Key, count = g.Count(), ageC = g.Sum(item => item.Age), moneyC = g.Sum(item => item.Money) }));
            foreach (var item in ls)
            {
                //Console.WriteLine(item.sex + "  " + item.count + "  " + item.ageC + "   " + item.moneyC);
                richTextBox1.Text += item.sex + "  " + item.count + "  " + item.ageC + "   " + item.moneyC + "\n";
            }

            //3030

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //類別List

            List<Member> m = new List<Member>();   // 泛型           

            m.Add(new Member() { Name = "David", Select = true, Score = 70 });
            m.Add(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Add(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Add(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine(" === 泛型 LIst 操作不需強制轉換 .... \n");
            foreach (var item in m)
            {
                Console.WriteLine("姓名:{0} \t 選課:{1} \t 成績:{2} \n ", item.Name, item.Select ? "是" : "否", item.Score.ToString());
                // Console.WriteLine(item.ToString());  // 執行此行 會呼叫覆寫覆類別 ToString()方法
            }
            Console.Read();
        }

        void show_list(List<int> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //一維整數串列

            //不用宣告長度的陣列(Array)
            // 宣告intList3 為List
            // 以下List 裡為int 型態
            //建立 一維整數串列
            List<int> intList3 = new List<int>();

            // 在List 裡新增int 整數
            intList3.Add(12);
            intList3.Add(34);
            intList3.Add(56);

            richTextBox1.Text += "intList3 has" + intList3.Count.ToString() + " elements\n";

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (int ii in intList3)
            {
                richTextBox1.Text += "\t" + ii.ToString();
            }
            richTextBox1.Text += "\n";

            //3030

            //List之搜尋語法1
            //這裡使用Where擴展方法獲取大於4的值。

            //建立 一維整數串列
            List<int> intList4 = new List<int>() { 1, 2, 3, 4, 5 };

            var maxIntList = intList4.Where(i => i > 4);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            intList4.Add(6);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            //3030

            //List之搜尋語法2
            //建立 一維整數串列
            List<int> intList5 = new List<int>() { 1, 2, 3, 4, 5 };

            maxIntList = intList5.Where(i => i > 4).ToList();//調用ToList()方法

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            intList5.Add(6);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            maxIntList = intList5.Where(i => i > 4).ToList();//調用ToList()方法

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            //3030

            int N = 10;
            Random rr = new Random();

            //建立 一維整數串列
            List<int> intList1 = new List<int>();   //宣告int型態的List

            /*  不均勻分配
            intList1.Add('A');
            intList1.Add('A');
            intList1.Add('A');
            intList1.Add('B');
            intList1.Add('C');
            */

            for (int i = 0; i < N; i++)
            {
                intList1.Add(rr.Next(10));
            }

            /*
            //特定分配
            for (int i = 50; i <= 57; i++)
                //ASCII碼，找出數字
                intList1.Add((char)i); //從2開始，排除了0，1，放入列表
            */

            richTextBox1.Text += "建立長度為 " + N.ToString() + " 的List\t內容:\n";
            show_list(intList1);

            //3030

            //建立 一維整數串列
            List<int> intList2 = new List<int>();   //宣告int型態的List

            for (int i = 0; i < N; i++)
            {
                intList2.Add(i);
            }
            richTextBox1.Text += "建立長度為 " + N.ToString() + " 的List\t內容:\t";
            show_list(intList2);

            richTextBox1.Text += "List亂序\t內容:\t";
            intList2 = get_random_list(intList2);

            show_list(intList2);
        }

        //建立 一維整數串列
        List<int> get_random_list(List<int> ContentList)
        {
            Random random = new Random();
            //建立 一維整數串列
            List<int> intList = new List<int>();
            foreach (int item in ContentList)
            {
                intList.Insert(random.Next(intList.Count), item);
            }
            return intList;
        }

        void show_list(List<string> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //一維字串串列

            // 宣告stringList3 為List
            // 以下List 裡為string 型態
            //建立 一維字串串列
            List<string> stringList3 = new List<string>();

            // 在List 裡新增string 字串
            stringList3.Add("lion");
            stringList3.Add("mouse");
            stringList3.Add("cat");
            stringList3.Add("dog");

            richTextBox1.Text += "stringList3 has" + stringList3.Count.ToString() + " elements\n";

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in stringList3)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "經過排序：\n";
            stringList3.Sort();
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in stringList3)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "增加內容：\n";
            stringList3.Insert(2, "elephant");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in stringList3)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "刪除內容：\n";
            stringList3.Remove("cat");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in stringList3)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            //3030

            //建立 一維字串串列
            List<string> stringList2 = new List<string>();   //宣告string型態的List

            stringList2.Add("john");
            stringList2.Add("mary");
            stringList2.Add("david");
            stringList2.Add("bill");
            stringList2.Add("tom");
            stringList2.Add("sue");
            stringList2.Add("larry");
            stringList2.Add("michael");
            stringList2.Add("pepa");
            stringList2.Add("eric");

            richTextBox1.Text += "一維字串串列內容 :\n";
            show_list(stringList2);

            richTextBox1.Text += "移除一些:\n";
            stringList2.Remove("sue");
            stringList2.Remove("john");
            stringList2.RemoveAt(2); //上述已經移除後, 再移除第2個
            show_list(stringList2);

            richTextBox1.Text += "新增一些:\n";
            stringList2.Insert(2, "rebecca");
            stringList2.Insert(6, "sharon");
            stringList2.Insert(1, "emily");
            show_list(stringList2);

            //3030

            //建立 一維字串串列
            List<String> stringList1 = new List<String>();

            stringList1.Add("AAA");
            stringList1.Add("BBB");
            stringList1.Add("CCC");
            stringList1.Add("DDD");
            stringList1.Add("EEE");

            stringList1.Add("FFF");
            stringList1.Add("GGG");
            stringList1.Add("HHH");
            stringList1.Add("III");
            stringList1.Add("JJJ");

            //在第3項前加一個項目
            richTextBox1.Text += "添加一項在第3項";
            stringList1.Insert(3, "xxxxxxxxxxxxxxxx");

            //刪除List資料3~7
            //richTextBox1.Text += "capacity : " + stringList1.Capacity.ToString() + "\n";
            //stringList1.RemoveAt(3);
            stringList1.RemoveRange(3, 5);
            richTextBox1.Text += "刪除此List之第3項開始的5項";

            //刪除List第3項
            stringList1.RemoveAt(3);
            richTextBox1.Text += "刪除此List之第3項";


            //顯示串列資料

            richTextBox1.Text += "共有 " + stringList1.Count.ToString() + " 個字串\n";

            // 取出單一個List 裡的值，如同陣列(Array)用法
            for (int i = 0; i < stringList1.Count; i++)
            {
                richTextBox1.Text += stringList1[i] + "\n";
            }

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "\n可用foreach 取出List 裡的值\n";
            foreach (string sss in stringList1)
            {
                richTextBox1.Text += sss + "\n";
            }




        }

        private void button4_Click(object sender, EventArgs e)
        {
            //二維整數串列
            List<List<int>> list7 = new List<List<int>>();

            //建立 一維整數串列
            List<int> intList7 = new List<int>();
            intList7.Add(0);
            intList7.Add(0);
            list7.Add(intList7);
            list7.Add(intList7);
            list7.Add(intList7);
            list7.Add(intList7);
            list7.Add(intList7);

            int i;
            for (i = 0; i < list7.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\n";
                list7[i][0] = i;
                list7[i][1] = list7.Count - i;
            }

            for (i = 0; i < list7.Count; i++)
            {
                richTextBox1.Text += "list7[" + i.ToString() + "][0] = " + list7[i][0].ToString() + " list7[" + i.ToString() + "][1] = " + list7[i][1].ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //二維字串串列
            List<List<string>> list4 = new List<List<string>>();
            list4.Add(new List<string>() { "A001", "David" });
            list4.Add(new List<string>() { "A002", "John" });
            list4.Add(new List<string>() { "A003", "Tom" });
            richTextBox1.Text += "學號\t->\t姓名\n";
            foreach (var showlist in list4)
            {
                richTextBox1.Text += showlist[0] + "\t->\t" + showlist[1] + "\n";
            }

            //3030

            //二維字串串列
            List<List<string>> list8 = new List<List<string>>();
            list8.Add(new List<string>() { "0,0 : Mike", "0, 1: Jane" });
            list8.Add(new List<string>() { "1,0 : Jack", "1, 1: John" });

            list8[0][0] = "0,0: Kyle";

            richTextBox1.Text += "result : " + list8[0][0] + "\n"; // 輸出: 0,0: Kyle
            richTextBox1.Text += "result : " + list8[0][1] + "\n"; // 輸出: 0,1: Jane
            richTextBox1.Text += "result : " + list8[1][0] + "\n"; // 輸出: 1,0: Jack
            richTextBox1.Text += "result : " + list8[1][1] + "\n"; // 輸出: 1,1: John

            //3030

            //二維字串串列

            //建立 二維字串串列
            List<string[]> stringList4 = new List<string[]>();
            stringList4.Add(new string[] { "AAA", "BBB" });
            stringList4.Add(new string[] { "CCC", "DDD" });
            stringList4.Add(new string[] { "CCC", "DDD" });
            richTextBox1.Text += "Result : " + stringList4[1][1].ToString() + "\n";
            richTextBox1.Text += "Count : " + stringList4.Count.ToString() + "\n";

            //3030

            //建立 二維字串串列
            List<string[]> stringList5 = new List<string[]>();

            stringList5.Clear();
            for (int i = 0; i < 10; i++)
            {
                stringList5.Add(new string[] { "aaaa" + i.ToString(), "bbbb" + i.ToString(), DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
            }

            if (stringList5.Count > 0)
            {
                richTextBox1.Text += "共有 " + stringList5.Count.ToString() + " 筆資料\t分別是:\n";
                for (int i = 0; i < stringList5.Count; i++)
                {
                    richTextBox1.Text += "stringList5[" + i.ToString() + "][0] = " + stringList5[i][0].ToString()
                        + "\tstringList5[" + i.ToString() + "][1] = " + stringList5[i][1].ToString()
                        + "\tstringList5[" + i.ToString() + "][2] = " + stringList5[i][2].ToString() + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //建立 二維字串串列
            List<string[]> stringList6 = new List<string[]>();

            for (int i = 0; i < 9; i++)
            {
                stringList6.Add(new string[] { i.ToString(), ('A' + i).ToString() });
            }

            //stringList6.Clear();

            if (stringList6.Count > 0)
            {
                richTextBox1.Text += "共有 " + stringList6.Count.ToString() + " 個項目, 分別是:\n";
            }

            for (int i = 0; i < stringList6.Count; i++)
            {
                int tt = int.Parse(stringList6[i][1]);
                richTextBox1.Text += "stringList6[" + i.ToString() + "][0] = " + stringList6[i][0].ToString() + "\tstringList6[" + i.ToString() + "][1] = " + (char)tt + "\n";
            }

            //刪除第N項
            int N;
            N = 1; stringList6.RemoveAt(N);  //index = N, 刪除第N項
            N = 3; stringList6.RemoveAt(N);  //index = N, 刪除第N項
            N = 5; stringList6.RemoveAt(N);  //index = N, 刪除第N項

            if (stringList6.Count > 0)
                richTextBox1.Text += "共有 " + stringList6.Count.ToString() + " 個項目, 分別是:\n";

            for (int i = 0; i < stringList6.Count; i++)
            {
                int aaa = int.Parse(stringList6[i][1]);
                richTextBox1.Text += "stringList6[" + i.ToString() + "][0] = " + stringList6[i][0].ToString() + "\tstringList6[" + i.ToString() + "][1] = " + (char)aaa + "\n";
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

            for (int i = 0; i < selected.Length; i++)
            {
                int n = r.Next(selected.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }
            richTextBox1.Text += "方法一結果：";
            for (int i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < selected.Length; i++)
            {
                selected[i] = i;
            }

            for (int i = selected.Length - 1; i > 0; i--)
            {
                int n = r.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = selected[i];
                selected[i] = selected[n];
                selected[n] = tmp;
            }

            richTextBox1.Text += "方法二結果：";
            for (int i = 0; i < selected.Length; i++)
            {
                richTextBox1.Text += selected[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //3030

            //建立 二維字串串列
            List<string[]> stringList7 = new List<string[]>();
            richTextBox1.Text += "len = " + stringList7.Count.ToString() + "\n";

            for (int i = 0; i < 10; i++)
            {
                stringList7.Add(new string[] { i.ToString(), "aaaaaaa", "bbbbb", "cccccc" });
            }
            richTextBox1.Text += "len = " + stringList7.Count.ToString() + "\n";

            for (int i = 0; i < stringList7.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (int j = 0; j < 4; j++)
                {
                    richTextBox1.Text += stringList7[i][j] + "\t";
                }
                richTextBox1.Text += "\n";
            }

            foreach (var fileName in stringList7)
            {
                string imgURL = fileName[0];
                richTextBox1.Text += imgURL + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //二維double串列
            List<double[]> doubleList = new List<double[]>();
            int g = 10;

            double t = 0;

            for (t = 0; t <= 5.0; t += 0.1)
            {
                //richTextBox1.Text += "t = " + t.ToString() + "\n";
                doubleList.Add(new double[] { t, g * t * t / 2, g * t * t * t / 2, Math.Sqrt(g * t * t / 2) });
            }

            int len = doubleList.Count;

            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += doubleList[i][0].ToString("n3") + "\t" + doubleList[i][1].ToString("n3") + "\t" + doubleList[i][2].ToString("n3") + "\t" + doubleList[i][3].ToString("n3") + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //一維字元串列 易經 六十四卦

            //List Char 易經 六十四卦
            char[] word = new char[64];
            word = GetChars();
            int i;
            for (i = 0; i < 64; i++)
            {
                richTextBox1.Text += word[i].ToString() + "    ";
            }
        }

        public static char[] GetChars()
        {
            List<char> chars = new List<char>();
            for (int i = 19904; i <= 19967; i++)
            {
                chars.Add((char)i);
            }
            return chars.ToArray();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //一維點串列

            //建立 一維點串列
            List<Point> pointList2 = new List<Point>(); // 紀錄滑鼠軌跡的陣列。

            //pointList2.Add(e.Location); // 將點加入到 points 陣列當中。
            //pointList2.Add(e.Location); // 將點加入到 points 陣列當中。
            pointList2.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。

            richTextBox1.Text += "共有 " + pointList2.Count.ToString() + " 個點\n";

            for (int i = 0; i < pointList2.Count; i++)
            {
                richTextBox1.Text += "(" + pointList2[i].X.ToString() + "," + pointList2[i].Y.ToString() + ") ";
            }
            richTextBox1.Text += "\n";



            pointList2.Clear();

            //3030

            // 收集滑鼠點數
            List<PointF> pointList1 = new List<PointF>();
            //pointList1.Add(new Point(e.X, e.Y));

            //收集滑鼠點數
            richTextBox1.Text += "共有點數 : " + pointList1.Count.ToString() + "\n";
            foreach (PointF pt in pointList1)
            {
                richTextBox1.Text += pt.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //清除
            pointList1 = new List<PointF>();
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private class classList
        {
            public string ID { get; set; }
            public string Name { get; set; }
            public string Level { get; set; }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //類別串列1
            //建立 一維類別串列
            List<classList> classList1 = new List<classList>();

            //Add
            classList1.Add(new classList { ID = "A001", Name = "David", Level = "A" });
            //classList1.Add(new classList { ID = "A002", Name = "John", Level = "B" });
            classList1.Add(new classList { ID = "A002", Name = "John" });  //可缺項
            classList1.Add(new classList { ID = "A003", Name = "Tom", Level = "A" });

            //Show
            richTextBox1.Text += "學號\t->\t姓名\t->\t等級\n";
            foreach (var showlist in classList1)
            {
                //richTextBox1.Text += "ID : " + showlist.ID + "\tName : " + showlist.Name + "\tLevel : " + showlist.Level + "\n";
                richTextBox1.Text += showlist.ID + "\t->\t" + showlist.Name + "\t->\t" + showlist.Level + "\n";
            }
        }

        public class classStudent
        {
            //靜態屬性 -- 記錄生成的物件
            public static int Number { get; private set; }

            public string Name;
            public int Score;

            //建構函式
            public classStudent(string name, int score)
            {
                this.Name = name;
                this.Score = score;
                Number++;   //建立物件就計數
                Console.WriteLine("第" + Number + "個學生");
            }

            ~classStudent() { }   //解構函式
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Console.WriteLine("未實體化，學生 : " + classStudent.Number + " 個\n");

            //類別串列2
            //建立 一維類別串列
            List<classStudent> classList2 = new List<classStudent>()
            {
                new classStudent("Student A", 90),
                new classStudent("Student B", 75),
                new classStudent("Student C", 83),
                new classStudent("Student D", 94),
                new classStudent("Student E", 60),
                new classStudent("Student F", 56),
                new classStudent("Student G", 30),
                new classStudent("Student I", 73),
                new classStudent("Student J", 68),
                new classStudent("Student K", 46)
            };
            foreach (var stu in classList2)
            {
                richTextBox1.Text += "Name : " + stu.Name + ", Score : " + stu.Score + "\n";
            }

            Console.WriteLine("已實體化，學生 : " + classStudent.Number + " 個\n");

            //排序
            classList2.Sort((x, y) => { return -x.Score.CompareTo(y.Score); });

            richTextBox1.Text += "排序後\n";

            foreach (var stu in classList2)
            {
                richTextBox1.Text += "Name : " + stu.Name + ", Score : " + stu.Score + "\n";
            }
        }

        // 定義 classEmployee 員工類別
        class classEmployee
        {
            public string EmpID { get; set; }   	// 編號屬性
            public string EmpName { get; set; } 	// 姓名屬性
            public string EmpSex { get; set; }     	// 性別屬性
            public bool EmpIsMarry { get; set; }  	// 婚姻屬性
        }

        //建立 一維類別串列
        List<classEmployee> classList3 = new List<classEmployee>();

        private void button12_Click(object sender, EventArgs e)
        {
            //類別串列3

            string id = "123";
            string name = "david";
            string sex = "先生";
            bool isMarry = true;
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });
            classList3.Add(new classEmployee() { EmpID = id, EmpName = name, EmpSex = sex, EmpIsMarry = isMarry });

            // 在txtShow文字方塊內顯示已新增的員工資料
            richTextBox1.Text += "編號\t姓名\t性別\t是否已婚" + Environment.NewLine;
            richTextBox1.Text += "============================" + Environment.NewLine;
            for (int i = 0; i < classList3.Count; i++)
            {
                richTextBox1.Text += classList3[i].EmpID + "\t" + classList3[i].EmpName + " \t" + classList3[i].EmpSex + "\t" + classList3[i].EmpIsMarry.ToString() + Environment.NewLine;
            }

        }

        public class tb_SensorRecordModel
        {
            public int ID { get; set; }
            public decimal Value1 { get; set; }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //類別串列4
            //建立 一維類別串列
            List<tb_SensorRecordModel> classList4a = new List<tb_SensorRecordModel>();
            classList4a.Add(new tb_SensorRecordModel { ID = 1, Value1 = 1 });
            classList4a.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2 });
            classList4a.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3 });

            //1、改变串列中某个元素的值
            var model = classList4a.Where(c => c.ID == 2).FirstOrDefault();
            model.Value1 = 2222;

            classList4a.ForEach(c =>
            {
                //打印的数据表明 串列中的那个元素 确实被改变了
                //知识：引用、地址
                richTextBox1.Text += "ID : " + c.ID.ToString() + "\tValue : " + c.Value1.ToString() + "\n";
            });

            //2、替换某一段数据
            List<tb_SensorRecordModel> classList4b = new List<tb_SensorRecordModel>();
            classList4b.Add(new tb_SensorRecordModel { ID = 1, Value1 = 1 });
            classList4b.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2 });
            classList4b.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3 });
            classList4b.Add(new tb_SensorRecordModel { ID = 4, Value1 = 4 });
            classList4b.Add(new tb_SensorRecordModel { ID = 5, Value1 = 5 });

            //构造新的一段数据
            List<tb_SensorRecordModel> classList4c = new List<tb_SensorRecordModel>();
            classList4c.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2222 });
            classList4c.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3333 });

            //删除 旧的 那段数据
            classList4b.RemoveRange(1, 2);

            //将新的 这段数据 插入到 指定位置
            classList4b.InsertRange(1, classList4c);

            classList4b.ForEach(c =>
            {
                //Console.WriteLine($"{c.ID},{c.Value1}");
                richTextBox1.Text += "ID : " + c.ID.ToString() + "\tValue : " + c.Value1.ToString() + "\n";
            });
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
            //建立 一維控件串列

            List<Button> controlList = new List<Button>();
            controlList.Add(button1);
            controlList.Add(button2);
            controlList.Add(button3);
            controlList.Add(button4);
            controlList.Add(button5);

            foreach (Button btn in controlList)
            {
                //btn.Text = btn.Name;
                btn.BackColor = Color.Pink;
                richTextBox1.Text += "控件 :" + btn.Name + "長度 :" + btn.Text.Length.ToString() + "\n";
            }
        }

        public static void PrintOut1(IEnumerable tempmySL)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            foreach (DictionaryEntry de in tempmySL)
            {
                Console.WriteLine("\t {0}  \t\t{1}", de.Key, de.Value);
            }
        }

        public static void PrintOut2(SortedList myList)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            for (int i = 0; i < myList.Count; i++)
            {
                Console.WriteLine("\t {0}  \t\t{1}", myList.GetKey(i), myList.GetByIndex(i));
                // GetKey(i):取得 SortedList 物件中指定之索引處的索引鍵。
                // GetByIndex(i):取得 SortedList 物件中指定之索引處的值。
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //SortedList 0
            SortedList mySL = new SortedList(); //建立myHT為屬於Hashtable實體

            Console.WriteLine("\n1.置入四筆Key&Value鍵值到SortedList串列內.");
            mySL["iPhone5S"] = 22000;  //添加 key&value鍵值對
            mySL["iPhone5C"] = 18000;  //添加 key&value鍵值對
            mySL["iPad2"] = 12500;     //添加 key&value鍵值對
            mySL["iPad Mini"] = 15900;  //添加 key&value鍵值對

            PrintOut1(mySL);
            Console.WriteLine(" 1.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            // 查詢產品單價
            Console.Write(" 2.請輸入Apple產品名稱 : ");
            string item = Console.ReadLine();
            if (!mySL.ContainsKey(item))//判斷SortedList是否含特定鍵
            {
                Console.WriteLine(" 2. {0} 不存在 !!", item);
            }
            else
            {
                Console.WriteLine(" 2.{0}單價 : {1}", item, mySL[item]);
            }
            Console.WriteLine(" --------------------------------------");

            // 移除剛查詢的 Key & Value 鍵值對
            Console.WriteLine(" 3.移除剛查詢鍵值 {0}", item);
            mySL.Remove(item);
            PrintOut2(mySL);
            Console.WriteLine(" 3.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            //移除所有元素
            Console.WriteLine(" 4.移除 SortedList串列內所有元素");
            mySL.Clear();
            Console.WriteLine(" 4.目前 SortedList串列內元素總個數 : {0}", mySL.Count);
            Console.WriteLine(" --------------------------------------");
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //SortedList 1
            SortedList m = new SortedList();  // 非泛型

            m.Add("David", new Member1() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member1() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member1() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member1() { Name = "Jack", Select = true, Score = 95 });

            //非泛型操作
            Console.WriteLine("=== 非泛型 SortedList 操作需強制轉換 .... \n");
            foreach (DictionaryEntry item in m)
            {
                Console.WriteLine(((Member1)item.Value).ToString());
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //SortedList 2
            SortedList<string, Member2> m = new SortedList<string, Member2>();

            m.Add("David", new Member2() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member2() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member2() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member2() { Name = "Jack", Select = true, Score = 95 });

            //泛型陣列操作
            Console.WriteLine("=== 泛型 SortedList 操作不需強制轉換 .... \n");
            foreach (KeyValuePair<string, Member2> item in m)
            {
                // Console.WriteLine (" 姓名:{0} \t 選課:{1}  \t  成績:{2}  \n" ,item.Key, item.Value.Select, item.Value.Score );
                Console.WriteLine(item.Value.ToString());
            }
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
            //串列共同函數

            //串列共同函數
            //反相
            //stringList1.Reverse();

            //排序
            //stringList1.Sort();

            //清除List資料
            //stringList1.Clear();


        }
    }

    public class Person
    {
        public string Name { get; set; }
        public int Age { get; private set; }
        public string Sex { get; set; }
        public int Money { get; set; }

        //建構函式
        public Person(string name, string sex, int age, int money)
        {
            Name = name;
            Age = age;
            Sex = sex;
            Money = money;
        }
        ~Person() { }   //解構函式
    }

    class Member
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        //public override string ToString()    // 覆寫覆類別 ToString()方法
        // {
        //   return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        //}
    }

    class Member1
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性  

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }

    class Member2
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */

