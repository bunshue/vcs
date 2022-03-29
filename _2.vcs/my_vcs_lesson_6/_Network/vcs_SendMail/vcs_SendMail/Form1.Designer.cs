namespace vcs_SendMail
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
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.richTextBox_mail = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_clear_attachments = new System.Windows.Forms.Button();
            this.bt_browse_attachments = new System.Windows.Forms.Button();
            this.bt_send = new System.Windows.Forms.Button();
            this.label11 = new System.Windows.Forms.Label();
            this.tb_mail_body = new System.Windows.Forms.TextBox();
            this.tb_email_addr_from_password = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.tb_mail_subject = new System.Windows.Forms.TextBox();
            this.tb_smtp_server = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.tb_attach_filename = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.tb_email_addr_bcc = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.tb_email_addr_cc = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.tb_email_addr_to_nicknane = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tb_email_addr_to = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.tb_email_addr_from_nicknane = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tb_email_addr_from = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 66);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(160, 48);
            this.button1.TabIndex = 0;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(437, 472);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(811, 241);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // richTextBox_mail
            // 
            this.richTextBox_mail.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox_mail.Location = new System.Drawing.Point(12, 403);
            this.richTextBox_mail.Name = "richTextBox_mail";
            this.richTextBox_mail.Size = new System.Drawing.Size(405, 263);
            this.richTextBox_mail.TabIndex = 2;
            this.richTextBox_mail.Text = "莫聽穿林打葉聲，何妨吟嘯且徐行。\n竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。\n料峭春風吹酒醒，微冷，山頭斜照卻相迎。\n回首向來蕭瑟處，歸去，也無風雨也無晴。\n";
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 120);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(160, 48);
            this.button2.TabIndex = 3;
            this.button2.Text = "用gmail寄信 c";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 174);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(160, 48);
            this.button3.TabIndex = 4;
            this.button3.Text = "用gmail寄信 d";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(12, 228);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(160, 48);
            this.button4.TabIndex = 5;
            this.button4.Text = "用gmail寄信 e";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(12, 282);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(160, 48);
            this.button5.TabIndex = 6;
            this.button5.Text = "用gmail寄信 f";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(12, 336);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(160, 48);
            this.button6.TabIndex = 7;
            this.button6.Text = "使用SmtpMail2類別寄信";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button7.Location = new System.Drawing.Point(216, 12);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(160, 48);
            this.button7.TabIndex = 8;
            this.button7.Text = "使用Email類別寄信1";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button8.Location = new System.Drawing.Point(216, 66);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(160, 48);
            this.button8.TabIndex = 9;
            this.button8.Text = "使用Email類別寄信2";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(216, 120);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(160, 48);
            this.button9.TabIndex = 10;
            this.button9.Text = "使用Email類別寄信3";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button10.Location = new System.Drawing.Point(216, 174);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(160, 48);
            this.button10.TabIndex = 11;
            this.button10.Text = "使用Email類別寄信4";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(958, 609);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(78, 37);
            this.bt_clear.TabIndex = 18;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(12, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(160, 48);
            this.button0.TabIndex = 19;
            this.button0.Text = "用gmail寄信 a";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button11
            // 
            this.button11.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button11.Location = new System.Drawing.Point(216, 228);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(160, 48);
            this.button11.TabIndex = 20;
            this.button11.Text = "使用SendMail類別寄信4";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button12
            // 
            this.button12.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button12.Location = new System.Drawing.Point(216, 282);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(160, 48);
            this.button12.TabIndex = 21;
            this.button12.Text = "用gmail寄信 NG";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button13
            // 
            this.button13.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button13.Location = new System.Drawing.Point(216, 336);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(160, 48);
            this.button13.TabIndex = 22;
            this.button13.Text = "用ymail寄信";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_clear_attachments);
            this.groupBox1.Controls.Add(this.bt_browse_attachments);
            this.groupBox1.Controls.Add(this.bt_send);
            this.groupBox1.Controls.Add(this.label11);
            this.groupBox1.Controls.Add(this.tb_mail_body);
            this.groupBox1.Controls.Add(this.tb_email_addr_from_password);
            this.groupBox1.Controls.Add(this.label10);
            this.groupBox1.Controls.Add(this.tb_mail_subject);
            this.groupBox1.Controls.Add(this.tb_smtp_server);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.tb_attach_filename);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.tb_email_addr_bcc);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.tb_email_addr_cc);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.tb_email_addr_to_nicknane);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.tb_email_addr_to);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.tb_email_addr_from_nicknane);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.tb_email_addr_from);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox1.Location = new System.Drawing.Point(437, 66);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(853, 376);
            this.groupBox1.TabIndex = 23;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "e-mail";
            // 
            // bt_clear_attachments
            // 
            this.bt_clear_attachments.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_attachments.Location = new System.Drawing.Point(509, 182);
            this.bt_clear_attachments.Name = "bt_clear_attachments";
            this.bt_clear_attachments.Size = new System.Drawing.Size(68, 40);
            this.bt_clear_attachments.TabIndex = 26;
            this.bt_clear_attachments.Text = "清除";
            this.bt_clear_attachments.UseVisualStyleBackColor = true;
            this.bt_clear_attachments.Click += new System.EventHandler(this.bt_clear_attachments_Click);
            // 
            // bt_browse_attachments
            // 
            this.bt_browse_attachments.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_browse_attachments.Location = new System.Drawing.Point(435, 182);
            this.bt_browse_attachments.Name = "bt_browse_attachments";
            this.bt_browse_attachments.Size = new System.Drawing.Size(68, 40);
            this.bt_browse_attachments.TabIndex = 25;
            this.bt_browse_attachments.Text = "瀏覽...";
            this.bt_browse_attachments.UseVisualStyleBackColor = true;
            this.bt_browse_attachments.Click += new System.EventHandler(this.bt_browse_attachments_Click);
            // 
            // bt_send
            // 
            this.bt_send.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_send.Location = new System.Drawing.Point(19, 270);
            this.bt_send.Name = "bt_send";
            this.bt_send.Size = new System.Drawing.Size(117, 84);
            this.bt_send.TabIndex = 24;
            this.bt_send.Text = "傳送";
            this.bt_send.UseVisualStyleBackColor = true;
            this.bt_send.Click += new System.EventHandler(this.bt_send_Click);
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label11.Location = new System.Drawing.Point(16, 232);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(72, 16);
            this.label11.TabIndex = 21;
            this.label11.Text = "郵件內容";
            // 
            // tb_mail_body
            // 
            this.tb_mail_body.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_mail_body.Location = new System.Drawing.Point(164, 229);
            this.tb_mail_body.Multiline = true;
            this.tb_mail_body.Name = "tb_mail_body";
            this.tb_mail_body.Size = new System.Drawing.Size(672, 125);
            this.tb_mail_body.TabIndex = 20;
            // 
            // tb_email_addr_from_password
            // 
            this.tb_email_addr_from_password.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_from_password.Location = new System.Drawing.Point(164, 122);
            this.tb_email_addr_from_password.Name = "tb_email_addr_from_password";
            this.tb_email_addr_from_password.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_from_password.TabIndex = 19;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label10.Location = new System.Drawing.Point(16, 125);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(40, 16);
            this.label10.TabIndex = 18;
            this.label10.Text = "密碼";
            // 
            // tb_mail_subject
            // 
            this.tb_mail_subject.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_mail_subject.Location = new System.Drawing.Point(164, 194);
            this.tb_mail_subject.Name = "tb_mail_subject";
            this.tb_mail_subject.Size = new System.Drawing.Size(253, 27);
            this.tb_mail_subject.TabIndex = 17;
            // 
            // tb_smtp_server
            // 
            this.tb_smtp_server.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_smtp_server.Location = new System.Drawing.Point(164, 93);
            this.tb_smtp_server.Name = "tb_smtp_server";
            this.tb_smtp_server.Size = new System.Drawing.Size(253, 27);
            this.tb_smtp_server.TabIndex = 15;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.Location = new System.Drawing.Point(16, 197);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(40, 16);
            this.label9.TabIndex = 16;
            this.label9.Text = "標題";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(16, 96);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(90, 16);
            this.label8.TabIndex = 14;
            this.label8.Text = "SMTP Server";
            // 
            // tb_attach_filename
            // 
            this.tb_attach_filename.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_attach_filename.Location = new System.Drawing.Point(583, 157);
            this.tb_attach_filename.Multiline = true;
            this.tb_attach_filename.Name = "tb_attach_filename";
            this.tb_attach_filename.Size = new System.Drawing.Size(253, 54);
            this.tb_attach_filename.TabIndex = 13;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(435, 157);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(40, 16);
            this.label7.TabIndex = 12;
            this.label7.Text = "附件";
            // 
            // tb_email_addr_bcc
            // 
            this.tb_email_addr_bcc.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_bcc.Location = new System.Drawing.Point(583, 124);
            this.tb_email_addr_bcc.Name = "tb_email_addr_bcc";
            this.tb_email_addr_bcc.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_bcc.TabIndex = 11;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(435, 125);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(72, 16);
            this.label6.TabIndex = 10;
            this.label6.Text = "密件副本";
            // 
            // tb_email_addr_cc
            // 
            this.tb_email_addr_cc.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_cc.Location = new System.Drawing.Point(583, 93);
            this.tb_email_addr_cc.Name = "tb_email_addr_cc";
            this.tb_email_addr_cc.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_cc.TabIndex = 9;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(435, 96);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(40, 16);
            this.label5.TabIndex = 8;
            this.label5.Text = "副本";
            // 
            // tb_email_addr_to_nicknane
            // 
            this.tb_email_addr_to_nicknane.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_to_nicknane.Location = new System.Drawing.Point(583, 63);
            this.tb_email_addr_to_nicknane.Name = "tb_email_addr_to_nicknane";
            this.tb_email_addr_to_nicknane.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_to_nicknane.TabIndex = 7;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(435, 66);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(120, 16);
            this.label3.TabIndex = 6;
            this.label3.Text = "收件者顯示名稱";
            // 
            // tb_email_addr_to
            // 
            this.tb_email_addr_to.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_to.Location = new System.Drawing.Point(583, 33);
            this.tb_email_addr_to.Name = "tb_email_addr_to";
            this.tb_email_addr_to.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_to.TabIndex = 5;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(435, 36);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(56, 16);
            this.label4.TabIndex = 4;
            this.label4.Text = "收件者";
            // 
            // tb_email_addr_from_nicknane
            // 
            this.tb_email_addr_from_nicknane.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_from_nicknane.Location = new System.Drawing.Point(164, 63);
            this.tb_email_addr_from_nicknane.Name = "tb_email_addr_from_nicknane";
            this.tb_email_addr_from_nicknane.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_from_nicknane.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(16, 66);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(120, 16);
            this.label2.TabIndex = 2;
            this.label2.Text = "寄件者顯示名稱";
            // 
            // tb_email_addr_from
            // 
            this.tb_email_addr_from.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_email_addr_from.Location = new System.Drawing.Point(164, 33);
            this.tb_email_addr_from.Name = "tb_email_addr_from";
            this.tb_email_addr_from.Size = new System.Drawing.Size(253, 27);
            this.tb_email_addr_from.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(16, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(56, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "寄件者";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1310, 705);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox_mail);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "vcs_SendMail";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.RichTextBox richTextBox_mail;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox tb_email_addr_to_nicknane;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tb_email_addr_to;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox tb_email_addr_from_nicknane;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tb_email_addr_from;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_email_addr_from_password;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox tb_mail_subject;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox tb_smtp_server;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox tb_attach_filename;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox tb_email_addr_bcc;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox tb_email_addr_cc;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button bt_send;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox tb_mail_body;
        private System.Windows.Forms.Button bt_browse_attachments;
        private System.Windows.Forms.Button bt_clear_attachments;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}

