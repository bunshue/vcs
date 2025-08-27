using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;

//C# FileSystemWatcher 監視磁盤文件變更
//http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188058.html
//可以監視所有邏輯盤或者某個文件夾。
//1.直接打開是監視所有邏輯磁盤文件變化。
//2.或者傳遞參數，監視某一路徑文件變化。如圖，監視e盤


namespace vcs_FileSystemWatcher2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            //watcher組
            FileSystemWatcher[] watchers;

            watchers = new FileSystemWatcher[1];
            watchers[0] = new FileSystemWatcher { Path = foldername };

            /*  多個路徑
            //若未傳遞參數,則監視所有文件系統,包括CD-ROM（不可用）,可移動磁盤（不可用）等
            string[] drivers = Directory.GetLogicalDrives();
            watchers = new FileSystemWatcher[drivers.Length];

            for (int i = 0; i < drivers.Length; i++)
            {
                try
                {
                    watchers[i] = new FileSystemWatcher { Path = drivers[i] };
                }
                catch (Exception ex)
                {
                    Trace.TraceWarning(ex.Message);
                }
            }
            */

            foreach (FileSystemWatcher w in watchers)
            {
                if (w == null) continue;

                w.Filter = "*";
                w.IncludeSubdirectories = true;
                w.EnableRaisingEvents = true;

                w.Created += onFileSystem_Changed;
                w.Deleted += onFileSystem_Changed;
                w.Changed += onFileSystem_Changed;
                w.Renamed += watcher_Renamed;
            }
        }

        #region [ 檢測文件是否占用 ]
        /// <summary>
        /// 檢測文件是否占用
        /// </summary>
        /// <param name="filename"></param>
        /// <returns></returns>
        static bool IsFileReady(string filename)
        {
            var fi = new FileInfo(filename);
            FileStream fs = null;
            try
            {
                fs = fi.Open(FileMode.Open, FileAccess.Read, FileShare.None);
                return true;
            }
            catch (IOException)
            {
                return false;
            }

            finally
            {
                if (fs != null)
                    fs.Close();
            }
        }
        #endregion

        private volatile object _lock = true;
        void onFileSystem_Changed(object sender, FileSystemEventArgs e)
        {
            lock (_lock)
            {
                richTextBox1.Text += "[";
                richTextBox1.Text += DateTime.Now.ToString("HH:mm:ss");
                richTextBox1.Text += "] ";

                switch (e.ChangeType.ToString().ToLower())
                {
                    case "created":
                        //while (!IsFileReady(e.FullPath))
                        //{
                        //    if (!File.Exists(e.FullPath))
                        //        return;
                        //    Thread.Sleep(100);
                        //}
                        richTextBox1.Text += e.ChangeType;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.Name;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.FullPath;

                        break;
                    case "deleted":
                        richTextBox1.Text += e.ChangeType;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.Name;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.FullPath;
                        break;
                    case "changed":
                        richTextBox1.Text += e.ChangeType;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.Name;
                        richTextBox1.Text += " ";
                        richTextBox1.Text += e.FullPath;
                        break;
                }
                richTextBox1.Text += "\n";
            }
        }

        void watcher_Renamed(object sender, RenamedEventArgs e)
        {
            richTextBox1.Text += e.ChangeType;
            richTextBox1.Text += " ";
            richTextBox1.Text += e.OldName;
            richTextBox1.Text += e.OldFullPath;
            richTextBox1.Text += " ";
            richTextBox1.Text += e.Name;
            richTextBox1.Text += e.FullPath;
            richTextBox1.Text += Thread.CurrentThread.Name;
            richTextBox1.Text += "\n";
        }
         
         
         





    }
}
