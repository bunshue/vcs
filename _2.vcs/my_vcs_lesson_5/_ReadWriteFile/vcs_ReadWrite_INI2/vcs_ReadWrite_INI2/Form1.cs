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
            filename = Application.StartupPath + "\\readwritetest.ini";		//INI文件的物理地址
            richTextBox1.Text += "filename = " + filename + "\n";
            strOne = System.IO.Path.GetFileNameWithoutExtension(filename); 		//獲取INI文件的文件名
            if (File.Exists(filename)) 						//判斷是否存在該INI文件
            {
                richTextBox1.Text += "第1項: " + ContentReader(strOne, "第1項", "") + "\n";			//讀取INI文件中的第1項
                richTextBox1.Text += "第2項: " + ContentReader(strOne, "第2項", "") + "\n";		    //讀取INI文件中的第2項
                richTextBox1.Text += "第3項: " + ContentReader(strOne, "第3項", "") + "\n";			//讀取INI文件中的第3項
                richTextBox1.Text += "第4項: " + ContentReader(strOne, "第4項", "") + "\n";			//讀取INI文件中的第4項

                textBox1.Text = ContentReader(strOne, "第1項", "");       //讀取INI文件中的第1項
                textBox2.Text = ContentReader(strOne, "第2項", "");       //讀取INI文件中的第2項
                textBox3.Text = ContentReader(strOne, "第3項", "");       //讀取INI文件中的第3項
                textBox4.Text = ContentReader(strOne, "第4項", "");       //讀取INI文件中的第4項
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            filename = Application.StartupPath + "\\readwritetest2.ini";		//INI文件的物理地址
            //if (File.Exists(filename))											//判断是否存在INI文件
            {
                WritePrivateProfileString(strOne, "第1項", textBox1.Text, filename); 		    //修改INI文件中的第1項
                WritePrivateProfileString(strOne, "第2項", textBox2.Text, filename); 		    //修改INI文件中的第2項
                WritePrivateProfileString(strOne, "第3項", textBox3.Text, filename); 			//修改INI文件中的第3項
                WritePrivateProfileString(strOne, "第4項", textBox4.Text, filename); 			//修改INI文件中的第4項
                richTextBox1.Text += "修改成功\n";
            }
            //else
            {
                //MessageBox.Show("对不起，你所要修改的文件不存在，请确认后再进行修改操作！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }

        }
    }
}
