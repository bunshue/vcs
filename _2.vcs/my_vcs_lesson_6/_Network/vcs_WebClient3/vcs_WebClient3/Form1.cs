using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Path
using System.Net;
using System.Xml;
using System.Text.RegularExpressions;

namespace vcs_WebClient3
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
            this.label1.Text = rows[0];
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

        private void button2_Click(object sender, EventArgs e)
        {
            string[] rows = GetCSVData();
            richTextBox1.Text += "len = " + rows.Length.ToString() + "\n";
            foreach (string r in rows)
            {
                richTextBox1.Text += r + "\n";
            }
        }


        private void SendGETRequest(string url)
        {
            using (WebClient wc = new WebClient())  // 建立 WebClient
            {
                wc.DownloadStringAsync(new Uri(url));
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
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

        private void button4_Click(object sender, EventArgs e)
        {
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

        private void button5_Click(object sender, EventArgs e)
        {
            //List<string[]> camera_serials = new List<string[]>();
            List<string> mobiles = new List<string>();
            mobiles.Clear();
            mobiles.Add("0922188156");
            string result = SendSms(mobiles);
            richTextBox1.Text += "result = " + result + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
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

        private void button7_Click(object sender, EventArgs e)
        {
            LoadData();
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
    }
}
