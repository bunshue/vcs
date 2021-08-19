using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Windows.Forms.DataVisualization.Charting;  //for Chart

namespace vcs_Draw_Trigonometry2
{
    public partial class Form1 : Form
    {
        //繪圖類別
        public class RealtimeChart
        {
            private Chart chart1 = null;
            private int chartWidth = 640*3/4;
            private int chartHeight = 480*3/4;
            private string nameAxisX = "X軸標題";
            private string nameAxisY = "Y軸標題";

            public RealtimeChart()
            {
                chart1 = new Chart();

                ChartArea ctArea = new ChartArea();
                Legend legend = new Legend();
                Series series = new Series();

                chart1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(243)))), ((int)(((byte)(223)))), ((int)(((byte)(193)))));
                chart1.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;
                chart1.BorderlineColor = System.Drawing.Color.FromArgb(((int)(((byte)(181)))), ((int)(((byte)(64)))), ((int)(((byte)(1)))));
                chart1.BorderlineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
                chart1.BorderlineWidth = 2;
                chart1.BorderSkin.SkinStyle = System.Windows.Forms.DataVisualization.Charting.BorderSkinStyle.Emboss;
                chart1.Location = new System.Drawing.Point(450, 150);
                chart1.Name = "chart1";
                chart1.Size = new System.Drawing.Size(chartWidth, chartHeight);
                chart1.TabIndex = 1;
                chart1.Dock = System.Windows.Forms.DockStyle.None;

                ctArea.Area3DStyle.Inclination = 15;
                ctArea.Area3DStyle.IsClustered = true;
                ctArea.Area3DStyle.IsRightAngleAxes = false;
                ctArea.Area3DStyle.Perspective = 10;
                ctArea.Area3DStyle.Rotation = 10;
                ctArea.Area3DStyle.WallWidth = 0;
                ctArea.AxisX.IsLabelAutoFit = false;
                ctArea.AxisX.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                ctArea.AxisX.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MajorGrid.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MinorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Dash;
                ctArea.AxisX.Title = nameAxisX;
                ctArea.AxisY.IsLabelAutoFit = false;
                ctArea.AxisY.LabelStyle.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                ctArea.AxisY.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.MajorGrid.LineColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.Maximum = 5000D;
                ctArea.AxisY.Minimum = 0D;
                ctArea.AxisY.Title = nameAxisY;
                ctArea.BackColor = System.Drawing.Color.OldLace;
                ctArea.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.TopBottom;
                ctArea.BackSecondaryColor = System.Drawing.Color.White;
                ctArea.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.BorderDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.Solid;
                ctArea.Name = "Default";
                ctArea.ShadowColor = System.Drawing.Color.Transparent;
                chart1.ChartAreas.Add(ctArea);

                legend.BackColor = System.Drawing.Color.Transparent;
                legend.Enabled = false;
                legend.Font = new System.Drawing.Font("Trebuchet MS", 8.25F, System.Drawing.FontStyle.Bold);
                legend.IsTextAutoFit = false;
                legend.Name = "Default";
                chart1.Legends.Add(legend);

                series.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(180)))), ((int)(((byte)(26)))), ((int)(((byte)(59)))), ((int)(((byte)(105)))));
                series.ChartArea = "Default";
                series.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
                series.Legend = "Default";
                series.Name = "Default";
                chart1.Series.Add(series);
            }

            public Chart GetChart
            {
                get { return chart1; }
            }
        }

        private int pointIndex = 0;
        Chart chart1 = new RealtimeChart().GetChart;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //this.pictureBox1.Invalidate();



            // Define some variables
            int numberOfPointsInChart = 15;
            int numberOfPointsAfterRemoval = 15;

            // Simulate adding new data points
            int x = pointIndex + 1;
            int y = (int)(2500 * Math.Sin(Math.PI * x * 40 / 180) + 2500);

            chart1.Series[0].Points.AddXY(x, y);
            ++pointIndex;

            // Adjust Y & X axis scale
            chart1.ResetAutoValues();
            if (chart1.ChartAreas["Default"].AxisX.Maximum < pointIndex)
            {
                chart1.ChartAreas["Default"].AxisX.Maximum = pointIndex;
            }

            // Keep a constant number of points by removing them from the left
            while (chart1.Series[0].Points.Count > numberOfPointsInChart)
            {
                // Remove data points on the left side
                while (chart1.Series[0].Points.Count > numberOfPointsAfterRemoval)
                {
                    chart1.Series[0].Points.RemoveAt(0);
                }

                // Adjust X axis scale
                chart1.ChartAreas["Default"].AxisX.Minimum = pointIndex - numberOfPointsAfterRemoval;
                chart1.ChartAreas["Default"].AxisX.Maximum = chart1.ChartAreas["Default"].AxisX.Minimum + numberOfPointsInChart;
            }

            // Redraw chart
            chart1.Invalidate();



        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void DrawCircle(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);
            // Draw the circle
            g.DrawEllipse(p, center.X - radius, center.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }

        double angle = 0;
        int x_st = 100;
        int y_st = 100;
        int L = 170;
        int cx = 200;
        int cy = 200;
        PointF pt = new PointF();

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawLine(new Pen(Color.Black, 2), cx - 200, cy, cx + 200, cy);
            e.Graphics.DrawLine(new Pen(Color.Black, 2), cx, cy - 200, cx, cy + 200);

            pt = new PointF(cx, cy);
            //e.Graphics.DrawEllipse(new Pen(Color.Red, 3), x_st, y_st, L, L);
            DrawCircle(e.Graphics, pt, L, 3, Color.Yellow);

            x_st = cx + (int)(L * cosd(angle));
            y_st = cy + (int)(L * sind(angle));

            e.Graphics.DrawLine(new Pen(Color.Black, 2), 200, y_st, x_st, y_st);
            e.Graphics.DrawLine(new Pen(Color.Black, 2), x_st, 200, x_st, y_st);


            pt = new PointF(x_st, y_st);
            FillCircle(e.Graphics, pt, 10, Color.Red);

            angle -= 6;




        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開始
            chart1 = new RealtimeChart().GetChart;
            timer1.Enabled = true;
            this.Controls.Add(chart1);
            chart1.BringToFront();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //停止
            timer1.Enabled = false;
            this.Controls.Remove(chart1);

        }
    }
}
