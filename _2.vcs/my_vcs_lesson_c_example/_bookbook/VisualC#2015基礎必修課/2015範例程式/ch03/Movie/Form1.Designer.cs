namespace Movie
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.txtQtyF = new System.Windows.Forms.TextBox();
            this.lblSumF = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.lblPriceF = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtQtyF
            // 
            this.txtQtyF.Location = new System.Drawing.Point(129, 59);
            this.txtQtyF.Name = "txtQtyF";
            this.txtQtyF.Size = new System.Drawing.Size(55, 22);
            this.txtQtyF.TabIndex = 16;
            this.txtQtyF.TextChanged += new System.EventHandler(this.txtQtyF_TextChanged);
            this.txtQtyF.Enter += new System.EventHandler(this.txtQtyF_Enter);
            // 
            // lblSumF
            // 
            this.lblSumF.BackColor = System.Drawing.SystemColors.Control;
            this.lblSumF.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblSumF.Location = new System.Drawing.Point(202, 59);
            this.lblSumF.Name = "lblSumF";
            this.lblSumF.Size = new System.Drawing.Size(58, 22);
            this.lblSumF.TabIndex = 13;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(200, 26);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(29, 12);
            this.label3.TabIndex = 14;
            this.label3.Text = "金額";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(137, 26);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 12);
            this.label2.TabIndex = 9;
            this.label2.Text = "張數";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(26, 62);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(29, 12);
            this.label4.TabIndex = 5;
            this.label4.Text = "全票";
            // 
            // lblPriceF
            // 
            this.lblPriceF.AutoSize = true;
            this.lblPriceF.Location = new System.Drawing.Point(81, 62);
            this.lblPriceF.Name = "lblPriceF";
            this.lblPriceF.Size = new System.Drawing.Size(23, 12);
            this.lblPriceF.TabIndex = 7;
            this.lblPriceF.Text = "250";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(72, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 12);
            this.label1.TabIndex = 8;
            this.label1.Text = "單價";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 113);
            this.Controls.Add(this.txtQtyF);
            this.Controls.Add(this.lblSumF);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.lblPriceF);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "電影院售票程式";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtQtyF;
        private System.Windows.Forms.Label lblSumF;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label lblPriceF;
        private System.Windows.Forms.Label label1;
    }
}

