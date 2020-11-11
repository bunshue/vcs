using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;        //for Directory, File

namespace my_vcs_22_LOG
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public static class EventLog
        {
            public static string FilePath { get; set; }
            public static void Write(string format, params object[] arg)
            {
                Write(string.Format(format, arg));
            }

            public static void Write(string message)
            {
                if (string.IsNullOrEmpty(FilePath))
                {
                    FilePath = Directory.GetCurrentDirectory();
                }

                string filename = FilePath + string.Format("\\{0:yyyy}-{0:MM}\\LOG_{0:yyyy-MM-dd}.txt", DateTime.Now);
                FileInfo finfo = new FileInfo(filename);
                if (finfo.Directory.Exists == false)
                {
                    finfo.Directory.Create();
                }
                string writeString = string.Format("{0:yyyy/MM/dd HH:mm:ss} {1}",
                    DateTime.Now, message) + Environment.NewLine;

                File.AppendAllText(filename, writeString, Encoding.Unicode);
            }
        }

        int aa = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            aa++;
            string str = "加入LOG aa = " + aa.ToString();
            EventLog.Write(str);
            richTextBox1.Text += str + "\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}
