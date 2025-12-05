using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path

using iTextSharp.text;
using iTextSharp.text.pdf;

//使用ICSharpCode.SharZipLib.dll製作pdf檔
//參考/加入參考/ dll/itextsharp.dll
//加入/現有項目 ICSharpCode.SharpZipLib.dll 有更新時才複製到輸出目錄

//參考/加入參考/PdfSharp.dll
using PdfSharp;
using PdfSharp.Pdf;
using PdfSharp.Drawing;

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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

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
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            groupBox1.Size = new Size(200, 580);
            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(600, 220);
            richTextBox2.Size = new Size(600, 220);
            webBrowser1.Size = new Size(600, 220);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox2.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            webBrowser1.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            y_st = 20;
            dx = 180 + 5;
            dy = 50 + 5;
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            this.Size = new Size(1260, 700);
        }

        void show_item_location2()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Visible = false;
            button1.Visible = false;
            button2.Visible = false;
            button3.Visible = false;
            button4.Visible = false;
            button5.Visible = false;
            button6.Visible = false;
            button7.Visible = false;
            button8.Visible = false;
            button9.Visible = false;
            button10.Visible = false;
            button11.Visible = false;
            button12.Visible = false;
            button13.Visible = false;
            button14.Visible = false;
            button15.Visible = false;
            button16.Visible = false;
            button17.Visible = false;
            button18.Visible = false;
            button19.Visible = false;

            groupBox1.Size = new Size(200, 580);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 600);
            richTextBox2.Size = new Size(600, 220);
            webBrowser1.Size = new Size(600, 600);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox2.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            webBrowser1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            richTextBox2.Visible = false;

            y_st = 20;
            dx = 180 + 5;
            dy = 50 + 5;
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            this.Size = new Size(1260, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //以RTB1的內容製作PDF檔案
            string filename = "tmp_pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

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

        private void button1_Click(object sender, EventArgs e)
        {
            //TXT轉PDF

            string filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";
            string filename2 = "tmp_pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

            var document = new Document(iTextSharp.text.PageSize.A4, 30f, 30f, 30f, 30f);
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

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";

            string result = ReadPdf(filename);
            richTextBox1.Text += "result : " + result + "\n";

            int pageCount = GetPdfPageCount(filename);

            richTextBox1.Text += "pageCount : " + pageCount.ToString() + "\n";
        }

        /// <summary>
        /// 讀取PDF文本內容
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static string ReadPdf(string fileName)
        {
            if (!File.Exists(fileName))
            {
                //LogHandler.LogWrite(@"指定的PDF文件不存在：" + fileName);
                return string.Empty;
            }
            //
            string fileContent = string.Empty;
            StringBuilder sbFileContent = new StringBuilder();
            //打開文件
            PdfReader reader = null;
            try
            {
                reader = new PdfReader(fileName);
            }
            catch (Exception ex)
            {
                //LogHandler.LogWrite(string.Format(@"加載PDF文件{0}失敗,錯誤:{1}", new string[] { fileName, ex.ToString() }));

                if (reader != null)
                {
                    reader = null;
                }

                return string.Empty;
            }

            try
            {
                //循環各頁（索引從1開始）
                for (int i = 1; i <= reader.NumberOfPages; i++)
                {
                    //sbFileContent.AppendLine(PdfTextExtractor.GetTextFromPage(reader, i));

                }

            }
            catch (Exception ex)
            {
                //LogHandler.LogWrite(string.Format(@"解析PDF文件{0}失敗,錯誤:{1}", new string[] { fileName, ex.ToString() }));

            }
            finally
            {
                if (reader != null)
                {
                    reader = null;
                }
            }
            //
            fileContent = sbFileContent.ToString();
            return fileContent;
        }
        /// <summary>
        /// 獲取PDF頁數
        /// </summary>
        /// <param name="fileName"></param>
        /// <returns></returns>
        public static int GetPdfPageCount(string fileName)
        {
            if (!File.Exists(fileName))
            {
                //LogHandler.LogWrite(@"指定的PDF文件不存在：" + fileName);
                return -1;
            }
            //打開文件
            PdfReader reader = null;
            try
            {
                reader = new PdfReader(fileName);
            }
            catch (Exception ex)
            {
                //LogHandler.LogWrite(string.Format(@"加載PDF文件{0}失敗,錯誤:{1}", new string[] { fileName, ex.ToString() }));

                if (reader != null)
                {
                    reader = null;
                }

                return -1;
            }
            //
            return reader.NumberOfPages;
        }

        string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename2 = string.Empty;
        bool success = false;

        private void button3_Click(object sender, EventArgs e)
        {
            filename2 = Path.GetDirectoryName(filename1) + "\\" + Path.GetFileNameWithoutExtension(filename1) + ".pdf";

            success = false;
            backgroundWorker1.RunWorkerAsync(new string[2] { filename1, filename2 });
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
                string filename2 = Application.StartupPath + "\\pdf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".pdf";

                PdfSharp.Pdf.PdfDocument doc = new PdfSharp.Pdf.PdfDocument();
                doc.Pages.Add(new PdfSharp.Pdf.PdfPage());
                XGraphics xgr = XGraphics.FromPdfPage(doc.Pages[0]);
                XImage img = XImage.FromFile(filename1);

                xgr.DrawImage(img, 0, 0);

                try
                {

                    doc.Save(filename2);
                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                doc.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

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

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_item_location2();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //讀取pdf檔至webbrowser

            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";
            webBrowser1.Navigate(filename);
        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            try
            {
                string source = (e.Argument as string[])[0];
                string destinaton = (e.Argument as string[])[1];

                PdfSharp.Pdf.PdfDocument doc = new PdfSharp.Pdf.PdfDocument();
                doc.Pages.Add(new PdfSharp.Pdf.PdfPage());
                XGraphics xgr = XGraphics.FromPdfPage(doc.Pages[0]);
                XImage img = XImage.FromFile(source);

                xgr.DrawImage(img, 0, 0);
                doc.Save(destinaton);
                doc.Close();
                success = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (success == true)
            {
                richTextBox1.Text += "圖片 : " + filename1 + "\n";
                richTextBox1.Text += "pdf :  " + filename2 + "\n";
                richTextBox1.Text += "轉換完成\n";
            }
        }
    }
}

