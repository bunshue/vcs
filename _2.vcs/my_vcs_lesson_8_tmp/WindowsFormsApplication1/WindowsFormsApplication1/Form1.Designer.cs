namespace WindowsFormsApplication1
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
            this.PicLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // PicLabel
            // 
            this.PicLabel.AutoSize = true;
            this.PicLabel.Location = new System.Drawing.Point(115, 155);
            this.PicLabel.Name = "PicLabel";
            this.PicLabel.Size = new System.Drawing.Size(33, 12);
            this.PicLabel.TabIndex = 0;
            this.PicLabel.Text = "label1";
            this.PicLabel.MouseDown += new System.Windows.Forms.MouseEventHandler(this.PicLabel_MouseDown);
            this.PicLabel.MouseMove += new System.Windows.Forms.MouseEventHandler(this.PicLabel_MouseMove);
            this.PicLabel.MouseUp += new System.Windows.Forms.MouseEventHandler(this.PicLabel_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(758, 583);
            this.Controls.Add(this.PicLabel);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label PicLabel;
    }
}

