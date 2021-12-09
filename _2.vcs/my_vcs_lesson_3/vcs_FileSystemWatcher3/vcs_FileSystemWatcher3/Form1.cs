using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//文件監視器

namespace vcs_FileSystemWatcher3
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
            FileSystemWatcher k8watcher = new FileSystemWatcher();
            k8watcher.Path = @"C:\______test_files\_pic";
            k8watcher.IncludeSubdirectories = true;
            k8watcher.EnableRaisingEvents = true;
            k8watcher.SynchronizingObject = this;
            k8watcher.Created += new FileSystemEventHandler(k8fileCreated);
            k8watcher.Changed += new FileSystemEventHandler(k8fileChanged);
            k8watcher.Renamed += new RenamedEventHandler(k8fileRenamed);
            k8watcher.Deleted += new FileSystemEventHandler(k8fileDeleted);
        }

        public void k8fileCreated(object sender, FileSystemEventArgs e)
        {
            string log = string.Format(e.ChangeType + ":{0} --時間:{1}\r\n\r\n", e.FullPath, DateTime.Now.ToString());
            richTextBox1.AppendText(log);
        }

        public void k8fileChanged(object sender, FileSystemEventArgs e)
        {
            string log = string.Format(e.ChangeType + ":{0} --時間:{1}\r\n\r\n", e.FullPath, DateTime.Now.ToString());
            richTextBox1.AppendText(log);
        }

        public void k8fileDeleted(object sender, FileSystemEventArgs e)
        {
            string log = string.Format(e.ChangeType + ":{0} --時間:{1}\r\n\r\n", e.FullPath, DateTime.Now.ToString());
            richTextBox1.AppendText(log);
        }

        public void k8fileRenamed(object sender, FileSystemEventArgs e)
        {
            string log = string.Format(e.ChangeType + ":{0} --時間:{1}\r\n\r\n", e.FullPath, DateTime.Now.ToString());
            richTextBox1.AppendText(log);
        }
    }
}
