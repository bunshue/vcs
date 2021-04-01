namespace WebClientFTP
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
          this.btnUploadFile = new System.Windows.Forms.Button();
          this.btnDownloadFile = new System.Windows.Forms.Button();
          this.Label6 = new System.Windows.Forms.Label();
          this.txtLocal = new System.Windows.Forms.TextBox();
          this.txtRemote = new System.Windows.Forms.TextBox();
          this.Label5 = new System.Windows.Forms.Label();
          this.txtPassword = new System.Windows.Forms.TextBox();
          this.txtLogin = new System.Windows.Forms.TextBox();
          this.txtURL = new System.Windows.Forms.TextBox();
          this.Label3 = new System.Windows.Forms.Label();
          this.Label2 = new System.Windows.Forms.Label();
          this.Label1 = new System.Windows.Forms.Label();
          this.btnSelect = new System.Windows.Forms.Button();
          this.statusStrip1 = new System.Windows.Forms.StatusStrip();
          this.StatusBar = new System.Windows.Forms.ToolStripStatusLabel();
          this.txtData = new System.Windows.Forms.TextBox();
          this.btnUploadData = new System.Windows.Forms.Button();
          this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
          this.label4 = new System.Windows.Forms.Label();
          this.statusStrip1.SuspendLayout();
          this.SuspendLayout();
          // 
          // btnUploadFile
          // 
          this.btnUploadFile.BackColor = System.Drawing.SystemColors.Control;
          this.btnUploadFile.Cursor = System.Windows.Forms.Cursors.Default;
          this.btnUploadFile.ForeColor = System.Drawing.SystemColors.ControlText;
          this.btnUploadFile.Location = new System.Drawing.Point(244, 57);
          this.btnUploadFile.Name = "btnUploadFile";
          this.btnUploadFile.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.btnUploadFile.Size = new System.Drawing.Size(94, 28);
          this.btnUploadFile.TabIndex = 8;
          this.btnUploadFile.Text = "Upload File";
          this.btnUploadFile.UseVisualStyleBackColor = false;
          this.btnUploadFile.Click += new System.EventHandler(this.btnUploadFile_Click);
          // 
          // btnDownloadFile
          // 
          this.btnDownloadFile.BackColor = System.Drawing.SystemColors.Control;
          this.btnDownloadFile.Cursor = System.Windows.Forms.Cursors.Default;
          this.btnDownloadFile.ForeColor = System.Drawing.SystemColors.ControlText;
          this.btnDownloadFile.Location = new System.Drawing.Point(244, 9);
          this.btnDownloadFile.Name = "btnDownloadFile";
          this.btnDownloadFile.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.btnDownloadFile.Size = new System.Drawing.Size(94, 28);
          this.btnDownloadFile.TabIndex = 7;
          this.btnDownloadFile.Text = "Download File";
          this.btnDownloadFile.UseVisualStyleBackColor = false;
          this.btnDownloadFile.Click += new System.EventHandler(this.btnDownloadFile_Click);
          // 
          // Label6
          // 
          this.Label6.BackColor = System.Drawing.SystemColors.Control;
          this.Label6.Cursor = System.Windows.Forms.Cursors.Default;
          this.Label6.ForeColor = System.Drawing.SystemColors.ControlText;
          this.Label6.Location = new System.Drawing.Point(14, 115);
          this.Label6.Name = "Label6";
          this.Label6.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.Label6.Size = new System.Drawing.Size(64, 19);
          this.Label6.TabIndex = 69;
          this.Label6.Text = "Local File:";
          // 
          // txtLocal
          // 
          this.txtLocal.AcceptsReturn = true;
          this.txtLocal.BackColor = System.Drawing.SystemColors.Window;
          this.txtLocal.Cursor = System.Windows.Forms.Cursors.IBeam;
          this.txtLocal.ForeColor = System.Drawing.SystemColors.WindowText;
          this.txtLocal.Location = new System.Drawing.Point(83, 109);
          this.txtLocal.MaxLength = 0;
          this.txtLocal.Name = "txtLocal";
          this.txtLocal.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.txtLocal.Size = new System.Drawing.Size(115, 22);
          this.txtLocal.TabIndex = 4;
          // 
          // txtRemote
          // 
          this.txtRemote.AcceptsReturn = true;
          this.txtRemote.BackColor = System.Drawing.SystemColors.Window;
          this.txtRemote.Cursor = System.Windows.Forms.Cursors.IBeam;
          this.txtRemote.ForeColor = System.Drawing.SystemColors.WindowText;
          this.txtRemote.Location = new System.Drawing.Point(83, 84);
          this.txtRemote.MaxLength = 0;
          this.txtRemote.Name = "txtRemote";
          this.txtRemote.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.txtRemote.Size = new System.Drawing.Size(146, 22);
          this.txtRemote.TabIndex = 3;
          // 
          // Label5
          // 
          this.Label5.BackColor = System.Drawing.SystemColors.Control;
          this.Label5.Cursor = System.Windows.Forms.Cursors.Default;
          this.Label5.ForeColor = System.Drawing.SystemColors.ControlText;
          this.Label5.Location = new System.Drawing.Point(14, 90);
          this.Label5.Name = "Label5";
          this.Label5.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.Label5.Size = new System.Drawing.Size(64, 16);
          this.Label5.TabIndex = 68;
          this.Label5.Text = "Remote File:";
          // 
          // txtPassword
          // 
          this.txtPassword.AcceptsReturn = true;
          this.txtPassword.BackColor = System.Drawing.SystemColors.Window;
          this.txtPassword.Cursor = System.Windows.Forms.Cursors.IBeam;
          this.txtPassword.ForeColor = System.Drawing.SystemColors.WindowText;
          this.txtPassword.Location = new System.Drawing.Point(83, 59);
          this.txtPassword.MaxLength = 0;
          this.txtPassword.Name = "txtPassword";
          this.txtPassword.PasswordChar = '*';
          this.txtPassword.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.txtPassword.Size = new System.Drawing.Size(146, 22);
          this.txtPassword.TabIndex = 2;
          this.txtPassword.Text = "athena@yahoo.com.tw";
          // 
          // txtLogin
          // 
          this.txtLogin.AcceptsReturn = true;
          this.txtLogin.BackColor = System.Drawing.SystemColors.Window;
          this.txtLogin.Cursor = System.Windows.Forms.Cursors.IBeam;
          this.txtLogin.ForeColor = System.Drawing.SystemColors.WindowText;
          this.txtLogin.Location = new System.Drawing.Point(83, 34);
          this.txtLogin.MaxLength = 0;
          this.txtLogin.Name = "txtLogin";
          this.txtLogin.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.txtLogin.Size = new System.Drawing.Size(146, 22);
          this.txtLogin.TabIndex = 1;
          this.txtLogin.Text = "anonymous";
          // 
          // txtURL
          // 
          this.txtURL.AcceptsReturn = true;
          this.txtURL.BackColor = System.Drawing.SystemColors.Window;
          this.txtURL.Cursor = System.Windows.Forms.Cursors.IBeam;
          this.txtURL.ForeColor = System.Drawing.SystemColors.WindowText;
          this.txtURL.Location = new System.Drawing.Point(83, 9);
          this.txtURL.MaxLength = 0;
          this.txtURL.Name = "txtURL";
          this.txtURL.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.txtURL.Size = new System.Drawing.Size(146, 22);
          this.txtURL.TabIndex = 0;
          this.txtURL.Text = "ftp://";
          // 
          // Label3
          // 
          this.Label3.BackColor = System.Drawing.SystemColors.Control;
          this.Label3.Cursor = System.Windows.Forms.Cursors.Default;
          this.Label3.ForeColor = System.Drawing.SystemColors.ControlText;
          this.Label3.Location = new System.Drawing.Point(14, 65);
          this.Label3.Name = "Label3";
          this.Label3.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.Label3.Size = new System.Drawing.Size(64, 16);
          this.Label3.TabIndex = 65;
          this.Label3.Text = "Password:";
          // 
          // Label2
          // 
          this.Label2.BackColor = System.Drawing.SystemColors.Control;
          this.Label2.Cursor = System.Windows.Forms.Cursors.Default;
          this.Label2.ForeColor = System.Drawing.SystemColors.ControlText;
          this.Label2.Location = new System.Drawing.Point(14, 40);
          this.Label2.Name = "Label2";
          this.Label2.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.Label2.Size = new System.Drawing.Size(64, 16);
          this.Label2.TabIndex = 64;
          this.Label2.Text = "Login:";
          // 
          // Label1
          // 
          this.Label1.BackColor = System.Drawing.SystemColors.Control;
          this.Label1.Cursor = System.Windows.Forms.Cursors.Default;
          this.Label1.ForeColor = System.Drawing.SystemColors.ControlText;
          this.Label1.Location = new System.Drawing.Point(14, 15);
          this.Label1.Name = "Label1";
          this.Label1.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.Label1.Size = new System.Drawing.Size(64, 16);
          this.Label1.TabIndex = 63;
          this.Label1.Text = "FTP URL:";
          // 
          // btnSelect
          // 
          this.btnSelect.Location = new System.Drawing.Point(204, 111);
          this.btnSelect.Name = "btnSelect";
          this.btnSelect.Size = new System.Drawing.Size(25, 20);
          this.btnSelect.TabIndex = 5;
          this.btnSelect.Text = "...";
          this.btnSelect.Click += new System.EventHandler(this.btnSelect_Click);
          // 
          // statusStrip1
          // 
          this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.StatusBar});
          this.statusStrip1.Location = new System.Drawing.Point(0, 291);
          this.statusStrip1.Name = "statusStrip1";
          this.statusStrip1.Size = new System.Drawing.Size(354, 22);
          this.statusStrip1.TabIndex = 72;
          this.statusStrip1.Text = "statusStrip1";
          // 
          // StatusBar
          // 
          this.StatusBar.Name = "StatusBar";
          this.StatusBar.Size = new System.Drawing.Size(0, 17);
          // 
          // txtData
          // 
          this.txtData.Location = new System.Drawing.Point(16, 165);
          this.txtData.Multiline = true;
          this.txtData.Name = "txtData";
          this.txtData.ScrollBars = System.Windows.Forms.ScrollBars.Both;
          this.txtData.Size = new System.Drawing.Size(322, 110);
          this.txtData.TabIndex = 6;
          // 
          // btnUploadData
          // 
          this.btnUploadData.BackColor = System.Drawing.SystemColors.Control;
          this.btnUploadData.Cursor = System.Windows.Forms.Cursors.Default;
          this.btnUploadData.ForeColor = System.Drawing.SystemColors.ControlText;
          this.btnUploadData.Location = new System.Drawing.Point(244, 103);
          this.btnUploadData.Name = "btnUploadData";
          this.btnUploadData.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.btnUploadData.Size = new System.Drawing.Size(94, 28);
          this.btnUploadData.TabIndex = 9;
          this.btnUploadData.Text = "Upload Data";
          this.btnUploadData.UseVisualStyleBackColor = false;
          this.btnUploadData.Click += new System.EventHandler(this.btnUploadData_Click);
          // 
          // saveFileDialog1
          // 
          this.saveFileDialog1.DefaultExt = "*.*";
          // 
          // label4
          // 
          this.label4.BackColor = System.Drawing.SystemColors.Control;
          this.label4.Cursor = System.Windows.Forms.Cursors.Default;
          this.label4.ForeColor = System.Drawing.SystemColors.ControlText;
          this.label4.Location = new System.Drawing.Point(14, 143);
          this.label4.Name = "label4";
          this.label4.RightToLeft = System.Windows.Forms.RightToLeft.No;
          this.label4.Size = new System.Drawing.Size(64, 19);
          this.label4.TabIndex = 73;
          this.label4.Text = "Data:";
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(354, 313);
          this.Controls.Add(this.label4);
          this.Controls.Add(this.btnUploadData);
          this.Controls.Add(this.txtData);
          this.Controls.Add(this.statusStrip1);
          this.Controls.Add(this.btnSelect);
          this.Controls.Add(this.btnUploadFile);
          this.Controls.Add(this.btnDownloadFile);
          this.Controls.Add(this.Label6);
          this.Controls.Add(this.txtLocal);
          this.Controls.Add(this.txtRemote);
          this.Controls.Add(this.Label5);
          this.Controls.Add(this.txtPassword);
          this.Controls.Add(this.txtLogin);
          this.Controls.Add(this.txtURL);
          this.Controls.Add(this.Label3);
          this.Controls.Add(this.Label2);
          this.Controls.Add(this.Label1);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
          this.MaximizeBox = false;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "WebClient - FTP Protocol";
          this.statusStrip1.ResumeLayout(false);
          this.statusStrip1.PerformLayout();
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.Button btnUploadFile;
        public System.Windows.Forms.Button btnDownloadFile;
        public System.Windows.Forms.Label Label6;
        public System.Windows.Forms.TextBox txtLocal;
        public System.Windows.Forms.TextBox txtRemote;
        public System.Windows.Forms.Label Label5;
        public System.Windows.Forms.TextBox txtPassword;
        public System.Windows.Forms.TextBox txtLogin;
        public System.Windows.Forms.TextBox txtURL;
        public System.Windows.Forms.Label Label3;
        public System.Windows.Forms.Label Label2;
        public System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Button btnSelect;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel StatusBar;
        private System.Windows.Forms.TextBox txtData;
        public System.Windows.Forms.Button btnUploadData;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        public System.Windows.Forms.Label label4;
    }
}

