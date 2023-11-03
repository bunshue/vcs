namespace CH1103
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
            this.linkLb2 = new System.Windows.Forms.LinkLabel();
            this.linkLb1 = new System.Windows.Forms.LinkLabel();
            this.SuspendLayout();
            // 
            // linkLb2
            // 
            this.linkLb2.AutoSize = true;
            this.linkLb2.LinkBehavior = System.Windows.Forms.LinkBehavior.HoverUnderline;
            this.linkLb2.LinkVisited = true;
            this.linkLb2.Location = new System.Drawing.Point(37, 87);
            this.linkLb2.Name = "linkLb2";
            this.linkLb2.Size = new System.Drawing.Size(41, 12);
            this.linkLb2.TabIndex = 3;
            this.linkLb2.TabStop = true;
            this.linkLb2.Text = "小算盤";
            this.linkLb2.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLb2_LinkClicked);
            // 
            // linkLb1
            // 
            this.linkLb1.AutoSize = true;
            this.linkLb1.LinkArea = new System.Windows.Forms.LinkArea(4, 4);
            this.linkLb1.Location = new System.Drawing.Point(37, 38);
            this.linkLb1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.linkLb1.Name = "linkLb1";
            this.linkLb1.Size = new System.Drawing.Size(165, 19);
            this.linkLb1.TabIndex = 2;
            this.linkLb1.TabStop = true;
            this.linkLb1.Text = "歡迎來到維基百科，快意巡覽";
            this.linkLb1.UseCompatibleTextRendering = true;
            this.linkLb1.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLb1_LinkClicked);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(250, 126);
            this.Controls.Add(this.linkLb2);
            this.Controls.Add(this.linkLb1);
            this.Name = "Form1";
            this.Text = "CH1103";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.LinkLabel linkLb2;
        private System.Windows.Forms.LinkLabel linkLb1;
    }
}

