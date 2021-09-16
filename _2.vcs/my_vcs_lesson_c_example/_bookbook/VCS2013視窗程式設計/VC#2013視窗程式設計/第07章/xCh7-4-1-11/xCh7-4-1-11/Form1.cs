using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace xCh7_4_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            textBox1.Text = openFileDialog1.FileName;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            printDocument1.DocumentName = textBox1.Text;
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
            string toPrintFile = textBox1.Text;
            stream = new FileStream(toPrintFile, FileMode.Open);
            streamToPrint = new StreamReader(
                stream,
                Encoding.GetEncoding("big5")
                );
        }
        private void PageSetting(System.Drawing.Printing.PrintPageEventArgs e)
        {
            printFont = new Font("標楷體", 10);
            pageNumberArea = new RectangleF(
                0, 
                e.PageBounds.Bottom - 20, 
                e.PageSettings.Bounds.Width, 
                20
                );
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
                    linesPerPage = 
                        e.MarginBounds.Height / printFont.GetHeight(e.Graphics);
                }

                // 列印檔案中的每一列
                while (count < linesPerPage &&
                    ((line = streamToPrint.ReadLine()) != null))
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
                    e.HasMorePages = false;

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

        private void button3_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pageSetupDialog1.Document = printDocument1;

            if (pageSetupDialog1.ShowDialog() == DialogResult.OK) 
                printDocument1.DefaultPageSettings = pageSetupDialog1.PageSettings;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            printDialog1.Document = printDocument1;
            printDialog1.PrinterSettings = pageSetupDialog1.PrinterSettings;

            if (printDialog1.ShowDialog() == DialogResult.OK)
                printDocument1.Print();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            xCh7_4_1_11AboutBox frmAboutbox = new xCh7_4_1_11AboutBox();
            frmAboutbox.ShowDialog();
        }
    }
}
