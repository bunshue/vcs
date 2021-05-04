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
            this.logList = new System.Windows.Forms.ListBox();
            this.numText1 = new System.Windows.Forms.TextBox();
            this.numText2 = new System.Windows.Forms.TextBox();
            this.numText3 = new System.Windows.Forms.TextBox();
            this.numText4 = new System.Windows.Forms.TextBox();
            this.guessButton = new System.Windows.Forms.Button();
            this.logLabel = new System.Windows.Forms.Label();
            this.resetButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // logList
            // 
            this.logList.FormattingEnabled = true;
            this.logList.ItemHeight = 12;
            this.logList.Location = new System.Drawing.Point(12, 81);
            this.logList.Name = "logList";
            this.logList.Size = new System.Drawing.Size(118, 160);
            this.logList.TabIndex = 0;
            // 
            // numText1
            // 
            this.numText1.Location = new System.Drawing.Point(12, 12);
            this.numText1.Name = "numText1";
            this.numText1.Size = new System.Drawing.Size(25, 22);
            this.numText1.TabIndex = 1;
            // 
            // numText2
            // 
            this.numText2.Location = new System.Drawing.Point(43, 12);
            this.numText2.Name = "numText2";
            this.numText2.Size = new System.Drawing.Size(25, 22);
            this.numText2.TabIndex = 2;
            // 
            // numText3
            // 
            this.numText3.Location = new System.Drawing.Point(74, 12);
            this.numText3.Name = "numText3";
            this.numText3.Size = new System.Drawing.Size(25, 22);
            this.numText3.TabIndex = 3;
            // 
            // numText4
            // 
            this.numText4.Location = new System.Drawing.Point(105, 12);
            this.numText4.Name = "numText4";
            this.numText4.Size = new System.Drawing.Size(25, 22);
            this.numText4.TabIndex = 4;
            // 
            // guessButton
            // 
            this.guessButton.Location = new System.Drawing.Point(12, 40);
            this.guessButton.Name = "guessButton";
            this.guessButton.Size = new System.Drawing.Size(118, 23);
            this.guessButton.TabIndex = 5;
            this.guessButton.Text = "Guess!";
            this.guessButton.UseVisualStyleBackColor = true;
            this.guessButton.Click += new System.EventHandler(this.guessButton_Click);
            // 
            // logLabel
            // 
            this.logLabel.AutoSize = true;
            this.logLabel.Location = new System.Drawing.Point(12, 66);
            this.logLabel.Name = "logLabel";
            this.logLabel.Size = new System.Drawing.Size(53, 12);
            this.logLabel.TabIndex = 6;
            this.logLabel.Text = "猜測記錄";
            // 
            // resetButton
            // 
            this.resetButton.Location = new System.Drawing.Point(14, 250);
            this.resetButton.Name = "resetButton";
            this.resetButton.Size = new System.Drawing.Size(118, 23);
            this.resetButton.TabIndex = 7;
            this.resetButton.Text = "重開新局";
            this.resetButton.UseVisualStyleBackColor = true;
            this.resetButton.Click += new System.EventHandler(this.resetButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(145, 285);
            this.Controls.Add(this.resetButton);
            this.Controls.Add(this.logLabel);
            this.Controls.Add(this.guessButton);
            this.Controls.Add(this.numText4);
            this.Controls.Add(this.numText3);
            this.Controls.Add(this.numText2);
            this.Controls.Add(this.numText1);
            this.Controls.Add(this.logList);
            this.Name = "Form1";
            this.Text = "1A2B猜數字遊戲";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox logList;
        private System.Windows.Forms.TextBox numText1;
        private System.Windows.Forms.TextBox numText2;
        private System.Windows.Forms.TextBox numText3;
        private System.Windows.Forms.TextBox numText4;
        private System.Windows.Forms.Button guessButton;
        private System.Windows.Forms.Label logLabel;
        private System.Windows.Forms.Button resetButton;
    }
}

