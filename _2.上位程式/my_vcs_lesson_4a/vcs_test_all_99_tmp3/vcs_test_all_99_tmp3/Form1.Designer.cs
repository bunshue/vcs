namespace vcs_test_all_99_tmp3
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.button5 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.button6 = new System.Windows.Forms.Button();
            this.label7 = new System.Windows.Forms.Label();
            this.textBox_hex = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.button9 = new System.Windows.Forms.Button();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.button10 = new System.Windows.Forms.Button();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.button_start_thread = new System.Windows.Forms.Button();
            this.button_stop_thread = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button16 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.label13 = new System.Windows.Forms.Label();
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.timer3 = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(34, 135);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(82, 24);
            this.label1.TabIndex = 4;
            this.label1.Text = "帳號：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(34, 185);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(82, 24);
            this.label2.TabIndex = 5;
            this.label2.Text = "密碼：";
            // 
            // button5
            // 
            this.button5.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.Location = new System.Drawing.Point(72, 244);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(88, 45);
            this.button5.TabIndex = 6;
            this.button5.Text = "登入";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(108, 132);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(200, 36);
            this.textBox1.TabIndex = 7;
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox2.Location = new System.Drawing.Point(108, 182);
            this.textBox2.Name = "textBox2";
            this.textBox2.PasswordChar = '*';
            this.textBox2.Size = new System.Drawing.Size(200, 36);
            this.textBox2.TabIndex = 8;
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(183, 244);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(88, 45);
            this.button6.TabIndex = 9;
            this.button6.Text = "清除";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(357, 27);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(357, 24);
            this.label7.TabIndex = 16;
            this.label7.Text = "最多輸入8個字的十六進位數字：";
            // 
            // textBox_hex
            // 
            this.textBox_hex.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox_hex.Location = new System.Drawing.Point(412, 77);
            this.textBox_hex.MaxLength = 8;
            this.textBox_hex.Name = "textBox_hex";
            this.textBox_hex.Size = new System.Drawing.Size(149, 36);
            this.textBox_hex.TabIndex = 17;
            this.textBox_hex.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox_hex_KeyPress);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(843, 144);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(82, 24);
            this.label8.TabIndex = 18;
            this.label8.Text = "結果：";
            // 
            // button9
            // 
            this.button9.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.Location = new System.Drawing.Point(594, 68);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(180, 45);
            this.button9.TabIndex = 19;
            this.button9.Text = "轉換為十進位";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 503);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(994, 24);
            this.statusStrip1.TabIndex = 20;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(158, 19);
            this.toolStripStatusLabel1.Text = "toolStripStatusLabel1";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.Location = new System.Drawing.Point(368, 149);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(346, 24);
            this.label9.TabIndex = 21;
            this.label9.Text = "ToolStripStatusLabel顯示系統時間";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label10.Location = new System.Drawing.Point(368, 185);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(559, 24);
            this.label10.TabIndex = 22;
            this.label10.Text = "ToolStripStatusLabel 控制項放置在 StatusStrip 控制項中";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label11.Location = new System.Drawing.Point(374, 80);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(32, 24);
            this.label11.TabIndex = 23;
            this.label11.Text = "0x";
            // 
            // button10
            // 
            this.button10.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button10.Location = new System.Drawing.Point(372, 244);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(120, 45);
            this.button10.TabIndex = 24;
            this.button10.Text = "測試Delay";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // textBox3
            // 
            this.textBox3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox3.Location = new System.Drawing.Point(508, 251);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(94, 36);
            this.textBox3.TabIndex = 25;
            this.textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button_start_thread
            // 
            this.button_start_thread.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button_start_thread.Location = new System.Drawing.Point(634, 244);
            this.button_start_thread.Name = "button_start_thread";
            this.button_start_thread.Size = new System.Drawing.Size(127, 45);
            this.button_start_thread.TabIndex = 26;
            this.button_start_thread.Text = "開啟thread";
            this.button_start_thread.UseVisualStyleBackColor = true;
            this.button_start_thread.Click += new System.EventHandler(this.button_start_thread_Click);
            // 
            // button_stop_thread
            // 
            this.button_stop_thread.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button_stop_thread.Location = new System.Drawing.Point(776, 244);
            this.button_stop_thread.Name = "button_stop_thread";
            this.button_stop_thread.Size = new System.Drawing.Size(129, 45);
            this.button_stop_thread.TabIndex = 27;
            this.button_stop_thread.Text = "關閉thread";
            this.button_stop_thread.UseVisualStyleBackColor = true;
            this.button_stop_thread.Click += new System.EventHandler(this.button_stop_thread_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button16);
            this.groupBox2.Controls.Add(this.button15);
            this.groupBox2.Controls.Add(this.button14);
            this.groupBox2.Controls.Add(this.label13);
            this.groupBox2.Controls.Add(this.progressBar1);
            this.groupBox2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox2.Location = new System.Drawing.Point(38, 320);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(643, 100);
            this.groupBox2.TabIndex = 30;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "測試Progress Bar";
            // 
            // button16
            // 
            this.button16.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button16.Location = new System.Drawing.Point(380, 29);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(79, 34);
            this.button16.TabIndex = 33;
            this.button16.Text = "清除";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // button15
            // 
            this.button15.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button15.Location = new System.Drawing.Point(550, 29);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(77, 34);
            this.button15.TabIndex = 32;
            this.button15.Text = "開始2";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // button14
            // 
            this.button14.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button14.Location = new System.Drawing.Point(465, 29);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(79, 34);
            this.button14.TabIndex = 31;
            this.button14.Text = "開始1";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label13.Location = new System.Drawing.Point(18, 26);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(147, 27);
            this.label13.TabIndex = 1;
            this.label13.Text = "讀取進度：";
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(22, 65);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(606, 29);
            this.progressBar1.TabIndex = 0;
            // 
            // timer3
            // 
            this.timer3.Tick += new System.EventHandler(this.timer3_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(994, 527);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.button_stop_thread);
            this.Controls.Add(this.button_start_thread);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.textBox_hex);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox textBox_hex;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Button button_start_thread;
        private System.Windows.Forms.Button button_stop_thread;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Timer timer3;
        private System.Windows.Forms.Button button16;
    }
}

