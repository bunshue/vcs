using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
namespace 获取网络中某台计算机的磁盘信息
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);
        private void button1_Click(object sender, EventArgs e)
        {
            if (this.folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                long fb, ftb, tfb;
                string str = this.folderBrowserDialog1.SelectedPath;
                this.textBox4.Text = str;
                if (GetDiskFreeSpaceEx(str, out fb, out ftb, out tfb) != 0)
                {
                    string strfb = Convert.ToString(fb / 1024 / 1024)+"M";
                    string strftb = Convert.ToString(ftb / 1024 / 1024)+"M";
                    string strtfb = Convert.ToString(tfb / 1024 / 1024)+"M";
                    this.textBox2.Text = strfb;//总空间
                    this.textBox1.Text = strftb;//可用空间
                    this.textBox3.Text = strtfb;//总剩余空间
                }
                else
                {
                    MessageBox.Show("NO");
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}