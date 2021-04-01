using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace DialogApplication
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      StreamReader sr = null;
      FileStream fs = null;

      OpenFileDialog1.InitialDirectory = "C:\\";
      OpenFileDialog1.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*";
      OpenFileDialog1.FilterIndex = 2;
      OpenFileDialog1.RestoreDirectory = true;
      OpenFileDialog1.ShowHelp = true;
      OpenFileDialog1.ShowReadOnly = true;
      OpenFileDialog1.Title = "Open File Dialog";

      if (OpenFileDialog1.ShowDialog() == DialogResult.OK)
      {
        TextBox1.Text = OpenFileDialog1.FileName;
        TextBox2.Text = "";

        if (OpenFileDialog1.ReadOnlyChecked)
          chkReadOnly.CheckState = CheckState.Checked;
        else
          chkReadOnly.CheckState = CheckState.Unchecked;

        try
        {
          fs = new FileStream(OpenFileDialog1.FileName, FileMode.Open, FileAccess.Read);
          sr = new StreamReader(fs, System.Text.Encoding.Default);

          TextBox2.Text = sr.ReadToEnd();
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString(), "Open File Error", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
        }
        finally
        {
          if (sr != null)
            sr.Close();

          if (fs != null)
            fs.Close();
        }
      }
    }
  }
}
