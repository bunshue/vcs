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




    }
}
