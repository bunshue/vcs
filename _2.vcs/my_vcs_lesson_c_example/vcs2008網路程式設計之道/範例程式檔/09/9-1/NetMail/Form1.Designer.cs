namespace NetMail
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
          this.OpenFileDialog1 = new System.Windows.Forms.OpenFileDialog();
          this.ImageList1 = new System.Windows.Forms.ImageList(this.components);
          this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
          this.MenuItem1 = new System.Windows.Forms.MenuItem();
          this.mnuExit = new System.Windows.Forms.MenuItem();
          this.ToolBar1 = new System.Windows.Forms.ToolBar();
          this.btnSend = new System.Windows.Forms.ToolBarButton();
          this.btnAttach = new System.Windows.Forms.ToolBarButton();
          this.btnClear = new System.Windows.Forms.ToolBarButton();
          this.TabControl1 = new System.Windows.Forms.TabControl();
          this.TabPage1 = new System.Windows.Forms.TabPage();
          this.Panel2 = new System.Windows.Forms.Panel();
          this.txtMessage = new System.Windows.Forms.TextBox();
          this.Panel1 = new System.Windows.Forms.Panel();
          this.cboPriority = new System.Windows.Forms.ComboBox();
          this.Label6 = new System.Windows.Forms.Label();
          this.chkHTML = new System.Windows.Forms.CheckBox();
          this.lstAttachment = new System.Windows.Forms.ListBox();
          this.Label5 = new System.Windows.Forms.Label();
          this.txtBcc = new System.Windows.Forms.TextBox();
          this.Label4 = new System.Windows.Forms.Label();
          this.txtCc = new System.Windows.Forms.TextBox();
          this.Label3 = new System.Windows.Forms.Label();
          this.txtSubject = new System.Windows.Forms.TextBox();
          this.Label2 = new System.Windows.Forms.Label();
          this.txtTo = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.TabPage2 = new System.Windows.Forms.TabPage();
          this.GroupBox1 = new System.Windows.Forms.GroupBox();
          this.txtPassword = new System.Windows.Forms.TextBox();
          this.label7 = new System.Windows.Forms.Label();
          this.txtLogin = new System.Windows.Forms.TextBox();
          this.label8 = new System.Windows.Forms.Label();
          this.txtFrom = new System.Windows.Forms.TextBox();
          this.label9 = new System.Windows.Forms.Label();
          this.txtHost = new System.Windows.Forms.TextBox();
          this.label10 = new System.Windows.Forms.Label();
          this.TabControl1.SuspendLayout();
          this.TabPage1.SuspendLayout();
          this.Panel2.SuspendLayout();
          this.Panel1.SuspendLayout();
          this.TabPage2.SuspendLayout();
          this.GroupBox1.SuspendLayout();
          this.SuspendLayout();
          // 
          // ImageList1
          // 
          this.ImageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("ImageList1.ImageStream")));
          this.ImageList1.TransparentColor = System.Drawing.Color.Transparent;
          this.ImageList1.Images.SetKeyName(0, "");
          this.ImageList1.Images.SetKeyName(1, "");
          this.ImageList1.Images.SetKeyName(2, "");
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
            this.btnAttach,
            this.btnClear});
          this.ToolBar1.ButtonSize = new System.Drawing.Size(30, 30);
          this.ToolBar1.DropDownArrows = true;
          this.ToolBar1.ImageList = this.ImageList1;
          this.ToolBar1.Location = new System.Drawing.Point(0, 0);
          this.ToolBar1.Name = "ToolBar1";
          this.ToolBar1.ShowToolTips = true;
          this.ToolBar1.Size = new System.Drawing.Size(315, 41);
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
          // btnAttach
          // 
          this.btnAttach.ImageIndex = 1;
          this.btnAttach.Name = "btnAttach";
          this.btnAttach.Text = "Attach ...";
          this.btnAttach.ToolTipText = "Attachment";
          // 
          // btnClear
          // 
          this.btnClear.ImageIndex = 2;
          this.btnClear.Name = "btnClear";
          this.btnClear.Text = "Clear";
          this.btnClear.ToolTipText = "Clear";
          // 
          // TabControl1
          // 
          this.TabControl1.Controls.Add(this.TabPage1);
          this.TabControl1.Controls.Add(this.TabPage2);
          this.TabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
          this.TabControl1.Location = new System.Drawing.Point(0, 41);
          this.TabControl1.Name = "TabControl1";
          this.TabControl1.SelectedIndex = 0;
          this.TabControl1.Size = new System.Drawing.Size(315, 366);
          this.TabControl1.TabIndex = 10;
          // 
          // TabPage1
          // 
          this.TabPage1.Controls.Add(this.Panel2);
          this.TabPage1.Controls.Add(this.Panel1);
          this.TabPage1.Location = new System.Drawing.Point(4, 21);
          this.TabPage1.Name = "TabPage1";
          this.TabPage1.Size = new System.Drawing.Size(307, 341);
          this.TabPage1.TabIndex = 0;
          this.TabPage1.Text = "SMTP";
          this.TabPage1.UseVisualStyleBackColor = true;
          // 
          // Panel2
          // 
          this.Panel2.Controls.Add(this.txtMessage);
          this.Panel2.Dock = System.Windows.Forms.DockStyle.Fill;
          this.Panel2.Location = new System.Drawing.Point(0, 168);
          this.Panel2.Name = "Panel2";
          this.Panel2.Padding = new System.Windows.Forms.Padding(2);
          this.Panel2.Size = new System.Drawing.Size(307, 173);
          this.Panel2.TabIndex = 1;
          // 
          // txtMessage
          // 
          this.txtMessage.Dock = System.Windows.Forms.DockStyle.Fill;
          this.txtMessage.Location = new System.Drawing.Point(2, 2);
          this.txtMessage.Multiline = true;
          this.txtMessage.Name = "txtMessage";
          this.txtMessage.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
          this.txtMessage.Size = new System.Drawing.Size(303, 169);
          this.txtMessage.TabIndex = 7;
          // 
          // Panel1
          // 
          this.Panel1.Controls.Add(this.cboPriority);
          this.Panel1.Controls.Add(this.Label6);
          this.Panel1.Controls.Add(this.chkHTML);
          this.Panel1.Controls.Add(this.lstAttachment);
          this.Panel1.Controls.Add(this.Label5);
          this.Panel1.Controls.Add(this.txtBcc);
          this.Panel1.Controls.Add(this.Label4);
          this.Panel1.Controls.Add(this.txtCc);
          this.Panel1.Controls.Add(this.Label3);
          this.Panel1.Controls.Add(this.txtSubject);
          this.Panel1.Controls.Add(this.Label2);
          this.Panel1.Controls.Add(this.txtTo);
          this.Panel1.Controls.Add(this.Label1);
          this.Panel1.Dock = System.Windows.Forms.DockStyle.Top;
          this.Panel1.Location = new System.Drawing.Point(0, 0);
          this.Panel1.Name = "Panel1";
          this.Panel1.Size = new System.Drawing.Size(307, 168);
          this.Panel1.TabIndex = 0;
          // 
          // cboPriority
          // 
          this.cboPriority.Items.AddRange(new object[] {
            "Normal",
            "Low",
            "High"});
          this.cboPriority.Location = new System.Drawing.Point(72, 141);
          this.cboPriority.Name = "cboPriority";
          this.cboPriority.Size = new System.Drawing.Size(124, 20);
          this.cboPriority.TabIndex = 5;
          this.cboPriority.Text = "Normal";
          // 
          // Label6
          // 
          this.Label6.Location = new System.Drawing.Point(8, 144);
          this.Label6.Name = "Label6";
          this.Label6.Size = new System.Drawing.Size(68, 15);
          this.Label6.TabIndex = 8;
          this.Label6.Text = "Priority:";
          // 
          // chkHTML
          // 
          this.chkHTML.Location = new System.Drawing.Point(202, 142);
          this.chkHTML.Name = "chkHTML";
          this.chkHTML.Size = new System.Drawing.Size(96, 20);
          this.chkHTML.TabIndex = 6;
          this.chkHTML.Text = "HTML Format";
          // 
          // lstAttachment
          // 
          this.lstAttachment.ItemHeight = 12;
          this.lstAttachment.Location = new System.Drawing.Point(72, 109);
          this.lstAttachment.Name = "lstAttachment";
          this.lstAttachment.ScrollAlwaysVisible = true;
          this.lstAttachment.Size = new System.Drawing.Size(226, 28);
          this.lstAttachment.TabIndex = 4;
          // 
          // Label5
          // 
          this.Label5.Location = new System.Drawing.Point(8, 110);
          this.Label5.Name = "Label5";
          this.Label5.Size = new System.Drawing.Size(68, 15);
          this.Label5.TabIndex = 6;
          this.Label5.Text = "Attachment:";
          // 
          // txtBcc
          // 
          this.txtBcc.Location = new System.Drawing.Point(72, 57);
          this.txtBcc.Name = "txtBcc";
          this.txtBcc.Size = new System.Drawing.Size(226, 22);
          this.txtBcc.TabIndex = 2;
          // 
          // Label4
          // 
          this.Label4.Location = new System.Drawing.Point(8, 60);
          this.Label4.Name = "Label4";
          this.Label4.Size = new System.Drawing.Size(68, 15);
          this.Label4.TabIndex = 5;
          this.Label4.Text = "Bcc:";
          // 
          // txtCc
          // 
          this.txtCc.Location = new System.Drawing.Point(72, 31);
          this.txtCc.Name = "txtCc";
          this.txtCc.Size = new System.Drawing.Size(226, 22);
          this.txtCc.TabIndex = 1;
          // 
          // Label3
          // 
          this.Label3.Location = new System.Drawing.Point(8, 35);
          this.Label3.Name = "Label3";
          this.Label3.Size = new System.Drawing.Size(68, 15);
          this.Label3.TabIndex = 3;
          this.Label3.Text = "Cc:";
          // 
          // txtSubject
          // 
          this.txtSubject.Location = new System.Drawing.Point(72, 83);
          this.txtSubject.Name = "txtSubject";
          this.txtSubject.Size = new System.Drawing.Size(226, 22);
          this.txtSubject.TabIndex = 3;
          // 
          // Label2
          // 
          this.Label2.Location = new System.Drawing.Point(8, 85);
          this.Label2.Name = "Label2";
          this.Label2.Size = new System.Drawing.Size(68, 15);
          this.Label2.TabIndex = 2;
          this.Label2.Text = "Subject:";
          // 
          // txtTo
          // 
          this.txtTo.Location = new System.Drawing.Point(72, 5);
          this.txtTo.Name = "txtTo";
          this.txtTo.Size = new System.Drawing.Size(226, 22);
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
          // TabPage2
          // 
          this.TabPage2.Controls.Add(this.GroupBox1);
          this.TabPage2.Location = new System.Drawing.Point(4, 21);
          this.TabPage2.Name = "TabPage2";
          this.TabPage2.Padding = new System.Windows.Forms.Padding(3);
          this.TabPage2.Size = new System.Drawing.Size(307, 341);
          this.TabPage2.TabIndex = 1;
          this.TabPage2.Text = "Profile";
          this.TabPage2.UseVisualStyleBackColor = true;
          // 
          // GroupBox1
          // 
          this.GroupBox1.Controls.Add(this.txtPassword);
          this.GroupBox1.Controls.Add(this.label7);
          this.GroupBox1.Controls.Add(this.txtLogin);
          this.GroupBox1.Controls.Add(this.label8);
          this.GroupBox1.Controls.Add(this.txtFrom);
          this.GroupBox1.Controls.Add(this.label9);
          this.GroupBox1.Controls.Add(this.txtHost);
          this.GroupBox1.Controls.Add(this.label10);
          this.GroupBox1.Location = new System.Drawing.Point(8, 6);
          this.GroupBox1.Name = "GroupBox1";
          this.GroupBox1.Size = new System.Drawing.Size(239, 140);
          this.GroupBox1.TabIndex = 10;
          this.GroupBox1.TabStop = false;
          this.GroupBox1.Text = "SMTP Server";
          // 
          // txtPassword
          // 
          this.txtPassword.Location = new System.Drawing.Point(65, 104);
          this.txtPassword.Name = "txtPassword";
          this.txtPassword.Size = new System.Drawing.Size(164, 22);
          this.txtPassword.TabIndex = 3;
          // 
          // label7
          // 
          this.label7.Location = new System.Drawing.Point(8, 107);
          this.label7.Name = "label7";
          this.label7.Size = new System.Drawing.Size(70, 15);
          this.label7.TabIndex = 9;
          this.label7.Text = "Password:";
          // 
          // txtLogin
          // 
          this.txtLogin.Location = new System.Drawing.Point(65, 76);
          this.txtLogin.Name = "txtLogin";
          this.txtLogin.Size = new System.Drawing.Size(164, 22);
          this.txtLogin.TabIndex = 2;
          // 
          // label8
          // 
          this.label8.Location = new System.Drawing.Point(8, 79);
          this.label8.Name = "label8";
          this.label8.Size = new System.Drawing.Size(70, 15);
          this.label8.TabIndex = 7;
          this.label8.Text = "Login:";
          // 
          // txtFrom
          // 
          this.txtFrom.Location = new System.Drawing.Point(65, 48);
          this.txtFrom.Name = "txtFrom";
          this.txtFrom.Size = new System.Drawing.Size(164, 22);
          this.txtFrom.TabIndex = 1;
          // 
          // label9
          // 
          this.label9.Location = new System.Drawing.Point(8, 52);
          this.label9.Name = "label9";
          this.label9.Size = new System.Drawing.Size(70, 15);
          this.label9.TabIndex = 5;
          this.label9.Text = "From:";
          // 
          // txtHost
          // 
          this.txtHost.Location = new System.Drawing.Point(65, 20);
          this.txtHost.Name = "txtHost";
          this.txtHost.Size = new System.Drawing.Size(164, 22);
          this.txtHost.TabIndex = 0;
          // 
          // label10
          // 
          this.label10.Location = new System.Drawing.Point(8, 25);
          this.label10.Name = "label10";
          this.label10.Size = new System.Drawing.Size(70, 15);
          this.label10.TabIndex = 0;
          this.label10.Text = "Host:";
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(315, 407);
          this.Controls.Add(this.TabControl1);
          this.Controls.Add(this.ToolBar1);
          this.Menu = this.MainMenu1;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "Net Mail";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.Resize += new System.EventHandler(this.Form1_Resize);
          this.TabControl1.ResumeLayout(false);
          this.TabPage1.ResumeLayout(false);
          this.Panel2.ResumeLayout(false);
          this.Panel2.PerformLayout();
          this.Panel1.ResumeLayout(false);
          this.Panel1.PerformLayout();
          this.TabPage2.ResumeLayout(false);
          this.GroupBox1.ResumeLayout(false);
          this.GroupBox1.PerformLayout();
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.OpenFileDialog OpenFileDialog1;
        internal System.Windows.Forms.ImageList ImageList1;
        internal System.Windows.Forms.MainMenu MainMenu1;
        internal System.Windows.Forms.MenuItem MenuItem1;
        internal System.Windows.Forms.MenuItem mnuExit;
        internal System.Windows.Forms.ToolBar ToolBar1;
        internal System.Windows.Forms.ToolBarButton btnSend;
        internal System.Windows.Forms.ToolBarButton btnAttach;
        internal System.Windows.Forms.ToolBarButton btnClear;
        internal System.Windows.Forms.TabControl TabControl1;
        internal System.Windows.Forms.TabPage TabPage1;
        internal System.Windows.Forms.Panel Panel2;
        internal System.Windows.Forms.TextBox txtMessage;
        internal System.Windows.Forms.Panel Panel1;
        internal System.Windows.Forms.ComboBox cboPriority;
        internal System.Windows.Forms.Label Label6;
        internal System.Windows.Forms.CheckBox chkHTML;
        internal System.Windows.Forms.ListBox lstAttachment;
        internal System.Windows.Forms.Label Label5;
        internal System.Windows.Forms.TextBox txtBcc;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.TextBox txtCc;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.TextBox txtSubject;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtTo;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.TabPage TabPage2;
        internal System.Windows.Forms.GroupBox GroupBox1;
        internal System.Windows.Forms.TextBox txtPassword;
        internal System.Windows.Forms.Label label7;
        internal System.Windows.Forms.TextBox txtLogin;
        internal System.Windows.Forms.Label label8;
        internal System.Windows.Forms.TextBox txtFrom;
        internal System.Windows.Forms.Label label9;
        internal System.Windows.Forms.TextBox txtHost;
        internal System.Windows.Forms.Label label10;
    }
}

