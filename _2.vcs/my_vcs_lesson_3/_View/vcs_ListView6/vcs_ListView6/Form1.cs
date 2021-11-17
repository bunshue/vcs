using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView6
{
    public partial class Form1 : Form
    {
        int flag_check_score_done = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //把 listView1 的 View 屬性設成 Details
            listView1.FullRowSelect = true; //整行一起選取
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listView1.Columns.Count == 0)
            {
                //設置列名稱、大小與對齊
                listView1.Columns.Add("座號", 60, HorizontalAlignment.Center);
                listView1.Columns.Add("姓名", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("國文", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("英文", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("數學", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("總分", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("平均", 100, HorizontalAlignment.Center);
                listView1.Columns.Add("名次", 100, HorizontalAlignment.Center);

                listView1.GridLines = true;
            }
            else
            {
                richTextBox1.Text += "已有標題\n";
            }
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
                int length = 8;
                int j;

                builder.Append("A");
                builder.Append(((listView1.Items.Count + 1) / 100).ToString());
                builder.Append(((listView1.Items.Count + 1) / 10).ToString());
                builder.Append(((listView1.Items.Count + 1) % 10).ToString());
                builder.Append("_");

                for (j = 5; j < length; j++)
                {
                    builder.Append(str[Rnd.Next(0, str.Length)]);
                }
                name_string = builder.ToString();

                score_chi = Rnd.Next(55, 90) + 1;
                score_eng = Rnd.Next(50, 80) + 1;
                score_math = Rnd.Next(40, 70) + 1;

                /* debug
                name_string = "david";

                score_chi = 80;
                score_eng = 90;
                score_math = 100;
                */

                //建立一行資料的檔頭與第0筆資料(座號)
                ListViewItem item = new ListViewItem((i + 1).ToString());

                //建立這一筆資料的第1個子項目(姓名)
                ListViewItem.ListViewSubItem sub_item_1 = new ListViewItem.ListViewSubItem();
                sub_item_1.Text = name_string;
                item.SubItems.Add(sub_item_1);

                //建立這一筆資料的第2個子項目(國文)
                ListViewItem.ListViewSubItem sub_item_2 = new ListViewItem.ListViewSubItem();
                sub_item_2.Text = score_chi.ToString();
                item.SubItems.Add(sub_item_2);

                //建立這一筆資料的第3個子項目(英文)
                ListViewItem.ListViewSubItem sub_item_3 = new ListViewItem.ListViewSubItem();
                sub_item_3.Text = score_eng.ToString();
                item.SubItems.Add(sub_item_3);

                /*  這項改成直接加入
                //建立這一筆資料的第4個子項目(數學)
                ListViewItem.ListViewSubItem sub_item_4 = new ListViewItem.ListViewSubItem();
                sub_item_4.Text = score_math.ToString();
                item.SubItems.Add(sub_item_4);
                */
                //直接加入
                item.SubItems.Add(score_math.ToString());

                //整行資料一次加入到listView1
                listView1.Items.Add(item);

                /*
                //添加item另法 AddRange
                ListViewItem item = new ListViewItem((i + 1).ToString());
                item.SubItems.Add(name_string);
                item.SubItems.Add(score_chi.ToString());
                item.SubItems.Add(score_eng.ToString());
                item.SubItems.Add(score_math.ToString());
                listView1.Items.AddRange(new ListViewItem[] { item });
                */

            }

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();

        }

        void print_listView_data(ListView lv)
        {
            richTextBox1.Text += "共有 : " + lv.Columns.Count.ToString() + " 個欄目\n";
            richTextBox1.Text += "共有 : " + lv.Items.Count.ToString() + " 個項目\n";

            if (lv.Items.Count <= 0)
            {
                richTextBox1.Text += "listView無內容\n";
                return;
            }

            richTextBox1.Text += "共有" + lv.Items.Count.ToString() + "個項目，分別是：\n";
            for (int i = 0; i < lv.Items.Count; i++)
            {
                //ListViewItem t = lv.Items[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += lv.Items[i].SubItems[0].Text + "\t" + lv.Items[i].SubItems[1].Text + "\t" + lv.Items[i].SubItems[2].Text + "\t" + lv.Items[i].SubItems[3].Text + "\n";
            }

            if (lv.SelectedItems.Count <= 0)
            {
                //richTextBox1.Text += "未選擇listView項目\n";
                return;
            }
            richTextBox1.Text += "選擇" + lv.SelectedItems.Count.ToString() + "個項目，分別是：\n";
            for (int i = 0; i < lv.SelectedItems.Count; i++)
            {
                //ListViewItem t = lv.SelectedItems[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += lv.SelectedItems[i].SubItems[0].Text + "\t" + lv.SelectedItems[i].SubItems[1].Text + "\t" + lv.SelectedItems[i].SubItems[2].Text + lv.SelectedItems[i].SubItems[3].Text + "\n";
            }

            richTextBox1.Text += "選擇" + lv.SelectedIndices.Count.ToString() + "個項目，Index分別是：\n";
            for (int i = 0; i < lv.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += lv.SelectedIndices[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            print_listView_data(listView1);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            richTextBox1.Clear();
            flag_check_score_done = 0;
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
            richTextBox1.Text += listView1.Items[selNdx].Text + "\t" + listView1.Items[selNdx].SubItems[1].Text + "\t" + listView1.Items[selNdx].SubItems[2].Text + "\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";


            /*  另法

            //C# listview 取得點選的值
            string str1 = listView1.FocusedItem.Text;
            string str2 = listView1.FocusedItem.SubItems[1].Text;
            string str3 = listView1.FocusedItem.SubItems[2].Text;
            string str4 = listView1.FocusedItem.SubItems[3].Text;

            richTextBox1.Text += str1 + "\t" + str2 + "\t" + str3 + "\t" + str4 + "\n";
             
             */

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

        class StudentData
        {
            public int number { get; set; }
            public string name { get; set; }
            public int score_chi { get; set; }
            public int score_eng { get; set; }
            public int score_math { get; set; }
            public int total { get; set; }
            public float average { get; set; }
            public int rank { get; set; }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (flag_check_score_done == 1)
            {
                richTextBox1.Text += "已做過成績\n";
                return;
            }

            if (listView1.Items.Count < 1)
            {
                richTextBox1.Text += "無資料\n";
                return;
            }

            int i;
            int j;
            StudentData[] StudentDataArray = new StudentData[listView1.Items.Count];
            int[] scores = new int[listView1.Items.Count];
            int total;
            float average;
            for (i = 0; i < listView1.Items.Count; i++)
            {
                ListViewItem item = listView1.Items[i];
                item.UseItemStyleForSubItems = false;
                if (int.Parse(item.SubItems[2].Text) < 60)  //這一筆資料的第2個子項目(國文)
                {
                    item.SubItems[2].ForeColor = Color.Red;
                }
                if (int.Parse(item.SubItems[3].Text) < 60)  //這一筆資料的第3個子項目(英文)
                {
                    item.SubItems[3].ForeColor = Color.Red;
                }
                if (int.Parse(item.SubItems[4].Text) < 60)  //這一筆資料的第4個子項目(數學)
                {
                    item.SubItems[4].ForeColor = Color.Red;
                }
                total = int.Parse(item.SubItems[2].Text) + int.Parse(item.SubItems[3].Text) + int.Parse(item.SubItems[4].Text);
                average = (float)total /3;
                item.SubItems.Add(total.ToString());
                item.SubItems.Add(average.ToString("#0.00"));

                richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\t" + listView1.Items[i].SubItems[3].Text + "\t" + listView1.Items[i].SubItems[4].Text + "\n";

                StudentDataArray[i] = new StudentData { };
                StudentDataArray[i].number = i;
                StudentDataArray[i].name = item.SubItems[1].Text;
                StudentDataArray[i].score_chi = int.Parse(item.SubItems[2].Text);
                StudentDataArray[i].score_eng = int.Parse(item.SubItems[3].Text);
                StudentDataArray[i].score_math = int.Parse(item.SubItems[4].Text);
                StudentDataArray[i].total = total;
                StudentDataArray[i].average = average;
                scores[i] = total;
            }

            /*  不是成績單用的排序
            richTextBox1.Text += "排序前：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (StudentData str in StudentDataArray)
            {
                richTextBox1.Text += str.name + "\t" + str.score_chi.ToString() + "\t" + str.score_eng.ToString() + "\t" + str.score_math.ToString() + "\t" + str.total.ToString() + "\t" + str.average.ToString("#0.00") + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Name_C排序, ";
            Array.Sort(StudentDataArray, delegate(StudentData s1, StudentData s2)
            {
                return s1.total.CompareTo(s2.total);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (StudentData str in StudentDataArray)
            {
                richTextBox1.Text += str.name + "\t" + str.score_chi.ToString() + "\t" + str.score_eng.ToString() + "\t" + str.score_math.ToString() + "\t" + str.total.ToString() + "\t" + str.average.ToString("#0.00") + "\n";
            }
            richTextBox1.Text += "\n";
            */

            //排名次
            int[] scores_new = new int[listView1.Items.Count];
            int[] rank = new int[listView1.Items.Count];

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
                        rank[j] = i;
                    }
                }

            }
            richTextBox1.Text += "排名次：\n";
            for (i = 0; i < scores.Length; i++)
            {
                //richTextBox1.Text += (i + 1).ToString() + "\t" + names[i] + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
                richTextBox1.Text += (i + 1).ToString() + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < listView1.Items.Count; i++)
            {
                ListViewItem t = listView1.Items[i];
                t.SubItems.Add((rank[i] + 1).ToString());
            }

            flag_check_score_done = 1;
        }

    }
}

