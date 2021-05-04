using System;
using System.Linq;
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

      webBrowser.Navigate(new Uri("file://\\windows\\default.htm"));
    }

    private void txtURL_KeyPress(object sender, KeyPressEventArgs e)
    {
      // 若在txtURL按下Enter則瀏覽txtURL網頁
      if (e.KeyChar == (char)Keys.Return)
        webBrowser.Navigate(new Uri(txtURL.Text));
    }

    private void webBrowser_CanGoForwardChanged(object sender, EventArgs e)
    {
      // 當CanGoForward屬性值改變時所驅動之事件
      ToolBar1.Buttons[1].Enabled = webBrowser.CanGoForward;

      if (webBrowser.CanGoForward)
        ToolBarForward.ImageIndex = 1;
      else
        ToolBarForward.ImageIndex = 5;
    }

    private void webBrowser_CanGoBackChanged(object sender, EventArgs e)
    {
      // 當CanGoBack屬性值改變時所驅動之事件
      ToolBar1.Buttons[0].Enabled = webBrowser.CanGoBack;

      if (webBrowser.CanGoBack)
        ToolBarBack.ImageIndex = 0;
      else
        ToolBarBack.ImageIndex = 4;
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

    private void webBrowser_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
    {
      try
      {
        // 當完成網頁或文件載入時所驅動之事件
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
        // 若瀏覽下載完畢
        txtURL.Text = webBrowser.Url.ToString();
        StatusBar.Text = webBrowser.Url.ToString();
      }
      catch (NullReferenceException ex)
      {
        ex.StackTrace.ToString();
      }
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // 上一頁
          if (webBrowser.CanGoBack)
            webBrowser.GoBack();
          break;

        case 1:
          // 下一頁
          if (webBrowser.CanGoForward)
            webBrowser.GoForward();
          break;

        case 2:
          // 停止
          webBrowser.Stop();
          break;

        case 3:
          // 重新整理
          webBrowser.Refresh();
          break;
      }

      StatusBar.Text = webBrowser.Url.ToString();
    }

    private void mnuExit_Click(object sender, EventArgs e)
    {
      DialogResult result = MessageBox.Show("Are you sure to quit?", ".Net Compact - Web Browser", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button1);

      if (result == DialogResult.Yes)
      {
        this.Close();
      }
    }
  }
}