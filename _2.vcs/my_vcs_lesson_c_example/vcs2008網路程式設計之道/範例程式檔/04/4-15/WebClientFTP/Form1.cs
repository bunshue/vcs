using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;

namespace WebClientFTP
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnSelect_Click(object sender, EventArgs e)
    {
      saveFileDialog1.Filter = "All files (*.*)|*.*";
      saveFileDialog1.OverwritePrompt = false;
      saveFileDialog1.Title = "Select File";

      if (saveFileDialog1.ShowDialog() == DialogResult.OK)
        txtLocal.Text = saveFileDialog1.FileName;
    }

    private void btnDownloadFile_Click(object sender, EventArgs e)
    {
      string address = "";
      string remotefile = "";
      string localfile = "";

      if (!txtURL.Text.StartsWith("ftp://"))
        address = "ftp://" + txtURL.Text;
      else
        address = txtURL.Text;

      if (!address.Trim().EndsWith("/"))
        address = address + "/";

      if (txtRemote.Text == "")
      {
        MessageBox.Show("Please input the remote file name to be downloaded.", "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Error);

        return;
      }
      else
        remotefile = txtRemote.Text;

      string uri = address + remotefile;

      if (txtLocal.Text != "")
        localfile = txtLocal.Text;
      else
      {
        localfile = remotefile;
        txtLocal.Text = localfile;
      }

      StatusBar.Text = "Downloading file from " + uri;

      // �إ�WebClient����
      WebClient webclient = new WebClient();

      // �U���ɮ�
      try
      {
        // �إ�NetworkCredential����A�аѦ�4-5�`������
        // �]�w�Τ�ݺ����{�ҡA�h�ϥΪ̱b���αK�X
        NetworkCredential credentials = new NetworkCredential(txtLogin.Text, txtPassword.Text);

        webclient.Credentials = credentials;

        // �۫��wURI�U����ơA���x�s���������ɮ�
        webclient.DownloadFile(uri, localfile);

        StatusBar.Text = "Download file from " + uri + " completed.";
        MessageBox.Show("Download file completed.", "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      }
      catch (WebException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }

      webclient.Dispose();
    }

    private void btnUploadFile_Click(object sender, EventArgs e)
    {
      string address = "";
      string remotefile = "";
      string localfile = "";

      if (!txtURL.Text.StartsWith("ftp://"))
        address = "ftp://" + txtURL.Text;
      else
        address = txtURL.Text;

      if (!address.Trim().EndsWith("/"))
        address = address + "/";

      if (txtLocal.Text == "")
      {
        MessageBox.Show("Please input the local file name to be uploaded.",
            "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Error);

        return;
      }
      else
        localfile = txtLocal.Text;

      if (txtRemote.Text != "")
        remotefile = txtRemote.Text;
      else
      {
        remotefile = localfile.Substring(localfile.LastIndexOf("\\") + 1);

        txtRemote.Text = remotefile;
      }

      string uri = address + remotefile;

      StatusBar.Text = "Uploading file to " + uri;

      // �إ�WebClient����
      WebClient webclient = new WebClient();

      // �W���ɮ�
      try
      {
        // �إ�NetworkCredential����A�аѦ�4-5�`������
        NetworkCredential credentials = new NetworkCredential(txtLogin.Text, txtPassword.Text);

        // �]�w�Τ�ݺ����{���ҡA�h�ϥΪ̱b���αK�X
        webclient.Credentials = credentials;

        // �W���ɮצܫ��w��URI
        byte[] response = webclient.UploadFile(uri, WebRequestMethods.Ftp.UploadFile, localfile);

        string msg;

        if (response.Length == 0)
          msg = "null";
        else
          msg = Encoding.UTF8.GetString(response);

        StatusBar.Text = "Upload file to " + uri + " completed.";
        MessageBox.Show("Upload file completed.\r\nResponse: " + msg, "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      }
      catch (WebException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }

      webclient.Dispose();
    }

    private void btnUploadData_Click(object sender, EventArgs e)
    {
      string address = "";
      string remotefile = "";

      if (!txtURL.Text.StartsWith("ftp://"))
        address = "ftp://" + txtURL.Text;
      else
        address = txtURL.Text;

      if (!address.Trim().EndsWith("/"))
        address = address + "/";

      if (txtRemote.Text == "")
      {
        MessageBox.Show("Please input the remote file name to be uploaded.", "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Error);

        return;
      }
      else
        remotefile = txtRemote.Text;

      string uri = address + remotefile;

      StatusBar.Text = "Uploading data to " + uri;

      // �إ�WebClient����
      WebClient webclient = new WebClient();

      // �W�Ǹ��
      try
      {
        // �إ�NetworkCredential����A�аѦ�4-5�`������
        NetworkCredential credentials = new NetworkCredential(txtLogin.Text, txtPassword.Text);

        // �]�w�Τ�ݺ����{���ҡA�h�ϥΪ̱b���αK�X
        webclient.Credentials = credentials;

        // ���W�Ǥ���ơA���줸�}�C�Φ�
        byte[] data = Encoding.ASCII.GetBytes(txtData.Text);

        // �W�Ǹ�Ʀܫ��w��URI
        byte[] response = webclient.UploadData(uri, WebRequestMethods.Ftp.UploadFile, data);

        string msg;

        if (response.Length == 0)
          msg = "null";
        else
          msg = Encoding.UTF8.GetString(response);

        StatusBar.Text = "Upload data to " + uri + " completed.";
        MessageBox.Show("Upload data completed.\r\nResponse: " + msg, "WebClient - FTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      }
      catch (WebException ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }

      webclient.Dispose();
    }
  }
}