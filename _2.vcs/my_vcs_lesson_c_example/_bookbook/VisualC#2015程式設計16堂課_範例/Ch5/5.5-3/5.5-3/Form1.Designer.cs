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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.monthLabel = new System.Windows.Forms.Label();
            this.monthText = new System.Windows.Forms.TextBox();
            this.convertButton = new System.Windows.Forms.Button();
            this.seasonLabel = new System.Windows.Forms.Label();
            this.seasonText = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // monthLabel
            // 
            this.monthLabel.AutoSize = true;
            this.monthLabel.Location = new System.Drawing.Point(12, 9);
            this.monthLabel.Name = "monthLabel";
            this.monthLabel.Size = new System.Drawing.Size(32, 12);
            this.monthLabel.TabIndex = 0;
            this.monthLabel.Text = "月份:";
            // 
            // monthText
            // 
            this.monthText.Location = new System.Drawing.Point(51, 6);
            this.monthText.Name = "monthText";
            this.monthText.Size = new System.Drawing.Size(28, 22);
            this.monthText.TabIndex = 1;
            // 
            // convertButton
            // 
            this.convertButton.Location = new System.Drawing.Point(85, 5);
            this.convertButton.Name = "convertButton";
            this.convertButton.Size = new System.Drawing.Size(75, 23);
            this.convertButton.TabIndex = 2;
            this.convertButton.Text = "轉換!";
            this.convertButton.UseVisualStyleBackColor = true;
            this.convertButton.Click += new System.EventHandler(this.convertButton_Click);
            // 
            // seasonLabel
            // 
            this.seasonLabel.AutoSize = true;
            this.seasonLabel.Location = new System.Drawing.Point(166, 10);
            this.seasonLabel.Name = "seasonLabel";
            this.seasonLabel.Size = new System.Drawing.Size(44, 12);
            this.seasonLabel.TabIndex = 3;
            this.seasonLabel.Text = "季節為:";
            // 
            // seasonText
            // 
            this.seasonText.Location = new System.Drawing.Point(216, 6);
            this.seasonText.Name = "seasonText";
            this.seasonText.Size = new System.Drawing.Size(61, 22);
            this.seasonText.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(289, 36);
            this.Controls.Add(this.seasonText);
            this.Controls.Add(this.seasonLabel);
            this.Controls.Add(this.convertButton);
            this.Controls.Add(this.monthText);
            this.Controls.Add(this.monthLabel);
            this.Name = "Form1";
            this.Text = "季節判斷程式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label monthLabel;
        private System.Windows.Forms.TextBox monthText;
        private System.Windows.Forms.Button convertButton;
        private System.Windows.Forms.Label seasonLabel;
        private System.Windows.Forms.TextBox seasonText;






    }
}

