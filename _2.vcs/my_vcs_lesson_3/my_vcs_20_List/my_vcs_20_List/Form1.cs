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
            richTextBox1.Text += "共有 " + strings.Count.ToString() + " 個字串\n";


            for (int i = 0; i < strings.Count; i++)
            {
                richTextBox1.Text += strings[i] + "\n";
            }

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
            strings.Clear();
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
    }
}
