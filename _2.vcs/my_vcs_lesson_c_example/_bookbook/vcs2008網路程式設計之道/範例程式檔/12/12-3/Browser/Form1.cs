using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace Browser
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Form1_Load(object sender, EventArgs e)
    {
      // �s�� C: �Ϻо�
      //webBrowser.Navigate("C:\\");

      ToolBar1.Buttons[0].Enabled = false;
      ToolBar1.Buttons[1].Enabled = false;

      // ��CanGoBack�ݩʭȧ��ܮɩ�Ĳ�o���ƥ�
      this.webBrowser.CanGoBackChanged += new System.EventHandler(this.webBrowser_CanGoBackChanged);

      // ��CanGoForward�ݩʭȧ��ܮɩ�Ĳ�o���ƥ�
      this.webBrowser.CanGoForwardChanged += new System.EventHandler(this.webBrowser_CanGoForwardChanged);

      // ��DocumentTitle�ݩʭȧ��ܮɩ�Ĳ�o���ƥ�
      this.webBrowser.DocumentTitleChanged += new System.EventHandler(this.webBrowser_DocumentTitleChanged);
    }

    private void Form1_Resize(object sender, EventArgs e)
    {
      Control control = (Control)sender;

      txtURL.Location = new System.Drawing.Point(44, 4);
      txtURL.Size = new System.Drawing.Size(control.Size.Width - 60, 22);
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // �W�@��
          if (webBrowser.CanGoBack)
            webBrowser.GoBack();
          break;

        case 1:
          // �U�@��
          if (webBrowser.CanGoForward)
            webBrowser.GoForward();
          break;

        case 2:
          // ����
          webBrowser.Stop();
          break;

        case 3:
          // ���s��z
          webBrowser.Refresh();
          break;

        case 4:
          // ����
          webBrowser.GoHome();
          break;

        case 5:
          // �j�M
          webBrowser.GoSearch();
          break;
      }

      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void txtURL_KeyPress(object sender, KeyPressEventArgs e)
    {
      // �Y�btxtURL���UEnter�h�s��txtURL����
      if (e.KeyChar == (char)Keys.Return)
        webBrowser.Navigate(txtURL.Text);
    }

    private void mnuCaption_Click(object sender, EventArgs e)
    {
      // �O�_��ܤ�r����
      mnuCaption.Checked = !mnuCaption.Checked;

      if (mnuCaption.Checked)
      {
        ToolBar1.Buttons[0].Text = "Back";
        ToolBar1.Buttons[1].Text = "Forward";
        ToolBar1.Buttons[2].Text = "Stop";
        ToolBar1.Buttons[3].Text = "Refresh";
        ToolBar1.Buttons[4].Text = "Home";
        ToolBar1.Buttons[5].Text = "Search";
        //ToolBar1.ButtonSize = new System.Drawing.Size(35, 35);
      }
      else
      {
        for (int i = 0; i <= 5; i++)
        {
          ToolBar1.Buttons[i].Text = "";
          //ToolBar1.ButtonSize = new System.Drawing.Size(20, 20);
        }
      }
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", "Web Browser", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
        this.Close();
    }

    private void mnuOpen_Click(object sender, EventArgs e)
    {
      // �}���ɮ��s��
      OpenFileDialog1.Filter = "All Files (*.*)|*.*";
      OpenFileDialog1.Title = "Open";

      if (OpenFileDialog1.ShowDialog() == DialogResult.OK)
        webBrowser.Navigate(OpenFileDialog1.FileName);
    }

    private void mnuSaveAs_Click(object sender, EventArgs e)
    {
      // �t�s�s��
      webBrowser.ShowSaveAsDialog();
    }

    private void mnuPageSetup_Click(object sender, EventArgs e)
    {
      // �]�w�C�L�榡
      webBrowser.ShowPageSetupDialog();
    }

    private void mnuPrint_Click(object sender, EventArgs e)
    {
      // �C�L�ثe��������ܦC�L��ܲ�
      webBrowser.ShowPrintDialog();
    }

    private void mnuPreview_Click(object sender, EventArgs e)
    {
      // �w���C�L
      webBrowser.ShowPrintPreviewDialog();
    }

    private void mnuProperties_Click(object sender, EventArgs e)
    {
      // �������e
      webBrowser.ShowPropertiesDialog();
    }

    private void mnuSourceString_Click(object sender, EventArgs e)
    {
      Form2 frmSource = new Form2();

      // ���o�������D
      frmSource.Text = "Source Code: " + webBrowser.DocumentTitle;

      // ���o����HTML���e
      frmSource.txtSource.Text = webBrowser.DocumentText;
      frmSource.ShowDialog();
    }

    private void mnuSourceStream_Click(object sender, EventArgs e)
    {
      Form2 frmSource = new Form2();

      // ���o�������D
      frmSource.Text = "Source Code: " + webBrowser.DocumentTitle;

      // ���o����HTML���e����y
      System.IO.Stream stream = webBrowser.DocumentStream;

      // ���o��y���e
      System.IO.StreamReader sr = new StreamReader(stream, Encoding.UTF8);

      string strBuff = "";
      char[] cbuffer = new char[256];
      int byteRead = 0;

      byteRead = sr.Read(cbuffer, 0, 256);

      while (byteRead != 0)
      {
        string strHtml = new string(cbuffer, 0, byteRead);

        strBuff = strBuff + strHtml;

        // �HStreamReader���O��Read��k
        // �̧�Ū��������l�{���X�C�@�檺���e�ܵ�������
        byteRead = sr.Read(cbuffer, 0, 256);
      }

      sr.Close();

      // ������Ʀ�y
      stream.Close();

      frmSource.txtSource.Text = strBuff;
      frmSource.ShowDialog();
    }

    private void webBrowser_CanGoBackChanged(object sender, EventArgs e)
    {
      // ��CanGoBack�ݩʭȧ��ܮɩ��X�ʤ��ƥ�
      ToolBar1.Buttons[0].Enabled = webBrowser.CanGoBack;
    }

    private void webBrowser_CanGoForwardChanged(object sender, EventArgs e)
    {
      // ��CanGoForward�ݩʭȧ��ܮɩ��X�ʤ��ƥ�
      ToolBar1.Buttons[1].Enabled = webBrowser.CanGoForward;
    }

    private void webBrowser_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
    {
      // ���������Τ����J�ɩ��X�ʤ��ƥ�
      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void webBrowser_DocumentTitleChanged(object sender, EventArgs e)
    {
      // ��DocumentTitle�ݩʭȧ��ܮɩ��X�ʤ��ƥ�
      this.Text = webBrowser.DocumentTitle;
    }

    private void webBrowser_Navigated(object sender, WebBrowserNavigatedEventArgs e)
    {
      // �Y�s���U������
      txtURL.Text = webBrowser.Url.ToString();
      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void webBrowser_ProgressChanged(object sender, WebBrowserProgressChangedEventArgs e)
    {
      // ���o�ҭn���J����`�줸�ռƥ�
      Progressbar.Maximum = (int)(e.MaximumProgress);
      // ���o�w�U�����줸�ռƥ�
      Progressbar.Value = (int)(e.CurrentProgress);
    }
  }
}
