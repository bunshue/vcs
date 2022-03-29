using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INIA
{
    public partial class Form1 : Form
    {
        public string path;				//INI文件名

        #region 修改INI文件中内容
        /// <summary>
        /// 修改INI文件中内容
        /// </summary>
        /// <param name="section">欲在其中写入的节点名称</param>
        /// <param name="key">欲设置的项名</param>
        /// <param name="val">要写入的新字符串</param>
        /// <param name="filePath">INI文件名</param>
        /// <returns>非零表示成功，零表示失败</returns>
        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        #endregion

        #region 为INI文件中指定的节点取得字符串
        /// <summary>
        /// 为INI文件中指定的节点取得字符串
        /// </summary>
        /// <param name="section">欲在其中查找关键字的节点名称</param>
        /// <param name="key">欲获取的项名</param>
        /// <param name="def">指定的项没有找到时返回的默认值</param>
        /// <param name="retVal">指定一个字串缓冲区，长度至少为nSize</param>
        /// <param name="size">指定装载到lpReturnedString缓冲区的最大字符数量</param>
        /// <param name="filePath">INI文件名</param>
        /// <returns>复制到lpReturnedString缓冲区的字节数量，其中不包括那些NULL中止字符</returns>
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);
        #endregion

        #region 向INI文件中写入内容
        /// <summary>
        /// 向INI文件中写入内容
        /// </summary>
        /// <param name="Section">节点名称</param>
        /// <param name="Key">项名</param>
        /// <param name="Value">要写入项的内容</param>
        public void IniWriteValue(string Section, string Key, string Value)
        {
            WritePrivateProfileString(Section, Key, Value, this.path);
        }
        #endregion

        #region 读取INI文件内容
        /// <summary>
        /// 读取INI文件内容
        /// </summary>
        /// <param name="Section">节点名称</param>
        /// <param name="Key">项名</param>
        /// <returns>返回INI项的内容</returns>
        public string IniReadValue(string Section, string Key)
        {
            StringBuilder temp = new StringBuilder(255);
            int i = GetPrivateProfileString(Section, Key, "", temp, 255, this.path);
            return temp.ToString();
        }
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            int i = 10;
            IniWriteValue("xiaoke", "dispaly", "1");
            IniWriteValue("xiaoke", "dispaly", "0");

            IniWriteValue("xiaoke", "direction", i.ToString());



            IniWriteValue("xiaoke", "width", i.ToString());

            IniWriteValue("xiaoke", "style", i.ToString());
            IniWriteValue("xiaoke", "Substyle", i.ToString());
            IniWriteValue("xiaoke", "cbbTrue", i.ToString());
            */

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //记录INI配置文件路径
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\SystemSet.ini";
            path = strg;
            try
            {
                //显示样式
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "style") + "\n";
                //显示子演示
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "Substyle") + "\n";
                //显示方向
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "direction") + "\n";
                //显示线条宽度
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "width") + "\n";
                //显示校验位
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "cbbTrue") + "\n";

                //判断默认条形码是否显示数据
                richTextBox1.Text += "aaaaa " + IniReadValue("xiaoke", "dispaly") + "\n";
            }
            catch { }

        }
    }
}
