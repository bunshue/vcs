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
    bool isBusy;
    WebClient webclient;

    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // �إ�WebClient����
      webclient = new WebClient();

      // �ŧiDownloadFileAsync�D�P�B�U���ɮק����ɩ�Ĳ�o���ƥ�
      // �éw�q�ҩI�s����k��DownloadFileCompletedCallback
      webclient.DownloadFileCompleted += new AsyncCompletedEventHandler(DownloadFileCompletedCallback);

      // �ŧi�D�P�B�U���@�~���椤��Ĳ�o���ƥ�
      // �éw�q�ҩI�s����k��DownloadProgressChangedCallback
      webclient.DownloadProgressChanged += new DownloadProgressChangedEventHandler(DownloadProgressChangedCallback);

      isBusy = false;
      ProgressBar.Visible = false;
    }

    private void btnDownload_Click(object sender, EventArgs e)
    {
      if (isBusy)
      {
        // �����D�P�B�@�~
        webclient.CancelAsync();
        isBusy = false;
        ProgressBar.Visible = false;
        btnDownload.Text = "&Download";
      }
      else
      {
        try
        {
          string uriString = "";

          if (!txtURL.Text.StartsWith("http://"))
            uriString = "http://" + txtURL.Text;
          else
            uriString = txtURL.Text;

          Uri uri = new Uri(uriString);

          string localfile = uriString.Substring(uriString.LastIndexOf("/") + 1); ;

          // �]�wProgressBar
          ProgressBar.Visible = true;
          ProgressBar.Value = 0;
          isBusy = true;
          btnDownload.Text = "&Cancel";

          // �إ�NetworkCredential����A�аѦ�4-5�`������
          // �]�w�Τ�ݺ����{�ҡA�h�ϥΪ̱b���αK�X
          NetworkCredential credentials = new NetworkCredential("anonymous", "test@microsoft.com");

          webclient.Credentials = credentials;

          // �D�P�B�۫��wURI�U���ɮצܥ���
          webclient.DownloadFileAsync(uri, localfile);
        }
        catch (Exception ex)
        {
          MessageBox.Show(ex.StackTrace.ToString());
        }
      }
    }

    // �ۭq��k�A�D�P�B�U���ɮק����ɩҩI�s����k
    private void DownloadFileCompletedCallback(object sender, AsyncCompletedEventArgs e)
    {
      isBusy = false;
      btnDownload.Text = "&Download";

      if (e.Error == null)
        MessageBox.Show("Download file completed.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Information);
      else
        MessageBox.Show("Download file error.", "WebClient - HTTP Protocol", MessageBoxButtons.OK, MessageBoxIcon.Error);

      ProgressBar.Visible = false;
      webclient.Dispose();
    }

    private void DownloadProgressChangedCallback(object sender, DownloadProgressChangedEventArgs e)
    {
      // ���o�D�P�B�@�~���i�צʤ���
      // ���Ǧ�����ProgressBar������ܶi��
      ProgressBar.Value = e.ProgressPercentage;
    }
  }
}