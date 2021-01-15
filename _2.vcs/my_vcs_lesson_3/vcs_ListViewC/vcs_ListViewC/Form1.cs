using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewC
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadStandardDateFormats();
            LoadStandardNumberFormats();
        }

        void LoadStandardDateFormats()
        {
            DateTime now = DateTime.Now;
            listView1.Items.Add(new ListViewItem(new String[] { "Short date", "d", now.ToString("d") }, listView1.Groups[0]));
            listView1.Items.Add(new ListViewItem(new String[] { "Long date", "D", now.ToString("D") }, listView1.Groups[0]));
            listView1.Items.Add(new ListViewItem(new String[] { "Month/day", "M or m", now.ToString("m") }, listView1.Groups[0]));
            listView1.Items.Add(new ListViewItem(new String[] { "Year/month", "Y or y", now.ToString("y") }, listView1.Groups[0]));

            listView1.Items.Add(new ListViewItem(new String[] { "Short time", "t", now.ToString("t") }, listView1.Groups[1]));
            listView1.Items.Add(new ListViewItem(new String[] { "Long time", "T", now.ToString("T") }, listView1.Groups[1]));

            listView1.Items.Add(new ListViewItem(new String[] { "Full date/time (short time)", "f", now.ToString("f") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "Full date/time (long time)", "F", now.ToString("F") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "General date/time (short time)", "g", now.ToString("g") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "General date/time (long time)", "G", now.ToString("G") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "Round-trip date/time", "O or o", now.ToString("o") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "RFC1123", "R or r", now.ToString("r") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "Sortable date/time", "s", now.ToString("s") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "Universal sortable date/time", "u", now.ToString("s") }, listView1.Groups[2]));
            listView1.Items.Add(new ListViewItem(new String[] { "Universal full date/time", "U", now.ToString("u") }, listView1.Groups[2]));

            // Generate code for an HTML table.
            Console.WriteLine(ListViewToHtmlTable(listView1, 1, 0, 5));
        }

        void LoadStandardNumberFormats()
        {
            double float_value = -12345.6789;

            listView2.Items.Add(new ListViewItem(new String[] { "Currency", "C or c", float_value.ToString("C") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "Exponential", "E or e", float_value.ToString("E") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "Fixed Point", "F or f", float_value.ToString("F") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "General", "G or g", float_value.ToString("G") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "Number", "N or n", float_value.ToString("N") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "Percent", "P or p", float_value.ToString("P") }, listView2.Groups[0]));
            listView2.Items.Add(new ListViewItem(new String[] { "Round-trip", "R or r", float_value.ToString("R") }, listView2.Groups[0]));

            int int_value = -123456789;
            listView2.Items.Add(new ListViewItem(new String[] { "Decimal", "D or d", int_value.ToString("D") }, listView2.Groups[1]));
            listView2.Items.Add(new ListViewItem(new String[] { "Hexadecimal", "H or h", int_value.ToString("X") }, listView2.Groups[1]));

            // Generate code for an HTML table.
            Console.WriteLine(ListViewToHtmlTable(listView2, 1, 0, 5));
        }

        // Return an HTML table showing the ListView's contents.
        private string ListViewToHtmlTable(ListView lvw, int border, int cell_spacing, int cell_padding)
        {
            // Open the <table> element.
            string txt = "<table " +
                "border=\"" + border.ToString() + "\" " +
                "cellspacing=\"" + cell_spacing.ToString() + "\" " +
                "cellpadding=\"" + cell_padding.ToString() + "\">\n";

            // See how many columns there are.
            int num_cols = lvw.Columns.Count;

            // See if there are any non-grouped items.
            bool have_non_grouped_items = false;
            foreach (ListViewItem item in lvw.Items)
            {
                if (item.Group == null)
                {
                    have_non_grouped_items = true;
                    break;
                }
            }

            // Display non-grouped items.
            if (have_non_grouped_items)
            {
                // Display the column headers.
                txt += ListViewColumnHeaderHtml(lvw);

                // Display the non-grouped items.
                foreach (ListViewItem item in lvw.Items)
                {
                    if (item.Group == null)
                    {
                        // Display this item.
                        txt += ListViewItemHtml(item);
                    }
                }
            }

            // Process the groups.
            foreach (ListViewGroup grp in lvw.Groups)
            {
                // Display the header.
                txt += "  <tr><th " +
                    "colspan=\"" + num_cols + "\" " +
                    "align=\"" + grp.HeaderAlignment.ToString() + "\" " +
                    "bgcolor=\"LightBlue\">" +
                    grp.Header + "</th></tr>\n";

                // Display the column headers.
                txt += ListViewColumnHeaderHtml(lvw);

                // Display the items in the group.
                foreach (ListViewItem item in grp.Items)
                {
                    txt += ListViewItemHtml(item);
                }
            }
            txt += "</table>\n";
            return txt;
        }

        // Return a string representing ListView column headers.
        private string ListViewColumnHeaderHtml(ListView lvw)
        {
            // Display the column headers.
            string txt = "  <tr>";
            foreach (ColumnHeader col in lvw.Columns)
            {
                // Display this column header.
                txt += "<th bgcolor=\"#CCFFFF\"" +
                    "width=\"" + col.Width.ToString() + "\" " +
                    "align=\"" + col.TextAlign.ToString() + "\">" +
                    col.Text + "</th>";
            }
            txt += "</tr>\n";
            return txt;
        }

        // Return the HTML text representing this item's row.
        private string ListViewItemHtml(ListViewItem item)
        {
            string txt = "  <tr>";
            ListView lvw = item.ListView;
            for (int i = 0; i < item.SubItems.Count; i++)
            {
                txt += "<td " +
                    "align=\"" + lvw.Columns[i].TextAlign.ToString() + "\">" +
                    item.SubItems[i].Text + "</td>";
            }
            txt += "</tr>\n";
            return txt;
        }
    }
}
