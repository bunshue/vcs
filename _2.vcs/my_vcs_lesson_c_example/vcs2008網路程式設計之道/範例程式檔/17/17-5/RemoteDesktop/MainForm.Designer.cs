namespace RemoteDesktop
{
    partial class MainForm
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
          System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
          this.mainMenu1 = new System.Windows.Forms.MainMenu(this.components);
          this.mnuFile = new System.Windows.Forms.MenuItem();
          this.mnuSlave = new System.Windows.Forms.MenuItem();
          this.mnuSlaveStart = new System.Windows.Forms.MenuItem();
          this.mnuSlaveStop = new System.Windows.Forms.MenuItem();
          this.mnuMaster = new System.Windows.Forms.MenuItem();
          this.mnuMasterStart = new System.Windows.Forms.MenuItem();
          this.mnuMasterStop = new System.Windows.Forms.MenuItem();
          this.menuItem10 = new System.Windows.Forms.MenuItem();
          this.mnuExit = new System.Windows.Forms.MenuItem();
          this.mnuView = new System.Windows.Forms.MenuItem();
          this.mnuNormal = new System.Windows.Forms.MenuItem();
          this.mnuFull = new System.Windows.Forms.MenuItem();
          this.desktopPicture = new System.Windows.Forms.PictureBox();
          this.timer1 = new System.Windows.Forms.Timer(this.components);
          this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
          this.contextMenu1 = new System.Windows.Forms.ContextMenu();
          this.mnuSlaveStop1 = new System.Windows.Forms.MenuItem();
          this.menuItem1 = new System.Windows.Forms.MenuItem();
          this.mnuExit1 = new System.Windows.Forms.MenuItem();
          ((System.ComponentModel.ISupportInitialize)(this.desktopPicture)).BeginInit();
          this.SuspendLayout();
          // 
          // mainMenu1
          // 
          this.mainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuFile,
            this.mnuView});
          // 
          // mnuFile
          // 
          this.mnuFile.Index = 0;
          this.mnuFile.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuSlave,
            this.mnuMaster,
            this.menuItem10,
            this.mnuExit});
          this.mnuFile.Text = "&File";
          // 
          // mnuSlave
          // 
          this.mnuSlave.Index = 0;
          this.mnuSlave.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuSlaveStart,
            this.mnuSlaveStop});
          this.mnuSlave.Text = "³Q±±ºÝ";
          // 
          // mnuSlaveStart
          // 
          this.mnuSlaveStart.Index = 0;
          this.mnuSlaveStart.Text = "Start";
          this.mnuSlaveStart.Click += new System.EventHandler(this.mnuSlaveStart_Click);
          // 
          // mnuSlaveStop
          // 
          this.mnuSlaveStop.Enabled = false;
          this.mnuSlaveStop.Index = 1;
          this.mnuSlaveStop.Text = "Stop";
          this.mnuSlaveStop.Click += new System.EventHandler(this.mnuSlaveStop_Click);
          // 
          // mnuMaster
          // 
          this.mnuMaster.Index = 1;
          this.mnuMaster.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuMasterStart,
            this.mnuMasterStop});
          this.mnuMaster.Text = "±±¨îºÝ";
          // 
          // mnuMasterStart
          // 
          this.mnuMasterStart.Index = 0;
          this.mnuMasterStart.Text = "Start";
          this.mnuMasterStart.Click += new System.EventHandler(this.mnuMasterStart_Click);
          // 
          // mnuMasterStop
          // 
          this.mnuMasterStop.Enabled = false;
          this.mnuMasterStop.Index = 1;
          this.mnuMasterStop.Text = "Stop";
          this.mnuMasterStop.Click += new System.EventHandler(this.mnuMasterStop_Click);
          // 
          // menuItem10
          // 
          this.menuItem10.Index = 2;
          this.menuItem10.Text = "-";
          // 
          // mnuExit
          // 
          this.mnuExit.Index = 3;
          this.mnuExit.Text = "E&xit";
          this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
          // 
          // mnuView
          // 
          this.mnuView.Index = 1;
          this.mnuView.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuNormal,
            this.mnuFull});
          this.mnuView.Text = "&View";
          this.mnuView.Visible = false;
          // 
          // mnuNormal
          // 
          this.mnuNormal.Index = 0;
          this.mnuNormal.Shortcut = System.Windows.Forms.Shortcut.CtrlZ;
          this.mnuNormal.Text = "&Normal Size";
          this.mnuNormal.Click += new System.EventHandler(this.mnuNormal_Click);
          // 
          // mnuFull
          // 
          this.mnuFull.Index = 1;
          this.mnuFull.Shortcut = System.Windows.Forms.Shortcut.CtrlF;
          this.mnuFull.Text = "&Full Screen";
          this.mnuFull.Click += new System.EventHandler(this.mnuFull_Click);
          // 
          // desktopPicture
          // 
          this.desktopPicture.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
          this.desktopPicture.Dock = System.Windows.Forms.DockStyle.Fill;
          this.desktopPicture.Location = new System.Drawing.Point(0, 0);
          this.desktopPicture.Name = "desktopPicture";
          this.desktopPicture.Size = new System.Drawing.Size(634, 435);
          this.desktopPicture.TabIndex = 0;
          this.desktopPicture.TabStop = false;
          this.desktopPicture.MouseMove += new System.Windows.Forms.MouseEventHandler(this.desktopPicture_MouseMove);
          this.desktopPicture.MouseDown += new System.Windows.Forms.MouseEventHandler(this.desktopPicture_MouseDown);
          this.desktopPicture.MouseUp += new System.Windows.Forms.MouseEventHandler(this.desktopPicture_MouseUp);
          // 
          // timer1
          // 
          this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
          // 
          // notifyIcon1
          // 
          this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject("notifyIcon1.Icon")));
          this.notifyIcon1.Text = "Remote Desktop - ³Q±±ºÝ";
          // 
          // contextMenu1
          // 
          this.contextMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuSlaveStop1,
            this.menuItem1,
            this.mnuExit1});
          // 
          // mnuSlaveStop1
          // 
          this.mnuSlaveStop1.Index = 0;
          this.mnuSlaveStop1.Text = "Stop";
          this.mnuSlaveStop1.Click += new System.EventHandler(this.mnuSlaveStop1_Click);
          // 
          // menuItem1
          // 
          this.menuItem1.Index = 1;
          this.menuItem1.Text = "-";
          // 
          // mnuExit1
          // 
          this.mnuExit1.Index = 2;
          this.mnuExit1.Text = "Exit";
          this.mnuExit1.Click += new System.EventHandler(this.mnuExit_Click);
          // 
          // MainForm
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(634, 435);
          this.Controls.Add(this.desktopPicture);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
          this.MaximizeBox = false;
          this.Menu = this.mainMenu1;
          this.Name = "MainForm";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "Remote Desktop";
          this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
          ((System.ComponentModel.ISupportInitialize)(this.desktopPicture)).EndInit();
          this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.MainMenu mainMenu1;
        private System.Windows.Forms.MenuItem mnuView;
        private System.Windows.Forms.MenuItem mnuFull;
        private System.Windows.Forms.MenuItem mnuNormal;
        private System.Windows.Forms.MenuItem mnuFile;
        private System.Windows.Forms.MenuItem mnuSlave;
        private System.Windows.Forms.PictureBox desktopPicture;
        private System.Windows.Forms.MenuItem mnuMaster;
        private System.Windows.Forms.MenuItem menuItem10;
        private System.Windows.Forms.MenuItem mnuExit;
        private System.Windows.Forms.MenuItem mnuSlaveStart;
        private System.Windows.Forms.MenuItem mnuSlaveStop;
        private System.Windows.Forms.MenuItem mnuMasterStart;
        private System.Windows.Forms.MenuItem mnuMasterStop;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.NotifyIcon notifyIcon1;
        private System.Windows.Forms.ContextMenu contextMenu1;
        private System.Windows.Forms.MenuItem mnuSlaveStop1;
        private System.Windows.Forms.MenuItem menuItem1;
        private System.Windows.Forms.MenuItem mnuExit1;
    }
}

