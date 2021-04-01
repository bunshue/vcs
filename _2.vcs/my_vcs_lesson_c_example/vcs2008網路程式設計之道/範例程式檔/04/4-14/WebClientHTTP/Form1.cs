using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// 命名空間
using System.Net;
using System.IO;

namespace WebClientHTTP
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnDownload_Click(object sender, EventArgs e)
    {
      string uri = "";

      if (!txtURL.Text.StartsWith("http://"))
        uri = "http://" + txtURL.Text;
      else
        uri = txtURL.Text;

      string localfile = uri.Substring(uri.LastIndexOf("/") + 1); ;

      StatusBar.Text = "Downloading file from " + uri;

      // 建立WebClient物件
      WebClient webclient = new WebClient();

      // 下載檔案
      try
      {
        // 建立NetworkCredential物件，請參考4-5節之說明
        // 設定用戶端網路認證，則使用者帳號及密碼
        NetworkCredential credentials = new NetworkCredential("anonymous", "test@microsoft.com");

        webclient.Credentials = credentials;

        // 自指定URI下載資料，並儲存為本機之檔案
        webclient.DownloadFile(uri, localfile);

        StatusBar.Text = "Download file from " + uri + " completed.";
        MessageBox.Show("Download file completed.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      }
      catch (WebException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }

      webclient.Dispose();
    }
  }
}