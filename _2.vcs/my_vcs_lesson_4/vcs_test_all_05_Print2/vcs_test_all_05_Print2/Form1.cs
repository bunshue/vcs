using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

namespace vcs_test_all_05_Print2
{
    public partial class Form1 : Form
    {
        string text_filename = @"D:\_git\vcs\_1.data\______test_files1\__text\王之渙_涼州詞.txt";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            printPreviewDialog0.Document = printDocument0;
            printDialog0.Document = printDocument0;
            pageSetupDialog0.Document = printDocument0;
            textBox1.ScrollBars = ScrollBars.Both;
            textBox1.Font = new Font("標楷體", 24, FontStyle.Regular);
            textBox1.Text =
                "老來多驚夢，" + Environment.NewLine +
                "似有獻刀人，" + Environment.NewLine +
                "醒來懼銅鏡，" + Environment.NewLine +
                "怕顯董賊身。";

        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;
            groupBox0.Size = new Size(200, 280);
            groupBox1.Size = new Size(200, 280);
            groupBox2.Size = new Size(200, 280);
            groupBox3.Size = new Size(200, 280);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            textBox1.Size = new Size(400, 300);
            textBox1.Location = new Point(x_st + dx * 2, y_st + dy * 4 + 20);

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            x_st = 10;
            y_st = 300;
            dx = 180 + 10;
            dy = 55 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 4);

            this.Size = new Size(1300, 750);
            this.Text = "vcs_test_all_05_Print2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void printDocument0_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            Graphics g = e.Graphics;
            Font prnFont = new Font(textBox1.Font.Name, textBox1.Font.Size, textBox1.Font.Style);
            SolidBrush prnBrush = new SolidBrush(textBox1.ForeColor);
            Single left = printDocument0.DefaultPageSettings.Margins.Left - 10;
            Single top = printDocument0.DefaultPageSettings.Margins.Top - 20;
            g.DrawString(textBox1.Text, prnFont, prnBrush, left, top);
            g.DrawRectangle(Pens.Red, 50, 50, 300, 200);
            int W = printDocument0.DefaultPageSettings.Bounds.Width;
            int H = printDocument0.DefaultPageSettings.Bounds.Height;
            g.DrawRectangle(Pens.Red, 20, 20, W - 40, H - 40);
        }

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

        }

        private void button02_Click(object sender, EventArgs e)
        {
            //預覽列印
            //加入PrintDocument 和 PrintPreviewDialog
            //printPreviewDialog1屬性之Document選printDocument1
            //編輯 printDocument1_PrintPage

            //無印表機也可以預覽列印

            printPreviewDialog0.ClientSize = new Size(500, 600);
            printPreviewDialog0.ShowDialog();
        }

        private void button03_Click(object sender, EventArgs e)
        {
            //列印
            if (printDialog0.ShowDialog() == DialogResult.OK)
            {
                //Print()方法會觸動PrintDocument控制項的PrintPage事件
                printDocument0.Print();
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            // printDocument1 要加上方法 printDocument1_PrintPage

            //版面設定
            pageSetupDialog1.Document = printDocument1;

            if (pageSetupDialog1.ShowDialog() == DialogResult.OK)
            {
                printDocument1.DefaultPageSettings = pageSetupDialog1.PageSettings;
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //列印設定
            printDialog1.Document = printDocument1;
            printDialog1.PrinterSettings = pageSetupDialog1.PrinterSettings;

            if (printDialog1.ShowDialog() == DialogResult.OK)
            {
                printDocument1.Print();
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //預覽列印
            printPreviewDialog1.ShowDialog();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //列印
            printDocument1.DocumentName = text_filename;
            printDocument1.Print();
        }

        bool isFirstPage = true;
        float leftMargin;
        float topMargin;
        int pageNumber = 0;
        FileStream stream;
        StreamReader streamToPrint;
        float linesPerPage = 0;
        string pageNumberTtile;
        Font printFont;
        StringFormat format;
        RectangleF pageNumberArea;

        private void OpenFile()
        {
            string toPrintFile = text_filename;
            stream = new FileStream(toPrintFile, FileMode.Open);
            streamToPrint = new StreamReader(stream, Encoding.GetEncoding("big5"));
        }
        private void PageSetting(System.Drawing.Printing.PrintPageEventArgs e)
        {
            printFont = new Font("標楷體", 10);
            pageNumberArea = new RectangleF(0, e.PageBounds.Bottom - 20, e.PageSettings.Bounds.Width, 20);
            format = new StringFormat();
            format.Alignment = StringAlignment.Center;

            leftMargin = e.MarginBounds.Left;
            topMargin = e.MarginBounds.Top;
        }

        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            float yPos = 0;
            int count = 0;
            string line = null;

            try
            {
                if (isFirstPage)
                {
                    OpenFile();     // 判斷是否否是列印第一頁
                    PageSetting(e); // 設定列印頁碼所需的資料
                    // 計算每頁的列數
                    linesPerPage = e.MarginBounds.Height / printFont.GetHeight(e.Graphics);
                }

                // 列印檔案中的每一列
                while (count < linesPerPage && ((line = streamToPrint.ReadLine()) != null))
                {
                    yPos = topMargin + (count * printFont.GetHeight(e.Graphics));
                    e.Graphics.DrawString(
                        line,
                        printFont,
                        Brushes.Black,
                        leftMargin,
                        yPos,
                        new StringFormat());
                    count++;
                }

                // 如果還有沒列印完的內容，則列印其他頁
                if (line != null)
                {
                    e.HasMorePages = true;

                    // 註明再度執行PrintPage事件處理程序時，
                    // 是第二頁以後的頁面
                    isFirstPage = false;
                }
                else
                {
                    e.HasMorePages = false;
                }

                // 印出頁碼
                pageNumber++;
                pageNumberTtile = "第 " + pageNumber.ToString() + " 頁";
                e.Graphics.DrawString(
                    pageNumberTtile,
                    printFont,
                    Brushes.Red,
                    pageNumberArea,
                    format);
            }
            finally
            {
                if (!e.HasMorePages)
                {
                    // 如果所有頁面皆已列印完畢，則關閉檔案
                    streamToPrint.Close();
                    isFirstPage = true;
                }
            }
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

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

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
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */
