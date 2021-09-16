namespace Guess
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
            this.lblMsg.Location = new System.Drawing.Point(30, 142);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(104, 19);
            this.lblMsg.TabIndex = 27;
            this.lblMsg.Text = "共猜了 2 次";
            // 
            // btnEnd
            // 
            this.btnEnd.Location = new System.Drawing.Point(216, 177);
            this.btnEnd.Name = "btnEnd";
            this.btnEnd.Size = new System.Drawing.Size(75, 30);
            this.btnEnd.TabIndex = 26;
            this.btnEnd.Text = "結束";
            this.btnEnd.UseVisualStyleBackColor = true;
            this.btnEnd.Click += new System.EventHandler(this.btnEnd_Click);
            // 
            // btnAgain
            // 
            this.btnAgain.Location = new System.Drawing.Point(124, 177);
            this.btnAgain.Name = "btnAgain";
            this.btnAgain.Size = new System.Drawing.Size(75, 30);
            this.btnAgain.TabIndex = 25;
            this.btnAgain.Text = "重玩";
            this.btnAgain.UseVisualStyleBackColor = true;
            this.btnAgain.Click += new System.EventHandler(this.btnAgain_Click);
            // 
            // btnOk
            // 
            this.btnOk.Location = new System.Drawing.Point(33, 177);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(75, 30);
            this.btnOk.TabIndex = 24;
            this.btnOk.Text = "確定";
            this.btnOk.UseVisualStyleBackColor = true;
            this.btnOk.Click += new System.EventHandler(this.btnOk_Click);
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(30, 102);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(104, 19);
            this.Label2.TabIndex = 23;
            this.Label2.Text = "要猜的數字";
            // 
            // txtGuess
            // 
            this.txtGuess.Location = new System.Drawing.Point(140, 99);
            this.txtGuess.Name = "txtGuess";
            this.txtGuess.Size = new System.Drawing.Size(100, 29);
            this.txtGuess.TabIndex = 22;
            // 
            // lblTitle
            // 
            this.lblTitle.AutoSize = true;
            this.lblTitle.Font = new System.Drawing.Font("新細明體", 26.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblTitle.Location = new System.Drawing.Point(51, 30);
            this.lblTitle.Name = "lblTitle";
            this.lblTitle.Size = new System.Drawing.Size(254, 44);
            this.lblTitle.TabIndex = 21;
            this.lblTitle.Text = "654 < ? < 956";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(347, 241);
            this.Controls.Add(this.lblMsg);
            this.Controls.Add(this.btnEnd);
            this.Controls.Add(this.btnAgain);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtGuess);
            this.Controls.Add(this.lblTitle);
            this.Font = new System.Drawing.Font("新細明體", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
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

