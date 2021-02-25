using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for SmoothingMode

using System.Net;
using System.Xml;
using System.IO;
using System.Globalization;

/* example
搜尋城市：Hsinchu
url : 
http://api.openweathermap.org/data/2.5/forecast?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc
data
<?xml version="1.0" encoding="UTF-8"?>
<weatherdata><location><name>Hsinchu</name><type></type><country>TW</country><timezone>28800</timezone><location altitude="0" latitude="24.8036" longitude="120.9686" geobase="geonames" geobaseid="1675151"></location></location><credit></credit><meta><lastupdate></lastupdate><calctime>0</calctime><nextupdate></nextupdate></meta><sun rise="2021-02-09T22:33:52" set="2021-02-10T09:46:59"></sun>

<forecast>

<time from="2021-02-10T12:00:00" to="2021-02-10T15:00:00"><symbol number="501" name="moderate rain" var="10n"></symbol><precipitation probability="1" unit="3h" value="4.69" type="rain"></precipitation><windDirection deg="261" code="W" name="West"></windDirection><windSpeed mps="6.91" unit="mph" name="Light breeze"></windSpeed><temperature unit="fahrenheit" value="64.47" min="64.47" max="66.04"></temperature><feels_like value="64.78" unit="fahrenheit"></feels_like><pressure unit="hPa" value="1010"></pressure><humidity value="93" unit="%"></humidity><clouds value="overcast clouds" all="96" unit="%"></clouds><visibility value="10000"></visibility></time>

<time from="2021-02-10T15:00:00" to="2021-02-10T18:00:00"><symbol number="500" name="light rain" var="10n"></symbol><precipitation probability="1" unit="3h" value="1.87" type="rain"></precipitation><windDirection deg="239" code="WSW" name="West-southwest"></windDirection><windSpeed mps="7.23" unit="mph" name="Light breeze"></windSpeed><temperature unit="fahrenheit" value="64.85" min="64.85" max="65.35"></temperature><feels_like value="65.01" unit="fahrenheit"></feels_like><pressure unit="hPa" value="1010"></pressure><humidity value="92" unit="%"></humidity><clouds value="overcast clouds" all="98" 
*/

namespace vcs_Network3_Weather
{
    public partial class Form1 : Form
    {
        List<float> temperature = new List<float>();
        List<string> date = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Items.Add("City");
            comboBox1.Items.Add("ZIP");
            comboBox1.Items.Add("ID");

            comboBox1.SelectedIndex = 0;

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        // Enter your API key here.
        // Get an API key by making a free account at:
        //      http://home.openweathermap.org/users/sign_in
        private const string API_KEY = "lionmouse";

        // Query URLs. Replace @LOCATION@ with the location.
        //即時天氣
        private const string CurrentUrl = "http://api.openweathermap.org/data/2.5/weather?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
        //天氣預測
        private const string ForecastUrl = "http://api.openweathermap.org/data/2.5/forecast?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;

        // Query URLs. Replace @LOCATION@ with the location.
        //即時天氣
        private const string CurrentUrl2 = "http://api.openweathermap.org/data/2.5/weather?" + "@QUERY@=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
        //天氣預測
        private const string ForecastUrl2 = "http://api.openweathermap.org/data/2.5/forecast?" + "@QUERY@=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;

        // Query codes.
        private string[] QueryCodes = { "q", "zip", "id", };

        /*
        //若是只查詢代碼為City(q)之條件, 用 q 取代 @QUERY@
        // Query URLs. Replace @LOCATION@ with the location.
        //即時天氣
        private const string CurrentUrl = "http://api.openweathermap.org/data/2.5/weather?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
        //天氣預測
        private const string ForecastUrl = "http://api.openweathermap.org/data/2.5/forecast?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
        */

        // List the temperature forecast.
        private void btnForecast_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "搜尋城市：" + txtLocation.Text + "\n";
            Cursor = Cursors.WaitCursor;

            // Compose the query URL.
            string url = ForecastUrl.Replace("@LOCATION@", txtLocation.Text);

