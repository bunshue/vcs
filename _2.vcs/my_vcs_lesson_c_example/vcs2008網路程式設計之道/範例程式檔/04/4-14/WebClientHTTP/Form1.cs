using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// �R�W�Ŷ�
using System.Net;
using System.IO;

namespace WebClientHTTP
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnDownload_Click(object sender, EventArgs e)
    {
      string uri = "";

      if (!txtURL.Text.StartsWith("http://"))
        uri = "http://" + txtURL.Text;
      else
        uri = txtURL.Text;

      string localfile = uri.Substring(uri.LastIndexOf("/") + 1); ;

      StatusBar.Text = "Downloading file from " + uri;

      // �إ�WebClient����
      WebClient webclient = new WebClient();

      // �U���ɮ�
      try
      {
        // �إ�NetworkCredential����A�аѦ�4-5�`������
        // �]�w�Τ�ݺ����{�ҡA�h�ϥΪ̱b���αK�X
        NetworkCredential credentials = new NetworkCredential("anonymous", "test@microsoft.com");

        webclient.Credentials = credentials;

        // �۫��wURI�U����ơA���x�s���������ɮ�
        webclient.DownloadFile(uri, localfile);

        StatusBar.Text = "Download file from " + uri + " completed.";
        MessageBox.Show("Download file completed.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      }
      catch (WebException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }

      webclient.Dispose();
    }
  }
}