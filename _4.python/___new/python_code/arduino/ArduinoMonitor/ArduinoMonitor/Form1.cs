using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                //for file read/write
using System.IO.Ports;          //for serial ports
using System.Diagnostics;       //for Process


namespace ArduinoMonitor
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;
        int IsRunning = 0;
        int IsCCW = 0;
        int Update_System_Status = 1;
        int IsVRRecording = 1;
        int IsDutyRecording = 1;
        int IsRpmRecording = 1;
        int IsPhaseComp = 0;
        int isCommandLog = 0;
        int Comport_Mode = 0;   //0: MysonLink, 1: putty mode, 2: hex mode
        int Demo_Mode = 0;

        String mysonlink_setup_filename = "mysonlink.ini";
        String mysonlink_log_filename = "mysonlink.log";
        string ezisp_path = "";
        int SelectedLanguage = 0;
        static int ProtectionFunction_default = 0x5f;          //default setting
        int ProtectionFunction = ProtectionFunction_default;
        private const int UART_BUF_LENGTH = 5;
        private const int _ALL = 63;
        private const int _CONTROL = 0;
        private const int _DIRECTION = 1;
        private const int _REAL_SPEED = 2;
        private const int _TARGET_SPEED = 3;
        private const int _MAX_SPEED = 4;
        private const int _MIN_SPEED = 5;
        private const int _DUTY = 6;
        private const int _SVPWM_M = 7;
        private const int _PWM_FREQUENCY = 8;
        private const int _POLE_PAIR = 9;
        private const int _TOLERANCE = 10;
        private const int _ACCELERATION = 11;
        private const int _HALL = 12;
        private const int _PROTECTION = 13;
        private const int _ERROR = 14;
        private const int _RUN_STATUS = 15;
        private const int _PHASE_COMP = 16;
        private const int _START_DUTY = 17;
        private const int _PCA_DUTY = 18;
        private const int _GPIO = 19;

        private const int _TIMER0 = 20;
        private const int _TIMER1 = 21;
        private const int _TIMER2 = 22;
        private const int _TIMER3 = 23;
        private const int _TIMER4 = 24;
        private const int _TIMER5 = 25;
        private const int _ADC1 = 26;
        private const int _ADC2 = 27;
        private const int _ADC3 = 28;
        private const int _ADC4 = 29;
        private const int _CMPA = 30;
        private const int _CMPB = 31;
        private const int _CMPC = 32;
        private const int _CMPD = 33;
        private const int _CMPVTH0 = 34;
        private const int _CMPVTH1 = 35;
        private const int _VDC = 40;
        private const int _IS = 41;
        private const int _VR = 42;
        private const int _DEADTIME = 43;

        private const int _ALIVE = 63;

        private const int _NONE = 0;
        private const int _STOP = 0;
        private const int _ONCE = 1;
        private const int _CONTINUOUS = 2;
        private const int _START = 1;
        private const int _TEST = 2;

        private const int NORMAL_MODE = 0;
        private const int VR_MODE = 1;
        private const int AUTO_MODE = 2;
        private const int TEST_MODE = 3;

        private const int _TEST_NONE = 0;
        private const int _TEST_PWM = 1;
        private const int _TEST_SVPWM = 2;
        private const int _TEST_SENSORLESS = 3;
        private const int _TEST_UART = 4;
        private const int _TEST_UVW = 5;

        private const int N = 15;

        private const int _PROTECTION_OCA = 0;
        private const int _PROTECTION_OCC = 1;
        private const int _PROTECTION_OCX = 2;
        private const int _PROTECTION_LOCK = 3;
        private const int _PROTECTION_HALL = 4;
        private const int _PROTECTION_VDC = 5;
        private const int _PROTECTION_WD = 6;

        private const int HALL_SENSOR_MODE = 0;
        private const int SENSORLESS_MODE = 1;
        private const int PCA_MODE = 2;

        int direction = 0;
        int real_speed = 0;
        int target_speed = 0;
        int max_speed = 0;
        int min_speed = 0;
        int duty = 0;
        int tolerance = 0;
        int acceleration = 0;
        int pwm_frequency_point = 0;
        int pwm_frequency = 0;
        int start_duty = 0;
        int pca_duty = 0;
        int timer0_th_tl = 0;
        int timer1_th_tl = 0;
        int timer2_th_tl = 0;
        int adc_vdc = 0;
        int adc_is = 0;
        int adc_vr = 0;
        int adc_vr_mv = 0;
        int hall_status = 0;

        int motor_status = 0;
        int power_status = 0;
        int fw_version = 0;
        int error_code = 0;
        int flag_error_1 = 0;
        int flag_error_2 = 0;
        int flag_error_3 = 0;
        int flag_error_4 = 0;
        int flag_error_5 = 0;
        int flag_error_6 = 0;
        int flag_error_7 = 0;
        int flag_error_8 = 0;
        int flag_error_9 = 0;
        int flag_error_10 = 0;
        int flag_error_11 = 0;

        int flag_get_duty = 0;
        int flag_get_target_speed = 0;
        int flag_get_max_speed = 0;
        int flag_get_min_speed = 0;
        int flag_get_acceleration = 0;
        int flag_get_tolerance = 0;
        int flag_get_pole_pair = 0;
        int flag_get_pwm_freq = 0;
        int flag_get_direction = 0;
        int flag_get_start_duty = 0;
        int flag_sensor_type = HALL_SENSOR_MODE;

        int control_1 = 0;	//CW/CCW
        int control_2 = 0;	//duty/rpm
        int control_3 = 0;	//sensor/sensorless
        //int control_4 = 0;	//PWM/SVPWM
        //int control_5 = 0;	//NNMOS/PNMOS
        //int control_6 = 2;	//CM2209A/CM2209B/CM2209C/CM2209D/CM2209_others
        int control_7 = 1;	//real hall/sensorless hall
        int target_vr = 0;
        int real_vr = 0;

        public Form1()
        {
            InitializeComponent();
        }

        void show_item_location()
        {

        }

        private void Comport_Scan()
        {
            string[] tempString = SerialPort.GetPortNames();
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox1.Items.Clear();    //Clear All items in Combobox

            foreach (string port in COM_Ports_NameArr)
            {
                //MessageBox.Show("get comport : " + port);
                comboBox1.Items.Add(port);
            }

            if (COM_Ports_NameArr.Length > 0)
                comboBox1.Text = COM_Ports_NameArr[0];
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            Comport_Scan();
        }

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
                System.Threading.Thread.Sleep(1);
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";
        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer, 0, BytesToRead);
                    if (Comport_Mode == 0)  //MysonLink mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                            SpyMonitorRX();
                        else
                        {
                            /*
                            //for UART debug
                            lb_uart_debug.Text += BytesToRead.ToString();
                            lb_uart_debug.Text += ' ';
                            */

                            //資料不是5拜，打印出來。
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
                            richTextBox1.AppendText("[UN]: ");
                            for (int i = 0; i < BytesToRead; i++)
                            { 
                                richTextBox1.AppendText(((int)input[i]).ToString("X2") + " ");
                            }
                            richTextBox1.AppendText("\n");
                            */
                            richTextBox1.AppendText(input);     //打印一般文字訊息

                            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                            //Write_Log_File(input);
                        }
                    }
                }
            }
        }

        private void DrawXY()//画X轴Y轴
        {
            Graphics g = this.panel4.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.panel4.Width * 90 / 100, this.panel4.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawXLine()    //画X轴平行线
        {
            Graphics g = this.panel4.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point px1 = new System.Drawing.Point(0, this.panel4.Height - i * 50);
                System.Drawing.Point px2 = new System.Drawing.Point(this.panel4.Width, this.panel4.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            g.Dispose();
        }
        private void DrawYLine()    //画X轴刻度
        {
            Graphics g = this.panel4.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.panel4.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.panel4.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }

        int y1_value = 0;
        int y2_value = 0;
        int y3_value = 0;
        int[] y1_data = new int[15];
        int[] y2_data = new int[15];
        int[] y3_data = new int[15];
        int x_st = 0;
        int x_step = 0;
        int h_st = 0;
        int ratio_vr = 0;
        int ratio_duty = 0;
        int ratio_rpm = 0;
        int control_data2 = 0;
        int control_data3 = 0;
        int board_number = 0;
        int loop = 0;
        int loop_old = -1;

        private void SpyMonitorRX()
        {
            string message = "";
            //if (BytesToRead == 5)
            {
                input = "";
                for (int i = 0; i < UART_BUF_LENGTH; i++)
                    input += (char)receive_buffer[i];

                if (isCommandLog == 1)
                {
                    richTextBox1.AppendText("[RX]: " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "\n");
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

                if (input[0] == 0xDD)
                {
                }
                else if (input[0] == 0xEE)
                {

                    error_code = (int)input[2] * 256 + (int)input[3];
                    //richTextBox1.AppendText("[PC]: error_code = " + error_code.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                    flag_error_1 = error_code & 0x01;           //parameter   btn_error1
                    flag_error_2 = (error_code & 0x02) >> 1;    //ov          btn_error2
                    flag_error_3 = (error_code & 0x04) >> 2;    //uv          btn_error3
                    flag_error_4 = (error_code & 0x08) >> 3;    //lock        btn_error4
                    flag_error_5 = (error_code & 0x10) >> 4;    //hall        btn_error5
                    flag_error_6 = (error_code & 0x20) >> 5;    //oca         btn_error6
                    flag_error_7 = (error_code & 0x40) >> 6;    //occ         btn_error7
                    flag_error_8 = (error_code & 0x80) >> 7;    //ocx         btn_error8
                    flag_error_9 = (error_code & 0x100) >> 8;   //uvw         btn_error9
                    flag_error_10 = (error_code & 0x200) >> 9;  //short       btn_error10
                    flag_error_11 = (error_code & 0x400) >> 10; //recover from ov uv, disable btn_error2 btn_error3

                }
                else if (input[0] == 0xC1)          //0xC1: 收到下位發送的馬達參數命令
                {
                    if (input[1] == _ALIVE)
                    {
                    }
                    else if (input[1] == _DUTY)
                    {
                        duty = (int)input[3];
                        //richTextBox1.AppendText("[PC]: duty = " + duty.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        aGauge_duty.Value = duty;
                        tb_main_duty2.Text = duty.ToString();
                        if (flag_get_duty == 1)
                        {
                            flag_get_duty = 0;
                        }

                        richTextBox1.Text += "D1 ";
                        adc_vr = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: adc_vr = " + adc_vr.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        //if (tabControl1.SelectedIndex == 0)
                        {
                            adc_vr_mv = adc_vr * 5000 / 4096;
                            delay(10);
                        }
                        //else if (tabControl1.SelectedIndex == 1)
                        {
                            delay(10);
                        }
                        //else if (tabControl1.SelectedIndex == 2)
                        {
                            delay(10);
                        }

                        richTextBox1.Text += "X";
                        if ((IsVRRecording == 1) || (IsDutyRecording == 1) || (IsRpmRecording == 1))
                        {
                            Graphics g = panel4.CreateGraphics();
                            //g.Clear(BackColor);
                            g.Clear(Color.White);
                            DrawXY();
                            //DrawXLine();
                            //DrawYLine();
                            g.Dispose();
                        }

                        x_st = panel4.Width * 10 / 100;
                        x_step = panel4.Width * 80 / 100 / (N - 1);
                        h_st = panel4.Height * 90 / 100;

                        if (IsDutyRecording == 1)
                        {
                            ratio_duty = (panel4.Height * 80 / 100) / 100;

                            //y2_value = duty*4;
                            y2_value = duty * ratio_duty;

                            for (int i = 0; i < 14; i++)
                            {
                                y2_data[i] = y2_data[i + 1];
                            }
                            y2_data[14] = y2_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen greenPen = new Pen(Color.Green, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y2_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y2_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y2_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y2_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y2_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y2_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y2_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y2_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y2_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y2_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y2_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y2_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y2_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y2_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y2_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(greenPen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(greenPen, curvePoints); //畫曲線

                            g.Dispose();
                        }
                    }
                    else if (input[1] == _DUTY)
                    {
                        richTextBox1.Text += "D1 ";
                        adc_vr = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: adc_vr = " + adc_vr.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        //if (tabControl1.SelectedIndex == 0)
                        {
                            adc_vr_mv = adc_vr * 5000 / 4096;
                            delay(10);
                        }
                        //else if (tabControl1.SelectedIndex == 1)
                        {
                            delay(10);
                        }
                        //else if (tabControl1.SelectedIndex == 2)
                        {
                            delay(10);
                        }

                        richTextBox1.Text += "X";
                        if ((IsVRRecording == 1) || (IsDutyRecording == 1) || (IsRpmRecording == 1))
                        {
                            Graphics g = panel4.CreateGraphics();
                            //g.Clear(BackColor);
                            g.Clear(Color.White);
                            DrawXY();
                            //DrawXLine();
                            //DrawYLine();
                            g.Dispose();
                        }

                        x_st = panel4.Width * 10 / 100;
                        x_step = panel4.Width * 80 / 100 / (N - 1);
                        h_st = panel4.Height * 90 / 100;

                        if (IsVRRecording == 1)
                        {
                            ratio_vr = 4096 / (panel4.Height * 80 / 100) + 2;

                            adc_vr_mv = adc_vr * 5000 / 4096;

                            //y1_value = (adc_vr_mv) / 13;
                            y1_value = (adc_vr_mv) / ratio_vr;

                            for (int i = 0; i < (N - 1); i++)
                            {
                                y1_data[i] = y1_data[i + 1];
                            }
                            y1_data[N - 1] = y1_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen redPen = new Pen(Color.Red, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y1_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y1_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y1_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y1_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y1_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y1_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y1_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y1_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y1_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y1_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y1_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y1_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y1_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y1_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y1_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(redPen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(redPen, curvePoints); //畫曲線
                            g.Dispose();
                        }

                        if (IsDutyRecording == 1)
                        {
                            ratio_duty = (panel4.Height * 80 / 100) / 100;

                            //y2_value = duty*4;
                            y2_value = duty * ratio_duty;

                            for (int i = 0; i < 14; i++)
                            {
                                y2_data[i] = y2_data[i + 1];
                            }
                            y2_data[14] = y2_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen greenPen = new Pen(Color.Green, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y2_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y2_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y2_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y2_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y2_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y2_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y2_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y2_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y2_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y2_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y2_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y2_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y2_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y2_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y2_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(greenPen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(greenPen, curvePoints); //畫曲線

                            g.Dispose();
                        }
                        if (IsRpmRecording == 1)
                        {
                            ratio_rpm = max_speed / (panel4.Height * 80 / 100) + 1;

                            y3_value = (int)(real_speed / ratio_rpm);

                            for (int i = 0; i < 14; i++)
                            {
                                y3_data[i] = y3_data[i + 1];
                            }
                            y3_data[14] = y3_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen bluePen = new Pen(Color.Blue, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y3_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y3_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y3_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y3_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y3_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y3_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y3_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y3_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y3_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y3_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y3_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y3_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y3_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y3_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y3_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(bluePen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(bluePen, curvePoints); //畫曲線

                            g.Dispose();
                        }



                    }
                    delay(10);
                }
                else if (input[0] == 0xC2)          //0xC2: 收到下位發送的目前系統狀態命令
                {
                }
                else if (input[0] == 0xCC)          //0xCC: Servo專用命令
                {
                }
                else if (input[0] == 0xCE)          //0xCE: Servo專用命令
                {
                }
                else
                {
                    //資料是5拜，但是解不出所要的資訊。
                    message += "[unknown data1]: ";
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
                message += "[unknown data2]: ";
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

        private void bt_comport_scan_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void bt_comport_connect_Click(object sender, EventArgs e)
        {
            if (comboBox1.Text.Length == 0)
            {
                MessageBox.Show("No comport selected.");
                return;
            }
            serialPort1.PortName = comboBox1.Text;
            serialPort1.BaudRate = int.Parse(comboBox2.Text);

            //serialPort1.Open(); //原本是這一行，改成以下18行。
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                {
                    //MessageBox.Show("已經連上" + serialPort1.PortName);
                }
                else
                {
                    //MessageBox.Show(language9[SelectedLanguage, 1]);
                }
            }

            if (serialPort1.IsOpen)
            {
                //panel1.BackColor = System.Drawing.Color.Yellow;
                //panel5.BackColor = System.Drawing.Color.Yellow;
                //button1.Enabled = false;
                //button2.Enabled = true;
                richTextBox1.ReadOnly = false;
                if (control_2 == 0)
                {
                    //tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                    //tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                }
                else
                {
                    //tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                    //tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                }
            }

        }

        private void bt_comport_disconnect_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                //button1.Enabled = true;
                //button2.Enabled = false;
                richTextBox1.ReadOnly = true;
                //tb_target.Text = "請連線Comport";
                //tb_target2.Text = "請連線Comport";
                //panel1.BackColor = System.Drawing.Color.OrangeRed;
                //panel5.BackColor = System.Drawing.Color.OrangeRed;
            }

        }

    }
}


