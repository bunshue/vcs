namespace vcs_PictureSlideShow
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
            this.btnS = new System.Windows.Forms.Button();
            this.lblNo = new System.Windows.Forms.Label();
            this.btnN = new System.Windows.Forms.Button();
            this.btnP = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // btnS
            // 
            this.btnS.Location = new System.Drawing.Point(212, 538);
            this.btnS.Name = "btnS";
            this.btnS.Size = new System.Drawing.Size(64, 23);
            this.btnS.TabIndex = 14;
            this.btnS.Text = "縮小";
            this.btnS.UseVisualStyleBackColor = true;
            this.btnS.Click += new System.EventHandler(this.btnS_Click);
            // 
            // lblNo
            // 
            this.lblNo.AutoSize = true;
            this.lblNo.Location = new System.Drawing.Point(87, 543);
            this.lblNo.Name = "lblNo";
            this.lblNo.Size = new System.Drawing.Size(33, 12);
            this.lblNo.TabIndex = 13;
            this.lblNo.Text = "label1";
            // 
            // btnN
            // 
            this.btnN.Location = new System.Drawing.Point(136, 538);
            this.btnN.Name = "btnN";
            this.btnN.Size = new System.Drawing.Size(64, 23);
            this.btnN.TabIndex = 12;
            this.btnN.Text = "下一張";
            this.btnN.UseVisualStyleBackColor = true;
            this.btnN.Click += new System.EventHandler(this.btnN_Click);
            // 
            // btnP
            // 
            this.btnP.Location = new System.Drawing.Point(16, 538);
            this.btnP.Name = "btnP";
            this.btnP.Size = new System.Drawing.Size(64, 23);
            this.btnP.TabIndex = 11;
            this.btnP.Text = "上一張";
            this.btnP.UseVisualStyleBackColor = true;
            this.btnP.Click += new System.EventHandler(this.btnP_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(16, 13);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(497, 481);
            this.pictureBox1.TabIndex = 10;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(726, 605);
            this.Controls.Add(this.btnS);
            this.Controls.Add(this.lblNo);
            this.Controls.Add(this.btnN);
            this.Controls.Add(this.btnP);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnS;
        private System.Windows.Forms.Label lblNo;
        private System.Windows.Forms.Button btnN;
        private System.Windows.Forms.Button btnP;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

