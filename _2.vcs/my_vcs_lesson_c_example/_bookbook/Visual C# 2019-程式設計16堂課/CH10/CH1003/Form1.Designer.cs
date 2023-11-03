namespace CH1003
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
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
            this.txtNumber = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnOK = new System.Windows.Forms.Button();
            this.btnPopup = new System.Windows.Forms.Button();
            this.btnFlat = new System.Windows.Forms.Button();
            this.btnStandard = new System.Windows.Forms.Button();
            this.lblShow = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtNumber
            // 
            this.txtNumber.Location = new System.Drawing.Point(191, 107);
            this.txtNumber.Name = "txtNumber";
            this.txtNumber.Size = new System.Drawing.Size(100, 22);
            this.txtNumber.TabIndex = 13;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(108, 106);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 12;
            this.label1.Text = "數字：";
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(27, 100);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 36);
            this.btnOK.TabIndex = 11;
            this.btnOK.Text = "確認";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // btnPopup
            // 
            this.btnPopup.Enabled = false;
            this.btnPopup.Location = new System.Drawing.Point(205, 56);
            this.btnPopup.Name = "btnPopup";
            this.btnPopup.Size = new System.Drawing.Size(89, 37);
            this.btnPopup.TabIndex = 10;
            this.btnPopup.Text = "停駐";
            this.btnPopup.UseVisualStyleBackColor = true;
            this.btnPopup.MouseHover += new System.EventHandler(this.btnPopup_MouseHover);
            // 
            // btnFlat
            // 
            this.btnFlat.Enabled = false;
            this.btnFlat.Location = new System.Drawing.Point(113, 56);
            this.btnFlat.Name = "btnFlat";
            this.btnFlat.Size = new System.Drawing.Size(89, 37);
            this.btnFlat.TabIndex = 9;
            this.btnFlat.Text = "平面";
            this.btnFlat.UseVisualStyleBackColor = true;
            this.btnFlat.MouseMove += new System.Windows.Forms.MouseEventHandler(this.btnFlat_MouseMove);
            // 
            // btnStandard
            // 
            this.btnStandard.Enabled = false;
            this.btnStandard.Location = new System.Drawing.Point(21, 56);
            this.btnStandard.Name = "btnStandard";
            this.btnStandard.Size = new System.Drawing.Size(89, 37);
            this.btnStandard.TabIndex = 8;
            this.btnStandard.Text = "標準";
            this.btnStandard.UseVisualStyleBackColor = true;
            this.btnStandard.Enter += new System.EventHandler(this.btnStandard_MouseEnter);
            // 
            // lblShow
            // 
            this.lblShow.AutoSize = true;
            this.lblShow.Location = new System.Drawing.Point(27, 14);
            this.lblShow.Name = "lblShow";
            this.lblShow.Size = new System.Drawing.Size(33, 12);
            this.lblShow.TabIndex = 7;
            this.lblShow.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(320, 152);
            this.Controls.Add(this.txtNumber);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.btnPopup);
            this.Controls.Add(this.btnFlat);
            this.Controls.Add(this.btnStandard);
            this.Controls.Add(this.lblShow);
            this.Name = "Form1";
            this.Text = "CH1003";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtNumber;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.Button btnPopup;
        private System.Windows.Forms.Button btnFlat;
        private System.Windows.Forms.Button btnStandard;
        private System.Windows.Forms.Label lblShow;
    }
}

