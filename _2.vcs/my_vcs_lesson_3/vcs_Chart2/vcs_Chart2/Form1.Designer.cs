namespace vcs_Chart2
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox_temperature = new System.Windows.Forms.GroupBox();
            this.bt_demo = new System.Windows.Forms.Button();
            this.lb_temperature = new System.Windows.Forms.Label();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.bt_temperature_off = new System.Windows.Forms.Button();
            this.bt_comport = new System.Windows.Forms.Button();
            this.bt_temperature_on = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.timer_demo = new System.Windows.Forms.Timer(this.components);
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox_temperature.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(169, 53);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 60;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(160, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 59;
            this.richTextBox1.Text = "";
            // 
            // groupBox_temperature
            // 
            this.groupBox_temperature.Controls.Add(this.bt_demo);
            this.groupBox_temperature.Controls.Add(this.lb_temperature);
            this.groupBox_temperature.Controls.Add(this.bt_comport_disconnect);
            this.groupBox_temperature.Controls.Add(this.bt_temperature_off);
            this.groupBox_temperature.Controls.Add(this.bt_comport);
            this.groupBox_temperature.Controls.Add(this.bt_temperature_on);
            this.groupBox_temperature.Location = new System.Drawing.Point(10, 10);
            this.groupBox_temperature.Name = "groupBox_temperature";
            this.groupBox_temperature.Size = new System.Drawing.Size(137, 274);
            this.groupBox_temperature.TabIndex = 188;
            this.groupBox_temperature.TabStop = false;
            // 
            // bt_demo
            // 
            this.bt_demo.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_demo.Location = new System.Drawing.Point(6, 203);
            this.bt_demo.Name = "bt_demo";
            this.bt_demo.Size = new System.Drawing.Size(120, 45);
            this.bt_demo.TabIndex = 190;
            this.bt_demo.Text = "Demo啟動";
            this.bt_demo.UseVisualStyleBackColor = true;
            this.bt_demo.Click += new System.EventHandler(this.bt_demo_Click);
            // 
            // lb_temperature
            // 
            this.lb_temperature.AutoSize = true;
            this.lb_temperature.Font = new System.Drawing.Font("Arial", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_temperature.ForeColor = System.Drawing.Color.Red;
            this.lb_temperature.Location = new System.Drawing.Point(15, 17);
            this.lb_temperature.Name = "lb_temperature";
            this.lb_temperature.Size = new System.Drawing.Size(31, 34);
            this.lb_temperature.TabIndex = 185;
            this.lb_temperature.Text = "c";
            // 
            // bt_comport_disconnect
            // 
            this.bt_comport_disconnect.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_comport_disconnect.Location = new System.Drawing.Point(57, 152);
            this.bt_comport_disconnect.Name = "bt_comport_disconnect";
            this.bt_comport_disconnect.Size = new System.Drawing.Size(45, 45);
            this.bt_comport_disconnect.TabIndex = 192;
            this.bt_comport_disconnect.Text = "斷";
            this.bt_comport_disconnect.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect.Click += new System.EventHandler(this.bt_comport_disconnect_Click);
            // 
            // bt_temperature_off
            // 
            this.bt_temperature_off.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_off.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_off.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_off.Location = new System.Drawing.Point(6, 102);
            this.bt_temperature_off.Name = "bt_temperature_off";
            this.bt_temperature_off.Size = new System.Drawing.Size(120, 45);
            this.bt_temperature_off.TabIndex = 184;
            this.bt_temperature_off.Text = "溫度偵測 OFF";
            this.bt_temperature_off.UseVisualStyleBackColor = false;
            this.bt_temperature_off.Click += new System.EventHandler(this.bt_temperature_off_Click);
            // 
            // bt_comport
            // 
            this.bt_comport.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_comport.Location = new System.Drawing.Point(6, 152);
            this.bt_comport.Name = "bt_comport";
            this.bt_comport.Size = new System.Drawing.Size(45, 45);
            this.bt_comport.TabIndex = 191;
            this.bt_comport.Text = "連";
            this.bt_comport.UseVisualStyleBackColor = true;
            this.bt_comport.Click += new System.EventHandler(this.bt_comport_Click);
            // 
            // bt_temperature_on
            // 
            this.bt_temperature_on.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_on.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_on.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_on.Location = new System.Drawing.Point(6, 61);
            this.bt_temperature_on.Name = "bt_temperature_on";
            this.bt_temperature_on.Size = new System.Drawing.Size(120, 45);
            this.bt_temperature_on.TabIndex = 183;
            this.bt_temperature_on.Text = "溫度偵測 ON";
            this.bt_temperature_on.UseVisualStyleBackColor = false;
            this.bt_temperature_on.Click += new System.EventHandler(this.bt_temperature_on_Click);
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
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(160, 116);
            this.chart1.Name = "chart1";
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(100, 100);
            this.chart1.TabIndex = 189;
            this.chart1.Text = "chart1";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(484, 461);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.groupBox_temperature);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox_temperature.ResumeLayout(false);
            this.groupBox_temperature.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox_temperature;
        private System.Windows.Forms.Button bt_temperature_off;
        private System.Windows.Forms.Label lb_temperature;
        private System.Windows.Forms.Button bt_temperature_on;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Timer timer_demo;
        private System.Windows.Forms.Button bt_demo;
        private System.Windows.Forms.Button bt_comport;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Timer timer1;
    }
}

