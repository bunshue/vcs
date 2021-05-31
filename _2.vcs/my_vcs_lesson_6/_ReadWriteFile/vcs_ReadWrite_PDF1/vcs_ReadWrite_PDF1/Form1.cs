using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using iTextSharp.text;
using iTextSharp.text.pdf;
using System.IO;

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

        private void button1_Click(object sender, EventArgs e)
        {
            //以RTB1的內容製作PDF檔案
            string filename = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

            //SaveFileDialog saveFileDialog = new SaveFileDialog(); 				//给出文件保存信息，确定保存位置
            //saveFileDialog.Filter = "PDF文件（*.PDF）|*.PDF";
            //if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                //开始创建PDF文档，首先声明一个Document对象
                Document document = new Document();
                //使用指定的路径和创建模式初始化文件流对象
                PdfWriter.getInstance(document, new FileStream(filename, FileMode.Create));
                document.Open();										//打开文档
                BaseFont baseFont = BaseFont.createFont(@"c:\windows\fonts\SIMSUN.TTC,1", BaseFont.IDENTITY_H, BaseFont.NOT_EMBEDDED);
                iTextSharp.text.Font font = new iTextSharp.text.Font(baseFont, 20); 	//设置文档字体样式
                document.Add(new Paragraph(richTextBox1.Text, font)); 			//添加内容至PDF文档中
                document.Close();										//关闭文档

                richTextBox2.Text += "存檔成功\n";
                richTextBox2.Text += "已存檔 : " + filename + "\n";

            }
        }
    }
}
