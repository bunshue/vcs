namespace Browser
{
  partial class Form1
  {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;
    private System.Windows.Forms.MainMenu mainMenu1;

    /// <summary>
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
      if (disposing && (components != null))
      {
        components.Dispose();
      }
      base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
      System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
      this.mainMenu1 = new System.Windows.Forms.MainMenu();
      this.menuItem1 = new System.Windows.Forms.MenuItem();
      this.mnuExit = new System.Windows.Forms.MenuItem();
      this.panel1 = new System.Windows.Forms.Panel();
      this.txtURL = new System.Windows.Forms.TextBox();
      this.label1 = new System.Windows.Forms.Label();
      this.StatusBar = new System.Windows.Forms.StatusBar();
      this.ToolBar1 = new System.Windows.Forms.ToolBar();
      this.ToolBarBack = new System.Windows.Forms.ToolBarButton();
      this.ToolBarForward = new System.Windows.Forms.ToolBarButton();
      this.ToolBarStop = new System.Windows.Forms.ToolBarButton();
      this.ImageList1 = new System.Windows.Forms.ImageList();
      this.webBrowser = new System.Windows.Forms.WebBrowser();
      this.ToolBarRefresh = new System.Windows.Forms.ToolBarButton();
      this.panel1.SuspendLayout();
      this.SuspendLayout();
      // 
      // mainMenu1
      // 
      this.mainMenu1.MenuItems.Add(this.menuItem1);
      // 
      // menuItem1
      // 
      this.menuItem1.MenuItems.Add(this.mnuExit);
      this.menuItem1.Text = "File";
      // 
      // mnuExit
      // 
      this.mnuExit.Text = "Exit";
      this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
      // 
      // panel1
      // 
      this.panel1.Controls.Add(this.txtURL);
      this.panel1.Controls.Add(this.label1);
      this.panel1.Dock = System.Windows.Forms.DockStyle.Top;
      this.panel1.Location = new System.Drawing.Point(0, 0);
      this.panel1.Name = "panel1";
      this.panel1.Size = new System.Drawing.Size(240, 31);
      // 
      // txtURL
      // 
      this.txtURL.Location = new System.Drawing.Point(36, 4);
      this.txtURL.Name = "txtURL";
      this.txtURL.Size = new System.Drawing.Size(201, 21);
      this.txtURL.TabIndex = 1;
      this.txtURL.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtURL_KeyPress);
      // 
      // label1
      // 
      this.label1.Location = new System.Drawing.Point(3, 4);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(50, 21);
      this.label1.Text = "URL:";
      // 
      // StatusBar
      // 
      this.StatusBar.Location = new System.Drawing.Point(0, 246);
      this.StatusBar.Name = "StatusBar";
      this.StatusBar.Size = new System.Drawing.Size(240, 22);
      // 
      // ToolBar1
      // 
      this.ToolBar1.Buttons.Add(this.ToolBarBack);
      this.ToolBar1.Buttons.Add(this.ToolBarForward);
      this.ToolBar1.Buttons.Add(this.ToolBarStop);
      this.ToolBar1.Buttons.Add(this.ToolBarRefresh);
      this.ToolBar1.ImageList = this.ImageList1;
      this.ToolBar1.Name = "ToolBar1";
      this.ToolBar1.ButtonClick += new System.Windows.Forms.ToolBarButtonClickEventHandler(this.ToolBar1_ButtonClick);
      // 
      // ToolBarBack
      // 
      this.ToolBarBack.ImageIndex = 0;
      // 
      // ToolBarForward
      // 
      this.ToolBarForward.ImageIndex = 1;
      // 
      // ToolBarStop
      // 
      this.ToolBarStop.ImageIndex = 2;
      this.ImageList1.Images.Clear();
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource"))));
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource1"))));
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource2"))));
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource3"))));
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource4"))));
      this.ImageList1.Images.Add(((System.Drawing.Image)(resources.GetObject("resource5"))));
      // 
      // webBrowser
      // 
      this.webBrowser.Dock = System.Windows.Forms.DockStyle.Fill;
      this.webBrowser.Location = new System.Drawing.Point(0, 31);
      this.webBrowser.Name = "webBrowser";
      this.webBrowser.Size = new System.Drawing.Size(240, 215);
      this.webBrowser.CanGoForwardChanged += new System.EventHandler(this.webBrowser_CanGoForwardChanged);
      this.webBrowser.CanGoBackChanged += new System.EventHandler(this.webBrowser_CanGoBackChanged);
      this.webBrowser.Navigating += new System.Windows.Forms.WebBrowserNavigatingEventHandler(this.webBrowser_Navigating);
      this.webBrowser.DocumentCompleted += new System.Windows.Forms.WebBrowserDocumentCompletedEventHandler(this.webBrowser_DocumentCompleted);
      this.webBrowser.Navigated += new System.Windows.Forms.WebBrowserNavigatedEventHandler(this.webBrowser_Navigated);
      // 
      // ToolBarRefresh
      // 
      this.ToolBarRefresh.ImageIndex = 3;
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(96F, 96F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
      this.AutoScroll = true;
      this.ClientSize = new System.Drawing.Size(240, 268);
      this.Controls.Add(this.webBrowser);
      this.Controls.Add(this.ToolBar1);
      this.Controls.Add(this.panel1);
      this.Controls.Add(this.StatusBar);
      this.Menu = this.mainMenu1;
      this.Name = "Form1";
      this.Text = ".Net Compact - Web Browser";
      this.Load += new System.EventHandler(this.Form1_Load);
      this.panel1.ResumeLayout(false);
      this.ResumeLayout(false);

    }

    #endregion

    private System.Windows.Forms.MenuItem menuItem1;
    private System.Windows.Forms.MenuItem mnuExit;
    private System.Windows.Forms.Panel panel1;
    private System.Windows.Forms.TextBox txtURL;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.StatusBar StatusBar;
    private System.Windows.Forms.ToolBar ToolBar1;
    private System.Windows.Forms.ToolBarButton ToolBarBack;
    private System.Windows.Forms.ToolBarButton ToolBarForward;
    private System.Windows.Forms.ToolBarButton ToolBarStop;
    private System.Windows.Forms.ImageList ImageList1;
    private System.Windows.Forms.WebBrowser webBrowser;
    private System.Windows.Forms.ToolBarButton ToolBarRefresh;
  }
}

