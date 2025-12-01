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

namespace vcs_ReadWrite_INI9
{
    public partial class Form1 : Form
    {
        string ini_filename = @"../../config.ini";

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool WritePrivateProfileString(string lpAppName, string lpKeyName, string lpString, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileString(string lpAppName, string lpKeyName, string lpDefault, StringBuilder lpReturnedString, int nSize, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileInt(string lpAppName, string lpKeyName, int lpDefault, string lpFileName);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "filename = " + ini_filename + "\n";
            readIniFile();
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

            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(960, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        /// <summary>
        /// 读取ini文件信息
        /// </summary>
        private void readIniFile()
        {
            if (File.Exists(this.ini_filename))
            {
                this.webAddresTxt.Text = IniFileHelper.GetValue("Web信息", "Web地址", this.ini_filename);
                this.webLoginNameTxt.Text = IniFileHelper.GetValue("Web信息", "用户名", this.ini_filename);
                this.webPwdTxt.Text = IniFileHelper.GetValue("Web信息", "密码", this.ini_filename);
                this.ftpAddressTxt.Text = IniFileHelper.GetValue("FTPInfo", "address", this.ini_filename);
                this.ftpLoginNameTxt.Text = IniFileHelper.GetValue("FTPInfo", "loginName", this.ini_filename);
                this.ftpPwdTxt.Text = IniFileHelper.GetValue("FTPInfo", "pwd", this.ini_filename);
                MessageBox.Show("读取文档成功");
            }
            else
            {
                MessageBox.Show("文件加载失败，请确认是否存在此文件：" + this.ini_filename);
            }
        }

        /// <summary>
        /// 储存ini文件信息
        /// </summary>
        private void saveIniFile()
        {
            if (!File.Exists(this.ini_filename))
            {
                using (File.Create(this.ini_filename)) { };
            }

            IniFileHelper.SetValue("Web信息", "Web地址", this.webAddresTxt.Text, this.ini_filename);
            IniFileHelper.SetValue("Web信息", "用户名", this.webLoginNameTxt.Text, this.ini_filename);
            IniFileHelper.SetValue("Web信息", "密码", this.webPwdTxt.Text, this.ini_filename);
            IniFileHelper.SetValue("FTPInfo", "address", this.ftpAddressTxt.Text, this.ini_filename);
            IniFileHelper.SetValue("FTPInfo", "loginName", this.ftpLoginNameTxt.Text, this.ini_filename);
            IniFileHelper.SetValue("FTPInfo", "pwd", this.ftpPwdTxt.Text, this.ini_filename);
            MessageBox.Show("存储成功");
        }

        // 【读取ini】
        private void readBtn_Click(object sender, EventArgs e)
        {
            readIniFile();
        }

        // 【保存ini】
        private void saveBtn_Click(object sender, EventArgs e)
        {
            saveIniFile();
        }

        // 【移除section】
        private void removeSectionBtn_Click(object sender, EventArgs e)
        {
            bool rs = IniFileHelper.RemoveSection("Web信息", this.ini_filename);
            if (rs)
            {
                MessageBox.Show("移除section成功");
            }
            else
            {
                MessageBox.Show("移除section失败");
            }
        }

        // 【移除key】
        private void removeKeyBtn_Click(object sender, EventArgs e)
        {
            bool rs = IniFileHelper.Removekey("Web信息", "密码", this.ini_filename);
            if (rs)
            {
                MessageBox.Show("移除key成功");
            }
            else
            {
                MessageBox.Show("移除key失败");
            }
        }

        // 【获取所有section】
        private void getAllSectionBtn_Click(object sender, EventArgs e)
        {
            List<string> rs = IniFileHelper.GetSectionNames(this.ini_filename);
            MessageBox.Show(string.Join(",", rs));
        }

        // 【获取所有key】
        private void getAllKeyBtn_Click(object sender, EventArgs e)
        {
            List<string> rs = IniFileHelper.GetKeys("Web信息", this.ini_filename);
            MessageBox.Show(string.Join(",", rs));
        }


        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"./tmp_config.ini";
            richTextBox1.Text += "Write ini data to " + filename + "\n";

            string section_name = "AnimalInfo0";
            string animal_cname = "鼠";
            string animal_ename = "mouse";
            int weight = 3;
            string address = @"C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\unittest\main.py";
            WritePrivateProfileString(section_name, "cname", animal_cname, filename);
            WritePrivateProfileString(section_name, "ename", animal_ename, filename);
            WritePrivateProfileString(section_name, "weight", weight.ToString(), filename);
            WritePrivateProfileString(section_name, "address", address, filename);

            section_name = "AnimalInfo1";
            animal_cname = "牛";
            animal_ename = "ox";
            weight = 48;
            address = "D:/.../.../.../.../.../folder/ABCD.EFG";
            WritePrivateProfileString(section_name, "cname", animal_cname, filename);
            WritePrivateProfileString(section_name, "ename", animal_ename, filename);
            WritePrivateProfileString(section_name, "weight", weight.ToString(), filename);
            WritePrivateProfileString(section_name, "address", address, filename);
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
            StringBuilder temp = new StringBuilder(1024);//定義一個最大長度為1024的可變字符串

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
            parameter_name = "address";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";

            string parameter_name1 = "cname";
            string parameter_name2 = "ename";
            string parameter_name3 = "weight";
            string parameter_name4 = "address";
            richTextBox1.Text += "第1項: " + ContentReader(section_name, parameter_name1, "", filename) + "\n";			//讀取INI文件中的第1項
            richTextBox1.Text += "第2項: " + ContentReader(section_name, parameter_name2, "", filename) + "\n";		    //讀取INI文件中的第2項
            richTextBox1.Text += "第3項: " + ContentReader(section_name, parameter_name3, "", filename) + "\n";			//讀取INI文件中的第3項
            richTextBox1.Text += "第4項: " + ContentReader(section_name, parameter_name4, "", filename) + "\n";			//讀取INI文件中的第4項

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
            parameter_name = "address";
            GetPrivateProfileString(section_name, parameter_name, "", temp, 255, filename);
            richTextBox1.Text += "取得資料 : " + temp + "\n";

            parameter_name1 = "cname";
            parameter_name2 = "ename";
            parameter_name3 = "weight";
            parameter_name4 = "address";
            richTextBox1.Text += "第1項: " + ContentReader(section_name, parameter_name1, "", filename) + "\n";			//讀取INI文件中的第1項
            richTextBox1.Text += "第2項: " + ContentReader(section_name, parameter_name2, "", filename) + "\n";		    //讀取INI文件中的第2項
            richTextBox1.Text += "第3項: " + ContentReader(section_name, parameter_name3, "", filename) + "\n";			//讀取INI文件中的第3項
            richTextBox1.Text += "第4項: " + ContentReader(section_name, parameter_name4, "", filename) + "\n";			//讀取INI文件中的第4項
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

