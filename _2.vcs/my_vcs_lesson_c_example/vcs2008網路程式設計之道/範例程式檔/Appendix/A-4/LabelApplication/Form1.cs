using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace LabelApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      LinkLabel1.Links.Add(0, 16, "http://www.microsoft.com/Taiwan");

      LinkLabel1.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
    }

    private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
    {
      LinkLabel1.Links[LinkLabel1.Links.IndexOf(e.Link)].Visited = true;

      System.Diagnostics.Process.Start(e.Link.LinkData.ToString());
    }
  }
}