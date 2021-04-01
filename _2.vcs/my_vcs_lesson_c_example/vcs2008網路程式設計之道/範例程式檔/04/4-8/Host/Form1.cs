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

    private void button1_Click(object sender, EventArgs e)
    {
      IPAddress ipAddr = null;
      IPHostEntry remoteHostEntry = null;

      try
      {
        ipAddr = IPAddress.Parse(txtIP.Text);

        // 透過DNS找尋IP位址相對應之主機名稱 
        remoteHostEntry = Dns.GetHostByAddress(ipAddr);

        txtHost.Text = remoteHostEntry.HostName;
      }
      catch (SocketException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
