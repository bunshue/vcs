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

namespace howto_list_temperatures
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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
            Cursor = Cursors.WaitCursor;

            // Compose the query URL.
            string url = ForecastUrl.Replace("@LOC@", txtLocation.Text);

            // Create a web client.
            XmlDocument xml_doc;
            using (WebClient client = new WebClient())
            {
                // Get the response string from the URL.
                string xml = client.DownloadString(url);

                // Load the response into an XML document.
                xml_doc = new XmlDocument();
                xml_doc.LoadXml(xml);
            }

            // List the temperatures.
            ListTemperatures(xml_doc);

            Cursor = Cursors.Default;
        }

        // List the temperatures.
        private void ListTemperatures(XmlDocument xml_doc)
        {
            lvwTemps.Items.Clear();

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
                    item = lvwTemps.Items.Add("");
                else
                {
                    last_day = start_time.DayOfWeek.ToString();
                    item = lvwTemps.Items.Add(last_day);
                }
                item.SubItems.Add(start_time.ToShortTimeString());
                item.SubItems.Add(temp.ToString("0.00"));
            }
        }
    }
}
