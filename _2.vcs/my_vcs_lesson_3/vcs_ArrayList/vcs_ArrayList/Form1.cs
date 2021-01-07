using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;   //for ArrayList

namespace vcs_ArrayList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        ArrayList ArrayListData = new ArrayList();

        private void button1_Click(object sender, EventArgs e)
        {
            ArrayListData.Add(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            /*
            for (i = 0; i < ArrayListData.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + ArrayListData[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in ArrayListData)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            textBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            ArrayListData.Remove(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int item = int.Parse(textBox2.Text);
            if((item > 0) && (item <= ArrayListData.Count))
                ArrayListData.RemoveAt(item - 1);      //刪除特定項目
        }

        private void button6_Click(object sender, EventArgs e)
        {
            ArrayListData.Sort();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            ArrayListData.Reverse();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Object tmp;
            if (textBox3.Text == "")
                return;
            tmp = textBox3.Text;  //取得所輸入的資料
            if (ArrayListData.IndexOf(tmp) < 0)
                //若超過陣列索引值則表示找不到符合的資料
                richTextBox1.Text += "找不到您所輸入的資料\n";
            else
                richTextBox1.Text += "您所尋找的資料在第 " + (ArrayListData.IndexOf(tmp) + 1).ToString() + " 筆\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            ArrayListData.Insert(3, "David"); //插入一個元素
        }
    }
}
