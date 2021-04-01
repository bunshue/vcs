namespace SMTP
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
          this.ImageList1 = new System.Windows.Forms.ImageList(this.components);
          this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
          this.MenuItem1 = new System.Windows.Forms.MenuItem();
          this.mnuExit = new System.Windows.Forms.MenuItem();
          this.ToolBar1 = new System.Windows.Forms.ToolBar();
          this.btnSend = new System.Windows.Forms.ToolBarButton();
          this.btnClear = new System.Windows.Forms.ToolBarButton();
          this.TabControl1 = new System.Windows.Forms.TabControl();
          this.tabPage1 = new System.Windows.Forms.TabPage();
          this.Panel2 = new System.Windows.Forms.Panel();
          this.txtMessage = new System.Windows.Forms.TextBox();
          this.Panel1 = new System.Windows.Forms.Panel();
          this.txtSubject = new System.Windows.Forms.TextBox();
          this.Label2 = new System.Windows.Forms.Label();
          this.txtTo = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.tabPage2 = new System.Windows.Forms.TabPage();
          this.panel3 = new System.Windows.Forms.Panel();
          this.txtPort = new System.Windows.Forms.TextBox();
          this.label5 = new System.Windows.Forms.Label();
          this.txtFrom = new System.Windows.Forms.TextBox();
          this.label3 = new System.Windows.Forms.Label();
          this.txtHost = new System.Windows.Forms.TextBox();
          this.label4 = new System.Windows.Forms.Label();
          this.tabPage3 = new System.Windows.Forms.TabPage();
          this.lstLog = new System.Windows.Forms.ListBox();
          this.TabControl1.SuspendLayout();
          this.tabPage1.SuspendLayout();
          this.Panel2.SuspendLayout();
          this.Panel1.SuspendLayout();
          this.tabPage2.SuspendLayout();
          this.panel3.SuspendLayout();
          this.tabPage3.SuspendLayout();
          this.SuspendLayout();
          // 
          // ImageList1
          // 
          this.ImageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("ImageList1.ImageStream")));
          this.ImageList1.TransparentColor = System.Drawing.Color.Transparent;
          this.ImageList1.Images.SetKeyName(0, "");
          this.ImageList1.Images.SetKeyName(1, "");
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
          // ToolBar1
          // 
          this.ToolBar1.AllowDrop = true;
          this.ToolBar1.Buttons.AddRange(new System.Windows.Forms.ToolBarButton[] {
            this.btnSend,
            this.btnClear});
          this.ToolBar1.ButtonSize = new System.Drawing.Size(35, 35);
          this.ToolBar1.DropDownArrows = true;
          this.ToolBar1.ImageList = this.ImageList1;
          this.ToolBar1.Location = new System.Drawing.Point(0, 0);
          this.ToolBar1.Name = "ToolBar1";
          this.ToolBar1.ShowToolTips = true;
          this.ToolBar1.Size = new System.Drawing.Size(292, 41);
          this.ToolBar1.TabIndex = 9;
          this.ToolBar1.ButtonClick += new System.Windows.Forms.ToolBarButtonClickEventHandler(this.ToolBar1_ButtonClick);
          // 
          // btnSend
          // 
          this.btnSend.ImageIndex = 0;
          this.btnSend.Name = "btnSend";
          this.btnSend.Text = "Send";
          this.btnSend.ToolTipText = "Send";
          // 
          // btnClear
          // 
          this.btnClear.ImageIndex = 1;
          this.btnClear.Name = "btnClear";
          this.btnClear.Text = "Clear";
          // 
          // TabControl1
          // 
          this.TabControl1.Controls.Add(this.tabPage1);
          this.TabControl1.Controls.Add(this.tabPage2);
          this.TabControl1.Controls.Add(this.tabPage3);
          this.TabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
          this.TabControl1.Location = new System.Drawing.Point(0, 41);
          this.TabControl1.Name = "TabControl1";
          this.TabControl1.SelectedIndex = 0;
          this.TabControl1.Size = new System.Drawing.Size(292, 268);
          this.TabControl1.TabIndex = 10;
          // 
          // tabPage1
          // 
          this.tabPage1.Controls.Add(this.Panel2);
          this.tabPage1.Controls.Add(this.Panel1);
          this.tabPage1.Location = new System.Drawing.Point(4, 21);
          this.tabPage1.Name = "tabPage1";
          this.tabPage1.Size = new System.Drawing.Size(284, 243);
          this.tabPage1.TabIndex = 0;
          this.tabPage1.Text = "Mail";
          // 
          // Panel2
          // 
          this.Panel2.Controls.Add(this.txtMessage);
          this.Panel2.Dock = System.Windows.Forms.DockStyle.Fill;
          this.Panel2.Location = new System.Drawing.Point(0, 64);
          this.Panel2.Name = "Panel2";
          this.Panel2.Padding = new System.Windows.Forms.Padding(2);
          this.Panel2.Size = new System.Drawing.Size(284, 179);
          this.Panel2.TabIndex = 1;
          // 
          // txtMessage
          // 
          this.txtMessage.Dock = System.Windows.Forms.DockStyle.Fill;
          this.txtMessage.Location = new System.Drawing.Point(2, 2);
          this.txtMessage.Multiline = true;
          this.txtMessage.Name = "txtMessage";
          this.txtMessage.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
          this.txtMessage.Size = new System.Drawing.Size(280, 175);
          this.txtMessage.TabIndex = 2;
          // 
          // Panel1
          // 
          this.Panel1.Controls.Add(this.txtSubject);
          this.Panel1.Controls.Add(this.Label2);
          this.Panel1.Controls.Add(this.txtTo);
          this.Panel1.Controls.Add(this.Label1);
          this.Panel1.Dock = System.Windows.Forms.DockStyle.Top;
          this.Panel1.Location = new System.Drawing.Point(0, 0);
          this.Panel1.Name = "Panel1";
          this.Panel1.Size = new System.Drawing.Size(284, 64);
          this.Panel1.TabIndex = 0;
          // 
          // txtSubject
          // 
          this.txtSubject.Location = new System.Drawing.Point(53, 35);
          this.txtSubject.Name = "txtSubject";
          this.txtSubject.Size = new System.Drawing.Size(221, 22);
          this.txtSubject.TabIndex = 1;
          // 
          // Label2
          // 
          this.Label2.Location = new System.Drawing.Point(8, 40);
          this.Label2.Name = "Label2";
          this.Label2.Size = new System.Drawing.Size(68, 15);
          this.Label2.TabIndex = 2;
          this.Label2.Text = "Subject:";
          // 
          // txtTo
          // 
          this.txtTo.Location = new System.Drawing.Point(53, 7);
          this.txtTo.Name = "txtTo";
          this.txtTo.Size = new System.Drawing.Size(221, 22);
          this.txtTo.TabIndex = 0;
          // 
          // Label1
          // 
          this.Label1.Location = new System.Drawing.Point(8, 10);
          this.Label1.Name = "Label1";
          this.Label1.Size = new System.Drawing.Size(68, 15);
          this.Label1.TabIndex = 0;
          this.Label1.Text = "To:";
          // 
          // tabPage2
          // 
          this.tabPage2.Controls.Add(this.panel3);
          this.tabPage2.Location = new System.Drawing.Point(4, 21);
          this.tabPage2.Name = "tabPage2";
          this.tabPage2.Size = new System.Drawing.Size(284, 217);
          this.tabPage2.TabIndex = 1;
          this.tabPage2.Text = "SMTP";
          // 
          // panel3
          // 
          this.panel3.Controls.Add(this.txtPort);
          this.panel3.Controls.Add(this.label5);
          this.panel3.Controls.Add(this.txtFrom);
          this.panel3.Controls.Add(this.label3);
          this.panel3.Controls.Add(this.txtHost);
          this.panel3.Controls.Add(this.label4);
          this.panel3.Dock = System.Windows.Forms.DockStyle.Top;
          this.panel3.Location = new System.Drawing.Point(0, 0);
          this.panel3.Name = "panel3";
          this.panel3.Size = new System.Drawing.Size(284, 92);
          this.panel3.TabIndex = 1;
          // 
          // txtPort
          // 
          this.txtPort.Location = new System.Drawing.Point(72, 32);
          this.txtPort.Name = "txtPort";
          this.txtPort.Size = new System.Drawing.Size(192, 22);
          this.txtPort.TabIndex = 1;
          // 
          // label5
          // 
          this.label5.Location = new System.Drawing.Point(8, 37);
          this.label5.Name = "label5";
          this.label5.Size = new System.Drawing.Size(68, 15);
          this.label5.TabIndex = 5;
          this.label5.Text = "Port:";
          // 
          // txtFrom
          // 
          this.txtFrom.Location = new System.Drawing.Point(72, 59);
          this.txtFrom.Name = "txtFrom";
          this.txtFrom.Size = new System.Drawing.Size(192, 22);
          this.txtFrom.TabIndex = 2;
          // 
          // label3
          // 
          this.label3.Location = new System.Drawing.Point(8, 64);
          this.label3.Name = "label3";
          this.label3.Size = new System.Drawing.Size(68, 15);
          this.label3.TabIndex = 3;
          this.label3.Text = "From:";
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
          this.tabPage3.Size = new System.Drawing.Size(284, 217);
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
          this.lstLog.Size = new System.Drawing.Size(284, 208);
          this.lstLog.TabIndex = 0;
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(292, 309);
          this.Controls.Add(this.TabControl1);
          this.Controls.Add(this.ToolBar1);
          this.Menu = this.MainMenu1;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "SMTP";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.Resize += new System.EventHandler(this.Form1_Resize);
          this.TabControl1.ResumeLayout(false);
          this.tabPage1.ResumeLayout(false);
          this.Panel2.ResumeLayout(false);
          this.Panel2.PerformLayout();
          this.Panel1.ResumeLayout(false);
          this.Panel1.PerformLayout();
          this.tabPage2.ResumeLayout(false);
          this.panel3.ResumeLayout(false);
          this.panel3.PerformLayout();
          this.tabPage3.ResumeLayout(false);
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ImageList ImageList1;
        private System.Windows.Forms.MainMenu MainMenu1;
        private System.Windows.Forms.MenuItem MenuItem1;
        private System.Windows.Forms.MenuItem mnuExit;
        private System.Windows.Forms.ToolBar ToolBar1;
        private System.Windows.Forms.ToolBarButton btnSend;
        private System.Windows.Forms.ToolBarButton btnClear;
        private System.Windows.Forms.TabControl TabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.Panel Panel2;
        private System.Windows.Forms.TextBox txtMessage;
        private System.Windows.Forms.Panel Panel1;
        private System.Windows.Forms.TextBox txtSubject;
        private System.Windows.Forms.Label Label2;
        private System.Windows.Forms.TextBox txtTo;
        private System.Windows.Forms.Label Label1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.TextBox txtPort;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox txtFrom;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtHost;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.ListBox lstLog;
    }
}

