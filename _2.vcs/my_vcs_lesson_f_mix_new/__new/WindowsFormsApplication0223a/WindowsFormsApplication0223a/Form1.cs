using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;
using System.Threading;

namespace WindowsFormsApplication0223a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //#制作閃動的窗體
        private void button1_Click(object sender, EventArgs e)
        {
            while (Visible) // 關閉窗體時，停止循環
            {
                for (int c = 0; c < 254 && Visible; c++)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c); // 此方法指定三個數字：red/green/blue.
                    Application.DoEvents(); // 此語句使操作系統能夠在程序之外執行其他操作。否則
                    // 程序將占用所有CPU周期
                    Thread.Sleep(3); // 此語句在循環中插入3毫秒的延遲。
                }
                for (int c = 254; c >= 0 && Visible; c--)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c);
                    Application.DoEvents();
                    Thread.Sleep(3);
                }
            }

        }

        //顯示Loading窗體
        private void button2_Click(object sender, EventArgs e)
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            pLoading.SetExecuteMethod(method);
            pLoading.ShowDialog();

        }

        private void method()
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            for (int i = 0; i < 10; i++)
            {
                pLoading.SetCaptionAndDescription("", "", "執行進度" + i.ToString() + "/10");

                //XXXXXXX

                Thread.Sleep(1000);
            }
            LoadingControl.getLoading().CloseLoadingForm();


        }

        private void button3_Click(object sender, EventArgs e)
        {
            //將純文字檔拆成一行一行的字串陣列, 可以去除前後空白
            string[] patterns;
            patterns = File.ReadAllLines("filename.txt").Select(i => i.Trim()).Where(i => i != string.Empty).ToArray();
            int len = patterns.Length;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            int ii;
            for (ii = 0; ii < len; ii++)
            {
                richTextBox1.Text += patterns[ii] + "\n";
            }



        }

        private void button4_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            List<string[]> fileNameList = new List<string[]>();

            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";
            for (i = 0; i < 10; i++)
            {
                fileNameList.Add(new string[] { i.ToString(), "aaaaaaa", "bbbbb", "cccccc" });
            }
            richTextBox1.Text += "len = " + fileNameList.Count.ToString() + "\n";

            for (i = 0; i < fileNameList.Count; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                for (j = 0; j < 4; j++)
                {
                    richTextBox1.Text += fileNameList[i][j] + "\t";
                }
                richTextBox1.Text += "\n";

            }

            foreach (var fileName in fileNameList)
            {
                string imgURL = fileName[0];
                richTextBox1.Text += imgURL + "\n";
            }





        }

        private void button5_Click(object sender, EventArgs e)
        {
            string url = @"C:/_git/vcs/_1.data/_html/朱冶蕙老師的電腦教室.html";
            //foreach (var fileName in fileNameList)
            {
                MemoryStream ms = GetResponse(url);
                File.WriteAllBytes("aaaaa.html", ms.ToArray());
            }

        }

        private MemoryStream GetResponse(string url)
        {
            while (true)
            {
                try
                {
                    HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
                    //request.Headers.Add("Cookie", cookie);
                    request.Method = "GET";
                    request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                    HttpWebResponse response = request.GetResponse() as HttpWebResponse;

                    MemoryStream ms = new MemoryStream();
                    response.GetResponseStream().CopyTo(ms);

                }
                catch (Exception ex)
                {
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files\__pic";

            IEnumerable<FileInfo> images = null;
            if (Directory.Exists(foldername) == true)
            {
                DirectoryInfo dirInfo = new DirectoryInfo(foldername);
                images = dirInfo.EnumerateFiles("*.jpg").OrderBy(i => i.Name[0]).ThenBy(i => i.Name.Length).ThenBy(i => i.Name);

                int len = images.Count();
                richTextBox1.Text += "len = " + len.ToString() + "\n";

                if (images != null && images.Count() > 0)
                {

                }

                foreach (var image in images)
                {
                    richTextBox1.Text += image.Name + "\n";
                    richTextBox1.Text += image.FullName + "\n";
                    richTextBox1.Text += image.Extension + "\n";
                    richTextBox1.Text += image.Length.ToString() + "\n";



                }



            }




        }








    }
}
