using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace FormApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      // �~��Form���O���ͷs���������
      Form Form2 = new Form();

      Form2.Cursor = System.Windows.Forms.Cursors.Cross;
      Form2.FormBorderStyle = FormBorderStyle.Sizable;
      Form2.Height = 400;
      Form2.HelpButton = true;
      Form2.MaximizeBox = true;
      Form2.MinimizeBox = true;
      Form2.Name = "Form2";
      Form2.ShowInTaskbar = true;
      Form2.StartPosition = FormStartPosition.CenterParent;
      Form2.Text = "New Form";
      Form2.Width = 500;
      Form2.WindowState = FormWindowState.Normal;
      Form2.Enabled = true;

      // �HForm���O��ShowDialog��k��ܵ������
      Form2.ShowDialog();
    }

  }
}
