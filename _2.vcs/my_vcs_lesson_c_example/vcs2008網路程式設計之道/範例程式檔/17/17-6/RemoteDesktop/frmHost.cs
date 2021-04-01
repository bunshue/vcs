using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace RemoteDesktop
{
  public partial class frmHost : Form
  {
    public string Host = "";

    public frmHost()
    {
      InitializeComponent();
    }

    private void btnOK_Click(object sender, EventArgs e)
    {
      Host = txtIP.Text;
    }
  }
}