using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.IO;
using System.Net.Mail;

namespace GetHTML
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private string savePath = System.Environment.GetFolderPath(Environment.SpecialFolder.Desktop) + "\\urlHtml.txt";
		private void btnGet_Click(object sender, EventArgs e)
		{
			if (this.txtUrl.Text == "")
			{
				return;
			}
			DateTime dtNow = DateTime.Now;
			string strHTML = "";
			switch (this.tabControl1.SelectedTab.Text)
			{
				case "WebClient":
					strHTML = GetWebClient(this.txtUrl.Text);
					break;
				case "WebRequest":
					strHTML = GetWebRequest(this.txtUrl.Text);
					break;
				case "HttpWebRequest":
					strHTML = GetHttpWebRequest(this.txtUrl.Text);
					break;
				default:
					break;
			}

			TimeSpan span = DateTime.Now - dtNow;
			MessageBox.Show("用时：[" + span.ToString() + "]");
			System.IO.File.WriteAllText(savePath, strHTML, System.Text.Encoding.GetEncoding(this.txtEncoder.Text));
			System.Diagnostics.Process.Start(savePath);
		}

		private string GetWebClient(string url)
		{
			string strHTML = "";
            WebClient wc = new WebClient();     // 建立 WebClient
			Stream myStream = wc.OpenRead(url);
			StreamReader sr = new StreamReader(myStream, System.Text.Encoding.GetEncoding(this.txtEncoder.Text));
			strHTML = sr.ReadToEnd();
			myStream.Close();

			return strHTML;
		}

		private string GetWebRequest(string url)
		{
			Uri uri = new Uri(url);
			WebRequest myReq = WebRequest.Create(uri);
			WebResponse result = myReq.GetResponse();
			Stream receviceStream = result.GetResponseStream();
			StreamReader readerOfStream = new StreamReader(receviceStream, System.Text.Encoding.GetEncoding(this.txtEncoder.Text));
			string strHTML = readerOfStream.ReadToEnd();
			readerOfStream.Close();
			receviceStream.Close();
			result.Close();

			return strHTML;
		}

		private string GetHttpWebRequest(string url)
		{
			Uri uri = new Uri(url);
			HttpWebRequest myReq = (HttpWebRequest)WebRequest.Create(uri);
			myReq.UserAgent = "User-Agent:Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705";
			myReq.Accept = "*/*";
			myReq.KeepAlive = true;
			myReq.Headers.Add("Accept-Language", "zh-cn,en-us;q=0.5");
			HttpWebResponse result = (HttpWebResponse)myReq.GetResponse();
			Stream receviceStream = result.GetResponseStream();
			StreamReader readerOfStream = new StreamReader(receviceStream, System.Text.Encoding.GetEncoding(this.txtEncoder.Text));
			string strHTML = readerOfStream.ReadToEnd();
			readerOfStream.Close();
			receviceStream.Close();
			result.Close();

			return strHTML;
		}

		private void btnSend_Click(object sender, EventArgs e)
		{
			MailMessage mailMessage = new MailMessage();
			mailMessage.To.Add(this.txtTo.Text);
			mailMessage.From = new System.Net.Mail.MailAddress(this.txtFrom.Text);
			mailMessage.Subject = this.txtTitle.Text;
			mailMessage.Body = this.txtContent.Text;
			mailMessage.IsBodyHtml = true;
			mailMessage.BodyEncoding = System.Text.Encoding.UTF8;
			mailMessage.Priority = System.Net.Mail.MailPriority.Normal;

			SmtpClient smtpClient = new SmtpClient();
			smtpClient.Credentials = new System.Net.NetworkCredential(mailMessage.From.Address, this.txtPassword.Text);
			smtpClient.DeliveryMethod = System.Net.Mail.SmtpDeliveryMethod.Network;
			smtpClient.Host = "smtp." + mailMessage.From.Host;
			smtpClient.Port = 25;
			smtpClient.Timeout = 3000;
			smtpClient.EnableSsl = false;
			smtpClient.Send(mailMessage);
		}
	}
}