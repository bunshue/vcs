using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using Word = Microsoft.Office.Interop.Word;

namespace WordReplace
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        string filename = @"C:\______test_files\__RW\_word\Step.doc";

        private Word.Application G_WordApplication;//定义Word应用程序字段

        //定义G_Missing字段并添加引用
        private object G_Missing = System.Reflection.Missing.Value;

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            txt_path.Text = filename;
            txt_Find.ReadOnly = false;//取消文本框的只读状态
            txt_Replace.ReadOnly = false;//取消文本框的只读状态
            btn_Begin.Enabled = true;//启用开始替换按钮
            btn_Display.Enabled = true;//启用显示文件按钮
        }

        private void txt_Find_TextChanged(object sender, EventArgs e)
        {
        }

        private void txt_Replace_TextChanged(object sender, EventArgs e)
        {
        }

        private void btn_Begin_Click(object sender, EventArgs e)
        {
            btn_Begin.Enabled = false;//停用替换按钮
            ThreadPool.QueueUserWorkItem(//开始线程池
                (o) =>//使用Lambda表达式
                {
                    G_WordApplication =//创建Word应用程序对象
                         new Microsoft.Office.Interop.Word.Application();
                    object P_FilePath = filename;//创建Object对象
                    Word.Document P_Document = G_WordApplication.Documents.Open(//打开Word文档
                        ref P_FilePath, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing);
                    Word.Range P_Range = //得到文档范围
                        P_Document.Range(ref G_Missing, ref G_Missing);
                    Word.Find P_Find = //得到Find对象
                        P_Range.Find;
                    this.Invoke(//在窗体线程中执行
                        (MethodInvoker)(() =>//使用Lambda表达式
                        {
                            P_Find.Text = txt_Find.Text;//设置查找的文本
                            P_Find.Replacement.Text = txt_Replace.Text;//设置替换的文本
                        }));
                    object P_Replace = Word.WdReplace.wdReplaceAll;//定义替换方式对象
                    bool P_bl = P_Find.Execute(//开始替换
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref P_Replace,
                        ref G_Missing, ref G_Missing, ref G_Missing, ref G_Missing);
                    G_WordApplication.Documents.Save(//保存文档
                        ref G_Missing, ref G_Missing);
                    ((Word._Document)P_Document).Close(//关闭文档
                        ref G_Missing, ref G_Missing, ref G_Missing);
                    ((Word._Application)G_WordApplication).Quit(//退出Word应用程序
                        ref G_Missing, ref G_Missing, ref G_Missing);
                    this.Invoke(//在窗体线程中执行
                        (MethodInvoker)(() =>//使用Lambda表达式
                        {
                            if (P_bl)//查看是否找到并替换
                            {
                                MessageBox.Show(//弹出消息对话框
                                    "找到字符串并替换", "提示！");
                            }
                            else
                            {
                                MessageBox.Show(//弹出消息对话框
                                    "没有找到字符串", "提示！");
                            }
                            btn_Begin.Enabled = true;//启用开始替换按钮
                        }));
                });
        }

        private void btn_Display_Click(object sender, EventArgs e)
        {
            ThreadPool.QueueUserWorkItem(//开始线程池
                (o) =>//使用Lambda表达式
                {
                    G_WordApplication =//创建Word应用程序对象
                         new Microsoft.Office.Interop.Word.Application();
                    G_WordApplication.Visible = true;//Word应用程序可在桌面显示
                    object P_FilePath = filename;//得到文件路径信息
                    Word.Document P_Document = G_WordApplication.Documents.Open(//打开文件
                        ref P_FilePath, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing, ref G_Missing, ref G_Missing,
                        ref G_Missing);
                    this.Invoke(//在窗体线程中执行
                        (MethodInvoker)(() =>
                        {
                            btn_Display.Enabled = true;//启用显示文件按钮
                        }));
                });
        }

    }
}
