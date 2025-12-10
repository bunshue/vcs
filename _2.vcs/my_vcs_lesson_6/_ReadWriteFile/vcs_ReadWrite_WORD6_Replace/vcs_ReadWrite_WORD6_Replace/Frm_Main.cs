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

            filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\Step.doc";
            filename2 = "tmp_test_word_file.doc";

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
    }
}
