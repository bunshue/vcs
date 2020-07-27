using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

using System.Reflection;    //for BindingFlags

using System.Net;   //for WebClient

using System.Xml.Linq;  //for XDocument
namespace WindowsFormsApplication1ffff
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            var dirnames = Directory.GetDirectories(@"C:\______test_files");
            int i = 0;

            try
            {
                foreach (var dir in dirnames)
                {
                    richTextBox1.Text += "aaaa3 dir = " + dir + "\n";
                    var fnames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                    DirectoryInfo d = new DirectoryInfo(dir);
                    FileInfo[] finfo = d.GetFiles("*.jpg");

                    foreach (var f in fnames)
                    {
                        i++;
                        //richTextBox1.Text += "The number of the file being renamed is: " + i.ToString() + "\n";

                        richTextBox1.Text += f + "\n";

                        if (!File.Exists(Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", ""))))
                        {
                            File.Move(Path.Combine(dir, f), Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", "")));
                        }
                        else
                        {
                            richTextBox1.Text += "The file you are attempting to rename already exists! The file path is " + dir + "\n";
                            foreach (FileInfo fi in finfo)
                            {
                                richTextBox1.Text += "The file modify date is: " + File.GetLastWriteTime(dir) + "\n";
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            richTextBox1.Text += "dirnames : " + dirnames + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //隨時產生臨時檔名
            //richTextBox1.Text += "臨時檔名 : " + string.Format("filename-{0:yyyy-MM-dd_HH:mm:ss}.txt", DateTime.Now) + "\n";

            //richTextBox1.Text += "臨時檔名 : " + string.Format("{0}{1}.txt", "filename-", DateTime.Now.ToString("yyyy-MM-dd_HH:mm:ss")) + "\n";


            string filename = string.Format("csv-{0:yyyy_MMdd_HHmmss}.csv", DateTime.Now);
            richTextBox1.Text += "filename : " + filename + "\n";

            int aaa = 123;
            int bbb = 456;

            using (var stream = File.CreateText(filename))
            {
                string first = aaa.ToString();
                string second = bbb.ToString();
                string csv = string.Format("{0},{1}\n", first, second);
                //File.WriteAllText(filename, csv);
                stream.WriteLine(csv);
                richTextBox1.Text += "csv : " + csv + "\n";
            }





        }


        private static void CreateShortCut(string shortCutFile, string targetPath, string description = "")
        {
            var type = Type.GetTypeFromProgID("WScript.Shell");
            object instance = Activator.CreateInstance(type);
            var result = type.InvokeMember("CreateShortCut", BindingFlags.InvokeMethod, null, instance, new object[] { shortCutFile });

            type = result.GetType();
            type.InvokeMember("TargetPath", BindingFlags.SetProperty, null, result, new object[] { targetPath });
            type.InvokeMember("Description", BindingFlags.SetProperty, null, result, new object[] { description });
            type.InvokeMember("Save", BindingFlags.InvokeMethod, null, result, null);
        }

        private static void CreateSendToShortCut(string shortCutFileName, string targetPath, string description = "")
        {
            var sendToFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            var shortCutFile = Path.Combine(sendToFolderPath, shortCutFileName);
            CreateShortCut(shortCutFile, targetPath, description);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            CreateSendToShortCut("david test.lnk", @"C:\Program Files (x86)\WinMerge\WinMergeU.exe");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //DownloadStaticMap(40.714728, -73.998672, "map.jpg");





        }

        private void DownloadStaticMap(double latitude, double longitude, string file)
        {
            if (string.IsNullOrEmpty(file))
                throw new ArgumentNullException("file");

            if (File.Exists(file))
                return;


            var urlFormat = @"http://maps.google.com/maps/api/staticmap?center={0},{1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
            var url = String.Format(urlFormat, latitude.ToString(), longitude.ToString());

            using (var wc = new WebClient())
            {
                wc.DownloadFile(url, file);
            }
        }

    }
}
