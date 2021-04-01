using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ButtonApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      TextBox1.Text = "Button1 Click";
    }

    private void Button2_Click(object sender, EventArgs e)
    {
      TextBox1.Text = "Button2 Click";
    }

    private void Button1_MouseDown(object sender, MouseEventArgs e)
    {
      TextBox1.Text = "Button1 Mouse Down";
    }

    private void Button1_MouseHover(object sender, EventArgs e)
    {
      TextBox1.Text = "Button1 Mouse Hover";
    }

    private void Button2_MouseDown(object sender, MouseEventArgs e)
    {
      TextBox1.Text = "Button2 Mouse Down";
    }

    private void Button2_MouseHover(object sender, EventArgs e)
    {
      TextBox1.Text = "Button2 Mouse Hover";
    }
  }
}