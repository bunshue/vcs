using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Remove any existing items.
            listView1.Items.Clear();

            // 加入列資料
            listView1.AddRow(new string[] { "鼠", "mouse", "3", "米老鼠", "2014" });
            listView1.AddRow(new string[] { "牛", "ox", "48", "班尼牛", "2013" });
            listView1.AddRow(new string[] { "虎", "tiger", "33", "跳跳虎", "2012" });
            listView1.AddRow("兔", "rabbit", "8", "彼得兔", "2013");
            listView1.AddRow("龍", "dragon", "38", "逗逗龍", "2008");
            listView1.AddRow("蛇", "snake", "16", "貪吃蛇", "2011");

            // Make the ListView column headers.
            listView1.MakeColumnHeaders(
                "中文名", HorizontalAlignment.Left,
                "英文名", HorizontalAlignment.Left,
                "體重", HorizontalAlignment.Left,
                "代表", HorizontalAlignment.Right,
                "Year", HorizontalAlignment.Right
            );

            // Size the columns to fit the data and colummn headers.
            listView1.SizeColumns(-2);

            // Make the form big enough to show the ListView.
            Rectangle item_rect =
                listView1.GetItemRect(listView1.Items.Count - 1);
        }

        //listView接受鍵盤的Delete鍵
        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox1.Text += "你在listView按了 : " + e.KeyCode + "\n";
            if (e.KeyCode == Keys.Delete)
            {
                if (listView1.SelectedItems.Count > 0)
                {
                    listView1.SelectedItems[0].Remove();
                }
            }
        }
    }
}
