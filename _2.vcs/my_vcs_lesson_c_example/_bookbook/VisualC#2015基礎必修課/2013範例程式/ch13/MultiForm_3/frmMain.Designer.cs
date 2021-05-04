namespace MultiForm_4
{
    partial class frmMain
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
            this.txtMoney = new System.Windows.Forms.TextBox();
            this.txtYear = new System.Windows.Forms.TextBox();
            this.txtRate = new System.Windows.Forms.TextBox();
            this.btnOpenCal = new System.Windows.Forms.Button();
            this.btnOpen = new System.Windows.Forms.Button();
            this.lblShow = new System.Windows.Forms.Label();
            this.Label3 = new System.Windows.Forms.Label();
            this.Label2 = new System.Windows.Forms.Label();
            this.Label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtMoney
            // 
            this.txtMoney.Location = new System.Drawing.Point(109, 19);
            this.txtMoney.Name = "txtMoney";
            this.txtMoney.Size = new System.Drawing.Size(79, 22);
            this.txtMoney.TabIndex = 48;
            // 
            // txtYear
            // 
            this.txtYear.Location = new System.Drawing.Point(109, 100);
            this.txtYear.Name = "txtYear";
            this.txtYear.Size = new System.Drawing.Size(79, 22);
            this.txtYear.TabIndex = 47;
            // 
            // txtRate
            // 
            this.txtRate.Location = new System.Drawing.Point(110, 56);
            this.txtRate.Name = "txtRate";
            this.txtRate.Size = new System.Drawing.Size(78, 22);
            this.txtRate.TabIndex = 46;
            // 
            // btnOpenCal
            // 
            this.btnOpenCal.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnOpenCal.Location = new System.Drawing.Point(214, 63);
            this.btnOpenCal.Name = "btnOpenCal";
            this.btnOpenCal.Size = new System.Drawing.Size(97, 25);
            this.btnOpenCal.TabIndex = 45;
            this.btnOpenCal.Text = "使用小算盤";
            this.btnOpenCal.UseVisualStyleBackColor = true;
            this.btnOpenCal.Click += new System.EventHandler(this.btnOpenCal_Click);
            // 
            // btnOpen
            // 
            this.btnOpen.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnOpen.Location = new System.Drawing.Point(214, 19);
            this.btnOpen.Name = "btnOpen";
            this.btnOpen.Size = new System.Drawing.Size(97, 25);
            this.btnOpen.TabIndex = 44;
            this.btnOpen.Text = "開啟試算";
            this.btnOpen.UseVisualStyleBackColor = true;
            this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
            // 
            // lblShow
            // 
            this.lblShow.AutoSize = true;
            this.lblShow.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblShow.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblShow.Location = new System.Drawing.Point(22, 156);
            this.lblShow.Name = "lblShow";
            this.lblShow.Size = new System.Drawing.Size(56, 17);
            this.lblShow.TabIndex = 43;
            this.lblShow.Text = "lblShow";
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label3.Location = new System.Drawing.Point(22, 107);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(82, 15);
            this.Label3.TabIndex = 42;
            this.Label3.Text = "幾年後領回";
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label2.Location = new System.Drawing.Point(22, 63);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(82, 15);
            this.Label2.TabIndex = 41;
            this.Label2.Text = "輸入年利率";
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label1.Location = new System.Drawing.Point(22, 19);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(82, 15);
            this.Label1.TabIndex = 40;
            this.Label1.Text = "請輸入本金";
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(334, 192);
            this.Controls.Add(this.txtMoney);
            this.Controls.Add(this.txtYear);
            this.Controls.Add(this.txtRate);
            this.Controls.Add(this.btnOpenCal);
            this.Controls.Add(this.btnOpen);
            this.Controls.Add(this.lblShow);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.Label1);
            this.Name = "frmMain";
            this.Text = "複利率本利和試算";
            this.Load += new System.EventHandler(this.frmMain_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.TextBox txtMoney;
        private System.Windows.Forms.TextBox txtYear;
        private System.Windows.Forms.TextBox txtRate;
        internal System.Windows.Forms.Button btnOpenCal;
        internal System.Windows.Forms.Button btnOpen;
        internal System.Windows.Forms.Label lblShow;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.Label Label1;
    }
}

