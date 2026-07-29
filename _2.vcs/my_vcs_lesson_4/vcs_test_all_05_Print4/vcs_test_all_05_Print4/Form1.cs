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
        //使用DGV1 ST
        int intPage = 0;//总页数
        int intRows = 0;//每页行数
        int EndRows = 0;//最后一页行数
        int currentpageindex = 1;//当前打印页
        Pen myPen = new Pen(Color.Black);
        Font myFont = new Font("宋体", 9);//字体
        Brush myBrush = new SolidBrush(Color.Black);//画刷
        int PrintPageHeight = 1169;//打印的默认高度
        int PrintPageWidth = 827;//打印的默认宽度
        int topmargin = 60; //顶边距 
        int rowgap = 0;//行高 
        int leftmargin = 50;//左边距 
        int rightmargin = 50;//右边距
        int buttommargin = 80;//底边距 
        int columnWidth1 = 57;//第一列宽度
        int columnWidth2 = 335;//第二列宽度
        //使用DGV1 SP

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

            //------------------------------------------------------------  # 60個

            //使用DGV1 ST
            intRows = Convert.ToInt32(textBox_page.Text);  // 每頁打印行數 

            add_datagridview(dataGridView1);

            //設置欄位寬度
            dataGridView1.Columns[0].Width = 57;
            dataGridView1.Columns[1].Width = 260;
            dataGridView1.Columns[2].Width = 280;

            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "資料總數 : " + R.ToString() + " 行\n";

            EndRows = (R - 2) % intRows;//去掉标题和最后一行的空行
            if (EndRows > 0)
            {
                intPage = Convert.ToInt32((R - 2) / intRows) + 1;
            }
            else
            {
                intPage = Convert.ToInt32((R - 2) / intRows);
            }
            richTextBox1.Text += "每頁行數 : " + intRows.ToString() + " 行\n";
            richTextBox1.Text += "總頁數 : " + intPage.ToString() + " 頁\n";

            //使用DGV1 SP
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

            groupBox4.Size = new Size(410, 70);
            //groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            groupBox5.Size = new Size(410, 100);
            //groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 100);

            dataGridView1.Size = new Size(410, 360);
            dataGridView1.Location = new Point(x_st + dx * 1, y_st + dy * 4+40);


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

            //版面設定
            // printDocument1 要加上方法 printDocument1_PrintPage

            //版面設定
            pageSetupDialog0.Document = printDocument0;

            if (pageSetupDialog0.ShowDialog() == DialogResult.OK)
            {
                printDocument0.DefaultPageSettings = pageSetupDialog0.PageSettings;
            }

            //6060

            PageSettings pageSetting = new System.Drawing.Printing.PageSettings();

            pageSetupDialog0.AllowMargins = true;
            pageSetupDialog0.AllowOrientation = true;
            pageSetupDialog0.AllowPaper = true;
            pageSetupDialog0.AllowPrinter = true;
            pageSetupDialog0.PageSettings = pageSetting;
            pageSetupDialog0.ShowDialog();
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

            //6060

            string text_filename = @"D:\_git\vcs\_1.data\______test_files1\__text\王之渙_涼州詞.txt";

            //列印
            printDocument0.DocumentName = text_filename;
            //printDocument0.Print();

        }

        private void printDocument0_PrintPage(object sender, PrintPageEventArgs e)
        {
            //整個紙張
            int xx = printDocument0.DefaultPageSettings.Bounds.X;
            int yy = printDocument0.DefaultPageSettings.Bounds.Y;
            int W = printDocument0.DefaultPageSettings.Bounds.Width;
            int H = printDocument0.DefaultPageSettings.Bounds.Height;
            e.Graphics.DrawRectangle(new Pen(Color.Green, 10), xx, yy, W, H);

            //3030

            //畫列印範圍, 可列印區間

            int x_st = e.MarginBounds.Left;
            int y_st = e.MarginBounds.Top;
            W = e.MarginBounds.Width;
            H = e.MarginBounds.Height;
            e.Graphics.DrawRectangle(Pens.Red, x_st, y_st, W, H);
            //e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            /*
            richTextBox1.Text += "可列印區間\n";
            richTextBox1.Text += e.MarginBounds.Left.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Right.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Top.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Bottom.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Width.ToString() + "\n";
            richTextBox1.Text += e.MarginBounds.Height.ToString() + "\n";
            */

            string text = "老來多驚夢，\n似有獻刀人，\n醒來懼銅鏡，\n怕顯董賊身。";

            Font f = new Font("標楷體", 64, FontStyle.Regular);
            f = new Font("標楷體", 50, FontStyle.Bold);

            SolidBrush sb = new SolidBrush(Color.Blue);
            x_st = printDocument0.DefaultPageSettings.Margins.Left;
            y_st = printDocument0.DefaultPageSettings.Margins.Top;
            e.Graphics.DrawString(text, f, sb, x_st, y_st);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap = new Bitmap(filename);
            e.Graphics.DrawImage(bitmap, 400, 640, bitmap.Width, bitmap.Height);

            x_st = e.MarginBounds.X;
            y_st = e.MarginBounds.Y;
            e.Graphics.FillEllipse(Brushes.Green, x_st - 20, y_st - 20, 40, 40);
            e.Graphics.DrawString("左上", new Font("細明體", 20, FontStyle.Regular), Brushes.Black, e.MarginBounds.X, e.MarginBounds.Y);

            /*
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
            */

            //DrawAxes(e);  // 在中間畫坐標軸

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
            if (flag_maximized == true)
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
            if (flag_zoom100 == true)
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
            printPreviewDialog555.PrintPreviewControl.Columns = 3;  // 每頁3欄
            printPreviewDialog555.PrintPreviewControl.Rows = 3;  // 每頁3列
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
            //畫列印範圍, 可列印區間
            e.Graphics.DrawRectangle(Pens.Red, e.MarginBounds.Left, e.MarginBounds.Top, e.MarginBounds.Width, e.MarginBounds.Height);

            Pen dashed_pen = new Pen(Color.Red, 5);
            dashed_pen.DashPattern = new float[] { 10, 10 };
            e.Graphics.DrawRectangle(dashed_pen, e.MarginBounds);
            e.Graphics.DrawEllipse(Pens.Blue, e.MarginBounds);

            // Draw the page number.
            // Center it inside the margins.
            StringFormat string_format = new StringFormat();
            string_format.Alignment = StringAlignment.Center;
            string_format.LineAlignment = StringAlignment.Center;

            Font the_font = new Font("Times New Roman", 200, FontStyle.Bold);
            Brush the_brush = new SolidBrush(Color.Black);
            e.Graphics.DrawString(String.Format("{0}", m_NextPage + 1), the_font, the_brush, e.MarginBounds, string_format);

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

        private void button2_Click(object sender, EventArgs e)
        {
            //預覽列印 月曆


            printPreviewDialog_Calendar.ShowDialog();  // 預覽列印
        }


        private void printDocument_Calendar_PrintPage(object sender, PrintPageEventArgs e)
        {

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
        }

        //------------------------------------------------------------  # 60個

        void add_datagridview(DataGridView dgv)
        {
            dgv.Columns.Clear();

            //設定DGV
            dgv.ColumnCount = 3;
            dgv.Columns[0].Name = "英文名";
            dgv.Columns[0].Width = 100;//設置欄位寬度
            dgv.Columns[1].Name = "中文名";
            dgv.Columns[1].Width = 100;//設置欄位寬度
            dgv.Columns[2].Name = "體重";
            dgv.Columns[2].Width = 100;//設置欄位寬度

            for (int i = 0; i < 80; i++)
            {
                dgv.Rows.Add(new Object[] { (i + 1).ToString("D4"), "班尼牛", 48 });
            }
        }

        //設置打印內容
        private void printDocument_dgv_PrintPage(object sender, PrintPageEventArgs e)
        {
            //畫列印範圍, 可列印區間
            e.Graphics.DrawRectangle(new Pen(Color.Green, 10), e.MarginBounds.Left - 10, e.MarginBounds.Top - 10, e.MarginBounds.Width + 20, e.MarginBounds.Height + 20);

            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "printDocument1_PrintPage, R = " + R.ToString() + "\n";

            if (R > 0)
            {
                PrintPageWidth = e.PageBounds.Width;//获取打印线张的宽度
                PrintPageHeight = e.PageBounds.Height;//获取打印线张的高度

                //myPen
                e.Graphics.DrawLine(Pens.Red, leftmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, topmargin);
                e.Graphics.DrawLine(Pens.Green, leftmargin, topmargin, leftmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(Pens.Blue, leftmargin, PrintPageHeight - topmargin - buttommargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(Pens.Cyan, PrintPageWidth - leftmargin - rightmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);

                int intPrintRows = currentpageindex * intRows;//当前页最后一条记录的索引
                //计算行高度
                rowgap = Convert.ToInt32((PrintPageHeight - topmargin - buttommargin - 5 * intRows) / intRows) + 3;
                int j = 0;//记录正在打印的行数
                for (int i = 0 + (intPrintRows - intRows); i < intPrintRows; i++)
                {
                    if (i <= R - 2)
                    {
                        richTextBox1.Text += "i = " + i.ToString() + "\t" +
                            dataGridView1.Rows[i].Cells[0].Value.ToString() + "\t" +
                            dataGridView1.Rows[i].Cells[1].Value.ToString() + "\t" +
                            dataGridView1.Rows[i].Cells[2].Value.ToString() + "\n";

                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[0].Value.ToString(),
                            myFont, myBrush, leftmargin + 5, topmargin + j * rowgap + 5);
                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[1].Value.ToString(),
                            myFont, myBrush, leftmargin + columnWidth1 + 5, topmargin + j * rowgap + 5);
                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[2].Value.ToString(),
                            myFont, myBrush, leftmargin + columnWidth1 + columnWidth2 + 5, topmargin + j * rowgap + 5);

                        //myPen
                        e.Graphics.DrawLine(Pens.Red, leftmargin, topmargin + j * rowgap + 1,
                            PrintPageWidth - leftmargin - rightmargin, topmargin + j * rowgap + 1);
                        e.Graphics.DrawLine(Pens.Green, leftmargin + columnWidth1, topmargin +
                            j * rowgap, leftmargin + columnWidth1, PrintPageHeight - topmargin - buttommargin);
                        e.Graphics.DrawLine(Pens.Blue, leftmargin + columnWidth1 + columnWidth2,
                            topmargin + j * rowgap, leftmargin + columnWidth1 + columnWidth2, PrintPageHeight - topmargin - buttommargin);

                        e.Graphics.DrawString("共 " + intPage + " 页   第 " + currentpageindex
                            + " 页", myFont, myBrush, PrintPageWidth - 200, (int)(PrintPageHeight - buttommargin / 2));
                        j++;//记数器
                    }
                }

                currentpageindex++;//下一页的页码
                if (currentpageindex <= intPage)//如果当前页不是最后一页
                {
                    e.HasMorePages = true;//打印副页
                }
                else
                {
                    e.HasMorePages = false;//不打印副页
                    currentpageindex = 1;//当前打印的页编号设为1
                }
            }
        }

        private void bt_dgv_print_Click(object sender, EventArgs e)
        {
            printPreviewDialog_dgv.ShowDialog();
        }

        //------------------------------------------------------------  # 60個

        private void bt_dgv_print2_Click(object sender, EventArgs e)
        {

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

//------------------------------------------------------------  # 60個

//預覽列印555
//1. 拉一個 PrintPreviewDialog 控件為 printPreviewDialog555
//2. 拉一個 PrintDocument      控件為 printDocument555, 在此選用印表機 printDocument_draw.PrinterSettings.PrinterName = use_printer;
//3. printPreviewDialog555     的屬性 Document   設定為 printDocument555
//3. printPreviewDialog555.Document = printDocument555
//4. printDocument555          的方法 PrintPage  設定為 printDocument555_PrintPage 設定要列印的內容
//5. printDocument555          的方法 BeginPrint 設定為 printDocument555_BeginPrint


//------------------------------------------------------------  # 60個

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

//------------------------------------------------------------  # 60個

 */
