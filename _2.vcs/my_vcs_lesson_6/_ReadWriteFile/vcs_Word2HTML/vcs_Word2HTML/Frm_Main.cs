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

namespace vcs_Word2HTML
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private Word.Application G_wa;//定义Word应用程序字段
        private object G_missing = //定义G_missing字段并添加引用
            System.Reflection.Missing.Value;
        private object G_FilePath;//定义文档路径字段

        private void btn_Open_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_word\Step.doc";

            btn_New.Enabled = false;//停用新建按钮
            btn_Open.Enabled = false;//停用打开按钮
            G_FilePath = filename;
            ThreadPool.QueueUserWorkItem(//开始线程池
                (pp) =>//使用Lambda表达式
                {
                    G_wa = //创建应用程序对象
                         new Microsoft.Office.Interop.Word.Application();
                    G_wa.Visible = true;//将文档设置为可见
                    Word.Document P_Document = G_wa.Documents.Open(//打开Word文档
                       ref G_FilePath, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                       ref G_missing, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                       ref G_missing, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                       ref G_missing);
                    this.Invoke(//窗体线程
                        (MethodInvoker)(() =>//使用Lambda表达式
                        {
                            btn_SaveAs.Enabled = true;//启用转换按钮
                        }));
                });


        }

        private void btn_New_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\doc_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".doc";

            btn_New.Enabled = false;//停用新建按钮
            btn_Open.Enabled = false;//停用打开按钮

            //if (P_DialogResult == DialogResult.OK)//判断是否确认选择文件夹
            {
                G_FilePath = filename;

                /*
                G_FilePath = string.Format(//计算文件保存路径
                    @"{0}\{1}", P_FolderBrowserDialog.SelectedPath,
                    DateTime.Now.ToString("yyyy年M月d日h时m分s秒fff毫秒") + ".doc");
                */

                ThreadPool.QueueUserWorkItem(//开始线程池
                    (pp) =>//使用lambda表达式
                    {
                        G_wa = new Microsoft.Office.Interop.Word.Application();//创建应用程序对象
                        G_wa.Visible = true;//将文档设置为可见
                        object P_obj = "Normal.dot";//定义文档模板
                        Word.Document P_wd = G_wa.Documents.Add(//向Word应用程序中添加文档
                            ref P_obj, ref G_missing, ref G_missing, ref G_missing);
                        P_wd.SaveAs(//保存Word文件
                            ref G_FilePath,
                            ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing);
                        this.Invoke(//窗体线程
                            (MethodInvoker)(() =>//使用Lambda表达式
                            {
                                btn_SaveAs.Enabled = true;//启用转换按钮
                            }));
                    });
            }
        }

        private void btn_SaveAs_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";

            btn_SaveAs.Enabled = false;//停用转换按钮
            try
            {
                G_wa.ActiveDocument.Save();//保存文档
                ((Word._Application)G_wa.Application).Quit(//退出应用程序
                  ref G_missing, ref G_missing, ref G_missing);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            //if (P_DialogResult == DialogResult.OK)//判断是否确认保存文件
            {
                object P_str_path = filename;
                ThreadPool.QueueUserWorkItem(//开始线程澉
                    (pp) =>//使用Lambda表达式
                    {
                        G_wa = //创建应用程序对象
                          new Microsoft.Office.Interop.Word.Application();
                        G_wa.Visible = false;
                        Word.Document P_wd = G_wa.Documents.Open(//打开Word文档
                           ref G_FilePath, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                           ref G_missing, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                           ref G_missing, ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                           ref G_missing);
                        object P_Format = Word.WdSaveFormat.wdFormatHTML;//创建保存文档参数
                        P_wd.SaveAs(//保存Word文件
                            ref P_str_path,
                            ref P_Format, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing, ref G_missing,
                            ref G_missing, ref G_missing, ref G_missing);
                        ((Word._Application)G_wa.Application).Quit(//退出应用程序
                            ref G_missing, ref G_missing, ref G_missing);
                        this.Invoke(//调用窗体线程
                            (MethodInvoker)(() =>//使用lambda表达式
                            {
                                btn_Open.Enabled = true;//启用打开按钮
                                btn_New.Enabled = true;//启用新建按钮
                                MessageBox.Show(//提示已经创建Word
                                    "文件已经创建", "提示！");
                            }));
                    });
            }
        }
    }
}
