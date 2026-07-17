using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for File
using System.Drawing.Printing;  // for PrinterSettings
using System.Globalization;  // for CultureInfo
using System.Drawing.Drawing2D;  // for SmoothingMode
using System.Drawing.Text;  // for TextRenderingHint
using System.Management;  // 參考/加入參考/.NET/System Management

namespace vcs_test_all_05_Print1
{
    public partial class Form1 : Form
    {
        public bool Aspect = true;//打印方向
        public bool boundary = false;//是否打印分割线

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //紙張大小
            comboBox_PageSize.SelectedIndex = 0;

        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            comboBox_PageSize.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            //列出印表機資訊
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            dataGridView1.Size = new Size(300, 300);
            dataGridView1.Location = new Point(x_st + dx * 2, y_st + dy * 5 + 120);

            printPreviewControl1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 420 + 260);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 6 - 260);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 910);
            this.Text = "vcs_test_all_05_Print1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        string use_printer = string.Empty;
        private void button0_Click(object sender, EventArgs e)
        {
            // 列出印表機資訊
            foreach (string printer in PrinterSettings.InstalledPrinters)
            {
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
                richTextBox1.Text += "打印機名稱：" + printer + "\n";
                cboPrinters.Items.Add(printer);

                /*
                //打印機訊息, many
                PrinterSettings mprinter = new PrinterSettings();
                mprinter.PrinterName = printer;
                if (mprinter.IsValid)
                {
                    foreach (PrinterResolution resolution in mprinter.PrinterResolutions)
                    {
                        richTextBox1.Text += "分辨率：" + resolution.ToString() + "\n";
                    }
                    string prinsize = "";
                    foreach (PaperSize size in mprinter.PaperSizes)
                    {
                        if (Enum.IsDefined(size.Kind.GetType(), size.Kind))
                        {
                            prinsize += size.ToString() + "\n";
                        }
                    }
                    //many
                    //richTextBox1.AppendText("打印尺寸：\n" + prinsize + "\n");
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXX\n";
                }
                */
            }
            if (cboPrinters.Items.Count > 0)
            {
                cboPrinters.SelectedIndex = 0;  // 選第1台印表機
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            PrinterSettings settings = new PrinterSettings();
            richTextBox1.Text += "\n預設印表機 :\t" + settings.PrinterName + "\n\n";
            use_printer = settings.PrinterName;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個            

            // 改使用PDF印表機
            foreach (string printer in PrinterSettings.InstalledPrinters)
            {
                //richTextBox1.Text += "打印機名稱：" + printer + "\n";
                if (printer.Contains("PDF"))
                {
                    richTextBox1.Text += "改使用PDF印表機 : " + printer + "\n";
                    use_printer = printer;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        //列印一個純文字檔
        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            /*
            Font font = new Font("Times New Roman", 30);

            //e.MarginBounds.Left, e.MarginBounds.Top 列印邊界點
            e.Graphics.DrawString("Sample text", font, Brushes.Black, e.MarginBounds.Left, e.MarginBounds.Top);

            e.HasMorePages = false;  // 是否還有下一頁
            */

            const float font_size = 24;
            const float dy = font_size * 1.5f;  // 1.5倍列高
            float x0 = e.MarginBounds.Left + 0.5f * 100;
            float y = e.MarginBounds.Top;

            e.Graphics.DrawRectangle(Pens.Blue, x0, y, 100, 500);

            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            Font font = new Font("Times New Roman", font_size);
            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Center;  // 致中對齊

            e.Graphics.DrawString("李白", font, Brushes.Black, x0, y, sf);
            y += dy;
            e.Graphics.DrawString("望廬山瀑布", font, Brushes.Black, x0, y, sf);
            y += dy;
            e.Graphics.DrawString("日照香爐生紫煙", font, Brushes.Black, x0, y, sf);
            y += dy;
            e.Graphics.DrawString("遙看瀑布掛前川", font, Brushes.Black, x0, y, sf);
            y += dy;
            e.Graphics.DrawString("飛流直下三千尺", font, Brushes.Black, x0, y, sf);
            y += dy;
            e.Graphics.DrawString("疑是銀河落九天", font, Brushes.Black, x0, y, sf);
            y += dy;

            return;

            richTextBox1.Text += "列印一個純文字檔, 超過一頁會有問題\n";
            // The text contained in the file.
            string FileContents;
            string filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";

            FileContents = File.ReadAllText(filename, Encoding.Default).Trim();

            //FileContents="李白\n望廬山瀑布\n日照香爐生紫煙，\n遙看瀑布掛前川。\n飛流直下三千尺，\n疑是銀河落九天";"

            //Font font = new Font("Courier New", 16);

            // Make a StringFormat to align text normally.
            StringFormat string_format = new StringFormat();

            // See how much of the remaining text will fit.
            SizeF layout_area = new SizeF(e.MarginBounds.Width, e.MarginBounds.Height);
            int chars_fitted, lines_filled; e.Graphics.MeasureString(FileContents, font, layout_area, string_format, out chars_fitted, out lines_filled);

            // Print as much as will fit.
            e.Graphics.DrawString(FileContents.Substring(0, chars_fitted), font, Brushes.Black, e.MarginBounds, string_format);

            // Remove the printed text from the string.
            FileContents = FileContents.Substring(chars_fitted).Trim();

            // See if we are done.
            e.HasMorePages = FileContents.Length > 0;  // 是否還有下一頁
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //選擇印表機, 要列印到 pdf
            use_printer = "Microsoft Print to PDF";  // 需要先找到列印pdf的印表機名稱
            printDocument1.PrinterSettings.PrinterName = use_printer;

            // Set the print document name.
            printDocument1.DocumentName = "印表機處理器看到的文件名稱";

            // Print.
            printDocument1.Print();
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        //#region 多頁預覽列印 多頁列印
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
            StringFormat sf = new StringFormat();
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

            // Next time print the next page.
            NextPageNum += 1;

            // We have more pages if we have not yet printed page 3.
            e.HasMorePages = (NextPageNum <= 3);  // 是否還有下一頁

            // If we have no more pages, reset for the next time we print.
            if (NextPageNum > 3)
            {
                NextPageNum = 0;
            }
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
        //#endregion

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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
                    {
                        txt += ": " + data.Value.ToString();
                    }
                    Console.WriteLine(txt);
                }
            }
        }

        // If the data is not null and has a value, return it.
        private string GetPropertyValue(PropertyData data)
        {
            if ((data == null) || (data.Value == null))
            {
                return "";
            }
            return data.Value.ToString();
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            //使用PrintClass

            //填充dataGridView1

            //設定DGV
            dataGridView1.ColumnCount = 3;
            dataGridView1.Columns[0].Name = "英文名";
            dataGridView1.Columns[0].Width = 80;//設置欄位寬度
            dataGridView1.Columns[1].Name = "中文名";
            dataGridView1.Columns[1].Width = 80;//設置欄位寬度
            dataGridView1.Columns[2].Name = "體重";
            dataGridView1.Columns[2].Width = 80;//設置欄位寬度

            //填入資料
            string ENAME = "mouse";
            string CNAME = "米老鼠";
            string WEIGHT = "3";
            string[] row = new string[] { ENAME, CNAME, WEIGHT };
            dataGridView1.Rows.Add(row);
            dataGridView1.Rows.Add(new Object[] { "ox", "班尼牛", 48 });
            dataGridView1.Rows.Add(new Object[] { "tiger", "跳跳虎", 33 });

            //

            //对打印信息进行设置
            bool print_direction_width = false; //false:縱, true:橫
            if (print_direction_width == false)
            {
                PrintClass.PageScape = false;//纵向打印
                richTextBox1.Text += "縱向列印\n";
            }
            else
            {
                PrintClass.PageScape = true;//横向打印
                richTextBox1.Text += "橫向列印\n";
            }

            richTextBox1.Text += "紙張大小 : " + comboBox_PageSize.SelectedIndex + "\n";

            PrintClass dgp = new PrintClass(this.dataGridView1, comboBox_PageSize.SelectedIndex, print_direction_width);

            MSetUp(dgp);//记录窗体中打印信息的相关设置
            string[] header = new string[dataGridView1.ColumnCount];//创建一个与数据列相等的字符串数组
            for (int p = 0; p < dataGridView1.ColumnCount; p++)//记录所有列标题的名列
            {
                header[p] = dataGridView1.Columns[p].HeaderCell.Value.ToString();
            }

            //NG
            dgp.print();//显示打印预览窗体
        }

        // 设置打印数据的相关信息
        /// <param dgp="PrintClass">公共类PrintClass</param>
        private void MSetUp(PrintClass dgp)
        {
            dgp.PageAspect = Aspect;//设置横向打印
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


/*
// Display the available resolutions.
foreach (PrinterResolution resolution in printDocument1.DefaultPageSettings.PrinterSettings.PrinterResolutions)
{
    richTextBox1.Text += "支援的解析度\t" + resolution.ToString() + "\n";
}
//設定解析度
printDocument1.DefaultPageSettings.PrinterResolution = printDocument1.DefaultPageSettings.PrinterSettings.PrinterResolutions[0];

            printPreviewDialog_grid.ClientSize = new Size(500, 600);
            printPreviewDialog_grid.ShowDialog();

*/
