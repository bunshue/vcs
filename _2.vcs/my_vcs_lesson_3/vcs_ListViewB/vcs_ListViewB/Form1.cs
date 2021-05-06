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

            // Add data rows.
            listView1.AddRow(new string[] { "C# 5.0 Programmer's Reference", "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", "978-1-118-84728-2", "960", "2014" });
            listView1.AddRow(new string[] { "MCSD Certification Toolkit (Exam 70-483): Programming in C#", "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", "978-1-118-61209-5", "648", "2013" });
            listView1.AddRow(new string[] { "Visual Basic 2012 Programmer's Reference", "http://www.wrox.com/WileyCDA/WroxTitle/Visual-Basic-2012-Programmer-s-Reference.productCd-1118314077.html", "978-1-118-31407-4", "840", "2012" });
            listView1.AddRow("Essential Algorithms: A Practical Approach to Computer Algorithms", "http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118612108.html", "978-1-118-61210-1", "624", "2013");
            listView1.AddRow("Beginning Database Design Solutions", "http://www.vb-helper.com/db_design.htm", "978-0-470-38549-4", "552", "2008");
            listView1.AddRow("Start Here! Fundamentals of Microsoft .NET Programming", "http://www.amazon.com/Start-Here-Fundamentals-Microsoft-Programming/dp/0735661685", "978-0-735-66168-4", "264", "2011");

            // Make the ListView column headers.
            listView1.MakeColumnHeaders(
                "Title", HorizontalAlignment.Left,
                "URL", HorizontalAlignment.Left,
                "ISBN", HorizontalAlignment.Left,
                "Pages", HorizontalAlignment.Right,
                "Year", HorizontalAlignment.Right
            );

            // Size the columns to fit the data and colummn headers.
            listView1.SizeColumns(-2);

            // Make the form big enough to show the ListView.
            Rectangle item_rect =
                listView1.GetItemRect(listView1.Items.Count - 1);
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