            richTextBox1.Text += "url : \n" + url + "\n";

            // Create a web client.
            XmlDocument xml_doc;
            using (WebClient client = new WebClient())
            {
                try
                {
                    // Get the response string from the URL.
                    string xml = client.DownloadString(url);

                    //richTextBox1.Text += "data\n" + xml + "\n";

                    // Load the response into an XML document.
                    xml_doc = new XmlDocument();
                    xml_doc.LoadXml(xml);

                    // List the temperatures.
                    ListTemperatures(xml_doc);
                }
                catch (FormatException)
                {
                    // A formatting error occurred.
                    // Report the error to the user.
                    richTextBox1.Text += "數值錯誤\n";
                }
                catch (Exception ex)
                {
                    // Some other error occurred.
                    // Report the error to the user.
                    richTextBox1.Text += "計算錯誤\t原因 : " + ex + "\n";
                    richTextBox1.Text += "計算錯誤\t原因 : " + ex.GetType().Name + "\n";
                }
                finally
                {
                    //richTextBox1.Text += "計算結束\n";
                }
            }
            Cursor = Cursors.Default;
        }

        // List the temperatures.
        private void ListTemperatures(XmlDocument xml_doc)
        {
            listView1.Items.Clear();
            temperature.Clear();
            date.Clear();

            /*
            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";

            XmlNode geo_node = loc_node.SelectSingleNode("location");
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n\n";

            foreach (XmlNode sun_node in xml_doc.SelectNodes("//sun"))
            {
                XmlAttribute time_attr1 = sun_node.Attributes["rise"];
                XmlAttribute time_attr2 = sun_node.Attributes["set"];
                richTextBox1.Text += "日出 : " + DateTime.Parse(time_attr1.Value).ToLocalTime() + "\n";
                richTextBox1.Text += "日落 : " + DateTime.Parse(time_attr2.Value).ToLocalTime() + "\n";
            }
            */

            char degrees = (char)176;

            // Loop throuh the time entries.
            string last_day = "";
            int aaa = 0;
            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the start date and time.
                XmlAttribute time_attr1 = time_node.Attributes["from"];
                XmlAttribute time_attr2 = time_node.Attributes["to"];

                aaa++;
                /* 解讀xml資料 
                richTextBox1.Text += "取得第 " + aaa.ToString() + " 筆資料 : " + time_attr1.Value + "\t" + time_attr2.Value + "\n";

                richTextBox1.Text += "預測時間 : " + DateTime.Parse(time_attr1.Value).ToLocalTime() + " 到 " + DateTime.Parse(time_attr2.Value).ToLocalTime()
                    + "\t 中間 " + (DateTime.Parse(time_attr1.Value) + new TimeSpan(1, 30, 0)).ToLocalTime() + "\n";

                richTextBox1.Text += "symbol" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["number"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["name"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["var"].Value.ToString() + "\n";

                richTextBox1.Text += "precipitation" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("precipitation").Attributes["probability"].Value.ToString() + "\n";

                richTextBox1.Text += "windDirection" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["deg"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["code"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["name"].Value.ToString() + "\n";

                richTextBox1.Text += "windSpeed" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["mps"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["name"].Value.ToString() + "\n";

                richTextBox1.Text += "temperature" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["min"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["max"].Value.ToString() + "\n";

                richTextBox1.Text += "feels_like" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("feels_like").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("feels_like").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "pressure" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("pressure").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("pressure").Attributes["value"].Value.ToString() + "\n";

                richTextBox1.Text += "humidity" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("humidity").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("humidity").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "clouds" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["all"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "visibility" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("visibility").Attributes["value"].Value.ToString() + "\n";
                */

                DateTime start_time = DateTime.Parse(time_attr1.Value);

                // Convert from UTC to local time.
                start_time = start_time.ToLocalTime();

                // Add 90 minutes to get to the middle of the interval.
                start_time += new TimeSpan(1, 30, 0);

                // Get the temperature node.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                XmlAttribute temp_attr = temp_node.Attributes["value"];
                float temp = 0;
                if (temp_attr != null)
                {
                    temp = float.Parse(temp_attr.Value.ToString());
                }

                ListViewItem item;
                if (start_time.DayOfWeek.ToString() == last_day)
                {
                    item = listView1.Items.Add("");
                }
                else
                {
                    last_day = start_time.DayOfWeek.ToString();
                    item = listView1.Items.Add(last_day);
                }
                item.SubItems.Add(start_time.ToShortTimeString());
                item.SubItems.Add(temp.ToString("0.00") + " " + degrees + "F");
                item.SubItems.Add(((temp - 32) * 5 / 9).ToString("0.00") + " " + degrees + "C");
                temperature.Add((temp - 32) * 5 / 9);
                date.Add(start_time.ToShortTimeString());
            }

