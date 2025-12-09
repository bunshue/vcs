using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

// Open the Add References dialog. On the COM tab, select
// "Microsoft Word 12.0 Object Library" (or whatever version you have installed on your system). 
// Add a reference to Microsoft Word 14.0 Object Library.

using Microsoft.Office.Interop.Word;
using Word = Microsoft.Office.Interop.Word;
using Core = Microsoft.Office.Core;

//using System.Text.RegularExpressions;

// Open the Add References dialog. On the COM tab, select
// "Microsoft Word 12.0 Object Library" (or whatever version you
// have installed on your system). 

//using System.Threading;

//using Microsoft.Office.Interop.Word;


namespace vcs_ReadWrite_WORD1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // Load the timezone lists.
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 9);

            groupBox1.Location = new System.Drawing.Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Size = new Size(600, 440);
            richTextBox1.Location = new System.Drawing.Point(x_st + dx * 3, y_st + dy * 0 + 200);
            bt_clear.Location = new System.Drawing.Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

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

        private void button0_Click(object sender, EventArgs e)
        {
            //建立一Word檔案

            string pic_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\test.png";

            // Get the Word application object.
            Word._Application word_app = new Word.ApplicationClass();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Create the Word document.
            object missing = Type.Missing;
            Word._Document word_doc = word_app.Documents.Add(ref missing, ref missing,
                ref missing, ref missing);

            // Create a header paragraph.
            Word.Paragraph para = word_doc.Paragraphs.Add(ref missing);
            para.Range.Text = "Lorem Ipsum";
            object style_name = "Heading 1";
            //para.Range.set_Style(ref style_name);
            para.Range.InsertParagraphAfter();

            // Add some paragraphs.
            string[] paragraphs =
            {
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tristique id ex ac mollis. Maecenas vestibulum porta arcu ac dictum. Praesent placerat hendrerit dui eu porttitor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Phasellus vitae dui sit amet ligula feugiat accumsan in sit amet tellus. Duis lobortis justo nec lobortis tempor. Nunc sagittis egestas dolor, sit amet iaculis massa sagittis eu. Quisque et turpis a massa tincidunt pharetra non pretium felis. Morbi fringilla sapien eu ex interdum hendrerit non facilisis lacus. Donec fermentum eros ut lectus consectetur, at accumsan nunc dignissim. Etiam varius iaculis vestibulum. Sed id condimentum neque, quis efficitur elit.",
                "Nam lacinia, risus ac ullamcorper commodo, ex diam mollis augue, ac dictum lacus est quis enim. Praesent vestibulum lorem id sem aliquet finibus. Etiam elementum tempor hendrerit. Mauris id interdum sapien. Vestibulum id viverra velit, ut mollis libero. Pellentesque orci lacus, facilisis vitae laoreet nec, molestie non urna. Fusce interdum dolor in varius luctus. Praesent sit amet malesuada libero. Ut rutrum diam eget erat iaculis vulputate.",
                "Nunc nec leo congue, facilisis tellus et, dignissim arcu. Vivamus vehicula congue consequat. Aliquam erat volutpat. In at porta lectus, nec feugiat tortor. Suspendisse vitae pellentesque magna. Phasellus fermentum est ut mauris tincidunt, ac luctus nisi fermentum. Sed gravida blandit est. Phasellus egestas lorem at lacus dapibus semper. Vestibulum sodales rhoncus diam, vel semper nisl ultrices malesuada. Suspendisse mattis arcu nunc, quis ullamcorper turpis facilisis ut.",
                "Vivamus interdum diam id dictum consectetur. Ut nisi nisl, tincidunt in massa sit amet, sollicitudin accumsan ipsum. Sed leo eros, aliquet a augue non, placerat hendrerit tellus. Fusce sodales est vel libero efficitur, id ultricies nisl pharetra. Suspendisse orci dui, placerat nec sapien ut, aliquet venenatis diam. Cras at leo ante. Fusce ut orci nisl. Nulla vehicula eget tortor sit amet interdum. Ut sagittis tellus risus, et convallis est gravida vitae. Donec fringilla lorem et arcu feugiat mattis.",
                "Vestibulum euismod mauris eget velit iaculis, vel aliquam ex accumsan. Donec ante urna, bibendum mollis ipsum vitae, luctus pulvinar neque. In ullamcorper leo id volutpat suscipit. Morbi ex mauris, commodo at leo quis, ultricies fermentum magna. Sed odio justo, pharetra a malesuada eget, ullamcorper eu lorem. Suspendisse lacinia augue neque, at fringilla ipsum imperdiet nec. Nulla sapien orci, faucibus non iaculis vel, porta vitae dui. Aenean at imperdiet mauris.",
            };

            // Add more text.
            foreach (string paragraph in paragraphs)
            {
                para.Range.Text = paragraph;
                para.Range.InsertParagraphAfter();
            }

            // Find the beginning of the document.
            // For other pre-defined bookmarks, see:
            //      http://support.microsoft.com/kb/212555
            object start_of_doc = "\\startofdoc";

            // Get a Range at the start of the document.
            Word.Range start_range = word_doc.Bookmarks.get_Item(ref start_of_doc).Range;

            // Add the picture to the Range's InlineShapes.
            string picture_file = pic_filename;
            Word.InlineShape inline_shape = start_range.InlineShapes.AddPicture(
                picture_file, ref missing, ref missing, ref missing);

            // Format the picture.
            Word.Shape shape = inline_shape.ConvertToShape();

            // Scale uniformly by 50%.
            shape.LockAspectRatio = Core.MsoTriState.msoTrue;
            shape.ScaleHeight(0.5f, Core.MsoTriState.msoTrue,
                Core.MsoScaleFrom.msoScaleFromTopLeft);

            // Wrap text around the picture's square.
            shape.WrapFormat.Type = Word.WdWrapType.wdWrapSquare;

            // Align the picture on the upper right.
            shape.Left = (float)Word.WdShapePosition.wdShapeRight;
            shape.Top = (float)Word.WdShapePosition.wdShapeTop;

            // Save the document.
            object filename = "tmp_word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";

            word_doc.SaveAs(ref filename, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing);

            // Close.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "建立Word檔案完成\t檔名 : " + filename + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //製作一個docx檔案 使用表格

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
            string filename = "tmp_word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".docx";

            object filename_obj = filename;
            word_doc.SaveAs(ref filename_obj, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing);

            // Close down Word.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "製作一個docx檔案 使用表格 完成\t檔名 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //讀取WORD檔案並將顯示純文字部分
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\bmp_format.docx";

            richTextBox1.Text += "讀取檔案 : " + filename + " ...\n";
            string txt = GrabWordFileWords(filename);
            richTextBox1.Text += txt + "\n";
            richTextBox1.Text += "完成\n";
        }

        // Read the text contents of a Word file.
        private string GrabWordFileWords(string file_name)
        {
            // Get the Word application object.
            Word._Application word_app = new Word.ApplicationClass();

            // Make Word visible (optional).
            word_app.Visible = false;

            // Open the file.
            object filename = file_name;
            object confirm_conversions = false;
            object read_only = true;
            object add_to_recent_files = false;
            object format = 0;
            object missing = System.Reflection.Missing.Value;

            Word._Document word_doc =
                word_app.Documents.Open(ref filename, ref confirm_conversions,
                    ref read_only, ref add_to_recent_files,
                    ref missing, ref missing, ref missing, ref missing,
                    ref missing, ref format, ref missing, ref missing,
                    ref missing, ref missing, ref missing, ref missing);

            // Return the document's text.
            string result = word_doc.Content.Text;

            //richTextBox1.Text += result + "\n";

            // Close the document without prompting.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            // Return the result.
            return result;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //移除WORD檔裡面的超連結

            string doc_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_ReadWrite_WORD7.docx";

            richTextBox1.Text += "開啟檔案 : " + doc_filename + "\n";

            Refresh();

            // Get the Word application object.
            Word._Application word_app = new Word.Application();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Open the Word document.
            object missing = Type.Missing;
            object filename = doc_filename;
            object confirm_conversions = false;
            object read_only = false;
            object add_to_recent_files = false;
            object format = 0;
            Word._Document word_doc =
                word_app.Documents.Open(ref filename, ref confirm_conversions,
                    ref read_only, ref add_to_recent_files,
                    ref missing, ref missing, ref missing, ref missing,
                    ref missing, ref format, ref missing, ref missing,
                    ref missing, ref missing, ref missing, ref missing);

            // Remove the hyperlinks.
            object index = 1;
            while (word_doc.Hyperlinks.Count > 0)
            {
                word_doc.Hyperlinks.get_Item(ref index).Delete();
            }

            // Save and close the document without prompting.
            object save_changes = true;
            word_doc.Close(ref save_changes, ref missing, ref missing);

            // Close the word application.
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "完成\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //生成Word文檔

            CreateDocument();
        }

        //Create document method  
        private void CreateDocument()
        {
            //Create an instance for word app  
            Microsoft.Office.Interop.Word.Application winword = new Microsoft.Office.Interop.Word.Application();

            //Set animation status for word application  
            //winword.ShowAnimation = false;

            //Set status for word application is to be visible or not.  
            winword.Visible = false;

            //Create a missing variable for missing value  
            object missing = System.Reflection.Missing.Value;

            //Create a new document  
            Microsoft.Office.Interop.Word.Document document = winword.Documents.Add(ref missing, ref missing, ref missing, ref missing);

            //頁邊距
            document.PageSetup.LeftMargin = 40; //1.41CM
            document.PageSetup.RightMargin = 40;
            document.PageSetup.TopMargin = 40;
            document.PageSetup.BottomMargin = 40;

            //頁眉 //Add header into the document
            foreach (Microsoft.Office.Interop.Word.Section section in document.Sections)
            {
                //Get the header range and add the header details.
                Microsoft.Office.Interop.Word.Range headerRange = section.Headers[Microsoft.Office.Interop.Word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range;
                headerRange.Fields.Add(headerRange, Microsoft.Office.Interop.Word.WdFieldType.wdFieldPage);
                headerRange.ParagraphFormat.Alignment = Microsoft.Office.Interop.Word.WdParagraphAlignment.wdAlignParagraphCenter;
                headerRange.Font.ColorIndex = Microsoft.Office.Interop.Word.WdColorIndex.wdBlue;
                headerRange.Font.Size = 10;
                headerRange.Text = "Header text goes here";
            }

            //頁腳 Add the footers into the document
            foreach (Microsoft.Office.Interop.Word.Section wordSection in document.Sections)
            {
                //Get the footer range and add the footer details.  
                Microsoft.Office.Interop.Word.Range footerRange = wordSection.Footers[Microsoft.Office.Interop.Word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range;
                footerRange.Font.ColorIndex = Microsoft.Office.Interop.Word.WdColorIndex.wdDarkRed;
                footerRange.Font.Size = 10;
                footerRange.ParagraphFormat.Alignment = Microsoft.Office.Interop.Word.WdParagraphAlignment.wdAlignParagraphCenter;
                footerRange.Text = "Footer text goes here";
            }

            //添加內容 adding text to document
            document.Content.SetRange(0, 0);
            document.Content.Text = "檢測報告 " + Environment.NewLine;

            //添加段落 Add paragraph with Heading 1 style
            Microsoft.Office.Interop.Word.Paragraph para1 = document.Content.Paragraphs.Add(ref missing);
            para1.Range.Text = "Para 1 text";
            para1.Range.InsertParagraphAfter();

            //Add paragraph with Heading 2 style  
            Microsoft.Office.Interop.Word.Paragraph para2 = document.Content.Paragraphs.Add(ref missing);
            para2.Range.Text = "Para 2 text";
            para2.Range.InsertParagraphAfter();

            //表格 Create a 5X5 table and insert some dummy record
            Table firstTable = document.Tables.Add(para1.Range, 5, 5, ref missing, ref missing);

            firstTable.Borders.Enable = 1;
            foreach (Row row in firstTable.Rows)
            {
                foreach (Cell cell in row.Cells)
                {
                    //表頭 Header row
                    if (cell.RowIndex == 1)
                    {
                        cell.Range.Text = "Column " + cell.ColumnIndex.ToString();
                        cell.Range.Font.Bold = 1;
                        //other format properties goes here  
                        cell.Range.Font.Name = "verdana";
                        cell.Range.Font.Size = 10;
                        //cell.Range.Font.ColorIndex = WdColorIndex.wdGray25;                              
                        cell.Shading.BackgroundPatternColor = WdColor.wdColorGray25;
                        //Center alignment for the Header cells  
                        cell.VerticalAlignment = WdCellVerticalAlignment.wdCellAlignVerticalCenter;
                        cell.Range.ParagraphFormat.Alignment = WdParagraphAlignment.wdAlignParagraphCenter;
                    }
                    //行 Data row
                    else
                    {
                        cell.Range.Text = (cell.RowIndex - 2 + cell.ColumnIndex).ToString();
                    }
                }

                try
                {
                    //保存
                    string filename = System.Windows.Forms.Application.StartupPath + "\\docx_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".docx";

                    document.SaveAs(filename);
                    document.Close(ref missing, ref missing, ref missing);
                    document = null;

                    winword.Quit(ref missing, ref missing, ref missing);
                    winword = null;
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立一個Word檔案
            // Make a Word document.
            // Get the Word application object.
            Word._Application word_app = new Word.ApplicationClass();

            // Make Word visible (optional).
            word_app.Visible = true;

            // Create the Word document.
            object missing = Type.Missing;
            Word._Document word_doc = word_app.Documents.Add(ref missing, ref missing,
                ref missing, ref missing);

            // Create a header paragraph.
            Word.Paragraph para = word_doc.Paragraphs.Add(ref missing);
            para.Range.Text = "Chrysanthemum Curve";
            object style_name = "Heading 1";
            //para.Range.set_Style(ref style_name);
            para.Range.InsertParagraphAfter();

            // Add more text.
            para.Range.Text = "To make a chrysanthemum curve, use the following " +
                "parametric equations as t goes from 0 to 21 * π to generate " +
                "points and then connect them.";
            para.Range.InsertParagraphAfter();

            // Save the current font and start using Courier New.
            string old_font = para.Range.Font.Name;
            para.Range.Font.Name = "Courier New";

            // Add the equations.
            para.Range.Text =
                "  r = 5 * (1 + Sin(11 * t / 5)) -\n" +
                "      4 * Sin(17 * t / 3) ^ 4 *\n" +
                "      Sin(2 * Cos(3 * t) - 28 * t) ^ 8\n" +
                "  x = r * Cos(t)\n" +
                "  y = r * Sin(t)";

            // Start a new paragraph and then switch back to the original font.
            para.Range.InsertParagraphAfter();
            para.Range.Font.Name = old_font;

            // Save the document.
            //object filename = Application.StartupPath + "\\word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";
            object filename = "tmp_word_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";

            word_doc.SaveAs(ref filename, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing, ref missing, ref missing, ref missing,
                ref missing, ref missing);

            // Close.
            object save_changes = false;
            word_doc.Close(ref save_changes, ref missing, ref missing);
            word_app.Quit(ref save_changes, ref missing, ref missing);

            richTextBox1.Text += "建立Word檔案完成, 檔名 : " + filename + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }
}

