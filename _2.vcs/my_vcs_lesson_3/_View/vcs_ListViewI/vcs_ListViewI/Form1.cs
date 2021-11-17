using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_ListViewI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Select whole rows.
            listView1.FullRowSelect = true;

            // Add some groups to the ListView.
            ListViewGroup csharp_group = new ListViewGroup("C# Books");
            ListViewGroup vb_group = new ListViewGroup("Visual Basic Books");
            listView1.Groups.Add(csharp_group);
            listView1.Groups.Add(vb_group);

            // C# Books.
            ListViewItem new_item;
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "C# 5.0 Programmer's Reference",
                    "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", 
                    "960", "2014"},
                csharp_group));
            new_item.Tag = "1118847288";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "MCSD Certification Toolkit (Exam 70-483): Programming in C#",
                    "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", 
                    "648", "2013"},
                csharp_group));
            new_item.Tag = "1118612094";

            // Visual Basic.
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "Visual Basic 2012 Programmer's Reference",
                    "http://www.wrox.com/WileyCDA/WroxTitle/Visual-Basic-2012-Programmer-s-Reference.productCd-1118314077.html", 
                    "840", "2012"},
                vb_group));
            new_item.Tag = "1118314077";

            // Misc.
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "Essential Algorithms: A Practical Approach to Computer Algorithms ",
                    "http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118612108.html", 
                    "624", "2013"}));
            new_item.Tag = "1118612108";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "Beginning Database Design Solutions",
                    "http://www.vb-helper.com/db_design.htm", 
                    "552", "2008"},
                csharp_group));
            new_item.Tag = "0470385499";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "Start Here! Fundamentals of Microsoft .NET Programming", 
                    "http://www.amazon.com/Start-Here-Fundamentals-Microsoft-Programming/dp/0735661685", 
                    "264", "2011"}));
            new_item.Tag = "0735661685";
        }

        private void mnuViewDetail_Click(object sender, EventArgs e)
        {
            listView1.View = View.Details;
            CheckMenuItem(mnuView, mnuViewDetail);
        }
        private void mnuViewLargeIcon_Click(object sender, EventArgs e)
        {
            listView1.View = View.LargeIcon;
            CheckMenuItem(mnuView, mnuViewLargeIcon);
        }
        private void mnuViewList_Click(object sender, EventArgs e)
        {
            listView1.View = View.List;
            CheckMenuItem(mnuView, mnuViewList);
        }
        private void mnuViewSmallIcon_Click(object sender, EventArgs e)
        {
            listView1.View = View.SmallIcon;
            CheckMenuItem(mnuView, mnuViewSmallIcon);
        }
        private void mnuViewTile_Click(object sender, EventArgs e)
        {
            listView1.View = View.Tile;
            CheckMenuItem(mnuView, mnuViewTile);
        }

        // Uncheck all menu items in this menu except checked_item.
        private void CheckMenuItem(ToolStripMenuItem mnu, ToolStripMenuItem checked_item)
        {
            // Uncheck all of the menu items.
            foreach (ToolStripItem item in mnu.DropDownItems)
            {
                if (item is ToolStripMenuItem)
                {
                    ToolStripMenuItem menu_item = item as ToolStripMenuItem;
                    menu_item.Checked = false;
                }
            }

            // Check the one that should be checked.
            checked_item.Checked = true;
        }

        // Open the Amazon page for the selected book.
        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count < 1) return;

            // Get the selected item.
            ListViewItem selected_item =
                listView1.SelectedItems[0];

            // Use the Tag value to build the URL.
            string url = "http://www.amazon.com/gp/product/@ISBN@";
            url = url.Replace("@ISBN@", (string)selected_item.Tag);

            // Open the URL.
            Process.Start(url);
        }
    }
}
