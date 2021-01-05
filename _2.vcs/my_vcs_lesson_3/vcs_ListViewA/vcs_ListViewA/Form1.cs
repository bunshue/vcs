#define Use_IndexOf
#define Use_HitTest

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewA
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Set the listView's column sizes to the same value.
        private void SetListViewColumnSizes(ListView lvw, int width)
        {
            foreach (ColumnHeader col in lvw.Columns)
                col.Width = width;
        }

        // Make all of the columns 100 pixels wide.
        private void btnSize100_Click(object sender, EventArgs e)
        {
            SetListViewColumnSizes(listView1, 100);
            SizeForm();
        }

        // Size the columns to fit their data.
        private void btnSizeMinus1_Click(object sender, EventArgs e)
        {
            SetListViewColumnSizes(listView1, -1);
            SizeForm();
        }

        // Size the columns to fit their data and column headers.
        private void btnSizeMinus2_Click(object sender, EventArgs e)
        {
            SetListViewColumnSizes(listView1, -2);
            SizeForm();
        }

        // Make the ListView fit its data
        // and make the form fit the listView.
        private void SizeForm()
        {
            // Add up the column widths.
            int wid = 0;
            foreach (ColumnHeader col in listView1.Columns)
        {
                wid += col.Width;
            }

            // Size the ListView and form.
            listView1.Width = wid + 5;
            this.ClientSize = new Size(
                listView1.Right + listView1.Left,
                this.ClientSize.Height);
        }

        // Display some data.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Remove any existing items.
            listView1.Items.Clear();

            // Create some data.
            // Name, URL, ISBN, pages, year.
            string[,] data =
            {
                { "C# 5.0 Programmer's Reference", "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", "978-1-118-84728-2", "960", "2014" },
                { "MCSD Certification Toolkit (Exam 70-483): Programming in C#", "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", "978-1-118-61209-5", "648", "2013" },
                { "Visual Basic 2012 Programmer's Reference", "http://www.wrox.com/WileyCDA/WroxTitle/Visual-Basic-2012-Programmer-s-Reference.productCd-1118314077.html", "978-1-118-31407-4", "840", "2012" },
                { "Essential Algorithms: A Practical Approach to Computer Algorithms ", "http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118612108.html", "978-1-118-61210-1", "624", "2013" },
                { "Beginning Database Design Solutions", "http://www.vb-helper.com/db_design.htm", "978-0-470-38549-4", "552", "2008" },
                { "Start Here! Fundamentals of Microsoft .NET Programming", "http://www.amazon.com/Start-Here-Fundamentals-Microsoft-Programming/dp/0735661685", "978-0-735-66168-4", "264", "2011" },
            };

            // Make the ListView's column headers.
            listView1.Columns.Clear();
            listView1.Columns.Add("Title", 250);
            listView1.Columns.Add("URL", 250);
            listView1.Columns.Add("ISBN", 150);
            listView1.Columns.Add("Number of Pages", 50, HorizontalAlignment.Right);
            listView1.Columns.Add("Publication Year", 50, HorizontalAlignment.Right);

            // Add the data.
            CopyArrayToListView(listView1, data);

            // Display the details view.
            listView1.View = View.Details;

            /* 自動格式化listView
            // Size the columns to fit the data and colummn headers.
            listView1.SizeColumns(-2);

            // Make the form big enough to show the ListView.
            Rectangle item_rect =
                listView1.GetItemRect(listView1.Items.Count - 1);
            this.ClientSize = new Size(
                item_rect.Left + item_rect.Width + 25,
                item_rect.Top + item_rect.Height + 75);
            */
        }

        // Display the row and column under the mouse.
        private void listView1_MouseMove(object sender, MouseEventArgs e)
        {
            txtRow.Clear();
            txtColumn.Clear();

#if Use_IndexOf
            // Method 3: Use HitTest and IndexOf.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            txtColumn.Text = item.SubItems.IndexOf(hti.SubItem).ToString();
#elif Use_HitTest
            // Method 2: Use HitTest.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            ListViewItem.ListViewSubItem subitem = hti.SubItem;
            for (int i = 0; i < item.SubItems.Count; i++)
            {
                if (item.SubItems[i] == subitem)
                {
                    txtColumn.Text = i.ToString();
                }
            }
#else
            // Method 1: Use the FindListViewRowColumn method.
            int row, column;
            if (listView1.FindListViewRowColumn(e.X, e.Y, out row, out column))
            {
                txtRow.Text = row.ToString();
                txtColumn.Text = column.ToString();
            }
#endif
        }

        // Copy a two-dimensional array of data into a ListView.
        private void CopyArrayToListView(ListView lvw, string[,] data)
        {
            int max_row = data.GetUpperBound(0);
            int max_col = data.GetUpperBound(1);
            for (int row = 0; row <= max_row; row++)
            {
                ListViewItem new_item = lvw.Items.Add(data[row, 0]);
                for (int col = 1; col <= max_col; col++)
                {
                    new_item.SubItems.Add(data[row, col]);
                }
            }
        }

    }
}
