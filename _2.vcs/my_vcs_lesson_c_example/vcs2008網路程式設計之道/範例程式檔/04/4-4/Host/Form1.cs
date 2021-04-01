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
      string[] aliasList = null;
      IPAddress[] addrList = null;

      string strTemp = "";

      try
      {
        hostEntry = Dns.GetHostEntry(txtHost.Text);

        // 由於主機有可能有一個以上的 Alias
        // 因此程式中以迴圈方式判斷 Aliases 
        aliasList = hostEntry.Aliases;

        for (int i = 0; i <= aliasList.Length - 1; i++)
          strTemp = strTemp + aliasList[i].ToString() + " ";

        txtAlias.Text = strTemp;

        // 由於主機有可能有一個以上的 IP Address
        // 因此程式中以迴圈方式判斷 AddressList 
        addrList = hostEntry.AddressList;

        for (int i = 0; i <= addrList.Length - 1; i++)
          strTemp = strTemp + addrList[i].ToString() + " ";

        txtIP.Text = strTemp;
      }
      catch (SocketException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
