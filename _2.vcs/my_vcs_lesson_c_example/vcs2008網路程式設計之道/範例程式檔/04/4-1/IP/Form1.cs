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
      // 將IP位址字串轉換為IPAddress類別
      IPAddress ipAddr1 = IPAddress.Parse(txtIP1.Text);
      IPAddress ipAddr2 = IPAddress.Parse(txtIP2.Text);

      // 比較兩個IP位址是否相同
      if (ipAddr1.Equals(ipAddr2))
        MessageBox.Show(ipAddr1.ToString() + " is equal to " +
          ipAddr2.ToString(), "IP Address",
          MessageBoxButtons.OK, MessageBoxIcon.Information,
          MessageBoxDefaultButton.Button1);
      else
        MessageBox.Show(ipAddr1.ToString() + " is different from " +
          ipAddr2.ToString(), "IP Address",
          MessageBoxButtons.OK, MessageBoxIcon.Warning,
          MessageBoxDefaultButton.Button1);

    }
  }
}
