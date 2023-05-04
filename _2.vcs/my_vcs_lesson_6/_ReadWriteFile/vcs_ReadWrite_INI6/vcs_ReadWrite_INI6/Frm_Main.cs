using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INI6
{
    public partial class Frm_Main : Form
    {
        #region 变量声明区
        public string filename = @"C:\______test_files1\__RW\_ini\ConnectString.ini";    //该变量保存INI文件所在的具体物理位置
        public string strOne = "";
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(
            string lpAppName,
            string lpKeyName,
            string lpDefault,
            StringBuilder lpReturnedString,
            int nSize,
            string lpFileName);

        public string ContentReader(string area, string key, string def)
        {
            StringBuilder stringBuilder = new StringBuilder(1024); 				//定义一个最大长度为1024的可变字符串
            GetPrivateProfileString(area, key, def, stringBuilder, 1024, filename); 			//读取INI文件
            return stringBuilder.ToString();								//返回INI文件的内容
        }

        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(
            string mpAppName,
            string mpKeyName,
            string mpDefault,
            string mpFileName);

        #endregion

        public Frm_Main()
        {
            InitializeComponent();
        }
        #region 窗体加载部分
        private void Form1_Load(object sender, EventArgs e)
        {
            strOne = System.IO.Path.GetFileNameWithoutExtension(filename); 				//获取INI文件的文件名
            if (File.Exists(filename)) 											//判断是否存在该INI文件
            {
                server.Text = ContentReader(strOne, "Data Source", "");				//读取INI文件中服务器节点的内容
                database.Text = ContentReader(strOne, "DataBase", "");				//读取INI文件中数据库节点的内容
                uid.Text = ContentReader(strOne, "Uid", "");						//读取INI文件中用户节点的内容
                pwd.Text = ContentReader(strOne, "Pwd", "");						//读取INI文件中密码节点的内容
            }
        }
        #endregion

        #region 进行修改操作
        private void button1_Click(object sender, EventArgs e)
        {
            if (File.Exists(filename))											//判断是否存在INI文件
            {
                WritePrivateProfileString(strOne, "Data Source", server.Text, filename); 		//修改INI文件中服务器节点的内容
                WritePrivateProfileString(strOne, "DataBase", database.Text, filename); 		//修改INI文件中数据库节点的内容
                WritePrivateProfileString(strOne, "Uid", uid.Text, filename); 			//修改INI文件中用户节点的内容
                WritePrivateProfileString(strOne, "Pwd", pwd.Text, filename); 			//修改INI文件中密码节点的内容
                MessageBox.Show("恭喜你，修改成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("对不起，你所要修改的文件不存在，请确认后再进行修改操作！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
        #endregion
    }
}
