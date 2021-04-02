namespace AddHyperLink
{
    partial class AddHyperLink
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if(disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "文字內容：";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(38, 36);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(283, 195);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "明日科技：http://www.mingrisoft.com/\n新浪：http://www.sina.com/\n雅虎：http://tw.yahoo.com\nGo" +
                "ogle：http://www.google.com/";
            this.richTextBox1.LinkClicked += new System.Windows.Forms.LinkClickedEventHandler(this.richTextBox1_LinkClicked);
            // 
            // AddHyperLink
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(336, 266);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label1);
            this.Name = "AddHyperLink";
            this.Text = "在RichTextBox控制元件上新增超連結文字";
            this.Load += new System.EventHandler(this.AddHyperLink_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

