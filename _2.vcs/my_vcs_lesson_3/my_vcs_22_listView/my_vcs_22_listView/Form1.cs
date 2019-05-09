using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_22_listView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ListViewItem i1 = new ListViewItem("File1.txt");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "1234";
            i1.SubItems.Add(sub_i1a);
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            sub_i1b.Text = "2016/5/25 02:10上午";
            i1.SubItems.Add(sub_i1b);

            ListViewItem i2 = new ListViewItem("File2.txt");
            ListViewItem.ListViewSubItem sub_i2a = new ListViewItem.ListViewSubItem();
            sub_i2a.Text = "5678";
            i2.SubItems.Add(sub_i2a);
            ListViewItem.ListViewSubItem sub_i2b = new ListViewItem.ListViewSubItem();
            sub_i2b.Text = "2016/5/25 02:10上午";
            i2.SubItems.Add(sub_i2b);

            ListViewItem i3 = new ListViewItem("File3.txt");
            ListViewItem.ListViewSubItem sub_i3a = new ListViewItem.ListViewSubItem();
            sub_i3a.Text = "3388";
            i3.SubItems.Add(sub_i3a);
            ListViewItem.ListViewSubItem sub_i3b = new ListViewItem.ListViewSubItem();
            sub_i3b.Text = "2016/5/25 02:10上午";
            i3.SubItems.Add(sub_i3b);

            listView1.Items.Add(i1);
            listView1.Items.Add(i2);
            listView1.Items.Add(i3);

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count-1].EnsureVisible();
       
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //設置列名稱、大小與對齊
            listView1.Columns.Add("檔名", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("容量", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("日期", 200, HorizontalAlignment.Center);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listView1.Items.Count <= 0)
            {
                richTextBox1.Text += "listView無內容\n";
                return;
            }

            richTextBox1.Text += "共有" + listView1.Items.Count.ToString() + "個項目，分別是：\n";
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                //ListViewItem t = listView1.Items[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\n";
            }
            if (listView1.SelectedItems.Count <= 0)
            {
                richTextBox1.Text += "未選擇listView項目\n";
                return;
            }
            richTextBox1.Text += "選擇" + listView1.SelectedItems.Count.ToString() + "個項目，分別是：\n";
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                //ListViewItem t = listView1.SelectedItems[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += listView1.SelectedItems[i].SubItems[0].Text + "\t" + listView1.SelectedItems[i].SubItems[1].Text + "\t" + listView1.SelectedItems[i].SubItems[2].Text + "\n";
            }
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                return;

            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了" + listView1.Items[selNdx].Text + "\t內容為：\n";

            //ListViewItem t = listView1.Items[selNdx]; //相同寫法
            //richTextBox1.Text += t.Text + "\t" + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
            richTextBox1.Text += listView1.Items[selNdx].Text + "\t" + listView1.Items[selNdx].SubItems[1].Text + "\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            richTextBox1.Clear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //測試中
            ListViewItem i1 = new ListViewItem("File_add.txt");
            ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
            sub_i1a.Text = "3333";
            i1.SubItems.Add(sub_i1a);
            ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
            sub_i1b.Text = "2016/5/25 02:10上午";
            i1.SubItems.Add(sub_i1b);

            listView1.Items.Add(i1);

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "目前共有 " + listView1.Items.Count.ToString() + " 個項目\n";
            if (listView1.Items.Count > 5)
                listView1.Items.RemoveAt(5);
        }

    }
}
