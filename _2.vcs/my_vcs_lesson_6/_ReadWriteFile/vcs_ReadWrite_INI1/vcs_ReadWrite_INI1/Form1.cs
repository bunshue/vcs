using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INI1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool WritePrivateProfileString(string lpAppName, string lpKeyName, string lpString, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileString(string lpAppName, string lpKeyName, string lpDefault, StringBuilder lpReturnedString, int nSize, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileInt(string lpAppName, string lpKeyName, int lpDefault, string lpFileName);

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"./tmp_config.ini";
            richTextBox1.Text += "Write ini data to " + filename + "\n";

            string section_name = "AnimalInfo0";
            string animal_cname = "鼠";
            string animal_ename = "mouse";
            int weight = 3;
            WritePrivateProfileString(section_name, "cname", animal_cname, filename);
            WritePrivateProfileString(section_name, "ename", animal_ename, filename);
            WritePrivateProfileString(section_name, "weight", weight.ToString(), filename);

            section_name = "AnimalInfo1";
            animal_cname = "牛";
            animal_ename = "ox";
            weight = 48;
            WritePrivateProfileString(section_name, "cname", animal_cname, filename);
            WritePrivateProfileString(section_name, "ename", animal_ename, filename);
            WritePrivateProfileString(section_name, "weight", weight.ToString(), filename);
        }

        public string ContentReader(string area, string key, string def, string filename)
        {
            StringBuilder stringBuilder = new StringBuilder(1024); 				//定义一个最大长度为1024的可变字符串
            GetPrivateProfileString(area, key, def, stringBuilder, 1024, filename); 			//读取INI文件
            return stringBuilder.ToString();								//返回INI文件的内容
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"./tmp_config.ini";
            richTextBox1.Text += "Read ini data from " + filename + "\n";
            StringBuilder temp = new StringBuilder();

            string section_name = "AnimalInfo0";

            string parameter_name = "cname";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";
            parameter_name = "ename";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";
            parameter_name = "weight";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";

            string parameter_name1 = "cname";
            string parameter_name2 = "ename";
            string parameter_name3 = "weight";
            richTextBox1.Text += "第1項: " + ContentReader(section_name, parameter_name1, "", filename) + "\n";			//讀取INI文件中的第1項
            richTextBox1.Text += "第2項: " + ContentReader(section_name, parameter_name2, "", filename) + "\n";		    //讀取INI文件中的第2項
            richTextBox1.Text += "第3項: " + ContentReader(section_name, parameter_name3, "", filename) + "\n";			//讀取INI文件中的第3項


            section_name = "AnimalInfo1";

            parameter_name = "cname";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";
            parameter_name = "ename";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";
            parameter_name = "weight";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";

            parameter_name1 = "cname";
            parameter_name2 = "ename";
            parameter_name3 = "weight";
            richTextBox1.Text += "第1項: " + ContentReader(section_name, parameter_name1, "", filename) + "\n";			//讀取INI文件中的第1項
            richTextBox1.Text += "第2項: " + ContentReader(section_name, parameter_name2, "", filename) + "\n";		    //讀取INI文件中的第2項
            richTextBox1.Text += "第3項: " + ContentReader(section_name, parameter_name3, "", filename) + "\n";			//讀取INI文件中的第3項
        }

        /// <summary>
        /// 取得 Key 相對的 Value 值，若沒有則使用預設值(DefaultValue)。
        /// </summary>
        /// <param name="Section">Section。</param>
        /// <param name="Key">Key。</param>
        /// <param name="DefaultValue">DefaultValue。</param>        
        public string getKeyValue(string Section, string Key, string DefaultValue, string filename)
        {
            StringBuilder sbResult = null;
            try
            {
                sbResult = new StringBuilder(255);
                GetPrivateProfileString(Section, Key, "", sbResult, 255, filename);
                return (sbResult.Length > 0) ? sbResult.ToString() : DefaultValue;
            }
            catch
            {
                return string.Empty;
            }
        }

        /// <summary>
        /// 移除指定的section
        /// </summary>
        /// <param name="sectionName">section名称</param>
        /// <param name="filePath">文件路径</param>
        /// <returns></returns>
        public static bool RemoveSection(string sectionName, string filePath)
        {
            try
            {
                bool rs = WritePrivateProfileString(sectionName, null, "", filePath);
                return rs;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }

        /// <summary>
        /// 移除指定的key
        /// </summary>
        /// <param name="sectionName">section名称</param>
        /// <param name="filePath">文件路径</param>
        /// <returns></returns>
        public static bool Removekey(string sectionName, string key, string filePath)
        {
            try
            {
                bool rs = WritePrivateProfileString(sectionName, key, null, filePath);
                return rs;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }


        private void button3_Click(object sender, EventArgs e)
        {
            //移除指定的section
            string filename = @"./tmp_config.ini";

            string section_name = "AnimalInfo1";

            bool rs = RemoveSection(section_name, filename);
            richTextBox1.Text += "移除section完成\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //移除key
            string filename = @"./tmp_config.ini";

            string section_name = "AnimalInfo0";
            string parameter_name2 = "ename";

            bool rs = Removekey(section_name, parameter_name2, filename);
            richTextBox1.Text += "移除key完成\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }
    }
}
