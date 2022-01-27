using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
參考/加入參考/瀏覽 選取ZedGraph.dll

工具箱空白處按右鍵/選擇項目/瀏覽 選取ZedGraph.dll, 確定
工具箱內出現ZedGraphControl控件
*/

/*
ZedGraph為Open Source的軟體，可從SourceForge下載最新的軟體
http://sourceforge.net/projects/zedgraph/files/zedgraph%20documentation/
ZedGraph的類別說明文件
http://zedgraph.sourceforge.net/documentation/default.html
*/

using ZedGraph;

namespace vcs_ZedGraph
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            double[] speed = new double[] { 4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25 };
            double[] dist = new double[] { 2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85 };
            GraphPane pane = PlotInitialize(zedGraphControl1);
            PlotPoint(speed, dist, pane);
            PlotFinalize(zedGraphControl1);
        }

        private GraphPane PlotInitialize(ZedGraphControl zgc)
        {
            /* Plot initialization */

            // Set to show point values
            //zgc.IsShowPointValues = true;
            //zgc.PointValueFormat = "0.000";
            //zgc.PointDateFormat = "d";

            // Get a reference to the GraphPane
            GraphPane myPane = zgc.GraphPane;

            // Clear all Curves
            myPane.CurveList.Clear();

            // Set Pane Color
            myPane.Fill.Color = Color.AliceBlue;// single color
            //myPane.Fill = new Fill(Color.White, Color.FromArgb(200, 200, 255), 45.0f);// gradient color

            // Set Chart Color
            myPane.Chart.Fill = new Fill(Color.White, Color.Azure, 45.0f);//gradient color

            // Set Pane Border
            myPane.Border.Color = Color.Silver;
            myPane.Border.Width = 1;

            // Set Chart Border
            myPane.Chart.Border.Color = Color.Blue;
            myPane.Chart.Border.Width = 1;

            // Set X-axis Label Angle
            myPane.XAxis.Scale.FontSpec.Angle = 270;

            // Set X-axis Label Type
            myPane.XAxis.Type = AxisType.Text;

            // Set X-axis Label Font and Size
            myPane.XAxis.Scale.FontSpec.Family = "Arial, Narrow";
            myPane.XAxis.Scale.FontSpec.Size = 10;

            // Set Y-axis Label Font and Size
            myPane.XAxis.Scale.FontSpec.Family = "Arial, Narrow";
            myPane.YAxis.Scale.FontSpec.Size = 10;

            // Set Title,X,Y-axis AntiAlias
            myPane.Title.FontSpec.Family = "Arial, Narrow";
            myPane.Title.FontSpec.IsAntiAlias = true;
            myPane.XAxis.Title.FontSpec.IsAntiAlias = true;
            myPane.YAxis.Title.FontSpec.IsAntiAlias = true;
            myPane.XAxis.Scale.FontSpec.IsAntiAlias = true;
            myPane.YAxis.Scale.FontSpec.IsAntiAlias = true;

            return myPane;
        }

        private void PlotPoint(double[] x, double[] y, GraphPane myPane)
        {
            PointPairList points = new PointPairList();
            points.Add(x, y);

            LineItem line = myPane.AddCurve("", points, Color.Black, SymbolType.Circle);
            line.Symbol.Size = 10;
            line.Symbol.Border.IsVisible = true;
            line.Symbol.Border.Color = Color.Red;
            line.Symbol.Border.Width = 2;
            line.Symbol.IsVisible = true;
            line.Symbol.Border.IsAntiAlias = true;
            line.Line.IsVisible = false;
            line.Symbol.Fill = new Fill(Color.Yellow);

            /* Pane properties setting */
            // Set Titles
            myPane.Title.Text = "Plot Point Series";
            myPane.XAxis.Title.Text = "Speed";
            myPane.YAxis.Title.Text = "Dist";

            // Set Footer
            TextObj testObj = new TextObj("ZedGraph 繪圖", 0.98, 0.98, CoordType.PaneFraction, AlignH.Right, AlignV.Bottom);
            testObj.FontSpec.Border.IsVisible = false;
            testObj.FontSpec.FontColor = Color.Red;
            testObj.FontSpec.Fill.Color = Color.Transparent;
            testObj.FontSpec.Size = 12;
            testObj.FontSpec.IsAntiAlias = true;
            myPane.GraphObjList.Add(testObj);

            //Change myPane properties if not use default settings
            myPane.XAxis.Scale.FontSpec.Angle = 0;
            myPane.XAxis.Type = AxisType.Linear;
        }

        private void PlotFinalize(ZedGraphControl zgc)
        {
            //SetSize();
            zgc.AxisChange();
            zgc.Refresh();
        }

        private void SetSize()
        {
            zedGraphControl1.Location = new Point(10, 10);
            // Leave a small margin around the outside of the control
            zedGraphControl1.Size = new Size(ClientRectangle.Width - 20, ClientRectangle.Height - 20);
        }
    }
}
