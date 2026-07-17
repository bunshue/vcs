using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Printing;
using System.Globalization;  // for CultureInfo

namespace vcs_test_all_05_Print4
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

            //------------------------------------------------------------  # 60個

            //列印設定
            printDialog0.Document = printDocument0;
            printDialog0.PrinterSettings = pageSetupDialog0.PrinterSettings;
            printPreviewDialog0.Document = printDocument0;            

            pageSetupDialog0.Document = printDocument0;

            textBox1.ScrollBars = ScrollBars.Both;
            textBox1.Font = new Font("標楷體", 64, FontStyle.Regular);
            textBox1.Text =
                "老來多驚夢，" + Environment.NewLine +
                "似有獻刀人，" + Environment.NewLine +
                "醒來懼銅鏡，" + Environment.NewLine +
                "怕顯董賊身。";
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 280 + 10;

            groupBox0.Size = new Size(200, 280);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            dy = 60 + 10;
            textBox1.Size = new Size(240, 180);
            textBox1.Location = new Point(x_st + dx * 3 - 50, y_st + dy * 4 + 20);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 180 + 10;
            dy = 55 + 10;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            this.Size = new Size(1300, 750);
            this.Text = "vcs_test_all_05_Print4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button00_Click(object sender, EventArgs e)
        {
            //版面設定
            if (pageSetupDialog0.ShowDialog() == DialogResult.OK)
            {
                printDocument0.DefaultPageSettings = pageSetupDialog0.PageSettings;
            }
        }

        private void button01_Click(object sender, EventArgs e)
        {
            //列印設定
        }

        private void button02_Click(object sender, EventArgs e)
        {
            printPreviewDialog0.ClientSize = new Size(500, 600);
            printPreviewDialog0.ShowDialog();  // 預覽列印
        }

        private void button03_Click(object sender, EventArgs e)
        {
            //列印
            if (printDialog0.ShowDialog() == DialogResult.OK)
            {
                //Print()方法會觸動PrintDocument控制項的PrintPage事件
                printDocument0.Print();  // 列印
            }
        }

        private void printDocument0_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            richTextBox1.Text += "可列印區間\n";

            richTextBox1.Text += e.MarginBounds.Left.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Right.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Top.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Bottom.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Width.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Height.ToString() + "\n";

            int x_st = e.MarginBounds.Left;
            int y_st = e.MarginBounds.Top;
            int W = e.MarginBounds.Width;
            int H = e.MarginBounds.Height;
            e.Graphics.DrawRectangle(Pens.Red, x_st, y_st, W, H);

            e.Graphics.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            e.Graphics.DrawRectangle(Pens.Red, 100, 200, 100, 100);
            e.Graphics.DrawRectangle(Pens.Red, 100, 300, 100, 100);

            /*
            Graphics g = e.Graphics;
            Font f = new Font(textBox1.Font.Name, textBox1.Font.Size, textBox1.Font.Style);
            SolidBrush sb = new SolidBrush(textBox1.ForeColor);
            Single left = printDocument0.DefaultPageSettings.Margins.Left - 10;
            Single top = printDocument0.DefaultPageSettings.Margins.Top - 20;
            g.DrawString(textBox1.Text, f, sb, left, top);
            g.DrawRectangle(Pens.Red, 50, 50, 300, 200);
            int W = printDocument0.DefaultPageSettings.Bounds.Width;
            int H = printDocument0.DefaultPageSettings.Bounds.Height;
            g.DrawRectangle(Pens.Red, 20, 20, W - 40, H - 40);

            int x_st = 100;
            int y_st = 550;
            int dy = 60;
            e.Graphics.DrawString("老來多驚夢，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st);
            e.Graphics.DrawString("似有獻刀人，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 1);
            e.Graphics.DrawString("醒來懼銅鏡，", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 2);
            e.Graphics.DrawString("怕顯董賊身。", new Font("細明體", 36, FontStyle.Regular), Brushes.Black, x_st, y_st + dy * 3);
            */

            // Convert mm to inches * 100.
            float diameter = 100;
            diameter = diameter / 25.4f * 100f;

            float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
            float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;
            float x = cx - diameter / 2f;
            float y = cy - diameter / 2f;

            RectangleF rect = new RectangleF(x, y, diameter, diameter);

            e.Graphics.DrawEllipse(Pens.Red, rect);

            /*
            Draw the star.
            */

            // Draw axes in the middle of the page.
            DrawAxes(e);

            e.HasMorePages = false;
        }

        // Draw axes in the middle of the page.
        private void DrawAxes(PrintPageEventArgs e)
        {
            float cx = (e.MarginBounds.Left + e.MarginBounds.Right) / 2f;
            float cy = (e.MarginBounds.Top + e.MarginBounds.Bottom) / 2f;

            e.Graphics.DrawLine(Pens.Black, e.MarginBounds.Left, cy, e.MarginBounds.Right, cy);
            e.Graphics.DrawLine(Pens.Black, cx, e.MarginBounds.Top, cx, e.MarginBounds.Bottom);

            for (float x = cx; x <= e.MarginBounds.Right; x += 100)
            {
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);
            }

            for (float x = cx; x >= e.MarginBounds.Left; x -= 100)
            {
                e.Graphics.DrawLine(Pens.Black, x, cy - 25, x, cy + 25);
            }

            for (float y = cy; y <= e.MarginBounds.Bottom; y += 100)
            {
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
            }

            for (float y = cy; y >= e.MarginBounds.Top; y -= 100)
            {
                e.Graphics.DrawLine(Pens.Black, cx - 25, y, cx + 25, y);
            }
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //列印畫圖 至 pdf

        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            bool flag_maximized = false;  // 最大化
            bool flag_zoom100 = false;  // zoom
            bool flag_anti_alias = false;  // 反鋸齒

            //預覽列印
            // Set the size.
            Form frm = printPreviewDialog555 as Form;
            if (flag_maximized==true)
            {
                // Display maximized.
                frm.WindowState = FormWindowState.Maximized;
            }
            else
            {
                // Make the client area 400 x 400.
                frm.WindowState = FormWindowState.Normal;
                frm.StartPosition = FormStartPosition.CenterScreen;
                printPreviewDialog555.ClientSize = new Size(400, 400);
            }

            // Set the dialog's title.
            frm.Text = "Numbers";

            // Set the zoom level.
            if (flag_zoom100==true)
            {
                // 100%.
                printPreviewDialog555.PrintPreviewControl.Zoom = 1.0;
            }
            else
            {
                // Auto.
                printPreviewDialog555.PrintPreviewControl.AutoZoom = true;
            }

            // Set anti-aliasing.
            printPreviewDialog555.PrintPreviewControl.UseAntiAlias = flag_anti_alias;

            // Set other properties.
            printPreviewDialog555.PrintPreviewControl.Columns = 3;
            printPreviewDialog555.PrintPreviewControl.Rows = 3;
            printPreviewDialog555.PrintPreviewControl.BackColor = Color.Orange; // Background color.
            printPreviewDialog555.PrintPreviewControl.ForeColor = Color.Yellow; // Paper color.
            printPreviewDialog555.PrintPreviewControl.StartPage = 3;            // Page 3 in the upper left.
            //第3頁

            printPreviewDialog555.ShowDialog();  // 預覽列印
        }

        // Print the document's pages.
        private int m_NextPage = 0;
        private void printDocument555_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

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
                    e.Graphics.DrawString(String.Format("{0}", m_NextPage + 1), the_font, the_brush, e.MarginBounds, sf);
                }
            }

            // Next time print the next page.
            m_NextPage += 1;

            // We have more pages if wee have not yet printed page 10.
            e.HasMorePages = (m_NextPage <= 10);
        }

        // Get ready to print.
        private void printDocument555_BeginPrint(object sender, PrintEventArgs e)
        {
            // Start with page 0.
            m_NextPage = 0;
        }

        //------------------------------------------------------------  # 60個

        // The calendar data.
        DateTime FirstOfMonth;
        private string[] CalendarData;

        // Display a print preview of the calendar.

        private void button2_Click(object sender, EventArgs e)
        {
            //預覽列印 月曆
            // Get the selected month and year.
            int year_num = 2026;
            int month_num = 7;
            richTextBox1.Text += "year = " + year_num.ToString() + "\n";
            richTextBox1.Text += "month = " + month_num.ToString() + "\n";

            DateTime first_of_month = new DateTime(year_num, month_num, 1);

            // See how many days are in the selected month.
            int num_days = DateTime.DaysInMonth(year_num, month_num);

            // Generate some "random" data for the indicated month.
            CalendarData = MakeData(num_days);

            // Save the first date of the selected month.
            FirstOfMonth = first_of_month;

            printPreviewDialog_Calendar.ShowDialog();  // 預覽列印
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

        // Draw the calendar.
        private void printDocument_Calendar_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            DrawCalendar(e.Graphics, e.MarginBounds, FirstOfMonth, CalendarData);
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
            DrawDateData(first_of_month, date_data, gr, x, y, col_wid, row_hgt);

            // Outline the calendar.
            gr.DrawRectangle(Pens.Black, bounds.X, bounds.Y, bounds.Width, bounds.Height);
        }

        // Return the number of week rows needed by this month.
        private int NumberOfWeekRows(DateTime first_of_month)
        {
            // Get the number of days in the month.
            int num_days = DateTime.DaysInMonth(first_of_month.Year, first_of_month.Month);

            // Add the column number for the first day of the month.
            num_days += DateColumn(first_of_month);

            // Divide by 7 and round up.
            return (int)Math.Ceiling(num_days / 7f);
        }

        // Return the column number for this date in the current locale.
        private int DateColumn(DateTime date)
        {
            int col = (int)date.DayOfWeek - (int)CultureInfo.CurrentCulture.DateTimeFormat.FirstDayOfWeek;
            if (col < 0)
            {
                col += 7;
            }
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

                string[] month_names = CultureInfo.CurrentCulture.DateTimeFormat.MonthNames;
                string title = month_names[date.Month - 1] + " " + date.Year.ToString();

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
            string[] day_names = CultureInfo.CurrentCulture.DateTimeFormat.DayNames;
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
        private void DrawDateData(DateTime first_of_month, string[] date_data, Graphics gr, float x, float y, float col_wid, float row_hgt)
        {
            // Let date numbers occupy the upper quarter and left third of the date box.
            RectangleF date_rectf = new RectangleF(x, y, col_wid / 3f, row_hgt / 4f);

            // The date data goes below the date rectangle.
            RectangleF data_rectf = new RectangleF(x, y, col_wid, row_hgt * 0.75f);

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

                        int num_days = DateTime.DaysInMonth(first_of_month.Year, first_of_month.Month);
                        for (int day_num = 0; day_num < num_days; day_num++)
                        {
                            // Outline the cell.
                            RectangleF cell_rectf = new RectangleF(x + col * col_wid, y, col_wid, row_hgt);
                            gr.DrawRectangle(Pens.Black, cell_rectf.X, cell_rectf.Y, cell_rectf.Width, cell_rectf.Height);

                            // Draw the date.
                            date_rectf.X = cell_rectf.X;
                            date_rectf.Y = cell_rectf.Y;
                            gr.DrawString((day_num + 1).ToString(), number_font, Brushes.Blue, date_rectf, ul_sf);

                            // Draw the data.
                            data_rectf.X = x + col * col_wid;
                            data_rectf.Y = y + row_hgt * 0.25f;
                            gr.DrawString(date_data[day_num], data_font, Brushes.Black, data_rectf, ul_sf);

                            // Move to the next cell.
                            col = (col + 1) % 7;
                            if (col == 0)
                            {
                                y += row_hgt;
                            }
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
                    if ((text_size.Width > rectf.Width) || (text_size.Height > rectf.Height))
                    {
                        return font_size - 1;
                    }
                }
            }
        }

        // Print in landscape mode.
        private void printDocument_Calendar_QueryPageSettings(object sender, QueryPageSettingsEventArgs e)
        {
            e.PageSettings.Landscape = true;
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            // 預覽列印 圖片
            printPreviewDialog_image.ShowDialog();  // 預覽列印
        }

        private void printDocument_image_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            string text = "千江有水千月，\n萬里晴空萬里晴";
            Font oneFont = new Font("標楷體", 50, FontStyle.Bold);
            e.Graphics.DrawString(text, oneFont, Brushes.Blue, 50, 50);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap = new Bitmap(filename);
            e.Graphics.DrawImage(bitmap, 150, 240, 350, 300);

            return;
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = (Bitmap)Bitmap.FromFile(filename);

            // Print in the upper left corner at its full size.
            e.Graphics.DrawImage(bmp, e.MarginBounds.X, e.MarginBounds.Y, bmp.Width, bmp.Height);
            e.Graphics.DrawString("左上", new Font("細明體", 20, FontStyle.Regular), Brushes.Black, e.MarginBounds.X, e.MarginBounds.Y);

            // Print in the upper right corner,
            // sized to fit beside the other image.
            int left = e.MarginBounds.Left + bmp.Width;
            int width = e.MarginBounds.Width - bmp.Width;
            float scale = width / (float)bmp.Width;

            int height = (int)(bmp.Height * scale);
            e.Graphics.DrawImage(bmp, left, e.MarginBounds.Y, width, height);
            e.Graphics.DrawString("右上", new Font("細明體", 20, FontStyle.Regular), Brushes.Black, left, e.MarginBounds.Y);

            // Print the same size in the lower right corner.
            int top = e.MarginBounds.Bottom - height;
            e.Graphics.DrawImage(bmp, left, top, width, height);
            e.Graphics.DrawString("右下", new Font("細明體", 20, FontStyle.Regular), Brushes.Black, left, top);
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*

