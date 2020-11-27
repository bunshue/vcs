using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
using System.Drawing.Printing;  //for PrinterSettings
using System.Globalization;     //for CultureInfo

namespace vcs_test_all_07_Printer
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        string use_printer = string.Empty;
        private void button0_Click(object sender, EventArgs e)
        {
            // Find all of the installed printers.
            foreach (string printer in PrinterSettings.InstalledPrinters)
            {
                richTextBox1.Text += "找到印表機 :\t" + printer + "\n";
            }

            // Find and select the default printer.
            try
            {
                PrinterSettings settings = new PrinterSettings();
                richTextBox1.Text += "\n預設印表機 :\t" + settings.PrinterName + "\n\n";
                use_printer = settings.PrinterName;
            }
            catch
            {
            }

            // 使用PDF印表機
            foreach (string printer in PrinterSettings.InstalledPrinters)
            {
                if (printer.Contains("PDF"))
                {
                    richTextBox1.Text += "使用PDF印表機\t" + printer + "\n";
                    use_printer = printer;


                    // Display the available resolutions.
                    foreach (PrinterResolution resolution in printDocument1.DefaultPageSettings.PrinterSettings.PrinterResolutions)
                    {
                        //cboResolution.Items.Add(resolution.ToString());
                        richTextBox1.Text += "支援的解析度\t" + resolution.ToString() + "\n";
                    }

                    //設定解析度
                    printDocument1.DefaultPageSettings.PrinterResolution = printDocument1.DefaultPageSettings.PrinterSettings.PrinterResolutions[0];
                }
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //預覽列印
            //加入PrintDocument 和 PrintPreviewDialog
            //printPreviewDialog1屬性之Document選printDocument1
            //編輯 printDocument1_PrintPage

            //無印表機也可以預覽列印

            printPreviewDialog1.ShowDialog();

        }







        /*  fewer
        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
        {
            using (Font font = new Font("Times New Roman", 30))
            {
                e.Graphics.DrawString("Sample text", font, Brushes.Black,
                    e.MarginBounds.Left, e.MarginBounds.Top);
            }
            e.HasMorePages = false;
        }
        */

        /*
        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
        {
            const float font_size = 12;
            const float dy = font_size * 1.5f;
            float x0 = e.MarginBounds.Left + 0.5f * 100;
            float x1 = x0 + 0.75f * 100;
            float y = e.MarginBounds.Top;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            using (Font font = new Font("Times New Roman", font_size))
            {
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;

                    e.Graphics.DrawString("Celsius", font, Brushes.Blue, x0, y, sf);
                    e.Graphics.DrawString("Fahrenheit", font, Brushes.Blue, x1, y, sf);
                    y += dy;

                    for (int celsius = 60; celsius <= 250; celsius += 5)
                    {
                        float fahrenheit = celsius * 9f / 5f + 32;
                        e.Graphics.DrawString(celsius.ToString(),
                            font, Brushes.Black, x0, y, sf);
                        e.Graphics.DrawString(fahrenheit.ToString("0"),
                            font, Brushes.Black, x1, y, sf);
                        y += dy;
                    }

                    y = e.MarginBounds.Top;
                    float x2 = x1 + 1.2f * 100;
                    float x3 = x2 + 0.75f * 100;
                    e.Graphics.DrawString("Fahrenheit", font, Brushes.Blue, x2, y, sf);
                    e.Graphics.DrawString("Celsius", font, Brushes.Blue, x3, y, sf);
                    y += dy;

                    for (int fahrenheit = 140; fahrenheit <= 500; fahrenheit += 10)
                    {
                        float celsius = (fahrenheit - 32) * 5f / 9f;
                        e.Graphics.DrawString(fahrenheit.ToString(),
                            font, Brushes.Black, x2, y, sf);
                        e.Graphics.DrawString(celsius.ToString("0"),
                            font, Brushes.Black, x3, y, sf);
                        y += dy;
                    }
                }
            }

        }
        */

        //列印一個純文字檔
        // Print a page of the text file.
        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
        {
            richTextBox1.Text += "列印一個純文字檔\n";
            // The text contained in the file.
            string FileContents;
            string filename = @"C:\\______test_files\\article.txt";

            // Read the file's contents.
            try
            {
                FileContents = File.ReadAllText(filename).Trim();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error reading file " + filename + ".\n" + ex.Message);
                return;
            }

            // Make a font for printing.
            using (Font font = new Font("Courier New", 10))
            {
                // Make a StringFormat to align text normally.
                using (StringFormat string_format = new StringFormat())
                {
                    // See how much of the remaining text will fit.
                    SizeF layout_area = new SizeF(
                        e.MarginBounds.Width, e.MarginBounds.Height);
                    int chars_fitted, lines_filled;
                    e.Graphics.MeasureString(FileContents, font,
                        layout_area, string_format,
                        out chars_fitted, out lines_filled);

                    // Print as much as will fit.
                    e.Graphics.DrawString(
                        FileContents.Substring(0, chars_fitted),
                        font, Brushes.Black, e.MarginBounds,
                        string_format);

                    // Remove the printed text from the string.
                    FileContents = FileContents.Substring(chars_fitted).Trim();
                }
            }

            // See if we are done.
            e.HasMorePages = FileContents.Length > 0;
        }



        private void button2_Click(object sender, EventArgs e)
        {
            button0_Click(sender, e);


            // Select the printer.
            printDocument1.PrinterSettings.PrinterName = use_printer;

            // Set the print document name.
            printDocument1.DocumentName = "印表機處理器看到的文件名稱";

            // Print.
            printDocument1.Print();

        }

        // Display the print preview dialog.
        private void button3_Click(object sender, EventArgs e)
        {
            printPreviewDialog_image.ShowDialog();
        }

        // Print an image.
        private void printDocument_image_PrintPage(object sender, PrintPageEventArgs e)
        {
            // Print in the upper left corner at its full size.
            e.Graphics.DrawImage(pictureBox1.Image, e.MarginBounds.X, e.MarginBounds.Y, pictureBox1.Image.Width, pictureBox1.Image.Height);

            // Print in the upper right corner,
            // sized to fit beside the other image.
            int left = e.MarginBounds.Left + pictureBox1.Image.Width;
            int width = e.MarginBounds.Width - pictureBox1.Image.Width;
            float scale = width / (float)pictureBox1.Image.Width;
            int height = (int)(pictureBox1.Image.Height * scale);
            e.Graphics.DrawImage(pictureBox1.Image, left, e.MarginBounds.Y, width, height);

            // Print the same size in the lower right corner.
            int top = e.MarginBounds.Bottom - height;
            e.Graphics.DrawImage(pictureBox1.Image, left, top, width, height);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            button0_Click(sender, e);

            // Select the printer.
            printDocument_draw.PrinterSettings.PrinterName = use_printer;

            // Set the print document name.
            printDocument_draw.DocumentName = "印表機處理器看到的文件名稱";

            // Print.
            printDocument_draw.Print();
        }


        // The calendar data.
        DateTime FirstOfMonth;
        private string[] CalendarData;

        // Display a print preview of the calendar.
        private void button5_Click(object sender, EventArgs e)
        {
            // Get the selected month and year.
            int year_num = 2020;
            int month_num = 11;

            richTextBox1.Text += "year = " + year_num.ToString() + "\n";
            richTextBox1.Text += "month = " + month_num.ToString() + "\n";


            DateTime first_of_month = new DateTime(year_num, month_num, 1);

            // See how many days are in the selected month.
            int num_days = DateTime.DaysInMonth(year_num, month_num);

            // Generate some "random" data for the indicated month.
            CalendarData = MakeData(num_days);

            // Save the first date of the selected month.
            FirstOfMonth = first_of_month;

            // Display the print preview of the calendar.
            printPreviewDialog_Calendar.ShowDialog();




        }


        // Generate some "random" data for
        // the indicated number of days.
        private string[] MakeData(int num_days)
        {
            string words = "lorem ipsum dolor sit amet consectetur adipiscing elit integer pulvinar diam ante quis cursus felis dignissim quis nullam non tristique sapien vitae dignissim mauris etiam et risus et purus efficitur dignissim nec ultricies eros aenean consequat scelerisque enim ut congue mi pulvinar dictum aliquam erat volutpat praesent vitae lobortis nisi aliquam ornare varius eros id feugiat in id orci interdum egestas tellus nec pharetra quam ";
            words += "vivamus lacus risus accumsan volutpat vestibulum id tempor vitae dolor fusce vehicula ligula at justo hendrerit et cursus nisl efficitur vestibulum sed ipsum vel ligula lacinia fringilla quis nec justo proin mattis faucibus dictum sed porttitor egestas porttitor ut erat magna tempus vel luctus a scelerisque id lacus class aptent taciti sociosqu ad litora torquent per conubia nostra per inceptos himenaeos ut enim odio tincidunt fringilla sollicitudin sit amet ultricies et orci ";
            words += "fusce ac interdum nibh a accumsan velit sed sagittis lacinia velit et rutrum diam ornare vel aenean porta molestie dolor praesent rhoncus quam sed felis tempor a elementum lacus congue phasellus fringilla metus et lorem semper rutrum phasellus volutpat posuere magna et rutrum maecenas vel aliquam massa morbi suscipit mi a tincidunt viverra nibh libero tristique orci at mattis erat augue mollis purus cras magna justo pulvinar nec dignissim eu malesuada sed enim donec ac posuere nisi mauris vitae mauris et arcu placerat sollicitudin nec quis dolor ";
            words += "integer vitae vestibulum nibh nunc sit amet eros ante nunc a dui ornare tristique ex id auctor enim mauris maximus ac felis vitae dignissim donec ex lorem mattis sit amet venenatis id laoreet vel neque donec sollicitudin orci varius ipsum sodales at maximus est suscipit donec id nulla porta sodales mauris eu auctor arcu nullam posuere tortor eget mauris suscipit bibendum maecenas sollicitudin faucibus libero ac facilisis erat lacinia vel aliquam erat volutpat maecenas pellentesque ultricies felis nec scelerisque turpis convallis fringilla ut venenatis et sapien ac vulputate ";
            words += "praesent feugiat rhoncus tellus sit amet pretium dolor mattis non cras blandit neque nulla ullamcorper dictum tellus semper tempus curabitur porttitor luctus urna vel venenatis tortor volutpat non phasellus magna odio sollicitudin at tincidunt a convallis quis velit nam sit amet aliquam mauris ut quis pretium odio nec pretium mi vestibulum congue diam nibh vitae rhoncus purus vestibulum ut vestibulum aliquam hendrerit quam quis commodo est fermentum ut lorem ipsum dolor sit amet consectetur adipiscing elit proin quis turpis fringilla pharetra ipsum eu tincidunt ex aliquam erat volutpat pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas aenean at tellus in justo iaculis pretium vitae sit amet massa suspendisse potenti sed sit amet pellentesque ligula aliquam ipsum nulla iaculis id fermentum sed gravida quis elit ";
            words += "duis leo augue tristique non finibus sit amet malesuada et ante proin nul";
            words += "la est commodo in massa vel euismod aliquam lectus curabitur facilisis cursus neque quis lacinia maecenas vel ullamcorper ligula suspendisse mollis arcu in luctus malesuada quam ex accumsan nulla id feugiat neque sapien in massa mauris porta faucibus augue mollis tincidunt eros porttitor non phasellus ut bibendum";

            Random rand = new Random();
            string[] result = new string[num_days];
            for (int i = 0; i < num_days; i++)
            {
                int length = rand.Next(3, 15);
                result[i] = TakeWords(ref words, length);
            }

            return result;
        }

        // Take the indicated number of words from the string.
        private string TakeWords(ref string source, int num_words)
        {
            string result = "";
            for (int word = 0; word < num_words; word++)
            {
                int space_pos = source.IndexOf(' ');
                result += source.Substring(0, space_pos + 1);
                source = source.Substring(space_pos + 1);
            }
            return result.Trim();
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

        // Draw the smiley face.
        private void printDocument_draw_PrintPage(object sender, PrintPageEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            e.Graphics.TranslateTransform(1, 1);
            e.Graphics.ScaleTransform(100, 100,
                System.Drawing.Drawing2D.MatrixOrder.Append);
            e.Graphics.TranslateTransform(
                e.MarginBounds.X,
                e.MarginBounds.Y,
                System.Drawing.Drawing2D.MatrixOrder.Append);
            DrawSmiley(e.Graphics);
        }

        // Draw a smiley face in the area (-1, -1)-(1, 1).
        private void DrawSmiley(Graphics gr)
        {
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                gr.FillEllipse(Brushes.Yellow, -1, -1, 2, 2);
                gr.DrawEllipse(thin_pen, -1, -1, 2, 2);

                gr.FillEllipse(Brushes.LightGreen, -0.5F, -0.5F, 0.3F, 0.5F);
                gr.DrawEllipse(thin_pen, -0.5F, -0.5F, 0.3F, 0.5F);
                gr.FillEllipse(Brushes.Black, -0.4F, -0.4F, 0.2F, 0.3F);

                gr.FillEllipse(Brushes.LightGreen, 0.2F, -0.5F, 0.3F, 0.5F);
                gr.DrawEllipse(thin_pen, 0.2F, -0.5F, 0.3F, 0.5F);
                gr.FillEllipse(Brushes.Black, 0.3F, -0.4F, 0.2F, 0.3F);

                gr.FillEllipse(Brushes.LightBlue, -0.2F, -0.1F, 0.4F, 0.6F);
                gr.DrawEllipse(thin_pen, -0.2F, -0.1F, 0.4F, 0.6F);

                gr.DrawArc(thin_pen, -0.75F, -0.75F, 1.5F, 1.5F, 20, 120);
            }
        }

        // Draw the calendar.
        private void printDocument_Calendar_PrintPage(object sender, PrintPageEventArgs e)
        {
            DrawCalendar(e.Graphics, e.MarginBounds, FirstOfMonth, CalendarData);
        }

        // Print in landscape mode.
        private void printDocument_Calendar_QueryPageSettings(object sender, QueryPageSettingsEventArgs e)
        {
            e.PageSettings.Landscape = true;
        }

        // Draw the calendar as big as posisble.
        private void DrawCalendar(Graphics gr, RectangleF bounds, DateTime first_of_month, string[] date_data)
        {
            // Make the rows and columns as big as possible.
            float col_wid = bounds.Width / 7f;

            // See how many weeks we will need.
            int num_rows = NumberOfWeekRows(first_of_month);

            // Add an extra row for the month and year at the top.
            num_rows++;

            // Calculate the row height.
            float row_hgt = bounds.Height / (float)num_rows;

            // Draw the month and year.
            float x = bounds.X;
            float y = bounds.Y;
            RectangleF rectf = new RectangleF(x, y, bounds.Width, row_hgt / 2f);
            DrawMonthAndYear(gr, rectf, first_of_month);
            y += row_hgt / 2f;

            // Draw the day names.
            DrawWeekdayNames(gr, x, y, col_wid, row_hgt / 2f);
            y += row_hgt / 2f;

            // Draw the date cells.
            DrawDateData(first_of_month, date_data,
                gr, x, y, col_wid, row_hgt);

            // Outline the calendar.
            gr.DrawRectangle(Pens.Black,
                bounds.X, bounds.Y, bounds.Width, bounds.Height);
        }

        // Return the number of week rows needed by this month.
        private int NumberOfWeekRows(DateTime first_of_month)
        {
            // Get the number of days in the month.
            int num_days = DateTime.DaysInMonth(
                first_of_month.Year, first_of_month.Month);

            // Add the column number for the first day of the month.
            num_days += DateColumn(first_of_month);

            // Divide by 7 and round up.
            return (int)Math.Ceiling(num_days / 7f);
        }

        // Return the column number for this date in the current locale.
        private int DateColumn(DateTime date)
        {
            int col =
                (int)date.DayOfWeek -
                (int)CultureInfo.CurrentCulture.DateTimeFormat.FirstDayOfWeek;
            if (col < 0) col += 7;
            return col;
        }

        // Draw the month and year.
        private void DrawMonthAndYear(Graphics gr, RectangleF rectf, DateTime date)
        {
            using (StringFormat sf = new StringFormat())
            {
                // Center the text.
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;

                string[] month_names =
                    CultureInfo.CurrentCulture.DateTimeFormat.MonthNames;
                string title = month_names[date.Month - 1] +
                    " " + date.Year.ToString();

                // Find the biggest font that will fit.
                int font_size = FindFontSize(gr, rectf, "Times New Roman", title);

                // Draw the text.
                gr.FillRectangle(Brushes.LightBlue, rectf);
                using (Font font = new Font("Times New Roman", font_size))
                {
                    gr.DrawString(title, font, Brushes.Blue, rectf, sf);
                }
            }
        }

        // Draw the weekday names.
        private void DrawWeekdayNames(Graphics gr, float x, float y, float col_wid, float hgt)
        {
            // Find the widest day name.
            float max_wid = 0;
            string[] day_names =
                CultureInfo.CurrentCulture.DateTimeFormat.DayNames;
            string widest_name = day_names[0];
            using (Font font = new Font("Times New Roman", 10))
            {
                foreach (string name in day_names)
                {
                    SizeF size = gr.MeasureString(name, font);
                    if (max_wid < size.Width)
                    {
                        max_wid = size.Width;
                        widest_name = name;
                    }
                }
            }

            // Find the biggest font size that will fit.
            RectangleF rectf = new RectangleF(x, y, col_wid, hgt);
            int font_size = FindFontSize(gr, rectf, "Times New Roman", widest_name);

            // Draw the day names.
            using (Font font = new Font("Times New Roman", font_size))
            {
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;
                    sf.LineAlignment = StringAlignment.Center;

                    int index = (int)CultureInfo.CurrentCulture.DateTimeFormat.FirstDayOfWeek;
                    for (int i = 0; i < 7; i++)
                    {
                        gr.FillRectangle(Brushes.LightBlue, rectf);
                        gr.DrawString(day_names[index], font, Brushes.Blue, rectf, sf);
                        index = (index + 1) % 7;
                        rectf.X += col_wid;
                    }
                }
            }
        }

        // Draw the data for each date.
        private void DrawDateData(DateTime first_of_month, string[] date_data,
            Graphics gr, float x, float y, float col_wid, float row_hgt)
        {
            // Let date numbers occupy the upper quarter
            // and left third of the date box.
            RectangleF date_rectf =
                new RectangleF(x, y, col_wid / 3f, row_hgt / 4f);

            // The date data goes below the date rectangle.
            RectangleF data_rectf =
                new RectangleF(x, y, col_wid, row_hgt * 0.75f);

            // See how big we can make the font.
            int font_size = FindFontSize(gr, date_rectf, "Times New Roman", "30");

            // Get the column number for the first day of the month.
            int col = DateColumn(first_of_month);

            // Draw the dates.
            using (Font number_font = new Font("Times New Roman", font_size))
            {
                using (Font data_font = new Font("Times New Roman", font_size * 0.75f))
                {
                    using (StringFormat ul_sf = new StringFormat())
                    {
                        ul_sf.Alignment = StringAlignment.Near;
                        ul_sf.LineAlignment = StringAlignment.Near;
                        ul_sf.Trimming = StringTrimming.EllipsisWord;
                        ul_sf.FormatFlags = StringFormatFlags.LineLimit;

                        int num_days = DateTime.DaysInMonth(
                            first_of_month.Year, first_of_month.Month);
                        for (int day_num = 0; day_num < num_days; day_num++)
                        {
                            // Outline the cell.
                            RectangleF cell_rectf = new RectangleF(
                                x + col * col_wid, y, col_wid, row_hgt);
                            gr.DrawRectangle(Pens.Black,
                                cell_rectf.X, cell_rectf.Y,
                                cell_rectf.Width, cell_rectf.Height);

                            // Draw the date.
                            date_rectf.X = cell_rectf.X;
                            date_rectf.Y = cell_rectf.Y;
                            gr.DrawString((day_num + 1).ToString(),
                                number_font, Brushes.Blue, date_rectf, ul_sf);

                            // Draw the data.
                            data_rectf.X = x + col * col_wid;
                            data_rectf.Y = y + row_hgt * 0.25f;
                            gr.DrawString(date_data[day_num],
                                data_font, Brushes.Black, data_rectf, ul_sf);

                            // Move to the next cell.
                            col = (col + 1) % 7;
                            if (col == 0) y += row_hgt;
                        }
                    }
                }
            }
        }

        // Find the largest integer font size that will fit in the given space.
        private int FindFontSize(Graphics gr, RectangleF rectf, string font_name, string text)
        {
            for (int font_size = 5; ; font_size++)
            {
                using (Font font = new Font(font_name, font_size))
                {
                    SizeF text_size = gr.MeasureString(text, font);
                    if ((text_size.Width > rectf.Width) ||
                        (text_size.Height > rectf.Height))
                        return font_size - 1;
                }
            }
        }



    }
}
