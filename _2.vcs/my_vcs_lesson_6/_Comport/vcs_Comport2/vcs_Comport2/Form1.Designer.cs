namespace vcs_Comport2
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
            this.button5 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.button6 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.groupBox20 = new System.Windows.Forms.GroupBox();
            this.bt_temperature_off = new System.Windows.Forms.Button();
            this.lb_temperature = new System.Windows.Forms.Label();
            this.bt_temperature_on = new System.Windows.Forms.Button();
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.groupBox_comport = new System.Windows.Forms.GroupBox();
            this.comboBox_comport = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport = new System.Windows.Forms.PictureBox();
            this.comboBox_baud_rate = new System.Windows.Forms.ComboBox();
            this.bt_comport_scan = new System.Windows.Forms.Button();
            this.bt_comport_connect = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.groupBox20.SuspendLayout();
            this.groupBox_comport.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).BeginInit();
            this.SuspendLayout();
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(12, 325);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(75, 23);
            this.button5.TabIndex = 11;
            this.button5.Text = "receive";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 159);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 10;
            this.button4.Text = "send";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(793, 60);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(255, 483);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            this.richTextBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.richTextBox1_KeyPress);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 114);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 8;
            this.button3.Text = "send";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // serialPort1
            // 
            this.serialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(12, 354);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(75, 53);
            this.button6.TabIndex = 12;
            this.button6.Text = "丟棄UART buffer內的資料";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
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
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(12, 201);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(75, 23);
            this.button8.TabIndex = 15;
            this.button8.Text = "send dir";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(12, 245);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(75, 23);
            this.button9.TabIndex = 16;
            this.button9.Text = "send textbox";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(12, 285);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(173, 22);
            this.textBox1.TabIndex = 17;
            this.textBox1.Text = "This is an ims test message.";
            // 
            // groupBox20
            // 
            this.groupBox20.Controls.Add(this.bt_temperature_off);
            this.groupBox20.Controls.Add(this.lb_temperature);
            this.groupBox20.Controls.Add(this.bt_temperature_on);
            this.groupBox20.Location = new System.Drawing.Point(12, 625);
            this.groupBox20.Name = "groupBox20";
            this.groupBox20.Size = new System.Drawing.Size(172, 136);
            this.groupBox20.TabIndex = 187;
            this.groupBox20.TabStop = false;
            // 
            // bt_temperature_off
            // 
            this.bt_temperature_off.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_off.Font = new System.Drawing.Font("Consolas", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_off.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_off.Location = new System.Drawing.Point(33, 95);
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
            this.lb_temperature.Location = new System.Drawing.Point(11, 16);
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
            this.bt_temperature_on.Location = new System.Drawing.Point(33, 60);
            this.bt_temperature_on.Name = "bt_temperature_on";
            this.bt_temperature_on.Size = new System.Drawing.Size(118, 32);
            this.bt_temperature_on.TabIndex = 183;
            this.bt_temperature_on.Text = "溫度偵測 ON";
            this.bt_temperature_on.UseVisualStyleBackColor = false;
            this.bt_temperature_on.Click += new System.EventHandler(this.bt_temperature_on_Click);
            // 
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // groupBox_comport
            // 
            this.groupBox_comport.Controls.Add(this.comboBox_comport);
            this.groupBox_comport.Controls.Add(this.pictureBox_comport);
            this.groupBox_comport.Controls.Add(this.comboBox_baud_rate);
            this.groupBox_comport.Controls.Add(this.bt_comport_scan);
            this.groupBox_comport.Controls.Add(this.bt_comport_connect);
            this.groupBox_comport.Controls.Add(this.bt_comport_disconnect);
            this.groupBox_comport.Location = new System.Drawing.Point(13, 9);
            this.groupBox_comport.Name = "groupBox_comport";
            this.groupBox_comport.Size = new System.Drawing.Size(443, 70);
            this.groupBox_comport.TabIndex = 188;
            this.groupBox_comport.TabStop = false;
            // 
            // comboBox_comport
            // 
            this.comboBox_comport.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_comport.FormattingEnabled = true;
            this.comboBox_comport.Location = new System.Drawing.Point(8, 18);
            this.comboBox_comport.Name = "comboBox_comport";
            this.comboBox_comport.Size = new System.Drawing.Size(80, 27);
            this.comboBox_comport.TabIndex = 19;
            // 
            // pictureBox_comport
            // 
            this.pictureBox_comport.Location = new System.Drawing.Point(344, 8);
            this.pictureBox_comport.Name = "pictureBox_comport";
            this.pictureBox_comport.Size = new System.Drawing.Size(48, 48);
            this.pictureBox_comport.TabIndex = 22;
            this.pictureBox_comport.TabStop = false;
            // 
            // comboBox_baud_rate
            // 
            this.comboBox_baud_rate.Enabled = false;
            this.comboBox_baud_rate.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_baud_rate.FormattingEnabled = true;
            this.comboBox_baud_rate.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox_baud_rate.Location = new System.Drawing.Point(92, 18);
            this.comboBox_baud_rate.Name = "comboBox_baud_rate";
            this.comboBox_baud_rate.Size = new System.Drawing.Size(76, 27);
            this.comboBox_baud_rate.TabIndex = 20;
            this.comboBox_baud_rate.Text = "115200";
            // 
            // bt_comport_scan
            // 
            this.bt_comport_scan.Location = new System.Drawing.Point(170, 15);
            this.bt_comport_scan.Name = "bt_comport_scan";
            this.bt_comport_scan.Size = new System.Drawing.Size(49, 33);
            this.bt_comport_scan.TabIndex = 21;
            this.bt_comport_scan.Text = "Scan";
            this.bt_comport_scan.UseVisualStyleBackColor = true;
            this.bt_comport_scan.Click += new System.EventHandler(this.bt_comport_scan_Click);
            // 
            // bt_comport_connect
            // 
            this.bt_comport_connect.Location = new System.Drawing.Point(220, 15);
            this.bt_comport_connect.Name = "bt_comport_connect";
            this.bt_comport_connect.Size = new System.Drawing.Size(58, 33);
            this.bt_comport_connect.TabIndex = 0;
            this.bt_comport_connect.Text = "Connect";
            this.bt_comport_connect.UseVisualStyleBackColor = true;
            this.bt_comport_connect.Click += new System.EventHandler(this.bt_comport_connect_Click);
            // 
            // bt_comport_disconnect
            // 
            this.bt_comport_disconnect.Location = new System.Drawing.Point(278, 15);
            this.bt_comport_disconnect.Name = "bt_comport_disconnect";
            this.bt_comport_disconnect.Size = new System.Drawing.Size(64, 33);
            this.bt_comport_disconnect.TabIndex = 1;
            this.bt_comport_disconnect.Text = "Disconnect";
            this.bt_comport_disconnect.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect.Click += new System.EventHandler(this.bt_comport_disconnect_Click);
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Location = new System.Drawing.Point(774, 24);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(77, 16);
            this.checkBox1.TabIndex = 189;
            this.checkBox1.Text = "putty mode";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(625, 130);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 190;
            this.button1.Text = "write 1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(625, 174);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 191;
            this.button2.Text = "write 2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(625, 220);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(75, 23);
            this.button7.TabIndex = 192;
            this.button7.Text = "write 3";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(12, 445);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(75, 23);
            this.button10.TabIndex = 193;
            this.button10.Text = "info";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(13, 501);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(75, 23);
            this.button11.TabIndex = 194;
            this.button11.Text = "send ^";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1058, 773);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.groupBox_comport);
            this.Controls.Add(this.groupBox20);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button3);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox20.ResumeLayout(false);
            this.groupBox20.PerformLayout();
            this.groupBox_comport.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button3;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.GroupBox groupBox20;
        private System.Windows.Forms.Button bt_temperature_off;
        private System.Windows.Forms.Label lb_temperature;
        private System.Windows.Forms.Button bt_temperature_on;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.GroupBox groupBox_comport;
        private System.Windows.Forms.ComboBox comboBox_comport;
        private System.Windows.Forms.PictureBox pictureBox_comport;
        private System.Windows.Forms.ComboBox comboBox_baud_rate;
        private System.Windows.Forms.Button bt_comport_scan;
        private System.Windows.Forms.Button bt_comport_connect;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
    }
}

