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

namespace IP
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
        // 將IP位址字串轉換為IPAddress類別
        IPAddress address = IPAddress.Parse(txtIP.Text);

        // 判斷IP位址是為否回送位址
        if (IPAddress.IsLoopback(address) && address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork)
          // 為IPv4及回送位址
          MessageBox.Show(address.ToString() + " is a IPv4 loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        else if (IPAddress.IsLoopback(address) && address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6)
          // 為IPv6及回送位址
          MessageBox.Show(address.ToString() + " is a IPv6 loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        else
          MessageBox.Show(address.ToString() + " is not a loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.Message);
      }
    }
  }
}
