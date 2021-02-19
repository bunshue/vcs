using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser2
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
        webBrowser1.Navigate("C:\\");
    }

    private void Form1_Resize(object sender, EventArgs e)
    {
      Control control = (Control)sender;

      textBox1.Location = new System.Drawing.Point(44, 4);
      textBox1.Size = new System.Drawing.Size(control.Size.Width - 60, 22);
    }

    private void ToolBar1_ButtonClick(object sender, ToolBarButtonClickEventArgs e)
    {
      switch (ToolBar1.Buttons.IndexOf(e.Button))
      {
        case 0:
          // 上一頁
              if (webBrowser1.CanGoBack)
                  webBrowser1.GoBack();
          break;

        case 1:
          // 下一頁
          if (webBrowser1.CanGoForward)
              webBrowser1.GoForward();
          break;

        case 2:
          // 停止
          webBrowser1.Stop();
          break;

        case 3:
          // 重新整理
          webBrowser1.Refresh();
          break;

        case 4:
          // 首頁
          webBrowser1.GoHome();
          break;

        case 5:
          // 搜尋
          webBrowser1.GoSearch();
          break;
      }

      StatusBar1.Panels[0].Text = webBrowser1.Url.ToString();
    }

    private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
    {
        // 若在textBox1按下Enter則瀏覽textBox1網頁
      if (e.KeyChar == (char)Keys.Return)
          webBrowser1.Navigate(textBox1.Text);
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

    private void webBrowser1_Navigated(object sender, WebBrowserNavigatedEventArgs e)
    {
      // 若瀏覽下載完畢
        textBox1.Text = webBrowser1.Url.ToString();
        StatusBar1.Panels[0].Text = webBrowser1.Url.ToString();
    }
  }
}
