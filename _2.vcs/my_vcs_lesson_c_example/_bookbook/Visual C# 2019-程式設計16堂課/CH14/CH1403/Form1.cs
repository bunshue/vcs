using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace CH1403
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool fileIsOpen;
        private string openFileName, folderName;

        private void Form1_Load(object sender, EventArgs e)
        {
            rtxtShow.Dock = DockStyle.Fill;

            //設定瀏覽資料夾對話方塊-從虛擬「桌面」為開始的資料夾
            dlgFolderBrowser.RootFolder =
               Environment.SpecialFolder.Desktop;

            //指定要瀏覽的資料夾為D碟
            dlgFolderBrowser.SelectedPath =
               @"D:\USERS\LSH\Documents";

            //瀏覽資料夾的提示文字
            dlgFolderBrowser.Description = "選取要瀏覽的資料夾";
        }

        //瀏覽資料夾
        private void tsmiFolder_Click(object sender, EventArgs e)
        {
            //進入FloderBrowserDialog並按確定鈕
            DialogResult result = dlgFolderBrowser.ShowDialog();
            if (result == DialogResult.OK)
            {
                //取得瀏覽資料夾對話方塊所選取的路徑
                folderName = dlgFolderBrowser.SelectedPath;
                //確認沒有開啟的檔案，依預設的資料夾來開啟
                if (!fileIsOpen)
                {
                    dlgOpenFile.InitialDirectory = folderName;
                    dlgOpenFile.FileName = null;
                    //取得Click事件的訊息
                    tsmiFile.PerformClick();
                }
            }
        }

        //檔案功能表的關閉項目
        private void tsmiEnd_Click(object sender, EventArgs e)
        {
            rtxtShow.Clear();
            fileIsOpen = false;
            tsmiEnd.Enabled = false;
        }

        //檔案功能表的開啟檔案項目
        private void tsmiOpen_Click(object sender, EventArgs e)
        {
            //判斷檔案未開啟的情形下，指定位置
            if (!fileIsOpen)
            {
                dlgOpenFile.InitialDirectory =
                   dlgFolderBrowser.SelectedPath;
                dlgOpenFile.FileName = null;
            }

            //開啟RTF格式檔案
            dlgOpenFile.DefaultExt = "rtf";
            dlgOpenFile.Filter =
               "RTF格式(*.rtf)|*.rtf|所有檔案(*.*)|*.*";

            //顯示開啟檔案對話方塊
            DialogResult result = dlgOpenFile.ShowDialog();
            if (result == DialogResult.OK)
            {
                openFileName = dlgOpenFile.FileName;
                try
                {
                    //以RichTextBox的LoadFile()方法載入檔案
                    Stream sr = dlgOpenFile.OpenFile();
                    rtxtShow.LoadFile(sr, RichTextBoxStreamType.RichText);
                    sr.Close();
                    fileIsOpen = true;
                }
                catch (Exception exp)
                {
                    MessageBox.Show("發生錯誤. 訊息: " +
                       $"{System.Environment.NewLine}" +
                       $"{exp.ToString()}, {Environment.NewLine}");
                    fileIsOpen = false;
                }
            }
            // 按了「取消」按鈕就回到原來的表單畫面
            else if (result == DialogResult.Cancel)
            {
                return;
            }
        }
    }
}
