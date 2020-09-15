namespace vcs_test_all_11_Chart1
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend3 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series3 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.button3 = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // chart1
            // 
            chartArea3.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea3);
            legend3.Name = "Legend1";
            this.chart1.Legends.Add(legend3);
            this.chart1.Location = new System.Drawing.Point(136, 73);
            this.chart1.Name = "chart1";
            series3.ChartArea = "ChartArea1";
            series3.Legend = "Legend1";
            series3.Name = "Series1";
            this.chart1.Series.Add(series3);
            this.chart1.Size = new System.Drawing.Size(622, 299);
            this.chart1.TabIndex = 0;
            this.chart1.Text = "chart1";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(101, 44);
            this.button1.TabIndex = 1;
            this.button1.Text = "Draw";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(13, 146);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(101, 44);
            this.button2.TabIndex = 2;
            this.button2.Text = "動畫 ST";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(13, 419);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(745, 204);
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
            this.comboBox1.Location = new System.Drawing.Point(136, 12);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(622, 29);
            this.comboBox1.TabIndex = 4;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 274);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(101, 44);
            this.button3.TabIndex = 5;
            this.button3.Text = "Clear";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(893, 647);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.chart1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Timer timer1;
    }
}

