using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_HTML2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            double float_value = -12345.6789;

            lvwResults.Items.Add(new ListViewItem(new String[] { "Currency", "C or c", float_value.ToString("C") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Exponential", "E or e", float_value.ToString("E") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Fixed Point", "F or f", float_value.ToString("F") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "General", "G or g", float_value.ToString("G") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Number", "N or n", float_value.ToString("N") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Percent", "P or p", float_value.ToString("P") }, lvwResults.Groups[0]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Round-trip", "R or r", float_value.ToString("R") }, lvwResults.Groups[0]));

            int int_value = -123456789;
            lvwResults.Items.Add(new ListViewItem(new String[] { "Decimal", "D or d", int_value.ToString("D") }, lvwResults.Groups[1]));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Hexadecimal", "H or h", int_value.ToString("X") }, lvwResults.Groups[1]));

            // Miscellaneous stuff.
            lvwResults.Items.Add(new ListViewItem(new String[] { "Apple", "Dog", "Book" } ));
            lvwResults.Items.Add(new ListViewItem(new String[] { "Penny", "Catabalpas", "Pickle" }));
        }

        // Display an HTML table showing the ListView's contents.
        private void btnGo_Click(object sender, EventArgs e)
        {
            wbrTable.DocumentText = ListViewToHtmlTable(lvwResults, 1, 1, 2);
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
