using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TextBoxApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Resize(object sender, EventArgs e)
    {
      Control control = (Control)sender;

      TextBox1.Location = new System.Drawing.Point(84, 11);
      TextBox1.Size = new System.Drawing.Size(control.Size.Width - 104, 22);
      TextBox2.Location = new System.Drawing.Point(84, 39);
      TextBox2.Size = new System.Drawing.Size(control.Size.Width - 104, 22);
      TextBox3.Location = new System.Drawing.Point(12, 95);
      TextBox3.Size = new System.Drawing.Size(control.Size.Width - 32, control.Size.Height - 133);
    }
  }
}