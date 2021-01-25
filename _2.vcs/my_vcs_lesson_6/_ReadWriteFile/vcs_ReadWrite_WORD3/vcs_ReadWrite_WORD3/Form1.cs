using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Add a reference to Microsoft.Office.Interop.Word.

using Word = Microsoft.Office.Interop.Word;

namespace vcs_ReadWrite_WORD3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Load the timezone lists.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Select the current date.
            dtpDate.Value = DateTime.Now;

            // Initialize the timezone lists.
            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                cboTimeZone1.Items.Add(info);
                cboTimeZone2.Items.Add(info);
            }

            // Select some defaults.
            SelectItemContaining(cboTimeZone1, "Mountain Time");
            SelectItemContaining(cboTimeZone2, "Tokyo");
        }

        // Select an item containing the target string.
        private void SelectItemContaining(ComboBox cbo, string target)
        {
            foreach (object item in cbo.Items)
            {
                if (item.ToString().Contains(target))
                {
                    cbo.SelectedItem = item;
                    return;
                }
            }

            // Select the first item.
            cbo.SelectedIndex = 0;
        }

        // Make a conversion chart.
        private void btnMakeChart_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "製作一個docx檔案 使用表格 ST\n";

            // Get the timezone information.
            TimeZoneInfo zone1 = cboTimeZone1.SelectedItem as TimeZoneInfo;
            TimeZoneInfo zone2 = cboTimeZone2.SelectedItem as TimeZoneInfo;

            // Get the Word application object.
            Word._Application word_app = new Word.Application();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Create the Word document.
            object missing = Type.Missing;
            Word._Document word_doc = word_app.Documents.Add(ref missing, ref missing, ref missing, ref missing);

            // Create a table.
            object start = 0;
            Word.Range range = word_doc.Range(ref start, ref start);
            object collapse_end = Word.WdCollapseDirection.wdCollapseEnd;
            range.Collapse(ref collapse_end);
            object default_table_behavior = Word.WdDefaultTableBehavior.wdWord9TableBehavior;
            object auto_fit_behavior = Word.WdAutoFitBehavior.wdAutoFitContent;
            Word.Table word_table = word_doc.Tables.Add(range, 25, 2, ref default_table_behavior, ref auto_fit_behavior);

            // Compose the headers.
            string name1 = zone1.DisplayName;
            name1 = name1.Replace(") ", ")\n");
            name1 = name1.Replace(" (", "\n(");
            if (name1.EndsWith("\n"))
            {
                name1 = name1.Substring(0, name1.Length - 1);
            }
            string name2 = zone2.DisplayName;
            name2 = name2.Replace(") ", ")\n");
            name2 = name2.Replace(" (", "\n(");
            if (name2.EndsWith("\n"))
            {
                name2 = name2.Substring(0, name2.Length - 2);
            }

            word_table.Cell(1, 1).Range.Text = name1;
            word_table.Cell(1, 2).Range.Text = name2;

            // Draw the hour conversions.
            DateTime time1 = new DateTime(DateTime.Now.Year, DateTime.Now.Month, DateTime.Now.Day, 0, 0, 0);
            for (int hour = 1; hour <= 24; hour++)
            {
                word_table.Cell(hour + 1, 1).Range.Text = time1.ToShortTimeString();

                DateTime time2 = TimeZoneInfo.ConvertTime(time1, zone1, zone2);
                string text2 = time2.ToShortTimeString();
                if (time1.Date < time2.Date)
                {
                    text2 += " (tomorrow)";
                }
                else if (time1.Date > time2.Date)
                {
                    text2 += " (yesterday)";
                }
                word_table.Cell(hour + 1, 2).Range.Text = text2;

                time1 = time1.AddHours(1);
            }

            // Center the table's columns.
            word_table.Range.Font.Size = 10;
            word_table.Range.Font.Name = "Times New Roman";
            word_table.Range.ParagraphFormat.Alignment =
                Word.WdParagraphAlignment.wdAlignParagraphCenter;
            word_table.Range.ParagraphFormat.LineSpacingRule =
                Word.WdLineSpacing.wdLineSpaceExactly;
            word_table.Range.ParagraphFormat.LineSpacing = 12f;
            word_table.Range.ParagraphFormat.SpaceAfter = 0f;

            // Save the document.
            string filename = Application.StartupPath + "\\word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".docx";

            object filename_obj = filename;
            word_doc.SaveAs(ref filename_obj, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing);

            // Close down Word.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "製作一個docx檔案 使用表格 完成\n";
        }
    }
}
