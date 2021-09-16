namespace xCh1_1_2_11
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
            this.fileDialog = new System.Windows.Forms.OpenFileDialog();
            this.btnLoad = new System.Windows.Forms.Button();
            this.lblFileName = new System.Windows.Forms.Label();
            this.picboxImage = new System.Windows.Forms.PictureBox();
            this.toolTips = new System.Windows.Forms.ToolTip(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picboxImage)).BeginInit();
            this.SuspendLayout();
            // 
            // fileDialog
            // 
            this.fileDialog.FileName = "openFileDialog1";
            // 
            // btnLoad
            // 
            this.btnLoad.Location = new System.Drawing.Point(12, 12);
            this.btnLoad.Name = "btnLoad";
            this.btnLoad.Size = new System.Drawing.Size(75, 23);
            this.btnLoad.TabIndex = 0;
            this.btnLoad.Text = "载入圖片(&L)";
            this.toolTips.SetToolTip(this.btnLoad, "按此鈕可載入圖片");
            this.btnLoad.UseVisualStyleBackColor = true;
            this.btnLoad.Click += new System.EventHandler(this.btnLoad_Click);
            // 
            // lblFileName
            // 
            this.lblFileName.AutoSize = true;
            this.lblFileName.Location = new System.Drawing.Point(93, 17);
            this.lblFileName.Name = "lblFileName";
            this.lblFileName.Size = new System.Drawing.Size(0, 14);
            this.lblFileName.TabIndex = 1;
            this.toolTips.SetToolTip(this.lblFileName, "目前圖片的檔案名稱");
            // 
            // picboxImage
            // 
            this.picboxImage.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.picboxImage.Cursor = System.Windows.Forms.Cursors.Hand;
            this.picboxImage.Location = new System.Drawing.Point(12, 52);
            this.picboxImage.Name = "picboxImage";
            this.picboxImage.Size = new System.Drawing.Size(419, 247);
            this.picboxImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picboxImage.TabIndex = 2;
            this.picboxImage.TabStop = false;
            // 
            // myForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(443, 311);
            this.Controls.Add(this.picboxImage);
            this.Controls.Add(this.lblFileName);
            this.Controls.Add(this.btnLoad);
            this.Name = "myForm";
            this.Text = "圖片瀏覽";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picboxImage)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.OpenFileDialog fileDialog;
        private System.Windows.Forms.Button btnLoad;
        private System.Windows.Forms.Label lblFileName;
        private System.Windows.Forms.PictureBox picboxImage;
        private System.Windows.Forms.ToolTip toolTips;
    }
}

