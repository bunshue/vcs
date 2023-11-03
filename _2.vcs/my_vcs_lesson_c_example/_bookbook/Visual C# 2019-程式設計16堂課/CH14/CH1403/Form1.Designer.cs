namespace CH1403
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.dlgFolderBrowser = new System.Windows.Forms.FolderBrowserDialog();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.msMain = new System.Windows.Forms.MenuStrip();
            this.tsmiFile = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiOpen = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiFolder = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripSeparator();
            this.tsmiEnd = new System.Windows.Forms.ToolStripMenuItem();
            this.dlgOpenFile = new System.Windows.Forms.OpenFileDialog();
            this.msMain.SuspendLayout();
            this.SuspendLayout();
            // 
            // rtxtShow
            // 
            this.rtxtShow.Location = new System.Drawing.Point(32, 54);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(188, 108);
            this.rtxtShow.TabIndex = 3;
            this.rtxtShow.Text = "";
            // 
            // msMain
            // 
            this.msMain.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.msMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiFile});
            this.msMain.Location = new System.Drawing.Point(0, 0);
            this.msMain.Name = "msMain";
            this.msMain.Size = new System.Drawing.Size(264, 24);
            this.msMain.TabIndex = 4;
            this.msMain.Text = "檔案功能表";
            // 
            // tsmiFile
            // 
            this.tsmiFile.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiOpen,
            this.tsmiFolder,
            this.toolStripMenuItem1,
            this.tsmiEnd});
            this.tsmiFile.Name = "tsmiFile";
            this.tsmiFile.Size = new System.Drawing.Size(57, 20);
            this.tsmiFile.Text = "檔案(&F)";
            // 
            // tsmiOpen
            // 
            this.tsmiOpen.Name = "tsmiOpen";
            this.tsmiOpen.Size = new System.Drawing.Size(180, 22);
            this.tsmiOpen.Text = "開啟檔案";
            this.tsmiOpen.Click += new System.EventHandler(this.tsmiOpen_Click);
            // 
            // tsmiFolder
            // 
            this.tsmiFolder.Name = "tsmiFolder";
            this.tsmiFolder.Size = new System.Drawing.Size(180, 22);
            this.tsmiFolder.Text = "瀏覽資料夾";
            this.tsmiFolder.Click += new System.EventHandler(this.tsmiFolder_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(131, 6);
            // 
            // tsmiEnd
            // 
            this.tsmiEnd.Name = "tsmiEnd";
            this.tsmiEnd.Size = new System.Drawing.Size(180, 22);
            this.tsmiEnd.Text = "關閉";
            this.tsmiEnd.Click += new System.EventHandler(this.tsmiEnd_Click);
            // 
            // dlgOpenFile
            // 
            this.dlgOpenFile.FileName = "開啟RTF檔";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(264, 194);
            this.Controls.Add(this.rtxtShow);
            this.Controls.Add(this.msMain);
            this.Name = "Form1";
            this.Text = "CH1403";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.msMain.ResumeLayout(false);
            this.msMain.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.FolderBrowserDialog dlgFolderBrowser;
        private System.Windows.Forms.RichTextBox rtxtShow;
        private System.Windows.Forms.MenuStrip msMain;
        private System.Windows.Forms.ToolStripMenuItem tsmiFile;
        private System.Windows.Forms.ToolStripMenuItem tsmiOpen;
        private System.Windows.Forms.ToolStripMenuItem tsmiFolder;
        private System.Windows.Forms.ToolStripSeparator toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem tsmiEnd;
        private System.Windows.Forms.OpenFileDialog dlgOpenFile;
    }
}

