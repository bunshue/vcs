using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh7_3_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 將可供瀏覽的資料夾寫入ComboBox物件
            comboBox1.Items.AddRange(new object[]{
                "MyComputer",
                "MyDocuments",
                "MyMusic",
                "MyPictures",
                "Desktop",
                "ProgramFiles",
                "StartMenu"});

            // 預設ComboBox物件的Text為第1個選項
            comboBox1.SelectedIndex = 0;

            // 設定FolderBrowserDialog的初值
            folderBrowserDialog1.ShowNewFolderButton = false;
            folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyComputer;
            folderBrowserDialog1.Description = "----資料夾瀏覽對話方塊----" +
                "\n請選擇所要開啟的檔案所在的資料夾";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
                textBox1.Text = folderBrowserDialog1.SelectedPath;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            folderBrowserDialog1.ShowNewFolderButton = checkBox1.Checked;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 取得ComboBox物件目前被選取的選項文字
            string x = comboBox1.SelectedItem.ToString();
            switch (x)
            {
                case "MyComputer":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyComputer; break;
                case "MyDocuments":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyDocuments; break;
                case "MyMusic":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyMusic; break;
                case "MyPictures":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyPictures; break;
                case "Desktop":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.Desktop; break;
                case "ProgramFiles":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.ProgramFiles; break;
                case "StartMenu":
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.StartMenu; break;
                default:
                    folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyComputer; break;
            }
        }
    }
}
