namespace Train
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
            this.chkSpecial = new System.Windows.Forms.CheckBox();
            this.lblTotal = new System.Windows.Forms.Label();
            this.btnOK = new System.Windows.Forms.Button();
            this.chkToBack = new System.Windows.Forms.CheckBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rdbKind3 = new System.Windows.Forms.RadioButton();
            this.rdbKind2 = new System.Windows.Forms.RadioButton();
            this.rdbKind1 = new System.Windows.Forms.RadioButton();
            this.txtKm = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // chkSpecial
            // 
            this.chkSpecial.AutoSize = true;
            this.chkSpecial.Location = new System.Drawing.Point(144, 57);
            this.chkSpecial.Name = "chkSpecial";
            this.chkSpecial.Size = new System.Drawing.Size(128, 16);
            this.chkSpecial.TabIndex = 28;
            this.chkSpecial.Text = "優待票(孩童、敬老)";
            this.chkSpecial.UseVisualStyleBackColor = true;
            // 
            // lblTotal
            // 
            this.lblTotal.AutoSize = true;
            this.lblTotal.Location = new System.Drawing.Point(144, 119);
            this.lblTotal.Name = "lblTotal";
            this.lblTotal.Size = new System.Drawing.Size(41, 12);
            this.lblTotal.TabIndex = 27;
            this.lblTotal.Text = "票價：";
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(188, 15);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 23);
            this.btnOK.TabIndex = 26;
            this.btnOK.Text = "確定";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // chkToBack
            // 
            this.chkToBack.AutoSize = true;
            this.chkToBack.Location = new System.Drawing.Point(144, 79);
            this.chkToBack.Name = "chkToBack";
            this.chkToBack.Size = new System.Drawing.Size(60, 16);
            this.chkToBack.TabIndex = 25;
            this.chkToBack.Text = "去回票";
            this.chkToBack.UseVisualStyleBackColor = true;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rdbKind3);
            this.groupBox1.Controls.Add(this.rdbKind2);
            this.groupBox1.Controls.Add(this.rdbKind1);
            this.groupBox1.Location = new System.Drawing.Point(14, 47);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(124, 100);
            this.groupBox1.TabIndex = 24;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "車種";
            // 
            // rdbKind3
            // 
            this.rdbKind3.AutoSize = true;
            this.rdbKind3.Location = new System.Drawing.Point(16, 70);
            this.rdbKind3.Name = "rdbKind3";
            this.rdbKind3.Size = new System.Drawing.Size(98, 16);
            this.rdbKind3.TabIndex = 2;
            this.rdbKind3.Text = "復興號/區間車";
            this.rdbKind3.UseVisualStyleBackColor = true;
            // 
            // rdbKind2
            // 
            this.rdbKind2.AutoSize = true;
            this.rdbKind2.Location = new System.Drawing.Point(16, 48);
            this.rdbKind2.Name = "rdbKind2";
            this.rdbKind2.Size = new System.Drawing.Size(59, 16);
            this.rdbKind2.TabIndex = 1;
            this.rdbKind2.Text = "莒光號";
            this.rdbKind2.UseVisualStyleBackColor = true;
            // 
            // rdbKind1
            // 
            this.rdbKind1.AutoSize = true;
            this.rdbKind1.Location = new System.Drawing.Point(16, 26);
            this.rdbKind1.Name = "rdbKind1";
            this.rdbKind1.Size = new System.Drawing.Size(59, 16);
            this.rdbKind1.TabIndex = 0;
            this.rdbKind1.Text = "自強號";
            this.rdbKind1.UseVisualStyleBackColor = true;
            // 
            // txtKm
            // 
            this.txtKm.Location = new System.Drawing.Point(95, 14);
            this.txtKm.Name = "txtKm";
            this.txtKm.Size = new System.Drawing.Size(74, 22);
            this.txtKm.TabIndex = 23;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 12);
            this.label1.TabIndex = 22;
            this.label1.Text = "輸入公里數：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 161);
            this.Controls.Add(this.chkSpecial);
            this.Controls.Add(this.lblTotal);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.chkToBack);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.txtKm);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkSpecial;
        private System.Windows.Forms.Label lblTotal;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.CheckBox chkToBack;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rdbKind3;
        private System.Windows.Forms.RadioButton rdbKind2;
        private System.Windows.Forms.RadioButton rdbKind1;
        private System.Windows.Forms.TextBox txtKm;
        private System.Windows.Forms.Label label1;
    }
}