//5. 開啟預覽列印
            // printDocument_pascal.PrinterSettings.PrinterName = "Dell Photo AIO Printer 926";
            printDocument_pascal.DefaultPageSettings.Margins = new System.Drawing.Printing.Margins(50, 50, 50, 50);
            printDocument_pascal.DefaultPageSettings.Landscape = true;
*/

//預覽列印555
//1. 拉一個 PrintPreviewDialog 控件為 printPreviewDialog555
//2. 拉一個 PrintDocument      控件為 printDocument555, 在此選用印表機 printDocument_draw.PrinterSettings.PrinterName = use_printer;
//3. printPreviewDialog555     的屬性 Document   設定為 printDocument555
//3. printPreviewDialog555.Document = printDocument555
//4. printDocument555          的方法 PrintPage  設定為 printDocument555_PrintPage 設定要列印的內容
//5. printDocument555          的方法 BeginPrint 設定為 printDocument555_BeginPrint


/*

            //對話方塊啟用頁數核取方塊
            printDialog2.AllowSomePages = true;
            //對話方塊啟用說明按鈕
            printDialog2.ShowHelp = true;
            //列印對話方塊中，按下確定鈕的話
            DialogResult result = printDialog2.ShowDialog();
            if (result == DialogResult.OK)
            {
                printDocument2.Print();
            }

*/