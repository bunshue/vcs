namespace vcs_Comport_Sample_Temperature
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
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.groupBox_comport = new System.Windows.Forms.GroupBox();
            this.bt_demo = new System.Windows.Forms.Button();
            this.comboBox_comport = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport = new System.Windows.Forms.PictureBox();
            this.bt_comport_scan = new System.Windows.Forms.Button();
            this.bt_comport_connect = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.groupBox20 = new System.Windows.Forms.GroupBox();
            this.bt_temperature_off = new System.Windows.Forms.Button();
            this.lb_temperature = new System.Windows.Forms.Label();
            this.bt_temperature_on = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.timer_demo = new System.Windows.Forms.Timer(this.components);
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox_comport.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).BeginInit();
            this.groupBox20.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox_comport
            // 
            this.groupBox_comport.Controls.Add(this.bt_demo);
            this.groupBox_comport.Controls.Add(this.comboBox_comport);
            this.groupBox_comport.Controls.Add(this.pictureBox_comport);
            this.groupBox_comport.Controls.Add(this.bt_comport_scan);
            this.groupBox_comport.Controls.Add(this.bt_comport_connect);
            this.groupBox_comport.Controls.Add(this.bt_comport_disconnect);
            this.groupBox_comport.Location = new System.Drawing.Point(12, 12);
            this.groupBox_comport.Name = "groupBox_comport";
            this.groupBox_comport.Size = new System.Drawing.Size(461, 68);
            this.groupBox_comport.TabIndex = 136;
            this.groupBox_comport.TabStop = false;
            // 
            // bt_demo
            // 
            this.bt_demo.Location = new System.Drawing.Point(409, 17);
            this.bt_demo.Name = "bt_demo";
            this.bt_demo.Size = new System.Drawing.Size(46, 35);
            this.bt_demo.TabIndex = 23;
            this.bt_demo.Text = "Demo";
            this.bt_demo.UseVisualStyleBackColor = true;
            this.bt_demo.Click += new System.EventHandler(this.bt_demo_Click);
            // 
            // comboBox_comport
            // 
            this.comboBox_comport.Font = new System.Drawing.Font("新細明體", 12.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_comport.FormattingEnabled = true;
            this.comboBox_comport.Location = new System.Drawing.Point(8, 20);
            this.comboBox_comport.Name = "comboBox_comport";
            this.comboBox_comport.Size = new System.Drawing.Size(75, 25);
            this.comboBox_comport.TabIndex = 19;
            // 
            // pictureBox_comport
            // 
            this.pictureBox_comport.Location = new System.Drawing.Point(244, 9);
            this.pictureBox_comport.Name = "pictureBox_comport";
            this.pictureBox_comport.Size = new System.Drawing.Size(48, 48);
            this.pictureBox_comport.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_comport.TabIndex = 22;
            this.pictureBox_comport.TabStop = false;
            // 
            // bt_comport_scan
            // 
            this.bt_comport_scan.Location = new System.Drawing.Point(85, 17);
            this.bt_comport_scan.Name = "bt_comport_scan";
            this.bt_comport_scan.Size = new System.Drawing.Size(40, 35);
            this.bt_comport_scan.TabIndex = 21;
            this.bt_comport_scan.Text = "Scan";
            this.bt_comport_scan.UseVisualStyleBackColor = true;
            this.bt_comport_scan.Click += new System.EventHandler(this.bt_comport_scan_Click);
            // 
            // bt_comport_connect
            // 
            this.bt_comport_connect.Location = new System.Drawing.Point(125, 17);
            this.bt_comport_connect.Name = "bt_comport_connect";
            this.bt_comport_connect.Size = new System.Drawing.Size(52, 35);
            this.bt_comport_connect.TabIndex = 0;
            this.bt_comport_connect.Text = "Connect";
            this.bt_comport_connect.UseVisualStyleBackColor = true;
            this.bt_comport_connect.Click += new System.EventHandler(this.bt_comport_connect_Click);
            // 
            // bt_comport_disconnect
            // 
            this.bt_comport_disconnect.Location = new System.Drawing.Point(177, 17);
            this.bt_comport_disconnect.Name = "bt_comport_disconnect";
            this.bt_comport_disconnect.Size = new System.Drawing.Size(64, 35);
            this.bt_comport_disconnect.TabIndex = 1;
            this.bt_comport_disconnect.Text = "Disconnect";
            this.bt_comport_disconnect.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect.Click += new System.EventHandler(this.bt_comport_disconnect_Click);
            // 
            // groupBox20
            // 
            this.groupBox20.Controls.Add(this.bt_temperature_off);
            this.groupBox20.Controls.Add(this.lb_temperature);
            this.groupBox20.Controls.Add(this.bt_temperature_on);
            this.groupBox20.Location = new System.Drawing.Point(640, 6);
            this.groupBox20.Name = "groupBox20";
            this.groupBox20.Size = new System.Drawing.Size(319, 84);
            this.groupBox20.TabIndex = 187;
            this.groupBox20.TabStop = false;
            // 
            // bt_temperature_off
            // 
            this.bt_temperature_off.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_off.Font = new System.Drawing.Font("Consolas", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_off.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_off.Location = new System.Drawing.Point(180, 46);
            this.bt_temperature_off.Name = "bt_temperature_off";
            this.bt_temperature_off.Size = new System.Drawing.Size(118, 32);
            this.bt_temperature_off.TabIndex = 184;
            this.bt_temperature_off.Text = "溫度偵測 OFF";
            this.bt_temperature_off.UseVisualStyleBackColor = false;
            this.bt_temperature_off.Click += new System.EventHandler(this.bt_temperature_off_Click);
            // 
            // lb_temperature
            // 
            this.lb_temperature.AutoSize = true;
            this.lb_temperature.Font = new System.Drawing.Font("Arial", 26.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_temperature.ForeColor = System.Drawing.Color.Red;
            this.lb_temperature.Location = new System.Drawing.Point(15, 17);
            this.lb_temperature.Name = "lb_temperature";
            this.lb_temperature.Size = new System.Drawing.Size(37, 41);
            this.lb_temperature.TabIndex = 185;
            this.lb_temperature.Text = "c";
            // 
            // bt_temperature_on
            // 
            this.bt_temperature_on.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_on.Font = new System.Drawing.Font("Consolas", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_on.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_on.Location = new System.Drawing.Point(180, 13);
            this.bt_temperature_on.Name = "bt_temperature_on";
            this.bt_temperature_on.Size = new System.Drawing.Size(118, 32);
            this.bt_temperature_on.TabIndex = 183;
            this.bt_temperature_on.Text = "溫度偵測 ON";
            this.bt_temperature_on.UseVisualStyleBackColor = false;
            this.bt_temperature_on.Click += new System.EventHandler(this.bt_temperature_on_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 594);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(368, 204);
            this.richTextBox1.TabIndex = 188;
            this.richTextBox1.Text = "";
            // 
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Enabled = true;
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // timer_demo
            // 
            this.timer_demo.Interval = 300;
            this.timer_demo.Tick += new System.EventHandler(this.timer_demo_Tick);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(682, 148);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(604, 477);
            this.pictureBox1.TabIndex = 189;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1348, 810);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox20);
            this.Controls.Add(this.groupBox_comport);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_comport.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).EndInit();
            this.groupBox20.ResumeLayout(false);
            this.groupBox20.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.GroupBox groupBox_comport;
        private System.Windows.Forms.ComboBox comboBox_comport;
        private System.Windows.Forms.PictureBox pictureBox_comport;
        private System.Windows.Forms.Button bt_comport_scan;
        private System.Windows.Forms.Button bt_comport_connect;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.GroupBox groupBox20;
        private System.Windows.Forms.Button bt_temperature_off;
        private System.Windows.Forms.Label lb_temperature;
        private System.Windows.Forms.Button bt_temperature_on;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Button bt_demo;
        private System.Windows.Forms.Timer timer_demo;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