            int i;
            richTextBox1.Text += "temperature len = " + temperature.Count.ToString() + "\n";
            for (i = 0; i < temperature.Count; i++)
            {
                richTextBox1.Text += temperature[i].ToString() + "\n";
            }

            richTextBox1.Text += "date len = " + date.Count.ToString() + "\n";
            for (i = 0; i < date.Count; i++)
            {
                richTextBox1.Text += date[i].ToString() + "\n";
            }

            Pen thin_pen = new Pen(Color.Black, 0);
            thin_pen.Color = Color.LightBlue;
            /* debug
            int num_numbers = 10;
            float[] numbers = new float[num_numbers];
            Random rand = new Random();
            for (i = 0; i < num_numbers; i++)
            {
                //result4 += r.NextDouble().ToString() + " ";
                numbers[i] = (float)rand.NextDouble() * 100;
                richTextBox1.Text += numbers[i].ToString() + " ";
            }
            */
            DrawHistogramF(pictureBox1, Brushes.Blue, thin_pen, temperature.ToArray());
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            listView1.Items.Clear();
            txtCity.Text = "";
            txtCountry.Text = "";
            txtLat.Text = "";
            txtLong.Text = "";
            txtId.Text = "";
        }

        // Display a histogram.
        private void DrawHistogramF(PictureBox pic, Brush brush, Pen pen, float[] values)
        {
            int border_x = 4;   //percentage of width
            int border_y = 12;  //percentage of height
            int W = pic.ClientSize.Width;
            int H = pic.ClientSize.Height;
            int N = values.Length;
            int w = W * (100 - border_x * 2) / N / 100;
            //int h = 0;

            float y_max = values.Max();
            float y_min = values.Min();
            float y_diff = y_max - y_min;
            //int ratio_x = 0;
            float ratio_y = H * (100 - border_y * 2) / (y_diff + 15) / 100;

            int x_st = border_x * W / 100;
            int y_st = border_y * H / 100;
            //richTextBox1.Text += "y_st = " + y_st.ToString() + "\n";

            richTextBox1.Text += "\n";
            richTextBox1.Text += "N = " + N.ToString() + "\n";
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";
            richTextBox1.Text += "y_diff = " + y_diff.ToString() + "\n";


            //先考慮滿框狀態

            int i;

            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + values[i].ToString() + "\n";

            }

            // Make a Bitmap.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;

                // Fill the histogram.
                for (i = 0; i < N; i++)
                {
                    g.FillRectangle(brush, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);

                    richTextBox1.Text += "i = " + i.ToString() + "\t" + (x_st + i * w).ToString() + "\t" + (H - values[i] * ratio_y - y_st).ToString() + " " + w.ToString() + " " + (values[i] * ratio_y).ToString() + "\n";
                    //g.DrawString(values[i].ToString(), new Font("標楷體", 8), new SolidBrush(Color.Red), new PointF(x_st + i * w + w / 3, H - y_st + 3));
                    //g.DrawString(date[i].ToString(), new Font("標楷體", 6), new SolidBrush(Color.Red), new PointF(x_st + i * w + w / 3, H - y_st + 3));
                }

                // Draw the histogram.
                if (N < 200)
                {
                    for (i = 0; i < N; i++)
                    {
                        //g.DrawRectangle(pen, i * w, 0, w, values[i] * ratio_y);
                        g.DrawRectangle(pen, x_st + i * w, H - values[i] * ratio_y - y_st, w, values[i] * ratio_y);
                    }
                }
            }

            // Display the histogram.
            pic.Image = bitmap1;
        }


        // 標準版XML讀取解析程式 ST
        private void ParseXML(string filename)
        {
            //加載XML文件
            XmlDocument xdDocument = new XmlDocument();
            richTextBox1.Text += "開啟XML文件 : " + filename + "\n";
            xdDocument.Load(filename);

            //得到主節點
            XmlElement xeRoot = xdDocument.DocumentElement;
            if (xeRoot != null)
            {
                XmlNode xnNodeRoot = (XmlNode)xeRoot;
                RecurseXmlDocument(xnNodeRoot, 0);
                richTextBox1.Text += "\n讀取XML文件 : " + filename + " 完成\n";
            }
        }

        /// <summary>
        /// 讀取ＸＭＬ
        /// </summary>
        /// <param name="aXnNode">節點</param>
        /// <param name="aIndent">縮進大小</param>
        private void RecurseXmlDocument(XmlNode aXnNode, int aIndent)
        {
            //判斷結點中是否有內容
            if (aXnNode == null)
            {
                return;
            }

            //節點是元素時
            if (aXnNode is XmlElement)
            {
                //顯示根元素的名稱
                richTextBox1.Text += "\n\t根元素 : " + "\"" + aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent) + "\"" + "\t";
                //lbXmlValue.Items.Add(aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent));
                if (aXnNode.Attributes != null)
                {
                    //得到屬性
                    foreach (XmlAttribute xaAttribute in aXnNode.Attributes)
                    {
                        string sText = "";
                        sText = xaAttribute.Name;
                        richTextBox1.Text += "\n\t\t屬性名 sText1 = " + "\"" + sText + "\"";
                        //lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent + 2));
                        sText = xaAttribute.Value;
                        //lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent + 4));
                        richTextBox1.Text += "\t屬性值 sText2 = " + "\"" + sText + "\"";
                    }
                }
                //根元素中是否有子元素
                if (aXnNode.HasChildNodes)
                {
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                //判斷下個節點是為空
                if (aXnNode.NextSibling != null)
                {
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
            }
            else if (aXnNode is XmlText)
            {
                //顯示節點中的內容
                string sText = ((XmlText)aXnNode).Value;
                //lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\t文本 sText3 = " + "\"" + sText + "\"";
            }
            else if (aXnNode is XmlComment)
            {
                string sText = aXnNode.Value;
                //lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\n註釋 sText4 = " + "\"" + sText + "\"";
                //如果不加下邊的遍歷，資料只會得出備註中的內容，不會得出子節點內容
                if (aXnNode.HasChildNodes)
                {
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                if (aXnNode.NextSibling != null)
                {
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
            }
        }
        // 標準版XML讀取解析程式 SP

        private void button1_Click(object sender, EventArgs e)
        {
            // vcs_ReadWrite_XML1 的 標準版XML讀取解析程式

            string filename = "C:\\______test_files\\__RW\\_xml\\weather.xml";

            ParseXML(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // vcsh 的 XML讀取程式

            string filename = "C:\\______test_files\\__RW\\_xml\\weather.xml";

            ParseXML_weather(filename);
        }

        private void ParseXML_weather(string filename)
        {
            string xml = File.ReadAllText(filename, System.Text.Encoding.Default);

            //richTextBox1.Text += "data\n" + xml + "\n";

            // Load the response into an XML document.
            XmlDocument xml_doc;
            xml_doc = new XmlDocument();
            xml_doc.LoadXml(xml);

            ParseXML_weather0(xml_doc);
        }

        private void ParseXML_weather0(XmlDocument xml_doc)
        {
            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";

            XmlNode geo_node = loc_node.SelectSingleNode("location");
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n\n";

            foreach (XmlNode sun_node in xml_doc.SelectNodes("//sun"))
            {
                XmlAttribute time_attr1 = sun_node.Attributes["rise"];
                XmlAttribute time_attr2 = sun_node.Attributes["set"];
                richTextBox1.Text += "日出 : " + DateTime.Parse(time_attr1.Value).ToLocalTime() + "\n";
                richTextBox1.Text += "日落 : " + DateTime.Parse(time_attr2.Value).ToLocalTime() + "\n";
            }

            char degrees = (char)176;

            // Loop throuh the time entries.
            //string last_day = "";
            int aaa = 0;
            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the start date and time.
                XmlAttribute time_attr1 = time_node.Attributes["from"];
                XmlAttribute time_attr2 = time_node.Attributes["to"];

                aaa++;
                // 解讀xml資料 
                richTextBox1.Text += "取得第 " + aaa.ToString() + " 筆資料 : " + time_attr1.Value + "\t" + time_attr2.Value + "\n";

                richTextBox1.Text += "預測時間 : " + DateTime.Parse(time_attr1.Value).ToLocalTime() + " 到 " + DateTime.Parse(time_attr2.Value).ToLocalTime()
                    + "\t 中間 " + (DateTime.Parse(time_attr1.Value) + new TimeSpan(1, 30, 0)).ToLocalTime() + "\n";

                richTextBox1.Text += "symbol" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["number"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["name"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("symbol").Attributes["var"].Value.ToString() + "\n";

                richTextBox1.Text += "precipitation" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("precipitation").Attributes["probability"].Value.ToString() + "\n";

                richTextBox1.Text += "windDirection" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["deg"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["code"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windDirection").Attributes["name"].Value.ToString() + "\n";

                richTextBox1.Text += "windSpeed" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["mps"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("windSpeed").Attributes["name"].Value.ToString() + "\n";

                richTextBox1.Text += "temperature" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["min"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("temperature").Attributes["max"].Value.ToString() + "\n";

                richTextBox1.Text += "feels_like" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("feels_like").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("feels_like").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "pressure" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("pressure").Attributes["unit"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("pressure").Attributes["value"].Value.ToString() + "\n";

                richTextBox1.Text += "humidity" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("humidity").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("humidity").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "clouds" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["all"].Value.ToString() + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("clouds").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "visibility" + "\t";
                richTextBox1.Text += time_node.SelectSingleNode("visibility").Attributes["value"].Value.ToString() + "\n";

                DateTime start_time = DateTime.Parse(time_attr1.Value);

                // Convert from UTC to local time.
                start_time = start_time.ToLocalTime();

                // Add 90 minutes to get to the middle of the interval.
                start_time += new TimeSpan(1, 30, 0);

                // Get the temperature node.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                XmlAttribute temp_attr = temp_node.Attributes["value"];
                float temp = 0;
                if (temp_attr != null)
                {
                    temp = float.Parse(temp_attr.Value.ToString());
                }

                richTextBox1.Text += "time : \t" + start_time.ToShortTimeString() + "\t";
                richTextBox1.Text += temp.ToString("0.00") + " " + degrees + "F" + "\t";
                richTextBox1.Text += ((temp - 32) * 5 / 9).ToString("0.00") + " " + degrees + "C" + "\n";
            }
        }

        //即時天氣XML解讀 ST
        private void button3_Click(object sender, EventArgs e)
        {
            // Compose the query URL.
            string url = CurrentUrl.Replace("@LOCATION@", txtLocation.Text);
            richTextBox1.Text += "url : " + url + "\n";

            richTextBox1.Text += GetFormattedXml(url) + "\n";     //only show data

            // 解讀 fail
            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    //DisplayForecast(client.DownloadString(url));    //抓資料 並 解讀 fail
                }
                catch (WebException ex)
                {
                    DisplayError(ex);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\n" + ex.Message);
                }
            }
        }

        //天氣預測XML解讀
        private void button4_Click(object sender, EventArgs e)
        {
            // Compose the query URL.
            string url = ForecastUrl.Replace("@LOCATION@", txtLocation.Text);
            richTextBox1.Text += "url : " + url + "\n";

            //richTextBox1.Text += GetFormattedXml(url) + "\n";     //only show data

            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    DisplayForecast(client.DownloadString(url));    //抓資料 並 解讀
                }
                catch (WebException ex)
                {
                    DisplayError(ex);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\n" + ex.Message);
                }
            }


        }

        //讀取XML資料 ST
        // Return the XML result of the URL.
        private string GetFormattedXml(string url)
        {
            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                string xml = client.DownloadString(url);

                // Load the response into an XML document.
                XmlDocument xml_document = new XmlDocument();
                xml_document.LoadXml(xml);

                // Format the XML.
                using (StringWriter string_writer = new StringWriter())
                {
                    XmlTextWriter xml_text_writer = new XmlTextWriter(string_writer);
                    xml_text_writer.Formatting = Formatting.Indented;
                    xml_document.WriteTo(xml_text_writer);

                    // Return the result.
                    return string_writer.ToString();
                }
            }
        }
        //讀取XML資料 SP


        // Get a forecast.
        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "查詢型態 : " + comboBox1.Text + "\t代碼 : " + QueryCodes[comboBox1.SelectedIndex] + "\n";

            // Compose the query URL.
            string url = ForecastUrl2.Replace("@LOCATION@", txtLocation.Text);
            richTextBox1.Text += "url : " + url + "\n";
            url = url.Replace("@QUERY@", QueryCodes[comboBox1.SelectedIndex]);
            richTextBox1.Text += "url : " + url + "\n";

            richTextBox1.Text += GetFormattedXml(url) + "\n";     //only show data

            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    DisplayForecast(client.DownloadString(url));    //抓資料 並 解讀
                }
                catch (WebException ex)
                {
                    DisplayError(ex);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\n" + ex.Message);
                }
            }
        }

        // Display the forecast.
        private void DisplayForecast(string xml)
        {
            //richTextBox1.Text += xml + "\n\n";
            // Load the response into an XML document.
            XmlDocument xml_doc = new XmlDocument();
            xml_doc.LoadXml(xml);

            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            txtCity.Text = loc_node.SelectSingleNode("name").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            txtCountry.Text = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            XmlNode geo_node = loc_node.SelectSingleNode("location");
            txtLat.Text = geo_node.Attributes["latitude"].Value;
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            txtLong.Text = geo_node.Attributes["longitude"].Value;
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            txtId.Text = geo_node.Attributes["geobaseid"].Value;
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n";

            listView1.Items.Clear();
            char degrees = (char)176;

            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the time in UTC.
                DateTime time =
                    DateTime.Parse(time_node.Attributes["from"].Value,
                        null, DateTimeStyles.AssumeUniversal);

                // Get the temperature.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                string temp = temp_node.Attributes["value"].Value;

                ListViewItem item = listView1.Items.Add(time.DayOfWeek.ToString());
                item.SubItems.Add(time.ToShortTimeString());


                item.SubItems.Add(temp + " " + degrees + "F");
                richTextBox1.Text += temp + "\n";

                //item.SubItems.Add(temp.ToString("0.00"));
                item.SubItems.Add(((float.Parse(temp) - 32) * 5 / 9).ToString("0.00") + " " + degrees + "C");

            }
        }

        // Display an error message.
        private void DisplayError(WebException exception)
        {
            try
            {
                StreamReader reader = new StreamReader(exception.Response.GetResponseStream());
                XmlDocument response_doc = new XmlDocument();
                response_doc.LoadXml(reader.ReadToEnd());
                XmlNode message_node = response_doc.SelectSingleNode("//message");
                MessageBox.Show(message_node.InnerText);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Unknown error\n" + ex.Message);
            }
        }



    }
}
