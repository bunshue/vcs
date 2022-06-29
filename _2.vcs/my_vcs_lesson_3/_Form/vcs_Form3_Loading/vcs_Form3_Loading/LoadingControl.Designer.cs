namespace vcs_Form3_Loading
{
    partial class LoadingControl
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
            this.lbl_caption = new System.Windows.Forms.Label();
            this.lbl_description = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lbl_caption
            // 
            this.lbl_caption.AutoSize = true;
            this.lbl_caption.Location = new System.Drawing.Point(72, 147);
            this.lbl_caption.Name = "lbl_caption";
            this.lbl_caption.Size = new System.Drawing.Size(33, 12);
            this.lbl_caption.TabIndex = 3;
            this.lbl_caption.Text = "label1";
            // 
            // lbl_description
            // 
            this.lbl_description.AutoSize = true;
            this.lbl_description.Location = new System.Drawing.Point(72, 90);
            this.lbl_description.Name = "lbl_description";
            this.lbl_description.Size = new System.Drawing.Size(33, 12);
            this.lbl_description.TabIndex = 2;
            this.lbl_description.Text = "label1";
            // 
            // LoadingControl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.lbl_caption);
            this.Controls.Add(this.lbl_description);
            this.Name = "LoadingControl";
            this.Text = "LoadingControl";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.LoadingControl_FormClosing);
            this.Load += new System.EventHandler(this.LoadingControl_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lbl_caption;
        private System.Windows.Forms.Label lbl_description;
    }
}