using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace TaskMessageWindow
{
    public partial class TaskMessageWindow : Form
    {
        public TaskMessageWindow()
        {
            InitializeComponent();
        }

        #region 声明的变量
        public static string MainFormTitle = "";//通知窗口的标题内容
        public static string MainFormContent = "";//通知窗口的文本内容
        MainForm InformWindow = new MainForm();  //实例化类MainForm的一个对象
        #endregion

        private void informButton_Click(object sender,EventArgs e)
        {
            MainForm.IconFlickerFlag = true;      //设置图标闪烁标识
            InformWindow.IconFlicker();          //调用闪烁图标方法
        }

        private void closeInform_Click(object sender,EventArgs e)
        {
            InformWindow.CloseNewWindow();       //关闭新显示的窗体
        }

        private void title_TextChanged(object sender,EventArgs e)
        {
            MainFormTitle = title.Text;          //记录通知的标题
        }

        private void content_TextChanged(object sender,EventArgs e)
        {
            MainFormContent = content.Text;      //记录通知的内容
        }
    }
}
