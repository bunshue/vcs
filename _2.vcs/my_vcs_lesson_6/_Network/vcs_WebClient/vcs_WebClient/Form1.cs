using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path, MemoryStream
using System.Net;
using System.Xml;
using System.Threading; //for Thread

using System.Text.RegularExpressions;   //for Regex

namespace vcs_WebClient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //for Romeo and Sugar    3072
            //ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            //ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            /*
            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
            */
        }

        void show_item_location()
        {
            int x_st = 10;
            int y_st = 10;
            int w = 120;
            int h = 50;
            int dx = w + 5;
            int dy = h + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(840, 540);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            webBrowser1.Size = new Size(600, 250);
            webBrowser1.Location = new Point(x_st + dx * 0, y_st + dy * 10);

            pictureBox1.Size = new Size(600, 250);
            pictureBox1.Location = new Point(x_st + dx * 5, y_st + dy * 10);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 870);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            try
            {
                string url = @"https://www.google.com.tw/";
                WebClient wc = new WebClient();

                //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
                //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3 | SecurityProtocolType.Tls;

                string res = wc.DownloadString(url);

                richTextBox1.Text += res + "\n";
            }

            catch (Exception ex)
            {
                richTextBox1.Text += "ERROR=" + ex.ToString() + "\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //WebClient DownloadString
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient DownloadString 1\t抓網頁資料到記憶體......\n";
            Application.DoEvents();

            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */

            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            WebClient wc1 = new WebClient();     // 建立 WebClient
            try  // Get the response string from the URL.
            {
                string data = wc1.DownloadString(url_file1);          //抓網頁資料到記憶體
                //richTextBox1.Text += data + "\n";
                richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "\nWebClient DownloadString 2\t抓網頁查詢資料到記憶體......\n";
            Application.DoEvents();

            string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";

            WebClient wc3 = new WebClient();     // 建立 WebClient
            try  // Get the response string from the URL.
            {
                // Get the response string from the URL.
                string xml = wc3.DownloadString(url_weather);        //抓資料
                //richTextBox1.Text += "data\n" + xml + "\n";
                richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "\nWebClient DownloadString 3\t網路下載純文字檔案......\n";

            WebClient wc = new WebClient();     // 建立 WebClient
            try
            {
                string url1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
                //下載純文字
                string result = wc.DownloadString(url1);
                //richTextBox1.Text += result;  //skip
                richTextBox1.Text += "網路下載純文字檔案\tOK\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }


            richTextBox1.Text += "\nWebClient DownloadString 4\t網路下載純文字檔案......\n";

            string url2 = "http://jsonplaceholder.typicode.com/posts";

            WebClient wc2 = new WebClient();     // 建立 WebClient
            wc2.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            wc2.Headers.Add(HttpRequestHeader.ContentType, "application/json");  // 指定 WebClient 的 Content-Type header

            // 從網路 url 上取得資料
            var result2 = wc2.DownloadString(url2);
            richTextBox1.Text += result2 + "\n";

            richTextBox1.Text += "\nWebClient DownloadString 測試\t完成\n";
            this.Cursor = Cursors.Default;
        }

        private void DownloadFile(string url, string filename)
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            try
            {
                wc.DownloadFile(url, filename);     // Download the file.
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
            /*
            finally
            {
                if (!File.Exists(filename))
                {
                    richTextBox1.Text += "下載 : " + filename + "\tNG\n";
                }
                else
                {
                    richTextBox1.Text += "下載 : " + filename + "\tOK\n";
                }
            }
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //WebClient DownloadFile for COVID-19   下載COVID-19資料
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient測試\t下載COVID-19資料a......\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            string url = "https://covidtracking.com/api/v1/states/daily.csv";

            //richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
            Application.DoEvents();
            DownloadFile(url, filename_covid19a);

            richTextBox1.Text += "\nWebClient測試\t下載COVID-19資料b......\n";
            //richTextBox1.Text += "Loading case data......\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
            Application.DoEvents();
            DownloadFile(url, filename_covid19b);
            richTextBox1.Text += "\nWebClient測試\t下載COVID-19資料\t完成\n";

            this.Cursor = Cursors.Default;
        }

        private WebClient wc = new WebClient();     // 建立 WebClient
        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟一個Thread, 下載一個網頁......\n";
            Application.DoEvents();
            Thread th = new Thread(new ThreadStart(StartDownload));
            th.Start();
        }

        private void StartDownload()
        {
            string url0 = "http://weisico.com/program/2015/0630/237.html";
            int n = url0.LastIndexOf("/");
            string url = url0;//.Substring(0, n);
            string fileName = url0.Substring(n + 1, url0.Length - n - 1);
            string Dir = @"D:\_git\vcs\_1.data\______test_files1\";
            //下载文件，直接覆盖
            string Path = Dir + fileName;

            //Datetime.Now.ToFileTime.ToString()用于区别下载时间
            // string Path = Dir +DateTime.Now.ToFileTime().ToString() + fileName  ;

            try
            {
                Stream stream = wc.OpenRead(url);
                StreamReader reader = new StreamReader(stream);

                FileStream outputStream = new FileStream(Path, FileMode.OpenOrCreate);
                try
                {
                    int bufferSize = 100; // 网络速度快的话可以设置大一点，慢的话可以小一点
                    int nRealCount;
                    byte[] bBuffer = new byte[bufferSize];
                    nRealCount = stream.Read(bBuffer, 0, bufferSize);

                    // 下载，一面读一面下载是最好的方式。这样就不用声明多大的数组了
                    while (nRealCount > 0)
                    {
                        outputStream.Write(bBuffer, 0, nRealCount);
                        nRealCount = stream.Read(bBuffer, 0, bBuffer.Length);
                    }
                    MessageBox.Show("下載完成, 檔案 : " + Path);
                }
                catch (WebException ex)
                {
                    MessageBox.Show("下載錯誤, 原因 : " + ex.Message);
                }
                finally
                {
                    stream.Close();
                    reader.Close();
                    outputStream.Close();
                }
                //Application.Exit();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                //MessageBox.Show("请输入正确的文件地址");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //WebClient DownloadData
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient DownloadData 1\t下載一個網頁......\n";
            Application.DoEvents();

            string url = "http://google.com.tw";
            //string url = "http://www.yahoo.com.tw";
            string web_data = "";

            WebClient wc1 = new WebClient();     // 建立 WebClient
            wc1.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");
            try
            {
                byte[] bd = wc1.DownloadData(url);
                web_data = (Encoding.Default.GetString(bd));
                richTextBox1.Text += "抓取網頁成功\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "\nWebClient DownloadData 2\t取得網頁純文字檔......\n";
            Application.DoEvents();

            url = "http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP950.TXT";
            string result = "";
            WebClient wc2 = new WebClient();     // 建立 WebClient
            try
            {
                url = url.Trim();
                if (!url.ToLower().StartsWith("http"))
                {
                    url = "http://" + url;
                }

                MemoryStream image_stream = new MemoryStream(wc2.DownloadData(url));
                StreamReader reader = new StreamReader(image_stream);
                result = reader.ReadToEnd();
                reader.Close();
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
            if (result != "")
            {
                //richTextBox1.Text += result + "\n";
            }

            richTextBox1.Text += "\nWebClient DownloadData 3\t圖片下載並顯示......\n";
            Application.DoEvents();

            url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            richTextBox1.Text += "圖片所在網址 : " + url + "\n";

            WebClient wc3 = new WebClient();     // 建立 WebClient
            try
            {
                //圖片下載並顯示
                Image img = null;

                try
                {
                    MemoryStream image_stream = new MemoryStream(wc3.DownloadData(url));
                    img = Image.FromStream(image_stream);
                }
                catch (WebException ex)
                {
                    richTextBox1.Text += "WebException\t" + ex.Message + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "Error\t" + ex.Message + "\n";
                }

                if (img == null)
                {
                    richTextBox1.Text += "圖片下載\t失敗\n";

                }
                else
                {
                    pictureBox1.Image = img;
                    richTextBox1.Text += "圖片下載並顯示\tOK\n";
                    Application.DoEvents();
                }
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "\nWebClient DownloadData 4\t網頁資料下載並顯示......\n";
            Application.DoEvents();

            //string url4 = "https://www.google.com.tw/";
            string url4 = "http://antwrp.gsfc.nasa.gov/apod/";
            WebClient wc4 = new WebClient();     // 建立 WebClient

            // Download home page data.
            richTextBox1.Text += "Downloading " + url4 + " ...\n";

            // Download the Web resource and save it into a data buffer.
            //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            byte[] data = wc4.DownloadData(url4);

            // Display the downloaded data.
            string result4 = Encoding.ASCII.GetString(data);
            richTextBox1.Text += result4 + "\n";

            richTextBox1.Text += "\nWebClient DownloadData 測試\t完成\n";

            this.Cursor = Cursors.Default;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //WebClient OpenRead
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient OpenRead\t取得網頁資料並存成檔案......\n";
            Application.DoEvents();

            string url = "file:///D:/_git/vcs/_1.data/_html/My_Link.html";
            //string url = "https://www.google.com.tw/";

            WebClient wc = new WebClient();     // 建立 WebClient
            try
            {
                Stream response = wc.OpenRead(url); // Get the indicated URL.
                richTextBox1.Text += "取得網頁資料並存成檔案, len = " + response.Length.ToString() + "\n";
                richTextBox1.Text += "CanSeek = " + response.CanSeek.ToString() + "\n";

                // Read the result.
                using (StreamReader stream_reader = new StreamReader(response))
                {
                    // Get the results.
                    string result = stream_reader.ReadToEnd();

                    // Close the stream reader and its underlying stream.
                    stream_reader.Close();

                    //richTextBox1.Text += result + "\n";

                    int pos1 = url.LastIndexOf('/');
                    int pos2 = url.LastIndexOf('.');

                    if (pos2 > pos1)
                    {
                        string filename = Application.StartupPath + "\\" + url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
                        richTextBox1.Text += "存檔檔名 : " + filename + "\n";

                        StreamWriter sw = File.CreateText(filename);
                        sw.Write(result);
                        sw.Close();
                    }
                }
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }


            richTextBox1.Text += "WebClient OpenRead\t取得網頁資料並存成檔案......2\n";

            string url2 = "http://jsonplaceholder.typicode.com/posts";

            WebClient wc2 = new WebClient();     // 建立 WebClient
            // Add a user agent header in case the requested URI contains a query.
            wc2.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)");

            using (Stream stream = wc2.OpenRead(url2))        // 從 url2 讀取資訊至 stream
            {
                using (StreamReader sr = new StreamReader(stream))      // 使用 StreamReader 讀取 stream 內的字元
                {
                    string result2 = sr.ReadToEnd();        // 將 StreamReader 所讀到的字元轉為 string
                    richTextBox1.Text += result2 + "\n";
                    sr.Close();
                }
                stream.Close();
            }

            this.Cursor = Cursors.Default;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //WebClient DownloadFile
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient DownloadFile\t取得網頁檔案......\n";
            Application.DoEvents();

            string url = "";
            string filename = "";

            //url = "https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/31/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-31-1.9.iso";    //從FTP下載檔案  ok
            url = "http://www.csharphelper.com/examples/howto_download_file.zip";    //ok
            //url = "http://s.pimg.tw/qrcode/charleslin74/blog.png";  //ok
            //url = "https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";  //ok
            //url = "http://snowball.tartarus.org/otherlangs/english_cpp.txt";    //ok

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');

            if (pos2 > pos1)
            {
                richTextBox1.Text += "遠端檔案: " + url + "\n";
                filename = Application.StartupPath + "\\" + url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
                richTextBox1.Text += "存檔檔名 : " + filename + "\n";
                richTextBox1.Text += "\n開始下載檔案...\n\n";
                Application.DoEvents();
                DownloadFile(url, filename);
                richTextBox1.Text += "下載完成\n";
            }

            richTextBox1.Text += "WebClient DownloadFile\t取得網頁檔案......2\n";

            //https://upload.wikimedia.org/wikipedia/commons/b/be/%E7%90%89%E7%90%83%E5%AE%AB%E5%BB%B7%E9%9F%B3%E4%B9%90.jpg
            //http://www.csharphelper.com/essential_algs_2e_251_317.jpg
            string url2 = "https://www.cwb.gov.tw/Data/satellite/";
            string filename2 = "LCC_IR1_CR_2750/LCC_IR1_CR_2750.jpg";
            string myStringWebResource = null;

            WebClient wc = new WebClient();     // 建立 WebClient

            //wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            wc.Headers.Add(HttpRequestHeader.ContentType, "application/json");  // 指定 WebClient 的 Content-Type header
            //wc.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)");

            // Concatenate the domain with the Web resource filename.
            myStringWebResource = url2 + filename2;
            richTextBox1.Text += "Downloading File " + filename2 + " from " + myStringWebResource + "\n";
            // Download the Web resource and save it into the current filesystem folder.
            try
            {
                wc.DownloadFile(myStringWebResource, filename2);
                richTextBox1.Text += "OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";

            }

            this.Cursor = Cursors.Default;
        }

        //讓 WebClient 擁有 Timeout 功能 ST
        public class MyWebClient : WebClient
        {
            protected override WebRequest GetWebRequest(Uri uri)
            {
                WebRequest WR = base.GetWebRequest(uri);
                WR.Timeout = 30 * 1000;     //30秒
                return WR;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //WebClient 讓 WebClient 擁有 Timeout 功能
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "WebClient DownloadString\t讓 WebClient 擁有 Timeout 功能......\n";
            Application.DoEvents();

            string url = @"http://www.google.com.tw/";
            MyWebClient MWC = new MyWebClient();
            string HTML = MWC.DownloadString(url);
            richTextBox1.Text += HTML;
            this.Cursor = Cursors.Default;
        }
        //讓 WebClient 擁有 Timeout 功能 SP

        //下載NASA網頁的圖片 ST
        private void button5_Click(object sender, EventArgs e)
        {
            //目前Kilo不可用
            //目前Romeo不可用

            //目前Sugar可用

            Cursor = Cursors.WaitCursor;
            get_nasa_picture();
            Cursor = Cursors.Default;
        }

        void get_nasa_picture()
        {
            string url = "http://antwrp.gsfc.nasa.gov/apod/";
            try
            {
                richTextBox1.Text += "開啟 NASA 圖片網址 : " + url + "\n";
                webBrowser1.Navigate(url);  // Load the web page.
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Error navigating to " + url + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
        }

        // The web page has loaded. Get the APOTD image.
        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            richTextBox1.Text += "NASA 圖片網站主頁下載完畢, 從網頁資料擷取圖片所在網址\n";
            // Get the image's URL.
            HtmlDocument doc = webBrowser1.Document;
            string img_src_url = doc.Images[0].GetAttribute("src");

            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";

            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔完成\n";

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示完成\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Download Error" + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            WebClient wc = new WebClient();     // 建立 WebClient

            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Download the file.
            wc.DownloadFile(url, filename);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            try
            {
                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream = new MemoryStream(wc.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
                return null;
            }
        }

        //下載NASA網頁的圖片 SP

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //提取並保存網頁源碼 ST
        string url = @"http://www.google.com";

        public string strS;//存取網頁內容
        public void GetPageSource()
        {
            string strAddress = url.Trim();//輸入網址
            if (ValidateDate1(strAddress))//檢查輸入網址是否合法
            {
                strAddress = strAddress.ToLower();
                strS = GetSource(strAddress);//呼叫方法提取網頁內容
                if (strS.Length > 1)
                {
                    showSource();  //設定視窗樣式
                }
            }
            else
            {
                MessageBox.Show("輸入網址不正確請從新輸入");
            }
        }
        //設定視窗樣式
        private void showSource()
        {
            richTextBox1.Text += strS;   //顯示網頁內容
        }


        //保存網頁訊息
        private void saveInfo(string strPath, string strDown)
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            wc.DownloadFile(strDown, strPath);
        }

        //驗證網址是否正確
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }
        //提取網頁內容。
        public string GetSource(string webAddress)
        {
            StringBuilder strSource = new StringBuilder("");
            try
            {

                WebRequest WReq = WebRequest.Create(webAddress);//對URl地址發出請求
                WebResponse WResp = WReq.GetResponse();//傳回服務器的響應
                StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//從數據流中讀取數據
                string strTemp = "";
                while ((strTemp = sr.ReadLine()) != null)//循環讀出數據
                {
                    strSource.Append(strTemp + "\r\n");//把數據新增到字串中
                }
                sr.Close();
            }
            catch (WebException WebExcp)
            {
                MessageBox.Show(WebExcp.Message, "error", MessageBoxButtons.OK);
            }
            return strSource.ToString();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //提取並保存網頁源碼
            GetPageSource();//取得網頁編碼

            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";

            saveInfo(filename, this.url.Trim().ToString());
            MessageBox.Show("保存成功");
        }
        //提取並保存網頁源碼 SP

        private void button11_Click(object sender, EventArgs e)
        {
            // 網頁抓取星座占卜資料
            // 透過 Regex 取得星座資料
            // http://vip.astro.sina.com.cn/astro/view/libra
            var fate = StarSignsUtil.GetFateToday("天秤座");
            richTextBox1.Text += fate.StarSign.Title + "\n";
            richTextBox1.Text += fate.StarSign.Id + "\n";
            richTextBox1.Text += fate.StarSign.DateRange + "\n";

            richTextBox1.Text += fate.Date + "\n";

            richTextBox1.Text += fate.Desc + "\n";

            richTextBox1.Text += "顯示此Dictionary的資料\n";
            richTextBox1.Text += "共有 " + fate.Datas.Count.ToString() + " 筆資料\n";

            foreach (string n in fate.Datas.Keys)
            {
                richTextBox1.Text += "Keys = " + n + "\tValues = " + fate.Datas[n] + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            byte[] buffer = wc.DownloadData("http://k-db.com/?p=all&download=csv");
            string str = Encoding.Default.GetString(buffer);
            string[] rows = str.Split(new string[] { Environment.NewLine }, StringSplitOptions.None);

            richTextBox1.Text += "len = " + rows.Length.ToString() + "\n";
            foreach (string r in rows)
            {
                richTextBox1.Text += r + "\n";
            }

            // １行目をラベルに表示

            richTextBox1.Text += "取得第一行資料 : " + rows[0] + "\n";

            // ２行目以下はカンマ区切りから文字列の配列に変換しておく
            List<string[]> list = new List<string[]>();
            rows.ToList().ForEach(row => list.Add(row.Split(new char[] { ',' })));

            // ヘッダの作成（データバインド用の設計）
            list.First().Select((item, cnt) => new { Count = cnt, Item = item }).ToList().ForEach(header =>
            {
                /*
                    {
                        Header = header.Item,
                        DisplayMemberBinding = new Binding(string.Format("[{0}]", header.Count))
                    };
                */
            });
        }

        public string[] GetCSVData()
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            byte[] buffer = wc.DownloadData("http://k-db.com/?p=all&download=csv");
            string str = Encoding.Default.GetString(buffer);
            return str.Split(new string[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string[] rows = GetCSVData();
            richTextBox1.Text += "len = " + rows.Length.ToString() + "\n";
            foreach (string r in rows)
            {
                richTextBox1.Text += r + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //WebClient 1
            //string sourceResource = "http://blogs.telerik.com/images/default-source/miroslav-miroslav/super_ninja.png?sfvrsn=2";
            string sourceResource = @"https://www.telerik.com/sfimages/default-source/blogs/super_ninja-png";
            string localFileName = Path.GetFileName(sourceResource);
            using (WebClient wc = new WebClient())  // 建立 WebClient
            {
                try
                {
                    richTextBox1.Text += "開始下載: " + sourceResource + "\n";
                    //Console.WriteLine("Start downloading {0}", sourceResource);
                    wc.DownloadFile(sourceResource, localFileName);
                    richTextBox1.Text += "下載完成, 在 bin/Debug\n";
                }
                catch (WebException ex)
                {
                    Console.Write(ex.Message);
                    if (ex.InnerException != null)
                    {
                        Console.WriteLine(" " + ex.InnerException.Message);
                        richTextBox1.Text += "下載失敗1, 原因 :\t" + ex.InnerException.Message + "\n";
                    }
                    else
                    {
                        Console.WriteLine();
                        richTextBox1.Text += "下載失敗3\n";
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Something going wrong. Details: " + ex.Message);
                    richTextBox1.Text += "下載失敗2, 原因 :\t" + ex.Message + "\n";
                }
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //WebClient 2
            WebClient wc = new WebClient();     // 建立 WebClient
            try
            {
                //wc.DownloadFile(url, fileName);
                wc.DownloadFile("http://www.devbg.org/img/Logo-BASD.jpg", @"C:\dddddddddd\txt.jpg");
                richTextBox1.Text += "下載完成\n";
            }
            catch (ArgumentException ae)
            {
                Console.WriteLine("{0} - {1}", ae.GetType(), ae.Message);
            }
            catch (WebException webEx)
            {
                Console.WriteLine("{0} - {1}", webEx.GetType(), webEx.Message);
                Console.WriteLine("Destination not found!");
            }
            catch (NotSupportedException supportEx)
            {
                Console.WriteLine("{0} - {1}", supportEx.GetType(), supportEx.Message);
                Console.WriteLine(supportEx.Message);
            }
            catch (Exception allExp)
            {
                Console.WriteLine("{0} - {1}", allExp.GetType(), allExp.Message);
            }
        }

        public string SendSms(List<string> mobiles)
        {
            using (WebClient wc = new WebClient())    // 建立 WebClient
            {
                try
                {
                    string langCode = "1";
                    if (Regex.IsMatch("lion-mouse", @"\p{IsArabic}+") == true)
                    {
                        langCode = "2";
                    }

                    wc.Headers.Add("content-type", "text/plain");
                    string mobile = String.Join(",", mobiles.ToArray());
                    string result = wc.DownloadString(String.Format("http://brazilboxtech.com/api/send.aspx?username=smartksa&password=ksasmrt95647&language={0}&sender=NCSS&mobile={1}&message={2}", langCode, mobile, "lion-mouse"));
                    if (result.StartsWith("OK"))
                    {
                        return String.Empty;
                    }
                    return result;
                }
                catch (Exception ex)
                {

                    return ex.Message;
                }
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //WebClient 3
            //List<string[]> camera_serials = new List<string[]>();
            List<string> mobiles = new List<string>();
            mobiles.Clear();
            mobiles.Add("0922188156");
            string result = SendSms(mobiles);
            richTextBox1.Text += "result = " + result + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //WebClient 4 解讀一個XML網頁資料

            return;

            //URL 未定

            //分析一個網頁回傳的XML資料
            try
            {
                string xml;
                using (WebClient wc = new WebClient())  // 建立 WebClient
                {
                    xml = wc.DownloadString("url" + "/main.xml");
                }
                XmlDocument xmlDocument = new XmlDocument();
                xmlDocument.LoadXml(xml);
                XmlNodeList elementsByTagName = xmlDocument.GetElementsByTagName("repofile");
                XmlNodeList elementsByTagName2 = ((XmlElement)elementsByTagName[0]).GetElementsByTagName("information");
                foreach (XmlElement xmlElement in elementsByTagName2)
                {
                    XmlNodeList elementsByTagName3 = xmlElement.GetElementsByTagName("id");
                    XmlNodeList elementsByTagName4 = xmlElement.GetElementsByTagName("name");
                    string s0 = elementsByTagName4[0].InnerText;
                    string s1 = elementsByTagName3[0].InnerText;
                }
                XmlNodeList elementsByTagName5 = ((XmlElement)elementsByTagName[0]).GetElementsByTagName("category");
                foreach (XmlElement xmlElement2 in elementsByTagName5)
                {
                    XmlNodeList elementsByTagName3 = xmlElement2.GetElementsByTagName("id");
                    XmlNodeList elementsByTagName4 = xmlElement2.GetElementsByTagName("name");
                    //GClass2 gClass = new GClass2();
                    string s2 = elementsByTagName4[0].InnerText;
                    string s3 = elementsByTagName3[0].InnerText;
                }
            }
            catch
            {
            }
        }

        public void LoadData()
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            wc.DownloadStringAsync(new Uri("http://data.taipei.gov.tw/opendata/apply/json/RjQzRThDNjUtMzU3OS00MTU5LUEwOUEtMUI2NzFDOTE5NDcz"));
            wc.DownloadStringCompleted += wc_DownloadStringCompleted;
        }

        void wc_DownloadStringCompleted(object sender, DownloadStringCompletedEventArgs e)
        {
            //e.Result
        }

        private void button18_Click(object sender, EventArgs e)
        {
            LoadData();
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //WebClient 1
            WebClient wc = new WebClient();
            wc.BaseAddress = "http://www.juedui100.com/";   //設置根目錄
            wc.Encoding = Encoding.UTF8;                    //設置按照何種編碼訪問，如果不加此行，獲取到的字符串中文將是亂碼
            string str = wc.DownloadString("/");
            Console.WriteLine(str);


            //----------------------以下為OpenRead()以流的方式讀取----------------------
            wc.Headers.Add("Accept", "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*");
            wc.Headers.Add("Accept-Language", "zh-cn");
            wc.Headers.Add("UA-CPU", "x86");
            //wc.Headers.Add("Accept-Encoding","gzip, deflate");    //因為我們的程序無法進行gzip解碼所以如果這樣請求獲得的資源可能無法解碼。當然我們可以給程序加入gzip處理的模塊 那是題外話了。
            wc.Headers.Add("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)");
            //Headers   用於添加添加請求的頭信息
            System.IO.Stream objStream = wc.OpenRead("user/6974068.html");      //獲取訪問流
            System.IO.StreamReader _read = new System.IO.StreamReader(objStream, System.Text.Encoding.UTF8);    //新建一個讀取流，用指定的編碼讀取，此處是utf-8
            Console.Write(_read.ReadToEnd());   //輸出讀取到的字符串

            //------------------------DownloadFile下載文件-------------------------------
            wc.DownloadFile("http://www.baidu.com/img/shouye_b5486898c692066bd2cbaeda86d74448.gif", @"D:\123.gif");     //將遠程文件保存到本地
            //------------------------DownloadFile下載到字節數組-------------------------------
            byte[] bytes = wc.DownloadData("http://www.baidu.com/img/shouye_b5486898c692066bd2cbaeda86d74448.gif");
            FileStream fs = new FileStream(@"E:\123.gif", FileMode.Create);
            fs.Write(bytes, 0, bytes.Length);
            fs.Flush();

            WebHeaderCollection whc = wc.ResponseHeaders;   //獲取響應頭信息
            foreach (string s in whc)
            {
                Console.WriteLine(s + ":" + whc.Get(s));
            }

            Console.WriteLine(wc.QueryString.Count);    //輸出0

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //WebClient 2

            //異步下載頁面的例子：
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;                    //設置按照何種編碼訪問，如果不加此行，獲取到的字符串中文將是亂碼
            wc.DownloadStringCompleted += new DownloadStringCompletedEventHandler(DownComplete);
            wc.DownloadStringAsync(new Uri("http://www.juedui100.com/"));
            Console.WriteLine("下載!");
        }

        public static void DownComplete(object sender, DownloadStringCompletedEventArgs e)
        {
            Console.WriteLine(sender.ToString());   //輸出 System.Net.WebClient   觸發事件的對象
            Console.WriteLine(e.Result);    //輸出頁面源代碼
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //WebClient 3
            //將數據下載到字節數組：
            WebClient wc = new WebClient();
            //直接下載
            wc.DownloadFile("http://24.duote.com.cn/kugou.zip", @"ku.zip");
            Console.WriteLine("下載完成了嗎？");   //下載完成後輸出 下載完成了嗎？

            //將數據下載到字節數組
            byte[] byteArr = wc.DownloadData("http://24.duote.com.cn/kugou.zip");
            FileStream fs = new FileStream(@"D:\kugo.zip", FileMode.OpenOrCreate, FileAccess.ReadWrite);
            fs.Write(byteArr, 0, byteArr.Length);

            //至於異步與下載雷同

            Console.WriteLine("現在完成了還是沒完成呢？");
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {
            WebClient webClient = new WebClient();
            string publicIp = webClient.DownloadString("https://api.ipify.org");
            richTextBox1.Text += "My public IP Address is: " + publicIp + "\n";
            Console.WriteLine("My public IP Address is: {0}", publicIp);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //取得 SecurityProtocol
            //GetSecurityProtocol();
            ServicePointManager.SecurityProtocol = GetSecurityProtocol();
        }

        private static SecurityProtocolType GetSecurityProtocol()
        {
            var result = 0;
            foreach (var value in Enum.GetValues(typeof(SecurityProtocolType)))
            {
                result += (int)value;
                Console.WriteLine(result.ToString());
            }

            return (SecurityProtocolType)result;
        }

    }

    public static class StarSignsUtil
    {
        /// <summary>
        /// 紀錄星座資料的模型
        /// </summary>
        public class StarSignInfo
        {
            public string Title { get; set; }
            public string Id { get; set; }
            public string DateRange { get; set; }
        }

        /// <summary>
        /// 查詢後的回應資料
        /// </summary>
        public class FateResult
        {
            public StarSignInfo StarSign { get; set; }
            public string Date { get; set; }


            public string Desc { get; set; }


            public System.Collections.Generic.Dictionary<string, string> Datas { get; set; }

            public FateResult()
            {
                Datas = new System.Collections.Generic.Dictionary<string, string>();
            }

        }

        /// <summary>
        /// 星座資料
        /// </summary>
        public static System.Collections.Generic.List<StarSignInfo> Datas { get; set; }


        //Ctor
        static StarSignsUtil()
        {
            Datas = new System.Collections.Generic.List<StarSignInfo>();
            Datas.Add(new StarSignInfo { Title = "白羊座", Id = "aries", DateRange = "03/21-04/19" });
            Datas.Add(new StarSignInfo { Title = "金牛座", Id = "taurus", DateRange = "04/20-05/20" });
            Datas.Add(new StarSignInfo { Title = "雙子座", Id = "gemini", DateRange = "05/21-06/21" });
            Datas.Add(new StarSignInfo { Title = "巨蟹座", Id = "cancer", DateRange = "06/22-07/22" });
            Datas.Add(new StarSignInfo { Title = "獅子座", Id = "leo", DateRange = "07/23-08/22" });
            Datas.Add(new StarSignInfo { Title = "處女座", Id = "virgo", DateRange = "08/23-09/22" });
            Datas.Add(new StarSignInfo { Title = "天秤座", Id = "libra", DateRange = "09/23-10/23" });
            Datas.Add(new StarSignInfo { Title = "天蠍座", Id = "scorpio", DateRange = "10/24-11/22" });
            Datas.Add(new StarSignInfo { Title = "射手座", Id = "sagittarius", DateRange = "11/23-12/21" });
            Datas.Add(new StarSignInfo { Title = "魔羯座", Id = "capricorn", DateRange = "12/22-01/19" });
            Datas.Add(new StarSignInfo { Title = "水瓶座", Id = "aquarius", DateRange = "01/20-02/18" });
            Datas.Add(new StarSignInfo { Title = "雙魚座", Id = "pisces", DateRange = "02/19-03/20" });
        }


        public static FateResult GetFateToday(string title)
        {
            var sInfo = Datas.SingleOrDefault(x => x.Title == title);
            if (sInfo == null)
            {
                throw new System.Exception("此星座我沒有找到");
            }


            var result = new StarSignsUtil.FateResult();
            result.StarSign = sInfo;

            string url = @"http://vip.astro.sina.com.cn/astro/view/" + sInfo.Id + "/";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            string source = wc.DownloadString(url);
            //MessageBox.Show(sInfo.Id);

            var regex = new System.Text.RegularExpressions.Regex(@"<div class=[\s""']tab[\s""']><h4>(?<KEY>.*?)</h4><p>(?<VALUE>.*?)</p>", System.Text.RegularExpressions.RegexOptions.IgnoreCase);
            System.Text.RegularExpressions.MatchCollection matches = regex.Matches(source);
            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {
                    var k = match.Groups["KEY"].Value.Replace("&nbsp;", "");
                    var v = match.Groups["VALUE"].Value.Replace("&nbsp;", "");
                    if (!string.IsNullOrEmpty(k) && !string.IsNullOrEmpty(v) && !result.Datas.ContainsKey(k))
                    {
                        result.Datas.Add(k, v);
                    }
                    //MessageBox.Show(k);
                    //MessageBox.Show(v);
                }
            }

            regex = new System.Text.RegularExpressions.Regex(@"&lt;p&gt;(?<VALUE>.*?)&lt;/p&gt", System.Text.RegularExpressions.RegexOptions.IgnoreCase | System.Text.RegularExpressions.RegexOptions.Singleline);
            matches = regex.Matches(source);

            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {

                    var v = match.Groups["VALUE"].Value.Trim();

                    if (!string.IsNullOrEmpty(v))
                    {
                        if (v.Contains("："))
                        {
                            result.Datas.Add(v.Split('：')[0].Trim(), v.Split('：')[1].Trim());
                        }
                        else
                        {
                            result.Desc = v.Trim();
                        }
                    }
                }
            }

            regex = new System.Text.RegularExpressions.Regex(@"有效日期:(?<VALUE>.*?)</li>", System.Text.RegularExpressions.RegexOptions.IgnoreCase | System.Text.RegularExpressions.RegexOptions.Singleline);
            matches = regex.Matches(source);
            foreach (System.Text.RegularExpressions.Match match in matches)
            {
                if (match.Success)
                {

                    result.Date = match.Groups["VALUE"].Value.Trim();
                }
            }
            return result;
        }
    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
}

/*

        private void SendGETRequest(string url)
        {
            using (WebClient wc = new WebClient())  // 建立 WebClient
            {
                wc.DownloadStringAsync(new Uri(url));
            }
        }

*/


