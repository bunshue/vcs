using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.IO;

namespace SoundCalculator
{
    public partial class Form2 : Form
    {
        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            GetIni(groupBox1.Controls);
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "確定\n";
            Clear_Control(groupBox1.Controls, Form1.VoxPath.Length);
            this.DialogResult = DialogResult.OK;
            Close();
        }

        public void Clear_Control(Control.ControlCollection Con, int m)
        {
            int tem_n = 0;
            foreach (Control C in Con)
            { //搜尋可視化組件中的所有控制元件
                if (C.GetType().Name == "TextBox")  //判斷是否為TextBox控制元件
                {
                    WritePrivateProfileString("Vox", ((TextBox)C).Tag.ToString(), ((TextBox)C).Text, Application.StartupPath + "\\Tem_File.ini");
                    tem_n += 1;
                }
                if (tem_n > m)
                {
                    break;
                }
            }
        }

        public void Clear_Control(Control.ControlCollection Con, int n, string Path)
        {
            foreach (Control C in Con)
            { //搜尋可視化組件中的所有控制元件
                if (C.GetType().Name == "TextBox")  //判斷是否為TextBox控制元件
                {
                    if (Convert.ToInt32(((TextBox)C).Tag.ToString()) == n)
                    {
                        ((TextBox)C).Text = Path;
                        break;
                    }

                }
            }
        }

        public void GetIni(Control.ControlCollection Con)
        {
            StringBuilder temp = new StringBuilder(255);
            if (File.Exists(Application.StartupPath + "\\Tem_File.ini") == true)
            {
                foreach (Control C in Con)
                { //搜尋可視化組件中的所有控制元件
                    if (C.GetType().Name == "TextBox")  //判斷是否為TextBox控制元件
                    {
                        GetPrivateProfileString("Vox", ((TextBox)C).Tag.ToString(), "數據讀取錯誤。", temp, 255, Application.StartupPath + "\\Tem_File.ini");
                        ((TextBox)C).Text = temp.ToString();
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Clear_Control(groupBox1.Controls, Convert.ToInt32(((Button)sender).Tag.ToString()), openFileDialog1.FileName);
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取消\n";
            Close();
        }
    }
}

