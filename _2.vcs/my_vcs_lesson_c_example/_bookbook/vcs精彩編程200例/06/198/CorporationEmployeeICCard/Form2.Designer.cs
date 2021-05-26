namespace CorporationEmployeeICCard
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.cbFolk = new System.Windows.Forms.ComboBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtDept = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.txtJob = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.cbSex = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtICCard = new System.Windows.Forms.TextBox();
            this.txtName = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.cbFolk);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.txtDept);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.txtJob);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.cbSex);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.txtICCard);
            this.groupBox1.Controls.Add(this.txtName);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.ForeColor = System.Drawing.Color.Black;
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(405, 128);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "输入员工信息";
            // 
            // cbFolk
            // 
            this.cbFolk.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbFolk.FormattingEnabled = true;
            this.cbFolk.Items.AddRange(new object[] {
            "汉族",
            "蒙古族",
            "回族",
            "藏族",
            "维吾尔族",
            "苗族",
            "彝族",
            "壮族",
            "布依族",
            "朝鲜族",
            "满族",
            "侗族",
            "瑶族",
            "白族",
            "土家族",
            "哈尼族",
            "哈萨克族",
            "傣族",
            "黎族",
            "傈僳族",
            "佤族",
            "畲族",
            "高山族",
            "拉祜族",
            "水族",
            "东乡族",
            "纳西族",
            "景颇族",
            "柯尔克孜族",
            "土族",
            "达斡尔族",
            "仫佬族",
            "羌族",
            "布朗族",
            "撒拉族",
            "毛南族",
            "仡佬族",
            "锡伯族",
            "阿昌族",
            "普米族",
            "怒族",
            "塔吉克族",
            "乌孜别克族",
            "俄罗斯族",
            "鄂温克族",
            "德昂族",
            "保安族",
            "裕固族",
            "京族",
            "塔塔尔族",
            "独龙族",
            "鄂伦春族",
            "赫哲族",
            "门巴族",
            "珞巴族",
            "基诺族"});
            this.cbFolk.Location = new System.Drawing.Point(75, 93);
            this.cbFolk.Name = "cbFolk";
            this.cbFolk.Size = new System.Drawing.Size(129, 20);
            this.cbFolk.TabIndex = 11;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(13, 98);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(65, 12);
            this.label6.TabIndex = 10;
            this.label6.Text = "员工民族：";
            // 
            // txtDept
            // 
            this.txtDept.Location = new System.Drawing.Point(268, 93);
            this.txtDept.Name = "txtDept";
            this.txtDept.Size = new System.Drawing.Size(129, 21);
            this.txtDept.TabIndex = 9;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(208, 98);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(65, 12);
            this.label5.TabIndex = 8;
            this.label5.Text = "所属部门：";
            // 
            // txtJob
            // 
            this.txtJob.Location = new System.Drawing.Point(268, 57);
            this.txtJob.Name = "txtJob";
            this.txtJob.Size = new System.Drawing.Size(129, 21);
            this.txtJob.TabIndex = 7;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(208, 62);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(65, 12);
            this.label4.TabIndex = 6;
            this.label4.Text = "员工职位：";
            // 
            // cbSex
            // 
            this.cbSex.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbSex.FormattingEnabled = true;
            this.cbSex.Items.AddRange(new object[] {
            "男性",
            "女性"});
            this.cbSex.Location = new System.Drawing.Point(75, 58);
            this.cbSex.Name = "cbSex";
            this.cbSex.Size = new System.Drawing.Size(129, 20);
            this.cbSex.TabIndex = 5;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(13, 62);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 4;
            this.label3.Text = "员工性别：";
            // 
            // txtICCard
            // 
            this.txtICCard.Location = new System.Drawing.Point(75, 22);
            this.txtICCard.Name = "txtICCard";
            this.txtICCard.Size = new System.Drawing.Size(129, 21);
            this.txtICCard.TabIndex = 1;
            this.txtICCard.Text = "IC-";
            this.txtICCard.TextChanged += new System.EventHandler(this.txtICCard_TextChanged);
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(268, 22);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(129, 21);
            this.txtName.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(208, 27);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "员工姓名：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "IC卡编号：";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(122, 146);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "增加";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(226, 146);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 2;
            this.button2.Text = "取消";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(429, 179);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.groupBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Form2";
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "员工信息设置";
            this.Load += new System.EventHandler(this.Form2_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtICCard;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox cbSex;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtJob;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtDept;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.ComboBox cbFolk;
        private System.Windows.Forms.Label label6;
    }
}