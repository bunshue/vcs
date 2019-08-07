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
using System.Diagnostics;       //for Process, Stopwatch
using System.Drawing.Imaging;   //for ImageFormat

using AForge.Video;
using AForge.Video.DirectShow;

using System.Runtime.InteropServices;   //for dll

namespace imsLink
{
    public partial class Form1 : Form
    {
        bool flag_release_mode = false;

        bool flag_awb_debug = true;

        bool flag_us_debug = false;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const bool SHOW_COMPORT_LOG = false;
        private const int UART_BUF_LENGTH = 5;
        private const int CAMERA_OK = 0;	//dongle + camera
        private const int CAMERA_NONE = 1;	//dongle only
        private const int DONGLE_NONE = 2;	//no dongle
        private const int CAMERA_UNKNOWN = 3;	//dongle camera unknown status
        private const int VIDEO_OK = 0;
        private const int VIDEO_FORBID_ALL = 1;
        private const int VIDEO_FORBID_USE_2HR = 2;

        private const int MODEL_PAGE = 0x07;	//model
        private const int SN_PAGE1 = 0x08;	    //serial1
        private const int SN_PAGE2 = 0x09;	    //serial2
        private const int DATE_PAGE0 = 0x0A;	//serial date, product time
        private const int DATE_PAGE1 = 0x0B;	//use 1 minute
        private const int DATE_PAGE3 = 0x0D;	//use 2 hrs
        private const int ERROR_PAGE = 0x0E;	//error code
        private const int ERROR_DATE = 0x0F;	//error date
        private const int AWB_PAGE = 0x10;	//awb data

        string imslink_log_filename = "imslink.log";
        string RxString = "";
        string[] COM_Ports_NameArr;
        int isCommandLog = 1;
        int Comport_Mode = 0;   //0: imsLink, 1: putty mode, 2: hex mode
        int fw_version = 0;
        int log_file_tmp_length = 0;
        string log_file_tmp_data = "";
        byte DongleAddr_h;
        byte DongleAddr_l;
        byte DongleData;
        byte xx;
        byte yy;
        byte zz;
        int flag_wait_receive_data = 0;
        int flag_receive_camera_serial = 0;
        int flag_receive_camera_flash_data = 0;
        int flag_receive_mb_model_data = 0;
        int flag_receive_ims_rtc_data = 0;
        int flag_request_item = 0;
        int flag_verify_serial_data = 0;
        int flag_need_to_merge_data = 0;
        int flag_burn_long_cnt = 0;
        int flag_camera_start = 0;
        byte cnt1 = 0;
        int cnt3 = 0;
		int g_conn_status = CAMERA_UNKNOWN;
        int[] camera_serial_data = new int[16];
        byte[] sn_data_send2 = new byte[16];
        byte[] rtc_data_send = new byte[7];
        byte[] camera_model_data_send = new byte[16];
        byte[] main_board_model_data_send = new byte[50];
        byte[] awb_data_send = new byte[4];
        string camera_serial_old = String.Empty;
        string camera_serial_enw = String.Empty;
        bool flag_auto_scan_mode = true;
        bool flag_read_connection_again = true;
        bool flag_comport_ok = false;
        bool flag_already_write_system_data = false;
        bool flag_fullscreen = false;

        int data_expo = 0;
        byte data_expo_h = 0;
        byte data_expo_l = 0;
        int data_gain = 0;
        byte data_gain_h = 0;
        byte data_gain_l = 0;
        int data_R = 0;
        byte data_R_h = 0;
        byte data_R_l = 0;
        int data_G = 0;
        byte data_G_h = 0;
        byte data_G_l = 0;
        int data_B = 0;
        byte data_B_h = 0;
        byte data_B_l = 0;

        private const int SENSOR_EXPO = 0x01;	//camera sensor expo
        private const int SENSOR_GAIN = 0x02;	//camera sensor gain
        private const int SENSOR_RGB_R = 0x03;	//camera sensor R
        private const int SENSOR_RGB_G = 0x04;	//camera sensor G
        private const int SENSOR_RGB_B = 0x05;	//camera sensor B
        private const int SENSOR_WPT = 0x06;	//camera sensor white point
        private const int SENSOR_BPT = 0x07;	//camera sensor black point

        int flag_wait_data_cmd = 0;
        bool flag_awb_update_expo = false;
        bool flag_awb_update_gain = false;
        bool flag_awb_update_R = false;
        bool flag_awb_update_G = false;
        bool flag_awb_update_B = false;
        bool flag_update_RGB_scrollbar = true;     //always update value
        bool flag_R_OK = false;
        bool flag_G_OK = false;
        bool flag_B_OK = false;
        bool flag_break = false;
        bool flag_do_awb = false;
        int timer_display_save_count = 0;
        int timer_display_r_count = 0;
        int timer_display_g_count = 0;
        int timer_display_b_count = 0;
        bool flag_display_r_do_awb = false;
        bool flag_display_g_do_awb = false;
        bool flag_display_b_do_awb = false;

        Stopwatch stopwatch = new Stopwatch();

        int zoom_cnt = 0;
        int zoom_cnt_max = 15;
        int zoom_step = 40;
        int usb_camera_width = 0;
        int usb_camera_height = 0;

        int btn_down_up_cnt = 0;
        int btn_right_left_cnt = 0;
        int flag_down_up_cnt = 0;
        int flag_right_left_cnt = 0;
        int awb_step = 10;
        int awb_block = 64;     //AWB block size width, height

        int TARGET_AWB_R = 255;
        int TARGET_AWB_G = 249;
        int TARGET_AWB_B = 253;

        int total_RGB_R = 0;
        int total_RGB_G = 0;
        int total_RGB_B = 0;

        int total_RGB_R_max = 0;
        int total_RGB_R_min = 0;
        int total_RGB_G_max = 0;
        int total_RGB_G_min = 0;
        int total_RGB_B_max = 0;
        int total_RGB_B_min = 0;
        int tolerance = 0;
        int tolerance_ratio = 1;

        private const int CHECK_SATURATION_FRAME = 30;
        bool flag_check_rgb_saturation = false;
        int rgb_saturation_check_cnt = 30000;
        int rgb_r_saturation_cnt = 0;
        int rgb_g_saturation_cnt = 0;
        int rgb_b_saturation_cnt = 0;

        private const int CHECK_AWB_FRAME = 30;
        bool flag_check_rgb = false;
        int rgb_check_cnt = 30000;
        int rgb_r_ok_cnt = 0;
        int rgb_g_ok_cnt = 0;
        int rgb_b_ok_cnt = 0;
        int rgb_r_fail_high_cnt = 0;
        int rgb_r_fail_low_cnt = 0;
        int rgb_g_fail_high_cnt = 0;
        int rgb_g_fail_low_cnt = 0;
        int rgb_b_fail_high_cnt = 0;
        int rgb_b_fail_low_cnt = 0;
        int diff_r = 0;
        int diff_g = 0;
        int diff_b = 0;

        //C# 提示視窗 ToolTip 
        //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
        ToolTip toolTip1 = new ToolTip();
        //SetToolTip：定義控制項會跳出提示的文字

        Graphics g;
        Graphics g2;

        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        void Write_Log_File(string input)
        {
            log_file_tmp_length += input.Length;
            log_file_tmp_data += input;

            if (log_file_tmp_length > 100)
            {
                //int i;
                if (System.IO.File.Exists(imslink_log_filename) == false)
                {
                    //MessageBox.Show("檔案 " + imslink_log_filename + " 不存在，製作一個。");
                    StreamWriter sw = File.CreateText(imslink_log_filename);
                    sw.Write(log_file_tmp_data);
                    sw.Close();
                }
                else
                {
                    //MessageBox.Show("檔案 " + imslink_log_filename + " 存在, 開啟，並接續寫入資料");

                    StreamWriter sw = File.AppendText(imslink_log_filename);
                    sw.Write(log_file_tmp_data);
                    sw.Close();
                }
                log_file_tmp_length = 0;
                log_file_tmp_data = "";
            }
        }

        public Form1()
        {
            InitializeComponent();

            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            g = panel6.CreateGraphics();
            g.Clear(BackColor);

            g2 = panel9.CreateGraphics();
            g2.Clear(BackColor);

            Reset_imsLink_Setting();

            tb_exposure.Text = trackBar6.Value.ToString();

            numericUpDown_expo.Value = trackBar_expo.Value;
            numericUpDown_gain.Value = trackBar_gain.Value;
            numericUpDown_R.Value = trackBar_R.Value;
            numericUpDown_G.Value = trackBar_G.Value;
            numericUpDown_B.Value = trackBar_B.Value;
            comboBox_temperature.SelectedIndex = 5; //6500K
            numericUpDown_TG_R.Value = TARGET_AWB_R;
            numericUpDown_TG_G.Value = TARGET_AWB_G;
            numericUpDown_TG_B.Value = TARGET_AWB_B;

            /*
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
                    MessageBox.Show("無法連上Comport, 請重新連線");
                }
            }

            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
            }
            */
        }

        private void Reset_imsLink_Setting()
        {
            if (flag_release_mode == true)
            {
                this.tp_Camera.Parent = null;   //camera
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
            }

            if (flag_us_debug == true)
            {
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
            }

            if (flag_us_debug == true)
            {
                tabControl1.SelectTab(tp_USB);       //程式啟動時，直接跳到USB那頁。
            }
            else
            {
                //tabControl1.SelectedTab = tp_Connection;    //程式啟動時，直接跳到Connection那頁。
                tabControl1.SelectTab(tp_Connection);       //程式啟動時，直接跳到Connection那頁。   the same
            }

            this.Width = 960;
            show_comport_log = SHOW_COMPORT_LOG;

            Comport_Mode = 0;
            this.richTextBox1.Location = new System.Drawing.Point(958, 67);
            this.richTextBox1.Size = new System.Drawing.Size(500, 586);

            if (isCommandLog == 1)
            {
                button74.Text = "CMD off";
                button74.ForeColor = Color.Red;
            }
            else
            {
                button74.Text = "CMD on";
                button74.ForeColor = Color.Green;
            }
            richTextBox1.Font = new Font("Courier New", 10);
            button33.BackgroundImage = imsLink.Properties.Resources.open_log;
            toolTip1.SetToolTip(button33, "log on");
        }

