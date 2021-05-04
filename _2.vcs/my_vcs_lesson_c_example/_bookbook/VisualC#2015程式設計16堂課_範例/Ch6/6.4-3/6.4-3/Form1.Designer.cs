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
            this.inputLabel = new System.Windows.Forms.Label();
            this.inputText = new System.Windows.Forms.TextBox();
            this.judgeButton = new System.Windows.Forms.Button();
            this.resultText = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // inputLabel
            // 
            this.inputLabel.AutoSize = true;
            this.inputLabel.Location = new System.Drawing.Point(12, 9);
            this.inputLabel.Name = "inputLabel";
            this.inputLabel.Size = new System.Drawing.Size(32, 12);
            this.inputLabel.TabIndex = 0;
            this.inputLabel.Text = "數字:";
            // 
            // inputText
            // 
            this.inputText.Location = new System.Drawing.Point(51, 6);
            this.inputText.Name = "inputText";
            this.inputText.Size = new System.Drawing.Size(100, 22);
            this.inputText.TabIndex = 1;
            this.inputText.Text = "0";
            // 
            // judgeButton
            // 
            this.judgeButton.Location = new System.Drawing.Point(157, 5);
            this.judgeButton.Name = "judgeButton";
            this.judgeButton.Size = new System.Drawing.Size(75, 23);
            this.judgeButton.TabIndex = 2;
            this.judgeButton.Text = "判斷!";
            this.judgeButton.UseVisualStyleBackColor = true;
            this.judgeButton.Click += new System.EventHandler(this.judgeButton_Click);
            // 
            // resultText
            // 
            this.resultText.Location = new System.Drawing.Point(238, 6);
            this.resultText.Name = "resultText";
            this.resultText.Size = new System.Drawing.Size(100, 22);
            this.resultText.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(351, 36);
            this.Controls.Add(this.resultText);
            this.Controls.Add(this.judgeButton);
            this.Controls.Add(this.inputText);
            this.Controls.Add(this.inputLabel);
            this.Name = "Form1";
            this.Text = "質數判斷";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label inputLabel;
        private System.Windows.Forms.TextBox inputText;
        private System.Windows.Forms.Button judgeButton;
        private System.Windows.Forms.TextBox resultText;







    }
}

