using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//使用 FileSystemWatcher 來監控資料夾下的文件
//FileSystemWatcher 是一個當目錄或目錄內檔案變更時，接聽 (Listen) 檔案系統變更告知並引發事件。
//會用到這類別，也是因為專案中要監控特別資料夾中的檔案是否有所變動。

/*
結果：
1.在資料夾中建立一個新的檔案，建立後會觸發 FileSystemWatcher 所提供的事件
2.對剛建立的檔案重新命名，重新命名後會觸發 FileSystemWatcher 所提供的事件
3.刪除重新命名的檔案，刪除後會觸發 FileSystemWatcher 所提供的事件
4.更改監控資料夾中檔案的內容，更改後會觸發 FileSystemWatcher 所提供的事件
*/

namespace vcs_FileSystemWatcher1
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files\__pic";

        FileInfo fi;
        StringBuilder sb;
        DirectoryInfo dirInfo;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            label1.Text = "監控路徑 : " + foldername;
            MyFileSystemWatcher();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void MyFileSystemWatcher()
        {
            //設定所要監控的資料夾
            fileSystemWatcher1.Path = foldername;

            //設定所要監控的變更類型
            fileSystemWatcher1.NotifyFilter = NotifyFilters.LastAccess | NotifyFilters.LastWrite | NotifyFilters.FileName | NotifyFilters.DirectoryName;

            //設定所要監控的檔案
            fileSystemWatcher1.Filter = "*.*";

            //設定是否監控子資料夾
            fileSystemWatcher1.IncludeSubdirectories = true;

            //設定是否啟動元件，此部分必須要設定為 true，不然事件是不會被觸發的
            fileSystemWatcher1.EnableRaisingEvents = true;

            //設定觸發事件
            fileSystemWatcher1.Created += new FileSystemEventHandler(fileSystemWatcher1_Created);
            fileSystemWatcher1.Changed += new FileSystemEventHandler(fileSystemWatcher1_Changed);
            fileSystemWatcher1.Renamed += new RenamedEventHandler(fileSystemWatcher1_Renamed);
            fileSystemWatcher1.Deleted += new FileSystemEventHandler(fileSystemWatcher1_Deleted);
        }

        /// <summary>
        /// 當所監控的資料夾有建立文字檔時觸發
        /// </summary>
        private void fileSystemWatcher1_Created(object sender, FileSystemEventArgs e)
        {
            sb = new StringBuilder();

            dirInfo = new DirectoryInfo(e.FullPath.ToString());

            sb.AppendLine("新建檔案於：" + dirInfo.FullName.Replace(dirInfo.Name, ""));
            sb.AppendLine("新建檔案名稱：" + dirInfo.Name);
            sb.AppendLine("建立時間：" + dirInfo.CreationTime.ToString());
            sb.AppendLine("目錄下共有：" + dirInfo.Parent.GetFiles().Count() + " 檔案");
            sb.AppendLine("目錄下共有：" + dirInfo.Parent.GetDirectories().Count() + " 資料夾");

            //MessageBox.Show(sb.ToString());
            richTextBox1.Text += sb.ToString() + "\n";

        }

        /// <summary>
        /// 當所監控的資料夾有文字檔檔案內容有異動時觸發
        /// </summary>
        private void fileSystemWatcher1_Changed(object sender, FileSystemEventArgs e)
        {
            sb = new StringBuilder();

            dirInfo = new DirectoryInfo(e.FullPath.ToString());

            sb.AppendLine("被異動的檔名為：" + e.Name);
            sb.AppendLine("檔案所在位址為：" + e.FullPath.Replace(e.Name, ""));
            sb.AppendLine("異動內容時間為：" + dirInfo.LastWriteTime.ToString());

            //MessageBox.Show(sb.ToString());
            richTextBox1.Text += sb.ToString() + "\n";
        }

        /// <summary>
        /// 當所監控的資料夾有文字檔檔案重新命名時觸發
        /// </summary>
        private void fileSystemWatcher1_Renamed(object sender, RenamedEventArgs e)
        {
            sb = new StringBuilder();

            fi = new FileInfo(e.FullPath.ToString());

            sb.AppendLine("檔名更新前：" + e.OldName.ToString());
            sb.AppendLine("檔名更新後：" + e.Name.ToString());
            sb.AppendLine("檔名更新前路徑：" + e.OldFullPath.ToString());
            sb.AppendLine("檔名更新後路徑：" + e.FullPath.ToString());
            sb.AppendLine("建立時間：" + fi.LastAccessTime.ToString());

            //MessageBox.Show(sb.ToString());
            richTextBox1.Text += sb.ToString() + "\n";
        }

        /// <summary>
        /// 當所監控的資料夾有文字檔檔案有被刪除時觸發
        /// </summary>
        private void fileSystemWatcher1_Deleted(object sender, FileSystemEventArgs e)
        {
            sb = new StringBuilder();

            sb.AppendLine("被刪除的檔名為：" + e.Name);
            sb.AppendLine("檔案所在位址為：" + e.FullPath.Replace(e.Name, ""));
            sb.AppendLine("刪除時間：" + DateTime.Now.ToString());

            //MessageBox.Show(sb.ToString());
            richTextBox1.Text += sb.ToString() + "\n";
        }





    }
}
