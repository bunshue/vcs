// Time Series Prediction using Genetic Programming and Gene Expression Programming
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
using System.IO;

using AForge;
using AForge.Genetic;
using AForge.Controls;

namespace TimeSeries
{
    /// <summary>
    /// Summary description for Form1.
    /// </summary>
    public class MainForm : System.Windows.Forms.Form
    {
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ListView dataList;
        private System.Windows.Forms.ColumnHeader yColumnHeader;
        private System.Windows.Forms.Button loadDataButton;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.ComponentModel.IContainer components;
        private System.Windows.Forms.GroupBox groupBox2;
        private AForge.Controls.Chart chart;
        private System.Windows.Forms.ColumnHeader estimatedYColumnHeader;
        private System.Windows.Forms.ToolTip toolTip;

        private double[] data = null;
        private double[,] dataToShow = null;

        private int populationSize = 100;
        private int iterations = 1000;
        private int windowSize = 5;
        private int predictionSize = 1;
        private int selectionMethod = 0;
        private int functionsSet = 0;
        private int geneticMethod = 0;

        private int headLength = 20;

        private double[,] windowDelimiter = new double[2, 2] { { 0, 0 }, { 0, 0 } };
        private RichTextBox richTextBox1;
        private double[,] predictionDelimiter = new double[2, 2] { { 0, 0 }, { 0, 0 } };

