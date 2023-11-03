namespace CH1302
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
            this.tsMain = new System.Windows.Forms.ToolStrip();
            this.tsbOpen = new System.Windows.Forms.ToolStripButton();
            this.tsbSave = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.tscobFont = new System.Windows.Forms.ToolStripComboBox();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.tsMain.SuspendLayout();
            this.SuspendLayout();
            // 
            // tsMain
            // 
            this.tsMain.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.tsMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsbOpen,
            this.tsbSave,
            this.toolStripSeparator1,
            this.tscobFont});
            this.tsMain.Location = new System.Drawing.Point(0, 0);
            this.tsMain.Name = "tsMain";
            this.tsMain.Size = new System.Drawing.Size(329, 29);
            this.tsMain.TabIndex = 2;
            this.tsMain.Text = "toolStrip1";
            // 
            // tsbOpen
            // 
            this.tsbOpen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.tsbOpen.Image = global::CH1302.Properties.Resources._012;
            this.tsbOpen.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.tsbOpen.Name = "tsbOpen";
            this.tsbOpen.Size = new System.Drawing.Size(26, 26);
            this.tsbOpen.Text = "開啟檔案";
            this.tsbOpen.Click += new System.EventHandler(this.tsbOpen_Click);
            // 
            // tsbSave
            // 
            this.tsbSave.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.tsbSave.Image = global::CH1302.Properties.Resources._005;
            this.tsbSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.tsbSave.Name = "tsbSave";
            this.tsbSave.Size = new System.Drawing.Size(26, 26);
            this.tsbSave.Text = "儲存檔案";
            this.tsbSave.Click += new System.EventHandler(this.tsbSave_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(6, 29);
            // 
            // tscobFont
            // 
            this.tscobFont.Items.AddRange(new object[] {
            "Arial",
            "Garamond",
            "Times New Roman"});
            this.tscobFont.Name = "tscobFont";
            this.tscobFont.Size = new System.Drawing.Size(120, 29);
            this.tscobFont.Text = "Arial";
            this.tscobFont.ToolTipText = "設定字型";
            this.tscobFont.SelectedIndexChanged += new System.EventHandler(this.tscobFont_SelectedIndexChanged);
            // 
            // rtxtShow
            // 
            this.rtxtShow.Dock = System.Windows.Forms.DockStyle.Fill;
            this.rtxtShow.Location = new System.Drawing.Point(0, 0);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(329, 197);
            this.rtxtShow.TabIndex = 3;
            this.rtxtShow.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(329, 197);
            this.Controls.Add(this.tsMain);
            this.Controls.Add(this.rtxtShow);
            this.Name = "Form1";
            this.Text = "CH1302";
            this.tsMain.ResumeLayout(false);
            this.tsMain.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ToolStrip tsMain;
        private System.Windows.Forms.ToolStripButton tsbOpen;
        private System.Windows.Forms.ToolStripButton tsbSave;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripComboBox tscobFont;
        private System.Windows.Forms.RichTextBox rtxtShow;
    }
}

