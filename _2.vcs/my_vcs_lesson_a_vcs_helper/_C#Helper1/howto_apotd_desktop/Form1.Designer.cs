namespace howto_apotd_desktop
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
            this.label1 = new System.Windows.Forms.Label();
            this.txtLastLoadTime = new System.Windows.Forms.TextBox();
            this.txtLastUrl = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.wbrApotd = new System.Windows.Forms.WebBrowser();
            this.tmrDownload = new System.Windows.Forms.Timer(this.components);
            this.lstMessages = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Last Loaded:";
            // 
            // txtLastLoadTime
            // 
            this.txtLastLoadTime.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtLastLoadTime.Location = new System.Drawing.Point(87, 11);
            this.txtLastLoadTime.Name = "txtLastLoadTime";
            this.txtLastLoadTime.ReadOnly = true;
            this.txtLastLoadTime.Size = new System.Drawing.Size(585, 22);
            this.txtLastLoadTime.TabIndex = 1;
            // 
            // txtLastUrl
            // 
            this.txtLastUrl.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtLastUrl.Location = new System.Drawing.Point(87, 35);
            this.txtLastUrl.Name = "txtLastUrl";
            this.txtLastUrl.ReadOnly = true;
            this.txtLastUrl.Size = new System.Drawing.Size(585, 22);
            this.txtLastUrl.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 38);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Last URL:";
            // 
            // wbrApotd
            // 
            this.wbrApotd.Location = new System.Drawing.Point(189, 22);
            this.wbrApotd.MinimumSize = new System.Drawing.Size(20, 18);
            this.wbrApotd.Name = "wbrApotd";
            this.wbrApotd.Size = new System.Drawing.Size(55, 46);
            this.wbrApotd.TabIndex = 6;
            this.wbrApotd.DocumentCompleted += new System.Windows.Forms.WebBrowserDocumentCompletedEventHandler(this.wbrApotd_DocumentCompleted);
            // 
            // tmrDownload
            // 
            this.tmrDownload.Tick += new System.EventHandler(this.tmrDownload_Tick);
            // 
            // lstMessages
            // 
            this.lstMessages.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.lstMessages.FormattingEnabled = true;
            this.lstMessages.IntegralHeight = false;
            this.lstMessages.ItemHeight = 12;
            this.lstMessages.Location = new System.Drawing.Point(12, 59);
            this.lstMessages.Name = "lstMessages";
            this.lstMessages.Size = new System.Drawing.Size(660, 310);
            this.lstMessages.TabIndex = 7;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 380);
            this.Controls.Add(this.lstMessages);
            this.Controls.Add(this.wbrApotd);
            this.Controls.Add(this.txtLastUrl);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtLastLoadTime);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_apotd_desktop";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtLastLoadTime;
        private System.Windows.Forms.TextBox txtLastUrl;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.WebBrowser wbrApotd;
        private System.Windows.Forms.Timer tmrDownload;
        private System.Windows.Forms.ListBox lstMessages;
    }
}

