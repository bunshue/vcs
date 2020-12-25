using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;

namespace vcs_PictureDownload
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Download the Astronomy Picture of the Day.
        private void Form1_Load(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            wbrApotd.Visible = false;

            const string url = "http://antwrp.gsfc.nasa.gov/apod/";
            try
            {
                // Load the web page.
                wbrApotd.Navigate(url);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message,
                    "Error navigating to " + url);
            }
        }

        // The web page has loaded. Get the APOTD image.
        private void wbrApotd_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            HtmlDocument doc = wbrApotd.Document;
            string src = doc.Images[0].GetAttribute("src");
            Image img = GetPicture(src);
            picApotd.Image = img;

            Cursor = Cursors.Default;
            Console.WriteLine(src);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            try
            {
                WebClient web_client = new WebClient();

                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream =
                    new MemoryStream(web_client.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error downloading picture " +
                    url + '\n' + ex.Message);
                return null;
            }
        }
    }
}
