using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports
using System.Windows.Forms.DataVisualization;
using System.Windows.Forms.DataVisualization.Charting;  // for Series, Chart  參考/加入參考/.NET/System.Windows.Forms.DataVisualization

//參考： http://wahahastudynote.blogspot.com/2013/04/c-realtime.html
//用 C# 建立 Realtime 圖表 
//加入參考： 參考/加入參考/.NET/System.Windows.Forms.DataVisualization

namespace vcs_Chart2
{
    public partial class Form1 : Form
    {
        int W = 720;
        int H = 400;

        //兩種圖表比較
        Chart chart1 = new Chart();
        Chart chart2 = new RealtimeChart().GetChart;
        Series series00 = new Series();  // 一般chart
        Series series10 = new Series();  // realtime-chart

        //量測溫度 A:ims B:demo

        private int pointIndexB = 0;
        Chart chart_temperature = new RealtimeChart().GetChart;  // 溫度偵測圖表

        //------------------------------------------------------------  # 60個

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int UART_BUF_LENGTH = 5;

        bool flag_comport_ok = false;

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        string input = "";
        int flag_need_to_merge_data = 0;
        bool flag_read_connection_again = true;
        bool flag_show_cpu_temperatureA = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            draw_chart12();  // 一般chart 和 realtime-chart

            this.Controls.Add(chart1);
            chart1.Location = new Point(10, 10);
            chart1.ChartAreas[0].AxisY.Maximum = 150D;
            chart1.ChartAreas[0].AxisY.Minimum = -150D;

            this.Controls.Add(chart2);
            chart2.Location = new Point(10, 10 + 400 + 10);
            chart2.ChartAreas[0].AxisY.Maximum = 150D;
            chart2.ChartAreas[0].AxisY.Minimum = -150D;

            //------------------------------------------------------------  # 60個

            this.Controls.Add(chart_temperature);
            chart_temperature.Location = new Point(10 + 720 + 10, 10);
            chart_temperature.ChartAreas[0].AxisX.Title = "時間";
            chart_temperature.ChartAreas[0].AxisY.Title = "溫度";
            chart_temperature.ChartAreas[0].AxisY.Maximum = 80D;
            chart_temperature.ChartAreas[0].AxisY.Minimum = 50D;

            //------------------------------------------------------------  # 60個

            this.BackColor = Color.Yellow;

            bt_demo.PerformClick();
        }

        void show_item_location()
        {
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            chart1.Size = new Size(W, H);
            chart1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox_temperature.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.Size = new Size(W - 360, H - 100);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 100);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox_temperature.Size = new Size(140, 280);
            lb_temperature.Location = new Point(6, 20);
            lb_temperature.Text = "";
            x_st = 10;
            y_st = 60;
            bt_temperature_on.Location = new Point(x_st + 0, y_st);
            bt_temperature_off.Location = new Point(x_st + 0, y_st + 45 + 10);
            bt_comport.Location = new Point(x_st + 0 + 10, y_st + 45 + 10 + 45 + 10);
            bt_comport_disconnect.Location = new Point(x_st + 45 + 10 + 10, y_st + 45 + 10 + 45 + 10);
            bt_demo.Location = new Point(x_st + 0, y_st + 45 + 10 + 45 + 10 + 45 + 10);

            bt_temperature_on.Enabled = false;
            bt_temperature_off.Enabled = false;
            bt_comport_disconnect.Enabled = false;

            this.Size = new Size(1880, 870);
            this.Text = "vcs_Chart2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void draw_chart12()
        {
            //清除圖表
            chart1.Series.Clear();
            chart1.Titles.Clear();

            series00.ChartType = SeriesChartType.Line;  // 圖表種類
            chart1.Series.Add(series00);

            ChartArea ctArea = new ChartArea();
            chart1.ChartAreas.Add(ctArea);

            //------------------------------------------------------------  # 60個

            //清除圖表
            chart2.Series.Clear();
            chart2.Titles.Clear();

            series10.ChartType = SeriesChartType.Line;  // 圖表種類
            chart2.Series.Add(series10);
        }

        //------------------------------------------------------------  # 60個

