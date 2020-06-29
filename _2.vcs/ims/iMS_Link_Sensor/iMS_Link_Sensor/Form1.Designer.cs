namespace iMS_Link_Sensor
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox21 = new System.Windows.Forms.GroupBox();
            this.button86 = new System.Windows.Forms.Button();
            this.button89 = new System.Windows.Forms.Button();
            this.button90 = new System.Windows.Forms.Button();
            this.label54 = new System.Windows.Forms.Label();
            this.label55 = new System.Windows.Forms.Label();
            this.comboBox6 = new System.Windows.Forms.ComboBox();
            this.comboBox7 = new System.Windows.Forms.ComboBox();
            this.button93 = new System.Windows.Forms.Button();
            this.button92 = new System.Windows.Forms.Button();
            this.button91 = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.timer_clock = new System.Windows.Forms.Timer(this.components);
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox21.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.Color.Black;
            this.richTextBox1.Font = new System.Drawing.Font("Courier New", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox1.ForeColor = System.Drawing.Color.White;
            this.richTextBox1.Location = new System.Drawing.Point(519, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(348, 480);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // groupBox21
            // 
            this.groupBox21.Controls.Add(this.button86);
            this.groupBox21.Controls.Add(this.button89);
            this.groupBox21.Controls.Add(this.button90);
            this.groupBox21.Controls.Add(this.label54);
            this.groupBox21.Controls.Add(this.label55);
            this.groupBox21.Controls.Add(this.comboBox6);
            this.groupBox21.Controls.Add(this.comboBox7);
            this.groupBox21.Location = new System.Drawing.Point(5, 10);
            this.groupBox21.Name = "groupBox21";
            this.groupBox21.Size = new System.Drawing.Size(508, 99);
            this.groupBox21.TabIndex = 34;
            this.groupBox21.TabStop = false;
            this.groupBox21.Text = "Comport";
            // 
            // button86
            // 
            this.button86.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button86.Location = new System.Drawing.Point(200, 41);
            this.button86.Name = "button86";
            this.button86.Size = new System.Drawing.Size(87, 33);
            this.button86.TabIndex = 28;
            this.button86.Text = "COM Scan";
            this.button86.UseVisualStyleBackColor = true;
            this.button86.Click += new System.EventHandler(this.button86_Click);
            // 
            // button89
            // 
            this.button89.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button89.Location = new System.Drawing.Point(306, 40);
            this.button89.Name = "button89";
            this.button89.Size = new System.Drawing.Size(75, 33);
            this.button89.TabIndex = 22;
            this.button89.Text = "Connect";
            this.button89.UseVisualStyleBackColor = true;
            this.button89.Click += new System.EventHandler(this.button89_Click);
            // 
            // button90
            // 
            this.button90.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button90.Location = new System.Drawing.Point(399, 42);
            this.button90.Name = "button90";
            this.button90.Size = new System.Drawing.Size(91, 33);
            this.button90.TabIndex = 23;
            this.button90.Text = "Disconnect";
            this.button90.UseVisualStyleBackColor = true;
            this.button90.Click += new System.EventHandler(this.button90_Click);
            // 
            // label54
            // 
            this.label54.AutoSize = true;
            this.label54.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label54.Location = new System.Drawing.Point(16, 23);
            this.label54.Name = "label54";
            this.label54.Size = new System.Drawing.Size(80, 21);
            this.label54.TabIndex = 24;
            this.label54.Text = "Comport";
            // 
            // label55
            // 
            this.label55.AutoSize = true;
            this.label55.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label55.Location = new System.Drawing.Point(120, 23);
            this.label55.Name = "label55";
            this.label55.Size = new System.Drawing.Size(52, 21);
            this.label55.TabIndex = 25;
            this.label55.Text = "Baud";
            // 
            // comboBox6
            // 
            this.comboBox6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox6.FormattingEnabled = true;
            this.comboBox6.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox6.Location = new System.Drawing.Point(112, 47);
            this.comboBox6.Name = "comboBox6";
            this.comboBox6.Size = new System.Drawing.Size(77, 24);
            this.comboBox6.TabIndex = 27;
            this.comboBox6.Text = "115200";
            // 
            // comboBox7
            // 
            this.comboBox7.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox7.FormattingEnabled = true;
            this.comboBox7.Location = new System.Drawing.Point(11, 47);
            this.comboBox7.Name = "comboBox7";
            this.comboBox7.Size = new System.Drawing.Size(92, 24);
            this.comboBox7.TabIndex = 26;
            // 
            // button93
            // 
            this.button93.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button93.Location = new System.Drawing.Point(287, 325);
            this.button93.Name = "button93";
            this.button93.Size = new System.Drawing.Size(172, 63);
            this.button93.TabIndex = 103;
            this.button93.Text = "到自動模式";
            this.button93.UseVisualStyleBackColor = true;
            this.button93.Click += new System.EventHandler(this.button93_Click);
            // 
            // button92
            // 
            this.button92.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button92.Location = new System.Drawing.Point(287, 202);
            this.button92.Name = "button92";
            this.button92.Size = new System.Drawing.Size(172, 63);
            this.button92.TabIndex = 102;
            this.button92.Text = "到手動模式";
            this.button92.UseVisualStyleBackColor = true;
            this.button92.Click += new System.EventHandler(this.button92_Click);
            // 
            // button91
            // 
            this.button91.BackColor = System.Drawing.Color.Black;
            this.button91.Font = new System.Drawing.Font("新細明體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button91.ForeColor = System.Drawing.Color.Gold;
            this.button91.Location = new System.Drawing.Point(39, 206);
            this.button91.Name = "button91";
            this.button91.Size = new System.Drawing.Size(175, 169);
            this.button91.TabIndex = 101;
            this.button91.Text = "LED";
            this.button91.UseVisualStyleBackColor = false;
            this.button91.Click += new System.EventHandler(this.button91_Click);
            // 
            // serialPort1
            // 
            this.serialPort1.RtsEnable = true;
            // 
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Enabled = true;
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("Arial", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(47, 140);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(107, 34);
            this.lb_main_mesg1.TabIndex = 134;
            this.lb_main_mesg1.Text = "mesg1";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 494);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(876, 22);
            this.statusStrip1.TabIndex = 135;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(0, 17);
            // 
            // timer_clock
            // 
            this.timer_clock.Enabled = true;
            this.timer_clock.Interval = 1000;
            this.timer_clock.Tick += new System.EventHandler(this.timer_clock_Tick);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(808, 458);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(56, 33);
            this.button1.TabIndex = 29;
            this.button1.Text = "Clear";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(876, 516);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.button93);
            this.Controls.Add(this.button92);
            this.Controls.Add(this.button91);
            this.Controls.Add(this.groupBox21);
            this.Controls.Add(this.richTextBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "ims camera";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox21.ResumeLayout(false);
            this.groupBox21.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox21;
        private System.Windows.Forms.Button button86;
        private System.Windows.Forms.Button button89;
        private System.Windows.Forms.Button button90;
        private System.Windows.Forms.Label label54;
        private System.Windows.Forms.Label label55;
        private System.Windows.Forms.ComboBox comboBox6;
        private System.Windows.Forms.ComboBox comboBox7;
        private System.Windows.Forms.Button button93;
        private System.Windows.Forms.Button button92;
        private System.Windows.Forms.Button button91;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.Timer timer_clock;
        private System.Windows.Forms.Button button1;
    }
}

