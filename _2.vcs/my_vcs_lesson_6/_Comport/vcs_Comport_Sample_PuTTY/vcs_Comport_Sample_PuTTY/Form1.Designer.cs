namespace vcs_Comport_Sample_PuTTY
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
            this.groupBox_comport = new System.Windows.Forms.GroupBox();
            this.comboBox_comport = new System.Windows.Forms.ComboBox();
            this.pictureBox_comport = new System.Windows.Forms.PictureBox();
            this.bt_comport_scan = new System.Windows.Forms.Button();
            this.bt_comport_connect = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.groupBox_comport.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox_comport
            // 
            this.groupBox_comport.Controls.Add(this.comboBox_comport);
            this.groupBox_comport.Controls.Add(this.pictureBox_comport);
            this.groupBox_comport.Controls.Add(this.bt_comport_scan);
            this.groupBox_comport.Controls.Add(this.bt_comport_connect);
            this.groupBox_comport.Controls.Add(this.bt_comport_disconnect);
            this.groupBox_comport.Location = new System.Drawing.Point(12, 12);
            this.groupBox_comport.Name = "groupBox_comport";
            this.groupBox_comport.Size = new System.Drawing.Size(461, 68);
            this.groupBox_comport.TabIndex = 137;
            this.groupBox_comport.TabStop = false;
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
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 86);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(802, 486);
            this.richTextBox1.TabIndex = 138;
            this.richTextBox1.Text = "";
            this.richTextBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.richTextBox1_KeyPress);
            // 
            // serialPort1
            // 
            this.serialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(826, 584);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox_comport);
            this.Name = "Form1";
            this.Text = "PuTTY";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_comport.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_comport)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox_comport;
        private System.Windows.Forms.ComboBox comboBox_comport;
        private System.Windows.Forms.PictureBox pictureBox_comport;
        private System.Windows.Forms.Button bt_comport_scan;
        private System.Windows.Forms.Button bt_comport_connect;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.IO.Ports.SerialPort serialPort1;
    }
}

