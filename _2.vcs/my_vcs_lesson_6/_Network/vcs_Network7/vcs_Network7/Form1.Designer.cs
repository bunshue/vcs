﻿namespace vcs_Network7
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblPerson = new System.Windows.Forms.Label();
            this.lblNum = new System.Windows.Forms.Label();
            this.lblPage = new System.Windows.Forms.Label();
            this.lblSpeed = new System.Windows.Forms.Label();
            this.bt_stop = new System.Windows.Forms.Button();
            this.bt_resume = new System.Windows.Forms.Button();
            this.bt_pause = new System.Windows.Forms.Button();
            this.bt_start = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.richTextBox_html1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.richTextBox_html2 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_clear_html1 = new System.Windows.Forms.Button();
            this.bt_clear_html2 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.lblPerson);
            this.groupBox1.Controls.Add(this.lblNum);
            this.groupBox1.Controls.Add(this.lblPage);
            this.groupBox1.Controls.Add(this.lblSpeed);
            this.groupBox1.Controls.Add(this.bt_stop);
            this.groupBox1.Controls.Add(this.bt_resume);
            this.groupBox1.Controls.Add(this.bt_pause);
            this.groupBox1.Controls.Add(this.bt_start);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(513, 207);
            this.groupBox1.TabIndex = 47;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "網頁爬蟲";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(155, 164);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 18;
            this.label1.Text = "label1";
            // 
            // lblPerson
            // 
            this.lblPerson.AutoSize = true;
            this.lblPerson.Location = new System.Drawing.Point(155, 126);
            this.lblPerson.Name = "lblPerson";
            this.lblPerson.Size = new System.Drawing.Size(36, 12);
            this.lblPerson.TabIndex = 17;
            this.lblPerson.Text = "Person";
            // 
            // lblNum
            // 
            this.lblNum.AutoSize = true;
            this.lblNum.Location = new System.Drawing.Point(155, 94);
            this.lblNum.Name = "lblNum";
            this.lblNum.Size = new System.Drawing.Size(28, 12);
            this.lblNum.TabIndex = 16;
            this.lblNum.Text = "Num";
            // 
            // lblPage
            // 
            this.lblPage.AutoSize = true;
            this.lblPage.Location = new System.Drawing.Point(155, 52);
            this.lblPage.Name = "lblPage";
            this.lblPage.Size = new System.Drawing.Size(27, 12);
            this.lblPage.TabIndex = 15;
            this.lblPage.Text = "Page";
            // 
            // lblSpeed
            // 
            this.lblSpeed.AutoSize = true;
            this.lblSpeed.Location = new System.Drawing.Point(155, 21);
            this.lblSpeed.Name = "lblSpeed";
            this.lblSpeed.Size = new System.Drawing.Size(33, 12);
            this.lblSpeed.TabIndex = 14;
            this.lblSpeed.Text = "Speed";
            // 
            // bt_stop
            // 
            this.bt_stop.Location = new System.Drawing.Point(33, 164);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(75, 23);
            this.bt_stop.TabIndex = 13;
            this.bt_stop.Text = "結束";
            this.bt_stop.UseVisualStyleBackColor = true;
            this.bt_stop.Click += new System.EventHandler(this.bt_stop_Click);
            // 
            // bt_resume
            // 
            this.bt_resume.Location = new System.Drawing.Point(33, 115);
            this.bt_resume.Name = "bt_resume";
            this.bt_resume.Size = new System.Drawing.Size(75, 23);
            this.bt_resume.TabIndex = 12;
            this.bt_resume.Text = "繼續";
            this.bt_resume.UseVisualStyleBackColor = true;
            this.bt_resume.Click += new System.EventHandler(this.bt_resume_Click);
            // 
            // bt_pause
            // 
            this.bt_pause.Location = new System.Drawing.Point(33, 68);
            this.bt_pause.Name = "bt_pause";
            this.bt_pause.Size = new System.Drawing.Size(75, 23);
            this.bt_pause.TabIndex = 11;
            this.bt_pause.Text = "暫停";
            this.bt_pause.UseVisualStyleBackColor = true;
            this.bt_pause.Click += new System.EventHandler(this.bt_pause_Click);
            // 
            // bt_start
            // 
            this.bt_start.Location = new System.Drawing.Point(33, 21);
            this.bt_start.Name = "bt_start";
            this.bt_start.Size = new System.Drawing.Size(75, 23);
            this.bt_start.TabIndex = 10;
            this.bt_start.Text = "開始";
            this.bt_start.UseVisualStyleBackColor = true;
            this.bt_start.Click += new System.EventHandler(this.bt_start_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(656, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(439, 350);
            this.richTextBox1.TabIndex = 48;
            this.richTextBox1.Text = "";
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(22, 270);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(399, 30);
            this.textBox1.TabIndex = 49;
            this.textBox1.Text = "https://pydoing.blogspot.com/";
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(449, 230);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(172, 70);
            this.button3.TabIndex = 50;
            this.button3.Text = "獲取遠程網頁中的所有鏈接URL";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // richTextBox_html1
            // 
            this.richTextBox_html1.Location = new System.Drawing.Point(17, 378);
            this.richTextBox_html1.Name = "richTextBox_html1";
            this.richTextBox_html1.Size = new System.Drawing.Size(512, 437);
            this.richTextBox_html1.TabIndex = 51;
            this.richTextBox_html1.Text = resources.GetString("richTextBox_html1.Text");
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(17, 745);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(172, 70);
            this.button1.TabIndex = 52;
            this.button1.Text = "獲取此網頁原始碼中所有鏈接URL";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button4
            // 
            this.button4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.Location = new System.Drawing.Point(547, 745);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(172, 70);
            this.button4.TabIndex = 56;
            this.button4.Text = "獲取此網頁原始碼中所有鏈接URL";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // richTextBox_html2
            // 
            this.richTextBox_html2.Location = new System.Drawing.Point(547, 378);
            this.richTextBox_html2.Name = "richTextBox_html2";
            this.richTextBox_html2.Size = new System.Drawing.Size(512, 437);
            this.richTextBox_html2.TabIndex = 55;
            this.richTextBox_html2.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1018, 308);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(62, 32);
            this.bt_clear.TabIndex = 57;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_clear_html1
            // 
            this.bt_clear_html1.Location = new System.Drawing.Point(449, 766);
            this.bt_clear_html1.Name = "bt_clear_html1";
            this.bt_clear_html1.Size = new System.Drawing.Size(62, 32);
            this.bt_clear_html1.TabIndex = 58;
            this.bt_clear_html1.Text = "Clear";
            this.bt_clear_html1.UseVisualStyleBackColor = true;
            this.bt_clear_html1.Click += new System.EventHandler(this.bt_clear_html1_Click);
            // 
            // bt_clear_html2
            // 
            this.bt_clear_html2.Location = new System.Drawing.Point(979, 766);
            this.bt_clear_html2.Name = "bt_clear_html2";
            this.bt_clear_html2.Size = new System.Drawing.Size(62, 32);
            this.bt_clear_html2.TabIndex = 59;
            this.bt_clear_html2.Text = "Clear";
            this.bt_clear_html2.UseVisualStyleBackColor = true;
            this.bt_clear_html2.Click += new System.EventHandler(this.bt_clear_html2_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(449, 302);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(172, 70);
            this.button2.TabIndex = 60;
            this.button2.Text = "獲取遠程網頁中的所有鏈接URL";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(1126, 12);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(172, 70);
            this.button5.TabIndex = 61;
            this.button5.Text = "抓取網頁裡面的所有鏈接";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1416, 846);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.bt_clear_html2);
            this.Controls.Add(this.bt_clear_html1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.richTextBox_html2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox_html1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblPerson;
        private System.Windows.Forms.Label lblNum;
        private System.Windows.Forms.Label lblPage;
        private System.Windows.Forms.Label lblSpeed;
        private System.Windows.Forms.Button bt_stop;
        private System.Windows.Forms.Button bt_resume;
        private System.Windows.Forms.Button bt_pause;
        private System.Windows.Forms.Button bt_start;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.RichTextBox richTextBox_html1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.RichTextBox richTextBox_html2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_clear_html1;
        private System.Windows.Forms.Button bt_clear_html2;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button5;
    }
}

