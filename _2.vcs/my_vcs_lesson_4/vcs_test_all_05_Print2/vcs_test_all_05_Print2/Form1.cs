using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Printing;

/*
預覽列印
printPreviewDialog3
改Document為printDocument3

列印
printDialog3
改Document為printDocument3

列印文件
printDocument3
改DocumentName 自訂 document3
加printDocument3_PrintPage
加printDocument3_EndPrint
*/

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

            //------------------------------------------------------------  # 60個

            printPreviewDialog0.Document = printDocument0;
            printDialog0.Document = printDocument0;
            pageSetupDialog0.Document = printDocument0;

            button30.Enabled = false;
            button31.Enabled = false;
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 280 + 10;

            groupBox0.Size = new Size(200, 280);
            groupBox1.Size = new Size(200, 280);
            groupBox3.Size = new Size(200, 280);
            groupBox4.Size = new Size(200, 280);
            groupBox5.Size = new Size(200, 280);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            printPreviewControl1.Size = new Size(240, 180);
            printPreviewControl1.Location = new Point(x_st + dx * 3 - 50, y_st + dy * 7);

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
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button53.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            x_st = 425;
            y_st = 300;
            dx = 180 + 10;
            dy = 55 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

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

        //------------------------------------------------------------  # 60個

        private void printDocument0_PrintPage(object sender, PrintPageEventArgs e)
        {
        }

        private void button00_Click(object sender, EventArgs e)
        {
        }

        private void button01_Click(object sender, EventArgs e)
        {

        }

        private void button02_Click(object sender, EventArgs e)
        {
        }

        private void button03_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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
        }

        private void button12_Click(object sender, EventArgs e)
        {
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
        private void PageSetting(PrintPageEventArgs e)
        {
            printFont = new Font("標楷體", 10);
            pageNumberArea = new RectangleF(0, e.PageBounds.Bottom - 20, e.PageSettings.Bounds.Width, 20);
            format = new StringFormat();
            format.Alignment = StringAlignment.Center;

            leftMargin = e.MarginBounds.Left;
            topMargin = e.MarginBounds.Top;
        }

        private void printDocument1_PrintPage(object sender, PrintPageEventArgs e)
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

        //------------------------------------------------------------  # 60個

        private string readToPrint, allContents;
        private Font printFont3;//列印字型

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        //利用FileStream來讀取檔案並開啟
        private void ReadPrintFile()
        {
            //設定要讀取取的檔名和路徑
            string printFile = "Demo02.txt";
            string filePath = @"D:\\vcs\\";
            //讀取的檔名「Demo02.txt」為列印文件的檔名
            printDocument3.DocumentName = printFile;
            //建立檔案並以Open開啟，以using指定範圍為唯讀
            using (FileStream stream = new FileStream(filePath + printFile, FileMode.Open))
            using (StreamReader reader = new
            StreamReader(stream)) //指定區段為唯讀
            {
                //allContents存放檔案內容
                allContents = reader.ReadToEnd();
            }
            readToPrint = allContents;
            printFont3 = new Font("標楷體", 20);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //預覽列印

            ReadPrintFile();

            printPreviewControl1.UseAntiAlias = true;//啟用平滑字效果
            printPreviewControl1.Document = printDocument3;
            printPreviewControl1.Document.DocumentName = "CH1407-Demo02";

            printPreviewDialog3.ShowDialog();//顯示預覽列印對話方塊
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //列印
            ReadPrintFile();//呼叫載入檔案方法
            //啟用「頁數」選項按鈕，「選取範圍」選項按鈕
            printDialog3.AllowSomePages = true;
            printDialog3.AllowSelection = true;
            //列印文件指定給列印對話方塊
            printDialog3.Document = printDocument3;
            DialogResult result = printDialog3.ShowDialog();
            //開啟列印對話方塊
            if (result == DialogResult.OK)
            {
                printDocument3.Print(); //執行列印
            }
        }

        private void printDocument3_PrintPage(object sender, PrintPageEventArgs e)
        {
            int charsPerPage = 0;//統計每頁字元
            int morePages = 0; //統計頁數        
            Graphics gs = e.Graphics;
            gs.MeasureString(readToPrint, printFont3, e.MarginBounds.Size, StringFormat.GenericTypographic, out charsPerPage, out morePages);

            //依據檔案內容繪製列印內容
            gs.DrawString(readToPrint, printFont3, Brushes.Black, e.MarginBounds, StringFormat.GenericTypographic);
            //移除已列印的字串
            readToPrint = readToPrint.Substring(charsPerPage);
            //當readToPrint大於零時，檢查是否要列印很多頁
            e.HasMorePages = (readToPrint.Length > 0);
            if (!e.HasMorePages)
            {
                readToPrint = allContents;
            }
        }

        //列印到最後一頁顯示訊息
        private void printDocument3_EndPrint(object sender, PrintEventArgs e)
        {
            MessageBox.Show(printDocument3.DocumentName + " -- 完成列印", "列印文件");
        }

        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button50_Click(object sender, EventArgs e)
        {

        }

        private void button51_Click(object sender, EventArgs e)
        {

        }

        private void button52_Click(object sender, EventArgs e)
        {

        }

        private void button53_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //print
            //printDocumentA
            richTextBox1.LoadFile("../../../Demo01.rtf");
            printDocumentA.DocumentName = "AAAAAAA";

            printDocumentA.Print();
        }

        //PrintDocument的事件
        private void printDocumentA_PrintPage(object sender, PrintPageEventArgs e)
        {
            //1.建立繪圖物件gs和參數ev的關聯
            Graphics gs = e.Graphics;
            //設定列印字型
            Font fontPrint = new Font("Segoe Print", 14);
            int morePages = 0; //計算每份文件頁數
            int OnPageChars = 0;//計算每頁字元數
            //2.測量要繪製的字串
            gs.MeasureString(richTextBox1.Text, fontPrint, e.MarginBounds.Size, StringFormat.GenericTypographic, out OnPageChars, out morePages);
            //3.繪製邊界內的字型
            gs.DrawString(richTextBox1.Text, fontPrint, Brushes.Black, e.MarginBounds, new StringFormat());
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //設定印表機
            //printDialogB
            printDialogB.AllowCurrentPage = true;       //顯示當前頁
            printDialogB.AllowPrintToFile = true;       //允許選擇打印到文件
            printDialogB.AllowSelection = true;         //啟用“選擇”單選按鈕
            printDialogB.AllowSomePages = true;         //啟用“頁”單選按鈕
            //printDialogB.Document = printDocument1;   //指定設置的PrintDocument對象
            //printDialogB.PrinterSettings = printDocument1.PrinterSettings;    //打印頁的默認設置
            printDialogB.PrintToFile = false;           //不選擇“打印到文件”
            printDialogB.ShowHelp = true;               //顯示“幫助”按鈕
            printDialogB.ShowNetwork = true;            //可以選擇網絡打印機
            if (printDialogB.ShowDialog() == DialogResult.OK)
            {
                //printDocumentB.Print();    //打印
            }
            else
            {
            }
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
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

