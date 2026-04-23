// 1D Optimization using Genetic Algorithms
// AForge.NET framework
// http://www.aforgenet.com/framework/
//
// Copyright ?AForge.NET, 2006-2011
// contacts@aforgenet.com
//

using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

using AForge;
using AForge.Genetic;
using AForge.Controls;

namespace Optimization1D
{
    /// <summary>
    /// Summary description for MainForm.
    /// </summary>
    public class MainForm : System.Windows.Forms.Form
    {
        private AForge.Controls.Chart chart;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox minXBox;
        private System.Windows.Forms.TextBox maxXBox;
        private System.Windows.Forms.Label label2;
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.Container components = null;

        private UserFunction userFunction = new UserFunction();

        private RichTextBox richTextBox1;

        // Constructor
        public MainForm()
        {
            //
            // Required for Windows Form Designer support
            //
            InitializeComponent();

            // add data series to chart
            chart.AddDataSeries("function", Color.Red, Chart.SeriesType.Line, 1);
            chart.AddDataSeries("solution", Color.Blue, Chart.SeriesType.Dots, 5);
            UpdateChart();
        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.chart = new AForge.Controls.Chart();
            this.label1 = new System.Windows.Forms.Label();
            this.minXBox = new System.Windows.Forms.TextBox();
            this.maxXBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // chart
            // 
            this.chart.Location = new System.Drawing.Point(12, 12);
            this.chart.Name = "chart";
            this.chart.RangeX = ((AForge.Range)(resources.GetObject("chart.RangeX")));
            this.chart.RangeY = ((AForge.Range)(resources.GetObject("chart.RangeY")));
            this.chart.Size = new System.Drawing.Size(500, 405);
            this.chart.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(10, 437);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 15);
            this.label1.TabIndex = 3;
            this.label1.Text = "Range:";
            // 
            // minXBox
            // 
            this.minXBox.Location = new System.Drawing.Point(60, 434);
            this.minXBox.Name = "minXBox";
            this.minXBox.Size = new System.Drawing.Size(50, 22);
            this.minXBox.TabIndex = 3;
            this.minXBox.TextChanged += new System.EventHandler(this.minXBox_TextChanged);
            // 
            // maxXBox
            // 
            this.maxXBox.Location = new System.Drawing.Point(130, 434);
            this.maxXBox.Name = "maxXBox";
            this.maxXBox.Size = new System.Drawing.Size(50, 22);
            this.maxXBox.TabIndex = 4;
            this.maxXBox.TextChanged += new System.EventHandler(this.maxXBox_TextChanged);
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(115, 437);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(8, 18);
            this.label2.TabIndex = 3;
            this.label2.Text = "-";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(689, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(423, 638);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // MainForm
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(1124, 662);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.chart);
            this.Controls.Add(this.minXBox);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.maxXBox);
            this.Controls.Add(this.label2);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "1D Optimization using Genetic Algorithms";
            this.Closing += new System.ComponentModel.CancelEventHandler(this.MainForm_Closing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.Run(new MainForm());
        }

        private void MainForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
        }

        // Update chart
        private void UpdateChart()
        {
            // update chart range
            chart.RangeX = userFunction.Range;

            double[,] data = null;

            if (chart.RangeX.Length > 0)
            {
                // prepare data
                data = new double[501, 2];

                double minX = userFunction.Range.Min;
                double length = userFunction.Range.Length;

                for (int i = 0; i <= 500; i++)
                {
                    data[i, 0] = minX + length * i / 500;
                    data[i, 1] = userFunction.OptimizationFunction(data[i, 0]);
                }
            }

            // update chart series
            chart.UpdateDataSeries("function", data);
        }

        // Update min value
        private void minXBox_TextChanged(object sender, System.EventArgs e)
        {
            try
            {
                userFunction.Range = new Range(float.Parse(minXBox.Text), userFunction.Range.Max);
                UpdateChart();
            }
            catch
            {
            }
        }

        // Update max value
        private void maxXBox_TextChanged(object sender, System.EventArgs e)
        {
            try
            {
                userFunction.Range = new Range(userFunction.Range.Min, float.Parse(maxXBox.Text));
                UpdateChart();
            }
            catch
            {
            }
        }

        // Delegates to enable async calls for setting controls properties
        private delegate void EnableCallback(bool enable);

        // Enable/disale controls (safe for threading)
        private void EnableControls(bool enable)
        {
            if (InvokeRequired)
            {
                EnableCallback d = new EnableCallback(EnableControls);
                Invoke(d, new object[] { enable });
            }
            else
            {
                minXBox.Enabled = enable;
                maxXBox.Enabled = enable;
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }
    }

    // Function to optimize
    public class UserFunction : OptimizationFunction1D
    {
        public UserFunction() : base(new Range(0, 255)) { }

        public override double OptimizationFunction(double x)
        {
            return Math.Cos(x / 23) * Math.Sin(x / 50) + 2;
        }
    }
}
