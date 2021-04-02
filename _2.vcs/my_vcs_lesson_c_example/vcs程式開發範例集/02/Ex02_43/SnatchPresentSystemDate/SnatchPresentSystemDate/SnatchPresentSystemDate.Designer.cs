namespace SnatchPresentSystemDate
{
    partial class SnatchPresentSystemDate
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

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.year = new System.Windows.Forms.NumericUpDown();
            this.month = new System.Windows.Forms.NumericUpDown();
            this.day = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.year)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.month)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.day)).BeginInit();
            this.SuspendLayout();
            // 
            // year
            // 
            this.year.Font = new System.Drawing.Font("mingliu", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.year.Location = new System.Drawing.Point(119, 49);
            this.year.Maximum = new decimal(new int[] {
            134217728,
            0,
            0,
            0});
            this.year.Name = "year";
            this.year.Size = new System.Drawing.Size(44, 21);
            this.year.TabIndex = 0;
            // 
            // month
            // 
            this.month.Font = new System.Drawing.Font("mingliu", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.month.Location = new System.Drawing.Point(197, 49);
            this.month.Name = "month";
            this.month.Size = new System.Drawing.Size(44, 21);
            this.month.TabIndex = 1;
            // 
            // day
            // 
            this.day.Font = new System.Drawing.Font("mingliu", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.day.Location = new System.Drawing.Point(275, 49);
            this.day.Name = "day";
            this.day.Size = new System.Drawing.Size(44, 21);
            this.day.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("mingliu", 10.5F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label1.Location = new System.Drawing.Point(1, 56);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(112, 14);
            this.label1.TabIndex = 3;
            this.label1.Text = "目前系統日期：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("mingliu", 10.5F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.Location = new System.Drawing.Point(169, 56);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 14);
            this.label2.TabIndex = 4;
            this.label2.Text = "年";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("mingliu", 10.5F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label3.Location = new System.Drawing.Point(247, 56);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(22, 14);
            this.label3.TabIndex = 4;
            this.label3.Text = "月";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("mingliu", 10.5F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label4.Location = new System.Drawing.Point(325, 56);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(22, 14);
            this.label4.TabIndex = 4;
            this.label4.Text = "日";
            // 
            // SnatchPresentSystemDate
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(366, 145);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.day);
            this.Controls.Add(this.month);
            this.Controls.Add(this.year);
            this.Name = "SnatchPresentSystemDate";
            this.Text = "在NumericUpDown控制元件中顯示目前系統日期";
            this.Load += new System.EventHandler(this.SnatchPresentSystemDate_Load);
            ((System.ComponentModel.ISupportInitialize)(this.year)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.month)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.day)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown year;
        private System.Windows.Forms.NumericUpDown month;
        private System.Windows.Forms.NumericUpDown day;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
    }
}

