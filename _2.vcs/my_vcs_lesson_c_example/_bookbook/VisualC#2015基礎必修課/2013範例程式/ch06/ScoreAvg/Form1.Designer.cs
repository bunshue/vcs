namespace ScoreAvg
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
            this.lblMsg = new System.Windows.Forms.Label();
            this.btnAvg = new System.Windows.Forms.Button();
            this.btnInput = new System.Windows.Forms.Button();
            this.txtScore = new System.Windows.Forms.TextBox();
            this.lblN = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblMsg
            // 
            this.lblMsg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.lblMsg.Location = new System.Drawing.Point(19, 58);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(214, 109);
            this.lblMsg.TabIndex = 14;
            // 
            // btnAvg
            // 
            this.btnAvg.Location = new System.Drawing.Point(256, 71);
            this.btnAvg.Name = "btnAvg";
            this.btnAvg.Size = new System.Drawing.Size(75, 23);
            this.btnAvg.TabIndex = 12;
            this.btnAvg.Text = "計算平均";
            this.btnAvg.UseVisualStyleBackColor = true;
            this.btnAvg.Click += new System.EventHandler(this.btnAvg_Click);
            // 
            // btnInput
            // 
            this.btnInput.Location = new System.Drawing.Point(256, 17);
            this.btnInput.Name = "btnInput";
            this.btnInput.Size = new System.Drawing.Size(75, 23);
            this.btnInput.TabIndex = 13;
            this.btnInput.Text = "輸入成績";
            this.btnInput.UseVisualStyleBackColor = true;
            this.btnInput.Click += new System.EventHandler(this.btnInput_Click);
            // 
            // txtScore
            // 
            this.txtScore.Location = new System.Drawing.Point(133, 17);
            this.txtScore.Name = "txtScore";
            this.txtScore.Size = new System.Drawing.Size(100, 22);
            this.txtScore.TabIndex = 11;
            // 
            // lblN
            // 
            this.lblN.AutoSize = true;
            this.lblN.Location = new System.Drawing.Point(19, 20);
            this.lblN.Name = "lblN";
            this.lblN.Size = new System.Drawing.Size(33, 12);
            this.lblN.TabIndex = 10;
            this.lblN.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(351, 185);
            this.Controls.Add(this.lblMsg);
            this.Controls.Add(this.btnAvg);
            this.Controls.Add(this.btnInput);
            this.Controls.Add(this.txtScore);
            this.Controls.Add(this.lblN);
            this.Name = "Form1";
            this.Text = "輸入成績並計算平均程式";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblMsg;
        private System.Windows.Forms.Button btnAvg;
        private System.Windows.Forms.Button btnInput;
        private System.Windows.Forms.TextBox txtScore;
        private System.Windows.Forms.Label lblN;
    }
}