        //繪圖類別
        public class RealtimeChart
        {
            private Chart chart1 = null;
            private string nameAxisX = "X軸標題";
            private string nameAxisY = "Y軸標題";

            public RealtimeChart()
            {
                chart1 = new Chart();

                ChartArea ctArea = new ChartArea();
                Legend legend = new Legend();
                Series series = new Series();

                chart1.BackColor = Color.FromArgb(((int)(((byte)(243)))), ((int)(((byte)(223)))), ((int)(((byte)(193)))));
                chart1.BackGradientStyle = GradientStyle.TopBottom;
                chart1.BorderlineColor = Color.FromArgb(((int)(((byte)(181)))), ((int)(((byte)(64)))), ((int)(((byte)(1)))));
                chart1.BorderlineDashStyle = ChartDashStyle.Solid;
                chart1.BorderlineWidth = 2;
                chart1.BorderSkin.SkinStyle = BorderSkinStyle.Emboss;
                chart1.Location = new Point(100, 100);
                chart1.Name = "chart1";
                chart1.Size = new Size(720, 400);
                chart1.TabIndex = 1;
                chart1.Dock = DockStyle.None;

                ctArea.Area3DStyle.Inclination = 15;
                ctArea.Area3DStyle.IsClustered = true;
                ctArea.Area3DStyle.IsRightAngleAxes = false;
                ctArea.Area3DStyle.Perspective = 10;
                ctArea.Area3DStyle.Rotation = 10;
                ctArea.Area3DStyle.WallWidth = 0;
                ctArea.AxisX.IsLabelAutoFit = false;
                ctArea.AxisX.LabelStyle.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);
                ctArea.AxisX.LineColor = Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MajorGrid.LineColor = Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisX.MinorGrid.LineDashStyle = ChartDashStyle.Dash;
                ctArea.AxisX.Title = nameAxisX;
                ctArea.AxisY.IsLabelAutoFit = false;
                ctArea.AxisY.LabelStyle.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);
                ctArea.AxisY.LineColor = Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.MajorGrid.LineColor = Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.AxisY.Maximum = 5000D;
                ctArea.AxisY.Minimum = 0D;
                ctArea.AxisY.Title = nameAxisY;
                ctArea.BackColor = Color.OldLace;
                ctArea.BackGradientStyle = GradientStyle.TopBottom;
                ctArea.BackSecondaryColor = Color.White;
                ctArea.BorderColor = Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
                ctArea.BorderDashStyle = ChartDashStyle.Solid;
                ctArea.Name = "Default";
                ctArea.ShadowColor = Color.Transparent;
                chart1.ChartAreas.Add(ctArea);

                legend.BackColor = Color.Transparent;
                legend.Enabled = false;
                legend.Font = new Font("Trebuchet MS", 8.25F, FontStyle.Bold);
                legend.IsTextAutoFit = false;
                legend.Name = "Default";
                chart1.Legends.Add(legend);

