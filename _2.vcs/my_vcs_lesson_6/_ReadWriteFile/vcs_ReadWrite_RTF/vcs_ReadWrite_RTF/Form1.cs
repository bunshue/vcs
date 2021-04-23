using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_RTF
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_rtf\VS2013Express.rtf";

            this.richTextBox1.LoadFile(filename, RichTextBoxStreamType.RichText);//從指定位置加載RTF文件
            richTextBox2.Text += "開啟檔案 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\rtf_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".rtf";

            richTextBox1.SaveFile(filename, RichTextBoxStreamType.RichNoOleObjs);//在指定路徑下保存

            //same
            //richTextBox1.SaveFile(filename);//在指定位置下保存RTF文件

            richTextBox2.Text += "儲存檔案 : " + filename + " 完成\n";
        }


    }
}
