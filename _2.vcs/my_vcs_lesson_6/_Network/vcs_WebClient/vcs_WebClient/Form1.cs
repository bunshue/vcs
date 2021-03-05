using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream
using System.Threading; //for Thread

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
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //for Romeo and Sugar    3072
            //ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            //ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */



            /*
            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            using (WebClient client1 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    string data = client1.DownloadString(url_file1);          //抓網頁資料到記憶體
                    //richTextBox1.Text += data + "\n";
                    richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            using (WebClient client2 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                    int pos1 = url_file2.LastIndexOf('/');
                    int pos2 = url_file2.LastIndexOf('.');
                    string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
                    richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

                    client2.DownloadFile(url_file2, filename_local);          //抓網頁資料到本地檔案
                    richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
            using (WebClient client3 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    // Get the response string from the URL.
                    string xml = client3.DownloadString(url_weather);        //抓資料
                    //richTextBox1.Text += "data\n" + xml + "\n";
                    richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔\tOK\n";
                Application.DoEvents();

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示\tOK\n";
                Application.DoEvents();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Download Error" + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
            Application.DoEvents();


            //下載COVID-19資料

            // Compose the local data file name.
            string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            string url = "https://covidtracking.com/api/v1/states/daily.csv";

            richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
            Application.DoEvents();

            DownloadFile(url, filename_covid19a);


            richTextBox1.Text += "Loading case data...\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
            DownloadFile(url, filename_covid19b);
            */




            //取得網頁資料並存成檔案

            string url = "file:///C:/_git/vcs/_1.data/_html/My_Link.html";
            //string url = "https://www.google.com.tw/";

            // Get the response.
            try
            {
                // Make a WebClient.
                WebClient client = new WebClient();


                try
                {
                    Stream response = client.OpenRead(url); // Get the indicated URL.
                    richTextBox1.Text += "取得網頁資料並存成檔案, len = " + response.Length.ToString() + "\n";

                    richTextBox1.Text += "CanSeek = " + response.CanSeek.ToString() + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }


                return;

                /*
                // Read the result.
                using (StreamReader stream_reader = new StreamReader(response))
                {
                    // Get the results.
                    string result = stream_reader.ReadToEnd();


                    // Close the stream reader and its underlying stream.
                    stream_reader.Close();

                    richTextBox1.Text += result + "\n";


                    string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";
                    StreamWriter sw = File.CreateText(filename);
                    sw.Write(result);
                    sw.Close();

                }
                 */

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Read Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            // Make a WebClient.
            WebClient client = new WebClient();

            /*
            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            */

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');
            string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
            richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Download the file.
            client.DownloadFile(url, filename);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            try
            {
                WebClient client = new WebClient();

                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream = new MemoryStream(client.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
                return null;
            }
        }

        private void DownloadFile(string url, string filename)
        {
            try
            {
                // Make a WebClient.
                WebClient client = new WebClient();

                // Download the file.
                client.DownloadFile(url, filename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
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
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //下載檔案的範例 - 使用WebClient
            WebClient client = new WebClient();
            client.DownloadFile("http://s.pimg.tw/qrcode/charleslin74/blog.png", "C:\\______test_files\\blog.png");
            richTextBox1.Text += "下載完成\n";

        }

        private WebClient client = new WebClient();
        private void button3_Click(object sender, EventArgs e)
        {
            //下載一個網頁1
            Thread th = new Thread(new ThreadStart(StartDownload));
            th.Start();
        }

        private void StartDownload()
        {
            string URL = "http://weisico.com/program/2015/0630/237.html";
            int n = URL.LastIndexOf("/");
            string URLAddress = URL;//.Substring(0, n);
            string fileName = URL.Substring(n + 1, URL.Length - n - 1);
            string Dir = @"C:\______test_files\";
            //下载文件，直接覆盖
            string Path = Dir + fileName;

            //Datetime.Now.ToFileTime.ToString()用于区别下载时间
            // string Path = Dir +DateTime.Now.ToFileTime().ToString() + fileName  ;

            try
            {
                WebRequest myre = WebRequest.Create(URLAddress);

                Stream stream = client.OpenRead(URLAddress);
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
                    MessageBox.Show("下載完成!");
                }
                catch (WebException ex)
                {
                    MessageBox.Show(ex.Message, "Error");
                    this.Text = "";
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
            //下載一個網頁2
            string strURL = "http://google.com.tw";
            //string strURL = "http://www.yahoo.com.tw";
            string web_data = GetWebPage(strURL);
            if (web_data == "fail")
                richTextBox1.Text += "抓取網頁失敗";
            else
                richTextBox1.Text += "抓取網頁成功";
        }

        public String GetWebPage(String sURL)
        {
            try
            {
                WebClient client = new WebClient();
                client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");
                byte[] bd = client.DownloadData(sURL);
                return (Encoding.Default.GetString(bd));
            }
            catch
            {
                return ("fail");
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //網路下載純文字檔案
            try
            {
                //下載純文字
                WebClient client = new WebClient();
                string somestring = client.DownloadString("http://snowball.tartarus.org/otherlangs/english_cpp.txt");
                richTextBox1.Text += somestring;
            }
            catch (WebException ex)
            {
                // add some kind of error processing
                richTextBox1.Text += ex.ToString() + "n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得網頁資料並存成檔案

            //取得網頁資料並存成檔案

            string url = "file:///C:/_git/vcs/_1.data/_html/My_Link.html";
            // Get the response.
            try
            {
                // Get the web response.
                string result = GetWebResponse(url);
                //Console.WriteLine(result.Replace("\\r\\n", "\r\n"));
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Read Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        // Get a web response.
        private string GetWebResponse(string url)
        {
            // Make a WebClient.
            WebClient client = new WebClient();

            // Get the indicated URL.
            Stream response = client.OpenRead(url);

            // Read the result.
            using (StreamReader stream_reader = new StreamReader(response))
            {
                // Get the results.
                string result = stream_reader.ReadToEnd();

                // Close the stream reader and its underlying stream.
                stream_reader.Close();

                // Return the result.

                richTextBox1.Text += result + "\n";

                string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";
                StreamWriter sw = File.CreateText(filename);
                sw.Write(result);
                sw.Close();

                return result;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //從FTP下載檔案
            WebClient client = new WebClient();
            //下載FTP檔案到指定位置
            client.DownloadFile("http://ftp.tku.edu.tw/Linux/Fedora/releases/27/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-27-1.6.iso", @"C:\______test_files\fedora27.iso");

        }

        private void button8_Click(object sender, EventArgs e)
        {
            // Download and display the text file.
            richTextBox1.Clear();
            richTextBox1.Text += "取得網頁純文字檔...\n";

            const string url = "http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP950.TXT";
            richTextBox1.Text += GetTextFile(url);
            //richTextBox1.Select(0, 500);  //useless
        }

        // Get the text file at a given URL.
        private string GetTextFile(string url)
        {
            try
            {
                url = url.Trim();
                if (!url.ToLower().StartsWith("http")) url = "http://" + url;
                WebClient client = new WebClient();
                MemoryStream image_stream = new MemoryStream(client.DownloadData(url));
                StreamReader reader = new StreamReader(image_stream);
                string result = reader.ReadToEnd();
                reader.Close();
                return result;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error downloading file " + url + '\n' + ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            return "";
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
            MyWebClient MWC = new MyWebClient();
            string HTML = MWC.DownloadString("http://www.google.com.tw/");
            richTextBox1.Text += HTML;
            //Console.WriteLine(HTML);
        }
        //讓 WebClient 擁有 Timeout 功能 SP
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
