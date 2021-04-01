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
    bool isBusy;
    WebClient webclient;

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // 建立WebClient物件
      webclient = new WebClient();

      // 宣告DownloadFileAsync非同步下載檔案完成時所觸發之事件
      // 並定義所呼叫的方法為DownloadFileCompletedCallback
      webclient.DownloadFileCompleted += new AsyncCompletedEventHandler(DownloadFileCompletedCallback);

      // 宣告非同步下載作業執行中所觸發之事件
      // 並定義所呼叫的方法為DownloadProgressChangedCallback
      webclient.DownloadProgressChanged += new DownloadProgressChangedEventHandler(DownloadProgressChangedCallback);

      isBusy = false;
      ProgressBar.Visible = false;
    }

    private void btnDownload_Click(object sender, EventArgs e)
    {
      if (isBusy)
      {
        // 取消非同步作業
        webclient.CancelAsync();
        isBusy = false;
        ProgressBar.Visible = false;
        btnDownload.Text = "&Download";
      }
      else
      {
        try
        {
          string uriString = "";

          if (!txtURL.Text.StartsWith("http://"))
            uriString = "http://" + txtURL.Text;
          else
            uriString = txtURL.Text;

          Uri uri = new Uri(uriString);

          string localfile = uriString.Substring(uriString.LastIndexOf("/") + 1); ;

          // 設定ProgressBar
          ProgressBar.Visible = true;
          ProgressBar.Value = 0;
          isBusy = true;
          btnDownload.Text = "&Cancel";

          // 建立NetworkCredential物件，請參考4-5節之說明
          // 設定用戶端網路認證，則使用者帳號及密碼
          NetworkCredential credentials = new NetworkCredential("anonymous", "test@microsoft.com");

          webclient.Credentials = credentials;

          // 非同步自指定URI下載檔案至本機
          webclient.DownloadFileAsync(uri, localfile);
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString());
        }
      }
    }

    // 自訂方法，非同步下載檔案完成時所呼叫的方法
    private void DownloadFileCompletedCallback(object sender, AsyncCompletedEventArgs e)
    {
      isBusy = false;
      btnDownload.Text = "&Download";

      if (e.Error == null)
        MessageBox.Show("Download file completed.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      else
        MessageBox.Show("Download file error.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Error);

      ProgressBar.Visible = false;
      webclient.Dispose();
    }

    private void DownloadProgressChangedCallback(object sender, DownloadProgressChangedEventArgs e)
    {
      // 取得非同步作業的進度百分比
      // 並藉此改變ProgressBar物件的顯示進度
      ProgressBar.Value = e.ProgressPercentage;
    }
  }
}