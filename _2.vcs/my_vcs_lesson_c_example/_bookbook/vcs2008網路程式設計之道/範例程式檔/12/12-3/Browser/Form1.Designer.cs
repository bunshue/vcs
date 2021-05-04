namespace Browser
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
          this.ToolBar1 = new System.Windows.Forms.ToolBar();
          this.ToolBarForward = new System.Windows.Forms.ToolBarButton();
          this.Panel1 = new System.Windows.Forms.Panel();
          this.txtURL = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
          this.mnuFile = new System.Windows.Forms.MenuItem();
          this.mnuOpen = new System.Windows.Forms.MenuItem();
          this.mnuCaption = new System.Windows.Forms.MenuItem();
          this.mnuSaveAs = new System.Windows.Forms.MenuItem();
          this.MenuItem1 = new System.Windows.Forms.MenuItem();
          this.mnuPageSetup = new System.Windows.Forms.MenuItem();
          this.mnuPrint = new System.Windows.Forms.MenuItem();
          this.mnuPreview = new System.Windows.Forms.MenuItem();
          this.MenuItem3 = new System.Windows.Forms.MenuItem();
          this.mnuProperties = new System.Windows.Forms.MenuItem();
          this.MenuItem2 = new System.Windows.Forms.MenuItem();
          this.mnuExit = new System.Windows.Forms.MenuItem();
          this.mnuView = new System.Windows.Forms.MenuItem();
          this.mnuSourceString = new System.Windows.Forms.MenuItem();
          this.mnuSourceStream = new System.Windows.Forms.MenuItem();
          this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
          this.StatusStrip1 = new System.Windows.Forms.StatusStrip();
          this.StatusLabel = new System.Windows.Forms.ToolStripStatusLabel();
          this.Progressbar = new System.Windows.Forms.ToolStripProgressBar();
          this.webBrowser = new System.Windows.Forms.WebBrowser();
          this.Panel1.SuspendLayout();
          this.StatusStrip1.SuspendLayout();
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
          this.ToolBar1.Size = new System.Drawing.Size(329, 41);
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
          // Panel1
          // 
          this.Panel1.Controls.Add(this.txtURL);
          this.Panel1.Controls.Add(this.Label1);
          this.Panel1.Dock = System.Windows.Forms.DockStyle.Top;
          this.Panel1.Location = new System.Drawing.Point(0, 41);
          this.Panel1.Name = "Panel1";
          this.Panel1.Size = new System.Drawing.Size(329, 30);
          this.Panel1.TabIndex = 10;
          // 
          // txtURL
          // 
          this.txtURL.Location = new System.Drawing.Point(44, 4);
          this.txtURL.Name = "txtURL";
          this.txtURL.Size = new System.Drawing.Size(278, 22);
          this.txtURL.TabIndex = 1;
          this.txtURL.WordWrap = false;
          this.txtURL.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtURL_KeyPress);
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
          // MainMenu1
          // 
          this.MainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuFile,
            this.mnuView});
          // 
          // mnuFile
          // 
          this.mnuFile.Index = 0;
          this.mnuFile.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuOpen,
            this.mnuCaption,
            this.mnuSaveAs,
            this.MenuItem1,
            this.mnuPageSetup,
            this.mnuPrint,
            this.mnuPreview,
            this.MenuItem3,
            this.mnuProperties,
            this.MenuItem2,
            this.mnuExit});
          this.mnuFile.Text = "&File";
          // 
          // mnuOpen
          // 
          this.mnuOpen.Index = 0;
          this.mnuOpen.Text = "&Open";
          this.mnuOpen.Click += new System.EventHandler(this.mnuOpen_Click);
          // 
          // mnuCaption
          // 
          this.mnuCaption.Checked = true;
          this.mnuCaption.Index = 1;
          this.mnuCaption.Text = "&Show Caption";
          this.mnuCaption.Click += new System.EventHandler(this.mnuCaption_Click);
          // 
          // mnuSaveAs
          // 
          this.mnuSaveAs.Index = 2;
          this.mnuSaveAs.Text = "Save &As ...";
          this.mnuSaveAs.Click += new System.EventHandler(this.mnuSaveAs_Click);
          // 
          // MenuItem1
          // 
          this.MenuItem1.Index = 3;
          this.MenuItem1.Text = "-";
          // 
          // mnuPageSetup
          // 
          this.mnuPageSetup.Index = 4;
          this.mnuPageSetup.Text = "Page Set&up";
          this.mnuPageSetup.Click += new System.EventHandler(this.mnuPageSetup_Click);
          // 
          // mnuPrint
          // 
          this.mnuPrint.Index = 5;
          this.mnuPrint.Text = "&Print";
          this.mnuPrint.Click += new System.EventHandler(this.mnuPrint_Click);
          // 
          // mnuPreview
          // 
          this.mnuPreview.Index = 6;
          this.mnuPreview.Text = "Print Pre&view";
          this.mnuPreview.Click += new System.EventHandler(this.mnuPreview_Click);
          // 
          // MenuItem3
          // 
          this.MenuItem3.Index = 7;
          this.MenuItem3.Text = "-";
          // 
          // mnuProperties
          // 
          this.mnuProperties.Index = 8;
          this.mnuProperties.Text = "P&roperties";
          this.mnuProperties.Click += new System.EventHandler(this.mnuProperties_Click);
          // 
          // MenuItem2
          // 
          this.MenuItem2.Index = 9;
          this.MenuItem2.Text = "-";
          // 
          // mnuExit
          // 
          this.mnuExit.Index = 10;
          this.mnuExit.Text = "E&xit";
          this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
          // 
          // mnuView
          // 
          this.mnuView.Index = 1;
          this.mnuView.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuSourceString,
            this.mnuSourceStream});
          this.mnuView.Text = "&View";
          // 
          // mnuSourceString
          // 
          this.mnuSourceString.Index = 0;
          this.mnuSourceString.Text = "Source (String)";
          this.mnuSourceString.Click += new System.EventHandler(this.mnuSourceString_Click);
          // 
          // mnuSourceStream
          // 
          this.mnuSourceStream.Index = 1;
          this.mnuSourceStream.Text = "Source (Stream)";
          this.mnuSourceStream.Click += new System.EventHandler(this.mnuSourceStream_Click);
          // 
          // StatusStrip1
          // 
          this.StatusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.StatusLabel,
            this.Progressbar});
          this.StatusStrip1.Location = new System.Drawing.Point(0, 270);
          this.StatusStrip1.Name = "StatusStrip1";
          this.StatusStrip1.Size = new System.Drawing.Size(329, 22);
          this.StatusStrip1.TabIndex = 12;
          this.StatusStrip1.Text = "statusStrip1";
          // 
          // StatusLabel
          // 
          this.StatusLabel.Name = "StatusLabel";
          this.StatusLabel.Size = new System.Drawing.Size(212, 17);
          this.StatusLabel.Spring = true;
          this.StatusLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
          // 
          // Progressbar
          // 
          this.Progressbar.Name = "Progressbar";
          this.Progressbar.Size = new System.Drawing.Size(100, 16);
          // 
          // webBrowser
          // 
          this.webBrowser.Dock = System.Windows.Forms.DockStyle.Fill;
          this.webBrowser.Location = new System.Drawing.Point(0, 71);
          this.webBrowser.MinimumSize = new System.Drawing.Size(20, 20);
          this.webBrowser.Name = "webBrowser";
          this.webBrowser.Size = new System.Drawing.Size(329, 199);
          this.webBrowser.TabIndex = 13;
          this.webBrowser.ProgressChanged += new System.Windows.Forms.WebBrowserProgressChangedEventHandler(this.webBrowser_ProgressChanged);
          this.webBrowser.DocumentCompleted += new System.Windows.Forms.WebBrowserDocumentCompletedEventHandler(this.webBrowser_DocumentCompleted);
          this.webBrowser.Navigated += new System.Windows.Forms.WebBrowserNavigatedEventHandler(this.webBrowser_Navigated);
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(329, 292);
          this.Controls.Add(this.webBrowser);
          this.Controls.Add(this.StatusStrip1);
          this.Controls.Add(this.Panel1);
          this.Controls.Add(this.ToolBar1);
          this.Menu = this.MainMenu1;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "Web Browser";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.Resize += new System.EventHandler(this.Form1_Resize);
          this.Panel1.ResumeLayout(false);
          this.Panel1.PerformLayout();
          this.StatusStrip1.ResumeLayout(false);
          this.StatusStrip1.PerformLayout();
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
        internal System.Windows.Forms.ToolBar ToolBar1;
        internal System.Windows.Forms.ToolBarButton ToolBarForward;
        internal System.Windows.Forms.Panel Panel1;
        internal System.Windows.Forms.TextBox txtURL;
        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.MainMenu MainMenu1;
        internal System.Windows.Forms.MenuItem mnuFile;
        internal System.Windows.Forms.MenuItem mnuOpen;
        internal System.Windows.Forms.MenuItem mnuCaption;
        internal System.Windows.Forms.MenuItem mnuSaveAs;
        internal System.Windows.Forms.MenuItem MenuItem1;
        internal System.Windows.Forms.MenuItem mnuPageSetup;
        internal System.Windows.Forms.MenuItem mnuPrint;
        internal System.Windows.Forms.MenuItem mnuPreview;
        internal System.Windows.Forms.MenuItem MenuItem3;
        internal System.Windows.Forms.MenuItem mnuProperties;
        internal System.Windows.Forms.MenuItem MenuItem2;
        internal System.Windows.Forms.MenuItem mnuExit;
        internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
        private System.Windows.Forms.MenuItem mnuView;
        private System.Windows.Forms.MenuItem mnuSourceString;
        private System.Windows.Forms.MenuItem mnuSourceStream;
        private System.Windows.Forms.StatusStrip StatusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel StatusLabel;
        private System.Windows.Forms.ToolStripProgressBar Progressbar;
        private System.Windows.Forms.WebBrowser webBrowser;
    }
}

