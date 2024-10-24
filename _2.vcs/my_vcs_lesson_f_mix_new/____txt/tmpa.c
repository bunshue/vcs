
client.DownloadFile(url, filename);
string data = client1.DownloadString(url_file1);          //抓網頁資料到記憶體
client2.DownloadFile(url_file2, filename_local);          //抓網頁資料到本地檔案
string xml = client3.DownloadString(url_weather);        //抓資料

MemoryStream image_stream = new MemoryStream(client.DownloadData(url));

byte[] bd = client.DownloadData(sURL);






Stream stream = client.OpenRead(URLAddress);


client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");









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

namespace vcs_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //for Romeo and Sugar    3072
            //ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            //ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */

            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            using ( client1 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
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
            using ( client2 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                    int pos1 = url_file2.LastIndexOf('/');
                    int pos2 = url_file2.LastIndexOf('.');
                    string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
                    richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

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
            using (  = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    // Get the response string from the URL.
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
            Application.DoEvents();


            //下載COVID-19資料

            // Compose the local data file name.
            string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            string url = "https://covidtracking.com/api/v1/states/daily.csv";

            richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
            Application.DoEvents();

            DownloadFile(url, filename_covid19a);


            richTextBox1.Text += "Loading case data...\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
            DownloadFile(url, filename_covid19b);
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            // Make a .
             client = new ();

            /*
            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            */

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');
            string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
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
                 client = new ();

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

        private void DownloadFile(string url, string filename)
        {
            try
            {
                // Make a .
                 client = new ();

                // Download the file.
                client.DownloadFile(url, filename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            finally
            {
                if (!File.Exists(filename))
                {
                    richTextBox1.Text += "下載 : " + filename + "\tNG\n";
                }
                else
                {
                    richTextBox1.Text += "下載 : " + filename + "\tOK\n";
                }
            }
        }

    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}




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

namespace vcs_
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}

private void Form1_Load(object sender, EventArgs e)
{
// Allow TLS 1.1 and TLS 1.2 protocols for file download.
//for Sugar     3840 Romeo也可用
ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

//for Romeo and Sugar    3072
//ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
//ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
//richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
}

private void button1_Click(object sender, EventArgs e)
{
/*
//加入這段語法忽略憑證
ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
*/

string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
//string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

using ( client1 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
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
using ( client2 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
//string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
int pos1 = url_file2.LastIndexOf('/');
int pos2 = url_file2.LastIndexOf('.');
string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

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
using (  = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
// Get the response string from the URL.
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
Application.DoEvents();


//下載COVID-19資料

// Compose the local data file name.
string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
string url = "https://covidtracking.com/api/v1/states/daily.csv";

richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
Application.DoEvents();

DownloadFile(url, filename_covid19a);


richTextBox1.Text += "Loading case data...\n";
Application.DoEvents();

// Compose the local data file name.
string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
DownloadFile(url, filename_covid19b);
}

// Download the indicated file.
private void DownloadImage(string url)
{
//richTextBox1.Text += "下載圖片 : " + url + "\n";

// Make a Web
 client = new ();

/*
int pos = url.LastIndexOf('/');
string filename = url.Substring(pos + 1);
*/

int pos1 = url.LastIndexOf('/');
int pos2 = url.LastIndexOf('.');
string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

// Use one of the following.
// For .NET Framework 4.5 and later:
//ServicePointManager.SecurityProtocol =
//    SecurityProtocolType.Tls12;
// For .NET Framework 4.0 through 4.4:
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

// Download the file.
}

// Download a file from the internet.
// Get the picture at a given URL.
private Image GetPicture(string url)
{
try
{
 client = new ();

// Use one of the following.
//ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

return Image.FromStream(image_stream);
}
catch (Exception ex)
{
richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
return null;
}
}

private void DownloadFile(string url, string filename)
{
try
{
// Make a Web
 client = new ();

// Download the file.
}
catch (Exception ex)
{
MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
}
finally
{
if (!File.Exists(filename))
{
richTextBox1.Text += "下載 : " + filename + "\tNG\n";
}
else
{
richTextBox1.Text += "下載 : " + filename + "\tOK\n";
}
}
}

}

public class Protocols
{
public const SecurityProtocolType
protocol_SystemDefault = 0,
protocol_Ssl3 = (SecurityProtocolType)48,
protocol_Tls = (SecurityProtocolType)192,
protocol_Tls11 = (SecurityProtocolType)768,
protocol_Tls12 = (SecurityProtocolType)3072;
}

}
