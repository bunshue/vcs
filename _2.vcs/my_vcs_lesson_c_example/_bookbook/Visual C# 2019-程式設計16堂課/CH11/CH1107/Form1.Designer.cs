namespace CH1107
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
            this.btnOK = new System.Windows.Forms.Button();
            this.dtpLogin = new System.Windows.Forms.DateTimePicker();
            this.label4 = new System.Windows.Forms.Label();
            this.txtName = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.rtxtChoice = new System.Windows.Forms.RichTextBox();
            this.cobSubject = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.cobMain = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(264, 137);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(75, 33);
            this.btnOK.TabIndex = 20;
            this.btnOK.Text = "確認";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // dtpLogin
            // 
            this.dtpLogin.Location = new System.Drawing.Point(71, 43);
            this.dtpLogin.MaxDate = new System.DateTime(2019, 12, 31, 0, 0, 0, 0);
            this.dtpLogin.MinDate = new System.DateTime(2019, 11, 1, 0, 0, 0, 0);
            this.dtpLogin.Name = "dtpLogin";
            this.dtpLogin.Size = new System.Drawing.Size(154, 22);
            this.dtpLogin.TabIndex = 14;
            this.dtpLogin.Value = new System.DateTime(2019, 11, 1, 0, 0, 0, 0);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(10, 47);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(41, 12);
            this.label4.TabIndex = 13;
            this.label4.Text = "日期：";
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(72, 10);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 22);
            this.txtName.TabIndex = 12;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(8, 15);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(41, 12);
            this.label3.TabIndex = 11;
            this.label3.Text = "名稱：";
            // 
            // rtxtChoice
            // 
            this.rtxtChoice.Location = new System.Drawing.Point(227, 15);
            this.rtxtChoice.Name = "rtxtChoice";
            this.rtxtChoice.Size = new System.Drawing.Size(163, 116);
            this.rtxtChoice.TabIndex = 19;
            this.rtxtChoice.Text = "";
            // 
            // cobSubject
            // 
            this.cobSubject.FormattingEnabled = true;
            this.cobSubject.Location = new System.Drawing.Point(124, 106);
            this.cobSubject.Name = "cobSubject";
            this.cobSubject.Size = new System.Drawing.Size(97, 20);
            this.cobSubject.TabIndex = 18;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(117, 80);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 17;
            this.label2.Text = "選修科目：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(10, 80);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 15;
            this.label1.Text = "主要科目：";
            // 
            // cobMain
            // 
            this.cobMain.FormattingEnabled = true;
            this.cobMain.Items.AddRange(new object[] {
            "計算機概論",
            "法律與科搜",
            "資訊數學",
            "程式設計(1)",
            "程式設計(2)"});
            this.cobMain.Location = new System.Drawing.Point(12, 106);
            this.cobMain.Margin = new System.Windows.Forms.Padding(4);
            this.cobMain.Name = "cobMain";
            this.cobMain.Size = new System.Drawing.Size(110, 20);
            this.cobMain.TabIndex = 16;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(412, 201);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.dtpLogin);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.rtxtChoice);
            this.Controls.Add(this.cobSubject);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.cobMain);
            this.Name = "Form1";
            this.Text = "CH1107";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.DateTimePicker dtpLogin;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.RichTextBox rtxtChoice;
        private System.Windows.Forms.ComboBox cobSubject;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cobMain;
    }
}

