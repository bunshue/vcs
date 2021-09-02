using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports
using System.Windows.Forms.DataVisualization.Charting;  //for Series,   參考/加入參考/.NET/System.Windows.Forms.DataVisualization

namespace vcs_Comport2
{
    public partial class Form1 : Form
    {
        private const int UART_BUF_LENGTH = 5;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }

            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 115200;
            serialPort1.Open();
            richTextBox1.Text += "已連線\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }
            richTextBox1.Text += "已離線\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'^';
                data[1] = (byte)'^';
                data[2] = (byte)'^';
                data[3] = (byte)'^';
                data[4] = (byte)'^';

                serialPort1.Write(data, 0, 5);
                richTextBox1.Text += "send message ok\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'a';
                data[1] = (byte)'b';
                data[2] = (byte)'c';
                data[3] = (byte)'d';
                data[4] = (byte)'e';
                data[5] = (byte)'f';
                data[6] = (byte)'g';

                serialPort1.Write(data, 0, 7);
                richTextBox1.Text += "send message ok\n";
            }

        }


        private void button5_Click(object sender, EventArgs e)
        {
            int BytesToRead = 0;							//緩衝區內可接收資料數

            if (serialPort1.IsOpen == true)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                if (BytesToRead > 0)
                {
                    //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";



                    Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區

                    if (BytesToRead <= 2048)
                    {
                        //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        serialPort1.Read(receive_buffer, 0, BytesToRead);
                    }
                    else
                    {
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }


                    string input = "";
                    for (int i = 0; i < BytesToRead; i++)
                    {
                        input += (char)receive_buffer[i];
                    }

                    richTextBox1.Text += input + "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                richTextBox1.Text += "丟棄UART buffer內的資料\n";
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
            }
        }


        string RxString = "";
        private void DisplayText(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            /*
            //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了
            RxString = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(DisplayText));
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        string[] COM_Ports_NameArr;
        private void Comport_Scan()
        {
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "a共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                for (int i = 0; i < COM_Ports_NameArr.Length; i++)
                {
                    richTextBox1.Text += "COM_Ports_NameArr[" + i.ToString() + "] = " + COM_Ports_NameArr[i] + "\n";
                }
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

        public bool Send_IMS_Data(byte cc, byte xx, byte yy, byte zz)
        {

            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            //serialPort1.Write(data, 0, data.Length);
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

        byte dir = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                dir++;
                if (dir > 3)
                    dir = 0;

                if (dir == 0)
                    richTextBox1.Text += "原圖\n";
                else if (dir == 1)
                    richTextBox1.Text += "左右\n";
                else if (dir == 2)
                    richTextBox1.Text += "上下\n";
                else if (dir == 3)
                    richTextBox1.Text += "左右+上下\n";
                else
                    richTextBox1.Text += "XXXXX\n";

                byte DongleAddr_h;
                byte DongleAddr_l;
                byte DongleData;
                DongleAddr_h = 0x38;
                DongleAddr_l = 0x20;
                DongleData = (byte)(0x10 | (dir << 2));
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            }
            else
            {
                richTextBox1.Text += "無連線\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                if (textBox1.TextLength > 0)
                {

                    richTextBox1.Text += "len = " + textBox1.TextLength.ToString() + "\n";

                    // Convert a C# string to a byte array  
                    byte[] data = Encoding.ASCII.GetBytes(textBox1.Text);   //字串 轉 拜列

                    //string str = Encoding.ASCII.GetString(data); //拜列 轉 字串
                    //richTextBox1.Text += "str = " + str + "\n";

                    foreach (byte b in data)
                    {
                        //richTextBox1.Text += b.ToString("X2") + "\n";
                    }

                    serialPort1.Write(data, 0, textBox1.TextLength);
                    richTextBox1.Text += "send message ok\n";
                }
                else
                {
                    richTextBox1.Text += "無資料可傳\n";
                }
            }
            else
            {
                richTextBox1.Text += "無連線\n";
            }
        }

        string input = "";
        private void SpyMonitorRX()
        {
            input = "";
            for (int i = 0; i < UART_BUF_LENGTH; i++)
                input += (char)receive_buffer[i];

            byte[] data = new byte[5];
            int temperature_data = 0;


            data[0] = (byte)input[0];
            data[1] = (byte)input[1];
            data[2] = (byte)input[2];
            data[3] = (byte)input[3];
            data[4] = CalcCheckSum(data, 4);

            /*
            richTextBox1.AppendText("[RX] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + "\n");
            */

            if (input[0] == 0xA1)
            {
                if (input[1] == 0xCD)
                {
                    if (flag_show_cpu_temperature == true)
                    {
                        //溫度偵測顯示
                        temperature_data = input[2] * 256 + input[3];
                        //richTextBox1.Text += temperature_data.ToString("X4") + "  ";
                        float temperature = ((((float)(temperature_data) / 65536.0f) / 0.00198421639f) - 273.15f);
                        //richTextBox1.Text += temperature.ToString()+" C ";

                        if (temperature > 70)
                            lb_temperature.ForeColor = Color.Red;
                        else
                            lb_temperature.ForeColor = Color.Blue;

                        lb_temperature.Text = temperature.ToString("#0.000") + " C ";

                        /*
                        #define XAdcPs_RawToTemperature(AdcData)				\
                        ((((float)(AdcData)/65536.0f)/0.00198421639f ) - 273.15f)
                        */

                        //溫度偵測圖表
                        // Define some variables
                        int numberOfPointsInChart = 15;
                        int numberOfPointsAfterRemoval = 15;

                        // Simulate adding new data points
                        float x = pointIndex + 1;
                        //int y = (int)(2500 * Math.Sin(Math.PI * x * 40 / 180) + 2500);
                        float y = temperature;

                        chart_temperature.Series[0].Points.AddXY(x, y);
                        ++pointIndex;

                        // Adjust Y & X axis scale
                        chart_temperature.ResetAutoValues();
                        if (chart_temperature.ChartAreas["Default"].AxisX.Maximum < pointIndex)
                        {
                            chart_temperature.ChartAreas["Default"].AxisX.Maximum = pointIndex;
                        }

                        // Keep a constant number of points by removing them from the left
                        while (chart_temperature.Series[0].Points.Count > numberOfPointsInChart)
                        {
                            // Remove data points on the left side
                            while (chart_temperature.Series[0].Points.Count > numberOfPointsAfterRemoval)
                            {
                                chart_temperature.Series[0].Points.RemoveAt(0);
                            }

                            // Adjust X axis scale
                            chart_temperature.ChartAreas["Default"].AxisX.Minimum = pointIndex - numberOfPointsAfterRemoval;
                            chart_temperature.ChartAreas["Default"].AxisX.Maximum = chart_temperature.ChartAreas["Default"].AxisX.Minimum + numberOfPointsInChart;
                        }

                        // Redraw chart
                        chart_temperature.Invalidate();
                    }

                }

            }


        }

        //ims 溫度偵測 ST


        bool flag_show_cpu_temperature = false;

        //溫度偵測圖表
        private int pointIndex = 0;
        Chart chart_temperature = new RealtimeChart().GetChart;

        private void bt_temperature_on_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            if (flag_show_cpu_temperature == false)
            {
                flag_show_cpu_temperature = true;
                SerialPortTimer100ms.Enabled = true;
                //溫度偵測 ON
                Send_IMS_Data(0xFF, 0xCC, 0xFF, 0xAA);

                this.Controls.Add(chart_temperature);
            }
        }

        private void bt_temperature_off_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            if (flag_show_cpu_temperature == true)
            {
                flag_show_cpu_temperature = false;
                SerialPortTimer100ms.Enabled = false;
                //溫度偵測 OFF
                Send_IMS_Data(0xFF, 0xCC, 0xFF, 0x55);
                lb_temperature.Text = "";
                this.Controls.Remove(chart_temperature);
            }
        }

        //溫度偵測圖表
        //繪圖類別
        public class RealtimeChart
        {
            private Chart chart1 = null;
            private int chartWidth = 640;
            private int chartHeight = 480;
            private string nameAxisX = "時間";
            private string nameAxisY = "溫度";

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
                chart1.Location = new System.Drawing.Point(100, 20);
                chart1.Name = "chart1";
                chart1.Size = new System.Drawing.Size(chartWidth, chartHeight);
                chart1.TabIndex = 1;
                chart1.Dock = DockStyle.None;

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
                ctArea.AxisY.Maximum = 80D;
                ctArea.AxisY.Minimum = 60D;
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

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區

        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            //計算serialPort1中有多少位元組 
            int BytesToRead = serialPort1.BytesToRead;

            if (BytesToRead == UART_BUF_LENGTH)
            {
                //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                serialPort1.Read(receive_buffer, 0, BytesToRead);
                SpyMonitorRX();
            }
            else if (BytesToRead > 0)
            {
                richTextBox1.Text += "丟棄UART buffer內的資料\n";
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
            }
        }

        //ims 溫度偵測 SP
    }
}
