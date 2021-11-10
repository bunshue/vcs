namespace vcs_ReadWrite_INI9
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.readBtn = new System.Windows.Forms.Button();
            this.saveBtn = new System.Windows.Forms.Button();
            this.userGb = new System.Windows.Forms.GroupBox();
            this.webAddresTxt = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.webLoginNameTxt = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.webPwdTxt = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.ftpPwdTxt = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.ftpLoginNameTxt = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.ftpGb = new System.Windows.Forms.GroupBox();
            this.ftpAddressTxt = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.removeSectionBtn = new System.Windows.Forms.Button();
            this.removeKeyBtn = new System.Windows.Forms.Button();
            this.getAllSectionBtn = new System.Windows.Forms.Button();
            this.getAllKeyBtn = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.userGb.SuspendLayout();
            this.ftpGb.SuspendLayout();
            this.SuspendLayout();
            // 
            // readBtn
            // 
            this.readBtn.Location = new System.Drawing.Point(113, 274);
            this.readBtn.Name = "readBtn";
            this.readBtn.Size = new System.Drawing.Size(103, 30);
            this.readBtn.TabIndex = 0;
            this.readBtn.Text = "读取ini文件";
            this.readBtn.UseVisualStyleBackColor = true;
            this.readBtn.Click += new System.EventHandler(this.readBtn_Click);
            // 
            // saveBtn
            // 
            this.saveBtn.Location = new System.Drawing.Point(273, 274);
            this.saveBtn.Name = "saveBtn";
            this.saveBtn.Size = new System.Drawing.Size(103, 30);
            this.saveBtn.TabIndex = 1;
            this.saveBtn.Text = "保存ini文件";
            this.saveBtn.UseVisualStyleBackColor = true;
            this.saveBtn.Click += new System.EventHandler(this.saveBtn_Click);
            // 
            // userGb
            // 
            this.userGb.Controls.Add(this.webAddresTxt);
            this.userGb.Controls.Add(this.label1);
            this.userGb.Location = new System.Drawing.Point(26, 12);
            this.userGb.Name = "userGb";
            this.userGb.Size = new System.Drawing.Size(361, 125);
            this.userGb.TabIndex = 2;
            this.userGb.TabStop = false;
            this.userGb.Text = "Web信息";
            // 
            // webAddresTxt
            // 
            this.webAddresTxt.Location = new System.Drawing.Point(71, 28);
            this.webAddresTxt.Name = "webAddresTxt";
            this.webAddresTxt.Size = new System.Drawing.Size(274, 22);
            this.webAddresTxt.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 31);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(63, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Web地址：";
            // 
            // webLoginNameTxt
            // 
            this.webLoginNameTxt.Location = new System.Drawing.Point(97, 71);
            this.webLoginNameTxt.Name = "webLoginNameTxt";
            this.webLoginNameTxt.Size = new System.Drawing.Size(274, 22);
            this.webLoginNameTxt.TabIndex = 5;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(37, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 4;
            this.label2.Text = "用户名：";
            // 
            // webPwdTxt
            // 
            this.webPwdTxt.Location = new System.Drawing.Point(97, 102);
            this.webPwdTxt.Name = "webPwdTxt";
            this.webPwdTxt.Size = new System.Drawing.Size(274, 22);
            this.webPwdTxt.TabIndex = 7;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(48, 108);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(41, 12);
            this.label3.TabIndex = 6;
            this.label3.Text = "密码：";
            // 
            // ftpPwdTxt
            // 
            this.ftpPwdTxt.Location = new System.Drawing.Point(97, 233);
            this.ftpPwdTxt.Name = "ftpPwdTxt";
            this.ftpPwdTxt.Size = new System.Drawing.Size(274, 22);
            this.ftpPwdTxt.TabIndex = 12;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(48, 239);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(41, 12);
            this.label4.TabIndex = 11;
            this.label4.Text = "密码：";
            // 
            // ftpLoginNameTxt
            // 
            this.ftpLoginNameTxt.Location = new System.Drawing.Point(97, 202);
            this.ftpLoginNameTxt.Name = "ftpLoginNameTxt";
            this.ftpLoginNameTxt.Size = new System.Drawing.Size(274, 22);
            this.ftpLoginNameTxt.TabIndex = 10;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(37, 208);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(53, 12);
            this.label5.TabIndex = 9;
            this.label5.Text = "用户名：";
            // 
            // ftpGb
            // 
            this.ftpGb.Controls.Add(this.ftpAddressTxt);
            this.ftpGb.Controls.Add(this.label6);
            this.ftpGb.Location = new System.Drawing.Point(26, 143);
            this.ftpGb.Name = "ftpGb";
            this.ftpGb.Size = new System.Drawing.Size(361, 125);
            this.ftpGb.TabIndex = 8;
            this.ftpGb.TabStop = false;
            this.ftpGb.Text = "FTP信息";
            // 
            // ftpAddressTxt
            // 
            this.ftpAddressTxt.Location = new System.Drawing.Point(71, 28);
            this.ftpAddressTxt.Name = "ftpAddressTxt";
            this.ftpAddressTxt.Size = new System.Drawing.Size(274, 22);
            this.ftpAddressTxt.TabIndex = 1;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(6, 31);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(60, 12);
            this.label6.TabIndex = 0;
            this.label6.Text = "FTP地址：";
            // 
            // removeSectionBtn
            // 
            this.removeSectionBtn.Location = new System.Drawing.Point(113, 312);
            this.removeSectionBtn.Name = "removeSectionBtn";
            this.removeSectionBtn.Size = new System.Drawing.Size(103, 30);
            this.removeSectionBtn.TabIndex = 13;
            this.removeSectionBtn.Text = "移除整个Web信息";
            this.removeSectionBtn.UseVisualStyleBackColor = true;
            this.removeSectionBtn.Click += new System.EventHandler(this.removeSectionBtn_Click);
            // 
            // removeKeyBtn
            // 
            this.removeKeyBtn.Location = new System.Drawing.Point(273, 312);
            this.removeKeyBtn.Name = "removeKeyBtn";
            this.removeKeyBtn.Size = new System.Drawing.Size(136, 30);
            this.removeKeyBtn.TabIndex = 14;
            this.removeKeyBtn.Text = "移除Web信息中的密码";
            this.removeKeyBtn.UseVisualStyleBackColor = true;
            this.removeKeyBtn.Click += new System.EventHandler(this.removeKeyBtn_Click);
            // 
            // getAllSectionBtn
            // 
            this.getAllSectionBtn.Location = new System.Drawing.Point(113, 353);
            this.getAllSectionBtn.Name = "getAllSectionBtn";
            this.getAllSectionBtn.Size = new System.Drawing.Size(130, 30);
            this.getAllSectionBtn.TabIndex = 15;
            this.getAllSectionBtn.Text = "获取所有Section名称";
            this.getAllSectionBtn.UseVisualStyleBackColor = true;
            this.getAllSectionBtn.Click += new System.EventHandler(this.getAllSectionBtn_Click);
            // 
            // getAllKeyBtn
            // 
            this.getAllKeyBtn.Location = new System.Drawing.Point(273, 353);
            this.getAllKeyBtn.Name = "getAllKeyBtn";
            this.getAllKeyBtn.Size = new System.Drawing.Size(145, 30);
            this.getAllKeyBtn.TabIndex = 16;
            this.getAllKeyBtn.Text = "获取Web信息中的所有Key";
            this.getAllKeyBtn.UseVisualStyleBackColor = true;
            this.getAllKeyBtn.Click += new System.EventHandler(this.getAllKeyBtn_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(481, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(357, 472);
            this.richTextBox1.TabIndex = 17;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(850, 496);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.getAllKeyBtn);
            this.Controls.Add(this.getAllSectionBtn);
            this.Controls.Add(this.removeKeyBtn);
            this.Controls.Add(this.removeSectionBtn);
            this.Controls.Add(this.ftpPwdTxt);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.ftpLoginNameTxt);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.ftpGb);
            this.Controls.Add(this.webPwdTxt);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.webLoginNameTxt);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.userGb);
            this.Controls.Add(this.saveBtn);
            this.Controls.Add(this.readBtn);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "配置信息";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.userGb.ResumeLayout(false);
            this.userGb.PerformLayout();
            this.ftpGb.ResumeLayout(false);
            this.ftpGb.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button readBtn;
        private System.Windows.Forms.Button saveBtn;
        private System.Windows.Forms.GroupBox userGb;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox webAddresTxt;
        private System.Windows.Forms.TextBox webLoginNameTxt;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox webPwdTxt;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox ftpPwdTxt;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox ftpLoginNameTxt;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.GroupBox ftpGb;
        private System.Windows.Forms.TextBox ftpAddressTxt;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button removeSectionBtn;
        private System.Windows.Forms.Button removeKeyBtn;
        private System.Windows.Forms.Button getAllSectionBtn;
        private System.Windows.Forms.Button getAllKeyBtn;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

