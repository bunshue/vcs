using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

using System.Threading;

namespace vcs_GetCookie
{
    public partial class Form1 : Form
    {
        //[DllImport("wininet.dll", CharSet = CharSet.Auto, SetLastError = true, CallingConvention = CallingConvention.Cdecl)]
        //static extern bool InternetGetCookieEx(string pchURL, string pchCookieName, StringBuilder pchCookieData, ref int pcchCookieData, int dwFlags, IntPtr lpReserved);
        //取出Cookie，当登录后才能取

        [DllImport("wininet.dll", CharSet = CharSet.Auto, SetLastError = true)]
        static extern bool InternetGetCookieEx(string pchURL, string pchCookieName, StringBuilder pchCookieData, ref System.UInt32 pcchCookieData, int dwFlags, IntPtr lpReserved);

        public static string GetCookieString(string url)
        {
            // Determine the size of the cookie      
            uint datasize = 256;
            StringBuilder cookieData = new StringBuilder((int)datasize);
            if (!InternetGetCookieEx(url, null, cookieData, ref datasize, 0x00002000, IntPtr.Zero))
            {
                if (datasize < 0)
                    return null;
                // Allocate stringbuilder large enough to hold the cookie    
                cookieData = new StringBuilder((int)datasize);
                if (!InternetGetCookieEx(url, null, cookieData, ref datasize, 0x00002000, IntPtr.Zero))
                    return null;
            }
            return cookieData.ToString();
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string url = @"https://www.google.com.tw/";
            string cookie = GetCookieString(url);
            richTextBox1.Text += "get cookie : " + cookie + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string url = @"https://www.google.com.tw/";
            string cookie = BrowserHelper.GetCookie(url);
            richTextBox1.Text += "get cookie : " + cookie + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string url = @"https://www.google.com.tw/";
            string cookie = BrowserHelper.GetCookie(url);
            richTextBox1.Text += "get cookie : " + cookie + "\n";


            string imgURL = @"https://www.google.com.tw/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes("aaaaaaa.jpg", ms.ToArray());


            /*
            string imgURL = domain + imgBaseURL + fileName[0] + "?.&uf=ssr&zoom=2";
            MemoryStream ms = GetResponse(imgURL, cookie);
            File.WriteAllBytes(string.Format(@"Download\{0}.jpg", fileName[1]), ms.ToArray());
            */


        }

        private MemoryStream GetResponse(string url, string cookie)
        {
            while (true)
            {
                try
                {
                    HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
                    request.Headers.Add("Cookie", cookie);
                    request.Method = "GET";
                    request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                    HttpWebResponse response = request.GetResponse() as HttpWebResponse;

                    MemoryStream ms = new MemoryStream();
                    response.GetResponseStream().CopyTo(ms);

                    if (response.ContentType.Contains("text/html") == true)
                    {
                        ms.Seek(0, SeekOrigin.Begin);
                        string html = new StreamReader(ms).ReadToEnd();

                        if (html.Contains("/processVerifyPng.ac") == true)
                        {
                            string domainName = Regex.Match(url, "^http://.*?(?=/)").Value;
                            string codeImageURL = domainName + "/n/n/processVerifyPng.ac";
                            request = WebRequest.Create(codeImageURL) as HttpWebRequest;
                            request.Headers.Add("Cookie", cookie);
                            request.Method = "GET";
                            request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                            response = request.GetResponse() as HttpWebResponse;

                            ms = new MemoryStream();
                            response.GetResponseStream().CopyTo(ms);

                            //waitEvent.Reset();
                            //this.Dispatcher.BeginInvoke(new Action<Stream>(EnableUI), ms);
                            //waitEvent.WaitOne();

                            string commitCodeString = domainName + "/n/processVerify.ac?ucode=";    // +code;
                            request = WebRequest.Create(commitCodeString) as HttpWebRequest;
                            request.Headers.Add("Cookie", cookie);
                            request.Method = "GET";
                            request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                            response = request.GetResponse() as HttpWebResponse;
                            response.Close();

                            continue;
                        }
                    }

                    ms.Seek(0, SeekOrigin.Begin);
                    return ms;
                }
                catch (Exception ex)
                {
                    WebException wex = ex as WebException;
                    wex = null;
                    if (wex != null && (wex.Response as HttpWebResponse).StatusCode == HttpStatusCode.Forbidden)
                    {
                        //this.Dispatcher.BeginInvoke(new Action<string>(ShowError), url);
                        Thread.CurrentThread.Abort();
                    }
                }
            }
        }
    }

    public class BrowserHelper
    {
        private const int INTERNET_COOKIE_HTTPONLY = 0x00002000;

        [DllImport("wininet.dll", SetLastError = true)]
        private static extern bool InternetGetCookieEx(
            string url,
            string cookieName,
            StringBuilder cookieData,
            ref int size,
            int flags,
            IntPtr pReserved);

        public static string GetCookie(string url)
        {
            int size = 512;
            StringBuilder sb = new StringBuilder(size);
            if (!InternetGetCookieEx(url, null, sb, ref size, INTERNET_COOKIE_HTTPONLY, IntPtr.Zero))
            {
                if (size < 0)
                {
                    return null;
                }
                sb = new StringBuilder(size);
                if (!InternetGetCookieEx(url, null, sb, ref size, INTERNET_COOKIE_HTTPONLY, IntPtr.Zero))
                {
                    return null;
                }
            }
            return sb.ToString();
        }
    }

}
