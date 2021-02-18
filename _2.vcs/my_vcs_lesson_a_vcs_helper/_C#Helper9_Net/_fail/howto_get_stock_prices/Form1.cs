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

namespace howto_get_stock_prices
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Get the stock prices.
        private void btnGetPrices_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Build the URL.
            string url = "";
            if (txtSymbol1.Text != "") url += txtSymbol1.Text + "+";
            if (txtSymbol2.Text != "") url += txtSymbol2.Text + "+";
            if (txtSymbol3.Text != "") url += txtSymbol3.Text + "+";
            if (txtSymbol4.Text != "") url += txtSymbol4.Text + "+";
            if (url != "")
            {
                // Remove the trailing plus sign.
                url = url.Substring(0, url.Length - 1);

                // Prepend the base URL.
                const string base_url =
                    "http://download.finance.yahoo.com/d/quotes.csv?s=@&f=sl1d1t1c1";
                url = base_url.Replace("@", url);

                // Get the response.
                try
                {
                    // Get the web response.
                    string result = GetWebResponse(url);

                    richTextBox1.Text += "result = " + result + "\n";

                    Console.WriteLine(result.Replace("\\r\\n", "\r\n"));

                    // Pull out the current prices.
                    string[] lines = result.Split(
                        new char[] { '\r', '\n' },
                        StringSplitOptions.RemoveEmptyEntries);
                    txtPrice1.Text = FormatCurrency(lines[0].Split(',')[1]);
                    txtPrice2.Text = FormatCurrency(lines[1].Split(',')[1]);
                    txtPrice3.Text = FormatCurrency(lines[2].Split(',')[1]);
                    txtPrice4.Text = FormatCurrency(lines[3].Split(',')[1]);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Read Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                }
            }

            this.Cursor = Cursors.Default;
        }

        // Return a number formatted as currency or
        // a blank string if the text isn't a number.
        private string FormatCurrency(string text)
        {
            decimal value;
            if (decimal.TryParse(text, out value)) return value.ToString("C3");
            return "";
        }

        // Get a web response.
        private string GetWebResponse(string url)
        {
            richTextBox1.Text += "url = " + url + "\n";
            // Make a WebClient.
            WebClient web_client = new WebClient();
            web_client.Proxy = null;

            // Get the indicated URL.
            web_client.Proxy = null;
            Stream response = web_client.OpenRead(url);

            // Read the result.
            using (StreamReader stream_reader = new StreamReader(response))
            {
                // Get the results.
                string result = stream_reader.ReadToEnd();

                // Close the stream reader and its underlying stream.
                stream_reader.Close();

                // Return the result.
                return result;
            }
        }
    }
}
