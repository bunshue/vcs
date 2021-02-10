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
using System.IO;


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

namespace howto_list_temperatures
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        // Enter your API key here.
        // Get an API key by making a free account at:
        //      http://home.openweathermap.org/users/sign_in
        private const string API_KEY = "lion-mouse";

        // Query URLs. Replace @LOC@ with the location.
        private const string CurrentUrl =
            "http://api.openweathermap.org/data/2.5/weather?" +
            "q=@LOC@&mode=xml&units=imperial&APPID=" + API_KEY;
        private const string ForecastUrl =
            "http://api.openweathermap.org/data/2.5/forecast?" +
            "q=@LOC@&mode=xml&units=imperial&APPID=" + API_KEY;

        // List the temperature forecast.
        private void btnForecast_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "搜尋城市：" + txtLocation.Text + "\n";
            Cursor = Cursors.WaitCursor;

            // Compose the query URL.
            string url = ForecastUrl.Replace("@LOC@", txtLocation.Text);

            richTextBox1.Text += "url : \n" + url + "\n";

            // Create a web client.
            XmlDocument xml_doc;
            using (WebClient client = new WebClient())
            {
                try
                {
                    // Get the response string from the URL.
                    string xml = client.DownloadString(url);

                    richTextBox1.Text += "data\n" + xml + "\n";

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

            // Loop throuh the time entries.
            string last_day = "";
            foreach (XmlNode time_node in xml_doc.SelectNodes("//time"))
            {
                // Get the start date and time.
                XmlAttribute time_attr = time_node.Attributes["from"];
                DateTime start_time = DateTime.Parse(time_attr.Value);

                // Convert from UTC to local time.
                start_time = start_time.ToLocalTime();

                // Add 90 minutes to get to the middle of the interval.
                start_time += new TimeSpan(1, 30, 0);

                // Get the temperature node.
                XmlNode temp_node = time_node.SelectSingleNode("temperature");
                XmlAttribute temp_attr = temp_node.Attributes["value"];
                float temp = 0;
                if (temp_attr != null)
                    temp = float.Parse(temp_attr.Value.ToString());

                ListViewItem item;
                if (start_time.DayOfWeek.ToString() == last_day)
                    item = listView1.Items.Add("");
                else
                {
                    last_day = start_time.DayOfWeek.ToString();
                    item = listView1.Items.Add(last_day);
                }
                item.SubItems.Add(start_time.ToShortTimeString());
                item.SubItems.Add(temp.ToString("0.00"));
                item.SubItems.Add(((temp - 32) * 5 / 9).ToString("0.00"));
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}

