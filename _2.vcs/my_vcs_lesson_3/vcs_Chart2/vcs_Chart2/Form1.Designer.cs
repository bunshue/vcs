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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea5 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend5 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series5 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart0 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer0 = new System.Windows.Forms.Timer(this.components);
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBoxA = new System.Windows.Forms.GroupBox();
            this.lb_temperatureA = new System.Windows.Forms.Label();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            this.bt_temperature_off = new System.Windows.Forms.Button();
            this.bt_comport = new System.Windows.Forms.Button();
            this.bt_demo = new System.Windows.Forms.Button();
            this.bt_temperature_on = new System.Windows.Forms.Button();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.timer_demo = new System.Windows.Forms.Timer(this.components);
            this.groupBoxB = new System.Windows.Forms.GroupBox();
            this.lb_temperatureB = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.chart0)).BeginInit();
            this.groupBoxA.SuspendLayout();
            this.groupBoxB.SuspendLayout();
            this.SuspendLayout();
            // 
            // chart0
            // 
            chartArea5.Name = "ChartArea1";
            this.chart0.ChartAreas.Add(chartArea5);
            legend5.Name = "Legend1";
            this.chart0.Legends.Add(legend5);
            this.chart0.Location = new System.Drawing.Point(12, 12);
            this.chart0.Name = "chart0";
            series5.ChartArea = "ChartArea1";
            series5.Legend = "Legend1";
            series5.Name = "Series1";
            this.chart0.Series.Add(series5);
            this.chart0.Size = new System.Drawing.Size(100, 100);
            this.chart0.TabIndex = 5;
            this.chart0.Text = "chart6";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(22, 162);
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
            this.richTextBox1.Location = new System.Drawing.Point(10, 129);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 59;
            this.richTextBox1.Text = "";
            // 
            // timer0
            // 
            this.timer0.Enabled = true;
            this.timer0.Tick += new System.EventHandler(this.timer0_Tick);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 300;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // groupBoxA
            // 
            this.groupBoxA.Controls.Add(this.lb_temperatureA);
            this.groupBoxA.Controls.Add(this.bt_comport_disconnect);
            this.groupBoxA.Controls.Add(this.bt_temperature_off);
            this.groupBoxA.Controls.Add(this.bt_comport);
            this.groupBoxA.Controls.Add(this.bt_temperature_on);
            this.groupBoxA.Location = new System.Drawing.Point(141, 12);
            this.groupBoxA.Name = "groupBoxA";
            this.groupBoxA.Size = new System.Drawing.Size(137, 217);
            this.groupBoxA.TabIndex = 188;
            this.groupBoxA.TabStop = false;
            // 
            // lb_temperatureA
            // 
            this.lb_temperatureA.AutoSize = true;
            this.lb_temperatureA.Font = new System.Drawing.Font("Arial", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_temperatureA.ForeColor = System.Drawing.Color.Red;
            this.lb_temperatureA.Location = new System.Drawing.Point(15, 17);
            this.lb_temperatureA.Name = "lb_temperatureA";
            this.lb_temperatureA.Size = new System.Drawing.Size(31, 34);
            this.lb_temperatureA.TabIndex = 185;
            this.lb_temperatureA.Text = "c";
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
            // bt_demo
            // 
            this.bt_demo.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_demo.Location = new System.Drawing.Point(16, 64);
            this.bt_demo.Name = "bt_demo";
            this.bt_demo.Size = new System.Drawing.Size(120, 45);
            this.bt_demo.TabIndex = 190;
            this.bt_demo.Text = "Demo";
            this.bt_demo.UseVisualStyleBackColor = true;
            this.bt_demo.Click += new System.EventHandler(this.bt_demo_Click);
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
            // groupBoxB
            // 
            this.groupBoxB.Controls.Add(this.lb_temperatureB);
            this.groupBoxB.Controls.Add(this.bt_demo);
            this.groupBoxB.Location = new System.Drawing.Point(296, 12);
            this.groupBoxB.Name = "groupBoxB";
            this.groupBoxB.Size = new System.Drawing.Size(142, 134);
            this.groupBoxB.TabIndex = 193;
            this.groupBoxB.TabStop = false;
            // 
            // lb_temperatureB
            // 
            this.lb_temperatureB.AutoSize = true;
            this.lb_temperatureB.Font = new System.Drawing.Font("Arial", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_temperatureB.ForeColor = System.Drawing.Color.Red;
            this.lb_temperatureB.Location = new System.Drawing.Point(15, 17);
            this.lb_temperatureB.Name = "lb_temperatureB";
            this.lb_temperatureB.Size = new System.Drawing.Size(31, 34);
            this.lb_temperatureB.TabIndex = 185;
            this.lb_temperatureB.Text = "c";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(631, 483);
            this.Controls.Add(this.groupBoxB);
            this.Controls.Add(this.groupBoxA);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.chart0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart0)).EndInit();
            this.groupBoxA.ResumeLayout(false);
            this.groupBoxA.PerformLayout();
            this.groupBoxB.ResumeLayout(false);
            this.groupBoxB.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart0;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer0;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.GroupBox groupBoxA;
        private System.Windows.Forms.Button bt_temperature_off;
        private System.Windows.Forms.Label lb_temperatureA;
        private System.Windows.Forms.Button bt_temperature_on;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Timer timer_demo;
        private System.Windows.Forms.Button bt_demo;
        private System.Windows.Forms.Button bt_comport;
        private System.Windows.Forms.Button bt_comport_disconnect;
        private System.Windows.Forms.GroupBox groupBoxB;
        private System.Windows.Forms.Label lb_temperatureB;
    }
}

