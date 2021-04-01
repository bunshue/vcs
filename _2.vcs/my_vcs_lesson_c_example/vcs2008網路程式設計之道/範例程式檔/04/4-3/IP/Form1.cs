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
      IPAddress address;
      IPEndPoint ipEndPoint;
      SocketAddress socketAddr;
      string strBuff = "";

      try
      {
        address = IPAddress.Parse(txtIP.Text);
        ipEndPoint = new System.Net.IPEndPoint(address, Int32.Parse(txtPort.Text));

        // 將IPEndPoint序列化為SocketAddress
        socketAddr = ipEndPoint.Serialize();

        strBuff = "Address Family: " + ipEndPoint.AddressFamily.ToString() + "\r\n";
        strBuff = strBuff + "IP:Port: " + ipEndPoint.Address.ToString() + ":" + ipEndPoint.Port.ToString() + "\r\n";
        strBuff = txtResult.Text + "SocketAddress 內容: " + socketAddr.ToString() + "\r\n";
        txtResult.Text = strBuff;
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
