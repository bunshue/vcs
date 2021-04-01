using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// 命名空間
using System.IO;
using System.Net;
using System.Net.Cache;

namespace Response
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
      System.Net.WebResponse response = null;

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

          // 使用WebRequest類別的GetResponse方法建立WebResponse物件
          response = request.GetResponse();

          // WebResponse類別之屬性

          // 用戶端所接收資料內容的大小（byte）
          result = result + "ContentLength: " + response.ContentLength.ToString() + "\r\n";

          // 用戶端所接收資料內容的MIME格式
          result = result + "ContentType: " + response.ContentType.ToString() + "\r\n";

          // 用戶端所接收的URI
          result = result + "ResponseUri: " + response.ResponseUri.ToString() + "\r\n";

          // 用戶端所接收之回應內容是否從快取中取得
          result = result + "伺服端回應是否取自Cache? " + response.IsFromCache;

          // 關閉回應串流
          response.Close();

          txtResponse.Text = result;
        }
        catch (Exception ex)
        {
          txtResponse.Text = ex.StackTrace.ToString();
        }
      }
    }
  }
}