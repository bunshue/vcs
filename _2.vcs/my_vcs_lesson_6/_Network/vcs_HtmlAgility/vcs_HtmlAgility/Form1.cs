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


/* Yahoo 氣象
taipei
https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179


hsinchu
https://tw.news.yahoo.com/weather/%E5%8F%B0%E7%81%A3/%E6%96%B0%E7%AB%B9%E5%B8%82/%E6%96%B0%E7%AB%B9%E5%B8%82-2306185
*/


            
/*
要用Chrome
開啟網頁 : https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179

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
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 3, y_st + dy * 4);

            x_st = 20;
            y_st = 20;
            dx = 200;
            dy = 75;
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

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

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData("http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm"));    //fail在此
            //以台灣銀行為範例

            // 使用預設編碼讀入 HTML 
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default);

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
            doc.Load(ms, Encoding.Default);

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument hdc = new HtmlAgilityPack.HtmlDocument();

            //XPath 來解讀它 /html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1] 
            hdc.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭 
            HtmlNodeCollection htnode = hdc.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值 
            string[] txt = hdc.DocumentNode.SelectSingleNode("./tr[2]").InnerText.Trim().Split('\n');
            int i = 0;

            // 輸出資料 
            foreach (HtmlNode nodeHeader in htnode)
            {
                //將 "加到投資組合" 這個字串過濾掉
                richTextBox1.Text += nodeHeader.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "\n";
                i++;
            }

            //清除資料
            doc = null;
            hdc = null;
            wc = null;
            ms.Close();




        }

        private void button2_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jackbgova/2015/01/14/148093
            /*
            //指定來源網頁
            WebClient url = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(url.DownloadData("http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm"));
            //以台灣銀行為範例

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default);

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
            url = null;
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
            WebClient client = new WebClient();
            MemoryStream ms = new MemoryStream(client.DownloadData(
        "http://tw.stock.yahoo.com/q/q?s=2317"));

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default);

            // 裝載第一層查詢結果
            HtmlAgilityPack.HtmlDocument docStockContext = new HtmlAgilityPack.HtmlDocument();

            docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode(
        "/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭
            HtmlNodeCollection nodeHeaders =
         docStockContext.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值
            string[] values = docStockContext.DocumentNode.SelectSingleNode(
        "./tr[2]").InnerText.Trim().Split('\n');
            int i = 0;

            // 輸出資料
            foreach (HtmlNode nodeHeader in nodeHeaders)
            {
                Console.WriteLine("Header: {0}, Value: {1}",
        nodeHeader.InnerText, values[i].Trim());
                i++;
            }

            doc = null;
            docStockContext = null;
            client = null;
            ms.Close();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //https://dotblogs.com.tw/jackbgova/2014/12/08/147553
            //fail
            //指定來源網頁
            WebClient url = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(url.DownloadData("http://tw.stock.yahoo.com/q/q?s=3008"));
            //以奇摩股市為例http://tw.stock.yahoo.com，3008以大立光為例

            // 使用預設編碼讀入 HTML
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(ms, Encoding.Default);

            //XPath 來解讀它 /html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]
            doc.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/center[1]/table[2]/tr[1]/td[1]/table[1]").InnerHtml);

            // 取得個股標頭
            HtmlNodeCollection htnode = doc.DocumentNode.SelectNodes("./tr[1]/th");
            // 取得個股數值
            string[] txt = doc.DocumentNode.SelectSingleNode("./tr[2]").InnerText.Trim().Split('\n');

            int i = 0;

            // 輸出資料
            foreach (HtmlNode nodeHeader in htnode)
            {
                //將 "加到投資組合" 這個字串過濾掉
                //Response.Write(nodeHeader.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "<br />");
                richTextBox1.Text += nodeHeader.InnerText + ":" + txt[i].Trim().Replace("加到投資組合", "") + "\n";
                i++;
            }
            //清除資料
            doc = null;
            url = null;
            ms.Close();

        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

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

            using (WebClient client = new WebClient())
            {
                using (MemoryStream ms = new MemoryStream(client.DownloadData(Url)))
                {
                    HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
                    doc.Load(ms, encoding);

                    // All content
                    HtmlAgilityPack.HtmlDocument docStockContext = new HtmlAgilityPack.HtmlDocument();

                    docStockContext.LoadHtml(doc.DocumentNode.SelectSingleNode(xPathFirst).InnerHtml);

                    // Content value
                    HtmlNodeCollection nodeHeaders = docStockContext.DocumentNode.SelectNodes(string.Format(xPathSecond, TableRowNum));

                    foreach (HtmlNode nodeHeader in nodeHeaders)
                    {
                        ListData.Add(nodeHeader.InnerHtml);
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
            doc.Load(ms, Encoding.UTF8);

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument hdc = new HtmlAgilityPack.HtmlDocument();

            //XPath 來解讀它 /html[1]/body[1]/div[3]
            hdc.LoadHtml(doc.DocumentNode.SelectSingleNode("/html[1]/body[1]/div[3]").InnerHtml);
            //這邊因為公告內文含有 img tag 所以需使用 InnerHtml
            string txt = hdc.DocumentNode.SelectSingleNode(".").InnerHtml.Trim();
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
            doc.Load(ms, Encoding.UTF8);

            // 裝載第一層查詢結果 
            HtmlAgilityPack.HtmlDocument hdc = new HtmlAgilityPack.HtmlDocument();

            // XPath 來解讀它
            hdc.LoadHtml(doc.DocumentNode.SelectSingleNode(XPath).InnerHtml);

            HtmlNodeCollection htnode = hdc.DocumentNode.SelectNodes(@"//div[@class='GN-lbox2B']/div/a");

            foreach (HtmlNode currNode in htnode)
            {
                string currLink = currNode.SelectSingleNode(".").Attributes["href"].Value;
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
            HtmlNodeCollection mtchrslts = doc.DocumentNode.SelectNodes("//tr[@id]");

            string date;
            string ateam;
            string hteam;
            string score;
            string idmess;
            string idnum;
            string[] teamscores;
            string teamscoreh;
            string teamscorea;

            foreach (HtmlNode matchresult in mtchrslts)
            {
                idmess = matchresult.SelectSingleNode("//tr[@id]").Id;
                idnum = idmess.Replace("match-row-", "");
                score = matchresult.SelectSingleNode("//abbr[@title='Score']").InnerText;
                teamscores = score.Split('-');
                teamscoreh = teamscores[0];
                teamscorea = teamscores[1];
                hteam = matchresult.SelectSingleNode("//p[(@class='team-home teams')]").InnerText;
                ateam = matchresult.SelectSingleNode("//p[(@class='team-away teams')]").InnerText;
                date = matchresult.SelectSingleNode("//td[(@class='match-date')]").InnerText;
            }

            return;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            List<string> outList = new List<string>();

            string url = @"https://yandex.by/search/?numdoc=10&p=0&rdrnd=601861&text=kinogo.co%20Один%20дома%201990%20&lr=157";
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            var web = new HtmlWeb
            {
                AutoDetectEncoding = false,
                OverrideEncoding = Encoding.UTF8 //GetEncoding("windows-1251")
            };

            doc = web.Load(url);

            HtmlNodeCollection NoAltElements = doc.DocumentNode.SelectNodes("//div");

            if (NoAltElements != null)
            {
                foreach (HtmlNode node in NoAltElements)
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
            string res = "", temp = "";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc;
            HtmlNode n;

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
                    if ((n = doc.DocumentNode.SelectSingleNode("//*[@id=\"bibtex\"]/p")) != null)
                    {
                        temp = n.InnerText;
                        temp = temp.Replace(",", ",\n").Replace("&nbsp;", " ");
                    }
                }
                catch (Exception e) { }
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
                HtmlAgilityPack.HtmlDocument doc = new HtmlWeb().Load("https://www.facebook.com/ABCNetwork/");

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

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {
            string url = "http://www.baidu.com";
            HtmlWeb web = new HtmlWeb();
            //从url中加载
            HtmlAgilityPack.HtmlDocument doc = web.Load(url);
            //获得title标签节点，其子标签下的所有节点也在其中
            HtmlNode headNode = doc.DocumentNode.SelectSingleNode("//title");
            
            //获得title标签中的内容
            string Title = headNode.InnerText;

            richTextBox1.Text += "取得標題:\t" + Title + "\n";

            //获得id选择器为u1标签（是u1非ul（L）)节点
            HtmlNode aNode = doc.DocumentNode.SelectSingleNode("//div[@id='u1']");
            //获得ul标签下的所有子节点
            HtmlNodeCollection aCollection = aNode.ChildNodes;
            foreach (var item in aCollection)
            {
                /*
                //获得标签属性为href的值
                string aValue = item.Attributes["href"].Value;
                //获得标签内的内容
                string aInterText = item.InnerText;
                Console.WriteLine("属性值：" + aValue + "\t" + "标签内容:" + aInterText);
                */
                richTextBox1.Text += item.InnerText.ToString() + "\n";
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //string url = @"https://www.syhtcgf.com/perl/perl-toc/about_toc.html";
            string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";

            try
            {
                HtmlWeb htmlWeb = new HtmlWeb();
                HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);

                foreach (HtmlNode link in doc.DocumentNode.SelectNodes("//a[@href]"))
                {
                    try
                    {
                        HtmlAttribute att = link.Attributes["href"];
                        Console.WriteLine(att.Value);
                        richTextBox1.Text += "找到 href \t" + att.Value + "\n";
                        //this._results.Add(new Uri(att.Value));
                    }
                    catch
                    {

                    }
                }

                foreach (HtmlNode link in doc.DocumentNode.SelectNodes("//article[@id]"))
                {
                    try
                    {
                        HtmlAttribute att = link.Attributes["id"];
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

        private void bt_00_Click(object sender, EventArgs e)
        {
            string url = @"https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);

            string location = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[1]/div[1]/div/h1").InnerText;
            richTextBox1.Text += "位置：" + location + "\n";

            string weather = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[1]/span[2]").InnerText;
            richTextBox1.Text += "現在天氣：" + weather + "\n";

            string temperature = doc.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[3]/span[1]").InnerText;
            richTextBox1.Text += "現在溫度：" + temperature + "\n";

        }

        private void bt_01_Click(object sender, EventArgs e)
        {
            string url = @"https://tw.stock.yahoo.com/quote/1101";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);

            //*[@id="main-0-QuoteHeader-Proxy"]/div/div[2]/div[1]/div/span[1]
            string stock = doc.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[1]").InnerText;
            richTextBox1.Text += "台泥 1101：" + stock + "\n";

        }

        private void bt_02_Click(object sender, EventArgs e)
        {
            //短XPATH //*[@id="entry-272"]/div/div/blockquote/pre[1]
            //長XPATH /html/body/div/div[2]/article/div/div/blockquote/pre[1]

            string url = @"https://www.syhtcgf.com/perl/perl-toc/ch09.html";

            //拷貝來的長短XPATH要包在 @"..." 以內
            //拷貝來的短XPATH要在 " 前多一個 "
            string xpath_short = @"//*[@id=""entry-272""]/div/div/blockquote/pre[1]";
            string xpath_full = @"/html/body/div/div[2]/article/div/div/blockquote/pre[1]";

            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);
            string str = string.Empty;

            str = doc.DocumentNode.SelectSingleNode(xpath_short).InnerText;
            richTextBox1.Text += "使用短XPATH:\t" + str + "\n";

            str = doc.DocumentNode.SelectSingleNode(xpath_full).InnerText;
            richTextBox1.Text += "使用長XPATH:\t" + str + "\n";


            String fullTitle = doc.DocumentNode.SelectSingleNode("//head/title").InnerText;
            richTextBox1.Text += "文件標題 : " + fullTitle + "\n";


            //get urls in page
            foreach (HtmlNode link in doc.DocumentNode.SelectNodes("//a[@href]"))
            {
                string href = link.GetAttributeValue("href", string.Empty);
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

            string url = @"https://tw.stock.yahoo.com/quote/" + stock_number.ToString();

            //string url = @"https://tw.stock.yahoo.com/quote/1101";


            HtmlWeb htmlWeb = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);

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
            doc.Load(ms, Encoding.Default);

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
            HtmlAgilityPack.HtmlDocument doc = htmlWeb.Load(url);

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
            MemoryStream memoryStream = new MemoryStream(wc.DownloadData(url));

            //使用HtmlDocument.Load()進行編碼，使用UTF8編譯，取得整份網頁結構
            HtmlAgilityPack.HtmlDocument doc = new HtmlAgilityPack.HtmlDocument();
            doc.Load(memoryStream, Encoding.UTF8);


            //從doc向下取得目標資料的html結構
            HtmlAgilityPack.HtmlDocument docData = new HtmlAgilityPack.HtmlDocument();
            docData.LoadHtml(doc.DocumentNode.SelectSingleNode(@"//div[@name='printhere']").InnerHtml);

            //獲得更新日期
            string UpdateDate = docData.DocumentNode.SelectSingleNode(@"/div/p/span").InnerText;

            //從docData向下取得網頁上目標表格的html結構
            HtmlAgilityPack.HtmlDocument dt_html = new HtmlAgilityPack.HtmlDocument();
            dt_html.LoadHtml(docData.DocumentNode.SelectSingleNode(@"//table[@class='table_c']").InnerHtml);

            //批次取得th資料，利用這些資料進行IEnumarable創造dt的Column
            HtmlNodeCollection headers = dt_html.DocumentNode.SelectNodes(@"//tbody/tr/th");

            DataTable dt = new DataTable();
            foreach (HtmlNode header in headers)
            {
                dt.Columns.Add(header.InnerText);
            }

            //可用rows取得所有列的資料，也可直接寫在foreach裡面，tr[td]的意思是選取「所有tr之下有td」的tr們
            //HtmlNodeCollection rows = dt_html.DocumentNode.SelectNodes(@"//tr[td]");
            foreach (HtmlNode row in dt_html.DocumentNode.SelectNodes(@"//tr[td]"))
            {
                //再用SelectNodes批次取得所有td的資料，利用lambda語法取得所有InnerText
                dt.Rows.Add(row.SelectNodes(@"td").Select(td => td.InnerText.Trim()).ToArray());
            }

            richTextBox1.Text += UpdateDate + "\n";
            dataGridView1.DataSource = new BindingSource(dt, null);
            dataGridView1.ColumnHeadersDefaultCellStyle.WrapMode = DataGridViewTriState.False;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
        }

        private void bt_13_Click(object sender, EventArgs e)
        {

        }

        private void bt_14_Click(object sender, EventArgs e)
        {

        }

        private void bt_15_Click(object sender, EventArgs e)
        {

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
