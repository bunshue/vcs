using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_List1
{
    public partial class Form1 : Form
    {
        bool isMouseDown = false;   // 紀錄滑鼠是否被按下

        List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。
        List<String> strings = new List<String>();

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
            x_st = 660;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 480);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1420, 820);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 " + points.Count.ToString() + " 個點\n";

            for (int i = 0; i < points.Count; i++)
            {
                richTextBox1.Text += "(" + points[i].X.ToString() + "," + points[i].Y.ToString() + ") ";
            }
            richTextBox1.Text += "\n";
        }

        Random r = new Random();
        private void button1_Click(object sender, EventArgs e)
        {
            string new_string;
            new_string = "string" + r.Next(100).ToString("D3");
            richTextBox1.Text += "加入新資料進List " + new_string + "\n";
            strings.Add(new_string);
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDown = true; // 滑鼠被按下後設定旗標值。
            points.Add(e.Location); // 將點加入到 points 陣列當中。
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown) // 如果滑鼠被按下
            {
                points.Add(e.Location); // 將點加入到 points 陣列當中。
                // 畫出上一點到此點的線段。
                //g.DrawLine(pen, points[points.Count - 2], points[points.Count - 1]);
                this.Invalidate();
            }
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            points.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。
            isMouseDown = false; // 滑鼠已經沒有被按下了。
        }

        private void button4_Click(object sender, EventArgs e)
        {
            points.Clear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (strings.Count < 5)
            {
                richTextBox1.Text += "count not enough, abort\n";
                return;
            }
            //richTextBox1.Text += "capacity : " + strings.Capacity.ToString() + "\n";
            //strings.RemoveAt(3);
            strings.RemoveRange(3, 5);
            richTextBox1.Text += "刪除此List之第3項開始的5項";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            strings.Reverse();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            strings.Sort();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (strings.Count < 5)
            {
                richTextBox1.Text += "count not enough, abort\n";
                return;
            }
            strings.RemoveAt(3);
            richTextBox1.Text += "刪除此List之第3項";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (strings.Count < 5)
            {
                richTextBox1.Text += "count not enough, abort\n";
                return;
            }
            strings.Insert(3, "xxxxxxxxxxxxxxxx");
            richTextBox1.Text += "添加一項在第3項";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //二維List for string
            List<string[]> MyList1 = new List<string[]>();
            MyList1.Add(new string[] { "AAA", "BBB" });
            MyList1.Add(new string[] { "CCC", "DDD" });
            MyList1.Add(new string[] { "CCC", "DDD" });
            richTextBox1.Text += "Result : " + MyList1[1][1].ToString() + "\n";
            richTextBox1.Text += "Count : " + MyList1.Count.ToString() + "\n";

            //二維List for int
            List<List<int>> MyList2 = new List<List<int>>();
            List<int> sublist = new List<int>();
            sublist.Add(0);
            sublist.Add(0);
            MyList2.Add(sublist);
            MyList2.Add(sublist);
            MyList2.Add(sublist);
            MyList2.Add(sublist);
            MyList2.Add(sublist);

            int i;
            for (i = 0; i < MyList2.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\n";
                MyList2[i][0] = i;
                MyList2[i][1] = MyList2.Count - i;
            }

            for (i = 0; i < MyList2.Count; i++)
            {
                richTextBox1.Text += "MyList2[" + i.ToString() + "][0] = " + MyList2[i][0].ToString() + " MyList2[" + i.ToString() + "][1] = " + MyList2[i][1].ToString() + "\n";
            }

            List<List<string>> MyList3 = new List<List<string>>();
            MyList3.Add(new List<string>() { "0,0 : Mike", "0, 1: Jane" });
            MyList3.Add(new List<string>() { "1,0 : Jack", "1, 1: John" });

            MyList3[0][0] = "0,0: Kyle";

            richTextBox1.Text += "result : " + MyList3[0][0] + "\n"; // 輸出: 0,0: Kyle
            richTextBox1.Text += "result : " + MyList3[0][1] + "\n"; // 輸出: 0,1: Jane
            richTextBox1.Text += "result : " + MyList3[1][0] + "\n"; // 輸出: 1,0: Jack
            richTextBox1.Text += "result : " + MyList3[1][1] + "\n"; // 輸出: 1,1: John
        }

        private void button11_Click(object sender, EventArgs e)
        {
            strings.Clear();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 " + strings.Count.ToString() + " 個字串\n";

            // 取出單一個List 裡的值，如同陣列(Array)用法
            for (int i = 0; i < strings.Count; i++)
            {
                richTextBox1.Text += strings[i] + "\n";
            }

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "\n可用foreach 取出List 裡的值\n";
            foreach (string sss in strings)
            {
                richTextBox1.Text += sss + "\n";
            }
        }

        void show_list(List<int> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        void show_list(List<string> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            int num = 20;
            Random rr = new Random();

            List<int> myList = new List<int>();   //宣告int型態的List

            /*  不均勻分配
            myList.Add('A');
            myList.Add('A');
            myList.Add('A');
            myList.Add('B');
            myList.Add('C');
            */

            for (int i = 0; i < num; i++)
            {
                myList.Add(rr.Next(10));
            }

            /*
            //特定分配
            for (int i = 50; i <= 57; i++)
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表
            */

            richTextBox1.Text += "建立長度為 " + num.ToString() + " 的List\t內容:\n";
            show_list(myList);

            myList.Sort();

            richTextBox1.Text += "排序後:\n";
            show_list(myList);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            int num = 10;
            List<string> myList = new List<string>();   //宣告string型態的List

            myList.Add("john");
            myList.Add("mary");
            myList.Add("david");
            myList.Add("bill");
            myList.Add("tom");
            myList.Add("sue");
            myList.Add("larry");
            myList.Add("michael");
            myList.Add("pepa");
            myList.Add("eric");

            richTextBox1.Text += "建立長度為 " + num.ToString() + " 的List\t內容:\n";
            show_list(myList);
            myList.Sort();

            richTextBox1.Text += "排序後:\n";
            show_list(myList);

            richTextBox1.Text += "移除一些:\n";
            myList.Remove("sue");
            myList.Remove("john");
            myList.RemoveAt(2); //上述已經移除後, 再移除第2個

            show_list(myList);

            richTextBox1.Text += "新增一些:\n";
            myList.Insert(2, "rebecca");
            myList.Insert(6, "sharon");
            myList.Insert(1, "emily");
            show_list(myList);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            List<List<string>> myList = new List<List<string>>();
            myList.Add(new List<string>() { "A001", "David" });
            myList.Add(new List<string>() { "A002", "John" });
            myList.Add(new List<string>() { "A003", "Tom" });
            richTextBox1.Text += "學號\t->\t姓名\n";
            foreach (var showlist in myList)
            {
                richTextBox1.Text += showlist[0] + "\t->\t" + showlist[1] + "\n";
            }
        }

        private class myList
        {
            public string ID { get; set; }
            public string Name { get; set; }
            public string Level { get; set; }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            List<myList> myList = new List<myList>();

            //二維List Add
            myList.Add(new myList { ID = "A001", Name = "David", Level = "A" });
            //myList.Add(new myList { ID = "A002", Name = "John", Level = "B" });
            myList.Add(new myList { ID = "A002", Name = "John" });  //可缺項
            myList.Add(new myList { ID = "A003", Name = "Tom", Level = "A" });

            //二維List Show
            richTextBox1.Text += "學號\t->\t姓名\t->\t等級\n";
            foreach (var showlist in myList)
            {
                //richTextBox1.Text += "ID : " + showlist.ID + "\tName : " + showlist.Name + "\tLevel : " + showlist.Level + "\n";
                richTextBox1.Text += showlist.ID + "\t->\t" + showlist.Name + "\t->\t" + showlist.Level + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int num = 10;
            Random rr = new Random();

            List<int> myList = new List<int>();   //宣告int型態的List

            for (int i = 0; i < num; i++)
            {
                myList.Add(i);
            }
            richTextBox1.Text += "建立長度為 " + num.ToString() + " 的List\t內容:\t";
            show_list(myList);

            richTextBox1.Text += "List亂序\t內容:\t";
            myList = get_random_list(myList);

            show_list(myList);
        }

        List<int> get_random_list(List<int> ContentList)
        {
            Random random = new Random();
            List<int> newList = new List<int>();
            foreach (int item in ContentList)
            {
                newList.Insert(random.Next(newList.Count), item);
            }
            return newList;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //二維List for string
            List<string[]> camera_serials = new List<string[]>();

            camera_serials.Clear();
            int i;
            for (i = 0; i < 10; i++)
            {
                camera_serials.Add(new string[] { "aaaa" + i.ToString(), "bbbb" + i.ToString(), DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
            }

            if (camera_serials.Count > 0)
            {
                richTextBox1.Text += "共有 " + camera_serials.Count.ToString() + " 筆資料\t分別是:\n";
                for (i = 0; i < camera_serials.Count; i++)
                {
                    richTextBox1.Text += "camera_serials[" + i.ToString() + "][0] = " + camera_serials[i][0].ToString()
                        + "\tcamera_serials[" + i.ToString() + "][1] = " + camera_serials[i][1].ToString()
                        + "\tcamera_serials[" + i.ToString() + "][2] = " + camera_serials[i][2].ToString() + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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

        private void button20_Click(object sender, EventArgs e)
        {
            //不用宣告長度的陣列(Array)
            // 宣告myIntLists 為List
            // 以下List 裡為int 型態
            List<int> myIntLists = new List<int>();

            // 宣告myStringLists 為List
            // 以下List 裡為string 型態
            List<string> myStringLists = new List<string>();

            // 在List 裡新增int 整數
            myIntLists.Add(12);
            myIntLists.Add(34);
            myIntLists.Add(56);

            // 在List 裡新增string 字串
            myStringLists.Add("lion");
            myStringLists.Add("mouse");
            myStringLists.Add("cat");
            myStringLists.Add("dog");

            richTextBox1.Text += "\n";
            richTextBox1.Text += "myIntLists has" + myIntLists.Count.ToString() + " elements\n";
            richTextBox1.Text += "myStringLists has" + myStringLists.Count.ToString() + " elements\n";

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (int ii in myIntLists)
            {
                richTextBox1.Text += "\t" + ii.ToString();
            }
            richTextBox1.Text += "\n";

            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "經過排序：\n";
            myStringLists.Sort();
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "增加內容：\n";
            myStringLists.Insert(2, "elephant");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "刪除內容：\n";
            myStringLists.Remove("cat");
            // 可用foreach 取出List 裡的值
            richTextBox1.Text += "取出List內容：";
            foreach (string str in myStringLists)
            {
                richTextBox1.Text += "\t" + str;
            }
            richTextBox1.Text += "\n";
        }

        public class tb_SensorRecordModel
        {
            public int ID { get; set; }
            public decimal Value1 { get; set; }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            List<tb_SensorRecordModel> list = new List<tb_SensorRecordModel>();
            list.Add(new tb_SensorRecordModel { ID = 1, Value1 = 1 });
            list.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2 });
            list.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3 });

            //1、改变list中某个元素的值
            var model = list.Where(c => c.ID == 2).FirstOrDefault();
            model.Value1 = 2222;

            list.ForEach(c =>
            {
                //打印的数据表明 list中的那个元素 确实被改变了
                //知识：引用、地址
                richTextBox1.Text += "ID : " + c.ID.ToString() + "\tValue : " + c.Value1.ToString() + "\n";
            });

            //2、替换某一段数据
            List<tb_SensorRecordModel> list1 = new List<tb_SensorRecordModel>();
            list1.Add(new tb_SensorRecordModel { ID = 1, Value1 = 1 });
            list1.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2 });
            list1.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3 });
            list1.Add(new tb_SensorRecordModel { ID = 4, Value1 = 4 });
            list1.Add(new tb_SensorRecordModel { ID = 5, Value1 = 5 });

            //构造新的一段数据
            List<tb_SensorRecordModel> list2 = new List<tb_SensorRecordModel>();
            list2.Add(new tb_SensorRecordModel { ID = 2, Value1 = 2222 });
            list2.Add(new tb_SensorRecordModel { ID = 3, Value1 = 3333 });

            //删除 旧的 那段数据
            list1.RemoveRange(1, 2);

            //将新的 这段数据 插入到 指定位置
            list1.InsertRange(1, list2);

            list1.ForEach(c =>
            {
                //Console.WriteLine($"{c.ID},{c.Value1}");
                richTextBox1.Text += "ID : " + c.ID.ToString() + "\tValue : " + c.Value1.ToString() + "\n";
            });
        }

        //二維List for double
        private void button22_Click(object sender, EventArgs e)
        {
            List<double[]> pts = new List<double[]>();    //二維List for double array
            int g = 10;

            double t = 0;

            for (t = 0; t <= 5.0; t += 0.1)
            {
                //richTextBox1.Text += "t = " + t.ToString() + "\n";
                pts.Add(new double[] { t, g * t * t / 2, g * t * t * t / 2, Math.Sqrt(g * t * t / 2) });
            }

            int len = pts.Count;

            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += pts[i][0].ToString("n3") + "\t" + pts[i][1].ToString("n3") + "\t" + pts[i][2].ToString("n3") + "\t" + pts[i][3].ToString("n3") + "\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
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

        private void button24_Click(object sender, EventArgs e)
        {
            //List測試

            int i;
            int j;
            List<string[]> fileNameList = new List<string[]>();

            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";
            for (i = 0; i < 10; i++)
            {
                fileNameList.Add(new string[] { i.ToString(), "aaaaaaa", "bbbbb", "cccccc" });
            }
            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";

            for (i = 0; i < fileNameList.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (j = 0; j < 4; j++)
                {
                    richTextBox1.Text += fileNameList[i][j] + "\t";
                }
                richTextBox1.Text += "\n";
            }

            foreach (var fileName in fileNameList)
            {
                string imgURL = fileName[0];
                richTextBox1.Text += imgURL + "\n";
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //List之搜尋語法1
            //這裡使用Where擴展方法獲取大於4的值。

            List<int> intList = new List<int>() { 1, 2, 3, 4, 5 };

            var maxIntList = intList.Where(i => i > 4);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            intList.Add(6);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //List之搜尋語法2
            List<int> intList = new List<int>() { 1, 2, 3, 4, 5 };

            var maxIntList = intList.Where(i => i > 4).ToList();//調用ToList()方法

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            intList.Add(6);

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }

            maxIntList = intList.Where(i => i > 4).ToList();//調用ToList()方法

            foreach (var item in maxIntList)
            {
                Console.WriteLine(item);
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //讀取一個檔案到List

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //把控件做成串列

            List<Button> Clients = new List<Button>();

            Clients.Add(button1);
            Clients.Add(button2);
            Clients.Add(button3);
            Clients.Add(button4);
            Clients.Add(button5);

            foreach (Button client in Clients)
            {
                //client.Text = client.Name;
                client.BackColor = Color.Pink;
                richTextBox1.Text += "控件 :" + client.Name + "長度 :" + client.Text.Length.ToString() + "\n";
            }
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


