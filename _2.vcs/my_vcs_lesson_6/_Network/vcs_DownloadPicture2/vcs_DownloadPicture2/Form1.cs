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
namespace vcs_DownloadPicture2
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

        private void button1_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            get_nasa_picture();
            Cursor = Cursors.Default;
        }

        void get_nasa_picture()
        {
            string url = "http://antwrp.gsfc.nasa.gov/apod/";
            try
            {
                richTextBox1.Text += "開啟 NASA 圖片網址 : " + url + "\n";
                webBrowser1.Navigate(url);  // Load the web page.
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Error navigating to " + url + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
        }

        // The web page has loaded. Get the APOTD image.
        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            richTextBox1.Text += "NASA 圖片網站主頁下載完畢, 從網頁資料擷取圖片所在網址\n";
            // Get the image's URL.
            HtmlDocument doc = webBrowser1.Document;
            string img_src_url = doc.Images[0].GetAttribute("src");

            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";

            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔完成\n";

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示完成\n";
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
