namespace CH1102
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
            this.btnOpen = new System.Windows.Forms.Button();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(124, 101);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(75, 33);
            this.btnSave.TabIndex = 5;
            this.btnSave.Text = "儲存";
            this.btnSave.UseVisualStyleBackColor = true;
            this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
            // 
            // btnOpen
            // 
            this.btnOpen.Location = new System.Drawing.Point(37, 101);
            this.btnOpen.Name = "btnOpen";
            this.btnOpen.Size = new System.Drawing.Size(80, 33);
            this.btnOpen.TabIndex = 4;
            this.btnOpen.Text = "開啟";
            this.btnOpen.UseVisualStyleBackColor = true;
            this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
            // 
            // rtxtShow
            // 
            this.rtxtShow.Location = new System.Drawing.Point(0, 0);
            this.rtxtShow.Margin = new System.Windows.Forms.Padding(4);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(269, 94);
            this.rtxtShow.TabIndex = 3;
            this.rtxtShow.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(268, 146);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.btnOpen);
            this.Controls.Add(this.rtxtShow);
            this.Name = "Form1";
            this.Text = "CH1102";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnOpen;
        private System.Windows.Forms.RichTextBox rtxtShow;
    }
}

