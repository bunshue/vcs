using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;   //for WebClient
using HtmlAgilityPack;

/*
//Yahoo氣象 台北
https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179

//Yahoo氣象 新竹
https://tw.news.yahoo.com/weather/%E5%8F%B0%E7%81%A3/%E6%96%B0%E7%AB%B9%E5%B8%82/%E6%96%B0%E7%AB%B9%E5%B8%82-2306185
*/

/*
要用Chrome
開啟網頁 : https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179 //Yahoo氣象 台北

更多工具/網頁人員工具/
反白要抓取的資料部分/右鍵/檢查
檢測器會跳到相關的程式碼去

確定HTML的位置後，在該元素按下右鍵/Copy/Copy XPath        不要Copy full XPath

將此路徑拷貝到程式裡
*/

/*
FireFox不可用

更多工具/網頁開發者工具/檢測器

反白要抓取的資料部分/右鍵/檢測
檢測器會跳到相關的程式碼去

確定HTML的位置後，在該元素按下右鍵/複製/XPATH

/html/body/div[1]/div/div/div/div[4]/div[1]/div/div[2]/div/div/section[2]/div/div[3]/span[1]
*/

namespace vcs_HtmlAgility
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
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 30;
            dx = 120;
            dy = 55;

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

            x_st = 20;
            y_st = 20;
            dx = 200;
            dy = 360;
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //fail

            return;

            //here
            string url = @"http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm";   //台銀的 不能用
            //string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";        //perl的 可以用

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));    //fail在此

            //以台灣銀行為範例

            // 使用預設編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            //取得現在的日期
            richTextBox1.Text += "現在時間：" + DateTime.Now + "\n";
            // 在Html內表示換行

            // 取得匯率 
            for (int x = 3; x <= 21; x++)
            {
                string txt1 = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[" + x + "]/td[1]").InnerText;
                string txt2 = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[" + x + "]/td[2]").InnerText;
                string txt3 = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[" + x + "]/td[3]").InnerText;
                string txt4 = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[" + x + "]/td[4]").InnerText;
                string txt5 = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[" + x + "]/td[5]").InnerText;
                string total = string.Format("幣別：{0} ，買入現金匯率：{1} ，賣出即期匯率：{2} ，買入遠期匯率：{3} ，賣出歷史匯率：{4}", txt1, txt2, txt3, txt4, txt5);
                richTextBox1.Text += total + "\n";
            }

            //清除資料
            doc = null;
            wc = null;
            ms.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jackbgova/2014/06/10/145471       台泥

            //Yahoo股市 台泥
            string url = @"http://tw.stock.yahoo.com/q/q?s=1101";

            return;

            //指定來源網頁

            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));
            //以奇摩股市為例http://tw.stock.yahoo.com
            //1101 表示為股票代碼

            // 使用預設編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            //XPath 來解讀它 /html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1] 
            doc1.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭 
            HtmlNodeCollection nodes = doc1.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值 
            string[] txt = doc1.DocumentNode.SelectSingleNode("./tr[2]").InnerText.Trim().Split('\n');
            int i = 0;

            // 輸出資料 
            foreach (HtmlNode node in nodes)
            {
                //將 "加到投資組合" 這個字串過濾掉
                richTextBox1.Text += node.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "\n";
                i++;
            }

            //清除資料
            doc = null;
            doc1 = null;
            wc = null;
            ms.Close();




        }

        private void button2_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jackbgova/2015/01/14/148093
            /*
            //指定來源網頁
            string url = @"http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm";
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));
            //以台灣銀行為範例

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            //取得現在的日期
            label2.Text = "牌告時間：" + DateTime.Now;
            label2.Font.Size = 20;
            // 在Html內表示換行

            //顏色設置
            buytxt01.ForeColor = buytxt02.ForeColor = buytxt03.ForeColor = buytxt04.ForeColor = buytxt05.ForeColor = Color.Red;
            selltxt01.ForeColor = selltxt02.ForeColor = selltxt03.ForeColor = selltxt04.ForeColor = selltxt05.ForeColor = Color.FromName("#008000");

            //幣別名稱
            //美金
            currencytxt01.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[3]/td[1]").InnerText;
            //英鎊
            currencytxt02.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[5]/td[1]").InnerText;
            //日幣
            currencytxt03.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[10]/td[1]").InnerText;
            //歐元
            currencytxt04.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[17]/td[1]").InnerText;
            //人民幣
            currencytxt05.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[21]/td[1]").InnerText;

            //買入
            buytxt01.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[3]/td[2]").InnerText;
            buytxt02.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[5]/td[2]").InnerText;
            buytxt03.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[10]/td[2]").InnerText;
            buytxt04.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[17]/td[2]").InnerText;
            buytxt05.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[21]/td[2]").InnerText;

            //賣出
            selltxt01.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[3]/td[3]").InnerText;
            selltxt02.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[5]/td[3]").InnerText;
            selltxt03.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[10]/td[3]").InnerText;
            selltxt04.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[17]/td[3]").InnerText;
            selltxt05.Text = doc.DocumentNode.SelectSingleNode(@"/html[1]/body[1]/ul[1]/li[2]/center[1]/div[1]/div[2]/table[2]/tr[21]/td[3]").InnerText;


            //清除資料
            doc = null;
            wc = null;
            ms.Close();

            //網頁更新
            HtmlMeta meta = new HtmlMeta();
            meta.Attributes.Add("http-equiv", "refresh");
            //設定秒數，5秒後執行頁面更新
            meta.Content = "5";
            this.Header.Controls.Add(meta);
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //M$範例 鴻海
            //fail

            return;

            // 下載 Yahoo 奇摩股市資料 (範例為 2317 鴻海)
            //Yahoo股市 鴻海
            string url = @"http://tw.stock.yahoo.com/q/q?s=2317";
            WebClient wc = new WebClient();
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            // 裝載第一層查詢結果
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            doc1.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭
            HtmlNodeCollection nodes = doc1.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值
            string[] values = doc1.DocumentNode.SelectSingleNode("./tr[2]").InnerText.Trim().Split('\n');
            int i = 0;

            // 輸出資料
            foreach (HtmlNode node in nodes)
            {
                Console.WriteLine("Header: {0}, Value: {1}", node.InnerText, values[i].Trim());
                i++;
            }

            doc = null;
            doc1 = null;
            wc = null;
            ms.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jackbgova/2014/12/08/147553
            //fail

            //Yahoo股市 大立光
            string url = @"http://tw.stock.yahoo.com/q/q?s=3008";
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));
            //以奇摩股市為例http://tw.stock.yahoo.com，3008以大立光為例

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            //XPath 來解讀它 /html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]
            doc.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭
            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值
            string[] txt = doc.DocumentNode.SelectSingleNode("./tr[2]").InnerText.Trim().Split('\n');

            int i = 0;

            // 輸出資料
            foreach (HtmlNode node in nodes)
            {
                //將 "加到投資組合" 這個字串過濾掉
                //Response.Write(node.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "<br />");
                richTextBox1.Text += node.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "\n";
                i++;
            }
            //清除資料
            doc = null;
            wc = null;
            ms.Close();

        }

        public class Model
        {
            public string Title { get; set; } //標題
            public string Content { get; set; } //內容
            public string Href { get; set; } //文章鏈接
            public string ComeFrom { get; set; } //來源
            public DateTime Time { get; set; } //發布時間
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //0303a
        }

        //1.下面這句話是 獲取全部 class為list_item article_item開始的div
        /// <summary>
        /// 獲取文章列表
        /// </summary>
        private const string MessageListXPath = "//div[starts-with(@class,'list_item article_item')]";

        //2.下面這句話是 獲取上面獲取出來的集合裡面每一項的標題
        /// <summary>
        /// 獲取標題 解釋: 第一個div,下的第一個div,下的第一個h1,下的第一個span,下的第一個a標簽
        /// </summary>
        private const string MessageNameXPath = "/div[1]/div[1]/h1[1]/span[1]/a[1]";

        //3.和上面一樣這個是獲取內容
        /// <summary>
        /// 獲取內容 解釋： 第一個div,下的第二個div
        /// </summary>
        private const string MessageContxtXPath = "/div[1]/div[2]";

        //4.這個是獲取發布時間
        /// <summary>
        /// 獲取時間 這個就是 獲取 第一個div,下的第3個div,下的span
        /// </summary>
        private const string MessageTimeXPath = "/div[1]/div[3]/span";

        //1. 獲網頁的Html

        #region 獲取文章列表 +GetHtml(string url)
        /// <summary>
        /// 獲取文章列表 Add shuaibi 2015-03-08
        /// </summary>
        /// <param name="url">頁面地址</param>
        /// <returns>文章列表</returns>
        public List<Model> GetHtml(string url)
        {
            var myWebClient = new WebClient();
            var myStream = myWebClient.OpenRead(url);
            var list = GetMessage(myStream); //這裡調用的是下面的方法
            if (myStream != null) myStream.Close();
            return list;
        }
        #endregion

        //2. 用Html Agility Pack 找出我們想要的東西

        #region 處理文章信息 +GetMessage(Stream myStream)
        /// <summary>
        /// 處理文章信息 Add shuaibi 2015-03-08
        /// </summary>
        /// <param name="myStream">網頁的數據流</param>
        /// <returns></returns>
        private static List<Model> GetMessage(Stream myStream)
        {
            var doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(myStream, Encoding.UTF8);
            var rootNode = doc.DocumentNode;
            var messageNodeList = rootNode.SelectNodes(MessageListXPath);
            return messageNodeList.Select(messageNode => HtmlNode.CreateNode(messageNode.OuterHtml)).Select(temp => new Model
            {
                Title = temp.SelectSingleNode(MessageNameXPath).InnerText,
                Href = "http://blog.csdn.net" + temp.SelectSingleNode(MessageNameXPath).Attributes["href"].Value,
                Content = temp.SelectSingleNode(MessageContxtXPath).InnerText,
                Time = Convert.ToDateTime(temp.SelectSingleNode(MessageTimeXPath).InnerText),
                ComeFrom = "csdn"
            }).ToList();
        }
        #endregion



        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            List<String> strings;
            strings = GetNodeFirstValue("http://www.cqcp.net/game/ssc/", "//*[@id=\"openlist\"]", "./ul[{0}]/li", Encoding.GetEncoding("gb2312"), 1);
            richTextBox1.Text += "len = " + strings.Count.ToString() + "\n";
        }
        /// <summary>
        /// Get table value for html
        /// Example: GetNodeTableValue("http://www.cqcp.net/game/ssc/", "//*[@id=\"openlist\"]", "./ul[{0}]/li", Encoding.GetEncoding("gb2312"), 1);
        /// </summary>
        /// <param name="Url">Url path</param>
        /// <param name="xPathFirst">All xPath</param>
        /// <param name="xPathSecond">Second xPath</param>
        /// <param name="encoding">Encoding</param>
        /// <param name="TableRowNum">Table row nunber</param>
        /// <returns></returns>
        public List<string> GetNodeFirstValue(string Url, string xPathFirst, string xPathSecond, Encoding encoding, int TableRowNum)
        {
            List<string> ListData = new List<string>();

            using (WebClient wc = new WebClient())
            {
                using (MemoryStream ms = new MemoryStream(wc.DownloadData(Url)))
                {
                    HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                    doc.Load(ms, encoding); //指定編碼格式

                    // All content
                    HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

                    doc1.LoadHtml(doc.DocumentNode.SelectSingleNode(xPathFirst).InnerHtml);

                    // Content value
                    HtmlNodeCollection nodes = doc1.DocumentNode.SelectNodes(string.Format(xPathSecond, TableRowNum));

                    foreach (HtmlNode node in nodes)
                    {
                        ListData.Add(node.InnerHtml);
                    }
                }
            }
            return ListData;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jakeuj/2016/06/14/HtmlAgilityPack

            string url = @"http://gnn.gamer.com.tw/4/133124.html";

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));
            //以巴哈新聞例http://gnn.gamer.com.tw/
            //4/133124.html 表示為文章編號

            // 使用 UTF8 編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8);    //指定編碼格式

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            //XPath 來解讀它 /html[1]/body[1]/div[3]
            doc1.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/div[3]").InnerHtml);
            //這邊因為公告內文含有 img tag 所以需使用 InnerHtml
            string txt = doc1.DocumentNode.SelectSingleNode(".").InnerHtml.Trim();
            // 去頭
            int p = txt.IndexOf("<!--區塊1開始-->");
            txt = txt.Substring(p);
            // 去尾
            p = txt.IndexOf("<!--新聞內容結束-->");
            txt = txt.Substring(0, p);
            // 解析 標題與內文 以字串 "<!--新聞內容開始-->" 分隔
            string[] txts = txt.Split(new string[] { "<!--新聞內容開始-->" }, StringSplitOptions.RemoveEmptyEntries);
            // 輸出結果
            string result = string.Format("標題：{0}<br>內文：<br>{1}", txts[0], txts[1]);

            richTextBox1.Text += result + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jakeuj/2016/06/14/HtmlAgilityPack


            string url = @"http://gnn.gamer.com.tw/index.php?k=4";

            //查詢新聞連結清單

            string link, XPath;

            link = url;
            XPath = "/html[1]/body[1]/div[3]/div[1]/div[5]/div[2]";

            // 指定來源網頁
            WebClient wc = new WebClient();
            // 將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(link));

            // 使用 UTF8 編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8);    //指定編碼格式

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            // XPath 來解讀它
            doc1.LoadHtml(doc.DocumentNode.SelectSingleNode(XPath).InnerHtml);

            HtmlNodeCollection nodes = doc1.DocumentNode.SelectNodes(@"//div[@class='GN-lbox2B']/div/a");

            foreach (HtmlNode node in nodes)
            {
                string currLink = node.SelectSingleNode(".").Attributes["href"].Value;
                //Response.Write(currLink + "<br/>");
                richTextBox1.Text += currLink + "\n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            datascraper();

        }

        public void datascraper()
        {
            string url = @"http://www.bbc.co.uk/sport/football/results/partial/competition-118996114";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument { OptionUseIdAttribute = true };
            doc = htmlWeb.Load(url);

            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//tr[@id]");

            string date;
            string ateam;
            string hteam;
            string score;
            string idmess;
            string idnum;
            string[] teamscores;
            string teamscoreh;
            string teamscorea;

            foreach (HtmlNode node in nodes)
            {
                idmess = node.SelectSingleNode("//tr[@id]").Id;
                idnum = idmess.Replace("match-row-", "");
                score = node.SelectSingleNode("//abbr[@title='Score']").InnerText;
                teamscores = score.Split('-');
                teamscoreh = teamscores[0];
                teamscorea = teamscores[1];
                hteam = node.SelectSingleNode("//p[(@class='team-home teams')]").InnerText;
                ateam = node.SelectSingleNode("//p[(@class='team-away teams')]").InnerText;
                date = node.SelectSingleNode("//td[(@class='match-date')]").InnerText;
            }

            return;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            List<string> outList = new List<string>();

            string url = @"https://yandex.by/search/?numdoc=10&p=0&rdrnd=601861&text=kinogo.co%20Один%20дома%201990%20&lr=157";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            HtmlWeb htmlWeb = new HtmlWeb
            {
                AutoDetectEncoding = false,
                OverrideEncoding = Encoding.UTF8 //GetEncoding("windows-1251")
            };
            doc = htmlWeb.Load(url);

            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//div");

            if (nodes != null)
            {
                foreach (HtmlNode node in nodes)
                {

                    string outputText = node.InnerHtml;
                    richTextBox1.Text += "找到" + outputText + "\n\n";
                }
            }
            else
            {
                richTextBox1.Text += "找不到資料\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //List<String> strings;
            //richTextBox1.Text += "len = " + strings.Count.ToString() + "\n";




        }



        private void button13_Click(object sender, EventArgs e)
        {
            string url = @"http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.31.3487";
            string result = getBibTex(url);
            richTextBox1.Text += "此網頁中 BibTeX 欄位內的資料:\n" + result + "\n";

            //抓此網頁中 BibTeX 欄位內的資料


            url = @"http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.4035&rank=3&q=Composite&osm=&ossid=";
            result = getBibTex(url);
            richTextBox1.Text += "此網頁中 BibTeX 欄位內的資料:\n" + result + "\n";


            url = @"http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.4035";
            result = getBibTex(url);
            richTextBox1.Text += "此網頁中 BibTeX 欄位內的資料:\n" + result + "\n";
        }

        public string getBibTex(string url)
        {
            string res = "";
            string temp = "";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            HtmlNode node;

            if (url.Contains("viewdoc"))//e.g. http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.31.3487
            {
                doc = htmlWeb.Load(url);

                if (doc != null)
                {
                    Console.WriteLine("Document Loaded!");
                    richTextBox1.Text += "Document Loaded!\n";
                }
                else
                {
                    Console.WriteLine("Load Error!");
                    richTextBox1.Text += "Load Error!\n";
                }
                try
                {
                    if ((node = doc.DocumentNode.SelectSingleNode("//*[@id=\"bibtex\"]/p")) != null)
                    {
                        temp = node.InnerText;
                        temp = temp.Replace(",", ",\n").Replace("&nbsp;", " ");
                    }
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                res = temp;
                return res;
            }
            else//e.g. http://citeseer.ist.psu.edu/showciting?cid=2131272
                return res;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            int ret = GetFaceBookLikes();
            richTextBox1.Text += "links = " + ret.ToString() + "\n";

        }

        /// <summary>
        /// WebCrawl facebook to get likes from ordbogen.com page
        /// </summary>
        /// <returns>int</returns>
        public int GetFaceBookLikes()
        {
            int numOfLikes = 0;
            string searchStart = "omBeskedDelMere";
            string searchEnd = " ";
            try
            {
                string url = @"https://www.facebook.com/ABCNetwork/";
                HtmlWeb htmlWeb = new HtmlWeb();
                HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                doc = htmlWeb.Load(url);

                if (doc != null)
                {
                    var divNodes = doc.DocumentNode.SelectNodes("//div");
                    foreach (var div in divNodes)
                    {
                        if (div.InnerText.Contains("personer synes godt om dette"))
                        {
                            int start = div.InnerText.IndexOf(searchStart, 0) + searchStart.Length;
                            int end = div.InnerText.IndexOf(searchEnd, start);
                            string number = div.InnerText.Substring(start, end - start);
                            int.TryParse(number, out numOfLikes);
                            return numOfLikes;
                        }
                    }
                    return -1;
                }
                else
                {
                    return -1;
                }
            }
            catch (Exception)
            {
                return -3;
            }
        }


        private void button15_Click(object sender, EventArgs e)
        {
            string url = @"https://www.cwb.gov.tw/V8/C/E/index.html";

            WebClient wc = new WebClient();

            //HTML Agility Pack預設編碼應是法文編碼，所以如果是讀取中文 HTML 內容的話，
            //無法直接使用HtmlDocument.LoadHtml() 方法，而要透過MemoryStream使用HtmlDocument.Load()方法，才可以指定中文的編碼。
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));

            //使用HtmlDocument.Load()進行編碼，使用UTF8編譯，取得整份網頁結構
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8);    //指定編碼格式

            //從doc向下取得目標資料的html結構
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            string pattern = @"/html/body/div[3]/main/div/div[2]/table/caption";

            string str = doc.DocumentNode.SelectSingleNode(pattern).InnerHtml;


            richTextBox1.Text += "str = " + str + "\n";

            //return;


        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //Perl學習手札
            //string url = @"https://easun.org/perl/perl-toc/ch08.html";
            string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";

            string result = GetContentFromUrl(url);

            richTextBox1.Text += result + "\n";
        }

        // C#获取页面显示的内容 
        private string GetContentFromUrl(string url)
        {
            string result = "";
            HttpWebRequest hwr = (HttpWebRequest)WebRequest.Create(url);
            hwr.Method = "GET";
            WebResponse wr = hwr.GetResponse();
            StreamReader sr = new StreamReader(wr.GetResponseStream(), System.Text.Encoding.GetEncoding("utf-8"));
            result = sr.ReadToEnd();
            wr.Close();
            sr.Close();
            return result;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string url = "http://www.baidu.com";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            //获得title标签节点，其子标签下的所有节点也在其中
            HtmlNode node = doc.DocumentNode.SelectSingleNode("//title");

            //获得title标签中的内容
            string Title = node.InnerText;

            richTextBox1.Text += "取得標題:\t" + Title + "\n";

            //获得id选择器为u1标签（是u1非ul（L）)节点
            HtmlNode node2 = doc.DocumentNode.SelectSingleNode("//div[@id='u1']");
            //获得ul标签下的所有子节点
            HtmlNodeCollection nodes = node2.ChildNodes;
            foreach (var nn in nodes)
            {
                /*
                //获得标签属性为href的值
                string aValue = nn.Attributes["href"].Value;
                //获得标签内的内容
                string aInterText = nn.InnerText;
                Console.WriteLine("属性值：" + aValue + "\t" + "标签内容:" + aInterText);
                */
                richTextBox1.Text += nn.InnerText.ToString() + "\n";
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            string url = "https://news.ycombinator.com/";
            ParseHtml(url);
        }

        private void ParseHtml(string html)
        {
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(html);
            var programmerLinks = doc.DocumentNode.Descendants("tr").Where(node => node.GetAttributeValue("class", "").Contains("athing")).Take(10).ToList();

            foreach (var link in programmerLinks)
            {
                var rank = link.SelectSingleNode(".//span[@class='rank']").InnerText;
                var storyName = link.SelectSingleNode(".//a[@class='storylink']").InnerText;
                var url = link.SelectSingleNode(".//a[@class='storylink']").GetAttributeValue("href", string.Empty);
                var score = link.SelectSingleNode("..//span[@class='score']").InnerText;


                richTextBox1.Text += storyName + "\n";
            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            string url = @"https://find.ruten.com.tw/s/?cateid=001100060001&q=win10";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);
            var docNode = doc.DocumentNode;
            var titleNodes = docNode.SelectNodes(@"//dl[@class='search_form s_grid']//div[@class='prod_info']//h5//a");
            var priceNodes = docNode.SelectNodes(@"//dl[@class='search_form s_grid']//div[@class='prod_info']//ul//li//span[@class='price'][1]");
            int count = titleNodes.Count;
            for (int index = 0; index < count; index++)
            {
                Console.WriteLine("{0} price={1}", titleNodes[index].InnerText, priceNodes[index].InnerText);
            }
        }

        public class Util
        {

            //Get byte[] format page source    
            public static byte[] GetPageSourceBytes(string url)
            {
                WebClient wc = new WebClient();
                byte[] pageSourceBytes = wc.DownloadData(new Uri(url));
                return pageSourceBytes;
            }

            //get string format page source    
            public static string GetPageSource(string url, string encodingType)
            {
                byte[] pageSourceBytes = GetPageSourceBytes(url);
                string pageSource = Encoding.GetEncoding(encodingType).GetString(pageSourceBytes);
                return pageSource;
            }

            //Save image to local file    
            public static void SavaImagesToFile(string url, string dirPath, string fileName)
            {
                if (!Directory.Exists(dirPath))
                {
                    Directory.CreateDirectory(dirPath);
                }
                WebClient wc = new WebClient();
                wc.DownloadFile(url, Path.Combine(dirPath, fileName + Guid.NewGuid().ToString()));
            }
        }

        public class ImageInfo
        {
            public string Title;
            public string SrcPath;
            public static List<ImageInfo> GetImageInfoList(string url)
            {
                // URL:http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15
                string pageSource = Util.GetPageSource(url, "gb2312");
                HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                doc.LoadHtml(pageSource);

                HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//span[@class='tt-w']");

                List<ImageInfo> imageList = new List<ImageInfo>();
                for (int i = 0; i < 24; i++)
                {
                    HtmlNode node = nodes[i];
                    HtmlNode curImageNode = node.SelectSingleNode("//img");
                    HtmlNode curLinkNode = node.SelectSingleNode("a");

                    ImageInfo image = new ImageInfo();
                    image.Title = curLinkNode.InnerText;
                    image.SrcPath = curImageNode.Attributes["src"].Value;
                    imageList.Add(image);
                }
                return imageList;
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            string url = @"https://www.deviantart.com/?order=15";

            int sumCount = 100;
            //string baseUrl = "http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15";

            List<ImageInfo> imageInfoList = new List<ImageInfo>();
            imageInfoList = GetSumImageInfoList(sumCount, url);

            foreach (ImageInfo imageInfo in imageInfoList)
            {
                Util.SavaImagesToFile(imageInfo.SrcPath, @"c:\dddddddddd", GetValidFilename(imageInfo.Title));
            }

            return;
        }

        static string GetValidFilename(string filename)
        {
            foreach (char c in Path.GetInvalidFileNameChars())
            {
                filename = filename.Replace(c, '_');
            }
            return filename;
        }

        static List<ImageInfo> GetSumImageInfoList(int sum, string baseUri)
        {
            List<ImageInfo> resultList = new List<ImageInfo>();
            int c = (sum - 1) / 24 + 1;
            for (int i = 0; i < c; i++)
            {
                int offset = i * 24;
                string url = string.Format("{0}&offset={1}", baseUri, offset);
                List<ImageInfo> curResultList = ImageInfo.GetImageInfoList(url);
                foreach (ImageInfo imageInfo in curResultList)
                {
                    if (resultList.Count < sum)
                    {
                        resultList.Add(imageInfo);
                    }
                }
            }
            return resultList;
        }

        private void button23_Click(object sender, EventArgs e)
        {
            string url = "http://top.baidu.com/buzz.php?p=top_keyword";
            WebClient wc = new WebClient();
            byte[] pageSourceBytes = wc.DownloadData(new Uri(url));
            string pageSource = Encoding.GetEncoding("gb2312").GetString(pageSourceBytes);

            //Regex searchKeyRegex = new Regex("<td class=\"key\">.*?target=\"_blank\">(?<keyWord>.*?)</a></td>");
            //MatchCollection mc = searchKeyRegex.Matches(pageSource);
            //List<string> keyWordList = new List<string>();
            //foreach(Match m in mc)
            //{
            //    keyWordList.Add(m.Groups["keyWord"].Value);
            //}

            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(pageSource);

            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//td[@class='key']/a[@ target='_blank']");
            List<string> keyWords = new List<string>();
            foreach (HtmlNode node in nodes)
            {
                keyWords.Add(node.InnerText);
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //通过HtmlDocument类加载html数据
            string url = @"http://www.zhishilin.com";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(url);
            //XPath路径表达式，这里表示选取所有span节点中的font最后一个子节点，其中span节点的class属性值为num
            HtmlNode node = doc.DocumentNode;
            //根据网页的内容设置XPath路径表达式
            string xpathstring = "//span[@class='num']/font[last()]";
            HtmlNodeCollection nodes = node.SelectNodes(xpathstring);    //所有找到的节点都是一个集合

            if (nodes != null)
            {
                string innertext = nodes[0].InnerText;
                //获取color属性，第二个参数为默认值
                string color = nodes[0].GetAttributeValue("color", "");
                //其他属性大家自己尝试

                richTextBox1.Text += "aaaa = " + innertext + "\n";
                richTextBox1.Text += "cccc = " + color + "\n";
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            /*
            string url = @"http://www.asp.net";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(new WebClient().DownloadString(url));
            var root = doc.DocumentNode;
            var nodes = root.Descendants();
            var totalNodes = nodes.Count();


            richTextBox1.Text += "cnt = " + totalNodes + "\n";
            */

            /*
            string url = @"http://www.asp.net";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(new WebClient().DownloadString(url));
            var root = doc.DocumentNode;
            var anchors = root.Descendants("a");
            var unorderedLists = root.Descendants("ul");

            richTextBox1.Text += unorderedLists + "\n";
            */

            /*
            string url = @"http://www.asp.net";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(new WebClient().DownloadString(url));
            var root = doc.DocumentNode;
            var commonPosts = root.Descendants().Where(n => n.GetAttributeValue("class", "").Equals("common-post"));

            richTextBox1.Text += "aaaa " + commonPosts.ToString() + "\n";
            */

            /*
            //fail
            string url = @"http://forums.asp.net/members/Mikesdotnetting.aspx";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.LoadHtml(new WebClient().DownloadString(url));
            var root = doc.DocumentNode;
            var p = root.Descendants()
                .Where(n => n.GetAttributeValue("class", "").Equals("module-profile-recognition"))
                .Single()
                .Descendants("p")
                .Single();
            var content = p.InnerText;

            richTextBox1.Text += content + "\n";
            */
        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void bt_00_Click(object sender, EventArgs e)
        {
            //Yahoo氣象 台北
            string url = @"https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            string location = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[1]/div[1]/div/h1").InnerText;
            richTextBox1.Text += "位置：" + location + "\n";

            string weather = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[1]/span[2]").InnerText;
            richTextBox1.Text += "現在天氣：" + weather + "\n";

            string temperature = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[3]/span[1]").InnerText;
            richTextBox1.Text += "現在溫度：" + temperature + "\n";

        }

        private void bt_01_Click(object sender, EventArgs e)
        {
            //Yahoo股市 台泥
            string url = @"https://tw.stock.yahoo.com/quote/1101";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            //*[@id="main-0-QuoteHeader-Proxy"]/div/div[2]/div[1]/div/span[1]
            string stock = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[1]").InnerText;
            richTextBox1.Text += "台泥 1101：" + stock + "\n";
        }

        private void bt_02_Click(object sender, EventArgs e)
        {
            //短XPATH //*[@id="entry-272"]/div/div/blockquote/pre[1]
            //長XPATH /html/body/div/div[2]/article/div/div/blockquote/pre[1]

            //Perl學習手札
            string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));

            /* 將網頁顯示出來
            string result = "";
            StreamReader sr = new StreamReader(ms);
            result = sr.ReadToEnd();
            sr.Close();

            richTextBox1.Text += result + "\n";

            */

            //拷貝來的長短XPATH要包在 @"..." 以內
            //拷貝來的短XPATH要在 " 前多一個 "
            string xpath_short = @"//*[@id=""entry-272""]/div/div/blockquote/pre[1]";
            string xpath_full = @"/html/body/div/div[2]/article/div/div/blockquote/pre[1]";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8); //指定編碼格式

            string str = string.Empty;

            str = doc.DocumentNode.SelectSingleNode(xpath_short).InnerText;
            richTextBox1.Text += "使用短XPATH:\t" + str + "\n";

            str = doc.DocumentNode.SelectSingleNode(xpath_full).InnerText;
            richTextBox1.Text += "使用長XPATH:\t" + str + "\n";

            String fullTitle = doc.DocumentNode.SelectSingleNode("//head/title").InnerText;
            richTextBox1.Text += "文件標題 : " + fullTitle + "\n";

            //get urls in page
            foreach (HtmlNode node in doc.DocumentNode.SelectNodes("//a[@href]"))
            {
                string href = node.GetAttributeValue("href", string.Empty);
                HashSet<String> links = new HashSet<String>();
                String[] hrefSplit = href.Split('/');
                String html = hrefSplit[hrefSplit.Length - 1];
                //if the href is not in the disallowed urls, is not already crawled, is not a duplicate link, is a valid html page, and on cnn or bleacherreport
                //if (!disallowedUrls.Any(s => href.Contains(s)) && !alreadyVisitedUrls.Any(s => s.Equals(href)) && !links.Contains(href) && rgx.IsMatch(html) && (href.Contains("cnn.com") || href.Contains("bleacherreport.com")))
                {
                    //store remaining into queue
                    //urlQueue.AddMessage(new CloudQueueMessage(href));

                    //adds link to current link set
                    links.Add(href);
                    richTextBox1.Text += "取得連結 : " + href + "\n";
                }
            }
        }

        private void bt_03_Click(object sender, EventArgs e)
        {
        }

        private void bt_04_Click(object sender, EventArgs e)
        {

        }

        private void bt_05_Click(object sender, EventArgs e)
        {
            string stock_name = string.Empty;
            int stock_number = 0;
            if (radioButton1.Checked == true)
            {
                stock_name = "台積電";
                stock_number = 2330;
            }
            else if (radioButton2.Checked == true)
            {
                stock_name = "聯發科";
                stock_number = 2454;
            }
            else if (radioButton3.Checked == true)
            {
                stock_name = "大立光";
                stock_number = 3008;
            }
            else
            {
                stock_name = "台泥";
                stock_number = 1101;
            }

            //Yahoo股市 + 公司
            string url = @"https://tw.stock.yahoo.com/quote/" + stock_number.ToString();

            ////Yahoo股市 台泥
            //string url = @"https://tw.stock.yahoo.com/quote/1101";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            //richTextBox1.Text += html.Text.ToString();  //顯示頁面原始碼

            richTextBox1.Text += stock_name + "\t" + stock_number.ToString() + "\n";

            string str = string.Empty;
            string name = string.Empty;
            string value = string.Empty;

            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[1]/h1").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[1]/span").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[1]").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[2]").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[3]").InnerText;
            richTextBox1.Text += str + "\n";

            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[1]/span[1]").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[1]/span[2]").InnerText;
            richTextBox1.Text += str + "\n";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[2]/span[1]").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[2]/span[2]").InnerText;
            richTextBox1.Text += str + "\n";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[3]/span[1]").InnerText;
            richTextBox1.Text += str + "\t";
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[2]/div[3]/span[2]").InnerText;
            richTextBox1.Text += str + "\n";

            //成交
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[1]").InnerText;
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "name與value 一起表示\n";
            //成交
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[1]").InnerText;
            richTextBox1.Text += str + "\n";

            //開盤
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[2]").InnerText;
            richTextBox1.Text += str + "\n";

            //最高
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[3]").InnerText;
            richTextBox1.Text += str + "\n";

            //最低
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[4]").InnerText;
            richTextBox1.Text += str + "\n";

            //均價
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[5]").InnerText;
            richTextBox1.Text += str + "\n";

            //成交值(億)
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[6]").InnerText;
            richTextBox1.Text += str + "\n";

            //昨收
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[7]").InnerText;
            richTextBox1.Text += str + "\n";

            //漲跌幅
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[8]").InnerText;
            richTextBox1.Text += str + "\n";

            //漲跌
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[9]").InnerText;
            richTextBox1.Text += str + "\n";

            //總量
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[10]").InnerText;
            richTextBox1.Text += str + "\n";

            //昨量
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[11]").InnerText;
            richTextBox1.Text += str + "\n";

            //振幅
            str = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[12]").InnerText;
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "name與value 分開表示\n";
            //成交
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[1]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[1]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //開盤
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[2]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[2]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //最高
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[3]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[3]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //最低
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[4]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[4]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //均價
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[5]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[5]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //成交值(億)
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[6]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[6]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //昨收
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[7]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[7]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //漲跌幅
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[8]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[8]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //漲跌
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[9]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[9]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //總量
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[10]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[10]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //昨量
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[11]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[11]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";

            //振幅
            name = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[12]/span[1]").InnerText;
            value = doc.DocumentNode.SelectSingleNode(@"//*[@id=""qsp-overview-realtime-info""]/div[2]/div[2]/div/ul/li[12]/span[2]").InnerText;
            richTextBox1.Text += name + "\t\t" + value + "\n";
        }

        private void bt_10_Click(object sender, EventArgs e)
        {
            //https://exfast.me/2016/07/c-use-the-htmlagilitypack-to-collect-web-pages/
            //原價屋
            string url = @"http://www.coolpc.com.tw/evaluate.php";

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));
            // 使用預設編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default); //指定編碼格式

            if (doc != null)
            {
                //判斷所要的商品類型(以CPU為例)，再擷取該商品類型內選單的分類
                var list_type = new List<string>();
                HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//select[@name='n4']//optgroup");

                foreach (HtmlNode node in nodes)
                {
                    var type = node.Attributes["label"].Value;
                    list_type.Add(type);
                }

                //接下來就要該使擷取商品名稱與價格了
                List<string> list_name = doc.DocumentNode.SelectSingleNode("//select[@name='n4']").InnerText.Split('\n').ToList();

                //刪除不必要的非商品選項
                list_name.RemoveRange(0, 3);
                list_name.RemoveAt(list_name.Count - 1);

                //將商品類型與名稱填入Model
                var models = new List<Product>();
                int number = 0;
                for (int i = 0; i < list_name.Count; i++)
                {
                    string type = list_type[number];
                    string name = list_name[i];

                    if (name == "")
                    {
                        number++;
                    }
                    else
                    {
                        models.Add(new Product()
                        {
                            type = type,
                            name = name
                        });

                        Console.WriteLine("類型：{0} ,", type);
                        Console.WriteLine("名稱：{0}", name);
                        richTextBox1.Text += "類型：" + type + "\t名稱：" + name + "\n";
                    }
                }
            }

        }

        private void bt_11_Click(object sender, EventArgs e)
        {
            //M$範例
            //讀取 W3C 首頁中最新公告的程式碼

            string url = @"http://www.w3.org/";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("/html[1]/body[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div");

            richTextBox1.Text += "取得資料:\n";
            foreach (HtmlNode node in nodes)
            {
                richTextBox1.Text += node.InnerText.Trim() + "\n";
            }

            doc = null;
            nodes = null;
            htmlWeb = null;

            richTextBox1.Text += "完成\n";
        }

        private void bt_12_Click(object sender, EventArgs e)
        {
            //https://wings890109.pixnet.net/blog/post/67905792-c%23-htmlagilitypack
            string url = @"http://www.taifex.com.tw/cht/5/stockMargining";

            WebClient wc = new WebClient();

            //HTML Agility Pack預設編碼應是法文編碼，所以如果是讀取中文 HTML 內容的話，
            //無法直接使用HtmlDocument.LoadHtml() 方法，而要透過MemoryStream使用HtmlDocument.Load()方法，才可以指定中文的編碼。
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));

            //使用HtmlDocument.Load()進行編碼，使用UTF8編譯，取得整份網頁結構
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8);    //指定編碼格式

            //從doc向下取得目標資料的html結構
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            string str = doc.DocumentNode.SelectSingleNode(@"//div[@name='printhere']").InnerHtml;

            //richTextBox1.Text += "str = " + str + "\n";
            //return;

            doc1.LoadHtml(doc.DocumentNode.SelectSingleNode(@"//div[@name='printhere']").InnerHtml);

            //獲得更新日期
            string UpdateDate = doc1.DocumentNode.SelectSingleNode(@"/div/p/span").InnerText;

            //從doc1向下取得網頁上目標表格的html結構
            HtmlAgilityPack.HtmlDocument doc2 = new HtmlAgilityPack.HtmlDocument();
            doc2.LoadHtml(doc1.DocumentNode.SelectSingleNode(@"//table[@class='table_c']").InnerHtml);

            //批次取得th資料，利用這些資料進行IEnumarable創造dt的Column
            HtmlNodeCollection nodes = doc2.DocumentNode.SelectNodes(@"//tbody/tr/th");

            DataTable dt = new DataTable();
            foreach (HtmlNode node in nodes)
            {
                dt.Columns.Add(node.InnerText);
                //richTextBox1.Text += "取得\t" + header.InnerText + "\n";
            }

            //可用rows取得所有列的資料，也可直接寫在foreach裡面，tr[td]的意思是選取「所有tr之下有td」的tr們
            //HtmlNodeCollection nodes = dt_html.DocumentNode.SelectNodes(@"//tr[td]");
            foreach (HtmlNode node in doc2.DocumentNode.SelectNodes(@"//tr[td]"))
            {
                //再用SelectNodes批次取得所有td的資料，利用lambda語法取得所有InnerText
                dt.Rows.Add(node.SelectNodes(@"td").Select(td => td.InnerText.Trim()).ToArray());
            }

            richTextBox1.Text += UpdateDate + "\n";
            dataGridView1.DataSource = new BindingSource(dt, null);
            dataGridView1.ColumnHeadersDefaultCellStyle.WrapMode = DataGridViewTriState.False;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
        }

        private void bt_13_Click(object sender, EventArgs e)
        {
            //博客來
            var url = @"https://www.books.com.tw/products/0010916142";
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            string str;
            str = doc.DocumentNode.SelectSingleNode("/html/body/div[4]/div/div[1]/div[2]/div[1]/h1").InnerText;
            richTextBox1.Text += str + "\n";
            str = doc.DocumentNode.SelectSingleNode("/html/body/div[4]/div/div[1]/div[2]/div[1]/h2").InnerText;
            richTextBox1.Text += str + "\n";
        }

        private void bt_14_Click(object sender, EventArgs e)
        {

        }

        private void bt_15_Click(object sender, EventArgs e)
        {

        }

        private void bt_20_Click(object sender, EventArgs e)
        {
            //ok
            //string url = @"../../html/sample.html";
            string url = @"../../html/My_Link2.html";

            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(url, Encoding.UTF8);     //指定編碼格式

            //Get all Hyperlinks in a page
            HtmlNode[] nodes = doc.DocumentNode.SelectNodes("//a").ToArray();
            foreach (HtmlNode nodez in nodes)
            {
                Console.WriteLine(nodez.InnerHtml);
                richTextBox1.Text += "aaa\t" + nodez.InnerHtml + "\n";
            }
            return;

            //Select a specific div in a page

            //Approach 1  
            HtmlNode node = doc.DocumentNode.SelectNodes("//div[@id='div1']").First();

            HtmlNode[] aNodes = node.SelectNodes(".//a").ToArray();

            //Approach 2  
            HtmlNode[] aNodes2 = doc.DocumentNode.SelectNodes("//div[@id='div1']//a").ToArray();

            HtmlNode[] nodes3 = doc.DocumentNode.SelectNodes("//a").Where(x => x.InnerHtml.Contains("div2")).ToArray();
            foreach (HtmlNode node2 in nodes3)
            {
                Console.WriteLine(node2.InnerHtml);
                richTextBox1.Text += "ccc\t" + node2.InnerHtml + "\n";
            }

            richTextBox1.Text += "\n\n================================================================================\n";
            richTextBox1.Text += "================================================================================\n";
            richTextBox1.Text += "================================================================================\n\n\n";

            /* fail
            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData(url));

            // 使用 UTF8 編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.UTF8);    //指定編碼格式

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument doc1 = new HtmlAgilityPack.HtmlDocument();

            HtmlNode[] nodes2 = doc1.DocumentNode.SelectNodes("//a").ToArray();
            foreach (HtmlNode node in nodes2)
            {
                Console.WriteLine(node.InnerHtml);
                richTextBox1.Text += "aaa\t" + node.InnerHtml + "\n";
            }
            */
        }

        private void bt_21_Click(object sender, EventArgs e)
        {
            //可解析本地文件

            string url = @"../../html/aaaaa.html";

            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();

            doc.OptionOutputOriginalCase = true;    //正確區分大小寫

            doc.Load(url);
            //HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//div");
            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("//img");
            foreach (HtmlNode node in nodes)
            {
                string templateString = node.InnerHtml; //lower case happens here.....

                richTextBox1.Text += "aaaaa" + templateString + "\n";
            }
        }

        private void bt_22_Click(object sender, EventArgs e)
        {
            string url = @"../../html/My_Link2.html";

            //get HtmlAgilityPack.HtmlDocument object   
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            //load HTML   
            doc.LoadHtml(url);
            //get HtmlNode by ID   

            //fail

            return;

            HtmlNode node = doc.GetElementbyId("CENTER");
            richTextBox1.Text += "ccccc" + node.InnerHtml + "\n";
        }

        /// <summary>  
        /// 定義的實體類用於接收數據  
        /// </summary>  
        public class Data
        {
            public string 時間 { get; set; }
            public string 類型 { get; set; }
            public string 名稱 { get; set; }
            public string 單位 { get; set; }
            public string 金額 { get; set; }
        }

        private void bt_23_Click(object sender, EventArgs e)
        {
            string strWebContent = @"<table><thead>  
        <tr>  
          <th>時間</th>  
          <th>類型</th>  
          <th>名稱</th>  
          <th>單位</th>  
          <th>金額</th>  
        </tr>  
        </thead>  
        <tbody>" +
@"<tr>  
          <td>2013-12-29</td>  
          <td>發票1</td>  
          <td>採購物資發票1</td>  
          <td>某某公司1</td>  
          <td>123元</td>  
        </tr>" +
@"<tr>  
          <td>2013-12-29</td>  
          <td>發票2</td>  
          <td>採購物資發票2</td>  
          <td>某某公司2</td>  
          <td>321元</td>  
        </tr>  
        </tbody>  
      </table>  
    ";

            string url = @"../../html/buy.html";

            List<Data> datas = new List<Data>();//定義1個列表用於保存結果  

            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            
            doc.LoadHtml(strWebContent);//加載HTML字符串，如果是文件可以用htmlDocument.Load方法加載
            //doc.LoadHtml(url);    fail

            HtmlNodeCollection collection = doc.DocumentNode.SelectSingleNode("table/tbody").ChildNodes;//跟Xpath一樣，輕鬆的定位到相應節點下  
            foreach (HtmlNode node in collection)
            {
                //去除\r\n以及空格，獲取到相應td裏面的數據  
                string[] line = node.InnerText.Split(new char[] { '\r', '\n', ' ' }, StringSplitOptions.RemoveEmptyEntries);

                //如果符合條件，就加載到對象列表裏面  
                if (line.Length == 5)
                {
                    datas.Add(new Data() { 時間 = line[0], 類型 = line[1], 名稱 = line[2], 單位 = line[3], 金額 = line[4] });
                }
            }

            //循環輸出查看結果是否正確  
            foreach (var v in datas)
            {
                Console.WriteLine(string.Join(",", v.時間, v.類型, v.名稱, v.單位, v.金額));

                richTextBox1.Text += string.Join(",", v.時間, v.類型, v.名稱, v.單位, v.金額) + "\n";
            }
        }

        private void bt_24_Click(object sender, EventArgs e)
        {
            //Perl學習手札
            //string url = @"https://www.syhtcgf.com/perl/perl-toc/about_toc.html";
            string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";

            try
            {
                HtmlWeb htmlWeb = new HtmlWeb();
                HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                doc = htmlWeb.Load(url);

                foreach (HtmlNode node in doc.DocumentNode.SelectNodes("//a[@href]"))
                {
                    try
                    {
                        HtmlAttribute att = node.Attributes["href"];
                        Console.WriteLine(att.Value);
                        richTextBox1.Text += "找到 href \t" + att.Value + "\n";
                        //this._results.Add(new Uri(att.Value));
                    }
                    catch
                    {

                    }
                }

                foreach (HtmlNode node in doc.DocumentNode.SelectNodes("//article[@id]"))
                {
                    try
                    {
                        HtmlAttribute att = node.Attributes["id"];
                        Console.WriteLine(att.Value);
                        richTextBox1.Text += "找到 id \t" + att.Value + "\n";
                        //this._results.Add(new Uri(att.Value));
                    }
                    catch
                    {

                    }
                }
            }
            catch
            {
                //What Should I Do Here?
                //Maybe Nothing for Now
            }
        }

        private void bt_25_Click(object sender, EventArgs e)
        {
            string url = @"https://www.technologycrowds.com/";

            ExtractHref(url);
        }

        void ExtractHref(string url)
        {
            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc = htmlWeb.Load(url);

            // extracting all links
            foreach (HtmlNode node in doc.DocumentNode.SelectNodes("//a[@href]"))
            {
                HtmlAttribute att = node.Attributes["href"];

                if (att.Value.Contains("a"))
                {
                    // showing output
                    Console.WriteLine(att.Value);
                    richTextBox1.Text += "取得連結:\t" + att.Value + "\n";
                }
            }
        }
    }

    class Product
    {
        public string type { get; set; }

        public string name { get; set; }
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
