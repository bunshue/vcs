using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// 命名空間
using System.Net;

namespace Request
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      System.Net.WebRequest request = null;
      string result = "";

      if (txtURL.Text != "")
      {
        string uriString = "";

        if (!txtURL.Text.StartsWith("http://"))
        {
          uriString = "http://" + txtURL.Text;
          txtURL.Text = uriString;
        }
        else
          uriString = txtURL.Text;

        try
        {
          // 以WebRequest抽象類別的Create方法建立WebRequest物件
          request = WebRequest.Create(new Uri(uriString));

          // 設定Proxy伺服器
          if (txtProxy.Text != "" && txtPort.Text != "")
          {
            string proxyString = "http://" + txtProxy.Text + ":" + txtPort.Text;

            if (proxyString != "")
              // 設定WebRequest類別之Proxy伺服器
              request.Proxy = new WebProxy(proxyString, true);
          }

          // WebRequest類別之屬性

          // 連結群組名稱
          if (request.ConnectionGroupName != null)
            result = result + "ConnectionGroupName: " + request.ConnectionGroupName.ToString() + "\r\n";

          // 用戶端所傳送資料內容的大小（byte）
          if (request.ContentLength != -1)
            result = result + "ContentLength: " + request.ContentLength.ToString() + "\r\n";

          // 用戶端所傳送資料內容的MIME格式
          if (request.ContentType != null)
            result = result + "ContentType: " + request.ContentType.ToString() + "\r\n";

          // 用戶端網路憑證
          if (request.Credentials != null)
            result = result + "Credentials: " + request.Credentials.ToString() + "\r\n";

          // 用戶端所傳送資料內容的標題資訊
          result = result + "Headers: " + request.Headers.ToString() + "\r\n";

          // 用戶端所使用的通訊協定方法
          result = result + "Method: " + request.Method.ToString() + "\r\n";

          // 是否要求預先驗證
          result = result + "PreAuthenticate: " + request.PreAuthenticate + "\r\n";

          // 用戶端所傳送的URI
          result = result + "RequestUri: " + request.RequestUri.ToString() + "\r\n";

          txtRequest.Text = result;
        }
        catch (Exception ex)
        {
          txtRequest.Text = ex.StackTrace.ToString();
        }
      }
    }
  }
}
