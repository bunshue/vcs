using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_listview2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.Columns.Add("Name", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("Chinese", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("English", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("Math", 100, HorizontalAlignment.Center);

            ListViewItem i1 = new ListViewItem("John");
            ListViewItem.ListViewSubItem sub_i1 = new ListViewItem.ListViewSubItem();
            sub_i1.Text = "80";
            i1.SubItems.Add(sub_i1.Text);
            sub_i1.Text = "87";
            i1.SubItems.Add(sub_i1.Text);
            sub_i1.Text = "92";
            i1.SubItems.Add(sub_i1.Text);


            ListViewItem i2 = new ListViewItem("Sue");
            ListViewItem.ListViewSubItem sub_i2 = new ListViewItem.ListViewSubItem();
            sub_i2.Text = "93";
            i2.SubItems.Add(sub_i2.Text);
            sub_i2.Text = "80";
            i2.SubItems.Add(sub_i2.Text);
            sub_i2.Text = "77";
            i2.SubItems.Add(sub_i2.Text);

            ListViewItem i3 = new ListViewItem("Tom");
            ListViewItem.ListViewSubItem sub_i3 = new ListViewItem.ListViewSubItem();
            sub_i3.Text = "85";
            i3.SubItems.Add(sub_i3.Text);
            sub_i3.Text = "88";
            i3.SubItems.Add(sub_i3.Text);
            sub_i3.Text = "91";
            i3.SubItems.Add(sub_i3.Text);

            listView1.Items.Add(i1);
            listView1.Items.Add(i2);
            listView1.Items.Add(i3);

            //AddRange()的用法
            ListViewItem i4 = new ListViewItem("David");
            i4.SubItems.Add("95");
            i4.SubItems.Add("96");
            i4.SubItems.Add("98");
            listView1.Items.AddRange(new ListViewItem[] { i4 });

            listView1.GridLines = true;


        }


        private void button1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i <= listView1.Items.Count - 1; i++)
            {
                ListViewItem t = listView1.Items[i];
                t.UseItemStyleForSubItems = false;
                if (int.Parse(t.SubItems[1].Text) < 90)
                {
                    t.SubItems[1].ForeColor = Color.Red;
                }
                if (int.Parse(t.SubItems[2].Text) < 90)
                {
                    t.SubItems[2].ForeColor = Color.Red;
                }
                if (int.Parse(t.SubItems[3].Text) < 90)
                {
                    t.SubItems[3].ForeColor = Color.Red;
                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "count = " + listView1.Items.Count.ToString() + "\n";
            richTextBox1.Text += "i\tname\tchi\teng\tmath\n";
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + listView1.Items[i].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\t" + listView1.Items[i].SubItems[3].Text + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }

        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            //C# listview 取得點選的值
            string str1 = listView1.FocusedItem.Text;
            string str2 = listView1.FocusedItem.SubItems[1].Text;
            string str3 = listView1.FocusedItem.SubItems[2].Text;
            string str4 = listView1.FocusedItem.SubItems[3].Text;

            richTextBox1.Text += str1 + "\t" + str2 + "\t" + str3 + "\t" + str4 + "\n";

        }


    
    }
}
