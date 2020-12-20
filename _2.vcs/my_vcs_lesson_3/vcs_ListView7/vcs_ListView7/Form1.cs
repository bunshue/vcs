using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make some data.
            // Remove any existing items.
            listView1.Items.Clear();

            // Add data rows.
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "1000" });
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "C" });
            ListViewMakeRow(listView1, "C", new string[] { "B", "C", "1000", "4/1/2014" });
            ListViewMakeRow(listView1, "A", new string[] { "B", "C", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "12/20/2013", "C" });
            ListViewMakeRow(listView1, "B", new string[] { "B" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A" });
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "20" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "12/20/2013", "A" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "1001", "8/20/2014" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "4/1/2014" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "100", "1/2/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "10" });

            // Make the ListView column headers.
            ListViewMakeColumnHeaders(listView1,
                new object[] {
                    "1", HorizontalAlignment.Left,
                    "2", HorizontalAlignment.Left,
                    "3", HorizontalAlignment.Left,
                    "4", HorizontalAlignment.Right,
                    "5", HorizontalAlignment.Right,
                    "6", HorizontalAlignment.Left
                });

            // Size the columns.
            foreach (ColumnHeader col in listView1.Columns)
            {
                col.Width = -2;
            }

            // Make the form big enough to show the ListView.
            Rectangle item_rect = listView1.GetItemRect(listView1.Columns.Count - 1);
            //Size new_size = new Size(item_rect.Left + item_rect.Width + 50, this.ClientSize.Height);
            //this.ClientSize = new_size;
        }

        // Make a ListView row.
        private void ListViewMakeRow(ListView lvw, String item_title, string[] subitem_titles)
        {
            // Make the item.
            ListViewItem new_item = lvw.Items.Add(item_title);

            // Make the sub-items.
            for (int i = subitem_titles.GetLowerBound(0); i <= subitem_titles.GetUpperBound(0); i++)
            {
                new_item.SubItems.Add(subitem_titles[i]);
            }
        }

        // Make the ListView's column headers.
        // The ParamArray entries should alternate between
        // strings and HorizontalAlignment values.
        private void ListViewMakeColumnHeaders(ListView lvw, Object[] header_info)
        {
            // Remove any existing headers.
            lvw.Columns.Clear();

            // Make the column headers.
            for (int i = header_info.GetLowerBound(0); i <= header_info.GetUpperBound(0); i += 2)
            {
                lvw.Columns.Add(
                    (string)header_info[i],
                    -1,
                    (HorizontalAlignment)header_info[i + 1]);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Sort ascending.

            // Create a comparer.
            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Ascending);

            // Sort.
            listView1.Sort();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Sort descending.

            // Create a comparer.
            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Descending);

            // Sort.
            listView1.Sort();


        }









    }
}
