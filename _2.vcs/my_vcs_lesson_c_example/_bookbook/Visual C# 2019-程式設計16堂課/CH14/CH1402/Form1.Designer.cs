namespace CH1402
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
            this.btnSave = new System.Windows.Forms.Button();
            this.dlgSaveFile = new System.Windows.Forms.SaveFileDialog();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(99, 120);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(104, 32);
            this.btnSave.TabIndex = 3;
            this.btnSave.Text = "儲存檔案";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // dlgSaveFile
            // 
            this.dlgSaveFile.FileName = "Demo02";
            // 
            // rtxtShow
            // 
            this.rtxtShow.Dock = System.Windows.Forms.DockStyle.Top;
            this.rtxtShow.Location = new System.Drawing.Point(0, 0);
            this.rtxtShow.Margin = new System.Windows.Forms.Padding(4);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(324, 96);
            this.rtxtShow.TabIndex = 2;
            this.rtxtShow.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(324, 179);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.rtxtShow);
            this.Name = "Form1";
            this.Text = "CH1402";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.SaveFileDialog dlgSaveFile;
        private System.Windows.Forms.RichTextBox rtxtShow;
    }
}

