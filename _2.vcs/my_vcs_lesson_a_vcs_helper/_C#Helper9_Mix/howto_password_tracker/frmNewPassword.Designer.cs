namespace howto_password_tracker
{
    partial class frmNewPassword
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
            this.GroupBox2 = new System.Windows.Forms.GroupBox();
            this.btnOk = new System.Windows.Forms.Button();
            this.txtPassword = new System.Windows.Forms.TextBox();
            this.Label11 = new System.Windows.Forms.Label();
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.GroupBox1 = new System.Windows.Forms.GroupBox();
            this.txtOther = new System.Windows.Forms.TextBox();
            this.chkRequireOther = new System.Windows.Forms.CheckBox();
            this.chkAllowOther = new System.Windows.Forms.CheckBox();
            this.chkRequireSpace = new System.Windows.Forms.CheckBox();
            this.chkRequireUnderscore = new System.Windows.Forms.CheckBox();
            this.chkRequireSpecial = new System.Windows.Forms.CheckBox();
            this.chkRequireNumber = new System.Windows.Forms.CheckBox();
            this.chkRequireUppercase = new System.Windows.Forms.CheckBox();
            this.chkRequireLowercase = new System.Windows.Forms.CheckBox();
            this.chkAllowSpace = new System.Windows.Forms.CheckBox();
            this.chkAllowUnderscore = new System.Windows.Forms.CheckBox();
            this.chkAllowSpecial = new System.Windows.Forms.CheckBox();
            this.chkAllowNumber = new System.Windows.Forms.CheckBox();
            this.chkAllowUppercase = new System.Windows.Forms.CheckBox();
            this.Label10 = new System.Windows.Forms.Label();
            this.Label9 = new System.Windows.Forms.Label();
            this.chkAllowLowercase = new System.Windows.Forms.CheckBox();
            this.Label8 = new System.Windows.Forms.Label();
            this.Label7 = new System.Windows.Forms.Label();
            this.Label6 = new System.Windows.Forms.Label();
            this.Label5 = new System.Windows.Forms.Label();
            this.Label4 = new System.Windows.Forms.Label();
            this.Label3 = new System.Windows.Forms.Label();
            this.txtMaxLength = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtMinLength = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.GroupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // GroupBox2
            // 
            this.GroupBox2.Location = new System.Drawing.Point(9, 267);
            this.GroupBox2.Name = "GroupBox2";
            this.GroupBox2.Size = new System.Drawing.Size(352, 8);
            this.GroupBox2.TabIndex = 21;
            this.GroupBox2.TabStop = false;
            // 
            // btnOk
            // 
            this.btnOk.DialogResult = System.Windows.Forms.DialogResult.OK;
            this.btnOk.Location = new System.Drawing.Point(193, 283);
            this.btnOk.Name = "btnOk";
            this.btnOk.Size = new System.Drawing.Size(75, 23);
            this.btnOk.TabIndex = 5;
            this.btnOk.Text = "OK";
            this.btnOk.UseVisualStyleBackColor = true;
            // 
            // txtPassword
            // 
            this.txtPassword.Location = new System.Drawing.Point(81, 235);
            this.txtPassword.Name = "txtPassword";
            this.txtPassword.Size = new System.Drawing.Size(160, 20);
            this.txtPassword.TabIndex = 3;
            // 
            // Label11
            // 
            this.Label11.AutoSize = true;
            this.Label11.Location = new System.Drawing.Point(9, 235);
            this.Label11.Name = "Label11";
            this.Label11.Size = new System.Drawing.Size(56, 13);
            this.Label11.TabIndex = 18;
            this.Label11.Text = "Password:";
            // 
            // btnCancel
            // 
            this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnCancel.Location = new System.Drawing.Point(289, 283);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(75, 23);
            this.btnCancel.TabIndex = 6;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = true;
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(289, 235);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(75, 23);
            this.btnGenerate.TabIndex = 4;
            this.btnGenerate.Text = "Generate";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // GroupBox1
            // 
            this.GroupBox1.Controls.Add(this.txtOther);
            this.GroupBox1.Controls.Add(this.chkRequireOther);
            this.GroupBox1.Controls.Add(this.chkAllowOther);
            this.GroupBox1.Controls.Add(this.chkRequireSpace);
            this.GroupBox1.Controls.Add(this.chkRequireUnderscore);
            this.GroupBox1.Controls.Add(this.chkRequireSpecial);
            this.GroupBox1.Controls.Add(this.chkRequireNumber);
            this.GroupBox1.Controls.Add(this.chkRequireUppercase);
            this.GroupBox1.Controls.Add(this.chkRequireLowercase);
            this.GroupBox1.Controls.Add(this.chkAllowSpace);
            this.GroupBox1.Controls.Add(this.chkAllowUnderscore);
            this.GroupBox1.Controls.Add(this.chkAllowSpecial);
            this.GroupBox1.Controls.Add(this.chkAllowNumber);
            this.GroupBox1.Controls.Add(this.chkAllowUppercase);
            this.GroupBox1.Controls.Add(this.Label10);
            this.GroupBox1.Controls.Add(this.Label9);
            this.GroupBox1.Controls.Add(this.chkAllowLowercase);
            this.GroupBox1.Controls.Add(this.Label8);
            this.GroupBox1.Controls.Add(this.Label7);
            this.GroupBox1.Controls.Add(this.Label6);
            this.GroupBox1.Controls.Add(this.Label5);
            this.GroupBox1.Controls.Add(this.Label4);
            this.GroupBox1.Controls.Add(this.Label3);
            this.GroupBox1.Location = new System.Drawing.Point(9, 11);
            this.GroupBox1.Name = "GroupBox1";
            this.GroupBox1.Size = new System.Drawing.Size(232, 216);
            this.GroupBox1.TabIndex = 0;
            this.GroupBox1.TabStop = false;
            this.GroupBox1.Text = "Characters";
            // 
            // txtOther
            // 
            this.txtOther.Location = new System.Drawing.Point(16, 184);
            this.txtOther.Name = "txtOther";
            this.txtOther.Size = new System.Drawing.Size(88, 20);
            this.txtOther.TabIndex = 12;
            // 
            // chkRequireOther
            // 
            this.chkRequireOther.AutoSize = true;
            this.chkRequireOther.Location = new System.Drawing.Point(184, 184);
            this.chkRequireOther.Name = "chkRequireOther";
            this.chkRequireOther.Size = new System.Drawing.Size(15, 14);
            this.chkRequireOther.TabIndex = 14;
            this.chkRequireOther.UseVisualStyleBackColor = true;
            this.chkRequireOther.CheckedChanged += new System.EventHandler(this.chkRequireOther_CheckedChanged);
            // 
            // chkAllowOther
            // 
            this.chkAllowOther.AutoSize = true;
            this.chkAllowOther.Location = new System.Drawing.Point(128, 184);
            this.chkAllowOther.Name = "chkAllowOther";
            this.chkAllowOther.Size = new System.Drawing.Size(15, 14);
            this.chkAllowOther.TabIndex = 13;
            this.chkAllowOther.UseVisualStyleBackColor = true;
            this.chkAllowOther.CheckedChanged += new System.EventHandler(this.chkAllowOther_CheckedChanged);
            // 
            // chkRequireSpace
            // 
            this.chkRequireSpace.AutoSize = true;
            this.chkRequireSpace.Location = new System.Drawing.Point(184, 160);
            this.chkRequireSpace.Name = "chkRequireSpace";
            this.chkRequireSpace.Size = new System.Drawing.Size(15, 14);
            this.chkRequireSpace.TabIndex = 11;
            this.chkRequireSpace.UseVisualStyleBackColor = true;
            this.chkRequireSpace.CheckedChanged += new System.EventHandler(this.chkRequireSpace_CheckedChanged);
            // 
            // chkRequireUnderscore
            // 
            this.chkRequireUnderscore.AutoSize = true;
            this.chkRequireUnderscore.Location = new System.Drawing.Point(184, 136);
            this.chkRequireUnderscore.Name = "chkRequireUnderscore";
            this.chkRequireUnderscore.Size = new System.Drawing.Size(15, 14);
            this.chkRequireUnderscore.TabIndex = 9;
            this.chkRequireUnderscore.UseVisualStyleBackColor = true;
            this.chkRequireUnderscore.CheckedChanged += new System.EventHandler(this.chkRequireUnderscore_CheckedChanged);
            // 
            // chkRequireSpecial
            // 
            this.chkRequireSpecial.AutoSize = true;
            this.chkRequireSpecial.Location = new System.Drawing.Point(184, 112);
            this.chkRequireSpecial.Name = "chkRequireSpecial";
            this.chkRequireSpecial.Size = new System.Drawing.Size(15, 14);
            this.chkRequireSpecial.TabIndex = 7;
            this.chkRequireSpecial.UseVisualStyleBackColor = true;
            this.chkRequireSpecial.CheckedChanged += new System.EventHandler(this.chkRequireSpecial_CheckedChanged);
            // 
            // chkRequireNumber
            // 
            this.chkRequireNumber.AutoSize = true;
            this.chkRequireNumber.Location = new System.Drawing.Point(184, 88);
            this.chkRequireNumber.Name = "chkRequireNumber";
            this.chkRequireNumber.Size = new System.Drawing.Size(15, 14);
            this.chkRequireNumber.TabIndex = 5;
            this.chkRequireNumber.UseVisualStyleBackColor = true;
            this.chkRequireNumber.CheckedChanged += new System.EventHandler(this.chkRequireNumber_CheckedChanged);
            // 
            // chkRequireUppercase
            // 
            this.chkRequireUppercase.AutoSize = true;
            this.chkRequireUppercase.Location = new System.Drawing.Point(184, 64);
            this.chkRequireUppercase.Name = "chkRequireUppercase";
            this.chkRequireUppercase.Size = new System.Drawing.Size(15, 14);
            this.chkRequireUppercase.TabIndex = 3;
            this.chkRequireUppercase.UseVisualStyleBackColor = true;
            this.chkRequireUppercase.CheckedChanged += new System.EventHandler(this.chkRequireUppercase_CheckedChanged);
            // 
            // chkRequireLowercase
            // 
            this.chkRequireLowercase.AutoSize = true;
            this.chkRequireLowercase.Location = new System.Drawing.Point(184, 40);
            this.chkRequireLowercase.Name = "chkRequireLowercase";
            this.chkRequireLowercase.Size = new System.Drawing.Size(15, 14);
            this.chkRequireLowercase.TabIndex = 1;
            this.chkRequireLowercase.UseVisualStyleBackColor = true;
            this.chkRequireLowercase.CheckedChanged += new System.EventHandler(this.chkRequireLowercase_CheckedChanged);
            // 
            // chkAllowSpace
            // 
            this.chkAllowSpace.AutoSize = true;
            this.chkAllowSpace.Location = new System.Drawing.Point(128, 160);
            this.chkAllowSpace.Name = "chkAllowSpace";
            this.chkAllowSpace.Size = new System.Drawing.Size(15, 14);
            this.chkAllowSpace.TabIndex = 10;
            this.chkAllowSpace.UseVisualStyleBackColor = true;
            this.chkAllowSpace.CheckedChanged += new System.EventHandler(this.chkAllowSpace_CheckedChanged);
            // 
            // chkAllowUnderscore
            // 
            this.chkAllowUnderscore.AutoSize = true;
            this.chkAllowUnderscore.Location = new System.Drawing.Point(128, 136);
            this.chkAllowUnderscore.Name = "chkAllowUnderscore";
            this.chkAllowUnderscore.Size = new System.Drawing.Size(15, 14);
            this.chkAllowUnderscore.TabIndex = 8;
            this.chkAllowUnderscore.UseVisualStyleBackColor = true;
            this.chkAllowUnderscore.CheckedChanged += new System.EventHandler(this.chkAllowUnderscore_CheckedChanged);
            // 
            // chkAllowSpecial
            // 
            this.chkAllowSpecial.AutoSize = true;
            this.chkAllowSpecial.Location = new System.Drawing.Point(128, 112);
            this.chkAllowSpecial.Name = "chkAllowSpecial";
            this.chkAllowSpecial.Size = new System.Drawing.Size(15, 14);
            this.chkAllowSpecial.TabIndex = 6;
            this.chkAllowSpecial.UseVisualStyleBackColor = true;
            this.chkAllowSpecial.CheckedChanged += new System.EventHandler(this.chkAllowSpecial_CheckedChanged);
            // 
            // chkAllowNumber
            // 
            this.chkAllowNumber.AutoSize = true;
            this.chkAllowNumber.Checked = true;
            this.chkAllowNumber.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkAllowNumber.Location = new System.Drawing.Point(128, 88);
            this.chkAllowNumber.Name = "chkAllowNumber";
            this.chkAllowNumber.Size = new System.Drawing.Size(15, 14);
            this.chkAllowNumber.TabIndex = 4;
            this.chkAllowNumber.UseVisualStyleBackColor = true;
            this.chkAllowNumber.CheckedChanged += new System.EventHandler(this.chkAllowNumber_CheckedChanged);
            // 
            // chkAllowUppercase
            // 
            this.chkAllowUppercase.AutoSize = true;
            this.chkAllowUppercase.Checked = true;
            this.chkAllowUppercase.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkAllowUppercase.Location = new System.Drawing.Point(128, 64);
            this.chkAllowUppercase.Name = "chkAllowUppercase";
            this.chkAllowUppercase.Size = new System.Drawing.Size(15, 14);
            this.chkAllowUppercase.TabIndex = 2;
            this.chkAllowUppercase.UseVisualStyleBackColor = true;
            this.chkAllowUppercase.CheckedChanged += new System.EventHandler(this.chkAllowUppercase_CheckedChanged);
            // 
            // Label10
            // 
            this.Label10.AutoSize = true;
            this.Label10.Location = new System.Drawing.Point(168, 16);
            this.Label10.Name = "Label10";
            this.Label10.Size = new System.Drawing.Size(44, 13);
            this.Label10.TabIndex = 8;
            this.Label10.Text = "Require";
            // 
            // Label9
            // 
            this.Label9.AutoSize = true;
            this.Label9.Location = new System.Drawing.Point(120, 16);
            this.Label9.Name = "Label9";
            this.Label9.Size = new System.Drawing.Size(32, 13);
            this.Label9.TabIndex = 7;
            this.Label9.Text = "Allow";
            // 
            // chkAllowLowercase
            // 
            this.chkAllowLowercase.AutoSize = true;
            this.chkAllowLowercase.Checked = true;
            this.chkAllowLowercase.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkAllowLowercase.Location = new System.Drawing.Point(128, 40);
            this.chkAllowLowercase.Name = "chkAllowLowercase";
            this.chkAllowLowercase.Size = new System.Drawing.Size(15, 14);
            this.chkAllowLowercase.TabIndex = 0;
            this.chkAllowLowercase.UseVisualStyleBackColor = true;
            this.chkAllowLowercase.CheckedChanged += new System.EventHandler(this.chkAllowLowercase_CheckedChanged);
            // 
            // Label8
            // 
            this.Label8.AutoSize = true;
            this.Label8.Location = new System.Drawing.Point(16, 160);
            this.Label8.Name = "Label8";
            this.Label8.Size = new System.Drawing.Size(50, 13);
            this.Label8.TabIndex = 5;
            this.Label8.Text = "Space ( )";
            // 
            // Label7
            // 
            this.Label7.AutoSize = true;
            this.Label7.Location = new System.Drawing.Point(16, 136);
            this.Label7.Name = "Label7";
            this.Label7.Size = new System.Drawing.Size(77, 13);
            this.Label7.TabIndex = 4;
            this.Label7.Text = "Underscore (_)";
            // 
            // Label6
            // 
            this.Label6.AutoSize = true;
            this.Label6.Location = new System.Drawing.Point(16, 112);
            this.Label6.Name = "Label6";
            this.Label6.Size = new System.Drawing.Size(72, 13);
            this.Label6.TabIndex = 3;
            this.Label6.Text = "Special ($%#)";
            // 
            // Label5
            // 
            this.Label5.AutoSize = true;
            this.Label5.Location = new System.Drawing.Point(16, 88);
            this.Label5.Name = "Label5";
            this.Label5.Size = new System.Drawing.Size(76, 13);
            this.Label5.TabIndex = 2;
            this.Label5.Text = "Numbers (123)";
            // 
            // Label4
            // 
            this.Label4.AutoSize = true;
            this.Label4.Location = new System.Drawing.Point(16, 64);
            this.Label4.Name = "Label4";
            this.Label4.Size = new System.Drawing.Size(89, 13);
            this.Label4.TabIndex = 1;
            this.Label4.Text = "Uppercase (ABC)";
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Location = new System.Drawing.Point(16, 40);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(86, 13);
            this.Label3.TabIndex = 0;
            this.Label3.Text = "Lowercase (abc)";
            // 
            // txtMaxLength
            // 
            this.txtMaxLength.Location = new System.Drawing.Point(329, 43);
            this.txtMaxLength.Name = "txtMaxLength";
            this.txtMaxLength.Size = new System.Drawing.Size(32, 20);
            this.txtMaxLength.TabIndex = 2;
            this.txtMaxLength.Text = "12";
            this.txtMaxLength.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(257, 43);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(66, 13);
            this.Label2.TabIndex = 13;
            this.Label2.Text = "Max Length:";
            // 
            // txtMinLength
            // 
            this.txtMinLength.Location = new System.Drawing.Point(329, 19);
            this.txtMinLength.Name = "txtMinLength";
            this.txtMinLength.Size = new System.Drawing.Size(32, 20);
            this.txtMinLength.TabIndex = 1;
            this.txtMinLength.Text = "8";
            this.txtMinLength.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(257, 19);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(63, 13);
            this.Label1.TabIndex = 11;
            this.Label1.Text = "Min Length:";
            // 
            // frmNewPassword
            // 
            this.AcceptButton = this.btnGenerate;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.btnCancel;
            this.ClientSize = new System.Drawing.Size(373, 317);
            this.Controls.Add(this.GroupBox2);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.txtPassword);
            this.Controls.Add(this.Label11);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnGenerate);
            this.Controls.Add(this.GroupBox1);
            this.Controls.Add(this.txtMaxLength);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtMinLength);
            this.Controls.Add(this.Label1);
            this.Name = "frmNewPassword";
            this.Text = "New Password";
            this.GroupBox1.ResumeLayout(false);
            this.GroupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.GroupBox GroupBox2;
        internal System.Windows.Forms.Button btnOk;
        internal System.Windows.Forms.TextBox txtPassword;
        internal System.Windows.Forms.Label Label11;
        internal System.Windows.Forms.Button btnCancel;
        internal System.Windows.Forms.Button btnGenerate;
        internal System.Windows.Forms.GroupBox GroupBox1;
        internal System.Windows.Forms.TextBox txtOther;
        internal System.Windows.Forms.CheckBox chkRequireOther;
        internal System.Windows.Forms.CheckBox chkAllowOther;
        internal System.Windows.Forms.CheckBox chkRequireSpace;
        internal System.Windows.Forms.CheckBox chkRequireUnderscore;
        internal System.Windows.Forms.CheckBox chkRequireSpecial;
        internal System.Windows.Forms.CheckBox chkRequireNumber;
        internal System.Windows.Forms.CheckBox chkRequireUppercase;
        internal System.Windows.Forms.CheckBox chkRequireLowercase;
        internal System.Windows.Forms.CheckBox chkAllowSpace;
        internal System.Windows.Forms.CheckBox chkAllowUnderscore;
        internal System.Windows.Forms.CheckBox chkAllowSpecial;
        internal System.Windows.Forms.CheckBox chkAllowNumber;
        internal System.Windows.Forms.CheckBox chkAllowUppercase;
        internal System.Windows.Forms.Label Label10;
        internal System.Windows.Forms.Label Label9;
        internal System.Windows.Forms.CheckBox chkAllowLowercase;
        internal System.Windows.Forms.Label Label8;
        internal System.Windows.Forms.Label Label7;
        internal System.Windows.Forms.Label Label6;
        internal System.Windows.Forms.Label Label5;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.TextBox txtMaxLength;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtMinLength;
        internal System.Windows.Forms.Label Label1;
    }
}