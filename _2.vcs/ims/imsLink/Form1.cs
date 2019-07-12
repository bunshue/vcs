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
        string camera_serial_old = String.Empty;
        string camera_serial_enw = String.Empty;
        bool flag_auto_scan_mode = true;
        bool flag_read_connection_again = true;
        bool flag_comport_ok = false;

        Stopwatch stopwatch = new Stopwatch();

        int zoom_cnt = 0;
        int zoom_cnt_max = 15;
        int zoom_step = 40;
        int usb_camera_width = 0;
        int usb_camera_height = 0;

        int btn_down_up_cnt = 0;
        int btn_right_left_cnt = 0;

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

            Form1.CheckForIllegalCrossThreadCalls = false;

            g = panel6.CreateGraphics();
            g.Clear(BackColor);

            g2 = panel9.CreateGraphics();
            g2.Clear(BackColor);

            Reset_imsLink_Setting();

            textBox1.Text = trackBar6.Value.ToString();

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
            //tabControl1.SelectedTab = tp_Connection;    //程式啟動時，直接跳到Connection那頁。
            tabControl1.SelectTab(tp_Connection);       //程式啟動時，直接跳到Connection那頁。   the same

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
                        serialPort1.Read(receive_buffer, 0, BytesToRead);
                    }
                    if (Comport_Mode == 0)  //imsLink mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                            SpyMonitorRX();
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
                                        label1.Text += "完成";
                                        richTextBox1.Text += "驗證完成, 序號相同\n";
                                        lb_sn3.Text = "驗證完成, 序號相同  ";
                                        tb_result.Text = "OK";
                                        tb_result.ForeColor = System.Drawing.Color.MediumSpringGreen;
                                        tb_result.BackColor = Color.Green;
                                    }
                                    else
                                    {
                                        richTextBox1.Text += "驗證失敗, 序號不同\n";
                                        lb_sn3.Text = "驗證失敗, 序號不同  ";
                                        tb_result.Text = "FAIL";
                                        tb_result.ForeColor = Color.Black;
                                        tb_result.BackColor = Color.Red;
                                        groupBox10.BackColor = Color.Red;
                                    }
                                    lb_sn2.Text = "";

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
                                lb_time2.Text = "ims時間 : " + ((int)input[0] + 1900).ToString() + "/" + ((int)input[1] + 1).ToString("00") + "/" + ((int)input[2]).ToString("00") + " " + weekday + " " +((int)input[4]).ToString("00") + ":" + ((int)input[5]).ToString("00") + ":" + ((int)input[6]).ToString("00");
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
                        else
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
                    //richTextBox1.AppendText("[RX] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "\n");
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
            Comport_Scan();
            label1.Text = "";
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

            tb_machine_serial.Text = "0000000-B0000";
            tb_mb_big_serial.Text = "0000000000000";
            tb_mb_small_serial.Text = "0000000 0000 000000 0000";

            tb_sn1.Text = "AA0000000";
            tb_sn2.Text = "00000000000";

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
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

            g.Clear(BackColor);

            //設定執行後的表單起始位置
            //this.StartPosition = FormStartPosition.Manual;
            //this.Location = new System.Drawing.Point(100, 100);

            // C# 設定視窗載入位置 
            this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            //C# 軟體啟動、版權宣告視窗 
            Frm_Start frm = new Frm_Start();    //實體化Form2視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示Form2視窗

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

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
                System.Threading.Thread.Sleep(1);
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

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            if (flag_comport_ok == true)
            {
                serialPort1.Write(data, 0, data.Length);
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
            textBox1.Text = trackBar6.Value.ToString();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            int exposure = 0;

            if (textBox1.Text.Length == 0)
                return;

            exposure = int.Parse(textBox1.Text);

            if ((exposure >= 0) && (exposure <= 255))
            {
                trackBar6.Value = exposure;
            }
            else
            {
                richTextBox1.Text += "數字不合法，abort....\n";
                textBox1.Text = trackBar6.Value.ToString();
                return;
            }

        }

        private void button123_Click(object sender, EventArgs e)
        {
            if (comboBox5.SelectedIndex == 0)
            {
                if (flag_comport_ok == false)
                {
                    MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                cnt1 = 0;
                int addr_h = Convert.ToInt32(tb_1.Text, 16);
                int addr_l = Convert.ToInt32(tb_2.Text, 16);
                DongleAddr_h = (byte)addr_h;
                DongleAddr_l = (byte)addr_l;
                DongleData = (byte)int.Parse(tb_4.Text);
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

        private void textBox4_TextChanged(object sender, EventArgs e)
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

        private void button124_Click(object sender, EventArgs e)
        {
            tb_4.Text = "";
            tb_3.Text = "";

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
            }
            else
            {
                richTextBox1.Text += "離開USB WebCam\n";
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
        Font drawFont;
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
            int ww = 64;
            int hh = 64;

            if (flag_awb_debug == true)
            {

                frame_cnt++;
                if (frame_cnt == 3)
                {
                    frame_cnt = 0;

                    //Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                    Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone();

                    int WW = bitmap1.Width;
                    int HH = bitmap1.Height;
                    int i;
                    int j;
                    Color pt;
                    x_st = WW / 2 - ww / 2;
                    y_st = HH / 2 - hh / 2;
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

            int w = bm.Width;
            int h = bm.Height;

            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);

            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * (btn_right_cnt - btn_left_cnt) / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2,
                                             (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4,
                                             w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);

            //寫字的功能
            //畫框的功能
            gg = Graphics.FromImage(bm);

            drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
            drawBrush = new SolidBrush(Color.Yellow);
            drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            x_st = 10;
            y_st = 10;
            gg.DrawString(drawDate, drawFont, drawBrush, x_st, y_st);

            if (flag_awb_debug == true)
            {
                x_st = w / 2 - ww / 2;
                y_st = h / 2 - hh / 2;
                gg.DrawRectangle(new Pen(Color.Red, 1), x_st, y_st, ww, hh);

                string rgb_value;
                x_st = 10;
                y_st = 250;
                drawBrush = new SolidBrush(Color.Red);
                rgb_value = (total_R / (ww * hh)).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);

                y_st = 290;
                drawBrush = new SolidBrush(Color.Green);
                rgb_value = (total_G / (ww * hh)).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);

                y_st = 330;
                drawBrush = new SolidBrush(Color.Blue);
                rgb_value = (total_B / (ww * hh)).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);

                y_st = 370;
                drawBrush = new SolidBrush(Color.Red);
                rgb_value = (total_R).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);

                y_st = 410;
                drawBrush = new SolidBrush(Color.Green);
                rgb_value = (total_G).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);

                y_st = 450;
                drawBrush = new SolidBrush(Color.Blue);
                rgb_value = (total_B).ToString();
                gg.DrawString(rgb_value, drawFont, drawBrush, x_st, y_st);
            }

            pictureBox1.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);

            usb_camera_width = w;
            usb_camera_height = h;

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
                    for (i = 2; i < 9; i++)
                    {
                        if ((tb_wait_camera_data.Text[i] < '0') || (tb_wait_camera_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "SN1格式不正確b\n";
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

                            flag_incorrect_data = false;
                            richTextBox1.Text += "資料正確, 開始燒錄\n";
                            panel9.BackgroundImage = null;
                            g2.Clear(BackColor);
                            button11_Click(sender, e);  //執行燒錄按鍵
                            tb_wait_camera_data.Text = "";
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
            if (flag_wait_receive_data == 1)
                richTextBox1.Text += ".";
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
            lb_sn1.Text = "";
            tb_sn2.Text = "";
            tb_sn1.Text = "";
            tb_sn2.Text = "";
            tb_result.Text = "----";
            tb_result.ForeColor = System.Drawing.Color.MediumSpringGreen;
            tb_result.BackColor = Color.Green;
            groupBox10.BackColor = System.Drawing.SystemColors.ControlLightLight;
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

                //int xPos = pictureBox1.Image.Width - (pictureBox1.Image.Width - 15);
                int xPos = 10;
                int yPos = 10;
                string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

                g.ReleaseHdc();
                g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);

                g.Dispose();

                String file = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_hhmmss");
                String file1 = file + ".jpg";
                String file2 = file + ".bmp";
                String file3 = file + ".png";

                bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(@file2, ImageFormat.Bmp);
                bitmap1.Save(@file3, ImageFormat.Png);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + file2 + "\n";
                richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            else
                richTextBox1.Text += "無圖可存\n";
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

        int flag_fullscreen = 0;
        //Size tab_size = tabcontrol
        private void button19_Click(object sender, EventArgs e)
        {
            if (flag_fullscreen == 0)
            {
                flag_fullscreen = 1;
                button19.BackgroundImage = imsLink.Properties.Resources.normal_screen;
                richTextBox1.Visible = false;
                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.TopMost = true;
                tabControl1.Size = new Size(1600, 1010);
                pictureBox1.Location = new Point(170, 15);
                //pictureBox1.Size = new Size(1120, 840);
                pictureBox1.Size = new Size(640 * 2, 480 * 2);
                toolTip1.SetToolTip(button19, "1X");
            }
            else
            {
                flag_fullscreen = 0;
                button19.BackgroundImage = imsLink.Properties.Resources.full_screen;
                richTextBox1.Visible = true;
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                //this.TopMost = false;
                tabControl1.Size = new Size(948, 616);
                pictureBox1.Location = new Point(170, 50);
                pictureBox1.Size = new Size(640, 480);
                toolTip1.SetToolTip(button19, "2X");
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
            g.Clear(BackColor);
            g.DrawString("燒錄中", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
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
            delay(800);
            lb_write_mb_model.Text = "寫入主機型號完成";
            lb_write_mb_model.ForeColor = Color.Black;
            button29.BackColor = System.Drawing.SystemColors.ControlLight;
            g.Clear(BackColor);
            g.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
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
            tb_sn1.Text = "AA0000000";
            tb_sn2.Text = "00000000000";
            lb_write_camera_serial2.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            g2.Clear(BackColor);
            g2.DrawString("燒錄中", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
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
                //delay(1000);

                lb_write_camera_serial2.Text = "寫入2相機序號完成";
                lb_write_camera_serial2.ForeColor = Color.Black;
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
                g2.Clear(BackColor);
                g2.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }

        }

        private void tb_result_TextChanged(object sender, EventArgs e)
        {

        }


    }
}

