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
        private string LogFileName;

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

        private void Form1_Load(object sender, EventArgs e)
        {
            LogFileName = Application.StartupPath + "\\log_" + DateTime.Now.ToString("yyyyMMdd") + ".txt";
            richTextBox1.Text += "自動存Log中.....\n";
        }

        // If the file exceeds max_size bytes, move it to a new file
        // with .1 appended to the name and bump down older versions.
        // (E.g. log.txt.1, log.txt.2, etc.)
        // Then write the text into the main log file. 
        private void WriteToLog(string new_text, string file_name, long max_size, int num_backups)
        {
            // See if the file is too big.
            FileInfo file_info = new FileInfo(file_name);
            if (file_info.Exists && file_info.Length > max_size)
            {
                // Remove the oldest version if it exists.
                if (File.Exists(file_name + "." + num_backups.ToString()))
                {
                    File.Delete(file_name + "." + num_backups.ToString());
                    richTextBox1.Text += "delete\t" + file_name + "\n";
                }

                // Bump down earlier backups.
                //richTextBox1.Text += "\n一個一個改名\n";
                for (int i = num_backups - 1; i > 0; i--)
                {
                    if (File.Exists(file_name + "." + i.ToString("D4")))
                    {
                        // Move file i to file i + 1.
                        File.Move(file_name + "." + i.ToString("D4"), file_name + "." + (i + 1).ToString("D4"));
                        //richTextBox1.Text += "i = " + i.ToString() + " rename\told = " + file_name + "." + i.ToString() + "\tnew = " + file_name + "." + (i + 1).ToString() + "\n";
                    }
                }

                // Move the main log file.
                File.Move(file_name, file_name + ".0001");
            }

            // Write the text.
            File.AppendAllText(file_name, new_text + '\n');
        }

        int i = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            i++;
            string ttt = i.ToString() + " " + DateTime.Now.ToString();
            WriteToLog(ttt, LogFileName, 100, 300);
        }

    }
}
