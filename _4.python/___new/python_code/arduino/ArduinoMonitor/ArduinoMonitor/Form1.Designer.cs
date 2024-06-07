namespace ArduinoMonitor
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
            this.bt_comport_scan = new System.Windows.Forms.Button();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.button9 = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.bt_comport_connect = new System.Windows.Forms.Button();
            this.panel3 = new System.Windows.Forms.Panel();
            this.tb_main_rpm = new System.Windows.Forms.TextBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.tb_main_duty2 = new System.Windows.Forms.TextBox();
            this.panel4 = new System.Windows.Forms.Panel();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.aGauge_rpm = new AGaugeApp.AGauge();
            this.aGauge_duty = new AGaugeApp.AGauge();
            this.panel3.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // bt_comport_scan
            // 
            this.bt_comport_scan.Location = new System.Drawing.Point(196, 12);
            this.bt_comport_scan.Name = "bt_comport_scan";
            this.bt_comport_scan.Size = new System.Drawing.Size(74, 33);
            this.bt_comport_scan.TabIndex = 27;
            this.bt_comport_scan.Text = "COM Scan";
            this.bt_comport_scan.UseVisualStyleBackColor = true;
            this.bt_comport_scan.Click += new System.EventHandler(this.bt_comport_scan_Click);
            // 
            // comboBox2
            // 
            this.comboBox2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox2.Location = new System.Drawing.Point(102, 13);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(88, 27);
            this.comboBox2.TabIndex = 26;
            this.comboBox2.Text = "115200";
            // 
            // comboBox1
            // 
            this.comboBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(12, 12);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(89, 27);
            this.comboBox1.TabIndex = 25;
            // 
            // button9
            // 
            this.button9.BackColor = System.Drawing.Color.Black;
            this.button9.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.ForeColor = System.Drawing.Color.White;
            this.button9.Location = new System.Drawing.Point(415, 11);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(64, 33);
            this.button9.TabIndex = 24;
            this.button9.Text = "Reset";
            this.button9.UseVisualStyleBackColor = false;
            // 
            // bt_comport_disconnect
            // 
            this.bt_comport_disconnect.Location = new System.Drawing.Point(342, 12);
            this.bt_comport_disconnect.Name = "bt_comport_disconnect";
            this.bt_comport_disconnect.Size = new System.Drawing.Size(67, 33);
            this.bt_comport_disconnect.TabIndex = 23;
            this.bt_comport_disconnect.Text = "Disconnect";
            this.bt_comport_disconnect.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect.Click += new System.EventHandler(this.bt_comport_disconnect_Click);
            // 
            // bt_comport_connect
            // 
            this.bt_comport_connect.Location = new System.Drawing.Point(278, 12);
            this.bt_comport_connect.Name = "bt_comport_connect";
            this.bt_comport_connect.Size = new System.Drawing.Size(57, 33);
            this.bt_comport_connect.TabIndex = 22;
            this.bt_comport_connect.Text = "Connect";
            this.bt_comport_connect.UseVisualStyleBackColor = true;
            this.bt_comport_connect.Click += new System.EventHandler(this.bt_comport_connect_Click);
            // 
            // panel3
            // 
            this.panel3.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.panel3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel3.Controls.Add(this.tb_main_rpm);
            this.panel3.Controls.Add(this.aGauge_rpm);
            this.panel3.Location = new System.Drawing.Point(291, 71);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(351, 300);
            this.panel3.TabIndex = 33;
            // 
            // tb_main_rpm
            // 
            this.tb_main_rpm.Font = new System.Drawing.Font("Consolas", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_main_rpm.Location = new System.Drawing.Point(122, 248);
            this.tb_main_rpm.Name = "tb_main_rpm";
            this.tb_main_rpm.Size = new System.Drawing.Size(104, 41);
            this.tb_main_rpm.TabIndex = 23;
            this.tb_main_rpm.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.panel2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel2.Controls.Add(this.tb_main_duty2);
            this.panel2.Controls.Add(this.aGauge_duty);
            this.panel2.Location = new System.Drawing.Point(12, 71);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(273, 300);
            this.panel2.TabIndex = 32;
            // 
            // tb_main_duty2
            // 
            this.tb_main_duty2.Font = new System.Drawing.Font("Consolas", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tb_main_duty2.Location = new System.Drawing.Point(108, 248);
            this.tb_main_duty2.Name = "tb_main_duty2";
            this.tb_main_duty2.Size = new System.Drawing.Size(104, 41);
            this.tb_main_duty2.TabIndex = 22;
            this.tb_main_duty2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // panel4
            // 
            this.panel4.BackColor = System.Drawing.Color.White;
            this.panel4.Location = new System.Drawing.Point(12, 377);
            this.panel4.Name = "panel4";
            this.panel4.Size = new System.Drawing.Size(630, 375);
            this.panel4.TabIndex = 34;
            // 
            // serialPort1
            // 
            this.serialPort1.RtsEnable = true;
            // 
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Enabled = true;
            this.SerialPortTimer100ms.Interval = 10;
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.Color.Black;
            this.richTextBox1.Font = new System.Drawing.Font("Courier New", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox1.ForeColor = System.Drawing.Color.White;
            this.richTextBox1.Location = new System.Drawing.Point(648, 71);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(382, 594);
            this.richTextBox1.TabIndex = 35;
            this.richTextBox1.Text = "";
            // 
            // aGauge_rpm
            // 
            this.aGauge_rpm.BackColor = System.Drawing.SystemColors.Window;
            this.aGauge_rpm.BaseArcColor = System.Drawing.Color.Gray;
            this.aGauge_rpm.BaseArcRadius = 120;
            this.aGauge_rpm.BaseArcStart = 135;
            this.aGauge_rpm.BaseArcSweep = 270;
            this.aGauge_rpm.BaseArcWidth = 2;
            this.aGauge_rpm.Cap_Idx = ((byte)(1));
            this.aGauge_rpm.CapColors = new System.Drawing.Color[] {
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black};
            this.aGauge_rpm.CapPosition = new System.Drawing.Point(150, 190);
            this.aGauge_rpm.CapsPosition = new System.Drawing.Point[] {
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(150, 190),
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(10, 10)};
            this.aGauge_rpm.CapsText = new string[] {
        "",
        "rpm",
        "",
        "",
        ""};
            this.aGauge_rpm.CapText = "rpm";
            this.aGauge_rpm.Center = new System.Drawing.Point(160, 160);
            this.aGauge_rpm.Location = new System.Drawing.Point(17, 1);
            this.aGauge_rpm.MaxValue = 3000F;
            this.aGauge_rpm.MinValue = 0F;
            this.aGauge_rpm.Name = "aGauge_rpm";
            this.aGauge_rpm.NeedleColor1 = AGaugeApp.AGauge.NeedleColorEnum.Gray;
            this.aGauge_rpm.NeedleColor2 = System.Drawing.Color.DimGray;
            this.aGauge_rpm.NeedleRadius = 80;
            this.aGauge_rpm.NeedleType = 0;
            this.aGauge_rpm.NeedleWidth = 2;
            this.aGauge_rpm.Range_Idx = ((byte)(2));
            this.aGauge_rpm.RangeColor = System.Drawing.Color.Red;
            this.aGauge_rpm.RangeEnabled = true;
            this.aGauge_rpm.RangeEndValue = 3000F;
            this.aGauge_rpm.RangeInnerRadius = 105;
            this.aGauge_rpm.RangeOuterRadius = 120;
            this.aGauge_rpm.RangesColor = new System.Drawing.Color[] {
        System.Drawing.Color.LightGreen,
        System.Drawing.Color.Yellow,
        System.Drawing.Color.Red,
        System.Drawing.SystemColors.Control,
        System.Drawing.SystemColors.Control};
            this.aGauge_rpm.RangesEnabled = new bool[] {
        true,
        true,
        true,
        false,
        false};
            this.aGauge_rpm.RangesEndValue = new float[] {
        2000F,
        2500F,
        3000F,
        0F,
        0F};
            this.aGauge_rpm.RangesInnerRadius = new int[] {
        105,
        105,
        105,
        70,
        70};
            this.aGauge_rpm.RangesOuterRadius = new int[] {
        120,
        120,
        120,
        80,
        80};
            this.aGauge_rpm.RangesStartValue = new float[] {
        0F,
        2000F,
        2500F,
        0F,
        0F};
            this.aGauge_rpm.RangeStartValue = 2500F;
            this.aGauge_rpm.ScaleLinesInterColor = System.Drawing.Color.Black;
            this.aGauge_rpm.ScaleLinesInterInnerRadius = 109;
            this.aGauge_rpm.ScaleLinesInterOuterRadius = 120;
            this.aGauge_rpm.ScaleLinesInterWidth = 1;
            this.aGauge_rpm.ScaleLinesMajorColor = System.Drawing.Color.Black;
            this.aGauge_rpm.ScaleLinesMajorInnerRadius = 105;
            this.aGauge_rpm.ScaleLinesMajorOuterRadius = 120;
            this.aGauge_rpm.ScaleLinesMajorStepValue = 300F;
            this.aGauge_rpm.ScaleLinesMajorWidth = 2;
            this.aGauge_rpm.ScaleLinesMinorColor = System.Drawing.Color.Gray;
            this.aGauge_rpm.ScaleLinesMinorInnerRadius = 112;
            this.aGauge_rpm.ScaleLinesMinorNumOf = 9;
            this.aGauge_rpm.ScaleLinesMinorOuterRadius = 120;
            this.aGauge_rpm.ScaleLinesMinorWidth = 1;
            this.aGauge_rpm.ScaleNumbersColor = System.Drawing.Color.Black;
            this.aGauge_rpm.ScaleNumbersFormat = null;
            this.aGauge_rpm.ScaleNumbersRadius = 142;
            this.aGauge_rpm.ScaleNumbersRotation = 0;
            this.aGauge_rpm.ScaleNumbersStartScaleLine = 0;
            this.aGauge_rpm.ScaleNumbersStepScaleLines = 1;
            this.aGauge_rpm.Size = new System.Drawing.Size(320, 280);
            this.aGauge_rpm.TabIndex = 1;
            this.aGauge_rpm.Text = "aGauge2";
            this.aGauge_rpm.Value = 0F;
            // 
            // aGauge_duty
            // 
            this.aGauge_duty.BackColor = System.Drawing.SystemColors.Window;
            this.aGauge_duty.BaseArcColor = System.Drawing.Color.Gray;
            this.aGauge_duty.BaseArcRadius = 120;
            this.aGauge_duty.BaseArcStart = 135;
            this.aGauge_duty.BaseArcSweep = 165;
            this.aGauge_duty.BaseArcWidth = 2;
            this.aGauge_duty.Cap_Idx = ((byte)(1));
            this.aGauge_duty.CapColors = new System.Drawing.Color[] {
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black,
        System.Drawing.Color.Black};
            this.aGauge_duty.CapPosition = new System.Drawing.Point(150, 190);
            this.aGauge_duty.CapsPosition = new System.Drawing.Point[] {
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(150, 190),
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(10, 10),
        new System.Drawing.Point(10, 10)};
            this.aGauge_duty.CapsText = new string[] {
        "",
        "duty",
        "",
        "",
        ""};
            this.aGauge_duty.CapText = "duty";
            this.aGauge_duty.Center = new System.Drawing.Point(160, 160);
            this.aGauge_duty.Location = new System.Drawing.Point(-1, -1);
            this.aGauge_duty.MaxValue = 100F;
            this.aGauge_duty.MinValue = 0F;
            this.aGauge_duty.Name = "aGauge_duty";
            this.aGauge_duty.NeedleColor1 = AGaugeApp.AGauge.NeedleColorEnum.Gray;
            this.aGauge_duty.NeedleColor2 = System.Drawing.Color.DimGray;
            this.aGauge_duty.NeedleRadius = 80;
            this.aGauge_duty.NeedleType = 0;
            this.aGauge_duty.NeedleWidth = 2;
            this.aGauge_duty.Range_Idx = ((byte)(2));
            this.aGauge_duty.RangeColor = System.Drawing.Color.Red;
            this.aGauge_duty.RangeEnabled = true;
            this.aGauge_duty.RangeEndValue = 100F;
            this.aGauge_duty.RangeInnerRadius = 105;
            this.aGauge_duty.RangeOuterRadius = 120;
            this.aGauge_duty.RangesColor = new System.Drawing.Color[] {
        System.Drawing.Color.LightGreen,
        System.Drawing.Color.Yellow,
        System.Drawing.Color.Red,
        System.Drawing.SystemColors.Control,
        System.Drawing.SystemColors.Control};
            this.aGauge_duty.RangesEnabled = new bool[] {
        true,
        true,
        true,
        false,
        false};
            this.aGauge_duty.RangesEndValue = new float[] {
        60F,
        80F,
        100F,
        0F,
        0F};
            this.aGauge_duty.RangesInnerRadius = new int[] {
        105,
        105,
        105,
        70,
        70};
            this.aGauge_duty.RangesOuterRadius = new int[] {
        120,
        120,
        120,
        80,
        80};
            this.aGauge_duty.RangesStartValue = new float[] {
        0F,
        60F,
        80F,
        0F,
        0F};
            this.aGauge_duty.RangeStartValue = 80F;
            this.aGauge_duty.ScaleLinesInterColor = System.Drawing.Color.Black;
            this.aGauge_duty.ScaleLinesInterInnerRadius = 109;
            this.aGauge_duty.ScaleLinesInterOuterRadius = 120;
            this.aGauge_duty.ScaleLinesInterWidth = 1;
            this.aGauge_duty.ScaleLinesMajorColor = System.Drawing.Color.Black;
            this.aGauge_duty.ScaleLinesMajorInnerRadius = 105;
            this.aGauge_duty.ScaleLinesMajorOuterRadius = 120;
            this.aGauge_duty.ScaleLinesMajorStepValue = 10F;
            this.aGauge_duty.ScaleLinesMajorWidth = 2;
            this.aGauge_duty.ScaleLinesMinorColor = System.Drawing.Color.Gray;
            this.aGauge_duty.ScaleLinesMinorInnerRadius = 112;
            this.aGauge_duty.ScaleLinesMinorNumOf = 9;
            this.aGauge_duty.ScaleLinesMinorOuterRadius = 120;
            this.aGauge_duty.ScaleLinesMinorWidth = 1;
            this.aGauge_duty.ScaleNumbersColor = System.Drawing.Color.Black;
            this.aGauge_duty.ScaleNumbersFormat = null;
            this.aGauge_duty.ScaleNumbersRadius = 95;
            this.aGauge_duty.ScaleNumbersRotation = 0;
            this.aGauge_duty.ScaleNumbersStartScaleLine = 0;
            this.aGauge_duty.ScaleNumbersStepScaleLines = 1;
            this.aGauge_duty.Size = new System.Drawing.Size(240, 280);
            this.aGauge_duty.TabIndex = 0;
            this.aGauge_duty.Text = "aGauge1";
            this.aGauge_duty.Value = 0F;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1038, 764);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.panel4);
            this.Controls.Add(this.panel3);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.bt_comport_scan);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.bt_comport_disconnect);
            this.Controls.Add(this.bt_comport_connect);
            this.Name = "Form1";
            this.Text = "ArduinoMonitor";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_comport_scan;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.Button bt_comport_connect;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.TextBox tb_main_rpm;
        private AGaugeApp.AGauge aGauge_rpm;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.TextBox tb_main_duty2;
        private AGaugeApp.AGauge aGauge_duty;
        private System.Windows.Forms.Panel panel4;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

