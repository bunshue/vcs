namespace WinListCombo
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
            this.label8 = new System.Windows.Forms.Label();
            this.btnEnd = new System.Windows.Forms.Button();
            this.btnAdd = new System.Windows.Forms.Button();
            this.lstJob = new System.Windows.Forms.ListBox();
            this.rdbF = new System.Windows.Forms.RadioButton();
            this.rdbM = new System.Windows.Forms.RadioButton();
            this.cboDay = new System.Windows.Forms.ComboBox();
            this.cboMonth = new System.Windows.Forms.ComboBox();
            this.cboYear = new System.Windows.Forms.ComboBox();
            this.cboName = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("新細明體", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(61, 16);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(236, 28);
            this.label8.TabIndex = 22;
            this.label8.Text = "會員基本登錄作業";
            // 
            // btnEnd
            // 
            this.btnEnd.Location = new System.Drawing.Point(283, 280);
            this.btnEnd.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.btnEnd.Name = "btnEnd";
            this.btnEnd.Size = new System.Drawing.Size(75, 32);
            this.btnEnd.TabIndex = 21;
            this.btnEnd.Text = "結束";
            this.btnEnd.UseVisualStyleBackColor = true;
            this.btnEnd.Click += new System.EventHandler(this.btnEnd_Click);
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(283, 218);
            this.btnAdd.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(75, 32);
            this.btnAdd.TabIndex = 20;
            this.btnAdd.Text = "新增";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // lstJob
            // 
            this.lstJob.FormattingEnabled = true;
            this.lstJob.ItemHeight = 15;
            this.lstJob.Location = new System.Drawing.Point(67, 218);
            this.lstJob.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.lstJob.Name = "lstJob";
            this.lstJob.Size = new System.Drawing.Size(147, 94);
            this.lstJob.TabIndex = 19;
            // 
            // rdbF
            // 
            this.rdbF.AutoSize = true;
            this.rdbF.Location = new System.Drawing.Point(129, 168);
            this.rdbF.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbF.Name = "rdbF";
            this.rdbF.Size = new System.Drawing.Size(43, 19);
            this.rdbF.TabIndex = 18;
            this.rdbF.TabStop = true;
            this.rdbF.Text = "女";
            this.rdbF.UseVisualStyleBackColor = true;
            // 
            // rdbM
            // 
            this.rdbM.AutoSize = true;
            this.rdbM.Location = new System.Drawing.Point(65, 168);
            this.rdbM.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbM.Name = "rdbM";
            this.rdbM.Size = new System.Drawing.Size(43, 19);
            this.rdbM.TabIndex = 17;
            this.rdbM.TabStop = true;
            this.rdbM.Text = "男";
            this.rdbM.UseVisualStyleBackColor = true;
            // 
            // cboDay
            // 
            this.cboDay.FormattingEnabled = true;
            this.cboDay.Location = new System.Drawing.Point(292, 119);
            this.cboDay.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.cboDay.Name = "cboDay";
            this.cboDay.Size = new System.Drawing.Size(59, 23);
            this.cboDay.TabIndex = 15;
            // 
            // cboMonth
            // 
            this.cboMonth.FormattingEnabled = true;
            this.cboMonth.Location = new System.Drawing.Point(192, 119);
            this.cboMonth.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.cboMonth.Name = "cboMonth";
            this.cboMonth.Size = new System.Drawing.Size(59, 23);
            this.cboMonth.TabIndex = 16;
            // 
            // cboYear
            // 
            this.cboYear.FormattingEnabled = true;
            this.cboYear.Location = new System.Drawing.Point(67, 119);
            this.cboYear.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.cboYear.Name = "cboYear";
            this.cboYear.Size = new System.Drawing.Size(77, 23);
            this.cboYear.TabIndex = 14;
            // 
            // cboName
            // 
            this.cboName.FormattingEnabled = true;
            this.cboName.Location = new System.Drawing.Point(65, 72);
            this.cboName.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.cboName.Name = "cboName";
            this.cboName.Size = new System.Drawing.Size(121, 23);
            this.cboName.TabIndex = 13;
            this.cboName.SelectedIndexChanged += new System.EventHandler(this.cboName_SelectedIndexChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(23, 218);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(37, 15);
            this.label4.TabIndex = 11;
            this.label4.Text = "職業";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(23, 169);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(37, 15);
            this.label3.TabIndex = 10;
            this.label3.Text = "性別";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(357, 122);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(22, 15);
            this.label7.TabIndex = 9;
            this.label7.Text = "日";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(255, 122);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(22, 15);
            this.label6.TabIndex = 8;
            this.label6.Text = "月";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(151, 122);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(22, 15);
            this.label5.TabIndex = 7;
            this.label5.Text = "年";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(23, 122);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(37, 15);
            this.label2.TabIndex = 12;
            this.label2.Text = "生日";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 75);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(37, 15);
            this.label1.TabIndex = 6;
            this.label1.Text = "姓名";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(407, 334);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.btnEnd);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.lstJob);
            this.Controls.Add(this.rdbF);
            this.Controls.Add(this.rdbM);
            this.Controls.Add(this.cboDay);
            this.Controls.Add(this.cboMonth);
            this.Controls.Add(this.cboYear);
            this.Controls.Add(this.cboName);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button btnEnd;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.ListBox lstJob;
        private System.Windows.Forms.RadioButton rdbF;
        private System.Windows.Forms.RadioButton rdbM;
        private System.Windows.Forms.ComboBox cboDay;
        private System.Windows.Forms.ComboBox cboMonth;
        private System.Windows.Forms.ComboBox cboYear;
        private System.Windows.Forms.ComboBox cboName;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

