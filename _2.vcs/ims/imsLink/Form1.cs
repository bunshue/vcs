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
        String compile_time = "6/23/2020 01:35下午";
        String software_version = "A04";

        int flag_operation_mode = MODE_RELEASE_STAGE2;  //不允許第四, 第七, 第八

        bool flag_david_test = false;   //david測試第12站時, ims主機要開putty模式

        bool flag_enaglb_awb_function = true;
        bool flag_usb_mode = false;  //for webcam, stage1, stage3
        bool flag_check_webcam_signal = true;

        bool flag_awb_save_data = true; //要寫資料進相機, 預設為true
        bool flag_auto_brightness_awb = false;  //自動亮度測試
        bool flag_enable_awb_timeout = true;   //AWB timeout 功能
        bool flag_wait_cosmo_message = false;
        bool flag_wait_for_confirm = false;

        int total_test_count = 20;
        int current_test_count = 0;

        private const int MODE_RELEASE_STAGE0 = 0x00;   //release mode stage 0, normal use
        private const int MODE_RELEASE_STAGE1A = 0x01;   //release mode stage 1, 4X4 USB camera
        private const int MODE_RELEASE_STAGE1B = 0x0A;   //release mode stage 1, 4X4 USB camera
        private const int MODE_RELEASE_STAGE1C = 0x0B;   //release mode stage 1, check result
        private const int MODE_RELEASE_STAGE2 = 0x02;   //release mode stage 2, AWB mode, writing camera serial
        private const int MODE_RELEASE_STAGE3 = 0x03;   //release mode stage 3, judge class
        private const int MODE_RELEASE_STAGE4 = 0x04;   //release mode stage 4, write camera serial
        private const int MODE_RELEASE_STAGE5 = 0x05;   //release mode stage 5, packaging product
        private const int MODE_RELEASE_STAGE6 = 0x06;   //release mode stage 6, packaging product package6
        private const int MODE_RELEASE_STAGE7 = 0x07;   //release mode stage 7, packaging product package7
        private const int MODE_RELEASE_STAGE8 = 0x08;   //release mode stage 8, packaging product package8
        private const int MODE_RELEASE_STAGE9 = 0x09;   //release mode stage 9, sale data
        private const int MODE_RELEASE_STAGE11 = 0x11;   //release mode stage 11, HiPot check
        private const int MODE_RELEASE_STAGE12 = 0x12;   //release mode stage 12, COSMO check
        private const int MODE_RELEASE_STAGE20 = 0x20;   //release mode stage 20, chicony test
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const bool SHOW_COMPORT_LOG = false;
        private const int UART_BUF_LENGTH = 5;
        private const int CAMERA_OK = 0;	//dongle + camera
        private const int CAMERA_NONE = 1;	//dongle only
        private const int DONGLE_NONE = 2;	//no dongle
        private const int CAMERA_UNKNOWN = 3;	//dongle camera unknown status
        private const int CAMERA_SENSOR_FAIL = 6;	//dongle camera sensor fail
        private const int REASON_AWB_PROCESSING = 7;	//AWB進行中
        private const int REASON_AWB_TIMEOUT = 8;	    //AWB作業延時
        private const int REASON_NO_COMPORT = 9;	//無comport連線
        private const int REASON_NO_IMS_CAMERA = 10;	//無IMS相機
        private const int REASON_FIND_AWB_AREA_FAIL_TOO_SMALL = 11;   //AWB搜尋失敗, 太小
        private const int REASON_FIND_AWB_AREA_FAIL_TOO_FAR = 12;   //AWB搜尋失敗, 太遠
        private const int REASON_MANUALLY_INTERRUPT = 13;   //AWB人為中斷

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
        private const int AWB_PAGE0 = 0x10;	    //awb data, old method
        private const int AWB_PAGE1 = 0x11;	    //awb data, new method
        private const int USER_PAGE1 = 0x12;    //UFM data page 1, WPT, BPT, saturation
        private const int USER_PAGE2 = 0x13;    //UFM data page 2, brightness
        private const int DISPLAY_FHD = 0x00;	//screen size FHD
        private const int DISPLAY_SD = 0x01;	//screen size SD
        private const int AWB_TIMEOUT = 120;	    //AWB timeoout in second

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
        int flag_display_mode = DISPLAY_FHD;
        int flag_read_camera_raw_data = 0;
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
        int flag_camera_use_insighteyes = 0;
        int flag_camera_already_have_serial = 0;
        int flag_stage1c_step = 0;
        int flag_stage3_step = 0;
        int flag_stage_awb = 0;
        int csv_index1 = 0;
        int csv_index2 = 0;
        int csv_index3 = 0;
        int csv_index4 = 0;
        int csv_index5 = 0;
        int csv_index6 = 0;
        int csv_index7 = 0;
        int csv_index8 = 0;
        int csv_index9 = 0;
        int csv_index12 = 0;
        int timer_cnt = 0;
        int g_conn_status = CAMERA_UNKNOWN;
        int[] camera_serial_data = new int[16];
        byte[] sn_data_send2 = new byte[16];
        byte[] rtc_data_send = new byte[7];
        byte[] camera_model_data_send = new byte[16];
        byte[] main_board_model_data_send = new byte[50];
        byte[] awb_data_send = new byte[4];
        string camera_serial_old = String.Empty;
        string camera_serial_enw = String.Empty;
        bool flag_break_doing_awb = false;
        bool flag_doing_awb = false;
        bool flag_auto_scan_mode = true;
        bool flag_read_connection_again = true;
        bool flag_comport_ok = false;
        bool flag_comport_connection_ok = false;
        bool flag_already_write_system_data = false;
        bool flag_fullscreen = false;
        bool flag_network_disk_status = true;

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
        double awb_time = 0;

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
        bool flag_awb_break = false;
        bool flag_awb_timeout = false;
        bool flag_awb_manually_interrupt = false;
        bool flag_update_RGB_scrollbar = true;     //always update value
        bool flag_R_OK = false;
        bool flag_G_OK = false;
        bool flag_B_OK = false;
        bool flag_do_awb = false;
        bool flag_do_find_awb_location = false;
        bool flag_do_find_awb_location_ok = false;
        bool flag_do_find_awb_location_fail = false;
        bool flag_do_find_awb_location_fail_too_small = false;
        bool flag_do_find_awb_location_fail_too_far = false;
        bool flag_doing_writing_data = false;
        bool flag_doing_refreshing_camera = false;
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;
        int timer_display_r_count = 0;
        int timer_display_g_count = 0;
        int timer_display_b_count = 0;
        bool flag_display_r_do_awb = false;
        bool flag_display_g_do_awb = false;
        bool flag_display_b_do_awb = false;
        decimal wpt_value_old = 0;
        byte camera_ybright_sign_bits = 0;
        byte camera_yoffset_sign_bits = 0;
        bool flag_ok_camera_ybright_sign_bit = false;
        bool flag_ok_camera_yoffset_sign_bit = false;
        bool flag_ok_data1 = false;
        bool flag_ok_data2 = false;
        bool flag_ok_data3 = false;
        bool flag_cancel_data = false;
        bool flag_ng_reason1 = false;
        bool flag_ng_reason2 = false;
        bool flag_ng_reason3 = false;
        bool flag_wait_for_ng_reason = false;
        string[] ng_reason = new string[] { "無資料", "鏡頭脫落", "影像有黑影", "Ring上有異物", "Ring未組裝好", "Ring裂痕", "LED脫落", "LED不亮", "LED有異物", "漏光", "其他：" };
        int stage1_ng_reason = 0;
        int ccc = 0;
        int check_cnt_large = 0;
        int check_cnt_small = 0;

        Stopwatch stopwatch = new Stopwatch();

        int zoom_cnt = 0;
        int zoom_cnt_max = 15;
        int zoom_step = 40;
        int usb_camera_width = 0;
        int usb_camera_height = 0;

        int btn_down_up_cnt = 0;
        int btn_right_left_cnt = 0;
        int flag_right_left_cnt = 0;
        int flag_down_up_cnt = 0;
        int flag_right_left_point_cnt = 0;
        int flag_down_up_point_cnt = 0;

        int awb_step = 10;
        int awb_block = 32;     //AWB block size width, height
        int awb_window_size = 200;     //AWB window size width, height
        int awb_auto_step = 5;

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

        private const int CHECK_SATURATION_FRAME = 3;
        bool flag_check_rgb_saturation = false;
        int rgb_saturation_check_cnt = 30000;
        int rgb_r_saturation_cnt = 0;
        int rgb_g_saturation_cnt = 0;
        int rgb_b_saturation_cnt = 0;

        private const int CHECK_AWB_FRAME = 3;
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
        int timer_awb_cnt = 0;
        int awb_cnt = 0;
        int Send_IMS_Data_cnt = 0;
        int awb_time_out = 600;

        string saturation_ratio = "X1.00";
        byte g_TH2 = 0;
        byte g_TH1 = 0;

        double[] brightness_data = new double[11];  //raw brightness data
        double[] brightness_data2 = new double[11]; //ring brightness data

        private const int FOCUS_ON_PICTURE = 0x00;	//timer_webcam focus on picture
        private const int FOCUS_ON_SERIAL = 0x01;	//timer_webcam focus on textbox serial
        int timer_webcam_mode = FOCUS_ON_SERIAL;
        DateTime bootup_time = DateTime.Now;

        //二維List for string
        List<string[]> camera_serials = new List<string[]>();

        //C# 提示視窗 ToolTip 
        //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
        ToolTip toolTip1 = new ToolTip();
        //SetToolTip：定義控制項會跳出提示的文字

        Graphics g;
        Graphics ga;
        Graphics g2;
        Graphics g3;
        Graphics g6;
        Graphics g7;
        Graphics g8;
        Graphics g9;
        Graphics g12;

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
                if (System.IO.File.Exists(imslink_log_filename) == false)
                {
                    //richTextBox1.Text += "檔案: " + imslink_log_filename + " 不存在，製作一個。\n";
                    StreamWriter sw = File.CreateText(imslink_log_filename);
                    sw.Write(log_file_tmp_data);
                    sw.Close();
                }
                else
                {
                    //richTextBox1.Text += "檔案: " + imslink_log_filename + " 存在, 開啟，並接續寫入資料。\n";
                    StreamWriter sw = File.AppendText(imslink_log_filename);
                    sw.Write(log_file_tmp_data);
                    sw.Close();
                }
                log_file_tmp_length = 0;
                log_file_tmp_data = "";
            }
        }

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        public Form1()
        {
            InitializeComponent();

            richTextBox1.Text += "\nimsLink " + software_version + " 啟動, 時間 : " + bootup_time.ToString() + "\n\n";
            richTextBox1.Text += "Compile time : " + compile_time + "\n";

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE0\n";
                flag_enaglb_awb_function = true;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = true;
            }
            else if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE1 A/B\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = true;  //for webcam
                flag_check_webcam_signal = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE1 C\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage1c.Enabled = true;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE2\n";
                flag_enaglb_awb_function = true;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE3\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = true;  //for webcam
                flag_check_webcam_signal = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE5)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE5\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE6)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE6\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage6.Enabled = true;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE9)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE9\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE11)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE11\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE12)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE12\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;
                timer_stage12.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE20)
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE20\t相機測試\n";
                flag_enaglb_awb_function = false;
                flag_usb_mode = false;  //for webcam
                flag_check_webcam_signal = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;
                timer_stage12.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "MODE_RELEASE_STAGE unknown\n";
            }

            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            g = panel6.CreateGraphics();
            g.Clear(BackColor);

            g2 = panel9.CreateGraphics();
            g2.Clear(BackColor);

            g3 = panel4.CreateGraphics();
            g3.Clear(BackColor);

            g6 = panel_package1.CreateGraphics();
            g6.Clear(BackColor);

            g7 = panel_package2.CreateGraphics();
            g7.Clear(BackColor);
            g7.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));

            g8 = panel_package3.CreateGraphics();
            g8.Clear(BackColor);
            g8.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));

            g9 = panel_sale.CreateGraphics();
            g9.Clear(BackColor);
            g9.DrawString("先填單別單號", new Font("標楷體", 43), new SolidBrush(Color.Green), new PointF(1, 30));

            g12 = panel_cosmo.CreateGraphics();
            g12.Clear(BackColor);
            g12.DrawString("輸入相機序號", new Font("標楷體", 43), new SolidBrush(Color.Green), new PointF(1, 30));

            Reset_imsLink_Setting();

            tb_exposure.Text = trackBar6.Value.ToString();

            numericUpDown_expo.Value = trackBar_expo.Value;
            numericUpDown_gain.Value = trackBar_gain.Value;
            numericUpDown_R.Value = trackBar_R.Value;
            numericUpDown_G.Value = trackBar_G.Value;
            numericUpDown_B.Value = trackBar_B.Value;
            if (software_version == "A03")
                comboBox_temperature.SelectedIndex = 29; //7700K modified
            else
                comboBox_temperature.SelectedIndex = 12; //6500K
            numericUpDown_TG_R.Value = TARGET_AWB_R;
            numericUpDown_TG_G.Value = TARGET_AWB_G;
            numericUpDown_TG_B.Value = TARGET_AWB_B;

            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標

            comboBox_saturation.SelectedIndex = 8;
            comboBox_denoise.SelectedIndex = 8;
            comboBox_sharpness.SelectedIndex = 2;

            if (flag_enable_awb_timeout == true)
            {
                if (flag_david_test == true)
                    awb_time_out = 20;
                else
                    awb_time_out = AWB_TIMEOUT;
            }
            else
                awb_time_out = 600;         //a very long time

            /*
            if (comboBox1.Text.Length == 0)
            {
                MessageBox.Show("No comport selected.");
                return;
            }
            serialPort1.PortName = comboBox1.Text;
            serialPort1.BaudRate = int.Parse(comboBox2.Text);

            //serialPort1.Open(); //原本是這一行，改寫成以下。
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
            }
            */
        }

        private void Reset_imsLink_Setting()
        {
            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                this.tp_Camera.Parent = null;   //camera
                this.tp_System.Parent = null;  //主機序號
                this.tp_Camera_Model.Parent = null;   //camera model
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer

                this.tp_Serial_Auto.Text = "第四站";

                if (flag_operation_mode == MODE_RELEASE_STAGE0)
                {
                    this.tp_USB.Text = "色彩校正";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1A)
                {
                    this.tp_USB.Text = "第一站A";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1B)
                {
                    this.tp_USB.Text = "第一站B";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE2)
                {
                    this.tp_USB.Text = "第二站";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    this.tp_USB.Text = "第三站";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE4)
                {
                    this.tp_USB.Text = "第二站";
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE1C) || (flag_operation_mode == MODE_RELEASE_STAGE5) || (flag_operation_mode == MODE_RELEASE_STAGE6) || (flag_operation_mode == MODE_RELEASE_STAGE9) || (flag_operation_mode == MODE_RELEASE_STAGE11) || (flag_operation_mode == MODE_RELEASE_STAGE12) || (flag_operation_mode == MODE_RELEASE_STAGE20))
                {
                    this.tp_USB.Text = "第一站";
                }

                bt_awb_test_init.Enabled = false;
                bt_awb_test2.Enabled = false;
                bt_tmp.Enabled = false;
                bt_erase.Enabled = false;
                bt_awb.Enabled = false;
                bt_disable_timer_webcam.Enabled = false;
                bt_test.Enabled = false;
                comboBox_temperature.Enabled = false;
                bt_script.Enabled = false;
                bt_script_load.Enabled = false;
                bt_script_save.Enabled = false;
                bt_script_cancel.Enabled = false;
                bt_write2.Enabled = false;
                bt_reset_camera.Enabled = false;
                bt_measure_brightness.Enabled = false;

                numericUpDown_TG_R.Enabled = false;
                numericUpDown_TG_G.Enabled = false;
                numericUpDown_TG_B.Enabled = false;

                comboBox_saturation.Enabled = false;
                comboBox_denoise.Enabled = false;
                comboBox_sharpness.Enabled = false;
                bt_save_data.Enabled = false;
                numericUpDown_sharpness.Enabled = false;
                numericUpDown_denoise.Enabled = false;
                numericUpDown_brightness.Enabled = false;
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
            {
                cb_show_grid.Checked = true;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Package1.Parent = null; //產品包裝6
                this.tp_Package2.Parent = null; //產品包裝7
                this.tp_Package3.Parent = null; //產品包裝8
                this.tp_sale.Parent = null;     //出貨紀錄
                this.tp_Camera_Test.Parent = null;  //相機測試
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                tabControl1.SelectTab(tp_USB);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = true;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = true;
                //Comport_Scan();
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
            {
                cb_show_grid.Checked = true;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Package1.Parent = null; //產品包裝6
                this.tp_Package2.Parent = null; //產品包裝7
                this.tp_Package3.Parent = null; //產品包裝8
                this.tp_sale.Parent = null;     //出貨紀錄
                this.tp_Camera_Test.Parent = null;  //相機測試
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                tabControl1.SelectTab(tp_Check);
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Package1.Parent = null; //產品包裝6
                this.tp_Package2.Parent = null; //產品包裝7
                this.tp_Package3.Parent = null; //產品包裝8
                this.tp_sale.Parent = null;     //出貨紀錄
                this.tp_Camera_Test.Parent = null;  //相機測試
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                //tabControl1.SelectedTab = tp_Connection;  //程式啟動時，直接跳到Connection那頁。
                tabControl1.SelectTab(tp_Connection);       //程式啟動時，直接跳到Connection那頁。   the same
                timer_rtc.Enabled = true;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                cb_show_grid.Checked = true;
                cb_air_ng.Checked = false;
                cb_change_rank.Checked = false;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Package1.Parent = null; //產品包裝6
                this.tp_Package2.Parent = null; //產品包裝7
                this.tp_Package3.Parent = null; //產品包裝8
                this.tp_sale.Parent = null;     //出貨紀錄
                this.tp_Camera_Test.Parent = null;  //相機測試
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                tabControl1.SelectTab(tp_USB);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = true;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage3.Enabled = true;
                //Comport_Scan();
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE5)
            {
                cb_show_grid.Checked = true;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                tabControl1.SelectTab(tp_Product);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = true;
                timer_stage1.Enabled = false;
                //Comport_Scan();
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE6)
            {
                cb_show_grid.Checked = true;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                tabControl1.SelectTab(tp_Package1);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
                //Comport_Scan();
            }
            else if ((flag_operation_mode == MODE_RELEASE_STAGE9) || (flag_operation_mode == MODE_RELEASE_STAGE11))
            {
                cb_show_grid.Checked = true;
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                this.tp_Package1.Parent = null;
                this.tp_Package2.Parent = null;
                this.tp_Package3.Parent = null;
                tabControl1.SelectTab(tp_sale);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
                //Comport_Scan();

                if (flag_operation_mode == MODE_RELEASE_STAGE11)
                {
                    tp_sale.Text = "HiPot";
                    checkBox1.Text = "NG";
                    lb_sale3.Text = "相機序號(9~10碼)";
                    label27.Text = "相機序號";
                    gb_ng_reason.Enabled = false;
                }
                else
                    gb_ng_reason.Visible = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE12)
            {
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                this.tp_Package1.Parent = null;
                this.tp_Package2.Parent = null;
                this.tp_Package3.Parent = null;
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_sale.Parent = null;     //出貨紀錄
                this.tp_Camera_Test.Parent = null;  //相機測試
                tabControl1.SelectTab(tp_Cosmo);  //程式啟動時，直接跳到USB那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
                //Comport_Scan();
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE20)
            {
                this.tp_Info.Parent = null;
                this.tp_Connection.Parent = null;
                this.tp_System.Parent = null;
                this.tp_Camera.Parent = null;   //camera
                this.tp_Camera_Model.Parent = null;
                this.tp_Serial_Auto.Parent = null;
                this.tp_Product.Parent = null;  //產品包裝
                this.tp_Test.Parent = null;     //Test
                this.tp_Layer.Parent = null;    //Layer
                this.tp_Package1.Parent = null;
                this.tp_Package2.Parent = null;
                this.tp_Package3.Parent = null;
                this.tp_Check.Parent = null;    //檢查結果
                this.tp_Cosmo.Parent = null;    //COSMO氣密測試
                this.tp_sale.Parent = null;     //出貨紀錄
                tabControl1.SelectTab(tp_Camera_Test);  //程式啟動時，直接跳到相機測試那頁。
                timer_rtc.Enabled = false;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
                //Comport_Scan();
            }
            else
            {
                //tabControl1.SelectedTab = tp_Connection;  //程式啟動時，直接跳到Connection那頁。
                tabControl1.SelectTab(tp_Connection);       //程式啟動時，直接跳到Connection那頁。   the same
                timer_rtc.Enabled = true;
                timer_rgb.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage1.Enabled = false;
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
            richTextBox1.Text += "manually call connect_IMS_comport()\n";
            connect_IMS_comport();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == true)
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button1.Enabled = true;
                button2.Enabled = false;
                flag_comport_ok = false;
                show_main_message1("COM未連線", S_FALSE, 100);
                pictureBox_comport.Image = imsLink.Properties.Resources.x;
                toolTip1.SetToolTip(pictureBox_comport, "COM未連線");
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
            show_main_message1("Reset", S_OK, 30);
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
        string input = "";

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
                                + (year + 100).ToString("0000") + " "
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
                            richTextBox1.Text += "a unknown flag_request_item = " + flag_request_item.ToString() + "\n";
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
                case AWB_PAGE0:
                    richTextBox1.Text += "AWB Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n";
                    break;
                default:
                    richTextBox1.Text += "b unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                    break;

            }

        }

        int timer12_cnt = 0;

        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            if (flag_operation_mode == MODE_RELEASE_STAGE12)
            {
                if (flag_comport_ok == true)
                {
                    if (serialPort1.IsOpen)
                    {
                        timer12_cnt++;

                        //計算serialPort1中有多少位元組 
                        BytesToRead = serialPort1.BytesToRead;

                        if (BytesToRead > 0)
                        {
                            //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                            if (flag_wait_cosmo_message == false)
                            {
                                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                                return;
                            }

                            if (BytesToRead > 141)
                            {
                                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                            }
                            else if (BytesToRead == 141)
                            {
                                richTextBox1.Text += "長度正確, 存檔, t = " + (timer12_cnt / 10).ToString() + "." + (timer12_cnt % 10).ToString() + "\n";
                                //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                                serialPort1.Read(receive_buffer, 0, BytesToRead);

                                input = "";
                                for (int i = 0; i < BytesToRead; i++)
                                    input += (char)receive_buffer[i];

                                richTextBox3.AppendText(input);
                                richTextBox3.ScrollToCaret();		//RichTextBox顯示訊息自動捲動，顯示最後一行

                                flag_ok_data2 = true;
                                check_export_data();
                                if (receive_buffer[7] == '2')
                                {
                                    lb_main_mesg12c.Text = "OK";
                                    lb_main_mesg12c.ForeColor = Color.Green;
                                }
                                else
                                {
                                    lb_main_mesg12c.Text = "NG";
                                    lb_main_mesg12c.ForeColor = Color.Red;
                                }
                            }
                            else if (BytesToRead > 0)
                            {
                                richTextBox1.Text += "累計\n";
                            }
                        }
                    }
                }
                return;
            }

            int data_r;
            int data_b;

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
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
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
                                    tb_info_aa1.Text = "xxxx[S/N] : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
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
                                    richTextBox1.Text += "xxxxxxxxxxxxxxx\n";
                                    flag_doing_writing_data = false;

                                    ////lb_mesg3.Text = stopwatch.ElapsedMilliseconds.ToString() + " msec";

                                }
                            }
                            else if (flag_receive_camera_flash_data == 1)
                            {
                                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                if (flag_read_camera_raw_data == 1)
                                {
                                    flag_read_camera_raw_data = 0;
                                    richTextBox1.AppendText("[Data] : "
                                        + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2") + "-"
                                        + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2") + "-"
                                        + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2") + "-"
                                        + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n");
                                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                                    textBox5.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");

                                    if (flag_request_item == AWB_PAGE1)
                                    {
                                        //    0  1   2  3  4  5  6  7  8  9 10 11 12 13 14 15 
                                        //ex: DA-52-1A-04-52-1B-D2-52-1E-07-52-1F-08-00-00-00
                                        tb_info_g4.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                            + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                            + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                            + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");

                                        data_r = input[3] * 256 + input[6];
                                        data_b = input[9] * 256 + input[12];
                                        richTextBox1.Text += "camera AWB data R : 0x" + data_r.ToString("X2") + "  B : 0x" + data_b.ToString("X2") + "\n";

                                        if ((data_r == 0) && (data_b == 0))
                                        {
                                            lb_awb_data.Text = "無AWB1資料";
                                            lb_awb1.Text = "無AWB1資料";

                                        }
                                        else
                                        {
                                            //lb_awb_data.Text = "R : 0x" + data_r.ToString("X4") + "  B : 0x" + data_b.ToString("X4");
                                            lb_awb_data.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                            lb_awb1.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                        }

                                        richTextBox1.Text += "AWB raw Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                            + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                            + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                            + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n";
                                    }
                                }
                                else
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
                                        case AWB_PAGE0:
                                            tb_info_g.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            data_r = input[0] * 256 + input[1];
                                            data_b = input[2] * 256 + input[3];
                                            richTextBox1.Text += "camera AWB data R : 0x" + data_r.ToString("X2") + "  B : 0x" + data_b.ToString("X2") + "\n";

                                            if ((data_r == 0) && (data_b == 0))
                                            {
                                                //lb_awb_data.Text = "無AWB0資料";
                                                lb_awb0.Text = "無AWB0資料";

                                            }
                                            else
                                            {
                                                //lb_awb_data.Text = "R : 0x" + data_r.ToString("X4") + "  B : 0x" + data_b.ToString("X4");
                                                lb_awb_data.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                                lb_awb0.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                            }

                                            richTextBox1.Text += "AWB raw Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n";
                                            break;
                                        case AWB_PAGE1:
                                            richTextBox1.Text += "xxxxxxxxxxxxxxxxxxxx AWB_PAGE1\n";
                                            tb_info_g.Text = "xxData : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            data_r = input[3] * 256 + input[6];
                                            data_b = input[9] * 256 + input[12];
                                            if ((data_r == 0) && (data_b == 0))
                                            {
                                                //lb_awb_data.Text = "無AWB1資料";
                                                lb_awb1.Text = "無AWB1資料aaaa";

                                            }
                                            else
                                            {
                                                //lb_awb_data.Text = "R : 0x" + data_r.ToString("X4") + "  B : 0x" + data_b.ToString("X4");
                                                lb_awb_data.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                                lb_awb1.Text = "R : " + data_r.ToString() + "   B : " + data_b.ToString();
                                            }

                                            richTextBox1.Text += "dddAWB raw Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n";

                                            break;
                                        default:
                                            richTextBox1.Text += "c unknown flag_request_item = " + flag_request_item.ToString() + "\n";
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
                                try
                                {
                                    string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
                                    string weekday = Day[input[3]].ToString();
                                    lb_time2.Text = "ims時間 : " + ((int)input[0] + 1900).ToString() + "/" + ((int)input[1] + 1).ToString("00") + "/" + ((int)input[2]).ToString("00") + " " + weekday + " " + ((int)input[4]).ToString("00") + ":" + ((int)input[5]).ToString("00") + ":" + ((int)input[6]).ToString("00");
                                    //richTextBox1.Text += ((int)input[6]).ToString("00") + " ";
                                    flag_read_connection_again = true;
                                }
                                catch (Exception ex)
                                {
                                    richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                                }

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

                            if ((int)input[9] == 0xff)  //9B
                            {
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
                            }
                            else    //10B
                            {
                                for (i = 0; i < 10; i++)
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

                                if (input[9] == 0xff)   //9B
                                {
                                    for (i = 0; i < 9; i++)
                                    {
                                        if (tb_sn1.Text[i] != input[i])
                                        {
                                            flag_same_serial = 0;
                                            break;
                                        }
                                    }
                                }
                                else   //10B
                                {
                                    for (i = 0; i < 10; i++)
                                    {
                                        if (tb_sn1.Text[i] != input[i])
                                        {
                                            flag_same_serial = 0;
                                            break;
                                        }
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
                                    playSound(S_OK);

                                    //richTextBox1.Text += "把資料暫存起來\n";
                                    camera_serials.Add(new string[] { tb_sn1.Text, tb_sn2.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });

                                    //if ((camera_serials.Count % 5) == 0)
                                    {
                                        richTextBox1.Text += "自動存檔\n";
                                        flag_operation_mode = MODE_RELEASE_STAGE4;
                                        exportCSV();
                                        flag_operation_mode = MODE_RELEASE_STAGE2;
                                    }
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
                                    timer_stage4.Enabled = false;
                                    playSound(S_FALSE);
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
                                flag_doing_writing_data = false;

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
                            Write_Log_File(input);
                        }
                        else
                        {
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
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
                    /*
                    richTextBox1.AppendText("[checksum fail] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                        + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + ", abort\n");
                    */
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
                    else if ((input[1] == 0xEE) && (input[2] == 0xEE))
                    {
                        if (input[3] == 0x00)
                        {
                            flag_camera_already_have_serial = 0;
                            richTextBox1.Text += "aries says no camera serial.........\n";
                        }
                        else
                        {
                            flag_camera_already_have_serial = 1;
                            richTextBox1.Text += "aries says already have camera serial.........\n";
                        }
                    }
                    else if ((input[1] == 0x11) && (input[2] == 0x52) && (input[3] == 0x00))
                    {
                        //richTextBox1.Text += "get uart response from aries egd system.\n";
                        flag_comport_connection_ok = true;
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
                                else if (input[2] == 0x19)
                                {
                                    lb_yuv_y3.Text = ((int)input[3]).ToString();
                                }
                            }
                            //richTextBox1.Text += "\n";
                        }
                        else if (input[1] == 0x58)
                        {
                            if (input[2] == 0x08)
                            {
                                camera_ybright_sign_bits = (byte)((input[3] >> 3) & 0x01);
                                camera_yoffset_sign_bits = (byte)((input[3] >> 2) & 0x01);
                                flag_ok_camera_ybright_sign_bit = true;
                                flag_ok_camera_yoffset_sign_bit = true;
                            }
                            //richTextBox1.Text += "ADDR : 0x" + ((int)input[1]).ToString("X2") + ((int)input[2]).ToString("X2") + ", value : 0x" + ((int)input[3]).ToString("X2") + "\n";

                            if (input[2] == 0x06)
                                lb_data_camera_gain.Text = "G 0x" + ((int)input[3]).ToString("X2");
                            else if (input[2] == 0x05)
                                lb_data_camera_offset.Text = "O 0x" + ((int)input[3]).ToString("X2");
                            else if (input[2] == 0x07)
                                lb_data_camera_bright.Text = "B 0x" + ((int)input[3]).ToString("X2");
                            else if (input[2] == 0x08)
                                lb_data_camera_sign.Text = "S 0x" + ((int)input[3]).ToString("X2");
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
                            show_main_message1("無連接器", S_OK, 30);
                            textBox7.Text = "無連接器";
                            textBox7.BackColor = Color.Red;
                            playSound(S_FALSE);
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status5.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                        }
                        else if (g_conn_status == CAMERA_NONE)
                        {
                            show_main_message1("無相機", S_OK, 30);
                            textBox7.Text = "有連接器, 無相機";
                            textBox7.BackColor = Color.Red;
                            playSound(S_FALSE);
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel_camera_status5.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                        }
                        else if (g_conn_status == CAMERA_OK)
                        {
                            show_main_message1("有相機", S_OK, 30);
                            textBox7.Text = "有連接器, 有相機";
                            textBox7.BackColor = Color.White;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel_camera_status5.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                        }
                        else if (g_conn_status == CAMERA_SENSOR_FAIL)
                        {
                            show_main_message1("相機失效", S_OK, 30);
                            textBox7.Text = "有連接器, 有相機, 但是相機無法讀寫";
                            textBox7.BackColor = Color.White;
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status5.BackgroundImage = imsLink.Properties.Resources.recorder_sensor_fail;

                            if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                            {
                                tb_awb_mesg.Text = "相機無法讀寫";
                                bt_awb_test.BackColor = Color.Red;
                                flag_doing_awb = false;
                                bt_awb_test.Enabled = false;
                                playSound(S_FALSE);
                            }
                        }
                        else
                        {
                            show_main_message1("相機狀態不明", S_OK, 30);
                            textBox7.Text = "狀態不明a, status = " + g_conn_status.ToString();
                            textBox7.BackColor = Color.Red;
                            playSound(S_FALSE);
                            panel_camera_status1.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel_camera_status5.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
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
            show_main_message1("COM重抓", S_OK, 50);
        }

        private void Comport_Scan()
        {
            comboBox1.Items.Clear();
            comboBox4.Items.Clear();
            comboBox7.Items.Clear();
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox1.Items.Clear();    //Clear All items in Combobox
            comboBox4.Items.Clear();    //Clear All items in Combobox
            comboBox7.Items.Clear();    //Clear All items in Combobox

            richTextBox1.Text += "a共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox1.Items.Add(port);
                comboBox4.Items.Add(port);
                comboBox7.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox1.Text = COM_Ports_NameArr[0];
                comboBox4.Text = COM_Ports_NameArr[0];
                comboBox7.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                comboBox1.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
                comboBox7.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }
        }

        void show_awb_item_visible(bool en)
        {
            lb_0x1.Visible = en;
            lb_0x2.Visible = en;
            lb_addr.Visible = en;
            lb_data.Visible = en;
            tb_1a.Visible = en;
            tb_2a.Visible = en;
            tb_3a.Visible = en;
            tb_4a.Visible = en;
            bt_read2.Visible = en;
            bt_write2.Visible = en;
            bt_reset_camera.Visible = en;
            bt_measure_brightness.Visible = en;

            bt_script.Visible = en;
            bt_script_load.Visible = en;

            bt_awb.Visible = en;
            bt_awb_test.Visible = en;
            progressBar_awb.Visible = en;
            tb_awb_mesg.Visible = en;
            lb_awb_time.Visible = en;
            bt_awb_test2.Visible = en;
            bt_awb_test_init.Visible = en;
            bt_disable_timer_webcam.Visible = en;
            bt_erase.Visible = en;
            bt_read_awb.Visible = en;
            lb_awb_data.Visible = en;
            bt_test.Visible = en;
            bt_clear.Visible = en;
            bt_location.Visible = en;
            bt_brightness.Visible = en;
            bt_tmp.Visible = en;
            pictureBox2.Visible = en;
            cb_auto_search.Visible = en;
            cb_only_search.Visible = en;

            lb_awb_result_expo.Visible = en;
            lb_awb_result_gain.Visible = en;
            lb_awb_result_R.Visible = en;
            lb_awb_result_G.Visible = en;
            lb_awb_result_B.Visible = en;
            bt_get_setup.Visible = en;

            comboBox_temperature.Visible = en;
            //comboBox_webcam.Visible = en;
            numericUpDown_TG_R.Visible = en;
            numericUpDown_TG_G.Visible = en;
            numericUpDown_TG_B.Visible = en;

            b7.Visible = en;
            b6.Visible = en;
            b5.Visible = en;
            b4.Visible = en;
            b3.Visible = en;
            b2.Visible = en;
            b1.Visible = en;
            b0.Visible = en;

            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                //Expo
                lb_expo.Visible = false;
                lb_0x3.Visible = false;
                lb_range_1.Visible = false;
                trackBar_expo.Visible = false;
                tb_expo.Visible = false;
                numericUpDown_expo.Visible = false;
                bt_setup_expo.Visible = false;

                //Gain
                lb_gain.Visible = false;
                lb_0x4.Visible = false;
                lb_range_2.Visible = false;
                trackBar_gain.Visible = false;
                tb_gain.Visible = false;
                numericUpDown_gain.Visible = false;
                bt_setup_gain.Visible = false;

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

                //AE_decrease, Saturation
                bt_ae_decrease.Visible = false;
                bt_saturation.Visible = false;

                //Saturation
                lb_function.Visible = false;
                numericUpDown_saturation.Visible = false;

                comboBox_saturation.Visible = false;
                comboBox_denoise.Visible = false;
                comboBox_sharpness.Visible = false;
                bt_save_data.Visible = false;
                numericUpDown_sharpness.Visible = false;
                numericUpDown_denoise.Visible = false;
                numericUpDown_brightness.Visible = false;

                //hide some buttons
                button32.Visible = false;
                button35.Visible = false;
                button70.Visible = false;
                button88.Visible = false;
                button74.Visible = false;
                button87.Visible = false;
                button9.Visible = false;

                bt_awb_test_init.Visible = false;
                bt_awb_test2.Visible = false;
                bt_tmp.Visible = false;
                bt_awb.Visible = false;
                bt_disable_timer_webcam.Visible = false;
                bt_clear.Visible = false;
                bt_location.Visible = false;
                bt_brightness.Visible = false;
                bt_erase.Visible = false;
                bt_test.Visible = false;

                bt_write2.Visible = false;
                bt_reset_camera.Visible = false;
                bt_measure_brightness.Visible = false;
                bt_script.Visible = false;
                bt_script_load.Visible = false;
                bt_cancel.Visible = false;

                button46.Visible = false;
                button48.Visible = false;

                bt_find_brightness.Visible = false;
                bt_show_brightness.Visible = false;
                cb_show_progress.Visible = false;
                cb_only_search.Visible = false;
                numericUpDown_find_brightness_h.Visible = false;
                numericUpDown_find_brightness_l.Visible = false;
                lb_th_h.Visible = false;
                lb_th_l.Visible = false;
                lb_yuv_y2.Visible = false;
                lb_yuv_y3.Visible = false;
                lb_auto_awb_cnt.Visible = false;

                gb_contrast_brightness.Visible = false;
                gb_contrast_brightness2.Visible = false;
                gb_contrast_brightness3.Visible = false;
                pictureBox_contrast.Visible = false;
                lb_data_camera_gain.Visible = false;
                lb_data_camera_offset.Visible = false;
                lb_data_camera_bright.Visible = false;
                lb_data_camera_sign.Visible = false;
                cb_Contrast_Brightness_Gamma.Visible = false;
                cb_Gamma.Visible = false;

                lb_yuv_y.Visible = false;
                lb_yuv_u.Visible = false;
                lb_yuv_v.Visible = false;
            }
            else
            {
                //Expo
                lb_expo.Visible = en;
                lb_0x3.Visible = en;
                lb_range_1.Visible = en;
                trackBar_expo.Visible = en;
                tb_expo.Visible = en;
                numericUpDown_expo.Visible = en;
                bt_setup_expo.Visible = en;

                //Gain
                lb_gain.Visible = en;
                lb_0x4.Visible = en;
                lb_range_2.Visible = en;
                trackBar_gain.Visible = en;
                tb_gain.Visible = en;
                numericUpDown_gain.Visible = en;
                bt_setup_gain.Visible = en;

                //R
                lb_R.Visible = en;
                lb_0xR.Visible = en;
                lb_range_3.Visible = en;
                trackBar_R.Visible = en;
                tb_R.Visible = en;
                numericUpDown_R.Visible = en;
                bt_setup_R.Visible = en;

                //G
                lb_G.Visible = en;
                lb_0xG.Visible = en;
                lb_range_4.Visible = en;
                trackBar_G.Visible = en;
                tb_G.Visible = en;
                numericUpDown_G.Visible = en;
                bt_setup_G.Visible = en;

                //B
                lb_BB.Visible = en;
                lb_0xB.Visible = en;
                lb_range_5.Visible = en;
                trackBar_B.Visible = en;
                tb_B.Visible = en;
                numericUpDown_B.Visible = en;
                bt_setup_B.Visible = en;

                //WPT
                lb_wpt.Visible = en;
                tb_wpt.Visible = en;
                numericUpDown_wpt.Visible = en;
                bt_read_wpt.Visible = en;
                bt_write_wpt.Visible = en;

                //BPT
                lb_bpt.Visible = en;
                tb_bpt.Visible = en;
                numericUpDown_bpt.Visible = en;
                bt_read_bpt.Visible = en;
                bt_write_bpt.Visible = en;

                //AE_decrease, Saturation
                bt_ae_decrease.Visible = en;
                bt_saturation.Visible = en;

                //Saturation
                lb_function.Visible = en;
                numericUpDown_saturation.Visible = en;

                comboBox_saturation.Visible = en;
                comboBox_denoise.Visible = en;
                comboBox_sharpness.Visible = en;
                bt_save_data.Visible = en;
                numericUpDown_sharpness.Enabled = en;
                numericUpDown_denoise.Enabled = en;
                numericUpDown_brightness.Enabled = en;

                lb_yuv_y2.Visible = en;
                lb_yuv_y3.Visible = en;
                lb_auto_awb_cnt.Visible = false;

                bt_tmp.Text = total_test_count.ToString() + "次";

                gb_contrast_brightness.Visible = true;
                gb_contrast_brightness2.Visible = true;
                gb_contrast_brightness3.Visible = true;
                pictureBox_contrast.Visible = true;
                lb_data_camera_gain.Visible = true;
                lb_data_camera_offset.Visible = true;
                lb_data_camera_bright.Visible = true;
                lb_data_camera_sign.Visible = true;
                cb_Contrast_Brightness_Gamma.Visible = true;
                cb_Gamma.Visible = true;
            }

            //note
            lb_note1.Visible = en;
            lb_note2.Visible = en;
            lb_note3.Visible = en;

            bt_save_img.Visible = false;
            bt_clear_serial.Visible = false;

            bt_awb_break.Visible = false;

            return;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            if (flag_display_mode == DISPLAY_SD)
            {
                dx = 10;
                button72.Location = new Point(button72.Location.X - dx, button72.Location.Y);
                dx = 15;
                button22.Location = new Point(button22.Location.X - dx, button22.Location.Y);
                dx = 20;
                button73.Location = new Point(button73.Location.X - dx, button73.Location.Y);

                dx = 80;
                button74.Location = new Point(button74.Location.X - dx, button74.Location.Y);
                button88.Location = new Point(button88.Location.X - dx, button88.Location.Y);
                button70.Location = new Point(button70.Location.X - dx, button70.Location.Y);
                button87.Location = new Point(button87.Location.X - dx, button87.Location.Y);
                button34.Location = new Point(button34.Location.X - dx, button34.Location.Y);
                dx = 85;
                button7.Location = new Point(button7.Location.X - dx, button7.Location.Y);
                bt_min.Location = new Point(button7.Location.X + 100, button7.Location.Y);
                bt_save_program_picture.Location = new Point(button7.Location.X + 100 + 65, button7.Location.Y);
                bt_read_camera_register.Location = new Point(button7.Location.X + 100 + 65+65, button7.Location.Y);
                bt_restore_camera_setup.Location = new Point(button7.Location.X + 100 + 65+65+65, button7.Location.Y);
            }
            else
            {
                bt_min.Location = new Point(button7.Location.X + 55, button7.Location.Y - 10);
                bt_save_program_picture.Location = new Point(button7.Location.X + 55 + 65, button7.Location.Y - 10);
                bt_read_camera_register.Location = new Point(button7.Location.X + 55 + 65 + 65, button7.Location.Y - 10);
                bt_restore_camera_setup.Location = new Point(button7.Location.X + 55 + 65+65+65, button7.Location.Y - 10);
            }

            x_st = 20;
            y_st = 30;
            dx = 0;
            dy = 60;

            textBox10.Location = new Point(x_st + dx, y_st + dy * 0);
            textBox4.Location = new Point(x_st + dx, y_st + dy * 1);
            textBox2.Location = new Point(x_st + dx, y_st + dy * 2);
            textBox8.Location = new Point(x_st + dx, y_st + dy * 3);
            textBox12.Location = new Point(x_st + dx, y_st + dy * 4);
            textBox14.Location = new Point(x_st + dx, y_st + dy * 5);
            textBox16.Location = new Point(x_st + dx, y_st + dy * 6);
            textBox9.Location = new Point(x_st + dx, y_st + dy * 7);
            textBox11.Location = new Point(x_st + dx, y_st + dy * 7 + 35);

            dx = 60;
            tb_info_82.Location = new Point(x_st + dx, y_st + dy * 0);
            textBox3.Location = new Point(x_st + dx, y_st + dy * 1);
            tb_info_a2.Location = new Point(x_st + dx, y_st + dy * 2);
            tb_info_b2.Location = new Point(x_st + dx, y_st + dy * 3);
            tb_info_d2.Location = new Point(x_st + dx, y_st + dy * 4);
            tb_info_e2.Location = new Point(x_st + dx, y_st + dy * 5);
            tb_info_f2.Location = new Point(x_st + dx, y_st + dy * 6);
            tb_info_g2.Location = new Point(x_st + dx, y_st + dy * 7);
            tb_info_g3.Location = new Point(x_st + dx, y_st + dy * 7 + 35);

            dx = 180;
            tb_info_8.Location = new Point(x_st + dx, y_st + dy * 0);
            tb_info_aa1.Location = new Point(x_st + dx, y_st + dy * 1);
            tb_info_aa2.Location = new Point(x_st + dx, y_st + dy * 2);
            tb_info_b.Location = new Point(x_st + dx, y_st + dy * 3);
            tb_info_d.Location = new Point(x_st + dx, y_st + dy * 4);
            tb_info_e.Location = new Point(x_st + dx, y_st + dy * 5);
            tb_info_f.Location = new Point(x_st + dx, y_st + dy * 6);
            tb_info_g.Location =  new Point(x_st + dx, y_st + dy * 7);
            tb_info_g4.Location = new Point(x_st + dx, y_st + dy * 7 + 35);

            dx = 180;
            lb_a.Location = new Point(x_st + dx, y_st + dy * 2 + 35);
            lb_b.Location = new Point(x_st + dx, y_st + dy * 3 + 35);
            lb_d.Location = new Point(x_st + dx, y_st + dy * 4 + 35);
            lb_e.Location = new Point(x_st + dx, y_st + dy * 5 + 35);
            lb_f.Location = new Point(x_st + dx, y_st + dy * 6 + 35);
            lb_awb0.Location = new Point(x_st + dx, y_st + dy * 8 + 10);
            lb_awb1.Location = new Point(x_st + dx + 300, y_st + dy * 8 + 10);

            x_st = 20;
            y_st = 130;
            dx = 40;
            data_00.Location = new Point(x_st + dx * 0, y_st);
            data_01.Location = new Point(x_st + dx * 1, y_st);
            data_02.Location = new Point(x_st + dx * 2, y_st);
            data_03.Location = new Point(x_st + dx * 3, y_st);
            data_04.Location = new Point(x_st + dx * 4, y_st);
            data_05.Location = new Point(x_st + dx * 5, y_st);
            data_06.Location = new Point(x_st + dx * 6, y_st);
            data_07.Location = new Point(x_st + dx * 7, y_st);
            data_08.Location = new Point(x_st + dx * 8, y_st);
            data_09.Location = new Point(x_st + dx * 9, y_st);
            data_10.Location = new Point(x_st + dx * 10, y_st);
            data_11.Location = new Point(x_st + dx * 11, y_st);
            data_12.Location = new Point(x_st + dx * 12, y_st);
            data_13.Location = new Point(x_st + dx * 13, y_st);
            data_14.Location = new Point(x_st + dx * 14, y_st);
            data_15.Location = new Point(x_st + dx * 15, y_st);

            y_st = 50;
            textBox5.Location = new Point(x_st + dx * 0, y_st);
            textBox5.Size = new Size(dx * 15 + data_00.Width, textBox5.Size.Height);

            //AWB
            bt_awb_test.Location = new Point(170 + 70 * 0 - 30, 460 + 40 * 0 - 200);
            bt_awb_test.Size = new Size(200, 97);
            bt_awb_test.BackColor = Color.Lime;
            progressBar_awb.Location = new Point(170 + 70 * 0 - 30, 460 + 40 * 0 - 200 + 100);
            //lb_awb_time.Location = new Point(170 + 70 * 0 + 330, 460 + 40 * 0 - 200 + 100 + 4);
            lb_awb_time.Location = new Point(170 + 70 * 0 + 10, 460 + 40 * 0 - 200 + 100 + 4);

            tb_awb_mesg.Location = new Point(170 + 70 * 0 - 30 + 205, 460 + 40 * 0 - 200 + 15);
            tb_awb_mesg.Size = new Size(250, 150);

            bt_awb_break.Location = new Point(170 + 70 * 0 - 30 + 205, 460 + 40 * 0 - 200 + 24 + 40);

            cb_auto_search.Location = new Point(500, 330);
            cb_auto_search.Checked = true;

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
                cb_auto_search.Enabled = true;
            else
                cb_auto_search.Enabled = false;

            cb_only_search.Location = new Point(530, 465);
            cb_only_search.Checked = false;

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
                groupBox_brightness.Enabled = true;
            else
                groupBox_brightness.Enabled = false;

            //button
            x_st = 140;
            y_st = 415;
            dx = 65;
            dy = 40;

            //第零排button
            bt_read_awb.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_erase.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            lb_awb_data.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 4);
            bt_get_setup.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            //第一排button
            bt_awb_test_init.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            //bt_awb_test.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_awb_test2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_tmp.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_awb.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            bt_disable_timer_webcam.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            //第二排button
            bt_test.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            bt_clear.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            bt_location.Location = new Point(x_st + dx * 6, y_st + dy * 2);

            y_st = 510;
            bt_brightness.Location = new Point(x_st + dx * 6, y_st + 30);
            //bt_brightness.Location = new Point(x_st + dx * 6, y_st + 30);

            //讀寫相機暫存器
            x_st = 140;
            y_st = 520;
            dx = 170;

            lb_addr.Location = new Point(30, y_st + 5);
            lb_0x1.Location = new Point(5, y_st + 3 + 30);
            tb_1a.Location = new Point(30, y_st + 30);
            tb_2a.Location = new Point(100, y_st + 30);

            lb_data.Location = new Point(30 + dx, y_st + 5);
            lb_0x2.Location = new Point(5 + dx, y_st + 3 + 30);
            tb_3a.Location = new Point(30 + dx, y_st + 30);
            tb_4a.Location = new Point(100 + dx, y_st + 30);

            y_st = 521;
            int dxx = 16;
            b7.Location = new Point(30 + dx + dxx * 0, y_st + 30 + 35);
            b6.Location = new Point(30 + dx + dxx * 1, y_st + 30 + 35);
            b5.Location = new Point(30 + dx + dxx * 2, y_st + 30 + 35);
            b4.Location = new Point(30 + dx + dxx * 3, y_st + 30 + 35);
            b3.Location = new Point(30 + dx + dxx * 4 + 5, y_st + 30 + 35);
            b2.Location = new Point(30 + dx + dxx * 5 + 5, y_st + 30 + 35);
            b1.Location = new Point(30 + dx + dxx * 6 + 5, y_st + 30 + 35);
            b0.Location = new Point(30 + dx + dxx * 7 + 5, y_st + 30 + 35);

            x_st = 140;
            y_st = 510;
            dx = 65;

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
            {
                bt_read2.Location = new Point(x_st + dx * 3, y_st + 30);
            }
            else
            {
                bt_read2.Location = new Point(x_st + dx * 3, y_st + 40);
            }

            bt_write2.Location = new Point(x_st + dx * 4, y_st + 30);
            bt_script.Location = new Point(x_st + dx * 5, y_st + 30);

            bt_cancel.Location = new Point(x_st + dx * 5, y_st + 30 + 32);       //at the same place
            bt_script_load.Location = new Point(x_st + dx * 5, y_st + 30 + 32);  //at the same place

            bt_reset_camera.Location = new Point(x_st + dx * 3, y_st + 30 + 32);
            bt_measure_brightness.Location = new Point(x_st + dx * 4, y_st + 30 + 32);

            //EXPO GAIN R G B
            x_st = 140;
            y_st = 390;
            dx = 80;
            lb_awb_result_expo.Location = new Point(x_st + dx * 0, y_st);
            lb_awb_result_gain.Location = new Point(x_st + dx * 1, y_st);
            lb_awb_result_R.Location = new Point(x_st + dx * 2, y_st);
            lb_awb_result_G.Location = new Point(x_st + dx * 3 + 20, y_st);
            lb_awb_result_B.Location = new Point(x_st + dx * 4 + 40, y_st);

            lb_awb_result_expo.ForeColor = Color.Silver;
            lb_awb_result_gain.ForeColor = Color.Gold;
            lb_awb_result_R.ForeColor = Color.Red;
            lb_awb_result_G.ForeColor = Color.Green;
            lb_awb_result_B.ForeColor = Color.Blue;

            if (flag_display_mode == DISPLAY_SD)
            {
                //EXPO
                lb_expo.Size = new Size(lb_expo.Size.Width * 3 / 5, lb_expo.Height * 3 / 5);
                lb_expo.Font = new Font("新細明體", lb_expo.Font.Size * 3 / 5);
                lb_0x3.Size = new Size(lb_0x3.Size.Width * 3 / 5, lb_0x3.Height * 3 / 5);
                lb_0x3.Font = new Font("新細明體", lb_0x3.Font.Size * 3 / 5);
                lb_range_1.Size = new Size(lb_range_1.Size.Width * 3 / 5, lb_range_1.Height * 3 / 5);
                lb_range_1.Font = new Font("新細明體", lb_range_1.Font.Size * 3 / 5);

                trackBar_expo.Size = new Size(trackBar_expo.Size.Width * 3 / 5, trackBar_expo.Height * 3 / 5);
                numericUpDown_expo.Size = new Size(numericUpDown_expo.Size.Width * 4 / 5, numericUpDown_expo.Height * 4 / 5);
                numericUpDown_expo.Font = new Font("Arial", numericUpDown_expo.Font.Size * 3 / 5);
                tb_expo.Size = new Size(tb_expo.Size.Width * 3 / 5, tb_expo.Height * 3 / 5);
                tb_expo.Font = new Font("Arial", tb_expo.Font.Size * 3 / 5);

                x_st = 550;
                y_st = 540;
                dx = 0;
                dy = 0;

                trackBar_expo.Location = new Point(x_st + dx, y_st + dy);
                lb_expo.Location = new Point(x_st + dx + 5, y_st + dy + 25);
                lb_0x3.Location = new Point(x_st + dx + 200 + 2, y_st + dy + 10);
                lb_0x3.Text = "0x                   =";
                numericUpDown_expo.Location = new Point(x_st + dx + 220, y_st + dy + 5);
                tb_expo.Location = new Point(x_st + dx + 280, y_st + dy + 5);
                bt_setup_expo.Location = new Point(x_st + dx + 320, y_st + dy + 0);
                lb_range_1.Location = new Point(x_st + dx + 220 + 6, y_st + dy + 5 + 25);
                lb_range_1.Text = "0~1FF           0~511";

                //GAIN
                lb_gain.Size = new Size(lb_gain.Size.Width * 3 / 5, lb_gain.Height * 3 / 5);
                lb_gain.Font = new Font("新細明體", lb_gain.Font.Size * 3 / 5);
                lb_0x4.Size = new Size(lb_0x4.Size.Width * 3 / 5, lb_0x4.Height * 3 / 5);
                lb_0x4.Font = new Font("新細明體", lb_0x4.Font.Size * 3 / 5);
                lb_range_2.Size = new Size(lb_range_2.Size.Width * 3 / 5, lb_range_2.Height * 3 / 5);
                lb_range_2.Font = new Font("新細明體", lb_range_2.Font.Size * 3 / 5);

                trackBar_gain.Size = new Size(trackBar_gain.Size.Width * 3 / 5, trackBar_gain.Height * 3 / 5);
                numericUpDown_gain.Size = new Size(numericUpDown_gain.Size.Width * 4 / 5, numericUpDown_gain.Height * 4 / 5);
                numericUpDown_gain.Font = new Font("Arial", numericUpDown_gain.Font.Size * 3 / 5);
                tb_gain.Size = new Size(tb_gain.Size.Width * 3 / 5, tb_gain.Height * 3 / 5);
                tb_gain.Font = new Font("Arial", tb_gain.Font.Size * 3 / 5);

                x_st = 550;
                y_st = 600;
                dx = 0;
                dy = 0;

                trackBar_gain.Location = new Point(x_st + dx, y_st + dy);
                lb_gain.Location = new Point(x_st + dx + 5, y_st + dy + 25);
                lb_0x4.Location = new Point(x_st + dx + 200 + 2, y_st + dy + 10);
                lb_0x4.Text = "0x                   =";
                numericUpDown_gain.Location = new Point(x_st + dx + 220, y_st + dy + 5);
                tb_gain.Location = new Point(x_st + dx + 280, y_st + dy + 5);
                bt_setup_gain.Location = new Point(x_st + dx + 320, y_st + dy + 0);
                lb_range_2.Location = new Point(x_st + dx + 220 + 6, y_st + dy + 5 + 25);
                lb_range_2.Text = "0~1FF           0~511";

                //R
                lb_R.Size = new Size(lb_R.Size.Width * 3 / 5, lb_R.Height * 3 / 5);
                lb_R.Font = new Font("新細明體", lb_R.Font.Size * 3 / 5);
                lb_0xR.Size = new Size(lb_0xR.Size.Width * 3 / 5, lb_0xR.Height * 3 / 5);
                lb_0xR.Font = new Font("新細明體", lb_0xR.Font.Size * 3 / 5);
                lb_range_3.Size = new Size(lb_range_3.Size.Width * 3 / 5, lb_range_3.Height * 3 / 5);
                lb_range_3.Font = new Font("新細明體", lb_range_3.Font.Size * 3 / 5);

                trackBar_R.Size = new Size(trackBar_R.Size.Width * 3 / 5, trackBar_R.Height * 3 / 5);
                numericUpDown_R.Size = new Size(numericUpDown_R.Size.Width * 4 / 5, numericUpDown_R.Height * 4 / 5);
                numericUpDown_R.Font = new Font("Arial", numericUpDown_R.Font.Size * 3 / 5);
                tb_R.Size = new Size(tb_R.Size.Width * 3 / 5, tb_R.Height * 3 / 5);
                tb_R.Font = new Font("Arial", tb_R.Font.Size * 3 / 5);

                x_st = 580 + 370;
                y_st = 540 - 2;
                dx = 0;
                dy = 0;

                trackBar_R.Location = new Point(x_st + dx, y_st + dy);
                lb_R.Location = new Point(x_st + dx + 5, y_st + dy + 25);
                lb_0xR.Location = new Point(x_st + dx + 200 + 2, y_st + dy + 10);
                lb_0xR.Text = "0x                   =";
                numericUpDown_R.Location = new Point(x_st + dx + 220, y_st + dy + 5);
                tb_R.Location = new Point(x_st + dx + 280, y_st + dy + 5);
                bt_setup_R.Location = new Point(x_st + dx + 320, y_st + dy + 0);
                lb_range_3.Location = new Point(x_st + dx + 220 + 6, y_st + dy + 5 + 25);
                lb_range_3.Text = "0~FFF          0~4095";

                //G
                lb_G.Size = new Size(lb_G.Size.Width * 3 / 5, lb_G.Height * 3 / 5);
                lb_G.Font = new Font("新細明體", lb_G.Font.Size * 3 / 5);
                lb_0xG.Size = new Size(lb_0xG.Size.Width * 3 / 5, lb_0xG.Height * 3 / 5);
                lb_0xG.Font = new Font("新細明體", lb_0xG.Font.Size * 3 / 5);
                lb_range_4.Size = new Size(lb_range_4.Size.Width * 3 / 5, lb_range_4.Height * 3 / 5);
                lb_range_4.Font = new Font("新細明體", lb_range_4.Font.Size * 3 / 5);

                trackBar_G.Size = new Size(trackBar_G.Size.Width * 3 / 5, trackBar_G.Height * 3 / 5);
                numericUpDown_G.Size = new Size(numericUpDown_G.Size.Width * 4 / 5, numericUpDown_G.Height * 4 / 5);
                numericUpDown_G.Font = new Font("Arial", numericUpDown_G.Font.Size * 3 / 5);
                tb_G.Size = new Size(tb_G.Size.Width * 3 / 5, tb_G.Height * 3 / 5);
                tb_G.Font = new Font("Arial", tb_G.Font.Size * 3 / 5);

                x_st = 580 + 370;
                y_st = 540 + 40 - 3;
                dx = 0;
                dy = 0;

                trackBar_G.Location = new Point(x_st + dx, y_st + dy);
                lb_G.Location = new Point(x_st + dx + 5, y_st + dy + 25);
                lb_0xG.Location = new Point(x_st + dx + 200 + 2, y_st + dy + 10);
                lb_0xG.Text = "0x                   =";
                numericUpDown_G.Location = new Point(x_st + dx + 220, y_st + dy + 5);
                tb_G.Location = new Point(x_st + dx + 280, y_st + dy + 5);
                bt_setup_G.Location = new Point(x_st + dx + 320, y_st + dy + 0);
                lb_range_4.Location = new Point(x_st + dx + 220 + 6, y_st + dy + 5 + 25);
                lb_range_4.Text = "0~FFF          0~4095";

                //B
                lb_BB.Size = new Size(lb_BB.Size.Width * 3 / 5, lb_BB.Height * 3 / 5);
                lb_BB.Font = new Font("新細明體", lb_BB.Font.Size * 3 / 5);
                lb_0xB.Size = new Size(lb_0xB.Size.Width * 3 / 5, lb_0xB.Height * 3 / 5);
                lb_0xB.Font = new Font("新細明體", lb_0xB.Font.Size * 3 / 5);
                lb_range_5.Size = new Size(lb_range_5.Size.Width * 3 / 5, lb_range_5.Height * 3 / 5);
                lb_range_5.Font = new Font("新細明體", lb_range_5.Font.Size * 3 / 5);

                trackBar_B.Size = new Size(trackBar_B.Size.Width * 3 / 5, trackBar_B.Height * 3 / 5);
                numericUpDown_B.Size = new Size(numericUpDown_B.Size.Width * 4 / 5, numericUpDown_B.Height * 4 / 5);
                numericUpDown_B.Font = new Font("Arial", numericUpDown_B.Font.Size * 3 / 5);
                tb_B.Size = new Size(tb_B.Size.Width * 3 / 5, tb_B.Height * 3 / 5);
                tb_B.Font = new Font("Arial", tb_B.Font.Size * 3 / 5);

                x_st = 580 + 370;
                y_st = 540 + 40 + 40- 5;
                dx = 0;
                dy = 0;

                trackBar_B.Location = new Point(x_st + dx, y_st + dy);
                lb_BB.Location = new Point(x_st + dx + 5, y_st + dy + 25);
                lb_0xB.Location = new Point(x_st + dx + 200 + 2, y_st + dy + 10);
                lb_0xB.Text = "0x                   =";
                numericUpDown_B.Location = new Point(x_st + dx + 220, y_st + dy + 5);
                tb_B.Location = new Point(x_st + dx + 280, y_st + dy + 5);
                bt_setup_B.Location = new Point(x_st + dx + 320, y_st + dy + 0);
                lb_range_5.Location = new Point(x_st + dx + 220 + 6, y_st + dy + 5 + 25);
                lb_range_5.Text = "0~FFF          0~4095";

                //note
                lb_note1.Font = new Font("標楷體", lb_note1.Font.Size * 5 / 6);
                lb_note2.Font = new Font("標楷體", lb_note2.Font.Size * 5 / 6);
                lb_note3.Font = new Font("標楷體", lb_note3.Font.Size * 5 / 6);

                if (flag_operation_mode != MODE_RELEASE_STAGE0)
                {
                    lb_sn_opal.Text = "序號";
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X - 12, cb_enable_awb.Location.Y + 56 + 65 + 2);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X + 50 - 4, cb_enable_awb.Location.Y + 56 + 65);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170 + 60 + 3, cb_enable_awb.Location.Y + 56 + 65);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170 + 3, cb_enable_awb.Location.Y + 56 + 65);
                    tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 70);
                }
                else
                {
                    lb_sn_opal.Text = "序號";
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X - 12, cb_enable_awb.Location.Y + 56 + 65 + 2);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X + 50 - 4, cb_enable_awb.Location.Y + 56 + 65);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170 + 60 + 3, cb_enable_awb.Location.Y + 56 + 65);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170 + 3, cb_enable_awb.Location.Y + 56 + 65);
                }

                lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 10);
                lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 10);
                lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 10);
            }
            else
            {
                //EXPO
                lb_expo.Location = new Point(30 / 2, 720 - 120 + 45);
                lb_0x3.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 3 - 130 + 45);
                lb_range_1.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 3 - 130 + 30 + 45);
                lb_range_1.Text = "0~1FF           0~511";
                trackBar_expo.Location = new Point(30 / 2, 750 - 130 + 45);
                numericUpDown_expo.Location = new Point(410 + 45, 750 - 130 + 45);
                tb_expo.Location = new Point(410 + 45 - 80, 750 - 130 + 45);
                bt_setup_expo.Location = new Point(480 + 45, 750 - 130 + 45);

                //GAIN
                lb_gain.Location = new Point(30 / 2, 720 + 100 - 50 - 90 + 50 - 15);
                lb_0x4.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 - 90 + 50 - 15);
                lb_range_2.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 - 90 + 30 + 50 - 15);
                lb_range_2.Text = "0~1FF           0~511";
                trackBar_gain.Location = new Point(30 / 2, 750 + 100 - 50 - 10 - 90 + 50 - 15);
                numericUpDown_gain.Location = new Point(410 + 45, 750 + 100 - 50 - 10 - 90 + 50 - 15);
                tb_gain.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 - 90 + 50 - 15);
                bt_setup_gain.Location = new Point(480 + 45, 750 + 100 - 50 - 10 - 90 + 50 - 15);

                //R
                lb_R.Location = new Point(0, 750 + 100 - 50 + 50 - 30 - 15);
                lb_0xR.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 - 30 - 15);
                lb_range_3.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50 - 15);
                lb_range_3.Text = "0~FFF          0~4095";
                trackBar_R.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 - 30 - 15);
                numericUpDown_R.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 - 30 - 15);
                tb_R.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 - 30 - 15);
                bt_setup_R.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 - 30 - 15);

                //G
                lb_G.Location = new Point(0, 750 + 100 - 50 + 50 * 2 - 20 - 15);
                lb_0xG.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 * 2 - 20 - 15);
                lb_range_4.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50 * 2 - 40 + 30 + 20 - 15);
                lb_range_4.Text = "0~FFF          0~4095";
                trackBar_G.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 * 2 - 20 - 15);
                numericUpDown_G.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 * 2 - 20 - 15);
                tb_G.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 * 2 - 20 - 15);
                bt_setup_G.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 * 2 - 20 - 15);

                //B
                lb_BB.Location = new Point(0, 750 + 100 - 50 + 50 * 3 - 10 - 15);
                lb_0xB.Location = new Point(410 + 35 - 50 - 50 + 5, 750 + 100 + 3 - 50 - 10 + 50 * 3 - 10 - 15);
                lb_range_5.Location = new Point(410 + 35 - 50 - 50 + 5 + 30, 750 + 100 + 3 - 50 - 10 + 50 * 3 - 20 + 30 + 10 - 15);
                lb_range_5.Text = "0~FFF          0~4095";
                trackBar_B.Location = new Point(30 / 2, 750 + 100 - 50 - 10 + 50 * 3 - 10 - 15);
                numericUpDown_B.Location = new Point(410 + 45, 750 + 100 - 50 - 10 + 50 * 3 - 10 - 15);
                tb_B.Location = new Point(410 + 45 - 80, 750 + 100 - 50 - 10 + 50 * 3 - 10 - 15);
                bt_setup_B.Location = new Point(480 + 45, 750 + 100 - 50 - 10 + 50 * 3 - 10 - 15);

                if (flag_operation_mode != MODE_RELEASE_STAGE0)
                {
                    dy = 100;
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X, cb_enable_awb.Location.Y + 28 + dy);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X, cb_enable_awb.Location.Y + 56 + dy);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170, cb_enable_awb.Location.Y + 56 - 20 + dy);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170, cb_enable_awb.Location.Y + 56 + 20 + dy);
                    tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 70);
                }
                else
                {
                    x_st = 1500;
                    y_st = 930;
                    lb_sn_opal.Location = new Point(x_st + 10, y_st + 5);
                    tb_sn_opal.Location = new Point(x_st + 120, y_st);
                    bt_save_img.Location = new Point(x_st + 250, y_st);
                    bt_clear_serial.Location = new Point(x_st + 315, y_st);
                }

                lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 18);
                lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 18);
                lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 18);

                lb_yuv_y.Location = new Point(5, 489 + 65 + 47 + 4);
                lb_yuv_u.Location = new Point(5 + 50, 489 + 65 + 47 + 4);
                lb_yuv_v.Location = new Point(5 + 100, 489 + 65 + 47 + 4);

                lb_yuv_y2.Location = new Point(1610, 740);
                lb_yuv_y3.Location = new Point(1215, 105);

                lb_auto_awb_cnt.Location = new Point(bt_awb_break.Location.X + 110, bt_awb_break.Location.Y + 5);
            }

            //TARGET RGB
            if (flag_display_mode == DISPLAY_SD)
            {
                comboBox_temperature.Size = new Size(comboBox_temperature.Size.Width * 3 / 4, comboBox_temperature.Height * 2 / 3);
                comboBox_temperature.Font = new Font("Arial", comboBox_temperature.Font.Size * 3 / 5);
                numericUpDown_TG_R.Size = new Size(numericUpDown_TG_R.Size.Width * 3 / 5, numericUpDown_TG_R.Height * 3 / 5);
                numericUpDown_TG_R.Font = new Font("Arial", numericUpDown_TG_R.Font.Size * 3 / 5);
                numericUpDown_TG_G.Size = new Size(numericUpDown_TG_G.Size.Width * 3 / 5, numericUpDown_TG_G.Height * 3 / 5);
                numericUpDown_TG_G.Font = new Font("Arial", numericUpDown_TG_G.Font.Size * 3 / 5);
                numericUpDown_TG_B.Size = new Size(numericUpDown_TG_B.Size.Width * 3 / 5, numericUpDown_TG_B.Height * 3 / 5);
                numericUpDown_TG_B.Font = new Font("Arial", numericUpDown_TG_B.Font.Size * 3 / 5);

                comboBox_temperature.Location = new Point(170 + 400 + 30 + 120 + 70, 15 + 230 * 11 / 10 + 115);
                numericUpDown_TG_R.Location = new Point(170 + 400 + 30 + 120 + 70, 15 + 250 * 11 / 10 + 120);
                numericUpDown_TG_G.Location = new Point(170 + 400 + 30 + 120 + 70, 15 + 290 * 11 / 10 + 120);
                numericUpDown_TG_B.Location = new Point(170 + 400 + 30 + 120 + 70, 15 + 330 * 11 / 10 + 120);
            }
            else
            {
                comboBox_temperature.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 230 * 2 + 120 * 2 - 10);
                numericUpDown_TG_R.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 250 * 2 + 120 * 2 - 10);
                numericUpDown_TG_G.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 290 * 2 + 120 * 2 - 10);
                numericUpDown_TG_B.Location = new Point(170 + 400 + 30 + 120 + 215, 15 + 330 * 2 + 120 * 2 - 10);
            }

            //WPT BPT AE_Target Saturation
            if (flag_display_mode == DISPLAY_SD)
            {
                x_st = 900;
                y_st = 460;
                dx = 100;
                dy = 550;
                //WPT
                lb_wpt.Location = new Point(x_st + 2, y_st + 2);
                tb_wpt.Location = new Point(x_st + 70, y_st);
                numericUpDown_wpt.Location = new Point(x_st + 140, y_st);
                bt_read_wpt.Location = new Point(x_st + 210, y_st);
                bt_write_wpt.Location = new Point(x_st + 280, y_st);

                y_st = 460 + 40;
                //BPT
                lb_bpt.Location = new Point(x_st + 2, y_st + 2);
                tb_bpt.Location = new Point(x_st + 70, y_st);
                numericUpDown_bpt.Location = new Point(x_st + 140, y_st);
                bt_read_bpt.Location = new Point(x_st + 210, y_st);
                bt_write_bpt.Location = new Point(x_st + 280, y_st);

                //AE Target
                bt_ae_decrease.Location = new Point(bt_read_wpt.Location.X, bt_read_wpt.Location.Y - 40);

                //Saturation
                bt_saturation.Location = new Point(bt_write_wpt.Location.X, bt_write_wpt.Location.Y - 40);


                //comboBox_saturation.Location
                //comboBox_denoise.Location
                //comboBox_sharpness.Location
                //bt_save_data.Location
                //numericUpDown_sharpness.Location
                //numericUpDown_denoise.Location
                //numericUpDown_brightness.Location
                //bt_find_brightness2.Location
                //bt_show_brightness.Location
                //cb_show_progress.Location
                //cb_only_search.Location
                //numericUpDown_find_brightness.Location

            }
            else
            {
                dx = 20;
                //WPT
                lb_wpt.Location = new Point(410 + 5 + 400 + 20 + 200 + dx, 750 + 100 - 50 - 10 + 50 * 2 - 15 + 20);
                tb_wpt.Location = new Point(410 + 45 + 25 + 400 + 20 + 200 + dx, 750 + 100 - 50 - 10 + 50 * 2 - 20 + 20);
                numericUpDown_wpt.Location = new Point(410 + 45 + 25 + 80 + 400 + 20 + 200 + dx, 750 + 100 - 50 - 10 + 50 * 2 - 20 + 20);
                bt_read_wpt.Location = new Point(410 + 45 + 25 + 80 + 80 + 400 + 20 + 200 + dx, 750 + 100 - 50 - 10 + 50 * 2 - 20 + 20);
                bt_write_wpt.Location = new Point(410 + 45 + 25 + 80 + 150 + 400 + 20 + 200 + dx, 750 + 100 - 50 - 10 + 50 * 2 - 20 + 20);

                //BPT
                lb_bpt.Location = new Point(410 + 5 + 400 + 20 + 200 + dx, lb_wpt.Location.Y + 40);
                tb_bpt.Location = new Point(410 + 45 + 25 + 400 + 20 + 200 + dx, tb_wpt.Location.Y + 40);
                numericUpDown_bpt.Location = new Point(410 + 45 + 25 + 80 + 400 + 20 + 200 + dx, numericUpDown_wpt.Location.Y + 40);
                bt_read_bpt.Location = new Point(410 + 45 + 25 + 80 + 80 + 400 + 20 + 200 + dx, bt_read_wpt.Location.Y + 40);
                bt_write_bpt.Location = new Point(410 + 45 + 25 + 80 + 150 + 400 + 20 + 200 + dx, bt_write_wpt.Location.Y + 40);

                //AE Target
                bt_ae_decrease.Location = new Point(numericUpDown_wpt.Location.X, numericUpDown_wpt.Location.Y - 40);

                //Saturation
                bt_saturation.Location = new Point(bt_write_wpt.Location.X + 100, bt_write_wpt.Location.Y - 40);
                numericUpDown_saturation.Location = new Point(bt_saturation.Location.X + 70, bt_saturation.Location.Y);
                lb_function.Location = new Point(bt_saturation.Location.X + 70, bt_saturation.Location.Y - 20);
                comboBox_saturation.Location = new Point(numericUpDown_saturation.Location.X + 70, numericUpDown_saturation.Location.Y);
                comboBox_denoise.Location = new Point(comboBox_saturation.Location.X + 85, comboBox_saturation.Location.Y);
                comboBox_sharpness.Location = new Point(comboBox_saturation.Location.X + 140, comboBox_saturation.Location.Y);
                bt_save_data.Location = new Point(comboBox_saturation.Location.X + 210, comboBox_saturation.Location.Y + 60);
                numericUpDown_denoise.Location = new Point(comboBox_denoise.Location.X, comboBox_denoise.Location.Y + 40);
                numericUpDown_sharpness.Location = new Point(comboBox_sharpness.Location.X, comboBox_sharpness.Location.Y + 40);
                numericUpDown_brightness.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y);

                bt_find_brightness.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 250);
                bt_show_brightness.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 200);
                cb_show_progress.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 150);
                numericUpDown_find_brightness_h.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 110);
                numericUpDown_find_brightness_l.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 70);

                lb_th_h.Location = new Point(numericUpDown_find_brightness_h.Location.X - 42, numericUpDown_find_brightness_h.Location.Y + 7);
                lb_th_l.Location = new Point(numericUpDown_find_brightness_l.Location.X - 42, numericUpDown_find_brightness_l.Location.Y + 7);

                groupBox_brightness.Location = new Point(bt_find_brightness.Location.X + 25, bt_find_brightness.Location.Y - 30);


            }

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
            {
                gb_contrast_brightness.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - gb_contrast_brightness.Width - 5, pictureBox1.Location.Y + 30);
                gb_contrast_brightness2.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - gb_contrast_brightness.Width - 5, pictureBox1.Location.Y + 30 + 115);
                //gb_contrast_brightness3.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - gb_contrast_brightness.Width - 5, pictureBox1.Location.Y + 30 + 115 + 115);
                gb_contrast_brightness3.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y);

                pictureBox_contrast.Location = new Point(pictureBox1.Location.X + 50, pictureBox1.Location.Y + 100);
                if(cb_Gamma.Checked == true)
                    pictureBox_contrast.Size = new Size(300, 256);
                else
                    pictureBox_contrast.Size = new Size(280, 256);
                lb_data_camera_gain.Location = new Point(1090, 40);
                lb_data_camera_offset.Location = new Point(1090, 40 + 40);
                lb_data_camera_bright.Location = new Point(1090, 40 + 80);
                lb_data_camera_sign.Location = new Point(1090, 40 + 120);

                cb_Contrast_Brightness_Gamma.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - 800, pictureBox1.Location.Y + 6);
                cb_Gamma.Location = new Point(cb_Contrast_Brightness_Gamma.Location.X + 230, cb_Contrast_Brightness_Gamma.Location.Y);
            }


            if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                bt_restore_camera_setup.Visible = false;
                /*
                //debug code
                bt_find_brightness.Visible = true;
                bt_show_brightness.Visible = true;
                cb_show_progress.Visible = true;
                cb_only_search.Visible = true;
                numericUpDown_find_brightness_h.Visible = true;
                numericUpDown_find_brightness_l.Visible = true;

                lb_th_h.Visible = true;
                lb_th_l.Visible = true;

                bt_find_brightness.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 250);
                bt_show_brightness.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 200);
                cb_show_progress.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 150);
                numericUpDown_find_brightness_h.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 110);
                numericUpDown_find_brightness_l.Location = new Point(comboBox_sharpness.Location.X + 55, comboBox_sharpness.Location.Y - 70);

                lb_th_h.Location = new Point(numericUpDown_find_brightness_h.Location.X - 42, numericUpDown_find_brightness_h.Location.Y + 7);
                lb_th_l.Location = new Point(numericUpDown_find_brightness_l.Location.X - 42, numericUpDown_find_brightness_l.Location.Y + 7);

                lb_yuv_y2.Visible = true;
                lb_auto_awb_cnt.Visible = false;
                */
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
            {
                button13.Visible = true;
                button47.Visible = true;
                button41.Visible = true;
                groupBox5.Visible = true;
                cb_enable_awb.Visible = true;
                bt_LED.Visible = true;
                groupBox_brightness.Visible = true;
            }
            else
            {
                button13.Visible = false;
                button47.Visible = false;
                button41.Visible = false;
                groupBox5.Visible = false;
                cb_enable_awb.Visible = false;
                bt_LED.Visible = false;
                groupBox_brightness.Visible = false;
            }

            if (flag_operation_mode <= MODE_RELEASE_STAGE3)
            {
                button49.Visible = true;
            }
            else
            {
                button49.Visible = false;
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B) || (flag_operation_mode == MODE_RELEASE_STAGE3))
            {
                button19.Location = new Point(button19.Location.X - 35, button19.Location.Y);
                groupBox_gridlinecolor.Location = new Point(cb_show_grid.Location.X + 110, cb_show_grid.Location.Y - 20-20);
            }
            else
                groupBox_gridlinecolor.Visible = false;

            if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
            {
                cb_stage1_ng.Text = "NG";
                cb_stage1_ng.Visible = false;

                checkBox2.Visible = false;

                gb_ng_reason1.Visible = false;

                if (flag_display_mode == DISPLAY_SD)
                {
                    //SD
                    cb_stage1_ng.Location = new Point(tb_wait_sn_data.Location.X + 90, tb_wait_sn_data.Location.Y + 14 - 455);
                    gb_ng_reason1.Location = new Point(tb_wait_sn_data.Location.X + 85, tb_wait_sn_data.Location.Y - 410);
                }
                else
                {
                    //FULLHD
                    cb_stage1_ng.Location = new Point(tb_wait_sn_data.Location.X + 180, tb_wait_sn_data.Location.Y + 14);
                    gb_ng_reason1.Location = new Point(tb_wait_sn_data.Location.X + 120, tb_wait_sn_data.Location.Y + 90);
                }
                lb_ng_reason.Text = "";
            }
            else
            {
                cb_stage1_ng.Visible = false;
                gb_ng_reason1.Visible = false;
            }

            if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                tb_wait_sn_data.Visible = true;
                lb_class.Visible = true;
                cb_air_ng.Visible = true;
                cb_change_rank.Visible = true;
            }
            else
            {
                tb_wait_sn_data.Visible = false;
                lb_class.Visible = false;
                cb_air_ng.Visible = false;
                cb_change_rank.Visible = false;
            }
            richTextBox2.Visible = false;

            refresh_picturebox2();
            return;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (Screen.PrimaryScreen.Bounds.Width < 1920)
            {
                flag_display_mode = DISPLAY_SD;
            }
            else
            {
                flag_display_mode = DISPLAY_FHD;
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE4) || (flag_operation_mode > MODE_RELEASE_STAGE20))
            {
                MessageBox.Show("不能使用此模式, mode = " + flag_operation_mode.ToString() + ", 離開", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE0) && (flag_display_mode == DISPLAY_SD))
            {
                MessageBox.Show("不能在SD螢幕使用模式0, 離開", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            if (flag_enaglb_awb_function == true)
            {
                cb_enable_awb.Checked = true;
            }
            else
            {
                cb_enable_awb.Checked = false;
            }

            this.Text = "imsLink " + software_version;

            pictureBox1.Size = new Size(640, 480);
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
            lb_a.Text = "";
            lb_b.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            lb_awb0.Text = "";
            lb_awb1.Text = "";
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
            lb_data_camera_gain.Text = "";
            lb_data_camera_offset.Text = "";
            lb_data_camera_bright.Text = "";
            lb_data_camera_sign.Text = "";
            lb_gain_value.Text = "1 X";
            tb_machine_serial.Text = "0000000-B0000";
            tb_mb_big_serial.Text = "0000000000000";
            tb_mb_small_serial.Text = "0000000 0000 000000 0000";
            tb_awb_mesg.Text = "";
            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
            lb_main_mesg3.Text = "";
            lb_main_mesg5.Text = "";
            lb_main_mesg6.Text = "";
            lb_main_mesg7.Text = "";
            lb_main_mesg8.Text = "";
            lb_main_mesg9.Text = "";
            lb_main_mesg12a.Text = "";
            lb_main_mesg12b.Text = "";
            lb_main_mesg12c.Text = "";
            lb_awb_data.Text = "";
            lb_awb_time.Text = "";
            lb_class.Text = "";
            bt_script_save.Visible = false;
            bt_script_cancel.Visible = false;
            tb_wpt.Text = Convert.ToString((Int32)numericUpDown_wpt.Value, 16).ToUpper();
            tb_bpt.Text = Convert.ToString((Int32)numericUpDown_bpt.Value, 16).ToUpper();
            wpt_value_old = numericUpDown_wpt.Value;

            //numericUpDown_gain3.Value = trackBar_Contrast3.Value;
            //numericUpDown_offset3.Value = trackBar_Y_Offset3.Value;
            //numericUpDown_brightness3.Value = trackBar_Brightness3.Value;
            numericUpDown_wpt3.Value = trackBar_WPT.Value;
            numericUpDown_bpt3.Value = trackBar_BPT.Value;
            trackBar_WPT.Minimum = trackBar_BPT.Value + 1;
            trackBar_BPT.Maximum = trackBar_WPT.Value - 1;

            tb_gain3.Text = ((int)numericUpDown_gain3.Value).ToString("X2");
            tb_offset3.Text = ((int)numericUpDown_offset3.Value).ToString("X2");
            tb_brightness3.Text = ((int)numericUpDown_brightness3.Value).ToString("X2");
            tb_wpt3.Text = ((int)numericUpDown_wpt3.Value).ToString("X2");
            tb_bpt3.Text = ((int)numericUpDown_bpt3.Value).ToString("X2");

            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                tb_sn1.Text = "AA0000000";
                tb_sn2.Text = "00000000000";
            }
            else
            {
                tb_sn1.Text = "AA1234567";
                tb_sn2.Text = "12345678901";
            }
            tb_sn1.Text = "";
            tb_sn2.Text = "";

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

            camera_serials.Clear();

            //Comport_Scan();
            this.BackColor = Color.Yellow;

            //connect_IMS_comport();

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
            pictureBox_comport.SizeMode = PictureBoxSizeMode.Zoom;

            if (flag_enaglb_awb_function == true)
                bt_goto_awb.Visible = true;
            else
                bt_goto_awb.Visible = false;

            show_awb_item_visible(false);   //111
            g.Clear(BackColor);

            //設定執行後的表單起始位置
            //this.StartPosition = FormStartPosition.Manual;
            //this.Location = new System.Drawing.Point(100, 100);

            // C# 設定視窗載入位置 
            this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            //if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                //C# 軟體啟動、版權宣告視窗 
                Frm_Start frm = new Frm_Start();    //實體化Form2視窗物件
                frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                frm.ShowDialog();   //顯示Form2視窗
            }

            toolTip1.SetToolTip(button17, "Zoom in");
            toolTip1.SetToolTip(button18, "Zoom out");
            toolTip1.SetToolTip(button12, "Refresh");
            toolTip1.SetToolTip(button16, "影像存檔");
            toolTip1.SetToolTip(button15, "Play/Pause");

            if (flag_display_mode == DISPLAY_SD)
            {
                toolTip1.SetToolTip(button19, "1.25X");
            }
            else
            {
                toolTip1.SetToolTip(button19, "2X");
            }

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

            if (flag_enaglb_awb_function == true)
            {
                richTextBox1.Text += "call bt_goto_awb_Click 111\n";
                bt_goto_awb_Click(sender, e);
            }
            if (cb_show_grid.Checked == false)
            {
                rb_3X3.Visible = false;
                rb_4X4.Visible = false;
                rb_5X5.Visible = false;
                rb_NXN.Visible = false;
                groupBox_gridlinecolor.Visible = false;
            }

            show_item_location();

            if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                bt_awb_test.Enabled = false;
                bt_awb_test.BackColor = Color.Pink;
            }

            if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2) 
                || (flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B) || (flag_operation_mode == MODE_RELEASE_STAGE3))
            {
                richTextBox1.Text += "call check_webcam() 111\n";
                check_webcam();
            }

            bt_script_save.Visible = false;
            bt_script_cancel.Visible = false;
            bt_cancel.Visible = false;

            if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B) || (flag_operation_mode == MODE_RELEASE_STAGE3))
            {
                button19_Click(sender, e);
            }

            if ((flag_operation_mode <= MODE_RELEASE_STAGE3) || (flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
            {
                //檢查存圖片的資料夾
                string Path = Application.StartupPath + "\\picture";
                if (Directory.Exists(Path) == false)     //確認資料夾是否存在
                {
                    Directory.CreateDirectory(Path);
                    richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
                }
                else
                    richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            }

            if (flag_operation_mode == MODE_RELEASE_STAGE12)
            {
                Comport_Scan();

                //auto connect to comport
                button82_Click(sender, e);
            }

            if (flag_operation_mode == MODE_RELEASE_STAGE20)
            {
                if (flag_comport_connection_ok == false)
                {
                    richTextBox1.Text += "MODE_RELEASE_STAGE20 call connect_IMS_comport()\n";
                    connect_IMS_comport();
                }

                if (serialPort1.IsOpen)
                {
                    button89.Enabled = false;
                    button90.Enabled = true;
                    this.BackColor = System.Drawing.SystemColors.ControlLight;
                    flag_comport_ok = true;
                }
                button84.Visible = false;
                button85.Visible = false;
                button47.Visible = false;
                button41.Visible = false;
            }

            if ((flag_operation_mode != MODE_RELEASE_STAGE20) && (check_network_disk() == S_OK))
            {
                show_main_message1("已連上網路磁碟機", S_OK, 30);
                show_main_message2("已連上網路磁碟機", S_OK, 30);
                show_main_message3("已連上網路磁碟機", S_OK, 30);
                tb_awb_mesg.BackColor = Color.White;
                tb_awb_mesg.Text = "";
            }

            //make sure comport is connected
            if (flag_enaglb_awb_function == true)
            {
                if (flag_comport_connection_ok == false)
                {
                    show_main_message1("重新連線COM Port", S_OK, 30);
                    show_main_message2("重新連線COM Port", S_OK, 30);
                    show_main_message3("重新連線COM Port", S_OK, 30);
                    richTextBox1.Text += "no comport, call connect_IMS_comport() again\n";
                    delay(30);
                    connect_IMS_comport();
                    if (flag_comport_connection_ok == true)
                    {
                        show_main_message1("重新連線COM Port, OK", S_OK, 30);
                        show_main_message2("重新連線COM Port, OK", S_OK, 30);
                        show_main_message3("重新連線COM Port, OK", S_OK, 30);
                    }
                }
            }

            cb_Contrast_Brightness_Gamma.Checked = false;

            richTextBox1.Text += "\nimsLink " + software_version + " 啟動完成, 時間 : " + DateTime.Now.ToString() + "\n\n";
            return;
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

            string[] Day = new string[] { "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" };
            string weekday = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            //richTextBox1.Text += weekday + "\n";
            lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");

            if (flag_network_disk_status == false)
            {
                if ((DateTime.Now.Second % 5) == 0)
                {
                    if (check_network_disk() == S_OK)
                    {
                        show_main_message1("已連上網路磁碟機", S_OK, 30);
                        show_main_message2("已連上網路磁碟機", S_OK, 30);
                        show_main_message3("已連上網路磁碟機", S_OK, 30);
                        tb_awb_mesg.BackColor = Color.White;
                        tb_awb_mesg.Text = "";
                    }
                }
            }
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
            //在退出程序前彈出確認退出程序的對話框
            if (e.CloseReason != CloseReason.WindowsShutDown)
            {
                if (flag_doing_refreshing_camera == true)
                {
                    richTextBox1.Text += "正在影像重抓, 忽略alt-f4\n";
                    e.Cancel = true;
                }
            }

            /*
            if (Cam != null)
            {
                if (Cam.IsRunning == true)  // When Form1 closes itself, WebCam must stop, too.
                {
                    flag_camera_start = 0;
                    Cam.Stop();   // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
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
            save_log_to_local_drive();
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
            byte cnt1 = 1;
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
            byte cnt1 = 0;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
        }

        public bool Send_IMS_Data0(byte cc, byte xx, byte yy, byte zz)  //directly send data
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //serialPort1.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息ims2 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
            return true;
        }

        public bool Send_IMS_Data(byte cc, byte xx, byte yy, byte zz)
        {
            Send_IMS_Data_cnt++;
            //serialPort1.DiscardInBuffer();    //can not use this

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
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    richTextBox1.Text += "xxx錯誤訊息ims1 : " + ex.Message + "\n";
                }
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

        private void button119_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 2;
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
            byte cnt1 = 3;
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
            byte cnt1 = 0;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 * 4 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button127_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 1;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 * 4 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);

        }

        private void button126_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 2;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 * 4 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button125_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 3;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 * 4 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button129_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 0;
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

            show_hex2bit(value);
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
            panel_camera_status5.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn2.Clear();
            tb_sn1.BackColor = Color.Gray;
            tb_info_aa1.Clear();
            tb_info_aa2.Clear();
            lb_sn1.Text = "相機序號1 讀取中...";
            lb_sn2.Text = "相機序號2 讀取中...";
            lb_sn3.Text = "";
            lb_write_camera_serial2.Text = "";
            lb_a.Text = "";

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
                tb_sn1.Text = "狀態不明b, status = " + g_conn_status.ToString();
            }
            button8.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button28_Click(object sender, EventArgs e)
        {
            flag_read_camera_raw_data = 1;
            textBox5.Clear();
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int page = Convert.ToInt32(textBox6.Text, 16);
            Send_IMS_Data(0xD1, (byte)page, 0, 0);
            return;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_system_info();     //顯示系統資訊
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
            tb_info_g.Clear();
            tb_info_g4.Clear();
            lb_camera_model.Text = "";
            lb_a.Text = "";
            lb_b.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            lb_sn1.Text = "相機序號1 讀取中...";
            lb_sn2.Text = "相機序號2 讀取中...";
            lb_sn3.Text = "";
            lb_awb0.Text = "";
            lb_awb1.Text = "";
            tb_info_a2.BackColor = Color.White;
            tb_info_b2.BackColor = Color.White;
            tb_info_82.BackColor = Color.White;
            tb_info_d2.BackColor = Color.White;
            tb_info_e2.BackColor = Color.White;
            tb_info_f2.BackColor = Color.White;
            tb_info_g2.BackColor = Color.White;
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;
            panel_camera_status5.BackgroundImage = null;
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

                //old method get awb data
                lb_awb_data.Text = "";
                cnt = 0;

                richTextBox1.Text += "\n\nread AWB_PAGE0\n";
                page = AWB_PAGE0;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox1.Text += "a";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                //new method get awb data
                flag_read_camera_raw_data = 1;
                richTextBox1.Text += "\n\nread AWB_PAGE1\n";
                page = AWB_PAGE1;
                Send_IMS_Data(0xD1, (byte)page, 0, 0);
            }
            else
            {
                tb_sn1.Text = "狀態不明c, status = " + g_conn_status.ToString();
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
                richTextBox1.Text += "進入USB WebCam頁\t";

                if (flag_operation_mode == MODE_RELEASE_STAGE0)
                {
                    richTextBox1.Text += "第零站\n";
                    timer_stage1.Enabled = false;
                    timer_stage2.Enabled = true;
                    timer_stage3.Enabled = false;
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
                {
                    richTextBox1.Text += "第一站 A/B\n";
                    timer_stage1.Enabled = true;
                    timer_stage2.Enabled = false;
                    timer_stage3.Enabled = false;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE2)
                {
                    richTextBox1.Text += "第二站\n";
                    timer_stage1.Enabled = false;
                    timer_stage2.Enabled = true;
                    timer_stage3.Enabled = false;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    richTextBox1.Text += "第三站\n";
                    timer_stage1.Enabled = false;
                    timer_stage2.Enabled = false;
                    timer_stage3.Enabled = true;
                }
                else
                {
                    richTextBox1.Text += "第XXX站\n";
                    timer_stage1.Enabled = false;
                    timer_stage2.Enabled = false;
                    timer_stage3.Enabled = false;
                }
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                timer_rgb.Enabled = true;
            }
            else if (tabControl1.SelectedTab == tp_Serial_Auto)
            {
                richTextBox1.Text += "進入相機序號頁\n";
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = true;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;

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

                    if (flag_display_mode == DISPLAY_SD)
                    {
                        toolTip1.SetToolTip(button19, "1.25X");
                    }
                    else
                    {
                        toolTip1.SetToolTip(button19, "2X");
                    }

                    show_awb_item_visible(false);   //222
                }
            }
            else if (tabControl1.SelectedTab == tp_Product)
            {
                richTextBox1.Text += "進入產品包裝頁, 第5站\n";
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = true;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                flag_operation_mode = MODE_RELEASE_STAGE5;
                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_product1.Clear();
                tb_product2.Clear();
                tb_product3.Clear();

                flag_auto_scan_mode = true;
                button54.Text = "到修改模式";
            }
            else if (tabControl1.SelectedTab == tp_Package1)
            {
                richTextBox1.Text += "進入主機 六\n";
                flag_operation_mode = MODE_RELEASE_STAGE6;
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = true;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_package11.Clear();
                tb_package12.Clear();
                tb_package13.Clear();

                flag_auto_scan_mode = true;
                button55.Text = "到修改模式";
            }
            else if (tabControl1.SelectedTab == tp_Package2)
            {
                richTextBox1.Text += "進入Dongle 七\n";
                flag_operation_mode = MODE_RELEASE_STAGE7;
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = true;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_package21.Clear();
                tb_package22.Clear();

                flag_auto_scan_mode = true;
                button58.Text = "到修改模式";

                g7.Clear(BackColor);
                g7.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));
            }
            else if (tabControl1.SelectedTab == tp_Package3)
            {
                richTextBox1.Text += "進入主機包裝 八\n";
                flag_operation_mode = MODE_RELEASE_STAGE8;
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = true;
                timer_stage9.Enabled = false;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_package31.Clear();
                tb_package32.Clear();
                tb_package33.Clear();

                flag_auto_scan_mode = true;
                button61.Text = "到修改模式";

                g8.Clear(BackColor);
                g8.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));
            }
            else if (tabControl1.SelectedTab == tp_sale)
            {
                if(flag_operation_mode == MODE_RELEASE_STAGE9)
                    richTextBox1.Text += "進入出貨記錄\n";
                else
                    richTextBox1.Text += "進入HiPot\n";
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = true;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_sale1.Clear();
                tb_sale2.Clear();
                tb_sale3.Clear();

                tb_sale1.BackColor = Color.Pink;
                tb_sale2.BackColor = Color.Pink;
                tb_sale3.BackColor = Color.White;

                flag_auto_scan_mode = true;
                button64.Text = "到修改模式";

                g9.Clear(BackColor);
                g9.DrawString("先填單別單號", new Font("標楷體", 43), new SolidBrush(Color.Green), new PointF(1, 30));
            }
            else if (tabControl1.SelectedTab == tp_Check)
            {
                richTextBox1.Text += "進入檢查結果 一C\n";
                flag_operation_mode = MODE_RELEASE_STAGE1C;
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;
                timer_stage1c.Enabled = true;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;
                tb_package11.Clear();
                tb_package12.Clear();
                tb_package13.Clear();

                //flag_auto_scan_mode = true;
                //button55.Text = "到修改模式";
            }
            else if (tabControl1.SelectedTab == tp_About)
            {
                richTextBox1.Text += "進入About頁\n";
                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

                flag_ok_data1 = false;
                flag_ok_data2 = false;
                flag_ok_data3 = false;

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

                    if (flag_display_mode == DISPLAY_SD)
                    {
                        toolTip1.SetToolTip(button19, "1.25X");
                    }
                    else
                    {
                        toolTip1.SetToolTip(button19, "2X");
                    }

                    show_awb_item_visible(false);   //222
                }
            }
            else
            {
                //richTextBox1.Text += "離開USB WebCam 其他分頁.......\n";
                if (tabControl1.SelectedTab == tp_Camera)
                {
                    richTextBox1.Text += "進入Camera頁\n";
                }
                else if (tabControl1.SelectedTab == tp_Info)
                {
                    richTextBox1.Text += "進入相機資料頁\n";
                }
                else if (tabControl1.SelectedTab == tp_Connection)
                {
                    richTextBox1.Text += "進入連線頁\n";
                }
                else if (tabControl1.SelectedTab == tp_System)
                {
                    richTextBox1.Text += "進入主機序號頁\n";
                }
                else if (tabControl1.SelectedTab == tp_Camera_Model)
                {
                    richTextBox1.Text += "進入相機型號頁\n";
                }
                else if (tabControl1.SelectedTab == tp_Test)
                {
                    richTextBox1.Text += "進入Test頁\n";
                }
                else if (tabControl1.SelectedTab == tp_Layer)
                {
                    richTextBox1.Text += "進入Layer頁\n";
                }
                else
                {
                    richTextBox1.Text += "進入????頁\n";
                }

                timer_rgb.Enabled = false;
                timer_stage1.Enabled = false;
                timer_stage2.Enabled = false;
                timer_stage3.Enabled = false;
                timer_stage4.Enabled = false;
                timer_stage5.Enabled = false;
                timer_stage6.Enabled = false;
                timer_stage7.Enabled = false;
                timer_stage8.Enabled = false;
                timer_stage9.Enabled = false;

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

                    if (flag_display_mode == DISPLAY_SD)
                    {
                        toolTip1.SetToolTip(button19, "1.25X");
                    }
                    else
                    {
                        toolTip1.SetToolTip(button19, "2X");
                    }

                    show_awb_item_visible(false);   //222
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
                    if (Cam.IsRunning == true)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        flag_camera_start = 0;
                        Cam.Stop();   // WebCam stops capturing images.
                        //Cam.SignalToStop();
                        //Cam.WaitForStop();
                        Cam = null;
                    }
                }
                */
                if(this.tb_sn2.Focused == false)
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

        int step = 1;
        int add_amount = 1;
        int add_tmp = 0;
        int frame_cnt = 0;
        int frame_cnt_old = 0;
        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        bool flag_capture_picture = false;
        int[] y_data_r = new int[8];
        int[] y_data_g = new int[8];
        int[] y_data_b = new int[8];
        int[] y_data_y = new int[8];
        int[] y_data_y_old = new int[] { 0, 29, 80, 105, 149, 178, 225, 255 };
        int[] g_data_new = new int[] { 0x00, 0x2C, 0x2F, 0x3A, 0x4E, 0x5F, 0x6C, 0x76, 0x7F, 0x87, 0x8F, 0x99, 0xA4, 0xB3, 0xC5, 0xD7 };
        int[] g_data_old = new int[] { 0x00, 0x2C, 0x2F, 0x3A, 0x4E, 0x5F, 0x6C, 0x76, 0x7F, 0x87, 0x8F, 0x99, 0xA4, 0xB3, 0xC5, 0xD7 };

        public Bitmap bm_contrast = null;
        Graphics gc;    //for contrast

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            if (flag_do_find_awb_location == true)
                return;

            if (flag_capture_picture == true)
            {
                richTextBox1.Text += "xxx Cam_NewFrame! ";
                return;
            }

            flag_capture_picture = true;

            int x_st = 0;
            int y_st = 0;
            int dy = 40;
            int ww = awb_block;
            int hh = awb_block;

            if (g_conn_status != CAMERA_OK)
            {
                //richTextBox1.Text += "QQQ ";
            }

            if ((flag_enaglb_awb_function == true) || (flag_check_webcam_signal == true))
            {
                frame_cnt++;
                if ((frame_cnt % 5) == 0)
                {
                    //frame_cnt = 0;

                    //Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                    Bitmap bitmap1 = (Bitmap)eventArgs.Frame.Clone();
                    //bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipX);

                    int WW = bitmap1.Width;
                    int HH = bitmap1.Height;
                    int i;
                    int j;
                    Color pt;
                    x_st = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                    if (x_st < 0)
                        x_st = 0;
                    if ((x_st + ww) > WW)
                        x_st = WW - ww;

                    y_st = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
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

                    total_RGB_R = total_R;
                    total_RGB_G = total_G;
                    total_RGB_B = total_B;

                    if (cb_Contrast_Brightness_Gamma.Checked == true)
                    {
                        Color pt2;
                        for (i = 0; i < 8; i++)
                        {
                            x_st = i * 80 + 20;
                            y_st = 300;

                            pt2 = bitmap1.GetPixel(x_st, y_st);
                            y_data_r[i] = pt2.R;
                            y_data_g[i] = pt2.G;
                            y_data_b[i] = pt2.B;

                            RGB pp = new RGB(pt2.R, pt2.G, pt2.B);
                            YUV yyy = new YUV();
                            yyy = RGBToYUV(pp);

                            y_data_y[i] = (int)yyy.Y;
                        }
                    }

                }
            }

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //bm.RotateFlip(RotateFlipType.RotateNoneFlipX);
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息s : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_capture_picture = false;
                return;
            }

            try
            {
                gg = Graphics.FromImage(bm);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_capture_picture = false;
                return;
            }

            int w;
            int h;
            try
            {
                w = bm.Width;
                h = bm.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息o : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_capture_picture = false;
                return;
            }

            //設定要抓取的區域
            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            //RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * (btn_right_cnt - btn_left_cnt) / 2, zoom_step * zoom_cnt * 3 / 4 / 2, w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);
            RectangleF rect = new RectangleF(zoom_step * zoom_cnt / 2 + zoom_step * btn_right_left_cnt / 2,
                                             (zoom_step * zoom_cnt / 2 + zoom_step * btn_down_up_cnt / 2) * 3 / 4,
                                             w - zoom_step * zoom_cnt, h - zoom_step * zoom_cnt * 3 / 4);

            if ((cb_show_grid.Checked == true) && (flag_enaglb_awb_function == false))
            {   //顯示格線
                int i;
                int j;

                j = 0;
                if (rb_3X3.Checked == true)
                {
                    j = 3;
                }
                else if (rb_4X4.Checked == true)
                {
                    j = 4;
                }
                else if (rb_5X5.Checked == true)
                {
                    j = 80;
                }
                else if (rb_NXN.Checked == true)
                {
                    j = 160;
                }
                else
                {
                    j = 4;
                }

                if (j >= 2)
                {
                    for (i = 1; i <= (j - 1); i++)
                    {
                        if (rb_gridlinecolor_white.Checked == true)
                        {
                            gg.DrawLine(new Pen(Color.Silver, 1), w * i / j, 0, w * i / j, h);
                            gg.DrawLine(new Pen(Color.Silver, 1), 0, h * i / j, w, h * i / j);
                        }
                        else
                        {
                            gg.DrawLine(new Pen(Color.Black, 1), w * i / j, 0, w * i / j, h);
                            gg.DrawLine(new Pen(Color.Black, 1), 0, h * i / j, w, h * i / j);
                        }
                    }
                }
            }
            else if ((cb_show_grid.Checked == true) && (flag_enaglb_awb_function == true))
            {
                int www = awb_block;
                int hhh = awb_block;

                //畫框的功能
                // Set the DashStyle property.
                Pen PenStyle2 = new Pen(Color.Black, 1);
                //PenStyle2.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
                PenStyle2.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;

                gg.DrawLine(PenStyle2, w / 2 - 140, h / 2, w / 2 + 140, h / 2);
                gg.DrawLine(PenStyle2, w / 2, h / 2 - 140, w / 2, h / 2 + 140);

                for (www = awb_block; www <= 192; www += awb_block)
                {
                    hhh = www;
                    x_st = w / 2 - www / 2;
                    if (x_st < 0)
                        x_st = 0;
                    if ((x_st + www) > w)
                        x_st = w - www;

                    y_st = h / 2 - hhh / 2;
                    if (y_st < 0)
                        y_st = 0;
                    if ((y_st + hhh) > h)
                        y_st = h - hhh;

                    gg.DrawRectangle(PenStyle2, x_st, y_st, www, hhh);
                }
            }

            if (cb_show_time.Checked == true)
            {   //顯示時間
                drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                drawBrush = new SolidBrush(Color.Yellow);
                drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                x_st = 10;
                y_st = 10;

                if (flag_david_test == true)
                {
                    gg.DrawString(saturation_ratio + ", TH2 = " + g_TH2.ToString() + ", TH1 = " + g_TH1.ToString(), drawFont1, drawBrush, x_st, y_st);
                }
                else
                {
                    gg.DrawString(drawDate, drawFont1, drawBrush, x_st, y_st);
                }
            }

            if ((flag_enaglb_awb_function == true) && (flag_fullscreen == true))
            {
                int hhh = 0;

                int ss = 10;
                int x_st2 = 0;
                int y_st2 = 0;
                Point[] points = new Point[3];
                drawFont3 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            //畫框的功能

                //if (flag_enaglb_awb_function == true)
            //{
                x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                if (x_st < 0)
                    x_st = 0;
                if ((x_st + ww) > w)
                    x_st = w - ww;

                y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
                if (y_st < 0)
                    y_st = 0;
                if ((y_st + hh) > h)
                    y_st = h - hh;

                if (timer_webcam_mode == FOCUS_ON_PICTURE)
                {
                    gg.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
                    gg.DrawRectangle(new Pen(Color.Red, 10), 0, 0, pictureBox1.Width / 2, pictureBox1.Height / 2);
                }

                if (flag_do_find_awb_location_ok == true)
                {
                    gg.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
                }
                else
                {
                    if (flag_doing_awb == false)
                    {
                        if (timer_webcam_mode == FOCUS_ON_PICTURE)
                        {
                            gg.DrawRectangle(new Pen(Color.Red, 1), x_st, y_st, ww, hh);
                            gg.DrawRectangle(new Pen(Color.Red, 10), 0, 0, pictureBox1.Width / 2, pictureBox1.Height / 2);
                        }
                        else
                            gg.DrawRectangle(new Pen(Color.Silver, 1), x_st, y_st, ww, hh);
                    }
                }

                if (flag_do_find_awb_location_ok == true)
                {
                    //gg.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
                }

                if ((cb_Contrast_Brightness_Gamma.Checked == true) && (cb_Gamma.Checked == false))
                {
                    int i;
                    i = 0;
                    x_st = i * 80 + 10;
                    y_st = 225;

                    gg.DrawString(y_data_r[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.White), x_st, y_st);
                    gg.DrawString(y_data_g[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.White), x_st, y_st + 20);
                    gg.DrawString(y_data_b[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.White), x_st, y_st + 40);
                    gg.DrawString(y_data_y_old[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Gray), x_st, y_st + 70);
                    if (y_data_y[i] == y_data_y_old[i])
                        gg.DrawString(y_data_y[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Gray), x_st, y_st + 100);
                    else
                    {
                        gg.FillRectangle(new SolidBrush(Color.White), x_st, y_st + 100, 40, 22);
                        gg.DrawString(y_data_y[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Red), x_st, y_st + 100);
                    }

                    for (i = 1; i < 8; i++)
                    {
                        x_st = i * 80 + 10;
                        y_st = 225;

                        gg.DrawString(y_data_r[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Black), x_st, y_st);
                        gg.DrawString(y_data_g[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Black), x_st, y_st + 20);
                        gg.DrawString(y_data_b[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Black), x_st, y_st + 40);
                        gg.DrawString(y_data_y_old[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Gray), x_st, y_st + 70);
                        if (y_data_y[i] == y_data_y_old[i])
                            gg.DrawString(y_data_y[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Gray), x_st, y_st + 100);
                        else
                        {
                            gg.FillRectangle(new SolidBrush(Color.White), x_st, y_st + 100, 40, 22);
                            gg.DrawString(y_data_y[i].ToString(), new Font("標楷體", 16), new SolidBrush(Color.Red), x_st, y_st + 100);
                        }
                    }

                    int ww2 = pictureBox_contrast.Width;
                    int hh2 = pictureBox_contrast.Height;
                    bm_contrast = new Bitmap(ww2, hh2);

                    gc = Graphics.FromImage(bm_contrast);
                    gc.Clear(Color.White);

                    // Create pens.
                    Pen redPen = new Pen(Color.Red, 3);
                    Pen grayPen = new Pen(Color.Gray, 10);


                    Point[] curvePoints = new Point[8];    //一維陣列內有 8 個Point

                    for (i = 0; i < 8; i++)
                    {
                        curvePoints[i].X = 40 * i;
                        curvePoints[i].Y = 255 - (y_data_y_old[i]);
                    }
                    // Draw lines between original points to screen.
                    gc.DrawLines(grayPen, curvePoints);   //畫直線
                    // Draw curve to screen.
                    //gc.DrawCurve(redPen, curvePoints); //畫曲線

                    for (i = 0; i < 8; i++)
                    {
                        curvePoints[i].X = 40 * i;
                        curvePoints[i].Y = 255 - (y_data_y[i]);
                    }
                    // Draw lines between original points to screen.
                    gc.DrawLines(redPen, curvePoints);   //畫直線
                    // Draw curve to screen.
                    //gc.DrawCurve(redPen, curvePoints); //畫曲線

                    pictureBox_contrast.Image = bm_contrast;
                }
                else if ((cb_Contrast_Brightness_Gamma.Checked == true) && (cb_Gamma.Checked == true))
                {
                    /*
                    int i;

                    int ww2 = pictureBox_contrast.Width;
                    int hh2 = pictureBox_contrast.Height;
                    bm_contrast = new Bitmap(ww2, hh2);

                    gc = Graphics.FromImage(bm_contrast);
                    gc.Clear(Color.White);

                    // Create pens.
                    Pen redPen = new Pen(Color.Red, 3);
                    Pen grayPen = new Pen(Color.Gray, 10);

                    Point[] curvePoints = new Point[16];    //一維陣列內有 16 個Point

                    for (i = 0; i < 16; i++)
                    {
                        curvePoints[i].X = 20 * i;
                        curvePoints[i].Y = 255 - (g_data_old[i]);
                    }
                    // Draw lines between original points to screen.
                    gc.DrawLines(grayPen, curvePoints);   //畫直線
                    // Draw curve to screen.
                    //gc.DrawCurve(redPen, curvePoints); //畫曲線
                    gc.DrawString("2.2", new Font("標楷體", 16), new SolidBrush(Color.Gray), 260, 80);

                    for (i = 0; i < 16; i++)
                    {
                        curvePoints[i].X = 20 * i;
                        curvePoints[i].Y = 255 - (g_data_new[i]);
                    }
                    // Draw lines between original points to screen.
                    gc.DrawLines(redPen, curvePoints);   //畫直線
                    // Draw curve to screen.
                    //gc.DrawCurve(redPen, curvePoints); //畫曲線

                    pictureBox_contrast.Image = bm_contrast;

                    */
                    pictureBox_contrast.Visible = false;

                }


                /*

                Graphics g;
                Bitmap bmp;
                //逐點製作圖檔
                int xx;
                int yy;

                bmp = new Bitmap(ww2, hh2);

                //background
                for (yy = 0; yy < hh2; yy++)
                {
                    for (xx = 0; xx < ww2; xx++)
                    {
                        bmp.SetPixel(xx, yy, Color.FromArgb(255, TARGET_AWB_R, TARGET_AWB_G, TARGET_AWB_B));
                        //bitmap3.SetPixel(xx, yy, Color.Red);
                    }
                }

                try
                {
                    g = Graphics.FromImage(bmp);
                    g.DrawRectangle(new Pen(Color.Silver, 2), 1, 1, ww2 - 2, hh2 - 2);    //draw boundary
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息r1 : " + ex.Message + "\n";
                    GC.Collect();       //回收資源
                    return;
                }

                try
                {
                    pictureBox_contrast.Image = bmp;
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息r2 : " + ex.Message + "\n";
                    GC.Collect();       //回收資源
                    return;
                }
                GC.Collect();       //回收資源
                */



                x_st = w / 2 - awb_window_size / 2;
                y_st = h / 2 - awb_window_size / 2;

                Pen PenStyle1;
                if (flag_do_find_awb_location_fail == true)
                {
                    PenStyle1 = new Pen(Color.Red, 12);
                }
                else
                    PenStyle1 = new Pen(Color.Silver, 1);
                // Set the DashStyle property.
                //PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
                PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                //PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDot;
                //PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;
                //PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
                //PenStyle1.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;

                // Draw a rectangle.
                gg.DrawRectangle(PenStyle1, x_st, y_st, awb_window_size, awb_window_size);

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

                y_st = 370;
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

                try
                {
                    //rgb_value = ((float)total_RGB_R / (ww * hh)).ToString("F2");
                    gg.DrawString(rgb_value, drawFont1, drawBrush, x_st, y_st);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
                    GC.Collect();       //回收資源
                    flag_capture_picture = false;
                    return;
                }

                if ((flag_do_awb == true) && (flag_display_r_do_awb == true))
                {
                    drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                    if (diff_r > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

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

                y_st += dy;
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
                    drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                    if (diff_g > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

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

                y_st += dy;
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
                    drawFont2 = new Font("Arial", 3, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                    if (diff_b > 0)
                    {
                        x_st2 = x_st + 100 - ss;
                        y_st2 = y_st + 6 + 3;
                        points[0] = new Point(x_st2 + ss / 2, y_st2);
                        points[1] = new Point(x_st2 + ss, y_st2 + ss);
                        points[2] = new Point(x_st2 + 0, y_st2 + ss);
                        gg.FillPolygon(new SolidBrush(Color.Red), points);

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

                /* old debug
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
                */

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

                //if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                if (flag_operation_mode == MODE_RELEASE_STAGE0)
                {
                    //draw auto awb region
                    int th_h = (int)numericUpDown_find_brightness_h.Value;
                    int th_l = (int)numericUpDown_find_brightness_l.Value;

                    //gg.DrawRectangle(new Pen(Color.Green, 1), 550, 347, 18, 255/4);
                    gg.FillRectangle(new SolidBrush(Color.LightGreen), 550, 347, 18, 255 / 4);

                    gg.FillRectangle(new SolidBrush(Color.Yellow), 550, 347, 18, (255 - th_h) / 4);
                    gg.FillRectangle(new SolidBrush(Color.Gold), 550, 347 + (255 - th_l) / 4, 18, (th_l / 4));
                }
            }
            usb_camera_width = w;
            usb_camera_height = h;

            try
            {
                //將處理之後的圖片貼出來
                pictureBox1.Image = bm.Clone(rect, PixelFormat.Format32bppArgb);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源

            flag_capture_picture = false;
            return;
        }

        bool flag_ok_camera_serial1 = false;
        bool flag_ok_camera_serial2 = false;
        private void timer_stage4_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在燒錄資料, 忽略\n";
                return;
            }

            if (flag_comport_ok == false)
                return;

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "四";
                if (this.tb_wait_camera_data.Focused == false)
                {
                    this.tb_wait_camera_data.Focus();
                    richTextBox1.Text += "F4";
                }
            }

            if (flag_network_disk_status == false)
            {
                tb_wait_camera_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            int len;
            len = tb_wait_camera_data.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_wait_camera_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_camera_data.Text[len - 2] == 0x0D) || (tb_wait_camera_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_camera_data.Text = tb_wait_camera_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_camera_data.Text.Length > 0)
            {
                lb_sn1.Text = "";
                lb_sn2.Text = "";
                lb_sn3.Text = "";

                int i;
                bool flag_incorrect_data = false;
                if ((tb_wait_camera_data.Text.Length == 9) || (tb_wait_camera_data.Text.Length == 10))
                {
                    //檢查英文字母的正確性
                    if (((tb_wait_camera_data.Text[0] >= 'A') && (tb_wait_camera_data.Text[0] <= 'Z')) || ((tb_wait_camera_data.Text[0] >= 'a') && (tb_wait_camera_data.Text[0] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        //richTextBox1.Text += "SN1格式不正確b0\n";
                        //tb_sn1.Text = "SN1格式不正確b0\n";
                    }

                    if (((tb_wait_camera_data.Text[1] >= 'A') && (tb_wait_camera_data.Text[1] <= 'Z')) || ((tb_wait_camera_data.Text[1] >= 'a') && (tb_wait_camera_data.Text[1] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        //richTextBox1.Text += "SN1格式不正確b1\n";
                        //tb_sn1.Text = "SN1格式不正確b1\n";
                    }


                    for (i = 2; i < tb_wait_camera_data.Text.Length; i++)
                    {
                        if ((tb_wait_camera_data.Text[i] < '0') || (tb_wait_camera_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            //richTextBox1.Text += "SN1格式不正確b\n";
                            //tb_sn1.Text = "SN1格式不正確b\n";
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "4取得 SN1序號 : " + tb_wait_camera_data.Text + "\n";
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
                            //richTextBox1.Text += "SN2格式不正確b\n";
                            //tb_sn2.Text = "SN2格式不正確\n";
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
                            flag_doing_writing_data = true;
                            if (flag_comport_ok == false)
                            {
                                richTextBox1.Text += "未連線comport, abort\n";
                                tb_wait_camera_data.Text = "";
                                flag_doing_writing_data = false;
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

                        lb_sn1.Text = "";
                        lb_sn2.Text = "";
                        lb_sn3.Text = "";

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
            panel_camera_status5.BackgroundImage = null;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            tb_wait_camera_data.Clear();
            lb_write_camera_serial2.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
            tb_sn1.Text = "";
            tb_sn2.Text = "";
            //groupBox10.BackColor = System.Drawing.SystemColors.ControlLightLight;
            lb_write_camera_serial2.Text += "";
            lb_write_camera_serial2.ForeColor = Color.Black;
            button11.BackColor = System.Drawing.SystemColors.ControlLight;
            g2.Clear(BackColor);

            bt_confirm.Visible = false;
            timer_stage4.Enabled = true;
        }

        //int camera_start = 0;
        private void button12_Click_1(object sender, EventArgs e)
        {
            if (flag_doing_refreshing_camera == true)
            {
                richTextBox1.Text += "正在影像重抓, 忽略\n";
                return;
            }

            if ((flag_operation_mode != MODE_RELEASE_STAGE1A) && (flag_operation_mode != MODE_RELEASE_STAGE1B) && (flag_operation_mode != MODE_RELEASE_STAGE3))
            {
                if (flag_comport_ok == false)
                {
                    show_main_message1("影像重抓", S_OK, 30);
                    richTextBox1.Text += "no comport, abort\n";
                    return;
                }
            }

            flag_doing_refreshing_camera = true;

            show_main_message1("影像重抓", S_OK, 30);
            if (Cam != null)
            {
                if ((flag_camera_start == 1) && (Cam.IsRunning == true))
                {
                    richTextBox1.Text += "USB影像傳輸中, 中斷重來ST\n";  //david : 應考慮此功能是否有用?
                    flag_camera_start = 0;
                    Cam.Stop();  // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
                    comboBox_webcam.Items.Clear();
                    richTextBox1.Text += "USB影像傳輸中, 中斷重來SP\n";
                }
            }

            richTextBox1.Text += "call check_webcam() 222\n";
            if (check_webcam() == S_OK)
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
                flag_camera_start = 0;
                Cam.Stop();  // WebCam stops capturing images.
                //Cam.SignalToStop();
                //Cam.WaitForStop();
                Cam = null;
            }
            */
            flag_doing_refreshing_camera = false;
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning == true)  // When Form1 closes itself, WebCam must stop, too.
                {
                    flag_camera_start = 0;
                    Cam.Stop();   // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
                }
            }

            richTextBox1.Text += "關閉程式\n";
            /*
            //Application.Exit();
            try
            {
                Environment.Exit(0);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f : " + ex.Message + "\n";
            }
            Environment.Exit(Environment.ExitCode);
            */

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();
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
                    flag_camera_start = 0;
                    Cam.Stop();
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
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
                    show_main_message1("影像停止", S_FALSE, 30);
                }
                else
                {
                    flag_camera_is_stopped = 0;
                    richTextBox1.Text += "繼續\n";
                    enable_camera_streaming(true);
                    show_main_message1("影像繼續", S_OK, 30);
                }
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
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
            //richTextBox1.AppendText("螢幕解析度 : " + Screen.PrimaryScreen.Bounds.Width.ToString() + "*" + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n");
            if (flag_fullscreen == false)
            {
                flag_fullscreen = true;

                if (flag_display_mode == DISPLAY_SD)
                {
                    int dy = 0;
                    lb_sn_opal.Text = "序號";
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X - 12, cb_enable_awb.Location.Y + 56 + 65 + 2 - dy);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X + 50 - 4, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170 + 60 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);

                    lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 10 - dy);

                    lb_main_mesg2.Location = new Point(tb_sn_opal.Location.X + 130, tb_sn_opal.Location.Y);

                    if (flag_operation_mode == MODE_RELEASE_STAGE3)
                    {
                        dy = 80;
                        lb_rgb_r.Location = new Point(lb_rgb_r.Location.X, lb_rgb_r.Location.Y - dy);
                        lb_rgb_g.Location = new Point(lb_rgb_g.Location.X, lb_rgb_g.Location.Y - dy);
                        lb_rgb_b.Location = new Point(lb_rgb_b.Location.X, lb_rgb_b.Location.Y - dy);
                        lb_sn_opal.Location = new Point(lb_sn_opal.Location.X, lb_sn_opal.Location.Y - dy);
                        tb_sn_opal.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y - dy);
                        tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 30);
                        lb_class.Location = new Point(tb_wait_sn_data.Location.X + 140 + 27, tb_wait_sn_data.Location.Y - 190);
                        lb_main_mesg2.Location = new Point(tb_wait_sn_data.Location.X + 140, tb_wait_sn_data.Location.Y);

                        cb_air_ng.Location = new Point(tb_sn_opal.Location.X + 145, tb_sn_opal.Location.Y - 40); //SD display + big show
                        cb_change_rank.Location = new Point(tb_sn_opal.Location.X + 145, tb_sn_opal.Location.Y - 5); //SD display + big show
                    }
                }
                else
                {
                    if (flag_operation_mode != MODE_RELEASE_STAGE0)
                    {
                        int dy = 100;
                        lb_sn_opal.Location = new Point(cb_enable_awb.Location.X, cb_enable_awb.Location.Y + 28 + dy);
                        tb_sn_opal.Location = new Point(cb_enable_awb.Location.X, cb_enable_awb.Location.Y + 56 + dy);
                        lb_main_mesg2.Location = new Point(cb_enable_awb.Location.X, cb_enable_awb.Location.Y + 56 + dy + 40);
                        bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170, cb_enable_awb.Location.Y + 56 - 20 + dy);
                        bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170, cb_enable_awb.Location.Y + 56 + 20 + dy);
                    }
                    else
                    {
                        int x_st = 1500;
                        int y_st = 930;
                        lb_sn_opal.Text = "Opal序號";
                        lb_sn_opal.Location = new Point(x_st + 10, y_st + 5);
                        tb_sn_opal.Location = new Point(x_st + 120, y_st);
                        bt_save_img.Location = new Point(x_st + 250, y_st);
                        bt_clear_serial.Location = new Point(x_st + 315, y_st);


                        lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 10);
                        lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 10);
                        lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 10);

                        lb_main_mesg2.Location = new Point(tb_sn_opal.Location.X - 500, tb_sn_opal.Location.Y - 150);

                    }
                    lb_rgb_r.Location = new Point(5, 489 + 65 + 47);
                    lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47);
                    lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47);

                    if (flag_operation_mode == MODE_RELEASE_STAGE3)
                    {
                        tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 70);
                        lb_class.Location = new Point(tb_wait_sn_data.Location.X + 138 + 10, tb_wait_sn_data.Location.Y - 150);
                        lb_main_mesg2.Location = new Point(lb_main_mesg2.Location.X, lb_main_mesg2.Location.Y - 8);

                        cb_air_ng.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 120); //HD display + big show
                        cb_change_rank.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 120 + 50); //HD display + big show
                    }
                }

                button19.BackgroundImage = imsLink.Properties.Resources.normal_screen;
                //this.TopMost = true;

                this.FormBorderStyle = FormBorderStyle.None;
                this.WindowState = FormWindowState.Maximized;
                //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                this.Location = new System.Drawing.Point(0, 0);

                if (flag_display_mode == DISPLAY_SD)
                {
                    //richTextBox1.Text += "this.Size W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString() + "\n";
                    this.Size = new Size(this.Size.Width + 200, 750);
                    tabControl1.Size = new Size(1600 + 200, 1010);
                    if (flag_enaglb_awb_function == true)
                        pictureBox1.Size = new Size(640 * 11 / 10, 480 * 11 / 10);
                    else
                    {
                        pictureBox1.Size = new Size(640 * 4 / 3, 480 * 4 / 3);
                    }
                }
                else   //DISPLAY_FHD
                {
                    tabControl1.Size = new Size(1600 + 300, 1010);
                    pictureBox1.Size = new Size(640 * 2, 480 * 2);
                }

                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y);
                toolTip1.SetToolTip(button19, "1X");

                if (flag_enaglb_awb_function == true)
                {
                    pictureBox1.Location = new Point(170 + 400 + 30, 7);
                    richTextBox1.Visible = true;
                   
                    this.richTextBox1.Location = new System.Drawing.Point(150, 90);
                    this.richTextBox1.Size = new System.Drawing.Size(400 + 30 + 20, 250);

                    show_awb_item_visible(true);    //333

                    if (flag_display_mode == DISPLAY_SD)
                    {
                        //lb_note1.Location = new Point(11 + 180 + 110, 489 + 98 + 19);
                        //lb_note2.Location = new Point(11 + 180 + 110, 489 + 98 + 25 + 12);
                        //lb_note3.Location = new Point(11 + 180 + 110, 489 + 98 + 50 + 6);
                        lb_note1.Location = new Point(10 + 180 + 150, 489 + 98 + 19);
                        lb_note2.Location = new Point(10 + 180 + 150, 489 + 98 + 25 + 12);
                        lb_note3.Location = new Point(10 + 180 + 150, 489 + 98 + 50 + 6);
                    }
                    else
                    {
                        //lb_note1.Location = new Point(11 + 180 + 110, 489 + 98 + 19);
                        //lb_note2.Location = new Point(11 + 180 + 110, 489 + 98 + 25 + 12);
                        //lb_note3.Location = new Point(11 + 180 + 110, 489 + 98 + 50 + 6);
                        lb_note1.Location = new Point(10 + 180 + 90, 489 + 98 + 19);
                        lb_note2.Location = new Point(10 + 180 + 90, 489 + 98 + 25 + 12);
                        lb_note3.Location = new Point(10 + 180 + 90, 489 + 98 + 50 + 6);
                    }
                }
                else
                {
                    pictureBox1.Location = new Point(170 + 90 + 80, 10);
                    richTextBox1.Visible = false;
                }
                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y);
            }
            else
            {
                flag_fullscreen = false;

                if (flag_display_mode == DISPLAY_SD)
                {
                    int dy = 62;
                    lb_sn_opal.Text = "序號";
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X - 12, cb_enable_awb.Location.Y + 56 + 65 + 2 - dy);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X + 50 - 4, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170 + 60 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);

                    lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 10 - dy);

                    lb_main_mesg2.Location = new Point(tb_sn_opal.Location.X + 140, tb_sn_opal.Location.Y);

                    if (flag_operation_mode == MODE_RELEASE_STAGE3)
                    {
                        dy = 28;
                        lb_rgb_r.Location = new Point(lb_rgb_r.Location.X, lb_rgb_r.Location.Y - dy);
                        lb_rgb_g.Location = new Point(lb_rgb_g.Location.X, lb_rgb_g.Location.Y - dy);
                        lb_rgb_b.Location = new Point(lb_rgb_b.Location.X, lb_rgb_b.Location.Y - dy);
                        lb_sn_opal.Location = new Point(lb_sn_opal.Location.X, lb_sn_opal.Location.Y - dy);
                        tb_sn_opal.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y - dy);
                        tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X, tb_sn_opal.Location.Y + 32);
                        lb_class.Location = new Point(tb_wait_sn_data.Location.X + 167, tb_wait_sn_data.Location.Y - 140);
                        lb_main_mesg2.Location = new Point(tb_wait_sn_data.Location.X + 140, tb_wait_sn_data.Location.Y);

                        cb_air_ng.Location = new Point(tb_sn_opal.Location.X + 600, tb_sn_opal.Location.Y + 20);   //SD display + small show
                        cb_change_rank.Location = new Point(tb_sn_opal.Location.X + 600 + 150, tb_sn_opal.Location.Y + 20);   //SD display + small show
                    }
                }
                else
                {
                    int dy = 62;
                    lb_sn_opal.Text = "序號";
                    lb_sn_opal.Location = new Point(cb_enable_awb.Location.X - 12, cb_enable_awb.Location.Y + 56 + 65 + 2 - dy);
                    tb_sn_opal.Location = new Point(cb_enable_awb.Location.X + 50 - 4, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    lb_main_mesg2.Location = new Point(cb_enable_awb.Location.X + 50 - 4 + 140, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_save_img.Location = new Point(cb_enable_awb.Location.X + 170 + 60 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);
                    bt_clear_serial.Location = new Point(cb_enable_awb.Location.X + 170 + 3, cb_enable_awb.Location.Y + 56 + 65 - dy);

                    lb_rgb_r.Location = new Point(5, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_g.Location = new Point(5 + 50, 489 + 65 + 47 - 10 - dy);
                    lb_rgb_b.Location = new Point(5 + 100, 489 + 65 + 47 - 10 - dy);

                    if (flag_operation_mode == MODE_RELEASE_STAGE3)
                    {
                        tb_wait_sn_data.Location = new Point(tb_sn_opal.Location.X + 140, tb_sn_opal.Location.Y);
                        lb_class.Location = new Point(tb_wait_sn_data.Location.X + 20 + 8, tb_wait_sn_data.Location.Y - 138);
                        lb_main_mesg2.Location = new Point(tb_wait_sn_data.Location.X + 140, tb_wait_sn_data.Location.Y);

                        cb_air_ng.Location = new Point(tb_sn_opal.Location.X + 600, tb_sn_opal.Location.Y - 5);     //HD display + small show
                        cb_change_rank.Location = new Point(tb_sn_opal.Location.X + 600+150, tb_sn_opal.Location.Y - 5);     //HD display + small show
                    }
                }

                button19.BackgroundImage = imsLink.Properties.Resources.full_screen;
                richTextBox1.Visible = true;
                this.richTextBox1.Location = new System.Drawing.Point(958, 67);
                this.richTextBox1.Size = new System.Drawing.Size(500, 586);
                this.FormBorderStyle = FormBorderStyle.Sizable;
                this.WindowState = FormWindowState.Normal;
                if (flag_display_mode == DISPLAY_SD)
                {
                    this.Size = new Size(960, 743);
                    tabControl1.Size = new Size(tabControl1.Size.Width - 200, 1010);
                }
                //this.TopMost = false;
                //tabControl1.Size = new Size(948, 616);
                pictureBox1.Location = new Point(220, 60);
                pictureBox1.Size = new Size(640, 480);
                comboBox_webcam.Location = new Point(pictureBox1.Location.X + pictureBox1.Width - comboBox_webcam.Width, pictureBox1.Location.Y - comboBox_webcam.Height);

                if (flag_display_mode == DISPLAY_SD)
                {
                    if (flag_enaglb_awb_function == true)
                    {
                        toolTip1.SetToolTip(button19, "1.10X");
                    }
                    else
                    {
                        toolTip1.SetToolTip(button19, "1.33X");
                    }
                }
                else
                {
                    toolTip1.SetToolTip(button19, "2X");
                }

                if (flag_enaglb_awb_function == true)
                {
                    show_awb_item_visible(false);   //444
                }
            }

            if (flag_operation_mode == MODE_RELEASE_STAGE0)
            {
                if (cb_Contrast_Brightness_Gamma.Checked == true)
                {
                    gb_contrast_brightness.Visible = true;
                    gb_contrast_brightness2.Visible = true;
                    gb_contrast_brightness3.Visible = true;
                    pictureBox_contrast.Visible = true;
                }
                else
                {
                    gb_contrast_brightness.Visible = false;
                    gb_contrast_brightness2.Visible = false;
                    gb_contrast_brightness3.Visible = false;
                    pictureBox_contrast.Visible = false;
                }
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            exit_program();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("https://www.insighteyes.com/");
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

            //richTextBox1.Text += "目前時間 : " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

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

            rtc_data_send[0] = (byte)(dt.Year - 2000);
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
            panel_camera_status5.BackgroundImage = null;

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
                tb_sn1.Text = "狀態不明d, status = " + g_conn_status.ToString();
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
            panel_camera_status5.BackgroundImage = null;

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
                tb_sn1.Text = "狀態不明e, status = " + g_conn_status.ToString();
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
            panel_camera_status5.BackgroundImage = null;

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
                tb_sn1.Text = "狀態不明f, status = " + g_conn_status.ToString();
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
            save_log_to_local_drive();
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
            //richTextBox1.Text += "pictureBox double click at x = " + MousePosition.X.ToString() + " y = " + MousePosition.Y.ToString() + "\n";

            int x_st = MousePosition.X - pictureBox1.Location.X - tabControl1.Location.X;
            int y_st = MousePosition.Y - pictureBox1.Location.Y - tabControl1.Location.Y - tabControl1.ItemSize.Height;

            richTextBox1.Text += "x_st = " + x_st.ToString() + " y_st = " + y_st.ToString() + "\n";
        }

        bool flag_ok_machine_serial = false;
        bool flag_ok_mb_big_serial = false;
        bool flag_ok_mb_small_serial = false;
        bool flag_ok_to_write_data = false;
        private void scanner_timer2_Tick(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
                return;

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "B1";
                if (this.tb_wait_data.Focused == false)
                {
                    this.tb_wait_data.Focus();
                    richTextBox1.Text += "FB1";
                }
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
                timer_stage4.Enabled = false;
                flag_auto_scan_mode = false;
                button40.Text = "到自動模式";
            }
            else
            {
                timer_stage4.Enabled = true;
                flag_auto_scan_mode = true;
                button40.Text = "到修改模式";
            }
        }

        //bool flag_try_connect_comport = false;
        int read_connection_cnt = 0;
        int read_connection_fail_cnt = 0;
        private void timer_rtc_Tick(object sender, EventArgs e)
        {
            /*
            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                if (flag_try_connect_comport == false)
                {
                    flag_try_connect_comport = true;
                    richTextBox1.Text += "auto call connect_IMS_comport()\n";
                    connect_IMS_comport();
                }
            }
            */

            if (flag_comport_ok == false)
                return;

            if (flag_comport_connection_ok == false)
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
                    panel_camera_status5.BackgroundImage = null;
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

        int cccc = 0;
        int total_RGB_R_old = -1;
        int total_RGB_G_old = -1;
        int total_RGB_B_old = -1;

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            //txtPoint.Text = Control.MousePosition.X.ToString() + "," + Control.MousePosition.Y.ToString();
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            panel1.BackColor = cl;
            lb_rgb_r.Text = cl.R.ToString();
            lb_rgb_g.Text = cl.G.ToString();
            lb_rgb_b.Text = cl.B.ToString();

            RGB pp = new RGB(cl.R, cl.G, cl.B);
            YUV yyy = new YUV();
            yyy = RGBToYUV(pp);
            lb_yuv_y.Text = ((int)yyy.Y).ToString();
            lb_yuv_u.Text = ((int)yyy.U).ToString();
            lb_yuv_v.Text = ((int)yyy.V).ToString();
            lb_yuv_y2.Text = ((int)yyy.Y).ToString();

            if (flag_check_webcam_signal == true)
            {
                cccc++;
                if ((cccc % 50) == 0)
                {
                    //richTextBox1.Text += "R " + total_RGB_R.ToString() + "    " + "G " + total_RGB_G.ToString() + "    " + "B " + total_RGB_B.ToString() + "\n";
                    if ((total_RGB_R == total_RGB_R_old) && (total_RGB_G == total_RGB_G_old) && (total_RGB_B == total_RGB_B_old))
                    {
                        //richTextBox1.Text += "refresh webcam\n";
                        //button12_Click_1(sender, e);
                    }
                    else
                    {
                        total_RGB_R_old = total_RGB_R;
                        total_RGB_G_old = total_RGB_G;
                        total_RGB_B_old = total_RGB_B;
                    }
                }
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);

            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                tb_sn1.Text = "AA0000000";
                tb_sn2.Text = "00000000000";
            }
            else
            {
                tb_sn1.Text = "AA1234567";
                tb_sn2.Text = "12345678901";
            }
            tb_sn1.Text = "";
            tb_sn2.Text = "";

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
            if ((tb_sn1.Text.Length != 9) && (tb_sn1.Text.Length != 10))
            {
                richTextBox1.Text += "相機序號1長度錯誤, 長度 : " + tb_sn1.Text.Length.ToString() + "\n";
                lb_write_camera_serial2.Text = "相機型號1長度錯誤";
                playSound(S_FALSE);
                flag_doing_writing_data = false;
                return;
            }
            if (tb_sn2.Text.Length != 11)
            {
                richTextBox1.Text += "相機序號2長度錯誤, 長度 : " + tb_sn2.Text.Length.ToString() + "\n";
                lb_write_camera_serial2.Text = "相機型號2長度錯誤";
                playSound(S_FALSE);
                flag_doing_writing_data = false;
                return;
            }

            panel_camera_status1.BackgroundImage = null;
            panel_camera_status2.BackgroundImage = null;
            panel_camera_status3.BackgroundImage = null;
            panel_camera_status4.BackgroundImage = null;
            panel_camera_status5.BackgroundImage = null;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                button11.BackColor = System.Drawing.SystemColors.ControlLight;
                playSound(S_FALSE);
                flag_doing_writing_data = false;
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            delay(200);
            delay(200);
            Send_IMS_Data(0xFF, 0, 0, 0);

            int cnt = 0;
            while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 30))
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
                playSound(S_FALSE);
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_aa1.Text = "有連接器, 無相機";
                tb_info_aa1.BackColor = Color.Red;
                lb_write_camera_serial2.Text = "有連接器, 無相機";
                playSound(S_FALSE);
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_info_8.Text = "有連接器, 有相機";
                tb_info_8.BackColor = Color.White;
                lb_write_camera_serial2.Text = "有連接器, 有相機, 寫入相機序號中...";

                int i;

                byte[] sn_data_tmp = new byte[21];
                for (i = 0; i < tb_sn1.Text.Length; i++)
                {
                    sn_data_tmp[i] = (byte)tb_sn1.Text[i];
                    //richTextBox1.Text += "\ni = " + i.ToString() + " tmp data : " + tb_sn1.Text[i].ToString();
                }

                if (tb_sn1.Text.Length == 9)
                    sn_data_tmp[9] = 0xff;

                //richTextBox1.Text += "\n";

                for (i = 10; i < (10 + tb_sn2.Text.Length); i++)
                {
                    sn_data_tmp[i] = (byte)tb_sn2.Text[i - 10];
                    //richTextBox1.Text += "\ni = " + i.ToString() + " tmp data : " + tb_sn2.Text[i - tb_sn1.Text.Length].ToString();
                }

                //richTextBox1.Text += "\n";

                Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write

                serialPort1.Write(sn_data_tmp, 0, 21);

                flag_camera_already_have_serial = 1;
                cnt = 0;
                int cnt_max = 50;
                while ((flag_camera_already_have_serial == 1) && (cnt < cnt_max))
                {
                    cnt++;
                    richTextBox1.Text += "s";
                    //richTextBox1.Text += "e" + cnt.ToString() + " ";
                    delay(10);
                }

                if (flag_camera_already_have_serial == 1)
                {
                    richTextBox1.Text += "相機已有序號, break\n";
                    lb_write_camera_serial2.Text = "相機已有序號, 中斷";

                    g2.Clear(BackColor);
                    g2.DrawString("燒錄失敗", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                    bt_confirm.Visible = true;
                    timer_stage4.Enabled = false;
                    playSound(S_FALSE);
                }
                else
                {
                    richTextBox1.Text += "相機無序號, continue\n";

                    richTextBox1.Text += "序號 : 寫入資料  完成\n";

                    lb_write_camera_serial2.Text = "寫入資料";

                    delay(500);

                    lb_write_camera_serial2.Text = "寫入相機序號完成";
                    lb_write_camera_serial2.ForeColor = Color.Black;
                    button11.BackColor = System.Drawing.SystemColors.ControlLight;
                    g2.Clear(BackColor);
                    g2.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
                    button11.BackColor = System.Drawing.SystemColors.ControlLight;
                    lb_write_camera_serial2.Text += "    燒錄完成";

                    delay(200);
                    delay(200);

                    //驗證資料
                    lb_write_camera_serial2.Text += "    驗證中";
                    lb_write_camera_serial2.ForeColor = Color.Blue;
                    richTextBox1.Text += "\n讀相機序號回來 " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

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

                    richTextBox1.Text += "delay ST\n";
                    //flag_verify_serial_data = 1;
                    //Get_IMS_Data(0, 0xAA, 0xAA);

                    //delay(200);
                    delay(200);
                    delay(200);
                    richTextBox1.Text += "delay SP\n";

                    richTextBox1.Text += "驗證完成, 序號相同\n";
                    lb_write_camera_serial2.Text += "    驗證完成";
                    lb_write_camera_serial2.ForeColor = Color.Black;
                    g2.Clear(BackColor);
                    g2.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    //richTextBox1.Text += "把資料暫存起來\n";
                    camera_serials.Add(new string[] { tb_sn1.Text, tb_sn2.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });

                    //if ((camera_serials.Count % 5) == 0)
                    {
                        richTextBox1.Text += "自動存檔\n";
                        flag_operation_mode = MODE_RELEASE_STAGE4;
                        exportCSV();
                        flag_operation_mode = MODE_RELEASE_STAGE2;
                    }

                    // Stop timing
                    stopwatch.Stop();
                    richTextBox1.Text += "燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

                    if (stopwatch.ElapsedMilliseconds > 7000)
                    {
                        flag_burn_long_cnt++;
                        ////lb_mesg2.Text = "耗時太久 " + flag_burn_long_cnt.ToString() + " 次";
                    }
                    flag_doing_writing_data = false;
                }
            }
            else
            {
                tb_sn1.Text = "狀態不明g, status = " + g_conn_status.ToString();
            }

            flag_doing_writing_data = false;
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (flag_enaglb_awb_function == false)
                return;
            if (flag_usb_mode == true)
                return;

            int x_st_old = 0;
            int y_st_old = 0;
            int ww = awb_block;
            int hh = awb_block;

            int WW = 640;
            int HH = 480;

            int flag_right_left_cnt_old = flag_right_left_cnt;
            int flag_down_up_cnt_old = flag_down_up_cnt;

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
                awb_block = 32;

                flag_right_left_point_cnt = 0;
                flag_down_up_point_cnt = 0;
                step = 1;
                add_amount = 1;
                add_tmp = 0;
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
                exit_program();
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
            else if ((e.KeyCode == Keys.Return) || (e.KeyCode == Keys.Escape))
            {
                lb_main_mesg2.Text = "等待輸入資料";
                timer_webcam_mode = FOCUS_ON_SERIAL;
                tb_sn_opal.BackColor = Color.Pink;
            }
            else
            {
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";

            }
            refresh_picturebox2();
        }

        int timer_webcam_cnt = 0;
        private void timer_stage2_Tick(object sender, EventArgs e)
        {
            if (flag_wait_for_confirm == true)
            {
                show_main_message1("等待確認", S_FALSE, 30);
                show_main_message2("等待確認", S_FALSE, 30);
                show_main_message3("等待確認", S_FALSE, 30);
                return;
            }

            if (flag_network_disk_status == false)
            {
                tb_sn_opal.Clear();
                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);

                tb_awb_mesg.BackColor = Color.Pink;
                tb_awb_mesg.Text = "無法連上網路磁碟機";
                return;
            }

            if (flag_enaglb_awb_function == false)
                return;

            if (timer_webcam_mode == FOCUS_ON_PICTURE)
            {
                if ((timer_cnt++ % 10) == 0)
                {
                    richTextBox1.Text += "二a";
                    if (this.pictureBox1.Focused == false)
                    {
                        this.pictureBox1.Focus();
                        richTextBox1.Text += "F2a";
                    }
                }
                if (frame_cnt_old == frame_cnt)
                {
                    //richTextBox1.Text += "X";
                    frame_cnt_old = frame_cnt;
                }
                else
                {
                    //richTextBox1.Text += "Y";
                    frame_cnt_old = frame_cnt;
                }
            }
            else if (timer_webcam_mode == FOCUS_ON_SERIAL)
            {
                if (flag_network_disk_status == true)
                {
                    ccc++;
                    if (flag_operation_mode == MODE_RELEASE_STAGE2)
                    {
                        if (flag_doing_awb == true)
                        {
                            lb_main_mesg2.Text = "色彩校正進行中 ....";
                        }
                        else
                        {
                            if ((ccc % 4) == 0)
                                lb_main_mesg2.Text = "刷Barcode啟動色彩校正 \\";
                            else if ((ccc % 4) == 1)
                                lb_main_mesg2.Text = "刷Barcode啟動色彩校正 |";
                            else if ((ccc % 4) == 2)
                                lb_main_mesg2.Text = "刷Barcode啟動色彩校正 /";
                            else
                                lb_main_mesg2.Text = "刷Barcode啟動色彩校正 -";
                        }
                    }
                    else   //mode0
                    {
                        if ((ccc % 4) == 0)
                            lb_main_mesg2.Text = "等待輸入資料 \\";
                        else if ((ccc % 4) == 1)
                            lb_main_mesg2.Text = "等待輸入資料 |";
                        else if ((ccc % 4) == 2)
                            lb_main_mesg2.Text = "等待輸入資料 /";
                        else
                            lb_main_mesg2.Text = "等待輸入資料 -";
                    }
                }

                if ((timer_cnt++ % 10) == 0)
                {
                    richTextBox1.Text += "二b";
                    if (this.tb_sn_opal.Focused == false)
                    {
                        this.tb_sn_opal.Focus();
                        richTextBox1.Text += "F2b";
                    }
                    this.tb_sn_opal.BackColor = Color.Pink;

                    /*  取得亮度
                    if (timer_cnt > 20)
                    {
                        DongleAddr_h = 0x3A;
                        DongleAddr_l = 0x19;
                        Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);
                    }
                    */
                }

                int result = check_tb_sn_opal_data();
                if (result == S_OK)
                {
                    /*  舊的存圖方法
                    timer_stage2.Enabled = false;
                    lb_main_mesg2.Text = "資料正確, 存檔中";
                    save_image_to_drive();
                    delay(30);
                    timer_stage2.Enabled = true;
                    */

                    //show_main_message1("存檔中...", S_OK, 10);
                    //tb_awb_mesg.Text = "相機序號正確";

                    int do_awb_result = do_awb(sender, e);
                    check_awb_result(do_awb_result);

                    tb_sn_opal.Text = "";

                    if (flag_operation_mode == MODE_RELEASE_STAGE2)
                    {
                        bt_awb_test.Enabled = false;
                        bt_awb_test.BackColor = Color.Pink;
                    }


                }


            }

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
                lb_rgb_r.Text = "";
                lb_rgb_g.Text = "";
                lb_rgb_b.Text = "";
                timer_stage2.Enabled = false;
                //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode
            }
            else
            {
                bt_awb.Text = "Manual";
                timer_stage2.Enabled = true;
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode
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
                richTextBox1.Text += "Fail " + DongleAddr_h.ToString("X2") + DongleAddr_l.ToString("X2") + "\t";
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
                richTextBox1.Text += "read again " + DongleAddr_h1.ToString("X2") + DongleAddr_l1.ToString("X2") + "\t";
                delay(20);
            }

            if ((DongleAddr_h2 == 0x00) && (DongleAddr_l2 == 0x00))
            {
                return;
            }

            while (read_camera_sensor0(cmd, DongleAddr_h2, DongleAddr_l2) == false)
            {
                richTextBox1.Text += "read again " + DongleAddr_h2.ToString("X2") + DongleAddr_l2.ToString("X2") + "\t";
                delay(20);
            }
        }

        private void bt_get_setup_Click(object sender, EventArgs e)
        {
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

            get_expo_data();
            get_gain_data();
            get_r_data();
            get_g_data();
            get_b_data();
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

        int get_expo_data()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            data_expo = -1;
            lb_awb_result_expo.Text = "";
            flag_awb_update_expo = false;
            read_camera_sensor(SENSOR_EXPO);

            if (data_expo != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整expo\t";
                return S_FALSE;
            }
        }

        int get_gain_data()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            data_gain = -1;
            lb_awb_result_gain.Text = "";
            flag_awb_update_gain = false;
            read_camera_sensor(SENSOR_GAIN);

            if (data_gain != -1)
            {
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料不完整gain\t";
                return S_FALSE;
            }
        }

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
                richTextBox1.Text += "資料不完整r\t";
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
                richTextBox1.Text += "資料不完整g\t";
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
                richTextBox1.Text += "資料不完整b\t";
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
                richTextBox1.Text += "RGB有飽和\t";

            int rgb_ok_cnt = 0;
            while (true)
            {
                if (flag_awb_break == true)
                {
                    richTextBox1.Text += "awb break 1\n";
                    break;
                }

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
                if (progressBar_awb.Value < (30 - 2))
                    progressBar_awb.Value += 2;
            }
            richTextBox1.Text += "RGB皆未飽和b\n";
        }

        int check_camera_status()
        {
            int result = S_OK;

            richTextBox1.Text += "check_camera_status ST\n";

            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料

            //開始檢查相機連線
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
                richTextBox1.Text += "無連接器\n";
                playSound(S_FALSE);
                result = g_conn_status;
                return result;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                richTextBox1.Text += "有連接器, 無相機\n";
                playSound(S_FALSE);
                result = g_conn_status;
                return result;
            }
            else if (g_conn_status == CAMERA_SENSOR_FAIL)
            {
                richTextBox1.Text += "有連接器, 有相機, 但是相機無法讀寫a\n";
                tb_awb_mesg.Text = "相機無法讀寫";
                bt_awb_test.BackColor = Color.Red;
                flag_doing_awb = false;
                bt_awb_test.Enabled = false;
                playSound(S_FALSE);
                bt_awb_break.Visible = true;
                bt_awb_break.Text = "確認";
                result = g_conn_status;
                return result;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                richTextBox1.Text += "有連接器, 有相機b\n";
                result = g_conn_status;
                return result;
            }
            else
            {
                richTextBox1.Text += "狀態不明h, status = " + g_conn_status.ToString() + "\n";
                richTextBox1.Text += "狀態不明h, 再呼叫自己一次\n";

                //再呼叫自己一次
                return check_camera_status();
            }
        }

        int do_awb(object sender, EventArgs e)
        {
            flag_break_doing_awb = false;

            int result = S_OK;
            if (flag_doing_awb == false)
            {
                //tb_awb_mesg.Text = "";
                flag_doing_awb = true;
                bt_awb_test.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "色彩校正 進行中, abort\n";
                playSound(S_FALSE);
                result = REASON_AWB_PROCESSING;
                return result;
            }

            if (cb_auto_search.Checked == true)
            {
                //自動搜尋模式需要先歸零
                flag_right_left_cnt = 0;
                flag_down_up_cnt = 0;
                flag_right_left_point_cnt = 0;
                flag_down_up_point_cnt = 0;
                awb_block = 32;
                step = 1;
                add_amount = 1;
                add_tmp = 0;
                //ww = awb_block;
                //hh = awb_block;
                refresh_picturebox2();
                delay(100);
            }

            richTextBox1.Text += "開始檢查相機連線\n";

            int camera_status;
            camera_status = check_camera_status();

            if (camera_status != CAMERA_OK)
                return camera_status;

            //david debug
            //flag_doing_awb = false;
            //return camera_status;

            richTextBox1.Text += "有連接器, 有相機c\n";

            if (flag_operation_mode == MODE_RELEASE_STAGE2)
                lb_main_mesg2.Text = "色彩校正進行中 ....";
            else
                lb_main_mesg2.Text = "等待輸入資料";
            
            timer_stage2.Enabled = true;
            timer_webcam_mode = FOCUS_ON_SERIAL;
            tb_sn_opal.BackColor = Color.Pink;

            int i;
            if (flag_comport_ok == false)
            {
                //MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //bt_awb_test.Text = "無COM連線";
                tb_awb_mesg.Text = "無COM連線";
                bt_awb_test.BackColor = Color.Red;
                flag_doing_awb = false;
                bt_awb_test.Enabled = true;
                playSound(S_FALSE);
                result = REASON_NO_COMPORT;
                return result;
            }

            if (flag_camera_use_insighteyes == 0)
            {
                //MessageBox.Show("No Insighteyes Camera", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //bt_awb_test.Text = "無IMS相機";
                tb_awb_mesg.Text = "無IMS相機";
                bt_awb_test.BackColor = Color.Red;
                flag_doing_awb = false;
                bt_awb_test.Enabled = true;
                playSound(S_FALSE);
                result = REASON_NO_IMS_CAMERA;
                return result;
            }

            /*
            //開始檢查相機連線
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
                tb_awb_mesg.Text = "無連接器";
                playSound(S_FALSE);
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_awb_mesg.Text = "有連接器, 無相機";
                playSound(S_FALSE);
            }
            else if (g_conn_status == CAMERA_OK)
            */
            {
                // Create stopwatch
                //Stopwatch stopwatch = new Stopwatch();
                stopwatch = new Stopwatch();
                // Begin timing
                stopwatch.Start();
                richTextBox1.Text += "\nAWB 開始 : 0 秒\n";
                Send_IMS_Data_cnt = 0;
                flag_awb_break = false;
                flag_awb_timeout = false;
                flag_awb_manually_interrupt = false;

                bt_awb_break.Visible = true;
                bt_awb_test.BackColor = Color.Pink;
                progressBar_awb.Value = 0;

                lb_awb_time.Text = "0";
                timer_awb_cnt = 0;
                timer_awb.Enabled = true;
                check_cnt_large = 0;    //粗調次數
                check_cnt_small = 0;    //細調次數

                if (cb_show_grid.Checked == true)
                {
                    cb_show_grid.Checked = false;
                    delay(10);
                }

                tb_awb_mesg.Text = "AWB 開始";
                tb_awb_mesg.Text = "有連接器, 有相機";
                playSound(S_OK);

                restore_camera_setup();

                timer_stage2.Enabled = true;
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode

                richTextBox1.Text += "量測亮度\n";
                measure_brightness_full();

                delay(20);

                /*
                //david debug
                flag_doing_awb = false;
                bt_awb_break.Visible = false;
                bt_awb_test.Enabled = true;
                bt_awb_test.BackColor = Color.Lime;
                return camera_status;
                */

                timer_stage2.Enabled = false;
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode

                if (cb_auto_search.Checked == true)
                {
                    //自動搜尋模式需要先歸零
                    flag_right_left_cnt = 0;
                    flag_down_up_cnt = 0;
                    flag_right_left_point_cnt = 0;
                    flag_down_up_point_cnt = 0;
                    awb_block = 32;
                    step = 1;
                    add_amount = 1;
                    add_tmp = 0;
                    //ww = awb_block;
                    //hh = awb_block;
                    refresh_picturebox2();
                    delay(100);
                }

                flag_do_find_awb_location_ok = false;
                if (cb_auto_search.Checked == true)
                {
                    bt_awb_test.BackColor = Color.Pink;
                    if (find_awb_location() == S_FALSE)
                    {
                        //check_awb_location();

                        /*
                        richTextBox1.Text += "打印搜尋結果2\n";
                        int w = 640;
                        int h = 480;
                        int x_st = 0;
                        int y_st = 0;
                        int ww = 0;
                        int hh = 0;
                        ww = awb_block;
                        hh = awb_block;
                        x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                        y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;


                        richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                            ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
                        richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
                        richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
                        richTextBox1.Text += "awb_block = " + awb_block.ToString() + ", awb_block = " + awb_block.ToString() + "\n";
                        if (ww < 20)
                        {
                            richTextBox1.Text += "找到的範圍太小\n";
                            richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
                            //return S_FALSE;
                        }
                        if ((Math.Abs(flag_down_up_point_cnt) > 70) || (Math.Abs(flag_right_left_point_cnt) > 70))
                        {
                            richTextBox1.Text += "找到的範圍太遙遠\n";
                            richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                                ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
                            //return S_FALSE;
                        }

                        tb_awb_mesg.Text = "尋找區域失敗";

                        bt_awb_break.Text = "確認";
                        //tb_awb_mesg.Text = "色彩校正中斷";
                        //richTextBox1.Text += "AWB 中斷 AWB 中斷 AWB 中斷\n";
                        flag_awb_break = true;
                        flag_do_find_awb_location_ok = true;
                        */

                        /*
                        bt_awb_test.BackColor = Color.Red;
                        bt_awb_test.Enabled = true;
                        bt_awb_break.Visible = false;
                        flag_doing_awb = false;
                        playSound(S_FALSE);
                        flag_do_find_awb_location_ok = true;
                        timer_stage2.Enabled = true;
                        */
                        result = S_FALSE;   //未知

                        if (flag_do_find_awb_location_fail_too_small == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_SMALL;
                        else if (flag_do_find_awb_location_fail_too_far == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_FAR;
                        else if (flag_break_doing_awb == true)
                            result = REASON_MANUALLY_INTERRUPT;
                        return result;
                    }

                    if (flag_break_doing_awb == true)
                    {
                        result = REASON_MANUALLY_INTERRUPT;
                        return result;
                    }

                    if (check_awb_location() == S_FALSE)
                    {
                        richTextBox1.Text += "check_awb_location() FAIL return 1\n";
                        // Stop timing
                        stopwatch.Stop();
                        timer_awb.Enabled = false;
                        bt_awb_break.Visible = true;
                        bt_awb_break.Text = "確認";

                        if (flag_do_find_awb_location_fail_too_small == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_SMALL;
                        else if (flag_do_find_awb_location_fail_too_far == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_FAR;

                        return result;
                    }
                    else
                        richTextBox1.Text += "check_awb_location() OK 1\n";
                }
                else    //manual search
                {
                    flag_do_find_awb_location_ok = true;
                    if (check_awb_location() == S_FALSE)
                    {
                        richTextBox1.Text += "check_awb_location() FAIL return 2\n";
                        // Stop timing
                        stopwatch.Stop();
                        timer_awb.Enabled = false;
                        bt_awb_break.Visible = true;
                        bt_awb_break.Text = "確認";
                        if (flag_do_find_awb_location_fail_too_small == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_SMALL;
                        else if (flag_do_find_awb_location_fail_too_far == true)
                            result = REASON_FIND_AWB_AREA_FAIL_TOO_FAR;
                        return result;
                    }
                    else
                        richTextBox1.Text += "check_awb_location() OK 2\n";
                }

                flag_do_find_awb_location_ok = true;

                /*
                //debug
                bt_awb_break.Text = "確認";
                tb_awb_mesg.Text = "色彩校正中斷";
                richTextBox1.Text += "AWB 中斷 AWB 中斷 AWB 中斷\n";
                flag_awb_break = true;
                */

                if (flag_auto_brightness_awb == true)
                {
                    tb_wpt.Text = "";
                    read_camera_sensor(SENSOR_WPT);
                    tb_bpt.Text = "";
                    read_camera_sensor(SENSOR_BPT);

                    richTextBox1.Text += "\nT(" + awb_cnt.ToString() + ")=" + awb_cnt.ToString() + ";" +
                        "WPT(" + awb_cnt.ToString() + ")=" + (20 + current_test_count * 5).ToString() + ";" +
                        "BPT(" + awb_cnt.ToString() + ")=" + (5 + current_test_count * 5).ToString() + ";" +
                        "\n";

                    flag_doing_awb = false;
                    bt_awb_break.Visible = false;
                    bt_awb_test.Enabled = true;
                    bt_awb_test.BackColor = Color.Lime;

                    return S_OK;
                }

                //check_awb_region();   //under test


                //bt_awb_test.Text = "清除相機資料";
                tb_awb_mesg.Text = "清除相機資料";
                //progressBar_awb.ForeColor = Color.Red;
                //progressBar_awb.BackColor = Color.Red;
                Send_IMS_Data(0xEE, 0xFF, 0xEE, 0xFF);   //erase all camera flash data

                if (cb_only_search.Checked == true)
                {
                    if (cb_auto_search.Checked == true)
                    {
                        progressBar_awb.Value = 5;
                        delay(10);

                        lb_rgb_r.Text = "";
                        lb_rgb_g.Text = "";
                        lb_rgb_b.Text = "";

                        timer_display.Enabled = true;
                        flag_do_awb = true;
                        //richTextBox1.Text += "AWB test ST write 0x3503 as 0x03\n";

                        // Stop timing
                        stopwatch.Stop();
                        timer_awb.Enabled = false;

                        // Write result

                        richTextBox1.Text += "AWB 完成\t總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                        //bt_awb_test.Text = "色彩校正完成";
                        tb_awb_mesg.Text = "色彩校正完成";
                        bt_awb_break.Visible = false;
                        bt_awb_test.BackColor = Color.Lime;
                        progressBar_awb.Value = 100;
                        //progressBar_awb.ForeColor = Color.Green;
                        //progressBar_awb.BackColor = Color.Green;
                        flag_do_awb = false;
                        timer_display.Enabled = false;
                        playSound(S_OK);

                        //for data analysis
                        richTextBox1.Text +=
                            "right_left_point_cnt[" + awb_cnt.ToString() + "]=" + flag_right_left_point_cnt.ToString() + ";" +
                            "down_up_point_cnt[" + awb_cnt.ToString() + "]=" + flag_down_up_point_cnt.ToString() + ";" +
                            "awb_block[" + awb_cnt.ToString() + "]=" + awb_block.ToString() + ";" +
                            "\t//for vcs1\n";
                        awb_cnt++;

                        flag_doing_awb = false;
                        bt_awb_test.Enabled = true;

                        /*
                        //debug picture
                        flag_stage_awb = 2;
                        save_image_to_local_drive();
                        */

                        //flag_doing_awb = false;
                        //bt_awb_test.Enabled = true;
                        timer_stage2.Enabled = true;

                        return S_OK;
                    }
                }

                progressBar_awb.Value = 5;
                delay(50);
                //bt_awb_test.Text = "色彩校正開始";
                tb_awb_mesg.Text = "色彩校正開始";
                progressBar_awb.Value = 10;
                delay(10);

                /*
                //debug picture
                flag_stage_awb = 0;
                save_image_to_local_drive();
                */

                lb_rgb_r.Text = "";
                lb_rgb_g.Text = "";
                lb_rgb_b.Text = "";
                //timer_stage2.Enabled = false;
                bt_awb.Text = "Auto";
                //richTextBox1.Text += "\nTo Auto mode\n";
                //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode

                timer_display.Enabled = true;
                flag_do_awb = true;
                //richTextBox1.Text += "AWB test ST write 0x3503 as 0x03\n";

                richTextBox1.Text += "檢查飽和 ST : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                //bt_awb_test.Text = "檢查飽和開始";
                tb_awb_mesg.Text = "檢查飽和開始";
                progressBar_awb.Value = 12;

                //no change gain.....
                //richTextBox1.Text += "setup gain to 0x7f = 127\n";
                //Send_IMS_Data(0xA0, 0x35, 0x0A, 0x00);
                //Send_IMS_Data(0xA0, 0x35, 0x0B, 0x7f);

                test_RGB_saturation();

                if (flag_break_doing_awb == true)
                {
                    result = REASON_MANUALLY_INTERRUPT;
                    return result;
                }

                int ret = 0;

                if (flag_awb_break == false)
                {
                    richTextBox1.Text += "檢查飽和 SP\t粗調 ST : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                    //bt_awb_test.Text = "檢查飽和結束";
                    tb_awb_mesg.Text = "檢查飽和結束";
                    progressBar_awb.Value = 30;
                    delay(50);
                    //bt_awb_test.Text = "粗調開始";
                    tb_awb_mesg.Text = "粗調開始";
                    progressBar_awb.Value = 32;

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

                    if (flag_awb_break == true)
                    {
                        if (flag_awb_timeout == true)
                            result = REASON_AWB_TIMEOUT;
                        else
                            result = REASON_MANUALLY_INTERRUPT;
                        return result;
                    }

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
                        //richTextBox1.Text += "AWB data R G B = " + data_R.ToString() + " " + data_G.ToString() + " " + data_B.ToString() + "\n";

                        check_RB_saturation();

                        for (i = 0; i < 50; i++)
                        {
                            richTextBox1.Text += "粗調c " + check_cnt_large.ToString() + ", t = " + stopwatch.Elapsed.TotalSeconds.ToString() + "\n";
                            if (stopwatch.Elapsed.TotalSeconds > awb_time_out)
                            {
                                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX 做太久, break 1\n";
                                flag_awb_break = true;
                                flag_awb_timeout = true;
                                break;
                            }

                            if (flag_awb_break == true)
                            {
                                richTextBox1.Text += "awb break 2\n";
                                break;
                            }
                            //richTextBox1.Text += "\ni = " + i.ToString() + "\t";
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
                                    richTextBox1.Text += "RGB皆符合, 完成a\n";
                                    break;
                                }
                            }
                            delay(10);
                            check_RB_saturation();
                            ret = check_RGB_value();
                            if (ret == S_OK)
                            {
                                richTextBox1.Text += "\nRGB皆符合, 完成b\n";
                                break;
                            }
                            check_RB_saturation();

                            ret = check_G_exposure(sender, e, total_RGB_G);

                            delay(10);
                            check_RB_saturation();
                            ret = check_RGB_value();
                            if (ret == S_OK)
                            {
                                richTextBox1.Text += "\nRGB皆符合, 完成c\n";
                                break;
                            }

                            if (progressBar_awb.Value < (52 - 2))
                                progressBar_awb.Value += 1;
                        }
                    }
                }

                if (flag_awb_break == false)
                {
                    //richTextBox1.Text += "AGC auto, EXPO auto\n";
                    //Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);    //To auto mode

                    //richTextBox1.Text += "Target  R G B = " + TARGET_AWB_R.ToString() + " " + TARGET_AWB_G.ToString() + " " + TARGET_AWB_B.ToString() + "\n";
                    //richTextBox1.Text += "Current R G B = " + (total_RGB_R / awb_block / awb_block).ToString() + " " + (total_RGB_G / awb_block / awb_block).ToString() + " " + (total_RGB_B / awb_block / awb_block).ToString() + "\n";

                    richTextBox1.Text += "粗調 SP\t細調 ST : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                    //bt_awb_test.Text = "粗調結束";
                    tb_awb_mesg.Text = "粗調結束";
                    progressBar_awb.Value = 52;
                    delay(50);
                    //bt_awb_test.Text = "細調開始";
                    tb_awb_mesg.Text = "細調開始";
                    progressBar_awb.Value = 56;

                    int ok_cnt = 0;
                    int check_cnt = 0;
                    while (true)
                    {
                        check_cnt_small++;
                        richTextBox1.Text += "細調 " + check_cnt_small.ToString() + ", t = " + stopwatch.Elapsed.TotalSeconds.ToString() + "\n";
                        if (stopwatch.Elapsed.TotalSeconds > awb_time_out)
                        {
                            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX 做太久, break 3\n";
                            flag_awb_break = true;
                            flag_awb_timeout = true;
                            break;
                        }

                        if (flag_awb_break == true)
                        {
                            richTextBox1.Text += "awb break 3\n";
                            break;
                        }
                        check_cnt++;
                        //richTextBox1.Text += "i = " + check_cnt.ToString() + "    ";
                        if (check_cnt < 5)
                            tolerance_ratio = 2;
                        else if (check_cnt < 10)
                            tolerance_ratio = 2;
                        else
                            tolerance_ratio = 1;
                        ret = awb_modify();

                        if (progressBar_awb.Value < (90 - 2))
                            progressBar_awb.Value += 1;

                        if (ret == S_OK)
                        {
                            ok_cnt++;
                            richTextBox1.Text += "S_OK " + ok_cnt.ToString() + " ";
                            if (ok_cnt == 3)
                                break;
                        }
                        else
                            ok_cnt = 0;
                    }
                    richTextBox1.Text += "\n細調 SP : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                    //bt_awb_test.Text = "細調結束";
                    tb_awb_mesg.Text = "細調結束";
                    progressBar_awb.Value = 90;

                    /*
                    //debug picture
                    save_image_to_local_drive();
                    */

                    delay(10);
                    progressBar_awb.Value = 95;
                    tolerance_ratio = 1;
                }

                //check_awb_region();

                //切換回自動模式
                bt_awb.Text = "Manual";
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode

                if ((flag_awb_break == false) && (flag_awb_save_data == true))
                {
                    tb_awb_mesg.Text = "寫資料進相機";
                    //do not write data to camera
                    //寫資料進相機裡
                    ret = get_r_data();
                    ret = get_b_data();

                    if (ret == S_FALSE)
                    {
                        ret = get_r_data();
                        ret = get_b_data();
                    }

                    //old method, write to AWB_PAGE0
                    //write_awb_data_to_camera(data_R, data_B);     old method

                    //new method, write to AWB_PAGE1
                    int page = AWB_PAGE1;

                    for (i = 0; i < 16; i++)
                    {
                        user_flash_data[i] = 0;
                    }

                    //ex: DA-52-1A-04-52-1B-D2-52-1E-07-52-1F-08-00-00-00

                    user_flash_data[0] = 0xDA;  //header

                    user_flash_data[1] = 0x52;  //AWB R H AH
                    user_flash_data[2] = 0x1A;  //AWB R H AL
                    user_flash_data[3] = (Byte)(data_R / 256);

                    user_flash_data[4] = 0x52;  //AWB R L AH
                    user_flash_data[5] = 0x1B;  //AWB R L AL
                    user_flash_data[6] = (Byte)(data_R % 256);

                    user_flash_data[7] = 0x52;  //AWB B H AH
                    user_flash_data[8] = 0x1E;  //AWB B H AL
                    user_flash_data[9] = (Byte)(data_B / 256);

                    user_flash_data[10] = 0x52; //AWB B L AH
                    user_flash_data[11] = 0x1F; //AWB B L AL
                    user_flash_data[12] = (Byte)(data_B % 256);

                    user_flash_data[13] = 0x00; //dummy, no data
                    user_flash_data[14] = 0x00; //dummy, no data
                    user_flash_data[15] = 0x00; //dummy, no data

                    Send_IMS_Data(0xD0, (byte)page, 0, 0);  //write user data to camera flash
                    serialPort1.Write(user_flash_data, 0, 16);
                    
                    do_save_camera_data();  //write saturation brightness data
                }

                // Stop timing
                stopwatch.Stop();
                timer_awb.Enabled = false;

                // Write result
                if (flag_awb_break == false)
                {
                    awb_time = stopwatch.Elapsed.TotalSeconds;
                    richTextBox1.Text += "AWB 完成\t總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                    richTextBox1.Text += "AWB 完成\t粗調 : " + check_cnt_large.ToString() + " 次\t細調 : " + check_cnt_small.ToString() + " 次\n";
                    richTextBox1.Text += "AWB 完成\t總命令個數 : " + Send_IMS_Data_cnt.ToString() + " 個\n";
                    //bt_awb_test.Text = "色彩校正完成";
                    tb_awb_mesg.Text = "色彩校正完成";
                    bt_awb_break.Visible = false;
                    bt_awb_test.BackColor = Color.Lime;
                    progressBar_awb.Value = 100;
                    //progressBar_awb.ForeColor = Color.Green;
                    //progressBar_awb.BackColor = Color.Green;
                    flag_do_awb = false;
                    timer_display.Enabled = false;
                    playSound(S_OK);

                    //for data analysis
                    awb_cnt++;
                    if (cb_auto_search.Checked == true)
                    {
                        richTextBox1.Text += "\nT(" + awb_cnt.ToString() + ")=" + awb_cnt.ToString() + ";" +
                            "awb_r(" + awb_cnt.ToString() + ")=" + data_R.ToString() + ";awb_b(" + awb_cnt.ToString() + ")=" + data_B.ToString() + ";" +
                            "t(" + awb_cnt.ToString() + ")=" + stopwatch.Elapsed.TotalSeconds.ToString() + ";" +
                            "right_left_point_cnt(" + awb_cnt.ToString() + ")=" + flag_right_left_point_cnt.ToString() + ";" +
                            "down_up_point_cnt(" + awb_cnt.ToString() + ")=" + flag_down_up_point_cnt.ToString() + ";" +
                            "awb_block(" + awb_cnt.ToString() + ")=" + awb_block.ToString() + ";" +
                            "cmd(" + awb_cnt.ToString() + ")=" + Send_IMS_Data_cnt.ToString() + ";" +
                            "\n";

                        int ww = awb_block;
                        int hh = awb_block;
                        richTextBox1.Text += "\nT(" + awb_cnt.ToString() + ")=" + awb_cnt.ToString() + ";" +
                            "total_RGB_R(" + awb_cnt.ToString() + ")=" + total_RGB_R.ToString() + ";RGB_R(" + awb_cnt.ToString() + ")=" + ((double)total_RGB_R / (ww * hh)).ToString() + ";" +
                            "total_RGB_G(" + awb_cnt.ToString() + ")=" + total_RGB_G.ToString() + ";RGB_G(" + awb_cnt.ToString() + ")=" + ((double)total_RGB_G / (ww * hh)).ToString() + ";" +
                            "total_RGB_B(" + awb_cnt.ToString() + ")=" + total_RGB_B.ToString() + ";RGB_B(" + awb_cnt.ToString() + ")=" + ((double)total_RGB_B / (ww * hh)).ToString() + ";" +
                            "\n";

                        awb_cnt--;
                        richTextBox1.Text +=
                            "awb_r[" + awb_cnt.ToString() + "]=" + data_R.ToString() + ";awb_b[" + awb_cnt.ToString() + "]=" + data_B.ToString() + ";" +
                            "right_left_point_cnt[" + awb_cnt.ToString() + "]=" + flag_right_left_point_cnt.ToString() + ";" +
                            "down_up_point_cnt[" + awb_cnt.ToString() + "]=" + flag_down_up_point_cnt.ToString() + ";" +
                            "awb_block[" + awb_cnt.ToString() + "]=" + awb_block.ToString() + ";" +
                            "\t//for vcs2\n";
                        awb_cnt++;
                    }
                    else
                    {
                        richTextBox1.Text += "\nT(" + awb_cnt.ToString() + ")=" + awb_cnt.ToString() + ";" +
                            "awb_r(" + awb_cnt.ToString() + ")=" + data_R.ToString() + ";awb_b(" + awb_cnt.ToString() + ")=" + data_B.ToString() + ";" +
                            "t(" + awb_cnt.ToString() + ")=" + stopwatch.Elapsed.TotalSeconds.ToString() + ";" +
                            "right_left(" + awb_cnt.ToString() + ")=" + flag_right_left_cnt.ToString() + ";" +
                            "down_up(" + awb_cnt.ToString() + ")=" + flag_down_up_cnt.ToString() + ";" +
                            "awb_block(" + awb_cnt.ToString() + ")=" + awb_block.ToString() + ";" +
                            "\n";
                    }

                    if (flag_auto_brightness_awb == true)
                    {
                        richTextBox1.Text += "\nT(" + awb_cnt.ToString() + ")=" + awb_cnt.ToString() + ";" +
                            "WPT(" + awb_cnt.ToString() + ")=" + (20 + current_test_count * 5).ToString() + ";" +
                            "BPT(" + awb_cnt.ToString() + ")=" + (5 + current_test_count * 5).ToString() + ";" +
                            "\n";
                    }

                    if (awb_cnt == 1)
                        richTextBox1.Text += "clear,clc,clf\t%RBD ring brightness data\n";
                    for (i = 0; i < brightness_data2.Length; i++)
                    {
                        richTextBox1.Text += "RBD(" + (i + 1).ToString() + ", " + awb_cnt.ToString() + ")=" + brightness_data2[i].ToString() + ";\n";
                    }
                    richTextBox1.Text += "plot(RBD(:," + awb_cnt.ToString() + "), \'r\');hold on\n";
                    
                    flag_doing_awb = false;
                    bt_awb_test.Enabled = true;

                    /*
                    //debug picture
                    flag_stage_awb = 2;
                    save_image_to_local_drive();
                    */
                    result = S_OK;
                }
                else
                {
                    richTextBox1.Text += "AWB 中斷\t總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                    //bt_awb_test.Text = "色彩校正中斷";
                    tb_awb_mesg.Text = "色彩校正中斷";

                    //bt_awb_break.Visible = false;
                    bt_awb_test.BackColor = Color.Red;
                    //progressBar_awb.Value = 100;
                    //progressBar_awb.ForeColor = Color.Green;
                    //progressBar_awb.BackColor = Color.Green;
                    //flag_do_awb = false;
                    //timer_display.Enabled = false;
                    playSound(S_OK);

                    //flag_awb_break = false;
                    //bt_awb_break.Visible = false;
                    bt_awb_break.Text = "確認";
                    if(flag_awb_timeout == true)
                        result = REASON_AWB_TIMEOUT;
                    else if (flag_awb_manually_interrupt == true)
                        result = REASON_MANUALLY_INTERRUPT;
                }
            }
            /*
            else
            {
                tb_awb_mesg.Text = "狀態不明i, status = " + g_conn_status.ToString();
            }
            */
            //flag_doing_awb = false;
            //bt_awb_test.Enabled = true;
            timer_stage2.Enabled = true;
            return result;
        }

        private void bt_awb_test_Click(object sender, EventArgs e)
        {
            int do_awb_result = do_awb(sender, e);
            check_awb_result(do_awb_result);
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

            //if ((check_cnt_large % 10) == 0)
            {
                //richTextBox1.Text += "粗調中 check_cnt_large = " + check_cnt_large.ToString() + "\n";
                //richTextBox1.Text += "粗調中, 時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
            }

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
                    check_cnt_large++;
                    richTextBox1.Text += "粗調a " + check_cnt_large.ToString() + ", t = " + stopwatch.Elapsed.TotalSeconds.ToString() + "\n";

                    if (stopwatch.Elapsed.TotalSeconds > awb_time_out)
                    {
                        richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX 做太久, break 1\n";
                        flag_awb_break = true;
                        flag_awb_timeout = true;
                        break;
                    }


                    if (flag_awb_break == true)
                    {
                        richTextBox1.Text += "awb break 4\n";
                        break;
                    }

                    //richTextBox1.Text += "call get_expo_data\t";
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
                        if (diff > 50)
                            diff = 50;

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
                    check_cnt_large++;
                    richTextBox1.Text += "粗調b " + check_cnt_large.ToString() + ", t = " + stopwatch.Elapsed.TotalSeconds.ToString() + "\n";

                    if (stopwatch.Elapsed.TotalSeconds > awb_time_out)
                    {
                        richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXX 做太久, break 2\n";
                        flag_awb_break = true;
                        break;
                    }

                    if (flag_awb_break == true)
                    {
                        richTextBox1.Text += "awb break 5\n";
                        break;
                    }

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
                        if (diff > 5)
                            diff = 5;

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
                diff_g = 0;
            //richTextBox1.Text += "G抵達目標 目前 " + (rgb_g / (awb_block * awb_block)).ToString() + " 目標 " + TARGET_AWB_G.ToString() + "\n\n";

            if (flag_awb_break == true)
                return S_FALSE;
            else
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
                    if ((SendData < 100) || (SendData > 4000))
                        return;

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
                    if ((SendData < 100) || (SendData > 4000))
                        return;

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
                    if ((SendData < 100) || (SendData > 4000))
                        return;

                    //richTextBox1.Text += "\n飽和 目前 data_R = " + data_R.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";
                    richTextBox1.Text += "R飽和 -99\t";

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
                    richTextBox1.Text += "G飽和 -10\t";

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
                            if ((SendData < 10) || (SendData > 1000))
                                return;

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
                    if ((SendData < 100) || (SendData > 4000))
                        return;

                    //richTextBox1.Text += "飽和 目前 data_B = " + data_B.ToString() + " 減一些 減成 " + SendData.ToString() + "\n";
                    richTextBox1.Text += "B飽和 -99\t";

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
                if (diff > 90)
                    diff = 90;

                diff_r = -diff;
                timer_display_r_count = 0;

                //richTextBox1.Text += "\ntotal_RGB_R = " + total_RGB_R.ToString() + ", TARGET_AWB_R = " + TARGET_AWB_R.ToString() + "\n";
                //richTextBox1.Text += "R太大 減低R_data, 目前data_R = " + data_R.ToString() + ", 減 " + diff.ToString() + "\n";
                richTextBox1.Text += "R-" + diff.ToString() + " ";

                int SendData = data_R - diff;
                if ((SendData < 100) || (SendData > 4000))
                    return;

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
                if (diff > 90)
                    diff = 90;

                diff_r = diff;
                timer_display_r_count = 0;

                //richTextBox1.Text += "\ntotal_RGB_R = " + total_RGB_R.ToString() + ", TARGET_AWB_R = " + TARGET_AWB_R.ToString() + "\n";
                //richTextBox1.Text += "R太小 增加R_data, 目前data_R = " + data_R.ToString() + ", 加 " + diff.ToString() + "\n";
                richTextBox1.Text += "R+" + diff.ToString() + " ";

                int SendData = data_R + diff;
                if ((SendData < 100) || (SendData > 4000))
                    return;

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
                if (diff > 90)
                    diff = 90;

                diff_b = -diff;
                timer_display_b_count = 0;

                //richTextBox1.Text += "B太大 減低B_data, 目前data_B = " + data_B.ToString() + ", 減 " + diff.ToString() + "\n";
                richTextBox1.Text += "B-" + diff.ToString() + " ";

                int SendData = data_B - diff;
                if ((SendData < 100) || (SendData > 4000))
                    return;

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
                if (diff > 90)
                    diff = 90;

                diff_b = diff;
                timer_display_b_count = 0;

                //richTextBox1.Text += "B太小 增加B_data, 目前data_B = " + data_B.ToString() + ", 加 " + diff.ToString() + "\n";
                richTextBox1.Text += "B+" + diff.ToString() + " ";

                int SendData = data_B + diff;
                if ((SendData < 100) || (SendData > 4000))
                    return;

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

            SendData = 127;

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
            richTextBox1.Text += "bt_goto_awb_Click ST\n";

            if (flag_comport_connection_ok == false)
            {
                richTextBox1.Text += "awb call connect_IMS_comport()\n";
                connect_IMS_comport();
            }

            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
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
                richTextBox1.Text += "1000K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 56;
                TARGET_AWB_B = 0;
            }
            else if (comboBox_temperature.SelectedIndex == 1)
            {
                richTextBox1.Text += "1400K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 101;
                TARGET_AWB_B = 0;
            }
            else if (comboBox_temperature.SelectedIndex == 2)
            {
                richTextBox1.Text += "1800K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 126;
                TARGET_AWB_B = 0;
            }
            else if (comboBox_temperature.SelectedIndex == 3)
            {
                richTextBox1.Text += "2200K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 147;
                TARGET_AWB_B = 44;
            }
            else if (comboBox_temperature.SelectedIndex == 4)
            {
                richTextBox1.Text += "2600K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 165;
                TARGET_AWB_B = 79;
            }
            else if (comboBox_temperature.SelectedIndex == 5)
            {
                richTextBox1.Text += "3000K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 180;
                TARGET_AWB_B = 107;
            }
            else if (comboBox_temperature.SelectedIndex == 6)
            {
                richTextBox1.Text += "3400K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 193;
                TARGET_AWB_B = 132;
            }
            else if (comboBox_temperature.SelectedIndex == 7)
            {
                richTextBox1.Text += "3800K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 204;
                TARGET_AWB_B = 153;
            }
            else if (comboBox_temperature.SelectedIndex == 8)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 213;
                TARGET_AWB_B = 173;
            }
            else if (comboBox_temperature.SelectedIndex == 9)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 221;
                TARGET_AWB_B = 190;
            }
            else if (comboBox_temperature.SelectedIndex == 10)
            {
                richTextBox1.Text += "5500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 236;
                TARGET_AWB_B = 224;
            }
            else if (comboBox_temperature.SelectedIndex == 11)
            {
                richTextBox1.Text += "5700K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 239;
                TARGET_AWB_B = 230;
            }
            else if (comboBox_temperature.SelectedIndex == 12)
            {
                richTextBox1.Text += "6500K\n";
                TARGET_AWB_R = 255;
                TARGET_AWB_G = 249;
                TARGET_AWB_B = 253;
            }
            else if (comboBox_temperature.SelectedIndex == 13)
            {
                richTextBox1.Text += "6700K\n";
                TARGET_AWB_R = 252;
                TARGET_AWB_G = 247;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 14)
            {
                richTextBox1.Text += "6900K\n";
                TARGET_AWB_R = 247;
                TARGET_AWB_G = 245;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 15)
            {
                richTextBox1.Text += "7100K\n";
                TARGET_AWB_R = 243;
                TARGET_AWB_G = 242;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 16)
            {
                richTextBox1.Text += "7300K\n";
                TARGET_AWB_R = 239;
                TARGET_AWB_G = 240;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 17)
            {
                richTextBox1.Text += "7500K\n";
                TARGET_AWB_R = 235;
                TARGET_AWB_G = 238;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 18)
            {
                richTextBox1.Text += "7700K\n";
                TARGET_AWB_R = 231;
                TARGET_AWB_G = 236;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 19)
            {
                richTextBox1.Text += "7900K\n";
                TARGET_AWB_R = 228;
                TARGET_AWB_G = 234;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 20)
            {
                richTextBox1.Text += "8100K\n";
                TARGET_AWB_R = 225;
                TARGET_AWB_G = 232;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 21)
            {
                richTextBox1.Text += "8300K\n";
                TARGET_AWB_R = 222;
                TARGET_AWB_G = 230;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 22)
            {
                richTextBox1.Text += "8500K\n";
                TARGET_AWB_R = 220;
                TARGET_AWB_G = 229;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 23)
            {
                richTextBox1.Text += "8700K\n";
                TARGET_AWB_R = 217;
                TARGET_AWB_G = 227;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 24)
            {
                richTextBox1.Text += "8900K\n";
                TARGET_AWB_R = 215;
                TARGET_AWB_G = 226;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 25)
            {
                richTextBox1.Text += "9100K\n";
                TARGET_AWB_R = 212;
                TARGET_AWB_G = 223;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 26)
            {
                richTextBox1.Text += "9300K\n";
                TARGET_AWB_R = 210;
                TARGET_AWB_G = 223;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 27)
            {
                richTextBox1.Text += "9500K\n";
                TARGET_AWB_R = 208;
                TARGET_AWB_G = 222;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 28)
            {
                richTextBox1.Text += "10000K\n";
                TARGET_AWB_R = 204;
                TARGET_AWB_G = 219;
                TARGET_AWB_B = 255;
            }
            else if (comboBox_temperature.SelectedIndex == 29)
            {
                richTextBox1.Text += "7700K modified\n";
                TARGET_AWB_R = 231;
                TARGET_AWB_G = 243;
                TARGET_AWB_B = 255;
            }
            else
                richTextBox1.Text += "XXXXXXXXXX\n";

            numericUpDown_TG_R.Value = TARGET_AWB_R;
            numericUpDown_TG_G.Value = TARGET_AWB_G;
            numericUpDown_TG_B.Value = TARGET_AWB_B;
            refresh_picturebox2();
            timer_stage2.Enabled = true;
        }

        void refresh_picturebox2()
        {
            if (flag_enaglb_awb_function == false)
                return;
            if (flag_usb_mode == true)
                return;

            int x_st = 0;
            int y_st = 0;
            int ww = awb_block;
            int hh = awb_block;

            int WW = 640 * 1;
            int HH = 480 * 1;

            x_st = WW / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > WW)
                x_st = WW - ww;

            y_st = HH / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > HH)
                y_st = HH - hh;

            if (flag_display_mode == DISPLAY_SD)
            {
                x_st = x_st * 11 / 10;
                y_st = y_st * 11 / 10;
                ww = ww * 11 / 10;
                hh = hh * 11 / 10;
                ww++;
                hh++;
            }
            else
            {
                x_st *= 2;
                y_st *= 2;
                ww *= 2;
                hh *= 2;
                ww++;
                hh++;
            }

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

            try
            {
                g = Graphics.FromImage(bmp);
                g.DrawRectangle(new Pen(Color.Silver, 2), 1, 1, ww - 2, hh - 2);    //draw boundary
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息r1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            try
            {
                pictureBox2.Image = bmp;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息r2 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }
            GC.Collect();       //回收資源
            return;
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

            //timer_webcam.Enabled = true;
            bt_awb.Text = "Manual";
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode
        }

        void to_awb_manual_mode()
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            //timer_webcam.Enabled = false;
            bt_awb.Text = "Auto";
            //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode
        }

        private void bt_disable_timer_webcam_Click(object sender, EventArgs e)
        {
            if (timer_stage2.Enabled == true)
            {
                richTextBox1.Text += "Disable Timer WebCam\n";
                timer_stage2.Enabled = false;
            }
            else
            {
                richTextBox1.Text += "Enable Timer WebCam\n";
                timer_stage2.Enabled = true;
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
            if (numericUpDown_wpt.Value > wpt_value_old)
            {
                if (numericUpDown_bpt.Value < 255)
                    numericUpDown_bpt.Value = numericUpDown_bpt.Value + 1;
            }
            else
            {
                if (numericUpDown_bpt.Value > 0)
                    numericUpDown_bpt.Value = numericUpDown_bpt.Value - 1;
            }

            wpt_value_old = numericUpDown_wpt.Value;
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
            int cnt = 0;
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
                cnt++;
                if (cnt > 10)
                    break;
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
                    if (data_new > 511)
                        data_new = 511;
                    else if (data_new < 0)
                        data_new = 0;
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
                    if (data_new > 4095)
                        data_new = 4095;
                    else if (data_new < 0)
                        data_new = 0;
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
                    if (data_new > 4095)
                        data_new = 4095;
                    else if (data_new < 0)
                        data_new = 0;
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
                //richTextBox1.Text += "\n";
                return S_FALSE;
            }
        }

        private void bt_awb_test2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Check 微調????????????????????????????????????\n";
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            lb_rgb_r.Text = "";
            lb_rgb_g.Text = "";
            lb_rgb_b.Text = "";
            timer_stage2.Enabled = false;
            bt_awb.Text = "Auto";
            //richTextBox1.Text += "\nTo Auto mode\n";
            //Send_IMS_Data(0xA0, 0x35, 0x03, 0x83);
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode

            timer_display.Enabled = true;
            flag_do_awb = true;

            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            richTextBox1.Text += "none\n";
            richTextBox1.Text += "\n微調 ST : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";

            int ret;
            int ok_cnt = 0;
            int check_cnt = 0;
            while (true)
            {
                check_cnt++;
                if (check_cnt < 10)
                    tolerance_ratio = 5;
                else if (check_cnt < 15)
                    tolerance_ratio = 3;
                else if (check_cnt < 20)
                    tolerance_ratio = 2;
                else
                    tolerance_ratio = 1;
                richTextBox1.Text += "i = " + check_cnt.ToString() + ", t = " + tolerance_ratio.ToString() + " ";
                ret = awb_modify();
                if (ret == S_OK)
                {
                    ok_cnt++;
                    richTextBox1.Text += "S_OK " + ok_cnt.ToString() + " ";
                    if (ok_cnt == 3)
                        break;
                }
                else
                    ok_cnt = 0;
            }
            richTextBox1.Text += "細調 SP : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
            tolerance_ratio = 1;


        }

        int precheck_RGB_saturation()
        {
            //richTextBox1.Text += "precheck RGB saturation ST\n";
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
            /*
            richTextBox1.Text += "none\n";
            //write_awb_data_to_camera(data_R, data_B);

            //check_webcam();

            //check_comport();
            richTextBox1.Text += "flag_camera_start = " + flag_camera_start.ToString() + "\n";
            richTextBox1.Text += "Cam.IsRunning = " + Cam.IsRunning.ToString() + "\n";

            if (Cam != null)
            {
                if ((flag_camera_start == 1) && (Cam.IsRunning == true))
                {
                    richTextBox1.Text += "USB影像傳輸中, 關閉\n";
                    flag_camera_start = 0;
                    Cam.Stop();  // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
                    comboBox_webcam.Items.Clear();
                }
            }
            */

            /*
            //設定相機亮度
            richTextBox1.Text += "設定相機亮度\n";

            byte SendData;

            SendData = 40;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(100);

            SendData = 25;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x04;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(100);
            */


            //check_awb_region();

            //find_brightness();

            //save_current_program_to_local_drive();

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_erase_Click(object sender, EventArgs e)
        {
            erase_camera_data();
        }

        bool flag_doing_check_webcam = false;
        int check_webcam()
        {
            int i;

            if ((flag_operation_mode != MODE_RELEASE_STAGE1A) && (flag_operation_mode != MODE_RELEASE_STAGE1B) && (flag_operation_mode != MODE_RELEASE_STAGE3))
            {
                if (flag_comport_ok == false)
                {
                    richTextBox1.Text += "no comport, abort\n";
                    return S_FALSE;
                }
            }

            if (flag_doing_check_webcam == false)
            {
                flag_doing_check_webcam = true;
            }
            else
            {
                richTextBox1.Text += "doing check_webcam, abort\n";
                return S_FALSE;
            }

            if (flag_enaglb_awb_function == true)
            {
                richTextBox1.Text += "call check_webcam ST, 檢查相機有無接上\n";
                g_conn_status = CAMERA_UNKNOWN;

                delay(1000);

                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料

                Send_IMS_Data(0xFF, 0, 0, 0);

                int cnt = 0;
                while ((g_conn_status == CAMERA_UNKNOWN) && (cnt++ < 60))
                {
                    richTextBox1.Text += "y";
                    delay(10);
                    if ((cnt % 40) == 39)
                    {
                        richTextBox1.Text += "無回應, 再發一次命令2\n";
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                        Send_IMS_Data(0xFF, 0, 0, 0);
                    }
                }
                richTextBox1.Text += "\ncnt = " + cnt.ToString() + "\n";    //usually cnt = 4
                richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";

                if (g_conn_status == DONGLE_NONE)
                {
                    richTextBox1.Text += "無連接器3\n";
                    flag_doing_check_webcam = false;
                    return S_FALSE;
                }
                else if (g_conn_status == CAMERA_NONE)
                {
                    richTextBox1.Text += "有連接器, 無相機\n";
                    flag_doing_check_webcam = false;
                    return S_FALSE;
                }
                else if (g_conn_status == CAMERA_OK)
                {
                    richTextBox1.Text += "有連接器, 有相機d\n";
                }
                else if (g_conn_status == CAMERA_SENSOR_FAIL)
                {
                    richTextBox1.Text += "有連接器, 有相機, 但是相機無法讀寫b\n";
                    tb_awb_mesg.Text = "相機無法讀寫";
                    bt_awb_test.BackColor = Color.Red;
                    flag_doing_awb = false;
                    bt_awb_test.Enabled = false;
                    playSound(S_FALSE);
                }
                else
                {
                    richTextBox1.Text += "狀態不明j, status = " + g_conn_status.ToString() + "\n";
                    flag_doing_check_webcam = false;
                    return S_FALSE;
                }
            }

            flag_camera_use_insighteyes = 0;
            comboBox_webcam.Items.Clear();
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            VideoCaptureDevice Cam_tmp = null;

            richTextBox1.Text += "check_webcam ST\n";

            //USBWebcams2 = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                if (USBWebcams.Count == 1)
                {
                    richTextBox1.Text += "There is " + USBWebcams.Count.ToString() + " camera\n";
                }
                else
                {
                    richTextBox1.Text += "There are " + USBWebcams.Count.ToString() + " cameras\n";
                }

                for (i = 0; i < USBWebcams.Count; i++)
                {
                    richTextBox1.Text += "camera " + i.ToString() + "\n";
                    richTextBox1.Text += "name : " + USBWebcams[i].Name + "\n";
                    richTextBox1.Text += "MonikerString: " + USBWebcams[i].MonikerString + "\n";

                    string webcam_name;
                    if (USBWebcams[i].Name.Contains("Virtual"))
                    {
                        richTextBox1.Text += "跳過 Virtual\n";
                        webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name;
                    }
                    else
                    {
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

                        webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name + " " + Cam_tmp.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam_tmp.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam_tmp.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                    }

                    comboBox_webcam.Items.Add(webcam_name);
                    richTextBox1.Text += webcam_name + "\n";
                }

                for (i = 0; i < USBWebcams.Count; i++)
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
                        flag_camera_use_insighteyes = 1;
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

                    //string webcam_name;
                    i = 0;
                    //webcam_name = (i + 1).ToString() + ". " + USBWebcams[i].Name + " " + Cam_tmp.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam_tmp.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam_tmp.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                    comboBox_webcam.Text = comboBox_webcam.Items[i].ToString();
                }
            }
            else
            {
                richTextBox1.Text += "無影像裝置\n";
                flag_doing_check_webcam = false;
                return S_FALSE;
            }
            flag_doing_check_webcam = false;
            return S_OK;
        }

        private void comboBox_webcam_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "你選取了" + comboBox_webcam.SelectedItem.ToString() + "\n";
            richTextBox1.Text += "SelectedIndex = " + comboBox_webcam.SelectedIndex.ToString() + "\n";

            if (Cam != null)
            {
                flag_camera_start = 0;
                Cam.Stop();  // WebCam stops capturing images.
                //Cam.SignalToStop();
                //Cam.WaitForStop();
                Cam = null;
            }

            Cam = new VideoCaptureDevice(USBWebcams[comboBox_webcam.SelectedIndex].MonikerString);
            Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
            Cam.Start();   // WebCam starts capturing images.
            flag_camera_start = 1;

        }

        void check_comport()
        {
            richTextBox1.Text += "check_comport ST\n";
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);

            richTextBox1.Text += "b共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string aaa in tempString)
            {
                richTextBox1.Text += "get comport : " + aaa + "\t";
            }
            richTextBox1.Text += "\n";

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

            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                    //lb_main_mesg2.Text = "";
                    lb_main_mesg3.Text = "";
                    lb_main_mesg12a.Text = "";
                }
                /*
                if (timer_display_show_main_mesg_count >= (timer_display_show_main_mesg_count_target * 2))
                {
                    //lb_main_mesg.Text = "";
                    lb_main_mesg2.Text = "";
                }
                */
            }
        }

        int try_connect_comport()
        {
            int ret = S_FALSE;
            //if (flag_comport_ok == true)  always close any comport
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button1.Enabled = true;
                button89.Enabled = true;
                button2.Enabled = false;
                button90.Enabled = false;
                flag_comport_ok = false;
            }

            comboBox1.Items.Clear();    //Clear All items in Combobox
            comboBox7.Items.Clear();    //Clear All items in Combobox
            richTextBox1.Text += "try_connect_comport ST\n";

            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "c共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox1.Items.Add(port);
                comboBox7.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length == 0)
            {
                richTextBox1.Text += "沒有comport\n";
                flag_comport_ok = false;
                return S_FALSE;
            }
            else if (COM_Ports_NameArr.Length == 1)
            {
                comboBox1.Text = COM_Ports_NameArr[0];
                comboBox7.Text = COM_Ports_NameArr[0];
            }
            else
            {
                comboBox1.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
                comboBox7.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }

            if (COM_Ports_NameArr.Length == 1)
            {
                richTextBox1.Text += "只有一個comport, try 一次\n";
                ret = connect_comport(comboBox1.Text);
            }
            else
            {
                richTextBox1.Text += "多個comport\n";

                int try_index;
                for (int i = 0; i < COM_Ports_NameArr.Length; i++)
                {
                    try_index = (i + COM_Ports_NameArr.Length - 2) % COM_Ports_NameArr.Length;  //從倒數第二個找起

                    //richTextBox1.Text += "try_index = " + try_index.ToString() + "\n";

                    comboBox1.Text = COM_Ports_NameArr[try_index];
                    comboBox7.Text = COM_Ports_NameArr[try_index];

                    serialPort1.Close();
                    this.BackColor = Color.Yellow;
                    button1.Enabled = true;
                    button89.Enabled = true;
                    button2.Enabled = false;
                    button90.Enabled = false;
                    flag_comport_ok = false;

                    ret = connect_comport(COM_Ports_NameArr[try_index]);
                    richTextBox1.Text += "\n";
                    if (ret == S_OK)
                    {
                        richTextBox1.Text += "找到可以連線到IMS EGD System的comport, 在 " + COM_Ports_NameArr[try_index] + "\n";
                        break;
                    }
                }
            }

            if (ret == S_OK)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                    serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                }
                return S_OK;
            }
            else
                return S_FALSE;
        }

        int connect_comport(string comport)
        {
            flag_comport_ok = false;
            serialPort1.PortName = comport;

            try
            {
                serialPort1.BaudRate = int.Parse(comboBox2.Text);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                //MessageBox.Show("無法連上Comport, 請重新連線");
                richTextBox1.Text += "無法連上 " + comport + ", 請重新連線";
                button1.Enabled = true;
                button89.Enabled = true;
                button2.Enabled = false;
                button90.Enabled = false;
                this.BackColor = Color.Pink;
                flag_comport_ok = false;
            }

            //serialPort1.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + comport + "\n";
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + comport + ", reason : " + ex.Message + "\n";
                //MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                {
                    serialPort1.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                    //MessageBox.Show("已經連上" + serialPort1.PortName);

                    flag_comport_ok = true;
                    flag_comport_connection_ok = false;

                    //計算serialPort1中有多少位元組 
                    BytesToRead = serialPort1.BytesToRead;

                    if (BytesToRead > 0)
                    {
                        //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }

                    delay(500);
                    Send_IMS_Data0(0xFF, 0x11, 0x52, 0x00); //directly send uart command

                    int cnt = 0;
                    while ((flag_comport_connection_ok == false) && (cnt++ < 20))
                    {
                        richTextBox1.Text += "x";
                        delay(10);
                        if ((cnt % 10) == 9)
                        {
                            richTextBox1.Text += "無回應, 再發一次命令1\n";
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                            Send_IMS_Data0(0xFF, 0x11, 0x52, 0x00); //directly send uart command
                        }
                    }
                    richTextBox1.Text += "\ncnt = " + cnt.ToString() + "\n";    //usually cnt = 4
                    richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";

                    flag_comport_ok = false;

                    if (flag_comport_connection_ok == true)
                    {
                        if (serialPort1.IsOpen)
                        {
                            button1.Enabled = false;
                            button89.Enabled = false;
                            button2.Enabled = true;
                            button90.Enabled = true;
                            this.BackColor = System.Drawing.SystemColors.ControlLight;
                            flag_comport_ok = true;
                        }
                        else
                        {
                            button1.Enabled = true;
                            button89.Enabled = true;
                            button2.Enabled = false;
                            button90.Enabled = false;
                            this.BackColor = Color.Pink;
                            flag_comport_ok = false;
                        }
                    }
                    else
                        flag_comport_ok = false;
                }
                else
                {
                    //MessageBox.Show("無法連上Comport, 請重新連線");
                    richTextBox1.Text += "無法連上 " + comport + ", 請重新連線";
                }
            }

            if(flag_comport_ok == true)
                return S_OK;
            else
                return S_FALSE;
        }

        private void cb_show_grid_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_show_grid.Checked == true)
            {
                rb_3X3.Visible = true;
                rb_4X4.Visible = true;
                rb_5X5.Visible = true;
                rb_NXN.Visible = true;
                groupBox_gridlinecolor.Visible = true;
            }
            else
            {
                rb_3X3.Visible = false;
                rb_4X4.Visible = false;
                rb_5X5.Visible = false;
                rb_NXN.Visible = false;
                groupBox_gridlinecolor.Visible = false;
            }
        }

        private void comboBox_temperature_DropDown(object sender, EventArgs e)
        {
            richTextBox1.Text += "DropDown\n";
            timer_stage2.Enabled = false;
        }

        private void comboBox_temperature_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e)
        {
            //richTextBox1.Text += "PreviewKeyDown\n";
        }

        private void bt_read_awb_Click(object sender, EventArgs e)
        {
            //old method get awb data
            lb_awb_data.Text = "讀取相機資料中...";
            byte page;
            int cnt = 0;

            richTextBox1.Text += "\n\nread camera awb data AWB_PAGE\n";
            page = AWB_PAGE0;
            Get_IMS_Data(1, page, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox1.Text += "a";
                delay(100);
            }
            flag_wait_receive_data = 0;

            //new method get awb data
            flag_read_camera_raw_data = 1;
            page = AWB_PAGE1;
            Send_IMS_Data(0xD1, (byte)page, 0, 0);
            return;
        }

        private void button43_Click(object sender, EventArgs e)
        {
            erase_camera_data();
        }

        Byte[] user_flash_data = new Byte[16];

        private void button27_Click(object sender, EventArgs e)
        {
            int page = Convert.ToInt32(textBox6.Text, 16);

            richTextBox1.Text += "位置 = " + page.ToString() + "\n";

            if ((page < MODEL_PAGE) || (page > (USER_PAGE1 + 100)))
            {
                richTextBox1.Text += "不支援的flash位址 0x%" + page.ToString("X2") + "=" + page.ToString() + ", abort\n";
                return;
            }

            //檢查資料
            int ret = check_write_data();

            if (ret == S_FALSE)
            {
                richTextBox1.Text += "檢查資料失敗, abort\n";
                return;
            }
            else
            {
                richTextBox1.Text += "檢查資料OK, continue\n";

            }

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
                lb_write_camera_serial2.Text = "有連接器, 有相機, 寫入相機資料中...";

                Send_IMS_Data(0xD0, (byte)page, 0, 0);  //write user data to camera flash

                serialPort1.Write(user_flash_data, 0, 16);


                richTextBox1.Text += "寫入資料  完成\n";

            }
            else
            {
                tb_sn1.Text = "狀態不明k, status = " + g_conn_status.ToString();
            }
        }

        private void button44_Click(object sender, EventArgs e)
        {
            textBox5.Text = "";
            data_00.Text = "00";
            data_01.Text = "00";
            data_02.Text = "00";
            data_03.Text = "00";
            data_04.Text = "00";
            data_05.Text = "00";
            data_06.Text = "00";
            data_07.Text = "00";
            data_08.Text = "00";
            data_09.Text = "00";
            data_10.Text = "00";
            data_11.Text = "00";
            data_12.Text = "00";
            data_13.Text = "00";
            data_14.Text = "00";
            data_15.Text = "00";
        }

        private void data_15_KeyPress(object sender, KeyPressEventArgs e)
        {
            e.Handled = check_textbox_hexadecimal(e);

        }


        int check_write_data()
        {
            int i;
            int data;

            for (i = 0; i < 16; i++)
            {
                user_flash_data[i] = 0;
            }

            data = Convert.ToInt32(data_00.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[0] = (Byte)data;
            }

            data = Convert.ToInt32(data_01.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[1] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_02.Text, 16);

            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[2] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_03.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[3] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_04.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[4] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_05.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[5] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_06.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[6] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_07.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[7] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_08.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[8] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_09.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[9] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_10.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[10] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_11.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[11] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_12.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[12] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_13.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[13] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_14.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[14] = (Byte)data;
            }
            
            data = Convert.ToInt32(data_15.Text, 16);
            if ((data < 0) || (data > 255))
            {
                return S_FALSE;
            }
            else
            {
                user_flash_data[15] = (Byte)data;
            }

            return S_OK;


        }

        private void button45_Click(object sender, EventArgs e)
        {
            int i;
            int page;
            int index;

            for (i = 0; i < 16; i++)
            {
                user_flash_data[i] = 0;
            }

            page = Convert.ToInt32(textBox1.Text, 16);
            if ((page < USER_PAGE1) || (page > (USER_PAGE1 + 10)))
            {
                richTextBox1.Text += "不支援的flash位址 0x%" + page.ToString("X2") + "=" + page.ToString() + ", abort\n";
                return;
            }
            richTextBox1.Text += "寫入頁位置 = " + page.ToString() + "\n";

            if ((rb_led_none.Checked == true) && (rb_meter_none.Checked == true) && (rb_brightness_none.Checked == true))
            {
                richTextBox1.Text += "無資料可寫\n";
                return;
            }

            index = 0;
            user_flash_data[0] = 0xDA;  //header

            if (rb_led_none.Checked == false)
            {
                if (rb_led_on.Checked == true)
                {
                    richTextBox1.Text += "LED ON\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x00;
                    user_flash_data[3 * index + 3] = 0x00;
                    index++;
                }
                else if (rb_led_off.Checked == true)
                {
                    richTextBox1.Text += "LED OFF\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x00;
                    user_flash_data[3 * index + 3] = 0x01;
                    index++;
                }
            }

            if (rb_meter_none.Checked == false)
            {
                if (rb_meter_cen.Checked == true)
                {
                    richTextBox1.Text += "Meter Center\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x01;
                    user_flash_data[3 * index + 3] = 0x00;
                    index++;
                }
                else if (rb_meter_avg.Checked == true)
                {
                    richTextBox1.Text += "Meter Average\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x01;
                    user_flash_data[3 * index + 3] = 0x01;
                    index++;
                }
                else if (rb_meter_auto.Checked == true)
                {
                    richTextBox1.Text += "Meter Auto\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x01;
                    user_flash_data[3 * index + 3] = 0x02;
                    index++;
                }
            }

            if (rb_brightness_none.Checked == false)
            {
                if (rb_brightness_1.Checked == true)
                {
                    richTextBox1.Text += "LED_1\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x02;
                    user_flash_data[3 * index + 3] = 0x01;
                    index++;
                }
                else if (rb_brightness_2.Checked == true)
                {
                    richTextBox1.Text += "LED_2\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x02;
                    user_flash_data[3 * index + 3] = 0x02;
                    index++;
                }
                else if (rb_brightness_3.Checked == true)
                {
                    richTextBox1.Text += "LED_3\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x02;
                    user_flash_data[3 * index + 3] = 0x03;
                    index++;
                }
                else if (rb_brightness_4.Checked == true)
                {
                    richTextBox1.Text += "LED_4\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x02;
                    user_flash_data[3 * index + 3] = 0x04;
                    index++;
                }
                else if (rb_brightness_5.Checked == true)
                {
                    richTextBox1.Text += "LED_5\n";
                    user_flash_data[3 * index + 1] = 0xFF;
                    user_flash_data[3 * index + 2] = 0x02;
                    user_flash_data[3 * index + 3] = 0x05;
                    index++;
                }
            }

            richTextBox1.Text += "Raw data : ";
            for (i = 0; i < 16; i++)
            {
                richTextBox1.Text += user_flash_data[i].ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
            richTextBox1.Text += "檢查資料OK, continue\n";

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
                lb_write_camera_serial2.Text = "有連接器, 有相機, 寫入相機資料中...";

                Send_IMS_Data(0xD0, (byte)page, 0, 0);  //write user data to camera flash

                serialPort1.Write(user_flash_data, 0, 16);
                richTextBox1.Text += "寫入資料  完成\n";
            }
            else
            {
                tb_sn1.Text = "狀態不明l, status = " + g_conn_status.ToString();
            }
        }

        private void cb_enable_awb_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_enable_awb.Checked == true)
            {
                flag_enaglb_awb_function = true;
                flag_fullscreen = false;
                button19_Click(sender, e);
                //cb_enable_awb.Location = new Point(11, 489 + 110);
            }
            else
            {
                flag_enaglb_awb_function = false;
                show_awb_item_visible(false);
            }
        }

        private void timer_awb_Tick(object sender, EventArgs e)
        {
            timer_awb_cnt++;
            lb_awb_time.Text = (timer_awb_cnt / 10).ToString() + "." + (timer_awb_cnt % 10).ToString();
        }

        void exportCSV()
        {
            if (camera_serials.Count > 0)
                richTextBox1.Text += "共有 " + camera_serials.Count.ToString() + " 筆資料要存\n";
            else
            {
                richTextBox1.Text += "無資料, 離開\n";
                show_main_message1("無資料", S_OK, 20);
                return;
            }

            String filename1 = string.Empty;
            String filename2 = string.Empty;

            if (flag_operation_mode == MODE_RELEASE_STAGE1A)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01a.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01a.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE1B)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01b.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01b.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01c.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_01c.csv";
            }
            else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_02.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_02.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_03.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_03.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE4)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_04.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_04.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE5)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_05.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_05.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE6)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_06.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_06.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE7)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_07.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_07.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE8)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_08.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_08.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE9)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_09.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_09.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE11)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_11.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_11.csv";
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE12)
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_12.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_12.csv";
            }
            else
            {
                filename1 = "N:\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_XX.csv";
                filename2 = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_00.csv";
            }

            if (check_network_disk() == S_FALSE)
            {
                richTextBox1.Text += "網路磁碟機不存在\n";
                return;
            }

            string content = "";
            StreamWriter sw;
            int i;

            if (File.Exists(filename1) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename1 + " 不存在\n";
                sw = new StreamWriter(File.Open(filename1, FileMode.Create), Encoding.Default);    //指名編碼格式

                if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
                {
                    content += "編號" + "," + "Opal序號" + "," + "存檔時間" + "," + "設備" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
                {
                    content += "編號" + "," + "Opal序號" + "," + "檢查1" + "," + "檢查2" + "," + "檢查3" + "," + "存檔時間" + "\n";
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    content += "編號" + "," + "Opal序號" + "," + "色彩校正結果" + "," + "時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    content += "編號" + "," + "Opal序號" + "," + "判定等級" + "," + "判定時間" + "," + "氣密NG" + "," + "改判" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE4)
                {
                    content += "編號" + "," + "Opal序號" + "," + "廠內生產製令序號" + "," + "燒錄時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE5)
                {
                    content += "No." + "," + "ERP-SN" + "," + "PI-SN" + "," + "BOX-Lot" + "," + "Date" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                {
                    content += "No." + "," + "主機序號" + "," + "小PCBA序號" + "," + "大PCBA序號" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                {
                    content += "No." + "," + "Dongle包裝" + "," + "Dongle序號" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                {
                    content += "No." + "," + "成品包裝序號" + "," + "主機序號" + "," + "Dongle包裝" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE9)
                {
                    content += "No." + "," + "箱號或序號" + "," + "單別" + "," + "單號" + "," + "時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE11)
                {
                    content += "No." + "," + "序號" + "," + "單別" + "," + "單號" + "," + "時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    content += "No." + "," + "序號" + "," + "COSMO資料" + "," + "檢查1" + "," + "檢查2" + "," + "檢查3" + "," + "時間" + "\n";
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx\n";
                    content += "編號" + "," + "Opal序號" + "," + "存檔時間" + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename1 + " 已存在\n";
                try
                {
                    sw = new StreamWriter(File.Open(filename1, FileMode.Append), Encoding.Default);    //指名編碼格式
                }
                    /*
                catch (IOException exception)
                {
                    var errorCode = Marshal.GetHRForException(exception) & 65535;
                    richTextBox1.Text += "xxxerrorCode   : " + errorCode.ToString() + "\n";
                    return;
                    //return errorCode == 32 || errorCode == 33;
                }
                     */
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息p : " + ex.ToString() + "\n";
                    richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\n";
                    show_main_message1("CSV檔使用中, 未儲存1", S_OK, 50);
                    show_main_message3("匯出CSV檔失敗", S_OK, 50);
                    return;
                }
            }

            for (i = 0; i < camera_serials.Count; i++)
            {
                //richTextBox1.Text += "camera_serials[" + i.ToString() + "][0] = " + camera_serials[i][0].ToString() + " camera_serials[" + i.ToString() + "][1] = " + camera_serials[i][1].ToString() + "\n";
                if (flag_operation_mode == MODE_RELEASE_STAGE1A)
                {
                    csv_index1++;
                    if (cb_stage1_ng.Checked == true)
                    {
                        if (stage1_ng_reason == 10)
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1,NG," + ng_reason[stage1_ng_reason] + tb_reason_stage1.Text;
                        else
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1,NG," + ng_reason[stage1_ng_reason];
                    }
                    else
                    {
                        content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1";
                    }
                    csv_index1 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1B)
                {
                    csv_index1++;
                    if (cb_stage1_ng.Checked == true)
                    {
                        if (stage1_ng_reason == 10)
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2,NG," + ng_reason[stage1_ng_reason] + tb_reason_stage1.Text;
                        else
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2,NG," + ng_reason[stage1_ng_reason];
                    }
                    else
                    {
                        content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2";
                    }
                    csv_index1 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
                {
                    csv_index1++;
                    content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ","
                        + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + "," + camera_serials[i][4].ToString();
                    csv_index1 -= camera_serials.Count;
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    csv_index2++;
                    content += csv_index2.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                    csv_index2 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    csv_index3++;
                    //cb_change_rank
                    /*
                    if(cb_air_ng.Checked == true)
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",1";
                    else
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                    */
                    if ((cb_air_ng.Checked == true) && (cb_change_rank.Checked == true))
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",1,1";
                    else if ((cb_air_ng.Checked == true) && (cb_change_rank.Checked == false))
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",1";
                    else if ((cb_air_ng.Checked == false) && (cb_change_rank.Checked == true))
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",,1";
                    else
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();

                    csv_index3 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE4)
                {
                    csv_index4++;
                    content += csv_index4.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                    csv_index4 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE5)
                {
                    csv_index5++;
                    content += csv_index5.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                    csv_index5 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                {
                    csv_index6++;
                    content += csv_index6.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                    csv_index6 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                {
                    csv_index7++;
                    content += csv_index7.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                    csv_index7 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                {
                    csv_index8++;
                    content += csv_index8.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                    csv_index8 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE9)
                {
                    csv_index9++;
                    if (flag_cancel_data == true)
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",取消";
                    else
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                    csv_index9 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE11)
                {
                    csv_index9++;
                    if (flag_cancel_data == true)
                    {
                        //content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG";
                        if (flag_ng_reason1 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,線材破損";
                        else if (flag_ng_reason2 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,Connector接觸不良";
                        else if (flag_ng_reason3 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,其他：" + tb_reason.Text;
                        else
                            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n";
                    }
                    else
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                    csv_index9 -= camera_serials.Count;
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    csv_index12++;
                    content += csv_index12.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ","
                        + camera_serials[i][3].ToString() + "," + camera_serials[i][4].ToString() + "," + camera_serials[i][5].ToString();
                    csv_index12 -= camera_serials.Count;
                }
                else
                {
                    csv_index1++;
                    content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString();
                    csv_index1 -= camera_serials.Count;
                }

                if ((camera_serials.Count > 1) && (i < (camera_serials.Count - 1)))
                {
                    content += "\n";
                }
            }
            sw.WriteLine(content);
            sw.Close();

            content = "";

            if (File.Exists(filename2) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename2 + " 不存在\n";
                sw = new StreamWriter(File.Open(filename2, FileMode.Create), Encoding.Default);    //指名編碼格式

                if ((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B))
                {
                    content += "編號" + "," + "Opal序號" + "," + "存檔時間" + "," + "設備" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
                {
                    content += "編號" + "," + "Opal序號" + "," + "檢查1" + "," + "檢查2" + "," + "檢查3" + "," + "存檔時間" + "\n";
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    content += "編號" + "," + "Opal序號" + "," + "色彩校正結果" + "," + "時間" + "," + "R" + "," + "B" + "," + "時間" + ",Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    content += "編號" + "," + "Opal序號" + "," + "判定等級" + "," + "判定時間" + "," + "氣密NG" + "," + "改判" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE4)
                {
                    content += "編號" + "," + "Opal序號" + "," + "廠內生產製令序號" + "," + "燒錄時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE5)
                {
                    content += "No." + "," + "ERP-SN" + "," + "PI-SN" + "," + "BOX-Lot" + "," + "Date" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                {
                    content += "No." + "," + "主機序號" + "," + "小PCBA序號" + "," + "大PCBA序號" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                {
                    content += "No." + "," + "Dongle包裝" + "," + "Dongle序號" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                {
                    content += "No." + "," + "成品包裝序號" + "," + "主機序號" + "," + "Dongle包裝" + "," + "生產時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE9)
                {
                    content += "No." + "," + "箱號或序號" + "," + "單別" + "," + "單號" + "," + "時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE11)
                {
                    content += "No." + "," + "序號" + "," + "單別" + "," + "單號" + "," + "時間" + "\n";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    content += "No." + "," + "序號" + "," + "COSMO資料" + "," + "檢查1" + "," + "檢查2" + "," + "檢查3" + "," + "時間" + "\n";
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n";
                    content += "編號" + "," + "Opal序號" + "," + "存檔時間" + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename2 + " 已存在\n";
                try
                {
                    sw = new StreamWriter(File.Open(filename2, FileMode.Append), Encoding.Default);    //指名編碼格式
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息r : " + ex.Message + "\n";
                    show_main_message1("CSV檔使用中, 未儲存2", S_OK, 50);
                    show_main_message3("匯出CSV檔失敗", S_OK, 50);
                    return;
                }
            }

            for (i = 0; i < camera_serials.Count; i++)
            {
                //richTextBox1.Text += "camera_serials[" + i.ToString() + "][0] = " + camera_serials[i][0].ToString() + " camera_serials[" + i.ToString() + "][1] = " + camera_serials[i][1].ToString() + "\n";
                if (flag_operation_mode == MODE_RELEASE_STAGE1A)
                {
                    csv_index1++;
                    if (cb_stage1_ng.Checked == true)
                    {
                        if (stage1_ng_reason == 10)
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1,NG," + ng_reason[stage1_ng_reason] + tb_reason_stage1.Text;
                        else
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1,NG," + ng_reason[stage1_ng_reason];
                    }
                    else
                    {
                        content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",1";
                    }
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1B)
                {
                    csv_index1++;
                    if (cb_stage1_ng.Checked == true)
                    {
                        if (stage1_ng_reason == 10)
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2,NG," + ng_reason[stage1_ng_reason] + tb_reason_stage1.Text;
                        else
                            content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2,NG," + ng_reason[stage1_ng_reason];
                    }
                    else
                    {
                        content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ",2";
                    }
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1C)
                {
                    csv_index1++;
                    content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + ","
                        + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + "," + camera_serials[i][4].ToString();
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    richTextBox1.Text += "R = " + data_R.ToString() + ", B = " + data_B.ToString() + ", T = " + awb_time.ToString() + "\n";
                    csv_index2++;
                    content += csv_index2.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + data_R.ToString() + "," + data_B.ToString() + "," + awb_time.ToString()
                        + "," + brightness_data2[0].ToString() + "," + brightness_data2[1].ToString() + "," + brightness_data2[2].ToString() + "," + brightness_data2[3].ToString()
                        + "," + brightness_data2[4].ToString() + "," + brightness_data2[5].ToString() + "," + brightness_data2[6].ToString() + "," + brightness_data2[7].ToString()
                        + "," + brightness_data2[8].ToString() + "," + brightness_data2[9].ToString() + "," + brightness_data2[10].ToString();
                    for (i = 0; i < brightness_data2.Length; i++)
                    {
                        brightness_data2[i] = -1;
                    }
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    csv_index3++;
                    if ((cb_air_ng.Checked == true) && (cb_change_rank.Checked == true))
                    {
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",1,1";
                        cb_air_ng.Checked = false;
                        cb_change_rank.Checked = false;
                    }
                    else if ((cb_air_ng.Checked == true) && (cb_change_rank.Checked == false))
                    {
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",1";
                        cb_air_ng.Checked = false;
                    }
                    else if ((cb_air_ng.Checked == false) && (cb_change_rank.Checked == true))
                    {
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ",,1";
                        cb_change_rank.Checked = false;
                    }
                    else
                        content += csv_index3.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE4)
                {
                    csv_index4++;
                    content += csv_index4.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE5)
                {
                    csv_index5++;
                    content += csv_index5.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                {
                    csv_index6++;
                    content += csv_index6.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                {
                    csv_index7++;
                    content += csv_index7.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                {
                    csv_index8++;
                    content += csv_index8.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE9)
                {
                    csv_index9++;
                    if (flag_cancel_data == true)
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",取消";
                    else
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE11)
                {
                    csv_index9++;
                    if (flag_cancel_data == true)
                    {
                        //content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG";
                        if (flag_ng_reason1 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,線材破損";
                        else if (flag_ng_reason2 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,Connector接觸不良";
                        else if (flag_ng_reason3 == true)
                            content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString() + ",NG,其他：" + tb_reason.Text;
                        else
                            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx\n";
                    }
                    else
                        content += csv_index9.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + "," + camera_serials[i][3].ToString();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    csv_index12++;
                    content += csv_index12.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString() + ","
                        + camera_serials[i][3].ToString() + "," + camera_serials[i][4].ToString() + "," + camera_serials[i][5].ToString();
                }
                else
                {
                    csv_index1++;
                    content += csv_index1.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString();
                }
                if ((camera_serials.Count > 1) && (i < (camera_serials.Count - 1)))
                {
                    content += "\n";
                }
            }
            sw.WriteLine(content);
            sw.Close();

            richTextBox1.Text += "存檔檔名: " + filename1 + "\n";
            richTextBox1.Text += "存檔檔名: " + filename2 + "\n";
            show_main_message1("已存檔CSV", S_OK, 20);
            show_main_message3("已存檔CSV", S_OK, 20);
            camera_serials.Clear();
        }

        /*
        void exportCSV3()
        {
            if (camera_serials.Count > 0)
                richTextBox1.Text += "共有 " + camera_serials.Count.ToString() + " 筆資料要存\n";
            else
            {
                richTextBox1.Text += "無資料, 離開\n";
                show_main_message1("無資料", S_OK, 20);
                return;
            }

            string filename = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_03.csv";

            string content = "";
            StreamWriter sw;

            if (File.Exists(filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.Default);    //指名編碼格式
                content += "編號" + "," + "Opal序號" + "," + "判定等級" + "," + "判定時間" + "\n";
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 已存在\n";
                try
                {
                    sw = new StreamWriter(File.Open(filename, FileMode.Append), Encoding.Default);    //指名編碼格式
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                    show_main_message1("CSV檔使用中, 未儲存", S_OK, 50);
                    show_main_message3("匯出CSV檔失敗", S_OK, 50);
                    return;
                }
            }

            int i;
            for (i = 0; i < camera_serials.Count; i++)
            {
                //richTextBox1.Text += "camera_serials[" + i.ToString() + "][0] = " + camera_serials[i][0].ToString() + " camera_serials[" + i.ToString() + "][1] = " + camera_serials[i][1].ToString() + "\n";
                csv_index++;
                //if (csv_index == 1)
                  //  content += "\n";
                content += csv_index.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                if ((camera_serials.Count > 1) && (i < (camera_serials.Count - 1)))
                {
                    content += "\n";
                }
            }

            sw.WriteLine(content);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            show_main_message1("已存檔CSV", S_OK, 20);
            show_main_message3("已存檔CSV", S_OK, 20);
            camera_serials.Clear();
        }

        void exportCSV4()
        {
            if (camera_serials.Count > 0)
                richTextBox1.Text += "共有 " + camera_serials.Count.ToString() + " 筆資料要存\n";
            else
            {
                richTextBox1.Text += "無資料, 離開\n";
                show_main_message1("無資料", S_OK, 20);
                return;
            }

            string filename = Application.StartupPath + "\\ims_" + DateTime.Now.ToString("yyyyMMdd") + "_04.csv";

            string content = "";
            StreamWriter sw;

            if (File.Exists(filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.Default);    //指名編碼格式
                content += "編號" + "," + "Opal序號" + "," + "廠內生產製令序號" + "," + "燒錄時間" + "\n";
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 已存在\n";
                try
                {
                    sw = new StreamWriter(File.Open(filename, FileMode.Append), Encoding.Default);    //指名編碼格式
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                    show_main_message1("CSV檔使用中, 未儲存", S_OK, 50);
                    show_main_message3("匯出CSV檔失敗", S_OK, 50);
                    return;
                }
            }

            int i;
            for (i = 0; i < camera_serials.Count; i++)
            {
                //richTextBox1.Text += "camera_serials[" + i.ToString() + "][0] = " + camera_serials[i][0].ToString() + " camera_serials[" + i.ToString() + "][1] = " + camera_serials[i][1].ToString() + "\n";
                csv_index++;
                //if (csv_index == 1)
                    //content += "\n";
                content += csv_index.ToString() + "," + camera_serials[i][0].ToString() + "," + camera_serials[i][1].ToString() + "," + camera_serials[i][2].ToString();
                if ((camera_serials.Count > 1) && (i < (camera_serials.Count - 1)))
                {
                    content += "\n";
                }
            }

            sw.WriteLine(content);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            show_main_message1("已存檔CSV", S_OK, 20);
            show_main_message3("已存檔CSV", S_OK, 20);
            camera_serials.Clear();
        }
        */

        void playSound(int number)
        {
            //播放系統預設的音效
            switch (number)
            {
                case S_OK:
                    System.Media.SystemSounds.Hand.Play();
                    break;
                case S_FALSE:
                    System.Media.SystemSounds.Beep.Play();
                    break;
                case 2:
                    System.Media.SystemSounds.Asterisk.Play();
                    break;
                case 3:
                    System.Media.SystemSounds.Exclamation.Play();
                    break;
                case 4:
                    System.Media.SystemSounds.Question.Play();
                    break;
                default:
                    System.Media.SystemSounds.Beep.Play();
                    break;
            }
        }

        void connect_IMS_comport()
        {
            int ret;
            ret = try_connect_comport();
            if (ret == S_OK)
            {
                richTextBox1.Text += "已連上IMS EGD System\n";
                show_main_message1("COM已連線", S_OK, 30);
                pictureBox_comport.Image = imsLink.Properties.Resources.comport;
                toolTip1.SetToolTip(pictureBox_comport, "COM已連線");

                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                    serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                }
            }
            else
            {
                richTextBox1.Text += "COM未連線\n";
                this.BackColor = Color.Pink;
                show_main_message1("COM未連線", S_FALSE, 100);
                pictureBox_comport.Image = imsLink.Properties.Resources.x;
                toolTip1.SetToolTip(pictureBox_comport, "COM未連線");
                
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button1.Enabled = true;
                button89.Enabled = true;
                button2.Enabled = false;
                button90.Enabled = false;
                flag_comport_ok = false;
            }
        }

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message2(string mesg, int number, int timeout)
        {
            lb_main_mesg2.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message3(string mesg, int number, int timeout)
        {
            lb_main_mesg3.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message12(string mesg, int number, int timeout)
        {
            lb_main_mesg12a.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        bool flag_script_data_on = false;
        private void bt_script_Click(object sender, EventArgs e)
        {
            if (flag_script_data_on == false)
            {
                flag_script_data_on = true;
                richTextBox2.Visible = true;
                bt_script_save.Visible = true;
                bt_script_cancel.Visible = true;
                bt_cancel.Visible = true;
                bt_script.Text = "Apply";

                int x_st;
                int y_st;
                if (flag_display_mode == DISPLAY_SD)
                {
                    x_st = 550 + 50;
                    y_st = 540;
                    richTextBox2.Location = new Point(x_st, y_st);
                    richTextBox2.Size = new System.Drawing.Size(340, 120);
                }
                else
                {
                    x_st = 191;
                    y_st = 489 + 98 + 20;
                    richTextBox2.Location = new Point(x_st, y_st);
                    richTextBox2.Size = new System.Drawing.Size(400, 300);
                    bt_script_save.Location = new Point(x_st + 318, y_st + 2);
                    bt_script_cancel.Location = new Point(x_st + 318, y_st + 2 + 32);
                }

            }
            else
            {
                flag_script_data_on = false;
                richTextBox2.Visible = false;
                bt_script_save.Visible = false;
                bt_script_cancel.Visible = false;
                bt_cancel.Visible = false;
                bt_script.Text = "Script";
                bt_script_load.Visible = true;

                if (flag_comport_ok == false)
                {
                    MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
                parse_script_command_and_send();
            }
        }

        private void bt_cancel_Click(object sender, EventArgs e)
        {
            flag_script_data_on = false;
            richTextBox2.Visible = false;
            bt_script_save.Visible = false;
            bt_script_cancel.Visible = false;
            bt_cancel.Visible = false;
            bt_script_load.Visible = true;
            bt_script.Text = "Script";
        }

        void parse_script_command_and_send()
        {
            richTextBox1.Text += "parse_script_command_and_send\trtb lines = " + richTextBox2.Lines.Length.ToString() + "\t";
            richTextBox1.Text += "content : \n";// +richTextBox2.Lines.Length.ToString();
            int i;
            for (i = 0; i < richTextBox2.Lines.Length; i++)
            {
                if (richTextBox2.Lines[i].Trim().Length == 7)
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + richTextBox2.Lines[i].Trim() + "\tlen = \t" + richTextBox2.Lines[i].Trim().Length.ToString() + "\n";

                    int addr_h = Convert.ToInt32(richTextBox2.Lines[i].Trim().Substring(0, 2), 16);
                    int addr_l = Convert.ToInt32(richTextBox2.Lines[i].Trim().Substring(2, 2), 16);
                    int data = Convert.ToInt32(richTextBox2.Lines[i].Trim().Substring(5, 2), 16);

                    richTextBox1.Text += " addr = " + addr_h.ToString("X2") + addr_l.ToString("X2") + " data = " + data.ToString("X2") + "\n";

                    DongleAddr_h = (byte)addr_h;
                    DongleAddr_l = (byte)addr_l;
                    DongleData = (byte)data;

                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
                    delay(20);

                    g_data_new[0] = 0x00;
                    if (cb_Gamma.Checked == true)
                    {
                        if ((DongleAddr_h == 0x53) && (DongleAddr_l == 0x01))
                        {
                            //setup avg_sel as Input data from GAMMA module
                            DongleAddr_h = 0x50;
                            DongleAddr_l = 0x02;
                            DongleData = 0x88;

                            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
                        }

                        if (DongleAddr_h == 0x53)
                        {
                            if ((DongleAddr_l > 0) && (DongleAddr_l < 0x10))
                            {
                                g_data_new[DongleAddr_l] = DongleData;
                            }
                        }
                    }
                }
            }
        }

        private void bt_script_file_Click(object sender, EventArgs e)
        {
            bt_script_load.Text = "Open";
            bt_cancel_Click(sender, e);

            openFileDialog1.Title = "把Script寫進檔案";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "文字檔|*.txt|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                //richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                flag_script_data_on = true;
                richTextBox2.Visible = true;
                bt_script_save.Visible = true;
                bt_script_cancel.Visible = true;
                bt_cancel.Visible = true;
                bt_script.Text = "Apply";

                int x_st;
                int y_st;
                if (flag_display_mode == DISPLAY_SD)
                {
                    x_st = 550 + 50;
                    y_st = 540;
                    richTextBox2.Location = new Point(x_st, y_st);
                    richTextBox2.Size = new System.Drawing.Size(340, 120);
                }
                else
                {
                    x_st = 191;
                    y_st = 489 + 98 + 20;
                    richTextBox2.Location = new Point(x_st, y_st);
                    richTextBox2.Size = new System.Drawing.Size(400, 300);
                    bt_script_save.Location = new Point(x_st + 318, y_st + 2);
                    bt_script_cancel.Location = new Point(x_st + 318, y_st + 2 + 32);
                }
                richTextBox2.Clear();

                //StreamReader sr = new StreamReader(openFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);
                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox2.Text += sr.ReadToEnd();	//讀取所有文字內容
                sr.Close();

                bt_script_load.Visible = false;
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
            bt_script_load.Text = "Load";
        }

        private void bt_script_save_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Title = "把Script寫進檔案";
            saveFileDialog1.FileName = "";
            saveFileDialog1.Filter = "文字檔|*.txt|所有檔|*.*";   //限定檔案格式
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + saveFileDialog1.FileName + "\n";
                //richTextBox1.Text += "length : " + saveFileDialog1.FileName.Length.ToString() + "\n";

                //StreamReader sr = new StreamReader(saveFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                FileStream filestream = File.Open(saveFileDialog1.FileName, FileMode.Create);
                StreamWriter str_writer = new StreamWriter(filestream);

                str_writer.WriteLine(richTextBox2.Text);
                // Dispose StreamWriter
                str_writer.Dispose();
                // Close FileStream
                filestream.Close();

                richTextBox1.Text += "儲存資料完畢111，檔案：" + saveFileDialog1.FileName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }
        }

        private void sensor_data_bit_change(object sender, EventArgs e)
        {
            //richTextBox1.Text += "sensor_data_bit_change\n";
            int value = 0;
            if (b7.Checked == true)
                value |= (1 << 7);
            if (b6.Checked == true)
                value |= (1 << 6);
            if (b5.Checked == true)
                value |= (1 << 5);
            if (b4.Checked == true)
                value |= (1 << 4);
            if (b3.Checked == true)
                value |= (1 << 3);
            if (b2.Checked == true)
                value |= (1 << 2);
            if (b1.Checked == true)
                value |= (1 << 1);
            if (b0.Checked == true)
                value |= (1 << 0);
            //richTextBox1.Text += "value = 0x " + value.ToString("X2") + " = " + value.ToString() + "\n";
            tb_3a.Text = value.ToString("X2");
            tb_4a.Text = value.ToString();
        }

        void show_hex2bit(int value)
        {
            //richTextBox1.Text += "show_hex2bit\n";
            if (((value >> 7) & 0x01) == 0x01)
                b7.Checked = true;
            else
                b7.Checked = false;
            if (((value >> 6) & 0x01) == 0x01)
                b6.Checked = true;
            else
                b6.Checked = false;
            if (((value >> 5) & 0x01) == 0x01)
                b5.Checked = true;
            else
                b5.Checked = false;
            if (((value >> 4) & 0x01) == 0x01)
                b4.Checked = true;
            else
                b4.Checked = false;
            if (((value >> 3) & 0x01) == 0x01)
                b3.Checked = true;
            else
                b3.Checked = false;
            if (((value >> 2) & 0x01) == 0x01)
                b2.Checked = true;
            else
                b2.Checked = false;
            if (((value >> 1) & 0x01) == 0x01)
                b1.Checked = true;
            else
                b1.Checked = false;
            if (((value >> 0) & 0x01) == 0x01)
                b0.Checked = true;
            else
                b0.Checked = false;
        }

        private void bt_script_cancel_Click(object sender, EventArgs e)
        {
            flag_script_data_on = false;
            richTextBox2.Visible = false;
            bt_script_save.Visible = false;
            bt_script_cancel.Visible = false;
            bt_cancel.Visible = false;
            bt_script_load.Visible = true;
            bt_script.Text = "Script";
        }

        private void bt_clear_serial_Click(object sender, EventArgs e)
        {
            tb_sn_opal.Clear();
            timer_stage2.Enabled = false;
            if (this.tb_sn_opal.Focused == false)
                this.tb_sn_opal.Focus();
        }

        private void bt_save_img_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void tb_sn_opal_MouseClick(object sender, MouseEventArgs e)
        {
            lb_main_mesg2.Text = "等待輸入資料";
            timer_stage2.Enabled = true;
            timer_webcam_mode = FOCUS_ON_SERIAL;
            tb_sn_opal.BackColor = Color.Pink;
        }

        int check_tb_sn_opal_data()
        {
            //richTextBox1.Text += "C";
            int i;
            int len;
            bool flag_incorrect_data = false;

            len = tb_sn_opal.Text.Length;

            if (flag_operation_mode != MODE_RELEASE_STAGE3)
            {
                if (len > 20)   //太長, 直接放棄
                {
                    tb_sn_opal.Clear();
                    //richTextBox1.Text += "X1";
                    flag_incorrect_data = true;
                    return S_FALSE;
                }
                else if (len > 5)    //檢查是否換行
                {
                    if (((flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B)) && (cb_stage1_ng.Checked == true))
                    {
                        //no trim
                    }
                    else
                    {
                        if ((tb_sn_opal.Text[len - 2] == 0x0D) || (tb_sn_opal.Text[len - 1] == 0x0A))
                        {
                            tb_sn_opal.Text = tb_sn_opal.Text.Trim();
                        }
                        else
                        {
                            //richTextBox1.Text += "X2";
                            flag_incorrect_data = true;
                            return S_FALSE;
                        }
                    }
                }
                else    //太短  留著累計
                {
                    //richTextBox1.Text += "X3";
                    flag_incorrect_data = true;
                    return S_FALSE;
                }
            }

            if (tb_sn_opal.Text.Length == 0)
            {
                //richTextBox1.Text += "未輸入資料\n";
                flag_incorrect_data = true;
                return S_FALSE;
            }
            else if ((tb_sn_opal.Text.Length == 9) || (tb_sn_opal.Text.Length == 10))
            {
                //檢查英文字母的正確性
                if (((tb_sn_opal.Text[0] >= 'A') && (tb_sn_opal.Text[0] <= 'Z')) || ((tb_sn_opal.Text[0] >= 'a') && (tb_sn_opal.Text[0] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b0\n";
                }

                if (((tb_sn_opal.Text[1] >= 'A') && (tb_sn_opal.Text[1] <= 'Z')) || ((tb_sn_opal.Text[1] >= 'a') && (tb_sn_opal.Text[1] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b1\n";
                }

                for (i = 2; i < tb_sn_opal.Text.Length; i++)
                {
                    if ((tb_sn_opal.Text[i] < '0') || (tb_sn_opal.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b\n";
                    }
                }

                if (flag_incorrect_data == false)
                {
                    richTextBox1.Text += "2取得 SN1序號 : " + tb_sn_opal.Text + "\n";
                }
            }
            else
            {
                flag_incorrect_data = true;
                richTextBox1.Text += "序號格式不正確\n";
            }

            if (flag_incorrect_data == true)
            {
                richTextBox1.Text += "資料錯誤,長度 " + tb_sn_opal.Text.Length.ToString() + "\t內容 " + tb_sn_opal.Text + "\t清除\n";
                show_main_message2("資料錯誤, 請重新輸入", S_OK, 30);
                tb_sn_opal.Clear();
                return S_FALSE;
            }
            else
            {
                tb_awb_mesg.Text = "相機序號正確";
                richTextBox1.Text += "資料正確\n";
                return S_OK;
            }
        }

        int check_tb_sn_opal_data_stage1()
        {
            richTextBox1.Text += "C";
            int i;
            int len;
            bool flag_incorrect_data = false;

            len = tb_sn_opal.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_sn_opal.Clear();
                //richTextBox1.Text += "X1";
                flag_incorrect_data = true;
                return S_FALSE;
            }
            else if (len > 2)    //檢查是否換行
            {
                if ((tb_sn_opal.Text[len - 2] == 0x0D) || (tb_sn_opal.Text[len - 1] == 0x0A))
                {
                    tb_sn_opal.Text = tb_sn_opal.Text.Trim();
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    flag_incorrect_data = true;
                    return S_FALSE;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                flag_incorrect_data = true;
                return S_FALSE;
            }

            if (tb_sn_opal.Text.Length == 0)
            {
                //richTextBox1.Text += "未輸入資料\n";
                flag_incorrect_data = true;
                return S_FALSE;
            }
            else if (tb_sn_opal.Text.Length == 2)
            {
                if (tb_sn_opal.Text == "1J")
                {
                    gb_ng_reason1.Size = new Size(200, 223);
                    //lb_ng_reason.Text = tb_sn_opal.Text + "\n其他：";
                    stage1_ng_reason = 10;
                    flag_wait_for_ng_reason = true;
                    button79.Visible = true;
                    tb_reason_stage1.Visible = true;
                    tb_reason_stage1.Clear();
                    tb_reason_stage1.Focus();
                }
                else
                {
                    gb_ng_reason1.Size = new Size(200, 100);
                    tb_reason_stage1.Visible = false;
                    button79.Visible = false;

                    if (tb_sn_opal.Text == "1A")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\n鏡頭脫落";
                        stage1_ng_reason = 1;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1B")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\n影像有黑影";
                        stage1_ng_reason = 2;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1C")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nRing上有異物";
                        stage1_ng_reason = 3;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1D")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nRing未組裝好";
                        stage1_ng_reason = 4;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1E")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nRing裂痕";
                        stage1_ng_reason = 5;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1F")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nLED脫落";
                        stage1_ng_reason = 6;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1G")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nLED不亮";
                        stage1_ng_reason = 7;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1H")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\nLED有異物";
                        stage1_ng_reason = 8;
                        flag_wait_for_ng_reason = false;
                    }
                    else if (tb_sn_opal.Text == "1I")
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\n漏光";
                        stage1_ng_reason = 9;
                        flag_wait_for_ng_reason = false;
                    }
                    else
                    {
                        //lb_ng_reason.Text = tb_sn_opal.Text + "\n未知";
                        stage1_ng_reason = 0;
                        flag_wait_for_ng_reason = false;
                    }
                }
                cb_stage1_ng.Visible = true;
                cb_stage1_ng.Checked = true;
                gb_ng_reason1.Visible = true;
                lb_ng_reason.Visible = true;
                lb_ng_reason.Text = tb_sn_opal.Text + "\n" + ng_reason[stage1_ng_reason];
                tb_sn_opal.Clear();
                return S_FALSE;
            }
            else if ((tb_sn_opal.Text.Length == 9) || (tb_sn_opal.Text.Length == 10))
            {
                //檢查英文字母的正確性
                if (((tb_sn_opal.Text[0] >= 'A') && (tb_sn_opal.Text[0] <= 'Z')) || ((tb_sn_opal.Text[0] >= 'a') && (tb_sn_opal.Text[0] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b0\n";
                }

                if (((tb_sn_opal.Text[1] >= 'A') && (tb_sn_opal.Text[1] <= 'Z')) || ((tb_sn_opal.Text[1] >= 'a') && (tb_sn_opal.Text[1] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b1\n";
                }

                for (i = 2; i < tb_sn_opal.Text.Length; i++)
                {
                    if ((tb_sn_opal.Text[i] < '0') || (tb_sn_opal.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b\n";
                    }
                }

                if (flag_incorrect_data == false)
                {
                    richTextBox1.Text += "1取得 SN1序號 : " + tb_sn_opal.Text + "\n";
                }
            }
            else
            {
                flag_incorrect_data = true;
                richTextBox1.Text += "序號格式不正確\n";
            }

            if (flag_incorrect_data == true)
            {
                richTextBox1.Text += "資料錯誤,長度 " + tb_sn_opal.Text.Length.ToString() + "\t內容 " + tb_sn_opal.Text + "\t清除\n";
                show_main_message2("資料錯誤, 請重新輸入", S_OK, 30);
                tb_sn_opal.Clear();
                return S_FALSE;
            }
            else
            {
                richTextBox1.Text += "資料正確\n";
                return S_OK;
            }
        }

        int check_tb_sn_opal_data2()
        {
            //richTextBox1.Text += "C";
            int i;
            int len;
            bool flag_incorrect_data = false;

            len = tb_sale3.Text.Length;

            if (flag_operation_mode != MODE_RELEASE_STAGE3)
            {
                if (len > 20)   //太長, 直接放棄
                {
                    tb_sale3.Clear();
                    //richTextBox1.Text += "X1";
                    flag_incorrect_data = true;
                    return S_FALSE;
                }
                else if (len > 5)    //檢查是否換行
                {

                }
                else    //太短  留著累計
                {
                    //richTextBox1.Text += "X3";
                    flag_incorrect_data = true;
                    return S_FALSE;
                }
            }

            if (tb_sale3.Text.Length == 0)
            {
                //richTextBox1.Text += "未輸入資料\n";
                flag_incorrect_data = true;
                return S_FALSE;
            }
            else if ((tb_sale3.Text.Length == 9) || (tb_sale3.Text.Length == 10))
            {
                //檢查英文字母的正確性
                if (((tb_sale3.Text[0] >= 'A') && (tb_sale3.Text[0] <= 'Z')) || ((tb_sale3.Text[0] >= 'a') && (tb_sale3.Text[0] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b0\n";
                }

                if (((tb_sale3.Text[1] >= 'A') && (tb_sale3.Text[1] <= 'Z')) || ((tb_sale3.Text[1] >= 'a') && (tb_sale3.Text[1] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b1\n";
                }

                for (i = 2; i < tb_sale3.Text.Length; i++)
                {
                    if ((tb_sale3.Text[i] < '0') || (tb_sale3.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b\n";
                    }
                }

                if (flag_incorrect_data == false)
                {
                    richTextBox1.Text += "b取得 SN1序號 : " + tb_sale3.Text + "\n";
                }
            }
            else
            {
                flag_incorrect_data = true;
                richTextBox1.Text += "序號格式不正確\n";
            }

            if (flag_incorrect_data == true)
            {
                richTextBox1.Text += "資料錯誤,長度 " + tb_sale3.Text.Length.ToString() + "\t內容 " + tb_sale3.Text + "\t清除\n";
                show_main_message2("資料錯誤, 請重新輸入", S_OK, 30);
                tb_sale3.Clear();
                return S_FALSE;
            }
            else
            {
                richTextBox1.Text += "資料正確\n";
                flag_ok_data3 = true;
                return S_OK;
            }
        }

        int check_tb_sn_opal_data12()
        {
            //richTextBox1.Text += "C";
            int i;
            int len;
            bool flag_incorrect_data = false;

            len = tb_wait_sn_data12.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_wait_sn_data12.Clear();
                flag_incorrect_data = true;
                return S_FALSE;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_sn_data12.Text[len - 2] == 0x0D) || (tb_wait_sn_data12.Text[len - 1] == 0x0A))
                {
                    tb_wait_sn_data12.Text = tb_wait_sn_data12.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return S_FALSE;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                flag_incorrect_data = true;
                return S_FALSE;
            }

            if (tb_wait_sn_data12.Text.Length == 0)
            {
                //richTextBox1.Text += "未輸入資料\n";
                flag_incorrect_data = true;
                richTextBox1.Text += "f3 ";
                return S_FALSE;
            }
            else if ((tb_wait_sn_data12.Text.Length == 9) || (tb_wait_sn_data12.Text.Length == 10))
            {
                //檢查英文字母的正確性
                if (((tb_wait_sn_data12.Text[0] >= 'A') && (tb_wait_sn_data12.Text[0] <= 'Z')) || ((tb_wait_sn_data12.Text[0] >= 'a') && (tb_wait_sn_data12.Text[0] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b0\n";
                }

                if (((tb_wait_sn_data12.Text[1] >= 'A') && (tb_wait_sn_data12.Text[1] <= 'Z')) || ((tb_wait_sn_data12.Text[1] >= 'a') && (tb_wait_sn_data12.Text[1] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b1\n";
                }

                for (i = 2; i < tb_wait_sn_data12.Text.Length; i++)
                {
                    if ((tb_wait_sn_data12.Text[i] < '0') || (tb_wait_sn_data12.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b\n";
                    }
                }

                if (flag_incorrect_data == false)
                {
                    richTextBox1.Text += "c取得 SN1序號 : " + tb_wait_sn_data12.Text + "\n";
                }
            }
            else
            {
                flag_incorrect_data = true;
                richTextBox1.Text += "序號格式不正確\n";
            }

            if (flag_incorrect_data == true)
            {
                richTextBox1.Text += "資料錯誤,長度 " + tb_wait_sn_data12.Text.Length.ToString() + "\t內容 " + tb_wait_sn_data12.Text + "\t清除\n";
                show_main_message12("資料錯誤, 請重新輸入", S_OK, 30);
                tb_wait_sn_data12.Clear();
                richTextBox1.Text += "f4 ";
                return S_FALSE;
            }
            else
            {
                richTextBox1.Text += "資料正確\n";
                return S_OK;
            }
        }

        private void bt_ae_decrease_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Setup AE Target\n";
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte SendData;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x03;
            SendData = 0x1A;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(1000);

            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x04;
            SendData = 0x10;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            /*
            //套用 WPT BPT 的值
            bt_write_wpt_Click(sender, e);
            delay(1000);
            bt_write_bpt_Click(sender, e);
            */
        }

        private void bt_saturation_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Setup saturation\n";
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            /*
            byte SendData;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x03;
            SendData = 0x20;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x04;
            SendData = 0x14;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */

            int sat = (int)numericUpDown_saturation.Value;
            
            richTextBox1.Text += "Setup saturation = " + sat.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x03;
            SendData = (byte)sat;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            sat = sat * 7 / 10;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x04;
            SendData = (byte)sat;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

        }

        private void comboBox_saturation_DropDown(object sender, EventArgs e)
        {
            richTextBox1.Text += "DropDown\n";
            timer_stage2.Enabled = false;
        }

        private void comboBox_saturation_SelectedIndexChanged(object sender, EventArgs e)
        {
            byte TH2 = 0x40;
            byte TH1 = 0x28;

            if (comboBox_saturation.SelectedIndex == 0)
            {
                richTextBox1.Text += "x0\n";
                saturation_ratio = "x0";
                TH2 = 0;
                TH1 = 0;
            }
            else if (comboBox_saturation.SelectedIndex == 1)
            {
                richTextBox1.Text += "x0.25\n";
                saturation_ratio = "x0.25";
                TH2 = 0x10;
                TH1 = 0x0A;
            }
            else if (comboBox_saturation.SelectedIndex == 2)
            {
                richTextBox1.Text += "x0.50\n";
                saturation_ratio = "x0.50";
                TH2 = 0x20;
                TH1 = 0x14;
            }
            else if (comboBox_saturation.SelectedIndex == 3)
            {
                richTextBox1.Text += "x0.75\n";
                saturation_ratio = "x0.75";
                TH2 = 0x26;
                TH1 = 0x1D;
            }
            else if (comboBox_saturation.SelectedIndex == 4)
            {
                richTextBox1.Text += "x0.80\n";
                saturation_ratio = "x0.80";
                TH2 = 44;
                TH1 = 32;
            }
            else if (comboBox_saturation.SelectedIndex == 5)
            {
                richTextBox1.Text += "x0.85\n";
                saturation_ratio = "x0.85";
                TH2 = 49;
                TH1 = 34;
            }
            else if (comboBox_saturation.SelectedIndex == 6)
            {
                richTextBox1.Text += "x0.90\n";
                saturation_ratio = "x0.90";
                TH2 = 54;
                TH1 = 36;
            }
            else if (comboBox_saturation.SelectedIndex == 7)
            {
                richTextBox1.Text += "x0.95\n";
                saturation_ratio = "x0.95";
                TH2 = 59;
                TH1 = 38;
            }
            else if (comboBox_saturation.SelectedIndex == 8)
            {
                richTextBox1.Text += "x1.00\n";
                saturation_ratio = "x1.00";
                TH2 = 0x40;
                TH1 = 0x28;
            }
            else if (comboBox_saturation.SelectedIndex == 9)
            {
                richTextBox1.Text += "x1.25\n";
                saturation_ratio = "x1.25";
                TH2 = 0x50;
                TH1 = 0x32;
            }
            else if (comboBox_saturation.SelectedIndex == 10)
            {
                richTextBox1.Text += "x1.50\n";
                saturation_ratio = "x1.50";
                TH2 = 0x60;
                TH1 = 0x3C;
            }
            else if (comboBox_saturation.SelectedIndex == 11)
            {
                richTextBox1.Text += "x1.75\n";
                saturation_ratio = "x1.75";
                TH2 = 0x70;
                TH1 = 0x46;
            }
            else if (comboBox_saturation.SelectedIndex == 12)
            {
                richTextBox1.Text += "x2.00\n";
                saturation_ratio = "x2.00";
                TH2 = 0x80;
                TH1 = 0x50;
            }
            else
                richTextBox1.Text += "XXXXXXXXXX\n";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            richTextBox1.Text += "Setup saturation,  TH2 = " + TH2.ToString() + ", TH1 = " + TH1.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x03;
            SendData = TH2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(1000);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x04;
            SendData = TH1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            
            timer_stage2.Enabled = true;

            g_TH2 = TH2;
            g_TH1 = TH1;
        }
        void do_save_camera_data()
        {
            if (g_conn_status != CAMERA_OK)
            {
                show_main_message1("無相機，不儲存", S_OK, 50);
                richTextBox1.Text += "無相機，不儲存\n";
                return;
            }

            if (software_version == "A03")
            {
                return;
            }

            delay(50);

            show_main_message1("相機寫入資料中....", S_OK, 50);

            int i;
            int page;
            byte data;
            //ex: DA-52-1A-04-52-1B-D2-52-1E-07-52-1F-08-00-00-00

            /*
            page = USER_PAGE1;

            for (i = 0; i < 16; i++)
            {
                user_flash_data[i] = 0;
            }

            user_flash_data[0] = 0xDA;  //header
            */
            /*
            data = 30;
            user_flash_data[1] = 0x3A;  //WPT AH
            user_flash_data[2] = 0x03;  //WPT AL
            user_flash_data[3] = data;

            data = 20;
            user_flash_data[4] = 0x3A;  //BPT AH
            user_flash_data[5] = 0x04;  //BPT AL
            user_flash_data[6] = data;
            */

            /*
            richTextBox1.Text += "Saturation x0.75\n";
            data = 0x26;
            user_flash_data[7] = 0x58;  //Saturation TH2 AH
            user_flash_data[8] = 0x03;  //Saturation TH2 AL
            user_flash_data[9] = data;

            data = 0x1d;
            user_flash_data[10] = 0x58; //Saturation TH1 AH
            user_flash_data[11] = 0x04; //Saturation TH1 AL
            user_flash_data[12] = data;

            user_flash_data[13] = 0x00; //dummy, no data
            user_flash_data[14] = 0x00; //dummy, no data
            user_flash_data[15] = 0x00; //dummy, no data

            Send_IMS_Data(0xD0, (byte)page, 0, 0);  //write user data to camera flash
            serialPort1.Write(user_flash_data, 0, 16);

            delay(500);
            */
            page = USER_PAGE2;

            for (i = 0; i < 16; i++)
            {
                user_flash_data[i] = 0;
            }

            user_flash_data[0] = 0xDA;  //header

            data = (byte)numericUpDown_brightness.Value;    //default WPT = 120, BPT = 100

            richTextBox1.Text += "Brightness = " + data.ToString() + "\n";

            user_flash_data[1] = 0xAA;
            user_flash_data[2] = 0xBB;
            user_flash_data[3] = data;

            user_flash_data[13] = 0x00; //dummy, no data
            user_flash_data[14] = 0x00; //dummy, no data
            user_flash_data[15] = 0x00; //dummy, no data

            Send_IMS_Data(0xD0, (byte)page, 0, 0);  //write user data to camera flash
            serialPort1.Write(user_flash_data, 0, 16);

            delay(3000);

            richTextBox1.Text += "寫入資料  完成\n";

            show_main_message1("相機寫入資料完成", S_OK, 30);
            return;
        }

        private void bt_save_data_Click(object sender, EventArgs e)
        {
            do_save_camera_data();
        }

        private void bt_min_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void comboBox_denoise_DropDown(object sender, EventArgs e)
        {
            richTextBox1.Text += "DropDown\n";
            timer_stage2.Enabled = false;
        }

        private void comboBox_denoise_SelectedIndexChanged(object sender, EventArgs e)
        {
            byte TH1 = 0x0e;
            byte TH2 = 0x20;

            if (comboBox_denoise.SelectedIndex == 0)
            {
                richTextBox1.Text += "de-noise OFF\n";
                TH1 = 0;
                TH2 = 0;
            }
            else if (comboBox_denoise.SelectedIndex == 1)
            {
                richTextBox1.Text += "de-noise 1\n";
                TH1 = 0x01;
                TH2 = 0x12;
            }
            else if (comboBox_denoise.SelectedIndex == 2)
            {
                richTextBox1.Text += "de-noise 2\n";
                TH1 = 0x02;
                TH2 = 0x14;
            }
            else if (comboBox_denoise.SelectedIndex == 3)
            {
                richTextBox1.Text += "de-noise 3\n";
                TH1 = 0x04;
                TH2 = 0x16;
            }
            else if (comboBox_denoise.SelectedIndex == 4)
            {
                richTextBox1.Text += "de-noise 4\n";
                TH1 = 0x06;
                TH2 = 0x18;
            }
            else if (comboBox_denoise.SelectedIndex == 5)
            {
                richTextBox1.Text += "de-noise 5\n";
                TH1 = 0x08;
                TH2 = 0x1a;
            }
            else if (comboBox_denoise.SelectedIndex == 6)
            {
                richTextBox1.Text += "de-noise 6\n";
                TH1 = 0x0a;
                TH2 = 0x1c;
            }
            else if (comboBox_denoise.SelectedIndex == 7)
            {
                richTextBox1.Text += "de-noise 7\n";
                TH1 = 0x0c;
                TH2 = 0x1e;
            }
            else if (comboBox_denoise.SelectedIndex == 8)
            {
                richTextBox1.Text += "de-noise 8\n";
                TH1 = 0x0e;
                TH2 = 0x20;
            }
            else if (comboBox_denoise.SelectedIndex == 9)
            {
                richTextBox1.Text += "de-noise 9\n";
                TH1 = 0x10;
                TH2 = 0x22;
            }
            else
                richTextBox1.Text += "XXXXXXXXXX\n";


            richTextBox1.Text += "Setup de-noise\n";
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            richTextBox1.Text += "Setup de-noise,  TH1 = " + TH1.ToString() + ", TH2 = " + TH2.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x55;
            DongleAddr_l = 0x06;
            SendData = TH1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(1000);

            DongleAddr_h = 0x55;
            DongleAddr_l = 0x07;
            SendData = TH2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            timer_stage2.Enabled = true;
        }

        private void comboBox_sharpness_DropDown(object sender, EventArgs e)
        {
            richTextBox1.Text += "DropDown\n";
            timer_stage2.Enabled = false;
        }

        private void comboBox_sharpness_SelectedIndexChanged(object sender, EventArgs e)
        {
            byte TH1 = 0x04;
            byte TH2 = 0x06;

            if (comboBox_sharpness.SelectedIndex == 0)
            {
                richTextBox1.Text += "sharpness OFF\n";
                TH1 = 0;
                TH2 = 0;
            }
            else if (comboBox_sharpness.SelectedIndex == 1)
            {
                richTextBox1.Text += "sharpness 1\n";
                TH1 = 0x02;
                TH2 = 0x04;
            }
            else if (comboBox_sharpness.SelectedIndex == 2)
            {
                richTextBox1.Text += "sharpness 2\n";
                TH1 = 0x04;
                TH2 = 0x06;
            }
            else if (comboBox_sharpness.SelectedIndex == 3)
            {
                richTextBox1.Text += "sharpness 3\n";
                TH1 = 0x06;
                TH2 = 0x08;
            }
            else if (comboBox_sharpness.SelectedIndex == 4)
            {
                richTextBox1.Text += "sharpness 4\n";
                TH1 = 0x08;
                TH2 = 0x0a;
            }
            else if (comboBox_sharpness.SelectedIndex == 5)
            {
                richTextBox1.Text += "sharpness 5\n";
                TH1 = 0x0a;
                TH2 = 0x0c;
            }
            else if (comboBox_sharpness.SelectedIndex == 6)
            {
                richTextBox1.Text += "sharpness 6\n";
                TH1 = 0x0c;
                TH2 = 0x0e;
            }
            else if (comboBox_sharpness.SelectedIndex == 7)
            {
                richTextBox1.Text += "sharpness 7\n";
                TH1 = 0x0e;
                TH2 = 0x10;
            }
            else if (comboBox_sharpness.SelectedIndex == 8)
            {
                richTextBox1.Text += "sharpness 8\n";
                TH1 = 0x10;
                TH2 = 0x12;
            }
            else if (comboBox_sharpness.SelectedIndex == 9)
            {
                richTextBox1.Text += "sharpness 9\n";
                TH1 = 0x10;
                TH2 = 0x22;
            }
            else
                richTextBox1.Text += "XXXXXXXXXX\n";


            richTextBox1.Text += "Setup sharpness\n";
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            richTextBox1.Text += "Setup sharpness,  TH1 = " + TH1.ToString() + ", TH2 = " + TH2.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x55;
            DongleAddr_l = 0x0b;
            SendData = TH1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(1000);

            DongleAddr_h = 0x55;
            DongleAddr_l = 0x0c;
            SendData = TH2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);


            timer_stage2.Enabled = true;

        }

        private void numericUpDown_denoise_ValueChanged(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            numericUpDown_denoise.BackColor = Color.Pink;
            richTextBox1.Text += "Setup de-noise " + numericUpDown_denoise.Value.ToString() + "\n";

            byte TH1 = 0x0e;
            byte TH2 = 0x20;

            switch ((int)numericUpDown_denoise.Value)
            {
                case 0:
                    richTextBox1.Text += "de-noise OFF\n";
                    TH1 = 0;
                    TH2 = 0;
                    break;
                case 1:
                    richTextBox1.Text += "de-noise 1\n";
                    TH1 = 0x01;
                    TH2 = 0x12;
                    break;
                case 2:
                    richTextBox1.Text += "de-noise 2\n";
                    TH1 = 0x02;
                    TH2 = 0x14;
                    break;
                case 3:
                    richTextBox1.Text += "de-noise 3\n";
                    TH1 = 0x04;
                    TH2 = 0x16;
                    break;
                case 4:
                    richTextBox1.Text += "de-noise 4\n";
                    TH1 = 0x06;
                    TH2 = 0x18;
                    break;
                case 5:
                    richTextBox1.Text += "de-noise 5\n";
                    TH1 = 0x08;
                    TH2 = 0x1a;
                    break;
                case 6:
                    richTextBox1.Text += "de-noise 6\n";
                    TH1 = 0x0a;
                    TH2 = 0x1c;
                    break;
                case 7:
                    richTextBox1.Text += "de-noise 7\n";
                    TH1 = 0x0c;
                    TH2 = 0x1e;
                    break;
                case 8:
                    richTextBox1.Text += "de-noise 8\n";
                    TH1 = 0x0e;
                    TH2 = 0x20;
                    break;
                case 9:
                    richTextBox1.Text += "de-noise 9\n";
                    TH1 = 0x10;
                    TH2 = 0x22;
                    break;
                default:
                    richTextBox1.Text += "de-noise XXXXXXXXXX\n";
                    break;
            }

            richTextBox1.Text += "Setup de-noise,  TH1 = " + TH1.ToString() + ", TH2 = " + TH2.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x55;
            DongleAddr_l = 0x06;
            SendData = TH1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(500);

            DongleAddr_h = 0x55;
            DongleAddr_l = 0x07;
            SendData = TH2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            numericUpDown_denoise.BackColor = Color.White;
        }

        private void numericUpDown_sharpness_ValueChanged(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            numericUpDown_sharpness.BackColor = Color.Pink;
            richTextBox1.Text += "Setup sharpness " + numericUpDown_sharpness.Value.ToString() + "\n";

            byte TH1 = 0x04;
            byte TH2 = 0x06;

            switch ((int)numericUpDown_sharpness.Value)
            {
                case 0:
                    richTextBox1.Text += "sharpness OFF\n";
                    TH1 = 0;
                    TH2 = 0;
                    break;
                case 1:
                    richTextBox1.Text += "sharpness 1\n";
                    TH1 = 0x02;
                    TH2 = 0x04;
                    break;
                case 2:
                    richTextBox1.Text += "sharpness 2\n";
                    TH1 = 0x04;
                    TH2 = 0x06;
                    break;
                case 3:
                    richTextBox1.Text += "sharpness 3\n";
                    TH1 = 0x06;
                    TH2 = 0x08;
                    break;
                case 4:
                    richTextBox1.Text += "sharpness 4\n";
                    TH1 = 0x08;
                    TH2 = 0x0a;
                    break;
                case 5:
                    richTextBox1.Text += "sharpness 5\n";
                    TH1 = 0x0a;
                    TH2 = 0x0c;
                    break;
                case 6:
                    richTextBox1.Text += "sharpness 6\n";
                    TH1 = 0x0c;
                    TH2 = 0x0e;
                    break;
                case 7:
                    richTextBox1.Text += "sharpness 7\n";
                    TH1 = 0x0e;
                    TH2 = 0x10;
                    break;
                case 8:
                    richTextBox1.Text += "sharpness 8\n";
                    TH1 = 0x10;
                    TH2 = 0x12;
                    break;
                case 9:
                    richTextBox1.Text += "sharpness 9\n";
                    TH1 = 0x10;
                    TH2 = 0x22;
                    break;
                default:
                    richTextBox1.Text += "sharpness XXXXXXXXXX\n";
                    TH1 = 0;
                    TH2 = 0;
                    break;
            }

            richTextBox1.Text += "Setup sharpness,  TH1 = " + TH1.ToString() + ", TH2 = " + TH2.ToString() + "\n";

            byte SendData;
            DongleAddr_h = 0x55;
            DongleAddr_l = 0x0b;
            SendData = TH1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            delay(500);

            DongleAddr_h = 0x55;
            DongleAddr_l = 0x0c;
            SendData = TH2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            numericUpDown_sharpness.BackColor = Color.White;

        }

        private void button41_Click_1(object sender, EventArgs e)
        {
            erase_camera_data();
        }

        private void button47_Click(object sender, EventArgs e)
        {
            make_camera_data();
        }

        private void button46_Click(object sender, EventArgs e)
        {
            make_camera_data();
        }

        private void button48_Click(object sender, EventArgs e)
        {
            erase_camera_data();
        }

        private void tb_sn_opal_KeyPress(object sender, KeyPressEventArgs e)
        {
            //撈取ESC
            if (e.KeyChar == (Char)27)
            {
                richTextBox1.Text += "Esc\n";
                tb_sn_opal.Clear();
                timer_stage2.Enabled = true;
                //timer_webcam_mode = FOCUS_ON_PICTURE;
                //this.tb_sn_opal.BackColor = Color.White;
                //this.pictureBox1.Focus();
                show_main_message2("取消存檔", S_OK, 10);

                e.Handled = true;
            }
            else
            {
                e.Handled = false;
            }
        }

        private void button20_MouseHover(object sender, EventArgs e)
        {
            /*
            if (flag_operation_mode == MODE_RELEASE_STAGE1)
            {
                timer_stage1.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                timer_stage2.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                timer_stage3.Enabled = false;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE5)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage5.Enabled = false;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE6)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage6.Enabled = false;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE7)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage7.Enabled = false;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE8)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage8.Enabled = false;
                }
            }
            lb_main_mesg1.Text = "下好離手";
            lb_main_mesg2.Text = "下好離手";
            lb_main_mesg3.Text = "下好離手";
            */
        }

        private void button20_MouseLeave(object sender, EventArgs e)
        {
            /*
            if (flag_operation_mode == MODE_RELEASE_STAGE1)
            {
                timer_stage1.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE2)
            {
                timer_stage2.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE3)
            {
                timer_stage3.Enabled = true;
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE5)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage5.Enabled = true;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE6)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage6.Enabled = true;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE7)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage7.Enabled = true;
                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE8)
            {
                if (flag_auto_scan_mode == true)
                {
                    timer_stage8.Enabled = true;
                }
            }
            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
            lb_main_mesg3.Text = "";
            */
        }

        private void button52_Click(object sender, EventArgs e)
        {
            tb_product1.Clear();
            tb_product2.Clear();
            tb_product3.Clear();
            tb_product1.BackColor = Color.White;
            tb_product2.BackColor = Color.White;
            tb_product3.BackColor = Color.White;
            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;
        }

        private void timer_stage5_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if ((ccc % 4) == 0)
                lb_main_mesg5.Text = "等待輸入資料 \\";
            else if ((ccc % 4) == 1)
                lb_main_mesg5.Text = "等待輸入資料 |";
            else if ((ccc % 4) == 2)
                lb_main_mesg5.Text = "等待輸入資料 /";
            else
                lb_main_mesg5.Text = "等待輸入資料 -";

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "五";
                if (this.tb_wait_product_data.Focused == false)
                {
                    this.tb_wait_product_data.Focus();
                    richTextBox1.Text += "F5";
                }
            }

            if (flag_network_disk_status == false)
            {
                tb_wait_product_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            int len;
            len = tb_wait_product_data.Text.Length;

            if (len > 50)   //太長, 直接放棄
            {
                tb_wait_product_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_product_data.Text[len - 2] == 0x0D) || (tb_wait_product_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_product_data.Text = tb_wait_product_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_product_data.Text.Length > 0)
            {
                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_product_data.Text.Length == 11)
                {
                    for (i = 0; i < tb_wait_product_data.Text.Length; i++)
                    {
                        if ((tb_wait_product_data.Text[i] < '0') || (tb_wait_product_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料p1格式不正確\n";
                            tb_wait_product_data.Text = "";
                            tb_product1.Clear();
                            tb_product1.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得資料1 : " + tb_wait_product_data.Text + "\n";
                        tb_product1.Text = tb_wait_product_data.Text;
                        tb_product1.BackColor = Color.White;
                        tb_wait_product_data.Text = "";
                        if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                        {
                            panel4.BackgroundImage = null;
                            g3.Clear(BackColor);
                        }
                        flag_ok_data1 = true;
                        check_export_data();
                    }
                }
                else if ((tb_wait_product_data.Text.Length == 38) || (tb_wait_product_data.Text.Length == 39))
                {
                    for (i = 0; i < tb_wait_product_data.Text.Length; i++)
                    {
                        if ((tb_wait_product_data.Text[i] < '0') || (tb_wait_product_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料p2格式不正確\n";
                            tb_wait_product_data.Text = "";
                            tb_product2.Clear();
                            tb_product2.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得資料2 : " + tb_wait_product_data.Text + "\n";
                        tb_product2.Text = tb_wait_product_data.Text;
                        tb_product2.BackColor = Color.White;
                        tb_wait_product_data.Text = "";
                        if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                        {
                            panel4.BackgroundImage = null;
                            g3.Clear(BackColor);
                        }
                        flag_ok_data2 = true;
                        check_export_data();
                    }
                }
                else if (tb_wait_product_data.Text.Length == 19)
                {
                    for (i = 0; i < tb_wait_product_data.Text.Length; i++)
                    {
                        if ((i == 6) || (i == 14))
                        {
                            if (tb_wait_product_data.Text[i] != '-')
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料p3格式不正確a\n";
                                tb_wait_product_data.Text = "";
                                tb_product3.Clear();
                                tb_product3.BackColor = Color.Pink;
                            }
                        }
                        else if ((tb_wait_product_data.Text[i] < '0') || (tb_wait_product_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料p3格式不正確b\n";
                            tb_wait_product_data.Text = "";
                            tb_product3.Clear();
                            tb_product3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得資料3 : " + tb_wait_product_data.Text + "\n";
                        tb_product3.Text = tb_wait_product_data.Text;
                        tb_product3.BackColor = Color.White;
                        tb_wait_product_data.Text = "";
                        if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                        {
                            panel4.BackgroundImage = null;
                            g3.Clear(BackColor);
                        }
                        flag_ok_data3 = true;
                        check_export_data();
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                    tb_wait_product_data.Text = "";
                }

            }

        }

        void check_export_data()
        {
            if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_ok_data3 == true))
            {
                flag_ok_to_write_data = true;
                richTextBox1.Text += "資料齊全, 準備存檔\n";

                if (flag_operation_mode == MODE_RELEASE_STAGE5)
                    camera_serials.Add(new string[] { tb_product1.Text, tb_product2.Text, tb_product3.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                    camera_serials.Add(new string[] { tb_package11.Text, tb_package12.Text, tb_package13.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                    camera_serials.Add(new string[] { tb_package21.Text, tb_package22.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                    camera_serials.Add(new string[] { tb_package31.Text, tb_package32.Text, tb_package33.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE9)
                    camera_serials.Add(new string[] { tb_sale3.Text, tb_sale1.Text, tb_sale2.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE11)
                    camera_serials.Add(new string[] { tb_sale3.Text, tb_sale1.Text, tb_sale2.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    if ((cb_check1c.Checked == true) && (cb_check2c.Checked == true) && (cb_check3c.Checked == true))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "底部", "Hi-pot", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == true) && (cb_check2c.Checked == true) && (cb_check3c.Checked == false))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "底部", "Hi-pot", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == true) && (cb_check2c.Checked == false) && (cb_check3c.Checked == true))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "底部", "", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == false) && (cb_check2c.Checked == true) && (cb_check3c.Checked == true))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "", "Hi-pot", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == true) && (cb_check2c.Checked == false) && (cb_check3c.Checked == false))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "底部", "", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == false) && (cb_check2c.Checked == true) && (cb_check3c.Checked == false))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "", "Hi-pot", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else if ((cb_check1c.Checked == false) && (cb_check2c.Checked == false) && (cb_check3c.Checked == true))
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "", "", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    else
                        camera_serials.Add(new string[] { tb_sn_opal12.Text, richTextBox3.Text.Trim(), "", "", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX\n";
                    return;
                }

                exportCSV();

                if (flag_operation_mode == MODE_RELEASE_STAGE5)
                {
                    g3.Clear(BackColor);
                    g3.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_product1.Text = "ERP-SN : " + tb_product1.Text;
                    lb_product2.Text = "PI-SN : " + tb_product2.Text;
                    lb_product3.Text = "BOX-Lot : " + tb_product3.Text;

                    tb_product1.Clear();
                    tb_product2.Clear();
                    tb_product3.Clear();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE6)
                {
                    g6.Clear(BackColor);
                    g6.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_package11.Text = "主機序號 : " + tb_package11.Text;
                    lb_package12.Text = "小PCBA序號 : " + tb_package12.Text;
                    lb_package13.Text = "大PCBA序號 : " + tb_package13.Text;

                    tb_package11.Clear();
                    tb_package12.Clear();
                    tb_package13.Clear();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE7)
                {
                    g7.Clear(BackColor);
                    g7.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_package21.Text = "Dongle包裝 : " + tb_package21.Text;
                    lb_package22.Text = "Dongle序號 : " + tb_package22.Text;

                    tb_package21.Clear();
                    tb_package22.Clear();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE8)
                {
                    g8.Clear(BackColor);
                    g8.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_package31.Text = "成品包裝序號 : " + tb_package31.Text;
                    lb_package32.Text = "主機序號 : " + tb_package32.Text;
                    lb_package33.Text = "Dongle包裝 : " + tb_package33.Text;

                    tb_package31.Clear();
                    tb_package32.Clear();
                    tb_package33.Clear();
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE9) || (flag_operation_mode == MODE_RELEASE_STAGE11))
                {
                    g9.Clear(BackColor);
                    g9.DrawString("存檔完成 " + csv_index9.ToString(), new Font("標楷體", 45), new SolidBrush(Color.Blue), new PointF(5, 30));
                    playSound(S_OK);

                    lb_sale1.Text = "單別(4碼) : " + tb_sale1.Text;
                    lb_sale2.Text = "單號(7碼) : " + tb_sale2.Text;

                    if (flag_operation_mode == MODE_RELEASE_STAGE9)
                        lb_sale3.Text = "箱號或序號 : " + tb_sale3.Text;
                    else
                        lb_sale3.Text = "相機序號(9~10碼) : " + tb_sale3.Text;

                    if (flag_cancel_data == true)
                    {
                        label16.Text = "取消資料";
                        flag_cancel_data = false;
                        checkBox1.Checked = false;
                        clear_group_ng_reason_data();
                        label16.ForeColor = Color.Red;
                        lb_sale1.ForeColor = Color.Red;
                        lb_sale2.ForeColor = Color.Red;
                        lb_sale3.ForeColor = Color.Red;
                    }
                    else
                    {
                        label16.Text = "寫入資料";
                        label16.ForeColor = Color.Black;
                        lb_sale1.ForeColor = Color.Black;
                        lb_sale2.ForeColor = Color.Black;
                        lb_sale3.ForeColor = Color.Black;
                    }

                    //tb_sale1.Clear();
                    //tb_sale2.Clear();
                    tb_sale3.Clear();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE12)
                {
                    g12.Clear(BackColor);
                    g12.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    tb_sn_opal12.Text = "";
                    tb_wait_sn_data12.Text = "";
                    flag_wait_cosmo_message = false;
                    flag_ok_data1 = false;
                    flag_ok_data2 = false;
                    flag_ok_data3 = false;

                    cb_check1c.Checked = false;
                    cb_check2c.Checked = false;
                    cb_check3c.Checked = false;
                    cb_check1c.BackColor = Color.White;
                    cb_check2c.BackColor = Color.White;
                    cb_check3c.BackColor = Color.White;
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX\n";
                    return;
                }

                if ((flag_operation_mode == MODE_RELEASE_STAGE9) || (flag_operation_mode == MODE_RELEASE_STAGE11))
                {
                    flag_ok_data3 = false;
                }
                else
                {
                    flag_ok_data1 = false;
                    flag_ok_data2 = false;
                    flag_ok_data3 = false;
                }

                flag_ok_to_write_data = false;
            }
            else
            {
                richTextBox1.Text += "資料還不齊全\n";
            }
        }

        void check_export_data78()
        {
            if (flag_operation_mode == MODE_RELEASE_STAGE7)
            {
                if ((flag_ok_data1 == true) && (flag_ok_data2 == true))
                {
                    flag_ok_to_write_data = true;
                    richTextBox1.Text += "資料齊全, 準備存檔\n";

                    camera_serials.Add(new string[] { tb_package21.Text, tb_package22.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });

                    exportCSV();

                    g7.Clear(BackColor);
                    g7.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_package21.Text = "Dongle包裝 : " + tb_package21.Text;
                    lb_package22.Text = "Dongle序號 : " + tb_package22.Text;

                    tb_package21.Clear();
                    tb_package22.Clear();

                    flag_ok_data1 = false;
                    flag_ok_data2 = false;

                    flag_ok_to_write_data = false;
                }
                else
                {
                    richTextBox1.Text += "資料還不齊全\n";

                }
            }
            else if (flag_operation_mode == MODE_RELEASE_STAGE8)
            {
                if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_ok_data3 == true))
                {
                    flag_ok_to_write_data = true;
                    richTextBox1.Text += "資料齊全, 準備存檔\n";

                    camera_serials.Add(new string[] { tb_package31.Text, tb_package32.Text, tb_package33.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });

                    exportCSV();

                    g8.Clear(BackColor);
                    g8.DrawString("存檔完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    playSound(S_OK);

                    lb_package31.Text = "成品包裝序號 : " + tb_package31.Text;
                    lb_package32.Text = "主機序號 : " + tb_package32.Text;
                    lb_package33.Text = "Dongle包裝 : " + tb_package33.Text;

                    tb_package31.Clear();
                    tb_package32.Clear();
                    tb_package33.Clear();

                    flag_ok_data1 = false;
                    flag_ok_data2 = false;
                    flag_ok_data3 = false;

                    flag_ok_to_write_data = false;
                }
                else
                {
                    richTextBox1.Text += "資料還不齊全\n";

                }
            }
        }

        private void button54_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                timer_stage5.Enabled = false;
                flag_auto_scan_mode = false;
                button54.Text = "到自動模式";
                lb_main_mesg5.Text = "修改模式";
            }
            else
            {
                timer_stage5.Enabled = true;
                flag_auto_scan_mode = true;
                button54.Text = "到修改模式";
                lb_main_mesg5.Text = "自動模式";
            }
        }

        private void button53_Click(object sender, EventArgs e)
        {
            int result = check_product_data();
            if (result == S_OK)
            {
                check_export_data();
            }
            else
            {
                richTextBox1.Text += "資料不齊全, 忽略\n";
                g3.Clear(BackColor);
                g3.DrawString("資料錯誤", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                playSound(S_FALSE);
            }
        }

        int check_product_data()
        {
            int i;
            bool flag_incorrect_data = false;

            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;

            flag_incorrect_data = false;
            if (tb_product1.Text.Length == 0)
            {
                richTextBox1.Text += "無資料p1\n";
                tb_product1.BackColor = Color.Pink;
            }
            else if (tb_product1.Text.Length == 11)
            {
                for (i = 0; i < tb_product1.Text.Length; i++)
                {
                    if ((tb_product1.Text[i] < '0') || (tb_product1.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料p1格式不正確\n";
                        tb_wait_product_data.Text = "";
                        tb_product1.Clear();
                        tb_product1.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data1 = true;
                    tb_product1.BackColor = Color.White;
                }
                else
                    flag_ok_data1 = false;
            }
            else
            {
                flag_ok_data1 = false;
                tb_product1.BackColor = Color.Pink;
                tb_product1.Clear();
            }

            flag_incorrect_data = false;
            if (tb_product2.Text.Length == 0)
            {
                richTextBox1.Text += "無資料p2\n";
                tb_product2.BackColor = Color.Pink;
            }
            else if ((tb_product2.Text.Length == 38) || (tb_product2.Text.Length == 39))
            {
                for (i = 0; i < tb_product2.Text.Length; i++)
                {
                    if ((tb_product2.Text[i] < '0') || (tb_product2.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料p2格式不正確\n";
                        tb_wait_product_data.Text = "";
                        tb_product2.Clear();
                        tb_product2.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data2 = true;
                    tb_product2.BackColor = Color.White;
                }
                else
                    flag_ok_data2 = false;
            }
            else
            {
                flag_ok_data2 = false;
                tb_product2.BackColor = Color.Pink;
                tb_product2.Clear();
            }

            flag_incorrect_data = false;
            if (tb_product3.Text.Length == 0)
            {
                richTextBox1.Text += "無資料p3\n";
                tb_product3.BackColor = Color.Pink;
            }
            else if (tb_product3.Text.Length == 19)
            {
                for (i = 0; i < tb_product3.Text.Length; i++)
                {
                    if ((i == 6) || (i == 14))
                    {
                        if (tb_product3.Text[i] != '-')
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料p3格式不正確a\n";
                            tb_wait_product_data.Text = "";
                            tb_product3.Clear();
                            tb_product3.BackColor = Color.Pink;
                        }
                    }
                    else if ((tb_product3.Text[i] < '0') || (tb_product3.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料p3格式不正確b\n";
                        tb_wait_product_data.Text = "";
                        tb_product3.Clear();
                        tb_product3.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data3 = true;
                    tb_product3.BackColor = Color.White;
                }
                else
                    flag_ok_data3 = false;
            }
            else
            {
                flag_ok_data3 = false;
                tb_product3.BackColor = Color.Pink;
                tb_product3.Clear();
            }

            if (flag_ok_data1 == true)
                tb_product1.BackColor = Color.White;
            else
                tb_product1.BackColor = Color.Pink;

            if (flag_ok_data2 == true)
                tb_product2.BackColor = Color.White;
            else
                tb_product2.BackColor = Color.Pink;

            if (flag_ok_data3 == true)
                tb_product3.BackColor = Color.White;
            else
                tb_product3.BackColor = Color.Pink;

            if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_ok_data3 == true))
            {
                richTextBox1.Text += "資料齊全\n";
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料未齊全\n";
                return S_FALSE;
            }
        }

        private void bt_awb_test_MouseHover(object sender, EventArgs e)
        {
            /*
            timer_stage2.Enabled = false;
            lb_main_mesg1.Text = "下好離手";
            lb_main_mesg2.Text = "下好離手";
            lb_main_mesg3.Text = "下好離手";
            */
        }

        private void bt_awb_test_MouseLeave(object sender, EventArgs e)
        {
            /*
            timer_stage2.Enabled = true;
            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
            lb_main_mesg3.Text = "";
            */
        }

        int check_network_disk()
        {
            //richTextBox1.Text += "check_network_disk()\n";
            string PathM = "M:\\";  //M槽放圖
            string PathN = "N:\\";  //N槽放CSV檔

            if ((flag_operation_mode != MODE_RELEASE_STAGE1C) && (flag_operation_mode != MODE_RELEASE_STAGE2) && (flag_operation_mode != MODE_RELEASE_STAGE5) && (flag_operation_mode != MODE_RELEASE_STAGE6) && (flag_operation_mode != MODE_RELEASE_STAGE7) && (flag_operation_mode != MODE_RELEASE_STAGE8) && (flag_operation_mode != MODE_RELEASE_STAGE9) && (flag_operation_mode != MODE_RELEASE_STAGE11) && (flag_operation_mode != MODE_RELEASE_STAGE12) && (Directory.Exists(PathM) == false))     //確認資料夾是否存在
            {
                show_main_message1("無法連上 " + PathM, S_FALSE, 30);
                show_main_message2("無法連上 " + PathM, S_FALSE, 30);
                show_main_message3("無法連上 " + PathM, S_FALSE, 30);
                flag_network_disk_status = false;
            }
            else if (Directory.Exists(PathN) == false)     //確認資料夾是否存在
            {
                show_main_message1("無法連上 " + PathN, S_FALSE, 30);
                show_main_message2("無法連上 " + PathN, S_FALSE, 30);
                show_main_message3("無法連上 " + PathN, S_FALSE, 30);
                flag_network_disk_status = false;
            }
            else
            {
                /*
                show_main_message1("已連上 " + Path, S_OK, 10);
                show_main_message2("已連上 " + Path, S_OK, 10);
                show_main_message3("已連上 " + Path, S_OK, 10);
                */
                flag_network_disk_status = true;
            }

            if (flag_network_disk_status == true)
                return S_OK;
            else
                return S_FALSE;
        }

        private void button49_Click(object sender, EventArgs e)
        {
            save_image_to_local_drive();
        }

        private void timer_stage6_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if ((ccc % 4) == 0)
                lb_main_mesg6.Text = "等待輸入資料 \\";
            else if ((ccc % 4) == 1)
                lb_main_mesg6.Text = "等待輸入資料 |";
            else if ((ccc % 4) == 2)
                lb_main_mesg6.Text = "等待輸入資料 /";
            else
                lb_main_mesg6.Text = "等待輸入資料 -";

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "六";
                if (this.tb_wait_package1_data.Focused == false)
                {
                    this.tb_wait_package1_data.Focus();
                    richTextBox1.Text += "F6";
                }
            }

            if (flag_network_disk_status == false)
            {
                tb_wait_package1_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            int len;
            len = tb_wait_package1_data.Text.Length;

            if (len > 50)   //太長, 直接放棄
            {
                tb_wait_package1_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_package1_data.Text[len - 2] == 0x0D) || (tb_wait_package1_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_package1_data.Text = tb_wait_package1_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_package1_data.Text.Length > 0)
            {
                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_package1_data.Text.Length == 13)    //part 1 or part3
                {
                    for (i = 0; i < tb_wait_package1_data.Text.Length; i++)
                    {
                        if ((i != 7) && (i != 8))
                        {
                            if ((tb_wait_package1_data.Text[i] < '0') || (tb_wait_package1_data.Text[i] > '9'))
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料1,3格式不正確\n";
                                tb_wait_package1_data.Text = "";
                                tb_package11.Clear();
                                tb_package11.BackColor = Color.Pink;
                                flag_ok_data1 = false;
                                tb_package13.Clear();
                                tb_package13.BackColor = Color.Pink;
                                flag_ok_data3 = false;
                            }
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        if ((tb_wait_package1_data.Text[7] == '-') && (((tb_wait_package1_data.Text[8] >= 'A') && (tb_wait_package1_data.Text[8] <= 'Z')) || ((tb_wait_package1_data.Text[8] >= 'a') && (tb_wait_package1_data.Text[8] <= 'z'))))
                        {
                            richTextBox1.Text += "取得資料1 : " + tb_wait_package1_data.Text + "\n";
                            tb_package11.Text = tb_wait_package1_data.Text;
                            tb_package11.BackColor = Color.White;
                            tb_wait_package1_data.Text = "";
                            if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                            {
                                panel_package1.BackgroundImage = null;
                                g6.Clear(BackColor);
                            }
                            flag_ok_data1 = true;
                            check_export_data();
                        }
                        else if ((tb_wait_package1_data.Text[7] >= '0') && (tb_wait_package1_data.Text[7] <= '9') && (tb_wait_package1_data.Text[8] >= '0') && (tb_wait_package1_data.Text[8] <= '9'))
                        {
                            richTextBox1.Text += "取得資料3 : " + tb_wait_package1_data.Text + "\n";
                            tb_package13.Text = tb_wait_package1_data.Text;
                            tb_package13.BackColor = Color.White;
                            tb_wait_package1_data.Text = "";
                            if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                            {
                                panel_package1.BackgroundImage = null;
                                g6.Clear(BackColor);
                            }
                            flag_ok_data3 = true;
                            check_export_data();
                        }
                        else
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料1,3格式不正確\n";
                            tb_wait_package1_data.Text = "";
                            tb_package11.Clear();
                            tb_package11.BackColor = Color.Pink;
                            flag_ok_data1 = false;
                            tb_package13.Clear();
                            tb_package13.BackColor = Color.Pink;
                            flag_ok_data3 = false;
                        }
                    }
                }
                else if (tb_wait_package1_data.Text.Length == 24)
                {
                    for (i = 0; i < tb_wait_package1_data.Text.Length; i++)
                    {
                        if ((i == 7) || (i == 12) || (i == 19))
                        {
                            if (tb_wait_package1_data.Text[i] != ' ')
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料12格式不正確a\n";
                                tb_wait_package1_data.Text = "";
                                tb_package12.Clear();
                                tb_package12.BackColor = Color.Pink;
                                flag_ok_data2 = false;
                            }
                        }
                        else if ((tb_wait_package1_data.Text[i] < '0') || (tb_wait_package1_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料12格式不正確b\n";
                            tb_wait_package1_data.Text = "";
                            tb_package12.Clear();
                            tb_package12.BackColor = Color.Pink;
                            flag_ok_data2 = false;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得資料2 : " + tb_wait_package1_data.Text + "\n";
                        tb_package12.Text = tb_wait_package1_data.Text;
                        tb_package12.BackColor = Color.White;
                        tb_wait_package1_data.Text = "";
                        if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                        {
                            panel_package1.BackgroundImage = null;
                            g6.Clear(BackColor);
                        }
                        flag_ok_data2 = true;
                        check_export_data();
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                    tb_wait_package1_data.Text = "";
                }
            }
        }

        private void timer_stage7_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if (flag_ok_data1 == false)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg7.Text = "等待輸入第 1 筆資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg7.Text = "等待輸入第 1 筆資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg7.Text = "等待輸入第 1 筆資料 /";
                else
                    lb_main_mesg7.Text = "等待輸入第 1 筆資料 -";
            }
            else
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg7.Text = "等待輸入第 2 筆資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg7.Text = "等待輸入第 2 筆資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg7.Text = "等待輸入第 2 筆資料 /";
                else
                    lb_main_mesg7.Text = "等待輸入第 2 筆資料 -";
            }

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "七";
                if (this.tb_wait_package2_data.Focused == false)
                {
                    this.tb_wait_package2_data.Focus();
                    richTextBox1.Text += "F7";
                }
            }

            if (flag_network_disk_status == false)
            {
                tb_wait_package2_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            int len;
            len = tb_wait_package2_data.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_wait_package2_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_package2_data.Text[len - 2] == 0x0D) || (tb_wait_package2_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_package2_data.Text = tb_wait_package2_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_package2_data.Text.Length > 0)
            {
                if ((flag_ok_data1 == false) && (flag_ok_data2 == false))
                {
                    panel_package2.BackgroundImage = null;
                    g7.Clear(BackColor);
                    g7.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));
                }

                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_package2_data.Text.Length == 13)
                {
                    for (i = 0; i < tb_wait_package2_data.Text.Length; i++)
                    {
                        if (i == 7)
                        {
                            if (tb_wait_package2_data.Text[i] != '-')
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料23格式不正確a\n";
                                tb_wait_package2_data.Text = "";
                                //tb_product3.Clear();
                                //tb_product3.BackColor = Color.Pink;
                            }
                        }
                        else if (i == 8)
                        {
                            //檢查英文字母的正確性
                            if (((tb_wait_package2_data.Text[i] >= 'A') && (tb_wait_package2_data.Text[i] <= 'Z')) || ((tb_wait_package2_data.Text[i] >= 'a') && (tb_wait_package2_data.Text[i] <= 'z')))
                            {
                                flag_incorrect_data = false;
                            }
                            else
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料23格式不正確a\n";
                                tb_wait_package2_data.Text = "";
                                //tb_product3.Clear();
                                //tb_product3.BackColor = Color.Pink;
                            }
                        }
                        else if ((tb_wait_package2_data.Text[i] < '0') || (tb_wait_package2_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料23格式不正確b\n";
                            tb_wait_package2_data.Text = "";
                            //tb_product3.Clear();
                            //tb_product3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        if (flag_ok_data1 == false)
                        {
                            flag_ok_data1 = true;
                            richTextBox1.Text += "取得資料1 : " + tb_wait_package2_data.Text + "\n";
                            tb_package21.Text = tb_wait_package2_data.Text;
                            tb_package21.BackColor = Color.White;
                            tb_wait_package2_data.Text = "";
                        }
                        else
                        {
                            flag_ok_data2 = true;
                            richTextBox1.Text += "取得資料2 : " + tb_wait_package2_data.Text + "\n";
                            tb_package22.Text = tb_wait_package2_data.Text;
                            tb_package22.BackColor = Color.White;
                            tb_wait_package2_data.Text = "";
                            /*
                            if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                            {
                                panel4.BackgroundImage = null;
                                g3.Clear(BackColor);
                            }
                            flag_ok_data1 = true;
                            */

                            delay(30);
                            check_export_data78();
                        }
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                    tb_wait_package2_data.Text = "";
                }

            }




        }

        private void timer_stage8_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if (flag_ok_data1 == false)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg8.Text = "等待輸入第 1 筆資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg8.Text = "等待輸入第 1 筆資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg8.Text = "等待輸入第 1 筆資料 /";
                else
                    lb_main_mesg8.Text = "等待輸入第 1 筆資料 -";
            }
            else if (flag_ok_data2 == false)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg8.Text = "等待輸入第 2 筆資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg8.Text = "等待輸入第 2 筆資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg8.Text = "等待輸入第 2 筆資料 /";
                else
                    lb_main_mesg8.Text = "等待輸入第 2 筆資料 -";
            }
            else
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg8.Text = "等待輸入第 3 筆資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg8.Text = "等待輸入第 3 筆資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg8.Text = "等待輸入第 3 筆資料 /";
                else
                    lb_main_mesg8.Text = "等待輸入第 3 筆資料 -";
            }

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "八";
                if (this.tb_wait_package3_data.Focused == false)
                {
                    this.tb_wait_package3_data.Focus();
                    richTextBox1.Text += "F8";
                }
            }

            if (flag_network_disk_status == false)
            {
                tb_wait_package3_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            int len;
            len = tb_wait_package3_data.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_wait_package3_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_package3_data.Text[len - 2] == 0x0D) || (tb_wait_package3_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_package3_data.Text = tb_wait_package3_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_package3_data.Text.Length > 0)
            {
                if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_ok_data3 == false))
                {
                    panel_package3.BackgroundImage = null;
                    g8.Clear(BackColor);
                    g8.DrawString("要照順序", new Font("標楷體", 60), new SolidBrush(Color.Green), new PointF(20, 20));
                }

                int i;
                bool flag_incorrect_data = false;
                if (tb_wait_package3_data.Text.Length == 13)
                {
                    for (i = 0; i < tb_wait_package3_data.Text.Length; i++)
                    {
                        if (i == 7)
                        {
                            if (tb_wait_package3_data.Text[i] != '-')
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料33格式不正確a\n";
                                tb_wait_package3_data.Text = "";
                                //tb_product3.Clear();
                                //tb_product3.BackColor = Color.Pink;
                            }
                        }
                        else if (i == 8)
                        {
                            //檢查英文字母的正確性
                            if (((tb_wait_package3_data.Text[i] >= 'A') && (tb_wait_package3_data.Text[i] <= 'Z')) || ((tb_wait_package3_data.Text[i] >= 'a') && (tb_wait_package3_data.Text[i] <= 'z')))
                            {
                                flag_incorrect_data = false;
                            }
                            else
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "資料33格式不正確a\n";
                                tb_wait_package3_data.Text = "";
                                //tb_product3.Clear();
                                //tb_product3.BackColor = Color.Pink;
                            }
                        }
                        else if ((tb_wait_package3_data.Text[i] < '0') || (tb_wait_package3_data.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料33格式不正確b\n";
                            tb_wait_package3_data.Text = "";
                            //tb_product3.Clear();
                            //tb_product3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        if (flag_ok_data1 == false)
                        {
                            flag_ok_data1 = true;
                            richTextBox1.Text += "取得資料1 : " + tb_wait_package3_data.Text + "\n";
                            tb_package31.Text = tb_wait_package3_data.Text;
                            tb_package31.BackColor = Color.White;
                            tb_wait_package3_data.Text = "";
                        }
                        else if (flag_ok_data2 == false)
                        {
                            flag_ok_data2 = true;
                            richTextBox1.Text += "取得資料2 : " + tb_wait_package3_data.Text + "\n";
                            tb_package32.Text = tb_wait_package3_data.Text;
                            tb_package32.BackColor = Color.White;
                            tb_wait_package3_data.Text = "";
                        }
                        else
                        {
                            flag_ok_data3 = true;
                            richTextBox1.Text += "取得資料3 : " + tb_wait_package3_data.Text + "\n";
                            tb_package33.Text = tb_wait_package3_data.Text;
                            tb_package33.BackColor = Color.White;
                            tb_wait_package3_data.Text = "";

                            delay(30);
                            check_export_data78();
                        }
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                    tb_wait_package3_data.Text = "";
                }

            }
        }

        private void button50_Click(object sender, EventArgs e)
        {
            tb_package11.Clear();
            tb_package12.Clear();
            tb_package13.Clear();
            tb_package11.BackColor = Color.White;
            tb_package12.BackColor = Color.White;
            tb_package13.BackColor = Color.White;
            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;
        }

        private void button56_Click(object sender, EventArgs e)
        {
            tb_package21.Clear();
            tb_package22.Clear();
            tb_package21.BackColor = Color.White;
            tb_package22.BackColor = Color.White;
            flag_ok_data1 = false;
            flag_ok_data2 = false;
        }

        private void button59_Click(object sender, EventArgs e)
        {
            tb_package31.Clear();
            tb_package32.Clear();
            tb_package33.Clear();
            tb_package31.BackColor = Color.White;
            tb_package32.BackColor = Color.White;
            tb_package33.BackColor = Color.White;
            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;
        }

        private void button55_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                timer_stage6.Enabled = false;
                flag_auto_scan_mode = false;
                button55.Text = "到自動模式";
                lb_main_mesg6.Text = "修改模式";
            }
            else
            {
                timer_stage6.Enabled = true;
                flag_auto_scan_mode = true;
                button55.Text = "到修改模式";
                lb_main_mesg6.Text = "自動模式";
            }

        }

        private void button58_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                timer_stage7.Enabled = false;
                flag_auto_scan_mode = false;
                button58.Text = "到自動模式";
                lb_main_mesg7.Text = "修改模式";
            }
            else
            {
                timer_stage7.Enabled = true;
                flag_auto_scan_mode = true;
                button58.Text = "到修改模式";
                lb_main_mesg7.Text = "自動模式";
            }

        }

        private void button61_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                timer_stage8.Enabled = false;
                flag_auto_scan_mode = false;
                button61.Text = "到自動模式";
                lb_main_mesg8.Text = "修改模式";
            }
            else
            {
                timer_stage8.Enabled = true;
                flag_auto_scan_mode = true;
                button61.Text = "到修改模式";
                lb_main_mesg8.Text = "自動模式";
            }

        }

        //第六站手動寫入
        private void button51_Click(object sender, EventArgs e)
        {
            int result = check_package1_data();
            if (result == S_OK)
            {
                check_export_data();
            }
            else
            {
                richTextBox1.Text += "資料不齊全, 忽略\n";
                g6.Clear(BackColor);
                g6.DrawString("資料錯誤", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                playSound(S_FALSE);
            }

        }

        //第七站手動寫入
        private void button57_Click(object sender, EventArgs e)
        {
            int result = check_package2_data();
            if (result == S_OK)
            {
                check_export_data();
            }
            else
            {
                richTextBox1.Text += "資料不齊全, 忽略\n";
                g7.Clear(BackColor);
                g7.DrawString("資料錯誤", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                playSound(S_FALSE);
            }

        }

        //第八站手動寫入
        private void button60_Click(object sender, EventArgs e)
        {
            int result = check_package3_data();
            if (result == S_OK)
            {
                check_export_data();
            }
            else
            {
                richTextBox1.Text += "資料不齊全, 忽略\n";
                g8.Clear(BackColor);
                g8.DrawString("資料錯誤", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                playSound(S_FALSE);
            }

        }

        int check_package1_data()
        {
            int i;
            bool flag_incorrect_data = false;

            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;

            flag_incorrect_data = false;
            if (tb_package11.Text.Length == 0)
            {
                richTextBox1.Text += "無資料11\n";
                tb_package11.BackColor = Color.Pink;
            }
            else if (tb_package11.Text.Length == 13)
            {
                for (i = 0; i < tb_package11.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package11.Text[i] < '0') || (tb_package11.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料11格式不正確\n";
                            tb_wait_package1_data.Text = "";
                            tb_package11.Clear();
                            tb_package11.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package11.Text[7] == '-') && (((tb_package11.Text[8] >= 'A') && (tb_package11.Text[8] <= 'Z')) || ((tb_package11.Text[8] >= 'a') && (tb_package11.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料11格式不正確\n";
                        tb_wait_package1_data.Text = "";
                        tb_package11.Clear();
                        tb_package11.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data1 = true;
                    tb_package11.BackColor = Color.White;
                }
                else
                    flag_ok_data1 = false;
            }
            else
            {
                flag_ok_data1 = false;
                tb_package11.Clear();
            }

            flag_incorrect_data = false;
            if (tb_package12.Text.Length == 0)
            {
                richTextBox1.Text += "無資料12\n";
                tb_package12.BackColor = Color.Pink;
            }
            else if (tb_package12.Text.Length == 24)
            {
                for (i = 0; i < tb_package12.Text.Length; i++)
                {
                    if ((i == 7) || (i == 12) || (i == 19))
                    {
                        if (tb_package12.Text[i] != ' ')
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料12格式不正確a\n";
                            tb_wait_package1_data.Text = "";
                            tb_package12.Clear();
                            tb_package12.BackColor = Color.Pink;
                        }
                    }
                    else
                    {
                        if ((tb_package12.Text[i] < '0') || (tb_package12.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料12格式不正確\n";
                            tb_wait_package1_data.Text = "";
                            tb_package12.Clear();
                            tb_package12.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data2 = true;
                    tb_package12.BackColor = Color.White;
                }
                else
                    flag_ok_data2 = false;
            }
            else
            {
                flag_ok_data2 = false;
                tb_package12.Clear();
            }


            flag_incorrect_data = false;
            if (tb_package13.Text.Length == 0)
            {
                richTextBox1.Text += "無資料13\n";
                tb_package13.BackColor = Color.Pink;
            }
            else if (tb_package13.Text.Length == 13)
            {
                for (i = 0; i < tb_package13.Text.Length; i++)
                {
                    if ((tb_package13.Text[i] < '0') || (tb_package13.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料13格式不正確b\n";
                        tb_wait_product_data.Text = "";
                        tb_package13.Clear();
                        tb_package13.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data3 = true;
                    tb_package13.BackColor = Color.White;
                }
                else
                    flag_ok_data3 = false;
            }
            else
            {
                flag_ok_data3 = false;
                tb_package13.Clear();
            }

            if (flag_ok_data1 == true)
                tb_package11.BackColor = Color.White;
            else
                tb_package11.BackColor = Color.Pink;

            if (flag_ok_data2 == true)
                tb_package12.BackColor = Color.White;
            else
                tb_package12.BackColor = Color.Pink;

            if (flag_ok_data3 == true)
                tb_package13.BackColor = Color.White;
            else
                tb_package13.BackColor = Color.Pink;

            if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_ok_data3 == true))
            {
                richTextBox1.Text += "資料齊全\n";
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料未齊全\n";
                return S_FALSE;
            }
        }

        int check_package2_data()
        {
            int i;
            bool flag_incorrect_data = false;

            flag_ok_data1 = false;
            flag_ok_data2 = false;

            flag_incorrect_data = false;
            if (tb_package21.Text.Length == 0)
            {
                richTextBox1.Text += "無資料21\n";
                tb_package21.BackColor = Color.Pink;
            }
            else if (tb_package21.Text.Length == 13)
            {
                for (i = 0; i < tb_package21.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package21.Text[i] < '0') || (tb_package21.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料21格式不正確\n";
                            tb_wait_package2_data.Text = "";
                            tb_package21.Clear();
                            tb_package21.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package21.Text[7] == '-') && (((tb_package21.Text[8] >= 'A') && (tb_package21.Text[8] <= 'Z')) || ((tb_package21.Text[8] >= 'a') && (tb_package21.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料21格式不正確\n";
                        tb_wait_package2_data.Text = "";
                        tb_package21.Clear();
                        tb_package21.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data1 = true;
                    tb_package21.BackColor = Color.White;
                }
                else
                    flag_ok_data1 = false;
            }
            else
            {
                flag_ok_data1 = false;
                tb_package21.Clear();
            }

            flag_incorrect_data = false;
            if (tb_package22.Text.Length == 0)
            {
                richTextBox1.Text += "無資料22\n";
                tb_package22.BackColor = Color.Pink;
            }
            else if (tb_package22.Text.Length == 13)
            {
                for (i = 0; i < tb_package22.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package22.Text[i] < '0') || (tb_package22.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料22格式不正確\n";
                            tb_wait_package2_data.Text = "";
                            tb_package22.Clear();
                            tb_package22.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package22.Text[7] == '-') && (((tb_package22.Text[8] >= 'A') && (tb_package22.Text[8] <= 'Z')) || ((tb_package22.Text[8] >= 'a') && (tb_package22.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料22格式不正確\n";
                        tb_wait_package2_data.Text = "";
                        tb_package22.Clear();
                        tb_package22.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data2 = true;
                    tb_package22.BackColor = Color.White;
                }
                else
                    flag_ok_data2 = false;
            }
            else
            {
                flag_ok_data2 = false;
                tb_package22.Clear();
            }

            if (flag_ok_data1 == true)
                tb_package21.BackColor = Color.White;
            else
                tb_package21.BackColor = Color.Pink;

            if (flag_ok_data2 == true)
                tb_package22.BackColor = Color.White;
            else
                tb_package22.BackColor = Color.Pink;

            if ((flag_ok_data1 == true) && (flag_ok_data2 == true))
            {
                richTextBox1.Text += "資料齊全\n";
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料未齊全\n";
                return S_FALSE;
            }
        }

        int check_package3_data()
        {
            int i;
            bool flag_incorrect_data = false;

            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;

            flag_incorrect_data = false;
            if (tb_package31.Text.Length == 0)
            {
                richTextBox1.Text += "無資料31\n";
                tb_package31.BackColor = Color.Pink;
            }
            else if (tb_package31.Text.Length == 13)
            {
                for (i = 0; i < tb_package31.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package31.Text[i] < '0') || (tb_package31.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料31格式不正確\n";
                            tb_wait_package3_data.Text = "";
                            tb_package31.Clear();
                            tb_package31.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package31.Text[7] == '-') && (((tb_package31.Text[8] >= 'A') && (tb_package31.Text[8] <= 'Z')) || ((tb_package31.Text[8] >= 'a') && (tb_package31.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料31格式不正確\n";
                        tb_wait_package3_data.Text = "";
                        tb_package31.Clear();
                        tb_package31.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data1 = true;
                    tb_package31.BackColor = Color.White;
                    richTextBox1.Text += "White\n";
                }
                else
                    flag_ok_data1 = false;
            }
            else
            {
                flag_ok_data1 = false;
                tb_package31.Clear();
            }

            flag_incorrect_data = false;
            if (tb_package32.Text.Length == 0)
            {
                richTextBox1.Text += "無資料32\n";
                tb_package32.BackColor = Color.Pink;
            }
            else if (tb_package32.Text.Length == 13)
            {
                for (i = 0; i < tb_package32.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package32.Text[i] < '0') || (tb_package32.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料32格式不正確\n";
                            tb_wait_package3_data.Text = "";
                            tb_package32.Clear();
                            tb_package32.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package32.Text[7] == '-') && (((tb_package32.Text[8] >= 'A') && (tb_package32.Text[8] <= 'Z')) || ((tb_package32.Text[8] >= 'a') && (tb_package32.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料32格式不正確\n";
                        tb_wait_package3_data.Text = "";
                        tb_package32.Clear();
                        tb_package32.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data2 = true;
                    tb_package32.BackColor = Color.White;
                }
                else
                    flag_ok_data2 = false;
            }
            else
            {
                flag_ok_data2 = false;
                tb_package32.Clear();
            }


            flag_incorrect_data = false;
            if (tb_package33.Text.Length == 0)
            {
                richTextBox1.Text += "無資料33\n";
                tb_package33.BackColor = Color.Pink;
            }
            else if (tb_package33.Text.Length == 13)
            {
                for (i = 0; i < tb_package33.Text.Length; i++)
                {
                    if ((i != 7) && (i != 8))
                    {
                        if ((tb_package33.Text[i] < '0') || (tb_package33.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料33格式不正確\n";
                            tb_wait_package3_data.Text = "";
                            tb_package33.Clear();
                            tb_package33.BackColor = Color.Pink;
                        }
                    }
                }

                if (flag_incorrect_data == false)
                {
                    if ((tb_package33.Text[7] == '-') && (((tb_package33.Text[8] >= 'A') && (tb_package33.Text[8] <= 'Z')) || ((tb_package33.Text[8] >= 'a') && (tb_package33.Text[8] <= 'z'))))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "資料33格式不正確\n";
                        tb_wait_package3_data.Text = "";
                        tb_package33.Clear();
                        tb_package33.BackColor = Color.Pink;
                    }
                }

                if (flag_incorrect_data == false)
                {
                    flag_ok_data3 = true;
                    tb_package33.BackColor = Color.White;
                }
                else
                    flag_ok_data3 = false;
            }
            else
            {
                flag_ok_data3 = false;
                tb_package33.Clear();
            }

            if (flag_ok_data1 == true)
                tb_package31.BackColor = Color.White;
            else
                tb_package31.BackColor = Color.Pink;

            if (flag_ok_data2 == true)
                tb_package32.BackColor = Color.White;
            else
                tb_package32.BackColor = Color.Pink;

            if (flag_ok_data3 == true)
                tb_package33.BackColor = Color.White;
            else
                tb_package33.BackColor = Color.Pink;

            if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_ok_data3 == true))
            {
                richTextBox1.Text += "資料齊全\n";
                return S_OK;
            }
            else
            {
                richTextBox1.Text += "資料未齊全\n";
                return S_FALSE;
            }
        }

        private void timer_stage3_Tick(object sender, EventArgs e)
        {
            if (flag_network_disk_status == false)
            {
                tb_wait_sn_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if (flag_stage3_step == 0)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg2.Text = "判定等級 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg2.Text = "判定等級 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg2.Text = "判定等級 /";
                else
                    lb_main_mesg2.Text = "判定等級 -";
            }
            else
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg2.Text = "輸入相機序號 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg2.Text = "輸入相機序號 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg2.Text = "輸入相機序號 /";
                else
                    lb_main_mesg2.Text = "輸入相機序號 -";
            }

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "三";
                if (this.tb_wait_sn_data.Focused == false)
                {
                    this.tb_wait_sn_data.Focus();
                    richTextBox1.Text += "F3";
                }
                this.tb_sn_opal.BackColor = Color.Pink;
            }

            int result = check_tb_sn_opal_data();
            if (result == S_OK)
            {
                timer_stage3.Enabled = false;
                lb_main_mesg2.Text = "資料正確, 存檔中";
                save_image_to_drive();
                delay(30);
                timer_stage3.Enabled = true;
            }

            int len;
            len = tb_wait_sn_data.Text.Length;

            if (len > 50)   //太長, 直接放棄
            {
                tb_wait_sn_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 2)    //檢查是否換行
            {
                if ((tb_wait_sn_data.Text[len - 2] == 0x0D) || (tb_wait_sn_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_sn_data.Text = tb_wait_sn_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            if (tb_wait_sn_data.Text.Length > 0)
            {
                if (tb_wait_sn_data.Text.Length == 1)
                {
                    if (tb_wait_sn_data.Text[0] == 'A')
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else if (tb_wait_sn_data.Text[0] == 'B')
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else if (tb_wait_sn_data.Text[0] == 'C')
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else if (tb_wait_sn_data.Text[0] == 'E')
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else if (tb_wait_sn_data.Text[0] == 'F')
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else
                    {
                        lb_class.Text = "不允許" + tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "錯誤判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 0;
                    }
                }
                else if (tb_wait_sn_data.Text.Length == 2)
                {
                    if ((tb_wait_sn_data.Text[0] == 'N') && (tb_wait_sn_data.Text[1] == 'G'))
                    {
                        lb_class.Text = tb_wait_sn_data.Text[0].ToString() + tb_wait_sn_data.Text[1].ToString();
                        richTextBox1.Text += "判定為" + tb_wait_sn_data.Text[0].ToString() + tb_wait_sn_data.Text[1].ToString() + "\n";
                        flag_stage3_step = 1;
                    }
                    else
                    {
                        lb_class.Text = "不允許" + tb_wait_sn_data.Text[0].ToString();
                        richTextBox1.Text += "錯誤判定為" + tb_wait_sn_data.Text[0].ToString() + "\n";
                        flag_stage3_step = 0;
                    }
                }
                else if ((tb_wait_sn_data.Text.Length == 9) || (tb_wait_sn_data.Text.Length == 10))
                {
                    if (flag_stage3_step == 0)
                    {
                        show_main_message1("未判定等級", S_OK, 30);
                        show_main_message2("未判定等級", S_OK, 30);
                    }
                    else
                    {
                        show_main_message2("準備存檔", S_OK, 10);
                        tb_sn_opal.Text = tb_wait_sn_data.Text;
                    }
                }
                else
                {
                    show_main_message2("資料錯誤", S_OK, 10);
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                }
                tb_wait_sn_data.Clear();
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //改成mode2不允許手動調整
            //if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
            if (flag_operation_mode == MODE_RELEASE_STAGE0)
            {
                tb_sn_opal.Clear();
                timer_stage2.Enabled = true;
                timer_webcam_mode = FOCUS_ON_PICTURE;
                this.tb_sn_opal.BackColor = Color.White;
                if (this.pictureBox1.Focused == false)
                    this.pictureBox1.Focus();
                show_main_message1("移動方塊", S_OK, 10);
                show_main_message2("移動方塊", S_OK, 10);
                show_main_message3("移動方塊", S_OK, 10);
            }
        }

        private void timer_stage1_Tick(object sender, EventArgs e)
        {
            if (flag_network_disk_status == false)
            {
                tb_sn_opal.Clear();
                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            if (flag_network_disk_status == true)
            {
                ccc++;
                if (flag_wait_for_ng_reason == true)
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg2.Text = "等待輸入NG原因 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg2.Text = "等待輸入NG原因 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg2.Text = "等待輸入NG原因 /";
                    else
                        lb_main_mesg2.Text = "等待輸入NG原因 -";
                    if(tb_reason_stage1.Focused == false)
                        tb_reason_stage1.Focus();
                }
                else
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg2.Text = "等待輸入相機序號 或 NG原因 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg2.Text = "等待輸入相機序號 或 NG原因 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg2.Text = "等待輸入相機序號 或 NG原因 /";
                    else
                        lb_main_mesg2.Text = "等待輸入相機序號 或 NG原因 -";
                }
            }

            if (flag_wait_for_ng_reason == false)
            {
                if ((timer_cnt++ % 10) == 0)
                {
                    richTextBox1.Text += "一";
                    if (this.tb_sn_opal.Focused == false)
                    {
                        this.tb_sn_opal.Focus();
                        richTextBox1.Text += "F1";
                    }
                    this.tb_sn_opal.BackColor = Color.Pink;
                }
            }

            if (flag_wait_for_ng_reason == false)
            {
                int result = check_tb_sn_opal_data_stage1();
                if (result == S_OK)
                {
                    timer_stage1.Enabled = false;
                    lb_main_mesg2.Text = "資料正確, 存檔中";
                    save_image_to_drive();
                    delay(30);
                    timer_stage1.Enabled = true;
                    flag_wait_for_ng_reason = false;
                    gb_ng_reason1.Visible = false;
                    cb_stage1_ng.Checked = false;
                    cb_stage1_ng.ForeColor = Color.Black;
                    lb_ng_reason.Text = "";
                }
            }
            return;
        }

        int check_pattern(string ptn, int type)
        {
            /*  type
                Opal序號		sn1 相機序號
                廠內生產製令序號	sn2

                MODE_RELEASE_STAGE5
                ERP-SN
                PI-SN
                BOX-Lot

                MODE_RELEASE_STAGE6
                主機序號
                小PCBA序號
                大PCBA序號

                MODE_RELEASE_STAGE7

                Dongle包裝
                Dongle序號

                MODE_RELEASE_STAGE8

                成品包裝序號
                主機序號
                Dongle包裝
             */


            return S_OK;
        }

        private void timer_stage9_Tick(object sender, EventArgs e)
        {
            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if ((flag_operation_mode == MODE_RELEASE_STAGE11) && (checkBox1.Checked == true) && (flag_ng_reason1 == false) && (flag_ng_reason2 == false) && (flag_ng_reason3 == false))
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg9.Text = "等待勾選 NG原因 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg9.Text = "等待勾選 NG原因 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg9.Text = "等待勾選 NG原因 /";
                else
                    lb_main_mesg9.Text = "等待勾選 NG原因 -";
            }
            else if ((flag_operation_mode == MODE_RELEASE_STAGE11) && (checkBox1.Checked == true) && (flag_ng_reason3 == true) && (flag_wait_for_ng_reason == true))
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg9.Text = "等待輸入 NG其他原因 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg9.Text = "等待輸入 NG其他原因 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg9.Text = "等待輸入 NG其他原因 /";
                else
                    lb_main_mesg9.Text = "等待輸入 NG其他原因 -";
            }
            else if ((flag_ok_data1 == false) && (flag_ok_data1 == false))
            {
                if (tb_sale1.Focused == true)
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg9.Text = "等待輸入 單別 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg9.Text = "等待輸入 單別 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg9.Text = "等待輸入 單別 /";
                    else
                        lb_main_mesg9.Text = "等待輸入 單別 -";
                }
                else
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg9.Text = "等待輸入 單號 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg9.Text = "等待輸入 單號 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg9.Text = "等待輸入 單號 /";
                    else
                        lb_main_mesg9.Text = "等待輸入 單號 -";
                }
            }
            else if (flag_ok_data1 == false)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg9.Text = "等待輸入 單別 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg9.Text = "等待輸入 單別 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg9.Text = "等待輸入 單別 /";
                else
                    lb_main_mesg9.Text = "等待輸入 單別 -";
            }
            else if (flag_ok_data2 == false)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg9.Text = "等待輸入 單號 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg9.Text = "等待輸入 單號 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg9.Text = "等待輸入 單號 /";
                else
                    lb_main_mesg9.Text = "等待輸入 單號 -";
            }
            else
            {
                if (tb_sale1.Focused == true)
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg9.Text = "等待輸入 單別 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg9.Text = "等待輸入 單別 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg9.Text = "等待輸入 單別 /";
                    else
                        lb_main_mesg9.Text = "等待輸入 單別 -";
                }
                else if (tb_sale2.Focused == true)
                {
                    if ((ccc % 4) == 0)
                        lb_main_mesg9.Text = "等待輸入 單號 \\";
                    else if ((ccc % 4) == 1)
                        lb_main_mesg9.Text = "等待輸入 單號 |";
                    else if ((ccc % 4) == 2)
                        lb_main_mesg9.Text = "等待輸入 單號 /";
                    else
                        lb_main_mesg9.Text = "等待輸入 單號 -";
                }
                else
                {
                    if (flag_operation_mode == MODE_RELEASE_STAGE9)
                    {
                        if ((ccc % 4) == 0)
                            lb_main_mesg9.Text = "等待輸入 箱號或序號 \\";
                        else if ((ccc % 4) == 1)
                            lb_main_mesg9.Text = "等待輸入 箱號或序號 |";
                        else if ((ccc % 4) == 2)
                            lb_main_mesg9.Text = "等待輸入 箱號或序號 /";
                        else
                            lb_main_mesg9.Text = "等待輸入 箱號或序號 -";
                    }
                    else
                    {
                        if ((ccc % 4) == 0)
                            lb_main_mesg9.Text = "等待輸入 序號 \\";
                        else if ((ccc % 4) == 1)
                            lb_main_mesg9.Text = "等待輸入 序號 |";
                        else if ((ccc % 4) == 2)
                            lb_main_mesg9.Text = "等待輸入 序號 /";
                        else
                            lb_main_mesg9.Text = "等待輸入 序號 -";
                    }
                }
                if (tb_sale3.Focused == true)
                    tb_sale3.BackColor = Color.Pink;
                else
                    tb_sale3.BackColor = Color.White;

                /*
                if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_wait_for_ng_reason == false))
                {
                    tb_sale3.Focus();
                    richTextBox1.Text += "G";
                }
                */
            }

            if ((timer_cnt++ % 10) == 0)
            {
                if (flag_operation_mode == MODE_RELEASE_STAGE9)
                    richTextBox1.Text += "九";
                else
                    richTextBox1.Text += "十一";

                if ((flag_ok_data1 == false) && (flag_ok_data2 == false) && (flag_wait_for_ng_reason == false))
                {
                    if ((tb_sale1.Focused == false) && (tb_sale2.Focused == false))
                    {
                        if (tb_sale1.Focused == false)
                        {
                            tb_sale1.Focus();
                            if (flag_operation_mode == MODE_RELEASE_STAGE9)
                                richTextBox1.Text += "F9";
                            else
                                richTextBox1.Text += "F11";
                        }
                    }
                }
                else if ((flag_ok_data1 == true) && (flag_ok_data2 == true) && (flag_wait_for_ng_reason == false))
                {
                    if (tb_sale3.Focused == false)
                    {
                        tb_sale3.Focus();
                        if (flag_operation_mode == MODE_RELEASE_STAGE9)
                            richTextBox1.Text += "f9";
                        else
                            richTextBox1.Text += "f11";
                    }
                }
            }

            if (flag_operation_mode == MODE_RELEASE_STAGE11)
            {
                if (checkBox1.Checked == true)
                {
                    if ((flag_ng_reason1 == false) && (flag_ng_reason2 == false) && (flag_ng_reason3 == false))
                    {
                        if (tb_sale3.Text.Length > 0)
                        {
                            tb_sale3.Clear();
                            richTextBox1.Text += "尚未選擇NG原因，清除tb_sale3資料\n";
                            g9.Clear(BackColor);
                            g9.DrawString("    ", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                        }
                    }
                    else if ((flag_ng_reason3 == true) && (flag_wait_for_ng_reason == true))
                    {
                        richTextBox1.Text += "尚未輸入NG原因，清除tb_sale3資料\n";
                        g9.Clear(BackColor);
                        g9.DrawString("    ", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                    }


                }


            }

            if (flag_network_disk_status == false)
            {
                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
            }

            check_tb_sale1_data();
            check_tb_sale2_data();

            int len;
            len = tb_sale3.Text.Length;

            if ((flag_ok_data1 == false) || (flag_ok_data1 == false))
            {
                if (len > 0)
                {
                    show_main_message1("請先輸入單別單號", S_FALSE, 30);
                    tb_sale3.Clear();
                }
                return;
            }

            if (len > 45)   //太長, 直接放棄
            {
                tb_sale3.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_sale3.Text[len - 2] == 0x0D) || (tb_sale3.Text[len - 1] == 0x0A))
                {
                    tb_sale3.Text = tb_sale3.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            int ret;
            if (flag_operation_mode == MODE_RELEASE_STAGE9)
            {
                ret = check_sale3_data();
            }
            else
            {
                ret = check_tb_sn_opal_data2();
            }
            if (ret == S_OK)
                check_export_data();
        }

        private void button62_Click(object sender, EventArgs e)
        {
            tb_sale1.Clear();
            tb_sale2.Clear();
            tb_sale3.Clear();
            tb_sale1.BackColor = Color.Pink;
            tb_sale2.BackColor = Color.Pink;
            tb_sale3.BackColor = Color.White;
            flag_ok_data1 = false;
            flag_ok_data2 = false;
            flag_ok_data3 = false;
            if (tb_sale1.Focused == false)
                tb_sale1.Focus();
        }

        //第九站手動寫入
        private void button63_Click(object sender, EventArgs e)
        {
            int ret1 = check_tb_sale1_data();
            int ret2 = check_tb_sale2_data();

            if ((ret1 == S_FALSE) && (ret2 == S_FALSE))
            {
                show_main_message1("請先輸入單別單號", S_FALSE, 30);
            }
            else if (ret1 == S_FALSE)
            {
                show_main_message1("請先輸入單別", S_FALSE, 30);
            }
            else if (ret2 == S_FALSE)
            {
                show_main_message1("請先輸入單號", S_FALSE, 30);
            }
            else
            {
                int ret = check_sale3_data();
                if (ret == S_OK)
                    check_export_data();
                else
                {
                    if (tb_sale3.Focused == false)
                        tb_sale3.Focus();
                    tb_sale3.BackColor = Color.Pink;
                    richTextBox1.Text += "資料不齊全, 忽略\n";
                    g9.Clear(BackColor);
                    g9.DrawString("資料錯誤", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                    playSound(S_FALSE);
                }
            }
        }

        private void button64_Click(object sender, EventArgs e)
        {
            if (flag_auto_scan_mode == true)
            {
                timer_stage9.Enabled = false;
                flag_auto_scan_mode = false;
                button64.Text = "到自動模式";
                lb_main_mesg9.Text = "修改模式";
            }
            else
            {
                timer_stage9.Enabled = true;
                flag_auto_scan_mode = true;
                button64.Text = "到修改模式";
                lb_main_mesg9.Text = "自動模式";
            }
        }

        private void tb_check_decimal_value_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void tb_sale1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                if (check_tb_sale1_data() == S_OK)
                {
                    if (flag_ok_data2 == false)
                    {
                        if (tb_sale2.Focused == false)
                            tb_sale2.Focus();
                        tb_sale3.BackColor = Color.White;
                    }
                    else
                    {
                        tb_sale3.BackColor = Color.Pink;
                        if (tb_sale3.Focused == false)
                            tb_sale3.Focus();
                    }
                }
            }
            else
            {
                e.Handled = true;
            }

        }

        int check_tb_sale1_data()
        {
            if ((tb_sale1.Text.Length > 0) && (tb_sale1.Text.Length < 5))
            {
                int value = int.Parse(tb_sale1.Text);
                if ((value >= 1000) && (value <= 9999))
                {
                    //richTextBox1.Text += "OK data 1 = " + value.ToString() + "\n";
                    tb_sale1.BackColor = Color.White;
                    flag_ok_data1 = true;
                    return S_OK;
                }
                else
                {
                    //richTextBox1.Text += "FAIL data 1 = " + value.ToString() + "\n";
                    tb_sale1.BackColor = Color.Pink;
                    flag_ok_data1 = false;
                    return S_FALSE;
                }
            }
            else
            {
                tb_sale1.BackColor = Color.Pink;
                flag_ok_data1 = false;
                return S_FALSE;
            }
        }

        private void tb_sale2_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                if (check_tb_sale2_data() == S_OK)
                {
                    if (flag_ok_data1 == false)
                    {
                        if (tb_sale1.Focused == false)
                            tb_sale1.Focus();
                        tb_sale3.BackColor = Color.White;
                    }
                    else
                    {
                        if (tb_sale3.Focused == false)
                            tb_sale3.Focus();
                        tb_sale3.BackColor = Color.Pink;
                    }
                }
            }
            else
            {
                e.Handled = true;
            }

        }

        int check_tb_sale2_data()
        {
            if ((tb_sale2.Text.Length > 0) && (tb_sale2.Text.Length < 8))
            {
                int value = int.Parse(tb_sale2.Text);
                if ((value >= 1000000) && (value <= 9999999))
                {
                    //richTextBox1.Text += "OK data 2 = " + value.ToString() + "\n";
                    tb_sale2.BackColor = Color.White;
                    flag_ok_data2 = true;
                    return S_OK;
                }
                else
                {
                    //richTextBox1.Text += "FAIL data 2 = " + value.ToString() + "\n";
                    tb_sale2.BackColor = Color.Pink;
                    flag_ok_data2 = false;
                    return S_FALSE;
                }
            }
            else
            {
                tb_sale2.BackColor = Color.Pink;
                flag_ok_data2 = false;
                return S_FALSE;
            }
        }

        private void tb_sale3_MouseClick(object sender, MouseEventArgs e)
        {
            int ret1 = check_tb_sale1_data();
            int ret2 = check_tb_sale2_data();

            if ((ret1 == S_FALSE) && (ret2 == S_FALSE))
            {
                show_main_message1("請先輸入單別單號", S_FALSE, 30);
            }
            else if (ret1 == S_FALSE)
            {
                show_main_message1("請先輸入單別", S_FALSE, 30);
            }
            else if (ret2 == S_FALSE)
            {
                show_main_message1("請先輸入單號", S_FALSE, 30);
            }
            else
            {
                if (tb_sale3.Focused == false)
                    tb_sale3.Focus();
                tb_sale3.BackColor = Color.Pink;
            }

        }

        int check_sale3_data()
        {
            tb_sale3.Text = tb_sale3.Text.Trim();
            if (tb_sale3.Text.Length > 0)
            {
                //richTextBox1.Text += "len = " + tb_sale3.Text.Length.ToString() + "\n";
                int i;
                bool flag_incorrect_data = false;
                /*
                if (tb_sale3.Text.Length == 11)
                {
                    for (i = 0; i < tb_sale3.Text.Length; i++)
                    {
                        if ((tb_sale3.Text[i] < '0') || (tb_sale3.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "序號格式不正確\n";
                            tb_sale3.Clear();
                            tb_sale3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得序號 : " + tb_sale3.Text + "\n";
                        tb_sale3.BackColor = Color.Pink;
                        flag_ok_data3 = true;
                        //check_export_data();
                    }
                }
                */
                if ((tb_sale3.Text.Length == 38) || (tb_sale3.Text.Length == 39))
                {
                    for (i = 0; i < tb_sale3.Text.Length; i++)
                    {
                        if ((tb_sale3.Text[i] < '0') || (tb_sale3.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "資料格式不正確\n";
                            tb_sale3.Clear();
                            tb_sale3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得序號 : " + tb_sale3.Text + "\n";
                        tb_sale3.BackColor = Color.Pink;
                        flag_ok_data3 = true;
                        //check_export_data();
                    }
                }
                else if (tb_sale3.Text.Length == 19)
                {
                    for (i = 0; i < tb_sale3.Text.Length; i++)
                    {
                        if ((i == 6) || (i == 14))
                        {
                            if (tb_sale3.Text[i] != '-')
                            {
                                flag_incorrect_data = true;
                                richTextBox1.Text += "箱號格式不正確a\n";
                                tb_sale3.Clear();
                                tb_sale3.BackColor = Color.Pink;
                            }
                        }
                        else if ((tb_sale3.Text[i] < '0') || (tb_sale3.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "箱號格式不正確b\n";
                            tb_sale3.Clear();
                            tb_sale3.BackColor = Color.Pink;
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "取得箱號 : " + tb_sale3.Text + "\n";
                        tb_sale3.BackColor = Color.Pink;
                        flag_ok_data3 = true;
                        //check_export_data();
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "有資料, 但是長度錯誤, 一律清除\n";
                    tb_sale3.Clear();
                    tb_sale3.BackColor = Color.Pink;
                }

                if (flag_incorrect_data == false)
                    return S_OK;
                else
                    return S_FALSE;
            }
            else
                return S_FALSE;
        }

        private void bt_awb_break_Click(object sender, EventArgs e)
        {
            if (bt_awb_break.Text == "中斷")
            {
                bt_awb_break.Text = "確認";
                tb_awb_mesg.Text = "色彩校正中斷";
                richTextBox1.Text += "AWB 中斷 AWB 中斷 AWB 中斷\n";
                flag_break_doing_awb = true;
                flag_awb_break = true;
                flag_awb_manually_interrupt = true;
            }
            else if (bt_awb_break.Text == "確認")
            {
                richTextBox1.Text += "AWB 中斷 確認\n";
                bt_awb_break.Text = "中斷";
                //tb_awb_mesg.Text = "";
                bt_awb_break.Visible = false;

                bt_awb_test.BackColor = Color.Lime;
                flag_do_awb = false;
                timer_display.Enabled = false;

                flag_doing_awb = false;
                bt_awb_test.Enabled = true;
                flag_do_find_awb_location_fail = false;
                flag_do_find_awb_location_fail_too_small = false;
                flag_do_find_awb_location_fail_too_far = false;

                lb_awb_time.Text = "";
                restore_camera_setup();
                timer_stage2.Enabled = true;
                Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode

                tb_awb_mesg.Text = "";
                tb_awb_mesg.Font = new Font("標楷體", 24);
                tb_awb_mesg.BackColor = Color.White;

                if (flag_operation_mode == MODE_RELEASE_STAGE2)
                {
                    bt_awb_test.Enabled = false;
                    bt_awb_test.BackColor = Color.Pink;
                    flag_wait_for_confirm = false;
                }
                flag_awb_break = false;
                flag_awb_timeout = false;
                flag_awb_manually_interrupt = false;
            }
            else
            {
                richTextBox1.Text += "bt_awb_break_Click XXXXXXXXXXXXXXXXXXXXXXXXX\n";
            }
        }

        private void bt_tmp_Click(object sender, EventArgs e)
        {
            int do_awb_result = 0;
            lb_auto_awb_cnt.Visible = true;
            richTextBox1.Text += "\n自動測試AWB ST, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB開始";
            awb_cnt = 0;

            for (current_test_count = 1; current_test_count <= total_test_count; current_test_count++)
            {
                lb_auto_awb_cnt.Text = current_test_count.ToString();
                do_awb_result = do_awb(sender, e);
                check_awb_result(do_awb_result);
            }
            lb_auto_awb_cnt.Visible = false;
            richTextBox1.Text += "\n自動測試AWB SP, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB結束";
        }

        void clear_group_ng_reason_data()
        {
            cb_reason1.Checked = false;
            cb_reason2.Checked = false;
            cb_reason3.Checked = false;
            tb_reason.Clear();
            tb_reason.BackColor = Color.White;
            flag_wait_for_ng_reason = false;
            flag_ng_reason1 = false;
            flag_ng_reason2 = false;
            flag_ng_reason3 = false;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                flag_cancel_data = true;
                gb_ng_reason.Enabled = true;
                checkBox1.ForeColor = Color.Red;
                gb_ng_reason.Focus();
            }
            else
            {
                flag_cancel_data = false;
                gb_ng_reason.Enabled = false;
                checkBox1.ForeColor = Color.Black;
                tb_sale3.Focus();
            }
            clear_group_ng_reason_data();
        }

        int find_awb_location()
        {
            int result = 0;
            int x_st = 0;
            int y_st = 0;
            int ww = 0;
            int hh = 0;
            int w;
            int h;
            int i;
            int j;
            Color p;
            Bitmap bm2 = null;
            int th_h = (int)numericUpDown_find_brightness_h.Value;
            int th_l = (int)numericUpDown_find_brightness_l.Value;

            tb_awb_mesg.Text = "尋找AWB區域ST";

            if (cb_show_grid.Checked == true)
            {
                cb_show_grid.Checked = false;
                delay(100);
            }

            flag_do_find_awb_location = true;

            //歸零
            flag_right_left_cnt = 0;
            flag_down_up_cnt = 0;
            flag_right_left_point_cnt = 0;
            flag_down_up_point_cnt = 0;
            awb_block = 32;
            step = 1;
            add_amount = 1;
            add_tmp = 0;
            ww = awb_block;
            hh = awb_block;
            refresh_picturebox2();
            delay(10);

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm2 = bm;
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                ga = Graphics.FromImage(bm2);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f2 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                w = bm2.Width;
                h = bm2.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f3 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;

            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > h)
                y_st = h - hh;

            /*
            try
            {
                if (timer_webcam_mode == FOCUS_ON_PICTURE)
                {
                    gg.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
                    gg.DrawRectangle(new Pen(Color.Red, 10), 0, 0, pictureBox1.Width / 2, pictureBox1.Height / 2);
                }
                else
                    gg.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f4 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }
            */

            flag_do_find_awb_location = true;
            delay(10);

            pictureBox1.Image = bm2;

            delay(100);

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm2 = bm;
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f5 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                ga = Graphics.FromImage(bm2);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f6 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                w = bm2.Width;
                h = bm2.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f7 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            x_st = w / 2 - awb_window_size / 2;
            y_st = h / 2 - awb_window_size / 2;

            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;

            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > h)
                y_st = h - hh;

            for (j = 0; j < awb_window_size; j++)
            {
                for (i = 0; i < awb_window_size; i++)
                {
                    p = bm2.GetPixel(x_st + i, y_st + j);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    if (yyy.Y > th_h)
                    {
                        bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                    }
                    else if (yyy.Y < th_l)
                    {
                        bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                    }
                    else
                    {
                    }
                    //bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                }
            }

            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;

            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > h)
                y_st = h - hh;

            bool flag_break = false;

            while(true)
            {
                if(cb_show_progress.Checked == true)
                    delay(10);

                flag_break = false;
                for (j = y_st; j < (y_st + awb_block); j++)
                {
                    for (i = x_st; i < (x_st + awb_block); i++)
                    {
                        p = bm2.GetPixel(i, j);

                        if (p.R == 255) //which was labeled Red
                        {
                            //catch red point, prepare to break, search next time
                            if (step == 1)
                            {
                                //flag_right_left_point_cnt += add_amount;
                                flag_right_left_point_cnt += awb_auto_step;
                                add_tmp++;
                                if (add_tmp == (add_amount * 2 - 1))
                                {
                                    add_tmp = 0;
                                    step = 2;
                                }
                                //richTextBox1.Text += "E";
                            }
                            else if (step == 2)
                            {
                                //flag_down_up_point_cnt += add_amount;
                                flag_down_up_point_cnt += awb_auto_step;
                                add_tmp++;
                                if (add_tmp == (add_amount * 2 - 1))
                                {
                                    add_tmp = 0;
                                    step = 3;
                                }
                                //richTextBox1.Text += "S";
                            }
                            else if (step == 3)
                            {
                                //flag_right_left_point_cnt -= (add_amount + 1);
                                flag_right_left_point_cnt -= awb_auto_step;
                                add_tmp++;
                                if (add_tmp == (add_amount * 2))
                                {
                                    add_tmp = 0;
                                    step = 4;
                                }
                                //richTextBox1.Text += "W";
                            }
                            else if (step == 4)
                            {
                                //flag_down_up_point_cnt -= (add_amount + 1);
                                flag_down_up_point_cnt -= awb_auto_step;
                                add_tmp++;
                                if (add_tmp == (add_amount * 2))
                                {
                                    add_tmp = 0;
                                    step = 1;
                                    add_amount++;
                                }
                                //richTextBox1.Text += "N";
                            }
                            if ((((Math.Abs(flag_right_left_point_cnt) + awb_block) > awb_window_size / 2) || ((Math.Abs(flag_down_up_point_cnt) + awb_block) > awb_window_size / 2)))
                            {
                                if (awb_block >= 8)
                                {
                                    //richTextBox1.Text += "awb_block old = " + awb_block.ToString() + "\n";
                                    awb_block -= 4;
                                    //richTextBox1.Text += "awb_block new = " + awb_block.ToString() + "\n";
                                    //richTextBox1.Text += "flag_down_up_cnt = " + flag_down_up_cnt.ToString() + ", flag_right_left_cnt = " + flag_right_left_cnt.ToString() + "\n";
                                    //richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() + ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";

                                    flag_right_left_cnt = 0;
                                    flag_down_up_cnt = 0;
                                    flag_right_left_point_cnt = 0;
                                    flag_down_up_point_cnt = 0;
                                    step = 1;
                                    add_amount = 1;
                                    add_tmp = 0;
                                }
                            }

                            ww = awb_block;
                            hh = awb_block;

                            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                            if (x_st < 0)
                                x_st = 0;
                            if ((x_st + ww) > w)
                                x_st = w - ww;

                            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
                            if (y_st < 0)
                                y_st = 0;
                            if ((y_st + hh) > h)
                                y_st = h - hh;

                            if (cb_show_progress.Checked == true)
                            {
                                try
                                {
                                    ga.DrawRectangle(new Pen(Color.Silver, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);
                                    pictureBox1.Image = bm2;
                                }
                                catch (Exception ex)
                                {
                                    richTextBox1.Text += "xxx錯誤訊息f9 : " + ex.Message + "\n";
                                    GC.Collect();       //回收資源
                                    flag_do_find_awb_location = false;
                                    return S_FALSE;
                                }
                            }

                            //refresh_picturebox2();
                            //richTextBox1.Text += "break, flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() + ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
                            flag_break = true;
                            break;
                        }
                        if (flag_break_doing_awb == true)
                        {
                            result = REASON_MANUALLY_INTERRUPT;
                            break;
                        }
                    }
                    if (flag_break == true)
                        break;
                    if (flag_break_doing_awb == true)
                    {
                        result = REASON_MANUALLY_INTERRUPT;
                        break;
                    }
                }

                if (flag_break_doing_awb == true)
                {
                    result = REASON_MANUALLY_INTERRUPT;
                    return result;
                }

                if (flag_break == false)
                {
                    tb_awb_mesg.Text = "尋找AWB區域SP";
                    richTextBox1.Text += "FIND OUT AWB LOCATION\n";

                    x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
                    if (x_st < 0)
                        x_st = 0;
                    if ((x_st + ww) > w)
                        x_st = w - ww;

                    y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
                    if (y_st < 0)
                        y_st = 0;
                    if ((y_st + hh) > h)
                        y_st = h - hh;

                    delay(10);

                    //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
                    //richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
                    //richTextBox1.Text += "awb_block = " + awb_block.ToString() + ", awb_block = " + awb_block.ToString() + "\n";

                    /*
                    try
                    {
                        ga.DrawRectangle(new Pen(Color.Green, 1), x_st - 2, y_st - 2, awb_block + 4, awb_block + 4);
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息fa : " + ex.Message + "\n";
                        GC.Collect();       //回收資源
                        flag_do_find_awb_location = false;
                        return S_FALSE;
                    }
                    */
                    
                    pictureBox1.Image = bm2;
                    refresh_picturebox2();
                    delay(100);

                    break;
                }
            }

            GC.Collect();       //回收資源

            pictureBox1.Image = bm2;

            delay(300);

            flag_do_find_awb_location = false;

            richTextBox1.Text += "打印搜尋結果1\n";
            richTextBox1.Text += "flag_down_up_cnt = " + flag_down_up_cnt.ToString() +
                ", flag_right_left_cnt = " + flag_right_left_cnt.ToString() + "\n";

            richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";

            richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
            richTextBox1.Text += "awb_block = " + awb_block.ToString() + ", awb_block = " + awb_block.ToString() + "\n";
            if (ww < 20)
            {
                richTextBox1.Text += "找到的範圍太小1\n";
                tb_awb_mesg.Text = "找到的範圍太小";
                richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
                flag_do_find_awb_location_ok = false;
                flag_do_find_awb_location_fail_too_small = true;
                return S_FALSE;
            }
            if ((Math.Abs(flag_down_up_point_cnt) > 70) || (Math.Abs(flag_right_left_point_cnt) > 70))
            {
                richTextBox1.Text += "找到的位置太遠\n";
                tb_awb_mesg.Text = "找到的位置太遠";
                richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                    ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
                flag_do_find_awb_location_ok = false;
                flag_do_find_awb_location_fail_too_far = true;
                return S_FALSE;
            }
            flag_do_find_awb_location_ok = true;
            flag_do_find_awb_location_fail_too_small = false;
            flag_do_find_awb_location_fail_too_far = false;
            return S_OK;
        }

        int check_awb_location()
        {
            flag_do_find_awb_location_fail = false;
            flag_do_find_awb_location_fail_too_small = false;
            flag_do_find_awb_location_fail_too_far = false;

            int w = 640;
            int h = 480;
            int x_st = 0;
            int y_st = 0;
            int ww = 0;
            int hh = 0;
            ww = awb_block;
            hh = awb_block;
            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;

            int offset_x = flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            int offset_y = flag_down_up_cnt * awb_step + flag_down_up_point_cnt;

            richTextBox1.Text += "打印搜尋結果\n";
            richTextBox1.Text += "flag_down_up_cnt = " + flag_down_up_cnt.ToString() +
                ", flag_right_left_cnt = " + flag_right_left_cnt.ToString() + "\n";

            richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
            richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
            richTextBox1.Text += "awb_block = " + awb_block.ToString() + ", awb_block = " + awb_block.ToString() + "\n";
            if (ww < 20)
            {
                richTextBox1.Text += "找到的範圍太小2\t" + "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
                flag_do_find_awb_location_fail = true;
                flag_do_find_awb_location_fail_too_small = true;
                return S_FALSE;
            }
            if ((Math.Abs(offset_x) > 70) || (Math.Abs(offset_y) > 70))
            {
                richTextBox1.Text += "找到的距離太遙遠\t" + "offset_x = " + offset_x.ToString() + ", offset_y = " + offset_y.ToString() + "\n";
                flag_do_find_awb_location_fail = true;
                flag_do_find_awb_location_fail_too_far = true;
                return S_FALSE;
            }
            flag_do_find_awb_location_fail = false;

            richTextBox1.Text += "找到的範圍OK\t" + "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
            richTextBox1.Text += "找到的距離OK\t" + "offset_x = " + offset_x.ToString() + ", offset_y = " + offset_y.ToString() + "\n";

            return S_OK;
        }

        private void bt_find_brightness2_Click(object sender, EventArgs e)
        {
            if (find_awb_location() == S_FALSE)
            {
                tb_awb_mesg.Text = "尋找區域失敗";
                bt_awb_test.BackColor = Color.Red;
                playSound(S_FALSE);
            }
            return;
        }

        private void bt_show_brightness_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "show_brightness()\n";
            show_brightness();
        }

        int show_brightness()
        {
            int x_st = 0;
            int y_st = 0;
            int ww = 0;
            int hh = 0;
            int w;
            int h;
            int i;
            int j;
            Color p;
            Bitmap bm2 = null;
            int th_h = (int)numericUpDown_find_brightness_h.Value;
            int th_l = (int)numericUpDown_find_brightness_l.Value;

            tb_awb_mesg.Text = "顯示過暗過亮";

            flag_do_find_awb_location = true;

            //歸零
            flag_right_left_cnt = 0;
            flag_down_up_cnt = 0;
            flag_right_left_point_cnt = 0;
            flag_down_up_point_cnt = 0;
            awb_block = 32;
            step = 1;
            add_amount = 1;
            add_tmp = 0;
            ww = awb_block;
            hh = awb_block;
            refresh_picturebox2();
            delay(10);

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm2 = bm;
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                ga = Graphics.FromImage(bm2);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f2 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                w = bm2.Width;
                h = bm2.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f3 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            x_st = w / 2 - awb_window_size / 2;
            y_st = h / 2 - awb_window_size / 2;

            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;

            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > h)
                y_st = h - hh;

            double y_max = 0;
            double y_min = 255;

            for (j = 0; j < awb_window_size; j++)
            {
                for (i = 0; i < awb_window_size; i++)
                {
                    p = bm2.GetPixel(x_st + i, y_st + j);
                    //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
                    //richTextBox1.Text += "x(" + p.R.ToString() + ", " + p.G.ToString() + ", " + p.B.ToString() + ")\n";

                    //bm2.SetPixel(xx, yy, Color.FromArgb(rrr.R, rrr.G, rrr.B));

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    if (y_max < yyy.Y)
                        y_max = yyy.Y;

                    if (y_min > yyy.Y)
                        y_min = yyy.Y;

                    int yy = (int)yyy.Y % 256;
                    yy = yy / 20 * 20;

                    bm2.SetPixel(x_st + i, y_st + j, Color.FromArgb(255, yy, yy, yy));


                    //g.DrawEllipse(new Pen(Color.FromArgb(255, 255, (j / 2) % 256, (j / 2) % 256), 1), i, j, 1, 1);

                    /*
                    if (yyy.Y > th_h)
                    {
                        //bitmap1.SetPixel(xx, yy, Color.FromArgb((int)yyy.Y, (int)yyy.Y, (int)yyy.Y));
                        //bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                        bm2.SetPixel(x_st + i, y_st + j, Color.Yellow);
                    }
                    else if (yyy.Y < th_l)
                    {
                        //bitmap1.SetPixel(xx, yy, Color.FromArgb((int)yyy.Y, (int)yyy.Y, (int)yyy.Y));
                        //bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                        bm2.SetPixel(x_st + i, y_st + j, Color.Gold);
                    }
                    else
                    {
                    }
                    */
                    //bm2.SetPixel(x_st + i, y_st + j, Color.Red);
                }
            }
            richTextBox1.Text += "Y max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "Y min = " + y_min.ToString() + "\n";

            GC.Collect();       //回收資源

            pictureBox1.Image = bm2;

            delay(5000);
            flag_do_find_awb_location = false;
            return S_OK;
        }

        int find_brightness()
        {
            flag_do_find_awb_location = true;
            int x_st = 0;
            int y_st = 0;
            int ww = 0;
            int hh = 0;
            int w;
            int h;
            int i;
            int j;
            Color p;
            Bitmap bm2 = null;
            double y_total = 0;

            tb_awb_mesg.Text = "量測亮度";

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm2 = bm;
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                ga = Graphics.FromImage(bm2);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f2 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            try
            {
                w = bm2.Width;
                h = bm2.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f3 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return S_FALSE;
            }

            ww = awb_block;
            hh = awb_block;
            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;

            int offset_x = flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            int offset_y = flag_down_up_cnt * awb_step + flag_down_up_point_cnt;

            richTextBox1.Text += "打印搜尋結果\n";
            richTextBox1.Text += "flag_down_up_cnt = " + flag_down_up_cnt.ToString() +
                ", flag_right_left_cnt = " + flag_right_left_cnt.ToString() + "\n";

            richTextBox1.Text += "flag_down_up_point_cnt = " + flag_down_up_point_cnt.ToString() +
                ", flag_right_left_point_cnt = " + flag_right_left_point_cnt.ToString() + "\n";
            richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
            richTextBox1.Text += "awb_block = " + awb_block.ToString() + ", awb_block = " + awb_block.ToString() + "\n";
            richTextBox1.Text += "距離\t" + "offset_x = " + offset_x.ToString() + ", offset_y = " + offset_y.ToString() + "\n";

            for (j = y_st; j < (y_st + hh); j++)
            {
                for (i = x_st; i < (x_st + ww); i++)
                {
                    p = bm2.GetPixel(i, j);
                    //bm2.SetPixel(i, j, Color.FromArgb(255, 0, 0));
                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);
                    y_total += yyy.Y;
                }
            }

            tb_awb_mesg.Text = (y_total / (ww * hh)).ToString();

            GC.Collect();       //回收資源
            pictureBox1.Image = bm2;

            flag_do_find_awb_location = false;
            return S_OK;
        }

        private void numericUpDown_find_brightness_h_ValueChanged(object sender, EventArgs e)
        {
            if (numericUpDown_find_brightness_h.Value <= numericUpDown_find_brightness_l.Value)
                numericUpDown_find_brightness_h.Value = (numericUpDown_find_brightness_l.Value + 1);
        }

        private void numericUpDown_find_brightness_l_ValueChanged(object sender, EventArgs e)
        {
            if (numericUpDown_find_brightness_l.Value >= numericUpDown_find_brightness_h.Value)
                numericUpDown_find_brightness_l.Value = (numericUpDown_find_brightness_h.Value - 1);
        }

        void restore_camera_setup()
        {
            int SendAddr;
            byte SendData;

            tb_awb_mesg.Text = "設定相機預設值";

            //Gamma恢復預設值
            int i;
            byte[] gamma_00 = new byte[] { 0x14, 0x22, 0x37, 0x4B, 0x5E, 0x6B, 0x76, 0x82, 0x8C, 0x9F, 0xAB, 0xB5, 0xCF, 0xDE, 0xED, 0x1B };
            for (i = 0; i < 16; i++)
            {
                SendAddr = 0x5301 + i;
                SendData = gamma_00[i];
                DongleAddr_h = (byte)((SendAddr >> 8) & 0xff);
                DongleAddr_l = (byte)((SendAddr >> 0) & 0xff);
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
                delay(10);
            }

            //停用Gamma
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x00;
            SendData = 0xFF;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x02;
            SendData = 0xC8;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);
            DongleAddr_h = 0x53;
            DongleAddr_l = 0x00;
            SendData = 0x01;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);

            //設定相機預設的RB值
            //R = 0x5B0 = 1456, 0x600 = 1536
            //B = 0x670 = 1648, 0x500 = 1280
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1A;
            SendData = 0x06;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1B;
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1E;
            SendData = 0x05;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);
            DongleAddr_h = 0x52;
            DongleAddr_l = 0x1F;
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            delay(10);

            //設定相機亮度, WPT BPT
            if (software_version == "A03")
            {
                SendData = 0x42;    //66
                DongleAddr_h = 0x3A;
                DongleAddr_l = 0x03;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //WPT

                delay(20);

                SendData = 0x38;    //56
                DongleAddr_h = 0x3A;
                DongleAddr_l = 0x04;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //BPT

                delay(20);
            }
            else    //A04
            {
                if (rb_brightness_color_1.Checked == true)
                    richTextBox1.Text += "使用白光 66 56\n";
                else
                    richTextBox1.Text += "使用黃光 40 25\n";
                if (rb_brightness_color_1.Checked == true)
                    SendData = 66;
                else
                    SendData = 40;
                if (flag_auto_brightness_awb == true)
                {
                    richTextBox1.Text += "自動亮度測試 20 5 + 5 * " + current_test_count.ToString() + "\n";
                    SendData = (byte)(20 + current_test_count * 5);
                }
                DongleAddr_h = 0x3A;
                DongleAddr_l = 0x03;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //WPT

                delay(20);

                if (rb_brightness_color_1.Checked == true)
                    SendData = 56;
                else
                    SendData = 25;
                if (flag_auto_brightness_awb == true)
                {
                    SendData = (byte)(5 + current_test_count * 5);
                }
                DongleAddr_h = 0x3A;
                DongleAddr_l = 0x04;
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //BPT

                delay(20);
            }

            //saturation恢復預設
            //saturation TH2
            SendData = 0x40;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //TH2

            delay(20);

            //saturation TH1
            SendData = 0x28;
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x04;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);  //TH1

            delay(20);

            return;
        }

        int check_awb_region()
        {
            flag_do_find_awb_location = true;
            if (cb_auto_search.Checked == true)
            {
                richTextBox1.Text +=
                    "right_left_point_cnt(" + awb_cnt.ToString() + ")=" + flag_right_left_point_cnt.ToString() + ";" +
                    "down_up_point_cnt(" + awb_cnt.ToString() + ")=" + flag_down_up_point_cnt.ToString() + ";" +
                    "awb_block(" + awb_cnt.ToString() + ")=" + awb_block.ToString() + ";" +
                    "\n";
            }
            else
            {
                richTextBox1.Text +=
                    "right_left(" + awb_cnt.ToString() + ")=" + flag_right_left_cnt.ToString() + ";" +
                    "down_up(" + awb_cnt.ToString() + ")=" + flag_down_up_cnt.ToString() + ";" +
                    "awb_block(" + awb_cnt.ToString() + ")=" + awb_block.ToString() + ";" +
                    "\n";
            }

            int x_st = 0;
            int y_st = 0;
            int ww = 0;
            int hh = 0;
            int w;
            int h;
            int i;
            int j;
            Color p;
            Bitmap bm2 = null;

            try
            {
                bm2 = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return S_FALSE;
            }

            w = bm2.Width;
            h = bm2.Height;

            ww = awb_block;
            hh = awb_block;

            x_st = w / 2 - ww / 2 + flag_right_left_cnt * awb_step + flag_right_left_point_cnt;
            if (x_st < 0)
                x_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;

            y_st = h / 2 - hh / 2 + flag_down_up_cnt * awb_step + flag_down_up_point_cnt;
            if (y_st < 0)
                y_st = 0;
            if ((y_st + hh) > h)
                y_st = h - hh;

            richTextBox1.Text += "\nbrightness = new int[,] { ";

            for (j = y_st; j < (y_st + awb_block); j++)
            {
                richTextBox1.Text += "{ ";
                for (i = x_st; i < (x_st + awb_block); i++)
                {
                    p = bm2.GetPixel(i, j);

                    bm2.SetPixel(i, j, Color.Red);

                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);

                    richTextBox1.Text += ((int)yyy.Y).ToString();

                    if ((i == x_st + awb_block - 1) && (j == y_st + awb_block - 1))
                        richTextBox1.Text += " }";
                    else if (i == x_st + awb_block - 1)
                        richTextBox1.Text += " }, ";
                    else
                        richTextBox1.Text += ", ";
                }
            }
            richTextBox1.Text += " };\n";
            pictureBox1.Image = bm2;


            delay(1000);

            flag_do_find_awb_location = false;

            return S_OK;
        }

        void save_log_to_local_drive()
        {
            show_system_info();     //顯示系統資訊

            //建立一個檔案
            richTextBox1.Text += "Bootup time : " + bootup_time.ToString() + "\n";
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - bootup_time).ToString() + " 秒\n";
            //richTextBox1.Text += "電腦開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒\n";  //wrong
            string filename = "imsLink_log." + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式            
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";

            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        void save_current_program_to_local_drive()
        {
            //本程式截圖
            Bitmap bmp = new Bitmap(this.Width, this.Height);
            Graphics g = Graphics.FromImage(bmp);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(this.Width, this.Height));
            //richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            //richTextBox1.Text += "H = " + this.Height.ToString() + "\n";
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            //存成bmp檔
            String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bmp.Save(filename, ImageFormat.Bmp);

            //存成jpg檔
            //String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //myImage.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
        }

        void save_image_to_drive()
        {
            show_main_message1("存檔中...", S_OK, 10);
            delay(10);

            if (flag_operation_mode != MODE_RELEASE_STAGE0)
            {
                int i;
                bool flag_incorrect_data = false;

                if (tb_sn_opal.Text.Length == 0)
                {
                    show_main_message1("未輸入相機序號", S_OK, 30);
                    show_main_message2("未輸入相機序號", S_OK, 30);
                    flag_incorrect_data = true;
                }
                else if ((tb_sn_opal.Text.Length == 9) || (tb_sn_opal.Text.Length == 10))
                {
                    //檢查英文字母的正確性
                    if (((tb_sn_opal.Text[0] >= 'A') && (tb_sn_opal.Text[0] <= 'Z')) || ((tb_sn_opal.Text[0] >= 'a') && (tb_sn_opal.Text[0] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b0\n";
                        show_main_message1("序號格式不正確", S_OK, 30);
                    }

                    if (((tb_sn_opal.Text[1] >= 'A') && (tb_sn_opal.Text[1] <= 'Z')) || ((tb_sn_opal.Text[1] >= 'a') && (tb_sn_opal.Text[1] <= 'z')))
                    {
                        flag_incorrect_data = false;
                    }
                    else
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b1\n";
                        show_main_message1("序號格式不正確", S_OK, 30);
                    }

                    for (i = 2; i < tb_sn_opal.Text.Length; i++)
                    {
                        if ((tb_sn_opal.Text[i] < '0') || (tb_sn_opal.Text[i] > '9'))
                        {
                            flag_incorrect_data = true;
                            richTextBox1.Text += "SN1格式不正確b\n";
                            show_main_message1("序號格式不正確", S_OK, 30);
                        }
                    }

                    if (flag_incorrect_data == false)
                    {
                        richTextBox1.Text += "d取得 SN1序號 : " + tb_sn_opal.Text + "\n";
                    }
                }
                else
                {
                    flag_incorrect_data = true;
                    show_main_message1("序號格式不正確", S_OK, 30);
                }

                if (flag_incorrect_data == true)
                {
                    richTextBox1.Text += "資料錯誤,長度 " + tb_sn_opal.Text.Length.ToString() + "\t內容 " + tb_sn_opal.Text + "\n";
                    return;
                }
                else
                {
                    richTextBox1.Text += "資料正確\n";
                }
            }

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                if (cb_show_time.Checked == true)
                {   //顯示時間
                    int xPos = 10;
                    int yPos = 10;
                    string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

                    g.ReleaseHdc();

                    if (flag_david_test == true)
                    {
                        g.DrawString(saturation_ratio + ", TH2 = " + g_TH2.ToString() + ", TH1 = " + g_TH1.ToString(), drawFont, drawBrush, xPos, yPos);
                    }
                    else
                    {
                        g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
                    }
                }
                else
                {
                    g.ReleaseHdc();
                }

                g.Dispose();

                String filename1 = string.Empty;
                String filename2 = string.Empty;

                if (flag_operation_mode == MODE_RELEASE_STAGE1A)
                {
                    filename1 = "M:\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_1";
                    filename2 = Application.StartupPath + "\\picture\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_1a";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE1B)
                {
                    filename1 = "M:\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_1";
                    filename2 = Application.StartupPath + "\\picture\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_1b";
                }
                else if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    filename1 = "M:\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_2";
                    filename2 = Application.StartupPath + "\\picture\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_2";
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    filename1 = "M:\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_3";
                    filename2 = Application.StartupPath + "\\picture\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + tb_sn_opal.Text + "_3";
                }
                else
                {
                    filename1 = "M:\\xxxx_ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                    filename2 = Application.StartupPath + "\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                }

                //String file1 = file + ".jpg";
                String filename1a = filename1 + ".bmp";
                String filename2a = filename2 + ".bmp";
                //String file3 = file + ".png";

                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename1a, ImageFormat.Bmp);
                    bitmap1.Save(filename2a, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename1a + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2a + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    show_main_message1("已存檔BMP", S_OK, 30);
                    show_main_message2("已存檔 : " + filename1a, S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息b1 : " + ex.Message + "\n";
                    show_main_message1("存檔失敗", S_OK, 30);
                    show_main_message2("存檔失敗 : " + ex.Message, S_OK, 30);
                }

                if ((flag_operation_mode == MODE_RELEASE_STAGE0) || (flag_operation_mode == MODE_RELEASE_STAGE1A) || (flag_operation_mode == MODE_RELEASE_STAGE1B) || (flag_operation_mode == MODE_RELEASE_STAGE2))
                {
                    camera_serials.Add(new string[] { tb_sn_opal.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                    exportCSV();
                }
                else if (flag_operation_mode == MODE_RELEASE_STAGE3)
                {
                    if ((lb_class.Text.Length == 1) || (lb_class.Text.Length == 2))
                    {
                        camera_serials.Add(new string[] { tb_sn_opal.Text, lb_class.Text, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                        lb_class.Text = "";
                        flag_stage3_step = 0;
                        exportCSV();
                    }
                    else
                    {
                        richTextBox1.Text += "等級資料錯誤, 不匯出csv檔, len = " + lb_class.Text.Length.ToString() + "\n";
                        show_main_message1("等級資料錯誤, 不匯出csv檔", S_OK, 30);
                        show_main_message1("等級資料錯誤, 不匯出csv檔", S_OK, 30);
                        show_main_message1("等級資料錯誤, 不匯出csv檔", S_OK, 30);
                    }
                }

                tb_sn_opal.Clear();
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                show_main_message1("無圖可存", S_FALSE, 30);
                show_main_message2("無圖可存", S_FALSE, 30);
                tb_sn_opal.Clear();
            }
            return;
        }

        void save_image_to_local_drive()
        {
            if (this.pictureBox1.Focused == false)
                this.pictureBox1.Focus();
            show_main_message1("存檔中...", S_OK, 10);
            delay(10);

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            if (bitmap1 != null)
            {
                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                if (cb_show_time.Checked == true)
                {   //顯示時間
                    int xPos = 10;
                    int yPos = 10;
                    string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

                    g.ReleaseHdc();

                    if (flag_david_test == true)
                    {
                        g.DrawString(saturation_ratio + ", TH2 = " + g_TH2.ToString() + ", TH1 = " + g_TH1.ToString(), drawFont, drawBrush, xPos, yPos);
                    }
                    else
                    {
                        g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
                    }
                }
                else
                {
                    g.ReleaseHdc();
                }

                int x_st = 0;
                int y_st = 0;

                y_st = 450;

                if (data_R > 0)
                {
                    drawFont1 = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
                    drawBrush = new SolidBrush(Color.Red);
                    x_st = 430;
                    g.DrawString(data_R.ToString(), drawFont1, drawBrush, x_st, y_st);
                }

                if (data_G > 0)
                {
                    drawBrush = new SolidBrush(Color.Green);
                    x_st = 430 + 70;
                    g.DrawString(data_G.ToString(), drawFont1, drawBrush, x_st, y_st);
                }

                if (data_B > 0)
                {
                    drawBrush = new SolidBrush(Color.Blue);
                    x_st = 430 + 140;
                    g.DrawString(data_B.ToString(), drawFont1, drawBrush, x_st, y_st);
                }

                if (lb_auto_awb_cnt.Visible == true)
                {
                    drawBrush = new SolidBrush(Color.Yellow);
                    x_st = 430 - 70 * 2 - 60;
                    g.DrawString(current_test_count.ToString(), drawFont1, drawBrush, x_st, y_st);
                }

                if (cb_auto_search.Checked == true)
                {
                    drawBrush = new SolidBrush(Color.DarkBlue);
                    x_st = 430 - 70 * 2 - 20;
                    g.DrawString("point  " + flag_right_left_point_cnt.ToString() + ",  " + flag_down_up_point_cnt.ToString(), drawFont1, drawBrush, x_st, y_st);
                }
                else
                {
                    drawBrush = new SolidBrush(Color.DarkBlue);
                    x_st = 430 - 70 * 2;
                    g.DrawString("step  " + flag_right_left_cnt.ToString() + ",  " + flag_down_up_cnt.ToString(), drawFont1, drawBrush, x_st, y_st);
                }
                g.Dispose();

                String filename1 = string.Empty;

                if (lb_auto_awb_cnt.Visible == true)
                {
                    filename1 = Application.StartupPath + "\\picture\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + "_" + current_test_count.ToString("D2");
                    if (flag_stage_awb == 0)
                    {
                        filename1 += "_a";
                    }
                    else if (flag_stage_awb == 1)
                    {
                        filename1 += "_b";

                    }
                    else if (flag_stage_awb == 2)
                    {
                        filename1 += "_c";
                    }
                    else
                    {
                        filename1 += "_xxxxxx";
                    }
                }
                else
                {
                    filename1 = Application.StartupPath + "\\picture\\ims_image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                }

                //String file1 = file + ".jpg";
                String filename1a = filename1 + ".bmp";
                //String file3 = file + ".png";

                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename1a, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename1a + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    show_main_message1("已存檔BMP", S_OK, 30);
                    show_main_message2("已存檔 : " + filename1a, S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息b2 : " + ex.Message + "\n";
                    show_main_message1("存檔失敗", S_OK, 30);
                    show_main_message2("存檔失敗 : " + ex.Message, S_OK, 30);
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                show_main_message1("無圖可存", S_FALSE, 30);
                show_main_message2("無圖可存", S_FALSE, 30);
            }
            return;
        }

        void show_system_info()
        {
            //顯示系統資訊
            OperatingSystem OSv = System.Environment.OSVersion;
            richTextBox1.AppendText("imsLink登錄時間 : " + compile_time + "\n");
            richTextBox1.AppendText("作業系統版本 : " + OSv.ToString() + "\n");
            richTextBox1.AppendText("圖形介面版本 : " + software_version + "\n");
            richTextBox1.AppendText("韌體版本 : F0" + fw_version.ToString() + "\n");
            richTextBox1.AppendText("螢幕解析度 : " + Screen.PrimaryScreen.Bounds.Width.ToString() + "*" + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n");
            richTextBox1.AppendText("目前時間 : " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        void exit_program()
        {
            richTextBox1.Text += "\n\nimsLink " + software_version + " 關閉, 時間 : " + bootup_time.ToString() + "\n\n";
            save_log_to_local_drive();
            if (flag_doing_refreshing_camera == true)
            {
                richTextBox1.Text += "正在影像重抓, 忽略\n";
                return;
            }

            show_main_message1("關閉程式", S_OK, 30);
            if (flag_comport_ok == true)
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button1.Enabled = true;
                button89.Enabled = true;
                button2.Enabled = false;
                button90.Enabled = false;
                flag_comport_ok = false;
                lb_main_mesg1.Text = "COM未連線";
                playSound(S_FALSE);
            }

            if (Cam != null)
            {
                if ((flag_camera_start == 1) && (Cam.IsRunning == true))
                {
                    richTextBox1.Text += "USB影像傳輸中, 關閉\n";
                    flag_camera_start = 0;
                    Cam.Stop();  // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
                    comboBox_webcam.Items.Clear();
                }
            }
            show_main_message1("關閉程式", S_OK, 30);
            richTextBox1.Text += "確認關閉ST\n";
            delay(100);
            richTextBox1.Text += "確認關閉SP\n";

            if (Cam != null)
            {
                if (Cam.IsRunning == true)  // When Form1 closes itself, WebCam must stop, too.
                {
                    flag_camera_start = 0;
                    Cam.Stop();   // WebCam stops capturing images.
                    //Cam.SignalToStop();
                    //Cam.WaitForStop();
                    Cam = null;
                    richTextBox1.Text += "先關閉camera\n";
                }
            }
            else
            {
                richTextBox1.Text += "camera is null\n";
            }

            /*
            richTextBox1.Text += "關閉程式\n";
            //Application.Exit();
            try
            {
                System.Environment.Exit(0);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f : " + ex.Message + "\n";
            }
            */

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();
            return;
        }

        void make_camera_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[10];
            var stringChars2 = new char[11];
            var random = new Random();
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if (i < 2)
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號1：" + finalString1 + "\n";

            for (int i = 0; i < stringChars2.Length; i++)
            {
                stringChars2[i] = chars2[random.Next(chars2.Length)];
            }
            var finalString2 = new String(stringChars2);
            richTextBox1.Text += "相機序號2：" + finalString2 + "\n";

            tb_sn1.Text = finalString1;
            tb_sn2.Text = finalString2;

            flag_ok_to_write_data = true;

            show_main_message1("製作相機資料完成", S_OK, 30);
            return;
        }

        void erase_camera_data()
        {
            richTextBox1.Text += "erase all camera flash data\n";

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xEE, 0xFF, 0xEE, 0xFF);   //erase all camera flash data
            show_main_message1("清除相機資料完成", S_OK, 30);
            return;
        }

        private void trackBar_Contrast_Scroll(object sender, EventArgs e)
        {
            get_camera_contrast_brightness_setup();

            byte SendData;

            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data3 = 0x00;  //Y_OFFSET
            byte data4 = 0x20;  //Y_GAIN
            //byte data5 = 0x00;  //Y_BRIGHT
            byte data6 = 0x00;  //SIGN

            //byte camera_yoffset_sign_bits_local = 0;

            switch (trackBar_Contrast.Value)
            {
                case 4:
                    data3 = 0xA0;
                    data4 = 0x24;
                    //data5 = 0x0F;
                    data6 = 0x00;
                    camera_yoffset_sign_bits = 0;
                    break;
                case 3:
                    data3 = 0x90;
                    data4 = 0x23;
                    //data5 = 0x0A;
                    data6 = 0x00;
                    camera_yoffset_sign_bits = 0;
                    break;
                case 2:
                    data3 = 0x90;
                    data4 = 0x22;
                    //data5 = 0x0A;
                    data6 = 0x00;
                    camera_yoffset_sign_bits = 0;
                    break;
                case 1:
                    data3 = 0x80;
                    data4 = 0x21;
                    //data5 = 0x05;
                    data6 = 0x00;
                    camera_yoffset_sign_bits = 0;
                    break;
                case 0:
                    data3 = 0x00;
                    data4 = 0x20;
                    //data5 = 0x00;
                    data6 = 0x00;
                    camera_yoffset_sign_bits = 0;
                    break;
                case -1:
                    data3 = 0x80;
                    data4 = 0x1F;
                    //data5 = 0x05;
                    data6 = 0x0C;
                    camera_yoffset_sign_bits = 1;
                    break;
                case -2:
                    data3 = 0x90;
                    data4 = 0x1E;
                    //data5 = 0x05;
                    data6 = 0x0C;
                    camera_yoffset_sign_bits = 1;
                    break;
                case -3:
                    data3 = 0x90;
                    data4 = 0x1D;
                    //data5 = 0x05;
                    data6 = 0x0C;
                    camera_yoffset_sign_bits = 1;
                    break;
                case -4:
                    data3 = 0xA0;
                    data4 = 0x1C;
                    //data5 = 0x05;
                    data6 = 0x0C;
                    camera_yoffset_sign_bits = 1;
                    break;
                default:
                    data3 = 0x00;
                    data4 = 0x20;
                    //data5 = 0x00;
                    data6 = 0x00;
                    richTextBox1.Text += "XXXXXXXX";
                    camera_yoffset_sign_bits = 0;
                    break;
            }

            data6 = (byte)((((int)camera_ybright_sign_bits) << 3) | (((int)camera_yoffset_sign_bits) << 2));

            richTextBox1.Text += "a選擇了對比 " + trackBar_Contrast.Value.ToString() + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = data3;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = data4;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            /*
            //  Y BRIGHT 不設定
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = data5;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = data6;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

        }

        private void trackBar_Brightness_Scroll(object sender, EventArgs e)
        {
            get_camera_contrast_brightness_setup();

            byte SendData;
            int brightness = 0;
            int sign_bit = 0;
            switch (trackBar_Brightness.Value)
            {
                case 4: brightness = 0x40; break;
                case 3: brightness = 0x30; break;
                case 2: brightness = 0x20; break;
                case 1: brightness = 0x10; break;
                case 0: brightness = 0x00; break;
                case -1: brightness = 0x10; sign_bit = 0x08; break;
                case -2: brightness = 0x20; sign_bit = 0x08; break;
                case -3: brightness = 0x30; sign_bit = 0x08; break;
                case -4: brightness = 0x40; sign_bit = 0x08; break;
                default: brightness = 0x00; richTextBox1.Text += "XXXXXXXX"; break;
            }

            richTextBox1.Text += "選擇了亮度 " + trackBar_Brightness.Value.ToString() + "\t設定 " + brightness.ToString() + "\n";


            richTextBox1.Text += "camera_yoffset_sign_bits = " + camera_yoffset_sign_bits.ToString("X2") + "\n";
            richTextBox1.Text += "sign_bit a = " + sign_bit.ToString("X2") + "\n";

            sign_bit = (byte)(sign_bit | (((int)camera_yoffset_sign_bits) << 2));

            richTextBox1.Text += "sign_bit b = " + sign_bit.ToString("X2") + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = 0x06;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = 0x02;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            /*
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = 0x20;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = (byte)brightness;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = (byte)sign_bit;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

        }

        void get_camera_contrast_brightness_setup()
        {
            flag_ok_camera_ybright_sign_bit = false;
            flag_ok_camera_yoffset_sign_bit = false;

            //read current Y SIGN BITS value;
            //讀取SIGN BITS	0x5808
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            int cnt = 0;
            while ((flag_ok_camera_yoffset_sign_bit == false) || (flag_ok_camera_ybright_sign_bit == false))
            {
                richTextBox1.Text += "W";
                delay(100);
                cnt++;
                if (cnt == 3)
                    break;
            }
            //richTextBox1.Text += "取得sign ybright " + ((int)camera_ybright_sign_bits).ToString("X2") + "\n";
            //richTextBox1.Text += "取得sign yoffset " + ((int)camera_yoffset_sign_bits).ToString("X2") + "\n";
        }

        private void button67_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            //read current Y BRIGHT value;
            //讀取亮度	0x5807
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            //read current Y SIGN BITS value;
            //讀取SIGN BITS	0x5808
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);
        }

        private void button65_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            richTextBox1.Text += "恢復預設值\n";


            byte SendData;

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = 0x06;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = 0x02;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = 0x20;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);


            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            trackBar_Contrast3.Value = 0;
            trackBar_Y_Offset3.Value = 0;
            trackBar_Brightness3.Value = 0;

            numericUpDown_gain3.Value = 0;
            numericUpDown_offset3.Value = 0;
            numericUpDown_brightness3.Value = 0;

            lb_gain_value.Text = "1 X";
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            byte SendData;

            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data3 = 0x00;  //Y_OFFSET
            byte data4 = 0x20;  //Y_GAIN
            byte data5 = 0x00;  //Y_BRIGHT
            byte data6 = 0x00;  //SIGN

            switch (trackBar2.Value)
            {
                case 4:
                    data3 = 0xA0;
                    data4 = 0xE0;
                    data5 = 0x0F;
                    data6 = 0x00;
                    break;
                case 3:
                    data3 = 0x90;
                    data4 = 0x90;
                    data5 = 0x0A;
                    data6 = 0x00;
                    break;
                case 2:
                    data3 = 0x90;
                    data4 = 0x60;
                    data5 = 0x0A;
                    data6 = 0x00;
                    break;
                case 1:
                    data3 = 0x80;
                    data4 = 0x30;
                    data5 = 0x05;
                    data6 = 0x00;
                    break;
                case 0:
                    data3 = 0x00;
                    data4 = 0x20;
                    data5 = 0x00;
                    data6 = 0x00;
                    break;
                case -1:
                    data3 = 0x80;
                    data4 = 0x25;
                    data5 = 0x05;
                    data6 = 0x0C;
                    break;
                case -2:
                    data3 = 0x90;
                    data4 = 0x2A;
                    data5 = 0x05;
                    data6 = 0x0C;
                    break;
                case -3:
                    data3 = 0x90;
                    data4 = 0x2F;
                    data5 = 0x05;
                    data6 = 0x0C;
                    break;
                case -4:
                    data3 = 0xA0;
                    data4 = 0x34;
                    data5 = 0x05;
                    data6 = 0x0C;
                    break;
                default:
                    data3 = 0x00;
                    data4 = 0x20;
                    data5 = 0x00;
                    data6 = 0x00;
                    richTextBox1.Text += "XXXXXXXX";
                    break;
            }

            richTextBox1.Text += "b選擇了對比 " + trackBar2.Value.ToString() + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = data3;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = data4;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            //  Y BRIGHT 不設定
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = data5;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = data6;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            byte SendData;
            int brightness = 0;
            int sign_bit = 0;
            switch (trackBar1.Value)
            {
                case 4: brightness = 0x40; break;
                case 3: brightness = 0x30; break;
                case 2: brightness = 0x20; break;
                case 1: brightness = 0x10; break;
                case 0: brightness = 0x00; break;
                case -1: brightness = 0x10; sign_bit = 0x08; break;
                case -2: brightness = 0x20; sign_bit = 0x08; break;
                case -3: brightness = 0x30; sign_bit = 0x08; break;
                case -4: brightness = 0x40; sign_bit = 0x08; break;
                default: brightness = 0x00; richTextBox1.Text += "XXXXXXXX"; break;
            }

            richTextBox1.Text += "選擇了亮度 " + trackBar1.Value.ToString() + "\t設定 " + brightness.ToString() + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = 0x06;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = 0x02;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            /*
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = 0x20;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
            */

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = (byte)brightness;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = (byte)sign_bit;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);


        }

        private void timer_stage1c_Tick(object sender, EventArgs e)
        {
            if (flag_network_disk_status == false)
            {
                tb_wait_check_data.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
            }

            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            ccc++;
            if (flag_stage1c_step == 0)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg1c.Text = "等待勾選項目 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg1c.Text = "等待勾選項目 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg1c.Text = "等待勾選項目 /";
                else
                    lb_main_mesg1c.Text = "等待勾選項目 -";

                return;
            }
            else
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg1c.Text = "輸入相機序號 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg1c.Text = "輸入相機序號 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg1c.Text = "輸入相機序號 /";
                else
                    lb_main_mesg1c.Text = "輸入相機序號 -";
            }

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "一C";
                if (this.tb_wait_check_data.Focused == false)
                {
                    this.tb_wait_check_data.Focus();
                    richTextBox1.Text += "F1c";
                }
            }

            //檢查相機序號
            int len;
            len = tb_wait_check_data.Text.Length;

            if (len > 20)   //太長, 直接放棄
            {
                tb_wait_check_data.Clear();
                //richTextBox1.Text += "X1";
                return;
            }
            else if (len > 5)    //檢查是否換行
            {
                if ((tb_wait_check_data.Text[len - 2] == 0x0D) || (tb_wait_check_data.Text[len - 1] == 0x0A))
                {
                    tb_wait_check_data.Text = tb_wait_check_data.Text.Trim();
                    //richTextBox1.Text += "OK";
                }
                else
                {
                    //richTextBox1.Text += "X2";
                    return;
                }
            }
            else    //太短  留著累計
            {
                //richTextBox1.Text += "X3";
                return;
            }

            int i;
            bool flag_incorrect_data = false;

            len = tb_wait_check_data.Text.Length;
            if ((len == 9) || (len == 10))
            {
                //檢查英文字母的正確性
                //檢查第0碼
                if (((tb_wait_check_data.Text[0] >= 'A') && (tb_wait_check_data.Text[0] <= 'Z')) || ((tb_wait_check_data.Text[0] >= 'a') && (tb_wait_check_data.Text[0] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b0\n";
                }

                //檢查第1碼
                if (((tb_wait_check_data.Text[1] >= 'A') && (tb_wait_check_data.Text[1] <= 'Z')) || ((tb_wait_check_data.Text[1] >= 'a') && (tb_wait_check_data.Text[1] <= 'z')))
                {
                    flag_incorrect_data = false;
                }
                else
                {
                    flag_incorrect_data = true;
                    richTextBox1.Text += "SN1格式不正確b1\n";
                }

                //檢查第 2~8 或 2~9 碼
                for (i = 2; i < len; i++)
                {
                    if ((tb_wait_check_data.Text[i] < '0') || (tb_wait_check_data.Text[i] > '9'))
                    {
                        flag_incorrect_data = true;
                        richTextBox1.Text += "SN1格式不正確b\n";
                    }
                }

                if (flag_incorrect_data == false)
                {
                    richTextBox1.Text += "1c取得 SN1序號 : " + tb_wait_check_data.Text + "\n";
                }
            }
            else
            {
                flag_incorrect_data = true;
                richTextBox1.Text += "序號格式不正確\n";
            }

            if (flag_incorrect_data == true)
            {
                richTextBox1.Text += "資料錯誤,長度 " + len.ToString() + "\t內容 " + tb_wait_check_data.Text + "\t清除\n";
                tb_wait_check_data.Clear();
            }
            else
            {
                richTextBox1.Text += "資料正確\n";
                lb_main_mesg1c.Text = "資料正確, 存檔中";

                timer_stage1c.Enabled = false;

                if ((cb_check1.Checked == true) && (cb_check2.Checked == true) && (cb_check3.Checked == true))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "底部", "Hi-pot", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == true) && (cb_check2.Checked == true) && (cb_check3.Checked == false))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "底部", "Hi-pot", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == true) && (cb_check2.Checked == false) && (cb_check3.Checked == true))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "底部", "", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == false) && (cb_check2.Checked == true) && (cb_check3.Checked == true))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "", "Hi-pot", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == true) && (cb_check2.Checked == false) && (cb_check3.Checked == false))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "底部", "", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == false) && (cb_check2.Checked == true) && (cb_check3.Checked == false))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "", "Hi-pot", "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else if ((cb_check1.Checked == false) && (cb_check2.Checked == false) && (cb_check3.Checked == true))
                    camera_serials.Add(new string[] { tb_wait_check_data.Text, "", "", "身體", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
                else
                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";

                exportCSV();

                delay(30);
                timer_stage1c.Enabled = true;
                tb_wait_check_data.Clear();

                cb_check1.Checked = false;
                cb_check2.Checked = false;
                cb_check3.Checked = false;
                cb_check1.BackColor = Color.White;
                cb_check2.BackColor = Color.White;
                cb_check3.BackColor = Color.White;
            }

        }

        private void cb_check1_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check1.Checked == true)
                cb_check1.BackColor = Color.Red;
            else
                cb_check1.BackColor = Color.White;

            if ((cb_check1.Checked == false) && (cb_check2.Checked == false) && (cb_check3.Checked == false))
                flag_stage1c_step = 0;
            else
                flag_stage1c_step = 1;
            this.tb_wait_check_data.Focus();
        }

        private void cb_check2_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check2.Checked == true)
                cb_check2.BackColor = Color.Red;
            else
                cb_check2.BackColor = Color.White;

            if ((cb_check1.Checked == false) && (cb_check2.Checked == false) && (cb_check3.Checked == false))
                flag_stage1c_step = 0;
            else
                flag_stage1c_step = 1;
            this.tb_wait_check_data.Focus();
        }

        private void cb_check3_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check3.Checked == true)
                cb_check3.BackColor = Color.Red;
            else
                cb_check3.BackColor = Color.White;

            if ((cb_check1.Checked == false) && (cb_check2.Checked == false) && (cb_check3.Checked == false))
                flag_stage1c_step = 0;
            else
                flag_stage1c_step = 1;
            this.tb_wait_check_data.Focus();
        }

        /*
        private void trackBar_Contrast3_Scroll(object sender, EventArgs e)
        {
            int setup = (int)trackBar_Contrast3.Value;
            int gain = 0;
            int offset = 0;

            if (setup >= 0)
            {
                if (setup < 8)
                    gain = setup * 2 + 0;
                else if (setup < 16)
                    gain = (setup - 8) * 6 + 16;
                else if (setup < 24)
                    gain = (setup - 16) * 6 + 64;
                else if (setup <= 32)
                    gain = (setup - 24) * 10 + 112;
                else
                {
                    richTextBox1.Text += "XXXXXXXXXXXXXX";
                }
                gain += 32;
            }
            else
            {
                gain = Math.Abs(setup) * 20 / 32 + 32;
            }

            offset = Math.Abs(setup) + 128;


            richTextBox1.Text += "setup = " + setup.ToString() + ", gain = " + gain.ToString() + ", offset = " + offset.ToString() + "\n";


            get_camera_contrast_brightness_setup();

            byte SendData;

            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data3 = 0x00;  //Y_OFFSET
            byte data4 = 0x20;  //Y_GAIN
            //byte data5 = 0x00;  //Y_BRIGHT
            byte data6 = 0x00;  //SIGN

            byte camera_yoffset_sign_bits_local = 0;

            if (setup >= 0)
            {
                data6 = 0x00;
                camera_yoffset_sign_bits_local = 0;
            }
            else
            {
                data6 = 0x0C;
                camera_yoffset_sign_bits_local = 1;
            }

            data3 = (byte)offset;
            data4 = (byte)gain;
            data6 = (byte)((((int)camera_ybright_sign_bits) << 3) | (((int)camera_yoffset_sign_bits_local) << 2));

            //richTextBox1.Text += "選擇了對比 " + trackBar_Contrast.Value.ToString() + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = data3;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = data4;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
*/
        /*
        //  Y BRIGHT 不設定
        DongleAddr_h = 0x58;
        DongleAddr_l = 0x07;    //Y_BRIGHT
        SendData = data5;
        Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        */
        /*
                    DongleAddr_h = 0x58;
                    DongleAddr_l = 0x08;    //SIGN
                    SendData = data6;
                    Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);








                }
                */

        private void trackBar_Brightness3_Scroll(object sender, EventArgs e)
        {
            //設定 Y_BRIGHT
            //get_camera_contrast_brightness_setup();

            byte SendData;
            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data6 = 0x00;  //SIGN
            //byte camera_ybright_sign_bits_local = 0;

            int setup = (int)trackBar_Brightness3.Value;
            numericUpDown_brightness3.Value = trackBar_Brightness3.Value;
            int brightness = 0;
            
            if (trackBar_Brightness3.Value >= 0)
            {
                brightness = setup;
                camera_ybright_sign_bits = 0;
            }
            else
            {
                brightness = -setup;
                camera_ybright_sign_bits = 1;
            }

            richTextBox1.Text += "選擇了亮度 " + setup.ToString() + "\t設定 " + brightness.ToString() + "\n";

            richTextBox1.Text += "camera_yoffset_sign_bits = " + camera_yoffset_sign_bits.ToString("X2") + "\n";
            
            data6 = (byte)((((int)camera_ybright_sign_bits) << 3) | (((int)camera_yoffset_sign_bits) << 2));

            richTextBox1.Text += "data6 = " + data6.ToString("X2") + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            SendData = (byte)brightness;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = data6;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        }

        private void trackBar_Contrast3_Scroll(object sender, EventArgs e)
        {
            //設定 Y_GAIN
            byte SendData;

            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data4 = 0x20;  //Y_GAIN

            int setup = (int)trackBar_Contrast3.Value;
            numericUpDown_gain3.Value = trackBar_Contrast3.Value;

            richTextBox1.Text += "c選擇了對比 " + setup.ToString() + "\t";

            data4 += (byte)setup;

            richTextBox1.Text += "設定值 " + data4.ToString() + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            SendData = data4;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            int num1 = (setup + 0x20) / 0x20;
            int num2 = (setup + 0x20) % 0x20;
            lb_gain_value.Text = (num1 + ((float)num2) / 32).ToString() + " X";
        }

        private void trackBar_Y_Offset3_Scroll(object sender, EventArgs e)
        {
            //設定 Y_OFFSET
            //get_camera_contrast_brightness_setup();

            byte SendData;
            byte data1 = 0x06;  //CTRL  //fixed
            byte data2 = 0x02;  //EN    //fixed
            byte data3 = 0x00;  //Y_OFFSET
            byte data6 = 0x00;  //SIGN
            //byte camera_yoffset_sign_bits_local = 0;
            int setup = (int)trackBar_Y_Offset3.Value;
            numericUpDown_offset3.Value = trackBar_Y_Offset3.Value;

            richTextBox1.Text += "選擇了OFFSET " + setup.ToString() + "\t";

            if (setup >= 0)
                camera_yoffset_sign_bits = 0;
            else
            {
                camera_yoffset_sign_bits = 1;
                setup = -setup;
            }

            data3 = (byte)setup;
            //richTextBox1.Text += "設定值 " + data3.ToString() + "\n";

            //richTextBox1.Text += "camera_yoffset_sign_bits = " + camera_yoffset_sign_bits.ToString("X2") + "\n";

            data6 = (byte)((((int)camera_ybright_sign_bits) << 3) | (((int)camera_yoffset_sign_bits) << 2));

            //richTextBox1.Text += "data6 = " + data6.ToString("X2") + "\n";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x00;    //CTRL
            SendData = data1;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x0B;    //EN
            SendData = data2;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            SendData = data3;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            SendData = data6;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);






        }

        private void button69_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte cnt1 = 0;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt1 * 4 + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);

            /*
            cnt1 = 1;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt1 << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            */

        }

        private void button71_Click(object sender, EventArgs e)
        {
            lb_data_camera_gain.Text = "";
            lb_data_camera_offset.Text = "";
            lb_data_camera_bright.Text = "";
            lb_data_camera_sign.Text = "";

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x06;    //Y_GAIN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            DongleAddr_h = 0x58;
            DongleAddr_l = 0x05;    //Y_OFFSET
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            //read current Y BRIGHT value;
            //讀取亮度	0x5807
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x07;    //Y_BRIGHT
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

            delay(100);

            //read current Y SIGN BITS value;
            //讀取SIGN BITS	0x5808
            DongleAddr_h = 0x58;
            DongleAddr_l = 0x08;    //SIGN
            Send_IMS_Data(0xA1, DongleAddr_h, DongleAddr_l, 0);

        }

        private void numericUpDown_offset3_ValueChanged(object sender, EventArgs e)
        {
            int dd = (int)numericUpDown_offset3.Value;
            if (dd < 0)
            {
                dd = -dd;
                tb_offset3.BackColor = Color.Gray;
            }
            else
            {
                tb_offset3.BackColor = Color.White;
            }
            tb_offset3.Text = dd.ToString("X2");
        }

        private void numericUpDown_gain3_ValueChanged(object sender, EventArgs e)
        {
            int dd = (int)numericUpDown_gain3.Value;
            if (dd < 0)
            {
                dd = -dd;
                tb_gain3.BackColor = Color.Gray;
            }
            else
            {
                tb_gain3.BackColor = Color.White;
            }
            tb_gain3.Text = dd.ToString("X2");
        }

        private void numericUpDown_brightness3_ValueChanged(object sender, EventArgs e)
        {
            int dd = (int)numericUpDown_brightness3.Value;
            if (dd < 0)
            {
                dd = -dd;
                tb_brightness3.BackColor = Color.Gray;
            }
            else
            {
                tb_brightness3.BackColor = Color.White;
            }
            tb_brightness3.Text = dd.ToString("X2");
        }

        private void button75_Click(object sender, EventArgs e)
        {
            button75.BackColor = Color.Red;
            button75.Text = "選檔";
            openFileDialog1.Title = "把Script寫進檔案";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "文字檔|*.txt|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                button75.Text = "設定中";
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                //richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";


                int x_st = 300;
                int y_st = 300;
                richTextBox2.Visible = true;
                richTextBox2.Location = new Point(x_st, y_st);
                richTextBox2.Size = new System.Drawing.Size(150, 500);
                richTextBox2.Clear();

                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox2.Text += sr.ReadToEnd();	//讀取所有文字內容
                sr.Close();

                parse_script_command_and_send();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
            button75.Text = "Gamma";
            button75.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button66_Click(object sender, EventArgs e)
        {
            string filename = "gamma_default.txt";
            richTextBox1.Text += "開啟Gamma檔案: " + filename + "\n";

            int x_st = 300;
            int y_st = 300;
            richTextBox2.Visible = true;
            richTextBox2.Location = new Point(x_st, y_st);
            richTextBox2.Size = new System.Drawing.Size(150, 500);
            richTextBox2.Clear();

            StreamReader sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            richTextBox2.Text += sr.ReadToEnd();	//讀取所有文字內容
            sr.Close();

            parse_script_command_and_send();
        }

        private void button68_Click(object sender, EventArgs e)
        {
            richTextBox2.Visible = false;
        }

        private void cb_Contrast_Brightness_Gamma_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_Contrast_Brightness_Gamma.Checked == true)
            {
                gb_contrast_brightness.Visible = true;
                gb_contrast_brightness2.Visible = true;
                gb_contrast_brightness3.Visible = true;
                pictureBox_contrast.Visible = true;
            }
            else
            {
                gb_contrast_brightness.Visible = false;
                gb_contrast_brightness2.Visible = false;
                gb_contrast_brightness3.Visible = false;
                pictureBox_contrast.Visible = false;
            }
        }

        private void cb_Gamma_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_Gamma.Checked == true)
                pictureBox_contrast.Size = new Size(300, 256);
            else
                pictureBox_contrast.Size = new Size(280, 256);

        }

        private void trackBar_WPT_Scroll(object sender, EventArgs e)
        {
            int setup = (int)trackBar_WPT.Value;
            numericUpDown_wpt3.Value = trackBar_WPT.Value;
            trackBar_BPT.Maximum = trackBar_WPT.Value - 1;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte SendData = (byte)setup;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        }

        private void numericUpDown_wpt3_ValueChanged(object sender, EventArgs e)
        {
            int dd = (int)numericUpDown_wpt3.Value;
            tb_wpt3.Text = dd.ToString("X2");
        }

        private void trackBar_BPT_Scroll(object sender, EventArgs e)
        {
            int setup = (int)trackBar_BPT.Value;
            numericUpDown_bpt3.Value = trackBar_BPT.Value;
            trackBar_WPT.Minimum = trackBar_BPT.Value + 1;

            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            byte SendData = (byte)setup;
            DongleAddr_h = 0x3A;
            DongleAddr_l = 0x04;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, SendData);
        }

        private void numericUpDown_bpt3_ValueChanged(object sender, EventArgs e)
        {
            int dd = (int)numericUpDown_bpt3.Value;
            tb_bpt3.Text = dd.ToString("X2");
        }

        private void button76_Click(object sender, EventArgs e)
        {
            //WPT BPT 也要 恢復成預設值
            trackBar_BPT.Maximum = 255;
            trackBar_WPT.Minimum = 0;
            trackBar_WPT.Value = 40;
            trackBar_BPT.Value = 25;
            trackBar_BPT.Maximum = trackBar_WPT.Value - 1;
            trackBar_WPT.Minimum = trackBar_BPT.Value + 1;
            numericUpDown_wpt3.Value = trackBar_WPT.Value;
            numericUpDown_bpt3.Value = trackBar_BPT.Value;

            trackBar_WPT_Scroll(sender, e);
            trackBar_BPT_Scroll(sender, e);
        }

        private void bt_location_Click(object sender, EventArgs e)
        {
            lb_auto_awb_cnt.Visible = true;
            cb_auto_search.Checked = false;
            richTextBox1.Text += "\n自動位置測試AWB ST, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB開始";
            awb_cnt = 0;
            flag_right_left_cnt = -8;
            flag_down_up_cnt = -8;

            //for (current_test_count = 1; current_test_count <= total_test_count; current_test_count++)
            for (current_test_count = 1; current_test_count <= 15; current_test_count++)
            {
                flag_right_left_cnt += 1;
                flag_down_up_cnt += 1;
                refresh_picturebox2();

                lb_auto_awb_cnt.Text = current_test_count.ToString();
                do_awb(sender, e);
                //delay(500);
            }
            lb_auto_awb_cnt.Visible = false;
            cb_auto_search.Checked = true;
            richTextBox1.Text += "\n自動位置測試AWB SP, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB結束";
        }

        private void bt_brightness_Click(object sender, EventArgs e)
        {
            flag_auto_brightness_awb = true;

            lb_auto_awb_cnt.Visible = true;
            cb_auto_search.Checked = false;
            richTextBox1.Text += "\n自動亮度測試AWB ST, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB開始";
            awb_cnt = 0;
            flag_right_left_cnt = 3;
            flag_down_up_cnt = 3;
            refresh_picturebox2();

            //for (current_test_count = 1; current_test_count <= total_test_count; current_test_count++)
            for (current_test_count = 1; current_test_count <= 30; current_test_count++)
            {
                lb_auto_awb_cnt.Text = current_test_count.ToString();
                do_awb(sender, e);
                delay(500);
            }
            lb_auto_awb_cnt.Visible = false;
            cb_auto_search.Checked = true;
            richTextBox1.Text += "\n自動亮度測試AWB SP, 時間 : " + DateTime.Now.ToString() + "\n";
            tb_awb_mesg.Text = "自動AWB結束";

            flag_auto_brightness_awb = false;

        }

        private void bt_reset_camera_Click(object sender, EventArgs e)
        {
            restore_camera_setup();
        }

        void measure_brightness_full()
        {
            int ww = 0;
            int hh = 0;
            int step = 20;
            int i;
            int count;
            double result = -1;
            int ww_st = 10;
            int ww_sp = 210;
            count = (ww_sp - ww_st) / step + 1;

            for (i = ww_st; i <= ww_sp; i += step)
            {
                ww = i;
                hh = i;
                do
                {
                    result = measure_brightness(0, 0, ww, hh);
                    brightness_data[(i - ww_st) / step] = result;
                }
                while (result < 0);

                delay(10);
            }

            richTextBox1.Text += "raw brightness data\n";
            for (i = 0; i < brightness_data.Length; i++)
            {
                richTextBox1.Text += "brightness_data(" + (i + 1).ToString() + ")=" + brightness_data[i].ToString() + ";\n";
            }

            richTextBox1.Text += "ring brightness data\n";
            int point_new;
            int point_old;
            brightness_data2[0] = brightness_data[0];
            for (i = 1; i < brightness_data.Length; i++)
            {
                point_new = (ww_st + step * i) * (ww_st + step * i);
                point_old = (ww_st + step * (i - 1)) * (ww_st + step * (i - 1));
                //richTextBox1.Text += "i = "+i.ToString() + ", point_new = " + point_new.ToString() + ", point_old = " + point_old + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + ", brightness_data_new = " + brightness_data[i].ToString() + ", brightness_data_old = " + brightness_data[i - 1] + "\n";
                brightness_data2[i] = (brightness_data[i] * point_new - brightness_data[i - 1] * point_old) / (point_new - point_old);
            }

            for (i = 0; i < brightness_data2.Length; i++)
            {
                richTextBox1.Text += "brightness_data2(" + (i + 1).ToString() + ")=" + brightness_data2[i].ToString() + ";\n";
            }
            return;
        }

        private void bt_measure_brightness_Click(object sender, EventArgs e)
        {
            //find_brightness();    old

            measure_brightness_full();

            /*
            int j;
            int cx = 0;
            int cy = 0;
            ww = 20;
            hh = 20;
            for (j = -100; j <= 100; j += 40)
            {
                cy = j;
                for (i = -100; i <= 100; i += 40)
                {
                    cx = i;
                    measure_brightness(cx, cy, ww, hh);
                    delay(50);
                }
            }
            */

            /*
            measure_brightness(0, 0, 25, 25);
            delay(50);
            measure_brightness(0, 0, 50, 50);
            delay(50);
            measure_brightness(0, 0, 75, 75);
            delay(50);
            measure_brightness(0, 0, 100, 100);
            delay(50);
            measure_brightness(0, 0, 125, 125);
            delay(50);
            measure_brightness(0, 0, 150, 150);
            delay(50);
            measure_brightness(0, 0, 175, 175);
            */
        }

        private void bt_save_program_picture_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive();
        }

        private void cb_reason1_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_reason1.Checked == true)
            {
                cb_reason2.Checked = false;
                cb_reason3.Checked = false;
                flag_ng_reason1 = true;
                flag_ng_reason2 = false;
                flag_ng_reason3 = false;
            }
            else
                flag_ng_reason1 = false;
            tb_reason.Clear();
            tb_reason.BackColor = Color.White;
            flag_wait_for_ng_reason = false;
        }

        private void cb_reason2_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_reason2.Checked == true)
            {
                cb_reason1.Checked = false;
                cb_reason3.Checked = false;
                flag_ng_reason1 = false;
                flag_ng_reason2 = true;
                flag_ng_reason3 = false;
            }
            else
                flag_ng_reason2 = false;
            tb_reason.Clear();
            tb_reason.BackColor = Color.White;
            flag_wait_for_ng_reason = false;
        }

        private void cb_reason3_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_reason3.Checked == true)
            {
                cb_reason1.Checked = false;
                cb_reason2.Checked = false;
                flag_ng_reason1 = false;
                flag_ng_reason2 = false;
                flag_ng_reason3 = true;
                tb_reason.BackColor = Color.Pink;
                flag_wait_for_ng_reason = true;
                tb_reason.Focus();
            }
            else
            {
                flag_ng_reason3 = false;
                tb_reason.Clear();
                tb_reason.BackColor = Color.White;
                flag_wait_for_ng_reason = false;
            }
        }

        private void button78_Click(object sender, EventArgs e)
        {
            if (tb_reason.Text.Length > 0)
            {
                //tb_reason.Text.Replace("\n", "");
                tb_reason.BackColor = Color.White;
                flag_wait_for_ng_reason = false;
            }
            else
            {
                lb_main_mesg9.Text = "等待輸入 NG其他原因";
                tb_reason.BackColor = Color.Pink;
                flag_wait_for_ng_reason = true;
            }
        }

        private void tb_reason_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button78_Click(sender, e);
            }
        }

        private void cb_stage1_ng_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_stage1_ng.Checked == true)
            {
                /*
                gb_ng_reason1.Visible = true;
                cb_stage1_ng.ForeColor = Color.Red;
                tb_reason_stage1.Visible = false;
                button79.Visible = false;
                gb_ng_reason1.Size = new Size(200, 100);
                */
            }
            else
            {
                gb_ng_reason1.Visible = false;
                cb_stage1_ng.ForeColor = Color.Black;
                cb_stage1_ng.Visible = false;
                cb_stage1_ng.Checked = false;
                flag_wait_for_ng_reason = false;
                tb_reason_stage1.Clear();
            }
            lb_ng_reason.Text = "";
        }

        private void button79_Click(object sender, EventArgs e)
        {
            if (tb_reason_stage1.Text.Length > 0)
            {
                tb_reason_stage1.BackColor = Color.White;
                flag_wait_for_ng_reason = false;
                this.tb_sn_opal.Focus();
            }
            else
            {
                lb_main_mesg2.Text = "等待輸入 NG其他原因";
                tb_reason_stage1.BackColor = Color.Pink;
                flag_wait_for_ng_reason = true;
            }

        }

        private void tb_reason_stage1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                richTextBox1.Text += "len = " + tb_reason_stage1.Text.Length.ToString() + "\n";
                tb_reason_stage1.Text = tb_reason_stage1.Text.Replace("\n", "");
                tb_reason_stage1.Text = tb_reason_stage1.Text.Replace("\r", "");

                button79_Click(sender, e);
                richTextBox1.Text += "len = " + tb_reason_stage1.Text.Length.ToString() + "\n";

            }
        }

        private void button80_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void button82_Click(object sender, EventArgs e)
        {
            if (flag_david_test == true)
            {
                serialPort1.PortName = "COM3";
                serialPort1.BaudRate = 115200;
            }
            else
            {
                serialPort1.PortName = comboBox4.Text;
                serialPort1.BaudRate = int.Parse(comboBox3.Text);
            }

            serialPort1.Open();
            if (serialPort1.IsOpen)
            {
                button82.Enabled = false;
                button81.Enabled = true;
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                flag_comport_ok = true;
            }
        }

        private void button81_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                button82.Enabled = true;
                button81.Enabled = false;
                this.BackColor = Color.Yellow;
                flag_comport_ok = false;
            }
        }

        private void button83_Click(object sender, EventArgs e)
        {
            richTextBox3.Clear();
            timer12_cnt = 0;
        }

        private void timer_stage12_Tick(object sender, EventArgs e)
        {
            if (flag_network_disk_status == false)
            {
                tb_wait_sn_data12.Clear();

                show_main_message1("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message2("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message3("無法連上網路磁碟機", S_FALSE, 30);
                show_main_message12("無法連上網路磁碟機", S_FALSE, 30);
                return;
            }

            ccc++;
            if (flag_wait_cosmo_message == true)
            {
                if ((ccc % 4) == 0)
                    lb_main_mesg12b.Text = "等待COSMO資料 \\";
                else if ((ccc % 4) == 1)
                    lb_main_mesg12b.Text = "等待COSMO資料 |";
                else if ((ccc % 4) == 2)
                    lb_main_mesg12b.Text = "等待COSMO資料 /";
                else
                    lb_main_mesg12b.Text = "等待COSMO資料 -";

                return;
            }

            if (flag_doing_writing_data == true)
            {
                richTextBox1.Text += "正在存檔, 忽略\n";
                return;
            }

            if ((ccc % 4) == 0)
                lb_main_mesg12b.Text = "輸入相機序號 \\";
            else if ((ccc % 4) == 1)
                lb_main_mesg12b.Text = "輸入相機序號 |";
            else if ((ccc % 4) == 2)
                lb_main_mesg12b.Text = "輸入相機序號 /";
            else
                lb_main_mesg12b.Text = "輸入相機序號 -";

            if ((ccc % 4) == 0)
            {
                if (this.tb_wait_sn_data12.Focused == false)
                {
                    richTextBox1.Text += "F12";
                    this.tb_sn_opal12.BackColor = Color.Pink;
                    this.tb_wait_sn_data12.Focus();
                }
            }

            if ((timer_cnt++ % 10) == 0)
            {
                richTextBox1.Text += "十二";
            }

            int result = check_tb_sn_opal_data12();

            if (result == S_OK)
            {
                lb_main_mesg12c.Text = "";
                timer12_cnt = 0;
                tb_sn_opal12.Text = tb_wait_sn_data12.Text;
                lb_main_mesg12a.Text = "SN : " + tb_sn_opal12.Text;
                //timer_stage12.Enabled = false;

                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料

                flag_wait_cosmo_message = true;
                flag_ok_data1 = true;   //camera serial ok
                flag_ok_data3 = true;   //dummy
                g12.Clear(BackColor);
                g12.DrawString("等待COSMO", new Font("標楷體", 55), new SolidBrush(Color.Blue), new PointF(10, 25));
                richTextBox3.Clear();

                //lb_main_mesg12b.Text = "資料正確, 存檔中";
                //lb_main_mesg12b.Text = "資料正確, 存檔中";
                //lb_main_mesg12b.Text = "資料正確, 存檔中";
                //lb_main_mesg12b.Text = "資料正確, 存檔中";

                //save_image_to_drive();
                
                //delay(30);
                //timer_stage12.Enabled = true;

                //tb_wait_sn_data12.Text = "";

                //tb_wait_sn_data12.Clear();

            }

        }

        private void cb_check1c_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check1c.Checked == true)
                cb_check1c.BackColor = Color.Red;
            else
                cb_check1c.BackColor = Color.White;
        }

        private void cb_check2c_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check2c.Checked == true)
                cb_check2c.BackColor = Color.Red;
            else
                cb_check2c.BackColor = Color.White;
        }

        private void cb_check3c_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_check3c.Checked == true)
                cb_check3c.BackColor = Color.Red;
            else
                cb_check3c.BackColor = Color.White;
        }

        private void bt_read_camera_register_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xDD, 0xEE, 0x01);
        }

        private void bt_restore_camera_setup_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xDD, 0xEE, 0x02);
        }

        private void button84_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xDD, 0xEE, 0x01);
        }

        private void button85_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xDD, 0xEE, 0x02);
        }

        double measure_brightness(int cx, int cy, int ww, int hh)
        {
            if ((ww <= 0) || (hh <= 0))
            {
                richTextBox1.Text += "量測點數 ww = " + ww.ToString() + ", hh = " + hh.ToString() + " 不合法\n";
                return -1;
            }
            flag_do_find_awb_location = true;
            int x_st = 0;
            int y_st = 0;
            int w;
            int h;
            int i;
            int j;
            Color p;
            Bitmap bm2 = null;
            double y_total = 0;
            int result = -1;

            tb_awb_mesg.Text = "量測亮度";

            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                //bm2 = bm;
                bm2 = (Bitmap)bm.Clone();
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f1 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return result;
            }

            try
            {
                ga = Graphics.FromImage(bm2);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f2 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return result;
            }

            try
            {
                w = bm2.Width;
                h = bm2.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息f3 : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                flag_do_find_awb_location = false;
                return result;
            }

            x_st = w / 2 + cx - ww / 2;
            y_st = h / 2 + cy - hh / 2;
            if (x_st < 0)
                x_st = 0;
            if (y_st < 0)
                y_st = 0;
            if ((x_st + ww) > w)
                x_st = w - ww;
            if ((y_st + hh) > h)
                y_st = h - hh;

            //richTextBox1.Text += "中心點c x = " + cx.ToString() + ", cy = " + cy.ToString() + "\n";
            //richTextBox1.Text += "量測點數 ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";
            //richTextBox1.Text += "起點 x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";

            for (j = y_st; j < (y_st + hh); j++)
            {
                for (i = x_st; i < (x_st + ww); i++)
                {
                    p = bm2.GetPixel(i, j);
                    //bm2.SetPixel(i, j, Color.FromArgb(255, 0, 0));
                    RGB pp = new RGB(p.R, p.G, p.B);
                    YUV yyy = new YUV();
                    yyy = RGBToYUV(pp);
                    y_total += yyy.Y;
                }
            }
            //ga.DrawRectangle(new Pen(Color.Red, 1), x_st - 2, y_st - 2, ww + 4, hh + 4);

            //richTextBox1.Text += "y_total = " + y_total.ToString() + "\n";
            //richTextBox1.Text += "y_avg = " + (y_total / (ww * hh)).ToString() + "\n\n";

            //tb_awb_mesg.Text = (y_total / (ww * hh)).ToString();

            GC.Collect();       //回收資源
            //pictureBox1.Image = bm2;

            delay(10);
            flag_do_find_awb_location = false;
            return y_total / (ww * hh);
        }

        void check_awb_result(int do_awb_result)
        {
            richTextBox1.Text += "AWB結果 : " + do_awb_result.ToString() + "\n";

            string awb_result = "OK";
            if (do_awb_result == S_OK)
            {
                awb_result = "OK";
            }
            else if (do_awb_result == DONGLE_NONE)
            {
                awb_result = "無連接器";
            }
            else if (do_awb_result == CAMERA_NONE)
            {
                awb_result = "\"有連接器, 無相機\"";
            }
            else if (do_awb_result == CAMERA_UNKNOWN)
            {
                awb_result = "相機狀態不明";
            }
            else if (do_awb_result == CAMERA_SENSOR_FAIL)
            {
                awb_result = "相機無法讀寫";
            }
            else if (do_awb_result == REASON_AWB_PROCESSING)
            {
                awb_result = "AWB進行中";
            }
            else if (do_awb_result == REASON_AWB_TIMEOUT)
            {
                awb_result = "AWB作業延時";
            }
            else if (do_awb_result == REASON_NO_COMPORT)
            {
                awb_result = "無comport連線";
            }
            else if (do_awb_result == REASON_NO_IMS_CAMERA)
            {
                awb_result = "無IMS相機";
            }
            else if (do_awb_result == REASON_FIND_AWB_AREA_FAIL_TOO_SMALL)
            {
                awb_result = "\"AWB搜尋失敗, 太小\"";
            }
            else if (do_awb_result == REASON_FIND_AWB_AREA_FAIL_TOO_FAR)
            {
                awb_result = "\"AWB搜尋失敗, 太遠\"";
            }
            else if (do_awb_result == REASON_MANUALLY_INTERRUPT)
            {
                awb_result = "AWB人為中斷";
            }
            else
            {
                //awb_result = "\"狀態不明a, status = " + g_conn_status.ToString()+"\"";
                awb_result = "其他";
            }

            //richTextBox1.Text += "old font = " + tb_awb_mesg.Font.Name + "\n";

            if (awb_result.Length > 15)
            {
                tb_awb_mesg.Font = new Font("標楷體", 10);
            }
            else if (awb_result.Length > 10)
            {
                tb_awb_mesg.Font = new Font("標楷體", 16);
            }

            tb_awb_mesg.Text = awb_result;
            lb_main_mesg2.Text = awb_result;

            richTextBox1.Text += "AWB結果 : " + awb_result + "\n";

            camera_serials.Add(new string[] { tb_sn_opal.Text, awb_result, DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });
            exportCSV();

            if (do_awb_result != S_OK)
            {
                tb_awb_mesg.BackColor = Color.Pink;
                timer_awb.Enabled = false;
                bt_awb_break.Visible = true;
                bt_awb_break.Text = "確認";
                flag_wait_for_confirm = true;
            }
            return;
        }

        private void button86_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void button89_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = comboBox7.Text;
            serialPort1.BaudRate = int.Parse(comboBox6.Text);

            serialPort1.Open();
            if (serialPort1.IsOpen)
            {
                button89.Enabled = false;
                button90.Enabled = true;
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                flag_comport_ok = true;
            }
        }

        private void button90_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                button89.Enabled = true;
                button90.Enabled = false;
                this.BackColor = Color.Yellow;
                flag_comport_ok = false;
            }
        }

        private void button91_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0xCC, 0xBB, 0xAA);
            show_main_message1("LED變換", S_FALSE, 10);
        }

        private void button92_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x03);  //To manual mode
            richTextBox1.Text += "到手動模式\n";
            show_main_message1("到手動模式", S_FALSE, 10);
            button92.BackColor = Color.Pink;
            button93.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void button93_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == false)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xA0, 0x35, 0x03, 0x00);  //To auto mode
            richTextBox1.Text += "到自動模式\n";
            show_main_message1("到自動模式", S_FALSE, 10);
            button92.BackColor = System.Drawing.SystemColors.ControlLight;
            button93.BackColor = Color.Pink;
        }
    }
}

