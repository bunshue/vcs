namespace vcs_Comport
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
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox_comport = new System.Windows.Forms.GroupBox();
            this.comboBox_comport = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport = new System.Windows.Forms.PictureBox();
            this.comboBox_baud_rate = new System.Windows.Forms.ComboBox();
            this.bt_comport_scan = new System.Windows.Forms.Button();
            this.bt_comport_connect = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.groupBox_comport.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 100);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(127, 47);
            this.button1.TabIndex = 0;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(190, 224);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(614, 335);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(737, 536);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(67, 23);
            this.bt_clear.TabIndex = 2;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // groupBox_comport
            // 
            this.groupBox_comport.Controls.Add(this.comboBox_comport);
            this.groupBox_comport.Controls.Add(this.pictureBox_comport);
            this.groupBox_comport.Controls.Add(this.comboBox_baud_rate);
            this.groupBox_comport.Controls.Add(this.bt_comport_scan);
            this.groupBox_comport.Controls.Add(this.bt_comport_connect);
            this.groupBox_comport.Controls.Add(this.bt_comport_disconnect);
            this.groupBox_comport.Location = new System.Drawing.Point(12, 12);
            this.groupBox_comport.Name = "groupBox_comport";
            this.groupBox_comport.Size = new System.Drawing.Size(443, 70);
            this.groupBox_comport.TabIndex = 136;
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
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Enabled = true;
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(825, 610);
            this.Controls.Add(this.groupBox_comport);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_comport.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.GroupBox groupBox_comport;
        private System.Windows.Forms.ComboBox comboBox_comport;
        private System.Windows.Forms.PictureBox pictureBox_comport;
        private System.Windows.Forms.ComboBox comboBox_baud_rate;
        private System.Windows.Forms.Button bt_comport_scan;
        private System.Windows.Forms.Button bt_comport_connect;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
    }
}

