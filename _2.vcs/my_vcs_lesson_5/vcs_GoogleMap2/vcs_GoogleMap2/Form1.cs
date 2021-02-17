using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Web;
using System.Net;
using Microsoft.Win32;
using System.Device.Location;

//參考/加入參考/.NET/System.Device
//參考/加入參考/.NET/System.Net
//參考/加入參考/.NET/System.Web

//專案屬性/目標FrameWork 改成 .NET Framework 4

namespace vcs_GoogleMap2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double lat = 24.8072;
            double lon = 120.9685;

            richTextBox1.Text += "指定GPS座標\n";
            richTextBox1.Text += "緯度\t" + lat.ToString() + "\n";
            richTextBox1.Text += "經度\t" + lon.ToString() + "\n";
            GeoCoordinate location = new GeoCoordinate(lat, lon);
            DisplayMap(location.Latitude, location.Longitude);
        }

        // Display a map for this location.
        private void DisplayMap(double latitude, double longitude)
        {
            // Emulate Internet Explorer 11.
            SetWebBrowserVersion(11001);

            // Get the Google maps hybrid URL with defult zoom.
            string address = "loc:" +
                latitude.ToString() + "+" +
                longitude.ToString();
            string url = GoogleMapUrl(address, "Map", 0);
            richTextBox1.Text += "URL : " + url + "\n";

            // Display the URL in the WebBrowser control.
            webBrowser1.Navigate(url);

            // Hide the label and display the map.
            //lblStatus.Hide();
            webBrowser1.Show();
        }

        // Return a Google map URL.
        // The URL format is:
        //      http://maps.google.com/maps?q=QUERY&t=TYPE&z=ZOOM
        //  Where:
        //      QUERY is the query. If it begins with "loc:" then its latitude+longitude.
        //      TYPE is map type:
        //          m = Map
        //          k = Satellite
        //          h = Hybrid
        //          p = Terrain
        //          e = Google Earth
        //      ZOOM is the zoom level, usually 1 - 20.
        private string GoogleMapUrl(string query, string map_type, int zoom)
        {
            // Start with the base map URL.
            string url = "http://maps.google.com/maps?";

            // Add the query.
            // If the query starts with "loc:", don't encode.
            if (query.StartsWith("loc:"))
                url += "q=" + query;
            else
                url += "q=" + HttpUtility.UrlEncode(query, Encoding.UTF8);

            // Add the type.
            richTextBox1.Text += "map_type = " + map_type + "\n";
            map_type = GoogleMapTypeCode(map_type);
            richTextBox1.Text += "map_type = " + map_type + "\n";
            if (map_type != null) url += "&t=" + map_type;

            // Add the zoom level.
            if (zoom > 0) url += "&z=" + zoom.ToString();

            return url;
        }

        // Return a Google map type code.
        private string GoogleMapTypeCode(string map_type)
        {
            // Insert the proper type.
            switch (map_type)
            {
                case "Map":
                    return "m";
                case "Satellite":
                    return "k";
                case "Hybrid":
                    return "h";
                case "Terrain":
                    return "p";
                case "Google Earth":
                    return "e";
                default:
                    return null;
            }
        }

        // Make the WebBrowser control emulate the indicated IE version.
        // See:
        //      https://msdn.microsoft.com/library/ee330730.aspx#browser_emulation
        private void SetWebBrowserVersion(int ie_version)
        {
            // For testing:
            //DeleteRegistryValue(key64bit, app_name);
            //DeleteRegistryValue(key32bit, app_name);

            const string key64bit =
                @"SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION";
            const string key32bit =
                @"SOFTWARE\Microsoft\Internet Explorer\MAIN\FeatureControl\FEATURE_BROWSER_EMULATION";
            string app_name = System.AppDomain.CurrentDomain.FriendlyName;

            // You can do both if you like.
            //SetRegistryDword(key64bit, app_name, ie_version);
            SetRegistryDword(key32bit, app_name, ie_version);
        }

        // Set a registry DWORD value.
        private void SetRegistryDword(string key_name, string value_name, int value)
        {
            // Open the key.
            RegistryKey key =
                Registry.CurrentUser.OpenSubKey(key_name, true);
            if (key == null)
                key = Registry.CurrentUser.CreateSubKey(key_name,
                    RegistryKeyPermissionCheck.ReadWriteSubTree);

            // Set the desired value.
            key.SetValue(value_name, value, RegistryValueKind.DWord);

            key.Close();
        }

        // Delete a registry value.
        private void DeleteRegistryValue(string key_name, string value_name)
        {
            // Open the key.
            RegistryKey key =
                Registry.CurrentUser.OpenSubKey(key_name, true);
            if (key == null) return;

            // Delete the desired value.
            key.DeleteValue(value_name, false);

            key.Close();
        }


    }
}
