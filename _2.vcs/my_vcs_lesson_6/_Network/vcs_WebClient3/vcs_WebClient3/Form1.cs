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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 130 + 10;
            dy = 50 + 10;

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
        }

        private void button0_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void button10_Click(object sender, EventArgs e)
        {
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

        private void button11_Click(object sender, EventArgs e)
        {
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


        private void button12_Click(object sender, EventArgs e)
        {

        //將數據下載到字節數組：
            WebClient wc = new WebClient();
            //直接下載
            wc.DownloadFile("http://24.duote.com.cn/kugou.zip", @"ku.zip");
            Console.WriteLine("下載完成了嗎？");   //下載完成後輸出 下載完成了嗎？

            //將數據下載到字節數組
            byte[] byteArr = wc.DownloadData("http://24.duote.com.cn/kugou.zip");
            FileStream fs = new FileStream(@"D:\kugo.zip",FileMode.OpenOrCreate,FileAccess.ReadWrite);
            fs.Write(byteArr,0,byteArr.Length);

            //至於異步與下載雷同
            
            Console.WriteLine("現在完成了還是沒完成呢？");


        }



        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

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
