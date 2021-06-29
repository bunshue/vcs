namespace vcs_MP3AlarmClock
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_ack = new System.Windows.Forms.Button();
            this.lb_mesg = new System.Windows.Forms.Label();
            this.lb_result = new System.Windows.Forms.Label();
            this.bt_cancel = new System.Windows.Forms.Button();
            this.bt_ok = new System.Windows.Forms.Button();
            this.nud_ss = new System.Windows.Forms.NumericUpDown();
            this.lb_time = new System.Windows.Forms.Label();
            this.nud_mm = new System.Windows.Forms.NumericUpDown();
            this.lb_date = new System.Windows.Forms.Label();
            this.nud_hh = new System.Windows.Forms.NumericUpDown();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.timer_date = new System.Windows.Forms.Timer(this.components);
            this.bt_clear = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_ss)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_mm)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_hh)).BeginInit();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(14, 6);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(482, 22);
            this.textBox1.TabIndex = 5;
            // 
            // axWindowsMediaPlayer1
            // 
            this.axWindowsMediaPlayer1.Enabled = true;
            this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(433, 36);
            this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            this.axWindowsMediaPlayer1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axWindowsMediaPlayer1.OcxState")));
            this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(63, 47);
            this.axWindowsMediaPlayer1.TabIndex = 8;
            this.axWindowsMediaPlayer1.Visible = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(509, 6);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(468, 524);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_ack);
            this.groupBox1.Controls.Add(this.lb_mesg);
            this.groupBox1.Controls.Add(this.lb_result);
            this.groupBox1.Controls.Add(this.bt_cancel);
            this.groupBox1.Controls.Add(this.bt_ok);
            this.groupBox1.Controls.Add(this.nud_ss);
            this.groupBox1.Controls.Add(this.lb_time);
            this.groupBox1.Controls.Add(this.nud_mm);
            this.groupBox1.Controls.Add(this.lb_date);
            this.groupBox1.Controls.Add(this.nud_hh);
            this.groupBox1.Controls.Add(this.rb3);
            this.groupBox1.Controls.Add(this.rb2);
            this.groupBox1.Controls.Add(this.rb1);
            this.groupBox1.Location = new System.Drawing.Point(7, 89);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(489, 296);
            this.groupBox1.TabIndex = 12;
            this.groupBox1.TabStop = false;
            // 
            // bt_ack
            // 
            this.bt_ack.Location = new System.Drawing.Point(402, 221);
            this.bt_ack.Name = "bt_ack";
            this.bt_ack.Size = new System.Drawing.Size(75, 62);
            this.bt_ack.TabIndex = 20;
            this.bt_ack.Text = "我知道了";
            this.bt_ack.UseVisualStyleBackColor = true;
            this.bt_ack.Click += new System.EventHandler(this.bt_ack_Click);
            // 
            // lb_mesg
            // 
            this.lb_mesg.AutoSize = true;
            this.lb_mesg.Font = new System.Drawing.Font("Consolas", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_mesg.Location = new System.Drawing.Point(223, 246);
            this.lb_mesg.Name = "lb_mesg";
            this.lb_mesg.Size = new System.Drawing.Size(89, 37);
            this.lb_mesg.TabIndex = 19;
            this.lb_mesg.Text = "mesg";
            // 
            // lb_result
            // 
            this.lb_result.AutoSize = true;
            this.lb_result.Font = new System.Drawing.Font("Consolas", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_result.ForeColor = System.Drawing.Color.Purple;
            this.lb_result.Location = new System.Drawing.Point(16, 208);
            this.lb_result.Name = "lb_result";
            this.lb_result.Size = new System.Drawing.Size(125, 37);
            this.lb_result.TabIndex = 18;
            this.lb_result.Text = "result";
            // 
            // bt_cancel
            // 
            this.bt_cancel.Location = new System.Drawing.Point(108, 260);
            this.bt_cancel.Name = "bt_cancel";
            this.bt_cancel.Size = new System.Drawing.Size(75, 23);
            this.bt_cancel.TabIndex = 17;
            this.bt_cancel.Text = "取消";
            this.bt_cancel.UseVisualStyleBackColor = true;
            this.bt_cancel.Click += new System.EventHandler(this.bt_cancel_Click);
            // 
            // bt_ok
            // 
            this.bt_ok.Location = new System.Drawing.Point(23, 260);
            this.bt_ok.Name = "bt_ok";
            this.bt_ok.Size = new System.Drawing.Size(75, 23);
            this.bt_ok.TabIndex = 16;
            this.bt_ok.Text = "確定";
            this.bt_ok.UseVisualStyleBackColor = true;
            this.bt_ok.Click += new System.EventHandler(this.bt_ok_Click);
            // 
            // nud_ss
            // 
            this.nud_ss.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_ss.Location = new System.Drawing.Point(287, 92);
            this.nud_ss.Maximum = new decimal(new int[] {
            59,
            0,
            0,
            0});
            this.nud_ss.Name = "nud_ss";
            this.nud_ss.Size = new System.Drawing.Size(91, 46);
            this.nud_ss.TabIndex = 15;
            this.nud_ss.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_ss.ValueChanged += new System.EventHandler(this.nud_hhmmss_ValueChanged);
            // 
            // lb_time
            // 
            this.lb_time.AutoSize = true;
            this.lb_time.Font = new System.Drawing.Font("Consolas", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_time.ForeColor = System.Drawing.Color.Purple;
            this.lb_time.Location = new System.Drawing.Point(101, 52);
            this.lb_time.Name = "lb_time";
            this.lb_time.Size = new System.Drawing.Size(89, 37);
            this.lb_time.TabIndex = 4;
            this.lb_time.Text = "time";
            // 
            // nud_mm
            // 
            this.nud_mm.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_mm.Location = new System.Drawing.Point(189, 92);
            this.nud_mm.Maximum = new decimal(new int[] {
            59,
            0,
            0,
            0});
            this.nud_mm.Name = "nud_mm";
            this.nud_mm.Size = new System.Drawing.Size(91, 46);
            this.nud_mm.TabIndex = 14;
            this.nud_mm.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_mm.ValueChanged += new System.EventHandler(this.nud_hhmmss_ValueChanged);
            // 
            // lb_date
            // 
            this.lb_date.AutoSize = true;
            this.lb_date.Font = new System.Drawing.Font("Consolas", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_date.ForeColor = System.Drawing.Color.Purple;
            this.lb_date.Location = new System.Drawing.Point(94, 15);
            this.lb_date.Name = "lb_date";
            this.lb_date.Size = new System.Drawing.Size(89, 37);
            this.lb_date.TabIndex = 3;
            this.lb_date.Text = "date";
            // 
            // nud_hh
            // 
            this.nud_hh.Font = new System.Drawing.Font("新細明體", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_hh.Location = new System.Drawing.Point(92, 92);
            this.nud_hh.Maximum = new decimal(new int[] {
            23,
            0,
            0,
            0});
            this.nud_hh.Name = "nud_hh";
            this.nud_hh.Size = new System.Drawing.Size(91, 46);
            this.nud_hh.TabIndex = 13;
            this.nud_hh.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.nud_hh.ValueChanged += new System.EventHandler(this.nud_hhmmss_ValueChanged);
            // 
            // rb3
            // 
            this.rb3.AutoSize = true;
            this.rb3.Location = new System.Drawing.Point(23, 113);
            this.rb3.Name = "rb3";
            this.rb3.Size = new System.Drawing.Size(47, 16);
            this.rb3.TabIndex = 2;
            this.rb3.Text = "之後";
            this.rb3.UseVisualStyleBackColor = true;
            this.rb3.CheckedChanged += new System.EventHandler(this.rb_CheckedChanged);
            // 
            // rb2
            // 
            this.rb2.AutoSize = true;
            this.rb2.Location = new System.Drawing.Point(23, 71);
            this.rb2.Name = "rb2";
            this.rb2.Size = new System.Drawing.Size(47, 16);
            this.rb2.TabIndex = 1;
            this.rb2.Text = "設定";
            this.rb2.UseVisualStyleBackColor = true;
            this.rb2.CheckedChanged += new System.EventHandler(this.rb_CheckedChanged);
            // 
            // rb1
            // 
            this.rb1.AutoSize = true;
            this.rb1.Checked = true;
            this.rb1.Location = new System.Drawing.Point(23, 35);
            this.rb1.Name = "rb1";
            this.rb1.Size = new System.Drawing.Size(47, 16);
            this.rb1.TabIndex = 0;
            this.rb1.TabStop = true;
            this.rb1.Text = "現在";
            this.rb1.UseVisualStyleBackColor = true;
            this.rb1.CheckedChanged += new System.EventHandler(this.rb_CheckedChanged);
            // 
            // timer_date
            // 
            this.timer_date.Enabled = true;
            this.timer_date.Interval = 1000;
            this.timer_date.Tick += new System.EventHandler(this.timer_date_Tick);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(902, 507);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(75, 23);
            this.bt_clear.TabIndex = 18;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(14, 47);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(47, 36);
            this.button1.TabIndex = 19;
            this.button1.Text = "選檔";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(76, 47);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(47, 36);
            this.button2.TabIndex = 20;
            this.button2.Text = "試聽";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(989, 542);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.axWindowsMediaPlayer1);
            this.Controls.Add(this.textBox1);
            this.Name = "Form1";
            this.Text = "mp3鬧鐘";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.axWindowsMediaPlayer1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_ss)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_mm)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_hh)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.TextBox textBox1;
        private AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.Label lb_time;
        private System.Windows.Forms.Label lb_date;
        private System.Windows.Forms.Timer timer_date;
        private System.Windows.Forms.NumericUpDown nud_ss;
        private System.Windows.Forms.NumericUpDown nud_mm;
        private System.Windows.Forms.NumericUpDown nud_hh;
        private System.Windows.Forms.Button bt_cancel;
        private System.Windows.Forms.Button bt_ok;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Label lb_result;
        private System.Windows.Forms.Label lb_mesg;
        private System.Windows.Forms.Button bt_ack;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}

