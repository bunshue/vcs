using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListView9
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            fill_listview_table();
        }

        void fill_listview_table()
        {
            // Add some groups to the ListView.
            ListViewGroup csharp_group = new ListViewGroup("C# Books");
            ListViewGroup vb_group = new ListViewGroup("Visual Basic Books");
            lvwBooks.Groups.Add(csharp_group);
            lvwBooks.Groups.Add(vb_group);

            // C# Books.
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "C# 5.0 Programmer's Reference",
                    "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", 
                    "978-1-118-84728-2", 
                    "960", "2014"},
                csharp_group));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "MCSD Certification Toolkit (Exam 70-483): Programming in C#",
                    "http://www.wrox.com/WileyCDA/WroxTitle/C-5-0-Programmer-s-Reference.productCd-1118847288.html", 
                    "978-1-118-61209-5", 
                    "648", "2013"},
                csharp_group));

            // Visual Basic.
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "Visual Basic 2012 Programmer's Reference",
                    "http://www.wrox.com/WileyCDA/WroxTitle/Visual-Basic-2012-Programmer-s-Reference.productCd-1118314077.html", 
                    "978-1-118-31407-4", 
                    "840", "2012"},
                vb_group));

            // Misc.
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "Essential Algorithms: A Practical Approach to Computer Algorithms ",
                    "http://www.wiley.com/WileyCDA/WileyTitle/productCd-1118612108.html", 
                    "978-1-118-61210-1", 
                    "624", "2013"}));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "Beginning Database Design Solutions",
                    "http://www.vb-helper.com/db_design.htm", 
                    "978-0-470-38549-4", 
                    "552", "2008"},
                csharp_group));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "Start Here! Fundamentals of Microsoft .NET Programming", 
                    "http://www.amazon.com/Start-Here-Fundamentals-Microsoft-Programming/dp/0735661685", 
                    "978-0-735-66168-4", 
                    "264", "2011"}));
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

        private void button1_Click(object sender, EventArgs e)
        {
            lvwBooks.View = View.Details;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            lvwBooks.View = View.LargeIcon;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            lvwBooks.View = View.List;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            lvwBooks.View = View.SmallIcon;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            lvwBooks.View = View.Tile;
        }
    }
}
