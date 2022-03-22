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

工具箱空白處按右鍵/選擇項目/在.NET Framework頁箋下 按 瀏覽 選取ZedGraph.dll, 確定
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
            Draw_ZedGraph1();
        }

        void Draw_ZedGraph1()
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

        private void button2_Click(object sender, EventArgs e)
        {
            Draw_ZedGraph2();
        }

        void Draw_ZedGraph2()
        {
            #region 1、准备数据
            #endregion

            #region 2、图表样式
            //ZedGraphControl zedGraphControl1 = new ZedGraphControl();
            GraphPane myPane = zedGraphControl1.GraphPane;
            //zedGraphControl1.ContextMenuBuilder += MyContextMenuBuilder;   // 手动修改ZedGraphControl控件右击菜单为中文（添加引用ZedGraph.resources也可）
            // 图表
            zedGraphControl1.IsShowContextMenu = true;        // 显示右键菜单
            zedGraphControl1.IsShowCopyMessage = true;        // 复制图像时是否显示提示信息
            zedGraphControl1.IsShowHScrollBar = false;            // 横向滚动条
            zedGraphControl1.IsShowVScrollBar = false;            // 纵向滚动条
            zedGraphControl1.IsEnableZoom = false;                 // 缩放
            zedGraphControl1.IsEnableHZoom = false;              // 横向缩放
            zedGraphControl1.IsEnableVZoom = false;              // 纵向缩放
            zedGraphControl1.IsZoomOnMouseCenter = true;  // 使用滚轮时以鼠标所在点为中心进行缩放还是以图形中心进行缩放
            zedGraphControl1.IsShowCursorValues = true;        // 鼠标在图表上移动时是否显示鼠标所在点对应的坐标 默认为false
            zedGraphControl1.IsShowPointValues = true;          // 鼠标经过图表上的点时是否显示该点所对应的值 默认为false 
            myPane.Fill = new Fill(BackColor);     // 背景色与form窗口颜色一致
            myPane.Border = new Border(false, Color.Gray, 2.0F);    // 取消图表边框
            // 表格
            myPane.Chart.Fill = new Fill(Color.WhiteSmoke);  // 表格背景色
            // 图例
            Border border = new Border(false, Color.Black, 10);   // 取消图例边框
            myPane.Legend.Border = border;
            myPane.Legend.FontSpec.IsBold = false;
            myPane.Legend.FontSpec.Size = 14f;
            myPane.Legend.FontSpec.Family = "楷体";
            myPane.Legend.Fill = new Fill(BackColor);  // 背景色与form窗口颜色一致
            // 取消表格边框
            myPane.Chart.Border.IsVisible = false;//首先设置边框为无
            myPane.XAxis.MajorTic.IsOpposite = false;  //X轴对面轴大间隔为无
            myPane.XAxis.MinorTic.IsOpposite = false;  //X轴对面轴小间隔为无
            myPane.YAxis.MajorTic.IsOpposite = false;  //Y轴对面轴大间隔为无
            myPane.YAxis.MinorTic.IsOpposite = false;  //Y轴对面轴小间隔为无
            myPane.XAxis.Scale.Min = 0;
            myPane.XAxis.Scale.Max = 10;
            myPane.YAxis.Scale.Min = 0;
            myPane.YAxis.Scale.Max = 100;
            // 标题
            myPane.Title.Text = "函数曲线图";
            myPane.Title.FontSpec.IsBold = true;
            myPane.Title.FontSpec.Size = 20f;
            myPane.Title.FontSpec.Family = "楷体";
            myPane.Title.FontSpec.Fill = new Fill(BackColor);  // 背景色与form窗口颜色一致
            // X轴
            myPane.XAxis.Title.Text = "X";
            myPane.XAxis.Title.FontSpec.IsBold = true;
            myPane.XAxis.Title.FontSpec.Size = 14f;
            myPane.XAxis.Title.FontSpec.Family = "楷体";
            myPane.XAxis.Title.FontSpec.Fill = new Fill(BackColor);  // 背景色与form窗口颜色一致
            // Y轴
            myPane.YAxis.Title.Text = "Y";
            myPane.YAxis.Title.FontSpec.IsBold = true;
            myPane.YAxis.Title.FontSpec.Size = 14f;
            myPane.YAxis.Title.FontSpec.Family = "楷体";
            myPane.YAxis.Title.FontSpec.Fill = new Fill(BackColor);  // 背景色与form窗口颜色一致
            #endregion

            #region 3、画图
            // 曲线1
            PointPairList list1 = new PointPairList();
            for (int x = 0; x < 100; x++)
            {

                if (x % 1 == 0)
                {

                    list1.Add((double)x, (double)(x * x + 10));
                }
            }
            LineItem myCurve1 = myPane.AddCurve("Y = X * X + 10", list1, Color.Red, SymbolType.Default);
            // 曲线2
            PointPairList list2 = new PointPairList();
            for (int x = 0; x < 100; x++)
            {

                if (x % 1 == 0)
                {

                    list2.Add((double)x, (double)(x * 5 + 15));
                }
            }
            LineItem myCurve2 = myPane.AddCurve("Y = X * 5 +15", list2, Color.Red, SymbolType.Star);

            zedGraphControl1.AxisChange();
            #endregion
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Draw_ZedGraph3(zedGraphControl1);
        }

        //zedGraphControl1设置函数
        public void Draw_ZedGraph3(ZedGraphControl zgc)
        {
            GraphPane myPane = zgc.GraphPane;

            //设置图标标题和x、y轴标题

            myPane.Title.Text = "机票波动情况";
            myPane.XAxis.Title.Text = "波动日期";
            myPane.YAxis.Title.Text = "机票价格";

            //更改标题的字体
            FontSpec myFont = new FontSpec("Arial", 20, Color.Red, false, false, false);
            myPane.Title.FontSpec = myFont;
            myPane.XAxis.Title.FontSpec = myFont;
            myPane.YAxis.Title.FontSpec = myFont;
            // 造一些数据，PointPairList里有数据对x，y的数组
            Random y = new Random();
            PointPairList list1 = new PointPairList();
            for (int i = 0; i < 36; i++)
            {
                double x = i;
                //double y1 = 1.5 + Math.Sin((double)i * 0.2);
                double y1 = y.NextDouble() * 1000;
                list1.Add(x, y1); //添加一组数据
            }

            // 用list1生产一条曲线，标注是“东航”
            LineItem myCurve = myPane.AddCurve("东航", list1, Color.Red, SymbolType.Star);
            //填充图表颜色
            myPane.Fill = new Fill(Color.White, Color.FromArgb(200, 200, 255), 45.0f);
            //以上生成的图标X轴为数字，下面将转换为日期的文本
            string[] labels = new string[36];
            for (int i = 0; i < 36; i++)
            {
                labels[i] = System.DateTime.Now.AddDays(i).ToShortDateString();
            }
            myPane.XAxis.Scale.TextLabels = labels; //X轴文本取值
            myPane.XAxis.Type = AxisType.Text;   //X轴类型
            //画到zedGraphControl1控件中，此句必加
            zgc.AxisChange();
            Refresh();  //重绘控件

            //在图上点位标注数字的方法
            // 点位和标注的偏置
            const double offset = 10;
            // 为每个点加标注
            for (int i = 0; i < 36; i++)
            {
                PointPair pt = myCurve.Points[i];
                TextObj text = new TextObj(pt.Y.ToString("f2"), pt.X, pt.Y + offset, CoordType.AxisXYScale, AlignH.Left, AlignV.Center);
                text.ZOrder = ZOrder.A_InFront;
                // 隐藏标注的边框和填充
                text.FontSpec.Border.IsVisible = false;
                text.FontSpec.Fill.IsVisible = false;
                // 选择标注字体90°
                text.FontSpec.Angle = 90;
                myPane.GraphObjList.Add(text);
            }
            Refresh();  //重绘控件
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //繪製 柱狀圖
            this.zedGraphControl1.Location = new System.Drawing.Point(120, 20);
            this.zedGraphControl1.Name = "zedGraphControl1";
            this.zedGraphControl1.ScrollGrace = 0;
            this.zedGraphControl1.ScrollMaxX = 0;
            this.zedGraphControl1.ScrollMaxY = 0;
            this.zedGraphControl1.ScrollMaxY2 = 0;
            this.zedGraphControl1.ScrollMinX = 0;
            this.zedGraphControl1.ScrollMinY = 0;
            this.zedGraphControl1.ScrollMinY2 = 0;
            this.zedGraphControl1.Size = new System.Drawing.Size(800, 400);
            this.zedGraphControl1.TabIndex = 0;

            ShowChart1();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //繪製 柱狀圖
            this.zedGraphControl1.Location = new System.Drawing.Point(120, 20);
            this.zedGraphControl1.Name = "zedGraphControl1";
            this.zedGraphControl1.ScrollGrace = 0;
            this.zedGraphControl1.ScrollMaxX = 0;
            this.zedGraphControl1.ScrollMaxY = 0;
            this.zedGraphControl1.ScrollMaxY2 = 0;
            this.zedGraphControl1.ScrollMinX = 0;
            this.zedGraphControl1.ScrollMinY = 0;
            this.zedGraphControl1.ScrollMinY2 = 0;
            this.zedGraphControl1.Size = new System.Drawing.Size(800, 400);
            this.zedGraphControl1.TabIndex = 0;

            ShowChart2();

        }

        private void ShowChart1()
        {
            zedGraphControl1.GraphPane.CurveList.Clear();
            zedGraphControl1.GraphPane.GraphObjList.Clear();
            // clearing not teste 


            GraphPane myPane = zedGraphControl1.GraphPane;


            myPane.Title.Text = "消費者學歷統計"; //設計圖表的標題  
            myPane.XAxis.Title.Text = "學歷類型";//X軸標題  
            myPane.YAxis.Title.Text = "人數";//Y軸標題  
            //      myPane.XAxis.Type = ZedGraph.AxisType.Date; 
            // Date wont work in our case 


            PointPairList PPLa = new PointPairList();
            PointPairList PPLb = new PointPairList();
            PointPairList PPLc = new PointPairList();
            PointPairList PPLd = new PointPairList();


            for (int i = 1; i < 2; i++)
            {
                PPLa.Add(i, i + 3);
                PPLb.Add(i + 1, i + 4);
                PPLc.Add(i + 2, i + 5);
                PPLd.Add(i + 3, i + 6);
            }


            // dragged drawing baritems out of forloop 
            BarItem myBara = myPane.AddBar("A", PPLa, Color.Red);
            BarItem myBarb = myPane.AddBar("B", PPLb, Color.Blue);
            BarItem myBarc = myPane.AddBar("C", PPLc, Color.Gray);
            BarItem myBard = myPane.AddBar("D", PPLd, Color.Black);


            zedGraphControl1.AxisChange();
            zedGraphControl1.Refresh();//這句話非常重要，否則不會立即顯示 
        }


        //如需要橫座標顯示文字：

        private void ShowChart2()
        {
            zedGraphControl1.GraphPane.CurveList.Clear();
            zedGraphControl1.GraphPane.GraphObjList.Clear();
            // clearing not teste 


            GraphPane myPane = zedGraphControl1.GraphPane;
            // 畫圖面版標題  
            myPane.Title.Text = "收入統計";
            // 畫圖面版X標題  
            myPane.XAxis.Title.Text = "區域";


            myPane.XAxis.Scale.Min = 0;
            //初始化數據  
            PointPairList list = new PointPairList();
            PointPairList list2 = new PointPairList();
            PointPairList list3 = new PointPairList();


            for (int i = 0; i < 5; i++)////這裏的數量要和lable的一致，比如橫座標顯示了5個lable，這裏就要給5個 
            {
                list.Add(i, i + 1);
                list2.Add(i, i + 2);
                list3.Add(i, i + 3);
            }



            // 畫圖面版Y標題  
            myPane.YAxis.Title.Text = "銷售情況";
            //柱的畫筆  
            //    public BarItem AddBar(string 名稱, IPointList 數據, Color 顏色); 

            BarItem myCurve = myPane.AddBar("收入1", list, Color.Blue);
            BarItem myCurve1 = myPane.AddBar("收入2", list2, Color.Purple);
            BarItem myCurve2 = myPane.AddBar("收入3", list3, Color.YellowGreen);

            //myCurve.Bar.Fill = new Fill(Color.Blue, Color.White, Color.Blue);//漸變 
            // BarItem myCurve2 = myPane.AddBar("買農藥", list2, Color.Red); 
            // myCurve2.Bar.Fill = new Fill(Color.Red, Color.White, Color.Red); 
            //  BarItem myCurve3 = myPane.AddBar("買化肥", list3, Color.Green); 
            // myCurve3.Bar.Fill = new Fill(Color.Green, Color.White, Color.Green); 


            //myPane.XAxis.MajorTic.IsBetweenLabels = true; 
            //XAxis標註  
            string[] labels = { "產品1", "產品2", "產品3", "產品4", "產品5" };
            myPane.XAxis.Scale.TextLabels = labels;
            myPane.XAxis.Type = AxisType.Text;
            //圖區以外的顏色  
            // myPane.Fill = new Fill(Color.White, Color.FromArgb(200, 200, 255), 45.0f); 
            //背景顏色  
            // myPane.Chart.Fill = new Fill(Color.Red, Color.LightGoldenrodYellow, 45.0f); 


            zedGraphControl1.AxisChange();
            zedGraphControl1.Refresh();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            zedGraphControl1.GraphPane.CurveList.Clear();
            zedGraphControl1.GraphPane.GraphObjList.Clear();
            GraphPane myPane = zedGraphControl1.GraphPane;
            myPane.Title.Text = "统计消费者";  //设计图表的标题
            myPane.XAxis.Title.Text = "男/女"; //X轴标题
            myPane.YAxis.Title.Text = "人数"; //Y轴标题          
            PointPairList PPLa = new PointPairList();
            PointPairList PPLb = new PointPairList();
            for (int i = 1; i < 2; i++)
            {
                PPLa.Add(i, i + 3);
                PPLb.Add(i + 1, i + 4);
            }
            BarItem myBara = myPane.AddBar("A", PPLa, System.Drawing.Color.Red);
            BarItem myBarb = myPane.AddBar("B", PPLb, System.Drawing.Color.Blue);
            zedGraphControl1.AxisChange();
            zedGraphControl1.Refresh();//这句话非常重要，否则不会立即显示

        }
    }
}