        // Constructor
        public MainForm()
        {
            //
            // Required for Windows Form Designer support
            //
            InitializeComponent();

            //
            chart.AddDataSeries("data", Color.Red, Chart.SeriesType.Dots, 5);
            chart.AddDataSeries("solution", Color.Blue, Chart.SeriesType.Line, 1);
            chart.AddDataSeries("window", Color.LightGray, Chart.SeriesType.Line, 1, false);
            chart.AddDataSeries("prediction", Color.Gray, Chart.SeriesType.Line, 1, false);
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.dataList = new System.Windows.Forms.ListView();
            this.yColumnHeader = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.estimatedYColumnHeader = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.loadDataButton = new System.Windows.Forms.Button();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.chart = new AForge.Controls.Chart();
            this.toolTip = new System.Windows.Forms.ToolTip(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.dataList);
            this.groupBox1.Controls.Add(this.loadDataButton);
            this.groupBox1.Location = new System.Drawing.Point(10, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(254, 438);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Data";
            // 
            // dataList
            // 
            this.dataList.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.yColumnHeader,
            this.estimatedYColumnHeader});
            this.dataList.FullRowSelect = true;
            this.dataList.GridLines = true;
            this.dataList.Location = new System.Drawing.Point(10, 23);
            this.dataList.Name = "dataList";
            this.dataList.Size = new System.Drawing.Size(238, 364);
            this.dataList.TabIndex = 1;
            this.dataList.UseCompatibleStateImageBehavior = false;
            this.dataList.View = System.Windows.Forms.View.Details;
            // 
            // yColumnHeader
            // 
            this.yColumnHeader.Text = "Y:Real";
            this.yColumnHeader.Width = 70;
            // 
            // estimatedYColumnHeader
            // 
            this.estimatedYColumnHeader.Text = "Y:Estimated";
            this.estimatedYColumnHeader.Width = 70;
            // 
            // loadDataButton
            // 
            this.loadDataButton.Location = new System.Drawing.Point(10, 398);
            this.loadDataButton.Name = "loadDataButton";
            this.loadDataButton.Size = new System.Drawing.Size(75, 27);
            this.loadDataButton.TabIndex = 1;
            this.loadDataButton.Text = "&Load";
            this.loadDataButton.Click += new System.EventHandler(this.loadDataButton_Click);
            // 
            // openFileDialog
            // 
            this.openFileDialog.Filter = "CSV (Comma delimited) (*.csv)|*.csv";
            this.openFileDialog.Title = "Select data file";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.chart);
            this.groupBox2.Location = new System.Drawing.Point(270, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(300, 438);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Function";
            // 
            // chart
            // 
            this.chart.Location = new System.Drawing.Point(10, 23);
            this.chart.Name = "chart";
            this.chart.RangeX = ((AForge.Range)(resources.GetObject("chart.RangeX")));
            this.chart.RangeY = ((AForge.Range)(resources.GetObject("chart.RangeY")));
            this.chart.Size = new System.Drawing.Size(280, 404);
            this.chart.TabIndex = 0;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(782, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(447, 501);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // MainForm
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(1241, 546);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "Time Series Prediction using Genetic Programming and Gene Expression Programming";
            this.Closing += new System.ComponentModel.CancelEventHandler(this.MainForm_Closing);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

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

        // Delegates to enable async calls for setting controls properties
        private delegate void SetTextCallback(System.Windows.Forms.Control control, string text);
        private delegate void AddSubItemCallback(System.Windows.Forms.ListView control, int item, string subitemText);

        // Thread safe updating of control's text property
        private void SetText(System.Windows.Forms.Control control, string text)
        {
            if (control.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(SetText);
                Invoke(d, new object[] { control, text });
            }
            else
            {
                control.Text = text;
            }
        }

        // Thread safe adding of subitem to list control
        private void AddSubItem(System.Windows.Forms.ListView control, int item, string subitemText)
        {
            if (control.InvokeRequired)
            {
                AddSubItemCallback d = new AddSubItemCallback(AddSubItem);
                Invoke(d, new object[] { control, item, subitemText });
            }
            else
            {
                control.Items[item].SubItems.Add(subitemText);
            }
        }

        private void MainForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
        }

        // ∂}±“.csv¿…
        private void loadDataButton_Click(object sender, System.EventArgs e)
        {
            openFileDialog.InitialDirectory = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..\Data Samples\"));
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                StreamReader reader = null;
                // read maximum 50 points
                double[] tempData = new double[50];

                try
                {
                    // open selected file
                    reader = File.OpenText(openFileDialog.FileName);
                    string str = null;
                    int i = 0;

                    // read the data
                    while ((i < 50) && ((str = reader.ReadLine()) != null))
                    {
                        // parse the value
                        tempData[i] = double.Parse(str);

                        i++;
                    }

                    // allocate and set data
                    data = new double[i];
                    dataToShow = new double[i, 2];
                    Array.Copy(tempData, 0, data, 0, i);
                    for (int j = 0; j < i; j++)
                    {
                        dataToShow[j, 0] = j;
                        dataToShow[j, 1] = data[j];
                    }
                }
                catch (Exception)
                {
                    MessageBox.Show("Failed reading the file", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                finally
                {
                    // close file
                    if (reader != null)
                        reader.Close();
                }

                // update list and chart
                UpdateDataListView();
                chart.RangeX = new Range(0, data.Length - 1);
                chart.UpdateDataSeries("data", dataToShow);
                chart.UpdateDataSeries("solution", null);
                // set delimiters
                UpdateDelimiters();

            }
        }

        // Update delimiters on the chart
        private void UpdateDelimiters()
        {
            // window delimiter
            windowDelimiter[0, 0] = windowDelimiter[1, 0] = windowSize;
            windowDelimiter[0, 1] = chart.RangeY.Min;
            windowDelimiter[1, 1] = chart.RangeY.Max;
            chart.UpdateDataSeries("window", windowDelimiter);
            // prediction delimiter
            predictionDelimiter[0, 0] = predictionDelimiter[1, 0] = data.Length - 1 - predictionSize;
            predictionDelimiter[0, 1] = chart.RangeY.Min;
            predictionDelimiter[1, 1] = chart.RangeY.Max;
            chart.UpdateDataSeries("prediction", predictionDelimiter);
        }

        // Update data in list view
        private void UpdateDataListView()
        {
            // remove all current records
            dataList.Items.Clear();
            // add new records
            for (int i = 0, n = data.GetLength(0); i < n; i++)
            {
                dataList.Items.Add(data[i].ToString());
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

                loadDataButton.Enabled = enable;
            }
        }

        // Clear current solution
        private void ClearSolution()
        {
            // remove solution form chart
            chart.UpdateDataSeries("solution", null);

            // remove it from data list view
            for (int i = 0, n = dataList.Items.Count; i < n; i++)
            {
                if (dataList.Items[i].SubItems.Count > 1)
                    dataList.Items[i].SubItems.RemoveAt(1);
            }
        }

        private void startButton_Click(object sender, System.EventArgs e)
        {
            ClearSolution();
        }

        private void stopButton_Click(object sender, System.EventArgs e)
        {
        }
    }
}
