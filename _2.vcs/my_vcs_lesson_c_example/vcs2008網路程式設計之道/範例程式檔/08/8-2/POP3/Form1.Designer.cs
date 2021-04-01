namespace POP3
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
          this.txtPass = new System.Windows.Forms.TextBox();
          this.label6 = new System.Windows.Forms.Label();
          this.txtPort = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.tabPage2 = new System.Windows.Forms.TabPage();
          this.panel3 = new System.Windows.Forms.Panel();
          this.label5 = new System.Windows.Forms.Label();
          this.txtLogin = new System.Windows.Forms.TextBox();
          this.label3 = new System.Windows.Forms.Label();
          this.txtHost = new System.Windows.Forms.TextBox();
          this.label4 = new System.Windows.Forms.Label();
          this.tabPage3 = new System.Windows.Forms.TabPage();
          this.lstLog = new System.Windows.Forms.ListBox();
          this.Panel1 = new System.Windows.Forms.Panel();
          this.btnPrevious = new System.Windows.Forms.ToolBarButton();
          this.btnNext = new System.Windows.Forms.ToolBarButton();
          this.btnClear = new System.Windows.Forms.ToolBarButton();
          this.ImageList1 = new System.Windows.Forms.ImageList(this.components);
          this.ToolBar1 = new System.Windows.Forms.ToolBar();
          this.btnReceive = new System.Windows.Forms.ToolBarButton();
          this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
          this.MenuItem1 = new System.Windows.Forms.MenuItem();
          this.mnuExit = new System.Windows.Forms.MenuItem();
          this.tabPage1 = new System.Windows.Forms.TabPage();
          this.Panel2 = new System.Windows.Forms.Panel();
          this.txtMessage = new System.Windows.Forms.TextBox();
          this.TabControl1 = new System.Windows.Forms.TabControl();
          this.tabPage2.SuspendLayout();
          this.panel3.SuspendLayout();
          this.tabPage3.SuspendLayout();
          this.Panel1.SuspendLayout();
          this.tabPage1.SuspendLayout();
          this.Panel2.SuspendLayout();
          this.TabControl1.SuspendLayout();
          this.SuspendLayout();
          // 
          // txtPass
          // 
          this.txtPass.Location = new System.Drawing.Point(72, 86);
          this.txtPass.Name = "txtPass";
          this.txtPass.PasswordChar = '*';
          this.txtPass.Size = new System.Drawing.Size(192, 22);
          this.txtPass.TabIndex = 3;
          // 
          // label6
          // 
          this.label6.Location = new System.Drawing.Point(8, 91);
          this.label6.Name = "label6";
          this.label6.Size = new System.Drawing.Size(68, 15);
          this.label6.TabIndex = 7;
          this.label6.Text = "Password:";
          // 
          // txtPort
          // 
          this.txtPort.Location = new System.Drawing.Point(72, 32);
          this.txtPort.Name = "txtPort";
          this.txtPort.Size = new System.Drawing.Size(192, 22);
          this.txtPort.TabIndex = 1;
          // 
          // Label1
          // 
          this.Label1.Location = new System.Drawing.Point(8, 10);
          this.Label1.Name = "Label1";
          this.Label1.Size = new System.Drawing.Size(256, 15);
          this.Label1.TabIndex = 0;
          this.Label1.Text = "Message:";
          // 
          // tabPage2
          // 
          this.tabPage2.Controls.Add(this.panel3);
          this.tabPage2.Location = new System.Drawing.Point(4, 21);
          this.tabPage2.Name = "tabPage2";
          this.tabPage2.Size = new System.Drawing.Size(284, 239);
          this.tabPage2.TabIndex = 1;
          this.tabPage2.Text = "POP3";
          // 
          // panel3
          // 
          this.panel3.Controls.Add(this.txtPass);
          this.panel3.Controls.Add(this.label6);
          this.panel3.Controls.Add(this.txtPort);
          this.panel3.Controls.Add(this.label5);
          this.panel3.Controls.Add(this.txtLogin);
          this.panel3.Controls.Add(this.label3);
          this.panel3.Controls.Add(this.txtHost);
          this.panel3.Controls.Add(this.label4);
          this.panel3.Dock = System.Windows.Forms.DockStyle.Top;
          this.panel3.Location = new System.Drawing.Point(0, 0);
          this.panel3.Name = "panel3";
          this.panel3.Size = new System.Drawing.Size(284, 116);
          this.panel3.TabIndex = 1;
          // 
          // label5
          // 
          this.label5.Location = new System.Drawing.Point(8, 37);
          this.label5.Name = "label5";
          this.label5.Size = new System.Drawing.Size(68, 15);
          this.label5.TabIndex = 5;
          this.label5.Text = "Port:";
          // 
          // txtLogin
          // 
          this.txtLogin.Location = new System.Drawing.Point(72, 59);
          this.txtLogin.Name = "txtLogin";
          this.txtLogin.Size = new System.Drawing.Size(192, 22);
          this.txtLogin.TabIndex = 2;
          // 
          // label3
          // 
          this.label3.Location = new System.Drawing.Point(8, 64);
          this.label3.Name = "label3";
          this.label3.Size = new System.Drawing.Size(68, 15);
          this.label3.TabIndex = 3;
          this.label3.Text = "Login:";
          // 
          // txtHost
          // 
          this.txtHost.Location = new System.Drawing.Point(72, 5);
          this.txtHost.Name = "txtHost";
          this.txtHost.Size = new System.Drawing.Size(192, 22);
          this.txtHost.TabIndex = 0;
          // 
          // label4
          // 
          this.label4.Location = new System.Drawing.Point(8, 10);
          this.label4.Name = "label4";
          this.label4.Size = new System.Drawing.Size(68, 15);
          this.label4.TabIndex = 0;
          this.label4.Text = "Host:";
          // 
          // tabPage3
          // 
          this.tabPage3.Controls.Add(this.lstLog);
          this.tabPage3.Location = new System.Drawing.Point(4, 21);
          this.tabPage3.Name = "tabPage3";
          this.tabPage3.Size = new System.Drawing.Size(284, 239);
          this.tabPage3.TabIndex = 2;
          this.tabPage3.Text = "Transaction";
          // 
          // lstLog
          // 
          this.lstLog.Dock = System.Windows.Forms.DockStyle.Fill;
          this.lstLog.ItemHeight = 12;
          this.lstLog.Location = new System.Drawing.Point(0, 0);
          this.lstLog.Name = "lstLog";
          this.lstLog.ScrollAlwaysVisible = true;
          this.lstLog.Size = new System.Drawing.Size(284, 232);
          this.lstLog.TabIndex = 0;
          // 
          // Panel1
          // 
          this.Panel1.Controls.Add(this.Label1);
          this.Panel1.Dock = System.Windows.Forms.DockStyle.Top;
          this.Panel1.Location = new System.Drawing.Point(0, 0);
          this.Panel1.Name = "Panel1";
          this.Panel1.Size = new System.Drawing.Size(284, 32);
          this.Panel1.TabIndex = 0;
          // 
          // btnPrevious
          // 
          this.btnPrevious.Enabled = false;
          this.btnPrevious.ImageIndex = 1;
          this.btnPrevious.Name = "btnPrevious";
          this.btnPrevious.Text = "Prev..";
          this.btnPrevious.ToolTipText = "Previous";
          // 
          // btnNext
          // 
          this.btnNext.Enabled = false;
          this.btnNext.ImageIndex = 2;
          this.btnNext.Name = "btnNext";
          this.btnNext.Text = "Next";
          this.btnNext.ToolTipText = "Next";
          // 
          // btnClear
          // 
          this.btnClear.ImageIndex = 3;
          this.btnClear.Name = "btnClear";
          this.btnClear.Text = "Clear";
          this.btnClear.ToolTipText = "Clear";
          // 
          // ImageList1
          // 
          this.ImageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("ImageList1.ImageStream")));
          this.ImageList1.TransparentColor = System.Drawing.Color.Transparent;
          this.ImageList1.Images.SetKeyName(0, "");
          this.ImageList1.Images.SetKeyName(1, "");
          this.ImageList1.Images.SetKeyName(2, "");
          this.ImageList1.Images.SetKeyName(3, "");
          // 
          // ToolBar1
          // 
          this.ToolBar1.AllowDrop = true;
          this.ToolBar1.Buttons.AddRange(new System.Windows.Forms.ToolBarButton[] {
            this.btnReceive,
            this.btnPrevious,
            this.btnNext,
            this.btnClear});
          this.ToolBar1.ButtonSize = new System.Drawing.Size(35, 35);
          this.ToolBar1.Dock = System.Windows.Forms.DockStyle.Fill;
          this.ToolBar1.DropDownArrows = true;
          this.ToolBar1.ImageList = this.ImageList1;
          this.ToolBar1.Location = new System.Drawing.Point(0, 0);
          this.ToolBar1.Name = "ToolBar1";
          this.ToolBar1.ShowToolTips = true;
          this.ToolBar1.Size = new System.Drawing.Size(292, 41);
          this.ToolBar1.TabIndex = 10;
          this.ToolBar1.ButtonClick += new System.Windows.Forms.ToolBarButtonClickEventHandler(this.ToolBar1_ButtonClick);
          // 
          // btnReceive
          // 
          this.btnReceive.ImageIndex = 0;
          this.btnReceive.Name = "btnReceive";
          this.btnReceive.Text = "Mail";
          this.btnReceive.ToolTipText = "Receive";
          // 
          // MainMenu1
          // 
          this.MainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.MenuItem1});
          // 
          // MenuItem1
          // 
          this.MenuItem1.Index = 0;
          this.MenuItem1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuExit});
          this.MenuItem1.Text = "&File";
          // 
          // mnuExit
          // 
          this.mnuExit.Index = 0;
          this.mnuExit.Text = "E&xit";
          this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
          // 
          // tabPage1
          // 
          this.tabPage1.Controls.Add(this.Panel2);
          this.tabPage1.Controls.Add(this.Panel1);
          this.tabPage1.Location = new System.Drawing.Point(4, 21);
          this.tabPage1.Name = "tabPage1";
          this.tabPage1.Size = new System.Drawing.Size(284, 239);
          this.tabPage1.TabIndex = 0;
          this.tabPage1.Text = "Mail";
          // 
          // Panel2
          // 
          this.Panel2.Controls.Add(this.txtMessage);
          this.Panel2.Dock = System.Windows.Forms.DockStyle.Fill;
          this.Panel2.Location = new System.Drawing.Point(0, 32);
          this.Panel2.Name = "Panel2";
          this.Panel2.Padding = new System.Windows.Forms.Padding(2);
          this.Panel2.Size = new System.Drawing.Size(284, 207);
          this.Panel2.TabIndex = 1;
          // 
          // txtMessage
          // 
          this.txtMessage.Dock = System.Windows.Forms.DockStyle.Fill;
          this.txtMessage.Location = new System.Drawing.Point(2, 2);
          this.txtMessage.Multiline = true;
          this.txtMessage.Name = "txtMessage";
          this.txtMessage.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
          this.txtMessage.Size = new System.Drawing.Size(280, 203);
          this.txtMessage.TabIndex = 2;
          // 
          // TabControl1
          // 
          this.TabControl1.Controls.Add(this.tabPage1);
          this.TabControl1.Controls.Add(this.tabPage2);
          this.TabControl1.Controls.Add(this.tabPage3);
          this.TabControl1.Dock = System.Windows.Forms.DockStyle.Bottom;
          this.TabControl1.Location = new System.Drawing.Point(0, 40);
          this.TabControl1.Name = "TabControl1";
          this.TabControl1.SelectedIndex = 0;
          this.TabControl1.Size = new System.Drawing.Size(292, 264);
          this.TabControl1.TabIndex = 9;
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(292, 304);
          this.Controls.Add(this.ToolBar1);
          this.Controls.Add(this.TabControl1);
          this.Menu = this.MainMenu1;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "POP3";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.tabPage2.ResumeLayout(false);
          this.panel3.ResumeLayout(false);
          this.panel3.PerformLayout();
          this.tabPage3.ResumeLayout(false);
          this.Panel1.ResumeLayout(false);
          this.tabPage1.ResumeLayout(false);
          this.Panel2.ResumeLayout(false);
          this.Panel2.PerformLayout();
          this.TabControl1.ResumeLayout(false);
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtPass;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtPort;
        private System.Windows.Forms.Label Label1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtLogin;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtHost;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.ListBox lstLog;
        private System.Windows.Forms.Panel Panel1;
        private System.Windows.Forms.ToolBarButton btnPrevious;
        private System.Windows.Forms.ToolBarButton btnNext;
        private System.Windows.Forms.ToolBarButton btnClear;
        private System.Windows.Forms.ImageList ImageList1;
        private System.Windows.Forms.ToolBar ToolBar1;
        private System.Windows.Forms.ToolBarButton btnReceive;
        private System.Windows.Forms.MainMenu MainMenu1;
        private System.Windows.Forms.MenuItem MenuItem1;
        private System.Windows.Forms.MenuItem mnuExit;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.Panel Panel2;
        private System.Windows.Forms.TextBox txtMessage;
        private System.Windows.Forms.TabControl TabControl1;
    }
}

