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
      IPHostEntry hostEntry = null;
      IPAddress[] addrList = null;
      string strTemp = "";

      try
      {
        hostEntry = Dns.Resolve(txtIP.Text);

        addrList = hostEntry.AddressList;

        strTemp = "";

        for (int i = 0; i <= addrList.Length - 1; i++)
          strTemp = strTemp + addrList[i].ToString() + "\r\n";

        MessageBox.Show("Address List: " + "\r\n" + strTemp,
          "DNS Resolve", MessageBoxButtons.OK,
          MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
      }
      catch (SocketException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
