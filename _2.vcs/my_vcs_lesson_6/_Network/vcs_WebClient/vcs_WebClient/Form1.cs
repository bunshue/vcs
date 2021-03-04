using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream

namespace vcs_WebClient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */

            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            using (WebClient client1 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    string data = client1.DownloadString(url_file1);          //抓網頁資料到記憶體
                    //richTextBox1.Text += data + "\n";
                    richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            using (WebClient client2 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                    client2.DownloadFile(url_file2, filename_local);          //抓網頁資料到本地檔案
                    richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
            using (WebClient client3 = new WebClient())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    // Get the response string from the URL.
                    string xml = client3.DownloadString(url_weather);        //抓資料
                    //richTextBox1.Text += "data\n" + xml + "\n";
                    richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔\tOK\n";
                Application.DoEvents();

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示\tOK\n";
                Application.DoEvents();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Download Error" + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            // Make a WebClient.
            WebClient client = new WebClient();

            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Download the file.
            client.DownloadFile(url, filename);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            try
            {
                WebClient client = new WebClient();

                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream = new MemoryStream(client.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
                return null;
            }
        }
    }
}
