namespace _4._7_3
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
            this.resultLabel = new System.Windows.Forms.Label();
            this.resultText = new System.Windows.Forms.TextBox();
            this.volumeButton = new System.Windows.Forms.Button();
            this.radiusLabel = new System.Windows.Forms.Label();
            this.radiusText = new System.Windows.Forms.TextBox();
            this.surfaceButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // resultLabel
            // 
            this.resultLabel.AutoSize = true;
            this.resultLabel.Location = new System.Drawing.Point(13, 69);
            this.resultLabel.Name = "resultLabel";
            this.resultLabel.Size = new System.Drawing.Size(68, 12);
            this.resultLabel.TabIndex = 11;
            this.resultLabel.Text = "計算結果為:";
            this.resultLabel.Click += new System.EventHandler(this.resultLabel_Click);
            // 
            // resultText
            // 
            this.resultText.Location = new System.Drawing.Point(87, 66);
            this.resultText.Name = "resultText";
            this.resultText.Size = new System.Drawing.Size(159, 22);
            this.resultText.TabIndex = 10;
            this.resultText.Text = "0";
            this.resultText.TextChanged += new System.EventHandler(this.resultText_TextChanged);
            // 
            // volumeButton
            // 
            this.volumeButton.Location = new System.Drawing.Point(137, 37);
            this.volumeButton.Name = "volumeButton";
            this.volumeButton.Size = new System.Drawing.Size(109, 23);
            this.volumeButton.TabIndex = 9;
            this.volumeButton.Text = "計算球體體積";
            this.volumeButton.UseVisualStyleBackColor = true;
            this.volumeButton.Click += new System.EventHandler(this.volumeButton_Click);
            // 
            // radiusLabel
            // 
            this.radiusLabel.AutoSize = true;
            this.radiusLabel.Location = new System.Drawing.Point(13, 12);
            this.radiusLabel.Name = "radiusLabel";
            this.radiusLabel.Size = new System.Drawing.Size(68, 12);
            this.radiusLabel.TabIndex = 8;
            this.radiusLabel.Text = "請輸入半徑:";
            this.radiusLabel.Click += new System.EventHandler(this.radiusLabel_Click);
            // 
            // radiusText
            // 
            this.radiusText.Location = new System.Drawing.Point(87, 9);
            this.radiusText.Name = "radiusText";
            this.radiusText.Size = new System.Drawing.Size(159, 22);
            this.radiusText.TabIndex = 7;
            this.radiusText.Text = "0";
            this.radiusText.TextChanged += new System.EventHandler(this.radiusText_TextChanged);
            // 
            // surfaceButton
            // 
            this.surfaceButton.Location = new System.Drawing.Point(13, 37);
            this.surfaceButton.Name = "surfaceButton";
            this.surfaceButton.Size = new System.Drawing.Size(118, 23);
            this.surfaceButton.TabIndex = 6;
            this.surfaceButton.Text = "計算球體面積";
            this.surfaceButton.UseVisualStyleBackColor = true;
            this.surfaceButton.Click += new System.EventHandler(this.surfaceButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(265, 95);
            this.Controls.Add(this.resultLabel);
            this.Controls.Add(this.resultText);
            this.Controls.Add(this.volumeButton);
            this.Controls.Add(this.radiusLabel);
            this.Controls.Add(this.radiusText);
            this.Controls.Add(this.surfaceButton);
            this.Name = "Form1";
            this.Text = "球體面積與體積計算程式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label resultLabel;
        private System.Windows.Forms.TextBox resultText;
        private System.Windows.Forms.Button volumeButton;
        private System.Windows.Forms.Label radiusLabel;
        private System.Windows.Forms.TextBox radiusText;
        private System.Windows.Forms.Button surfaceButton;
    }
}

