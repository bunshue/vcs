namespace _15._3_1
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
            this.candidateButton1 = new System.Windows.Forms.Button();
            this.candidateText1 = new System.Windows.Forms.TextBox();
            this.candidateButton2 = new System.Windows.Forms.Button();
            this.candidateButton3 = new System.Windows.Forms.Button();
            this.candidateText2 = new System.Windows.Forms.TextBox();
            this.candidateText3 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // candidateButton1
            // 
            this.candidateButton1.Location = new System.Drawing.Point(12, 242);
            this.candidateButton1.Name = "candidateButton1";
            this.candidateButton1.Size = new System.Drawing.Size(75, 23);
            this.candidateButton1.TabIndex = 0;
            this.candidateButton1.Text = "候選人1";
            this.candidateButton1.UseVisualStyleBackColor = true;
            this.candidateButton1.Click += new System.EventHandler(this.candidateButton1_Click);
            // 
            // candidateText1
            // 
            this.candidateText1.BackColor = System.Drawing.Color.Yellow;
            this.candidateText1.Location = new System.Drawing.Point(12, 272);
            this.candidateText1.Name = "candidateText1";
            this.candidateText1.Size = new System.Drawing.Size(75, 22);
            this.candidateText1.TabIndex = 1;
            this.candidateText1.Text = "0";
            // 
            // candidateButton2
            // 
            this.candidateButton2.Location = new System.Drawing.Point(93, 242);
            this.candidateButton2.Name = "candidateButton2";
            this.candidateButton2.Size = new System.Drawing.Size(75, 23);
            this.candidateButton2.TabIndex = 2;
            this.candidateButton2.Text = "候選人2";
            this.candidateButton2.UseVisualStyleBackColor = true;
            this.candidateButton2.Click += new System.EventHandler(this.candidateButton2_Click);
            // 
            // candidateButton3
            // 
            this.candidateButton3.Location = new System.Drawing.Point(174, 242);
            this.candidateButton3.Name = "candidateButton3";
            this.candidateButton3.Size = new System.Drawing.Size(75, 23);
            this.candidateButton3.TabIndex = 3;
            this.candidateButton3.Text = "候選人3";
            this.candidateButton3.UseVisualStyleBackColor = true;
            this.candidateButton3.Click += new System.EventHandler(this.candidateButton3_Click);
            // 
            // candidateText2
            // 
            this.candidateText2.BackColor = System.Drawing.Color.Green;
            this.candidateText2.Location = new System.Drawing.Point(93, 271);
            this.candidateText2.Name = "candidateText2";
            this.candidateText2.Size = new System.Drawing.Size(75, 22);
            this.candidateText2.TabIndex = 4;
            this.candidateText2.Text = "0";
            // 
            // candidateText3
            // 
            this.candidateText3.BackColor = System.Drawing.Color.Red;
            this.candidateText3.Location = new System.Drawing.Point(174, 271);
            this.candidateText3.Name = "candidateText3";
            this.candidateText3.Size = new System.Drawing.Size(75, 22);
            this.candidateText3.TabIndex = 5;
            this.candidateText3.Text = "0";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(265, 306);
            this.Controls.Add(this.candidateText3);
            this.Controls.Add(this.candidateText2);
            this.Controls.Add(this.candidateButton3);
            this.Controls.Add(this.candidateButton2);
            this.Controls.Add(this.candidateText1);
            this.Controls.Add(this.candidateButton1);
            this.Name = "Form1";
            this.Text = "投票比例繪圖程式";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button candidateButton1;
        private System.Windows.Forms.TextBox candidateText1;
        private System.Windows.Forms.Button candidateButton2;
        private System.Windows.Forms.Button candidateButton3;
        private System.Windows.Forms.TextBox candidateText2;
        private System.Windows.Forms.TextBox candidateText3;
    }
}

