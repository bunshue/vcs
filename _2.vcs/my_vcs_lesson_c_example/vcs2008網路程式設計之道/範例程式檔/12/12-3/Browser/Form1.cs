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
      // 瀏覽 C: 磁碟機
      //webBrowser.Navigate("C:\\");

      ToolBar1.Buttons[0].Enabled = false;
      ToolBar1.Buttons[1].Enabled = false;

      // 當CanGoBack屬性值改變時所觸發之事件
      this.webBrowser.CanGoBackChanged += new System.EventHandler(this.webBrowser_CanGoBackChanged);

      // 當CanGoForward屬性值改變時所觸發之事件
      this.webBrowser.CanGoForwardChanged += new System.EventHandler(this.webBrowser_CanGoForwardChanged);

      // 當DocumentTitle屬性值改變時所觸發之事件
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

        case 4:
          // 首頁
          webBrowser.GoHome();
          break;

        case 5:
          // 搜尋
          webBrowser.GoSearch();
          break;
      }

      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void txtURL_KeyPress(object sender, KeyPressEventArgs e)
    {
      // 若在txtURL按下Enter則瀏覽txtURL網頁
      if (e.KeyChar == (char)Keys.Return)
        webBrowser.Navigate(txtURL.Text);
    }

    private void mnuCaption_Click(object sender, EventArgs e)
    {
      // 是否顯示文字標籤
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
      // 開啟檔案瀏覽
      OpenFileDialog1.Filter = "All Files (*.*)|*.*";
      OpenFileDialog1.Title = "Open";

      if (OpenFileDialog1.ShowDialog() == DialogResult.OK)
        webBrowser.Navigate(OpenFileDialog1.FileName);
    }

    private void mnuSaveAs_Click(object sender, EventArgs e)
    {
      // 另存新檔
      webBrowser.ShowSaveAsDialog();
    }

    private void mnuPageSetup_Click(object sender, EventArgs e)
    {
      // 設定列印格式
      webBrowser.ShowPageSetupDialog();
    }

    private void mnuPrint_Click(object sender, EventArgs e)
    {
      // 列印目前網頁並顯示列印對話盒
      webBrowser.ShowPrintDialog();
    }

    private void mnuPreview_Click(object sender, EventArgs e)
    {
      // 預覽列印
      webBrowser.ShowPrintPreviewDialog();
    }

    private void mnuProperties_Click(object sender, EventArgs e)
    {
      // 網頁內容
      webBrowser.ShowPropertiesDialog();
    }

    private void mnuSourceString_Click(object sender, EventArgs e)
    {
      Form2 frmSource = new Form2();

      // 取得網頁標題
      frmSource.Text = "Source Code: " + webBrowser.DocumentTitle;

      // 取得網頁HTML內容
      frmSource.txtSource.Text = webBrowser.DocumentText;
      frmSource.ShowDialog();
    }

    private void mnuSourceStream_Click(object sender, EventArgs e)
    {
      Form2 frmSource = new Form2();

      // 取得網頁標題
      frmSource.Text = "Source Code: " + webBrowser.DocumentTitle;

      // 取得網頁HTML內容的串流
      System.IO.Stream stream = webBrowser.DocumentStream;

      // 取得串流內容
      System.IO.StreamReader sr = new StreamReader(stream, Encoding.UTF8);

      string strBuff = "";
      char[] cbuffer = new char[256];
      int byteRead = 0;

      byteRead = sr.Read(cbuffer, 0, 256);

      while (byteRead != 0)
      {
        string strHtml = new string(cbuffer, 0, byteRead);

        strBuff = strBuff + strHtml;

        // 以StreamReader類別的Read方法
        // 依序讀取網頁原始程式碼每一行的內容至結束為止
        byteRead = sr.Read(cbuffer, 0, 256);
      }

      sr.Close();

      // 關閉資料串流
      stream.Close();

      frmSource.txtSource.Text = strBuff;
      frmSource.ShowDialog();
    }

    private void webBrowser_CanGoBackChanged(object sender, EventArgs e)
    {
      // 當CanGoBack屬性值改變時所驅動之事件
      ToolBar1.Buttons[0].Enabled = webBrowser.CanGoBack;
    }

    private void webBrowser_CanGoForwardChanged(object sender, EventArgs e)
    {
      // 當CanGoForward屬性值改變時所驅動之事件
      ToolBar1.Buttons[1].Enabled = webBrowser.CanGoForward;
    }

    private void webBrowser_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
    {
      // 當完成網頁或文件載入時所驅動之事件
      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void webBrowser_DocumentTitleChanged(object sender, EventArgs e)
    {
      // 當DocumentTitle屬性值改變時所驅動之事件
      this.Text = webBrowser.DocumentTitle;
    }

    private void webBrowser_Navigated(object sender, WebBrowserNavigatedEventArgs e)
    {
      // 若瀏覽下載完畢
      txtURL.Text = webBrowser.Url.ToString();
      StatusLabel.Text = webBrowser.Url.ToString();
    }

    private void webBrowser_ProgressChanged(object sender, WebBrowserProgressChangedEventArgs e)
    {
      // 取得所要載入文件的總位元組數目
      Progressbar.Maximum = (int)(e.MaximumProgress);
      // 取得已下載的位元組數目
      Progressbar.Value = (int)(e.CurrentProgress);
    }
  }
}
