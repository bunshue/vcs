using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

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
      ToolBar1.Buttons[0].Enabled = false;
      ToolBar1.Buttons[1].Enabled = false;

      // ��CanGoBack�ݩʭȧ��ܮɩ�Ĳ�o���ƥ�
      //this.webBrowser.CanGoBackChanged += new System.EventHandler(this.webBrowser_CanGoBackChanged);

      // ��CanGoForward�ݩʭȧ��ܮɩ�Ĳ�o���ƥ�
      //this.webBrowser.CanGoForwardChanged += new System.EventHandler(this.webBrowser_CanGoForwardChanged);

      webBrowser.Navigate(new Uri("file://\\windows\\default.htm"));
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

        // .Net Compact Framework���䴩GoHome��k
        //case 4:
        //    // ����
        //    webBrowser.GoHome();
        //    break;

        // .Net Compact Framework���䴩GoSearch��k
        //case 5:
        //    // �j�M
        //    webBrowser.GoSearch();
        //    break;
      }

      StatusBar.Text = webBrowser.Url.ToString();
    }

    private void txtURL_KeyPress(object sender, KeyPressEventArgs e)
    {
      // �Y�btxtURL���UEnter�h�s��txtURL����
      if (e.KeyChar == (char)Keys.Return)
        webBrowser.Navigate(new Uri(txtURL.Text));

      // .Net Compact Framework���䴩Navigate(string urlString)��k
      // �Ȥ䴩:
      //    public void Navigate(Uri url)
      //    public void Navigate(Uri url, string targetFrameName)
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", ".Net Compact - Web Browser", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        this.Close();
      }
    }

    private void webBrowser_CanGoBackChanged(object sender, EventArgs e)
    {
      // ��CanGoBack�ݩʭȧ��ܮɩ��X�ʤ��ƥ�
      ToolBar1.Buttons[0].Enabled = webBrowser.CanGoBack;

      if (webBrowser.CanGoBack)
        ToolBarBack.ImageIndex = 0;
      else
        ToolBarBack.ImageIndex = 4;
    }

    private void webBrowser_CanGoForwardChanged(object sender, EventArgs e)
    {
      // ��CanGoForward�ݩʭȧ��ܮɩ��X�ʤ��ƥ�
      ToolBar1.Buttons[1].Enabled = webBrowser.CanGoForward;

      if (webBrowser.CanGoForward)
        ToolBarForward.ImageIndex = 1;
      else
        ToolBarForward.ImageIndex = 5;
    }

    private void webBrowser_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
    {
      try
      {
        // ���������Τ����J�ɩ��X�ʤ��ƥ�
        StatusBar.Text = webBrowser.Url.ToString();
      }
      catch (NullReferenceException ex)
      {
        ex.StackTrace.ToString();
      }
    }

    private void webBrowser_Navigated(object sender, WebBrowserNavigatedEventArgs e)
    {
      try
      {
        // �Y�s���U������
        txtURL.Text = webBrowser.Url.ToString();
        StatusBar.Text = webBrowser.Url.ToString();
      }
      catch (NullReferenceException ex)
      {
        ex.StackTrace.ToString();
      }
    }

    private void webBrowser_Navigating(object sender, WebBrowserNavigatingEventArgs e)
    {
      try
      {
        int index = e.Url.ToString().LastIndexOf("=");

        if (index != -1)
        {
          string Redirect = e.Url.ToString().Substring(index + 1);

          if (Redirect != "")
          {
            webBrowser.Navigate(new Uri(Redirect));
          }
          else
          {
            MessageBox.Show("Specify a URL");
          }
        }
      }
      catch (NullReferenceException ex)
      {
        ex.StackTrace.ToString();
      }
    }
  }
}