namespace Vocation
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
            this.btnOk = new System.Windows.Forms.Button();
            this.mcaVacation = new System.Windows.Forms.MonthCalendar();
            this.lblVacation = new System.Windows.Forms.Label();
            this.nudYears = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.nudYears)).BeginInit();
            this.SuspendLayout();
            // 
            // btnOk
            // 
            this.btnOk.Location = new System.Drawing.Point(170, 289);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(75, 30);
            this.btnOk.TabIndex = 14;
            this.btnOk.Text = "確定";
            this.btnOk.UseVisualStyleBackColor = true;
            this.btnOk.Click += new System.EventHandler(this.btnOk_Click);
            // 
            // mcaVacation
            // 
            this.mcaVacation.Location = new System.Drawing.Point(25, 106);
            this.mcaVacation.Name = "mcaVacation";
            this.mcaVacation.TabIndex = 13;
            // 
            // lblVacation
            // 
            this.lblVacation.AutoSize = true;
            this.lblVacation.Location = new System.Drawing.Point(23, 74);
            this.lblVacation.Name = "lblVacation";
            this.lblVacation.Size = new System.Drawing.Size(33, 12);
            this.lblVacation.TabIndex = 12;
            this.lblVacation.Text = "label2";
            // 
            // nudYears
            // 
            this.nudYears.Location = new System.Drawing.Point(131, 22);
            this.nudYears.Name = "nudYears";
            this.nudYears.Size = new System.Drawing.Size(99, 22);
            this.nudYears.TabIndex = 11;
            this.nudYears.ValueChanged += new System.EventHandler(this.nudYears_ValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(101, 12);
            this.label1.TabIndex = 10;
            this.label1.Text = "請輸入工作年資：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(269, 341);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.mcaVacation);
            this.Controls.Add(this.lblVacation);
            this.Controls.Add(this.nudYears);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.nudYears)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnOk;
        private System.Windows.Forms.MonthCalendar mcaVacation;
        private System.Windows.Forms.Label lblVacation;
        private System.Windows.Forms.NumericUpDown nudYears;
        private System.Windows.Forms.Label label1;
    }
}

