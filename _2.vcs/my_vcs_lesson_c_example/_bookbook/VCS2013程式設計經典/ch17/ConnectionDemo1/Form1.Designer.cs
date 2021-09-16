namespace ConnectionDemo1
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
            this.btnCnState = new System.Windows.Forms.Button();
            this.txtShow = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnCnState
            // 
            this.btnCnState.Location = new System.Drawing.Point(12, 12);
            this.btnCnState.Name = "btnCnState";
            this.btnCnState.Size = new System.Drawing.Size(75, 31);
            this.btnCnState.TabIndex = 0;
            this.btnCnState.Text = "開啟";
            this.btnCnState.UseVisualStyleBackColor = true;
            this.btnCnState.Click += new System.EventHandler(this.btnCnState_Click);
            // 
            // txtShow
            // 
            this.txtShow.Location = new System.Drawing.Point(12, 60);
            this.txtShow.Multiline = true;
            this.txtShow.Name = "txtShow";
            this.txtShow.Size = new System.Drawing.Size(450, 126);
            this.txtShow.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(475, 206);
            this.Controls.Add(this.txtShow);
            this.Controls.Add(this.btnCnState);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnCnState;
        private System.Windows.Forms.TextBox txtShow;
    }
}

