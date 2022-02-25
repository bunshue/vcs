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

namespace vcs_Comport_Sample_Temperature
{
    public partial class Form1 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int UART_BUF_LENGTH = 5;

        string[] COM_Ports_NameArr;
        bool flag_comport_ok = false;

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        string input = "";
        int flag_need_to_merge_data = 0;
        bool flag_read_connection_again = true;
        bool flag_show_cpu_temperature = false;

        //溫度偵測圖表
        private int pointIndex = 0;
        Chart chart_temperature = new RealtimeChart().GetChart;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_temperature.Text = "";
            this.BackColor = Color.Yellow;
            Comport_Scan();

            pictureBox1.Location = new Point(chart_temperature.Location.X + chart_temperature.Width + 30, chart_temperature.Location.Y);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {

        }

        private void bt_comport_scan_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void Comport_Scan()
        {
            comboBox_comport.Items.Clear();
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox_comport.Items.Clear();    //Clear All items in Combobox

            richTextBox1.Text += "共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox_comport.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox_comport.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                comboBox_comport.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 1];   //倒數第1個
            }
        }

        private void bt_comport_connect_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Yellow;
            bt_comport_connect.Enabled = true;
            bt_comport_disconnect.Enabled = false;
            flag_comport_ok = false;

            serialPort1.PortName = comboBox_comport.Text;
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

                    pictureBox_comport.Image = vcs_Comport_Sample_Temperature.Properties.Resources.comport;
                    this.BackColor = SystemColors.ControlLight;

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


                    /*
                                        if (flag_comport_connection_ok == true)
                                        {
                                            if (serialPort1.IsOpen)
                                            {
                                                bt_comport_connect1b.Enabled = false;
                                                bt_comport_disconnect1b.Enabled = true;
                                                this.BackColor = SystemColors.ControlLight;
                                                flag_comport_ok = true;
                                            }
                                            else
                                            {
                                                bt_comport_connect1b.Enabled = true;
                                                bt_comport_disconnect1b.Enabled = false;
                                                this.BackColor = Color.Pink;
                                                flag_comport_ok = false;
                                            }
                                        }
                                        else
                                            flag_comport_ok = false;
                        
                                            */
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
            if (flag_comport_ok == true)
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                bt_comport_connect.Enabled = true;
                bt_comport_disconnect.Enabled = false;
                flag_comport_ok = false;
                //show_main_message1("COM未連線", S_FALSE, 100);
                pictureBox_comport.Image = vcs_Comport_Sample_Temperature.Properties.Resources.x;
                //toolTip1.SetToolTip(pictureBox_comport1b, "COM未連線");
            }
        }

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
            if (flag_show_cpu_temperature == false)
            {
                flag_show_cpu_temperature = true;
                //溫度偵測 ON
                Send_IMS_Data(0xFF, 0xCC, 0xFF, 0xAA);
                this.Controls.Add(chart_temperature);
            }
        }

        private void bt_temperature_off_Click(object sender, EventArgs e)
        {
            if (flag_show_cpu_temperature == true)
            {
                flag_show_cpu_temperature = false;
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

                chart1.BackColor = Color.FromArgb(((int)(((byte)(243)))), ((int)(((byte)(223)))), ((int)(((byte)(193)))));
                chart1.BackGradientStyle = GradientStyle.TopBottom;
                chart1.BorderlineColor = Color.FromArgb(((int)(((byte)(181)))), ((int)(((byte)(64)))), ((int)(((byte)(1)))));
                chart1.BorderlineDashStyle = ChartDashStyle.Solid;
                chart1.BorderlineWidth = 2;
                chart1.BorderSkin.SkinStyle = BorderSkinStyle.Emboss;
                chart1.Location = new Point(50, 100);
                chart1.Name = "chart1";
                chart1.Size = new Size(chartWidth, chartHeight);
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
                ctArea.AxisY.Maximum = 80D;
                ctArea.AxisY.Minimum = 60D;
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
                        if (flag_show_cpu_temperature == true)
                        {
                            //溫度偵測顯示
                            int temperature_data = input[2] * 256 + input[3];

                            draw_chart_temperature(temperature_data);
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

        void draw_chart_temperature(int temperature_data)
        {
            //richTextBox1.Text += temperature_data.ToString() + "  ";
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

        private void bt_demo_Click(object sender, EventArgs e)
        {
            if (flag_show_cpu_temperature == false)
            {
                flag_show_cpu_temperature = true;
                //溫度偵測 ON

                //demo
                timer_demo.Enabled = true;

                this.Controls.Add(chart_temperature);
            }
            else
            {
                flag_show_cpu_temperature = false;
                //溫度偵測 OFF

                //demo
                timer_demo.Enabled = false;

                lb_temperature.Text = "";
                this.Controls.Remove(chart_temperature);

                Graphics g = pictureBox1.CreateGraphics();
                g.Clear(Color.Yellow);
                //順道清掉舊資料
                for (int i = 0; i < (N); i++)
                {
                    temp_data[i] = 0;
                }
            }
        }

        private void timer_demo_Tick(object sender, EventArgs e)
        {
            Random r = new Random();
            int hh = r.Next(172, 175);
            int ll = r.Next(0, 256);
            //溫度偵測顯示
            int temperature_data = hh * 256 + ll;

            draw_chart_temperature(temperature_data);
            //richTextBox1.Text += hh.ToString() + " " + ll.ToString() + "\n";

            draw_temperature_picture(temperature_data);
        }

        private const int N = 15;

        int[] temp_data = new int[N];

        //int demo_duty = 36;
        void draw_temperature_picture(int temperature_data)
        {
            /*
            demo_duty++;
            if (demo_duty >= 100)
                demo_duty = 36;
            */

            Graphics g = pictureBox1.CreateGraphics();
            //g.Clear(BackColor);
            g.Clear(Color.White);
            DrawXY();
            //DrawXLine();
            //DrawYLine();
            g.Dispose();

            demo_record_function(temperature_data);
        }

        void demo_record_function(int temperature_data)
        {
            //richTextBox1.Text += temperature_data.ToString() + "  ";
            float temperature = ((((float)(temperature_data) / 65536.0f) / 0.00198421639f) - 273.15f);
            //richTextBox1.Text += temperature.ToString() + " C ";

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            int temp_value = 0;
            int ratio = 0;

            int x_st = 0;
            int x_step = 0;
            int h_st = 0;

            x_st = W * 10 / 100;
            x_step = W * 80 / 100 / (N - 1);
            h_st = H * 90 / 100;

            //ratio = (H * 80 / 100) / 100;
            ratio = 80960 / (H * 80 / 100) + 2;

            //richTextBox1.Text += "a " + H.ToString() + " ";
            //richTextBox1.Text += "b "+ratio.ToString() + " ";

            temp_value = temperature_data / ratio;

            for (int i = 0; i < 14; i++)
            {
                temp_data[i] = temp_data[i + 1];
            }
            temp_data[14] = temp_value;

            Graphics g = pictureBox1.CreateGraphics();
            // Create pens.
            Pen greenPen = new Pen(Color.Green, 3);

            // Create points that define curve.
            Point point0 = new Point(x_st + x_step * 0, h_st - temp_data[0]);
            Point point1 = new Point(x_st + x_step * 1, h_st - temp_data[1]);
            Point point2 = new Point(x_st + x_step * 2, h_st - temp_data[2]);
            Point point3 = new Point(x_st + x_step * 3, h_st - temp_data[3]);
            Point point4 = new Point(x_st + x_step * 4, h_st - temp_data[4]);
            Point point5 = new Point(x_st + x_step * 5, h_st - temp_data[5]);
            Point point6 = new Point(x_st + x_step * 6, h_st - temp_data[6]);
            Point point7 = new Point(x_st + x_step * 7, h_st - temp_data[7]);
            Point point8 = new Point(x_st + x_step * 8, h_st - temp_data[8]);
            Point point9 = new Point(x_st + x_step * 9, h_st - temp_data[9]);
            Point point10 = new Point(x_st + x_step * 10, h_st - temp_data[10]);
            Point point11 = new Point(x_st + x_step * 11, h_st - temp_data[11]);
            Point point12 = new Point(x_st + x_step * 12, h_st - temp_data[12]);
            Point point13 = new Point(x_st + x_step * 13, h_st - temp_data[13]);
            Point point14 = new Point(x_st + x_step * 14, h_st - temp_data[14]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

            // Draw lines between original points to screen.
            //g.DrawLines(greenPen, curvePoints);   //畫直線

            // Draw curve to screen.
            g.DrawCurve(greenPen, curvePoints); //畫曲線

            g.Dispose();
        }

        //以下為自己畫的
        private void DrawXY()//画X轴Y轴
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            Graphics g = this.pictureBox1.CreateGraphics();
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawXLine()    //画X轴平行线
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                Point px1 = new Point(0, H - i * 50);
                Point px2 = new Point(W, H - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            g.Dispose();
        }
        private void DrawYLine()    //画X轴刻度
        {
            int H = pictureBox1.Height;
            Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                Point py1 = new Point(100 * i, H - 5);
                Point py2 = new Point(100 * i, H);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }
    }
}

