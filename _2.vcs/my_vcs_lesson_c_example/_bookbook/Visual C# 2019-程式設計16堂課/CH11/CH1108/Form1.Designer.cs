namespace CH1108
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
            this.lstSubject = new System.Windows.Forms.ListBox();
            this.lstChoice = new System.Windows.Forms.ListBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lstSubject
            // 
            this.lstSubject.FormattingEnabled = true;
            this.lstSubject.ItemHeight = 12;
            this.lstSubject.Location = new System.Drawing.Point(164, 46);
            this.lstSubject.Name = "lstSubject";
            this.lstSubject.Size = new System.Drawing.Size(132, 76);
            this.lstSubject.TabIndex = 7;
            // 
            // lstChoice
            // 
            this.lstChoice.FormattingEnabled = true;
            this.lstChoice.ItemHeight = 12;
            this.lstChoice.Location = new System.Drawing.Point(26, 46);
            this.lstChoice.Name = "lstChoice";
            this.lstChoice.Size = new System.Drawing.Size(132, 76);
            this.lstChoice.TabIndex = 6;
            this.lstChoice.SelectedIndexChanged += new System.EventHandler(this.lstChoice_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(164, 17);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(77, 12);
            this.label2.TabIndex = 5;
            this.label2.Text = "選取的科目：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(26, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 12);
            this.label1.TabIndex = 4;
            this.label1.Text = "請選擇科目：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(323, 148);
            this.Controls.Add(this.lstSubject);
            this.Controls.Add(this.lstChoice);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "CH1108";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox lstSubject;
        private System.Windows.Forms.ListBox lstChoice;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

