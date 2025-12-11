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

        private const int MODE_FORECAST = 0x00;     //天氣預測
        private const int MODE_CURRENT = 0x01;      //即時天氣
        private const int MODE_VERBOSE0 = 0x00;     //簡版
        private const int MODE_VERBOSE1 = 0x01;     //詳版1
        private const int MODE_VERBOSE2 = 0x02;     //詳版2

        // Enter your API key here.
        // Get an API key by making a free account at:
        //      http://home.openweathermap.org/users/sign_in
        string API_KEY;
        private char degrees = (char)176;

        // Query codes.
        private string Query = "";
        private string[] QueryCodes = { "q", "zip", "id", };

        string ForecastUrl;     //天氣預測 查詢網址
        string CurrentUrl;      //即時天氣 查詢網址
        string data_country = "";
        string data_city = "";
        string data_id = "";
        string data_lat = "";
        string data_lon = "";

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


            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\api_key.txt";


            if (File.Exists(filename) == false)
            {
                MessageBox.Show("API_KEY 檔案不存在, 離開", "vcs_weather", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            //讀取檔案
            string kk = File.ReadAllText(filename, System.Text.Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + kk + "\n";
            richTextBox1.Text += "長度：" + kk.Length.ToString() + "\n";

            if (kk.Length == 32)
            {
                API_KEY = kk;
            }
            else
            {
                API_KEY = "xxxx";
            }

            // Query URLs. Replace @LOCATION@ with the location.
            //天氣預測
            ForecastUrl = "http://api.openweathermap.org/data/2.5/forecast?" + "@QUERY@=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
            //即時天氣
            CurrentUrl = "http://api.openweathermap.org/data/2.5/weather?" + "@QUERY@=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;

            //若是只查詢代碼為City(q)之條件, 用 q 取代 @QUERY@
            // Query URLs. Replace @LOCATION@ with the location.
            //天氣預測
            //private const string ForecastUrl3 = "http://api.openweathermap.org/data/2.5/forecast?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;
            //即時天氣
            //private const string CurrentUrl3 = "http://api.openweathermap.org/data/2.5/weather?" + "q=@LOCATION@&mode=xml&units=imperial&APPID=" + API_KEY;

            if (API_KEY.Length != 32)
            {
                MessageBox.Show("API_KEY 錯誤, 離開", "vcs_weather", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }
        }

        void clear_data()
        {
            data_country = "";
            data_city = "";
            data_id = "";
            data_lat = "";
            data_lon = "";

            tb_country.Text = data_country;
            tb_city.Text = data_city;
            tb_id.Text = data_id;
            tb_lat.Text = data_lat;
            tb_lon.Text = data_lon;

            temperature.Clear();
            date.Clear();
            richTextBox1.Clear();
            listView1.Items.Clear();
            pictureBox1.Image = null;
        }

        void show_data()
        {
            tb_country.Text = data_country;
            tb_city.Text = data_city;
            tb_id.Text = data_id;
            tb_lat.Text = data_lat;
            tb_lon.Text = data_lon;

            if (tb_city.Text == "")
            {
                tb_country.Text = "-----";
                tb_city.Text = "-----";
                tb_id.Text = "-----";
                tb_lat.Text = "-----";
                tb_lon.Text = "-----";
            }
        }

        // List the temperatures.
        private void ListTemperatures(XmlDocument xml_doc)
        {
            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            data_city = loc_node.SelectSingleNode("name").InnerText;
            data_country = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";
            XmlNode geo_node = loc_node.SelectSingleNode("location");
            data_lat = geo_node.Attributes["latitude"].Value;
            data_lon = geo_node.Attributes["longitude"].Value;
            data_id = geo_node.Attributes["geobaseid"].Value;
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n";

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
            clear_data();
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
            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案 " + filename + " 不存在，離開。\n";
                return;
            }

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

        private void button1_Click(object sender, EventArgs e)
        {
            //解讀XML1 OK 標準版XML
            clear_data();
            richTextBox1.Text += "解讀XML檔案\tvcs_ReadWrite_XML1 的 標準版XML讀取解析程式, 讀取天氣預測XML檔案\n";

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\weather_forecast.xml";
            ParseXML(filename);
            show_data();
        }
        // 標準版XML讀取解析程式 SP

        private void button2_Click(object sender, EventArgs e)
        {
            //解讀XML2 OK VCSH天氣預測
            clear_data();
            richTextBox1.Text += "解讀XML檔案\tvcsh 的 XML讀取程式, 讀取天氣預測XML檔案\n";

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\weather_forecast.xml";
            ParseXML_weather_forecast(filename);
            show_data();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //解讀XML3 OK VCSH即時天氣
            clear_data();
            richTextBox1.Text += "解讀XML檔案\tvcsh 的 XML讀取程式, 讀取即時天氣XML檔案\n";

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\weather_current.xml";
            ParseXML_weather_current(filename);
            show_data();
        }

        //vcsh 的 XML讀取程式, 讀取天氣預測XML檔案 ST
        private void ParseXML_weather_forecast(string filename)
        {
            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案 " + filename + " 不存在，離開。\n";
                return;
            }

            string xml = File.ReadAllText(filename, System.Text.Encoding.Default);

            //richTextBox1.Text += "data\n" + xml + "\n";

            // Load the response into an XML document.
            XmlDocument xml_doc;
            xml_doc = new XmlDocument();
            xml_doc.LoadXml(xml);

            ParseXML_weather_forecast0(xml_doc);
        }

        private void ParseXML_weather_forecast0(XmlDocument xml_doc)
        {
            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            data_city = loc_node.SelectSingleNode("name").InnerText;
            data_country = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";

            XmlNode geo_node = loc_node.SelectSingleNode("location");
            data_lat = geo_node.Attributes["latitude"].Value;
            data_lon = geo_node.Attributes["longitude"].Value;
            data_id = geo_node.Attributes["geobaseid"].Value;

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
        //vcsh 的 XML讀取程式, 讀取天氣預測XML檔案 SP

        //vcsh 的 XML讀取程式, 讀取即時天氣XML檔案 ST
        private void ParseXML_weather_current(string filename)
        {
            if (File.Exists(filename) == false)
            {
                richTextBox1.Text += "檔案 " + filename + " 不存在，離開。\n";
                return;
            }

            string xml = File.ReadAllText(filename, System.Text.Encoding.Default);

            //richTextBox1.Text += "data\n" + xml + "\n";

            // Load the response into an XML document.
            XmlDocument xml_doc;
            xml_doc = new XmlDocument();
            xml_doc.LoadXml(xml);

            ParseXML_weather_current0(xml_doc);
        }

        private void ParseXML_weather_current0(XmlDocument xml_doc)
        {
            foreach (XmlNode current_node in xml_doc.SelectNodes("//current"))
            {
                foreach (XmlNode city_node in xml_doc.SelectNodes("//city"))
                {
                    XmlAttribute city_attr1 = city_node.Attributes["id"];
                    XmlAttribute city_attr2 = city_node.Attributes["name"];
                    data_id = city_attr1.Value;
                    data_city = city_attr2.Value;
                    richTextBox1.Text += "city id : " + city_attr1.Value + "\n";
                    richTextBox1.Text += "city name : " + city_attr2.Value + "\n";

                    foreach (XmlNode coord_node in xml_doc.SelectNodes("//coord"))
                    {
                        XmlAttribute coord_attr1 = coord_node.Attributes["lon"];
                        XmlAttribute coord_attr2 = coord_node.Attributes["lat"];
                        data_lon = coord_attr1.Value;
                        data_lat = coord_attr2.Value;
                        richTextBox1.Text += "東經 : " + coord_attr1.Value + "\n";
                        richTextBox1.Text += "北緯 : " + coord_attr2.Value + "\n";
                    }
                    data_country = city_node.SelectSingleNode("country").InnerText;
                    richTextBox1.Text += "國家\t" + city_node.SelectSingleNode("country").InnerText + "\n";
                    richTextBox1.Text += "時區\t" + city_node.SelectSingleNode("timezone").InnerText + "\n";

                    foreach (XmlNode sun_node in xml_doc.SelectNodes("//sun"))
                    {
                        XmlAttribute time_attr1 = sun_node.Attributes["rise"];
                        XmlAttribute time_attr2 = sun_node.Attributes["set"];
                        richTextBox1.Text += "日出 : " + DateTime.Parse(time_attr1.Value).ToLocalTime() + "\n";
                        richTextBox1.Text += "日落 : " + DateTime.Parse(time_attr2.Value).ToLocalTime() + "\n";
                    }
                }

                richTextBox1.Text += "temperature" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("temperature").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("temperature").Attributes["min"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("temperature").Attributes["max"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("temperature").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "feels_like" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("feels_like").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("feels_like").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "humidity" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("humidity").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("humidity").Attributes["unit"].Value.ToString() + "\n";

                richTextBox1.Text += "pressure" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("pressure").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("pressure").Attributes["unit"].Value.ToString() + "\n";

                foreach (XmlNode wind_node in xml_doc.SelectNodes("//wind"))
                {
                    richTextBox1.Text += "wind" + "\n";
                    richTextBox1.Text += wind_node.SelectSingleNode("speed").Attributes["value"].Value.ToString() + "\t";
                    richTextBox1.Text += wind_node.SelectSingleNode("speed").Attributes["unit"].Value.ToString() + "\t";
                    richTextBox1.Text += wind_node.SelectSingleNode("speed").Attributes["name"].Value.ToString() + "\n";
                    richTextBox1.Text += wind_node.SelectSingleNode("direction").Attributes["value"].Value.ToString() + "\t";
                    richTextBox1.Text += wind_node.SelectSingleNode("direction").Attributes["code"].Value.ToString() + "\t";
                    richTextBox1.Text += wind_node.SelectSingleNode("direction").Attributes["name"].Value.ToString() + "\n";
                }

                richTextBox1.Text += "clouds" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("clouds").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("clouds").Attributes["name"].Value.ToString() + "\n";

                richTextBox1.Text += "visibility" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("visibility").Attributes["value"].Value.ToString() + "\n";

                richTextBox1.Text += "precipitation" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("precipitation").Attributes["mode"].Value.ToString() + "\n";

                richTextBox1.Text += "weather" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("weather").Attributes["number"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("weather").Attributes["value"].Value.ToString() + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("weather").Attributes["icon"].Value.ToString() + "\n";

                richTextBox1.Text += "lastupdate" + "\t";
                richTextBox1.Text += current_node.SelectSingleNode("lastupdate").Attributes["value"].Value.ToString() + "\n";
            }
        }
        //vcsh 的 XML讀取程式, 讀取即時天氣XML檔案 SP

        //讀取XML資料 ST
        // Return the XML result of the URL.
        private string GetFormattedXml(string url)
        {
            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                string xml = client.DownloadString(url);        //抓資料

                //richTextBox1.Text += "data\n" + xml + "\n";

                //prepare
                //ParseXML_Forecast(xml);    //解讀

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

        // Display the forecast.
        private void ParseXML_Forecast_old(string xml)      //舊的解讀資料
        {
            //richTextBox1.Text += xml + "\n\n";
            // Load the response into an XML document.
            XmlDocument xml_doc = new XmlDocument();
            xml_doc.LoadXml(xml);

            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            data_city = loc_node.SelectSingleNode("name").InnerText;
            data_country = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";
            XmlNode geo_node = loc_node.SelectSingleNode("location");
            data_lat = geo_node.Attributes["latitude"].Value;
            data_lon = geo_node.Attributes["longitude"].Value;
            data_id = geo_node.Attributes["geobaseid"].Value;
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n";

            // Loop throuh the time entries.
            string last_day = "";
            int aaa = 0;
            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                /*
                // Get the time in UTC.
                DateTime time = DateTime.Parse(time_node.Attributes["from"].Value, null, DateTimeStyles.AssumeUniversal);

                // Get the temperature.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                string temp = temp_node.Attributes["value"].Value;

                ListViewItem item = listView1.Items.Add(time.DayOfWeek.ToString());
                item.SubItems.Add(time.ToShortTimeString());

                item.SubItems.Add(temp + " " + degrees + "F");
                richTextBox1.Text += temp + "\n";

                item.SubItems.Add(((float.Parse(temp) - 32) * 5 / 9).ToString("0.00") + " " + degrees + "C");
                */

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

        private void ParseXML_Forecast0(XmlDocument xml_doc)
        {
            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            data_city = loc_node.SelectSingleNode("name").InnerText;
            data_country = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";
            XmlNode geo_node = loc_node.SelectSingleNode("location");
            data_lat = geo_node.Attributes["latitude"].Value;
            data_lon = geo_node.Attributes["longitude"].Value;
            data_id = geo_node.Attributes["geobaseid"].Value;
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n";

            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the time in UTC.
                DateTime time = DateTime.Parse(time_node.Attributes["from"].Value, null, DateTimeStyles.AssumeUniversal);

                // Get the temperature.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                string temp = temp_node.Attributes["value"].Value;

                ListViewItem item = listView1.Items.Add(time.DayOfWeek.ToString());
                item.SubItems.Add(time.ToShortTimeString());

                item.SubItems.Add(temp + " " + degrees + "F");
                richTextBox1.Text += temp + "\n";

                item.SubItems.Add(((float.Parse(temp) - 32) * 5 / 9).ToString("0.00") + " " + degrees + "C");
            }
        }

        //ParseXML_weather_forecast0
        //private void ParseXML_weather_forecast0(XmlDocument xml_doc)
        private void ParseXML_Current0(XmlDocument xml_doc)
        {
            // TBD
            return;


            // 解讀xml資料
            // Get the city, country, latitude, and longitude.
            XmlNode loc_node = xml_doc.SelectSingleNode("weatherdata/location");
            data_city = loc_node.SelectSingleNode("name").InnerText;
            data_country = loc_node.SelectSingleNode("country").InnerText;
            richTextBox1.Text += "城市\t" + loc_node.SelectSingleNode("name").InnerText + "\n";
            richTextBox1.Text += "國家\t" + loc_node.SelectSingleNode("country").InnerText + "\n";
            richTextBox1.Text += "時區\t" + loc_node.SelectSingleNode("timezone").InnerText + "\n";
            XmlNode geo_node = loc_node.SelectSingleNode("location");
            data_lat = geo_node.Attributes["latitude"].Value;
            data_lon = geo_node.Attributes["longitude"].Value;
            data_id = geo_node.Attributes["geobaseid"].Value;
            richTextBox1.Text += "高度\t" + geo_node.Attributes["altitude"].Value + "\n";
            richTextBox1.Text += "緯度\t" + geo_node.Attributes["latitude"].Value + "\n";
            richTextBox1.Text += "經度\t" + geo_node.Attributes["longitude"].Value + "\n";
            richTextBox1.Text += "geobase\t" + geo_node.Attributes["geobase"].Value + "\n";
            richTextBox1.Text += "ID\t" + geo_node.Attributes["geobaseid"].Value + "\n";

            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the time in UTC.
                DateTime time = DateTime.Parse(time_node.Attributes["from"].Value, null, DateTimeStyles.AssumeUniversal);

                // Get the temperature.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                string temp = temp_node.Attributes["value"].Value;

                ListViewItem item = listView1.Items.Add(time.DayOfWeek.ToString());
                item.SubItems.Add(time.ToShortTimeString());

                item.SubItems.Add(temp + " " + degrees + "F");
                richTextBox1.Text += temp + "\n";

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
                MessageBox.Show("Unknown error\t" + ex.Message);
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            clear_data();
        }

        //天氣預測XML解讀_簡版
        private void button4_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            clear_data();
            get_weather_data(MODE_FORECAST, MODE_VERBOSE0);
            show_data();
            Cursor = Cursors.Default;
        }

        //天氣預測XML解讀_詳版 1
        private void button10_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            clear_data();
            get_weather_data(MODE_FORECAST, MODE_VERBOSE1);
            show_data();
            Cursor = Cursors.Default;
        }

        //天氣預測XML解讀_詳版 2
        private void button7_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            clear_data();
            get_weather_data(MODE_FORECAST, MODE_VERBOSE2);
            show_data();
            Cursor = Cursors.Default;
        }

        //即時天氣XML解讀_簡版
        private void button3_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            clear_data();
            get_weather_data(MODE_CURRENT, MODE_VERBOSE0);
            show_data();
            Cursor = Cursors.Default;
            richTextBox1.Text += "未完成\n";
        }

        //即時天氣XML解讀_詳版
        private void button11_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            clear_data();
            get_weather_data(MODE_CURRENT, MODE_VERBOSE1);
            show_data();
            Cursor = Cursors.Default;
        }

        void get_weather_data(int mode, int verbose)    //mode 0: 天氣預測    1: 即時天氣     verbose 0: 簡版    1: 詳版1     2: 詳版2
        {
            // Compose the query URL.
            Query = QueryCodes[comboBox1.SelectedIndex];
            string url = "";

            if (mode == MODE_FORECAST)
                url = ForecastUrl.Replace("@LOCATION@", tb_location.Text);
            else
                url = CurrentUrl.Replace("@LOCATION@", tb_location.Text);

            richTextBox1.Text += "url : " + url + "\n";
            url = url.Replace("@QUERY@", Query);
            richTextBox1.Text += "url : " + url + "\n";

            Application.DoEvents(); //把以上資訊顯示出來

            //richTextBox1.Text += GetFormattedXml(url) + "\n";     //only show data

            // Create a web client.
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                try
                {
                    // Get the response string from the URL.
                    string xml = client.DownloadString(url);        //抓資料

                    //richTextBox1.Text += "data\n" + xml + "\n";

                    // Load the response into an XML document.
                    XmlDocument xml_doc = new XmlDocument();
                    xml_doc.LoadXml(xml);

                    if (mode == MODE_FORECAST)
                    {
                        //ParseXML_Forecast(xml, verbose);    //解讀
                        if (verbose == 0)
                        {
                            ParseXML_Forecast0(xml_doc);            //簡版
                        }
                        else if (verbose == 1)
                        {
                            ParseXML_weather_forecast0(xml_doc);    //詳版 1
                        }
                        else if (verbose == 2)
                        {
                            ListTemperatures(xml_doc);              //詳版 2
                        }
                    }
                    else
                    {
                        //ParseXML_Current(xml, verbose);    //解讀
                        if (verbose == 0)
                        {
                            ParseXML_Current0(xml_doc);            //簡版  TBD
                        }
                        else if (verbose == 1)
                        {
                            ParseXML_weather_current0(xml_doc);    //詳版
                        }
                    }
                }
                catch (WebException ex)
                {
                    DisplayError(ex);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
        }
    }
}

