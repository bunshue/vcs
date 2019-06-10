using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_13_ListView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //把 listView1 的 View 屬性設成 Details
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //設置列名稱、大小與對齊
            listView1.Columns.Add("姓名", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("國文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("英文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("數學", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("總分", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("平均", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("名次", 100, HorizontalAlignment.Center);

        }

        public static string GetRandomString2(int length)
        {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            //var next = new Random();
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[Rnd.Next(0, str.Length)]);
            }
            return builder.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            string name_string;
            int score_chi;
            int score_eng;
            int score_math;


            for (int i = 0; i < 10; i++)
            {
                var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                //var next = new Random();
                //Random Rnd = new Random(); //加入Random，產生的數字不會重覆
                var builder = new StringBuilder();
                int length = 5;
                int j;
                for (j = 0; j < length; j++)
                {
                    builder.Append(str[Rnd.Next(0, str.Length)]);
                }
                name_string = builder.ToString();

                score_chi = Rnd.Next(80, 100) + 1;
                score_eng = Rnd.Next(70, 100) + 1;
                score_math = Rnd.Next(60, 100) + 1;

                ListViewItem i1 = new ListViewItem(name_string);
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = score_chi.ToString();
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                sub_i1b.Text = score_eng.ToString();
                i1.SubItems.Add(sub_i1b);
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();
                sub_i1c.Text = score_math.ToString();
                i1.SubItems.Add(sub_i1c);

                listView1.Items.Add(i1);

            }

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 : " + listView1.Items.Count.ToString() + " 個項目\n";

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
                richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\t" + listView1.Items[i].SubItems[3].Text + "\n";
            }
            if (listView1.SelectedItems.Count <= 0)
            {
                //richTextBox1.Text += "未選擇listView項目\n";
                return;
            }
            richTextBox1.Text += "選擇" + listView1.SelectedItems.Count.ToString() + "個項目，分別是：\n";
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                //ListViewItem t = listView1.SelectedItems[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += listView1.SelectedItems[i].SubItems[0].Text + "\t" + listView1.SelectedItems[i].SubItems[1].Text + "\t" + listView1.SelectedItems[i].SubItems[2].Text + listView1.SelectedItems[i].SubItems[3].Text + "\n";
            }


        }

        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            richTextBox1.Clear();

        }

        private void listView1_DoubleClick(object sender, EventArgs e)
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

        private void button3_Click(object sender, EventArgs e)
        {
            int selNdx;
            int selCount;

            selCount = listView1.SelectedIndices.Count;
            if (selCount <= 0)  //總共選擇的個數
            {
                richTextBox1.Text += "未選擇要刪除的項目\n";
                return;
            }
            richTextBox1.Text += "共選擇 " + selCount.ToString() + " 個項目, 分別是\n";
            for (int i = (selCount - 1); i >= 0; i--)
            {
                selNdx = listView1.SelectedItems[i].Index;
                richTextBox1.Text += "item : " + listView1.SelectedItems[i].Text + " index = " + selNdx.ToString() + "\n";
                listView1.Items.RemoveAt(selNdx);
            }
            return;
        }

        private void listView1_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            richTextBox1.Text += "你按了 " + e.Column.ToString() + " Column\t";

            switch (e.Column)
            {
                case 0:
                    richTextBox1.Text += "依姓名排序\n";
                    break;
                case 1:
                    richTextBox1.Text += "依國文成績排序\n";
                    break;
                case 2:
                    richTextBox1.Text += "依英文成績排序\n";
                    break;
                case 3:
                    richTextBox1.Text += "依數學成績排序\n";
                    break;
                case 4:
                    richTextBox1.Text += "依總分排序\n";
                    break;
                case 5:
                    richTextBox1.Text += "依平均分數排序\n";
                    break;
                default:
                    richTextBox1.Text += "\n";
                    break;
            }


        }

    }
}
