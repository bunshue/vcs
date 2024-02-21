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
            ListViewGroup group1 = new ListViewGroup("Group 1");
            ListViewGroup group2 = new ListViewGroup("Group 2");
            lvwBooks.Groups.Add(group1);
            lvwBooks.Groups.Add(group2);

            // Group 1.
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "鼠",
                    "mouse", 
                    "3", 
                    "米老鼠", "2014"},
                group1));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "牛",
                    "ox", 
                    "48", 
                    "班尼牛", "2013"},
                group1));

            // Group 2
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "龍",
                    "dragon", 
                    "38", 
                    "逗逗龍", "2012"},
                group2));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "蛇",
                    "snake", 
                    "16", 
                    "貪吃蛇", "2008"},
                group2));

            // Misc.
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "猴",
                    "monkey", 
                    "22", 
                    "山道猴", "2013"}));
            lvwBooks.Items.Add(new ListViewItem(new string[]
                {   "雞", 
                    "chicken", 
                    "6", 
                    "肯德雞", "2011"}));
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
