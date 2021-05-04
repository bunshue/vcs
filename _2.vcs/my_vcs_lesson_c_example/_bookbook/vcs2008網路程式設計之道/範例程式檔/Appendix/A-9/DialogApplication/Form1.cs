using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace DialogApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // Show Color Dialog
          ColorDialog1.AllowFullOpen = false;
          ColorDialog1.ShowHelp = true;
          ColorDialog1.Color = TextBox1.ForeColor;

          if (ColorDialog1.ShowDialog() == DialogResult.OK)
            TextBox1.ForeColor = ColorDialog1.Color;

          break;

        case 1:
          // Show Font Dialog
          FontDialog1.Font = TextBox1.Font;
          FontDialog1.ShowHelp = true;
          FontDialog1.Color = TextBox1.ForeColor;
          FontDialog1.ShowColor = true;

          if (FontDialog1.ShowDialog() == DialogResult.OK)
          {
            TextBox1.Font = FontDialog1.Font;
            TextBox1.ForeColor = FontDialog1.Color;
          }

          break;
      }
    }
  }
}
