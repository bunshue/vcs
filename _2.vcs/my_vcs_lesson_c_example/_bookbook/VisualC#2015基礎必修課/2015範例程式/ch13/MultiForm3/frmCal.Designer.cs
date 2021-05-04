namespace MultiForm3
{
    partial class frmCal
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
            this.radMonth = new System.Windows.Forms.RadioButton();
            this.radYear = new System.Windows.Forms.RadioButton();
            this.SuspendLayout();
            // 
            // radMonth
            // 
            this.radMonth.AutoSize = true;
            this.radMonth.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radMonth.Location = new System.Drawing.Point(76, 100);
            this.radMonth.Name = "radMonth";
            this.radMonth.Size = new System.Drawing.Size(85, 19);
            this.radMonth.TabIndex = 12;
            this.radMonth.Text = "每月計息";
            this.radMonth.UseVisualStyleBackColor = true;
            // 
            // radYear
            // 
            this.radYear.AutoSize = true;
            this.radYear.Checked = true;
            this.radYear.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radYear.Location = new System.Drawing.Point(76, 58);
            this.radYear.Name = "radYear";
            this.radYear.Size = new System.Drawing.Size(85, 19);
            this.radYear.TabIndex = 11;
            this.radYear.TabStop = true;
            this.radYear.Text = "每年計息";
            this.radYear.UseVisualStyleBackColor = true;
            // 
            // frmCal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(235, 140);
            this.Controls.Add(this.radMonth);
            this.Controls.Add(this.radYear);
            this.Name = "frmCal";
            this.Text = "選擇計算方式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.RadioButton radMonth;
        internal System.Windows.Forms.RadioButton radYear;
    }
}

