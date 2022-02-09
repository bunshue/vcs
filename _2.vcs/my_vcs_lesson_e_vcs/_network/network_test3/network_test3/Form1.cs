using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using System.Net;   //for HttpWebRequest

using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

namespace network_test3
{
    public partial class Form1 : Form
    {
        List<Thread> threadList = new List<Thread>();
        Thread thread = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            foreach (Thread thread in threadList)
            {
                thread.Abort();
            }
        }

        private void bt_start_Click(object sender, EventArgs e)
        {
            DateTime dtStart = DateTime.Now;
            bt_resume.Enabled = true;
            bt_pause.Enabled = true;
            bt_start.Enabled = false;
            int page = 0;
            int count = 0;
            int personCount = 0;
            lblPage.Text = "已完成頁數：0";
            int index = 0;

            richTextBox1.Text += "aaaaaaaaaa\n";
            for (int i = 1; i <= 10; i++)
            {

                thread = new Thread(new ParameterizedThreadStart(delegate(object obj)
                {
                    for (int j = 1; j <= 10; j++)
                    {
                        label1.Text = j.ToString();
                        try
                        {
                            index = (Convert.ToInt32(obj) - 1) * 10 + j;
                            richTextBox1.Text += "http://tt.mop.com/c44/0/1_" + index.ToString() + ".html" + "\n";
                            string pageHtml = HttpRequestUtil.GetPageHtml("http://tt.mop.com/c44/0/1_" + index.ToString() + ".html");
                            //this.Text = pageHtml;
                            Regex regA = new Regex("<a[\\s]+class=\"J-userPic([^<>]*?)[\\s]+href=\"([^\"]*?)\"");
                            Regex regImg = new Regex("<p class=\"tc mb10\"><img[\\s]+src=\"([^\"]*?)\"");
                            MatchCollection mc = regA.Matches(pageHtml);
                            foreach (Match match in mc)
                            {
                                int start = match.ToString().IndexOf("href=\"");
                                string url = match.ToString().Substring(start + 6);
                                int end = url.IndexOf("\"");
                                url = url.Substring(0, end);
                                if (url.IndexOf("/") == 0)
                                {
                                    string imgPageHtml = HttpRequestUtil.GetPageHtml("http://tt.mop.com" + url);
                                    personCount++;
                                    lblPerson.Invoke(new Action(delegate() { lblPerson.Text = "已完成條數：" + personCount.ToString(); }));
                                    MatchCollection mcImgPage = regImg.Matches(imgPageHtml);
                                    foreach (Match matchImgPage in mcImgPage)
                                    {
                                        start = matchImgPage.ToString().IndexOf("src=\"");
                                        string imgUrl = matchImgPage.ToString().Substring(start + 5);
                                        end = imgUrl.IndexOf("\"");
                                        imgUrl = imgUrl.Substring(0, end);
                                        if (imgUrl.IndexOf("http://i1") == 0)
                                        {
                                            try
                                            {
                                                HttpRequestUtil.HttpDownloadFile(imgUrl);
                                                count++;
                                                lblNum.Invoke(new Action(delegate()
                                                {
                                                    lblNum.Text = "已下載圖片數" + count.ToString();
                                                    DateTime dt = DateTime.Now;
                                                    double time = dt.Subtract(dtStart).TotalSeconds;
                                                    if (time > 0)
                                                    {
                                                        lblSpeed.Text = "速度：" + (count / time).ToString("0.0") + "張/秒";
                                                    }
                                                }));
                                            }
                                            catch { }
                                            Thread.Sleep(1);
                                        }
                                    }
                                }
                            }
                        }
                        catch { }
                        page++;
                        lblPage.Invoke(new Action(delegate() { lblPage.Text = "已完成頁數：" + page.ToString(); }));

                        if (page == 100)
                        {
                            bt_start.Invoke(new Action(delegate() { bt_start.Enabled = true; }));
                            MessageBox.Show("完成！");
                        }
                    }
                }));
                thread.Start(i);
                threadList.Add(thread);
            }
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            bt_start.Invoke(new Action(delegate()
            {
                foreach (Thread thread in threadList)
                {
                    if (thread.ThreadState == ThreadState.Suspended)
                    {
                        thread.Resume();
                    }
                    thread.Abort();
                }
                bt_start.Enabled = true;
                bt_pause.Enabled = false;
                bt_resume.Enabled = false;
                bt_stop.Enabled = false;
            }));
        }

        private void bt_resume_Click(object sender, EventArgs e)
        {
            foreach (Thread thread in threadList)
            {
                if (thread.ThreadState == ThreadState.Running)
                {
                    thread.Suspend();
                }
            }
            bt_resume.Enabled = false;
            bt_stop.Enabled = true;
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            foreach (Thread thread in threadList)
            {
                if (thread.ThreadState == ThreadState.Suspended)
                {
                    thread.Resume();
                }
            }
            bt_resume.Enabled = true;
            bt_stop.Enabled = false;
        }
    }

    /// <summary>
    /// HTTP要求對象類
    /// </summary>
    public class HttpRequestUtil
    {
        /// <summary>
        /// 獲得頁面html
        /// </summary>
        public static string GetPageHtml(string url)
        {
            // 設置參數
            HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)";
            //發送要求並獲得響應回應數據
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            //直到request.GetResponse()法式才開端向目的網頁發送Post要求
            Stream responseStream = response.GetResponseStream();
            StreamReader sr = new StreamReader(responseStream, Encoding.UTF8);
            //前往成果網頁（html）代碼
            string content = sr.ReadToEnd();
            return content;
        }

        /// <summary>
        /// Http下載文件
        /// </summary>
        public static void HttpDownloadFile(string url)
        {
            int pos = url.LastIndexOf("/") + 1;
            string fileName = url.Substring(pos);
            string path = Application.StartupPath + "\\download";
            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }
            string filePathName = path + "\\" + fileName;
            if (File.Exists(filePathName)) return;

            // 設置參數
            HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)";
            request.Proxy = null;
            //發送要求並獲得響應回應數據
            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            //直到request.GetResponse()法式才開端向目的網頁發送Post要求
            Stream responseStream = response.GetResponseStream();

            //創立當地文件寫入流
            Stream stream = new FileStream(filePathName, FileMode.Create);

            byte[] bArr = new byte[1024];
            int size = responseStream.Read(bArr, 0, (int)bArr.Length);
            while (size > 0)
            {
                stream.Write(bArr, 0, size);
                size = responseStream.Read(bArr, 0, (int)bArr.Length);
            }
            stream.Close();
            responseStream.Close();
        }
    }
}
