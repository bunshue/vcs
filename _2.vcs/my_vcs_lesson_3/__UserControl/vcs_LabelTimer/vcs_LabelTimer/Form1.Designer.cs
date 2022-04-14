namespace vcs_LabelTimer
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
            this.labelTimer1 = new vcs_LabelTimer.LabelTimer();
            this.SuspendLayout();
            // 
            // labelTimer1
            // 
            this.labelTimer1.Location = new System.Drawing.Point(94, 161);
            this.labelTimer1.Name = "labelTimer1";
            this.labelTimer1.Size = new System.Drawing.Size(435, 150);
            this.labelTimer1.TabIndex = 0;
            this.labelTimer1.USER_Color_Background = System.Drawing.Color.Pink;
            this.labelTimer1.USER_Color_Foreground = System.Drawing.Color.Black;
            this.labelTimer1.USER_use_24hr = vcs_LabelTimer.LabelTimer.USE24HR.YES;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(680, 521);
            this.Controls.Add(this.labelTimer1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private LabelTimer labelTimer1;
    }
}