        private void button1_Click(object sender, EventArgs e)
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
                    MessageBox.Show("無法連上Comport, 請重新連線");
            }
            
            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                flag_comport_ok = true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == true)
            {
                serialPort1.Close();
                button1.Enabled = true;
                button2.Enabled = false;
                richTextBox1.ReadOnly = true;
                flag_comport_ok = false;
            }
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // If the port is closed, don't try to send a character.
            if (flag_comport_ok == false)
                return;

            // If the port is Open, declare a char[] array with one element.
            char[] buff = new char[1];

            // Load element 0 with the key character.
            buff[0] = e.KeyChar;

            // Send the one character buffer.
            serialPort1.Write(buff, 0, 1);

            // Set the KeyPress event as handled so the character won't
            // display locally. If you want it to display, omit the next line.
            e.Handled = true;
        }

        private void DisplayText(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }
        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            //RxString = serialPort1.ReadExisting();
            //this.Invoke(new EventHandler(DisplayText));
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC] : Reset imsLink\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Reset_imsLink_Setting();
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

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        string input ="";

        private void show_info(int item)
        {
            //richTextBox1.Text += "show_info item = " + item.ToString() + "\n";
            switch (flag_request_item)
            {
                case MODEL_PAGE:
                    break;
                //case SN_PAGE2:
                case DATE_PAGE0:
                case DATE_PAGE1:
                case DATE_PAGE3:
                case ERROR_DATE:
                    if ((input[12] == 0xAA) && (input[13] == 0xBB) && (input[14] == 0xCC) && (input[15] == 0xDD))
                    {
                        int year;
                        int month;
                        int mday;
                        int wday;
                        int hour;
                        int minutes;
                        int seconds;
                        year = (int)input[0] + 1900;
                        month = (int)input[1];
                        mday = (int)input[2];
                        wday = (int)input[3];
                        hour = (int)input[4];
                        minutes = (int)input[5];
                        seconds = (int)input[6];
                        richTextBox1.Text += "year = " + year.ToString("00") + "\n";
                        richTextBox1.Text += "month = " + month.ToString("00") + "\n";
                        richTextBox1.Text += "mday = " + mday.ToString("0000") + "\n";
                        richTextBox1.Text += "wday = " + wday.ToString() + "\n";
                        richTextBox1.Text += "hour = " + hour.ToString("00") + "\n";
                        richTextBox1.Text += "minutes = " + minutes.ToString("00") + "\n";
                        richTextBox1.Text += "seconds = " + seconds.ToString("00") + "\n";
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行


                        if (flag_request_item == DATE_PAGE0)
                        {
                            lb_a.Text = "Product : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                            lb_sn3.Text = lb_a.Text;
                        }
                        else if (flag_request_item == DATE_PAGE1)
                        {
                            lb_b.Text = "1MIN : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                        }
                        else if (flag_request_item == DATE_PAGE3)
                        {
                            lb_d.Text = "2HR : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                        }
                        else if (flag_request_item == ERROR_DATE)
                        {
                            lb_f.Text = "Expired : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                            tb_info_f2.BackColor = Color.Red;
                        }
                        else
                        {
                            richTextBox1.Text += "unknown data for flag_request_item = " + flag_request_item.ToString() + "\n";
                        }
                    }
                    else
                    {
                        if (flag_request_item == DATE_PAGE0)
                        {
                            //lb_aa.Text = "Product : ----------------------------------";
                        }
                        else if (flag_request_item == DATE_PAGE1)
                        {
                            lb_b.Text = "1MIN : ----------------------------------";
                        }
                        else if (flag_request_item == DATE_PAGE3)
                        {
                            lb_d.Text = "2HR : ----------------------------------";
                        }
                        else if (flag_request_item == ERROR_DATE)
                        {
                            lb_f.Text = "----- : ----------------------------------";
                            tb_info_f2.BackColor = Color.White;
                        }
                        else
                        {
                            richTextBox1.Text += "unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                        }
                    
                    }
                    break;
                case ERROR_PAGE:
                    int flag_video_status = 0;
                    if (((int)input[0] == 0xEE) && ((int)input[1] == 0xCC) && ((int)input[2] == 0xDD) && ((int)input[3] == 0xEE))
                    {
                        flag_video_status = (int)input[4];
                    }
                    else if (((int)input[0] == 0) && ((int)input[1] == 0) && ((int)input[2] == 0) && ((int)input[3] == 0))
                    {
                        //camera page 0xe no data
                    }
                    else
                    {
                        //wrong data
                    }
                    switch (flag_video_status)
                    {
                        case VIDEO_OK: lb_e.Text = "VIDEO_OK"; break;
                        case VIDEO_FORBID_ALL: lb_e.Text = "VIDEO_FORBID_ALL"; break;
                        case VIDEO_FORBID_USE_2HR: lb_e.Text = "VIDEO_FORBID_USE_2HR"; break;
                        default: lb_e.Text = "unknown video status : " + flag_video_status.ToString(); break;
                    }
                    if (flag_video_status == VIDEO_OK)
                        tb_info_e2.BackColor = Color.White;
                    else
                        tb_info_e2.BackColor = Color.Red;

                    break;
                default:
                    richTextBox1.Text += "unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                    break;

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
                            serialPort1.DiscardInBuffer();
                            richTextBox1.Text += "丟棄UART buffer內的資料 aaa\n";
                        }
                    }
                    if (Comport_Mode == 0)  //imsLink mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                        {
                            SpyMonitorRX();
                        }
                        else if (BytesToRead == 21) // 5 + 16
                        {
                            /*
                            richTextBox1.Text += "BytesToRead = 21 Bytes, data\t";
                            for (int i = 0; i < BytesToRead; i++)
                            {
                                richTextBox1.Text += receive_buffer[i].ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";
                            */

                            SpyMonitorRX();

                            input = "";
                            for (int i = 5; i < (16 + 5); i++)
                                input += (char)receive_buffer[i];

                            if (flag_receive_camera_serial == 1)
                            {
                                richTextBox1.Text += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n";

                                //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                //if (BytesToRead == 21)
                                {
                                    //input = "";
                                    //for (int i = 5; i < (16 + 5); i++)
                                        //input += (char)receive_buffer[i];

                                    richTextBox1.AppendText("[S/N] : "
                                        + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2") + "-"
                                        + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2") + "-"
                                        + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2") + "-"
                                        + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n");
                                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                                    /*
                                    tb_sn1.Text = "[S/N] : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                    */

                                    //xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                    tb_info_aa1.Text = "[S/N] : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                }
                                flag_receive_camera_serial = 0;
                                flag_wait_receive_data = 0;

                                if (flag_verify_serial_data == 1)
                                {
                                    flag_verify_serial_data = 0;
                                    int flag_same_serial = 1;
                                    for (int i = 0; i < 16; i++)
                                    {
                                        if (sn_data_send2[i] != input[i])
                                        {
                                            flag_same_serial = 0;
                                        }
                                    }
                                    if (flag_same_serial == 1)
                                    {
                                        richTextBox1.Text += "xxxxxxx 驗證完成, 序號相同\n";
                                        lb_sn3.Text = "xxxxxxx 驗證完成, 序號相同  ";
                                    }
                                    else
                                    {
                                        richTextBox1.Text += "xxxxxx驗證失敗, 序號不同\n";
                                        lb_sn3.Text = "xxxxx驗證失敗, 序號不同  ";
                                        groupBox10.BackColor = Color.Red;
                                    }
                                    lb_sn2.Text = "";

                                    // Stop timing
                                    stopwatch.Stop();
                                    richTextBox1.Text += "xxxxxxxxxxxxx 燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

                                    if (stopwatch.ElapsedMilliseconds > 7000)
                                    {
                                        flag_burn_long_cnt++;
                                        ////lb_mesg2.Text = "耗時太久 " + flag_burn_long_cnt.ToString() + " 次";
                                    }

                                    ////lb_mesg3.Text = stopwatch.ElapsedMilliseconds.ToString() + " msec";

                                }
                            }
                            else if (flag_receive_camera_flash_data == 1)
                            {
                                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                //if (BytesToRead == 16)
                                {

                                    //input = "";
                                    //for (int i = 0; i < 16; i++)
                                        //input += (char)receive_buffer[i];

                                    richTextBox1.AppendText("[Data] : "
                                        + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2") + "-"
                                        + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2") + "-"
                                        + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2") + "-"
                                        + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n");
                                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                                    /*
                                    textBox5.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                    */

                                    switch (flag_request_item)
                                    {
                                        case MODEL_PAGE:
                                            bool flag_no_camera_model = true;
                                            tb_info_8.Text = "[Model] : ";
                                            for (int i = 0; i < 16; i++)
                                            {
                                                if (((int)input[i] < 32) || ((int)input[i] > 126))
                                                {
                                                    if ((int)input[i] != 0)
                                                    {
                                                        flag_no_camera_model = false;
                                                    }
                                                }
                                                else
                                                {
                                                    tb_info_8.Text += (char)input[i];
                                                    flag_no_camera_model = false;
                                                }
                                            }
                                            if (flag_no_camera_model == true)
                                            {
                                                tb_info_8.Text = "[Model] : 無相機型號資料";
                                            }
                                            lb_camera_model.Text = tb_info_8.Text;
                                            break;
                                        case DATE_PAGE0:
                                            break;
                                        case DATE_PAGE1:
                                            tb_info_b.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case DATE_PAGE3:
                                            tb_info_d.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case ERROR_PAGE:
                                            tb_info_e.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case ERROR_DATE:
                                            tb_info_f.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        default:
                                            richTextBox1.Text += "unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                                            break;

                                    }
                                    show_info(flag_request_item);
                                }
                                flag_receive_camera_flash_data = 0;
                                flag_wait_receive_data = 0;


                            }
                            else if (flag_receive_mb_model_data == 1)
                            {
                                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                bool flag_no_mb_model = true;
                                bool flag_no_mb_serial = true;
                                lb_machine_serial.Text = "[主機序號] : ";
                                lb_mb_big_serial.Text = "[大PCBA序號] : ";
                                lb_mb_small_serial.Text = "[小PCBA序號] : ";
                                for (int i = 0; i < 8; i++)
                                {
                                    if (((int)input[i] < 32) || ((int)input[i] > 126))
                                    {
                                        if ((int)input[i] != 0)
                                        {
                                            flag_no_mb_model = false;
                                        }
                                    }
                                    else
                                    {
                                        lb_machine_serial.Text += (char)input[i];
                                        flag_no_mb_model = false;
                                    }
                                }
                                for (int i = 8; i < 16; i++)
                                {
                                    if (((int)input[i] < 32) || ((int)input[i] > 126))
                                    {
                                        if ((int)input[i] != 0)
                                        {
                                            flag_no_mb_serial = false;
                                        }
                                    }
                                    else
                                    {
                                        lb_mb_big_serial.Text += (char)input[i];
                                        flag_no_mb_serial = false;
                                    }
                                }

                                if (flag_no_mb_model == true)
                                {
                                    lb_machine_serial.Text = "[Model] : 無主機型號資料";
                                }
                                if (flag_no_mb_serial == true)
                                {
                                    lb_machine_serial.Text = "[Model] : 無主機序號資料";
                                }

                                flag_receive_mb_model_data = 0;
                                flag_wait_receive_data = 0;
                            }
                            else if (flag_receive_ims_rtc_data == 1)
                            {
                                flag_receive_ims_rtc_data = 0;
                                flag_wait_receive_data = 0;

                                string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
                                string weekday = Day[input[3]].ToString();
                                lb_time2.Text = "ims時間 : " + ((int)input[0] + 1900).ToString() + "/" + ((int)input[1] + 1).ToString("00") + "/" + ((int)input[2]).ToString("00") + " " + weekday + " " + ((int)input[4]).ToString("00") + ":" + ((int)input[5]).ToString("00") + ":" + ((int)input[6]).ToString("00");
                                //richTextBox1.Text += ((int)input[6]).ToString("00") + " ";
                                flag_read_connection_again = true;

                                progressBar2.Value = 100;
                            }
                        }
                        else if (BytesToRead == 37) // 5 + 16 + 16
                        {
                            int i;
                            richTextBox1.Text += "BytesToRead = 37 Bytes, data\t";
                            for (i = 0; i < BytesToRead; i++)
                            {
                                richTextBox1.Text += receive_buffer[i].ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";

                            SpyMonitorRX();

                            input = "";
                            for (i = 5; i < (32 + 5); i++)
                                input += (char)receive_buffer[i];


                            richTextBox1.Text += "input data \n";
                            for (i = 0; i < 32; i++)
                            {
                                richTextBox1.Text += ((int)input[i]).ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";

                            bool flag_no_camera_serial1 = true;
                            bool flag_no_camera_serial2 = true;
                            tb_info_aa1.Text = "[S/N] : ";
                            tb_info_aa2.Text = "[S/N] : ";

                            for (i = 0; i < 9; i++)
                            {
                                if (((int)input[i] < 32) || ((int)input[i] > 126))
                                {
                                    flag_no_camera_serial1 = true;
                                    break;
                                }
                                else
                                {
                                    tb_info_aa1.Text += (char)input[i];
                                    flag_no_camera_serial1 = false;
                                }
                            }

                            for (i = 16; i < (16 + 11); i++)
                            {
                                if (((int)input[i] < '0') || ((int)input[i] > '9'))
                                {
                                    flag_no_camera_serial2 = true;
                                    break;
                                }
                                else
                                {
                                    tb_info_aa2.Text += (char)input[i];
                                    flag_no_camera_serial2 = false;
                                }
                            }

                            if (flag_no_camera_serial1 == true)
                            {
                                lb_sn1.Text = "[S/N] : 無相機序號資料1";
                            }
                            else
                            {
                                lb_sn1.Text = tb_info_aa1.Text;
                            }
                            if (flag_no_camera_serial2 == true)
                            {
                                lb_sn2.Text = "[S/N] : 無相機序號資料2";
                            }
                            else
                            {
                                lb_sn2.Text = tb_info_aa2.Text;
                            }

                            if (flag_verify_serial_data == 1)
                            {
                                flag_verify_serial_data = 0;

                                richTextBox1.Text += "AAAAAAAAAAAAAAAAAA flag_verify_serial_data AAAAAAAAAAAAAAAAAAAAAAa\n";

                                int flag_same_serial = 1;
                                for (i = 0; i < 9; i++)
                                {
                                    if (tb_sn1.Text[i] != input[i])
                                    {
                                        flag_same_serial = 0;
                                        break;
                                    }
                                }
                                if (flag_same_serial == 1)
                                {
                                    for (i = 16; i < (16 + 11); i++)
                                    {
                                        if (tb_sn2.Text[i - 16] != input[i])
                                        {
                                            flag_same_serial = 0;
                                            break;
                                        }
                                    }
                                }

                                if (flag_same_serial == 1)
                                {
                                    richTextBox1.Text += "驗證完成, 序號相同\n";
                                    lb_write_camera_serial2.Text += "    驗證完成";
                                    lb_write_camera_serial2.ForeColor = Color.Black;
                                    g2.Clear(BackColor);
                                    g2.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));

                                }
                                else
                                {
                                    richTextBox1.Text += "驗證失敗, 序號不同\n";
                                    lb_write_camera_serial2.Text += "    驗證失敗";
                                    lb_write_camera_serial2.ForeColor = Color.Red;
                                    //groupBox10.BackColor = Color.Red;
                                    g2.Clear(BackColor);
                                    g2.DrawString("驗證失敗", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                                    bt_confirm.Visible = true;

                                }
                                //lb_sn2.Text = "";

                                // Stop timing
                                stopwatch.Stop();
                                richTextBox1.Text += "燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

                                if (stopwatch.ElapsedMilliseconds > 7000)
                                {
                                    flag_burn_long_cnt++;
                                    ////lb_mesg2.Text = "耗時太久 " + flag_burn_long_cnt.ToString() + " 次";
                                }

                                ////lb_mesg3.Text = stopwatch.ElapsedMilliseconds.ToString() + " msec";

                            }











                            if (flag_receive_camera_serial == 1)
                            {
                                flag_receive_camera_serial = 0;
                                flag_wait_receive_data = 0;
                            }

                        }
                        else if (BytesToRead == 55) // 5 + 50
                        {
                            richTextBox1.Text += "BytesToRead = 55 Bytes, data\t";
                            for (int i = 0; i < BytesToRead; i++)
                            {
                                richTextBox1.Text += receive_buffer[i].ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";

                            SpyMonitorRX();

                            richTextBox1.Text += "check received data.............\n";


                            input = "";
                            for (int i = 5; i < (50 + 5); i++)
                                input += (char)receive_buffer[i];

                            if (flag_receive_mb_model_data == 1)
                            {
                                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                bool flag_no_machine_serial = true;
                                bool flag_no_mb_big_serial = true;
                                bool flag_no_mb_small_serial = true;
                                lb_machine_serial.Text = "[主機序號] : ";
                                lb_mb_big_serial.Text = "[大PCBA序號] : ";
                                lb_mb_small_serial.Text = "[小PCBA序號] : ";
                                for (int i = 0; i < 13; i++)
                                {
                                    lb_machine_serial.Text += (char)input[i];
                                    flag_no_machine_serial = false;
                                }
                                for (int i = 13; i < 26; i++)
                                {
                                    lb_mb_big_serial.Text += (char)input[i];
                                    flag_no_mb_big_serial = false;
                                }
                                for (int i = 26; i < 50; i++)
                                {
                                    lb_mb_small_serial.Text += (char)input[i];
                                    flag_no_mb_small_serial = false;
                                }

                                if (flag_no_machine_serial == true)
                                {
                                    lb_machine_serial.Text = "[Model] : 無主機序號資料";
                                }
                                if (flag_no_mb_big_serial == true)
                                {
                                    lb_machine_serial.Text = "[Model] : 無大PCBA序號資料";
                                }
                                if (flag_no_mb_small_serial == true)
                                {
                                    lb_machine_serial.Text = "[Model] : 無小PCBA序號資料";
                                }
                                flag_receive_mb_model_data = 0;
                                flag_wait_receive_data = 0;
                            }
                        }
                        else if (BytesToRead <= 2048)
                        {
                            /*
                            //for UART debug
                            lb_uart_debug.Text += BytesToRead.ToString();
                            lb_uart_debug.Text += ' ';
                            */

                            //資料不是5拜，打印出來。
                            //richTextBox1.Text += "\n得到資料不是5拜 " + DateTime.Now.ToString() + "\t";

                            input = "aa unknown data, len = " + BytesToRead.ToString() + "\n";
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
                            input += ", len = " + BytesToRead.ToString() + "\n";
                            richTextBox1.AppendText(input);     //打印一般文字訊息

                            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                            Write_Log_File(input);
                        }
                        else
                        {
                            serialPort1.DiscardInBuffer();
                            richTextBox1.Text += "丟棄UART buffer內的資料 bbb\n";
                        }
                    }
                    else if (Comport_Mode == 1)  //putty mode
                    {
                        input = "";
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
                        input += "\n";

                        richTextBox1.AppendText(input);     //打印一般文字訊息
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    
                    }
                    else if (Comport_Mode == 2)  //hex mode
                    {
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                        {
                            input += ((int)receive_buffer[i]).ToString("X2") + " ";
                        }
                        richTextBox1.AppendText(input);     //打印一般文字訊息
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
                    richTextBox1.AppendText("[checksum fail] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                        + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + ", abort\n");

                    if (flag_read_connection_again == false)
                        flag_read_connection_again = true;

                    return;
                }

                //richTextBox1.AppendText("[checksum] : " + ((int)input[4]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

                if (isCommandLog == 1)
                {
                    //richTextBox1.AppendText("[RX] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  ");
                    //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

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
                        flag_wait_receive_data = 0;
                        flag_receive_camera_serial = 0;
                        flag_receive_camera_flash_data = 0;
                    }
                    else if (input[1] <= 0x58)  //ims send camera sensor data
                    {
                        int dd = (int)input[3];
                        tb_3.Text = dd.ToString("X2");
                        tb_4.Text = dd.ToString();
                        tb_3a.Text = dd.ToString("X2");
                        tb_4a.Text = dd.ToString();

                        //richTextBox1.Text += "cmd : " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + "\n";

                        if ((input[1] == 0x35) || (input[1] == 0x52) || (input[1] == 0x3A))
                        {
                            if (input[1] == 0x35)
                            {
                                if (input[2] == 0x01)
                                {
                                    data_expo_h = (byte)input[3];
                                    flag_awb_update_expo = true;
                                    //richTextBox1.Text += "eH  ";
                                    if (flag_wait_data_cmd == SENSOR_EXPO)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x02)
                                {
                                    data_expo_l = (byte)input[3];
                                    //richTextBox1.Text += "eL  ";
                                    if (flag_awb_update_expo == true)
                                    {
                                        flag_awb_update_expo = false;
                                        data_expo = (int)data_expo_h * 256 + (int)data_expo_l;
                                        lb_awb_result_expo.Text = "0x" + data_expo.ToString("X2") + " " + data_expo.ToString("D3");
                                        if (flag_update_RGB_scrollbar == true)
                                            numericUpDown_expo.Value = data_expo;
                                        flag_wait_receive_data = 0;
                                    }
                                    if (flag_wait_data_cmd == SENSOR_EXPO)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x0A)
                                {
                                    data_gain_h = (byte)input[3];
                                    flag_awb_update_gain = true;
                                    //richTextBox1.Text += "gH  ";
                                    if (flag_wait_data_cmd == SENSOR_GAIN)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x0B)
                                {
                                    data_gain_l = (byte)input[3];
                                    //richTextBox1.Text += "gL  ";
                                    if (flag_awb_update_gain == true)
                                    {
                                        flag_awb_update_gain = false;
                                        data_gain = (int)data_gain_h * 256 + (int)data_gain_l;
                                        lb_awb_result_gain.Text = "0x" + data_gain.ToString("X2") + " " + data_gain.ToString("D3");
                                        if (flag_update_RGB_scrollbar == true)
                                            numericUpDown_gain.Value = data_gain;
                                    }
                                    if (flag_wait_data_cmd == SENSOR_GAIN)
                                        flag_wait_data_cmd = 0;
                                }
                            }
                            else if (input[1] == 0x52)
                            {
                                if (input[2] == 0x1A)
                                {
                                    data_R_h = (byte)input[3];
                                    flag_awb_update_R = true;
                                    //richTextBox1.Text += "RH  ";
                                    if (flag_wait_data_cmd == SENSOR_RGB_R)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x1B)
                                {
                                    data_R_l = (byte)input[3];
                                    //richTextBox1.Text += "RL  ";
                                    if (flag_awb_update_R == true)
                                    {
                                        flag_awb_update_R = false;
                                        lb_awb_result_R.Text = "0x" + (data_R_h * 256 + data_R_l).ToString("X2") + " " + (data_R_h * 256 + data_R_l).ToString("D3");
                                        data_R = (int)data_R_h * 256 + (int)data_R_l;
                                        if (flag_update_RGB_scrollbar == true)
                                            numericUpDown_R.Value = data_R;
                                    }
                                    if (flag_wait_data_cmd == SENSOR_RGB_R)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x1C)
                                {
                                    data_G_h = (byte)input[3];
                                    flag_awb_update_G = true;
                                    //richTextBox1.Text += "GH  ";
                                    if (flag_wait_data_cmd == SENSOR_RGB_G)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x1D)
                                {
                                    data_G_l = (byte)input[3];
                                    //richTextBox1.Text += "GL  ";
                                    if (flag_awb_update_G == true)
                                    {
                                        flag_awb_update_G = false;
                                        lb_awb_result_G.Text = "0x" + (data_G_h * 256 + data_G_l).ToString("X2") + " " + (data_G_h * 256 + data_G_l).ToString("D3");
                                        data_G = (int)data_G_h * 256 + (int)data_G_l;
                                        if (flag_update_RGB_scrollbar == true)
                                            numericUpDown_G.Value = data_G;
                                    }
                                    if (flag_wait_data_cmd == SENSOR_RGB_G)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x1E)
                                {
                                    data_B_h = (byte)input[3];
                                    flag_awb_update_B = true;
                                    //richTextBox1.Text += "BH  ";
                                    if (flag_wait_data_cmd == SENSOR_RGB_B)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x1F)
                                {
                                    data_B_l = (byte)input[3];
                                    //richTextBox1.Text += "BL\n";
                                    if (flag_awb_update_B == true)
                                    {
                                        flag_awb_update_B = false;
                                        lb_awb_result_B.Text = "0x" + (data_B_h * 256 + data_B_l).ToString("X2") + " " + (data_B_h * 256 + data_B_l).ToString("D3");
                                        data_B = (int)data_B_h * 256 + (int)data_B_l;
                                        flag_wait_receive_data = 0;
                                        if (flag_update_RGB_scrollbar == true)
                                        {
                                            //flag_update_RGB_scrollbar = false;    //always update value
                                            numericUpDown_B.Value = data_B;
                                        }
                                    }
                                    if (flag_wait_data_cmd == SENSOR_RGB_B)
                                        flag_wait_data_cmd = 0;
                                }
                            }
                            else if (input[1] == 0x3A)
                            {
                                if (input[2] == 0x03)
                                {
                                    numericUpDown_wpt.Value = input[3];
                                    tb_wpt.Text = Convert.ToString((Int32)numericUpDown_wpt.Value, 16).ToUpper();
                                    if (flag_wait_data_cmd == SENSOR_WPT)
                                        flag_wait_data_cmd = 0;
                                }
                                else if (input[2] == 0x04)
                                {
                                    numericUpDown_bpt.Value = input[3];
                                    tb_bpt.Text = Convert.ToString((Int32)numericUpDown_bpt.Value, 16).ToUpper();
                                    if (flag_wait_data_cmd == SENSOR_BPT)
                                        flag_wait_data_cmd = 0;
                                }
                            }
                            //richTextBox1.Text += "\n";
                        }
                    }
                    else if (input[1] == 0xA1)
                    {
                        //useless
                        int dd = (int)input[2];
                        tb_3.Text = dd.ToString("X2");
                        tb_4.Text = dd.ToString();
                        tb_3a.Text = dd.ToString("X2");
                        tb_4a.Text = dd.ToString();
                    }
                    else if (input[1] == 0xC1)
                    {
                        flag_receive_camera_serial = 1;
                        richTextBox1.Text += "let flag_receive_camera_serial = 1\n";
                    }
                    else if (input[1] == 0xD1)
                    {
                        flag_receive_camera_flash_data = 1;
                        flag_request_item = input[2];
                    }
                    else if (input[1] == 0xE1)
                    {
                        flag_receive_camera_flash_data = 1;
                        flag_request_item = MODEL_PAGE;
                    }
                    else if (input[1] == 0xF1)
                    {
                        flag_receive_mb_model_data = 1;
                        //flag_request_item = MODEL_PAGE;
                    }
                    else if (input[1] == 0xB1)
                    {
                        flag_receive_ims_rtc_data = 1;
                        flag_request_item = input[2];
                    }
                    else if (input[1] == 0xFF)
                    {
                        g_conn_status = input[2];
                        if (g_conn_status == DONGLE_NONE)
                        {
                            textBox7.Text = "無連接器";
                            textBox7.BackColor = Color.Red;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                        }
                        else if (g_conn_status == CAMERA_NONE)
                        {
                            textBox7.Text = "有連接器, 無相機";
                            textBox7.BackColor = Color.Red;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_none;

                        }
                        else if (g_conn_status == CAMERA_OK)
                        {
                            textBox7.Text = "有連接器, 有相機";
                            textBox7.BackColor = Color.White;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                        }
                        else
                        {
                            textBox7.Text = "狀態不明, status = " + g_conn_status.ToString();
                            textBox7.BackColor = Color.Red;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                        }
                        flag_read_connection_again = true;
                        progressBar1.Value = 100;
                    }
                    else if (input[1] == 0x99)
                    {
                        if ((input[2] == 0x00) && (input[3] == 0x00))
                        {
                            button36.BackgroundImage = imsLink.Properties.Resources.console;
                            button36.BackColor = System.Drawing.SystemColors.ControlLight;
                            button37.BackColor = System.Drawing.SystemColors.ControlLight;
                        }
                        else if ((input[2] == 0x11) && (input[3] == 0x11))
                        {
                            button36.BackgroundImage = imsLink.Properties.Resources.ims3;
                            button35.BackColor = System.Drawing.SystemColors.ControlLight;
                            button36.BackColor = System.Drawing.SystemColors.ControlLight;
                            button37.BackColor = System.Drawing.SystemColors.ControlLight;
                        }
                        else
                        {
                            richTextBox1.Text += "unknown status\n";
                        }
                    }

                }
                else if (input[0] == 0xC2)
                {
                }
                else if (input[0] == 0xCC)
                {
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
                    Write_Log_File(message);
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

        private void button10_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void Comport_Scan()
        {
            string[] tempString = SerialPort.GetPortNames();
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox1.Items.Clear();    //Clear All items in Combobox

            richTextBox1.Text += "共抓到 " + tempString.Length.ToString() + " 個 comport :\n";

            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\n";
                comboBox1.Items.Add(port);
            }

            if (COM_Ports_NameArr.Length > 0)
                comboBox1.Text = COM_Ports_NameArr[0];

            if (COM_Ports_NameArr.Length >= 2)
            {
                comboBox1.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(640, 480);
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
            Comport_Scan();
            lb_a.Text = "";
            lb_b.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
            this.tb_sn2.Focus();
            bt_confirm.Visible = false;
            lb_time1.Text = "";
            lb_time2.Text = "";
            lb_rtc.Text = "";
            lb_camera_model.Text = "";
            lb_machine_serial.Text = "";
            lb_mb_big_serial.Text = "";
            lb_mb_small_serial.Text = "";
            lb_write_camera_model.Text = "";
            lb_write_camera_serial.Text = "";
            lb_write_mb_model.Text = "";
            lb_write_camera_serial2.Text = "";
            lb_zoom.Text = "1.00 X";
            lb_rtc2.Text = "";
            tb_machine_serial.Text = "0000000-B0000";
            tb_mb_big_serial.Text = "0000000000000";
            tb_mb_small_serial.Text = "0000000 0000 000000 0000";
            lb_save_message.Text = "";

            if (flag_release_mode == true)
            {
                tb_sn1.Text = "AA0000000";
                tb_sn2.Text = "00000000000";
            }
            else
            {
                tb_sn1.Text = "AA1234567";
                tb_sn2.Text = "12345678901";
            }

            button12.BackgroundImage = imsLink.Properties.Resources.refresh;
            button15.BackgroundImage = imsLink.Properties.Resources.play_pause;
            button17.BackgroundImage = imsLink.Properties.Resources.plus;
            button18.BackgroundImage = imsLink.Properties.Resources.minus;
            button19.BackgroundImage = imsLink.Properties.Resources.full_screen;
            button20.BackgroundImage = imsLink.Properties.Resources.power;
            button32.BackgroundImage = imsLink.Properties.Resources.console;
            button35.BackgroundImage = imsLink.Properties.Resources.ims3;
            btnUp.BackgroundImage = imsLink.Properties.Resources.up;
            btnDown.BackgroundImage = imsLink.Properties.Resources.down;
            btnLeft.BackgroundImage = imsLink.Properties.Resources.left;
            btnRight.BackgroundImage = imsLink.Properties.Resources.right;
            btnCenter.BackgroundImage = imsLink.Properties.Resources.stop;

            check_webcam();

            /*
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.VideoResolution = Cam.VideoCapabilities[0];
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);     //綁定事件

                Cam.Start();   // WebCam starts capturing images.
                flag_camera_start = 1;
                richTextBox1.Text += "有影像裝置\n";
            }
            else
            {
                //button12.Enabled = true;
                flag_camera_start = 0;
                richTextBox1.Text += "無影像裝置\n";
            }
            */

            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

            if (flag_awb_debug == true)
                bt_goto_awb.Visible = true;
            else
                bt_goto_awb.Visible = false;

            lb_0x1.Visible = false;
            lb_0x2.Visible = false;
            lb_0x3.Visible = false;
            lb_0x4.Visible = false;
            lb_addr.Visible = false;
            lb_data.Visible = false;
            tb_1a.Visible = false;
            tb_2a.Visible = false;
            tb_3a.Visible = false;
            tb_4a.Visible = false;
            bt_read2.Visible = false;
            bt_write2.Visible = false;

            bt_awb.Visible = false;
            bt_awb_test.Visible = false;
            bt_awb_test2.Visible = false;
            bt_awb_test_init.Visible = false;
            bt_disable_timer_webcam.Visible = false;
            bt_erase.Visible = false;
            bt_test.Visible = false;
            bt_clear.Visible = false;
            bt_break.Visible = false;
            pictureBox2.Visible = false;
            lb_range_1.Visible = false;
            lb_range_2.Visible = false;
            lb_expo.Visible = false;
            trackBar_expo.Visible = false;
            tb_expo.Visible = false;
            numericUpDown_expo.Visible = false;
            bt_setup_expo.Visible = false;
            lb_gain.Visible = false;
            trackBar_gain.Visible = false;
            tb_gain.Visible = false;
            numericUpDown_gain.Visible = false;
            bt_setup_gain.Visible = false;

            lb_awb_result_expo.Visible = false;
            lb_awb_result_gain.Visible = false;
            lb_awb_result_R.Visible = false;
            lb_awb_result_G.Visible = false;
            lb_awb_result_B.Visible = false;
            bt_get_setup.Visible = false;

            comboBox_temperature.Visible = false;
            //comboBox_webcam.Visible = false;
            numericUpDown_TG_R.Visible = false;
            numericUpDown_TG_G.Visible = false;
            numericUpDown_TG_B.Visible = false;

            //R
            lb_R.Visible = false;
            lb_0xR.Visible = false;
            lb_range_3.Visible = false;
            trackBar_R.Visible = false;
            tb_R.Visible = false;
            numericUpDown_R.Visible = false;
            bt_setup_R.Visible = false;

            //G
            lb_G.Visible = false;
            lb_0xG.Visible = false;
            lb_range_4.Visible = false;
            trackBar_G.Visible = false;
            tb_G.Visible = false;
            numericUpDown_G.Visible = false;
            bt_setup_G.Visible = false;

            //B
            lb_BB.Visible = false;
            lb_0xB.Visible = false;
            lb_range_5.Visible = false;
            trackBar_B.Visible = false;
            tb_B.Visible = false;
            numericUpDown_B.Visible = false;
            bt_setup_B.Visible = false;

            //WPT
            lb_wpt.Visible = false;
            tb_wpt.Visible = false;
            numericUpDown_wpt.Visible = false;
            bt_read_wpt.Visible = false;
            bt_write_wpt.Visible = false;

            //BPT
            lb_bpt.Visible = false;
            tb_bpt.Visible = false;
            numericUpDown_bpt.Visible = false;
            bt_read_bpt.Visible = false;
            bt_write_bpt.Visible = false;

            g.Clear(BackColor);

            //設定執行後的表單起始位置
            //this.StartPosition = FormStartPosition.Manual;
            //this.Location = new System.Drawing.Point(100, 100);

            // C# 設定視窗載入位置 
            this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            if ((flag_release_mode == true) || (flag_us_debug == true))
            {
                //C# 軟體啟動、版權宣告視窗 
                Frm_Start frm = new Frm_Start();    //實體化Form2視窗物件
                frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                frm.ShowDialog();   //顯示Form2視窗
            }

            this.BackColor = Color.Yellow;

            toolTip1.SetToolTip(button17, "Zoom in");
            toolTip1.SetToolTip(button18, "Zoom out");
            toolTip1.SetToolTip(button12, "Refresh");
            toolTip1.SetToolTip(button16, "Save");
            toolTip1.SetToolTip(button15, "Play/Pause");
            toolTip1.SetToolTip(button19, "2X");
            toolTip1.SetToolTip(btnUp, "Up");
            toolTip1.SetToolTip(btnDown, "Down");
            toolTip1.SetToolTip(btnLeft, "Left");
            toolTip1.SetToolTip(btnRight, "Right");
            toolTip1.SetToolTip(btnCenter, "Default");

            toolTip1.SetToolTip(button10, "Comport Scan");
            toolTip1.SetToolTip(button1, "Comport Connect");
            toolTip1.SetToolTip(button2, "Comport Disconnect");
            toolTip1.SetToolTip(button9, "Reset");
            toolTip1.SetToolTip(button13, "START");
            toolTip1.SetToolTip(button35, "To imsLink Mode");
            toolTip1.SetToolTip(button32, "To PuTTy Mode");
            toolTip1.SetToolTip(button20, "Exit");
            toolTip1.SetToolTip(button33, "log on");


            //以下為提示視窗的設定(通常會設定的部分)
            //ToolTipIcon：設定顯示在提示視窗的圖示類型。
            //toolTip1.ToolTipIcon = ToolTipIcon.Info;
            //ForeColor：前景顏色
            toolTip1.ForeColor = Color.Blue;
            //BackColor：背景顏色
            toolTip1.BackColor = Color.Gray;
            //AutoPopDelay：當游標停滯在控制項，顯示提示視窗的時間。(以毫秒為單位)
            toolTip1.AutoPopDelay = 5000;
            //ToolTipTitle：設定提示視窗的標題。
            //toolTip1.ToolTipTitle = "提示訊息";

            comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y - comboBox_webcam.Height);
            lb_save_message.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y - comboBox_webcam.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString();

            string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
            string weekday = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            //richTextBox1.Text += weekday + "\n";
            lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");
        }

        public double hex2dec(string hex_data)
        {
            byte value = 0;
            double dec_value = 0;
            //MessageBox.Show("data = " + hex_data);
            for (int i = 0; i < hex_data.Length; i++)
            {
                if ((hex_data[i] >= (Char)48 && hex_data[i] <= (Char)57))
                {
                    value = (byte)(hex_data[i] - 48);

                }
                else if ((hex_data[i] >= 'A') && (hex_data[i] <= 'F'))
                {
                    value = (byte)(hex_data[i] - 'A' + 10);
                }
                else if ((hex_data[i] >= 'a') && (hex_data[i] <= 'f'))
                {
                    value = (byte)(hex_data[i] - 'a' + 10);
                }
                dec_value = dec_value * 16 + value;
                //MessageBox.Show("data : " + hex_data[i] + " value : " + value);
            }
            return dec_value;
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            /*
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    //Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                    richTextBox1.Text += "先關閉camera\n";
                }
            }
            */
        }

        bool show_comport_log = SHOW_COMPORT_LOG;
        private void button33_Click(object sender, EventArgs e)
        {
            if (show_comport_log == false)
            {
                show_comport_log = true;
                button33.BackgroundImage = imsLink.Properties.Resources.close_log;
                toolTip1.SetToolTip(button33, "log off");
                this.Width += 520;
            }
            else
            {
                show_comport_log = false;
                button33.BackgroundImage = imsLink.Properties.Resources.open_log;
                toolTip1.SetToolTip(button33, "log on");
                this.Width -= 520;
            }
        }

        private void button34_Click(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = true;
            fontDialog1.ShowColor = true;
            fontDialog1.ShowEffects = true;
            fontDialog1.ShowHelp = true;

            fontDialog1.Font = richTextBox1.Font;
            fontDialog1.Color = richTextBox1.ForeColor;

            if (fontDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Font = fontDialog1.Font;
                richTextBox1.ForeColor = fontDialog1.Color;
            }
        }

        private void button72_Click(object sender, EventArgs e)
        {
            //建立一個檔案
            string filename = "imsLink_log." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".txt";
            StreamWriter sw = File.CreateText(filename);
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button73_Click(object sender, EventArgs e)
        {
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
            //開啟檔案總管
            System.Diagnostics.Process.Start(currentPath);

        }

        private void button74_Click(object sender, EventArgs e)
        {
            if (isCommandLog == 0)
            {
                isCommandLog = 1;
                button74.Text = "CMD off";
                button74.ForeColor = Color.Red;
            }
            else
            {
                isCommandLog = 0;
                button74.Text = "CMD on";
                button74.ForeColor = Color.Green;
            }
        }

        /* old  delay 10000 約 17.2秒
        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
                System.Threading.Thread.Sleep(1);
        }
        */

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

        private void button70_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC] : Putty mode\n");
            Comport_Mode = 1;
            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
        }

        private void button88_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC] : imsLink mode\n");
            Comport_Mode = 0;
            this.richTextBox1.Location = new System.Drawing.Point(958, 67);
            this.richTextBox1.Size = new System.Drawing.Size(500, 586);
        }

        private void button87_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC] : Hex mode\n");
            Comport_Mode = 2;
            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.H:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        //int Comport_Mode = 0;   //0: imsLink, 1: putty mode, 2: hex mode
                        if (Comport_Mode == 0)
                        {
                            Comport_Mode = 1;
                            richTextBox1.AppendText("[PC] : Putty mode\n");
                            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
                            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
                        }
                        else if (Comport_Mode == 1)
                        {
                            Comport_Mode = 2;
                            richTextBox1.AppendText("[PC] : Hex mode\n");
                            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
                            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
                        }
                        if (Comport_Mode == 2)
                        {
                            Comport_Mode = 0;
                            richTextBox1.AppendText("[PC] : imsLink mode\n");
                            this.richTextBox1.Location = new System.Drawing.Point(958, 67);
                            this.richTextBox1.Size = new System.Drawing.Size(382, 594);
                        }
                    }
                    break;
                default:
                    break;
            }
        }

        private void button118_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 1;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button117_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 0;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
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

            if (flag_comport_ok == true)
            {
                //serialPort1.Write(data, 0, data.Length);
                try
                {   //可能會產生錯誤的程式區段
                    serialPort1.Write(data, 0, data.Length);
                }
                /*
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    MessageBox.Show(ex.Message);
                }
                */
                finally
                {
                    //一定會被執行的程式區段
                }
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
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

            if (flag_comport_ok == true)
            {
                serialPort1.Write(data, 0, data.Length);
                flag_wait_receive_data = 1;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt1++;
            cnt1 %= 4;
            
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;

            DongleData = (byte)(0x10 | (cnt1 << 2));

            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
            



        }

        private void button119_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 2;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 

        }

        private void button120_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 3;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
        }

        private void button121_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            DongleData = (byte)trackBar6.Value;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x04;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
        }

        private void trackBar6_Scroll(object sender, EventArgs e)
        {
            tb_exposure.Text = trackBar6.Value.ToString();
        }

        private void trackBar_expo_Scroll(object sender, EventArgs e)
        {
            numericUpDown_expo.Value = trackBar_expo.Value;
        }

        private void trackBar_gain_Scroll(object sender, EventArgs e)
        {
            numericUpDown_gain.Value = trackBar_gain.Value;
        }

        private void tb_exposure_TextChanged(object sender, EventArgs e)
        {
            int exposure = 0;

            if (tb_exposure.Text.Length == 0)
                return;

            exposure = int.Parse(tb_exposure.Text);

            if ((exposure >= 0) && (exposure <= 255))
            {
                trackBar6.Value = exposure;
            }
            else
            {
                richTextBox1.Text += "數字不合法，abort....\n";
                tb_exposure.Text = trackBar6.Value.ToString();
                return;
            }
        }

        private void bt_write_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (tabControl1.SelectedTab == tp_Camera)
            {
                if (comboBox5.SelectedIndex == 0)
                {
                    if (tb_1.Text.Length <= 0)
                        return;
                    if (tb_2.Text.Length <= 0)
                        return;
                    if (tb_3.Text.Length <= 0)
                        return;
                    if (tb_4.Text.Length <= 0)
                        return;
                    cnt1 = 0;   //???
                    int addr_h = Convert.ToInt32(tb_1.Text, 16);
                    int addr_l = Convert.ToInt32(tb_2.Text, 16);
                    DongleAddr_h = (byte)addr_h;
                    DongleAddr_l = (byte)addr_l;
                    DongleData = (byte)int.Parse(tb_4.Text);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
                }
            }
            else if (tabControl1.SelectedTab == tp_USB)
            {
                if (tb_1a.Text.Length <= 0)
                    return;
                if (tb_2a.Text.Length <= 0)
                    return;
                if (tb_3a.Text.Length <= 0)
                    return;
                if (tb_4a.Text.Length <= 0)
                    return;
                cnt1 = 0;   //???
                int addr_h = Convert.ToInt32(tb_1a.Text, 16);
                int addr_l = Convert.ToInt32(tb_2a.Text, 16);
                DongleAddr_h = (byte)addr_h;
                DongleAddr_l = (byte)addr_l;
                DongleData = (byte)int.Parse(tb_4a.Text);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            }
        }

        private void button128_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 1;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button127_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 2;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);

        }

        private void button126_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 3;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button125_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 4;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button129_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt1 = 0;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 + 0);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void tb_3_TextChanged(object sender, EventArgs e)
        {
            if (tb_3.Text.Length == 0)
            {
                tb_4.Text = "";
                return;
            }

            int value = Convert.ToInt32(tb_3.Text, 16);
            tb_4.Text = value.ToString();
        }

        private void tb_3a_TextChanged(object sender, EventArgs e)
        {
            if (tb_3a.Text.Length == 0)
            {
                tb_4a.Text = "";
                return;
            }

            int value = Convert.ToInt32(tb_3a.Text, 16);
            tb_4a.Text = value.ToString();
        }

        private void tb_4_TextChanged(object sender, EventArgs e)
        {
            if (tb_4.Text.Length == 0)
            {
                tb_3.Text = "";
                return;
            }
            int value = int.Parse(tb_4.Text);
            if ((value < 0) || (value > 255))
            {
                tb_4.Text = "";
                tb_3.Text = "";
            }
            else
                tb_3.Text = Convert.ToString(value, 16).ToUpper();
        }

        private void tb_4a_TextChanged(object sender, EventArgs e)
        {
            if (tb_4a.Text.Length == 0)
            {
                tb_3a.Text = "";
                return;
            }
            int value = int.Parse(tb_4a.Text);
            if ((value < 0) || (value > 255))
            {
                tb_4a.Text = "";
                tb_3a.Text = "";
            }
            else
                tb_3a.Text = Convert.ToString(value, 16).ToUpper();
        }

        private void bt_read_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (tabControl1.SelectedTab == tp_Camera)
            {
                if (comboBox5.SelectedIndex == 0)
                {
                    if (tb_1.Text.Length <= 0)
                        return;
                    if (tb_2.Text.Length <= 0)
                        return;
                    tb_3.Text = "";
                    tb_4.Text = "";

                    int addr_h = Convert.ToInt32(tb_1.Text, 16);
                    int addr_l = Convert.ToInt32(tb_2.Text, 16);
                    DongleAddr_h = (byte)addr_h;
                    DongleAddr_l = (byte)addr_l;
                    Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);
                }
            }
            else if (tabControl1.SelectedTab == tp_USB)
            {
                if (tb_1a.Text.Length <= 0)
                    return;
                if (tb_2a.Text.Length <= 0)
                    return;
                tb_3a.Text = "";
                tb_4a.Text = "";
                int addr_h = Convert.ToInt32(tb_1a.Text, 16);
                int addr_l = Convert.ToInt32(tb_2a.Text, 16);
                DongleAddr_h = (byte)addr_h;
                DongleAddr_l = (byte)addr_l;
                Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);
            }
        }

        private void button131_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            xx = 0;
            yy = 0;
            zz = 0xff;
            Send_IMS_Data(0xD0, xx, yy, zz);
        }

        private void button130_Click(object sender, EventArgs e)
        {
            int setup = 0;

            if (cb_0.Checked == true)
                setup |= 1 << 0;
            if (cb_1.Checked == true)
                setup |= 1 << 1;
            if (cb_2.Checked == true)
                setup |= 1 << 2;
            if (cb_3.Checked == true)
                setup |= 1 << 3;

            xx = 0;
            yy = (byte)setup;
            zz = 0;

            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button133_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 5; //lion
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);
        }

        private void button132_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 0; //clear
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button135_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 1; //step_1
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);
        }

        private void button134_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 2; //step_2
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button137_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 3; //step_3
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button136_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 4; //ims_logo
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button138_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 6; //lion 2
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button139_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 7; //lion 3
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button140_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 20; //gdispImageDraw
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button141_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 8; //test new pic
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button142_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 21; //lion test position
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button143_Click(object sender, EventArgs e)
        {
            xx = 2; //picture
            yy = 22; //lion test position
            zz = 0;
            Send_IMS_Data(0xD0, xx, yy, zz);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g2.Clear(BackColor);
            button8.BackColor = Color.Red;
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn2.Clear();
            tb_sn1.BackColor = Color.Gray;
            tb_info_aa1.Clear();
            tb_info_aa2.Clear();
            lb_sn1.Text = "相機序號1 讀取中...";
            lb_sn2.Text = "相機序號2 讀取中...";
            lb_sn3.Text = "";
            lb_write_camera_serial2.Text = "";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                button8.BackColor = System.Drawing.SystemColors.ControlLight;
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-1";
                delay(100);
            }

            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_sn1.Text = "有連接器, 有相機";
                tb_sn1.BackColor = Color.White;
                Get_IMS_Data(0, 0xAA, 0xAA);    //camera serial read

                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                byte page;
                page = 0xa;
                Get_IMS_Data(1, page, 0xAA);    //read camera page 10 for product time
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }
                flag_wait_receive_data = 0;
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
            button8.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button28_Click(object sender, EventArgs e)
        {
            textBox5.Clear();
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int page = Convert.ToInt32(textBox6.Text, 16);
            Send_IMS_Data(0xD1, (byte)page, 0, 0); 
        }

        private void button3_Click(object sender, EventArgs e)
        {
            OperatingSystem OSv = System.Environment.OSVersion;
            richTextBox1.AppendText("imsLink登錄時間 : " + "2017/1/3 03:00下午" + "\n");
            richTextBox1.AppendText("作業系統版本 : " + OSv.ToString() + "\n");
            richTextBox1.AppendText("圖形介面版本 : A02\n");
            richTextBox1.AppendText("韌體版本 : F0" + fw_version.ToString() + "\n");
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("螢幕解析度 : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");
            richTextBox1.AppendText("目前時間 : " + DateTime.Now.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            byte page;
            button4.BackColor = Color.Red;

            tb_info_8.Clear();
            lb_camera_model.Text = "";
            tb_info_82.BackColor = Color.White;

            tb_sn2.Clear();
            tb_info_aa1.BackColor = Color.White;
            tb_info_aa1.Clear();
            tb_info_aa2.BackColor = Color.White;
            tb_info_aa2.Clear();
            tb_info_b.Clear();
            tb_info_8.Clear();
            tb_info_d.Clear();
            tb_info_e.Clear();
            tb_info_f.Clear();
            lb_camera_model.Text = "";
            lb_a.Text = "";
            lb_b.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            tb_info_a2.BackColor = Color.White;
            tb_info_b2.BackColor = Color.White;
            tb_info_82.BackColor = Color.White;
            tb_info_d2.BackColor = Color.White;
            tb_info_e2.BackColor = Color.White;
            tb_info_f2.BackColor = Color.White;
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn1.BackColor = Color.Gray;
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-2xx";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "無連接器";
                tb_info_aa1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_sn1.Text = "有連接器, 有相機";
                tb_sn1.BackColor = Color.White;
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;

                tb_info_8.Text = "[Model] :";
                lb_camera_model.Text = "[Model] :";
                //Send_IMS_Data(0xE1, 0xAB, 0xCD, 0xEF);

                richTextBox1.Text += "\n\n\nread MODEL_PAGE\n";
                //get camera model
                page = MODEL_PAGE;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "m";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread camera serial\n";
                //get camera serial
                Get_IMS_Data(0, 0xAA, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread DATE_PAGE0\n";
                //get camera date_page0 product time
                page = DATE_PAGE0;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "a";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread DATE_PAGE1\n";
                page = DATE_PAGE1;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "b";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread DATE_PAGE3\n";
                page = DATE_PAGE3;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "d";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread ERROR_PAGE\n";
                page = ERROR_PAGE;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "e";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                richTextBox1.Text += "\n\nread ERROR_DATE\n";
                page = ERROR_DATE;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "f";
                    delay(100);
                }
                flag_wait_receive_data = 0;
                richTextBox1.Text += "\n\n";
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
            button4.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            flag_auto_scan_mode = true;
            button25.Text = "到修改模式";
            button40.Text = "到修改模式";

            if (tabControl1.SelectedTab == tp_Connection)
            {
                timer_rtc.Enabled = true;
            }
            else
            {
                timer_rtc.Enabled = false;
            }
            if (tabControl1.SelectedTab == tp_Serial_Auto)
            {
                scanner_timer.Enabled = true;
            }
            else
            {
                scanner_timer.Enabled = false;
            }
            if (tabControl1.SelectedTab == tp_System)
            {
                scanner_timer2.Enabled = true;
            }
            else
            {
                scanner_timer2.Enabled = false;
            }

            if (tabControl1.SelectedTab == tp_USB)
            {
                richTextBox1.Text += "進入USB WebCam\n";
                timer_webcam.Enabled = true;
            }
            else
            {
                richTextBox1.Text += "離開USB WebCam\n";
                timer_webcam.Enabled = false;

                if (flag_fullscreen == true)
                {
                    flag_fullscreen = false;
                    button19.BackgroundImage = imsLink.Properties.Resources.full_screen;
                    richTextBox1.Visible = true;
                    this.richTextBox1.Location = new System.Drawing.Point(958, 67);
                    this.richTextBox1.Size = new System.Drawing.Size(500, 586);
                    this.FormBorderStyle = FormBorderStyle.Sizable;
                    this.WindowState = FormWindowState.Normal;
                    //this.TopMost = false;
                    tabControl1.Size = new Size(948, 616);
                    pictureBox1.Location = new Point(170, 50);
                    pictureBox1.Size = new Size(640, 480);
                    comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y - comboBox_webcam.Height);
                    toolTip1.SetToolTip(button19, "2X");

                    lb_0x1.Visible = false;
                    lb_0x2.Visible = false;
                    lb_0x3.Visible = false;
                    lb_0x4.Visible = false;
                    lb_addr.Visible = false;
                    lb_data.Visible = false;
                    tb_1a.Visible = false;
                    tb_2a.Visible = false;
                    tb_3a.Visible = false;
                    tb_4a.Visible = false;
                    bt_read2.Visible = false;
                    bt_write2.Visible = false;

                    bt_awb.Visible = false;
                    bt_awb_test.Visible = false;
                    bt_awb_test2.Visible = false;
                    bt_awb_test_init.Visible = false;
                    bt_disable_timer_webcam.Visible = false;
                    bt_erase.Visible = false;
                    bt_test.Visible = false;
                    bt_clear.Visible = false;
                    bt_break.Visible = false;
                    pictureBox2.Visible = false;
                    lb_range_1.Visible = false;
                    lb_range_2.Visible = false;
                    lb_expo.Visible = false;
                    trackBar_expo.Visible = false;
                    tb_expo.Visible = false;
                    numericUpDown_expo.Visible = false;
                    bt_setup_expo.Visible = false;
                    lb_gain.Visible = false;
                    trackBar_gain.Visible = false;
                    tb_gain.Visible = false;
                    numericUpDown_gain.Visible = false;
                    bt_setup_gain.Visible = false;

                    lb_awb_result_expo.Visible = false;
                    lb_awb_result_gain.Visible = false;
                    lb_awb_result_R.Visible = false;
                    lb_awb_result_G.Visible = false;
                    lb_awb_result_B.Visible = false;
                    bt_get_setup.Visible = false;

                    comboBox_temperature.Visible = false;
                    //comboBox_webcam.Visible = false;
                    numericUpDown_TG_R.Visible = false;
                    numericUpDown_TG_G.Visible = false;
                    numericUpDown_TG_B.Visible = false;

                    //R
                    lb_R.Visible = false;
                    lb_0xR.Visible = false;
                    lb_range_3.Visible = false;
                    trackBar_R.Visible = false;
                    tb_R.Visible = false;
                    numericUpDown_R.Visible = false;
                    bt_setup_R.Visible = false;

                    //G
                    lb_G.Visible = false;
                    lb_0xG.Visible = false;
                    lb_range_4.Visible = false;
                    trackBar_G.Visible = false;
                    tb_G.Visible = false;
                    numericUpDown_G.Visible = false;
                    bt_setup_G.Visible = false;

                    //B
                    lb_BB.Visible = false;
                    lb_0xB.Visible = false;
                    lb_range_5.Visible = false;
                    trackBar_B.Visible = false;
                    tb_B.Visible = false;
                    numericUpDown_B.Visible = false;
                    bt_setup_B.Visible = false;

                    //WPT
                    lb_wpt.Visible = false;
                    tb_wpt.Visible = false;
                    numericUpDown_wpt.Visible = false;
                    bt_read_wpt.Visible = false;
                    bt_write_wpt.Visible = false;

                    //BPT
                    lb_bpt.Visible = false;
                    tb_bpt.Visible = false;
                    numericUpDown_bpt.Visible = false;
                    bt_read_bpt.Visible = false;
                    bt_write_bpt.Visible = false;
                }
            }

            if (tabControl1.SelectedTab == tp_USB)
            {
                /*
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
                {
                    button12.Enabled = true;
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                }
                else
                {
                    button12.Enabled = false;
                    richTextBox1.Text += "無影像裝置\n";
                }
                */
            }
            else
            {
                /*
                if (Cam != null)
                {
                    if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        //Cam.Stop();   // WebCam stops capturing images.
                        Cam.SignalToStop();
                        Cam.WaitForStop();
                    }
                }
                */
                this.tb_sn2.Focus();
            }
        }

        //寫字的功能
        //畫框的功能
        Graphics gg;
        SolidBrush drawBrush;
        Font drawFont1;
        Font drawFont2;
        Font drawFont3;
        string drawDate;
        int total_R = 0;
        int total_G = 0;
        int total_B = 0;

        int frame_cnt = 0;
        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            int x_st = 0;
            int y_st = 0;
            int ww = awb_block;
            int hh = awb_block;

            if (flag_awb_debug == true)
            {
                frame_cnt++;
                if (frame_cnt == 5)
                {
                    frame_cnt = 0;

                    //Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                    Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone();

                    int WW = bitmap1.Width;
                    int HH = bitmap1.Height;
                    int i;
                    int j;
                    Color pt;
                    x_st = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step;
                    if (x_st < 0)
                        x_st = 0;
                    if ((x_st + ww) > WW)
                        x_st = WW - ww;

                    y_st = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step;
                    if (y_st < 0)
                        y_st = 0;
                    if ((y_st + hh) > HH)
                        y_st = HH - hh;

                    total_R = 0;
                    total_G = 0;
                    total_B = 0;

                    for (j = 0; j < hh; j++)
                    {
                        for (i = 0; i < ww; i++)
                        {
                            pt = bitmap1.GetPixel(x_st + i, y_st + j);
                            total_R += pt.R;
                            total_G += pt.G;
                            total_B += pt.B;
                        }
                    }
                    GC.Collect();       //回收資源
                }
            }

            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //pictureBox1.Image = bm;

            gg = Graphics.FromImage(bm);

            int w = bm.Width;
            int h = bm.Height;

            //設定要抓取的區域
            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * (btn_right_cnt - btn_left_cnt) / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2,
                                             (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4,
                                             w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);

            if (flag_us_debug == true)
            {
                int i;
                for (i = 1; i <= 3; i++)
                {
                    gg.DrawLine(new Pen(Color.Silver, 1), w * i / 4, 0, w * i / 4, h);
                    gg.DrawLine(new Pen(Color.Silver, 1), 0, h * i / 4, w, h * i / 4);
                }
            }
            else
            {
                //寫字的功能
                drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                drawBrush = new SolidBrush(Color.Yellow);
                drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                //drawFont2 = new Font("Arial", 4, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                drawFont3 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                x_st = 10;
                y_st = 10;
                gg.DrawString(drawDate, drawFont1, drawBrush, x_st, y_st);
            }

            if ((flag_awb_debug == true) && (flag_fullscreen == true))
            {
                int hhh = 0;

                int ss = 10;
                int x_st2 = 0;
                int y_st2 = 0;
                Point[] points = new Point[3];

            //畫框的功能

            //if (flag_awb_debug == true)
            //{
                x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step;
                if (x_st < 0)
                    x_st = 0;
                if ((x_st + ww) > w)
                    x_st = w - ww;

                y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step;
                if (y_st < 0)
                    y_st = 0;
                if ((y_st + hh) > h)
                    y_st = h - hh;

                gg.DrawRectangle(new Pen(Color.Silver, 1), x_st, y_st, ww, hh);

                x_st = w / 2 - 100;
                y_st = h / 2 - 100;

                Pen PenStyle = new Pen(Color.Silver, 1);
                // Set the DashStyle property.
                //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
                PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDot;
                //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;
                //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
                //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;

                // Draw a rectangle.
                gg.DrawRectangle(PenStyle, x_st, y_st, 100 * 2, 100 * 2);

                total_RGB_R = total_R;
                total_RGB_G = total_G;
                total_RGB_B = total_B;

                if (total_RGB_R_max < total_RGB_R)
                    total_RGB_R_max = total_RGB_R;
                if (total_RGB_R_min > total_RGB_R)
                    total_RGB_R_min = total_RGB_R;

                if (total_RGB_G_max < total_RGB_G)
                    total_RGB_G_max = total_RGB_G;
                if (total_RGB_G_min > total_RGB_G)
                    total_RGB_G_min = total_RGB_G;

                if (total_RGB_B_max < total_RGB_B)
                    total_RGB_B_max = total_RGB_B;
                if (total_RGB_B_min > total_RGB_B)
                    total_RGB_B_min = total_RGB_B;

                tolerance = ww * hh / tolerance_ratio;
                string rgb_value;
                x_st = 0;

                y_st = 250;
                if ((total_RGB_R >= (TARGET_AWB_R * ww * hh - tolerance)) && (total_RGB_R <= (TARGET_AWB_R * ww * hh + tolerance)))
                {
                    drawBrush = new SolidBrush(Color.Gray);
                    rgb_value = ((float)total_RGB_R / (ww * hh)).ToString("F2");
                    if (rgb_check_cnt < CHECK_AWB_FRAME)
                    {
                        rgb_r_ok_cnt++;
                    }
                }
                else
                {
                    //drawBrush = new SolidBrush(Color.Red);
                    if (total_RGB_R < (TARGET_AWB_R * ww * hh - tolerance))
                    {
                        rgb_value = ((float)total_RGB_R / (ww * hh)).ToString("F2") + "-";
                        drawBrush = new SolidBrush(Color.Pink);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_r_fail_low_cnt++;
                        }
                    }
                    else
                    {
                        rgb_value = ((float)total_RGB_R / (ww * hh)).ToString("F2") + "+";
                        drawBrush = new SolidBrush(Color.DarkRed);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_r_fail_high_cnt++;
                        }
                    }
                }

                if ((total_RGB_R >= (TARGET_AWB_R * ww * hh - tolerance)) && (total_RGB_R <= (TARGET_AWB_R * ww * hh + tolerance)))
                {
                    flag_R_OK = true;
                }
                else
                {
                    flag_R_OK = false;
                }
                //rgb_value = ((float)total_RGB_R / (ww * hh)).ToString("F2");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                if ((flag_do_awb == true) && (flag_display_r_do_awb == true))
                {
                    if (diff_r > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString(diff_r.ToString(), drawFont2, new SolidBrush(Color.Red), x_st + 101, y_st + 7);
                    }
                    else if (diff_r < 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[2] = new Point(x_st2 + 0, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2);
                        points[0] = new Point(x_st2 + ss / 2, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Green), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString((-diff_r).ToString(), drawFont2, new SolidBrush(Color.Green), x_st + 101, y_st + 7);
                    }
                }

                gg.DrawRectangle(new Pen(Color.Red, 1), x_st + 96 + 22, y_st + 1, 8, 24);
                if (TARGET_AWB_R < 255)
                {
                    hhh = (int)((24 * (total_RGB_R - (TARGET_AWB_R - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance * 2));
                }
                else
                {
                    hhh = (int)((24 * (total_RGB_R - (TARGET_AWB_R - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance));
                }
                if (hhh < -5)
                {
                    hhh = -5;
                }
                else if (hhh > (24 + 5))
                {
                    hhh = 24 + 5;
                }
                gg.DrawLine(new Pen(Color.Red, 1), x_st + 96 - 2 + 20, y_st + 1 + 24 - hhh, x_st + 96 - 2 + 36, y_st + 1 + 24 - hhh);

                if (TARGET_AWB_R < 255)
                    rgb_value = ((float)TARGET_AWB_R + (1 - 0.01) / tolerance_ratio).ToString("F2");
                else
                    rgb_value = ((float)TARGET_AWB_R).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Red), x_st + 92 + 38, y_st - 2);
                rgb_value = ((float)TARGET_AWB_R - 1 / (float)tolerance_ratio).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Red), x_st + 92 + 38, y_st + 16);

                y_st = 290;
                if ((total_RGB_G >= (TARGET_AWB_G * ww * hh - tolerance)) && (total_RGB_G <= (TARGET_AWB_G * ww * hh + tolerance)))
                {
                    drawBrush = new SolidBrush(Color.Gray);
                    rgb_value = ((float)total_RGB_G / (ww * hh)).ToString("F2");
                    if (rgb_check_cnt < CHECK_AWB_FRAME)
                    {
                        rgb_g_ok_cnt++;
                    }
                }
                else
                {
                    //drawBrush = new SolidBrush(Color.Green);
                    if (total_RGB_G < (TARGET_AWB_G * ww * hh - tolerance))
                    {
                        rgb_value = ((float)total_RGB_G / (ww * hh)).ToString("F2") + "-";
                        drawBrush = new SolidBrush(Color.LightGreen);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_g_fail_low_cnt++;
                        }
                    }
                    else
                    {
                        rgb_value = ((float)total_RGB_G / (ww * hh)).ToString("F2") + "+";
                        drawBrush = new SolidBrush(Color.DarkGreen);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_g_fail_high_cnt++;
                        }
                    }
                }
                if ((total_RGB_G >= (TARGET_AWB_G * ww * hh - tolerance)) && (total_RGB_G <= (TARGET_AWB_G * ww * hh + tolerance)))
                {
                    flag_G_OK = true;
                }
                else
                {
                    flag_G_OK = false;
                }
                //rgb_value = ((float)total_RGB_G / (ww * hh)).ToString("F2");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                if ((flag_do_awb == true) && (flag_display_g_do_awb == true))
                {
                    if (diff_g > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString(diff_g.ToString(), drawFont2, new SolidBrush(Color.Red), x_st + 101, y_st + 7);
                    }
                    else if (diff_g < 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[2] = new Point(x_st2 + 0, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2);
                        points[0] = new Point(x_st2 + ss / 2, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Green), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString((-diff_g).ToString(), drawFont2, new SolidBrush(Color.Green), x_st + 101, y_st + 7);
                    }
                }

                gg.DrawRectangle(new Pen(Color.Green, 1), x_st + 96 + 22, y_st + 1, 8, 24);
                if (TARGET_AWB_G < 255)
                {
                    hhh = (int)((24 * (total_RGB_G - (TARGET_AWB_G - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance * 2));
                }
                else
                {
                    hhh = (int)((24 * (total_RGB_G - (TARGET_AWB_G - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance));
                }
                if (hhh < -5)
                {
                    hhh = -5;
                }
                else if (hhh > (24 + 5))
                {
                    hhh = 24 + 5;
                }
                gg.DrawLine(new Pen(Color.Green, 1), x_st + 96 - 2 + 20, y_st + 1 + 24 - hhh, x_st + 96 - 2 + 36, y_st + 1 + 24 - hhh);

                if (TARGET_AWB_G < 255)
                    rgb_value = ((float)TARGET_AWB_G + (1 - 0.01) / tolerance_ratio).ToString("F2");
                else
                    rgb_value = ((float)TARGET_AWB_G).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Green), x_st + 92 + 38, y_st - 2);
                rgb_value = ((float)TARGET_AWB_G - 1 / (float)tolerance_ratio).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Green), x_st + 92 + 38, y_st + 16);

                y_st = 330;
                if ((total_RGB_B >= (TARGET_AWB_B * ww * hh - tolerance)) && (total_RGB_B <= (TARGET_AWB_B * ww * hh + tolerance)))
                {
                    drawBrush = new SolidBrush(Color.Gray);
                    rgb_value = ((float)total_RGB_B / (ww * hh)).ToString("F2");
                    if (rgb_check_cnt < CHECK_AWB_FRAME)
                    {
                        rgb_check_cnt++;
                        rgb_b_ok_cnt++;
                    }
                }
                else
                {
                    //drawBrush = new SolidBrush(Color.Blue);
                    if (total_RGB_B < (TARGET_AWB_B * ww * hh - tolerance))
                    {
                        rgb_value = ((float)total_RGB_B / (ww * hh)).ToString("F2") + "-";
                        drawBrush = new SolidBrush(Color.LightBlue);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_check_cnt++;
                            rgb_b_fail_low_cnt++;
                        }
                    }
                    else
                    {
                        rgb_value = ((float)total_RGB_B / (ww * hh)).ToString("F2") + "+";
                        drawBrush = new SolidBrush(Color.DarkBlue);
                        if (rgb_check_cnt < CHECK_AWB_FRAME)
                        {
                            rgb_check_cnt++;
                            rgb_b_fail_high_cnt++;
                        }
                    }
                }
                if (rgb_check_cnt == CHECK_AWB_FRAME)
                {
                    rgb_check_cnt++;
                    flag_check_rgb = false;
                    //richTextBox1.Text += "already " + CHECK_AWB_FRAME.ToString() + " frames\n";
                }

                if ((total_RGB_B >= (TARGET_AWB_B * ww * hh - tolerance)) && (total_RGB_B <= (TARGET_AWB_B * ww * hh + tolerance)))
                {
                    flag_B_OK = true;
                }
                else
                {
                    flag_B_OK = false;
                }
                //rgb_value = ((float)total_RGB_B / (ww * hh)).ToString("F2");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                if ((flag_do_awb == true) && (flag_display_b_do_awb == true))
                {
                    if (diff_b > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString(diff_b.ToString(), drawFont2, new SolidBrush(Color.Red), x_st + 101, y_st + 7);
                    }
                    else if (diff_b < 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[2] = new Point(x_st2 + 0, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2);
                        points[0] = new Point(x_st2 + ss / 2, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Green), points);

                        drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                        gg.DrawString((-diff_b).ToString(), drawFont2, new SolidBrush(Color.Green), x_st + 101, y_st + 7);
                    }
                }

                gg.DrawRectangle(new Pen(Color.Blue, 1), x_st + 96 + 22, y_st + 1, 8, 24);
                if (TARGET_AWB_B < 255)
                {
                    hhh = (int)((24 * (total_RGB_B - (TARGET_AWB_B - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance * 2));
                }
                else
                {
                    hhh = (int)((24 * (total_RGB_B - (TARGET_AWB_B - 1 / (float)tolerance_ratio) * ww * hh)) / (tolerance));
                }

                if (hhh < -5)
                {
                    hhh = -5;
                }
                else if (hhh > (24 + 5))
                {
                    hhh = 24 + 5;
                }
                gg.DrawLine(new Pen(Color.Blue, 1), x_st + 96 - 2 + 20, y_st + 1 + 24 - hhh, x_st + 96 - 2 + 36, y_st + 1 + 24 - hhh);

                if (TARGET_AWB_B < 255)
                    rgb_value = ((float)TARGET_AWB_B + (1 - 0.01) / tolerance_ratio).ToString("F2");
                else
                    rgb_value = ((float)TARGET_AWB_B).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Blue), x_st + 92 + 38, y_st - 2);
                rgb_value = ((float)TARGET_AWB_B - 1 / (float)tolerance_ratio).ToString("F2");
                gg.DrawString(rgb_value, drawFont3, new SolidBrush(Color.Blue), x_st + 92 + 38, y_st + 16);

                y_st = 370;
                drawBrush = new SolidBrush(Color.Red);
                rgb_value = total_R.ToString() + "   " + (((float)total_R) / awb_block / awb_block).ToString("F3");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                y_st = 410;
                drawBrush = new SolidBrush(Color.Green);
                rgb_value = total_G.ToString() + "   " + (((float)total_G) / awb_block / awb_block).ToString("F3");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                y_st = 450;
                drawBrush = new SolidBrush(Color.Blue);
                rgb_value = total_B.ToString() + "   " + (((float)total_B) / awb_block / awb_block).ToString("F3");
                gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);

                if (flag_check_rgb_saturation == true)
                {
                    if (rgb_saturation_check_cnt < CHECK_SATURATION_FRAME)
                    {
                        rgb_saturation_check_cnt++;

                        if (total_RGB_R == 255 * awb_block * awb_block)
                        {
                            rgb_r_saturation_cnt++;
                        }
                        if (total_RGB_G == 255 * awb_block * awb_block)
                        {
                            rgb_g_saturation_cnt++;
                        }
                        if (total_RGB_B == 255 * awb_block * awb_block)
                        {
                            rgb_b_saturation_cnt++;
                        }
                    }
                    if (rgb_saturation_check_cnt == CHECK_SATURATION_FRAME)
                    {
                        rgb_saturation_check_cnt++;
                        flag_check_rgb_saturation = false;
                        //richTextBox1.Text += "already " + CHECK_SATURATION_FRAME.ToString() + " frames\n";
                    }
                }

            }
            usb_camera_width = w;
            usb_camera_height = h;
            pictureBox1.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);

            GC.Collect();       //回收資源
        }

        bool flag_ok_camera_serial1 = false;
        bool flag_ok_camera_serial2 = false;
        private void scanner_timer_Tick(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
                return;

            richTextBox1.Text += "A";
            if ((cnt3 % 1) == 0)
            {
                this.tb_wait_camera_data.Focus();
            }

            if (tb_wait_camera_data.Text.Length > 0)
            {
                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_camera_data.Text.Length == 9)
                {
                    //檢查英文字母的正確性
                    if (((tb_wait_camera_data.Text[0] >= 'A') && (tb_wait_camera_data.Text[0] <= 'Z')) || ((tb_wait_camera_data.Text[0] >= 'a') && (tb_wait_camera_data.Text[0] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b0\n";
                        tb_sn1.Text = "SN1格式不正確b0\n";
                    }

                    if (((tb_wait_camera_data.Text[1] >= 'A') && (tb_wait_camera_data.Text[1] <= 'Z')) || ((tb_wait_camera_data.Text[1] >= 'a') && (tb_wait_camera_data.Text[1] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b1\n";
                        tb_sn1.Text = "SN1格式不正確b1\n";
                    }


                    for (i = 2; i < 9; i++)
                    {
                        if ((tb_wait_camera_data.Text[i] < '0') || (tb_wait_camera_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "SN1格式不正確b\n";
                            tb_sn1.Text = "SN1格式不正確b\n";
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得 SN1序號 : " + tb_wait_camera_data.Text + "\n";
                        tb_sn1.Text = tb_wait_camera_data.Text;
                        tb_sn1.BackColor = Color.White;
                        tb_wait_camera_data.Text = "";
                        flag_ok_camera_serial1 = true;
                    }
                }
                else if (tb_wait_camera_data.Text.Length == 11)
                {
                    for (i = 0; i < 11; i++)
                    {
                        if ((tb_wait_camera_data.Text[i] < '0') || (tb_wait_camera_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "SN2格式不正確b\n";
                            tb_sn2.Text = "SN2格式不正確\n";
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得 SN2序號 : " + tb_wait_camera_data.Text + "\n";
                        tb_sn2.Text = tb_wait_camera_data.Text;
                        tb_sn2.BackColor = Color.White;
                        tb_wait_camera_data.Text = "";
                        flag_ok_camera_serial2 = true;
                    }
                }
                else if (tb_wait_camera_data.Text.Length == 14)
                {
                    if (flag_ok_to_write_data == true)
                    {
                        if (tb_wait_camera_data.Text == "IMS EGD SYSTEM")
                        {
                            if (flag_comport_ok == false)
                            {
                                richTextBox1.Text += "未連線comport, abort\n";
                                tb_wait_camera_data.Text = "";
                                return;
                            }

                            tb_wait_camera_data.Text = "";
                            flag_incorrect_data = false;
                            richTextBox1.Text += "資料正確, 開始燒錄\n";
                            panel9.BackgroundImage = null;
                            g2.Clear(BackColor);
                            button11_Click(sender, e);  //執行燒錄按鍵
                            flag_incorrect_data = true;
                            flag_ok_camera_serial1 = false;
                            flag_ok_camera_serial2 = false;
                            flag_ok_to_write_data = false;
                            return;
                        }
                        else
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料錯誤\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "資料未齊全, 忽略\n";
                        tb_wait_camera_data.Text = "";
                        lb_write_camera_serial2.Text = "";

                        if (flag_ok_camera_serial1 == false)
                        {
                            tb_sn1.Text = "";
                        }
                        if (flag_ok_camera_serial2 == false)
                        {
                            tb_sn2.Text = "";
                        }
                        g2.Clear(BackColor);
                        return;
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                }

                if (flag_incorrect_data == true)
                {
                    richTextBox1.Text += "資料錯誤,長度 " + tb_wait_camera_data.Text.Length.ToString() + "\t內容 " + tb_wait_camera_data.Text + "\n";
                    tb_wait_camera_data.Text = "";
                }
                else
                {
                    richTextBox1.Text += "資料正確\n";

                    if (flag_ok_camera_serial1 == false)
                    {
                        tb_sn1.Text = "";
                        //lb_write_camera_serial2.Text = "";
                        panel9.BackgroundImage = null;
                        g2.Clear(BackColor);
                    }
                    if (flag_ok_camera_serial2 == false)
                    {
                        tb_sn2.Text = "";
                        //lb_write_camera_serial2.Text = "";
                        panel9.BackgroundImage = null;
                        g2.Clear(BackColor);
                    }
                    if ((flag_ok_camera_serial1 == true) && (flag_ok_camera_serial2 == true))
                    {
                        lb_write_camera_serial2.Text = "準備燒錄";
                        lb_write_camera_serial2.ForeColor = Color.Black;
                        richTextBox1.Text += "準備燒錄\n";
                        flag_ok_to_write_data = true;
                        panel9.BackgroundImage = imsLink.Properties.Resources.ims_egd_system;
                    }
                }
                tb_wait_camera_data.Text = "";
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            /*
            if (flag_wait_receive_data == 1)
                richTextBox1.Text += ".";
            */
        }

        private void button5_Click(object sender, EventArgs e)
        {
            tb_sn2.Clear();
            tb_info_aa1.Clear();
            tb_info_aa2.Clear();
            tb_info_b.Clear();
            tb_info_8.Clear();
            tb_info_d.Clear();
            tb_info_e.Clear();
            tb_info_f.Clear();
            lb_a.Text = "";
            lb_b.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            lb_camera_model.Text = "";
            tb_info_a2.BackColor = Color.White;
            tb_info_b2.BackColor = Color.White;
            tb_info_82.BackColor = Color.White;
            tb_info_d2.BackColor = Color.White;
            tb_info_e2.BackColor = Color.White;
            tb_info_f2.BackColor = Color.White;
            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            lb_write_camera_serial2.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
            tb_sn1.Text = "";
            tb_sn2.Text = "";
            //groupBox10.BackColor = System.Drawing.SystemColors.ControlLightLight;
            lb_write_camera_serial2.Text += "";
            lb_write_camera_serial2.ForeColor = Color.Black;

            bt_confirm.Visible = false;
        }

        //int camera_start = 0;
        private void button12_Click_1(object sender, EventArgs e)
        {
            if ((flag_camera_start == 1) && (Cam.IsRunning == true))
            {
                richTextBox1.Text += "USB影像傳輸中\n";
            }
            else
            {
                richTextBox1.Text += "重新抓取USB影像\t";
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
                {
                    //button12.Enabled = false;
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                    Cam.Start();   // WebCam starts capturing images.
                    flag_camera_start = 1;
                    richTextBox1.Text += "有影像裝置\n";
                }
                else
                {
                    //button12.Enabled = true;
                    flag_camera_start = 0;
                    richTextBox1.Text += "無影像裝置\n";
                }
            }
            /*
            if (camera_start == 0)
            {
                camera_start = 1;
                button12.Text = "Stop";
                Cam.Start();   // WebCam starts capturing images.
            }
            else
            {
                camera_start = 0;
                button12.Text = "Start";
                //Cam.Stop();  // WebCam stops capturing images.
                Cam.SignalToStop();
                Cam.WaitForStop();
            }
            */
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    //Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }

        }

        private void button13_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xAA, 0xBB, 0xCC);
        }

        int flag_camera_is_stopped = 0;
        private void button15_Click(object sender, EventArgs e)
        {
            /*
            if (flag_camera_start == 1)
            {
                if (flag_camera_is_stopped == 0)
                {
                    //Cam.Stop();
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                    flag_camera_is_stopped = 1;
                    richTextBox1.Text += "停止\n";
                }
                else
                {
                    Cam.Start();
                    flag_camera_is_stopped = 0;
                    richTextBox1.Text += "繼續\n";
                }
            }
            */
            if (flag_camera_start == 1)
            {
                if (flag_camera_is_stopped == 0)
                {
                    flag_camera_is_stopped = 1;
                    richTextBox1.Text += "停止\n";
                    enable_camera_streaming(false);
                }
                else
                {
                    flag_camera_is_stopped = 0;
                    richTextBox1.Text += "繼續\n";
                    enable_camera_streaming(true);
                }
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                if (flag_us_debug == false)
                {
                    int xPos = 10;
                    int yPos = 10;
                    string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

                    g.ReleaseHdc();
                    g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
                }
                else
                {
                    g.ReleaseHdc();
                }

                g.Dispose();

                String file = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_hhmmss");
                //String file1 = file + ".jpg";
                String file2 = file + ".bmp";
                //String file3 = file + ".png";

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(@file2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + file2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                lb_save_message.Text = "已存檔";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                lb_save_message.Text = "無圖可存";
            }
            timer_display.Enabled = true;
            timer_display_save_count = 0;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            if (zoom_cnt < zoom_cnt_max)
            {
                zoom_cnt++;
                //pictureBox1.Size = new Size(pictureBox1.Size.Width + zoom_step, pictureBox1.Size.Height + zoom_step * 3 / 4);
                //pictureBox1.Size = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);
                //pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

                int w = usb_camera_width;
                int h = usb_camera_height;
                richTextBox1.Text += "zoom_cnt = " + zoom_cnt.ToString() + "\tx_st = " + (zoom_step * zoom_cnt / 2).ToString() + "\ty_st = " + (zoom_step * zoom_cnt / 2 * 3 / 4).ToString()
                    + "\tW = " + (w - zoom_step * zoom_cnt).ToString() + "\tH = " + (h - zoom_step * zoom_cnt * 3 / 4).ToString() + "\n";

                float ratio;
                ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                lb_zoom.Text = ratio.ToString("#0.00") + " X";
            }
            else
                richTextBox1.Text += "已達最大放大倍率\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (zoom_cnt > 0)
            {
                int w = usb_camera_width;
                int h = usb_camera_height;
                int x_st =  zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W = w - zoom_step * zoom_cnt;
                int H = h - zoom_step * zoom_cnt * 3 / 4;
                //richTextBox1.Text += "原抓取位置 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " W = " + W.ToString() + " H = " + H.ToString() + "\n";

                int x_st_next = zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_right_left_cnt / 2;
                int y_st_next = (zoom_step * (zoom_cnt - 1) / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                int W2 = w - zoom_step * (zoom_cnt - 1) + x_st_next;
                int H2 = h - zoom_step * (zoom_cnt - 1) * 3 / 4 + y_st_next;

                //richTextBox1.Text += "x_st_next = " + x_st_next.ToString() + " y_st_next = " + y_st_next.ToString() + "\n";
                if (x_st_next < 0)
                {
                    richTextBox1.Text += "已到左邊界, 不動作left, 回走, 向右一步\n";
                    btn_right_left_cnt++;
                }
                if (y_st_next < 0)
                {
                    richTextBox1.Text += "已到上邊界, 不動作up, 回走, 向下一步\n";
                    btn_down_up_cnt++;
                }
                if (W2 > 640)
                {
                    richTextBox1.Text += "已到右邊界, 不動作right, 回走, 向左一步\n";
                    btn_right_left_cnt--;
                }
                if (H2 > 480)
                {
                    richTextBox1.Text += "已到下邊界, 不動作down, 回走, 向上一步\n";
                    btn_down_up_cnt--;
                }

                {
                    zoom_cnt--;
                    x_st = zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2;
                    y_st = (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4;
                    W = w - zoom_step * zoom_cnt;
                    H = h - zoom_step * zoom_cnt * 3 / 4;
                    //richTextBox1.Text += "後抓取位置 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " W = " + W.ToString() + " H = " + H.ToString() + "\n";
                }

                //pictureBox1.Size = new Size(pictureBox1.Size.Width - zoom_step, pictureBox1.Size.Height - zoom_step * 3 / 4);
                //pictureBox1.Size = new Size(pictureBox1.Size.Width, pictureBox1.Size.Height);
                //pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

                //int w = usb_camera_width;
                //int h = usb_camera_height;

                /*
                richTextBox1.Text += "zoom_cnt = " + zoom_cnt.ToString() + "\tx_st = " + (zoom_step * zoom_cnt / 2).ToString() + "\ty_st = " + (zoom_step * zoom_cnt / 2 * 3 / 4).ToString()
                    + "\tW = " + (w - zoom_step * zoom_cnt).ToString() + "\tH = " + (h - zoom_step * zoom_cnt * 3 / 4).ToString() + "\n";
                */
                float ratio;
                ratio = 640 / (float)(w - zoom_step * zoom_cnt);
                lb_zoom.Text = ratio.ToString("#0.00") + " X";
            }
            else
                richTextBox1.Text += "已達最小放大倍率\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;
                button19.BackgroundImage = imsLink.Properties.Resources.normal_screen;
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.TopMost = true;
                tabControl1.Size = new Size(1600 + 300, 1010);
                //pictureBox1.Size = new Size(1120, 840);
                pictureBox1.Size = new Size(640 * 2, 480 * 2);
                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y);
                toolTip1.SetToolTip(button19, "1X");

                if (flag_awb_debug == true)
                {
                    pictureBox1.Location = new Point(170 + 400 + 30, 15);
                    this.richTextBox1.Location = new System.Drawing.Point(170, 90);
                    this.richTextBox1.Size = new System.Drawing.Size(400 + 30, 470);
                    lb_0x1.Visible = true;
                    lb_0x2.Visible = true;
                    lb_0x3.Visible = true;
                    lb_0x4.Visible = true;
                    lb_addr.Visible = true;
                    lb_data.Visible = true;
                    tb_1a.Visible = true;
                    tb_2a.Visible = true;
                    tb_3a.Visible = true;
                    tb_4a.Visible = true;
                    bt_read2.Visible = true;
                    bt_write2.Visible = true;

                    bt_awb.Visible = true;
                    bt_awb_test.Visible = true;
                    bt_awb_test2.Visible = true;
                    bt_awb_test_init.Visible = true;
                    bt_disable_timer_webcam.Visible = true;
                    bt_erase.Visible = true;
                    bt_test.Visible = true;
                    bt_clear.Visible = true;
                    bt_break.Visible = true;
                    pictureBox2.Visible = true;
                    lb_range_1.Visible = true;
                    lb_range_2.Visible = true;
                    lb_expo.Visible = true;
                    trackBar_expo.Visible = true;
                    tb_expo.Visible = true;
                    numericUpDown_expo.Visible = true;
                    bt_setup_expo.Visible = true;
                    lb_gain.Visible = true;
                    trackBar_gain.Visible = true;
                    tb_gain.Visible = true;
                    numericUpDown_gain.Visible = true;
                    bt_setup_gain.Visible = true;

                    lb_awb_result_expo.Visible = true;
                    lb_awb_result_gain.Visible = true;
                    lb_awb_result_R.Visible = true;
                    lb_awb_result_G.Visible = true;
                    lb_awb_result_B.Visible = true;
                    bt_get_setup.Visible = true;

                    comboBox_temperature.Visible = true;
                    //comboBox_webcam.Visible = true;
                    numericUpDown_TG_R.Visible = true;
                    numericUpDown_TG_G.Visible = true;
                    numericUpDown_TG_B.Visible = true;

                    //R
                    lb_R.Visible = true;
                    lb_0xR.Visible = true;
                    lb_range_3.Visible = true;
                    trackBar_R.Visible = true;
                    tb_R.Visible = true;
                    numericUpDown_R.Visible = true;
                    bt_setup_R.Visible = true;

                    //G
                    lb_G.Visible = true;
                    lb_0xG.Visible = true;
                    lb_range_4.Visible = true;
                    trackBar_G.Visible = true;
                    tb_G.Visible = true;
                    numericUpDown_G.Visible = true;
                    bt_setup_G.Visible = true;

                    //B
                    lb_BB.Visible = true;
                    lb_0xB.Visible = true;
                    lb_range_5.Visible = true;
                    trackBar_B.Visible = true;
                    tb_B.Visible = true;
                    numericUpDown_B.Visible = true;
                    bt_setup_B.Visible = true;

                    //WPT
                    lb_wpt.Visible = true;
                    tb_wpt.Visible = true;
                    numericUpDown_wpt.Visible = true;
                    bt_read_wpt.Visible = true;
                    bt_write_wpt.Visible = true;

                    //BPT
                    lb_bpt.Visible = true;
                    tb_bpt.Visible = true;
                    numericUpDown_bpt.Visible = true;
                    bt_read_bpt.Visible = true;
                    bt_write_bpt.Visible = true;


                    bt_awb_test_init.Location = new Point(170, 500);
                    bt_awb_test.Location = new Point(170 + 70, 500);
                    bt_awb_test2.Location = new Point(170 + 70 * 2, 500);
                    bt_break.Location = new Point(170 + 70 * 3, 500);
                    bt_awb.Location = new Point(170 + 70 * 4, 500);
                    bt_disable_timer_webcam.Location = new Point(170 + 70 * 5, 500);
                    bt_erase.Location = new Point(170 + 70 * 2, 500 + 40);
                    bt_test.Location = new Point(170 + 70 * 4, 500 + 40);
                    bt_clear.Location = new Point(170 + 70 * 5, 500 + 40);

                    lb_addr.Location = new Point(30, 620 - 100 + 30);
                    lb_0x1.Location = new Point(5, 650 + 3 - 100 + 30);
                    tb_1a.Location = new Point(30, 650 - 100 + 30);
                    tb_2a.Location = new Point(100, 650 - 100 + 30);

                    lb_data.Location = new Point(30 + 200, 620 - 100 + 30);
                    lb_0x2.Location = new Point(5 + 200, 650 + 3 - 100 + 30);
                    tb_3a.Location = new Point(30 + 200, 650 - 100 + 30);
                    tb_4a.Location = new Point(100 + 200, 650 - 100 + 30);

                    bt_read2.Location = new Point(410 + 45 - 80, 650 - 100 + 30);
                    bt_write2.Location = new Point(480 + 45 - 80, 650 - 100 + 30);

                    lb_awb_result_expo.Location = new Point(5 + 102 * 0, 720 - 120 + 30);
                    lb_awb_result_gain.Location = new Point(5 + 102 * 1 + 10, 720 - 120 + 30);
                    lb_awb_result_R.Location = new Point(5 + 102 * 2 + 10, 720 - 120 + 30);
                    lb_awb_result_G.Location = new Point(5 + 102 * 3 + 28*1 + 10, 720 - 120 + 30);
                    lb_awb_result_B.Location = new Point(5 + 102 * 4 + 28*2, 720 - 120 + 30);

                    lb_awb_result_expo.ForeColor = Color.Silver;
                    lb_awb_result_gain.ForeColor = Color.Gold;
                    lb_awb_result_R.ForeColor = Color.Red;
                    lb_awb_result_G.ForeColor = Color.Green;
                    lb_awb_result_B.ForeColor = Color.Blue;

                    bt_get_setup.Location = new Point(480 + 45, 720 - 120 + 15 - 20);

                    //EXPO
                    lb_expo.Location = new Point(30 / 2, 720 - 120 + 60);
                    lb_0x3.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 3 - 130 + 60);
                    lb_range_1.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 3 - 130 + 30 + 60);
                    lb_range_1.Text = "0~1FF           0~511";
                    trackBar_expo.Location = new Point(30 / 2, 750 - 130 + 60);
                    numericUpDown_expo.Location = new Point(410 + 45, 750 - 130 + 60);
                    tb_expo.Location = new Point(410 + 45 - 80, 750 - 130 + 60);
                    bt_setup_expo.Location = new Point(480 + 45, 750 - 130 + 60);

                    //GAIN
                    lb_gain.Location = new Point(30 / 2, 720 + 100 - 50 - 90 + 50);
                    lb_0x4.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 - 90 + 50);
                    lb_range_2.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 - 90 + 30 + 50);
                    lb_range_2.Text = "0~1FF           0~511";
                    trackBar_gain.Location = new Point(30 / 2, 750 + 100 - 50 - 10 - 90 + 50);
                    numericUpDown_gain.Location = new Point(410 + 45, 750 + 100 - 50 - 10 - 90 + 50);
                    tb_gain.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 - 90 + 50);
                    bt_setup_gain.Location = new Point(480 + 45, 750 + 100 - 50 - 10 - 90 + 50);

                    //R
                    lb_R.Location = new Point(0, 750 + 100 - 50 + 50 - 30);
                    lb_0xR.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 - 30);
                    lb_range_3.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50);
                    lb_range_3.Text = "0~FFF          0~4095";
                    trackBar_R.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 - 30);
                    numericUpDown_R.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 - 30);
                    tb_R.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 - 30);
                    bt_setup_R.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 - 30);

                    //G
                    lb_G.Location = new Point(0, 750 + 100 - 50 + 50 * 2 - 20);
                    lb_0xG.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 * 2 - 20);
                    lb_range_4.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50 * 2 - 40+30 + 20);
                    lb_range_4.Text = "0~FFF          0~4095";
                    trackBar_G.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    numericUpDown_G.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    tb_G.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    bt_setup_G.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 * 2 - 20);

                    //B
                    lb_BB.Location = new Point(0, 750 + 100 - 50 + 50 * 3 - 10);
                    lb_0xB.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 * 3 - 10);
                    lb_range_5.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50 * 3 - 20+30 + 10);
                    lb_range_5.Text = "0~FFF          0~4095";
                    trackBar_B.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 * 3 - 10);
                    numericUpDown_B.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 * 3 - 10);
                    tb_B.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 * 3 - 10);
                    bt_setup_B.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 * 3 - 10);

                    //TARGET RGB
                    comboBox_temperature.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 230 * 2);
                    numericUpDown_TG_R.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 250 * 2);
                    numericUpDown_TG_G.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 290 * 2);
                    numericUpDown_TG_B.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 330 * 2);

                    //WPT
                    lb_wpt.Location = new Point(410 + 5 + 400 + 20 + 200, 750 + 100 - 50 - 10 + 50 * 2 - 15);
                    tb_wpt.Location = new Point(410 + 45 + 25 + 400 + 20 + 200, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    numericUpDown_wpt.Location = new Point(410 + 45 + 25 + 80 + 400 + 20 + 200, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    bt_read_wpt.Location = new Point(410 + 45 + 25 + 80 + 80 + 400 + 20 + 200, 750 + 100 - 50 - 10 + 50 * 2 - 20);
                    bt_write_wpt.Location = new Point(410 + 45 + 25 + 80 + 150 + 400 + 20 + 200, 750 + 100 - 50 - 10 + 50 * 2 - 20);

                    //BPT
                    lb_bpt.Location = new Point(410 + 5 + 400 + 20 + 200, lb_wpt.Location.Y + 60);
                    tb_bpt.Location = new Point(410 + 45 + 25 + 400 + 20 + 200, tb_wpt.Location.Y + 60);
                    numericUpDown_bpt.Location = new Point(410 + 45 + 25 + 80 + 400 + 20 + 200, numericUpDown_wpt.Location.Y + 60);
                    bt_read_bpt.Location = new Point(410 + 45 + 25 + 80 + 80 + 400 + 20 + 200, bt_read_wpt.Location.Y + 60);
                    bt_write_bpt.Location = new Point(410 + 45 + 25 + 80 + 150 + 400 + 20 + 200, bt_write_wpt.Location.Y + 60);
                    refresh_picturebox2();
                    lb_save_message.Visible = false;
                }
                else
                {
                    pictureBox1.Location = new Point(170 + 160 + 30, 15);
                    richTextBox1.Visible = false;
                    lb_save_message.Visible = true;
                }
                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y);
            }
            else
            {
                flag_fullscreen = false;
                button19.BackgroundImage = imsLink.Properties.Resources.full_screen;
                richTextBox1.Visible = true;
                this.richTextBox1.Location = new System.Drawing.Point(958, 67);
                this.richTextBox1.Size = new System.Drawing.Size(500, 586);
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                //this.TopMost = false;
                tabControl1.Size = new Size(948, 616);
                pictureBox1.Location = new Point(170, 50);
                pictureBox1.Size = new Size(640, 480);
                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y - comboBox_webcam.Height);
                toolTip1.SetToolTip(button19, "2X");
                lb_save_message.Visible = true;

                if (flag_awb_debug == true)
                {
                    lb_0x1.Visible = false;
                    lb_0x2.Visible = false;
                    lb_0x3.Visible = false;
                    lb_0x4.Visible = false;
                    lb_addr.Visible = false;
                    lb_data.Visible = false;
                    tb_1a.Visible = false;
                    tb_2a.Visible = false;
                    tb_3a.Visible = false;
                    tb_4a.Visible = false;
                    bt_read2.Visible = false;
                    bt_write2.Visible = false;

                    bt_awb.Visible = false;
                    bt_awb_test.Visible = false;
                    bt_awb_test2.Visible = false;
                    bt_awb_test_init.Visible = false;
                    bt_disable_timer_webcam.Visible = false;
                    bt_erase.Visible = false;
                    bt_test.Visible = false;
                    bt_clear.Visible = false;
                    bt_break.Visible = false;
                    pictureBox2.Visible = false;
                    lb_range_1.Visible = false;
                    lb_range_2.Visible = false;
                    lb_expo.Visible = false;
                    trackBar_expo.Visible = false;
                    tb_expo.Visible = false;
                    numericUpDown_expo.Visible = false;
                    bt_setup_expo.Visible = false;
                    lb_gain.Visible = false;
                    trackBar_gain.Visible = false;
                    tb_gain.Visible = false;
                    numericUpDown_gain.Visible = false;
                    bt_setup_gain.Visible = false;

                    lb_awb_result_expo.Visible = false;
                    lb_awb_result_gain.Visible = false;
                    lb_awb_result_R.Visible = false;
                    lb_awb_result_G.Visible = false;
                    lb_awb_result_B.Visible = false;
                    bt_get_setup.Visible = false;

                    comboBox_temperature.Visible = false;
                    //comboBox_webcam.Visible = false;
                    numericUpDown_TG_R.Visible = false;
                    numericUpDown_TG_G.Visible = false;
                    numericUpDown_TG_B.Visible = false;

                    //R
                    lb_R.Visible = false;
                    lb_0xR.Visible = false;
                    lb_range_3.Visible = false;
                    trackBar_R.Visible = false;
                    tb_R.Visible = false;
                    numericUpDown_R.Visible = false;
                    bt_setup_R.Visible = false;

                    //G
                    lb_G.Visible = false;
                    lb_0xG.Visible = false;
                    lb_range_4.Visible = false;
                    trackBar_G.Visible = false;
                    tb_G.Visible = false;
                    numericUpDown_G.Visible = false;
                    bt_setup_G.Visible = false;

                    //B
                    lb_BB.Visible = false;
                    lb_0xB.Visible = false;
                    lb_range_5.Visible = false;
                    trackBar_B.Visible = false;
                    tb_B.Visible = false;
                    numericUpDown_B.Visible = false;
                    bt_setup_B.Visible = false;

                    //WPT
                    lb_wpt.Visible = false;
                    tb_wpt.Visible = false;
                    numericUpDown_wpt.Visible = false;
                    bt_read_wpt.Visible = false;
                    bt_write_wpt.Visible = false;

                    //BPT
                    lb_bpt.Visible = false;
                    tb_bpt.Visible = false;
                    numericUpDown_bpt.Visible = false;
                    bt_read_bpt.Visible = false;
                    bt_write_bpt.Visible = false;

                }
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    //Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                    richTextBox1.Text += "先關閉camera\n";
                }
            }
            else
            {
                richTextBox1.Text += "camera is null\n";
            }

            richTextBox1.Text += "關閉程式\n";
            Application.Exit();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("https://www.insighteyes.com/");
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            lb_rtc.Text = "";
            button21.BackColor = Color.Red;
            //richTextBox1.Text += "更新系統時間\n";

            //richTextBox1.Text += "目前時間 : " + DateTime.Now.ToString() + "\n";

            System.DateTime dt = System.DateTime.Now;
            /*
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            */
            //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

            Send_IMS_Data(0xB0, 0x12, 0x34, 0x56);      //RTC write

            rtc_data_send[0] = (byte)(dt.Year - 1900);
            rtc_data_send[1] = (byte)dt.Month;
            rtc_data_send[2] = (byte)dt.Day;
            rtc_data_send[3] = (byte)dt.DayOfWeek;
            rtc_data_send[4] = (byte)dt.Hour;
            rtc_data_send[5] = (byte)dt.Minute;
            rtc_data_send[6] = (byte)dt.Second;

            if (rtc_data_send[5] < 59)
            {
                rtc_data_send[6] += 2;
                if (rtc_data_send[6] > 59)
                {
                    rtc_data_send[6] -= 60;
                    rtc_data_send[5]++;
                }
            }
            serialPort1.Write(rtc_data_send, 0, 7);
            delay(300);

            lb_rtc.Text = "已更新RTC時間";
            button21.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            byte page;
            button24.BackColor = Color.Red;

            tb_info_8.Clear();
            lb_camera_model.Text = "相機型號讀取中...";
            tb_info_82.BackColor = Color.White;
            tb_info_83.Text = "";

            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-2xx";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "無連接器";
                tb_info_aa1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;

                //tb_info_83.Text = "有連接器, 有相機";
                //tb_info_83.BackColor = Color.White;

                tb_info_8.Text = "[Model] :";
                lb_camera_model.Text = "[Model] :";

                //Send_IMS_Data(0xE1, 0xAB, 0xCD, 0xEF);

                /*
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }
                flag_wait_receive_data = 0;
                */

                page = MODEL_PAGE;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "m";
                    delay(100);
                }
                flag_wait_receive_data = 0;

            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
            button24.BackColor = System.Drawing.SystemColors.ControlLight;

        }

        private void button23_Click(object sender, EventArgs e)
        {
            lb_camera_model.Text = "";
            lb_write_camera_model.Text = "燒錄資料進行中.....";
            richTextBox1.Text += "相機型號長度 : " + tb_info_83.Text.Length.ToString() + "\n";
            if ((tb_info_83.Text.Length <= 0) || (tb_info_83.Text.Length > 16))
            {
                richTextBox1.Text += "相機型號長度錯誤, 長度 : " + tb_info_83.Text.Length.ToString() + "\n";
                lb_write_camera_model.Text = "相機型號長度錯誤";
                return;
            }

            //byte page;
            button23.BackColor = Color.Red;

            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-2xx";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "無連接器";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_model.Text = "無連接器";
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_model.Text = "有連接器, 無相機";
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;
                lb_write_camera_model.Text = "有連接器, 有相機, 寫入中";

                int i;
                for (i = 0; i < 16; i++)
                {
                    camera_model_data_send[i] = 0;
                }
                for (i = 0; i < tb_info_83.Text.Length; i++)
                {
                    camera_model_data_send[i] = (byte)tb_info_83.Text[i];
                }

                Send_IMS_Data(0xE0, 0x12, 0x34, 0x56);   //camera model write

                serialPort1.Write(camera_model_data_send, 0, 16);
                lb_write_camera_model.Text = "寫入相機型號完成";


            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
            button23.BackColor = System.Drawing.SystemColors.ControlLight;

        }

        private void button31_Click(object sender, EventArgs e)
        {
            //byte page;
            button31.BackColor = Color.Red;

            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-2xx";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "無連接器";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_serial.Text = "無連接器";
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_serial.Text = "有連接器, 無相機";
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;
                lb_write_camera_serial.Text = "有連接器, 有相機, 寫入中";

                Send_IMS_Data(0xC0, 0x65, 0x43, 0x21);   //camera serial write random data
                lb_write_camera_serial.Text = "寫入相機任意序號完成";
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
            button31.BackColor = System.Drawing.SystemColors.ControlLight;



        }

        private void button30_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);
            lb_write_mb_model.Text = "";
            lb_machine_serial.Text = "主機序號 讀取中...";
            lb_mb_big_serial.Text = "大PCBA序號 讀取中...";
            lb_mb_small_serial.Text = "小PCBA序號 讀取中...";
            button30.BackColor = Color.Red;
            tb_machine_serial.Text = "";
            tb_mb_big_serial.Text = "";
            tb_mb_small_serial.Text = "";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                button30.BackColor = System.Drawing.SystemColors.ControlLight;
                return;
            }

            Send_IMS_Data(0xF1, 0xAB, 0xCD, 0xEF);  //main board model read

            int cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox1.Text += "+";
                delay(100);
            }
            flag_wait_receive_data = 0;

            button30.BackColor = System.Drawing.SystemColors.ControlLight;

        }

        private void button29_Click(object sender, EventArgs e)
        {
            if (flag_already_write_system_data == true)
            {
                MessageBox.Show("已經燒錄過主機資料");
                return;
            }

            g.Clear(BackColor);
            g.DrawString("燒錄中", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(60, 20));
            button29.BackColor = Color.Red;
            lb_machine_serial.Text = "";
            lb_mb_big_serial.Text = "";
            lb_mb_small_serial.Text = "";
            lb_write_mb_model.Text = "燒錄資料進行中.....";
            lb_write_mb_model.ForeColor = Color.Red;
            richTextBox1.Text += "主機序號長度 : " + tb_machine_serial.Text.Length.ToString() + "\n";
            richTextBox1.Text += "大PCBA序號長度 : " + tb_mb_big_serial.Text.Length.ToString() + "\n";
            richTextBox1.Text += "小PCBA序號長度 : " + tb_mb_small_serial.Text.Length.ToString() + "\n";

            if ((tb_machine_serial.Text.Length <= 0) || (tb_machine_serial.Text.Length != 13))
            {
                richTextBox1.Text += "主機序號長度錯誤, 長度 : " + tb_machine_serial.Text.Length.ToString() + "\n";
                lb_write_mb_model.Text = "主機序號長度錯誤";
                return;
            }
            if ((tb_mb_big_serial.Text.Length <= 0) || (tb_mb_big_serial.Text.Length != 13))
            {
                richTextBox1.Text += "大PCBA序號長度錯誤, 長度 : " + tb_mb_big_serial.Text.Length.ToString() + "\n";
                lb_write_mb_model.Text = "大PCBA序號長度錯誤";
                return;
            }
            if ((tb_mb_small_serial.Text.Length <= 0) || (tb_mb_small_serial.Text.Length != 24))
            {
                richTextBox1.Text += "小PCBA序號長度錯誤, 長度 : " + tb_mb_small_serial.Text.Length.ToString() + "\n";
                lb_write_mb_model.Text = "小PCBA序號長度錯誤";
                return;
            }

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                button29.BackColor = System.Drawing.SystemColors.ControlLight;
                return;
            }

            string total_data = tb_machine_serial.Text + tb_mb_big_serial.Text + tb_mb_small_serial.Text;
            richTextBox1.Text += "total_data len = " + total_data.Length.ToString() + "\n";

            int i;
            for (i = 0; i < main_board_model_data_send.Length; i++)
            {
                main_board_model_data_send[i] = 0;
            }
            for (i = 0; i < total_data.Length; i++)
            {
                main_board_model_data_send[i] = (byte)total_data[i];
            }

            Send_IMS_Data(0xF0, 0x12, 0x34, 0x56);   //main board model write

            serialPort1.Write(main_board_model_data_send, 0, main_board_model_data_send.Length);
            delay(200);
            lb_write_mb_model.Text = "寫入主機型號完成";
            lb_write_mb_model.ForeColor = Color.Black;
            button29.BackColor = System.Drawing.SystemColors.ControlLight;
            g.Clear(BackColor);
            g.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
            flag_already_write_system_data = true;
        }

        private void button32_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            richTextBox1.Text += "離開IMS Link，進入putty mode\n";
            Send_IMS_Data(0xFF, 0x11, 0x66, 0x88);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            button35.BackColor = Color.Red;
            richTextBox1.Text += "離開putty mode，進入IMS Link\n";

            byte[] data = new byte[8];

            data[0] = (byte)'i';
            data[1] = (byte)'m';
            data[2] = (byte)'s';
            data[3] = (byte)'l';
            data[4] = (byte)'i';
            data[5] = (byte)'n';
            data[6] = (byte)'k';
            data[7] = 0x0d;

            delay(100);
            serialPort1.Write(data, 0, 8);
            delay(100);
            button35.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button37_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            button37.BackColor = Color.Red;
            button36.BackgroundImage = null;
            button36.BackColor = Color.Red;
            Send_IMS_Data(0x99, 0, 0, 0x0D);
            button36.BackgroundImage = imsLink.Properties.Resources.console;
        
            /* reserved
            byte[] data = new byte[4];

            data[0] = 0x99;
            data[1] = 0x00;
            data[2] = 0x00;
            data[3] = 0x0D;

            delay(100);
            serialPort1.Write(data, 0, 4);
            delay(100);
            */

        }

        private void button6_Click(object sender, EventArgs e)
        {
            button72_Click(sender, e);
        }

        private void btnLeft_Click(object sender, EventArgs e)
        {
            if (btn_right_left_cnt > -zoom_cnt)
            {
                btn_right_left_cnt--;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
            }
            else
                richTextBox1.Text += "已達邊界最左\n";
        }

        private void btnRight_Click(object sender, EventArgs e)
        {
            if (btn_right_left_cnt < zoom_cnt)
            {
                btn_right_left_cnt++;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
            }
            else
                richTextBox1.Text += "已達邊界最右\n";
        }

        private void btnUp_Click(object sender, EventArgs e)
        {
            if (btn_down_up_cnt > -zoom_cnt)
            {
                btn_down_up_cnt--;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
            }
            else
                richTextBox1.Text += "已達邊界最上\n";
        }

        private void btnDown_Click(object sender, EventArgs e)
        {
            if (btn_down_up_cnt < zoom_cnt)
            {
                btn_down_up_cnt++;
                //richTextBox1.Text += "Rt-Lt = " + btn_right_left_cnt.ToString() + "\tDn-Up = " + btn_down_up_cnt.ToString() + "\n";
            }
            else
                richTextBox1.Text += "已達邊界最下\n";
        }

        private void btnCenter_Click(object sender, EventArgs e)
        {
            zoom_cnt = 0;
            btn_down_up_cnt = 0;
            btn_right_left_cnt = 0;
            lb_zoom.Text = "1.00 X";
            richTextBox1.Text += "恢復置中\n";
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox1.SelectionStart = richTextBox1.TextLength;
            richTextBox1.ScrollToCaret();
        }

        private void button39_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);
            tb_machine_serial.Text = "0000000-B0000";
            tb_mb_big_serial.Text = "0000000000000";
            tb_mb_small_serial.Text = "0000000 0000 000000 0000";
            lb_write_mb_model.Text = "";
            lb_machine_serial.Text = "";
            lb_mb_big_serial.Text = "";
            lb_mb_small_serial.Text = "";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            tb_info_83.Text = "";
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            richTextBox1.Text += "pictureBox double click at x = " + MousePosition.X.ToString() + " y = " + MousePosition.Y.ToString() + "\n";

            //MouseButtons.
            //MouseButtons.Left

        }

        bool flag_ok_machine_serial = false;
        bool flag_ok_mb_big_serial = false;
        bool flag_ok_mb_small_serial = false;
        bool flag_ok_to_write_data = false;
        private void scanner_timer2_Tick(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
                return;

            richTextBox1.Text += "B";
            if ((cnt3 % 1) == 0)
            {
                this.tb_wait_data.Focus();
            }
            if (tb_wait_data.Text.Length > 0)
            {
                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_data.Text.Length == 13)
                {
                    if ((tb_wait_data.Text[7] == '-') && (tb_wait_data.Text[8] == 'B'))
                    {
                        for (i = 0; i < 13; i++)
                        {
                            if ((i == 7) || (i == 8))
                                continue;
                            if ((tb_wait_data.Text[i] < '0') || (tb_wait_data.Text[i] > '9'))
                            {
                                flag_incorrect_data = true;
                            }
                        }

                        if (flag_incorrect_data == false)
                        {
                            richTextBox1.Text += "取得 主機序號 : " + tb_wait_data + "\n";
                            tb_machine_serial.Text = tb_wait_data.Text;
                            tb_wait_data.Text = "";
                            flag_ok_machine_serial = true;
                        }
                    }
                    else
                    {
                        for (i = 0; i < 13; i++)
                        {
                            if ((tb_wait_data.Text[i] < '0') || (tb_wait_data.Text[i] > '9'))
                            {
                                flag_incorrect_data = true;
                            }
                        }

                        if (flag_incorrect_data == false)
                        {
                            richTextBox1.Text += "取得 大PCBA序號 : " + tb_wait_data + "\n";
                            tb_mb_big_serial.Text = tb_wait_data.Text;
                            tb_wait_data.Text = "";
                            flag_ok_mb_big_serial = true;
                        }
                    }
                }
                else if (tb_wait_data.Text.Length == 24)
                {
                    if ((tb_wait_data.Text[7] != ' ') || (tb_wait_data.Text[12] != ' ') || (tb_wait_data.Text[19] != ' '))
                    {
                        richTextBox1.Text += "小PCBA序號格式不正確a\n";
                        return;
                    }

                    for (i = 0; i < 24; i++)
                    {
                        if (((tb_wait_data.Text[i] < '0') || (tb_wait_data.Text[i] > '9')) && (tb_wait_data.Text[i] != ' '))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "小PCBA序號格式不正確b\n";
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得 小PCBA序號 : " + tb_wait_data + "\n";
                        tb_mb_small_serial.Text = tb_wait_data.Text;
                        tb_wait_data.Text = "";
                        flag_ok_mb_small_serial = true;
                    }
                }
                else if (tb_wait_data.Text.Length == 14)
                {
                    if (flag_ok_to_write_data == true)
                    {
                        if (tb_wait_data.Text == "IMS EGD SYSTEM")
                        {
                            if (flag_comport_ok == false)
                            {
                                richTextBox1.Text += "未連線comport, abort\n";
                                tb_wait_data.Text = "";
                                return;
                            }

                            flag_incorrect_data = false;
                            richTextBox1.Text += "資料正確, 開始燒錄\n";
                            panel6.BackgroundImage = null;
                            g.Clear(BackColor);
                            button29_Click(sender, e);  //執行燒錄按鍵
                            tb_wait_data.Text = "";
                            flag_incorrect_data = true;
                            flag_ok_machine_serial = false;
                            flag_ok_mb_big_serial = false;
                            flag_ok_mb_small_serial = false;
                            flag_ok_to_write_data = false;
                            return;
                        }
                        else
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料錯誤\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "資料未齊全, 忽略\n";
                        tb_wait_data.Text = "";
                        lb_write_mb_model.Text = "";

                        if (flag_ok_machine_serial == false)
                        {
                            tb_machine_serial.Text = "";
                        }
                        if (flag_ok_mb_big_serial == false)
                        {
                            tb_mb_big_serial.Text = "";
                        }
                        if (flag_ok_mb_small_serial == false)
                        {
                            tb_mb_small_serial.Text = "";
                        }
                        g.Clear(BackColor);
                        return;
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                }

                if (flag_incorrect_data == true)
                {
                    richTextBox1.Text += "資料錯誤,長度 " + tb_wait_data.Text.Length.ToString() + "\t內容 " + tb_wait_data.Text + "\n";
                    tb_wait_data.Text = "";
                }
                else
                {
                    richTextBox1.Text += "資料正確\n";
                    //bool flag_ok_machine_serial = false;
                    //bool flag_ok_mb_big_serial = false;
                    //bool flag_ok_mb_small_serial = false;
                    if (flag_ok_machine_serial == false)
                    {
                        tb_machine_serial.Text = "";
                        lb_write_mb_model.Text = "";
                        panel6.BackgroundImage = null;
                        g.Clear(BackColor);
                    }
                    if (flag_ok_mb_big_serial == false)
                    {
                        tb_mb_big_serial.Text = "";
                        lb_write_mb_model.Text = "";
                        panel6.BackgroundImage = null;
                        g.Clear(BackColor);
                    }
                    if (flag_ok_mb_small_serial == false)
                    {
                        tb_mb_small_serial.Text = "";
                        lb_write_mb_model.Text = "";
                        panel6.BackgroundImage = null;
                        g.Clear(BackColor);
                    }
                    if ((flag_ok_machine_serial == true) && (flag_ok_mb_big_serial == true) && (flag_ok_mb_small_serial == true))
                    {
                        lb_write_mb_model.Text = "準備燒錄";
                        lb_write_mb_model.ForeColor = Color.Black;
                        richTextBox1.Text += "準備燒錄\n";
                        flag_ok_to_write_data = true;
                        panel6.BackgroundImage = imsLink.Properties.Resources.ims_egd_system;
                    }
                }
                tb_wait_data.Text = "";
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);
            if (flag_auto_scan_mode == true)
            {
                scanner_timer2.Enabled = false;
                flag_auto_scan_mode = false;
                button25.Text = "到自動模式";
            }
            else
            {
                scanner_timer2.Enabled = true;
                flag_auto_scan_mode = true;
                button25.Text = "到修改模式";
            }
        }

        private void button40_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                scanner_timer.Enabled = false;
                flag_auto_scan_mode = false;
                button40.Text = "到自動模式";
            }
            else
            {
                scanner_timer.Enabled = true;
                flag_auto_scan_mode = true;
                button40.Text = "到修改模式";
            }
        }

        int read_connection_cnt = 0;
        int read_connection_fail_cnt = 0;
        private void timer_rtc_Tick(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
                return;

            //richTextBox1.Text += "C";
            if (flag_read_connection_again == true)
            {
                read_connection_fail_cnt = 0;
                read_connection_cnt++;

                flag_read_connection_again = false;

                if (read_connection_cnt == 4)
                {
                    read_connection_cnt = 0;
                    //richTextBox1.Text += "\nread camera status.......\t";
                    progressBar1.Value = 0;

                    textBox7.Clear();
                    textBox7.BackColor = Color.Gray;
                    panel_camera_status1.BackgroundImage = null;
                    panel_camera_status2.BackgroundImage = null;
                    panel_camera_status3.BackgroundImage = null;
                    panel_camera_status4.BackgroundImage = null;
                    Send_IMS_Data(0xFF, 0, 0, 0);
                }
                else
                {
                    //richTextBox1.Text += "\nread rtc.......\t";
                    progressBar2.Value = 0;
                    Get_IMS_Data(3, 0x11, 0xAA);    //read RTC data
                }
                int cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    //richTextBox1.Text += "+" + cnt.ToString() + " ";
                    delay(100);
                    if (cnt == 20)
                    {
                        flag_read_connection_again = true;
                    }
                }
                flag_wait_receive_data = 0;
            }
            else
            {
                read_connection_fail_cnt++;
                richTextBox1.Text += " F " + read_connection_fail_cnt.ToString();
                if (read_connection_fail_cnt == 5)
                {
                    richTextBox1.Text += "fail cnt = 5, let flag - true\t";
                    read_connection_fail_cnt = 0;
                    flag_read_connection_again = true;
                }

            }

        }

        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }
        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }
        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }

        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }  

        private void timer_get_rgb_Tick(object sender, EventArgs e)
        {
            //txtPoint.Text = Control.MousePosition.X.ToString() + "," + Control.MousePosition.Y.ToString();
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            panel1.BackColor = cl;
            lb_rgb.Text = cl.R + ", " + cl.G + ", " + cl.B;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);
            if (flag_release_mode == true)
            {
                tb_sn1.Text = "AA0000000";
                tb_sn2.Text = "00000000000";
            }
            else
            {
                tb_sn1.Text = "AA1234567";
                tb_sn2.Text = "12345678901";
            }
            lb_write_camera_serial2.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            g2.Clear(BackColor);
            g2.DrawString("燒錄中", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(60, 20));
            button11.BackColor = Color.Red;
            lb_write_camera_serial2.Text = "燒錄資料進行中.....";
            lb_write_camera_serial2.ForeColor = Color.Red;
            richTextBox1.Text += "相機序號1長度 : " + tb_sn1.Text.Length.ToString() + "\n";
            richTextBox1.Text += "相機序號2長度 : " + tb_sn2.Text.Length.ToString() + "\n";
            if (tb_sn1.Text.Length != 9)
            {
                richTextBox1.Text += "相機序號1長度錯誤, 長度 : " + tb_sn1.Text.Length.ToString() + "\n";
                lb_write_camera_serial2.Text = "相機型號1長度錯誤";
                return;
            }
            if (tb_sn2.Text.Length != 11)
            {
                richTextBox1.Text += "相機序號2長度錯誤, 長度 : " + tb_sn2.Text.Length.ToString() + "\n";
                lb_write_camera_serial2.Text = "相機型號2長度錯誤";
                return;
            }

            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 20))
            {
                richTextBox1.Text += "-2xx";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "無連接器";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_serial2.Text = "無連接器";
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_serial2.Text = "有連接器, 無相機";
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;
                lb_write_camera_serial2.Text = "有連接器, 有相機, 寫入相機序號中...";

                int i;

                byte[] sn_data_tmp = new byte[20];
                for (i = 0; i < tb_sn1.Text.Length; i++)
                {
                    sn_data_tmp[i] = (byte)tb_sn1.Text[i];
                    //richTextBox1.Text += "\ni = " + i.ToString() + " tmp data : " + tb_sn1.Text[i].ToString();
                }

                //richTextBox1.Text += "\n";

                for (i = tb_sn1.Text.Length; i < (tb_sn1.Text.Length + tb_sn2.Text.Length); i++)
                {
                    sn_data_tmp[i] = (byte)tb_sn2.Text[i - tb_sn1.Text.Length];
                    //richTextBox1.Text += "\ni = " + i.ToString() + " tmp data : " + tb_sn2.Text[i - tb_sn1.Text.Length].ToString();
                }

                //richTextBox1.Text += "\n";

                Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write

                serialPort1.Write(sn_data_tmp, 0, 20);

                richTextBox1.Text += "序號 : 寫入資料  完成\n";

                lb_write_camera_serial2.Text = "寫入1";

                delay(500);

                lb_write_camera_serial2.Text = "寫入相機序號完成";
                lb_write_camera_serial2.ForeColor = Color.Black;
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
                g2.Clear(BackColor);
                g2.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
                lb_write_camera_serial2.Text += "    燒錄完成";

                delay(200);

                //驗證資料
                lb_write_camera_serial2.Text += "    驗證中";
                lb_write_camera_serial2.ForeColor = Color.Blue;
                richTextBox1.Text += "\n讀相機序號回來 " + DateTime.Now.ToString() + "\n";

                Font f = new Font("標楷體", 60);
                int tmp_width = 0;
                int tmp_height = 0;
                string str = "驗證中";

                tmp_width = g.MeasureString(str, f).ToSize().Width;
                tmp_height = g.MeasureString(str, f).ToSize().Height;

                richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";
                richTextBox1.Text += "W = " + panel9.Width.ToString() + "  H = " + panel9.Height.ToString() + "\n";

                g2.Clear(BackColor);
                g2.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(60, 20));
                //g2.DrawString(str, f, new SolidBrush(Color.Blue), new PointF((panel9.Width - tmp_width) / 2, (panel9.Height - tmp_height) / 2));
                button11.BackColor = System.Drawing.SystemColors.ControlLight;

                flag_verify_serial_data = 1;
                Get_IMS_Data(0, 0xAA, 0xAA);

            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }

        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (flag_awb_debug == false)
                return;
            if (flag_us_debug == true)
                return;

            int x_st_old = 0;
            int y_st_old = 0;
            int ww = awb_block;
            int hh = awb_block;

            int WW = 640;
            int HH = 480;

            int flag_down_up_cnt_old = flag_down_up_cnt;
            int flag_right_left_cnt_old = flag_right_left_cnt;

            x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step;
            y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt_old * awb_step;

            //richTextBox1.Text += "flag_right_left_cnt_old = " + flag_right_left_cnt_old.ToString() + " flag_down_up_cnt_old = " + flag_down_up_cnt_old.ToString() + "\n";
            //richTextBox1.Text += "x_st_old = " + x_st_old.ToString() + " y_st_old = " + y_st_old.ToString() + "\n";

            if ((e.KeyCode == Keys.PageDown) || (e.KeyCode == Keys.Space))
            {
                richTextBox1.Text += "下一首\n";
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                richTextBox1.Text += "上一首\n";
            }
            else if (e.KeyCode == Keys.Up)
            {
                richTextBox1.Text += "Up\n";
            }
            else if (e.KeyCode == Keys.Down)
            {
                richTextBox1.Text += "Down\n";
            }
            else if (e.KeyCode == Keys.NumPad8)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (y_st_old > 0)
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step - awb_step;
                        if (y_st_old > 0)
                        {
                            flag_down_up_cnt -= 2;
                            richTextBox1.Text += "Up2\n";
                        }
                        else
                        {
                            flag_down_up_cnt--;
                            richTextBox1.Text += "Up1\n";
                        }
                    }
                }
                else
                {
                    if (y_st_old > 0)
                    {
                        flag_down_up_cnt--;
                        richTextBox1.Text += "Up1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad9)
            {
                richTextBox1.Text += "Up-Right\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (y_st_old > 0)
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step - awb_step;
                        if (y_st_old > 0)
                        {
                            flag_down_up_cnt -= 2;
                            richTextBox1.Text += "Up2\n";
                        }
                        else
                        {
                            flag_down_up_cnt--;
                            richTextBox1.Text += "Up1\n";
                        }
                    }
                    if (x_st_old < (WW - ww))
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step + awb_step;
                        if (x_st_old < (WW - ww))
                        {
                            flag_right_left_cnt += 2;
                            richTextBox1.Text += "Right2\n";
                        }
                        else
                        {
                            flag_right_left_cnt++;
                            richTextBox1.Text += "Right1\n";
                        }
                    }
                }
                else
                {
                    if (y_st_old > 0)
                    {
                        flag_down_up_cnt--;
                        richTextBox1.Text += "Up1\n";
                    }
                    if (x_st_old < (WW - ww))
                    {
                        flag_right_left_cnt++;
                        richTextBox1.Text += "Right1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad2)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (y_st_old < (HH - hh))
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + awb_step;
                        if (y_st_old < (HH - hh))
                        {
                            flag_down_up_cnt += 2;
                            richTextBox1.Text += "Down2\n";
                        }
                        else
                        {
                            flag_down_up_cnt++;
                            richTextBox1.Text += "Down1\n";
                        }
                    }
                }
                else
                {
                    if (y_st_old < (HH - hh))
                    {
                        flag_down_up_cnt++;
                        richTextBox1.Text += "Down1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad1)
            {
                richTextBox1.Text += "Down-Left\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (y_st_old < (HH - hh))
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + awb_step;
                        if (y_st_old < (HH - hh))
                        {
                            flag_down_up_cnt += 2;
                            richTextBox1.Text += "Down2\n";
                        }
                        else
                        {
                            flag_down_up_cnt++;
                            richTextBox1.Text += "Down1\n";
                        }
                    }
                    if (x_st_old > 0)
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step - awb_step;
                        if (x_st_old > 0)
                        {
                            flag_right_left_cnt -= 2;
                            richTextBox1.Text += "Left2\n";
                        }
                        else
                        {
                            flag_right_left_cnt--;
                            richTextBox1.Text += "Left1\n";
                        }
                    }
                }
                else
                {
                    if (y_st_old < (HH - hh))
                    {
                        flag_down_up_cnt++;
                        richTextBox1.Text += "Down1\n";
                    }
                    if (x_st_old > 0)
                    {
                        flag_right_left_cnt--;
                        richTextBox1.Text += "Left1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad4)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (x_st_old > 0)
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step - awb_step;
                        if (x_st_old > 0)
                        {
                            flag_right_left_cnt -= 2;
                            richTextBox1.Text += "Left2\n";
                        }
                        else
                        {
                            flag_right_left_cnt--;
                            richTextBox1.Text += "Left1\n";
                        }
                    }
                }
                else
                {
                    if (x_st_old > 0)
                    {
                        flag_right_left_cnt--;
                        richTextBox1.Text += "Left1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad7)
            {
                richTextBox1.Text += "Up-Left\n";

                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (x_st_old > 0)
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step - awb_step;
                        if (x_st_old > 0)
                        {
                            flag_right_left_cnt -= 2;
                            richTextBox1.Text += "Left2\n";
                        }
                        else
                        {
                            flag_right_left_cnt--;
                            richTextBox1.Text += "Left1\n";
                        }
                    }
                    if (y_st_old > 0)
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step - awb_step;
                        if (y_st_old > 0)
                        {
                            flag_down_up_cnt -= 2;
                            richTextBox1.Text += "Up2\n";
                        }
                        else
                        {
                            flag_down_up_cnt--;
                            richTextBox1.Text += "Up1\n";
                        }
                    }
                }
                else
                {
                    if (x_st_old > 0)
                    {
                        flag_right_left_cnt--;
                        richTextBox1.Text += "Left1\n";
                    }
                    if (y_st_old > 0)
                    {
                        flag_down_up_cnt--;
                        richTextBox1.Text += "Up1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad6)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (x_st_old < (WW - ww))
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step + awb_step;
                        if (x_st_old < (WW - ww))
                        {
                            flag_right_left_cnt += 2;
                            richTextBox1.Text += "Right2\n";
                        }
                        else
                        {
                            flag_right_left_cnt++;
                            richTextBox1.Text += "Right1\n";
                        }
                    }
                }
                else
                {
                    if (x_st_old < (WW - ww))
                    {
                        flag_right_left_cnt++;
                        richTextBox1.Text += "Right1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad3)
            {
                richTextBox1.Text += "Down-Right\n";
                //2
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (y_st_old < (HH - hh))
                    {
                        y_st_old = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + awb_step;
                        if (y_st_old < (HH - hh))
                        {
                            flag_down_up_cnt += 2;
                            richTextBox1.Text += "Down2\n";
                        }
                        else
                        {
                            flag_down_up_cnt++;
                            richTextBox1.Text += "Down1\n";
                        }
                    }
                    if (x_st_old < (WW - ww))
                    {
                        x_st_old = WW / 2 - ww / 2 + flag_right_left_cnt_old * awb_step + awb_step;
                        if (x_st_old < (WW - ww))
                        {
                            flag_right_left_cnt += 2;
                            richTextBox1.Text += "Right2\n";
                        }
                        else
                        {
                            flag_right_left_cnt++;
                            richTextBox1.Text += "Right1\n";
                        }
                    }
                }
                else
                {
                    if (y_st_old < (HH - hh))
                    {
                        flag_down_up_cnt++;
                        richTextBox1.Text += "Down1\n";
                    }
                    if (x_st_old < (WW - ww))
                    {
                        flag_right_left_cnt++;
                        richTextBox1.Text += "Right1\n";
                    }
                }
            }
            else if (e.KeyCode == Keys.NumPad5)
            {
                richTextBox1.Text += "Center\n";
                flag_right_left_cnt = 0;
                flag_down_up_cnt = 0;
                awb_block = 64;
            }
            else if (e.KeyCode == Keys.Home)
            {
                richTextBox1.Text += "Home\n";
            }
            else if (e.KeyCode == Keys.End)
            {
                richTextBox1.Text += "End\n";
            }
            else if (e.KeyCode == Keys.Add)
            {
                if (awb_block < 300)
                    awb_block += 5;
                richTextBox1.Text += "awb_block = " + awb_block.ToString() + "\n";
            }
            else if (e.KeyCode == Keys.Subtract)
            {
                if (awb_block > 8)
                    awb_block -= 5;
                richTextBox1.Text += "awb_block = " + awb_block.ToString() + "\n";
            }
            else if (e.KeyCode == Keys.X)
            {
            }
            else if (e.KeyCode == Keys.F1)
            {
                richTextBox1.Text += "F1 : Help\n";
            }
            else if (e.KeyCode == Keys.F10)
            {
                richTextBox1.Text += "F10 : Setup\n";
            }
            else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
            {
                if (e.KeyCode == Keys.W)
                {
                }
                else if (e.KeyCode == Keys.H)
                {
                }
            }
            else if (e.KeyCode == Keys.W)
            {
            }
            else if (e.KeyCode == Keys.H)
            {
            }
            else
            {
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";
            }
            refresh_picturebox2();
        }

        int timer_webcam_cnt = 0;
        private void timer_webcam_Tick(object sender, EventArgs e)
        {
            if (flag_awb_debug == false)
                return;
            if (flag_us_debug == true)
                return;

            this.pictureBox1.Focus();

            /*
            int ret;
            ret = check_RGB_value();
            if (ret == 0)
                richTextBox1.Text += "AWB OK\n";
            else
                richTextBox1.Text += "AWB FAIL\n";

            */

            timer_webcam_cnt++;
            if ((timer_webcam_cnt % 1) == 0)
            {
                /*
                richTextBox1.Text += "d_R " + (total_RGB_R_max - total_RGB_R_min).ToString() + "    " + (((float)(total_RGB_R_max - total_RGB_R_min)) / awb_block / awb_block).ToString("F3")
                    + "       d_G " + (total_RGB_G_max - total_RGB_G_min).ToString() + "    " + (((float)(total_RGB_G_max - total_RGB_G_min)) / awb_block / awb_block).ToString("F3")
                    + "       d_B " + (total_RGB_B_max - total_RGB_B_min).ToString() + "    " + (((float)(total_RGB_B_max - total_RGB_B_min)) / awb_block / awb_block).ToString("F3") + "\n";

                richTextBox1.Text += "d_R " + (total_RGB_R_max - total_RGB_R_min).ToString() + "    " + (((float)(total_RGB_R_max - total_RGB_R_min)) / awb_block / awb_block).ToString("F3")
                    + "       d_G " + (total_RGB_G_max - total_RGB_G_min).ToString() + "    " + (((float)(total_RGB_G_max - total_RGB_G_min)) / awb_block / awb_block).ToString("F3")
                    + "       d_B " + (total_RGB_B_max - total_RGB_B_min).ToString() + "    " + (((float)(total_RGB_B_max - total_RGB_B_min)) / awb_block / awb_block).ToString("F3") + "\n";
                */

                //richTextBox1.Text += "R_max(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_R_max.ToString() + ";R_min(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_R_min.ToString() + ";";
                //richTextBox1.Text += "G_max(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_G_max.ToString() + ";G_min(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_G_min.ToString() + ";";
                //richTextBox1.Text += "B_max(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_B_max.ToString() + ";B_min(" + (timer_webcam_cnt / 1).ToString() + ")=" + total_RGB_B_min.ToString() + ";\n";

               
                total_RGB_R_max = 0;
                total_RGB_R_min = 255 * awb_block * awb_block;
                total_RGB_G_max = 0;
                total_RGB_G_min = 255 * awb_block * awb_block;
                total_RGB_B_max = 0;
                total_RGB_B_min = 255 * awb_block * awb_block;
            }
        }

        private void bt_setup_expo_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int SendData = trackBar_expo.Value;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x01;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x02;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        bool flag_awb_mode = false;
        private void bt_awb_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if(bt_awb.Text == "Manual")
            {
                bt_awb.Text = "Auto";
                lb_rgb.Text = "";
                flag_awb_mode = true;
                timer_webcam.Enabled = false;
                //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);
            }
            else
            {
                bt_awb.Text = "Manual";
                flag_awb_mode = false;
                timer_webcam.Enabled = true;
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);
            }
        }

        private void bt_setup_gain_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int SendData = trackBar_gain.Value;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x0A;
            //Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x0B;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        private void button41_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xCC, 0xBB, 0xAA);
        }

        private void button42_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            System.DateTime dt = System.DateTime.Now;
            /*
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            */
            //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

            Send_IMS_Data(0xB0, 0x12, 0x34, 0x56);      //RTC write

            rtc_data_send[0] = (byte)(dt.Year - 1900);
            rtc_data_send[1] = (byte)(dt.Month - 3);
            rtc_data_send[2] = (byte)dt.Day;
            rtc_data_send[3] = (byte)dt.DayOfWeek;
            rtc_data_send[4] = (byte)dt.Hour;
            rtc_data_send[5] = (byte)dt.Minute;
            rtc_data_send[6] = (byte)dt.Second;

            if (rtc_data_send[5] < 59)
            {
                rtc_data_send[6] += 2;
                if (rtc_data_send[6] > 59)
                {
                    rtc_data_send[6] -= 60;
                    rtc_data_send[5]++;
                }
            }
            serialPort1.Write(rtc_data_send, 0, 7);
            delay(300);

            lb_rtc2.Text = "已設定錯誤時間";
        }

        private void tb_expo_TextChanged(object sender, EventArgs e)
        {
            if (tb_expo.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_expo.Text, 16);
            if ((value < 0) || (value > 511))
            {
                tb_expo.Text = "";
                return;
            }
            numericUpDown_expo.Value = value;
        }

        private void tb_gain_TextChanged(object sender, EventArgs e)
        {
            if (tb_gain.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_gain.Text, 16);
            if ((value < 0) || (value > 511))
            {
                tb_gain.Text = "";
                return;
            }
            numericUpDown_gain.Value = value;
        }

        private void tb_expo_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_expo_Click(sender, e);
            }
        }

        private void tb_gain_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_gain_Click(sender, e);
            }
        }

        private void trackBar_R_Scroll(object sender, EventArgs e)
        {
            numericUpDown_R.Value = trackBar_R.Value;
        }

        private void trackBar_G_Scroll(object sender, EventArgs e)
        {
            numericUpDown_G.Value = trackBar_G.Value;
        }

        private void trackBar_B_Scroll(object sender, EventArgs e)
        {
            numericUpDown_B.Value = trackBar_B.Value;
        }

        private void tb_R_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_R_Click(sender, e);
            }
        }

        private void tb_R_TextChanged(object sender, EventArgs e)
        {
            if (tb_R.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_R.Text, 16);
            if ((value < 0) || (value > 4095))
            {
                tb_R.Text = "";
                return;
            }
            numericUpDown_R.Value = value;
        }

        private void bt_setup_R_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int SendData = trackBar_R.Value;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1A;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1B;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        private void tb_G_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_G_Click(sender, e);
            }
        }

        private void tb_G_TextChanged(object sender, EventArgs e)
        {
            if (tb_G.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_G.Text, 16);
            if ((value < 0) || (value > 4095))
            {
                tb_G.Text = "";
                return;
            }
            numericUpDown_G.Value = value;
        }

        private void bt_setup_G_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int SendData = trackBar_G.Value;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1C;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1D;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        private void tb_B_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_B_Click(sender, e);
            }
        }

        private void tb_B_TextChanged(object sender, EventArgs e)
        {
            if (tb_B.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_B.Text, 16);
            if ((value < 0) || (value > 4095))
            {
                tb_B.Text = "";
                return;
            }
            numericUpDown_B.Value = value;
        }

        private void bt_setup_B_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int SendData = trackBar_B.Value;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1E;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1F;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        bool read_camera_sensor0(int cmd, byte DongleAddr_h, byte DongleAddr_l)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }

            flag_wait_data_cmd = cmd;
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            int cnt = 0;
            int cnt_max = 30;

            cnt = 0;
            while ((flag_wait_data_cmd != 0) && (cnt < cnt_max))
            {
                cnt++;
                //richTextBox1.Text += "e";
                //richTextBox1.Text += "e" + cnt.ToString() + " ";
                delay(10);
            }

            flag_wait_data_cmd = 0;

            //richTextBox1.Text += "wait result ok cnt = " + cnt.ToString() + "\n";
            if (cnt == cnt_max)
            {
                richTextBox1.Text += "Fail " + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\n";
                return false;
            }
            else
            {
                //richTextBox1.Text += "OK " + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\n";
                return true;
            }
        }

        void read_camera_sensor(int cmd)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            byte DongleAddr_h1 = 0;
            byte DongleAddr_l1 = 0;
            byte DongleAddr_h2 = 0;
            byte DongleAddr_l2 = 0;

            if (cmd == SENSOR_EXPO)
            {
                DongleAddr_h1 = 0x35;
                DongleAddr_l1 = 0x01;
                DongleAddr_h2 = 0x35;
                DongleAddr_l2 = 0x02;
            }
            else if (cmd == SENSOR_GAIN)
            {
                DongleAddr_h1 = 0x35;
                DongleAddr_l1 = 0x0A;
                DongleAddr_h2 = 0x35;
                DongleAddr_l2 = 0x0B;
            }
            else if (cmd == SENSOR_RGB_R)
            {
                DongleAddr_h1 = 0x52;
                DongleAddr_l1 = 0x1A;
                DongleAddr_h2 = 0x52;
                DongleAddr_l2 = 0x1B;
            }
            else if (cmd == SENSOR_RGB_G)
            {
                DongleAddr_h1 = 0x52;
                DongleAddr_l1 = 0x1C;
                DongleAddr_h2 = 0x52;
                DongleAddr_l2 = 0x1D;
            }
            else if (cmd == SENSOR_RGB_B)
            {
                DongleAddr_h1 = 0x52;
                DongleAddr_l1 = 0x1E;
                DongleAddr_h2 = 0x52;
                DongleAddr_l2 = 0x1F;
            }
            else if (cmd == SENSOR_WPT)
            {
                DongleAddr_h1 = 0x3A;
                DongleAddr_l1 = 0x03;
                DongleAddr_h2 = 0x00;   //no use
                DongleAddr_l2 = 0x00;   //no use
            }
            else if (cmd == SENSOR_BPT)
            {
                DongleAddr_h1 = 0x3A;
                DongleAddr_l1 = 0x04;
                DongleAddr_h2 = 0x00;   //no use
                DongleAddr_l2 = 0x00;   //no use
            }
            else
            {
                richTextBox1.Text += "unknown cmd = " + cmd.ToString() + ", abort\n";
                return;
            }

            while (read_camera_sensor0(cmd, DongleAddr_h1, DongleAddr_l1) == false)
            {
                richTextBox1.Text += "read again " + DongleAddr_h1.ToString("X2") + DongleAddr_l1.ToString("X2") + "\n";
                delay(10);
            }

            if ((DongleAddr_h2 == 0x00) && (DongleAddr_l2 == 0x00))
            {
                return;
            }

            while (read_camera_sensor0(cmd, DongleAddr_h2, DongleAddr_l2) == false)
            {
                richTextBox1.Text += "read again " + DongleAddr_h2.ToString("X2") + DongleAddr_l2.ToString("X2") + "\n";
                delay(10);
            }
        }

        private void bt_get_setup_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            lb_awb_result_expo.Text = "";
            lb_awb_result_gain.Text = "";
            lb_awb_result_R.Text = "";
            lb_awb_result_G.Text = "--------";
            lb_awb_result_B.Text = "";
            flag_awb_update_expo = false;
            flag_awb_update_gain = false;
            flag_awb_update_R = false;
            flag_awb_update_G = false;
            flag_awb_update_B = false;

            read_camera_sensor(SENSOR_EXPO);

            read_camera_sensor(SENSOR_GAIN);

            read_camera_sensor(SENSOR_RGB_R);

            read_camera_sensor(SENSOR_RGB_G);

            read_camera_sensor(SENSOR_RGB_B);

        }

        private void numericUpDown_expo_ValueChanged(object sender, EventArgs e)
        {
            trackBar_expo.Value = (Int32)numericUpDown_expo.Value;
            tb_expo.Text = Convert.ToString(trackBar_expo.Value, 16).ToUpper();
        }

        private void numericUpDown_gain_ValueChanged(object sender, EventArgs e)
        {
            trackBar_gain.Value = (Int32)numericUpDown_gain.Value;
            tb_gain.Text = Convert.ToString(trackBar_gain.Value, 16).ToUpper();
        }

        private void numericUpDown_R_ValueChanged(object sender, EventArgs e)
        {
            trackBar_R.Value = (Int32)numericUpDown_R.Value;
            tb_R.Text = Convert.ToString(trackBar_R.Value, 16).ToUpper();
        }

        private void numericUpDown_G_ValueChanged(object sender, EventArgs e)
        {
            trackBar_G.Value = (Int32)numericUpDown_G.Value;
            tb_G.Text = Convert.ToString(trackBar_G.Value, 16).ToUpper();
        }

        private void numericUpDown_B_ValueChanged(object sender, EventArgs e)
        {
            trackBar_B.Value = (Int32)numericUpDown_B.Value;
            tb_B.Text = Convert.ToString(trackBar_B.Value, 16).ToUpper();
        }

        int ccccc = 0;
        int get_expo_data()
        {
            data_expo = -1;
            lb_awb_result_expo.Text = "";
            flag_awb_update_expo = false;

            richTextBox1.Text += "send cmd read sensor expo\n";
            read_camera_sensor(SENSOR_EXPO);

            if (data_expo != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整1" + (ccccc++).ToString() + "\n";

                return S_FALSE;
            }
        }

        /* seperated to 3 functions
        int get_rgb_data()
        {
            int ret;

            ret = get_r_data();
            if (ret == S_FALSE)
            {
                richTextBox1.Text += "資料不完整\n";
                return S_FALSE;
            }

            //skip g

            ret = get_b_data();
            if (ret == S_FALSE)
            {
                richTextBox1.Text += "資料不完整\n";
                return S_FALSE;
            }

            return S_OK;
        }
        */

        int get_r_data()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            data_R = -1;
            lb_awb_result_R.Text = "";
            flag_awb_update_R = false;
            read_camera_sensor(SENSOR_RGB_R);

            if (data_R != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整r\n";
                return S_FALSE;
            }
        }

        int get_g_data()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            data_G = -1;
            lb_awb_result_G.Text = "";
            flag_awb_update_G = false;
            read_camera_sensor(SENSOR_RGB_G);

            if (data_G != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整r\n";
                return S_FALSE;
            }
        }

        int get_b_data()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            data_B = -1;
            lb_awb_result_B.Text = "";
            flag_awb_update_B = false;
            read_camera_sensor(SENSOR_RGB_B);

            if (data_B != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整b\n";
                return S_FALSE;
            }
        }
        
        void test_RGB_saturation()
        {
            int ret = 0;

            ret = precheck_RGB_saturation();
            if (ret == S_OK)
            {
                richTextBox1.Text += "RGB皆未飽和a\n";
                return;
            }
            else
                richTextBox1.Text += "RGB有飽和\n";

            int rgb_ok_cnt = 0;
            while (true)
            {
                //richTextBox1.Text += "test saturation " + i.ToString() + "\n";
                //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";
                if ((total_RGB_R < 255 * awb_block * awb_block) && (total_RGB_G < 255 * awb_block * awb_block) && (total_RGB_B < 255 * awb_block * awb_block))
                {
                    delay(20);
                    rgb_ok_cnt++;
                }
                else
                {
                    ret = get_r_data();

                    ret = get_b_data();

                    delay(30);
                    //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";
                    check_RGB_saturation();
                    delay(30);
                    //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";
                }
                if (rgb_ok_cnt == 5)
                    break;
                if (flag_break == true)
                {
                    richTextBox1.Text += "收到break\n";
                    break;
                }
            }
            richTextBox1.Text += "RGB皆未飽和b\n";
        }

        private void bt_awb_test_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            //if (flag_awb_mode == false)
            {
                lb_rgb.Text = "";
                flag_awb_mode = true;
                timer_webcam.Enabled = false;
                bt_awb.Text = "Auto";
                richTextBox1.Text += "\nTo Auto mode\n";
                //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);
            }

            timer_display.Enabled = true;
            flag_do_awb = true;
            flag_break = false;
            richTextBox1.Text += "\n\n\n";
            richTextBox1.Text += "AWB test ST write 0x3503 as 0x03\n";

            richTextBox1.Text += "開始計時\n";
            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            //no change gain.....
            //richTextBox1.Text += "setup gain to 0x7f = 127\n";
            //Send_IMS_Data(0xA0, 0x35, 0x0A, 0x00);
            //Send_IMS_Data(0xA0, 0x35, 0x0B, 0x7f);

            test_RGB_saturation();

            richTextBox1.Text += "目前時間 : " + stopwatch.Elapsed.Seconds.ToString() + "." + stopwatch.Elapsed.Milliseconds.ToString() + " 秒\n";

            int ret = 0;
            flag_update_RGB_scrollbar = true;

            ret = get_r_data();
            ret = get_b_data();

            if (ret == S_FALSE)
            {
                ret = get_r_data();
                ret = get_b_data();
            }

            //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";

            ret = check_G_exposure(sender, e, total_RGB_G);

            flag_update_RGB_scrollbar = true;

            ret = get_r_data();
            ret = get_b_data();
            if (ret == S_FALSE)
            {
                ret = get_r_data();
                ret = get_b_data();
            }

            if ((ret == S_OK) && (flag_break == false))
            {
                //richTextBox1.Text += "AWB data R G B = " + data_R.ToString() + " " + data_G.ToString() + " " + data_B.ToString() + "\n";

                check_RB_saturation();

                int i;

                for (i = 0; i < 50; i++)
                {
                    richTextBox1.Text += "\ni = " + i.ToString() + "\t";
                    flag_update_RGB_scrollbar = true;

                    ret = get_r_data();
                    ret = get_b_data();
                    if (ret == S_FALSE)
                    {
                        ret = get_r_data();
                        ret = get_b_data();
                    }

                    if (ret == S_OK)
                    {
                        check_RB_data(sender, e);
                        ret = check_RGB_value();
                        if (ret == S_OK)
                        {
                            richTextBox1.Text += "\nRGB皆符合, 完成a\n";
                            break;
                        }
                    }
                    delay(20);
                    check_RB_saturation();
                    ret = check_RGB_value();
                    if (ret == S_OK)
                    {
                        richTextBox1.Text += "\nRGB皆符合, 完成b\n";
                        break;
                    }
                    check_RB_saturation();

                    ret = check_G_exposure(sender, e, total_RGB_G);

                    delay(20);
                    check_RB_saturation();
                    ret = check_RGB_value();
                    if (ret == S_OK)
                    {
                        richTextBox1.Text += "\nRGB皆符合, 完成c\n";
                        break;
                    }

                    if (flag_break == true)
                    {
                        flag_break = false;
                        richTextBox1.Text += "收到break\n";
                        break;
                    }

                }

            }

            //richTextBox1.Text += "AGC auto, EXPO auto\n";
            //Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);

            richTextBox1.Text += "Target  R G B = " + TARGET_AWB_R.ToString() + " " + TARGET_AWB_G.ToString() + " " + TARGET_AWB_B.ToString() + "\n";
            richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";

            richTextBox1.Text += "\nAWB test SP\n";

            richTextBox1.Text += "目前時間 : " + stopwatch.Elapsed.Seconds.ToString() + "." + stopwatch.Elapsed.Milliseconds.ToString() + " 秒\n";

            richTextBox1.Text += "AWB check ST\n";
            int ok_cnt = 0;
            int check_cnt = 0;
            while(true)
            {
                check_cnt++;
                richTextBox1.Text += "i = " + check_cnt.ToString() + "    ";
                if(check_cnt < 5)
                    tolerance_ratio = 2;
                else if (check_cnt < 10)
                    tolerance_ratio = 2;
                else
                    tolerance_ratio = 1;
                ret = awb_modify();
                if (ret == S_OK)
                {
                    ok_cnt++;
                    richTextBox1.Text += "S_OK " + ok_cnt.ToString() + "\n";
                    if (ok_cnt == 3)
                        break;
                }
                else
                    ok_cnt = 0;
            }
            tolerance_ratio = 1;

            richTextBox1.Text += "AWB check SP\n";

            bt_awb.Text = "Manual";
            flag_awb_mode = false;
            timer_webcam.Enabled = true;
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);

            //do not write data to camera
            //write_awb_data_to_camera(data_R, data_B);

            richTextBox1.Text += "目前時間 : " + stopwatch.Elapsed.Seconds.ToString() + "." + stopwatch.Elapsed.Milliseconds.ToString() + " 秒\n";

            // Stop timing
            stopwatch.Stop();

            // Write result
            richTextBox1.Text += "總時間: " + (stopwatch.ElapsedMilliseconds / 1000).ToString() + "." + ((stopwatch.ElapsedMilliseconds % 1000) / 100).ToString() + " 秒\n";
            flag_break = false;
            flag_do_awb = false;
            timer_display.Enabled = false;
        }

        int check_RGB_value()
        {
            if ((flag_R_OK == true) && (flag_G_OK == true) && (flag_B_OK == true))
            {
                return S_OK;
            }
            else
            {
                return S_FALSE;
            }
        }

        int check_G_exposure(object sender, EventArgs e, int rgb_g)
        {
            int ret = 0;
            int diff = 0;

            //rgb_g = rgb_g / awb_block / awb_block;

            //richTextBox1.Text += "check G expo : rgb_g = " + rgb_g.ToString() + " RGB_G = " + (rgb_g / (awb_block * awb_block)).ToString() + "  TG_G = " + TARGET_AWB_G.ToString() + "\t";
            if ((rgb_g >= (TARGET_AWB_G * awb_block * awb_block - 1 * awb_block * awb_block)) && (rgb_g <= (TARGET_AWB_G * awb_block * awb_block + 1 * awb_block * awb_block)))
            {
                //richTextBox1.Text += "G已在目標內\n";
                return S_OK;
            }

            if (rgb_g < (TARGET_AWB_G * awb_block * awb_block - 1 * awb_block * awb_block))
            {
                //richTextBox1.Text += "G太小 要增加expo\n";
                while (rgb_g < (TARGET_AWB_G * awb_block * awb_block - 1 * awb_block * awb_block))
                {
                    richTextBox1.Text += "call get_expo_data\t";
                    ret = get_expo_data();
                    if (ret == S_OK)
                    {
                        if ((data_expo < 0) || (data_expo > 500))
                        {
                            richTextBox1.Text += "impossible data_expo " + data_expo.ToString() + "\n";
                            return S_FALSE;
                        }

                        if (data_expo == 511)
                        {
                            richTextBox1.Text += "reach expo max\n";
                            return S_FALSE;
                        }
                        diff = TARGET_AWB_G * awb_block * awb_block - rgb_g;
                        //diff = diff * 10 / 4;
                        diff = diff * 1 / (awb_block * awb_block);
                        if (diff > 20)
                            diff = 20;

                        data_expo += diff;
                        diff_g = diff;
                        timer_display_g_count = 0;
                        richTextBox1.Text += "E+" + diff.ToString() + " ";

                        if (data_expo > 500)
                            data_expo = 500;

                        if ((data_expo < 0) || (data_expo > 500))
                            richTextBox1.Text += "xxxxxxxxxxxxxxxx  data_expo " + data_expo.ToString() + "\n";
                        else
                        {
                            numericUpDown_expo.Value = data_expo;
                            bt_setup_expo_Click(sender, e);
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "read expo fail, delay long\n";
                        delay(300);
                    }
                    delay(20);
                    rgb_g = total_RGB_G;
                    check_RB_saturation();
                }
            }
            else if (rgb_g > (TARGET_AWB_G * awb_block * awb_block + 1 * awb_block * awb_block))
            {
                while (rgb_g > (TARGET_AWB_G * awb_block * awb_block + 1 * awb_block * awb_block))
                {
                    //richTextBox1.Text += "G太大 要減少expo\n";
                    ret = get_expo_data();
                    if (ret == S_OK)
                    {
                        if ((data_expo < 0) || (data_expo > 511))
                        {
                            richTextBox1.Text += "impossible data_expo " + data_expo.ToString() + "\n";
                            return S_FALSE;
                        }

                        if (data_expo == 0)
                        {
                            richTextBox1.Text += "reach expo min\n";
                            return S_FALSE;
                        }
                        diff = rgb_g - TARGET_AWB_G * awb_block * awb_block;
                        //diff = diff * 10 / 4;
                        diff = diff * 1 / (awb_block * awb_block);
                        if (diff > 20)
                            diff = 20;
                        
                        data_expo -= diff;
                        diff_g = -diff;
                        timer_display_g_count = 0;
                        richTextBox1.Text += "E-" + diff.ToString() + " ";

                        if (data_expo < 0)
                            data_expo = 0;

                        if ((data_expo < 0) || (data_expo > 511))
                            richTextBox1.Text += "xxxxxxxxxxxxxxxx  data_expo " + data_expo.ToString() + "\n";
                        else
                        {
                            numericUpDown_expo.Value = data_expo;
                            bt_setup_expo_Click(sender, e);
                        }
                    }
                    delay(100);
                    rgb_g = total_RGB_G;
                    check_RB_saturation();
                }
            }
            else
                diff_g =0;
            //richTextBox1.Text += "G抵達目標 目前 " + (rgb_g / (awb_block * awb_block)).ToString() + " 目標 " + TARGET_AWB_G.ToString() + "\n\n";
            return S_OK;
        }

        void check_RB_saturation()
        {
            if (total_RGB_R == 255 * awb_block * awb_block)
            {
                if (data_R == -1)
                {
                    richTextBox1.Text += "讀資料R錯誤 跳過\n";
                }
                else
                {
                    int SendData = data_R - 100;
                    richTextBox1.Text += "飽和 目前 data_R = " + data_R.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";

                    if (SendData > 500)
                        numericUpDown_R.Value = SendData;
                    byte dd;

                    dd = (byte)(SendData / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1A;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1B;

                    dd = (byte)(SendData % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }
            //else
                //richTextBox1.Text += "R 未飽和\n";

            if (total_RGB_B == 255 * awb_block * awb_block)
            {
                if (data_B == -1)
                {
                    richTextBox1.Text += "讀資料B錯誤 跳過\n";
                }
                else
                {
                    int SendData = data_B - 100;
                    richTextBox1.Text += "飽和 目前 data_B = " + data_B.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";

                    if (SendData > 500)
                        numericUpDown_B.Value = SendData;
                    byte dd;

                    dd = (byte)(SendData / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1E;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1F;

                    dd = (byte)(SendData % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }
            //else
                //richTextBox1.Text += "B 未飽和\n";
        }

        void check_RGB_saturation()
        {
            if (total_RGB_R == 255 * awb_block * awb_block)
            {
                if (data_R == -1)
                {
                    richTextBox1.Text += "讀資料錯誤 跳過1\n";
                }
                else
                {
                    diff_r = -99;
                    timer_display_r_count = 0;

                    int SendData = data_R - 99;
                    //richTextBox1.Text += "\n飽和 目前 data_R = " + data_R.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";
                    richTextBox1.Text += "R飽和 -99\n";

                    if (SendData > 500)
                        numericUpDown_R.Value = SendData;
                    byte dd;

                    dd = (byte)(SendData / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1A;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1B;

                    dd = (byte)(SendData % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }
            //else
            //richTextBox1.Text += "R 未飽和\n";

            if (total_RGB_G == 255 * awb_block * awb_block)
            {
                int ret;
                ret = get_expo_data();

                if (ret == S_OK)
                {
                    //richTextBox1.Text += "飽和 目前 expo = " + data_expo.ToString() + " 減一些 減成 " + (data_expo - 10).ToString() + "\n";
                    richTextBox1.Text += "G飽和 -10\n";

                    if ((data_expo < 0) || (data_expo > 511))
                    {
                        richTextBox1.Text += "impossible data_expo " + data_expo.ToString() + "\n";
                        richTextBox1.Text += "讀資料錯誤 跳過2\n";
                    }
                    else if (data_expo == 0)
                    {
                        richTextBox1.Text += "reach expo min\n";
                        richTextBox1.Text += "跳過\n";
                    }
                    else
                    {
                        diff_g = -10;
                        timer_display_g_count = 0;
                        data_expo -= 10;
                        //richTextBox1.Text += "G dec " + data_expo.ToString() + " ";

                        if (data_expo < 0)
                            data_expo = 0;

                        if ((data_expo < 0) || (data_expo > 511))
                            richTextBox1.Text += "xxxxxxxxxxxxxxxx  data_expo " + data_expo.ToString() + "\n";
                        else
                        {
                            numericUpDown_expo.Value = data_expo;

                            int SendData = data_expo;
                            byte dd;

                            dd = (byte)(SendData / 256);
                            DongleAddr_h = 0x35;
                            DongleAddr_l = 0x01;
                            //Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                            DongleAddr_h = 0x35;
                            DongleAddr_l = 0x02;

                            dd = (byte)(SendData % 256);
                            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);

                        }
                    }
                }
                delay(100);
            }
            //else
            //richTextBox1.Text += "R 未飽和\n";

            if (total_RGB_B == 255 * awb_block * awb_block)
            {
                if (data_B == -1)
                {
                    richTextBox1.Text += "讀資料錯誤 跳過3\n";
                }
                else
                {
                    diff_b = -99;
                    timer_display_b_count = 0;
                    int SendData = data_B - 99;
                    //richTextBox1.Text += "飽和 目前 data_B = " + data_B.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";
                    richTextBox1.Text += "B飽和 -99\n";

                    if (SendData > 500)
                        numericUpDown_B.Value = SendData;
                    byte dd;

                    dd = (byte)(SendData / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1E;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1F;

                    dd = (byte)(SendData % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }
            //else
            //richTextBox1.Text += "B 未飽和\n";
        }

        void check_RB_data(object sender, EventArgs e)
        {
            int diff = 0;
            int R_OK = 0;
            int B_OK = 0;

            //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";

            //richTextBox1.Text += "RGB_R = " + (total_RGB_R / awb_block / awb_block).ToString() + "\tTG_AWB_R = " + TARGET_AWB_R.ToString() + "\t";
            //if ((total_RGB_R / awb_block / awb_block) > (TARGET_AWB_R + 1))
            if (total_RGB_R > (TARGET_AWB_R * awb_block * awb_block + 1 * awb_block * awb_block))
            {
                //diff = (total_RGB_R / awb_block / awb_block) - (TARGET_AWB_R + 1);
                //diff = (total_RGB_R / awb_block / awb_block) - (TARGET_AWB_R + 1);
                diff = total_RGB_R - (TARGET_AWB_R * awb_block * awb_block + 1 * awb_block * awb_block);
                diff = diff * 16 / (awb_block * awb_block);
                if (diff > 40)
                    diff = 40;

                diff_r = -diff;
                timer_display_r_count = 0;

                //richTextBox1.Text += "\ntotal_RGB_R = " + total_RGB_R.ToString() + ", TARGET_AWB_R = " + TARGET_AWB_R.ToString() + "\n";
                //richTextBox1.Text += "R太大 減低R_data, 目前data_R = " + data_R.ToString() + ", 減 " + diff.ToString() + "\n";
                richTextBox1.Text += "R-" + diff.ToString() + " ";

                int SendData = data_R - diff;
                //trackBar_R.Value = SendData;
                numericUpDown_R.Value = SendData;
                byte dd;

                dd = (byte)(SendData / 256);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1A;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1B;

                dd = (byte)(SendData % 256);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            }
            //else if ((total_RGB_R / awb_block / awb_block) < (TARGET_AWB_R - 1))
            else if (total_RGB_R < (TARGET_AWB_R * awb_block * awb_block - 1 * awb_block * awb_block))
            {
                diff = (TARGET_AWB_R * awb_block * awb_block - 1 * awb_block * awb_block) - total_RGB_R;
                diff = diff * 16 / (awb_block * awb_block);
                if (diff > 40)
                    diff = 40;

                diff_r = diff;
                timer_display_r_count = 0;

                //richTextBox1.Text += "\ntotal_RGB_R = " + total_RGB_R.ToString() + ", TARGET_AWB_R = " + TARGET_AWB_R.ToString() + "\n";
                //richTextBox1.Text += "R太小 增加R_data, 目前data_R = " + data_R.ToString() + ", 加 " + diff.ToString() + "\n";
                richTextBox1.Text += "R+" + diff.ToString() + " ";

                int SendData = data_R + diff;
                //trackBar_R.Value = SendData;
                numericUpDown_R.Value = SendData;
                byte dd;

                dd = (byte)(SendData / 256);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1A;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1B;

                dd = (byte)(SendData % 256);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            }
            else
            {
                //richTextBox1.Text += "R已在目標內\n";
                R_OK = 1;
                diff_r = 0;
            }

            //richTextBox1.Text += "RGB_B = " + (total_RGB_B / awb_block / awb_block).ToString() + "\tTG_AWB_B = " + TARGET_AWB_B.ToString() + "\t";
            if (total_RGB_B > (TARGET_AWB_B * awb_block * awb_block + 1 * awb_block * awb_block))
            {
                diff = total_RGB_B - (TARGET_AWB_B * awb_block * awb_block + 1 * awb_block * awb_block);
                diff = diff * 16 / (awb_block * awb_block);
                if (diff > 40)
                    diff = 40;

                diff_b = -diff;
                timer_display_b_count = 0;

                //richTextBox1.Text += "B太大 減低B_data, 目前data_B = " + data_B.ToString() + ", 減 " + diff.ToString() + "\n";
                richTextBox1.Text += "B-" + diff.ToString() + " ";

                int SendData = data_B - diff;
                //trackBar_B.Value = SendData;
                numericUpDown_B.Value = SendData;
                byte dd;

                dd = (byte)(SendData / 256);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1E;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1F;

                dd = (byte)(SendData % 256);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            }
            else if (total_RGB_B < (TARGET_AWB_B * awb_block * awb_block - 1 * awb_block * awb_block))
            {
                diff = (TARGET_AWB_B * awb_block * awb_block - 1 * awb_block * awb_block) - total_RGB_B;
                diff = diff * 16 / (awb_block * awb_block);
                if (diff > 40)
                    diff = 40;

                diff_b = diff;
                timer_display_b_count = 0;

                //richTextBox1.Text += "B太小 增加B_data, 目前data_B = " + data_B.ToString() + ", 加 " + diff.ToString() + "\n";
                richTextBox1.Text += "B+" + diff.ToString() + " ";

                int SendData = data_B + diff;
                //trackBar_B.Value = SendData;
                numericUpDown_B.Value = SendData;
                byte dd;

                dd = (byte)(SendData / 256);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1E;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                DongleAddr_h = 0x52;
                DongleAddr_l = 0x1F;

                dd = (byte)(SendData % 256);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            }
            else
            {
                //richTextBox1.Text += "B已在目標內\n";
                B_OK = 1;
                diff_b = 0;
            }
            if ((R_OK == 1) && (B_OK == 1))
                richTextBox1.Text += "\n";

        }

        private void bt_awb_test_init_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            richTextBox1.Text += "回復初始值\n";

            int SendData = 134;
            byte dd;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x01;
            //Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x02;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);

            SendData = 5;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x0A;
            //Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x35;
            DongleAddr_l = 0x0B;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);


            SendData = 1456;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1A;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1B;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);


            SendData = 1024;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1C;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1D;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);

            SendData = 1648;

            dd = (byte)(SendData / 256);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1E;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1F;

            dd = (byte)(SendData % 256);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        private void bt_goto_awb_Click(object sender, EventArgs e)
        {
            if (flag_release_mode == false)
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
                        MessageBox.Show("無法連上Comport, 請重新連線");
                }
            }

            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                flag_comport_ok = true;
            }

            tabControl1.SelectedTab = tp_USB;

            button19_Click(sender, e);

            bt_goto_awb.Visible = false;
        }

        private void numericUpDown_TG_R_ValueChanged(object sender, EventArgs e)
        {
            TARGET_AWB_R = (Int32)numericUpDown_TG_R.Value;
            refresh_picturebox2();
        }

        private void numericUpDown_TG_G_ValueChanged(object sender, EventArgs e)
        {
            TARGET_AWB_G = (Int32)numericUpDown_TG_G.Value;
            refresh_picturebox2();
        }

        private void numericUpDown_TG_B_ValueChanged(object sender, EventArgs e)
        {
            TARGET_AWB_B = (Int32)numericUpDown_TG_B.Value;
            refresh_picturebox2();
        }

        private void comboBox_temperature_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox_temperature.SelectedIndex == 0)
            {
                richTextBox1.Text += "3800K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 204;
                TARGET_AWB_B = 153;
            }
            else if (comboBox_temperature.SelectedIndex == 1)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 213;
                TARGET_AWB_B = 173;
            }
            else if (comboBox_temperature.SelectedIndex == 2)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 221;
                TARGET_AWB_B = 190;
            }
            else if (comboBox_temperature.SelectedIndex == 3)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 236;
                TARGET_AWB_B = 224;
            }
            else if (comboBox_temperature.SelectedIndex == 4)
            {
                richTextBox1.Text += "5700K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 239;
                TARGET_AWB_B = 230;
            }
            else if (comboBox_temperature.SelectedIndex == 5)
            {
                richTextBox1.Text += "6500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 249;
                TARGET_AWB_B = 253;
            }
            else if (comboBox_temperature.SelectedIndex == 6)
            {
                richTextBox1.Text += "6700K\n";
                TARGET_AWB_R = 252;
                TARGET_AWB_G = 247;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 7)
            {
                richTextBox1.Text += "6900K\n";
                TARGET_AWB_R = 247;
                TARGET_AWB_G = 245;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 8)
            {
                richTextBox1.Text += "7100K\n";
                TARGET_AWB_R = 243;
                TARGET_AWB_G = 242;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 9)
            {
                richTextBox1.Text += "7300K\n";
                TARGET_AWB_R = 239;
                TARGET_AWB_G = 240;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 10)
            {
                richTextBox1.Text += "7500K\n";
                TARGET_AWB_R = 235;
                TARGET_AWB_G = 238;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 11)
            {
                richTextBox1.Text += "8500K\n";
                TARGET_AWB_R = 220;
                TARGET_AWB_G = 229;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 12)
            {
                richTextBox1.Text += "9500K\n";
                TARGET_AWB_R = 208;
                TARGET_AWB_G = 222;
                TARGET_AWB_B = 255;
            }
            else
                richTextBox1.Text += "XXXXXXXXXX\n";

            numericUpDown_TG_R.Value = TARGET_AWB_R;
            numericUpDown_TG_G.Value = TARGET_AWB_G;
            numericUpDown_TG_B.Value = TARGET_AWB_B;
            refresh_picturebox2();
        }

        void refresh_picturebox2()
        {
            if (flag_awb_debug == false)
                return;
            if (flag_us_debug == true)
                return;

            int x_st = 0;
            int y_st = 0;
            int ww = awb_block;
            int hh = awb_block;


            int WW = 640 * 1;
            int HH = 480 * 1;

            x_st = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step;
            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > WW)
                x_st = WW - ww;

            y_st = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step;
            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > HH)
                y_st = HH - hh;

            x_st *= 2;
            y_st *= 2;
            ww *= 2;
            hh *= 2;
            ww++;
            hh++;

            //richTextBox1.Text += "refresh_picturebox2 x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + " ww = " + ww.ToString() + " hh = " + hh.ToString() + "\n";
            //pictureBox2.Location = new Point(x_st, y_st + hh + 10);

            pictureBox2.Location = new Point(pictureBox1.Location.X + x_st, pictureBox1.Location.Y + y_st + hh + 10);

            //pictureBox2.Location = new Point(600, 600);
            pictureBox2.Size = new Size(ww, hh);

            Graphics g;
            Bitmap bmp;
            //逐點製作圖檔
            int xx;
            int yy;

            bmp = new Bitmap(ww, hh);

            //background
            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    bmp.SetPixel(xx, yy, Color.FromArgb(255, TARGET_AWB_R, TARGET_AWB_G, TARGET_AWB_B));
                    //bitmap3.SetPixel(xx, yy, Color.Red);
                }
            }

            g = Graphics.FromImage(bmp);
            g.DrawRectangle(new Pen(Color.Silver, 2), 1, 1, ww - 2, hh - 2);

            pictureBox2.Image = bmp;
        }

        private void bt_break_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "BREAK\n";
            flag_break = true;
        }

        private void numericUpDown_R_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_R_Click(sender, e);
            }
        }

        private void numericUpDown_G_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_G_Click(sender, e);
            }
        }

        private void numericUpDown_B_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_B_Click(sender, e);
            }
        }

        void enable_camera_streaming(bool enable)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte dd;
            if (enable == true)
            {
                dd = 1;     //Streaming
            }
            else
            {
                dd = 0;     //Sleep
            }
            DongleAddr_h = 0x01;
            DongleAddr_l = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
        }

        void to_awb_auto_mode()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            //flag_awb_mode = false;
            //timer_webcam.Enabled = true;
            bt_awb.Text = "Manual";
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);
        }

        void to_awb_manual_mode()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            //flag_awb_mode = true;
            //timer_webcam.Enabled = false;
            bt_awb.Text = "Auto";
            //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);
        }

        private void bt_disable_timer_webcam_Click(object sender, EventArgs e)
        {
            if (timer_webcam.Enabled == true)
            {
                richTextBox1.Text += "Disable Timer WebCam\n";
                timer_webcam.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "Enable Timer WebCam\n";
                timer_webcam.Enabled = true;
                timer_webcam_cnt = 0;

            }
        }

        private void tb_3a_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_Click(sender, e);
            }
        }

        private void tb_4a_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_Click(sender, e);
            }
        }

        private void tb_1a_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_read_Click(sender, e);
            }
        }

        private void tb_2a_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_read_Click(sender, e);
            }
        }

        private void numericUpDown_gain_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_gain_Click(sender, e);
            }
        }

        private void numericUpDown_expo_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_setup_expo_Click(sender, e);
            }
        }

        private void bt_read_wpt_Click(object sender, EventArgs e)
        {
            tb_wpt.Text = "";
            read_camera_sensor(SENSOR_WPT);
        }

        private void bt_read_bpt_Click(object sender, EventArgs e)
        {
            tb_bpt.Text = "";
            read_camera_sensor(SENSOR_BPT);
        }

        private void numericUpDown_wpt_ValueChanged(object sender, EventArgs e)
        {
            tb_wpt.Text = Convert.ToString((Int32)numericUpDown_wpt.Value, 16).ToUpper();
        }

        private void numericUpDown_bpt_ValueChanged(object sender, EventArgs e)
        {
            tb_bpt.Text = Convert.ToString((Int32)numericUpDown_bpt.Value, 16).ToUpper();
        }

        private void tb_wpt_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_wpt_Click(sender, e);
            }
        }

        private void tb_bpt_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_bpt_Click(sender, e);
            }
        }

        private void tb_wpt_TextChanged(object sender, EventArgs e)
        {
            if (tb_wpt.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_wpt.Text, 16);
            if ((value < 0) || (value > 255))
            {
                tb_wpt.Text = "";
                return;
            }
            numericUpDown_wpt.Value = value;
        }

        private void tb_bpt_TextChanged(object sender, EventArgs e)
        {
            if (tb_bpt.Text.Length == 0)
            {
                return;
            }

            int value = Convert.ToInt32(tb_bpt.Text, 16);
            if ((value < 0) || (value > 255))
            {
                tb_gain.Text = "";
                return;
            }
            numericUpDown_bpt.Value = value;
        }

        private void bt_write_wpt_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte SendData = (byte)numericUpDown_wpt.Value;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        }

        private void bt_write_bpt_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte SendData = (byte)numericUpDown_bpt.Value;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x04;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        }

        private void numericUpDown_wpt_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_wpt_Click(sender, e);
            }
        }

        private void numericUpDown_bpt_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_decimal(e);
            
            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                bt_write_bpt_Click(sender, e);
            }
        }

        bool check_textbox_decimal(KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            

            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        bool check_textbox_hexadecimal(KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            

            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                return false;
            }
            else if ((e.KeyChar >= (Char)'A') && (e.KeyChar <= (Char)'F'))
            {
                return false;
            }
            else if ((e.KeyChar >= (Char)'a') && (e.KeyChar <= (Char)'f'))
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        int awb_modify()
        {
            flag_check_rgb = true;
            rgb_check_cnt = 0;
            rgb_r_ok_cnt = 0;
            rgb_g_ok_cnt = 0;
            rgb_b_ok_cnt = 0;
            rgb_r_fail_high_cnt = 0;
            rgb_r_fail_low_cnt = 0;
            rgb_g_fail_high_cnt = 0;
            rgb_g_fail_low_cnt = 0;
            rgb_b_fail_high_cnt = 0;
            rgb_b_fail_low_cnt = 0;

            while (flag_check_rgb == true)
            {
                richTextBox1.Text += " .";
                delay(100);
            }

            //richTextBox1.Text += "\n";
            //richTextBox1.Text += "R : " + CHECK_AWB_FRAME.ToString() + "  /  OK : " + rgb_r_ok_cnt.ToString() + "  /  H : " + rgb_r_fail_high_cnt.ToString() + "  /  L : " + rgb_r_fail_low_cnt.ToString() + "\n";
            //richTextBox1.Text += "G : " + CHECK_AWB_FRAME.ToString() + "  /  OK : " + rgb_g_ok_cnt.ToString() + "  /  H : " + rgb_g_fail_high_cnt.ToString() + "  /  L : " + rgb_g_fail_low_cnt.ToString() + "\n";
            //richTextBox1.Text += "B : " + CHECK_AWB_FRAME.ToString() + "  /  OK : " + rgb_b_ok_cnt.ToString() + "  /  H : " + rgb_b_fail_high_cnt.ToString() + "  /  L : " + rgb_b_fail_low_cnt.ToString() + "\n";

            int ret;
            int data_new;
            int diff;

            if (rgb_g_ok_cnt != CHECK_AWB_FRAME)
            {
                ret = get_expo_data();
                if (ret == S_OK)
                {
                    diff = (rgb_g_fail_high_cnt - rgb_g_fail_low_cnt) / 10;
                    if (diff == 0)
                    {
                        if (rgb_g_fail_high_cnt > rgb_g_fail_low_cnt)
                            diff = 1;
                        else
                            diff = -1;
                    }
                    else if (diff > 0)
                        diff = 1;
                    else if (diff < 0)
                        diff = -1;
                    data_new = data_expo - diff;
                    diff_g = -diff;
                    timer_display_g_count = 0;
                    /*
                    richTextBox1.Text += "data_expo_old = " + data_expo.ToString();
                    if (diff > 0)
                        richTextBox1.Text += ", 減少 " + diff.ToString() + "\n";
                    else
                        richTextBox1.Text += ", 增加 " + (-diff).ToString() + "\n";
                    */
                    if (diff > 0)
                        richTextBox1.Text += "E-";
                    else
                        richTextBox1.Text += "E+";
                    numericUpDown_expo.Value = data_new;
                    byte dd;

                    dd = (byte)(data_new / 256);
                    DongleAddr_h = 0x35;
                    DongleAddr_l = 0x01;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x35;
                    DongleAddr_l = 0x02;

                    dd = (byte)(data_new % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);

                }
            }

            if (rgb_r_ok_cnt != CHECK_AWB_FRAME)
            {
                ret = get_r_data();
                if (ret == S_OK)
                {
                    diff = (rgb_r_fail_high_cnt - rgb_r_fail_low_cnt) / 2;
                    if (diff == 0)
                    {
                        if (rgb_r_fail_high_cnt > rgb_r_fail_low_cnt)
                            diff = 1;
                        else
                            diff = -1;
                    }
                    else if (diff > 0)
                        diff = 1;
                    else if (diff < 0)
                        diff = -1;
                    data_new = data_R - diff;
                    diff_r = -diff;
                    timer_display_r_count = 0;

                    /*
                    richTextBox1.Text += "data_R_old = " + data_R.ToString();
                    if (diff > 0)
                        richTextBox1.Text += ", 減少 " + diff.ToString() + "\n";
                    else
                        richTextBox1.Text += ", 增加 " + (-diff).ToString() + "\n";
                    */
                    if (diff > 0)
                        richTextBox1.Text += "R-";
                    else
                        richTextBox1.Text += "R+";
                    numericUpDown_R.Value = data_new;
                    byte dd;

                    dd = (byte)(data_new / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1A;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1B;

                    dd = (byte)(data_new % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }
            if (rgb_b_ok_cnt != CHECK_AWB_FRAME)
            {
                ret = get_b_data();
                if (ret == S_OK)
                {
                    diff = (rgb_b_fail_high_cnt - rgb_b_fail_low_cnt) / 2;
                    if (diff == 0)
                    {
                        if (rgb_b_fail_high_cnt > rgb_b_fail_low_cnt)
                            diff = 1;
                        else
                            diff = -1;
                    }
                    else if (diff > 0)
                        diff = 1;
                    else if (diff < 0)
                        diff = -1;
                    data_new = data_B - diff;
                    diff_b = -diff;
                    timer_display_b_count = 0;

                    /*
                    richTextBox1.Text += "data_B_old = " + data_B.ToString();
                    if (diff > 0)
                        richTextBox1.Text += ", 減少 " + diff.ToString() + "\n";
                    else
                        richTextBox1.Text += ", 增加 " + (-diff).ToString() + "\n";
                    */
                    if (diff > 0)
                        richTextBox1.Text += "B-";
                    else
                        richTextBox1.Text += "B+";
                    numericUpDown_B.Value = data_new;
                    byte dd;

                    dd = (byte)(data_new / 256);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1E;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                    DongleAddr_h = 0x52;
                    DongleAddr_l = 0x1F;

                    dd = (byte)(data_new % 256);
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, dd);
                }
            }

            delay(50);

            if ((rgb_r_ok_cnt == CHECK_AWB_FRAME) && (rgb_g_ok_cnt == CHECK_AWB_FRAME) && (rgb_b_ok_cnt == CHECK_AWB_FRAME))
                return S_OK;
            else
            {
                richTextBox1.Text += "\n";
                return S_FALSE;
            }
        }

        private void bt_awb_test2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "AWB check ST\n";
            tolerance_ratio = 2;
            int i;
            int ok_cnt = 0;
            int ret;
            for (i = 0; i < 20; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "  ";
                ret = awb_modify();
                if (ret == S_OK)
                {
                    ok_cnt++;
                    richTextBox1.Text += "S_OK " + ok_cnt.ToString() + "\n";
                    if (ok_cnt == 3)
                        break;
                }
                else
                    ok_cnt = 0;
            }
            tolerance_ratio = 1;
            richTextBox1.Text += "AWB check SP\n";
        }

        int precheck_RGB_saturation()
        {
            richTextBox1.Text += "precheck RGB saturation ST\n";
            rgb_saturation_check_cnt = 0;
            rgb_r_saturation_cnt = 0;
            rgb_g_saturation_cnt = 0;
            rgb_b_saturation_cnt = 0;
            flag_check_rgb_saturation = true;

            while (flag_check_rgb_saturation == true)
            {
                richTextBox1.Text += " .";
                delay(100);
            }
            //richTextBox1.Text += "\n";
            //richTextBox1.Text += "R_saturation = " + rgb_r_saturation_cnt.ToString() + "\n";
            //richTextBox1.Text += "G_saturation = " + rgb_g_saturation_cnt.ToString() + "\n";
            //richTextBox1.Text += "B_saturation = " + rgb_b_saturation_cnt.ToString() + "\n";
            if ((rgb_r_saturation_cnt == 0) && (rgb_g_saturation_cnt == 0) && (rgb_b_saturation_cnt == 0))
                return S_OK;
            else
                return S_FALSE;
        }

        void write_awb_data_to_camera(int data_r, int data_b)
        {
            richTextBox1.Text += "wrtie awb data to AWB_PAGE\n";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int i;
            for (i = 0; i < 4; i++)
            {
                awb_data_send[i] = 0;
            }
            awb_data_send[0] = (byte)(data_r / 256);
            awb_data_send[1] = (byte)(data_r % 256);
            awb_data_send[2] = (byte)(data_b / 256);
            awb_data_send[3] = (byte)(data_b % 256);

            Send_IMS_Data(0xE2, 0x12, 0x34, 0x56);   //camera awb write
            serialPort1.Write(awb_data_send, 0, 4);
            richTextBox1.Text += "寫入AWB資料完成\n";
        }

        private void bt_test_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "none\n";
            //write_awb_data_to_camera(data_R, data_B);

            //check_webcam();

            check_comport();

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_erase_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "erase all camera flash data\n";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xEE, 0xFF, 0xEE, 0xFF);   //erase all camera flash data
        }

        int check_webcam()
        {
            comboBox_webcam.Items.Clear();
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            VideoCaptureDevice Cam_tmp = null;

            richTextBox1.Text += "check_webcam ST\n";

            //USBWebcams2 = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                richTextBox1.Text += "There are " + USBWebcams.Count.ToString() + " camera(s)\n";
                for (int i = 0; i < USBWebcams.Count; i++)
                {
                    richTextBox1.Text += "camera " + i.ToString() + "\n";
                    richTextBox1.Text += "name : " + USBWebcams[i].Name + "\n";
                    richTextBox1.Text += "MonikerString: " + USBWebcams[i].MonikerString + "\n";

                    Cam_tmp = new VideoCaptureDevice(USBWebcams[i].MonikerString);  //實例化對象
                    Cam_tmp.VideoResolution = Cam_tmp.VideoCapabilities[0];


                    richTextBox1.Text += "FR1 = " + Cam_tmp.VideoCapabilities[0].AverageFrameRate.ToString() + "\n";
                    //richTextBox1.Text += "FR1 = " + Cam_tmp.VideoCapabilities[0].FrameRate.ToString();
                    richTextBox1.Text += "W = " + Cam_tmp.VideoCapabilities[0].FrameSize.Width.ToString() + "\n";
                    richTextBox1.Text += "H = " + Cam_tmp.VideoCapabilities[0].FrameSize.Height.ToString() + "\n";
                    /*
                    richTextBox1.Text += "BitCount = " + Cam_tmp.VideoCapabilities[0].BitCount.ToString() + "\n";
                    richTextBox1.Text += "FR_max = " + Cam_tmp.VideoCapabilities[0].MaximumFrameRate.ToString() + "\n";
                    richTextBox1.Text += "ProvideSnapshots = " + Cam_tmp.ProvideSnapshots.ToString() + "\n";
                    if (Cam_tmp.ProvideSnapshots == true)
                    {
                        richTextBox1.Text += "Snapshot len = " + Cam_tmp.SnapshotCapabilities.Length.ToString() + "\n";
                        richTextBox1.Text += "Snapshot W = " + Cam_tmp.SnapshotResolution.FrameSize.Width.ToString() + "\n";
                        richTextBox1.Text += "Snapshot H = " + Cam_tmp.SnapshotResolution.FrameSize.Height.ToString() + "\n";
                        richTextBox1.Text += "Snapshot FR = " + Cam_tmp.SnapshotResolution.MaximumFrameRate.ToString() + "\n";
                    }
                    richTextBox1.Text += "Cam.Source = " + Cam_tmp.Source.ToString() + "\n";
                    richTextBox1.Text += "Cam.Source.Length = " + Cam_tmp.Source.Length.ToString() + "\n";
                    richTextBox1.Text += "FrameRate = " + Cam_tmp.VideoResolution.FrameRate.ToString() + "\n";    //old
                    richTextBox1.Text += "FrameSize.W = " + Cam_tmp.VideoResolution.FrameSize.Width.ToString() + "\n";
                    richTextBox1.Text += "FrameSize.H = " + Cam_tmp.VideoResolution.FrameSize.Height.ToString() + "\n";
                    */

                    string webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name + " " + Cam_tmp.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam_tmp.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam_tmp.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";

                    comboBox_webcam.Items.Add(webcam_name);
                    richTextBox1.Text += webcam_name + "\n";

                    richTextBox1.Text += "\n";


                }

                for (int i = 0; i < USBWebcams.Count; i++)
                {
                    if (USBWebcams[i].Name == "InsightEyes")
                    {
                        richTextBox1.Text += "有InsightEyes影像裝置 在 i = " + i.ToString() + "\n";

                        Cam = new VideoCaptureDevice(USBWebcams[i].MonikerString);  //實例化對象
                        Cam.VideoResolution = Cam.VideoCapabilities[0];
                        Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);     //綁定事件

                        Cam.Start();   // WebCam starts capturing images.
                        flag_camera_start = 1;

                        comboBox_webcam.Text = comboBox_webcam.Items[i].ToString();
                        break;
                    }

                }

                if (flag_camera_start != 1)     //若是找不到InsightEyes, 用第1個
                {
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                    Cam.VideoResolution = Cam.VideoCapabilities[0];
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);     //綁定事件

                    Cam.Start();   // WebCam starts capturing images.
                    flag_camera_start = 1;
                    richTextBox1.Text += "有影像裝置\n";
                }
            }
            else
            {
                richTextBox1.Text += "無影像裝置\n";
                return S_FALSE;
            }
            return S_OK;
        }

        private void comboBox_webcam_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "你選取了" + comboBox_webcam.SelectedItem.ToString() + "\n";
            richTextBox1.Text += "SelectedIndex = " + comboBox_webcam.SelectedIndex.ToString() + "\n";

            flag_camera_start = 0;
            //Cam.Stop();  // WebCam stops capturing images.
            Cam.SignalToStop();
            Cam.WaitForStop();

            Cam = new VideoCaptureDevice(USBWebcams[comboBox_webcam.SelectedIndex].MonikerString);
            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
            Cam.Start();   // WebCam starts capturing images.
            flag_camera_start = 1;

        }

        void check_comport()
        {
            richTextBox1.Text += "check_comport ST\n";
            string[] tempString = SerialPort.GetPortNames();

            richTextBox1.Text += "共抓到 " + tempString.Length.ToString() + " 個 comport\n";
            foreach (string aaa in tempString)
            {
                richTextBox1.Text += "get comport : " + aaa + "\n";
            }


            /*
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += "get comport : " + port + "\n";
                richTextBox1.Text += "port.Length : " + port.Length.ToString() + "\n";

            }
            */



        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_r_count < 10)
            {
                timer_display_r_count++;
                flag_display_r_do_awb = true;
            }
            else
                flag_display_r_do_awb = false;

            if (timer_display_g_count < 10)
            {
                timer_display_g_count++;
                flag_display_g_do_awb = true;
            }
            else
                flag_display_g_do_awb = false;

            if (timer_display_b_count < 10)
            {
                timer_display_b_count++;
                flag_display_b_do_awb = true;
            }
            else
                flag_display_b_do_awb = false;

            if (timer_display_save_count < 10)
            {
                timer_display_save_count++;
                if (timer_display_save_count == 10)
                    lb_save_message.Text = "";
            }
        }
    }
}

