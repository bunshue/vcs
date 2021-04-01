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

namespace Cookie
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      string strBuff = "";

      System.Net.Cookie cookie = new System.Net.Cookie("HASH", "", "/", "microsoft.com");

      strBuff = "Comment: " + cookie.Comment.ToString() + "\r\n";
      strBuff = strBuff + "Domain: " + cookie.Domain.ToString() + "\r\n";
      strBuff = strBuff + "Expired: " + cookie.Expired.ToString() + "\r\n";
      strBuff = strBuff + "Expires: " + cookie.Expires.ToString() + "\r\n";
      strBuff = strBuff + "Name: " + cookie.Name.ToString() + "\r\n";
      strBuff = strBuff + "Path: " + cookie.Path.ToString() + "\r\n";
      strBuff = strBuff + "Port: " + cookie.Port.ToString() + "\r\n";
      strBuff = strBuff + "Secure: " + cookie.Secure.ToString() + "\r\n";
      strBuff = strBuff + "Value: " + cookie.Value.ToString() + "\r\n";
      strBuff = strBuff + "Version: " + (cookie.Version == 1 ? "2109" : "2965") + "\r\n";

      txtCookie.Text = strBuff;
    }
  }
}
