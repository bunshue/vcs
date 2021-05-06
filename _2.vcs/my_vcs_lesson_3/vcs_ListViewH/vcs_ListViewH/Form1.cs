using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewH
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //listView檢視方法
            listView1.View = View.Details;

            //listView製作標題
            listView1.SetColumnHeaders(
                new object[] {
                    "Title", HorizontalAlignment.Left,
                    "URL", HorizontalAlignment.Left,
                    "ISBN", HorizontalAlignment.Left,
                    "Picture", HorizontalAlignment.Left,
                    "Pages", HorizontalAlignment.Right,
                    "Year", HorizontalAlignment.Right,
                    "Pub Date", HorizontalAlignment.Right
                });

            // Remove any existing items.
            listView1.Items.Clear();

            // Add data rows.
            listView1.AddRow("Ready-to-Run Visual Basic Algorithms", "http://www.vb-helper.com/vba.htm", "0-471-24268-3", "http://www.vb-helper.com/vba.jpg", "395", "1998", "1/5/1998");
            listView1.AddRow("Visual Basic Graphics Programming", "http://www.vb-helper.com/vbgp.htm", "0-472-35599-2", "http://www.vb-helper.com/vbgp.jpg", "712", "2000", "2/2/2000");
            listView1.AddRow("Advanced Visual Basic Techniques", "http://www.vb-helper.com/avbt.htm", "0-471-18881-6", "http://www.vb-helper.com/avbt.jpg", "440", "1997", "3/3/1997");
            listView1.AddRow("Custom Controls Library", "http://www.vb-helper.com/ccl.htm", "0-471-24267-5", "http://www.vb-helper.com/ccl.jpg", "684", "1998", "10/10/1998");
            listView1.AddRow("Ready-to-Run Delphi Algorithms", "http://www.vb-helper.com/da.htm", "0-471-25400-2", "http://www.vb-helper.com/da.jpg", "398", "1998", "01/20/1998");
            listView1.AddRow("Bug Proofing Visual Basic", "http://www.vb-helper.com/err.htm", "0-471-32351-9", "http://www.vb-helper.com/err.jpg", "397", "1999", "5/5/1999");
            listView1.AddRow("Ready-to-Run Visual Basic Code Library", "http://www.vb-helper.com/vbcl.htm", "0-471-33345-X", "http://www.vb-helper.com/vbcl.jpg", "424", "1999", "8/8/1999");

            listView1.AddRow("Bogus Book", "http://www.noplace.com/bogus.htm", "0-123-45678-9", "http://www.noplace.com/bogus.jpg", "100", "6", "1/09/1998");
            listView1.AddRow("Fakey", "http://www.skatepark.com/fakey.htm", "9-876-54321-0", "http://www.skatepark.com/fakey.jpg", "9", "700", "1/08/1998");

            // Size the columns.    //欄位對齊標題欄
            listView1.SizeColumnsToFitDataAndHeaders();

            // Size the columns.    //欄位對齊資料
            //listView1.SizeColumnsToFitData();

            // Make the form big enough to show the ListView.
            Rectangle item_rect =
                listView1.GetItemRect(listView1.Columns.Count - 1);
            this.SetClientSizeCore(
                item_rect.Left + item_rect.Width + 50,
                item_rect.Top + item_rect.Height + 75);
        }

        // Sort on clicked columns.
        private void radSortClickedColumn_Click(object sender, EventArgs e)
        {
            listView1.SetSortMode(ListViewExtensions.SortMode.SortOnClickedColumn);
        }

        // Sort on all columns.
        private void radSortAllColumns_Click(object sender, EventArgs e)
        {
            listView1.SetSortMode(ListViewExtensions.SortMode.SortOnAllColumns);
        }

        // Do not sort.
        private void radNoSort_Click(object sender, EventArgs e)
        {
            listView1.SetSortMode(ListViewExtensions.SortMode.SortNone);
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //listView接受鍵盤的Delete鍵
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
