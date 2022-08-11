namespace vcs_Chart1
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
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.button1 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.bt_save = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_clear_chart = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button0 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(151, 12);
            this.chart1.Name = "chart1";
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(300, 300);
            this.chart1.TabIndex = 0;
            this.chart1.Text = "chart1";
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(12, 69);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(130, 40);
            this.button1.TabIndex = 1;
            this.button1.Text = "靜畫範例1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(12, 184);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(130, 40);
            this.button3.TabIndex = 2;
            this.button3.Text = "動畫 ST";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(12, 288);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(130, 40);
            this.bt_save.TabIndex = 3;
            this.bt_save.Text = "存檔";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(881, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(252, 566);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(12, 127);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(130, 40);
            this.button2.TabIndex = 5;
            this.button2.Text = "靜畫範例2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1061, 537);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 39);
            this.bt_clear.TabIndex = 6;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_clear_chart
            // 
            this.bt_clear_chart.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_chart.Location = new System.Drawing.Point(12, 243);
            this.bt_clear_chart.Name = "bt_clear_chart";
            this.bt_clear_chart.Size = new System.Drawing.Size(130, 40);
            this.bt_clear_chart.TabIndex = 7;
            this.bt_clear_chart.Text = "清除";
            this.bt_clear_chart.UseVisualStyleBackColor = true;
            this.bt_clear_chart.Click += new System.EventHandler(this.bt_clear_chart_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(15, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(130, 40);
            this.button0.TabIndex = 8;
            this.button0.Text = "Chart初始化";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1145, 588);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.bt_clear_chart);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.bt_save);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.chart1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_clear_chart;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button button0;
    }
}

