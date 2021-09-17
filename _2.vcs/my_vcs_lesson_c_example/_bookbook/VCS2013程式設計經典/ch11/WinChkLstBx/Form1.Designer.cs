namespace WinChkLstBx
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
            this.btnCls = new System.Windows.Forms.Button();
            this.lblShow = new System.Windows.Forms.Label();
            this.btnCheckLot = new System.Windows.Forms.Button();
            this.chkListLot = new System.Windows.Forms.CheckedListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnCls
            // 
            this.btnCls.Location = new System.Drawing.Point(124, 333);
            this.btnCls.Margin = new System.Windows.Forms.Padding(2);
            this.btnCls.Name = "btnCls";
            this.btnCls.Size = new System.Drawing.Size(74, 35);
            this.btnCls.TabIndex = 11;
            this.btnCls.Text = "清除";
            this.btnCls.UseVisualStyleBackColor = true;
            this.btnCls.Click += new System.EventHandler(this.btnCls_Click);
            // 
            // lblShow
            // 
            this.lblShow.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.lblShow.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblShow.Location = new System.Drawing.Point(28, 227);
            this.lblShow.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblShow.Name = "lblShow";
            this.lblShow.Size = new System.Drawing.Size(262, 87);
            this.lblShow.TabIndex = 10;
            this.lblShow.Text = "lblShow";
            // 
            // btnCheckLot
            // 
            this.btnCheckLot.Location = new System.Drawing.Point(29, 333);
            this.btnCheckLot.Margin = new System.Windows.Forms.Padding(2);
            this.btnCheckLot.Name = "btnCheckLot";
            this.btnCheckLot.Size = new System.Drawing.Size(74, 35);
            this.btnCheckLot.TabIndex = 8;
            this.btnCheckLot.Text = "對獎";
            this.btnCheckLot.UseVisualStyleBackColor = true;
            this.btnCheckLot.Click += new System.EventHandler(this.btnCheckLot_Click);
            // 
            // chkListLot
            // 
            this.chkListLot.FormattingEnabled = true;
            this.chkListLot.Location = new System.Drawing.Point(29, 56);
            this.chkListLot.Margin = new System.Windows.Forms.Padding(2);
            this.chkListLot.Name = "chkListLot";
            this.chkListLot.Size = new System.Drawing.Size(261, 144);
            this.chkListLot.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 16);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(154, 15);
            this.label1.TabIndex = 6;
            this.label1.Text = "大樂透-請選擇6個號碼";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(324, 391);
            this.Controls.Add(this.btnCls);
            this.Controls.Add(this.lblShow);
            this.Controls.Add(this.btnCheckLot);
            this.Controls.Add(this.chkListLot);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnCls;
        private System.Windows.Forms.Label lblShow;
        private System.Windows.Forms.Button btnCheckLot;
        private System.Windows.Forms.CheckedListBox chkListLot;
        private System.Windows.Forms.Label label1;
    }
}

