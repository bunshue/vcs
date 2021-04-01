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
using System.Net.Sockets;

namespace Host
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      try
      {
        // 取得Local主機的識別名稱
        string localHostName = Dns.GetHostName();

        TextBox1.Text = localHostName;
      }
      catch (SocketException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
