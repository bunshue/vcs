using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;   //for DllImport, DllImportAttribute

//參考/加入參考/.NET/Microsoft.VisualBasic

//編輯 vcs_RecycleBin.csproj 把x86改成x64

namespace vcs_RecycleBin
{
    public partial class Form1 : Form
    {
        string filename = Application.StartupPath + "\\test_delete_file.txt";
        string foldername = Application.StartupPath + "\\test_delete_folder";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Make files we can delete.
            MakeTestFiles();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (!File.Exists(filename))
            {
                richTextBox1.Text += "測試檔案不存在, 離開\n";
                return;
            }

            //刪除檔案
            //                              確認              永久刪除
            Recycler.DeleteFile(filename, checkBox1.Checked, radioButton2.Checked);
            richTextBox1.Text += "刪除檔案\t完成\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (!Directory.Exists(foldername))
            {
                richTextBox1.Text += "測試資料夾不存在, 離開\n";
                return;
            }

            //刪除資料夾
            //                                          確認              永久刪除
            Recycler.DeleteDirectory(foldername, checkBox1.Checked, radioButton2.Checked);
            richTextBox1.Text += "刪除資料夾\t完成\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //清理資源回收筒
            //                             進度                音效             確認
            Recycler.EmptyWastebasket(checkBox2.Checked, checkBox3.Checked, checkBox4.Checked);
            richTextBox1.Text += "清理資源回收筒\t完成\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "資源回收筒狀態\n";
            richTextBox1.Text += "目前資源回收筒內有 " + Recycler.NumberOfFilesInRecycleBin().ToString() + " 個項目\n";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Text = "目前資源回收筒內有 " + Recycler.NumberOfFilesInRecycleBin().ToString() + " 個項目";
        }

        // Make a file and a directory that we can delete.
        private void MakeTestFiles()
        {
            richTextBox1.Text += "建立測試檔案\n";

            // Make a file.
            richTextBox1.Text += "建立測試檔案 : " + filename + "\n";

            if (!File.Exists(filename))
            {
                richTextBox1.Text += "測試檔案不存在, 建立之\n";
                File.WriteAllText(filename, "This is a test file.");
            }

            // Make a directory.
            richTextBox1.Text += "建立測試資料夾 : " + foldername + "\n";

            if (!Directory.Exists(foldername))
            {
                richTextBox1.Text += "測試資料夾不存在, 建立之\n";
                Directory.CreateDirectory(foldername);
            }

            string filename2 = foldername + "\\Test2.txt";
            richTextBox1.Text += "建立測試檔案 : " + filename2 + "\n";

            if (!File.Exists(filename2))
            {
                richTextBox1.Text += "測試檔案不存在, 建立之\n";
                File.WriteAllText(filename2, "This is another test file.");
            }
        }

        //清理資源回收筒 ST
        const int SHERB_NOCONFIRMATION = 0x000001;	//整型常量在API中表示删除时没有确认对话框
        const int SHERB_NOPROGRESSUI = 0x000002;		//在API中表示不显示删除进度条
        const int SHERB_NOSOUND = 0x000004;			//在API中表示删除完毕时不播放声音

        [DllImportAttribute("shell32.dll")]					//声明API函数
        private static extern int SHEmptyRecycleBin(IntPtr handle, string root, int falgs);

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "清理資源回收筒\n";
            SHEmptyRecycleBin(this.Handle, "", SHERB_NOCONFIRMATION + SHERB_NOPROGRESSUI + SHERB_NOSOUND);
        }
        //清理資源回收筒 SP

    }
}

