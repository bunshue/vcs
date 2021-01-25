#define TEST    // Resets so we load a new image immediately.

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Runtime.InteropServices;
using System.IO;
using System.Drawing.Imaging;

namespace howto_apotd_desktop
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool SystemParametersInfo(uint uiAction, uint uiParam, String pvParam, uint fWinIni);

        private const uint SPI_SETDESKWALLPAPER = 0x14;
        private const uint SPIF_UPDATEINIFILE = 0x1;
        private const uint SPIF_SENDWININICHANGE = 0x2;

        public Form1()
        {
            InitializeComponent();
        }

        // Display the last load time and URL.
        private void Form1_Load(object sender, EventArgs e)
        {
#if TEST
            Properties.Settings.Default.LastLoadTime = DateTime.Now.AddDays(-1);
            Properties.Settings.Default.LastUrl = "";
            Properties.Settings.Default.Save();
#endif

            tmrDownload.Enabled = false;
            wbrApotd.Visible = false;

            // If the last saved display time and
            // URL are non-blank, display them.
            DateTime last_time = Properties.Settings.Default.LastLoadTime;
            if (last_time > new DateTime(1, 1, 1))
                txtLastLoadTime.Text = last_time.ToString();

            string url = Properties.Settings.Default.LastUrl;
            if (url.Length > 0)
                txtLastUrl.Text = url;

            // Display the new APOTD image.
            CheckForNewDay();
        }

        // See if it's a new day since the last time
        // we displayed an image. If it is, try to
        // display a new image.
        private void CheckForNewDay()
        {
            // See if today is a new day.
            DateTime last_time =
                Properties.Settings.Default.LastLoadTime;
            if (DateTime.Now.Date > last_time)
            {
                // It's a new day. Check for a new image.
                CheckForNewImage();
            }
            else
            {
                // Wait until tomorrow.
                WaitUntilTomorrow();
            }
        }

        // Look for a new image.
        private void tmrDownload_Tick(object sender, EventArgs e)
        {
            tmrDownload.Enabled = false;
            CheckForNewImage();
        }

        // It's a new day. Look for a new image.
        private void CheckForNewImage()
        {
            ShowMessage("Checking for new image " + DateTime.Now.ToString());

            const string url = "http://antwrp.gsfc.nasa.gov/apod/";
            try
            {
                // Load the web page.
                wbrApotd.Navigate(url);
            }
            catch (Exception ex)
            {
                ShowMessage("*** Error navigating to " + url);
                ShowMessage("*** " + ex.Message);
                WaitTenMinutes();
            }
        }

        // The web page has loaded. Get the APOTD image.
        private void wbrApotd_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            // Get the image's URL.
            HtmlDocument doc = wbrApotd.Document;
            string img_url = doc.Images[0].GetAttribute("src");

            // See if this is a new image.
            string last_url = Properties.Settings.Default.LastUrl;
            if (img_url == last_url)
            {
                // This is the same image we loaded before.
                // Wait 10 minutes and try again.
                WaitTenMinutes();
            }
            else
            {
                try
                {
                    // Download and display the new image.
                    DownloadImage(img_url);

                    // Wait to get tomorrow's image.
                    WaitUntilTomorrow();
                }
                catch (Exception ex)
                {
                    ShowMessage("*** Download Error");
                    ShowMessage("*** " + ex.Message);

                    // Wait 10 minutes and try again.
                    WaitTenMinutes();
                }
            }
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            ShowMessage("Downloading image " +
                url + " at " + DateTime.Now.ToString());

            // Make a WebClient.
            WebClient web_client = new WebClient();

            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol =
                (SecurityProtocolType)3072;

            // Download the file.
            web_client.DownloadFile(url, filename);

            // Display the picture on the desktop.
            filename = Application.StartupPath + "\\" + filename;
            DisplayPicture(filename, true);

            // Save the new display time and URL.
            DateTime now = DateTime.Now;
            txtLastLoadTime.Text = now.ToString();
            txtLastUrl.Text = url;
            Properties.Settings.Default.LastLoadTime = now;
            Properties.Settings.Default.LastUrl = url;
            Properties.Settings.Default.Save();
        }

        // Display the file on the desktop.
        private void DisplayPicture(string file_name, bool update_registry)
        {
            ShowMessage("Displaying " + file_name);

            // If we should update the registry,
            // set the appropriate flags.
            uint flags = 0;
            if (update_registry)
                flags = SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE;

            // Set the desktop background to this file.
            if (!SystemParametersInfo(SPI_SETDESKWALLPAPER,
                0, file_name, flags))
            {
                ShowMessage("*** SystemParametersInfo failed.");
            }
        }

        // Set the timer to wait until 10 minutes
        // after midnights tomorrow morning.
        private void WaitUntilTomorrow()
        {
            DateTime now = DateTime.Now;
            DateTime tomorrow = now.AddDays(1);
            DateTime wait_until =
                new DateTime(tomorrow.Year,
                    tomorrow.Month, tomorrow.Day, 0, 10, 0);
            TimeSpan wait_length = wait_until - now;

            tmrDownload.Enabled = false;
            tmrDownload.Interval = (int)wait_length.TotalMilliseconds;
            tmrDownload.Enabled = true;

            ShowWait();
        }

        // Wait for 10 minutes and try again.
        private void WaitTenMinutes()
        {
            int ten_minutes = 10 * 60 * 1000;
            tmrDownload.Enabled = false;
            tmrDownload.Interval = ten_minutes;
            tmrDownload.Enabled = true;

            ShowWait();
        }

        // Display the wait time.
        private void ShowWait()
        {
            DateTime dt = DateTime.Now.AddMilliseconds(tmrDownload.Interval);
            ShowMessage("Waiting until " + dt.ToString());
        }

        // Add a message to the listbox.
        private void ShowMessage(string txt)
        {
            lstMessages.Items.Add(txt);
        }
    }
}
