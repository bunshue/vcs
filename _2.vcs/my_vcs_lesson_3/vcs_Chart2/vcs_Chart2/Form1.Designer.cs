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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend2 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series2 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_start = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.cb_show_data = new System.Windows.Forms.CheckBox();
            this.bt_save = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // chart1
            // 
            chartArea2.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea2);
            legend2.Name = "Legend1";
            this.chart1.Legends.Add(legend2);
            this.chart1.Location = new System.Drawing.Point(138, 47);
            this.chart1.Name = "chart1";
            series2.ChartArea = "ChartArea1";
            series2.Legend = "Legend1";
            series2.Name = "Series1";
            this.chart1.Series.Add(series2);
            this.chart1.Size = new System.Drawing.Size(300, 300);
            this.chart1.TabIndex = 0;
            this.chart1.Text = "chart1";
            this.chart1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.chart1_MouseMove);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 64);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(101, 44);
            this.button1.TabIndex = 1;
            this.button1.Text = "plotChart 1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_start
            // 
            this.bt_start.Location = new System.Drawing.Point(12, 512);
            this.bt_start.Name = "bt_start";
            this.bt_start.Size = new System.Drawing.Size(101, 44);
            this.bt_start.TabIndex = 2;
            this.bt_start.Text = "動畫 ST";
            this.bt_start.UseVisualStyleBackColor = true;
            this.bt_start.Click += new System.EventHandler(this.bt_start_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(138, 444);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(791, 267);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // comboBox1
            // 
            this.comboBox1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "Point = 0,        //     點狀圖類型。",
            "FastPoint = 1,        //     FastPoint 圖表類型。",
            "Bubble = 2,        //     泡泡圖類型。",
            "Line = 3,        //     折線圖類型。",
            "Spline = 4,        //     曲線圖類型。",
            "StepLine = 5,        //     StepLine 圖表類型。",
            "FastLine = 6,        //     FastLine 圖表類型。",
            "Bar = 7,        //     橫條圖類型。",
            "StackedBar = 8,        //     堆疊橫條圖類型。",
            "StackedBar100 = 9,        //     100% 堆疊橫條圖類型。",
            "Column = 10,        //     直條圖類型。",
            "StackedColumn = 11,        //     堆疊直條圖類型。",
            "StackedColumn100 = 12,        //     100% 堆疊直條圖類型。",
            "Area = 13,        //     區域圖表類型。",
            "SplineArea = 14,        //     曲線區域圖類型。",
            "StackedArea = 15,        //     堆疊區域圖類型。",
            "StackedArea100 = 16,        //     100% 堆疊區域圖類型。",
            "Pie = 17,        //     圓形圖類型。",
            "Doughnut = 18,        //     環圈圖類型。",
            "Stock = 19,        //     股票圖類型。",
            "Candlestick = 20,        //     K 線圖類型。",
            "Range = 21,        //     範圍圖類型。",
            "SplineRange = 22,        //     曲線範圍圖類型。",
            "RangeBar = 23,        //     範圍橫條圖類型。",
            "RangeColumn = 24,        //     範圍直條圖類型。",
            "Radar = 25,        //     雷達圖類型。",
            "Polar = 26,        //     極座標圖類型。",
            "ErrorBar = 27,        //     誤差長條圖類型。",
            "BoxPlot = 28,        //     盒狀圖類型。",
            "Renko = 29,        //     磚形圖類型。",
            "ThreeLineBreak = 30,        //     ThreeLineBreak 圖表類型。",
            "Kagi = 31,        //     Kagi 圖表類型。",
            "PointAndFigure = 32,        //     PointAndFigure 圖表類型。",
            "Funnel = 33,        //     漏斗圖類型。",
            "Pyramid = 34,        //     金字塔圖類型。"});
            this.comboBox1.Location = new System.Drawing.Point(138, 12);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(745, 29);
            this.comboBox1.TabIndex = 4;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(12, 622);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(101, 44);
            this.bt_clear.TabIndex = 5;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 210);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(101, 44);
            this.button4.TabIndex = 6;
            this.button4.Text = "plotChart 4";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(11, 263);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(101, 44);
            this.button5.TabIndex = 7;
            this.button5.Text = "plotChart 5";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(12, 317);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(101, 44);
            this.button6.TabIndex = 7;
            this.button6.Text = "plotChart 6";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(12, 369);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(101, 44);
            this.button7.TabIndex = 8;
            this.button7.Text = "plotChart 7";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(12, 14);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(101, 44);
            this.button0.TabIndex = 9;
            this.button0.Text = "plotChart 0";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 110);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(101, 44);
            this.button2.TabIndex = 10;
            this.button2.Text = "plotChart 2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 160);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(101, 44);
            this.button3.TabIndex = 11;
            this.button3.Text = "plotChart 3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // cb_show_data
            // 
            this.cb_show_data.AutoSize = true;
            this.cb_show_data.Location = new System.Drawing.Point(12, 680);
            this.cb_show_data.Name = "cb_show_data";
            this.cb_show_data.Size = new System.Drawing.Size(72, 16);
            this.cb_show_data.TabIndex = 12;
            this.cb_show_data.Text = "顯示資料";
            this.cb_show_data.UseVisualStyleBackColor = true;
            // 
            // bt_save
            // 
            this.bt_save.Location = new System.Drawing.Point(12, 562);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(101, 44);
            this.bt_save.TabIndex = 13;
            this.bt_save.Text = "Save";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(12, 431);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(101, 44);
            this.button8.TabIndex = 14;
            this.button8.Text = "plotChart 8 用滑鼠指線 顯示數值";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(953, 720);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.bt_save);
            this.Controls.Add(this.cb_show_data);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.bt_start);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.chart1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_start;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.CheckBox cb_show_data;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.Button button8;
    }
}

