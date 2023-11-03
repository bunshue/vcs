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
using System.Drawing.Printing;

namespace CH1407
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string readToPrint, allContents;
        private Font printFont;//列印字型

        //按下「預覽列印」按鈕
        private void btnPreview_Click(object sender, EventArgs e)
        {
            ReadPrintFile();
            printPreview.UseAntiAlias = true;//啟用平滑字效果
            printPreview.Document = OnPaper;
            printPreview.Document.DocumentName =
               "CH1407-Demo02";
            dlgPreview.ShowDialog();//顯示預覽列印對話方塊
        }

        //列印文件的PrintPage()事件處理
        private void OnPaper_PrintPage(object sender,
           PrintPageEventArgs ev)
        {
            int charsPerPage = 0;//統計每頁字元
            int morePages = 0; //統計頁數        
            Graphics gs = ev.Graphics;
            gs.MeasureString(readToPrint, printFont,
               ev.MarginBounds.Size,
               StringFormat.GenericTypographic,
               out charsPerPage, out morePages);

            //依據檔案內容繪製列印內容
            gs.DrawString(readToPrint, printFont,
               Brushes.Black, ev.MarginBounds,
               StringFormat.GenericTypographic);
            //移除已列印的字串
            readToPrint =
               readToPrint.Substring(charsPerPage);
            //當readToPrint大於零時，檢查是否要列印很多頁
            ev.HasMorePages = (readToPrint.Length > 0);
            if (!ev.HasMorePages)
                readToPrint = allContents;
        }

        //按下「列印」按鈕
        private void btnPrint_Click(object sender, EventArgs e)
        {
            ReadPrintFile();//呼叫載入檔案方法
                            //啟用「頁數」選項按鈕，「選取範圍」選項按鈕
            dlgPrint.AllowSomePages = true;
            dlgPrint.AllowSelection = true;
            //列印文件指定給列印對話方塊
            dlgPrint.Document = OnPaper;
            DialogResult result = dlgPrint.ShowDialog();
            //開啟列印對話方塊
            if (result == DialogResult.OK)
            {
                OnPaper.Print(); //執行列印
            }
        }

        //列印到最後一頁顯示訊息
        private void OnPaper_EndPrint(object sender,
              PrintEventArgs e)
        {
            MessageBox.Show(OnPaper.DocumentName +
               " -- 完成列印", "列印文件");
        }

        //利用FileStream來讀取檔案並開啟
        private void ReadPrintFile()
        {
            //設定要讀取取的檔名和路徑
            string printFile = "Demo02.txt";
            string filePath =
               @"D:\\C#Lab\\";
            //讀取的檔名「Demo02.txt」為列印文件的檔名
            OnPaper.DocumentName = printFile;
            //建立檔案並以Open開啟，以using指定範圍為唯讀
            using (FileStream stream = new FileStream(
               filePath + printFile, FileMode.Open))
            using (StreamReader reader = new
            StreamReader(stream)) //指定區段為唯讀
            {
                //allContents存放檔案內容
                allContents = reader.ReadToEnd();
            }
            readToPrint = allContents;
            printFont = new Font("標楷體", 20);
        }
    }
}
