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
            this.lb_gain = new System.Windows.Forms.Label();
            this.trackBar_gain = new System.Windows.Forms.TrackBar();
            this.lb_expo = new System.Windows.Forms.Label();
            this.trackBar_expo = new System.Windows.Forms.TrackBar();
            this.numericUpDown_gain = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown_expo = new System.Windows.Forms.NumericUpDown();
            this.tb_gain = new System.Windows.Forms.TextBox();
            this.tb_expo = new System.Windows.Forms.TextBox();
            this.lb_range_5 = new System.Windows.Forms.Label();
            this.lb_range_4 = new System.Windows.Forms.Label();
            this.bt_setup_gain = new System.Windows.Forms.Button();
            this.bt_setup_expo = new System.Windows.Forms.Button();
            this.lb_0x4 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lb_awb_result_gain = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.lb_awb_result_expo = new System.Windows.Forms.Label();
            this.groupBox21.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gain)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_expo)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_gain)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_expo)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.Color.Black;
            this.richTextBox1.Font = new System.Drawing.Font("Courier New", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox1.ForeColor = System.Drawing.Color.White;
            this.richTextBox1.Location = new System.Drawing.Point(621, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(378, 569);
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
            this.button93.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button93.Location = new System.Drawing.Point(326, 115);
            this.button93.Name = "button93";
            this.button93.Size = new System.Drawing.Size(196, 63);
            this.button93.TabIndex = 103;
            this.button93.Text = "自動曝光(AE) 開";
            this.button93.UseVisualStyleBackColor = true;
            this.button93.Visible = false;
            this.button93.Click += new System.EventHandler(this.button93_Click);
            // 
            // button92
            // 
            this.button92.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button92.Location = new System.Drawing.Point(326, 184);
            this.button92.Name = "button92";
            this.button92.Size = new System.Drawing.Size(190, 190);
            this.button92.TabIndex = 102;
            this.button92.Text = "自動曝光(AE) 關 EXPO = 50";
            this.button92.UseVisualStyleBackColor = true;
            this.button92.Click += new System.EventHandler(this.button92_Click);
            // 
            // button91
            // 
            this.button91.BackColor = System.Drawing.Color.Black;
            this.button91.Font = new System.Drawing.Font("新細明體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button91.ForeColor = System.Drawing.Color.Gold;
            this.button91.Location = new System.Drawing.Point(83, 184);
            this.button91.Name = "button91";
            this.button91.Size = new System.Drawing.Size(190, 190);
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
            this.lb_main_mesg1.Location = new System.Drawing.Point(110, 127);
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
            this.statusStrip1.Location = new System.Drawing.Point(0, 582);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(1005, 22);
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
            this.button1.Location = new System.Drawing.Point(943, 546);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(56, 33);
            this.button1.TabIndex = 29;
            this.button1.Text = "Clear";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // lb_gain
            // 
            this.lb_gain.AutoSize = true;
            this.lb_gain.Location = new System.Drawing.Point(7, 112);
            this.lb_gain.Name = "lb_gain";
            this.lb_gain.Size = new System.Drawing.Size(33, 12);
            this.lb_gain.TabIndex = 139;
            this.lb_gain.Text = "GAIN";
            // 
            // trackBar_gain
            // 
            this.trackBar_gain.LargeChange = 1;
            this.trackBar_gain.Location = new System.Drawing.Point(9, 131);
            this.trackBar_gain.Maximum = 511;
            this.trackBar_gain.Name = "trackBar_gain";
            this.trackBar_gain.Size = new System.Drawing.Size(324, 45);
            this.trackBar_gain.TabIndex = 138;
            this.trackBar_gain.TickStyle = System.Windows.Forms.TickStyle.TopLeft;
            this.trackBar_gain.Value = 59;
            this.trackBar_gain.Scroll += new System.EventHandler(this.trackBar_gain_Scroll);
            // 
            // lb_expo
            // 
            this.lb_expo.AutoSize = true;
            this.lb_expo.Location = new System.Drawing.Point(6, 29);
            this.lb_expo.Name = "lb_expo";
            this.lb_expo.Size = new System.Drawing.Size(34, 12);
            this.lb_expo.TabIndex = 137;
            this.lb_expo.Text = "EXPO";
            // 
            // trackBar_expo
            // 
            this.trackBar_expo.LargeChange = 1;
            this.trackBar_expo.Location = new System.Drawing.Point(9, 59);
            this.trackBar_expo.Maximum = 511;
            this.trackBar_expo.Name = "trackBar_expo";
            this.trackBar_expo.Size = new System.Drawing.Size(324, 45);
            this.trackBar_expo.TabIndex = 136;
            this.trackBar_expo.TickStyle = System.Windows.Forms.TickStyle.TopLeft;
            this.trackBar_expo.Value = 50;
            this.trackBar_expo.Scroll += new System.EventHandler(this.trackBar_expo_Scroll);
            // 
            // numericUpDown_gain
            // 
            this.numericUpDown_gain.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.numericUpDown_gain.Location = new System.Drawing.Point(440, 122);
            this.numericUpDown_gain.Maximum = new decimal(new int[] {
            511,
            0,
            0,
            0});
            this.numericUpDown_gain.Name = "numericUpDown_gain";
            this.numericUpDown_gain.Size = new System.Drawing.Size(64, 32);
            this.numericUpDown_gain.TabIndex = 145;
            this.numericUpDown_gain.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown_gain.ValueChanged += new System.EventHandler(this.numericUpDown_gain_ValueChanged);
            this.numericUpDown_gain.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.numericUpDown_gain_KeyPress);
            // 
            // numericUpDown_expo
            // 
            this.numericUpDown_expo.Font = new System.Drawing.Font("Arial Narrow", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.numericUpDown_expo.Location = new System.Drawing.Point(440, 59);
            this.numericUpDown_expo.Maximum = new decimal(new int[] {
            511,
            0,
            0,
            0});
            this.numericUpDown_expo.Name = "numericUpDown_expo";
            this.numericUpDown_expo.Size = new System.Drawing.Size(64, 32);
            this.numericUpDown_expo.TabIndex = 144;
            this.numericUpDown_expo.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown_expo.ValueChanged += new System.EventHandler(this.numericUpDown_expo_ValueChanged);
            this.numericUpDown_expo.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.numericUpDown_expo_KeyPress);
            // 
            // tb_gain
            // 
            this.tb_gain.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_gain.Location = new System.Drawing.Point(361, 122);
            this.tb_gain.Name = "tb_gain";
            this.tb_gain.Size = new System.Drawing.Size(58, 32);
            this.tb_gain.TabIndex = 141;
            this.tb_gain.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tb_gain.TextChanged += new System.EventHandler(this.tb_gain_TextChanged);
            this.tb_gain.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.tb_gain_KeyPress);
            // 
            // tb_expo
            // 
            this.tb_expo.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_expo.Location = new System.Drawing.Point(361, 59);
            this.tb_expo.Name = "tb_expo";
            this.tb_expo.Size = new System.Drawing.Size(58, 32);
            this.tb_expo.TabIndex = 140;
            this.tb_expo.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tb_expo.TextChanged += new System.EventHandler(this.tb_expo_TextChanged);
            this.tb_expo.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.tb_expo_KeyPress);
            // 
            // lb_range_5
            // 
            this.lb_range_5.AutoSize = true;
            this.lb_range_5.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_range_5.Location = new System.Drawing.Point(367, 154);
            this.lb_range_5.Name = "lb_range_5";
            this.lb_range_5.Size = new System.Drawing.Size(127, 20);
            this.lb_range_5.TabIndex = 143;
            this.lb_range_5.Text = "0~1FF           0~511";
            // 
            // lb_range_4
            // 
            this.lb_range_4.AutoSize = true;
            this.lb_range_4.Font = new System.Drawing.Font("Arial Narrow", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_range_4.Location = new System.Drawing.Point(367, 90);
            this.lb_range_4.Name = "lb_range_4";
            this.lb_range_4.Size = new System.Drawing.Size(127, 20);
            this.lb_range_4.TabIndex = 142;
            this.lb_range_4.Text = "0~1FF           0~511";
            // 
            // bt_setup_gain
            // 
            this.bt_setup_gain.BackColor = System.Drawing.SystemColors.Control;
            this.bt_setup_gain.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup_gain.ForeColor = System.Drawing.Color.Blue;
            this.bt_setup_gain.Location = new System.Drawing.Point(523, 123);
            this.bt_setup_gain.Name = "bt_setup_gain";
            this.bt_setup_gain.Size = new System.Drawing.Size(58, 32);
            this.bt_setup_gain.TabIndex = 147;
            this.bt_setup_gain.Text = "確定";
            this.bt_setup_gain.UseVisualStyleBackColor = false;
            this.bt_setup_gain.Click += new System.EventHandler(this.bt_setup_gain_Click);
            // 
            // bt_setup_expo
            // 
            this.bt_setup_expo.BackColor = System.Drawing.SystemColors.Control;
            this.bt_setup_expo.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup_expo.ForeColor = System.Drawing.Color.Blue;
            this.bt_setup_expo.Location = new System.Drawing.Point(523, 59);
            this.bt_setup_expo.Name = "bt_setup_expo";
            this.bt_setup_expo.Size = new System.Drawing.Size(58, 32);
            this.bt_setup_expo.TabIndex = 146;
            this.bt_setup_expo.Text = "確定";
            this.bt_setup_expo.UseVisualStyleBackColor = false;
            this.bt_setup_expo.Click += new System.EventHandler(this.bt_setup_expo_Click);
            // 
            // lb_0x4
            // 
            this.lb_0x4.AutoSize = true;
            this.lb_0x4.Font = new System.Drawing.Font("Arial Narrow", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_0x4.Location = new System.Drawing.Point(335, 62);
            this.lb_0x4.Name = "lb_0x4";
            this.lb_0x4.Size = new System.Drawing.Size(104, 23);
            this.lb_0x4.TabIndex = 148;
            this.lb_0x4.Text = "0x                 =";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial Narrow", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(335, 125);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(104, 23);
            this.label1.TabIndex = 149;
            this.label1.Text = "0x                 =";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lb_awb_result_gain);
            this.groupBox1.Controls.Add(this.button2);
            this.groupBox1.Controls.Add(this.lb_awb_result_expo);
            this.groupBox1.Controls.Add(this.tb_gain);
            this.groupBox1.Controls.Add(this.tb_expo);
            this.groupBox1.Controls.Add(this.bt_setup_gain);
            this.groupBox1.Controls.Add(this.lb_expo);
            this.groupBox1.Controls.Add(this.bt_setup_expo);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.numericUpDown_gain);
            this.groupBox1.Controls.Add(this.lb_0x4);
            this.groupBox1.Controls.Add(this.numericUpDown_expo);
            this.groupBox1.Controls.Add(this.trackBar_expo);
            this.groupBox1.Controls.Add(this.trackBar_gain);
            this.groupBox1.Controls.Add(this.lb_gain);
            this.groupBox1.Controls.Add(this.lb_range_5);
            this.groupBox1.Controls.Add(this.lb_range_4);
            this.groupBox1.Location = new System.Drawing.Point(18, 385);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(597, 181);
            this.groupBox1.TabIndex = 150;
            this.groupBox1.TabStop = false;
            // 
            // lb_awb_result_gain
            // 
            this.lb_awb_result_gain.AutoSize = true;
            this.lb_awb_result_gain.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_awb_result_gain.Location = new System.Drawing.Point(71, 105);
            this.lb_awb_result_gain.Name = "lb_awb_result_gain";
            this.lb_awb_result_gain.Size = new System.Drawing.Size(48, 19);
            this.lb_awb_result_gain.TabIndex = 152;
            this.lb_awb_result_gain.Text = "GAIN";
            // 
            // button2
            // 
            this.button2.BackColor = System.Drawing.SystemColors.Control;
            this.button2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.ForeColor = System.Drawing.Color.Blue;
            this.button2.Location = new System.Drawing.Point(523, 18);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(58, 32);
            this.button2.TabIndex = 150;
            this.button2.Text = "讀取";
            this.button2.UseVisualStyleBackColor = false;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // lb_awb_result_expo
            // 
            this.lb_awb_result_expo.AutoSize = true;
            this.lb_awb_result_expo.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_awb_result_expo.Location = new System.Drawing.Point(71, 24);
            this.lb_awb_result_expo.Name = "lb_awb_result_expo";
            this.lb_awb_result_expo.Size = new System.Drawing.Size(54, 19);
            this.lb_awb_result_expo.TabIndex = 151;
            this.lb_awb_result_expo.Text = "EXPO";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1005, 604);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.button93);
            this.Controls.Add(this.button92);
            this.Controls.Add(this.button91);
            this.Controls.Add(this.groupBox21);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "ims camera";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox21.ResumeLayout(false);
            this.groupBox21.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gain)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_expo)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_gain)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_expo)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
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
        private System.Windows.Forms.Label lb_gain;
        private System.Windows.Forms.TrackBar trackBar_gain;
        private System.Windows.Forms.Label lb_expo;
        private System.Windows.Forms.TrackBar trackBar_expo;
        private System.Windows.Forms.NumericUpDown numericUpDown_gain;
        private System.Windows.Forms.NumericUpDown numericUpDown_expo;
        private System.Windows.Forms.TextBox tb_gain;
        private System.Windows.Forms.TextBox tb_expo;
        private System.Windows.Forms.Label lb_range_5;
        private System.Windows.Forms.Label lb_range_4;
        private System.Windows.Forms.Button bt_setup_gain;
        private System.Windows.Forms.Button bt_setup_expo;
        private System.Windows.Forms.Label lb_0x4;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label lb_awb_result_gain;
        private System.Windows.Forms.Label lb_awb_result_expo;
    }
}

