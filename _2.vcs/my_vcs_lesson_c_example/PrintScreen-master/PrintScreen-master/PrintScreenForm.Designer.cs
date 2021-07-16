namespace PrintScreen
{
    partial class PrintScreenForm
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(PrintScreenForm));
            this.chkSound = new System.Windows.Forms.CheckBox();
            this.btnBrowse = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.tbFilePath = new System.Windows.Forms.TextBox();
            this.folderBrowserDialog = new System.Windows.Forms.FolderBrowserDialog();
            this.notifyIcon = new System.Windows.Forms.NotifyIcon(this.components);
            this.timerKeyboard = new System.Windows.Forms.Timer(this.components);
            this.chkBalloonTips = new System.Windows.Forms.CheckBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // chkSound
            // 
            this.chkSound.AutoSize = true;
            this.chkSound.Checked = true;
            this.chkSound.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkSound.Location = new System.Drawing.Point(20, 55);
            this.chkSound.Name = "chkSound";
            this.chkSound.Size = new System.Drawing.Size(54, 16);
            this.chkSound.TabIndex = 14;
            this.chkSound.Text = "Sound";
            this.chkSound.UseVisualStyleBackColor = true;
            this.chkSound.Click += new System.EventHandler(this.chkSound_Click);
            // 
            // btnBrowse
            // 
            this.btnBrowse.Location = new System.Drawing.Point(496, 12);
            this.btnBrowse.Name = "btnBrowse";
            this.btnBrowse.Size = new System.Drawing.Size(59, 23);
            this.btnBrowse.TabIndex = 13;
            this.btnBrowse.Text = "Browse";
            this.btnBrowse.UseVisualStyleBackColor = true;
            this.btnBrowse.Click += new System.EventHandler(this.btnBrowse_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(18, 15);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(51, 12);
            this.label3.TabIndex = 12;
            this.label3.Text = "File Path :";
            // 
            // tbFilePath
            // 
            this.tbFilePath.Enabled = false;
            this.tbFilePath.Location = new System.Drawing.Point(75, 12);
            this.tbFilePath.Name = "tbFilePath";
            this.tbFilePath.Size = new System.Drawing.Size(415, 22);
            this.tbFilePath.TabIndex = 11;
            // 
            // notifyIcon
            // 
            this.notifyIcon.BalloonTipText = "Print Screen";
            this.notifyIcon.Icon = ((System.Drawing.Icon)(resources.GetObject("notifyIcon.Icon")));
            this.notifyIcon.Text = "notifyIcon";
            this.notifyIcon.Visible = true;
            this.notifyIcon.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.notifyIcon_MouseDoubleClick);
            // 
            // timerKeyboard
            // 
            this.timerKeyboard.Enabled = true;
            this.timerKeyboard.Tick += new System.EventHandler(this.timerKeyboard_Tick);
            // 
            // chkBalloonTips
            // 
            this.chkBalloonTips.AutoSize = true;
            this.chkBalloonTips.Checked = true;
            this.chkBalloonTips.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkBalloonTips.Location = new System.Drawing.Point(92, 55);
            this.chkBalloonTips.Name = "chkBalloonTips";
            this.chkBalloonTips.Size = new System.Drawing.Size(84, 16);
            this.chkBalloonTips.TabIndex = 15;
            this.chkBalloonTips.Text = "Balloon Tips";
            this.chkBalloonTips.UseVisualStyleBackColor = true;
            this.chkBalloonTips.Click += new System.EventHandler(this.chkBalloonTips_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(20, 124);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(535, 319);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // PrintScreenForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(567, 455);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.chkBalloonTips);
            this.Controls.Add(this.chkSound);
            this.Controls.Add(this.btnBrowse);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.tbFilePath);
            this.Name = "PrintScreenForm";
            this.Text = "Print Screen";
            this.TopMost = true;
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.PrintScreenForm_FormClosed);
            this.Load += new System.EventHandler(this.PrintScreenForm_Load);
            this.Resize += new System.EventHandler(this.PrintScreenForm_Resize);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkSound;
        private System.Windows.Forms.Button btnBrowse;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbFilePath;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog;
        private System.Windows.Forms.NotifyIcon notifyIcon;
        private System.Windows.Forms.Timer timerKeyboard;
        private System.Windows.Forms.CheckBox chkBalloonTips;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

