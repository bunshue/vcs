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
using System.Drawing.Drawing2D; //for SmoothingMode

using System.Management;        //參考/加入參考/.NET/System Management

namespace vcs_test_all_05_Print
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

            //列出印表機資訊
            // List the installed printers.
            // Find all of the installed printers.
            foreach (string printer in PrinterSettings.InstalledPrinters)
            {
                cboPrinters.Items.Add(printer);
            }

            // Select the first printer.
            cboPrinters.SelectedIndex = 0;
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
            dx = 200;
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

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            groupBox_control.Location = new Point(x_st + dx * 0, y_st + dy * 13);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            printPreviewControl1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_print.Location = new Point(x_st + dx * 5, y_st + dy * 2 + 30);
            groupBox3.Location = new Point(x_st + dx * 5, y_st + dy * 3+50);

            richTextBox1.Size = new Size(240, 400);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 8);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1280, 910);
            this.Text = "vcs_test_all_05_Print";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";

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



        private const int HeaderMargin = 5;
        private const int ColMargin = 5;
        private const int RowMargin = 30;
        // Display the print preview.
        private void button6_Click(object sender, EventArgs e)
        {
            printPreviewDialog_grid.ClientSize = new Size(500, 600);
            printPreviewDialog_grid.ShowDialog();
        }

        // Draw the grid.
        private void printDocument_grid_PrintPage(object sender, PrintPageEventArgs e)
        {
            // Make some sample data.
            string[] headers;
            object[][] values;
            MakeSampleData(out headers, out values);

            // See how wide the columns need to be.
            using (Font header_font =
                new Font("Times New Roman", 18, FontStyle.Bold))
            {
                using (Font body_font =
                    new Font("Times New Roman", 18, FontStyle.Regular))
                {
                    int[] col_wid = FindColumnSizes(e.Graphics, header_font, body_font, headers, values);

                    // Define the column alignments.
                    StringAlignment[] alignments = FindColumnAlignments(values);

                    // Get the total width.
                    int grid_wid = 0;
                    for (int i = 0; i < col_wid.Length; i++)
                    {
                        grid_wid += col_wid[i] + 2 * ColMargin;
                    }

                    // Print the data.
                    Rectangle grid_bounds = new Rectangle(
                        e.MarginBounds.Left, e.MarginBounds.Top, grid_wid, e.MarginBounds.Bottom);
                    PrintGrid(grid_bounds, e.Graphics, col_wid, alignments,
                        header_font, body_font, headers, values);
                }
            }
        }

        // Make some sample data.
        private void MakeSampleData(out string[] headers, out object[][] values)
        {
            headers = new string[] { "Fruit", "Vegetable", "Price" };
            values = new object[][] {
                new object[] {"Apple", "Artichoke", 12.45M},
                new object[] {"Banana", "Bean", 19.95M},
                new object[] {"Cherry", "Corn", 1.23M},
                new object[] {"Date", "Donut", 0.45M},
                new object[] {"Egg", "Eclair", 19.95M},
                new object[] {"Fig", "Fruit cup", 1.23M}
            };
        }

        // Calculate column sizes.
        private int[] FindColumnSizes(Graphics gr, Font header_font, Font body_font, string[] headers, object[][] values)
        {
            int num_rows = values.Length;
            int num_cols = values[0].Length;

            // Check the header widths.
            int[] col_wid = new int[num_cols];
            CheckColWidths(col_wid, gr, header_font, headers);

            // Check the data widths.
            foreach (object[] row in values)
            {
                CheckColWidths(col_wid, gr, body_font, row);
            }

            // Add a margin.
            for (int i = 0; i < num_cols; i++)
            {
                col_wid[i] += 20;
            }

            // Return the result.
            return col_wid;
        }

        // Update the column widths for the values in this array.
        private void CheckColWidths(int[] col_wid, Graphics gr, Font the_font, object[] values)
        {
            for (int i = 0; i < values.Length; i++)
            {
                SizeF txt_size = gr.MeasureString(values[i].ToString(), the_font);
                if (col_wid[i] < txt_size.Width) col_wid[i] = (int)txt_size.Width;
            }
        }

        // Define the column alignments.
        private StringAlignment[] FindColumnAlignments(object[][] values)
        {
            StringAlignment[] alignments = new StringAlignment[values.Length];
            for (int i = 0; i < values[0].Length; i++)
            {
                if (values[0][i].GetType() == typeof(int) ||
                    values[0][i].GetType() == typeof(float) ||
                    values[0][i].GetType() == typeof(double) ||
                    values[0][i].GetType() == typeof(decimal))
                {
                    alignments[i] = StringAlignment.Far;
                }
                else
                {
                    alignments[i] = StringAlignment.Near;
                }
            }

            return alignments;
        }

        // Print the grid.
        private void PrintGrid(Rectangle grid_bounds, Graphics gr,
            int[] col_wid, StringAlignment[] alignments,
            Font header_font, Font body_font, string[] headers, object[][] values)
        {
            // Print the headers.
            int x = grid_bounds.Left;
            int y = grid_bounds.Top;

            // Fill the header's background.
            Rectangle bg_rect = new Rectangle(
                x, y, grid_bounds.Width, RowMargin + HeaderMargin);
            gr.FillRectangle(Brushes.Blue, bg_rect);

            // Draw the header text.
            using (StringFormat string_format = new StringFormat())
            {
                for (int i = 0; i < headers.Length; i++)
                {
                    RectangleF layout_rect = new
                        RectangleF(x + ColMargin, y, col_wid[i], RowMargin);
                    string_format.Alignment = alignments[i];
                    string_format.LineAlignment = StringAlignment.Near;
                    gr.DrawString(headers[i],
                        header_font, Brushes.White,
                        layout_rect, string_format);
                    x += col_wid[i] + 2 * ColMargin;
                }
            }
            bg_rect.Height -= HeaderMargin;
            y += HeaderMargin;

            // Print the values.
            int max_x = x;
            for (int r = 0; r < values.Length; r++)
            {
                x = grid_bounds.Left;
                y += RowMargin;

                // Fill the row's background.
                bg_rect.Y = y;
                if (r % 2 == 0)
                {
                    gr.FillRectangle(Brushes.LightGreen, bg_rect);
                }
                else
                {
                    gr.FillRectangle(Brushes.LightBlue, bg_rect);
                }

                using (StringFormat string_format = new StringFormat())
                {
                    for (int i = 0; i < values[r].Length; i++)
                    {
                        // Draw the text.
                        RectangleF layout_rect = new
                            RectangleF(x + ColMargin, y, col_wid[i], RowMargin);
                        string_format.Alignment = alignments[i];
                        string_format.LineAlignment = StringAlignment.Near;
                        gr.DrawString(values[r][i].ToString(),
                            body_font, Brushes.Black,
                            layout_rect, string_format);

                        x += col_wid[i] + 2 * ColMargin;
                    }
                }
                gr.DrawLine(Pens.Black, grid_bounds.X, y, max_x, y);
            }

            // Outline the grid.
            grid_bounds = new Rectangle(
                grid_bounds.X, grid_bounds.Y, grid_bounds.Width,
                (values.Length + 1) * RowMargin + HeaderMargin);
            gr.DrawRectangle(Pens.Black, grid_bounds);
        }


        #region 預覽列印 Star

        private void bt_print_star_Click(object sender, EventArgs e)
        {
            //預覽列印 Star
            printPreviewDialog_star.ShowDialog();
        }

        // Draw the star.
        private void printDocument_star_PrintPage(object sender, PrintPageEventArgs e)
        {
            try
            {
                // Convert mm to inches * 100.
                float diameter = float.Parse(txtRadius.Text);
                diameter = diameter / 25.4f * 100f;

                float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
                float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;
                float x = cx - diameter / 2f;
                float y = cy - diameter / 2f;

                RectangleF rect = new RectangleF(x, y, diameter, diameter);

                // Draw the star.
                e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                DrawStar(e.Graphics, Pens.Red, Brushes.Yellow,
                    (int)nudPoints.Value, (int)nudSkip.Value,
                    rect);

                // Draw axes in the middle of the page.
                // DrawAxes(e);

                e.HasMorePages = false;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Draw axes in the middle of the page.
        private void DrawAxes(PrintPageEventArgs e)
        {
            float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
            float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;

            e.Graphics.DrawLine(Pens.Black,
                e.MarginBounds.Left, cy,
                e.MarginBounds.Right, cy);
            e.Graphics.DrawLine(Pens.Black,
                cx, e.MarginBounds.Top,
                cx, e.MarginBounds.Bottom);

            for (float x = cx; x <= e.MarginBounds.Right; x += 100)
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);
            for (float x = cx; x >= e.MarginBounds.Left; x -= 100)
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);

            for (float y = cy; y <= e.MarginBounds.Bottom; y += 100)
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
            for (float y = cy; y >= e.MarginBounds.Top; y -= 100)
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
        }

        // Draw the indicated star in the rectangle.
        private void DrawStar(Graphics gr, Pen the_pen, Brush the_brush, int num_points, int skip, RectangleF rect)
        {
            // Get the star's points.
            PointF[] star_points = MakeStarPoints(-Math.PI / 2, num_points, skip, rect);

            // Draw the star.
            gr.FillPolygon(the_brush, star_points);
            gr.DrawPolygon(the_pen, star_points);
        }

        // Generate the points for a star.
        private PointF[] MakeStarPoints(double start_theta, int num_points, int skip, RectangleF rect)
        {
            double theta, dtheta;
            PointF[] result;
            float rx = rect.Width / 2f;
            float ry = rect.Height / 2f;
            float cx = rect.X + rx;
            float cy = rect.Y + ry;

            // If this is a polygon, don't bother with concave points.
            if (skip == 1)
            {
                result = new PointF[num_points];
                theta = start_theta;
                dtheta = 2 * Math.PI / num_points;
                for (int i = 0; i < num_points; i++)
                {
                    result[i] = new PointF(
                        (float)(cx + rx * Math.Cos(theta)),
                        (float)(cy + ry * Math.Sin(theta)));
                    theta += dtheta;
                }
                return result;
            }

            // Find the radius for the concave vertices.
            double concave_radius = CalculateConcaveRadius(num_points, skip);

            // Make the points.
            result = new PointF[2 * num_points];
            theta = start_theta;
            dtheta = Math.PI / num_points;
            for (int i = 0; i < num_points; i++)
            {
                result[2 * i] = new PointF(
                    (float)(cx + rx * Math.Cos(theta)),
                    (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
                result[2 * i + 1] = new PointF(
                    (float)(cx + rx * Math.Cos(theta) * concave_radius),
                    (float)(cy + ry * Math.Sin(theta) * concave_radius));
                theta += dtheta;
            }
            return result;
        }

        // Calculate the inner star radius.
        private double CalculateConcaveRadius(int num_points, int skip)
        {
            // For really small numbers of points.
            if (num_points < 5) return 0.33f;

            // Calculate angles to key points.
            double dtheta = 2 * Math.PI / num_points;
            double theta00 = -Math.PI / 2;
            double theta01 = theta00 + dtheta * skip;
            double theta10 = theta00 + dtheta;
            double theta11 = theta10 - dtheta * skip;

            // Find the key points.
            PointF pt00 = new PointF(
                (float)Math.Cos(theta00),
                (float)Math.Sin(theta00));
            PointF pt01 = new PointF(
                (float)Math.Cos(theta01),
                (float)Math.Sin(theta01));
            PointF pt10 = new PointF(
                (float)Math.Cos(theta10),
                (float)Math.Sin(theta10));
            PointF pt11 = new PointF(
                (float)Math.Cos(theta11),
                (float)Math.Sin(theta11));

            // See where the segments connecting the points intersect.
            bool lines_intersect, segments_intersect;
            PointF intersection, close_p1, close_p2;
            FindIntersection(pt00, pt01, pt10, pt11,
                out lines_intersect, out segments_intersect,
                out intersection, out close_p1, out close_p2);

            // Calculate the distance between the
            // point of intersection and the center.
            return Math.Sqrt(
                intersection.X * intersection.X +
                intersection.Y * intersection.Y);
        }

        // Find the point of intersection between
        // the lines p1 --> p2 and p3 --> p4.
        private void FindIntersection(
            PointF p1, PointF p2, PointF p3, PointF p4,
            out bool lines_intersect, out bool segments_intersect,
            out PointF intersection,
            out PointF close_p1, out PointF close_p2)
        {
            // Get the segments' parameters.
            float dx12 = p2.X - p1.X;
            float dy12 = p2.Y - p1.Y;
            float dx34 = p4.X - p3.X;
            float dy34 = p4.Y - p3.Y;

            // Solve for t1 and t2
            float denominator = (dy12 * dx34 - dx12 * dy34);

            float t1 =
                ((p1.X - p3.X) * dy34 + (p3.Y - p1.Y) * dx34)
                    / denominator;
            if (float.IsInfinity(t1))
            {
                // The lines are parallel (or close enough to it).
                lines_intersect = false;
                segments_intersect = false;
                intersection = new PointF(float.NaN, float.NaN);
                close_p1 = new PointF(float.NaN, float.NaN);
                close_p2 = new PointF(float.NaN, float.NaN);
                return;
            }
            lines_intersect = true;

            float t2 =
                ((p3.X - p1.X) * dy12 + (p1.Y - p3.Y) * dx12)
                    / -denominator;

            // Find the point of intersection.
            intersection = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);

            // The segments intersect if t1 and t2 are between 0 and 1.
            segments_intersect =
                ((t1 >= 0) && (t1 <= 1) &&
                 (t2 >= 0) && (t2 <= 1));

            // Find the closest points on the segments.
            if (t1 < 0)
            {
                t1 = 0;
            }
            else if (t1 > 1)
            {
                t1 = 1;
            }

            if (t2 < 0)
            {
                t2 = 0;
            }
            else if (t2 > 1)
            {
                t2 = 1;
            }

            close_p1 = new PointF(p1.X + dx12 * t1, p1.Y + dy12 * t1);
            close_p2 = new PointF(p3.X + dx34 * t2, p3.Y + dy34 * t2);
        }


        // Draw the star.
        private void pictureBox_star_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the star.
            DrawStar(e.Graphics, Pens.Red, Brushes.Yellow,
                (int)nudPoints.Value, (int)nudSkip.Value,
                pictureBox_star.ClientRectangle);
        }

        // Redraw the star with the new parameters.
        private void nudPoints_ValueChanged(object sender, EventArgs e)
        {
            nudSkip.Maximum = (int)(((int)nudPoints.Value - 1) / 2.0);
            pictureBox_star.Refresh();
        }

        private void nudSkip_ValueChanged(object sender, EventArgs e)
        {
            pictureBox_star.Refresh();
        }

        #endregion

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

        #region 多頁預覽列印 多頁列印
        // Print the document's pages.
        private int NextPageNum = 0;
        private void printDocument_pages_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            // Draw a shape depending on the page we are printing.
            switch (NextPageNum)
            {
                case 0: // Draw an ellipse.
                    using (Pen the_pen = new Pen(Color.Red, 10))
                    {
                        e.Graphics.DrawEllipse(the_pen, e.MarginBounds);
                    }
                    break;
                case 1: // Draw a triangle.
                    using (Pen the_pen = new Pen(Color.Green, 10))
                    {
                        int xmid = (int)(e.MarginBounds.X + e.MarginBounds.Width / 2);
                        Point[] pts = 
                        {
                            new Point(xmid, e.MarginBounds.Top),
                            new Point(e.MarginBounds.Right, e.MarginBounds.Bottom),
                            new Point(e.MarginBounds.Left, e.MarginBounds.Bottom),
                        };
                        e.Graphics.DrawPolygon(the_pen, pts);
                    }
                    break;
                case 2: // Draw a rectangle.
                    using (Pen the_pen = new Pen(Color.Blue, 10))
                    {
                        e.Graphics.DrawRectangle(the_pen, e.MarginBounds);
                    }
                    break;
                case 3: // Draw a diamond.
                    using (Pen the_pen = new Pen(Color.Orange, 10))
                    {
                        int xmid = (int)(e.MarginBounds.X + e.MarginBounds.Width / 2);
                        int ymid = (int)(e.MarginBounds.Y + e.MarginBounds.Height / 2);
                        Point[] pts = 
                        {
                            new Point(xmid, e.MarginBounds.Top),
                            new Point(e.MarginBounds.Right, ymid),
                            new Point(xmid, e.MarginBounds.Bottom),
                            new Point(e.MarginBounds.Left, ymid),
                        };
                        e.Graphics.DrawPolygon(the_pen, pts);
                    }
                    break;
            }

            // Draw the margins.
            using (Pen dashed_pen = new Pen(Color.Red, 5))
            {
                dashed_pen.DashPattern = new float[] { 10, 10 };
                e.Graphics.DrawRectangle(dashed_pen, e.MarginBounds);
            }

            // Draw the page number centered.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;

                using (Font the_font = new Font("Times New Roman", 200, FontStyle.Bold))
                {
                    using (Brush the_brush = new SolidBrush(Color.Black))
                    {
                        e.Graphics.DrawString(String.Format("{0}", NextPageNum + 1),
                            the_font, the_brush, e.MarginBounds, sf);
                    }
                }
            }

            // Next time print the next page.
            NextPageNum += 1;

            // We have more pages if we have not yet printed page 3.
            e.HasMorePages = (NextPageNum <= 3);

            // If we have no more pages, reset for the next time we print.
            if (NextPageNum > 3) NextPageNum = 0;
        }

        // Get ready to print.
        private void printDocument_pages_BeginPrint(object sender, PrintEventArgs e)
        {
            // Start with page 0.
            NextPageNum = 0;
        }

        // Prepare to print the next page.
        private void printDocument_pages_QueryPageSettings(object sender, QueryPageSettingsEventArgs e)
        {
            const int GUTTER = 100;
            // Even numbered pages have a big margin on the left.
            if (NextPageNum == 0)
            {
                // The first page. Increase the left margin.
                e.PageSettings.Margins.Left += GUTTER;
            }
            else if (NextPageNum % 2 == 0)
            {
                // An even page. Increase the left margin
                // and decrease the right margin.
                e.PageSettings.Margins.Left += GUTTER;
                e.PageSettings.Margins.Right -= GUTTER;
            }
            else
            {
                // An odd page. Decrease the left margin
                // and increase the right margin.
                e.PageSettings.Margins.Left -= GUTTER;
                e.PageSettings.Margins.Right += GUTTER;
            }
        }

        // Display a print preview.
        private void button10_Click(object sender, EventArgs e)
        {
            printPreviewDialog_pages.ClientSize = new Size(1920 / 2, 1080 / 2);
            printPreviewDialog_pages.ShowDialog();
        }

        // Print.
        private void button11_Click(object sender, EventArgs e)
        {
            //printDocument_pages.Print();  //comment for safety
        }
        #endregion

        #region 格式化表單預覽列印
        // The sample data.
        private string[] Headers = { "Name", "Street", "City", "State", "Zip" };
        private string[,] Data =
            {
                {"Alice Archer", "1276 Ash Ave", "Ann Arbor", "MI", "12893"},
                {"Bill Blaze", "26157 Beach Blvd", "Boron", "CA", "23617"},
                {"Cindy Carruthers", "352 Cherry Ct", "Chicago", "IL", "35271"},
                {"Dean Dent", "4526 Deerfield Dr", "Denver", "CO", "47848"},
            };

        // Print the document's page.
        // Note that this version doesn't handle multiple pages.
        private void printDocument_grid2_PrintPage(object sender, PrintPageEventArgs e)
        {
            // Use this font.
            using (Font header_font = new Font("Times New Roman", 16, FontStyle.Bold))
            {
                using (Font body_font = new Font("Times New Roman", 12))
                {
                    // We'll skip this much space between rows.
                    int line_spacing = 20;

                    // See how wide the columns must be.
                    int[] column_widths = FindColumnWidths(
                        e.Graphics, header_font, body_font, Headers, Data);

                    // Start at the left margin.
                    int x = e.MarginBounds.Left;

                    // Print by columns.
                    for (int col = 0; col < Headers.Length; col++)
                    {
                        // Print the header.
                        int y = e.MarginBounds.Top;
                        e.Graphics.DrawString(Headers[col],
                            header_font, Brushes.Blue, x, y);
                        y += (int)(line_spacing * 1.5);

                        // Print the items in the column.
                        for (int row = 0; row <= Data.GetUpperBound(0); row++)
                        {
                            e.Graphics.DrawString(Data[row, col],
                                body_font, Brushes.Black, x, y);
                            y += line_spacing;
                        }

                        // Move to the next column.
                        x += column_widths[col];
                    } // Looping over columns
                } // using body_font
            } // using header_font

            //DrawGrid(e, y)
            e.HasMorePages = false;
        }

        // Figure out how wide each column should be.
        private int[] FindColumnWidths(Graphics gr, Font header_font, Font body_font, string[] headers, string[,] values)
        {
            // Make room for the widths.
            int[] widths = new int[headers.Length];

            // Find the width for each column.
            for (int col = 0; col < widths.Length; col++)
            {
                // Check the column header.
                widths[col] = (int)gr.MeasureString(headers[col], header_font).Width;

                // Check the items.
                for (int row = 0; row <= values.GetUpperBound(0); row++)
                {
                    int value_width = (int)gr.MeasureString(values[row, col], body_font).Width;
                    if (widths[col] < value_width) widths[col] = value_width;
                }

                // Add some extra space.
                widths[col] += 20;
            }

            return widths;
        }


        // Display a print preview.
        private void button12_Click(object sender, EventArgs e)
        {
            printPreviewDialog_grid2.ShowDialog();
        }
        #endregion

        //預覽列印巴斯卡三角形 ST

        // Display the print preview.
        private void button13_Click(object sender, EventArgs e)
        {
            // printDocument_pascal.PrinterSettings.PrinterName = "Dell Photo AIO Printer 926";

            printDocument_pascal.DefaultPageSettings.Margins = new System.Drawing.Printing.Margins(50, 50, 50, 50);
            printDocument_pascal.DefaultPageSettings.Landscape = true;
            printPreviewDialog_pascal.ShowDialog();
        }

        // Draw the triangle.
        private void printDocument_pascal_PrintPage(object sender, PrintPageEventArgs e)
        {
            using (Font font = new Font("Courier New", 4))
            {
                using (StringFormat format = new StringFormat())
                {
                    // Center each line.
                    format.Alignment = StringAlignment.Center;

                    const float width_factor = 6.5f;
                    int num_wid = (int)(width_factor * e.Graphics.MeasureString("0", font).Width);
                    int num_hgt = (int)e.Graphics.MeasureString("0", font).Height;
                    int y = e.MarginBounds.Top;
                    int xmid = (e.MarginBounds.Left + e.MarginBounds.Right) / 2;

                    // Make the first row.
                    List<int> numbers = new List<int>();
                    numbers.Add(1);

                    // Display rows.
                    while (y < e.MarginBounds.Height)
                    {
                        int x = xmid - (num_wid * numbers.Count) / 2;
                        if (x < e.MarginBounds.Left) break;

                        // Display the current list of numbers.
                        foreach (int num in numbers)
                        {
                            e.Graphics.DrawString(num.ToString(),
                                font, Brushes.Black, x, y, format);
                            x += num_wid;
                        }

                        // Add the next number to the list.
                        List<int> new_numbers = new List<int>();
                        new_numbers.Add(1);
                        for (int i = 1; i < numbers.Count; i++)
                        {
                            new_numbers.Add(numbers[i - 1] + numbers[i]);
                        }
                        new_numbers.Add(1);
                        numbers = new_numbers;

                        y += num_hgt;
                    }
                }
            }

        }

        //預覽列印巴斯卡三角形 SP

        // Display information about the selected printer.
        private void cboPrinters_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Lookup arrays.
            string[] PrinterStatuses = 
            {
                "Other", "Unknown", "Idle", "Printing", "WarmUp",
                "Stopped Printing", "Offline"
            };
            string[] PrinterStates = 
            {
                "Paused", "Error", "Pending Deletion", "Paper Jam",
                "Paper Out", "Manual Feed", "Paper Problem",
                "Offline", "IO Active", "Busy", "Printing",
                "Output Bin Full", "Not Available", "Waiting",
                "Processing", "Initialization", "Warming Up", 
                "Toner Low", "No Toner", "Page Punt",
                "User Intervention Required", "Out of Memory",
                "Door Open", "Server_Unknown", "Power Save"};

            // Get a ManagementObjectSearcher for the printer.
            string query = "SELECT * FROM Win32_Printer WHERE Name='" + cboPrinters.SelectedItem.ToString() + "'";
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);

            // Get the ManagementObjectCollection representing
            // the result of the WMI query. Loop through its
            // single item. Display some of that item's properties.
            foreach (ManagementObject service in searcher.Get())
            {
                txtName.Text = service.Properties["Name"].Value.ToString();

                UInt32 state = (UInt32)service.Properties["PrinterState"].Value;
                txtState.Text = PrinterStates[state];

                UInt16 status = (UInt16)service.Properties["PrinterStatus"].Value;
                txtStatus.Text = PrinterStatuses[status];

                txtDescription.Text = GetPropertyValue(service.Properties["Description"]);
                txtDefault.Text = GetPropertyValue(service.Properties["Default"]);
                txtHorRes.Text = GetPropertyValue(service.Properties["HorizontalResolution"]);
                txtVertRes.Text = GetPropertyValue(service.Properties["VerticalResolution"]);
                txtPort.Text = GetPropertyValue(service.Properties["PortName"]);

                lstPaperSizes.Items.Clear();
                string[] paper_sizes = (string[])service.Properties["PrinterPaperNames"].Value;
                foreach (string paper_size in paper_sizes)
                {
                    lstPaperSizes.Items.Add(paper_size);
                }

                // List the available properties.
                foreach (PropertyData data in service.Properties)
                {
                    string txt = data.Name;
                    if (data.Value != null)
                        txt += ": " + data.Value.ToString();
                    Console.WriteLine(txt);
                }
            }
        }

        // If the data is not null and has a value, return it.
        private string GetPropertyValue(PropertyData data)
        {
            if ((data == null) || (data.Value == null)) return "";
            return data.Value.ToString();
        }


        // At design time set:
        //      printPreviewDialog_control.Document = printDocument_control

        // Display a print preview.
        private void bt_print_control_Click(object sender, EventArgs e)
        {
            // Set the size.
            Form frm = printPreviewDialog_control as Form;
            if (chkMaximized.Checked)
            {
                // Display maximized.
                frm.WindowState = FormWindowState.Maximized;
            }
            else
            {
                // Make the client area 400 x 400.
                frm.WindowState = FormWindowState.Normal;
                frm.StartPosition = FormStartPosition.CenterScreen;
                printPreviewDialog_control.ClientSize = new Size(400, 400);
            }

            // Set the dialog's title.
            frm.Text = "Numbers";

            // Set the zoom level.
            if (chkZoom100.Checked)
            {
                // 100%.
                printPreviewDialog_control.PrintPreviewControl.Zoom = 1.0;
            }
            else
            {
                // Auto.
                printPreviewDialog_control.PrintPreviewControl.AutoZoom = true;
            }

            // Set anti-aliasing.
            printPreviewDialog_control.PrintPreviewControl.UseAntiAlias = chkAntiAlias.Checked;

            // Set other properties.
            printPreviewDialog_control.PrintPreviewControl.Columns = 3;
            printPreviewDialog_control.PrintPreviewControl.Rows = 3;
            printPreviewDialog_control.PrintPreviewControl.BackColor = Color.Orange; // Background color.
            printPreviewDialog_control.PrintPreviewControl.ForeColor = Color.Yellow; // Paper color.
            printPreviewDialog_control.PrintPreviewControl.StartPage = 3;            // Page 3 in the upper left.

            // Display the dialog.
            printPreviewDialog_control.ShowDialog();

        }


        // Print the document's pages.
        private int m_NextPage = 0;
        private void printDocument_control_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            // Draw the margins.
            using (Pen dashed_pen = new Pen(Color.Red, 5))
            {
                dashed_pen.DashPattern = new float[] { 10, 10 };
                e.Graphics.DrawRectangle(dashed_pen, e.MarginBounds);
            }

            // Draw an ellipse.
            e.Graphics.DrawEllipse(Pens.Blue, e.MarginBounds);

            // Draw the page number.
            // Center it inside the margins.
            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;
            sf.LineAlignment = StringAlignment.Center;

            using (Font the_font = new Font("Times New Roman", 200, FontStyle.Bold))
            {
                using (Brush the_brush = new SolidBrush(Color.Black))
                {
                    e.Graphics.DrawString(String.Format("{0}", m_NextPage + 1),
                        the_font, the_brush, e.MarginBounds, sf);
                }
            }

            // Next time print the next page.
            m_NextPage += 1;

            // We have more pages if wee have not yet printed page 10.
            e.HasMorePages = (m_NextPage <= 10);
        }

        // Get ready to print.
        private void printDocument_control_BeginPrint(object sender, System.Drawing.Printing.PrintEventArgs e)
        {
            // Start with page 0.
            m_NextPage = 0;
        }

        //6060

        private void bt_print_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.Document = this.printDocument_preview;
            printPreviewDialog1.ShowDialog();
            printDocument1.Print();
        }

        private void printDocument_preview_PrintPage(object sender, PrintPageEventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            try
            {
                Bitmap bitmap = new Bitmap(filename);
                e.Graphics.DrawImage(bitmap, 150, 240, 350, 300);
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        //6060

        private void bt_print2_Click(object sender, EventArgs e)
        {
            printDialog2.ShowDialog();
            printPreviewDialog2.Document = this.printDocument2;
            printPreviewDialog2.ShowDialog();
        }

        private void printDocument2_PrintPage(object sender, PrintPageEventArgs e)
        {
            e.Graphics.DrawString(label1.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 260, 400);
            e.Graphics.DrawString(textBox1.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 400);
            e.Graphics.DrawString(label2.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 270, 420);
            e.Graphics.DrawString(textBox2.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 420);
            e.Graphics.DrawString(label3.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 270, 440);
            e.Graphics.DrawString(textBox3.Text, new Font("細明體", 10, FontStyle.Regular), Brushes.Black, 330, 440);
        }
    }
}
