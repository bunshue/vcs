using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

namespace vcs_ReadWritePrivateProfileString
{
    public partial class Form1 : Form
    {
        public string path;

        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retval, int size, string filePath);

        public void IniWriteValue(string section, string key, string value)
        {
            WritePrivateProfileString(section, key, value, path);
        }
        public string IniReadValue(string section, string key)
        {
            StringBuilder temp = new StringBuilder(255);
            int i = GetPrivateProfileString(section, key, "", temp, 255, path);
            return temp.ToString();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            path = Application.StartupPath.ToString();
            path = path.Substring(0, path.LastIndexOf("\\"));
            path = path.Substring(0, path.LastIndexOf("\\"));
            path += @"\Setup.ini";

            show_item_location();
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

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            richTextBox1.Size = new Size(400, 600);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(660, 670);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        string MyCursor;
        string MyPicPath;

        private void button0_Click(object sender, EventArgs e)
        {
            //Read

            MyCursor = IniReadValue("Setup", "CapMouse");
            MyPicPath = IniReadValue("Setup", "Dir");

            richTextBox1.Text += "MyCursor : " + MyCursor + "\n";
            richTextBox1.Text += "MyPicPath : " + MyPicPath + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\dddddddddd";
            //Write        主欄位   次欄位      內容
            IniWriteValue("Setup", "CapMouse", "1111");
            IniWriteValue("Setup", "Dir", foldername);
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }
}
