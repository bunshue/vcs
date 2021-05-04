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
      StreamWriter sw = null;
      FileStream fs = null;

      SaveFileDialog1.InitialDirectory = "C:\\";
      SaveFileDialog1.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*";
      SaveFileDialog1.FilterIndex = 1;
      SaveFileDialog1.RestoreDirectory = true;
      SaveFileDialog1.ShowHelp = true;
      SaveFileDialog1.Title = "Save File Dialog";

      if (SaveFileDialog1.ShowDialog() == DialogResult.OK)
      {
        TextBox1.Text = SaveFileDialog1.FileName;

        try
        {
          fs = new FileStream(SaveFileDialog1.FileName, FileMode.Create, FileAccess.Write);
          sw = new StreamWriter(fs, System.Text.Encoding.Default);

          sw.Write(TextBox2.Text);
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString(), "Save File Error", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
        }
        finally
        {
          if (sw != null)
            sw.Close();

          if (fs != null)
            fs.Close();

          MessageBox.Show("Save file " + TextBox1.Text + " successfully.", "Save File", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        }
      }
    }
  }
}
