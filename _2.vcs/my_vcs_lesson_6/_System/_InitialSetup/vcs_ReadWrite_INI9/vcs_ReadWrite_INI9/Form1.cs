using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_INI9
{
    public partial class Form1 : Form
    {
        string ini_filename = @"../../config.ini";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "filename = " + ini_filename + "\n";
            readIniFile();
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
    }
}

