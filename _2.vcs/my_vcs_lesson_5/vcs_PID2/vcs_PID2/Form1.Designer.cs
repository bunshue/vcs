namespace vcs_PID2
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea7 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series7 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.bt_clear = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.lb_total_candles = new System.Windows.Forms.Label();
            this.lb_total_energy = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tb_kp = new System.Windows.Forms.TextBox();
            this.tb_ki = new System.Windows.Forms.TextBox();
            this.tb_kd = new System.Windows.Forms.TextBox();
            this.lb_pid = new System.Windows.Forms.Label();
            this.lb_target = new System.Windows.Forms.Label();
            this.lb_temperature = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 35);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(197, 467);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(730, 236);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 191);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 2;
            this.button2.Text = "+ 100";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // timer1
            // 
            this.timer1.Interval = 400;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(787, 608);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(75, 23);
            this.bt_clear.TabIndex = 3;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 234);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 4;
            this.button3.Text = "+ 50";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 279);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 5;
            this.button4.Text = "+ 10";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // chart1
            // 
            chartArea7.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea7);
            this.chart1.Location = new System.Drawing.Point(197, 12);
            this.chart1.Name = "chart1";
            series7.ChartArea = "ChartArea1";
            series7.Name = "Series1";
            this.chart1.Series.Add(series7);
            this.chart1.Size = new System.Drawing.Size(730, 305);
            this.chart1.TabIndex = 6;
            this.chart1.Text = "chart1";
            // 
            // lb_total_candles
            // 
            this.lb_total_candles.AutoSize = true;
            this.lb_total_candles.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_total_candles.Location = new System.Drawing.Point(13, 93);
            this.lb_total_candles.Name = "lb_total_candles";
            this.lb_total_candles.Size = new System.Drawing.Size(74, 27);
            this.lb_total_candles.TabIndex = 7;
            this.lb_total_candles.Text = "label1";
            // 
            // lb_total_energy
            // 
            this.lb_total_energy.AutoSize = true;
            this.lb_total_energy.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_total_energy.Location = new System.Drawing.Point(13, 138);
            this.lb_total_energy.Name = "lb_total_energy";
            this.lb_total_energy.Size = new System.Drawing.Size(74, 27);
            this.lb_total_energy.TabIndex = 8;
            this.lb_total_energy.Text = "label1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(13, 404);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(295, 27);
            this.label1.TabIndex = 9;
            this.label1.Text = "Kp              Ki              Kd";
            // 
            // tb_kp
            // 
            this.tb_kp.Font = new System.Drawing.Font("新細明體", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_kp.Location = new System.Drawing.Point(56, 401);
            this.tb_kp.Name = "tb_kp";
            this.tb_kp.Size = new System.Drawing.Size(80, 42);
            this.tb_kp.TabIndex = 10;
            this.tb_kp.Text = "1.5";
            this.tb_kp.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_ki
            // 
            this.tb_ki.Font = new System.Drawing.Font("新細明體", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_ki.Location = new System.Drawing.Point(180, 400);
            this.tb_ki.Name = "tb_ki";
            this.tb_ki.Size = new System.Drawing.Size(80, 42);
            this.tb_ki.TabIndex = 11;
            this.tb_ki.Text = "0.6";
            this.tb_ki.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_kd
            // 
            this.tb_kd.Font = new System.Drawing.Font("新細明體", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_kd.Location = new System.Drawing.Point(314, 400);
            this.tb_kd.Name = "tb_kd";
            this.tb_kd.Size = new System.Drawing.Size(80, 42);
            this.tb_kd.TabIndex = 12;
            this.tb_kd.Text = "0.6";
            this.tb_kd.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_pid
            // 
            this.lb_pid.AutoSize = true;
            this.lb_pid.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_pid.Location = new System.Drawing.Point(13, 460);
            this.lb_pid.Name = "lb_pid";
            this.lb_pid.Size = new System.Drawing.Size(74, 27);
            this.lb_pid.TabIndex = 13;
            this.lb_pid.Text = "label1";
            // 
            // lb_target
            // 
            this.lb_target.AutoSize = true;
            this.lb_target.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_target.Location = new System.Drawing.Point(12, 521);
            this.lb_target.Name = "lb_target";
            this.lb_target.Size = new System.Drawing.Size(74, 27);
            this.lb_target.TabIndex = 14;
            this.lb_target.Text = "label1";
            // 
            // lb_temperature
            // 
            this.lb_temperature.AutoSize = true;
            this.lb_temperature.Font = new System.Drawing.Font("新細明體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_temperature.Location = new System.Drawing.Point(13, 570);
            this.lb_temperature.Name = "lb_temperature";
            this.lb_temperature.Size = new System.Drawing.Size(74, 27);
            this.lb_temperature.TabIndex = 15;
            this.lb_temperature.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(998, 725);
            this.Controls.Add(this.lb_temperature);
            this.Controls.Add(this.lb_target);
            this.Controls.Add(this.lb_pid);
            this.Controls.Add(this.tb_kd);
            this.Controls.Add(this.tb_ki);
            this.Controls.Add(this.tb_kp);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lb_total_energy);
            this.Controls.Add(this.lb_total_candles);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Label lb_total_candles;
        private System.Windows.Forms.Label lb_total_energy;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_kp;
        private System.Windows.Forms.TextBox tb_ki;
        private System.Windows.Forms.TextBox tb_kd;
        private System.Windows.Forms.Label lb_pid;
        private System.Windows.Forms.Label lb_target;
        private System.Windows.Forms.Label lb_temperature;
    }
}

