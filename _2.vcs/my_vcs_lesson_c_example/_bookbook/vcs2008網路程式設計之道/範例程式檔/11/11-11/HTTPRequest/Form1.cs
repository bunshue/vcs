using System;
using System.Linq;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;

namespace HTTPRequest
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

          httpReq = (HttpWebRequest)WebRequest.Create(httpURL);

          strBuff = "Address: " + httpReq.Address.ToString() + "\r\n";
          strBuff = strBuff + "AllowAutoRedirect: " + httpReq.AllowAutoRedirect.ToString() + "\r\n";
          strBuff = strBuff + "AllowWriteStreamBuffering: " + httpReq.AllowWriteStreamBuffering.ToString() + "\r\n";

          // .Net Compact Framework不支援ClientCertificates屬性
          //strBuff = strBuff + "ClientCertificates: " + httpReq.ClientCertificates.ToString() + "\r\n";

          if (httpReq.Connection != null)
            strBuff = strBuff + "Connection: " + httpReq.Connection.ToString() + "\r\n";

          if (httpReq.ConnectionGroupName != null)
            strBuff = strBuff + "ConnectionGroupName: " + httpReq.ConnectionGroupName.ToString() + "\r\n";

          if (httpReq.ContentLength != -1)
            strBuff = strBuff + "ContentLength: " + httpReq.ContentLength.ToString() + "\r\n";

          if (httpReq.ContentType != null)
            strBuff = strBuff + "ContentType: " + httpReq.ContentType.ToString() + "\r\n";

          strBuff = strBuff + "HaveResponse: " + httpReq.HaveResponse.ToString() + "\r\n";
          strBuff = strBuff + "IfModifiedSince: " + httpReq.IfModifiedSince.ToString() + "\r\n";
          strBuff = strBuff + "KeepAlive: " + httpReq.KeepAlive + "\r\n";
          strBuff = strBuff + "MaximumAutomaticRedirections: " + httpReq.MaximumAutomaticRedirections + "\r\n";

          if (httpReq.MediaType != null)
            strBuff = strBuff + "MediaType: " + httpReq.MediaType.ToString() + "\r\n";

          strBuff = strBuff + "Method: " + httpReq.Method.ToString() + "\r\n";
          strBuff = strBuff + "PreAuthenticate: " + httpReq.PreAuthenticate + "\r\n";
          strBuff = strBuff + "ProtocolVersion: " + httpReq.ProtocolVersion.ToString() + "\r\n";

          if (httpReq.Referer != null)
            strBuff = strBuff + "Referer: " + httpReq.Referer.ToString() + "\r\n";

          strBuff = strBuff + "RequestUri: " + httpReq.RequestUri.ToString() + "\r\n";

          if (httpReq.RequestUri.ToString() != httpReq.Address.ToString())
            strBuff = strBuff + "URL has been changed." + "\r\n";

          if (httpReq.TransferEncoding != null)
            strBuff = strBuff + "TransferEncoding: " + httpReq.TransferEncoding.ToString() + "\r\n";

          if (httpReq.TransferEncoding != null)
            strBuff = strBuff + "UserAgent: " + httpReq.UserAgent.ToString() + "\r\n";

          txtRequest.Text = strBuff;
        }
        catch (Exception ex)
        {
          txtRequest.Text = ex.StackTrace.ToString();
        }
      }
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "HTTP Request", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        this.Close();
      }
    }
  }
}