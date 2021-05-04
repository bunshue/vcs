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
            this.computeButton = new System.Windows.Forms.Button();
            this.integerLabel1 = new System.Windows.Forms.Label();
            this.integerText1 = new System.Windows.Forms.TextBox();
            this.integerLabel2 = new System.Windows.Forms.Label();
            this.integerText2 = new System.Windows.Forms.TextBox();
            this.gcdLabel = new System.Windows.Forms.Label();
            this.gcdText = new System.Windows.Forms.TextBox();
            this.lcmLabel = new System.Windows.Forms.Label();
            this.lcmText = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // computeButton
            // 
            this.computeButton.Location = new System.Drawing.Point(12, 34);
            this.computeButton.Name = "computeButton";
            this.computeButton.Size = new System.Drawing.Size(348, 23);
            this.computeButton.TabIndex = 0;
            this.computeButton.Text = "計算結果";
            this.computeButton.UseVisualStyleBackColor = true;
            this.computeButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // integerLabel1
            // 
            this.integerLabel1.AutoSize = true;
            this.integerLabel1.Location = new System.Drawing.Point(30, 9);
            this.integerLabel1.Name = "integerLabel1";
            this.integerLabel1.Size = new System.Drawing.Size(47, 12);
            this.integerLabel1.TabIndex = 1;
            this.integerLabel1.Text = "正整數1";
            // 
            // integerText1
            // 
            this.integerText1.Location = new System.Drawing.Point(83, 6);
            this.integerText1.Name = "integerText1";
            this.integerText1.Size = new System.Drawing.Size(100, 22);
            this.integerText1.TabIndex = 2;
            // 
            // integerLabel2
            // 
            this.integerLabel2.AutoSize = true;
            this.integerLabel2.Location = new System.Drawing.Point(207, 9);
            this.integerLabel2.Name = "integerLabel2";
            this.integerLabel2.Size = new System.Drawing.Size(47, 12);
            this.integerLabel2.TabIndex = 3;
            this.integerLabel2.Text = "正整數2";
            // 
            // integerText2
            // 
            this.integerText2.Location = new System.Drawing.Point(260, 6);
            this.integerText2.Name = "integerText2";
            this.integerText2.Size = new System.Drawing.Size(100, 22);
            this.integerText2.TabIndex = 4;
            // 
            // gcdLabel
            // 
            this.gcdLabel.AutoSize = true;
            this.gcdLabel.Location = new System.Drawing.Point(12, 66);
            this.gcdLabel.Name = "gcdLabel";
            this.gcdLabel.Size = new System.Drawing.Size(65, 12);
            this.gcdLabel.TabIndex = 5;
            this.gcdLabel.Text = "最大公因數";
            // 
            // gcdText
            // 
            this.gcdText.Location = new System.Drawing.Point(83, 63);
            this.gcdText.Name = "gcdText";
            this.gcdText.Size = new System.Drawing.Size(100, 22);
            this.gcdText.TabIndex = 6;
            // 
            // lcmLabel
            // 
            this.lcmLabel.AutoSize = true;
            this.lcmLabel.Location = new System.Drawing.Point(189, 66);
            this.lcmLabel.Name = "lcmLabel";
            this.lcmLabel.Size = new System.Drawing.Size(65, 12);
            this.lcmLabel.TabIndex = 7;
            this.lcmLabel.Text = "最小公倍數";
            // 
            // lcmText
            // 
            this.lcmText.Location = new System.Drawing.Point(260, 63);
            this.lcmText.Name = "lcmText";
            this.lcmText.Size = new System.Drawing.Size(100, 22);
            this.lcmText.TabIndex = 8;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(372, 92);
            this.Controls.Add(this.lcmText);
            this.Controls.Add(this.lcmLabel);
            this.Controls.Add(this.gcdText);
            this.Controls.Add(this.gcdLabel);
            this.Controls.Add(this.integerText2);
            this.Controls.Add(this.integerLabel2);
            this.Controls.Add(this.integerText1);
            this.Controls.Add(this.integerLabel1);
            this.Controls.Add(this.computeButton);
            this.Name = "Form1";
            this.Text = "求最大公因數和最小公倍數";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button computeButton;
        private System.Windows.Forms.Label integerLabel1;
        private System.Windows.Forms.TextBox integerText1;
        private System.Windows.Forms.Label integerLabel2;
        private System.Windows.Forms.TextBox integerText2;
        private System.Windows.Forms.Label gcdLabel;
        private System.Windows.Forms.TextBox gcdText;
        private System.Windows.Forms.Label lcmLabel;
        private System.Windows.Forms.TextBox lcmText;






    }
}

