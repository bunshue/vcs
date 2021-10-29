using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

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
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //c# 下載網頁源碼 獲取http狀態碼
            //c# 下載網頁源碼 獲取http狀態碼
            HttpWebRequest hwr = (HttpWebRequest)WebRequest.Create("http://www.baidu.com");
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

            //建立 WebRequest 並指定目標的 uri
            WebRequest request = WebRequest.Create("http://jsonplaceholder.typicode.com/posts");
            // 使用 HttpWebRequest.Create 實際上也是呼叫 WebRequest.Create
            //WebRequest request = HttpWebRequest.Create("http://jsonplaceholder.typicode.com/posts");
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
            //string Url = "HTTP://list.mp3.baidu.com/topso/mp3topsong.html?id=1#top2";
            string Url = "http://jsonplaceholder.typicode.com/posts";

            //得到指定Url的源碼

            string strWebContent = GetWebContent(Url);

            richTextBox1.Text += strWebContent + "\n";
        }

        //根據Url位址得到網頁的html源碼
        private string GetWebContent(string Url)
        {
            string strResult = "";
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
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

            string Url = "http://www.google.com/webhp?hl=zh-TW";
            HttpWebRequest req = (HttpWebRequest)HttpWebRequest.Create(Url);
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
            string url = "http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188537.html";

            WebClient wc = new WebClient();

            wc.Encoding = System.Text.Encoding.UTF8;

            string str = wc.DownloadString(url);

            richTextBox1.Text += str + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得網頁資料
            //C#獲取網頁源碼，自動判斷網頁字符集編碼
        }

        private string getHtml(string url)
        //url是要訪問的網站地址，charSet是目標網頁的編碼，如果傳入的是null或者""，那就自動分析網頁的編碼
        {
            WebClient myWebClient = new WebClient();
            //創建WebClient實例myWebClient 
            // 需要注意的：
            //有的網頁可能下不下來，有種種原因比如需要cookie,編碼問題等等
            //這是就要具體問題具體分析比如在頭部加入cookie 
            // webclient.Headers.Add("Cookie", cookie); 
            //這樣可能需要一些重載方法。根據需要寫就可以了
            //獲取或設置用於對向 Internet 資源的請求進行身份驗證的網絡憑據。
            myWebClient.Credentials = CredentialCache.DefaultCredentials;
            //如果服務器要驗證用戶名,密碼 
            //NetworkCredential mycred = new NetworkCredential(struser, strpassword);
            //myWebClient.Credentials = mycred; 
            //從資源下載數據並返回字節數組。（加@是因為網址中間有"/"符號）
            byte[] myDataBuffer = myWebClient.DownloadData(url);
            string strWebData = Encoding.Default.GetString(myDataBuffer);
            //獲取網頁字符編碼描述信息
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

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

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

    }
}

