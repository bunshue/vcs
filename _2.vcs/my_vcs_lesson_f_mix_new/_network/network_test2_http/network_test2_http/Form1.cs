using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Security;
using System.Xml;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.IO;
using System.Management;
using System.Drawing.Imaging;

using System.Security.Cryptography.X509Certificates;

using Shell32;

namespace network_test2_http
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;

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
            dx = 180;
            dy = 80;

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

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            button40.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //c# 下載網頁源碼 獲取http狀態碼
            string url = @"http://www.baidu.com";

            HttpWebRequest hwr = (HttpWebRequest)WebRequest.Create(url);
            hwr.AllowAutoRedirect = false; //不允許重定向
            hwr.Timeout = 10000; //連接超時時間設置
            hwr.Method = "GET"; //協議：GET、HEAD、POST、PUT、DELETE、TRACE 或OPTIONS。

            try
            {
                HttpWebResponse hwrs = (HttpWebResponse)hwr.GetResponse();
                MessageBox.Show(((int)hwrs.StatusCode).ToString()); //獲得http狀態碼 如:200但是404卻捕捉不到
                Stream stream = hwrs.GetResponseStream();
                MessageBox.Show(hwrs.CharacterSet); //獲取返回結果的字符編碼
                StreamReader sr = new StreamReader(stream, Encoding.GetEncoding(hwrs.CharacterSet)); //注意讀取的文字編碼格式要和寫入文件的文字編碼格式相同
                StreamWriter sw = new StreamWriter("c:\\b.html", false, Encoding.GetEncoding(hwrs.CharacterSet)); //寫入文字的編碼格式和讀取時候的編碼格式一樣
                sw.Write(sr.ReadToEnd());
                sw.Flush();
                sw.Close();
                sr.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼
            FailCount = 0;
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188493.html";
            string result = GetHtml(url);
            richTextBox1.Text += result + "\n";
        }

        //C#下載網頁HTML源碼，
        private static int FailCount = 0; //記錄下載失敗的次數

        public static string GetHtml(string url) //傳入要下載的網址
        {
            string str = string.Empty;
            try
            {
                System.Net.WebRequest request = System.Net.WebRequest.Create(url);
                request.Timeout = 10000; //下載超時時間
                request.Headers.Set("Pragma", "no-cache");
                System.Net.WebResponse response = request.GetResponse();
                System.IO.Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("gb2312");//utf-8 網頁文字編碼
                System.IO.StreamReader streamReader = new System.IO.StreamReader(streamReceive, encoding);
                str = streamReader.ReadToEnd();
                streamReader.Close();
            }
            catch (Exception ex)
            {
                FailCount++;

                if (FailCount > 5)
                {
                    var result = System.Windows.Forms.MessageBox.Show("已下載失敗" + FailCount + "次，是否要繼續嘗試？" + Environment.NewLine + ex.ToString(), "數據下載異常", System.Windows.Forms.MessageBoxButtons.YesNo, System.Windows.Forms.MessageBoxIcon.Error);
                    if (result == System.Windows.Forms.DialogResult.Yes)
                    {
                        str = GetHtml(url);
                    }
                    else
                    {
                        System.Windows.Forms.MessageBox.Show("下載HTML失敗" + Environment.NewLine + ex.ToString(), "下載HTML失敗", System.Windows.Forms.MessageBoxButtons.OK, System.Windows.Forms.MessageBoxIcon.Error);
                        throw ex;
                    }
                }
                else
                {
                    str = GetHtml(url);
                }
            }

            FailCount = 0; //如果能執行到這一步就表示下載終於成功了
            return str;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼

            string url = @"http://jsonplaceholder.typicode.com/posts";

            //建立 WebRequest 並指定目標的 uri
            WebRequest request = WebRequest.Create(url);
            // 使用 HttpWebRequest.Create 實際上也是呼叫 WebRequest.Create
            //WebRequest request = HttpWebRequest.Create(url);
            //指定 request 使用的 http verb
            request.Method = "GET";
            //使用 GetResponse 方法將 request 送出，如果不是用 using 包覆，請記得手動 close WebResponse 物件，避免連線持續被佔用而無法送出新的 request
            using (var httpResponse = (HttpWebResponse)request.GetResponse())
            //使用 GetResponseStream 方法從 server 回應中取得資料，stream 必需被關閉
            //使用 stream.close 就可以直接關閉 WebResponse 及 stream，但同時使用 using 或是關閉兩者並不會造成錯誤，養成習慣遇到其他情境時就比較不會出錯
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();

                richTextBox1.Text += result + "\n";
                //result.Dump();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼
            //要抓取的URL位址
            string url = @"http://jsonplaceholder.typicode.com/posts";

            //得到指定Url的源碼

            string strWebContent = GetWebContent(url);

            richTextBox1.Text += strWebContent + "\n";
        }

        //根據Url位址得到網頁的html源碼
        private string GetWebContent(string url)
        {
            string strResult = "";
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
                //聲明一個HttpWebRequest請求
                request.Timeout = 30000;
                //設置連接逾時時間
                request.Headers.Set("Pragma", "no-cache");
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("GB2312");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                strResult = streamReader.ReadToEnd();
            }
            catch
            {
                MessageBox.Show("出錯"); //HTTP://ike.126.com
            }
            return strResult;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼

            string url = @"http://www.google.com/webhp?hl=zh-TW";
            HttpWebRequest req = (HttpWebRequest)HttpWebRequest.Create(url);
            req.Method = "GET";
            using (WebResponse wr = req.GetResponse())
            {
                //在這裡對接收到的頁面內容進行處理
                //richTextBox1.Text += wr + "\n";
                Stream streamReceive = wr.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("Big5");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                string strResult = streamReader.ReadToEnd();

                richTextBox1.Text += strResult + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得網頁資料
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188537.html";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼

            string str = wc.DownloadString(url);

            richTextBox1.Text += str + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得網頁資料, 尋找資料
            //C#獲取網頁源碼，自動判斷網頁字符集編碼
        }

        private string getHtml(string url, string charSet)  //url是要訪問的網站地址，charSet是目標網頁的編碼，如果傳入的是null或者""，那就自動分析網頁的編碼
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            //創建WebClient實例myWebClient 
            // 需要注意的：
            //有的網頁可能下不下來，有種種原因比如需要cookie,編碼問題等等
            //這是就要具體問題具體分析比如在頭部加入cookie 
            // webclient.Headers.Add("Cookie", cookie); 
            //這樣可能需要一些重載方法。根據需要寫就可以了
            //獲取或設置用於對向 Internet 資源的請求進行身份驗證的網絡憑據。
            wc.Credentials = CredentialCache.DefaultCredentials;
            //如果服務器要驗證用戶名,密碼 
            //NetworkCredential mycred = new NetworkCredential(struser, strpassword);
            //myWebClient.Credentials = mycred; 
            //從資源下載數據並返回字節數組。（加@是因為網址中間有"/"符號）
            byte[] myDataBuffer = wc.DownloadData(url);
            string strWebData = Encoding.Default.GetString(myDataBuffer);

            //獲取網頁字符編碼描述信息
            Match charSetMatch = Regex.Match(strWebData, "<meta([^<]*)charset=([^<]*)\"", RegexOptions.IgnoreCase | RegexOptions.Multiline);
            string webCharSet = charSetMatch.Groups[2].Value;
            if (charSet == null || charSet == "")
                charSet = webCharSet;

            if (charSet != null && charSet != "" && Encoding.GetEncoding(charSet) != Encoding.Default)
                strWebData = Encoding.GetEncoding(charSet).GetString(myDataBuffer);
            return strWebData;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //C#獲取網上圖片的寬高代碼
            string url = @"http://www.aspphp.online/Skin/apsp/logo.gif";
            WebRequest request = WebRequest.Create(url);//图片src内容
            request.Credentials = CredentialCache.DefaultCredentials;

            Stream s = request.GetResponse().GetResponseStream();

            byte[] b = new byte[74373];
            MemoryStream mes_keleyi_com = new MemoryStream(b);
            s.Read(b, 0, 74373);
            s.Close();
            Image image = Image.FromStream(mes_keleyi_com);
            Console.WriteLine("高{0}，寬{1}", image.Height, image.Width);
            richTextBox1.Text += "獲取網上圖片的寬高代碼\tW = " + image.Width.ToString() + ", H = " + image.Height.ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string url = @"http://www.aspphp.online/Skin/apsp/logo.gif";

            WebRequest request = WebRequest.Create(url);//图片src内容
            WebResponse response = request.GetResponse();
            //文件流获取图片操作
            Stream reader = response.GetResponseStream();
            string path = "aaa.gif";        //图片路径命名 
            FileStream writer = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);
            byte[] buff = new byte[512];
            int c = 0;                                           //实际读取的字节数   
            while ((c = reader.Read(buff, 0, buff.Length)) > 0)
            {
                writer.Write(buff, 0, c);
            }
            //释放资源
            writer.Close();
            writer.Dispose();
            reader.Close();
            reader.Dispose();
            response.Close();
            richTextBox1.Text += "圖片下載成功, 檔案 : " + path + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        /// <summary> 
        /// 取得HTML中所有图片的 URL
        /// </summary> 
        /// <param name="sHtmlText">HTML代码</param> 
        /// <returns>图片的URL列表</returns> 
        public static string[] GetHtmlImageUrlList(string sHtmlText)
        {
            // 定义正则表达式用来匹配 img 标签 
            Regex regImg = new Regex(@"<img\b[^<>]*?\bsrc[\s\t\r\n]*=[\s\t\r\n]*[""']?[\s\t\r\n]*(?<imgUrl>[^\s\t\r\n""'<>]*)[^<>]*?/?[\s\t\r\n]*>", RegexOptions.IgnoreCase);
            // 搜索匹配的字符串 
            MatchCollection matches = regImg.Matches(sHtmlText);
            int i = 0;
            string[] sUrlList = new string[matches.Count];
            // 取得匹配项列表 
            foreach (Match match in matches)
            {
                sUrlList[i++] = match.Groups["imgUrl"].Value;
            }
            return sUrlList;
        }

        /// <summary> 
        ///根據url獲取網站html圖片並保存 
        /// </summary> 
        public void getimages(string url)
        {
            //創建一個request 同時可以配置requst其余屬性  
            System.Net.WebRequest imgRequst = System.Net.WebRequest.Create(url);
            //在這裡我是以流的方式保存圖片  
            Image downImage = Image.FromStream(imgRequst.GetResponse().GetResponseStream());
            string filename = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            downImage.Save(filename);

            downImage.Dispose();//用完一定要釋放  
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //下載圖片
            string url = @"http://www.aspphp.online/Skin/apsp/logo.gif";

            getimages(url);
        }

        /// <summary> 
        ///根據url獲取網站html內容 
        /// </summary> 
        /// <param name="url">url鏈接</param>
        /// <param name="msg">返回提示信息</param>
        public string GetHtmlContentByUrl(string url, out string msg)
        {
            string httpRequesttsdbTimeout = "30000";//超時值（以毫秒為單位）30S
            var htmlContent = string.Empty;
            try
            {
                var httpWebRequest = (HttpWebRequest)WebRequest.Create(url);
                httpWebRequest.Timeout = int.Parse(httpRequesttsdbTimeout);
                var httpWebResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                var stream = httpWebResponse.GetResponseStream();
                if (stream != null)
                {
                    var streamReader = new StreamReader(stream, Encoding.UTF8);
                    htmlContent = streamReader.ReadToEnd();
                    streamReader.Close();
                    streamReader.Dispose();
                    stream.Close();
                    stream.Dispose();
                }
                httpWebResponse.Close();
                msg = "";
                return htmlContent;
            }
            catch (Exception ex)
            {
                msg = "網絡連接失敗：" + ex.Message;
                return "";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/132908.html";
            string str = GetHtmlContentByUrl(url, out str);
            richTextBox1.Text = str + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //C#下載網頁HTML源碼
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/132908.html";
            string str = DownLoad_HTML.GetHtml(url);
            richTextBox1.Text = str + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //網頁抓取
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/132908.html";
            string str = GetContentFromUrll(url);
            richTextBox1.Text = str + "\n";
        }

        private string GetContentFromUrll(string _requestUrl)
        {
            string _StrResponse = "";
            HttpWebRequest _WebRequest = (HttpWebRequest)WebRequest.Create(_requestUrl);
            _WebRequest.Method = "GET";
            WebResponse _WebResponse = _WebRequest.GetResponse();
            StreamReader _ResponseStream = new StreamReader(_WebResponse.GetResponseStream(), Encoding.GetEncoding("gb2312"));
            _StrResponse = _ResponseStream.ReadToEnd();
            _WebResponse.Close();
            _ResponseStream.Close();
            return _StrResponse;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //下載圖片
            string url = @"http://www.aspphp.online/Skin/apsp/logo.gif";
            downfile(url, "aaaaaa.gif", Application.StartupPath);
        }

        public static void downfile(string downloadUrl, string filename, string filepath)
        {
            HttpWebRequest hwr = (HttpWebRequest)WebRequest.Create(downloadUrl);
            hwr.Timeout = 15000;
            HttpWebResponse hwp = (HttpWebResponse)hwr.GetResponse();
            Stream ss = hwp.GetResponseStream();
            byte[] buffer = new byte[10240];
            if (!Directory.Exists(filepath))
            {
                Directory.CreateDirectory(filepath);
            }
            FileStream fs = new FileStream(
            string.Format(filepath + @"\" + filename),
            FileMode.Create);
            try
            {
                int i;
                while ((i = ss.Read(buffer, 0, buffer.Length)) > 0)
                {
                    fs.Write(buffer, 0, i);
                }
                fs.Close();
                ss.Close();
            }
            catch (Exception)
            {
                throw;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //抓取網頁資料
            //抓取網頁並分析數據

            //要抓取的URL地址
            //string url = @"http://list.mp3.baidu.com/topso/mp3topsong.html?id=1#top2";
            string url = @"https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG3n.Oxg00wAkRB7rolQ;_ylc=X1MDMTM1MTIwMDM3OQRfcgMyBGZyAwRncHJpZAM1cFFoWDdMWFFLbTByV2N1Z3d3WThBBG5fcnNsdAMwBG5fc3VnZwMxBG9yaWdpbgN0dy5kaWN0aW9uYXJ5LnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzgEcXVlcnkDcHJlc3RpZ2UEdF9zdG1wAzE2MjYxNDI5Nzk-?p=prestige&fr=sfp&iscqry=";
            //string url = @"http://mirlab.org/jang/books/matlabProgramming4beginner/example/03-%E4%BA%8C%E7%B6%AD%E5%B9%B3%E9%9D%A2%E7%B9%AA%E5%9C%96/plotxy12.m";
            //string url = @"https://zh.wikipedia.org/wiki/%E6%98%8E%E7%A5%9E%E5%AE%97";
            //得到指定Url的源码
            string strWebContent = GetWebContent(url);
            richTextBox1.Text = strWebContent;

            return;

            //取出和数据有关的那段源码
            int iBodyStart = strWebContent.IndexOf("<body", 0);
            int iStart = strWebContent.IndexOf("歌曲TOP500", iBodyStart);
            int iTableStart = strWebContent.IndexOf("<table", iStart);
            int iTableEnd = strWebContent.IndexOf("</table>", iTableStart);
            string strWeb = strWebContent.Substring(iTableStart, iTableEnd - iTableStart + 8);
            //生成HtmlDocument
            WebBrowser webb = new WebBrowser();
            webb.Navigate("about:blank");
            HtmlDocument htmldoc = webb.Document.OpenNew(true);
            htmldoc.Write(strWeb);
            HtmlElementCollection htmlTR = htmldoc.GetElementsByTagName("TR");
            foreach (HtmlElement tr in htmlTR)
            {
                string strID = tr.GetElementsByTagName("TD")[0].InnerText;
                richTextBox1.Text += "get : " + strID + "\n";

                //string strName = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "MusicName");
                //string strSinger = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "Singer");
                strID = strID.Replace(".", "");
                //插入DataTable
                //AddLine(strID, strName, strSinger, "0");

                string strID1 = tr.GetElementsByTagName("TD")[2].InnerText;
                //string strName1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "MusicName");
                //string strSinger1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "Singer");
                //插入DataTable
                strID1 = strID1.Replace(".", "");
                //AddLine(strID1, strName1, strSinger1, "0");
                string strID2 = tr.GetElementsByTagName("TD")[4].InnerText;
                //string strName2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "MusicName");
                //string strSinger2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "Singer");
                //插入DataTable
                strID2 = strID2.Replace(".", "");
                //AddLine(strID2, strName2, strSinger2, "0");
            }
            //插入数据库
            //InsertData(dt);

            //dataGridView1.DataSource = dt.DefaultView;

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //獲取網頁內容 1

            string url = @"http://www.hao123.com/";

            WebRequest request = WebRequest.Create(url);
            // If required by the server, set the credentials.
            request.Credentials = CredentialCache.DefaultCredentials;
            // Get the response.
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            // Display the status.
            //Response.Write(response.StatusDescription);

            richTextBox1.Text += "StatusDescription\n" + response.StatusDescription + "\n";

            // Get the stream containing content returned by the server.
            Stream dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.
            StreamReader reader = new StreamReader(dataStream, Encoding.Default);// 注：漢字需要轉為UTF8格式
            // Read the content.
            string responseFromServer = reader.ReadToEnd();
            // Display the content.
            //Response.Write(responseFromServer);
            richTextBox1.Text += "responseFromServer\n" + responseFromServer + "\n";

            // Cleanup the streams and the response.
            reader.Close();
            dataStream.Close();
            response.Close();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //獲取網頁內容 2

            string url = @"http://www.hao123.com/";

            WebClient wc = new WebClient();     // 建立 WebClient

            // Add a user agent header in case the
            // requested URI contains a query.

            wc.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)");

            Stream data = wc.OpenRead(url);
            StreamReader reader = new StreamReader(data, Encoding.Default); // 注：漢字需要轉為UTF8格式
            string s = reader.ReadToEnd();
            //Response.Write(s);
            richTextBox1.Text += s + "\n";
            data.Close();
            reader.Close();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //獲取網頁內容 3
            string url = @"http://www.hao123.com/";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            string str = wc.DownloadString(url);
            richTextBox1.Text += str + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //使用HTTP頭檢測網絡資源是否有效
            string url = @"http://hovertree.com/themes/hvtimages/hwqlogo.png";
            bool flag_available = IsWebResourceAvailable(url);
            richTextBox1.Text += "網絡資源是否有效 : " + flag_available.ToString() + "\n";
        }

        static bool IsWebResourceAvailable(string webResourceAddress)
        {
            //一種行之有效的方式，就是利用HTTP頭返回的狀態碼來確定資源的可用性

            try
            {
                HttpWebRequest req = (HttpWebRequest)WebRequest.CreateDefault(new Uri(webResourceAddress));
                req.Method = "HEAD";
                req.Timeout = 1000;
                HttpWebResponse res = (HttpWebResponse)req.GetResponse();
                return (res.StatusCode == HttpStatusCode.OK);
            }
            catch (WebException wex)
            {
                System.Diagnostics.Trace.Write(wex.Message); return false;
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //獲取遠程網頁中的所有鏈接URL（網絡蜘蛛實現原理）
            //使用System.Net.WebClient類獲取遠程網頁內容，然後使用URL正則表達式分析Html代碼中的鏈接。

            string url = @"http://news.163.com";

            WebClient wc = new WebClient();     // 建立 WebClient
            byte[] page = wc.DownloadData(url);
            string content = Encoding.UTF8.GetString(page);
            string regex = "href=[\\\"\\\'](http:\\/\\/|\\.\\/|\\/)?\\w+(\\.\\w+)*(\\/\\w+(\\.\\w+)?)*(\\/|\\?\\w*=\\w*(&\\w*=\\w*)*)?[\\\"\\\']";
            Regex re = new Regex(regex);
            MatchCollection matches = re.Matches(content);

            System.Collections.IEnumerator enu = matches.GetEnumerator();
            while (enu.MoveNext() && enu.Current != null)
            {
                Match match = (Match)(enu.Current);
                richTextBox1.Text += match.Value + "\n";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //抓取網頁資料並分析之
            //file:///C:/_git/vcs/_1.data/_html/%E6%9C%B1%E5%86%B6%E8%95%99%E8%80%81%E5%B8%AB%E7%9A%84%E9%9B%BB%E8%85%A6%E6%95%99%E5%AE%A4.html

            string url = @"file:///C:/_git/vcs/_1.data/_html/%E6%9C%B1%E5%86%B6%E8%95%99%E8%80%81%E5%B8%AB%E7%9A%84%E9%9B%BB%E8%85%A6%E6%95%99%E5%AE%A4.html";
            string txtURL = "aaaa.txt";

            GetHtmlData();

            List<string> getlist = Read(txtURL);

            //<h3>

            int len = getlist.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + getlist[i].ToString() + "\n";
            }
        }

        /// <summary>
        /// 获取页面数据保存至txt
        /// </summary>
        public static void GetHtmlData()
        {
            string url = @"file:///C:/_git/vcs/_1.data/_html/%E6%9C%B1%E5%86%B6%E8%95%99%E8%80%81%E5%B8%AB%E7%9A%84%E9%9B%BB%E8%85%A6%E6%95%99%E5%AE%A4.html";
            string txtURL = "aaaa.txt";

            WebRequest request = WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("gb2312"));
            //reader.ReadToEnd() 表示取得网页的源码

            FileStream fs = new FileStream(txtURL, FileMode.Create);
            byte[] data = Encoding.Default.GetBytes(reader.ReadToEnd());
            //开始写入
            fs.Write(data, 0, data.Length);
            //清空缓冲区、关闭流
            fs.Flush();
            fs.Close();
        }

        /// <summary>
        /// 根据路径读取txt文件
        /// </summary>
        /// <param name="path">txt路径</param>
        /// <returns></returns>
        public static List<string> Read(string path)
        {
            List<string> list = new List<string>();
            StreamReader sr = new StreamReader(path, Encoding.Default);
            String line;
            while ((line = sr.ReadLine()) != null)
            {
                int i = line.ToString().IndexOf("<h3>");
                if (i > 0)
                {
                    //分析解讀資料
                    list.Add(line);
                    string titleStr = line.ToString().Substring(i + 7); //截取到title后面的值
                    string[] titlelist = titleStr.Split('"');        //以"  截取
                    string titledata = titlelist[0];
                    string[] datalist = titledata.Split('&');  //以& 截取
                    string data = datalist[0];
                    string[] datastrlist = data.Split(new char[] { ';' }, StringSplitOptions.RemoveEmptyEntries);//以; 截取
                    //list.Add(datastrlist);

                }
            }
            sr.Close();
            return list;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //獲取百度首頁生成靜態文件

            string url = @"http://www.baidu.com";

            this.DownUrltoFile(url, "baidu.htm", "GB2312");

            //DownUrltoFile("http://www.xueit.com/show.aspx?pid=1", "html/news/20091224-001.html", "GB2312");
            //其中URL：http://www.xueit.com/show.aspx?pid=1 是动态显示文章，html/news/20091224-001.html是表字段htmlFile预先保存的文件名，这样就可以生成静态文件了。

        }

        /// 獲取遠程URL並生成文件的代碼：
        /// <summary>
        /// 生成網頁文件
        /// </summary>
        /// <param name="url">遠程URL</param>
        /// <param name="filename">生成文件名路徑</param>
        /// <param name="pagecode">目標URL頁面編碼</param>
        protected void DownUrltoFile(string url, string filename, string pagecode)
        {
            try
            {
                //編碼
                Encoding encode = Encoding.GetEncoding(pagecode);
                //請求URL
                HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
                //設置超時(10秒)
                req.Timeout = 10000;
                //this.NotFolderIsCreate(filename);
                //獲取Response
                HttpWebResponse rep = (HttpWebResponse)req.GetResponse();
                //創建StreamReader與StreamWriter文件流對象
                StreamReader sr = new StreamReader(rep.GetResponseStream(), encode);
                StreamWriter sw = new StreamWriter(filename, false, encode);
                //寫入內容
                sw.Write(sr.ReadToEnd());
                //清理當前緩存區，並將緩存寫入文件
                sw.Flush();
                //釋放相關對象資源
                sw.Close();
                sw.Dispose();
                sr.Close();
                sr.Dispose();
                //Response.Write("生成文件"   filename   "成功");
            }
            catch (Exception ex)
            {
                //Response.Write("生成文件"   filename   "失敗，原因："   ex.Message);
            }
        }

        //以上代碼關鍵知識點，通過HttpWebRequest、HttpWebResponse請求獲取遠程URL數據，之後使用StreamReader、StreamWriter文件流讀寫數據寫入文件，注意還有編碼Encoding。

        /*
        /// <summary>
        /// 文件夾不存在則創建
        /// </summary>
        /// <param name="filename">文件名所在路徑</param>
        protected void NotFolderIsCreate(string filename)
        {
            string fileAtDir = Server.MapPath(Path.GetDirectoryName(filename));
            if (!Directory.Exists(fileAtDir))
                Directory.CreateDirectory(fileAtDir);
        }
        */

        private void button23_Click(object sender, EventArgs e)
        {
            //HttpWebRequest
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190339.html";
            string str = GetHtmlData(url);
            richTextBox1.Text += str + "\n";
        }

        public string GetHtmlData(string url)
        {
            try
            {
                HttpWebRequest request;
                request = (HttpWebRequest)WebRequest.Create(url);
                request.Method = "GET";
                HttpWebResponse response;
                response = (HttpWebResponse)request.GetResponse();
                Stream s;
                s = response.GetResponseStream();
                string StrDate = "";
                string strValue = "";
                StreamReader Reader = new StreamReader(s, Encoding.UTF8);
                while ((StrDate = Reader.ReadLine()) != null)
                {
                    strValue += StrDate + "\r\n";
                }
                return strValue;
            }
            catch (Exception)
            {
            }
            return "";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //提取網頁標題
            richTextBox1.Text += "提取網頁標題\n";

            string url = @"https://www.youtube.com/watch?v=ViyVmAU0zgo";

            if (ValidateDate1(url))
            {
                string strl;//儲存編碼
                WebRequest wb = WebRequest.Create(url);//請求資源
                WebResponse webRed = wb.GetResponse();//響應請求
                Stream redweb = webRed.GetResponseStream();//傳回數據存入流中
                StreamReader sr = new StreamReader(redweb, Encoding.UTF8);//從流中讀出數據
                StringBuilder sb = new StringBuilder();//可變字符
                while ((strl = sr.ReadLine()) != null)
                {
                    sb.Append(strl);//讀出數據存入可變字符中
                }
                string result = getstr(sb.ToString());//呼叫正則表達式方法讀出標題
                richTextBox1.Text += "網頁標題:\t" + result + "\n";
            }
            else
            {
                MessageBox.Show("請輸入正確的網址");
                return;
            }
        }

        public string getstr(string strUrl)
        {
            string d = @"<title>(?<title>[^<]*)</title>";
            return Regex.Match(strUrl, d).ToString();
        }

        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }

        static void download_file()
        {
            string url = @"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Breathe-face-smile.svg/1200px-Breathe-face-smile.svg.png";
            using (WebClient wc = new WebClient())  // 建立 WebClient
            {
                wc.DownloadFile(new Uri(url), "Image.png");
            }
        }


        private void button25_Click(object sender, EventArgs e)
        {
            //下載檔案

            try
            {
                download_file();
            }
            catch (ExternalException ex)
            {
                Console.WriteLine(ex.Message);

            }
            catch (ArgumentNullException ex)
            {
                Console.WriteLine(ex.Message);
            }



        }

        private void button26_Click(object sender, EventArgs e)
        {
            //在 C# 中使用 DownloadFile() 方法從一個 URL 下載檔案

            string url = @"https://wiki.linuxfoundation.org/_media/wiki/logo.png";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.DownloadFile(url, "aaaaa.png");
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //http test 1
            //語法01
            //資料來源:https://shunnien.github.io/2017/07/13/Accessing-HTTPS-URL-using-csharp/
            var url = @"https://www.moi.gov.tw/";//台灣內政部網址
            string results;
            // 強制認為憑證都是通過的，特殊情況再使用
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;
            // 加入憑證驗證
            //request.ClientCertificates.Add(new System.Security.Cryptography.X509Certificates.X509Certificate());
            HttpWebResponse resp = (HttpWebResponse)request.GetResponse();
            using (StreamReader sr = new StreamReader(resp.GetResponseStream()))
            {
                results = sr.ReadToEnd();
                sr.Close();
            }
            richTextBox1.Text += results + "\n";
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //http test 2
            //語法02
            string url = @"https://www.moi.gov.tw/";
            getUrlResponse(url);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //http test 3
            //語法3
            string url = @"https://www.moi.gov.tw/";
            string result = PostUrl(url, "key=123");
            richTextBox1.Text += result + "\n";
        }

        static private bool CheckValidationResult(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors)
        {
            return true;// Always accept
        }

        static private HttpWebResponse getUrlResponse(string url)
        {
            HttpWebResponse resp = null;
            HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);

            if (url.StartsWith("https", StringComparison.OrdinalIgnoreCase))
            {
                ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);
            }

            resp = (HttpWebResponse)req.GetResponse();
            using (StreamReader sr = new StreamReader(resp.GetResponseStream()))
            {
                String results = sr.ReadToEnd();
                Console.WriteLine(results);
                sr.Close();
            }

            return resp;
        }

        private static string PostUrl(string url, string postData)
        {
            HttpWebRequest request = null;
            if (url.StartsWith("https", StringComparison.OrdinalIgnoreCase))
            {
                request = WebRequest.Create(url) as HttpWebRequest;
                ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);
                request.ProtocolVersion = HttpVersion.Version11;
                // 這裡設置了協議類型。

                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;// SecurityProtocolType.Tls1.2; 
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls;

                request.KeepAlive = false;
                ServicePointManager.CheckCertificateRevocationList = true;
                ServicePointManager.DefaultConnectionLimit = 100;
                ServicePointManager.Expect100Continue = false;
            }
            else
            {
                request = (HttpWebRequest)WebRequest.Create(url);
            }

            request.Method = "POST";//使用get方式發送數據
            request.ContentType = null;
            request.Referer = null;
            request.AllowAutoRedirect = true;
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727)";
            request.Accept = "*/*";

            byte[] data = Encoding.UTF8.GetBytes(postData);
            Stream newStream = request.GetRequestStream();
            newStream.Write(data, 0, data.Length);
            newStream.Close();

            //獲取網頁響應結果
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream stream = response.GetResponseStream();
            //client.Headers.Add("Content-Type", "application/x-www-form-urlencoded");
            string result = string.Empty;
            using (StreamReader sr = new StreamReader(stream))
            {
                result = sr.ReadToEnd();
            }
            return result;
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //網頁截圖
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            string url = @"https://www.google.com.tw/";

            WebBrowser webBrowser1 = new WebBrowser();
            webBrowser1.ScrollBarsEnabled = false;
            webBrowser1.Size = new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

            //取得網頁資料
            webBrowser1.Navigate(url);
            while (webBrowser1.ReadyState != WebBrowserReadyState.Complete)
            {
                Application.DoEvents();
            }

            //截圖
            Bitmap bitmap1 = new Bitmap(W, H);
            Rectangle DrawRect = new Rectangle(0, 0, W, H);
            webBrowser1.DrawToBitmap(bitmap1, DrawRect);

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            Image image = null;
            try
            {
                //string fileName = imgs[i];

                string url = @"http://www.aspphp.online/Skin/apsp/logo.gif";

                string localFile = "aaaaaa.gif";

                HttpWebRequest webrequest = (HttpWebRequest)WebRequest.Create(url);
                HttpWebResponse webresponse = (HttpWebResponse)webrequest.GetResponse();
                if (webresponse.StatusCode == HttpStatusCode.OK)
                {
                    image = Image.FromStream(webresponse.GetResponseStream());
                    //保存在服務器的本地硬盤

                    image.Save(localFile);

                    richTextBox1.Text += "下載圖片完成\n";
                }
            }
            catch (Exception ex)
            {
                string result = "遠程圖片保存失敗,原因為：\n" + ex.Message;
                //Response.Write(result);
                //Response.End();
                //break;
            }
            finally
            {
                if (image != null)
                {
                    image.Dispose(); //釋放資源
                }
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //下載網頁HTML源碼

            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188350.html";
            //產業群首頁
            string tempGroupData = GetHttpData(url);
            using (StreamWriter sw = new StreamWriter(filename, false, Encoding.GetEncoding("utf-8")))
            {
                sw.Write(tempGroupData);
                sw.Flush();
            }
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        public string GetHttpData(string sUrl)
        {
            string sRslt = null;
            WebResponse oWebRps = null;
            WebRequest oWebRqst = WebRequest.Create(sUrl);
            oWebRqst.Timeout = 50000;
            try
            {
                oWebRps = oWebRqst.GetResponse();
            }

            finally
            {
                if (oWebRps != null)
                {
                    StreamReader oStreamRd = new StreamReader(oWebRps.GetResponseStream(), Encoding.GetEncoding("utf-8"));
                    sRslt = oStreamRd.ReadToEnd();
                    oStreamRd.Close();
                    oWebRps.Close();
                }
            }
            return sRslt;
        }


        private void button33_Click(object sender, EventArgs e)
        {
            //c# 獲取網頁源碼 by WebClient
            string url = @"http://www.google.com/webhp?hl=zh-TW";
            string result = GetWebClient(url);
            richTextBox1.Text += result + "\n";
        }

        private string GetWebClient(string url)
        {
            string strHTML = "";
            WebClient wc = new WebClient();     // 建立 WebClient
            Stream myStream = wc.OpenRead(url);
            StreamReader sr = new StreamReader(myStream, Encoding.GetEncoding("utf-8"));
            strHTML = sr.ReadToEnd();
            myStream.Close();
            return strHTML;
        }


        private void button34_Click(object sender, EventArgs e)
        {
            //c# 獲取網頁源碼 by WebRequest
            string url = @"http://www.google.com/webhp?hl=zh-TW";
            string result = GetWebRequest(url);
            richTextBox1.Text += result + "\n";
        }

        private string GetWebRequest(string url)
        {
            Uri uri = new Uri(url);
            WebRequest myReq = WebRequest.Create(uri);
            WebResponse result = myReq.GetResponse();
            Stream receviceStream = result.GetResponseStream();
            StreamReader readerOfStream = new StreamReader(receviceStream, Encoding.GetEncoding("utf-8"));
            string strHTML = readerOfStream.ReadToEnd();
            readerOfStream.Close();
            receviceStream.Close();
            result.Close();
            return strHTML;
        }


        private void button35_Click(object sender, EventArgs e)
        {
            //差很多~~~~~

            //c# 獲取網頁源碼 by HttpWebRequest
            string url = @"http://www.google.com/webhp?hl=zh-TW";
            string result = GetHttpWebRequest(url);
            richTextBox1.Text += result + "\n";
        }

        private string GetHttpWebRequest(string url)
        {
            Uri uri = new Uri(url);
            HttpWebRequest myReq = (HttpWebRequest)WebRequest.Create(uri);
            myReq.UserAgent = "User-Agent:Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705";
            myReq.Accept = "*/*";
            myReq.KeepAlive = true;
            myReq.Headers.Add("Accept-Language", "zh-cn,en-us;q=0.5");
            HttpWebResponse result = (HttpWebResponse)myReq.GetResponse();
            Stream receviceStream = result.GetResponseStream();
            StreamReader readerOfStream = new StreamReader(receviceStream, Encoding.GetEncoding("utf-8"));
            string strHTML = readerOfStream.ReadToEnd();
            readerOfStream.Close();
            receviceStream.Close();
            result.Close();
            return strHTML;
        }
        //注意"utf-8"應與指定網頁的編碼對應。
        //可以看到HttpWebRequest 方式最復雜，但確提供了更多的選擇性。
        //有的網站檢測客戶端的UserAgent！如163.com，你如果使用WebClient WebRequest方式獲取時，將獲取到的是錯誤提示頁面內容。
        //而通過HttpWebRequest 就沒問題。


        private void button36_Click(object sender, EventArgs e)
        {
            //抓取網頁資料 1
            string url = @"http://140.129.118.16/~richwang/";

            string rl;
            WebRequest Request = WebRequest.Create(url.Trim());

            WebResponse Response = Request.GetResponse();

            Stream resStream = Response.GetResponseStream();

            StreamReader sr = new StreamReader(resStream, Encoding.Default);
            StringBuilder sb = new StringBuilder();
            while ((rl = sr.ReadLine()) != null)
            {
                sb.Append(rl);
            }

            richTextBox1.Text += sb + "\n";

            richTextBox1.Text += "完成\n";
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //抓取網頁資料 2
            string url = @"http://www.lagou.com/";

            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼

            string str = wc.DownloadString(url);

            richTextBox1.Text += str + "\n";
        }

        //過濾html標簽 ST
        private void button38_Click(object sender, EventArgs e)
        {
            //過濾html標簽 
        }

        //過濾html標簽
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");
            //htmlStr = htmlStr.Replace(""", "");//去除異常的引號" " "
            //htmlStr = htmlStr.Replace(""", "");
            return htmlStr.Trim();
        }

        //過濾html標簽 SP

        private void button39_Click(object sender, EventArgs e)
        {
            //獲取指定路徑下的模板的HTML源代碼
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/10747.html";
            string str = GetHtmlCode(url, "UTF8");
            richTextBox1.Text += str + "\n";
        }

        /// <summary>
        /// 獲取指定路徑下的HTML源代碼
        /// </summary>
        /// <param name="EncodingType">網頁類型（有些是UTF8，有些是GB2312）</param>
        /// <returns>源代碼</returns>
        private string GetHtmlCode(string url, string EncodingType)
        {
            try
            {
                if (url != string.Empty)
                {
                    WebClient wc = new WebClient();     // 建立 WebClient

                    //設置網絡憑證為系統憑證
                    wc.Credentials = CredentialCache.DefaultCredentials;

                    //獲取指定URI的網頁的源代碼
                    byte[] byteDataBuffer = wc.DownloadData(url);

                    string htmlCode = "";
                    if (EncodingType == "UTF8")
                    {
                        htmlCode = Encoding.UTF8.GetString(byteDataBuffer);
                    }
                    else
                    {
                        htmlCode = Encoding.GetEncoding(EncodingType).GetString(byteDataBuffer);
                    }

                    htmlCode = Regex.Replace(htmlCode, @"<!DOCTYPE\s*HTML\s*PUBLIC[^>]+>", "", RegexOptions.Singleline);
                    htmlCode = Regex.Replace(htmlCode, @"\s+", " ", RegexOptions.Singleline);

                    return htmlCode;
                }
                else
                {
                    return "";
                }
            }
            catch (Exception ee)
            {
                throw (ee);
            }
        }


        private void button40_Click(object sender, EventArgs e)
        {
            //根據url獲取遠程html源碼
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/10747.html";
            string str = GetSearchHtml(url);
            richTextBox1.Text += str + "\n";
        }

        /// <summary>
        /// 根據url獲取遠程html源碼
        /// </summary>
        /// <param name="url">搜索url</param>
        /// <returns>返回DownloadData</returns>
        public static string GetSearchHtml(string url)
        {
            WebClient wc = new WebClient();     // 建立 WebClient
            wc.Credentials = CredentialCache.DefaultCredentials;   //獲取或設置用於對向Internet資源的請求進行身份驗證的網絡憑據。
            Byte[] pageData = wc.DownloadData(url);                //從指定url下載數據
            return Encoding.UTF8.GetString(pageData);                       //獲取網站頁面采用的是UTF-8
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //httpWebRequest 文件下載
            string uri = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/SMS_K%C3%B6nig_Albert.jpg/450px-SMS_K%C3%B6nig_Albert.jpg";
            var req = WebRequest.Create(uri) as HttpWebRequest;
            //req.ContentType = "application/octet-stream";
            if (req != null)
            {
                var response = req.GetResponse() as HttpWebResponse;
                if (response != null)
                {
                    Console.WriteLine("ContentType:" + response.ContentType);
                    var stream = response.GetResponseStream();
                    if (stream != null)
                    {
                        string format = string.Empty;
                        switch (response.ContentType)
                        {
                            case "image/jpeg":
                                format = "jpg";
                                break;
                            case "audio/amr":
                                format = "amr";
                                break;
                        }

                        var path = string.Format(@"1.{0}", format);
                        //var fs = new FileStream($"c:\\1.{format}", FileMode.Create);
                        var fs = File.Create(path);
                        richTextBox1.Text += "下載完成, 檔案 : \t" + path + "\n";

                        int count = 0;
                        do
                        {
                            var buffer = new byte[4096];
                            count = stream.Read(buffer, 0, buffer.Length);
                            fs.Write(buffer, 0, count);
                        } while (count > 0);
                    }
                }
            }
        }

        private void button42_Click(object sender, EventArgs e)
        {
            //檢查URL鏈接是否有效
            richTextBox1.Text += "檢查URL鏈接是否有效\n";
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/11093.html";
            bool ret = CheckUri(url);
            richTextBox1.Text += "結果 : \t" + ret.ToString() + "\n";

            url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/11093XX.html";
            ret = CheckUri(url);
            richTextBox1.Text += "結果 : \t" + ret.ToString() + "\n";
        }

        /// <summary>
        /// 檢查url鏈接是否有效
        /// </summary>
        /// <param name="strUri"></param>
        /// <returns></returns>
        public static bool CheckUri(string strUri)
        {
            try
            {
                System.Net.HttpWebRequest.Create(strUri).GetResponse();
                return true;
            }
            catch
            {
                return false;
            }
        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        private void button45_Click(object sender, EventArgs e)
        {

        }

        private void button46_Click(object sender, EventArgs e)
        {

        }

        private void button47_Click(object sender, EventArgs e)
        {

        }

        private void button48_Click(object sender, EventArgs e)
        {

        }

        private void button49_Click(object sender, EventArgs e)
        {

        }
    }


    //C#下載網頁HTML源碼


    public static class DownLoad_HTML
    {
        private static int FailCount = 0; //記錄下載失敗的次數

        public static string GetHtml(string url) //傳入要下載的網址
        {
            string str = string.Empty;
            try
            {
                System.Net.WebRequest request = System.Net.WebRequest.Create(url);
                request.Timeout = 10000; //下載超時時間
                request.Headers.Set("Pragma", "no-cache");
                System.Net.WebResponse response = request.GetResponse();
                System.IO.Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("gb2312");//utf-8 網頁文字編碼
                System.IO.StreamReader streamReader = new System.IO.StreamReader(streamReceive, encoding);
                str = streamReader.ReadToEnd();
                streamReader.Close();
            }
            catch (Exception ex)
            {
                FailCount++;

                if (FailCount > 5)
                {
                    var result = System.Windows.Forms.MessageBox.Show("已下載失敗" + FailCount + "次，是否要繼續嘗試？" + Environment.NewLine + ex.ToString(), "數據下載異常", System.Windows.Forms.MessageBoxButtons.YesNo, System.Windows.Forms.MessageBoxIcon.Error);
                    if (result == System.Windows.Forms.DialogResult.Yes)
                    {
                        str = GetHtml(url);
                    }
                    else
                    {
                        System.Windows.Forms.MessageBox.Show("下載HTML失敗" + Environment.NewLine + ex.ToString(), "下載HTML失敗", System.Windows.Forms.MessageBoxButtons.OK, System.Windows.Forms.MessageBoxIcon.Error);
                        throw ex;
                    }
                }
                else
                {
                    str = GetHtml(url);
                }
            }

            FailCount = 0; //如果能執行到這一步就表示下載終於成功了
            return str;
        }
    }
    /*
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
    */

}

