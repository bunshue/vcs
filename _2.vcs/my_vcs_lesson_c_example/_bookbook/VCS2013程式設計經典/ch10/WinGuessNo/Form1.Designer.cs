namespace WinGuessNo
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
            this.btnEnd = new System.Windows.Forms.Button();
            this.btnAgain = new System.Windows.Forms.Button();
            this.btnOk = new System.Windows.Forms.Button();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtGuess = new System.Windows.Forms.TextBox();
            this.lblTitle = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblMsg
            // 
            this.lblMsg.AutoSize = true;
            this.lblMsg.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblMsg.Location = new System.Drawing.Point(43, 135);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(88, 16);
            this.lblMsg.TabIndex = 34;
            this.lblMsg.Text = "共猜了 2 次";

            // 
            // btnEnd
            // 
            this.btnEnd.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEnd.Location = new System.Drawing.Point(229, 170);
            this.btnEnd.Name = "btnEnd";
            this.btnEnd.Size = new System.Drawing.Size(75, 30);
            this.btnEnd.TabIndex = 33;
            this.btnEnd.Text = "結束";
            this.btnEnd.UseVisualStyleBackColor = true;
            this.btnEnd.Click += new System.EventHandler(this.btnEnd_Click);
            // 
            // btnAgain
            // 
            this.btnAgain.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnAgain.Location = new System.Drawing.Point(137, 170);
            this.btnAgain.Name = "btnAgain";
            this.btnAgain.Size = new System.Drawing.Size(75, 30);
            this.btnAgain.TabIndex = 32;
            this.btnAgain.Text = "重玩";
            this.btnAgain.UseVisualStyleBackColor = true;
            this.btnAgain.Click += new System.EventHandler(this.btnAgain_Click);
            // 
            // btnOk
            // 
            this.btnOk.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnOk.Location = new System.Drawing.Point(46, 170);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(75, 30);
            this.btnOk.TabIndex = 31;
            this.btnOk.Text = "確定";
            this.btnOk.UseVisualStyleBackColor = true;
            this.btnOk.Click += new System.EventHandler(this.btnOk_Click);
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label2.Location = new System.Drawing.Point(43, 95);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(88, 16);
            this.Label2.TabIndex = 30;
            this.Label2.Text = "要猜的數字";
     
            // 
            // txtGuess
            // 
            this.txtGuess.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.txtGuess.Location = new System.Drawing.Point(153, 92);
            this.txtGuess.Name = "txtGuess";
            this.txtGuess.Size = new System.Drawing.Size(100, 27);
            this.txtGuess.TabIndex = 29;

            // 
            // lblTitle
            // 
            this.lblTitle.AutoSize = true;
            this.lblTitle.Font = new System.Drawing.Font("新細明體", 26.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblTitle.Location = new System.Drawing.Point(64, 23);
            this.lblTitle.Name = "lblTitle";
            this.lblTitle.Size = new System.Drawing.Size(168, 35);
            this.lblTitle.TabIndex = 28;
            this.lblTitle.Text = "1 < ? < 100";
    
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(350, 233);
            this.Controls.Add(this.lblMsg);
            this.Controls.Add(this.btnEnd);
            this.Controls.Add(this.btnAgain);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtGuess);
            this.Controls.Add(this.lblTitle);
            this.Name = "Form1";
            this.Text = "猜數字遊戲";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label lblMsg;
        internal System.Windows.Forms.Button btnEnd;
        internal System.Windows.Forms.Button btnAgain;
        internal System.Windows.Forms.Button btnOk;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtGuess;
        internal System.Windows.Forms.Label lblTitle;
    }
}

