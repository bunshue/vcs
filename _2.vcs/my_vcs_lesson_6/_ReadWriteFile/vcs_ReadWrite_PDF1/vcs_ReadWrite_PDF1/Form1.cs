using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using iTextSharp.text;
using iTextSharp.text.pdf;

//參考/加入參考/ itextsharp.dll
//加入/現有項目 ICSharpCode.SharpZipLib.dll 有更新時才複製到輸出目錄

namespace vcs_ReadWrite_PDF1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //以RTB1的內容製作PDF檔案
            string filename = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

            //SaveFileDialog saveFileDialog = new SaveFileDialog(); 				//給出文件保存信息，確定保存位置
            //saveFileDialog.Filter = "PDF文件（*.PDF）|*.PDF";
            //if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                //開始創建PDF文檔，首先聲明一個Document對象
                Document document = new Document();
                //使用指定的路徑和創建模式初始化文件流對象
                PdfWriter.getInstance(document, new FileStream(filename, FileMode.Create));
                document.Open();										//打開文檔
                BaseFont baseFont = BaseFont.createFont(@"c:\windows\fonts\SIMSUN.TTC,1", BaseFont.IDENTITY_H, BaseFont.NOT_EMBEDDED);
                iTextSharp.text.Font font = new iTextSharp.text.Font(baseFont, 20); 	//設置文檔字體樣式
                document.Add(new Paragraph(richTextBox1.Text, font)); 			//添加內容至PDF文檔中
                document.Close();										//關閉文檔

                richTextBox2.Text += "存檔成功\n";
                richTextBox2.Text += "已存檔 : " + filename + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //TXT轉PDF

            string filename1 = @"C:\_git\vcs\_2.vcs\______test_files\__RW\_txt\琵琶行.txt";
            string filename2 = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

            var document = new Document(PageSize.A4, 30f, 30f, 30f, 30f);
            PdfWriter.getInstance(document, new FileStream(filename2, FileMode.Create));
            document.Open();

            BaseFont baseFont = BaseFont.createFont(@"c:\windows\fonts\SIMSUN.TTC,1", BaseFont.IDENTITY_H, BaseFont.NOT_EMBEDDED);
            iTextSharp.text.Font font = new iTextSharp.text.Font(baseFont, 20); 	//設置文檔字體樣式

            var objReader = new StreamReader(filename1, Encoding.GetEncoding("big5"));
            var str = "";
            while (str != null)
            {
                str = objReader.ReadLine();
                if (str != null)
                {
                    document.Add(new Paragraph(str, font));             //添加內容至PDF文檔中
                }
            }
            objReader.Close();
            document.Close();
            richTextBox2.Text += "存檔成功\n";
            richTextBox2.Text += "已存檔 : " + filename2 + "\n";
        }

    }
}