                series.BorderColor = Color.FromArgb(((int)(((byte)(180)))), ((int)(((byte)(26)))), ((int)(((byte)(59)))), ((int)(((byte)(105)))));
                series.ChartArea = "Default";
                series.ChartType = SeriesChartType.Line;
                series.Legend = "Default";
                series.Name = "Default";
                chart1.Series.Add(series);
            }

            public Chart GetChart
            {
                get { return chart1; }
            }
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        double x = 0;
        double y = 0;
        private void FunctionGenerator(out double xx, out double yy)
        {
            /* 正弦波
            xx = x;
            yy = 110 * sind(x);
            x += 26;
            */

            /*
            // 三角波
            xx = x;
            if ((x % 100) < 50)
                yy = x % 100;
            else
                yy = 100 - (x % 100);
            x += 10;
            */

            // 方波
            xx = x;
            if ((x % 100) < 50)
                yy = 50;
            else
                yy = 10;
            x += 10;


        }

        private const int POINTS_IN_AXIS = 36;      //製作動畫時X軸要保留的點數

        void update_chart12(double x, double y)
        {
            series00.Points.AddXY(x, y);  // AddXY 二維加入chart1, 一般Chart

            if (series00.Points.Count > POINTS_IN_AXIS)
                series00.Points.RemoveAt(0);

            //設定X軸邊界, 保存最新36點
            chart1.ChartAreas[0].AxisX.Minimum = series00.Points[0].XValue;
            chart1.ChartAreas[0].AxisX.Maximum = x;
            chart1.ChartAreas[0].AxisY.Minimum = -10;
            chart1.ChartAreas[0].AxisY.Maximum = 70;

            // Adjust Y & X axis scale
            //chart1.ResetAutoValues(); 有沒有看起來一樣

            //------------------------------  # 30個

            series10.Points.AddXY(x, y);  // AddXY 二維加入chart2, realtime_chart

            if (series10.Points.Count > POINTS_IN_AXIS)
                series10.Points.RemoveAt(0);

            //設定X軸邊界, 保存最新36點
            chart2.ChartAreas[0].AxisX.Minimum = series10.Points[0].XValue;
            chart2.ChartAreas[0].AxisX.Maximum = x;
            chart2.ChartAreas[0].AxisY.Minimum = -10;
            chart2.ChartAreas[0].AxisY.Maximum = 70;

            //------------------------------  # 30個

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double xx;
            double yy;
            FunctionGenerator(out xx, out yy);

            update_chart12(xx, yy);
        }

        //------------------------------------------------------------  # 60個

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private byte CalcCheckSum(byte[] pData, int len)
        {
            byte sum = 0x00;
            short ii = 0;
            for (ii = 0; ii < len; ii++)
            {
                sum += pData[ii];
            }
            sum = (byte)((sum ^ 0xFF) + 1);
            return sum;
        }

        public bool Send_IMS_Data0(byte cc, byte xx, byte yy, byte zz)  //directly send data
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);
            //richTextBox1.Text += "Send data:\t" + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n";
            //serialPort1.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
            return true;
        }

        public bool Send_IMS_Data(byte cc, byte xx, byte yy, byte zz)
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            /*
            if ((xx == 0x35) && (yy == 0x01))
            {
                richTextBox1.AppendText("xxxxxxxxxxx  [TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");
            }
            if ((xx == 0x35) && (yy == 0x0A))
            {
                richTextBox1.AppendText("yyyyyyyyyyy  [TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");
            }
            */

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            //serialPort1.Write(data, 0, data.Length);  改掉
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e03 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
            return true;
        }

        public bool Get_IMS_Data(byte xx, byte yy, byte zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xAA;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            serialPort1.Write(data, 0, data.Length);
            //flag_wait_receive_data = 1;

            return true;
        }

        private void bt_temperature_on_Click(object sender, EventArgs e)
        {
            if (flag_show_cpu_temperatureA == false)
            {
                flag_show_cpu_temperatureA = true;
                //溫度偵測 ON
                Send_IMS_Data(0xFF, 0xCC, 0xFF, 0xAA);
                lb_temperature.Text = "";
            }
        }

        private void bt_temperature_off_Click(object sender, EventArgs e)
        {
            if (flag_show_cpu_temperatureA == true)
            {
                flag_show_cpu_temperatureA = false;
                //溫度偵測 OFF
                Send_IMS_Data(0xFF, 0xCC, 0xFF, 0x55);
                lb_temperature.Text = "";
            }
        }

        private void timer_demo_Tick(object sender, EventArgs e)
        {
            Random r = new Random();
            int hh = r.Next(172, 175);
            int ll = r.Next(0, 256);
            //溫度偵測顯示
            int temperature_data = hh * 256 + ll;

            draw_chart_temperature(chart_temperature, temperature_data);
            //richTextBox1.Text += hh.ToString() + " " + ll.ToString() + "\n";
        }

        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            if (flag_comport_ok == true)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if ((BytesToRead > 0) && (BytesToRead < 21) && (BytesToRead != UART_BUF_LENGTH) && (flag_need_to_merge_data == 0))
                {
                    richTextBox1.Text += "t";
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer_tmp, 0, BytesToRead);
                    BytesToRead_tmp = BytesToRead;
                    flag_need_to_merge_data = 1;
                    //groupBox10.BackColor = Color.Red;
                    /*
                    richTextBox1.Text += "[debug] BytesToRead = " + BytesToRead.ToString() + ", backup data\tdata:\t";
                    for (int i = 0; i < BytesToRead_tmp; i++)
                    {
                        richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";
                    }
                    */
                    /*
                    for (int i = 0; i < BytesToRead_tmp; i++)
                    {
                        if (char.IsDigit((char)receive_buffer_tmp[i]) == true)
                        {
                            richTextBox1.Text += receive_buffer_tmp[i] + " ";
                        }
                        else
                            richTextBox1.Text += ". ";
                    }
                    */

                    //richTextBox1.Text += "\n";
                    return;
                }
                else if (BytesToRead > 0)
                {
                    if (flag_need_to_merge_data == 1)
                    {
                        flag_need_to_merge_data = 0;
                        if (BytesToRead == 21)
                        {
                            //directly use new data.....
                            //richTextBox1.Text += "[debug] BytesToRead = " + BytesToRead.ToString() + ", use new data\n";
                            //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                            serialPort1.Read(receive_buffer, 0, BytesToRead);
                        }
                        else
                        {
                            /*
                            richTextBox1.Text += "[debug] BytesToRead = " + BytesToRead.ToString() + ", restore data\n";
                            for (int i = 0; i < BytesToRead_tmp; i++)
                            {
                                receive_buffer[i] = receive_buffer_tmp[i];
                            }
                            */
                            //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                            serialPort1.Read(receive_buffer, BytesToRead_tmp, BytesToRead);
                            BytesToRead += BytesToRead_tmp;
                            //richTextBox1.Text += "[debug] BytesToRead_new = " + BytesToRead.ToString() + "\n";
                        }
                        if (BytesToRead == 21)
                        {
                            if (receive_buffer[0] == 0xA1)
                            {
                                //richTextBox1.Text += "red 111 here\n";
                                //groupBox10.BackColor = Color.Red;
                            }
                        }
                    }
                    else
                    {
                        //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        if (BytesToRead <= 2048)
                            serialPort1.Read(receive_buffer, 0, BytesToRead);
                        else
                        {
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                        }
                    }

                    //if (Comport_Mode == 0)  //iMS_Link mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                        {
                            SpyMonitorRX();
                        }
                        else if (BytesToRead <= 2048)
                        {
                            /*
                            //for UART debug
                            lb_uart_debug.Text += BytesToRead.ToString();
                            lb_uart_debug.Text += ' ';
                            */

                            //資料不是5拜，打印出來。
                            //richTextBox1.Text += "\n得到資料不是5拜 " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\t";

                            //input = "aa unknown data, len = " + BytesToRead.ToString() + "\n";
                            input = "";
                            if (BytesToRead >= 4)
                            {
                                //if (BytesToRead == 23)
                                {
                                    //MessageBox.Show("aaaa" + receive_buffer[BytesToRead - 5].ToString() + "aaaa" + receive_buffer[BytesToRead - 4].ToString() + "aaaa" + receive_buffer[BytesToRead - 3].ToString());
                                }

                                if ((receive_buffer[BytesToRead - 2] == 0x0a) && (receive_buffer[BytesToRead - 1] == 0x0d))
                                {
                                    //MessageBox.Show("xxxxxx");
                                    BytesToRead -= 1;
                                }

                            }
                            for (int i = 0; i < BytesToRead; i++)
                            {
                                if ((i >= 1) && (receive_buffer[i - 1] != 0x0a) && (receive_buffer[i] != 0x0d))
                                {
                                    //MessageBox.Show("got data : " + receive_buffer[i].ToString());
                                    input += (char)receive_buffer[i];
                                }
                                if (i == 0)
                                    input += (char)receive_buffer[i];
                                /*
                                if (i >= 1)
                                {
                                    if ((receive_buffer[i - 1] == 0x0a) && (receive_buffer[i] == 0x0d))
                                    {
                                        receive_buffer[i] = (byte)'~';
                                    }
                                }
                                input += (char)receive_buffer[i];
                                */
                            }
                            /*
                            richTextBox1.AppendText("[UN] : ");
                            for (int i = 0; i < BytesToRead; i++)
                            { 
                                richTextBox1.AppendText(((int)input[i]).ToString("X2") + " ");
                            }
                            richTextBox1.AppendText("\n");
                            */
                            //input += ", len = " + BytesToRead.ToString() + "\n";
                            richTextBox1.AppendText(input);     //打印一般文字訊息

                            richTextBox1.SelectionStart = richTextBox1.Text.Length;
                            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                            //Write_Log_File(input);
                        }
                        else
                        {
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                        }
                    }
                }
            }
        }

        private void SpyMonitorRX()
        {
            //richTextBox1.Text += "do SpyMonitorRX() len = " + BytesToRead.ToString() + "\n";

            string message = "";
            //if (BytesToRead == 5)
            {
                input = "";
                for (int i = 0; i < UART_BUF_LENGTH; i++)
                    input += (char)receive_buffer[i];

                byte[] data = new byte[5];

                data[0] = (byte)input[0];
                data[1] = (byte)input[1];
                data[2] = (byte)input[2];
                data[3] = (byte)input[3];
                data[4] = CalcCheckSum(data, 4);

                if (data[4] != input[4])
                {
                    /*
                    richTextBox1.AppendText("[checksum fail] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                        + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + ", abort\n");
                    */
                    if (flag_read_connection_again == false)
                        flag_read_connection_again = true;

                    return;
                }

                //richTextBox1.AppendText("[checksum] : " + ((int)input[4]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

                if (input[0] == 0xDD)
                {
                }
                else if (input[0] == 0xEE)
                {
                }
                else if (input[0] == 0xA1)
                {
                    if ((input[1] == 0xFF) && (input[2] == 0xFF) && (input[3] == 0xFF))
                    {
                        richTextBox1.Text += "aries says command fail.........\n";
                        //flag_wait_receive_data = 0;
                    }
                    else if ((input[1] == 0x11) && (input[2] == 0x52) && (input[3] == 0x00))
                    {
                        //richTextBox1.Text += "get uart response from aries egd system.\n";
                        //flag_comport_connection_ok = true;
                    }
                    else if (input[1] == 0xCD)
                    {
                        if (flag_show_cpu_temperatureA == true)
                        {
                            //溫度偵測顯示
                            int temperature_data = input[2] * 256 + input[3];

                            draw_chart_temperature(chart_temperature, temperature_data);
                            //richTextBox1.Text += ((int)input[2]).ToString() + " " + ((int)input[3]).ToString() + "\n";
                        }
                    }
                }
                else
                {
                    //資料是5拜，但是解不出所要的資訊。
                    message += "[bb unknown data1] : ";
                    for (int i = 0; i < 5; i++)
                    {
                        message += ((int)input[i]).ToString("X2") + " ";
                    }
                    message += Environment.NewLine;
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    //Write_Log_File(message);
                }
            }
            /*
            else
            {
                //資料是5拜，但是解不出所要的資訊。
                message += "[cc unknown data2] : ";
                for (int i = 0; i < 5; i++)
                {
                    message += ((int)input[i]).ToString("X2") + " ";
                }
                message += Environment.NewLine;
                richTextBox1.AppendText(message);
                //richTextBox1.AppendText(input);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
            */
        }

        private void bt_demo_Click(object sender, EventArgs e)
        {
            if (bt_demo.Text == "Demo啟動")
            {
                bt_demo.Text = "Demo停止";

                //溫度偵測 ON

                //demo
                timer_demo.Enabled = true;

                bt_temperature_on.Enabled = false;
                bt_temperature_off.Enabled = false;
                bt_comport.Enabled = false;
                bt_comport_disconnect.Enabled = false;
            }
            else
            {
                bt_demo.Text = "Demo啟動";

                //溫度偵測 OFF

                //demo
                timer_demo.Enabled = false;

                bt_temperature_on.Enabled = true;
                bt_temperature_off.Enabled = true;
                bt_comport.Enabled = true;
                bt_comport_disconnect.Enabled = true;
            }
        }

        void draw_chart_temperature(Chart chart, int temperature_data)
        {
            //richTextBox1.Text += temperature_data.ToString() + "  ";
            float temperature = ((((float)(temperature_data) / 65536.0f) / 0.00198421639f) - 273.15f);
            //richTextBox1.Text += temperature.ToString()+" C ";

            if (temperature > 70)
                lb_temperature.ForeColor = Color.Red;
            else
                lb_temperature.ForeColor = Color.Blue;
            lb_temperature.Text = temperature.ToString("#0.000") + " C";

            /*
            #define XAdcPs_RawToTemperature(AdcData)				\
            ((((float)(AdcData)/65536.0f)/0.00198421639f ) - 273.15f)
            */

            //溫度偵測圖表
            // Define some variables
            //int numberOfPointsInChart = 15;
            int numberOfPointsAfterRemoval = 15;

            // Simulate adding new data points
            float x = pointIndexB + 1;
            //int y = (int)(2500 * Math.Sin(Math.PI * x * 40 / 180) + 2500);
            float y = temperature;

            chart.Series[0].Points.AddXY(x, y);  // AddXY 二維加入
            ++pointIndexB;

            // Adjust Y & X axis scale
            chart.ResetAutoValues();
            if (chart.ChartAreas[0].AxisX.Maximum < pointIndexB)
            {
                chart.ChartAreas[0].AxisX.Maximum = pointIndexB;
            }

            // Keep a constant number of points by removing them from the left
            while (chart.Series[0].Points.Count > 15)
            {
                // Remove data points on the left side
                while (chart.Series[0].Points.Count > numberOfPointsAfterRemoval)
                {
                    chart.Series[0].Points.RemoveAt(0);
                }

                // Adjust X axis scale
                chart.ChartAreas[0].AxisX.Minimum = pointIndexB - numberOfPointsAfterRemoval;
                chart.ChartAreas[0].AxisX.Maximum = chart.ChartAreas[0].AxisX.Minimum + 15;
            }
            chart.Invalidate();
        }

        //------------------------------------------------------------  # 60個

        private void bt_comport_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 115200;

            //serialPort1.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + serialPort1.PortName + "\n";
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + serialPort1.PortName + ", reason : " + ex.Message + "\n";
                //MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                {
                    richTextBox1.Text += "已連上\n";

                    this.BackColor = SystemColors.ControlLight;
                    bt_temperature_on.Enabled = true;
                    bt_temperature_off.Enabled = true;
                    bt_comport.Enabled = false;
                    bt_comport_disconnect.Enabled = true;
                    bt_demo.Enabled = false;

                    serialPort1.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                    //MessageBox.Show("已經連上" + serialPort1.PortName);

                    flag_comport_ok = true;
                    //flag_comport_connection_ok = false;

                    Application.DoEvents();

                    /*
                    //計算serialPort1中有多少位元組 
                    BytesToRead = serialPort1.BytesToRead;

                    if (BytesToRead > 0)
                    {
                        //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }
                    */
                    delay(50);
                    serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    //SerialPortTimer100ms2.Stop();
                    //SerialPortTimer100ms2.Start();
                    Application.DoEvents();
                    delay(100);

                    //計算serialPort1中有多少位元組 
                    BytesToRead = serialPort1.BytesToRead;

                    if (BytesToRead > 0)
                    {
                        richTextBox1.Text += "XXXXXX BytesToRead = " + BytesToRead.ToString() + "\n";
                    }

                    Application.DoEvents();

                    if (serialPort1.IsOpen)
                    {
                        this.BackColor = SystemColors.ControlLight;
                        flag_comport_ok = true;
                    }
                    else
                    {
                        this.BackColor = Color.Pink;
                        flag_comport_ok = false;
                    }
                }
                else
                {
                    //MessageBox.Show("無法連上Comport, 請重新連線");
                    richTextBox1.Text += "無法連上 " + serialPort1.PortName + ", 請重新連線";
                }
            }

            //計算serialPort1中有多少位元組 
            BytesToRead = serialPort1.BytesToRead;

            if (BytesToRead > 0)
            {
                //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
            }
        }

        private void bt_comport_disconnect_Click(object sender, EventArgs e)
        {
            serialPort1.Close();
            this.BackColor = Color.Yellow;
            flag_comport_ok = false;
            //show_main_message1("COM未連線", S_FALSE, 100);
            //toolTip1.SetToolTip(pictureBox_comport1b, "COM未連線");

            bt_temperature_on.Enabled = false;
            bt_temperature_off.Enabled = false;
            bt_comport.Enabled = true;
            bt_comport_disconnect.Enabled = false;
            bt_demo.Enabled = true;
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

