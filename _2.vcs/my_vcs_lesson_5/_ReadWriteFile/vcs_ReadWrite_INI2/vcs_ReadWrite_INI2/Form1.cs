using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport
using System.IO;

namespace vcs_ReadWrite_INI2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string filename = "";//該變量保存INI文件所在的具体物理位置
        string strOne = "";

        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(
            string lpAppName,
            string lpKeyName,
            string lpDefault,
            StringBuilder lpReturnedString,
            int nSize,
            string lpFileName);

        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(
            string mpAppName,
            string mpKeyName,
            string mpDefault,
            string mpFileName);

        public string ContentReader(string area, string key, string def)
        {
            StringBuilder stringBuilder = new StringBuilder(1024); 				//定义一个最大长度为1024的可变字符串
            GetPrivateProfileString(area, key, def, stringBuilder, 1024, filename); 			//读取INI文件
            return stringBuilder.ToString();								//返回INI文件的内容
        }

        private void button1_Click(object sender, EventArgs e)
        {
            filename = Application.StartupPath + "\\ConnectString.ini";		//INI文件的物理地址
            richTextBox1.Text += "filename = " + filename + "\n";
            strOne = System.IO.Path.GetFileNameWithoutExtension(filename); 		//獲取INI文件的文件名
            if (File.Exists(filename)) 						//判斷是否存在該INI文件
            {
                richTextBox1.Text += "服務器: " + ContentReader(strOne, "Data Source", "") + "\n";			//讀取INI文件中服務器節點的內容
                richTextBox1.Text += "數據庫: " + ContentReader(strOne, "DataBase", "") + "\n";			    //讀取INI文件中數據庫節點的內容
                richTextBox1.Text += "登錄身份: " + ContentReader(strOne, "Uid", "") + "\n";				//讀取INI文件中用戶節點的內容
                richTextBox1.Text += "登錄密碼: " + ContentReader(strOne, "Pwd", "") + "\n";				//讀取INI文件中密碼節點的內容

                textBox1.Text = ContentReader(strOne, "Data Source", "");			//讀取INI文件中服務器節點的內容
                textBox2.Text = ContentReader(strOne, "DataBase", "");			    //讀取INI文件中數據庫節點的內容
                textBox3.Text = ContentReader(strOne, "Uid", "");   				//讀取INI文件中用戶節點的內容
                textBox4.Text = ContentReader(strOne, "Pwd", "");	    			//讀取INI文件中密碼節點的內容
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            filename = Application.StartupPath + "\\ConnectString2.ini";		//INI文件的物理地址
            //if (File.Exists(filename))											//判断是否存在INI文件
            {
                WritePrivateProfileString(strOne, "Data Source", textBox1.Text, filename); 		//修改INI文件中服务器节点的内容
                WritePrivateProfileString(strOne, "DataBase", textBox2.Text, filename); 		//修改INI文件中数据库节点的内容
                WritePrivateProfileString(strOne, "Uid", textBox3.Text, filename); 			//修改INI文件中用户节点的内容
                WritePrivateProfileString(strOne, "Pwd", textBox4.Text, filename); 			//修改INI文件中密码节点的内容
                MessageBox.Show("恭喜你，修改成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            //else
            {
                //MessageBox.Show("对不起，你所要修改的文件不存在，请确认后再进行修改操作！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        }
    }
}
