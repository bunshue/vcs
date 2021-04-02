namespace BankClient
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的程式碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.txtFromBank = new System.Windows.Forms.TextBox();
            this.txtFromAccount = new System.Windows.Forms.TextBox();
            this.txtToBank = new System.Windows.Forms.TextBox();
            this.txtToAccount = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.txtBalance = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(289, 107);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "開始轉賬";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // txtFromBank
            // 
            this.txtFromBank.Location = new System.Drawing.Point(83, 24);
            this.txtFromBank.Name = "txtFromBank";
            this.txtFromBank.Size = new System.Drawing.Size(100, 21);
            this.txtFromBank.TabIndex = 1;
            this.txtFromBank.Text = "Bank_CCB";
            // 
            // txtFromAccount
            // 
            this.txtFromAccount.Location = new System.Drawing.Point(273, 24);
            this.txtFromAccount.Name = "txtFromAccount";
            this.txtFromAccount.Size = new System.Drawing.Size(100, 21);
            this.txtFromAccount.TabIndex = 2;
            this.txtFromAccount.Text = "123456";
            // 
            // txtToBank
            // 
            this.txtToBank.Location = new System.Drawing.Point(83, 67);
            this.txtToBank.Name = "txtToBank";
            this.txtToBank.Size = new System.Drawing.Size(100, 21);
            this.txtToBank.TabIndex = 3;
            this.txtToBank.Text = "Bank_ICBC";
            // 
            // txtToAccount
            // 
            this.txtToAccount.Location = new System.Drawing.Point(273, 67);
            this.txtToAccount.Name = "txtToAccount";
            this.txtToAccount.Size = new System.Drawing.Size(100, 21);
            this.txtToAccount.TabIndex = 4;
            this.txtToAccount.Text = "654321";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 5;
            this.label1.Text = "轉賬銀行：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(202, 33);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 5;
            this.label2.Text = "轉賬賬號：";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 76);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "接收銀行：";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(202, 76);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(65, 12);
            this.label4.TabIndex = 5;
            this.label4.Text = "接收賬號：";
            // 
            // txtBalance
            // 
            this.txtBalance.Location = new System.Drawing.Point(200, 107);
            this.txtBalance.Name = "txtBalance";
            this.txtBalance.Size = new System.Drawing.Size(67, 21);
            this.txtBalance.TabIndex = 6;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(129, 112);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(65, 12);
            this.label5.TabIndex = 5;
            this.label5.Text = "轉賬金額：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(387, 144);
            this.Controls.Add(this.txtBalance);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtToAccount);
            this.Controls.Add(this.txtToBank);
            this.Controls.Add(this.txtFromAccount);
            this.Controls.Add(this.txtFromBank);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "COM+ 客戶端---銀行轉賬";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox txtFromBank;
        private System.Windows.Forms.TextBox txtFromAccount;
        private System.Windows.Forms.TextBox txtToBank;
        private System.Windows.Forms.TextBox txtToAccount;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtBalance;
        private System.Windows.Forms.Label label5;
    }
}

