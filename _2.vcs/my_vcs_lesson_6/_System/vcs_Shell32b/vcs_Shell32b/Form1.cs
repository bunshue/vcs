using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//參考/加入參考 /COM/Microsoft Shell Controls and Automation
using Shell32;

namespace vcs_Shell32b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得檔案內容中的詳細資料\n";

            string filename = @"C:\______test_files\picture1.jpg";

            int i;
            for (i = 0; i < 30; i++)
            {
                string result = GetDetailValue(filename, i);
                richTextBox1.Text += i.ToString() + "\t" + result + "\n";
            }
        }

        static string GetDetailValue(string file, int column)
        {
            Shell shell = new Shell();
            Folder dir = shell.NameSpace(Path.GetDirectoryName(file));
            FolderItem item = dir.ParseName(Path.GetFileName(file));
            return dir.GetDetailsOf(item, column);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得媒體資訊
            //使用Shell32讀取影音文件屬性
            /*
            由於需要用到實時讀取影音文件(mp3、wma、wmv …)播放時間長度的功能，搜索到的結果有：
            （1）硬編碼分析影音文件，需要分析各種媒體格式，代價最大；
            （2）使用WMLib SDK，需要熟悉SDK各個接口，且不同版本的WM接口有別，代價次之；
            （3）使用系統Shell32的COM接口，直接訪問媒體文體屬性，取其特定內容，代價最小。
            顯然第3種方案見效最快，立即操刀：
            ①引用Shell32底層接口c:\windows\system32\shell32.dll，VS自動轉換成Interop.Shell32.dll（注：64位系統和32位系統生成的Interop.Shell32.dll不一樣）
            ②編碼讀取播放時間長度：
            */

            //取得媒體資訊
            //string filename = @"C:\______test_files\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\______test_files\_mp3\aaaa.mp3";
            int i;
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + GetMediaInfo(filename, i) + "\n";
            }
        }

        public string GetMediaInfo(string path, int item)
        {
            //參考/Shell32/右鍵/屬性/內嵌Interop型別改成False
            try
            {
                string result = string.Empty;
                Shell shell = new ShellClass();
                Folder folder = shell.NameSpace(path.Substring(0, path.LastIndexOf("\\")));
                FolderItem folderItem = folder.ParseName(path.Substring(path.LastIndexOf("\\") + 1));
                return folder.GetDetailsOf(folderItem, item);

                /* another
                ShellClass sh = new ShellClass();
                Folder dir = sh.NameSpace(Path.GetDirectoryName(sFile));
                FolderItem item = dir.ParseName(Path.GetFileName(sFile));
                string det = dir.GetDetailsOf(item, iCol);
                */
            }
            catch (Exception ex)
            {
                return null;
            }
        }
    }
}
