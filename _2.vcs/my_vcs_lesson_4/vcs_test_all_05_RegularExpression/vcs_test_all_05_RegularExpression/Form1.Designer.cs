﻿namespace vcs_test_all_05_RegularExpression
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtDigits = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtLetters = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtString = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.txtTestString = new System.Windows.Forms.TextBox();
            this.Label4 = new System.Windows.Forms.Label();
            this.lblResult = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.txtReplacementPattern = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtPattern = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.lblResult2 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.txtInput = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.txtReplacementPattern2 = new System.Windows.Forms.TextBox();
            this.label12 = new System.Windows.Forms.Label();
            this.txtPattern2 = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.tb_email = new System.Windows.Forms.TextBox();
            this.tb_rul = new System.Windows.Forms.TextBox();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.txtDigits);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.txtLetters);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.txtString);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(243, 138);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "英數分離";
            // 
            // txtDigits
            // 
            this.txtDigits.Location = new System.Drawing.Point(54, 100);
            this.txtDigits.Name = "txtDigits";
            this.txtDigits.Size = new System.Drawing.Size(171, 22);
            this.txtDigits.TabIndex = 19;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(11, 103);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(23, 12);
            this.label3.TabIndex = 18;
            this.label3.Text = "數 :";
            // 
            // txtLetters
            // 
            this.txtLetters.Location = new System.Drawing.Point(54, 76);
            this.txtLetters.Name = "txtLetters";
            this.txtLetters.Size = new System.Drawing.Size(171, 22);
            this.txtLetters.TabIndex = 17;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(11, 79);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(23, 12);
            this.label2.TabIndex = 16;
            this.label2.Text = "英 :";
            // 
            // txtString
            // 
            this.txtString.Location = new System.Drawing.Point(54, 25);
            this.txtString.Name = "txtString";
            this.txtString.Size = new System.Drawing.Size(171, 22);
            this.txtString.TabIndex = 15;
            this.txtString.Text = "COVID-19 2020 Dec";
            this.txtString.TextChanged += new System.EventHandler(this.txtString_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 12);
            this.label1.TabIndex = 14;
            this.label1.Text = "字串 :";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.txtTestString);
            this.groupBox2.Controls.Add(this.Label4);
            this.groupBox2.Controls.Add(this.lblResult);
            this.groupBox2.Controls.Add(this.label5);
            this.groupBox2.Controls.Add(this.txtReplacementPattern);
            this.groupBox2.Controls.Add(this.label6);
            this.groupBox2.Controls.Add(this.txtPattern);
            this.groupBox2.Controls.Add(this.label7);
            this.groupBox2.Location = new System.Drawing.Point(261, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(319, 183);
            this.groupBox2.TabIndex = 20;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "置換";
            // 
            // txtTestString
            // 
            this.txtTestString.Location = new System.Drawing.Point(6, 114);
            this.txtTestString.Name = "txtTestString";
            this.txtTestString.Size = new System.Drawing.Size(290, 22);
            this.txtTestString.TabIndex = 38;
            this.txtTestString.Text = "The QUICK BROWN fox jumps over the LAZY dog.";
            this.txtTestString.TextChanged += new System.EventHandler(this.txtTestString_TextChanged);
            // 
            // Label4
            // 
            this.Label4.AutoSize = true;
            this.Label4.Location = new System.Drawing.Point(6, 99);
            this.Label4.Name = "Label4";
            this.Label4.Size = new System.Drawing.Size(55, 12);
            this.Label4.TabIndex = 43;
            this.Label4.Text = "Test String";
            // 
            // lblResult
            // 
            this.lblResult.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblResult.Location = new System.Drawing.Point(9, 153);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(290, 15);
            this.lblResult.TabIndex = 42;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(9, 139);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(34, 12);
            this.label5.TabIndex = 41;
            this.label5.Text = "Result";
            // 
            // txtReplacementPattern
            // 
            this.txtReplacementPattern.Location = new System.Drawing.Point(6, 77);
            this.txtReplacementPattern.Name = "txtReplacementPattern";
            this.txtReplacementPattern.Size = new System.Drawing.Size(290, 22);
            this.txtReplacementPattern.TabIndex = 36;
            this.txtReplacementPattern.Text = ".";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(6, 62);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(100, 12);
            this.label6.TabIndex = 39;
            this.label6.Text = "Replacement Pattern";
            // 
            // txtPattern
            // 
            this.txtPattern.Location = new System.Drawing.Point(6, 32);
            this.txtPattern.Name = "txtPattern";
            this.txtPattern.Size = new System.Drawing.Size(290, 22);
            this.txtPattern.TabIndex = 40;
            this.txtPattern.Text = "[aeiouAEIOU]";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(6, 18);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(37, 12);
            this.label7.TabIndex = 37;
            this.label7.Text = "Pattern";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.lblResult2);
            this.groupBox3.Controls.Add(this.label9);
            this.groupBox3.Controls.Add(this.label10);
            this.groupBox3.Controls.Add(this.txtInput);
            this.groupBox3.Controls.Add(this.label11);
            this.groupBox3.Controls.Add(this.txtReplacementPattern2);
            this.groupBox3.Controls.Add(this.label12);
            this.groupBox3.Controls.Add(this.txtPattern2);
            this.groupBox3.Location = new System.Drawing.Point(12, 218);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(310, 287);
            this.groupBox3.TabIndex = 20;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "英數分離";
            // 
            // lblResult2
            // 
            this.lblResult2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblResult2.Location = new System.Drawing.Point(11, 201);
            this.lblResult2.Name = "lblResult2";
            this.lblResult2.Size = new System.Drawing.Size(273, 74);
            this.lblResult2.TabIndex = 26;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(11, 186);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(34, 12);
            this.label9.TabIndex = 25;
            this.label9.Text = "Result";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(11, 99);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(26, 12);
            this.label10.TabIndex = 24;
            this.label10.Text = "Text";
            // 
            // txtInput
            // 
            this.txtInput.AcceptsReturn = true;
            this.txtInput.Location = new System.Drawing.Point(11, 114);
            this.txtInput.Multiline = true;
            this.txtInput.Name = "txtInput";
            this.txtInput.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.txtInput.Size = new System.Drawing.Size(273, 74);
            this.txtInput.TabIndex = 23;
            this.txtInput.Text = "Archer, Ann\r\nBaker, Bob\r\nCarter, Cindy\r\nDeevers, Dan";
            this.txtInput.TextChanged += new System.EventHandler(this.do_regular_expression);
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(11, 54);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(100, 12);
            this.label11.TabIndex = 22;
            this.label11.Text = "Replacement Pattern";
            // 
            // txtReplacementPattern2
            // 
            this.txtReplacementPattern2.Location = new System.Drawing.Point(11, 69);
            this.txtReplacementPattern2.Name = "txtReplacementPattern2";
            this.txtReplacementPattern2.Size = new System.Drawing.Size(273, 22);
            this.txtReplacementPattern2.TabIndex = 21;
            this.txtReplacementPattern2.Text = "$2 $1";
            this.txtReplacementPattern2.TextChanged += new System.EventHandler(this.do_regular_expression);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(11, 18);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(37, 12);
            this.label12.TabIndex = 20;
            this.label12.Text = "Pattern";
            // 
            // txtPattern2
            // 
            this.txtPattern2.Location = new System.Drawing.Point(11, 32);
            this.txtPattern2.Name = "txtPattern2";
            this.txtPattern2.Size = new System.Drawing.Size(273, 22);
            this.txtPattern2.TabIndex = 19;
            this.txtPattern2.Text = "(?m)^([^,]*), ([^\\r]*)\\r?$";
            this.txtPattern2.TextChanged += new System.EventHandler(this.do_regular_expression);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(765, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(321, 579);
            this.richTextBox1.TabIndex = 21;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(341, 258);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(160, 40);
            this.button2.TabIndex = 24;
            this.button2.Text = "驗證每個月的天數";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(341, 221);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(160, 22);
            this.textBox2.TabIndex = 23;
            this.textBox2.Text = "25";
            this.textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_email
            // 
            this.tb_email.Location = new System.Drawing.Point(341, 314);
            this.tb_email.Name = "tb_email";
            this.tb_email.Size = new System.Drawing.Size(160, 22);
            this.tb_email.TabIndex = 30;
            this.tb_email.Text = "david@yahoo.com.tw";
            this.tb_email.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_rul
            // 
            this.tb_rul.Location = new System.Drawing.Point(341, 402);
            this.tb_rul.Name = "tb_rul";
            this.tb_rul.Size = new System.Drawing.Size(160, 22);
            this.tb_rul.TabIndex = 31;
            this.tb_rul.Text = "http://www.yahoo.com.tw";
            this.tb_rul.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(341, 350);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(160, 40);
            this.button6.TabIndex = 32;
            this.button6.Text = "驗證Email格式";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(341, 439);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(160, 40);
            this.button7.TabIndex = 33;
            this.button7.Text = "驗證URl網址格式";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(586, 12);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(160, 40);
            this.button8.TabIndex = 34;
            this.button8.Text = "all";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(586, 63);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(160, 40);
            this.button9.TabIndex = 35;
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(586, 115);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(160, 40);
            this.button10.TabIndex = 36;
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(586, 165);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(160, 40);
            this.button11.TabIndex = 37;
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(586, 218);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(160, 40);
            this.button12.TabIndex = 38;
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(586, 264);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(160, 40);
            this.button13.TabIndex = 39;
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(586, 315);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(160, 40);
            this.button14.TabIndex = 40;
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(586, 366);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(160, 40);
            this.button15.TabIndex = 41;
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(586, 419);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(160, 40);
            this.button16.TabIndex = 42;
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(586, 465);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(160, 40);
            this.button17.TabIndex = 43;
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(586, 511);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(160, 40);
            this.button18.TabIndex = 44;
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1086, 579);
            this.Controls.Add(this.button18);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button16);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.tb_rul);
            this.Controls.Add(this.tb_email);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtDigits;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtLetters;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtString;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox2;
        internal System.Windows.Forms.TextBox txtTestString;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.Label lblResult;
        internal System.Windows.Forms.Label label5;
        internal System.Windows.Forms.TextBox txtReplacementPattern;
        internal System.Windows.Forms.Label label6;
        internal System.Windows.Forms.TextBox txtPattern;
        internal System.Windows.Forms.Label label7;
        private System.Windows.Forms.GroupBox groupBox3;
        internal System.Windows.Forms.Label lblResult2;
        internal System.Windows.Forms.Label label9;
        internal System.Windows.Forms.Label label10;
        internal System.Windows.Forms.TextBox txtInput;
        internal System.Windows.Forms.Label label11;
        internal System.Windows.Forms.TextBox txtReplacementPattern2;
        internal System.Windows.Forms.Label label12;
        internal System.Windows.Forms.TextBox txtPattern2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox tb_email;
        private System.Windows.Forms.TextBox tb_rul;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
    }
}

