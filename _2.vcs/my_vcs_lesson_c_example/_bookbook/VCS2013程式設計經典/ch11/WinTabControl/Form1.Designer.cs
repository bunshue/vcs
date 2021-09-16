namespace WinTabControl
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
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.btnAdd = new System.Windows.Forms.Button();
            this.chkIsMarry = new System.Windows.Forms.CheckBox();
            this.rdbF = new System.Windows.Forms.RadioButton();
            this.rdbM = new System.Windows.Forms.RadioButton();
            this.txtName = new System.Windows.Forms.TextBox();
            this.txtEmpId = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.txtShow = new System.Windows.Forms.TextBox();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(354, 223);
            this.tabControl1.TabIndex = 1;
            this.tabControl1.SelectedIndexChanged += new System.EventHandler(this.tabControl1_SelectedIndexChanged);
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.btnAdd);
            this.tabPage1.Controls.Add(this.chkIsMarry);
            this.tabPage1.Controls.Add(this.rdbF);
            this.tabPage1.Controls.Add(this.rdbM);
            this.tabPage1.Controls.Add(this.txtName);
            this.tabPage1.Controls.Add(this.txtEmpId);
            this.tabPage1.Controls.Add(this.label4);
            this.tabPage1.Controls.Add(this.label3);
            this.tabPage1.Controls.Add(this.label2);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Location = new System.Drawing.Point(4, 29);
            this.tabPage1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPage1.Size = new System.Drawing.Size(346, 190);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "會員新增";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(227, 26);
            this.btnAdd.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(75, 30);
            this.btnAdd.TabIndex = 4;
            this.btnAdd.Text = "新增";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // chkIsMarry
            // 
            this.chkIsMarry.AutoSize = true;
            this.chkIsMarry.Location = new System.Drawing.Point(81, 152);
            this.chkIsMarry.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.chkIsMarry.Name = "chkIsMarry";
            this.chkIsMarry.Size = new System.Drawing.Size(69, 23);
            this.chkIsMarry.TabIndex = 3;
            this.chkIsMarry.Text = "已婚";
            this.chkIsMarry.UseVisualStyleBackColor = true;
            // 
            // rdbF
            // 
            this.rdbF.AutoSize = true;
            this.rdbF.Location = new System.Drawing.Point(139, 109);
            this.rdbF.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbF.Name = "rdbF";
            this.rdbF.Size = new System.Drawing.Size(49, 23);
            this.rdbF.TabIndex = 2;
            this.rdbF.TabStop = true;
            this.rdbF.Text = "女";
            this.rdbF.UseVisualStyleBackColor = true;
            // 
            // rdbM
            // 
            this.rdbM.AutoSize = true;
            this.rdbM.Location = new System.Drawing.Point(81, 109);
            this.rdbM.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.rdbM.Name = "rdbM";
            this.rdbM.Size = new System.Drawing.Size(49, 23);
            this.rdbM.TabIndex = 2;
            this.rdbM.TabStop = true;
            this.rdbM.Text = "男";
            this.rdbM.UseVisualStyleBackColor = true;
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(81, 65);
            this.txtName.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(129, 30);
            this.txtName.TabIndex = 1;
            // 
            // txtEmpId
            // 
            this.txtEmpId.Location = new System.Drawing.Point(81, 26);
            this.txtEmpId.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.txtEmpId.Name = "txtEmpId";
            this.txtEmpId.Size = new System.Drawing.Size(129, 30);
            this.txtEmpId.TabIndex = 1;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(27, 152);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(47, 19);
            this.label4.TabIndex = 0;
            this.label4.Text = "婚姻";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(27, 109);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 19);
            this.label3.TabIndex = 0;
            this.label3.Text = "性別";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(27, 68);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(47, 19);
            this.label2.TabIndex = 0;
            this.label2.Text = "姓名";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(27, 29);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 19);
            this.label1.TabIndex = 0;
            this.label1.Text = "編號";
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.txtShow);
            this.tabPage2.Location = new System.Drawing.Point(4, 29);
            this.tabPage2.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.tabPage2.Size = new System.Drawing.Size(346, 190);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "會員列表";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // txtShow
            // 
            this.txtShow.Location = new System.Drawing.Point(32, 30);
            this.txtShow.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.txtShow.Name = "txtShow";
            this.txtShow.Size = new System.Drawing.Size(100, 30);
            this.txtShow.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 19F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(354, 223);
            this.Controls.Add(this.tabControl1);
            this.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.CheckBox chkIsMarry;
        private System.Windows.Forms.RadioButton rdbF;
        private System.Windows.Forms.RadioButton rdbM;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.TextBox txtEmpId;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TextBox txtShow;
    }
}

