using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;

using Word = Microsoft.Office.Interop.Word;
using Microsoft.Office.Interop.Word;

namespace vcs_ReadWrite_WORD6_Replace
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string filename1 = string.Empty;
        string filename2 = string.Empty;

        private Word.Application G_WordApplication;//定義Word應用程序字段

        //定義G_Missing字段并添加引用
        private object G_Missing = System.Reflection.Missing.Value;

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
            //Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            filename1 = Path.GetFullPath(Path.Combine(System.Windows.Forms.Application.StartupPath, @"..\..")) + @"\Step.doc";
            filename2 = System.Windows.Forms.Application.StartupPath + "\\test_word_file.doc";

            if (File.Exists(filename1) == false)    //確認原始檔案是否存在
            {
                richTextBox1.Text += "原始檔案: " + filename1 + " 不存在, 無法拷貝\n";
            }

            if (File.Exists(filename2) == true)    //確認原始檔案是否存在
            {
                File.Delete(filename2);
                richTextBox1.Text += "檔案: " + filename2 + " 存在, 已刪除\n";
            }

            if (File.Exists(filename2) == false)    //確認目標檔案是否存在
            {
                // Copy the file.
                File.Copy(filename1, filename2);
                richTextBox1.Text += "目標檔案: " + filename2 + " 不存在, 已拷貝\n";
            }

            txt_path.Text = filename2;
            txt_Find.ReadOnly = false;//取消文本框的只讀狀態
            txt_Replace.ReadOnly = false;//取消文本框的只讀狀態
            btn_Begin.Enabled = true;//啟用開始替換按鈕
            btn_Display.Enabled = true;//啟用顯示文件按鈕
        }

        private void txt_Find_TextChanged(object sender, EventArgs e)
        {
        }

        private void txt_Replace_TextChanged(object sender, EventArgs e)
        {
        }

        private void btn_Begin_Click(object sender, EventArgs e)
        {
            btn_Begin.Enabled = false;//停用替換按鈕
            ThreadPool.QueueUserWorkItem(//開始線程池
                (o) =>//使用Lambda表達式
                {
                    //創建Word應用程序對象
                    G_WordApplication = new Microsoft.Office.Interop.Word.Application();
                    object P_FilePath = filename2;//創建Object對象
                    richTextBox1.Text += "開啟檔案 :\t" + P_FilePath + "\n";
                    Word.Document P_Document = G_WordApplication.Documents.Open(//打開Word文檔
                        ref P_FilePath, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing);
                    Word.Range P_Range = //得到文檔范圍
                        P_Document.Range(ref G_Missing, ref G_Missing);
                    Word.Find P_Find = //得到Find對象
                        P_Range.Find;
                    this.Invoke(//在窗體線程中執行
                        (MethodInvoker)(() =>//使用Lambda表達式
                        {
                            P_Find.Text = txt_Find.Text;//設置查找的文本
                            P_Find.Replacement.Text = txt_Replace.Text;//設置替換的文本
                        }));
                    object P_Replace = Word.WdReplace.wdReplaceAll;//定義替換方式對象
                    bool P_bl = P_Find.Execute(//開始替換
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref P_Replace,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref G_Missing);
                    G_WordApplication.Documents.Save(//保存文檔
                        ref G_Missing, ref G_Missing);
                    ((Word._Document)P_Document).Close(//關閉文檔
                        ref G_Missing, ref G_Missing, ref G_Missing);
                    ((Word._Application)G_WordApplication).Quit(//退出Word應用程序
                        ref G_Missing, ref G_Missing, ref G_Missing);
                    this.Invoke(//在窗體線程中執行
                        (MethodInvoker)(() =>//使用Lambda表達式
                        {
                            if (P_bl)//查看是否找到并替換
                            {
                                MessageBox.Show("找到字符串并替換", "提示！");
                            }
                            else
                            {
                                MessageBox.Show("沒有找到字符串", "提示！");
                            }
                            btn_Begin.Enabled = true;//啟用開始替換按鈕
                        }));
                });
        }

        private void btn_Display_Click(object sender, EventArgs e)
        {
            ThreadPool.QueueUserWorkItem(//開始線程池
                (o) =>//使用Lambda表達式
                {
                    G_WordApplication =//創建Word應用程序對象
                         new Microsoft.Office.Interop.Word.Application();
                    G_WordApplication.Visible = true;//Word應用程序可在桌面顯示
                    object P_FilePath = filename2;//得到文件路徑信息
                    Word.Document P_Document = G_WordApplication.Documents.Open(//打開文件
                        ref P_FilePath, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing);
                    this.Invoke(//在窗體線程中執行
                        (MethodInvoker)(() =>
                        {
                            btn_Display.Enabled = true;//啟用顯示文件按鈕
                        }));
                });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CreateDocument();
        }

        //Create document method  
        private void CreateDocument()
        {
            //Create an instance for word app  
            Microsoft.Office.Interop.Word.Application winword = new Microsoft.Office.Interop.Word.Application();

            //Set animation status for word application  
            winword.ShowAnimation = false;

            //Set status for word application is to be visible or not.  
            winword.Visible = false;

            //Create a missing variable for missing value  
            object missing = System.Reflection.Missing.Value;

            //Create a new document  
            Microsoft.Office.Interop.Word.Document document = winword.Documents.Add(ref missing, ref missing, ref missing, ref missing);

            //頁邊距
            document.PageSetup.LeftMargin = 40; //1.41CM
            document.PageSetup.RightMargin = 40;
            document.PageSetup.TopMargin = 40;
            document.PageSetup.BottomMargin = 40;

            //頁眉 //Add header into the document
            foreach (Microsoft.Office.Interop.Word.Section section in document.Sections)
            {
                //Get the header range and add the header details.
                Microsoft.Office.Interop.Word.Range headerRange = section.Headers[Microsoft.Office.Interop.Word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range;
                headerRange.Fields.Add(headerRange, Microsoft.Office.Interop.Word.WdFieldType.wdFieldPage);
                headerRange.ParagraphFormat.Alignment = Microsoft.Office.Interop.Word.WdParagraphAlignment.wdAlignParagraphCenter;
                headerRange.Font.ColorIndex = Microsoft.Office.Interop.Word.WdColorIndex.wdBlue;
                headerRange.Font.Size = 10;
                headerRange.Text = "Header text goes here";
            }

            //頁腳 Add the footers into the document
            foreach (Microsoft.Office.Interop.Word.Section wordSection in document.Sections)
            {
                //Get the footer range and add the footer details.  
                Microsoft.Office.Interop.Word.Range footerRange = wordSection.Footers[Microsoft.Office.Interop.Word.WdHeaderFooterIndex.wdHeaderFooterPrimary].Range;
                footerRange.Font.ColorIndex = Microsoft.Office.Interop.Word.WdColorIndex.wdDarkRed;
                footerRange.Font.Size = 10;
                footerRange.ParagraphFormat.Alignment = Microsoft.Office.Interop.Word.WdParagraphAlignment.wdAlignParagraphCenter;
                footerRange.Text = "Footer text goes here";
            }

            //添加內容 adding text to document
            document.Content.SetRange(0, 0);
            document.Content.Text = "檢測報告 " + Environment.NewLine;

            //添加段落 Add paragraph with Heading 1 style
            Microsoft.Office.Interop.Word.Paragraph para1 = document.Content.Paragraphs.Add(ref missing);
            para1.Range.Text = "Para 1 text";
            para1.Range.InsertParagraphAfter();

            //Add paragraph with Heading 2 style  
            Microsoft.Office.Interop.Word.Paragraph para2 = document.Content.Paragraphs.Add(ref missing);
            para2.Range.Text = "Para 2 text";
            para2.Range.InsertParagraphAfter();

            //表格 Create a 5X5 table and insert some dummy record
            Table firstTable = document.Tables.Add(para1.Range, 5, 5, ref missing, ref missing);

            firstTable.Borders.Enable = 1;
            foreach (Row row in firstTable.Rows)
            {
                foreach (Cell cell in row.Cells)
                {
                    //表頭 Header row
                    if (cell.RowIndex == 1)
                    {
                        cell.Range.Text = "Column " + cell.ColumnIndex.ToString();
                        cell.Range.Font.Bold = 1;
                        //other format properties goes here  
                        cell.Range.Font.Name = "verdana";
                        cell.Range.Font.Size = 10;
                        //cell.Range.Font.ColorIndex = WdColorIndex.wdGray25;                              
                        cell.Shading.BackgroundPatternColor = WdColor.wdColorGray25;
                        //Center alignment for the Header cells  
                        cell.VerticalAlignment = WdCellVerticalAlignment.wdCellAlignVerticalCenter;
                        cell.Range.ParagraphFormat.Alignment = WdParagraphAlignment.wdAlignParagraphCenter;
                    }
                    //行 Data row
                    else
                    {
                        cell.Range.Text = (cell.RowIndex - 2 + cell.ColumnIndex).ToString();
                    }
                }

                try
                {
                    //保存
                    string filename = System.Windows.Forms.Application.StartupPath + "\\docx_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".docx";

                    document.SaveAs(filename);
                    document.Close(ref missing, ref missing, ref missing);
                    document = null;

                    winword.Quit(ref missing, ref missing, ref missing);
                    winword = null;
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }
    }
}