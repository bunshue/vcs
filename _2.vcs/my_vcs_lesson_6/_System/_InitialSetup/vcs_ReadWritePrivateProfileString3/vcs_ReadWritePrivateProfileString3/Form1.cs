using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ReadWritePrivateProfileString3
{
    public partial class Form1 : Form
    {
        string ini_filename0 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_System\_InitialSetup\vcs_ReadWritePrivateProfileString3\vcs_ReadWritePrivateProfileString3\ini\setup0.ini";

        //#region 为INI文件中指定的节点取得字符串
        /// <summary>
        /// 为INI文件中指定的节点取得字符串
        /// </summary>
        /// <param name="lpAppName">欲在其中查找关键字的节点名称</param>
        /// <param name="lpKeyName">欲获取的项名</param>
        /// <param name="lpDefault">指定的项没有找到时返回的默认值</param>
        /// <param name="lpReturnedString">指定一个字串缓冲区，长度至少为nSize</param>
        /// <param name="nSize">指定装载到lpReturnedString缓冲区的最大字符数量</param>
        /// <param name="lpFileName">INI文件名</param>
        /// <returns>复制到lpReturnedString缓冲区的字节数量，其中不包括那些NULL中止字符</returns>
        [DllImport("kernel32")]
        public static extern int GetPrivateProfileString(
            string lpAppName,
            string lpKeyName,
            string lpDefault,
            StringBuilder lpReturnedString,
            int nSize,
            string lpFileName);
        //#endregion

        //#region 修改INI文件中内容
        /// <summary>
        /// 修改INI文件中内容
        /// </summary>
        /// <param name="lpApplicationName">欲在其中写入的节点名称</param>
        /// <param name="lpKeyName">欲设置的项名</param>
        /// <param name="lpString">要写入的新字符串</param>
        /// <param name="lpFileName">INI文件名</param>
        /// <returns>非零表示成功，零表示失败</returns>
        [DllImport("kernel32")]
        public static extern int WritePrivateProfileString(
            string lpApplicationName,
            string lpKeyName,
            string lpString,
            string lpFileName);
        //#endregion

        //#region 从INI文件中读取指定节点的内容
        /// <summary>
        /// 从INI文件中读取指定节点的内容
        /// </summary>
        /// <param name="section">INI节点</param>
        /// <param name="key">节点下的项</param>
        /// <param name="def">没有找到内容时返回的默认值</param>
        /// <param name="def">要读取的INI文件</param>
        /// <returns>读取的节点内容</returns>
        public string ReadString(string section, string key, string def, string fileName)
        {
            StringBuilder temp = new StringBuilder(1024);
            GetPrivateProfileString(section, key, def, temp, 1024, fileName);
            return temp.ToString();
        }
        //#endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(850, 750);
            this.Text = "vcs_ReadWritePrivateProfileString3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //讀取 ini

            string str1 = ReadString("Set", "MultiExcel", "", ini_filename0);//读取默认的多个Excel文件
            string str2 = ReadString("Set", "Excel", "", ini_filename0);//读取目标Excel文件
            richTextBox1.Text += "取得 : " + str1 + "\n";
            richTextBox1.Text += "取得 : " + str2 + "\n";

            string str3 = ReadString("Set", "Hour", "", ini_filename0);//读取小时
            string str4 = ReadString("Set", "Min", "", ini_filename0);//读取分钟

            richTextBox1.Text += "取得 時 : " + str3 + "\n";
            richTextBox1.Text += "取得 分 : " + str4 + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //寫入 ini
            string str1 = "aaaa";
            string str2 = "bbbb";
            string str3 = "123";
            string str4 = "456";
            /*
            WritePrivateProfileString("Set", "MultiExcel", str1, ini_filename0);//设置多个Excel文件路径
            WritePrivateProfileString("Set", "Excel", str2, ini_filename0);//设置目标Excel文件路径
            WritePrivateProfileString("Set", "Hour", str3, ini_filename0);//设置小时
            WritePrivateProfileString("Set", "Min", str4, ini_filename0);//设置分钟
            */
            richTextBox1.Text += "寫入 ini 完成\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
