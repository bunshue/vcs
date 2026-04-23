using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

using AForge;
using AForge.Controls;
using AForge.Genetic;

namespace vcs_AForgeTest1
{
    public partial class Form1 : Form
    {
        private double[,] data = null;
        private UserFunction userFunction = new UserFunction();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            chart1.AddDataSeries("data", Color.Red, Chart.SeriesType.Dots, 5);
            chart1.AddDataSeries("solution", Color.Blue, Chart.SeriesType.Line, 1);

            // add data series to chart
            chart2.AddDataSeries("function", Color.Red, Chart.SeriesType.Line, 1);
            chart2.AddDataSeries("solution", Color.Blue, Chart.SeriesType.Dots, 5);
            UpdateChart();

            this.listView1.FullRowSelect = true;
            this.listView1.GridLines = true;
            this.listView1.View = System.Windows.Forms.View.Details;

            //設定欄位
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "X";
            ch1.Width = 100;
            listView1.Columns.Add(ch1);

            ColumnHeader ch2 = new ColumnHeader();
            ch2.Text = "Y";
            ch2.Width = 100;
            listView1.Columns.Add(ch2);
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 9);

            listView1.Size = new Size(400, 300);
            listView1.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 0);

            chart1.Size = new Size(400, 200);
            chart1.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 5);
            chart2.Size = new Size(400, 200);
            chart2.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 8);

            pictureBox1.Size = new Size(100, 100);
            pictureBox1.Location = new System.Drawing.Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 800);
            richTextBox1.Location = new System.Drawing.Point(x_st + dx * 4 + 30, y_st + dy * 0);
            bt_clear.Location = new System.Drawing.Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1300, 1050);
            this.Text = "vcs_AForgeTest1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string csv_filename1 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\AForge.NET Framework-2.2.5\Samples\vcs_AForgeTest1\vcs_AForgeTest1\data\sample1.csv";
            string csv_filename2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\AForge.NET Framework-2.2.5\Samples\vcs_AForgeTest1\vcs_AForgeTest1\data\sample2.csv";

            StreamReader reader = null;
            // read maximum 50 points
            float[,] tempData = new float[50, 2];
            float minX = float.MaxValue;
            float maxX = float.MinValue;

            try
            {
                // open selected file
                reader = File.OpenText(csv_filename2);
                string str = null;
                int i = 0;

                // read the data
                while ((i < 50) && ((str = reader.ReadLine()) != null))
                {
                    string[] strs = str.Split(';');
                    if (strs.Length == 1)
                    {
                        strs = str.Split(',');
                    }
                    // parse X
                    tempData[i, 0] = float.Parse(strs[0]);
                    tempData[i, 1] = float.Parse(strs[1]);

                    // search for min value
                    if (tempData[i, 0] < minX)
                    {
                        minX = tempData[i, 0];
                    }
                    // search for max value
                    if (tempData[i, 0] > maxX)
                    {
                        maxX = tempData[i, 0];
                    }
                    i++;
                }

                // allocate and set data
                data = new double[i, 2];
                Array.Copy(tempData, 0, data, 0, i * 2);
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
                {
                    reader.Close();
                }
            }

            // update list and chart1
            UpdateDataListView();
            chart1.RangeX = new Range(minX, maxX);
            chart1.UpdateDataSeries("data", data);
            chart1.UpdateDataSeries("solution", null);
        }


        // Update data in list view
        private void UpdateDataListView()
        {
            // remove all current records
            listView1.Items.Clear();
            // add new records
            for (int i = 0, n = data.GetLength(0); i < n; i++)
            {
                listView1.Items.Add(data[i, 0].ToString());
                listView1.Items[i].SubItems.Add(data[i, 1].ToString());
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            userFunction.Range = new Range(userFunction.Range.Min + 5, userFunction.Range.Max - 5);
            UpdateChart();
        }

        private void UpdateChart()
        {
            // update chart range
            chart2.RangeX = userFunction.Range;

            double[,] data = null;

            if (chart2.RangeX.Length > 0)
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
            chart2.UpdateDataSeries("function", data);
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
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



//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/



