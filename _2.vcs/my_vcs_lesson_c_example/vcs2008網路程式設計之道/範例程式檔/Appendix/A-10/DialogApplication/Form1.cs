using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Printing;

namespace DialogApplication
{
  public partial class Form1 : Form
  {
    private System.Drawing.Printing.PageSettings pageSetting;
    private StreamReader streamReader;
    private String filename;

    public Form1()
    {
      InitializeComponent();
    }

    private void mnuOpen_Click(object sender, EventArgs e)
    {
      FileStream fileStream = null;

      OpenFileDialog1.InitialDirectory = "C:\\";
      OpenFileDialog1.Filter = "Text files (*.txt)|*.txt";
      OpenFileDialog1.FilterIndex = 2;
      OpenFileDialog1.RestoreDirectory = true;
      OpenFileDialog1.ShowHelp = true;
      OpenFileDialog1.Title = "Open File Dialog";

      if (OpenFileDialog1.ShowDialog() == DialogResult.OK)
      {
        this.Text = OpenFileDialog1.FileName;
        filename = OpenFileDialog1.FileName;

        TextBox1.Text = "";

        try
        {
          fileStream = new FileStream(OpenFileDialog1.FileName, FileMode.Open, FileAccess.Read);
          streamReader = new StreamReader(fileStream, System.Text.Encoding.Default);

          TextBox1.Text = streamReader.ReadToEnd();
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString(), "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
        }
        finally
        {
          if (streamReader != null)
            streamReader.Close();

          if (fileStream != null)
            fileStream.Close();
        }
      }
    }

    private void mnuPageSetup_Click(object sender, EventArgs e)
    {
      try
      {
        if (pageSetting == null)
          pageSetting = new System.Drawing.Printing.PageSettings();

        PageSetupDialog1.AllowMargins = true;
        PageSetupDialog1.AllowOrientation = true;
        PageSetupDialog1.AllowPaper = true;
        PageSetupDialog1.AllowPrinter = true;
        PageSetupDialog1.PageSettings = pageSetting;
        PageSetupDialog1.ShowDialog();
      }
      catch (Exception ex)
      {
        MessageBox.Show(ex.StackTrace.ToString(), "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
      }
    }

    private void mnuPreview_Click(object sender, EventArgs e)
    {
      if (filename != null)
      {
        try
        {
          streamReader = new StreamReader(filename);

          PrintClass printFile = new PrintClass(streamReader);

          if (pageSetting != null)
            printFile.DefaultPageSettings = pageSetting;

          PrintPreviewDialog1.Document = printFile;
          PrintPreviewDialog1.ShowDialog();
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.Message, "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
        }
        finally
        {
          if (streamReader != null)
            streamReader.Close();
        }
      }
      else
        MessageBox.Show("Please select file first.", "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
    }

    private void mnuPrint_Click(object sender, EventArgs e)
    {
      if (filename != null)
      {
        try
        {
          streamReader = new StreamReader(filename);

          PrintClass printFile = new PrintClass(streamReader);

          if (pageSetting != null)
            printFile.DefaultPageSettings = pageSetting;

          PrintDialog1.Document = printFile;
          PrintDialog1.AllowPrintToFile = true;
          PrintDialog1.AllowSelection = true;
          PrintDialog1.AllowSomePages = true;

          if (PrintDialog1.ShowDialog() == DialogResult.OK)
            printFile.Print();
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString(), "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
        }
        finally
        {
          if (streamReader != null)
            streamReader.Close();
        }
      }
      else
        MessageBox.Show("Please select file first.", "Print", MessageBoxButtons.OK, MessageBoxIcon.Error, MessageBoxDefaultButton.Button1);
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Dialog Application", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
        this.Close();
    }
  }
}
