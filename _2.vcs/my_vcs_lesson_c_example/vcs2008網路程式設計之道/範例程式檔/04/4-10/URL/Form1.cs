using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace URL
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      System.Uri URL = null;
      string sResult = "";
      string uriString = "";

      if (!txtURL.Text.StartsWith("http://"))
      {
        uriString = "http://" + txtURL.Text;
        txtURL.Text = uriString;
      }
      else
        uriString = txtURL.Text;

      URL = new System.Uri(uriString);

      // System.Uri類別之屬性
      sResult = "AbsolutePath: " + URL.AbsolutePath + "\r\n";
      sResult = sResult + "AbsoluteUri: " + URL.AbsoluteUri + "\r\n";
      sResult = sResult + "Authority: " + URL.Authority + "\r\n";
      sResult = sResult + "Host: " + URL.Host + "\r\n";
      sResult = sResult + "Port: " + URL.Port + "\r\n";
      sResult = sResult + "LocalPath: " + URL.LocalPath + "\r\n";
      sResult = sResult + "IsDefaultPort: " + URL.IsDefaultPort + "\r\n";
      sResult = sResult + "IsFile: " + URL.IsFile + "\r\n";
      sResult = sResult + "PathAndQuery: " + URL.PathAndQuery + "\r\n";
      sResult = sResult + "Query: " + URL.Query + "\r\n";
      sResult = sResult + "Scheme: " + URL.Scheme + "\r\n";
      sResult = sResult + "UserEscaped: " + URL.UserEscaped + "\r\n";
      sResult = sResult + "UserInfo: " + URL.UserInfo + "\r\n";

      if (URL.HostNameType == UriHostNameType.Basic)
        sResult = sResult + "HostNameType: Basic" + "\r\n";
      else if (URL.HostNameType == UriHostNameType.Dns)
        sResult = sResult + "HostNameType: DNS" + "\r\n";
      else if (URL.HostNameType == UriHostNameType.IPv4)
        sResult = sResult + "HostNameType: IPv4" + "\r\n";
      else if (URL.HostNameType == UriHostNameType.IPv6)
        sResult = sResult + "HostNameType: IPv6" + "\r\n";
      else if (URL.HostNameType == UriHostNameType.Unknown)
        sResult = sResult + "HostNameType: Unknown" + "\r\n";

      txtResult.Text = sResult;
    }
  }
}
