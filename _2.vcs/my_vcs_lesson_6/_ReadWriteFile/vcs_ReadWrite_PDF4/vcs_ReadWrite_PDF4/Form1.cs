using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_PDF4
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\__RW\\_pdf\\note_Linux_workstation.pdf";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {


        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //string filename = @"D:\_backup\_語言雜誌壓縮檔\_常春藤\202102常春藤解析英語\常春藤解析英語-202102.pdf";

            string command = filename;

            int toolbar = 1;    //show adobe pdf's toolbar


            //webBrowser1.Navigate(command);

            //webBrowser1.Navigate(pdf_filename + "?#zoom=" + zoomFactor.ToString() + "%&view=fith&navpanes=0&toolbar=0&page=" + PDF_PAGE.ToString());

            //int zoomFactor = 50;
            //command = filename + "?#view=fith&navpanes=0&toolbar=1&page=10";

            command = filename + "#page=10";    //顯示第幾頁

            command = filename + "#toolbar=0";  //上方工具列, 預設為開

            command = filename + "#navpanes=1";  //左方工具列, 預設為關

            command = filename + "#zoom = 60 %";    //顯示比例  有無%皆可


            command = filename + "#view = fit&page=10";    //顯示比例

            command = filename + "?#zoom = 70 % & navpanes = 0 & toolbar = 0 & page = 10";

            command = filename + "#search=tom"; //搜尋pattern

            command = filename + "#scrollbar=1&toolbar=1&statusbar=1&navpanes=1"; //全部打開

            command = filename + "#page=10 & view = FitBV";
            //The value for fit can be Fit, FitH, FitV, FitB, FitBH, or FitBV. 

            command = filename;
            command = filename + "#page=12&zoom=200,250,100";
            command = filename + "#page=12&view=fit,1000";
            command = filename + "#view=fitb&nameddest=tom";
            command = filename + "#pagemode=none";
            command = filename + "#pagemode=bookmarks&page=12";
            command = filename + "#page=12&pagemode=thumbs";    //有頁面縮圖

            command = filename + "#nameddest=02.15";

            webBrowser1.Navigate(command);


            /*

                              url: 'ConferenceGuide.pdf', 
                  pdfOpenParams: { 
                       view: 'Fit', 
                       scrollbars: '0', 
                       toolbar: '0', 
                       statusbar: '0', 
                       navpanes: '0' }
                   }).embed('pdf1'); 
              */     

        }
    }
}
