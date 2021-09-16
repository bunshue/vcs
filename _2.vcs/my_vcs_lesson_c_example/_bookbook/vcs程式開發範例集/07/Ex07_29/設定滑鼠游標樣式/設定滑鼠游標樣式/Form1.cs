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

namespace 設定滑鼠游標樣式
{
    public partial class Form1 : Form
    {
        [DllImport("user32", EntryPoint = "LoadCursorFromFile")]
        public static extern int IntLoadCursorFromFile(string lpFileName);
        [DllImport("user32", EntryPoint = "SetSystemCursor")]
        public static extern void SetSystemCursor(int hcur, int i);

        const int OCR_NORAAC = 32512;   //標準
        const int OCR_HAND = 32649;     //手
        const int OCR_NO = 32648;       //斜的圓
        const int OCR_SIZEALL = 32646;  //移動

        string WindowsPath = "";    //windows目錄路徑
        string CursorsPath = "";    //儲存滑鼠游標樣式的目錄
        string strg = @"C:\______test_files\__RW\_cursor";  //儲存滑鼠游標樣式的文件夾路徑

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            WindowsPath = Environment.GetEnvironmentVariable("WinDir");
            CursorsPath = WindowsPath + "\\Cursors";
            /*
            strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\Image";
            */

            richTextBox1.Text += "CursorsPath = " + CursorsPath + "\n";
            richTextBox1.Text += "strg = " + strg + "\n";
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
            {
                DirectoryInfo di = new DirectoryInfo(CursorsPath + @"\Image");
                if (!di.Exists)
                {
                    di.Create();
                    string[] str = Directory.GetFiles(strg);
                    for (int i = 0; i < str.Length; i++)
                    {
                        string filename = str[i].Substring(str[i].LastIndexOf("\\") + 1, str[i].Length - 1 - str[i].LastIndexOf("\\"));
                        File.Copy(str[i], CursorsPath + @"\Image\" + filename, true);
                    }
                }
                else
                {
                    string[] str = Directory.GetFiles(strg);
                    for (int i = 0; i < str.Length; i++)
                    {
                        string filename = str[i].Substring(str[i].LastIndexOf("\\") + 1, str[i].Length - 1 - str[i].LastIndexOf("\\"));
                        File.Copy(str[i], CursorsPath + @"\Image\" + filename, true);
                    }
                }

                //將要修改的標鼠圖片存入到系統的WINDOWS\Cursors目錄下
                //設定正常選擇滑鼠游標
                int cur = IntLoadCursorFromFile(CursorsPath + @"\Image\01.cur");
                SetSystemCursor(cur, OCR_NORAAC);
                //設定移動
                cur = IntLoadCursorFromFile(CursorsPath + @"\Image\03.cur");
                SetSystemCursor(cur, OCR_SIZEALL);
                //設定不可用
                cur = IntLoadCursorFromFile(CursorsPath + @"\Image\04.cur");
                SetSystemCursor(cur, OCR_NO);
                //設定超鏈接
                cur = IntLoadCursorFromFile(CursorsPath + @"\Image\06.cur");
                SetSystemCursor(cur, OCR_HAND);
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked)
            {
                DirectoryInfo di = new DirectoryInfo(CursorsPath + @"\Image");
                if (di.Exists)
                    di.Delete(true);

                //恢復正常選擇滑鼠游標
                int cur = IntLoadCursorFromFile(CursorsPath + @"\arrow_m.cur");
                SetSystemCursor(cur, OCR_NORAAC);
                //恢復移動
                cur = IntLoadCursorFromFile(CursorsPath + @"\move_r.cur");
                SetSystemCursor(cur, OCR_SIZEALL);
                //恢復不可用
                cur = IntLoadCursorFromFile(CursorsPath + @"\no_r.cur");
                SetSystemCursor(cur, OCR_NO);
                //恢復超鏈接
                cur = IntLoadCursorFromFile(CursorsPath + @"\hand.cur");
                SetSystemCursor(cur, OCR_HAND);
            }
        }
    }
}

