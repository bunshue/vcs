using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;

namespace HTTPResponse
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnOK_Click(object sender, EventArgs e)
    {
      System.Net.HttpWebRequest httpReq;
      System.Net.HttpWebResponse httpResp;

      string strBuff = "";

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
          System.Uri httpURL = new Uri(uriString);

          // 以WebRequest抽象類別的Create方法建立HttpWebRequest
          httpReq = (HttpWebRequest)WebRequest.Create(httpURL);

          // 使用HttpWebRequest類別的GetResponse方法建立HttpWebResponse
          httpResp = (HttpWebResponse)httpReq.GetResponse();

          // HttpWebResponse 類別之屬性
          strBuff = "CharacterSet: " + httpResp.CharacterSet.ToString() + "\r\n";
          strBuff = strBuff + "ContentEncoding: " + httpResp.ContentEncoding.ToString() + "\r\n";
          strBuff = strBuff + "ContentLength: " + httpResp.ContentLength.ToString() + "\r\n";
          strBuff = strBuff + "ContentType: " + httpResp.ContentType.ToString() + "\r\n";
          strBuff = strBuff + "LastModified: " + httpResp.LastModified.ToString() + "\r\n";
          strBuff = strBuff + "Method: " + httpResp.Method.ToString() + "\r\n";
          strBuff = strBuff + "ProtocolVersion: " + httpResp.ProtocolVersion.ToString() + "\r\n";
          strBuff = strBuff + "ResponseUri: " + httpResp.ResponseUri.ToString() + "\r\n";
          strBuff = strBuff + "Server: " + httpResp.Server.ToString() + "\r\n";
          strBuff = strBuff + "StatusCode: " + httpResp.StatusCode.ToString() + "\r\n";
          strBuff = strBuff + "StatusDescription: " + httpResp.StatusDescription.ToString() + "\r\n";

          txtResponse.Text = strBuff;
        }
        catch (Exception ex)
        {
          txtResponse.Text = ex.StackTrace.ToString();
        }
      }
    }
  }
}