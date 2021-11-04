namespace vcs_Comport3
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.bt_clear = new System.Windows.Forms.Button();
            this.SerialPortTimer100ms1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox_comport1 = new System.Windows.Forms.GroupBox();
            this.comboBox_comport1 = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport1 = new System.Windows.Forms.PictureBox();
            this.comboBox_baud_rate1 = new System.Windows.Forms.ComboBox();
            this.bt_comport_scan1 = new System.Windows.Forms.Button();
            this.bt_comport_connect1 = new System.Windows.Forms.Button();
            this.bt_comport_disconnect1 = new System.Windows.Forms.Button();
            this.serialPort2 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms2 = new System.Windows.Forms.Timer(this.components);
            this.bt_plc_1 = new System.Windows.Forms.Button();
            this.groupBox_comport2 = new System.Windows.Forms.GroupBox();
            this.comboBox_comport2 = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport2 = new System.Windows.Forms.PictureBox();
            this.comboBox_baud_rate2 = new System.Windows.Forms.ComboBox();
            this.bt_comport_scan2 = new System.Windows.Forms.Button();
            this.bt_comport_connect2 = new System.Windows.Forms.Button();
            this.bt_comport_disconnect2 = new System.Windows.Forms.Button();
            this.groupBox_plc = new System.Windows.Forms.GroupBox();
            this.lb_sn3 = new System.Windows.Forms.Label();
            this.lb_sn2 = new System.Windows.Forms.Label();
            this.lb_sn1 = new System.Windows.Forms.Label();
            this.bt_plc_generate_sn = new System.Windows.Forms.Button();
            this.lb_sn = new System.Windows.Forms.Label();
            this.tb_sn1 = new System.Windows.Forms.TextBox();
            this.tb_sn2 = new System.Windows.Forms.TextBox();
            this.bt_plc_8 = new System.Windows.Forms.Button();
            this.bt_plc_9 = new System.Windows.Forms.Button();
            this.lb_main_mesg1b = new System.Windows.Forms.Label();
            this.bt_plc_7 = new System.Windows.Forms.Button();
            this.bt_plc_6 = new System.Windows.Forms.Button();
            this.bt_plc_0 = new System.Windows.Forms.Button();
            this.bt_plc_5 = new System.Windows.Forms.Button();
            this.bt_plc_4 = new System.Windows.Forms.Button();
            this.bt_plc_3 = new System.Windows.Forms.Button();
            this.bt_plc_2 = new System.Windows.Forms.Button();
            this.lb_main_mesg1a = new System.Windows.Forms.Label();
            this.groupBox_pc = new System.Windows.Forms.GroupBox();
            this.lb_main_mesg2b = new System.Windows.Forms.Label();
            this.bt_pc_8 = new System.Windows.Forms.Button();
            this.bt_pc_7 = new System.Windows.Forms.Button();
            this.bt_pc_6 = new System.Windows.Forms.Button();
            this.bt_pc_0 = new System.Windows.Forms.Button();
            this.bt_pc_5 = new System.Windows.Forms.Button();
            this.lb_main_mesg2a = new System.Windows.Forms.Label();
            this.bt_pc_4 = new System.Windows.Forms.Button();
            this.bt_pc_1 = new System.Windows.Forms.Button();
            this.bt_pc_3 = new System.Windows.Forms.Button();
            this.bt_pc_2 = new System.Windows.Forms.Button();
            this.groupBox_ims = new System.Windows.Forms.GroupBox();
            this.lb_main_mesg3b = new System.Windows.Forms.Label();
            this.bt_ims_0 = new System.Windows.Forms.Button();
            this.bt_ims_5 = new System.Windows.Forms.Button();
            this.lb_main_mesg3a = new System.Windows.Forms.Label();
            this.bt_ims_4 = new System.Windows.Forms.Button();
            this.bt_ims_1 = new System.Windows.Forms.Button();
            this.bt_ims_3 = new System.Windows.Forms.Button();
            this.bt_ims_2 = new System.Windows.Forms.Button();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.lb_main_mesg0 = new System.Windows.Forms.Label();
            this.lb_sn_pc3 = new System.Windows.Forms.Label();
            this.lb_sn_pc2 = new System.Windows.Forms.Label();
            this.lb_sn_pc1 = new System.Windows.Forms.Label();
            this.groupBox_comport1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport1)).BeginInit();
            this.groupBox_comport2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport2)).BeginInit();
            this.groupBox_plc.SuspendLayout();
            this.groupBox_pc.SuspendLayout();
            this.groupBox_ims.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(890, 42);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(218, 483);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            this.richTextBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.richTextBox1_KeyPress);
            // 
            // serialPort1
            // 
            this.serialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(962, 445);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(75, 23);
            this.bt_clear.TabIndex = 13;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // SerialPortTimer100ms1
            // 
            this.SerialPortTimer100ms1.Tick += new System.EventHandler(this.SerialPortTimer100ms1_Tick);
            // 
            // groupBox_comport1
            // 
            this.groupBox_comport1.Controls.Add(this.comboBox_comport1);
            this.groupBox_comport1.Controls.Add(this.pictureBox_comport1);
            this.groupBox_comport1.Controls.Add(this.comboBox_baud_rate1);
            this.groupBox_comport1.Controls.Add(this.bt_comport_scan1);
            this.groupBox_comport1.Controls.Add(this.bt_comport_connect1);
            this.groupBox_comport1.Controls.Add(this.bt_comport_disconnect1);
            this.groupBox_comport1.Location = new System.Drawing.Point(13, 9);
            this.groupBox_comport1.Name = "groupBox_comport1";
            this.groupBox_comport1.Size = new System.Drawing.Size(421, 81);
            this.groupBox_comport1.TabIndex = 188;
            this.groupBox_comport1.TabStop = false;
            this.groupBox_comport1.Text = "連向PLC";
            // 
            // comboBox_comport1
            // 
            this.comboBox_comport1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_comport1.FormattingEnabled = true;
            this.comboBox_comport1.Location = new System.Drawing.Point(8, 29);
            this.comboBox_comport1.Name = "comboBox_comport1";
            this.comboBox_comport1.Size = new System.Drawing.Size(80, 27);
            this.comboBox_comport1.TabIndex = 19;
            // 
            // pictureBox_comport1
            // 
            this.pictureBox_comport1.Location = new System.Drawing.Point(350, 19);
            this.pictureBox_comport1.Name = "pictureBox_comport1";
            this.pictureBox_comport1.Size = new System.Drawing.Size(48, 48);
            this.pictureBox_comport1.TabIndex = 22;
            this.pictureBox_comport1.TabStop = false;
            // 
            // comboBox_baud_rate1
            // 
            this.comboBox_baud_rate1.Enabled = false;
            this.comboBox_baud_rate1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_baud_rate1.FormattingEnabled = true;
            this.comboBox_baud_rate1.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox_baud_rate1.Location = new System.Drawing.Point(92, 29);
            this.comboBox_baud_rate1.Name = "comboBox_baud_rate1";
            this.comboBox_baud_rate1.Size = new System.Drawing.Size(76, 27);
            this.comboBox_baud_rate1.TabIndex = 20;
            this.comboBox_baud_rate1.Text = "115200";
            // 
            // bt_comport_scan1
            // 
            this.bt_comport_scan1.Location = new System.Drawing.Point(170, 26);
            this.bt_comport_scan1.Name = "bt_comport_scan1";
            this.bt_comport_scan1.Size = new System.Drawing.Size(49, 33);
            this.bt_comport_scan1.TabIndex = 21;
            this.bt_comport_scan1.Text = "Scan";
            this.bt_comport_scan1.UseVisualStyleBackColor = true;
            this.bt_comport_scan1.Click += new System.EventHandler(this.bt_comport_scan1_Click);
            // 
            // bt_comport_connect1
            // 
            this.bt_comport_connect1.Location = new System.Drawing.Point(220, 26);
            this.bt_comport_connect1.Name = "bt_comport_connect1";
            this.bt_comport_connect1.Size = new System.Drawing.Size(58, 33);
            this.bt_comport_connect1.TabIndex = 0;
            this.bt_comport_connect1.Text = "Connect";
            this.bt_comport_connect1.UseVisualStyleBackColor = true;
            this.bt_comport_connect1.Click += new System.EventHandler(this.bt_comport_connect1_Click);
            // 
            // bt_comport_disconnect1
            // 
            this.bt_comport_disconnect1.Location = new System.Drawing.Point(278, 26);
            this.bt_comport_disconnect1.Name = "bt_comport_disconnect1";
            this.bt_comport_disconnect1.Size = new System.Drawing.Size(64, 33);
            this.bt_comport_disconnect1.TabIndex = 1;
            this.bt_comport_disconnect1.Text = "Disconnect";
            this.bt_comport_disconnect1.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect1.Click += new System.EventHandler(this.bt_comport_disconnect1_Click);
            // 
            // serialPort2
            // 
            this.serialPort2.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort2_DataReceived);
            // 
            // SerialPortTimer100ms2
            // 
            this.SerialPortTimer100ms2.Tick += new System.EventHandler(this.SerialPortTimer100ms2_Tick);
            // 
            // bt_plc_1
            // 
            this.bt_plc_1.Location = new System.Drawing.Point(14, 124);
            this.bt_plc_1.Name = "bt_plc_1";
            this.bt_plc_1.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_1.TabIndex = 23;
            this.bt_plc_1.Text = "讀取相機序號";
            this.bt_plc_1.UseVisualStyleBackColor = true;
            this.bt_plc_1.Click += new System.EventHandler(this.bt_plc_1_Click);
            // 
            // groupBox_comport2
            // 
            this.groupBox_comport2.Controls.Add(this.comboBox_comport2);
            this.groupBox_comport2.Controls.Add(this.pictureBox_comport2);
            this.groupBox_comport2.Controls.Add(this.comboBox_baud_rate2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_scan2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_connect2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_disconnect2);
            this.groupBox_comport2.Location = new System.Drawing.Point(13, 113);
            this.groupBox_comport2.Name = "groupBox_comport2";
            this.groupBox_comport2.Size = new System.Drawing.Size(421, 81);
            this.groupBox_comport2.TabIndex = 189;
            this.groupBox_comport2.TabStop = false;
            this.groupBox_comport2.Text = "連向IMS";
            // 
            // comboBox_comport2
            // 
            this.comboBox_comport2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_comport2.FormattingEnabled = true;
            this.comboBox_comport2.Location = new System.Drawing.Point(8, 29);
            this.comboBox_comport2.Name = "comboBox_comport2";
            this.comboBox_comport2.Size = new System.Drawing.Size(80, 27);
            this.comboBox_comport2.TabIndex = 19;
            // 
            // pictureBox_comport2
            // 
            this.pictureBox_comport2.Location = new System.Drawing.Point(350, 19);
            this.pictureBox_comport2.Name = "pictureBox_comport2";
            this.pictureBox_comport2.Size = new System.Drawing.Size(48, 48);
            this.pictureBox_comport2.TabIndex = 22;
            this.pictureBox_comport2.TabStop = false;
            // 
            // comboBox_baud_rate2
            // 
            this.comboBox_baud_rate2.Enabled = false;
            this.comboBox_baud_rate2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_baud_rate2.FormattingEnabled = true;
            this.comboBox_baud_rate2.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox_baud_rate2.Location = new System.Drawing.Point(92, 29);
            this.comboBox_baud_rate2.Name = "comboBox_baud_rate2";
            this.comboBox_baud_rate2.Size = new System.Drawing.Size(76, 27);
            this.comboBox_baud_rate2.TabIndex = 20;
            this.comboBox_baud_rate2.Text = "115200";
            // 
            // bt_comport_scan2
            // 
            this.bt_comport_scan2.Location = new System.Drawing.Point(170, 26);
            this.bt_comport_scan2.Name = "bt_comport_scan2";
            this.bt_comport_scan2.Size = new System.Drawing.Size(49, 33);
            this.bt_comport_scan2.TabIndex = 21;
            this.bt_comport_scan2.Text = "Scan";
            this.bt_comport_scan2.UseVisualStyleBackColor = true;
            this.bt_comport_scan2.Click += new System.EventHandler(this.bt_comport_scan2_Click);
            // 
            // bt_comport_connect2
            // 
            this.bt_comport_connect2.Location = new System.Drawing.Point(220, 26);
            this.bt_comport_connect2.Name = "bt_comport_connect2";
            this.bt_comport_connect2.Size = new System.Drawing.Size(58, 33);
            this.bt_comport_connect2.TabIndex = 0;
            this.bt_comport_connect2.Text = "Connect";
            this.bt_comport_connect2.UseVisualStyleBackColor = true;
            this.bt_comport_connect2.Click += new System.EventHandler(this.bt_comport_connect2_Click);
            // 
            // bt_comport_disconnect2
            // 
            this.bt_comport_disconnect2.Location = new System.Drawing.Point(278, 26);
            this.bt_comport_disconnect2.Name = "bt_comport_disconnect2";
            this.bt_comport_disconnect2.Size = new System.Drawing.Size(64, 33);
            this.bt_comport_disconnect2.TabIndex = 1;
            this.bt_comport_disconnect2.Text = "Disconnect";
            this.bt_comport_disconnect2.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect2.Click += new System.EventHandler(this.bt_comport_disconnect2_Click);
            // 
            // groupBox_plc
            // 
            this.groupBox_plc.Controls.Add(this.lb_sn3);
            this.groupBox_plc.Controls.Add(this.lb_sn2);
            this.groupBox_plc.Controls.Add(this.lb_sn1);
            this.groupBox_plc.Controls.Add(this.bt_plc_generate_sn);
            this.groupBox_plc.Controls.Add(this.lb_sn);
            this.groupBox_plc.Controls.Add(this.tb_sn1);
            this.groupBox_plc.Controls.Add(this.tb_sn2);
            this.groupBox_plc.Controls.Add(this.bt_plc_8);
            this.groupBox_plc.Controls.Add(this.bt_plc_9);
            this.groupBox_plc.Controls.Add(this.lb_main_mesg1b);
            this.groupBox_plc.Controls.Add(this.bt_plc_7);
            this.groupBox_plc.Controls.Add(this.bt_plc_6);
            this.groupBox_plc.Controls.Add(this.bt_plc_0);
            this.groupBox_plc.Controls.Add(this.bt_plc_5);
            this.groupBox_plc.Controls.Add(this.bt_plc_4);
            this.groupBox_plc.Controls.Add(this.bt_plc_3);
            this.groupBox_plc.Controls.Add(this.bt_plc_2);
            this.groupBox_plc.Controls.Add(this.lb_main_mesg1a);
            this.groupBox_plc.Controls.Add(this.bt_plc_1);
            this.groupBox_plc.Location = new System.Drawing.Point(13, 214);
            this.groupBox_plc.Name = "groupBox_plc";
            this.groupBox_plc.Size = new System.Drawing.Size(253, 460);
            this.groupBox_plc.TabIndex = 190;
            this.groupBox_plc.TabStop = false;
            this.groupBox_plc.Text = "PLC控制台";
            // 
            // lb_sn3
            // 
            this.lb_sn3.AutoSize = true;
            this.lb_sn3.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn3.Location = new System.Drawing.Point(114, 283);
            this.lb_sn3.Name = "lb_sn3";
            this.lb_sn3.Size = new System.Drawing.Size(60, 22);
            this.lb_sn3.TabIndex = 190;
            this.lb_sn3.Text = "S/N :";
            // 
            // lb_sn2
            // 
            this.lb_sn2.AutoSize = true;
            this.lb_sn2.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn2.Location = new System.Drawing.Point(114, 246);
            this.lb_sn2.Name = "lb_sn2";
            this.lb_sn2.Size = new System.Drawing.Size(60, 22);
            this.lb_sn2.TabIndex = 189;
            this.lb_sn2.Text = "S/N :";
            // 
            // lb_sn1
            // 
            this.lb_sn1.AutoSize = true;
            this.lb_sn1.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn1.Location = new System.Drawing.Point(114, 208);
            this.lb_sn1.Name = "lb_sn1";
            this.lb_sn1.Size = new System.Drawing.Size(60, 22);
            this.lb_sn1.TabIndex = 188;
            this.lb_sn1.Text = "S/N :";
            // 
            // bt_plc_generate_sn
            // 
            this.bt_plc_generate_sn.Location = new System.Drawing.Point(184, 424);
            this.bt_plc_generate_sn.Name = "bt_plc_generate_sn";
            this.bt_plc_generate_sn.Size = new System.Drawing.Size(54, 30);
            this.bt_plc_generate_sn.TabIndex = 187;
            this.bt_plc_generate_sn.Text = "產生";
            this.bt_plc_generate_sn.UseVisualStyleBackColor = true;
            this.bt_plc_generate_sn.Click += new System.EventHandler(this.bt_plc_generate_sn_Click);
            // 
            // lb_sn
            // 
            this.lb_sn.AutoSize = true;
            this.lb_sn.Font = new System.Drawing.Font("Consolas", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn.Location = new System.Drawing.Point(113, 324);
            this.lb_sn.Name = "lb_sn";
            this.lb_sn.Size = new System.Drawing.Size(106, 24);
            this.lb_sn.TabIndex = 185;
            this.lb_sn.Text = "相機序號";
            // 
            // tb_sn1
            // 
            this.tb_sn1.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_sn1.Location = new System.Drawing.Point(113, 354);
            this.tb_sn1.Multiline = true;
            this.tb_sn1.Name = "tb_sn1";
            this.tb_sn1.Size = new System.Drawing.Size(160, 35);
            this.tb_sn1.TabIndex = 184;
            this.tb_sn1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_sn2
            // 
            this.tb_sn2.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_sn2.Location = new System.Drawing.Point(113, 381);
            this.tb_sn2.Multiline = true;
            this.tb_sn2.Name = "tb_sn2";
            this.tb_sn2.Size = new System.Drawing.Size(160, 35);
            this.tb_sn2.TabIndex = 186;
            this.tb_sn2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // bt_plc_8
            // 
            this.bt_plc_8.Location = new System.Drawing.Point(129, 78);
            this.bt_plc_8.Name = "bt_plc_8";
            this.bt_plc_8.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_8.TabIndex = 144;
            this.bt_plc_8.Text = "命令ims影像存檔";
            this.bt_plc_8.UseVisualStyleBackColor = true;
            this.bt_plc_8.Click += new System.EventHandler(this.bt_plc_8_Click);
            // 
            // bt_plc_9
            // 
            this.bt_plc_9.Location = new System.Drawing.Point(129, 124);
            this.bt_plc_9.Name = "bt_plc_9";
            this.bt_plc_9.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_9.TabIndex = 143;
            this.bt_plc_9.Text = "寫入相機序號";
            this.bt_plc_9.UseVisualStyleBackColor = true;
            this.bt_plc_9.Click += new System.EventHandler(this.bt_plc_9_Click);
            // 
            // lb_main_mesg1b
            // 
            this.lb_main_mesg1b.AutoSize = true;
            this.lb_main_mesg1b.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1b.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1b.Location = new System.Drawing.Point(141, 37);
            this.lb_main_mesg1b.Name = "lb_main_mesg1b";
            this.lb_main_mesg1b.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1b.TabIndex = 142;
            this.lb_main_mesg1b.Text = "mesg1";
            // 
            // bt_plc_7
            // 
            this.bt_plc_7.Location = new System.Drawing.Point(14, 400);
            this.bt_plc_7.Name = "bt_plc_7";
            this.bt_plc_7.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_7.TabIndex = 141;
            this.bt_plc_7.Text = "錯誤命令";
            this.bt_plc_7.UseVisualStyleBackColor = true;
            this.bt_plc_7.Click += new System.EventHandler(this.bt_plc_7_Click);
            // 
            // bt_plc_6
            // 
            this.bt_plc_6.Location = new System.Drawing.Point(14, 354);
            this.bt_plc_6.Name = "bt_plc_6";
            this.bt_plc_6.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_6.TabIndex = 140;
            this.bt_plc_6.Text = "LED";
            this.bt_plc_6.UseVisualStyleBackColor = true;
            this.bt_plc_6.Click += new System.EventHandler(this.bt_plc_6_Click);
            // 
            // bt_plc_0
            // 
            this.bt_plc_0.Location = new System.Drawing.Point(14, 78);
            this.bt_plc_0.Name = "bt_plc_0";
            this.bt_plc_0.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_0.TabIndex = 139;
            this.bt_plc_0.Text = "讀取連線狀態";
            this.bt_plc_0.UseVisualStyleBackColor = true;
            this.bt_plc_0.Click += new System.EventHandler(this.bt_plc_0_Click);
            // 
            // bt_plc_5
            // 
            this.bt_plc_5.Location = new System.Drawing.Point(14, 308);
            this.bt_plc_5.Name = "bt_plc_5";
            this.bt_plc_5.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_5.TabIndex = 138;
            this.bt_plc_5.Text = "START";
            this.bt_plc_5.UseVisualStyleBackColor = true;
            this.bt_plc_5.Click += new System.EventHandler(this.bt_plc_5_Click);
            // 
            // bt_plc_4
            // 
            this.bt_plc_4.Location = new System.Drawing.Point(14, 262);
            this.bt_plc_4.Name = "bt_plc_4";
            this.bt_plc_4.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_4.TabIndex = 137;
            this.bt_plc_4.Text = "發送命令給PC";
            this.bt_plc_4.UseVisualStyleBackColor = true;
            this.bt_plc_4.Click += new System.EventHandler(this.bt_plc_4_Click);
            // 
            // bt_plc_3
            // 
            this.bt_plc_3.Location = new System.Drawing.Point(14, 216);
            this.bt_plc_3.Name = "bt_plc_3";
            this.bt_plc_3.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_3.TabIndex = 136;
            this.bt_plc_3.Text = "讀取色彩校正結果";
            this.bt_plc_3.UseVisualStyleBackColor = true;
            this.bt_plc_3.Click += new System.EventHandler(this.bt_plc_3_Click);
            // 
            // bt_plc_2
            // 
            this.bt_plc_2.Location = new System.Drawing.Point(14, 170);
            this.bt_plc_2.Name = "bt_plc_2";
            this.bt_plc_2.Size = new System.Drawing.Size(90, 40);
            this.bt_plc_2.TabIndex = 135;
            this.bt_plc_2.Text = "啟動色彩校正";
            this.bt_plc_2.UseVisualStyleBackColor = true;
            this.bt_plc_2.Click += new System.EventHandler(this.bt_plc_2_Click);
            // 
            // lb_main_mesg1a
            // 
            this.lb_main_mesg1a.AutoSize = true;
            this.lb_main_mesg1a.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1a.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1a.Location = new System.Drawing.Point(10, 37);
            this.lb_main_mesg1a.Name = "lb_main_mesg1a";
            this.lb_main_mesg1a.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1a.TabIndex = 134;
            this.lb_main_mesg1a.Text = "mesg1";
            // 
            // groupBox_pc
            // 
            this.groupBox_pc.Controls.Add(this.lb_sn_pc3);
            this.groupBox_pc.Controls.Add(this.lb_main_mesg2b);
            this.groupBox_pc.Controls.Add(this.bt_pc_8);
            this.groupBox_pc.Controls.Add(this.lb_sn_pc2);
            this.groupBox_pc.Controls.Add(this.bt_pc_7);
            this.groupBox_pc.Controls.Add(this.bt_pc_6);
            this.groupBox_pc.Controls.Add(this.lb_sn_pc1);
            this.groupBox_pc.Controls.Add(this.bt_pc_0);
            this.groupBox_pc.Controls.Add(this.bt_pc_5);
            this.groupBox_pc.Controls.Add(this.lb_main_mesg2a);
            this.groupBox_pc.Controls.Add(this.bt_pc_4);
            this.groupBox_pc.Controls.Add(this.bt_pc_1);
            this.groupBox_pc.Controls.Add(this.bt_pc_3);
            this.groupBox_pc.Controls.Add(this.bt_pc_2);
            this.groupBox_pc.Location = new System.Drawing.Point(291, 216);
            this.groupBox_pc.Name = "groupBox_pc";
            this.groupBox_pc.Size = new System.Drawing.Size(231, 458);
            this.groupBox_pc.TabIndex = 191;
            this.groupBox_pc.TabStop = false;
            this.groupBox_pc.Text = "PC控制台";
            // 
            // lb_main_mesg2b
            // 
            this.lb_main_mesg2b.AutoSize = true;
            this.lb_main_mesg2b.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2b.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2b.Location = new System.Drawing.Point(131, 35);
            this.lb_main_mesg2b.Name = "lb_main_mesg2b";
            this.lb_main_mesg2b.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg2b.TabIndex = 148;
            this.lb_main_mesg2b.Text = "mesg1";
            // 
            // bt_pc_8
            // 
            this.bt_pc_8.Location = new System.Drawing.Point(107, 76);
            this.bt_pc_8.Name = "bt_pc_8";
            this.bt_pc_8.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_8.TabIndex = 147;
            this.bt_pc_8.Text = "發送命令給IMS";
            this.bt_pc_8.UseVisualStyleBackColor = true;
            this.bt_pc_8.Click += new System.EventHandler(this.bt_pc_8_Click);
            // 
            // bt_pc_7
            // 
            this.bt_pc_7.Location = new System.Drawing.Point(11, 398);
            this.bt_pc_7.Name = "bt_pc_7";
            this.bt_pc_7.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_7.TabIndex = 146;
            this.bt_pc_7.UseVisualStyleBackColor = true;
            this.bt_pc_7.Click += new System.EventHandler(this.bt_pc_7_Click);
            // 
            // bt_pc_6
            // 
            this.bt_pc_6.Location = new System.Drawing.Point(11, 352);
            this.bt_pc_6.Name = "bt_pc_6";
            this.bt_pc_6.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_6.TabIndex = 145;
            this.bt_pc_6.UseVisualStyleBackColor = true;
            this.bt_pc_6.Click += new System.EventHandler(this.bt_pc_6_Click);
            // 
            // bt_pc_0
            // 
            this.bt_pc_0.Location = new System.Drawing.Point(11, 76);
            this.bt_pc_0.Name = "bt_pc_0";
            this.bt_pc_0.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_0.TabIndex = 144;
            this.bt_pc_0.Text = "發送系統連線狀態給PLC";
            this.bt_pc_0.UseVisualStyleBackColor = true;
            this.bt_pc_0.Click += new System.EventHandler(this.bt_pc_0_Click);
            // 
            // bt_pc_5
            // 
            this.bt_pc_5.Location = new System.Drawing.Point(11, 306);
            this.bt_pc_5.Name = "bt_pc_5";
            this.bt_pc_5.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_5.TabIndex = 143;
            this.bt_pc_5.UseVisualStyleBackColor = true;
            this.bt_pc_5.Click += new System.EventHandler(this.bt_pc_5_Click);
            // 
            // lb_main_mesg2a
            // 
            this.lb_main_mesg2a.AutoSize = true;
            this.lb_main_mesg2a.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2a.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2a.Location = new System.Drawing.Point(23, 35);
            this.lb_main_mesg2a.Name = "lb_main_mesg2a";
            this.lb_main_mesg2a.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg2a.TabIndex = 135;
            this.lb_main_mesg2a.Text = "mesg1";
            // 
            // bt_pc_4
            // 
            this.bt_pc_4.Location = new System.Drawing.Point(11, 260);
            this.bt_pc_4.Name = "bt_pc_4";
            this.bt_pc_4.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_4.TabIndex = 142;
            this.bt_pc_4.UseVisualStyleBackColor = true;
            this.bt_pc_4.Click += new System.EventHandler(this.bt_pc_4_Click);
            // 
            // bt_pc_1
            // 
            this.bt_pc_1.Location = new System.Drawing.Point(11, 122);
            this.bt_pc_1.Name = "bt_pc_1";
            this.bt_pc_1.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_1.TabIndex = 139;
            this.bt_pc_1.Text = "發送命令給PLC";
            this.bt_pc_1.UseVisualStyleBackColor = true;
            this.bt_pc_1.Click += new System.EventHandler(this.bt_pc_1_Click);
            // 
            // bt_pc_3
            // 
            this.bt_pc_3.Location = new System.Drawing.Point(11, 214);
            this.bt_pc_3.Name = "bt_pc_3";
            this.bt_pc_3.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_3.TabIndex = 141;
            this.bt_pc_3.UseVisualStyleBackColor = true;
            this.bt_pc_3.Click += new System.EventHandler(this.bt_pc_3_Click);
            // 
            // bt_pc_2
            // 
            this.bt_pc_2.Location = new System.Drawing.Point(11, 168);
            this.bt_pc_2.Name = "bt_pc_2";
            this.bt_pc_2.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_2.TabIndex = 140;
            this.bt_pc_2.Text = "回傳色彩校正結果";
            this.bt_pc_2.UseVisualStyleBackColor = true;
            this.bt_pc_2.Click += new System.EventHandler(this.bt_pc_2_Click);
            // 
            // groupBox_ims
            // 
            this.groupBox_ims.Controls.Add(this.lb_main_mesg3b);
            this.groupBox_ims.Controls.Add(this.bt_ims_0);
            this.groupBox_ims.Controls.Add(this.bt_ims_5);
            this.groupBox_ims.Controls.Add(this.lb_main_mesg3a);
            this.groupBox_ims.Controls.Add(this.bt_ims_4);
            this.groupBox_ims.Controls.Add(this.bt_ims_1);
            this.groupBox_ims.Controls.Add(this.bt_ims_3);
            this.groupBox_ims.Controls.Add(this.bt_ims_2);
            this.groupBox_ims.Location = new System.Drawing.Point(539, 216);
            this.groupBox_ims.Name = "groupBox_ims";
            this.groupBox_ims.Size = new System.Drawing.Size(231, 458);
            this.groupBox_ims.TabIndex = 192;
            this.groupBox_ims.TabStop = false;
            this.groupBox_ims.Text = "IMS控制台";
            // 
            // lb_main_mesg3b
            // 
            this.lb_main_mesg3b.AutoSize = true;
            this.lb_main_mesg3b.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg3b.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg3b.Location = new System.Drawing.Point(126, 35);
            this.lb_main_mesg3b.Name = "lb_main_mesg3b";
            this.lb_main_mesg3b.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg3b.TabIndex = 150;
            this.lb_main_mesg3b.Text = "mesg1";
            // 
            // bt_ims_0
            // 
            this.bt_ims_0.Location = new System.Drawing.Point(13, 76);
            this.bt_ims_0.Name = "bt_ims_0";
            this.bt_ims_0.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_0.TabIndex = 149;
            this.bt_ims_0.Text = "發送命令給PC";
            this.bt_ims_0.UseVisualStyleBackColor = true;
            this.bt_ims_0.Click += new System.EventHandler(this.bt_ims_0_Click);
            // 
            // bt_ims_5
            // 
            this.bt_ims_5.Location = new System.Drawing.Point(13, 306);
            this.bt_ims_5.Name = "bt_ims_5";
            this.bt_ims_5.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_5.TabIndex = 148;
            this.bt_ims_5.UseVisualStyleBackColor = true;
            this.bt_ims_5.Click += new System.EventHandler(this.bt_ims_5_Click);
            // 
            // lb_main_mesg3a
            // 
            this.lb_main_mesg3a.AutoSize = true;
            this.lb_main_mesg3a.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg3a.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg3a.Location = new System.Drawing.Point(25, 35);
            this.lb_main_mesg3a.Name = "lb_main_mesg3a";
            this.lb_main_mesg3a.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg3a.TabIndex = 136;
            this.lb_main_mesg3a.Text = "mesg1";
            // 
            // bt_ims_4
            // 
            this.bt_ims_4.Location = new System.Drawing.Point(13, 260);
            this.bt_ims_4.Name = "bt_ims_4";
            this.bt_ims_4.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_4.TabIndex = 147;
            this.bt_ims_4.UseVisualStyleBackColor = true;
            this.bt_ims_4.Click += new System.EventHandler(this.bt_ims_4_Click);
            // 
            // bt_ims_1
            // 
            this.bt_ims_1.Location = new System.Drawing.Point(13, 122);
            this.bt_ims_1.Name = "bt_ims_1";
            this.bt_ims_1.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_1.TabIndex = 144;
            this.bt_ims_1.UseVisualStyleBackColor = true;
            this.bt_ims_1.Click += new System.EventHandler(this.bt_ims_1_Click);
            // 
            // bt_ims_3
            // 
            this.bt_ims_3.Location = new System.Drawing.Point(13, 214);
            this.bt_ims_3.Name = "bt_ims_3";
            this.bt_ims_3.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_3.TabIndex = 146;
            this.bt_ims_3.UseVisualStyleBackColor = true;
            this.bt_ims_3.Click += new System.EventHandler(this.bt_ims_3_Click);
            // 
            // bt_ims_2
            // 
            this.bt_ims_2.Location = new System.Drawing.Point(13, 168);
            this.bt_ims_2.Name = "bt_ims_2";
            this.bt_ims_2.Size = new System.Drawing.Size(90, 40);
            this.bt_ims_2.TabIndex = 145;
            this.bt_ims_2.UseVisualStyleBackColor = true;
            this.bt_ims_2.Click += new System.EventHandler(this.bt_ims_2_Click);
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // lb_main_mesg0
            // 
            this.lb_main_mesg0.AutoSize = true;
            this.lb_main_mesg0.Font = new System.Drawing.Font("Arial", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg0.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg0.Location = new System.Drawing.Point(470, 41);
            this.lb_main_mesg0.Name = "lb_main_mesg0";
            this.lb_main_mesg0.Size = new System.Drawing.Size(103, 32);
            this.lb_main_mesg0.TabIndex = 135;
            this.lb_main_mesg0.Text = "mesg1";
            // 
            // lb_sn_pc3
            // 
            this.lb_sn_pc3.AutoSize = true;
            this.lb_sn_pc3.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn_pc3.Location = new System.Drawing.Point(117, 281);
            this.lb_sn_pc3.Name = "lb_sn_pc3";
            this.lb_sn_pc3.Size = new System.Drawing.Size(60, 22);
            this.lb_sn_pc3.TabIndex = 193;
            this.lb_sn_pc3.Text = "S/N :";
            // 
            // lb_sn_pc2
            // 
            this.lb_sn_pc2.AutoSize = true;
            this.lb_sn_pc2.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn_pc2.Location = new System.Drawing.Point(117, 244);
            this.lb_sn_pc2.Name = "lb_sn_pc2";
            this.lb_sn_pc2.Size = new System.Drawing.Size(60, 22);
            this.lb_sn_pc2.TabIndex = 192;
            this.lb_sn_pc2.Text = "S/N :";
            // 
            // lb_sn_pc1
            // 
            this.lb_sn_pc1.AutoSize = true;
            this.lb_sn_pc1.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_sn_pc1.Location = new System.Drawing.Point(117, 206);
            this.lb_sn_pc1.Name = "lb_sn_pc1";
            this.lb_sn_pc1.Size = new System.Drawing.Size(60, 22);
            this.lb_sn_pc1.TabIndex = 191;
            this.lb_sn_pc1.Text = "S/N :";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1119, 686);
            this.Controls.Add(this.lb_main_mesg0);
            this.Controls.Add(this.groupBox_ims);
            this.Controls.Add(this.groupBox_pc);
            this.Controls.Add(this.groupBox_plc);
            this.Controls.Add(this.groupBox_comport2);
            this.Controls.Add(this.groupBox_comport1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "imsLink";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_comport1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport1)).EndInit();
            this.groupBox_comport2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport2)).EndInit();
            this.groupBox_plc.ResumeLayout(false);
            this.groupBox_plc.PerformLayout();
            this.groupBox_pc.ResumeLayout(false);
            this.groupBox_pc.PerformLayout();
            this.groupBox_ims.ResumeLayout(false);
            this.groupBox_ims.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer SerialPortTimer100ms1;
        private System.Windows.Forms.GroupBox groupBox_comport1;
        private System.Windows.Forms.ComboBox comboBox_comport1;
        private System.Windows.Forms.PictureBox pictureBox_comport1;
        private System.Windows.Forms.ComboBox comboBox_baud_rate1;
        private System.Windows.Forms.Button bt_comport_scan1;
        private System.Windows.Forms.Button bt_comport_connect1;
        private System.Windows.Forms.Button bt_comport_disconnect1;
        private System.IO.Ports.SerialPort serialPort2;
        private System.Windows.Forms.Timer SerialPortTimer100ms2;
        private System.Windows.Forms.Button bt_plc_1;
        private System.Windows.Forms.GroupBox groupBox_comport2;
        private System.Windows.Forms.ComboBox comboBox_comport2;
        private System.Windows.Forms.PictureBox pictureBox_comport2;
        private System.Windows.Forms.ComboBox comboBox_baud_rate2;
        private System.Windows.Forms.Button bt_comport_scan2;
        private System.Windows.Forms.Button bt_comport_connect2;
        private System.Windows.Forms.Button bt_comport_disconnect2;
        private System.Windows.Forms.GroupBox groupBox_plc;
        private System.Windows.Forms.GroupBox groupBox_pc;
        private System.Windows.Forms.GroupBox groupBox_ims;
        private System.Windows.Forms.Label lb_main_mesg1a;
        private System.Windows.Forms.Label lb_main_mesg2a;
        private System.Windows.Forms.Label lb_main_mesg3a;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Label lb_main_mesg0;
        private System.Windows.Forms.Button bt_plc_5;
        private System.Windows.Forms.Button bt_plc_4;
        private System.Windows.Forms.Button bt_plc_3;
        private System.Windows.Forms.Button bt_plc_2;
        private System.Windows.Forms.Button bt_pc_5;
        private System.Windows.Forms.Button bt_pc_4;
        private System.Windows.Forms.Button bt_pc_1;
        private System.Windows.Forms.Button bt_pc_3;
        private System.Windows.Forms.Button bt_pc_2;
        private System.Windows.Forms.Button bt_ims_5;
        private System.Windows.Forms.Button bt_ims_4;
        private System.Windows.Forms.Button bt_ims_1;
        private System.Windows.Forms.Button bt_ims_3;
        private System.Windows.Forms.Button bt_ims_2;
        private System.Windows.Forms.Button bt_plc_0;
        private System.Windows.Forms.Button bt_pc_0;
        private System.Windows.Forms.Button bt_ims_0;
        private System.Windows.Forms.Button bt_plc_6;
        private System.Windows.Forms.Button bt_plc_7;
        private System.Windows.Forms.Button bt_pc_8;
        private System.Windows.Forms.Button bt_pc_7;
        private System.Windows.Forms.Button bt_pc_6;
        private System.Windows.Forms.Label lb_main_mesg1b;
        private System.Windows.Forms.Label lb_main_mesg2b;
        private System.Windows.Forms.Label lb_main_mesg3b;
        private System.Windows.Forms.Button bt_plc_8;
        private System.Windows.Forms.Button bt_plc_9;
        private System.Windows.Forms.Button bt_plc_generate_sn;
        private System.Windows.Forms.Label lb_sn;
        private System.Windows.Forms.TextBox tb_sn1;
        private System.Windows.Forms.TextBox tb_sn2;
        private System.Windows.Forms.Label lb_sn3;
        private System.Windows.Forms.Label lb_sn2;
        private System.Windows.Forms.Label lb_sn1;
        private System.Windows.Forms.Label lb_sn_pc3;
        private System.Windows.Forms.Label lb_sn_pc2;
        private System.Windows.Forms.Label lb_sn_pc1;
    }
}

