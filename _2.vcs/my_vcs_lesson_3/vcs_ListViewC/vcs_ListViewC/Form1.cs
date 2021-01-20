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
            LoadCustomDateFormats();
            LoadCustomNumberFormats();
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

        void LoadCustomDateFormats()
        {
            DateTime now = DateTime.Now;
            listView3.Items.Add(new ListViewItem(new String[] { "Day of month (1 - 31)", "d", now.ToString("%d") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Day of month (01 - 31)", "dd", now.ToString("dd") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Abbreviated day of week", "ddd", now.ToString("ddd") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Full day of week", "dddd", now.ToString("ddd") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Month (1 - 12)", "M", now.ToString("%M") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Month (01 - 12)", "MM", now.ToString("MM") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Month abbreviation", "MMM", now.ToString("MMM") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Month name", "MMMM", now.ToString("MMMM") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Year (0 - 99)", "y", now.ToString("%y") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Year (01 - 99)", "yy", now.ToString("yy") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Year (minimum 3 digits)", "yyy", now.ToString("yyy") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Year (4 digits)", "yyyy", now.ToString("yyyy") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Year (5 digits)", "yyyyy", now.ToString("yyyyy") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Era", "g", now.ToString("%g") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Era", "gg", now.ToString("gg") }, listView3.Groups[0]));
            listView3.Items.Add(new ListViewItem(new String[] { "Date separator", "/", now.ToString("%/") }, listView3.Groups[0]));

            listView3.Items.Add(new ListViewItem(new String[] { "Hour (1 - 12)", "h", now.ToString("%h") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Hour (01 - 12)", "hh", now.ToString("hh") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Hour (1 - 23)", "H", now.ToString("%H") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Hour (01 - 23)", "HH", now.ToString("HH") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Minute (0 - 59)", "m", now.ToString("%m") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Minute (00 - 59)", "mm", now.ToString("mm") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Second (0 - 59)", "s", now.ToString("%s") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Second (00 - 59)", "ss", now.ToString("ss") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Tenths of seconds", "f", now.ToString("%f") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Hundredths of seconds", "ff", now.ToString("ff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Milliseconds", "fff", now.ToString("fff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Ten thousandths of seconds", "ffff", now.ToString("ffff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Hundred thousandths of seconds", "fffff", now.ToString("fffff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Millionths of seconds", "ffffff", now.ToString("ffffff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Ten millionths of seconds", "fffffff", now.ToString("fffffff") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "A/P", "t", now.ToString("%t") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "AM/PM", "tt", now.ToString("tt") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, tenths of seconds", "F", now.ToString("%F") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, hundredths of seconds", "FF", now.ToString("FF") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, milliseconds", "FFF", now.ToString("FFF") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, ten thousandths of seconds", "FFFF", now.ToString("FFFF") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, hundred thousandths of seconds", "FFFFF", now.ToString("FFFFF") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, millionths of seconds", "FFFFFF", now.ToString("FFFFFF") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "If non-zero, ten millionths of seconds", "FFFFFFF", now.ToString("FFFFFFF") }, listView3.Groups[1]));

            listView3.Items.Add(new ListViewItem(new String[] { "UTC hour offset", "z", now.ToString("%z") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "UTC hour offset with leading 0", "zz", now.ToString("zz") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "UTC hour and minute offset", "zzz", now.ToString("zzz") }, listView3.Groups[1]));
            listView3.Items.Add(new ListViewItem(new String[] { "Time separator", ":", now.ToString("%:") }, listView3.Groups[1]));

            // Generate code for an HTML table.
            Console.WriteLine(ListViewToHtmlTable(listView3, 1, 0, 5));
        }

        void LoadCustomNumberFormats()
        {
            listView4.Items.Add(new ListViewItem(new String[] { "Zero placeholder", "0", "A digit or 0 if no digit is present" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Digit placeholder", "#", "A digit or nothing if no digit is present" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Decimal separator", ".", "The decimal separator" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Thousands separator", ",", "Thousands separator" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Scaling", ",", "When placed at the end of the format string, divides by 1000" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Percent placeholder", "%", "Multiplies by 100 and inserts a percent symbol" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Per mille placeholder", "‰", "Multiplies by 100 and inserts a per mille symbol" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Exponentiation", "E+0", "Exponentiation." }));
            listView4.Items.Add(new ListViewItem(new String[] { "Escape character", "\\", "The following character is not interpreted as a formatting character" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Literal string", "'...'", "The characters in single or double quotes are displayed literally" }));
            listView4.Items.Add(new ListViewItem(new String[] { "Section separator", ";", "Creates up to three sections for values > 0, < 0, or = 0." }));

            listView5.Items.Add(new ListViewItem(new String[] { "123(\"00000\")", 123.ToString("00000") }));
            listView5.Items.Add(new ListViewItem(new String[] { "123(\"#####\")", 123.ToString("#####") }));
            listView5.Items.Add(new ListViewItem(new String[] { "123.4567(\"0.00\")", 123.4567.ToString("0.00") }));
            listView5.Items.Add(new ListViewItem(new String[] { "1234567890(\"#,#\")", 1234567890.ToString("#,#") }));
            listView5.Items.Add(new ListViewItem(new String[] { "1234567890(\"#,#,,\")", 1234567890.ToString("#,#,,") }));
            listView5.Items.Add(new ListViewItem(new String[] { "0.1234(\"#.#%\")", 0.1234.ToString("#.#%") }));
            listView5.Items.Add(new ListViewItem(new String[] { "1234567890(\"#E000\")", 1234567890.ToString("#E000") }));
            listView5.Items.Add(new ListViewItem(new String[] { "1234567890(\"#E+000\")", 1234567890.ToString("#E+000") }));
            listView5.Items.Add(new ListViewItem(new String[] { "0.00001234(\"#E000\")", 0.00001234.ToString("#E000") }));
            listView5.Items.Add(new ListViewItem(new String[] { "1.234(\"+0.00;<0.00>;-zero-\")", 1.234.ToString("+0.00;<0.00>;-zero-") }));
            listView5.Items.Add(new ListViewItem(new String[] { "-1.234(\"+0.00;<0.00>;-zero-\")", (-1.234).ToString("+0.00;<0.00>;-zero-") }));
            listView5.Items.Add(new ListViewItem(new String[] { "0(\"+0.00;<0.00>;-zero-\")", 0.ToString("+0.00;<0.00>;-zero-") }));

            // Generate code for an HTML tables.
            Console.WriteLine(ListViewToHtmlTable(listView4, 1, 0, 5));
            Console.WriteLine(ListViewToHtmlTable(listView5, 1, 0, 5));
        }

    }
}
