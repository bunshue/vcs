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
            x_st = 10;
            y_st = 10;
            dx = 170;
            dy = 75;

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
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //fail

            //指定來源網頁
            WebClient wc = new WebClient();
            //將網頁來源資料暫存到記憶體內
            MemoryStream ms = new MemoryStream(wc.DownloadData("http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm"));
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
            string url = @"https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179";

            HtmlWeb hap = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument html = hap.Load(url);

            string location = html.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[1]/div[1]/div/h1").InnerText;
            richTextBox1.Text += "位置：" + location + "\n";

            string weather = html.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[1]/span[2]").InnerText;
            richTextBox1.Text += "現在天氣：" + weather + "\n";

            string temperature = html.DocumentNode.SelectSingleNode(@"//*[@id=""Lead-1-WeatherLocationAndTemperature""]/div/section[2]/div/div[3]/span[1]").InnerText;
            richTextBox1.Text += "現在溫度：" + temperature + "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string url = @"https://tw.stock.yahoo.com/quote/1101";

            HtmlWeb hap = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument html = hap.Load(url);

            //*[@id="main-0-QuoteHeader-Proxy"]/div/div[2]/div[1]/div/span[1]
            string stock = html.DocumentNode.SelectSingleNode(@"//*[@id=""main-0-QuoteHeader-Proxy""]/div/div[2]/div[1]/div/span[1]").InnerText;
            richTextBox1.Text += "台泥 1101：" + stock + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //M$範例
            //讀取 W3C 首頁中最新公告的程式碼

            string url = @"http://www.w3.org/";

            HtmlWeb hap = new HtmlWeb();
            HtmlAgilityPack.HtmlDocument doc = hap.Load(url);

            HtmlNodeCollection nodes = doc.DocumentNode.SelectNodes("/html[1]/body[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div");

            richTextBox1.Text += "取得資料:\n";
            foreach (HtmlNode node in nodes)
            {
                richTextBox1.Text += node.InnerText.Trim() + "\n";
            }

            doc = null;
            nodes = null;
            hap = null;

            richTextBox1.Text += "完成\n";
        }

        //private WebClient webClient = new WebClient();
        //private MemoryStream memoryStream = null;

        public string UpdateDate = "";
        public DataTable dt = new DataTable();

        private void button6_Click(object sender, EventArgs e)
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
            docData.LoadHtml(doc.DocumentNode.SelectSingleNode(@"//div[@name='printhere']")
                                             .InnerHtml);

            //獲得更新日期
            UpdateDate = docData.DocumentNode.SelectSingleNode(@"/div/p/span").InnerText;

            //從docData向下取得網頁上目標表格的html結構
            HtmlAgilityPack.HtmlDocument dt_html = new HtmlAgilityPack.HtmlDocument();
            dt_html.LoadHtml(docData.DocumentNode.SelectSingleNode(@"//table[@class='table_c']")
                                                 .InnerHtml);

            //批次取得th資料，利用這些資料進行IEnumarable創造dt的Column
            HtmlNodeCollection headers = dt_html.DocumentNode.SelectNodes(@"//tbody/tr/th");

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

            label1.Text = UpdateDate;
            dataGridView1.DataSource = new BindingSource(dt, null);
            dataGridView1.ColumnHeadersDefaultCellStyle.WrapMode = DataGridViewTriState.False;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;

        }

        private void button7_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
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



