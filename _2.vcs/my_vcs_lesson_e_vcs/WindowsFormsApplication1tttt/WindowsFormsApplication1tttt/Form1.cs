using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
//using System.Runtime.InteropServices;

//using Microsoft.Win32;

using System.IO;
using System.Net;
using Newtonsoft.Json;

using System.Xml;

namespace WindowsFormsApplication1tttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        public class BaiDuGeoCoding
        {
            public int Status { get; set; }
            public Result Result { get; set; }
        }

        public class Result
        {
            public Location Location { get; set; }

            public string Formatted_Address { get; set; }

            public string Business { get; set; }

            public AddressComponent AddressComponent { get; set; }

            public string CityCode { get; set; }
        }

        public class AddressComponent
        {
            /// <summary>
            /// 省份
            /// </summary>
            public string Province { get; set; }
            /// <summary>
            /// 城市名
            /// </summary>
            public string City { get; set; }

            /// <summary>
            /// 区县名
            /// </summary>
            public string District { get; set; }

            /// <summary>
            /// 街道名
            /// </summary>
            public string Street { get; set; }

            public string Street_number { get; set; }

        }

        public class Location
        {
            public string Lng { get; set; }
            public string Lat { get; set; }
        }

        //2.新建一个帮助类根据URL获取页面内容:

        public class HttpClientHelper
        {
            /// <summary>
            /// GET请求
            /// </summary>
            /// <typeparam name="T"></typeparam>
            /// <param name="url"></param>
            /// <returns></returns>
            public static T GetResponse<T>(string url) where T : class,new()
            {
                string returnValue = string.Empty;
                Console.WriteLine("url = " + url);
                HttpWebRequest webReq = (HttpWebRequest)WebRequest.Create(new Uri(url));
                webReq.Method = "GET";
                webReq.ContentType = "application/json";
                using (HttpWebResponse response = (HttpWebResponse)webReq.GetResponse())
                {
                    using (StreamReader streamReader = new StreamReader(response.GetResponseStream(), Encoding.UTF8))
                    {
                        returnValue = streamReader.ReadToEnd();
                        T result = default(T);
                        result = JsonConvert.DeserializeObject<T>(returnValue);
                        return result;
                    }
                }
            }
        }

        //3.定义字段和方法获取:

        //百度地图Api  Ak
        public const string BaiduAk = "84ZCmEMi3GmDX8LboHSfpoCOP2LAxh9c";

        /// <summary>
        /// 经纬度  逆地理编码 Url  需要Format 0.ak  1.经度  2.纬度
        /// </summary>
        private const string BaiduGeoCoding_ApiUrl = "http://api.map.baidu.com/geocoder/v2/?ak={0}&location={1},{2}&output=json&pois=0";

        /// <summary>
        /// /// <summary>
        /// 经纬度  逆地理编码 Url  需要Format 0.经度  1.纬度 
        /// </summary>
        /// </summary>
        public static string Baidu_GeoCoding_ApiUrl
        {
            get
            {
                return string.Format(BaiduGeoCoding_ApiUrl, BaiduAk, "{0}", "{1}");
            }
        }

        /// <summary>
        /// 根据经纬度  获取 地址信息
        /// </summary>
        /// <param name="lat">经度</param>
        /// <param name="lng">纬度</param>
        /// <returns></returns>
        public static BaiDuGeoCoding GeoCoder(string lat, string lng)
        {
            string url = string.Format(Baidu_GeoCoding_ApiUrl, lat, lng);
            var model = HttpClientHelper.GetResponse<BaiDuGeoCoding>(url);
            return model;
        }



        private void button3_Click(object sender, EventArgs e)
        {
            string lat = "22.228962";
            string lng = "113.308784";
            var model = GeoCoder(lat, lng); //model拿到的就是详细物理地址
            richTextBox1.Text += "get : " + model.Result + "\n";
            richTextBox1.Text += "get : " + model.Status + "\n";
            richTextBox1.Text += "get : " + model.ToString() + "\n";
        }


        //C#百度api 根据经纬度获取地址

        public string GetAddress(string lat, string lng)
        {
            try
            {
                string res = "";
                string url = @"http://api.map.baidu.com/geocoder/v2/?ak=r5QMq6ntQE7hdQUMNIsDrwapO1li0frR&location=" + lat + "," + lng + "&output=xml";
                WebRequest request = WebRequest.Create(url);
                request.Method = "POST";
                XmlDocument xmlDoc = new XmlDocument();
                string sendData = xmlDoc.InnerXml;
                byte[] byteArray = Encoding.Default.GetBytes(sendData);

                Stream dataStream = request.GetRequestStream();
                dataStream.Write(byteArray, 0, byteArray.Length);
                dataStream.Close();

                WebResponse response = request.GetResponse();
                dataStream = response.GetResponseStream();
                StreamReader reader = new StreamReader(dataStream, System.Text.Encoding.GetEncoding("utf-8"));
                string responseXml = reader.ReadToEnd();

                XmlDocument xml = new XmlDocument();
                xml.LoadXml(responseXml);
                string status = xml.DocumentElement.SelectSingleNode("status").InnerText;
                if (status == "0")
                {

                    XmlNodeList nodes = xml.DocumentElement.GetElementsByTagName("formatted_address");
                    XmlNodeList nodes1 = xml.DocumentElement.GetElementsByTagName("sematic_description");
                    if (nodes.Count > 0 && !string.IsNullOrEmpty(nodes[0].InnerText))
                    {
                        res += "地址信息: " + nodes[0].InnerText;
                    }
                    if (nodes1.Count > 0 && !string.IsNullOrEmpty(nodes1[0].InnerText))
                    {
                        res += "  结果描述: " + nodes1[0].InnerText;
                    }
                    if (nodes.Count <= 0 && nodes1.Count <= 0)
                        res = "未获取到位置信息,错误码3";
                }
                else
                {
                    res = "未获取到位置信息,错误码1";
                }
                return res;
            }
            catch (System.Exception ex)
            {
                return "未获取到位置信息,错误码2";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //http://api.map.baidu.com/geocoder/v2/ak=ZndyfXErtTiZQwfgNgQ7yqb7ALKdk4DA&location=39.963175,116.400244&output=json
            /*
            string lat = "22.228962";
            string lng = "113.308784";
            var model = GeoCoder(lat, lng); //model拿到的就是详细物理地址
            richTextBox1.Text += "get : " + model.Result + "\n";
            richTextBox1.Text += "get : " + model.Status + "\n";
            richTextBox1.Text += "get : " + model.ToString() + "\n";
            */
            //public string GetAddress(string lat, string lng)
            string lat = "22.228962";
            string lng = "113.308784";
            string result = GetAddress(lat, lng);
            richTextBox1.Text += result + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }
    }
}





