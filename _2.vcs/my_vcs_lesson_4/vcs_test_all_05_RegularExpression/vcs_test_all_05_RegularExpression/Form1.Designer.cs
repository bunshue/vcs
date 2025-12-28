namespace vcs_test_all_05_RegularExpression
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
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.tb_email = new System.Windows.Forms.TextBox();
            this.tb_rul = new System.Windows.Forms.TextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.bt_re3 = new System.Windows.Forms.Button();
            this.bt_re2 = new System.Windows.Forms.Button();
            this.bt_re1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.bt_re6 = new System.Windows.Forms.Button();
            this.bt_re5 = new System.Windows.Forms.Button();
            this.txtInput2 = new System.Windows.Forms.TextBox();
            this.bt_re4 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox0.SuspendLayout();
            this.groupBox4.SuspendLayout();
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
            this.groupBox1.Location = new System.Drawing.Point(218, 350);
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
            this.groupBox2.Location = new System.Drawing.Point(485, 15);
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
            this.groupBox3.Location = new System.Drawing.Point(485, 213);
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
            this.richTextBox1.Location = new System.Drawing.Point(1051, 17);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 21;
            this.richTextBox1.Text = "";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(18, 27);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(160, 22);
            this.textBox2.TabIndex = 23;
            this.textBox2.Text = "25";
            this.textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_email
            // 
            this.tb_email.Location = new System.Drawing.Point(18, 120);
            this.tb_email.Name = "tb_email";
            this.tb_email.Size = new System.Drawing.Size(160, 22);
            this.tb_email.TabIndex = 30;
            this.tb_email.Text = "david@yahoo.com.tw";
            this.tb_email.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_rul
            // 
            this.tb_rul.Location = new System.Drawing.Point(18, 208);
            this.tb_rul.Name = "tb_rul";
            this.tb_rul.Size = new System.Drawing.Size(160, 22);
            this.tb_rul.TabIndex = 31;
            this.tb_rul.Text = "http://www.yahoo.com.tw";
            this.tb_rul.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1067, 43);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(65, 37);
            this.bt_clear.TabIndex = 65;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 75);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(200, 60);
            this.button1.TabIndex = 66;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(12, 9);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(200, 60);
            this.button0.TabIndex = 67;
            this.button0.Text = "正規表示式的使用";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 200);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(200, 60);
            this.button3.TabIndex = 68;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(12, 266);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(200, 60);
            this.button4.TabIndex = 69;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(12, 332);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(200, 60);
            this.button5.TabIndex = 70;
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.bt_re3);
            this.groupBox0.Controls.Add(this.textBox2);
            this.groupBox0.Controls.Add(this.tb_email);
            this.groupBox0.Controls.Add(this.bt_re2);
            this.groupBox0.Controls.Add(this.tb_rul);
            this.groupBox0.Controls.Add(this.bt_re1);
            this.groupBox0.Location = new System.Drawing.Point(232, 12);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(229, 307);
            this.groupBox0.TabIndex = 71;
            this.groupBox0.TabStop = false;
            // 
            // bt_re3
            // 
            this.bt_re3.Location = new System.Drawing.Point(18, 241);
            this.bt_re3.Name = "bt_re3";
            this.bt_re3.Size = new System.Drawing.Size(160, 40);
            this.bt_re3.TabIndex = 34;
            this.bt_re3.Text = "驗證URl網址格式";
            this.bt_re3.UseVisualStyleBackColor = true;
            this.bt_re3.Click += new System.EventHandler(this.bt_re3_Click);
            // 
            // bt_re2
            // 
            this.bt_re2.Location = new System.Drawing.Point(18, 156);
            this.bt_re2.Name = "bt_re2";
            this.bt_re2.Size = new System.Drawing.Size(160, 40);
            this.bt_re2.TabIndex = 34;
            this.bt_re2.Text = "驗證Email格式";
            this.bt_re2.UseVisualStyleBackColor = true;
            this.bt_re2.Click += new System.EventHandler(this.bt_re2_Click);
            // 
            // bt_re1
            // 
            this.bt_re1.Location = new System.Drawing.Point(18, 65);
            this.bt_re1.Name = "bt_re1";
            this.bt_re1.Size = new System.Drawing.Size(160, 40);
            this.bt_re1.TabIndex = 34;
            this.bt_re1.Text = "驗證每個月的天數";
            this.bt_re1.UseVisualStyleBackColor = true;
            this.bt_re1.Click += new System.EventHandler(this.bt_re1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 138);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(200, 60);
            this.button2.TabIndex = 72;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(12, 399);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(200, 60);
            this.button6.TabIndex = 73;
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button7.Location = new System.Drawing.Point(12, 465);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(200, 60);
            this.button7.TabIndex = 74;
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.bt_re6);
            this.groupBox4.Controls.Add(this.bt_re5);
            this.groupBox4.Controls.Add(this.txtInput2);
            this.groupBox4.Controls.Add(this.bt_re4);
            this.groupBox4.Location = new System.Drawing.Point(825, 17);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(154, 232);
            this.groupBox4.TabIndex = 75;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "正則表達式";
            // 
            // bt_re6
            // 
            this.bt_re6.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_re6.Location = new System.Drawing.Point(6, 168);
            this.bt_re6.Name = "bt_re6";
            this.bt_re6.Size = new System.Drawing.Size(142, 42);
            this.bt_re6.TabIndex = 59;
            this.bt_re6.Text = "驗證身份證字號";
            this.bt_re6.UseVisualStyleBackColor = true;
            this.bt_re6.Click += new System.EventHandler(this.bt_re6_Click);
            // 
            // bt_re5
            // 
            this.bt_re5.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_re5.Location = new System.Drawing.Point(6, 120);
            this.bt_re5.Name = "bt_re5";
            this.bt_re5.Size = new System.Drawing.Size(142, 42);
            this.bt_re5.TabIndex = 58;
            this.bt_re5.Text = "檢查身分證格式";
            this.bt_re5.UseVisualStyleBackColor = true;
            this.bt_re5.Click += new System.EventHandler(this.bt_re5_Click);
            // 
            // txtInput2
            // 
            this.txtInput2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.txtInput2.Location = new System.Drawing.Point(6, 25);
            this.txtInput2.Name = "txtInput2";
            this.txtInput2.Size = new System.Drawing.Size(142, 30);
            this.txtInput2.TabIndex = 46;
            this.txtInput2.Text = "P123456789";
            // 
            // bt_re4
            // 
            this.bt_re4.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_re4.Location = new System.Drawing.Point(6, 70);
            this.bt_re4.Name = "bt_re4";
            this.bt_re4.Size = new System.Drawing.Size(142, 42);
            this.bt_re4.TabIndex = 57;
            this.bt_re4.Text = "檢查手機號碼格式";
            this.bt_re4.UseVisualStyleBackColor = true;
            this.bt_re4.Click += new System.EventHandler(this.bt_re4_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1367, 722);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.bt_clear);
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
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);

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
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox tb_email;
        private System.Windows.Forms.TextBox tb_rul;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.Button bt_re1;
        private System.Windows.Forms.Button bt_re2;
        private System.Windows.Forms.Button bt_re3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button bt_re6;
        private System.Windows.Forms.Button bt_re5;
        private System.Windows.Forms.TextBox txtInput2;
        private System.Windows.Forms.Button bt_re4;
    }
}

