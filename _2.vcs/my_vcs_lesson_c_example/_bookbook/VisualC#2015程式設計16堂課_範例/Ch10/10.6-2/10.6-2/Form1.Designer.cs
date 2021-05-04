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
            this.stepButton = new System.Windows.Forms.Button();
            this.numText1 = new System.Windows.Forms.TextBox();
            this.numText2 = new System.Windows.Forms.TextBox();
            this.numText3 = new System.Windows.Forms.TextBox();
            this.numText4 = new System.Windows.Forms.TextBox();
            this.numText5 = new System.Windows.Forms.TextBox();
            this.numText6 = new System.Windows.Forms.TextBox();
            this.numText7 = new System.Windows.Forms.TextBox();
            this.numText8 = new System.Windows.Forms.TextBox();
            this.targetLabel = new System.Windows.Forms.Label();
            this.targetText = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // stepButton
            // 
            this.stepButton.Location = new System.Drawing.Point(424, 12);
            this.stepButton.Name = "stepButton";
            this.stepButton.Size = new System.Drawing.Size(75, 23);
            this.stepButton.TabIndex = 0;
            this.stepButton.Text = "開始";
            this.stepButton.UseVisualStyleBackColor = true;
            this.stepButton.Click += new System.EventHandler(this.stepButton_Click);
            // 
            // numText1
            // 
            this.numText1.Location = new System.Drawing.Point(12, 12);
            this.numText1.Name = "numText1";
            this.numText1.Size = new System.Drawing.Size(32, 22);
            this.numText1.TabIndex = 1;
            this.numText1.Text = "0";
            // 
            // numText2
            // 
            this.numText2.Location = new System.Drawing.Point(50, 12);
            this.numText2.Name = "numText2";
            this.numText2.Size = new System.Drawing.Size(32, 22);
            this.numText2.TabIndex = 2;
            this.numText2.Text = "0";
            // 
            // numText3
            // 
            this.numText3.Location = new System.Drawing.Point(88, 12);
            this.numText3.Name = "numText3";
            this.numText3.Size = new System.Drawing.Size(32, 22);
            this.numText3.TabIndex = 3;
            this.numText3.Text = "0";
            // 
            // numText4
            // 
            this.numText4.Location = new System.Drawing.Point(126, 12);
            this.numText4.Name = "numText4";
            this.numText4.Size = new System.Drawing.Size(32, 22);
            this.numText4.TabIndex = 4;
            this.numText4.Text = "0";
            // 
            // numText5
            // 
            this.numText5.Location = new System.Drawing.Point(164, 12);
            this.numText5.Name = "numText5";
            this.numText5.Size = new System.Drawing.Size(32, 22);
            this.numText5.TabIndex = 5;
            this.numText5.Text = "0";
            // 
            // numText6
            // 
            this.numText6.Location = new System.Drawing.Point(202, 12);
            this.numText6.Name = "numText6";
            this.numText6.Size = new System.Drawing.Size(32, 22);
            this.numText6.TabIndex = 6;
            this.numText6.Text = "0";
            // 
            // numText7
            // 
            this.numText7.Location = new System.Drawing.Point(240, 12);
            this.numText7.Name = "numText7";
            this.numText7.Size = new System.Drawing.Size(32, 22);
            this.numText7.TabIndex = 7;
            this.numText7.Text = "0";
            // 
            // numText8
            // 
            this.numText8.Location = new System.Drawing.Point(278, 12);
            this.numText8.Name = "numText8";
            this.numText8.Size = new System.Drawing.Size(32, 22);
            this.numText8.TabIndex = 8;
            this.numText8.Text = "0";
            // 
            // targetLabel
            // 
            this.targetLabel.AutoSize = true;
            this.targetLabel.Location = new System.Drawing.Point(316, 17);
            this.targetLabel.Name = "targetLabel";
            this.targetLabel.Size = new System.Drawing.Size(68, 12);
            this.targetLabel.TabIndex = 9;
            this.targetLabel.Text = "搜尋目標是:";
            // 
            // targetText
            // 
            this.targetText.Location = new System.Drawing.Point(386, 12);
            this.targetText.Name = "targetText";
            this.targetText.Size = new System.Drawing.Size(32, 22);
            this.targetText.TabIndex = 10;
            this.targetText.Text = "0";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(507, 46);
            this.Controls.Add(this.targetText);
            this.Controls.Add(this.targetLabel);
            this.Controls.Add(this.numText8);
            this.Controls.Add(this.numText7);
            this.Controls.Add(this.numText6);
            this.Controls.Add(this.numText5);
            this.Controls.Add(this.numText4);
            this.Controls.Add(this.numText3);
            this.Controls.Add(this.numText2);
            this.Controls.Add(this.numText1);
            this.Controls.Add(this.stepButton);
            this.Name = "Form1";
            this.Text = "二分搜尋法演示";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button stepButton;
        private System.Windows.Forms.TextBox numText1;
        private System.Windows.Forms.TextBox numText2;
        private System.Windows.Forms.TextBox numText3;
        private System.Windows.Forms.TextBox numText4;
        private System.Windows.Forms.TextBox numText5;
        private System.Windows.Forms.TextBox numText6;
        private System.Windows.Forms.TextBox numText7;
        private System.Windows.Forms.TextBox numText8;
        private System.Windows.Forms.Label targetLabel;
        private System.Windows.Forms.TextBox targetText;











    }
}

