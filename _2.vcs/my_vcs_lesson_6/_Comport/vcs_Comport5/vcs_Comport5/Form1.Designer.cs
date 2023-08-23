namespace vcs_Comport5
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
            this.lb_main_mesg0 = new System.Windows.Forms.Label();
            this.groupBox_comport2 = new System.Windows.Forms.GroupBox();
            this.comboBox_comport2 = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport2 = new System.Windows.Forms.PictureBox();
            this.comboBox_baud_rate2 = new System.Windows.Forms.ComboBox();
            this.bt_comport_scan2 = new System.Windows.Forms.Button();
            this.bt_comport_connect2 = new System.Windows.Forms.Button();
            this.bt_comport_disconnect2 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox_pc = new System.Windows.Forms.GroupBox();
            this.groupBox_ae = new System.Windows.Forms.GroupBox();
            this.bt_ae_on = new System.Windows.Forms.Button();
            this.bt_ae_off = new System.Windows.Forms.Button();
            this.groupBox_led = new System.Windows.Forms.GroupBox();
            this.bt_led_off = new System.Windows.Forms.Button();
            this.bt_pc_8 = new System.Windows.Forms.Button();
            this.lb_main_mesg2b = new System.Windows.Forms.Label();
            this.bt_pc_7 = new System.Windows.Forms.Button();
            this.bt_pc_6 = new System.Windows.Forms.Button();
            this.bt_pc_0 = new System.Windows.Forms.Button();
            this.bt_pc_5 = new System.Windows.Forms.Button();
            this.lb_main_mesg2a = new System.Windows.Forms.Label();
            this.bt_pc_4 = new System.Windows.Forms.Button();
            this.bt_pc_1 = new System.Windows.Forms.Button();
            this.bt_pc_3 = new System.Windows.Forms.Button();
            this.bt_pc_2 = new System.Windows.Forms.Button();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.SerialPortTimer100ms2 = new System.Windows.Forms.Timer(this.components);
            this.serialPort2 = new System.IO.Ports.SerialPort(this.components);
            this.groupBox_comport2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport2)).BeginInit();
            this.groupBox_pc.SuspendLayout();
            this.groupBox_ae.SuspendLayout();
            this.groupBox_led.SuspendLayout();
            this.SuspendLayout();
            // 
            // lb_main_mesg0
            // 
            this.lb_main_mesg0.AutoSize = true;
            this.lb_main_mesg0.Font = new System.Drawing.Font("Arial", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg0.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg0.Location = new System.Drawing.Point(439, 9);
            this.lb_main_mesg0.Name = "lb_main_mesg0";
            this.lb_main_mesg0.Size = new System.Drawing.Size(103, 32);
            this.lb_main_mesg0.TabIndex = 190;
            this.lb_main_mesg0.Text = "mesg1";
            // 
            // groupBox_comport2
            // 
            this.groupBox_comport2.Controls.Add(this.comboBox_comport2);
            this.groupBox_comport2.Controls.Add(this.pictureBox_comport2);
            this.groupBox_comport2.Controls.Add(this.comboBox_baud_rate2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_scan2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_connect2);
            this.groupBox_comport2.Controls.Add(this.bt_comport_disconnect2);
            this.groupBox_comport2.Location = new System.Drawing.Point(12, 31);
            this.groupBox_comport2.Name = "groupBox_comport2";
            this.groupBox_comport2.Size = new System.Drawing.Size(421, 81);
            this.groupBox_comport2.TabIndex = 191;
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
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(482, 94);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 30);
            this.bt_clear.TabIndex = 195;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(464, 60);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 194;
            this.richTextBox1.Text = "";
            // 
            // panel1
            // 
            this.panel1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("panel1.BackgroundImage")));
            this.panel1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.panel1.Location = new System.Drawing.Point(649, 31);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(260, 77);
            this.panel1.TabIndex = 196;
            // 
            // groupBox_pc
            // 
            this.groupBox_pc.Controls.Add(this.groupBox_ae);
            this.groupBox_pc.Controls.Add(this.groupBox_led);
            this.groupBox_pc.Controls.Add(this.bt_pc_8);
            this.groupBox_pc.Controls.Add(this.lb_main_mesg2b);
            this.groupBox_pc.Controls.Add(this.bt_pc_7);
            this.groupBox_pc.Controls.Add(this.bt_pc_6);
            this.groupBox_pc.Controls.Add(this.bt_pc_0);
            this.groupBox_pc.Controls.Add(this.bt_pc_5);
            this.groupBox_pc.Controls.Add(this.lb_main_mesg2a);
            this.groupBox_pc.Controls.Add(this.bt_pc_4);
            this.groupBox_pc.Controls.Add(this.bt_pc_1);
            this.groupBox_pc.Controls.Add(this.bt_pc_3);
            this.groupBox_pc.Controls.Add(this.bt_pc_2);
            this.groupBox_pc.Location = new System.Drawing.Point(202, 136);
            this.groupBox_pc.Name = "groupBox_pc";
            this.groupBox_pc.Size = new System.Drawing.Size(538, 458);
            this.groupBox_pc.TabIndex = 197;
            this.groupBox_pc.TabStop = false;
            this.groupBox_pc.Text = "PC控制台";
            // 
            // groupBox_ae
            // 
            this.groupBox_ae.Controls.Add(this.bt_ae_on);
            this.groupBox_ae.Controls.Add(this.bt_ae_off);
            this.groupBox_ae.Location = new System.Drawing.Point(121, 270);
            this.groupBox_ae.Name = "groupBox_ae";
            this.groupBox_ae.Size = new System.Drawing.Size(146, 113);
            this.groupBox_ae.TabIndex = 200;
            this.groupBox_ae.TabStop = false;
            this.groupBox_ae.Text = "自動曝光開關";
            // 
            // bt_ae_on
            // 
            this.bt_ae_on.BackColor = System.Drawing.Color.Black;
            this.bt_ae_on.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_ae_on.ForeColor = System.Drawing.Color.Gold;
            this.bt_ae_on.Location = new System.Drawing.Point(72, 36);
            this.bt_ae_on.Name = "bt_ae_on";
            this.bt_ae_on.Size = new System.Drawing.Size(60, 60);
            this.bt_ae_on.TabIndex = 213;
            this.bt_ae_on.Text = "LED";
            this.bt_ae_on.UseVisualStyleBackColor = false;
            this.bt_ae_on.Click += new System.EventHandler(this.bt_ae_on_Click);
            // 
            // bt_ae_off
            // 
            this.bt_ae_off.BackColor = System.Drawing.Color.Black;
            this.bt_ae_off.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_ae_off.ForeColor = System.Drawing.Color.Gold;
            this.bt_ae_off.Location = new System.Drawing.Point(6, 36);
            this.bt_ae_off.Name = "bt_ae_off";
            this.bt_ae_off.Size = new System.Drawing.Size(60, 60);
            this.bt_ae_off.TabIndex = 212;
            this.bt_ae_off.Text = "LED";
            this.bt_ae_off.UseVisualStyleBackColor = false;
            this.bt_ae_off.Click += new System.EventHandler(this.bt_ae_off_Click);
            // 
            // groupBox_led
            // 
            this.groupBox_led.Controls.Add(this.bt_led_off);
            this.groupBox_led.Location = new System.Drawing.Point(121, 141);
            this.groupBox_led.Name = "groupBox_led";
            this.groupBox_led.Size = new System.Drawing.Size(146, 113);
            this.groupBox_led.TabIndex = 197;
            this.groupBox_led.TabStop = false;
            this.groupBox_led.Text = "LED開關";
            // 
            // bt_led_off
            // 
            this.bt_led_off.BackColor = System.Drawing.Color.Black;
            this.bt_led_off.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_led_off.ForeColor = System.Drawing.Color.Gold;
            this.bt_led_off.Location = new System.Drawing.Point(6, 27);
            this.bt_led_off.Name = "bt_led_off";
            this.bt_led_off.Size = new System.Drawing.Size(60, 60);
            this.bt_led_off.TabIndex = 210;
            this.bt_led_off.Text = "LED";
            this.bt_led_off.UseVisualStyleBackColor = false;
            this.bt_led_off.Click += new System.EventHandler(this.bt_led_off_Click);
            // 
            // bt_pc_8
            // 
            this.bt_pc_8.Location = new System.Drawing.Point(121, 76);
            this.bt_pc_8.Name = "bt_pc_8";
            this.bt_pc_8.Size = new System.Drawing.Size(90, 40);
            this.bt_pc_8.TabIndex = 196;
            this.bt_pc_8.UseVisualStyleBackColor = true;
            this.bt_pc_8.Click += new System.EventHandler(this.bt_pc_8_Click);
            // 
            // lb_main_mesg2b
            // 
            this.lb_main_mesg2b.AutoSize = true;
            this.lb_main_mesg2b.Font = new System.Drawing.Font("Arial", 15F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2b.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2b.Location = new System.Drawing.Point(131, 35);
            this.lb_main_mesg2b.Name = "lb_main_mesg2b";
            this.lb_main_mesg2b.Size = new System.Drawing.Size(72, 24);
            this.lb_main_mesg2b.TabIndex = 148;
            this.lb_main_mesg2b.Text = "mesg1";
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
            this.lb_main_mesg2a.Font = new System.Drawing.Font("Arial", 15F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg2a.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2a.Location = new System.Drawing.Point(23, 35);
            this.lb_main_mesg2a.Name = "lb_main_mesg2a";
            this.lb_main_mesg2a.Size = new System.Drawing.Size(72, 24);
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
            this.bt_pc_2.UseVisualStyleBackColor = true;
            this.bt_pc_2.Click += new System.EventHandler(this.bt_pc_2_Click);
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // SerialPortTimer100ms2
            // 
            this.SerialPortTimer100ms2.Tick += new System.EventHandler(this.SerialPortTimer100ms2_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(954, 634);
            this.Controls.Add(this.groupBox_pc);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.lb_main_mesg0);
            this.Controls.Add(this.groupBox_comport2);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "imsLink";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_comport2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport2)).EndInit();
            this.groupBox_pc.ResumeLayout(false);
            this.groupBox_pc.PerformLayout();
            this.groupBox_ae.ResumeLayout(false);
            this.groupBox_led.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_main_mesg0;
        private System.Windows.Forms.GroupBox groupBox_comport2;
        private System.Windows.Forms.ComboBox comboBox_comport2;
        private System.Windows.Forms.PictureBox pictureBox_comport2;
        private System.Windows.Forms.ComboBox comboBox_baud_rate2;
        private System.Windows.Forms.Button bt_comport_scan2;
        private System.Windows.Forms.Button bt_comport_connect2;
        private System.Windows.Forms.Button bt_comport_disconnect2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.GroupBox groupBox_pc;
        private System.Windows.Forms.Button bt_pc_8;
        private System.Windows.Forms.Label lb_main_mesg2b;
        private System.Windows.Forms.Button bt_pc_7;
        private System.Windows.Forms.Button bt_pc_6;
        private System.Windows.Forms.Button bt_pc_0;
        private System.Windows.Forms.Button bt_pc_5;
        private System.Windows.Forms.Label lb_main_mesg2a;
        private System.Windows.Forms.Button bt_pc_4;
        private System.Windows.Forms.Button bt_pc_1;
        private System.Windows.Forms.Button bt_pc_3;
        private System.Windows.Forms.Button bt_pc_2;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Timer SerialPortTimer100ms2;
        private System.IO.Ports.SerialPort serialPort2;
        private System.Windows.Forms.GroupBox groupBox_ae;
        private System.Windows.Forms.GroupBox groupBox_led;
        private System.Windows.Forms.Button bt_ae_on;
        private System.Windows.Forms.Button bt_ae_off;
        private System.Windows.Forms.Button bt_led_off;
    }
}

