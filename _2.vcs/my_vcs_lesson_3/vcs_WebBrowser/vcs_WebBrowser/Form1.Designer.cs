namespace vcs_WebBrowser
{
  partial class Form1
  {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

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
        this.components = new System.ComponentModel.Container();
        System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
        this.ToolBarBack = new System.Windows.Forms.ToolBarButton();
        this.ImageList1 = new System.Windows.Forms.ImageList(this.components);
        this.ToolBarStop = new System.Windows.Forms.ToolBarButton();
        this.ToolBarRefresh = new System.Windows.Forms.ToolBarButton();
        this.ToolBarSearch = new System.Windows.Forms.ToolBarButton();
        this.ToolBarHome = new System.Windows.Forms.ToolBarButton();
        this.StatusBar1 = new System.Windows.Forms.StatusBar();
        this.StatusBarPanel1 = new System.Windows.Forms.StatusBarPanel();
        this.ToolBar1 = new System.Windows.Forms.ToolBar();
        this.ToolBarForward = new System.Windows.Forms.ToolBarButton();
        this.MenuItem1 = new System.Windows.Forms.MenuItem();
        this.mnuExit = new System.Windows.Forms.MenuItem();
        this.mnuFile = new System.Windows.Forms.MenuItem();
        this.mnuCaption = new System.Windows.Forms.MenuItem();
        this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
        this.webBrowser1 = new System.Windows.Forms.WebBrowser();
        this.Panel1 = new System.Windows.Forms.Panel();
        this.textBox1 = new System.Windows.Forms.TextBox();
        this.Label1 = new System.Windows.Forms.Label();
        ((System.ComponentModel.ISupportInitialize)(this.StatusBarPanel1)).BeginInit();
        this.Panel1.SuspendLayout();
        this.SuspendLayout();
        // 
        // ToolBarBack
        // 
        this.ToolBarBack.ImageIndex = 0;
        this.ToolBarBack.Name = "ToolBarBack";
        this.ToolBarBack.Text = "Back";
        this.ToolBarBack.ToolTipText = "Back";
        // 
        // ImageList1
        // 
        this.ImageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("ImageList1.ImageStream")));
        this.ImageList1.TransparentColor = System.Drawing.Color.Transparent;
        this.ImageList1.Images.SetKeyName(0, "");
        this.ImageList1.Images.SetKeyName(1, "");
        this.ImageList1.Images.SetKeyName(2, "");
        this.ImageList1.Images.SetKeyName(3, "");
        this.ImageList1.Images.SetKeyName(4, "");
        this.ImageList1.Images.SetKeyName(5, "");
        // 
        // ToolBarStop
        // 
        this.ToolBarStop.ImageIndex = 2;
        this.ToolBarStop.Name = "ToolBarStop";
        this.ToolBarStop.Text = "Stop";
        this.ToolBarStop.ToolTipText = "Stop";
        // 
        // ToolBarRefresh
        // 
        this.ToolBarRefresh.ImageIndex = 3;
        this.ToolBarRefresh.Name = "ToolBarRefresh";
        this.ToolBarRefresh.Text = "Refresh";
        this.ToolBarRefresh.ToolTipText = "Refresh";
        // 
        // ToolBarSearch
        // 
        this.ToolBarSearch.ImageIndex = 5;
        this.ToolBarSearch.Name = "ToolBarSearch";
        this.ToolBarSearch.Text = "Search";
        this.ToolBarSearch.ToolTipText = "Search";
        // 
        // ToolBarHome
        // 
        this.ToolBarHome.ImageIndex = 4;
        this.ToolBarHome.Name = "ToolBarHome";
        this.ToolBarHome.Text = "Home";
        this.ToolBarHome.ToolTipText = "Home";
        // 
        // StatusBar1
        // 
        this.StatusBar1.Font = new System.Drawing.Font("·s²Ó©úÅé", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        this.StatusBar1.Location = new System.Drawing.Point(0, 610);
        this.StatusBar1.Name = "StatusBar1";
        this.StatusBar1.Panels.AddRange(new System.Windows.Forms.StatusBarPanel[] {
            this.StatusBarPanel1});
        this.StatusBar1.ShowPanels = true;
        this.StatusBar1.Size = new System.Drawing.Size(1038, 22);
        this.StatusBar1.TabIndex = 9;
        this.StatusBar1.Text = "Status:";
        // 
        // StatusBarPanel1
        // 
        this.StatusBarPanel1.AutoSize = System.Windows.Forms.StatusBarPanelAutoSize.Spring;
        this.StatusBarPanel1.Name = "StatusBarPanel1";
        this.StatusBarPanel1.Text = "Status: ";
        this.StatusBarPanel1.Width = 1021;
        // 
        // ToolBar1
        // 
        this.ToolBar1.Appearance = System.Windows.Forms.ToolBarAppearance.Flat;
        this.ToolBar1.Buttons.AddRange(new System.Windows.Forms.ToolBarButton[] {
            this.ToolBarBack,
            this.ToolBarForward,
            this.ToolBarStop,
            this.ToolBarRefresh,
            this.ToolBarHome,
            this.ToolBarSearch});
        this.ToolBar1.ButtonSize = new System.Drawing.Size(35, 35);
        this.ToolBar1.DropDownArrows = true;
        this.ToolBar1.ImageList = this.ImageList1;
        this.ToolBar1.Location = new System.Drawing.Point(0, 0);
        this.ToolBar1.Name = "ToolBar1";
        this.ToolBar1.ShowToolTips = true;
        this.ToolBar1.Size = new System.Drawing.Size(1038, 41);
        this.ToolBar1.TabIndex = 8;
        this.ToolBar1.ButtonClick += new System.Windows.Forms.ToolBarButtonClickEventHandler(this.ToolBar1_ButtonClick);
        // 
        // ToolBarForward
        // 
        this.ToolBarForward.ImageIndex = 1;
        this.ToolBarForward.Name = "ToolBarForward";
        this.ToolBarForward.Text = "Forward";
        this.ToolBarForward.ToolTipText = "Forward";
        // 
        // MenuItem1
        // 
        this.MenuItem1.Index = 1;
        this.MenuItem1.Text = "-";
        // 
        // mnuExit
        // 
        this.mnuExit.Index = 2;
        this.mnuExit.Text = "E&xit";
        this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
        // 
        // mnuFile
        // 
        this.mnuFile.Index = 0;
        this.mnuFile.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuCaption,
            this.MenuItem1,
            this.mnuExit});
        this.mnuFile.Text = "&File";
        // 
        // mnuCaption
        // 
        this.mnuCaption.Checked = true;
        this.mnuCaption.Index = 0;
        this.mnuCaption.Text = "&Show Caption";
        this.mnuCaption.Click += new System.EventHandler(this.mnuCaption_Click);
        // 
        // MainMenu1
        // 
        this.MainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuFile});
        // 
        // webBrowser1
        // 
        this.webBrowser1.Dock = System.Windows.Forms.DockStyle.Fill;
        this.webBrowser1.Location = new System.Drawing.Point(0, 71);
        this.webBrowser1.MinimumSize = new System.Drawing.Size(20, 20);
        this.webBrowser1.Name = "webBrowser1";
        this.webBrowser1.Size = new System.Drawing.Size(1038, 539);
        this.webBrowser1.TabIndex = 11;
        this.webBrowser1.Navigated += new System.Windows.Forms.WebBrowserNavigatedEventHandler(this.webBrowser1_Navigated);
        // 
        // Panel1
        // 
        this.Panel1.Controls.Add(this.textBox1);
        this.Panel1.Controls.Add(this.Label1);
        this.Panel1.Dock = System.Windows.Forms.DockStyle.Top;
        this.Panel1.Location = new System.Drawing.Point(0, 41);
        this.Panel1.Name = "Panel1";
        this.Panel1.Size = new System.Drawing.Size(1038, 30);
        this.Panel1.TabIndex = 10;
        // 
        // textBox1
        // 
        this.textBox1.Location = new System.Drawing.Point(44, 4);
        this.textBox1.Name = "textBox1";
        this.textBox1.Size = new System.Drawing.Size(982, 22);
        this.textBox1.TabIndex = 1;
        this.textBox1.WordWrap = false;
        this.textBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
        // 
        // Label1
        // 
        this.Label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
        this.Label1.Location = new System.Drawing.Point(10, 10);
        this.Label1.Name = "Label1";
        this.Label1.Size = new System.Drawing.Size(40, 15);
        this.Label1.TabIndex = 0;
        this.Label1.Text = "URL:";
        this.Label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
        // 
        // Form1
        // 
        this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(1038, 632);
        this.Controls.Add(this.webBrowser1);
        this.Controls.Add(this.Panel1);
        this.Controls.Add(this.StatusBar1);
        this.Controls.Add(this.ToolBar1);
        this.Menu = this.MainMenu1;
        this.Name = "Form1";
        this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
        this.Text = "Web Browser";
        this.Load += new System.EventHandler(this.Form1_Load);
        this.Resize += new System.EventHandler(this.Form1_Resize);
        ((System.ComponentModel.ISupportInitialize)(this.StatusBarPanel1)).EndInit();
        this.Panel1.ResumeLayout(false);
        this.Panel1.PerformLayout();
        this.ResumeLayout(false);
        this.PerformLayout();

    }

    #endregion

    internal System.Windows.Forms.ToolBarButton ToolBarBack;
    internal System.Windows.Forms.ImageList ImageList1;
    internal System.Windows.Forms.ToolBarButton ToolBarStop;
    internal System.Windows.Forms.ToolBarButton ToolBarRefresh;
    internal System.Windows.Forms.ToolBarButton ToolBarSearch;
    internal System.Windows.Forms.ToolBarButton ToolBarHome;
    internal System.Windows.Forms.StatusBar StatusBar1;
    internal System.Windows.Forms.StatusBarPanel StatusBarPanel1;
    internal System.Windows.Forms.ToolBar ToolBar1;
    internal System.Windows.Forms.ToolBarButton ToolBarForward;
    internal System.Windows.Forms.MenuItem MenuItem1;
    internal System.Windows.Forms.MenuItem mnuExit;
    internal System.Windows.Forms.MenuItem mnuFile;
    internal System.Windows.Forms.MenuItem mnuCaption;
    internal System.Windows.Forms.MainMenu MainMenu1;
    internal System.Windows.Forms.WebBrowser webBrowser1;
    internal System.Windows.Forms.Panel Panel1;
    internal System.Windows.Forms.TextBox textBox1;
    internal System.Windows.Forms.Label Label1;
  }
}

