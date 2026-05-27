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
            this.chart0 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer0 = new System.Windows.Forms.Timer(this.components);
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_temperature_off = new System.Windows.Forms.Button();
            this.lb_temperature = new System.Windows.Forms.Label();
            this.bt_temperature_on = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.timer_demo = new System.Windows.Forms.Timer(this.components);
            this.bt_demo = new System.Windows.Forms.Button();
            this.bt_comport = new System.Windows.Forms.Button();
            this.bt_comport_disconnect = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.chart0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // chart0
            // 
            chartArea1.Name = "ChartArea1";
            this.chart0.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart0.Legends.Add(legend1);
            this.chart0.Location = new System.Drawing.Point(12, 12);
            this.chart0.Name = "chart0";
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart0.Series.Add(series1);
            this.chart0.Size = new System.Drawing.Size(100, 100);
            this.chart0.TabIndex = 5;
            this.chart0.Text = "chart6";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(27, 294);
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
            this.richTextBox1.Location = new System.Drawing.Point(15, 261);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 59;
            this.richTextBox1.Text = "";
            // 
            // timer0
            // 
            this.timer0.Tick += new System.EventHandler(this.timer0_Tick);
            // 
            // timer1
            // 
            this.timer1.Interval = 300;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 140);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 61;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lb_temperature);
            this.groupBox1.Controls.Add(this.bt_comport_disconnect);
            this.groupBox1.Controls.Add(this.bt_temperature_off);
            this.groupBox1.Controls.Add(this.bt_comport);
            this.groupBox1.Controls.Add(this.bt_demo);
            this.groupBox1.Controls.Add(this.bt_temperature_on);
            this.groupBox1.Location = new System.Drawing.Point(141, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(449, 134);
            this.groupBox1.TabIndex = 188;
            this.groupBox1.TabStop = false;
            // 
            // bt_temperature_off
            // 
            this.bt_temperature_off.BackColor = System.Drawing.SystemColors.Control;
            this.bt_temperature_off.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_off.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_off.Location = new System.Drawing.Point(202, 54);
            this.bt_temperature_off.Name = "bt_temperature_off";
            this.bt_temperature_off.Size = new System.Drawing.Size(120, 45);
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
            this.bt_temperature_on.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bt_temperature_on.ForeColor = System.Drawing.Color.Red;
            this.bt_temperature_on.Location = new System.Drawing.Point(202, 13);
            this.bt_temperature_on.Name = "bt_temperature_on";
            this.bt_temperature_on.Size = new System.Drawing.Size(120, 45);
            this.bt_temperature_on.TabIndex = 183;
            this.bt_temperature_on.Text = "溫度偵測 ON";
            this.bt_temperature_on.UseVisualStyleBackColor = false;
            this.bt_temperature_on.Click += new System.EventHandler(this.bt_temperature_on_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(132, 140);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 189;
            this.pictureBox2.TabStop = false;
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
            // bt_demo
            // 
            this.bt_demo.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_demo.Location = new System.Drawing.Point(326, 13);
            this.bt_demo.Name = "bt_demo";
            this.bt_demo.Size = new System.Drawing.Size(100, 45);
            this.bt_demo.TabIndex = 190;
            this.bt_demo.Text = "Demo";
            this.bt_demo.UseVisualStyleBackColor = true;
            this.bt_demo.Click += new System.EventHandler(this.bt_demo_Click);
            // 
            // bt_comport
            // 
            this.bt_comport.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_comport.Location = new System.Drawing.Point(326, 54);
            this.bt_comport.Name = "bt_comport";
            this.bt_comport.Size = new System.Drawing.Size(45, 45);
            this.bt_comport.TabIndex = 191;
            this.bt_comport.Text = "連";
            this.bt_comport.UseVisualStyleBackColor = true;
            this.bt_comport.Click += new System.EventHandler(this.bt_comport_Click);
            // 
            // bt_comport_disconnect
            // 
            this.bt_comport_disconnect.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_comport_disconnect.Location = new System.Drawing.Point(377, 54);
            this.bt_comport_disconnect.Name = "bt_comport_disconnect";
            this.bt_comport_disconnect.Size = new System.Drawing.Size(45, 45);
            this.bt_comport_disconnect.TabIndex = 192;
            this.bt_comport_disconnect.Text = "斷";
            this.bt_comport_disconnect.UseVisualStyleBackColor = true;
            this.bt_comport_disconnect.Click += new System.EventHandler(this.bt_comport_disconnect_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(695, 518);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.chart0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart0;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer0;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_temperature_off;
        private System.Windows.Forms.Label lb_temperature;
        private System.Windows.Forms.Button bt_temperature_on;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Timer timer_demo;
        private System.Windows.Forms.Button bt_demo;
        private System.Windows.Forms.Button bt_comport;
        private System.Windows.Forms.Button bt_comport_disconnect;
    }
}

