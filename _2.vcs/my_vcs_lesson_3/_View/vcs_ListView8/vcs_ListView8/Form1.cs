using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Make some data.
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

            // Size the columns.
            listView1.SizeColumns(-2);
        }

        // The column we are currently using for sorting.
        private ColumnHeader SortingColumn = null;

        // Sort on this column.
        private void listView1_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            // Get the new sorting column.
            ColumnHeader new_sorting_column = listView1.Columns[e.Column];

            // Figure out the new sorting order.
            System.Windows.Forms.SortOrder sort_order;
            if (SortingColumn == null)
            {
                // New column. Sort ascending.
                sort_order = SortOrder.Ascending;
            }
            else
            {
                // See if this is the same column.
                if (new_sorting_column == SortingColumn)
                {
                    // Same column. Switch the sort order.
                    if (SortingColumn.Text.StartsWith("> "))
                    {
                        sort_order = SortOrder.Descending;
                    }
                    else
                    {
                        sort_order = SortOrder.Ascending;
                    }
                }
                else
                {
                    // New column. Sort ascending.
                    sort_order = SortOrder.Ascending;
                }

                // Remove the old sort indicator.
                SortingColumn.Text = SortingColumn.Text.Substring(2);
            }

            // Display the new sort order.
            SortingColumn = new_sorting_column;
            if (sort_order == SortOrder.Ascending)
            {
                SortingColumn.Text = "> " + SortingColumn.Text;
            }
            else
            {
                SortingColumn.Text = "< " + SortingColumn.Text;
            }

            // Create a comparer.
            listView1.ListViewItemSorter = new ListViewComparer(e.Column, sort_order);

            // Sort.
            listView1.Sort();
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

