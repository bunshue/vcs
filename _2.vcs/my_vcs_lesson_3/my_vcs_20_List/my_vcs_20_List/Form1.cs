using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_20_List
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

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
    }
}
