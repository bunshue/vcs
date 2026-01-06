namespace vcs_DateTimePicker
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
            this.components = new System.ComponentModel.Container();
            this.dateTimePicker1 = new System.Windows.Forms.DateTimePicker();
            this.dateTimePicker2 = new System.Windows.Forms.DateTimePicker();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox8 = new System.Windows.Forms.GroupBox();
            this.lb_time_interval = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.dateTimePicker3 = new System.Windows.Forms.DateTimePicker();
            this.bt1 = new System.Windows.Forms.Button();
            this.bt2 = new System.Windows.Forms.Button();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.bt_dtp_get = new System.Windows.Forms.Button();
            this.bt_dtp_set = new System.Windows.Forms.Button();
            this.dateTimePicker4 = new System.Windows.Forms.DateTimePicker();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox8.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.SuspendLayout();
            // 
            // dateTimePicker1
            // 
            this.dateTimePicker1.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.dateTimePicker1.Location = new System.Drawing.Point(33, 49);
            this.dateTimePicker1.Name = "dateTimePicker1";
            this.dateTimePicker1.Size = new System.Drawing.Size(288, 36);
            this.dateTimePicker1.TabIndex = 0;
            // 
            // dateTimePicker2
            // 
            this.dateTimePicker2.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.dateTimePicker2.Format = System.Windows.Forms.DateTimePickerFormat.Time;
            this.dateTimePicker2.Location = new System.Drawing.Point(33, 149);
            this.dateTimePicker2.Name = "dateTimePicker2";
            this.dateTimePicker2.ShowUpDown = true;
            this.dateTimePicker2.Size = new System.Drawing.Size(288, 36);
            this.dateTimePicker2.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(341, 57);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 24);
            this.label1.TabIndex = 2;
            this.label1.Text = "預設";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(341, 157);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(394, 24);
            this.label2.TabIndex = 3;
            this.label2.Text = "改Format為Time、ShowUpDown為True";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(743, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(355, 565);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // groupBox8
            // 
            this.groupBox8.Controls.Add(this.lb_time_interval);
            this.groupBox8.Controls.Add(this.textBox2);
            this.groupBox8.Controls.Add(this.dateTimePicker3);
            this.groupBox8.Controls.Add(this.bt1);
            this.groupBox8.Controls.Add(this.bt2);
            this.groupBox8.Location = new System.Drawing.Point(33, 215);
            this.groupBox8.Name = "groupBox8";
            this.groupBox8.Size = new System.Drawing.Size(220, 140);
            this.groupBox8.TabIndex = 89;
            this.groupBox8.TabStop = false;
            this.groupBox8.Text = "DateTimePicker";
            // 
            // lb_time_interval
            // 
            this.lb_time_interval.AutoSize = true;
            this.lb_time_interval.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_time_interval.Location = new System.Drawing.Point(9, 106);
            this.lb_time_interval.Name = "lb_time_interval";
            this.lb_time_interval.Size = new System.Drawing.Size(139, 21);
            this.lb_time_interval.TabIndex = 113;
            this.lb_time_interval.Text = "lb_time_interval";
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox2.Location = new System.Drawing.Point(10, 24);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(150, 36);
            this.textBox2.TabIndex = 49;
            this.textBox2.Text = "10";
            this.textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // dateTimePicker3
            // 
            this.dateTimePicker3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.dateTimePicker3.Location = new System.Drawing.Point(10, 69);
            this.dateTimePicker3.Name = "dateTimePicker3";
            this.dateTimePicker3.Size = new System.Drawing.Size(150, 30);
            this.dateTimePicker3.TabIndex = 37;
            this.dateTimePicker3.ValueChanged += new System.EventHandler(this.dateTimePicker3_ValueChanged);
            // 
            // bt1
            // 
            this.bt1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt1.Location = new System.Drawing.Point(166, 25);
            this.bt1.Name = "bt1";
            this.bt1.Size = new System.Drawing.Size(55, 30);
            this.bt1.TabIndex = 70;
            this.bt1.Text = "倒數";
            this.bt1.UseVisualStyleBackColor = true;
            this.bt1.Click += new System.EventHandler(this.bt1_Click);
            // 
            // bt2
            // 
            this.bt2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt2.Location = new System.Drawing.Point(166, 74);
            this.bt2.Name = "bt2";
            this.bt2.Size = new System.Drawing.Size(55, 30);
            this.bt2.TabIndex = 71;
            this.bt2.Text = "恢復";
            this.bt2.UseVisualStyleBackColor = true;
            this.bt2.Click += new System.EventHandler(this.bt2_Click);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.bt_dtp_get);
            this.groupBox5.Controls.Add(this.bt_dtp_set);
            this.groupBox5.Controls.Add(this.dateTimePicker4);
            this.groupBox5.Location = new System.Drawing.Point(287, 215);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(160, 140);
            this.groupBox5.TabIndex = 88;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "DateTimePicker";
            // 
            // bt_dtp_get
            // 
            this.bt_dtp_get.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_dtp_get.Location = new System.Drawing.Point(10, 63);
            this.bt_dtp_get.Name = "bt_dtp_get";
            this.bt_dtp_get.Size = new System.Drawing.Size(80, 35);
            this.bt_dtp_get.TabIndex = 86;
            this.bt_dtp_get.Text = "取得時間";
            this.bt_dtp_get.UseVisualStyleBackColor = true;
            this.bt_dtp_get.Click += new System.EventHandler(this.bt_dtp_get_Click);
            // 
            // bt_dtp_set
            // 
            this.bt_dtp_set.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_dtp_set.Location = new System.Drawing.Point(10, 24);
            this.bt_dtp_set.Name = "bt_dtp_set";
            this.bt_dtp_set.Size = new System.Drawing.Size(80, 35);
            this.bt_dtp_set.TabIndex = 85;
            this.bt_dtp_set.Text = "設定範圍";
            this.bt_dtp_set.UseVisualStyleBackColor = true;
            this.bt_dtp_set.Click += new System.EventHandler(this.bt_dtp_set_Click);
            // 
            // dateTimePicker4
            // 
            this.dateTimePicker4.Location = new System.Drawing.Point(10, 104);
            this.dateTimePicker4.Name = "dateTimePicker4";
            this.dateTimePicker4.Size = new System.Drawing.Size(147, 22);
            this.dateTimePicker4.TabIndex = 83;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1019, 540);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(79, 37);
            this.bt_clear.TabIndex = 90;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1112, 589);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox8);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dateTimePicker2);
            this.Controls.Add(this.dateTimePicker1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox8.ResumeLayout(false);
            this.groupBox8.PerformLayout();
            this.groupBox5.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DateTimePicker dateTimePicker1;
        private System.Windows.Forms.DateTimePicker dateTimePicker2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox8;
        private System.Windows.Forms.Label lb_time_interval;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.DateTimePicker dateTimePicker3;
        private System.Windows.Forms.Button bt1;
        private System.Windows.Forms.Button bt2;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Button bt_dtp_get;
        private System.Windows.Forms.Button bt_dtp_set;
        private System.Windows.Forms.DateTimePicker dateTimePicker4;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button bt_clear;
    }
}

