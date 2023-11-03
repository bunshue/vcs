namespace CH1404
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
            this.dlgColor = new System.Windows.Forms.ColorDialog();
            this.dlgFont = new System.Windows.Forms.FontDialog();
            this.btnFont = new System.Windows.Forms.Button();
            this.btnColor = new System.Windows.Forms.Button();
            this.rtxtShow = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // btnFont
            // 
            this.btnFont.Location = new System.Drawing.Point(219, 100);
            this.btnFont.Margin = new System.Windows.Forms.Padding(4);
            this.btnFont.Name = "btnFont";
            this.btnFont.Size = new System.Drawing.Size(100, 33);
            this.btnFont.TabIndex = 5;
            this.btnFont.Text = "字型";
            this.btnFont.UseVisualStyleBackColor = true;
            this.btnFont.Click += new System.EventHandler(this.btnFont_Click);
            // 
            // btnColor
            // 
            this.btnColor.Location = new System.Drawing.Point(219, 22);
            this.btnColor.Margin = new System.Windows.Forms.Padding(4);
            this.btnColor.Name = "btnColor";
            this.btnColor.Size = new System.Drawing.Size(100, 33);
            this.btnColor.TabIndex = 4;
            this.btnColor.Text = "色彩";
            this.btnColor.UseVisualStyleBackColor = true;
            this.btnColor.Click += new System.EventHandler(this.btnColor_Click);
            // 
            // rtxtShow
            // 
            this.rtxtShow.Dock = System.Windows.Forms.DockStyle.Left;
            this.rtxtShow.Location = new System.Drawing.Point(0, 0);
            this.rtxtShow.Margin = new System.Windows.Forms.Padding(4);
            this.rtxtShow.Name = "rtxtShow";
            this.rtxtShow.Size = new System.Drawing.Size(192, 160);
            this.rtxtShow.TabIndex = 3;
            this.rtxtShow.Text = "Pride and Prejudice";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(343, 160);
            this.Controls.Add(this.btnFont);
            this.Controls.Add(this.btnColor);
            this.Controls.Add(this.rtxtShow);
            this.Name = "Form1";
            this.Text = "CH1404";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ColorDialog dlgColor;
        private System.Windows.Forms.FontDialog dlgFont;
        private System.Windows.Forms.Button btnFont;
        private System.Windows.Forms.Button btnColor;
        private System.Windows.Forms.RichTextBox rtxtShow;
    }
}

