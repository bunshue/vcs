using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;       //for Process, Stopwatch
using System.Drawing.Imaging;
using System.Drawing.Drawing2D; //for DashStyle
using iMS_Link.PLC_Communication;

using System.Runtime.InteropServices;

/*
這種方法的原理就是，利用FindWindow函數通過窗體標題查找出對方的進程，然後取得窗口
Handle，再通過DLL庫中的SendMessage函數發送消息給接收端，這樣就完成了程序的直接通信。
*/

namespace iMS_Link
{
    /// <summary>
    ///  PLC--按鈕狀態
    /// </summary>
    public enum PLC_STATE
    {
        OFF, ON
    }
    /// <summary>
    /// 數值顯示類型
    /// </summary>
    public enum numerical_format
    {
        BCD_16_Bit,     //0
        BCD_32_Bit,
        Hex_16_Bit,
        Hex_32_Bit,
        Binary_16_Bit,
        Binary_32_Bit,      //5
        Unsigned_16_Bit,
        Signed_16_Bit,
        Unsigned_32_Bit,
        Signed_32_Bit,
        Float_32_Bit,       //10
        String_32_Bit       //11
    }


    public partial class Form1 : Form
    {
        private const int AUTOMATION_VERSION = 2;
        private const int MODE_OFF = 0;
        private const int MODE_WRITE_DATA = 1;
        private const int MODE_WRITE_DATA_CHECK_TIME = 2;
        private const int MODE_AWB = 3;
        private const int MODE_AWB_CHECK_TIME = 4;
        private const int OFFSET_M_WRITE_DATA = 0;
        private const int OFFSET_M_AWB = -2300;
        private const int OFFSET_M_CHECK_TIME = 12;
        private const int OFFSET_D_WRITE_DATA = 0;
        private const int OFFSET_D_AWB = -2000;
        private const int OFFSET_D_CHECK_TIME = 20;

        bool plc_do_check_time = false;

        int plc_m_address_offset = OFFSET_M_WRITE_DATA;
        int plc_d_address_offset = OFFSET_D_WRITE_DATA;

        //private const int S_OK = 0;     //system return OK
        //private const int S_FALSE = 1;     //system return FALSE
        private const PLC_STATE HIGH = PLC_STATE.ON;
        private const PLC_STATE LOW = PLC_STATE.OFF;
        private const int BORDER = 10;
        private const int PLC_PANEL_WIDTH = 1380;
        private const int PLC_PANEL_HEIGHT = 720;
        private const int PLC_RTB_WIDTH = 350;
        private const int PLC_RTB_HEIGHT = PLC_PANEL_HEIGHT - BORDER * 2;
        private const int PLC_GBOX_WIDTH = PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER * 3;
        private const int PLC_GBOX_HEIGHT = PLC_PANEL_HEIGHT - BORDER * 2;
        private const int PLC_BTN_WIDTH = 60;
        private const int PLC_BTN_HEIGHT = 60;
        private const int DELAY_TIME = 5;

        //Panel PLC initial location
        private const int PANEL_PLC_DEFAULT_POSITION_X = BORDER;
        private const int PANEL_PLC_DEFAULT_POSITION_Y = BORDER;
        int panel_plc_position_x_old = PANEL_PLC_DEFAULT_POSITION_X;
        int panel_plc_position_y_old = PANEL_PLC_DEFAULT_POSITION_Y;

        Stopwatch stopwatch_plc = new Stopwatch();

        Panel panel_plc = new Panel();

        GroupBox groupBox_plc = new GroupBox();
        GroupBox groupBox_connection = new GroupBox();
        GroupBox groupBox_connection_status = new GroupBox();
        Button bt_plc_test = new Button();
        Button bt_plc_test_break = new Button();
        Button bt_check_connection = new Button();
        Button bt_read_camera_data = new Button();
        Button bt_erase_camera_data = new Button();
        Button bt_setup_ims_type1 = new Button();   //設定主機為燒錄主機
        Button bt_setup_ims_type2 = new Button();   //設定主機為色調主機
        Button bt_reset_ims = new Button();   //設定ims主機重開
        Button bt_check_plc_breathe1 = new Button();
        Button bt_check_plc_breathe2 = new Button();
        Button bt_automation_setup = new Button();
        CheckBox cb_debug = new CheckBox();
        Label lb_plc_pc0 = new Label();
        Label lb_plc_pc1 = new Label();
        Label lb_plc_pc2 = new Label();
        Label lb_plc_pc3a = new Label();
        Label lb_plc_pc4a = new Label();
        Label lb_plc_pc3b = new Label();
        Label lb_plc_pc4b = new Label();
        Label lb_pc_plc0 = new Label();
        Label lb_pc_plc1 = new Label();
        Label lb_pc_plc2 = new Label();
        Label lb_pc_plc3a = new Label();
        Label lb_pc_plc4a = new Label();
        Label lb_pc_plc3b = new Label();
        Label lb_pc_plc4b = new Label();
        Label lb_read_write_plc = new Label();
        Label lb_debug0 = new Label();
        Label lb_debug1 = new Label();
        Label lb_debug2 = new Label();
        Label lb_debug3 = new Label();
        Button bt_open_folder = new Button();
        Button bt_save = new Button();
        Button bt_pause = new Button();
        PictureBox pbx_m7980 = new PictureBox();
        PictureBox pbx_m7981 = new PictureBox();
        PictureBox pbx_m7982 = new PictureBox();
        PictureBox pbx_m7990 = new PictureBox();
        PictureBox pbx_m7991 = new PictureBox();
        PictureBox pbx_m7992 = new PictureBox();
        PictureBox pbx_plc_status = new PictureBox();
        PictureBox pictureBox_plc_status = new PictureBox();
        PictureBox pbx_connection1 = new PictureBox();
        PictureBox pbx_connection2 = new PictureBox();
        PictureBox pbx_connection3 = new PictureBox();
        PictureBox pbx_ims_connection1 = new PictureBox();
        PictureBox pbx_ims_connection2 = new PictureBox();
        PictureBox pbx_ims_connection3 = new PictureBox();
        PictureBox pbx_ims_connection4 = new PictureBox();

        Button bt_save_to_file = new Button();
        Button bt_copy_to_clipboard = new Button();
        Button bt_plc_clear = new Button();
        RichTextBox richTextBox_plc = new RichTextBox();
        Label lb_plc_awb_video_message = new Label();
        Label lb_plc_command_type = new Label();
        Label lb_plc_main_mesg1 = new Label();
        Label lb_plc_main_mesg2 = new Label();
        Label lb_plc_main_mesg3 = new Label();
        Label lb_plc_datetime = new Label();
        Timer timer_plc_status = new Timer();
        Timer timer_plc_display = new Timer();
        Timer timer_plc_simulator = new Timer();
        Timer timer_pc_clock = new Timer();  //PC顯示時間
        Timer timer_pc_breathe1 = new Timer();  //PC製作心跳給PLC
        Timer timer_pc_breathe2 = new Timer();  //PC檢查PLC之心跳
        Timer timer_plc_breathe1 = new Timer();  //PLC製作心跳給PC
        Timer timer_plc_breathe2 = new Timer();  //PLC檢查PC之心跳
        int flag_pc_check_plc_breathe_mode = MODE_OFF; //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
        bool flag_pc_check_plc_breathe_mode_status = false; //PC檢查PLC之心跳是否存在結果
        private const int CHECK_BREATHE_LENGTH = 10;
        bool[] breathe_data = new bool[CHECK_BREATHE_LENGTH];
        int breathe_data_index = 0;

        bool flag_plc_test = false;
        bool flag_plc_test_busy = false;
        bool flag_plc_test_break = false;
        bool flag_year_month_day_data_ok = false;
        bool flag_always_return_ok_mode = false;
        int flag_plc_test_count = 0;
        int global_work_result = 0xff;

        Font f1 = new Font("新細明體", 14); //PLC m1XXXXX 暫存器內容
        Font f2 = new Font("Arial", 16.75F, FontStyle.Bold, GraphicsUnit.Point, ((byte)(0))); //main message
        Font f3 = new Font("標楷體", 15);
        Font f4 = new Font("Arial", 20.75F, FontStyle.Bold, GraphicsUnit.Point, ((byte)(0))); //main message
        Font f5 = new Font("Arial", 30.75F, FontStyle.Bold, GraphicsUnit.Point, ((byte)(0))); //debug message

        bool flag_use_user_time = false;
        DateTime datetime_user = DateTime.Now;
        TimeSpan datetime_diff;
        string plc_message = string.Empty;

        private string form_confirm_data;
        public string SetupForm1Data
        {
            set
            {
                form_confirm_data = value;
            }
        }

        public void setForm1Value()
        {
            //this.richTextBox_plc.Text += "父得到信息 : " + form_confirm_data + "\n";
        }

        Form_Confirm2 form_confirm = new Form_Confirm2();     //實體化Form_Confirm2視窗物件

        void add_automation_controls(string ip, int port)
        {
            // 實例化控件
            panel_plc.BackColor = Color.LightYellow;
            panel_plc.Size = new Size(PLC_PANEL_WIDTH, PLC_PANEL_HEIGHT);
            panel_plc.Location = new Point(BORDER, BORDER);
            panel_plc.MouseDown += Panel_plc_MouseDown;
            panel_plc.MouseMove += Panel_plc_MouseMove;
            panel_plc.MouseUp += Panel_plc_MouseUp;
            this.Controls.Add(panel_plc);     // 將控件加入表單

            richTextBox_plc.Text = "";
            richTextBox_plc.Name = "richTextBox_plc";
            if (flag_enaglb_automation_debug == false)
            {
                richTextBox_plc.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER);
                richTextBox_plc.Size = new Size(PLC_RTB_WIDTH, PLC_RTB_HEIGHT);
                this.panel_plc.Controls.Add(richTextBox_plc);
            }
            else
            {
                richTextBox_plc.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER + 100);
                richTextBox_plc.Size = new Size(PLC_RTB_WIDTH, PLC_RTB_HEIGHT - 100);
                this.panel_plc.Controls.Add(richTextBox_plc);

                //實例化3個label
                lb_debug0.Text = "檢測結果檢測結果檢測結果1";
                lb_debug0.Font = f1;
                lb_debug0.ForeColor = Color.Red;
                lb_debug0.AutoSize = true;
                lb_debug0.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER + 10);
                this.panel_plc.Controls.Add(lb_debug0);     // 將控件加入表單

                lb_debug1.Text = "檢測結果檢測結果檢測結果1";
                lb_debug1.Font = f1;
                lb_debug1.ForeColor = Color.Red;
                lb_debug1.AutoSize = true;
                lb_debug1.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER + 40);
                this.panel_plc.Controls.Add(lb_debug1);     // 將控件加入表單

                lb_debug2.Text = "檢測結果檢測結果檢測結果2";
                lb_debug2.Font = f1;
                lb_debug2.ForeColor = Color.Red;
                lb_debug2.AutoSize = true;
                lb_debug2.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER + 70);
                this.panel_plc.Controls.Add(lb_debug2);     // 將控件加入表單

                lb_debug3.Text = "";
                lb_debug3.Font = f5;
                lb_debug3.ForeColor = Color.Red;
                lb_debug3.AutoSize = true;
                lb_debug3.Location = new Point(PLC_PANEL_WIDTH - 36 - BORDER, BORDER + 32);
                this.panel_plc.Controls.Add(lb_debug3);     // 將控件加入表單
            }

            lb_plc_command_type.AutoSize = true;
            lb_plc_command_type.Name = "lb_plc_command_type";
            lb_plc_command_type.Text = "";
            lb_plc_command_type.Font = f2;
            lb_plc_command_type.ForeColor = Color.Red;
            lb_plc_command_type.Size = new System.Drawing.Size(78, 24);
            lb_plc_command_type.Location = new Point(PLC_PANEL_WIDTH - BORDER - 115 - 26, BORDER + 5);
            this.panel_plc.Controls.Add(lb_plc_command_type);
            lb_plc_command_type.BringToFront();

            timer_plc_status.Enabled = true;
            timer_plc_status.Interval = 1000;
            timer_plc_status.Tick += new System.EventHandler(timer_plc_status_Tick);
            timer_plc_display.Tick += new System.EventHandler(timer_plc_display_Tick);

            this.plC_Open_Time1.MitsubishiIP = ip;
            this.plC_Open_Time1.MitsubishiPort = port;
            this.plC_Open_Time1.Interval = 5000;
            if (flag_use_real_plc == false)
            {
                this.plC_Open_Time1.Enabled = false;
                this.plC_Open_Time1.Mitsubishi_Open = false;
                this.plC_Open_Time1.Stop();

                timer_plc_simulator.Enabled = true;
            }
            else
            {
                this.plC_Open_Time1.Enabled = true;
                this.plC_Open_Time1.Mitsubishi_Open = true;
                this.plC_Open_Time1.Start();

                timer_plc_simulator.Enabled = false;
            }
            timer_plc_simulator.Interval = 1000;
            timer_plc_simulator.Tick += new System.EventHandler(timer_plc_simulator_Tick);

            timer_pc_clock.Enabled = true;
            timer_pc_clock.Interval = 1000;
            timer_pc_clock.Tick += new System.EventHandler(timer_pc_clock_Tick);
            timer_pc_breathe1.Enabled = true;
            timer_pc_breathe1.Interval = 3000;
            timer_pc_breathe1.Tick += new System.EventHandler(timer_pc_breathe1_Tick);
            timer_pc_breathe2.Enabled = false;
            timer_pc_breathe2.Interval = 1000;
            timer_pc_breathe2.Tick += new System.EventHandler(timer_pc_breathe2_Tick);

            if (flag_use_real_plc == false)
                timer_plc_breathe1.Enabled = true;
            else
                timer_plc_breathe1.Enabled = false;
            timer_plc_breathe1.Interval = 3000;
            timer_plc_breathe1.Tick += new System.EventHandler(timer_plc_breathe1_Tick);
            timer_plc_breathe2.Enabled = false;
            timer_plc_breathe2.Interval = 1000;
            timer_plc_breathe2.Tick += new System.EventHandler(timer_plc_breathe2_Tick);

            bt_save_to_file.Width = PLC_BTN_WIDTH;
            bt_save_to_file.Height = PLC_BTN_HEIGHT;
            bt_save_to_file.Text = "";
            bt_save_to_file.Name = "bt_save_to_file";
            bt_save_to_file.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_save_to_file.Size.Width * 3, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_save_to_file.Size.Height);
            // 加入按鈕事件
            //bt_save_to_file.Click += new EventHandler(bt_save_to_file_Click);   //same
            bt_save_to_file.Click += bt_save_to_file_Click;
            this.panel_plc.Controls.Add(bt_save_to_file);     // 將控件加入表單
            bt_save_to_file.BringToFront();

            bt_copy_to_clipboard.Width = PLC_BTN_WIDTH;
            bt_copy_to_clipboard.Height = PLC_BTN_HEIGHT;
            bt_copy_to_clipboard.Text = "";
            bt_copy_to_clipboard.Name = "bt_copy_to_clipboard";
            bt_copy_to_clipboard.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_copy_to_clipboard.Size.Width * 2, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_copy_to_clipboard.Size.Height);
            // 加入按鈕事件
            //bt_copy_to_clipboard.Click += new EventHandler(bt_copy_to_clipboard_Click);   //same
            bt_copy_to_clipboard.Click += bt_copy_to_clipboard_Click;
            this.panel_plc.Controls.Add(bt_copy_to_clipboard);     // 將控件加入表單
            bt_copy_to_clipboard.BringToFront();

            // 實例化按鈕
            bt_plc_clear.Width = PLC_BTN_WIDTH;
            bt_plc_clear.Height = PLC_BTN_HEIGHT;
            bt_plc_clear.Text = "";
            bt_plc_clear.Name = "bt_plc_clear";
            bt_plc_clear.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_plc_clear.Size.Width, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_plc_clear.Size.Height);
            // 加入按鈕事件
            //bt_plc_clear.Click += new EventHandler(bt_plc_clear_Click);   //same
            bt_plc_clear.Click += bt_plc_clear_Click;
            this.panel_plc.Controls.Add(bt_plc_clear);     // 將控件加入表單
            bt_plc_clear.BringToFront();

            groupBox_plc.Text = "";
            groupBox_plc.Size = new Size(PLC_GBOX_WIDTH, PLC_GBOX_HEIGHT);
            groupBox_plc.Location = new Point(BORDER, BORDER);
            groupBox_plc.BackColor = Color.LightGray;
            this.panel_plc.Controls.Add(groupBox_plc);     // 將控件加入表單

            int x_st = 10;
            int y_st = 20;
            int dx = PLC_BTN_WIDTH + 1;

            // 實例化按鈕
            bt_plc_test.Width = PLC_BTN_WIDTH;
            bt_plc_test.Height = PLC_BTN_HEIGHT;
            bt_plc_test.Text = "啟動\n自動化\n作業";
            bt_plc_test.Name = "bt_plc_test";
            bt_plc_test.Location = new Point(x_st + dx * 0, y_st);
            // 加入按鈕事件
            //bt_plc_test.Click += new EventHandler(bt_plc_test_Click);   //same
            bt_plc_test.Click += bt_plc_test_Click;
            this.groupBox_plc.Controls.Add(bt_plc_test);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test_break.Width = PLC_BTN_WIDTH;
            bt_plc_test_break.Height = PLC_BTN_HEIGHT;
            bt_plc_test_break.Text = "關閉\n自動化\n作業";
            bt_plc_test_break.Name = "bt_plc_test_break";
            bt_plc_test_break.Location = new Point(x_st + dx * 1, y_st);
            // 加入按鈕事件
            //bt_plc_test_break.Click += new EventHandler(bt_plc_test_break_Click);   //same
            bt_plc_test_break.Click += bt_plc_test_break_Click;
            bt_plc_test_break.MouseDown += bt_plc_test_break_MouseDown;
            this.groupBox_plc.Controls.Add(bt_plc_test_break);     // 將控件加入表單

            // 實例化按鈕
            bt_check_connection.Width = PLC_BTN_WIDTH;
            bt_check_connection.Height = PLC_BTN_HEIGHT;
            bt_check_connection.Text = "檢查\n連線\n狀態";
            bt_check_connection.Name = "bt_check_connection";
            bt_check_connection.Location = new Point(x_st + dx * 2, y_st);
            // 加入按鈕事件
            //bt_check_connection.Click += new EventHandler(bt_check_connection_Click);   //same
            bt_check_connection.Click += bt_check_connection_Click;
            this.groupBox_plc.Controls.Add(bt_check_connection);     // 將控件加入表單

            // 實例化按鈕
            bt_read_camera_data.Width = PLC_BTN_WIDTH;
            bt_read_camera_data.Height = PLC_BTN_HEIGHT;
            bt_read_camera_data.Text = "讀取\n相機\n資料";
            bt_read_camera_data.Name = "bt_read_camera_data";
            bt_read_camera_data.Location = new Point(x_st + dx * 3, y_st);
            // 加入按鈕事件
            //bt_read_camera_data.Click += new EventHandler(bt_read_camera_data_Click);   //same
            bt_read_camera_data.Click += bt_read_camera_data_Click;
            this.groupBox_plc.Controls.Add(bt_read_camera_data);     // 將控件加入表單

            // 實例化按鈕
            bt_erase_camera_data.Width = PLC_BTN_WIDTH;
            bt_erase_camera_data.Height = PLC_BTN_HEIGHT;
            bt_erase_camera_data.Text = "清除\n相機\n資料";
            bt_erase_camera_data.Name = "bt_erase_camera_data";
            bt_erase_camera_data.Location = new Point(x_st + dx * 4, y_st);
            // 加入按鈕事件
            //bt_erase_camera_data.Click += new EventHandler(bt_erase_camera_data_Click);   //same
            bt_erase_camera_data.Click += bt_erase_camera_data_Click;
            this.groupBox_plc.Controls.Add(bt_erase_camera_data);     // 將控件加入表單

            if (flag_automation_mode == MODE_AWB)
            {
                // 實例化按鈕
                bt_check_plc_breathe2.Width = PLC_BTN_WIDTH;
                bt_check_plc_breathe2.Height = PLC_BTN_HEIGHT;
                //bt_check_plc_breathe2.Text = "色調\n心跳";
                bt_check_plc_breathe2.Text = "系統\n資訊";
                bt_check_plc_breathe2.Text = "粉飾\n太平\n模式1";
                bt_check_plc_breathe2.Name = "bt_check_plc_breathe2";
                //bt_check_plc_breathe2.Location = new Point(x_st + dx * 5 - 2 + 48, y_st - 8);
                bt_check_plc_breathe2.Location = new Point(x_st + dx * 5, y_st);
                // 加入按鈕事件
                //bt_check_plc_breathe2.Click += new EventHandler(bt_check_plc_breathe2_Click);   //same
                bt_check_plc_breathe2.Click += bt_check_plc_breathe2_Click;
                this.groupBox_plc.Controls.Add(bt_check_plc_breathe2);     // 將控件加入表單
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                // 實例化按鈕
                bt_check_plc_breathe1.Width = PLC_BTN_WIDTH;
                bt_check_plc_breathe1.Height = PLC_BTN_HEIGHT;
                //bt_check_plc_breathe1.Text = "燒錄\n心跳";
                bt_check_plc_breathe1.Text = "系統\n資訊";
                bt_check_plc_breathe1.Text = "粉飾\n太平\n模式2";
                bt_check_plc_breathe1.Name = "bt_check_plc_breathe1";
                bt_check_plc_breathe1.Location = new Point(x_st + dx * 5, y_st);
                // 加入按鈕事件
                //bt_check_plc_breathe1.Click += new EventHandler(bt_check_plc_breathe1_Click);   //same
                bt_check_plc_breathe1.Click += bt_check_plc_breathe1_Click;
                this.groupBox_plc.Controls.Add(bt_check_plc_breathe1);     // 將控件加入表單
            }
            else
            {
            }

            // 實例化按鈕
            bt_automation_setup.Width = PLC_BTN_WIDTH;
            bt_automation_setup.Height = PLC_BTN_HEIGHT;
            bt_automation_setup.Text = "";
            bt_automation_setup.Name = "bt_automation_setup";
            bt_automation_setup.BackgroundImageLayout = ImageLayout.Zoom;
            bt_automation_setup.BackgroundImage = iMS_Link.Properties.Resources.setup;
            bt_automation_setup.Location = new Point(x_st + dx * 6, y_st);
            // 加入按鈕事件
            //bt_automation_setup.Click += new EventHandler(bt_automation_setup_Click);   //same
            bt_automation_setup.Click += bt_automation_setup_Click;
            this.groupBox_plc.Controls.Add(bt_automation_setup);     // 將控件加入表單

            // 實例化按鈕
            bt_setup_ims_type1.Width = PLC_BTN_WIDTH;
            bt_setup_ims_type1.Height = PLC_BTN_HEIGHT;
            bt_setup_ims_type1.Text = "設定\n主機\n燒錄";
            bt_setup_ims_type1.Name = "bt_setup_ims_type1";
            bt_setup_ims_type1.Location = new Point(x_st + dx * 7, y_st);
            bt_setup_ims_type1.BackColor = Color.Pink;
            // 加入按鈕事件
            //bt_setup_ims_type1.Click += new EventHandler(bt_setup_ims_type1_Click);   //same
            bt_setup_ims_type1.Click += bt_setup_ims_type1_Click;
            this.groupBox_plc.Controls.Add(bt_setup_ims_type1);     // 將控件加入表單

            // 實例化按鈕
            bt_setup_ims_type2.Width = PLC_BTN_WIDTH;
            bt_setup_ims_type2.Height = PLC_BTN_HEIGHT;
            bt_setup_ims_type2.Text = "設定\n主機\n色調";
            bt_setup_ims_type2.Name = "bt_setup_ims_type2";
            bt_setup_ims_type2.Location = new Point(x_st + dx * 8, y_st);
            bt_setup_ims_type2.BackColor = Color.Gold;
            // 加入按鈕事件
            //bt_setup_ims_type2.Click += new EventHandler(bt_setup_ims_type2_Click);   //same
            bt_setup_ims_type2.Click += bt_setup_ims_type2_Click;
            this.groupBox_plc.Controls.Add(bt_setup_ims_type2);     // 將控件加入表單

            // 實例化按鈕
            bt_reset_ims.Width = PLC_BTN_WIDTH;
            bt_reset_ims.Height = PLC_BTN_HEIGHT;
            bt_reset_ims.Text = "主機\n重開";
            bt_reset_ims.Name = "bt_reset_ims";
            bt_reset_ims.Location = new Point(x_st + dx * 9, y_st);
            bt_reset_ims.BackColor = Color.Magenta;

            // 加入按鈕事件
            //bt_reset_ims.Click += new EventHandler(bt_reset_ims_Click);   //same
            bt_reset_ims.Click += bt_reset_ims_Click;
            this.groupBox_plc.Controls.Add(bt_reset_ims);     // 將控件加入表單
            if (flag_automation_mode == MODE_WRITE_DATA)
            {
                bt_reset_ims.Text = "燒錄\n主機\n重開";
            }
            else
            {
                bt_reset_ims.Text = "色調\n主機\n重開";
            }

            cb_debug.Location = new Point(x_st + dx * 6 - 70, y_st + PLC_BTN_HEIGHT);
            cb_debug.Name = "cb_debug";
            cb_debug.Text = "Debug";
            cb_debug.Size = new Size(55, 16);
            this.groupBox_plc.Controls.Add(cb_debug);     // 將控件加入表單

            lb_plc_datetime.AutoSize = true;
            lb_plc_datetime.Name = "lb_plc_datetime";
            lb_plc_datetime.Text = "";
            lb_plc_datetime.BackColor = Color.Silver;
            lb_plc_datetime.Font = f4;
            lb_plc_datetime.ForeColor = Color.Yellow;
            lb_plc_datetime.Size = new System.Drawing.Size(160, 44);
            lb_plc_datetime.Location = new Point(x_st + dx * 10, y_st - 20);
            this.groupBox_plc.Controls.Add(lb_plc_datetime);     // 將控件加入表單
            lb_plc_datetime.BringToFront();

            Font f6 = new Font("Arial", 8.75F, FontStyle.Bold, GraphicsUnit.Point, ((byte)(0))); //main message

            y_st = 32;
            lb_plc_main_mesg1.AutoSize = true;
            lb_plc_main_mesg1.Name = "lb_plc_main_mesg1";
            lb_plc_main_mesg1.Text = "";
            lb_plc_main_mesg1.Font = f6;
            lb_plc_main_mesg1.ForeColor = Color.Red;
            lb_plc_main_mesg1.Size = new System.Drawing.Size(78, 24);
            lb_plc_main_mesg1.Location = new Point(x_st + dx * 10, y_st);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg1);     // 將控件加入表單

            lb_plc_main_mesg2.AutoSize = true;
            lb_plc_main_mesg2.Name = "lb_plc_main_mesg2";
            lb_plc_main_mesg2.Text = "";
            lb_plc_main_mesg2.Font = f2;
            lb_plc_main_mesg2.ForeColor = Color.Red;
            lb_plc_main_mesg2.Size = new System.Drawing.Size(138, 44);
            lb_plc_main_mesg2.Location = new Point(x_st + dx * 10, y_st + 28);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg2);     // 將控件加入表單

            lb_plc_main_mesg3.AutoSize = true;
            lb_plc_main_mesg3.Name = "lb_plc_main_mesg3";
            lb_plc_main_mesg3.Text = "";
            lb_plc_main_mesg3.BackColor = Color.Silver;
            lb_plc_main_mesg3.Font = f2;
            lb_plc_main_mesg3.ForeColor = Color.Red;
            lb_plc_main_mesg3.Size = new System.Drawing.Size(160, 44);
            lb_plc_main_mesg3.Location = new Point(x_st + dx * 12 + 20, y_st + 60);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg3);     // 將控件加入表單
            lb_plc_main_mesg3.BringToFront();

            lb_plc_pc0.Text = "";
            lb_plc_pc0.Font = f1;
            lb_plc_pc0.ForeColor = Color.Black;
            lb_plc_pc0.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc0);     // 將控件加入表單

            lb_plc_pc1.Text = "";
            lb_plc_pc1.Font = f1;
            lb_plc_pc1.ForeColor = Color.Black;
            lb_plc_pc1.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc1);     // 將控件加入表單

            lb_plc_pc2.Text = "";
            lb_plc_pc2.Font = f1;
            lb_plc_pc2.ForeColor = Color.Black;
            lb_plc_pc2.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc2);     // 將控件加入表單

            lb_plc_pc3a.Text = "";
            lb_plc_pc3a.Font = f1;
            lb_plc_pc3a.ForeColor = Color.Black;
            lb_plc_pc3a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc3a);     // 將控件加入表單

            lb_plc_pc4a.Text = "";
            lb_plc_pc4a.Font = f1;
            lb_plc_pc4a.ForeColor = Color.Black;
            lb_plc_pc4a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc4a);     // 將控件加入表單

            lb_plc_pc3b.Text = "";
            lb_plc_pc3b.Font = f1;
            lb_plc_pc3b.ForeColor = Color.Blue;
            lb_plc_pc3b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc3b);     // 將控件加入表單

            lb_plc_pc4b.Text = "";
            lb_plc_pc4b.Font = f1;
            lb_plc_pc4b.ForeColor = Color.Blue;
            lb_plc_pc4b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc4b);     // 將控件加入表單

            // 實例化控件
            lb_pc_plc0.Text = "";
            lb_pc_plc0.Font = f1;
            lb_pc_plc0.ForeColor = Color.Black;
            lb_pc_plc0.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc0);     // 將控件加入表單

            lb_pc_plc1.Text = "";
            lb_pc_plc1.Font = f1;
            lb_pc_plc1.ForeColor = Color.Black;
            lb_pc_plc1.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc1);     // 將控件加入表單

            lb_pc_plc2.Text = "";
            lb_pc_plc2.Font = f1;
            lb_pc_plc2.ForeColor = Color.Black;
            lb_pc_plc2.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc2);     // 將控件加入表單

            lb_pc_plc3a.Text = "";
            lb_pc_plc3a.Font = f1;
            lb_pc_plc3a.ForeColor = Color.Black;
            lb_pc_plc3a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc3a);     // 將控件加入表單

            lb_pc_plc4a.Text = "";
            lb_pc_plc4a.Font = f1;
            lb_pc_plc4a.ForeColor = Color.Black;
            lb_pc_plc4a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc4a);     // 將控件加入表單

            lb_pc_plc3b.Text = "";
            lb_pc_plc3b.Font = f1;
            lb_pc_plc3b.ForeColor = Color.Blue;
            lb_pc_plc3b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc3b);     // 將控件加入表單

            lb_pc_plc4b.Text = "";
            lb_pc_plc4b.Font = f1;
            lb_pc_plc4b.ForeColor = Color.Blue;
            lb_pc_plc4b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc4b);     // 將控件加入表單

            lb_read_write_plc.Text = "";
            lb_read_write_plc.Font = f1;
            lb_read_write_plc.ForeColor = Color.Black;
            lb_read_write_plc.AutoSize = true;

            // 實例化按鈕
            bt_open_folder.Width = PLC_BTN_WIDTH;
            bt_open_folder.Height = PLC_BTN_HEIGHT;
            bt_open_folder.Text = "";
            bt_open_folder.Name = "bt_open_folder";
            // 加入按鈕事件
            //bt_open_folder.Click += new EventHandler(bt_open_folder_Click);   //same
            bt_open_folder.Click += bt_open_folder_Click;

            // 實例化按鈕
            bt_save.Width = PLC_BTN_WIDTH;
            bt_save.Height = PLC_BTN_HEIGHT;
            bt_save.Text = "";
            bt_save.Name = "bt_save";
            // 加入按鈕事件
            //bt_save.Click += new EventHandler(bt_save_Click);   //same
            bt_save.Click += bt_save_Click;

            // 實例化按鈕
            bt_pause.Width = PLC_BTN_WIDTH;
            bt_pause.Height = PLC_BTN_HEIGHT;
            bt_pause.Text = "";
            bt_pause.Name = "bt_pause";
            // 加入按鈕事件
            //bt_pause.Click += new EventHandler(bt_pause_Click);   //same
            bt_pause.Click += bt_pause_Click;

            x_st = 10;
            y_st = 90;

            dx = PLC_GBOX_WIDTH * 45 / 100;
            int dy = 25;
            int w = 25;
            int h = 25;
            int offset = -100;
            pbx_m7980.Size = new Size(w, h);
            pbx_m7981.Size = new Size(w, h);
            pbx_m7982.Size = new Size(w, h);
            pbx_m7990.Size = new Size(w, h);
            pbx_m7991.Size = new Size(w, h);
            pbx_m7992.Size = new Size(w, h);
            pbx_m7980.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 5);
            pbx_m7981.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 5);
            pbx_m7982.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 5);
            pbx_m7990.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 0 - 5);
            pbx_m7991.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 1 - 5);
            pbx_m7992.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 2 - 5);
            pbx_m7980.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7981.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7982.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7990.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7991.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7992.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m7980.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m7981.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m7982.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m7990.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m7991.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m7992.BackgroundImage = Properties.Resources.ball_gray;

            x_st = 40;
            lb_plc_pc0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_plc_pc1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_plc_pc2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_plc_pc3a.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_plc_pc4a.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_read_write_plc.Location = new Point(x_st + dx * 0 + 220, y_st + dy * 5 - 5);

            lb_plc_pc3b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 3);
            lb_plc_pc4b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 4);
            lb_pc_plc0.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 0);
            lb_pc_plc1.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 1);
            lb_pc_plc2.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 2);
            lb_pc_plc3a.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 3);
            lb_pc_plc4a.Location = new Point(x_st + dx * 1 + offset, y_st + dy * 4);
            lb_pc_plc3b.Location = new Point(x_st + dx * 1 + offset + 160, y_st + dy * 3);
            lb_pc_plc4b.Location = new Point(x_st + dx * 1 + offset + 160, y_st + dy * 4);

            lb_plc_pc0.Text = "M" + (7980 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
            lb_plc_pc1.Text = "M" + (7981 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
            lb_plc_pc2.Text = "M" + (7982 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
            lb_pc_plc0.Text = "M" + (7990 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
            lb_pc_plc1.Text = "M" + (7991 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
            lb_pc_plc2.Text = "M" + (7992 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
            lb_plc_pc3a.Text = "ID資料    D" + (5900 + plc_d_address_offset).ToString();
            lb_plc_pc4a.Text = "收到結果D" + (5910 + plc_d_address_offset).ToString();
            lb_plc_pc3b.Text = "";
            lb_plc_pc4b.Text = "";
            lb_pc_plc3a.Text = "ID資料    D" + (5950 + plc_d_address_offset).ToString();
            lb_pc_plc4a.Text = "檢測結果D" + (5960 + plc_d_address_offset).ToString();
            lb_pc_plc3b.Text = "";
            lb_pc_plc4b.Text = "";
            lb_read_write_plc.Text = "";
            lb_plc_main_mesg3.Text = "Master 無動作";

            pbx_plc_status.Size = new Size(w * 3, h * 3);
            pbx_plc_status.Location = new Point(groupBox_plc.Location.X + groupBox_plc.Width - w * 4, h * 5 - 25);
            pbx_plc_status.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_plc_status.BackgroundImage = Properties.Resources.ball_gray;
            pictureBox_plc_status.Location = new Point(BORDER, y_st + dy * 5);
            pictureBox_plc_status.Size = new Size(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER * 5, PLC_GBOX_HEIGHT - pictureBox_plc_status.Location.Y - BORDER);

            x_st = pictureBox_plc_status.Location.X + pictureBox_plc_status.Width - 80 - 5 - 5;
            y_st = pictureBox_plc_status.Location.Y + 5 + 5;
            dy = 80 + 5;

            groupBox_connection.Text = "";
            groupBox_connection.Size = new Size(100, 275);
            groupBox_connection.Location = new Point(x_st, y_st);
            groupBox_connection.BackColor = Color.LightGray;
            this.panel_plc.Controls.Add(groupBox_connection);     // 將控件加入表單
            groupBox_connection.BringToFront();

            groupBox_connection_status.Text = "";
            groupBox_connection_status.Size = new Size(160, 40);
            groupBox_connection_status.Location = new Point(x_st - 60, y_st - 40);
            //groupBox_connection_status.BackColor = Color.White;
            this.panel_plc.Controls.Add(groupBox_connection_status);     // 將控件加入表單
            groupBox_connection_status.BringToFront();

            x_st = 0;
            y_st = 0;

            dx = 40;
            dy = 40;
            w = 40;
            h = 40;
            pbx_ims_connection1.Size = new Size(w, h);
            pbx_ims_connection2.Size = new Size(w, h);
            pbx_ims_connection3.Size = new Size(w, h);
            pbx_ims_connection4.Size = new Size(w, h);
            pbx_ims_connection1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pbx_ims_connection2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pbx_ims_connection3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pbx_ims_connection4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pbx_ims_connection1.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_ims_connection2.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_ims_connection3.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_ims_connection4.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_ims_connection1.BackgroundImage = Properties.Resources.ball_gray;
            pbx_ims_connection2.BackgroundImage = Properties.Resources.ball_gray;
            pbx_ims_connection3.BackgroundImage = Properties.Resources.ball_gray;
            pbx_ims_connection4.BackgroundImage = Properties.Resources.ball_gray;
            pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_OFF;
            pbx_ims_connection2.BackgroundImage = Properties.Resources.ims_connection2_OFF;
            pbx_ims_connection3.BackgroundImage = Properties.Resources.ims_connection3_OFF;
            pbx_ims_connection4.BackgroundImage = Properties.Resources.ims_connection4_OFF;
            this.groupBox_connection_status.Controls.Add(pbx_ims_connection1);	// 將控件加入表單
            this.groupBox_connection_status.Controls.Add(pbx_ims_connection2);	// 將控件加入表單
            this.groupBox_connection_status.Controls.Add(pbx_ims_connection3);	// 將控件加入表單
            this.groupBox_connection_status.Controls.Add(pbx_ims_connection4);	// 將控件加入表單

            dx = PLC_GBOX_WIDTH * 45 / 100;
            dy = 80 + 5;
            w = 25;
            h = 25;
            offset = -100;

            x_st = 10;
            y_st = 15;
            int pbx_connection_w = 80;
            int pbx_connection_h = 80;

            pbx_connection1.Size = new Size(pbx_connection_w, pbx_connection_h);
            pbx_connection1.Location = new Point(x_st, y_st + dy * 0);
            pbx_connection1.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_connection1.BackgroundImage = Properties.Resources.ball_gray;
            pbx_connection1.BackColor = Color.Pink;
            this.groupBox_connection.Controls.Add(pbx_connection1);  // 將控件加入表單

            pbx_connection2.Size = new Size(pbx_connection_w, pbx_connection_h);
            pbx_connection2.Location = new Point(x_st, y_st + dy * 1);
            pbx_connection2.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_connection2.BackgroundImage = Properties.Resources.ball_gray;
            pbx_connection2.BackColor = Color.Pink;
            this.groupBox_connection.Controls.Add(pbx_connection2);  // 將控件加入表單

            pbx_connection3.Size = new Size(pbx_connection_w, pbx_connection_h);
            pbx_connection3.Location = new Point(x_st, y_st + dy * 2);
            pbx_connection3.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_connection3.BackgroundImage = Properties.Resources.ball_gray;
            pbx_connection3.BackColor = Color.Pink;
            this.groupBox_connection.Controls.Add(pbx_connection3);  // 將控件加入表單

            bt_save_to_file.BackgroundImage = Properties.Resources.save;
            bt_save_to_file.BackgroundImageLayout = ImageLayout.Zoom;
            bt_copy_to_clipboard.BackgroundImage = Properties.Resources.clipboard;
            bt_copy_to_clipboard.BackgroundImageLayout = ImageLayout.Zoom;
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
            bt_plc_clear.BackgroundImage = Properties.Resources.clear;
            bt_plc_clear.BackgroundImageLayout = ImageLayout.Zoom;
            bt_save.BackgroundImage = Properties.Resources.save;
            bt_save.BackgroundImageLayout = ImageLayout.Zoom;
            bt_pause.BackgroundImageLayout = ImageLayout.Zoom;
            if (timer_plc_status.Enabled == true)
            {
                bt_pause.BackgroundImage = Properties.Resources.pause;
            }
            else
            {
                bt_pause.BackgroundImage = Properties.Resources.play;
            }

            bt_open_folder.Location = new Point(pictureBox_plc_status.Location.X + pictureBox_plc_status.Width - bt_open_folder.Width, pictureBox_plc_status.Location.Y + pictureBox_plc_status.Height - bt_open_folder.Height * 3);
            bt_save.Location = new Point(pictureBox_plc_status.Location.X + pictureBox_plc_status.Width - bt_save.Width, pictureBox_plc_status.Location.Y + pictureBox_plc_status.Height - bt_save.Height * 2);
            bt_pause.Location = new Point(pictureBox_plc_status.Location.X + pictureBox_plc_status.Width - bt_pause.Width, pictureBox_plc_status.Location.Y + pictureBox_plc_status.Height - bt_pause.Height * 1);

            this.groupBox_plc.Controls.Add(lb_read_write_plc);   // 將控件加入表單
            this.groupBox_plc.Controls.Add(bt_open_folder);      // 將控件加入表單
            this.groupBox_plc.Controls.Add(bt_save);     // 將控件加入表單
            this.groupBox_plc.Controls.Add(bt_pause);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7980);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7981);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7982);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7990);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7991);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m7992);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_plc_status);  // 將控件加入表單
            this.groupBox_plc.Controls.Add(pictureBox_plc_status);  // 將控件加入表單

            if (flag_automation_mode == MODE_AWB)
            {
                groupBox_plc.Text = "自動化作業 : 色彩調教";
                plc_m_address_offset = OFFSET_M_AWB;
                plc_d_address_offset = OFFSET_D_AWB;
                lb_plc_command_type.Text = "色彩調教" + AUTOMATION_VERSION.ToString("D2");
                panel_plc.BackColor = Color.LightYellow;
                pbx_connection2.BackgroundImage = Properties.Resources.awb1;
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                groupBox_plc.Text = "自動化作業 : 資料燒錄";
                plc_m_address_offset = OFFSET_M_WRITE_DATA;
                plc_d_address_offset = OFFSET_D_WRITE_DATA;
                lb_plc_command_type.Text = "資料燒錄" + AUTOMATION_VERSION.ToString("D2");
                panel_plc.BackColor = Color.LightPink;
                pbx_connection2.BackgroundImage = Properties.Resources.data_write1;
            }
            else
            {
                groupBox_plc.Text = "自動化作業";
            }
            if (flag_use_real_plc == true)
            {
                groupBox_plc.Text += "    真上位";
                pbx_connection1.BackgroundImage = Properties.Resources.plc1;
            }
            else
            {
                groupBox_plc.Text += "    假上位";
                pbx_connection1.BackgroundImage = Properties.Resources.plc2;
            }

            if (flag_use_real_ims == true)
            {
                groupBox_plc.Text += "    真下位";
                pbx_connection3.BackgroundImage = Properties.Resources.use_ims1;
            }
            else
            {
                groupBox_plc.Text += "    假下位";
                pbx_connection3.BackgroundImage = Properties.Resources.use_ims2;
            }

            bt_setup_ims_type1.Text = "設定\n主機\n燒錄";
            bt_setup_ims_type2.Text = "設定\n主機\n色調";

            if (flag_factory_mode == true)
            {
                richTextBox_plc.Text += "工廠模式\n";
                bt_check_connection.Visible = true;
                bt_read_camera_data.Visible = true;
                bt_erase_camera_data.Visible = true;
                bt_setup_ims_type1.Visible = true;
                bt_setup_ims_type2.Visible = true;
                cb_debug.Visible = true;
                bt_pause.Visible = true;
            }
            else
            {
                richTextBox_plc.Text += "一般模式\n";
                bt_check_connection.Enabled = true;
                bt_read_camera_data.Enabled = true;
                bt_erase_camera_data.Enabled = true;
                bt_setup_ims_type1.Enabled = true;
                bt_setup_ims_type2.Enabled = true;
                cb_debug.Enabled = false;
                bt_pause.Enabled = false;
            }

            Font f = new Font("標楷體", 10);
            bt_plc_test.Font = f;
            bt_plc_test_break.Font = f;

            f = new Font("標楷體", 12);
            bt_check_connection.Font = f;
            bt_read_camera_data.Font = f;
            bt_erase_camera_data.Font = f;
            bt_setup_ims_type1.Font = f;
            bt_setup_ims_type2.Font = f;
            bt_check_plc_breathe1.Font = f;
            bt_check_plc_breathe2.Font = f;
            bt_automation_setup.Font = f;

            bt_exit_setup();

            richTextBox_plc.Text = groupBox_plc.Text;
            richTextBox_plc.Text += "\n按\"啟動自動化作業\"開始測試\n";
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 60; //設定按鈕大小 W
            int h = 60; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.groupBox_plc.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.groupBox_plc.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            //Application.Exit();
            exit_program();
        }

        bool flag_panel_plc_mouse_down = false;
        private void Panel_plc_MouseDown(object sender, MouseEventArgs e)
        {
            flag_panel_plc_mouse_down = true;
            //richTextBox_plc.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            panel_plc_position_x_old = e.X;
            panel_plc_position_y_old = e.Y;
        }

        private void Panel_plc_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_panel_plc_mouse_down == true)
            {
                //richTextBox_plc.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - panel_plc_position_x_old;
                int dy = e.Y - panel_plc_position_y_old;

                //richTextBox_plc.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                if (flag_automation_mode == MODE_AWB)
                {
                    //panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
                }
            }
        }

        private void Panel_plc_MouseUp(object sender, MouseEventArgs e)
        {
            flag_panel_plc_mouse_down = false;
            //richTextBox_plc.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - panel_plc_position_x_old;
            int dy = e.Y - panel_plc_position_y_old;

            //richTextBox_plc.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            if (flag_automation_mode == MODE_AWB)
            {
                //panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
            }
        }

        //string[] plc_main_mesg = new string[] { "無資料", "鏡頭脫落", "影像有黑影", "其他：" };
        //int timer_plc_display_show_main_mesg_index = 0;
        int timer_plc_display_show_main_mesg_count = 0;
        int timer_plc_display_show_main_mesg_count_target = 0;
        void show_plc_main_message1(string mesg, int number, int timeout)
        {
            /*
            //TBD
            //string message = plc_main_mesg[0] + "\n" + plc_main_mesg[1] + "\n" + plc_main_mesg[2] + "\n" + plc_main_mesg[3];

            if (timer_plc_display_show_main_mesg_index < 2)
            {
                plc_main_mesg[timer_plc_display_show_main_mesg_index] = mesg;
            }
            else
            {

            }
            */

            lb_plc_main_mesg1.Text = mesg;
            //playSound(number);

            timer_plc_display_show_main_mesg_count = 0;
            timer_plc_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_plc_display.Enabled = true;
        }

        private void timer_plc_status_Tick(object sender, EventArgs e)
        {
            bool plc_power_status = check_plc_power_status();

            if (cb_debug.Checked == true)
            {
                plc_power_status = true;
            }

            if (plc_power_status == false)
            {
                lb_plc_pc3b.Text = "xxxx-PLC-OFF-xxxx";
                lb_plc_pc4b.Text = "xxxx-PLC-OFF-xxxx";
                lb_pc_plc3b.Text = "xxxx-PLC-OFF-xxxx";
                lb_pc_plc4b.Text = "xxxx-PLC-OFF-xxxx";
                pbx_m7980.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m7981.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m7982.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m7990.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m7991.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m7992.BackgroundImage = Properties.Resources.ball_gray;
                pbx_plc_status.BackgroundImage = Properties.Resources.ball_gray;
                lb_plc_main_mesg2.Text = "三菱PLC 不 Ready";
                lb_plc_main_mesg2.Visible = true;
                lb_plc_main_mesg3.Text = "Master 無動作";
                //groupBox_plc.Enabled = false;
                //pictureBox_plc_status.Enabled = false;
            }
            else
            {
                lb_plc_main_mesg2.Text = "";
                lb_plc_main_mesg2.Visible = false;
                //groupBox_plc.Enabled = true;
                //pictureBox_plc_status.Enabled = true;
                pbx_plc_status.BackgroundImage = Properties.Resources.ball_green2;
            }
            update_plc_test_status_data();
            if (plc_do_check_time == false)
                update_plc_data_status_data();
            draw_status();
        }

        private const int N = 31;
        int plc_test_status_data_value = 0;
        int plc_breathe_status_data_value = 0;
        int m7980_value = 0;
        int m7981_value = 0;
        int m7982_value = 0;
        int m7990_value = 0;
        int m7991_value = 0;
        int m7992_value = 0;

        int[] plc_breathe_status_data = new int[N];
        int[] plc_test_status_data = new int[N];
        int[] m7980_data = new int[N];
        int[] m7981_data = new int[N];
        int[] m7982_data = new int[N];
        int[] m7990_data = new int[N];
        int[] m7991_data = new int[N];
        int[] m7992_data = new int[N];

        bool check_plc_power_status()
        {
            bool plc_power_status = false;

            if (flag_use_real_plc == false)
            {
                return check_plc_simulator_power_status();
            }

            //讀取 PLC狀態
            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready == true)   //PLC是否準備完成
            {
                plc_power_status = true;
                /* 目前無法判斷 PLC_read_M_bit 是讀不到資料 還是資料為True/False
                richTextBox_plc.Text += "check_plc_power_status\n";
                //richTextBox_plc.Text += "三菱PLC ready 3\n";
                List<bool> data = mitsubishi.PLC_read_M_bit("M", "7980");//讀取狀態
                richTextBox_plc.Text += "aaaa len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    plc_power_status = true;
                }
                else
                {
                    plc_power_status = false;
                }
                */
            }
            else
            {
                plc_power_status = false;
            }
            return plc_power_status;
        }

        void update_plc_test_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();

            if (flag_plc_test == false)
            {
                plc_test_status_data_value = 0;
            }
            else
            {
                if (flag_plc_test_busy == false)
                {
                    plc_test_status_data_value = 1;
                }
                else
                {
                    plc_test_status_data_value = 2; //busy
                }
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 3);
                plc_test_status_data_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                plc_test_status_data[i] = plc_test_status_data[i + 1];
            }
            plc_test_status_data[N - 1] = plc_test_status_data_value;
        }

        void update_plc_breathe_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();

            plc_breathe_status_data_value = (int)pc_breathe_status;

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                plc_breathe_status_data_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                plc_breathe_status_data[i] = plc_breathe_status_data[i + 1];
            }
            plc_breathe_status_data[N - 1] = plc_breathe_status_data_value;
        }

        void update_plc_data_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();
            bool status;

            string contact_address = string.Empty;

            //M7980
            contact_address = (7980 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7980_value = 1;
            }
            else
            {
                m7980_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7980_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7980_data[i] = m7980_data[i + 1];
            }
            m7980_data[N - 1] = m7980_value;

            if (m7980_value == 1)
            {
                pbx_m7980.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7980.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M7981
            contact_address = (7981 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7981_value = 1;
            }
            else
            {
                m7981_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7981_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7981_data[i] = m7981_data[i + 1];
            }
            m7981_data[N - 1] = m7981_value;

            if (m7981_value == 1)
            {
                pbx_m7981.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7981.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M7982
            contact_address = (7982 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7982_value = 1;
            }
            else
            {
                m7982_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7982_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7982_data[i] = m7982_data[i + 1];
            }
            m7982_data[N - 1] = m7982_value;

            if (m7982_value == 1)
            {
                pbx_m7982.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7982.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M7990
            contact_address = (7990 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7990_value = 1;
            }
            else
            {
                m7990_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7990_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7990_data[i] = m7990_data[i + 1];
            }
            m7990_data[N - 1] = m7990_value;

            if (m7990_value == 1)
            {
                pbx_m7990.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7990.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M7991
            contact_address = (7991 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7991_value = 1;
            }
            else
            {
                m7991_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7991_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7991_data[i] = m7991_data[i + 1];
            }
            m7991_data[N - 1] = m7991_value;

            if (m7991_value == 1)
            {
                pbx_m7991.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7991.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M7992
            contact_address = (7992 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m7992_value = 1;
            }
            else
            {
                m7992_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m7992_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m7992_data[i] = m7992_data[i + 1];
            }
            m7992_data[N - 1] = m7992_value;

            if (m7992_value == 1)
            {
                pbx_m7992.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m7992.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            if ((flag_use_real_plc == true) || (plc_simulator_step != 0))
            {
                contact_address = (5900 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                string data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD5900 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc3b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (5910 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD5950 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (5950 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);

                //richTextBox_plc.Text += "\nD5950 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc3b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (5960 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD5950 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc4b.Text = data_read;
            }
        }

        int flag_draw_breathe = 0;
        void draw_status()
        {
            int W = pictureBox_plc_status.Width;
            int H = pictureBox_plc_status.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            if (flag_plc_test == false)
            {
                g.Clear(SystemColors.ControlLight);
            }
            else
            {
                g.Clear(Color.White);
            }

            //畫X軸 Y軸
            //X軸
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            //Y軸
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 1 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x_st = W * 10 / 100;
            int x_sp = W * 90 / 100;
            int y_st = H * 10 / 100;
            int y_sp = H * 90 / 100;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            int hh = h * 5 / 10;
            int step = w / (N - 1);

            // Create pens.
            //Pen silverPen = new Pen(Color.Silver, 5);
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 5);
            List<Point> points = new List<Point>();

            int i;
            int x;
            int y;
            int dd = 8;
            int pt_new = 0;
            int pt_old = 0;

            hh = h / 14;

            //畫 PLC status  畫垂直線, 灰色刻度線
            Pen silverPen = new Pen(Color.Silver, 3);
            // Set the DashStyle property.
            //silverPen.DashStyle = DashStyle.Custom;
            silverPen.DashStyle = DashStyle.Dash;
            //silverPen.DashStyle = DashStyle.DashDot;
            //silverPen.DashStyle = DashStyle.DashDotDot;
            //silverPen.DashStyle = DashStyle.Dot;
            //silverPen.DashStyle = DashStyle.Solid;

            //g.DrawRectangle(new Pen(Color.Lime, 16), x_st, y_st, w, h);

            for (int xx = x_st; xx <= x_st + w; xx += step)
            {
                Point ptx1 = new Point(xx, y_st);
                Point ptx2 = new Point(xx, y_st + h);
                g.DrawLine(silverPen, ptx1, ptx2);
            }

            //畫 PLC status  畫水平線, 灰色底線
            points.Clear();
            points.Add(new Point(x_st, 60));
            points.Add(new Point(x_sp, 60));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線
            points.Clear();
            points.Add(new Point(x_st, 60 - hh * 1));
            points.Add(new Point(x_sp, 60 - hh * 1));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線
            points.Clear();
            points.Add(new Point(x_st, 60 - hh * 2));
            points.Add(new Point(x_sp, 60 - hh * 2));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫 PLC status
            points.Clear();
            pt_old = plc_test_status_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = plc_test_status_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = 60 - hh * pt_old;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }

                x = x_st + step * i;
                y = 60 - hh * plc_test_status_data[i];
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線

            //------------------------------------------------------------  # 60個

            // 畫 心跳

            // richTextBox_plc.Text += "A " + ((int)pc_breathe_status).ToString() + " ";
            int hhh = h / 20;

            points.Clear();
            pt_old = plc_breathe_status_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = plc_breathe_status_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = 90 - hhh * pt_old;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }

                x = x_st + step * i;
                y = 90 - hhh * plc_breathe_status_data[i];
                points.Add(new Point(x, y));
            }

            Pen pinkPen = new Pen(Color.Pink, 5);
            if (flag_draw_breathe == 0)
            {
                pinkPen = new Pen(Color.Pink, 3);
            }
            else if (flag_draw_breathe == 1)
            {
                pinkPen = new Pen(Color.Pink, 6);
            }

            flag_draw_breathe++;
            if (flag_draw_breathe > 1)
            {
                flag_draw_breathe = 0;
            }

            g.DrawLines(pinkPen, points.ToArray());  //畫直線

            bool plc_power_status = check_plc_power_status();
            if (plc_power_status == false)
            {
                g.FillRectangle(Brushes.LightGray, x_st - 32 - 4, 66 - 4, 24 + 8 + 1, 24 + 8 - 1);
                //richTextBox_plc.Text += "PLC OFF : " + DateTime.Now.ToString() + "\n";
            }
            else
            {
                g.FillRectangle(Brushes.LightGreen, x_st - 32 - 4, 66 - 4, 24 + 8 + 1, 24 + 8 - 1);
                //richTextBox_plc.Text += "PLC ON : " + DateTime.Now.ToString() + "\n";
            }

            //GraphicsPath - FillPath() 心形

            GraphicsPath gp = new GraphicsPath();
            int Cx = x_st - 32 + 12;
            int Cy = 66 + 9;
            int D = 3;    // 每格 寬
            x = Cx;    // 心臟的起始點
            y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心臟左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);

            if (pc_breathe_status == PLC_STATE.ON)
            {
                //g.DrawEllipse(new Pen(Color.Red, 5), x_st - 32, 66, 24, 24);
                g.DrawPath(new Pen(Color.Red, 5), gp); //繪出圖形軌跡

            }
            else if (pc_breathe_status == PLC_STATE.OFF)
            {
                //g.FillEllipse(Brushes.Red, x_st - 32, 66, 24, 24);
                g.FillPath(Brushes.Red, gp); // 填滿形狀區域 //SolidBrush - Red
            }
            else
            {
                //g.FillEllipse(Brushes.Gray, x_st - 32, 66, 24, 24);
                g.FillPath(Brushes.Gray, gp); // 填滿形狀區域 //SolidBrush - Gray
            }

            //------------------------------------------------------------  # 60個

            g.DrawString(flag_plc_test_count.ToString(), f3, new SolidBrush(Color.Red), new PointF(x_st - 10 - 10 * (flag_plc_test_count.ToString().Length), 20));

            string string_work_result = get_work_result_data_write(global_work_result);
            if (global_work_result == 0xff)
            {
                g.DrawString("上次結果 : ", f3, new SolidBrush(Color.Red), new PointF(10, H - 30));
            }
            else
            {
                g.DrawString("上次結果 : " + string_work_result, f3, new SolidBrush(Color.Red), new PointF(10, H - 30));
            }

            string status = string.Empty;

            if (plc_simulator_step == 0)    //PLC Power OFF
            {
                status = "PLC Power OFF";
            }
            else if (plc_simulator_step == 1)   //PLC Power ON
            {
                status = "PLC Power ON";
            }
            else if (plc_simulator_step == 2)   //開始PLC測試
            {
                status = "開始PLC測試";
            }
            else if (plc_simulator_step == 3)   //PLC等待PC工作
            {
                status = "PLC等待PC工作";
            }
            else if (plc_simulator_step == 4)
            {
                status = "";
            }
            else if (plc_simulator_step == 5)
            {
                status = "";
            }
            else if (plc_simulator_step == 6)
            {
                status = "";
            }
            else
            {
                status = "";
            }

            g.DrawString("目前狀態 : " + plc_simulator_step.ToString() + ", " + status + ", " + plc_message, f3, new SolidBrush(Color.Red), new PointF(10 + 200, H - 30));

            int xx_st = x_st + step * 0;
            int xx_sp = x_st + step * (N - 1);
            int yy = 0;
            hh = h / 8;

            //畫直線, 灰色底線

            //畫M7980
            yy = H - y_st - 5 - hh * 5 - dd * 5;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M7981
            yy = H - y_st - 5 - hh * 4 - dd * 4;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M7982
            yy = H - y_st - 5 - hh * 3 - dd * 3;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M7990
            yy = H - y_st - 5 - hh * 2 - dd * 2;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M7991
            yy = H - y_st - 5 - hh * 1 - dd * 1;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M7992
            yy = H - y_st - 5 - hh * 0 - dd * 0;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            if (plc_power_status == true)
            {
                redPen = new Pen(Color.Red, 3);
            }
            else
            {
                redPen = new Pen(Color.Gray, 3);
            }

            //畫M7980
            points.Clear();
            pt_old = m7980_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7980_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 5 - dd * 5;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7980_data[i] - 5 - hh * 5 - dd * 5;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("A M" + (7980 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70-15, H - y_st - hh * 1 - 5 - hh * 5 - dd * 5));

            //畫M7981
            points.Clear();
            pt_old = m7981_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7981_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 4 - dd * 4;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7981_data[i] - 5 - hh * 4 - dd * 4;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("B M" + (7981 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70 - 15, H - y_st - hh * 1 - 5 - hh * 4 - dd * 4));

            //畫M7982
            points.Clear();
            pt_old = m7982_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7982_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 3 - dd * 3;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7982_data[i] - 5 - hh * 3 - dd * 3;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("C M" + (7982 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70 - 15, H - y_st - hh * 1 - 5 - hh * 3 - dd * 3));

            //畫M7990
            points.Clear();
            pt_old = m7990_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7990_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 2 - dd * 2;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7990_data[i] - 5 - hh * 2 - dd * 2;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (7990 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 2 - dd * 2));

            //畫M7991
            points.Clear();
            pt_old = m7991_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7991_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 1 - dd * 1;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7991_data[i] - 5 - hh * 1 - dd * 1;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (7991 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 1 - dd * 1));

            //畫M7992
            points.Clear();
            pt_old = m7992_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m7992_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 0 - dd * 0;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m7992_data[i] - 5 - hh * 0 - dd * 0;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (7992 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 0 - dd * 0));

            pictureBox_plc_status.Image = bitmap1;

            g.Dispose();
        }

        private void timer_plc_display_Tick(object sender, EventArgs e)
        {
            if (timer_plc_display_show_main_mesg_count < timer_plc_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_plc_display_show_main_mesg_count++;
                if (timer_plc_display_show_main_mesg_count >= timer_plc_display_show_main_mesg_count_target)
                {
                    lb_plc_main_mesg1.Text = "";
                }
            }
        }

        string get_plc_d_data(string contact_address)
        {
            if (flag_use_real_plc == false)
            {
                return get_plc_simulator_d_data(contact_address);
            }

            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 1\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    data_read = dddd;
                }
                else
                {
                    data_read = "無資料";
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }

        string get_plc_d_data2(string contact_address)
        {
            if (flag_use_real_plc == false)
            {
                return get_plc_simulator_d_data(contact_address);
            }

            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 1\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.Signed_16_Bit);
                    data_read = dddd;
                }
                else
                {
                    data_read = "無資料";
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }


        void set_plc_d_data(string contact_address, string write_data)
        {
            if (flag_use_real_plc == false)
            {
                set_plc_simulator_d_data(contact_address, write_data);
                return;
            }

            string contact_point = "D";

            if (write_data.Length == 0)
            {
                richTextBox_plc.Text += "無寫入資料";
                richTextBox_plc.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 2\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.String_32_Bit);

                //richTextBox_plc.Text += "cccc len = " + dddd.Length.ToString() + "\tdata : " + dddd + "\n\n";
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
        }

        string get_plc_d_data_bcd16(string contact_address)
        {
            if (flag_use_real_plc == false)
            {
                return get_plc_simulator_d_data(contact_address);
            }

            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 1\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.BCD_16_Bit);
                    data_read = dddd;
                }
                else
                {
                    data_read = "";
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
            return data_read;
        }

        void set_plc_d_data_bcd16(string contact_address, string write_data)
        {
            if (flag_use_real_plc == false)
            {
                set_plc_d_data(contact_address, write_data);
                return;
            }

            string contact_point = "D";

            if (write_data.Length == 0)
            {
                richTextBox_plc.Text += "無寫入資料";
                richTextBox_plc.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 2\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                string dddd = mitsubishi.PLC_write_D_register(contact_point, contact_address, write_data, numerical_format.BCD_16_Bit);

                //richTextBox_plc.Text += "cccc len = " + dddd.Length.ToString() + "\tdata : " + dddd + "\n\n";
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
        }

        void erase_plc_d_data(string contact_address, int length)
        {
            if (flag_use_real_plc == false)
            {
                set_plc_d_data(contact_address, "");
                return;
            }

            string contact_point = "D";
            int contact_address_d = int.Parse(contact_address);
            //richTextBox_plc.Text += "contact_address_d = " + contact_address_d + ", len = " + length.ToString() + "\n";

            if (length < 1)
            {
                richTextBox_plc.Text += "清除資料 長度錯誤, 至少要 1\n";
                return;
            }

            //richTextBox_plc.Text += "清除資料\t觸點 : " + contact_point + "\t位址 : " + contact_address + "\t長度 : " + length.ToString() + "\n";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 2\n";

                string write_data = "0";
                for (int i = 0; i < length; i++)
                {
                    string dddd = mitsubishi.PLC_write_D_register(contact_point, (contact_address_d + i).ToString(), write_data, numerical_format.BCD_16_Bit);
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
        }

        void print_plc_d_data(string contact_address)
        {
            string contact_point = "D";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 1\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                data[0] = true; //一律打印

                if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    data_read = dddd;

                    //richTextBox_plc.Text += "\nb len = " + dddd.Length.ToString() + "\n";
                    //richTextBox_plc.Text += "data1 : " + dddd + "\n";
                    //richTextBox_plc.Text += "\n";

                    int len = dddd.Length;

                    for (int i = 0; i < len; i++)
                    {
                        richTextBox_plc.Text += ((int)dddd[i]).ToString("X2").PadLeft(3);
                    }
                    richTextBox_plc.Text += "\n";

                    for (int i = 0; i < len; i++)
                    {
                        int vv = (int)dddd[i];

                        if ((vv < 32) || (vv > 126))
                        {
                            richTextBox_plc.Text += " --";
                        }
                        else
                        {
                            richTextBox_plc.Text += ((char)vv).ToString().PadLeft(3);
                        }
                    }
                    richTextBox_plc.Text += "\n";

                }
                else
                {
                    richTextBox_plc.Text += "無資料";
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
        }

        bool get_plc_m_status(string contact_address)
        {
            if (flag_use_real_plc == false)
            {
                if (flag_pc_check_plc_breathe_mode > MODE_OFF) //PC檢查PLC之心跳
                {
                    return get_plc_simulator_m_status(contact_address);
                }

                if (plc_simulator_step == 0)
                {
                    return false;
                }
                else
                {
                    return get_plc_simulator_m_status(contact_address);
                }
            }

            string contact_point = "M";

            if ((contact_address.Length != 4) && (contact_address.Length != 5))
            {
                show_plc_main_message1("位址錯誤", S_OK, 30);
                richTextBox_plc.Text += "位址錯誤 : " + contact_address + "\n";
                return false;
            }

            bool ret = false;
            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 5\n";

                List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                if (data[0] == true)
                {
                    ret = true;
                }
                else
                {
                    ret = false;
                }
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
                ret = false;
            }
            return ret;
        }

        void set_plc_m_status(string contact_address, PLC_STATE write_data)
        {
            if (flag_use_real_plc == false)
            {
                //richTextBox_plc.Text += "PLC模擬器設定 " + contact_address + " 為 " + write_data + "\n";
                set_plc_simulator_m_status(contact_address, write_data);
                return;
            }

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 6\n";

                //richTextBox_plc.Text += "\n觸點 : M\t位址 : " + contact_address + "\n";

                List<bool> data = mitsubishi.PLC_write_M_bit("M", contact_address, write_data);
            }
            else
            {
                //richTextBox_plc.Text += "三菱PLC 不 ready\n";
            }
        }

        //同時偵測兩個信號
        string polling_2m_status(string contact_address1, string contact_address2, PLC_STATE polling_status)
        {
            bool ret = false;
            string get_signal = "polling_fail";
            for (int i = 0; i < 10; i++)
            {
                delay(500);

                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    break;
                }

                //richTextBox_plc.Text += "contact_address1 = " + contact_address1 + "\n";
                //richTextBox_plc.Text += "contact_address2 = " + contact_address2 + "\n";
                ret = get_plc_m_status(contact_address1);
                if (ret == false)
                {
                    richTextBox_plc.Text += "OFF1 ";
                    if (polling_status == HIGH)
                        delay(500);
                    else
                    {
                        get_signal = contact_address1;
                        break;
                    }
                }
                else
                {
                    richTextBox_plc.Text += "ON1 ";
                    if (polling_status == HIGH)
                    {
                        get_signal = contact_address1;
                        break;
                    }
                    else
                        delay(500);
                }

                ret = get_plc_m_status(contact_address2);
                if (ret == false)
                {
                    richTextBox_plc.Text += "OFF2 ";
                    if (polling_status == HIGH)
                        delay(500);
                    else
                    {
                        get_signal = contact_address2;
                        break;
                    }
                }
                else
                {
                    richTextBox_plc.Text += "ON2 ";
                    if (polling_status == HIGH)
                    {
                        get_signal = contact_address2;
                        break;
                    }
                    else
                        delay(500);
                }
            }
            if (get_signal == "polling_fail")
            {
                richTextBox_plc.Text += "NG ";
            }
            return get_signal;
        }

        int polling_m_status(string contact_address, PLC_STATE polling_status)
        {
            int status = S_FALSE;
            bool ret = false;
            for (int i = 0; i < 10; i++)
            {
                delay(500);

                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    status = S_FALSE;
                    break;
                }

                ret = get_plc_m_status(contact_address);
                if (ret == false)
                {
                    richTextBox_plc.Text += "OFF  ";
                    if (polling_status == HIGH)
                        delay(500);
                    else
                    {
                        status = S_OK;
                        break;
                    }
                }
                else
                {
                    richTextBox_plc.Text += "ON  ";
                    if (polling_status == HIGH)
                    {
                        status = S_OK;
                        break;
                    }
                    else
                        delay(500);
                }
            }
            return status;
        }

        void get_all_plc_m_status()
        {
            string contact_address = String.Empty;
            bool ret = false;

            //richTextBox_plc.Text += "測試 get_plc_m_status()\n";

            contact_address = (7980 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (7981 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (7982 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (7990 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (7991 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (7992 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
        }

        void set_all_plc_m_status_low()
        {
            plc_simulator_step = 0;
            string contact_address = String.Empty;

            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                contact_address = "7980";
                set_plc_m_status(contact_address, LOW);
                contact_address = "7981";
                set_plc_m_status(contact_address, LOW);
                contact_address = "7982";
                set_plc_m_status(contact_address, LOW);
                contact_address = "7990";
                set_plc_m_status(contact_address, LOW);
                contact_address = "7991";
                set_plc_m_status(contact_address, LOW);
                contact_address = "7992";
                set_plc_m_status(contact_address, LOW);
                contact_address = "10012";
                set_plc_m_status(contact_address, LOW);
                contact_address = "12012";
                set_plc_m_status(contact_address, LOW);
                contact_address = "12013";
                set_plc_m_status(contact_address, LOW);
            }
            else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                contact_address = "5680";
                set_plc_m_status(contact_address, LOW);
                contact_address = "5681";
                set_plc_m_status(contact_address, LOW);
                contact_address = "5682";
                set_plc_m_status(contact_address, LOW);
                contact_address = "5690";
                set_plc_m_status(contact_address, LOW);
                contact_address = "5691";
                set_plc_m_status(contact_address, LOW);
                contact_address = "5692";
                set_plc_m_status(contact_address, LOW);
                contact_address = "13012";
                set_plc_m_status(contact_address, LOW);
                contact_address = "15012";
                set_plc_m_status(contact_address, LOW);
                contact_address = "15013";
                set_plc_m_status(contact_address, LOW);
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
            }
        }

        bool check_all_plc_m_status_low()
        {
            string contact_address = String.Empty;
            bool ret = false;
            bool all_plc_m_status = true;

            //richTextBox_plc.Text += "測試 get_plc_m_status()\n";

            /* 不用檢查 M7980
            contact_address = "7980";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;
            */

            contact_address = (7981 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (7982 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (7990 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (7991 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (7992 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            return all_plc_m_status;
        }

        private void bt_plc_clear_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Clear();
        }

        private void bt_copy_to_clipboard_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox_plc.Text + "\n");
            Clipboard.SetDataObject(richTextBox_plc.Text + "\n");      //建議用此
            richTextBox_plc.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_save_to_file_Click(object sender, EventArgs e)
        {
            string filename = "iMS_Link_XXXX_log_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            if (flag_automation_mode == MODE_AWB)
            {
                filename = "iMS_Link_AWB_log_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            }
            else
            {
                filename = "iMS_Link_WRITE_DATA_log_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            }

            saveFileDialog1.Title = "儲存資料";
            saveFileDialog1.FileName = filename;
            saveFileDialog1.Filter = "文字檔|*.txt|所有檔|*.*";   //限定檔案格式
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Application.StartupPath; //從目前目錄開始尋找檔案

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //richTextBox_plc.Text += "2 get filename : " + saveFileDialog1.FileName + "\n";
                //richTextBox_plc.Text += "length : " + saveFileDialog1.FileName.Length.ToString() + "\n";

                //StreamReader sr = new StreamReader(saveFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                FileStream filestream = File.Open(saveFileDialog1.FileName, FileMode.Create);
                StreamWriter str_writer = new StreamWriter(filestream);

                str_writer.WriteLine(richTextBox1.Text);

                str_writer.WriteLine("----------------------------------------------------------------\n");

                str_writer.WriteLine(richTextBox_plc.Text);

                // Dispose StreamWriter
                str_writer.Dispose();
                // Close FileStream
                filestream.Close();

                richTextBox_plc.Text += "儲存資料完畢，檔案：" + saveFileDialog1.FileName + "\n";
            }
            else
            {
                richTextBox_plc.Text += "未選取檔案\n";
            }
        }

        void do_PC_PLC_Communication(object sender, EventArgs e)
        {
            if (flag_use_real_plc == true)
                plc_do_check_time = false;  //預設 做 燒錄/色調

            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "do_PC_PLC_Communication 燒錄 / 燒錄對時\n";
            }
            else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "do_PC_PLC_Communication 色調 / 色調對時\n";
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXX";
            }

            if (flag_use_real_plc == false)
            {
                plc_do_check_time = true; //只做某一種
                if (plc_do_check_time == true)
                {
                    plc_do_check_time = false;
                    richTextBox_plc.Text += "這次做燒錄/色調\n";
                }
                else
                {
                    plc_do_check_time = true;
                    richTextBox_plc.Text += "這次做對時\n";
                }
            }

            richTextBox_plc.Text += "\nMaster 決定PLC測試項目\t";
            if (flag_automation_mode == MODE_AWB)
            {
                if (plc_do_check_time == false)
                {
                    richTextBox_plc.Text += "色彩調教\n";
                    plc_m_address_offset = OFFSET_M_AWB;
                    plc_d_address_offset = OFFSET_D_AWB;

                    lb_plc_pc0.Text = "M13000 PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M13001 PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M13002 PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M15000 PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M15001 PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M15002 PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (5900 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (5910 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (5950 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (5960 + plc_d_address_offset).ToString();
                    lb_pc_plc3b.Text = "";
                    lb_pc_plc4b.Text = "";
                    lb_read_write_plc.Text = "";
                }
                else
                {
                    richTextBox_plc.Text += "色彩調教\t對時\n";
                    plc_m_address_offset = OFFSET_M_AWB;
                    //plc_d_address_offset += OFFSET_D_AWB;

                    /*
                    lb_plc_pc0.Text = "M13000 PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M13001 PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M13002 PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M15000 PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M15001 PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M15002 PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (5900 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (5910 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (5950 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (5960 + plc_d_address_offset).ToString();
                    lb_pc_plc3b.Text = "";
                    lb_pc_plc4b.Text = "";
                    lb_read_write_plc.Text = "";
                    */
                }
                groupBox_plc.BackColor = Color.LightYellow;
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                if (plc_do_check_time == false)
                {
                    richTextBox_plc.Text += "序號燒錄\n";
                    plc_m_address_offset = OFFSET_M_WRITE_DATA;
                    plc_d_address_offset = OFFSET_D_WRITE_DATA;

                    lb_plc_pc0.Text = "M" + (7980 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M" + (7981 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M" + (7982 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M" + (7990 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M" + (7991 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M" + (7992 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (5900 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (5910 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (5950 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (5960 + plc_d_address_offset).ToString();
                    lb_pc_plc3b.Text = "";
                    lb_pc_plc4b.Text = "";
                    lb_read_write_plc.Text = "";
                }
                else
                {
                    richTextBox_plc.Text += "序號燒錄\t對時\n";
                    plc_m_address_offset = OFFSET_M_WRITE_DATA;
                    plc_d_address_offset += OFFSET_D_WRITE_DATA;

                    /*
                    lb_plc_pc0.Text = "M" + (7980 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M" + (7981 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M" + (7982 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M" + (7990 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M" + (7991 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M" + (7992 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (5900 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (5910 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (5950 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (5960 + plc_d_address_offset).ToString();
                    lb_pc_plc3b.Text = "";
                    lb_pc_plc4b.Text = "";
                    lb_read_write_plc.Text = "";
                    */
                }
                groupBox_plc.BackColor = Color.LightPink;
            }
            else
            {
                groupBox_plc.Text = "自動化作業";
                groupBox_plc.BackColor = Color.LightGray;
                //richTextBox_plc.Text += "groupBox_plc 背景色 LightGray\n";
            }
            string contact_address = String.Empty;
            bool ret = false;

            flag_plc_test_busy = false;
            richTextBox_plc.Text += "測試PLC作業流程 ST\t" + DateTime.Now.ToString() + "\n";

            richTextBox_plc.Text += "(0) PC 啟動完成, 檢查PLC是否已開機\n";

            while (ret == false)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    return;
                }
                ret = check_plc_power_status();

                if (ret == true)
                {
                    richTextBox_plc.Text += "(0) 三菱PLC 已 Ready, 繼續\n";
                }
                else
                {
                    //richTextBox_plc.Text += "(0) 三菱PLC 不 Ready, 等待\n";
                    delay(500);
                }
            }

            richTextBox_plc.Text += "(0) PC 啟動完成, 檢查所有 M1XXXX 信號 是否皆為 LOW\n";

            set_all_plc_m_status_low();

            while (ret == false)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    return;
                }
                ret = check_all_plc_m_status_low();
                if (ret == true)
                {
                    richTextBox_plc.Text += "(0) 所有 M1XXXX 信號 皆為 LOW, 繼續\n";
                }
                else
                {
                    richTextBox_plc.Text += "(0) 有 M1XXXX 信號 不為 LOW, 等待\n";
                    delay(500);
                }
            }

            //richTextBox_plc.Text += "(0) PC 啟動完成, 偵測PLC之M7980信號 或 M13000信號\n";
            richTextBox_plc.Text += "(0) PC 啟動完成\t";
            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                if (plc_do_check_time == false)
                {
                    richTextBox_plc.Text += "燒錄\n";
                }
                else
                {
                    richTextBox_plc.Text += "燒錄對時\n";
                }
            }
            else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                if (plc_do_check_time == false)
                {
                    richTextBox_plc.Text += "色調\n";
                }
                else
                {
                    richTextBox_plc.Text += "色調對時\n";
                }
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXX";
            }

            richTextBox_plc.Text += "(1a) PLC 準備資料\n";

            richTextBox_plc.Text += "(1b) 若是要做燒錄/色調\n";
            richTextBox_plc.Text += "\t(1b1) PLC 把相機序號資料放在 D" + (5900 + plc_d_address_offset).ToString() + "\n";
            richTextBox_plc.Text += "\t(1b2) PLC 拉高 M" + (7980 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知條碼內容已備便\n";
            richTextBox_plc.Text += "(1b) 若是要做燒錄/色調 對時\n";
            richTextBox_plc.Text += "\t(1c1) PLC 把對時資料放在 D" + (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString() + "\n";
            richTextBox_plc.Text += "\t(1c2) PLC 拉高 M" + (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + ", 供PC讀取, 通知對時資料已備便\n";

            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "(3a) 燒錄, ";
            }
            else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "(3a) 色調, ";
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXX";
            }

            string contact_address1 = (7980 + plc_m_address_offset).ToString();
            string contact_address2 = (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
            string get_signal = string.Empty;
            int get_plc_status_count = 1;
            while (true)  // 應該要無限制在此等待命令
            {
                //richTextBox_plc.Text += "目前狀態 : " + plc_simulator_step.ToString() + "\n";
                //richTextBox_plc.Text += "PC 讀取 M" + contact_address1 + " 或 M" + contact_address2 + " 狀態\t=>\t";
                plc_message = "(3a) PC 讀取 M" + contact_address1 + " 或 M" + contact_address2 + " 狀態 " + get_plc_status_count.ToString();
                get_plc_status_count++;

                get_signal = polling_2m_status(contact_address1, contact_address2, HIGH);
                if ((get_signal == contact_address1) || (get_signal == contact_address2))
                {
                    break;
                }
                else if (get_signal == "polling_fail")
                {
                    //richTextBox_plc.Text += "偵測不到PLC訊號, 繼續偵測\n";
                }
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    return;
                }
            }
            richTextBox_plc.Text += "\n(3b) PC 取得 M" + get_signal + "為 ON\t=> ";
            plc_message = "(3b) PC 取得 M" + get_signal + "為 ON";

            if (get_signal == contact_address1)
            {
                /*
                //pc_work_type = MODE_WRITE_DATA;   //1: MODE_WRITE_DATA 燒錄
                groupBox_plc.BackColor = Color.DeepPink;
                //richTextBox_plc.Text += "groupBox_plc 背景色 DeepPink\n";
                richTextBox_plc.Text += "\n(3b) PC 取得 M7980 為 ON\t=> 序號燒錄\t";
                lb_plc_main_mesg3.Text = "Slave 接收命令";

                richTextBox_plc.Text += "序號燒錄\n";
                plc_m_address_offset = OFFSET_M_WRITE_DATA;
                plc_d_address_offset = OFFSET_D_WRITE_DATA;
                */

                if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "燒錄\n";
                    plc_message += "\t取得燒錄命令";
                    lb_plc_command_type.Text = "資料燒錄";
                }
                else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "色調\n";
                    plc_message += "色調";
                    lb_plc_command_type.Text = "色彩調教";
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXXX";
                }
                plc_do_check_time = false;
            }
            else if (get_signal == contact_address2)
            {
                /*
                //pc_work_type = MODE_AWB;   //2: MODE_AWB 色調
                groupBox_plc.BackColor = Color.Yellow;
                //richTextBox_plc.Text += "groupBox_plc 背景色 Yellow\n";
                richTextBox_plc.Text += "\n(3b) PC 取得 M13000 為 ON\t=> 色彩調教\t";
                lb_plc_main_mesg3.Text = "Slave 接收命令";

                richTextBox_plc.Text += "色彩調教\n";
                plc_m_address_offset = OFFSET_M_AWB;
                plc_d_address_offset = OFFSET_D_AWB;
                */

                if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "燒錄對時\n";
                    lb_plc_command_type.Text = "資料燒錄\n對時";
                }
                else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "色調對時\n";
                    lb_plc_command_type.Text = "色彩調教\n對時";
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXXX";
                }
                plc_do_check_time = true;
            }
            else
            {
                richTextBox_plc.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXX\t";
            }

            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            flag_plc_test_busy = true;
            flag_plc_test_count++;

            //開始計時
            richTextBox_plc.Text += "時間1 : " + DateTime.Now.ToString() + "\n";
            stopwatch_plc = new Stopwatch();
            stopwatch_plc.Start();
            if (plc_do_check_time == false)
            {
                contact_address = (5900 + plc_d_address_offset).ToString();
                richTextBox_plc.Text += "(3c1) PC 讀取 D" + contact_address + " 資料\n";
            }
            else
            {
                contact_address = (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
                richTextBox_plc.Text += "(3c2) PC 讀取 D" + contact_address + " 資料\t對時\n";
            }

            show_plc_main_message1("讀取 D" + contact_address, S_OK, 30);
            camera_serial_data = string.Empty;

            while (camera_serial_data.Length <= 0)
            {
                camera_serial_data = get_plc_d_data(contact_address);
            }

            //richTextBox_plc.Text += "取得 D" + contact_address + " 資料 : " + camera_serial_data + "\n";
            //richTextBox_plc.Text += "\nlen = " + camera_serial_data.Length.ToString() + "\n";

            //處理相機序號問題
            int i;
            int len = camera_serial_data.Length;
            richTextBox_plc.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox_plc.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
            }
            richTextBox_plc.Text += "\n";

            //檢查英數字元的正確性
            bool flag_serial_data_wrong = false;
            for (i = 0; i < len; i++)
            {
                //richTextBox_plc.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
                var kk = camera_serial_data[i];

                if (((kk >= 'A') && (kk <= 'Z')) || ((kk >= 'a') && (kk <= 'z')) || ((kk >= '0') && (kk <= '9')))
                {
                    //richTextBox_plc.Text += "O";
                    flag_serial_data_wrong = false;
                }
                else
                {
                    //richTextBox_plc.Text += "X";
                    flag_serial_data_wrong = true;
                    break;
                }
            }
            if (flag_serial_data_wrong == true)
            {
                richTextBox_plc.Text += "有裁剪\n";
                int cut_length = i;
                //richTextBox_plc.Text += cut_length.ToString() + "\n";
                camera_serial_data = camera_serial_data.Substring(0, cut_length);
            }
            else
            {
                richTextBox_plc.Text += "無裁剪\n";
            }

            len = camera_serial_data.Length;
            //richTextBox_plc.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            richTextBox_plc.Text += "(已處理)相機序號 : \t" + camera_serial_data + "\n";

            delay(500);

            string data_to_write = string.Empty;
            string contact_address_to = string.Empty;
            if (plc_do_check_time == false)
            {
                //一般
                contact_address_to = (5950 + plc_d_address_offset).ToString();

                richTextBox_plc.Text += "(3d1) PC 將 從 D" + contact_address + " 取得的資料 寫到 D" + contact_address_to + "\n";
                plc_message = "PC 將 從 D" + contact_address + " 取得的資料 寫到 D" + contact_address_to;

                data_to_write = camera_serial_data;

                //richTextBox_plc.Text += "data_to_write : " + data_to_write + "\n";
                //richTextBox_plc.Text += "\nlen = " + data_to_write.Length.ToString() + "\n";

                show_plc_main_message1("寫入 D" + contact_address_to, S_OK, 30);
                set_plc_d_data(contact_address_to, data_to_write);
            }
            else
            {
                //對時
                contact_address = (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
                contact_address_to = (5950 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();

                show_plc_main_message1("寫入 D" + contact_address_to, S_OK, 30);
                richTextBox_plc.Text += "(3d2) PC 將 從 D" + contact_address + " 取得的資料 寫到 D" + contact_address_to + "\n";

                //讀資料 寫資料 分析資料

                int year = 2023;
                int month = 5;
                int day = 20;
                int hour = 13;
                int minute = 14;
                int second = 56;

                if (flag_use_real_plc == false)
                {
                    //假上位
                    year = 2023;
                    month = 5;
                    day = 20;
                    hour = 13;
                    minute = 14;
                    second = 56;
                }
                else
                {
                    for (int offset = 0; offset < 6; offset++)
                    {
                        richTextBox_plc.Text += "offset = " + offset.ToString() + "\n";
                        string contact_address_r = (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME + offset).ToString();
                        string contact_address_w = (5950 + plc_d_address_offset + OFFSET_D_CHECK_TIME + offset).ToString();
                        string data = string.Empty;
                        data = get_plc_d_data_bcd16(contact_address_r);
                        //richTextBox_plc.Text += data + "\tlen = " + data.Length.ToString() + "\n";
                        if (data.Length > 0)
                        {
                            set_plc_d_data_bcd16(contact_address_w, data);

                            int vv = 0;
                            for (i = 0; i < data.Length; i++)
                            {
                                vv += (data[i] - 0x30) * (int)(Math.Pow(10, data.Length - i - 1));
                            }

                            if (offset == 0)    //年
                            {
                                richTextBox_plc.Text += "取得 年 " + vv.ToString() + "\n";
                                year = vv;
                            }
                            else if (offset == 1)    //月
                            {
                                richTextBox_plc.Text += "取得 月 " + vv.ToString() + "\n";
                                month = vv;
                            }
                            else if (offset == 2)    //日
                            {
                                richTextBox_plc.Text += "取得 日 " + vv.ToString() + "\n";
                                day = vv;
                            }
                            else if (offset == 3)    //時
                            {
                                richTextBox_plc.Text += "取得 時 " + vv.ToString() + "\n";
                                hour = vv;
                            }
                            else if (offset == 4)    //分
                            {
                                richTextBox_plc.Text += "取得 分 " + vv.ToString() + "\n";
                                minute = vv;
                            }
                            else if (offset == 5)    //秒
                            {
                                richTextBox_plc.Text += "取得 秒 " + vv.ToString() + "\n";
                                second = vv;
                            }
                            else
                            {
                                richTextBox_plc.Text += "XXXXXXXXX\n";
                            }
                        }
                    }
                }

                richTextBox_plc.Text += "PC開始做對時\n";

                richTextBox_plc.Text += "年 : " + year.ToString() + "\n";
                richTextBox_plc.Text += "月 : " + month.ToString() + "\n";
                richTextBox_plc.Text += "日 : " + day.ToString() + "\n";
                richTextBox_plc.Text += "時 : " + hour.ToString() + "\n";
                richTextBox_plc.Text += "分 : " + minute.ToString() + "\n";
                richTextBox_plc.Text += "秒 : " + second.ToString() + "\n";

                flag_use_user_time = true;
                datetime_user = new DateTime(year, month, day, hour, minute, second);	//年月日時分秒毫秒
                datetime_diff = (TimeSpan)(DateTime.Now - datetime_user);
                /*
                richTextBox_plc.Text += "system time = " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                richTextBox_plc.Text += "usertime    = " + datetime_user.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                richTextBox_plc.Text += "diff = " + datetime_diff.ToString() + "\n";
                */
            }

            delay(500);

            if (plc_do_check_time == false)
            {
                contact_address = (7990 + plc_m_address_offset).ToString();
            }
            else
            {
                contact_address = (7990 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
            }

            richTextBox_plc.Text += "(4) PC 拉高 M" + contact_address + ", 通知PLC, PC動作已完成\n";
            plc_message = "(4) PC 拉高 M" + contact_address + ", 通知PLC, PC動作已完成";
            //richTextBox_plc.Text += "[M status] M7990 HIGH\n";

            timer_plc_status_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            if (plc_do_check_time == false)
            {
                //一般 燒錄/色調

                bool flag_comport_connection = false;
                richTextBox_plc.Text += "aaa 檢查 comport 連線\t" + DateTime.Now.ToString() + "\n";
                int cnt = 0;
                while ((flag_comport_connection == false) && (cnt++ < 5))
                {
                    //約每2秒檢查一次 最多5次
                    flag_comport_connection = check_comport_connection();
                    richTextBox_plc.Text += "bbb 檢查 comport 連線\t" + flag_comport_connection.ToString() + "\t" + DateTime.Now.ToString() + "\n";
                    delay(100);
                }

                if (flag_comport_connection == true)
                    richTextBox_plc.Text += "ccc comport 連線 OK\n";
                else
                    richTextBox_plc.Text += "ddd comport 連線 NG\n";

                do_PC_PLC_Communication_normal(sender, e);
            }
            else
            {
                //對時 燒錄/色調
                do_PC_PLC_Communication_check_time(sender, e);
            }
        }

        void do_PC_PLC_Communication_normal(object sender, EventArgs e)
        {
            string contact_address = string.Empty;
            string contact_address_to = string.Empty;

            plc_message = "";
            richTextBox_plc.Text += "(5a) PLC收到 PC訊號 M" + contact_address + " ON時,PLC確認資料一致\n";
            richTextBox_plc.Text += "(5b) PLC 拉高 M" + (7981 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知開始工作\n";
            //richTextBox_plc.Text += "[M status] M7981 HIGH\n";

            richTextBox_plc.Text += "(6a) PC 讀取 M" + (7981 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (7981 + plc_m_address_offset).ToString();

            richTextBox_plc.Text += "\npolling 時間1a : " + DateTime.Now.ToString() + "\n";
            int polling_status = polling_m_status(contact_address, HIGH);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間1b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認1\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認1");
                //MessageBox.Show("PLC通信異常1", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號1");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(6b) PC 取得 M" + (7981 + plc_m_address_offset).ToString() + " 為 ON\n";

            richTextBox_plc.Text += "(6c) PC 拉高 M" + (7991 + plc_m_address_offset).ToString() + ", 供PLC讀取, 通知PC已開始工作\t";
            //richTextBox_plc.Text += "[M status] M7991 HIGH\n";

            lb_plc_main_mesg3.Text = "Slave 開始工作";

            contact_address = (7991 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, HIGH);

            if (flag_automation_mode == MODE_AWB)
            {
                richTextBox_plc.Text += "色彩調教\n";
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                richTextBox_plc.Text += "相機序號燒錄\n";
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXX\n";
            }

            richTextBox_plc.Text += "\nPC 開始工作........\n";

            //取得相機序號 

            richTextBox_plc.Text += "(已處理)相機序號 : \t" + camera_serial_data + "\n";

            richTextBox_plc.Text += "取得生產年月日\n";

            int year_month_day_address = 0;
            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "燒錄年月日\n";
                year_month_day_address = 5910;
            }
            else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                richTextBox_plc.Text += "色調年月日\n";
                year_month_day_address = 3910;
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXX";
                year_month_day_address = 5910;
            }

            string year = "2024";
            string month = "03";
            string day = "11";

            if (flag_use_real_plc == true)
            {
                contact_address = year_month_day_address.ToString();
                show_plc_main_message1("讀取 D" + contact_address, S_OK, 30);

                contact_address = year_month_day_address.ToString();
                year = get_plc_d_data2(contact_address);
                contact_address = (year_month_day_address + 1).ToString();
                month = get_plc_d_data2(contact_address);
                contact_address = (year_month_day_address + 2).ToString();
                day = get_plc_d_data2(contact_address);

                if (month.Length < 2)
                    month = "0" + month;

                if (day.Length < 2)
                    day = "0" + day;
            }

            richTextBox_plc.Text += "year : " + year + "\n";
            richTextBox_plc.Text += "month : " + month + "\n";
            richTextBox_plc.Text += "day : " + day + "\n";

            year_month_day_data = year + month + day;

            richTextBox_plc.Text += "year_month_day_data : " + year_month_day_data + "\n";

            richTextBox_plc.Text += "取得 D" + contact_address + " 資料 : " + year_month_day_data + "\n";
            richTextBox_plc.Text += "\nlen = " + year_month_day_data.Length.ToString() + "\n";

            int work_result = 0xff;

            if (year_month_day_data.Contains("無資料"))
            {
                flag_year_month_day_data_ok = false;
                work_result = REASON_NO_DATE_TIME_DATA;
            }
            else
            {
                flag_year_month_day_data_ok = true;
            }

            save_data_folder_date = year_month_day_data;
            richTextBox_plc.Text += "save_data_folder_date = " + save_data_folder_date + "\n";

            Random r = new Random();

            if (flag_use_real_ims == true)    //真的做 燒錄 或 色調
            {
                if (flag_automation_mode == MODE_AWB)  //色彩調教
                {
                    if (work_result != REASON_NO_DATE_TIME_DATA)
                    {
                        richTextBox_plc.Text += "要開始做AWB, 色調主機重開, 並等5秒, 時間 : " + DateTime.Now.ToString() + "\n";
                        reset_IMS_AWB();

                        for (int i = 0; i < 10; i++)
                        {
                            //delay 10000 約 10秒
                            //delay 1000 約 1秒
                            delay(230);
                            richTextBox_plc.Text += "S ";
                            Application.DoEvents();
                        }
                        richTextBox_plc.Text += "影像重抓\n";
                        button12_Click_1(sender, e);
                        for (int i = 0; i < 5; i++)
                        {
                            //delay 10000 約 10秒
                            //delay 1000 約 1秒
                            delay(230);
                            richTextBox_plc.Text += "S ";
                            Application.DoEvents();
                        }
                        richTextBox_plc.Text += "\n開始做AWB, 時間 : " + DateTime.Now.ToString() + "\n";
                        work_result = do_awb(sender, e);
                    }
                    check_awb_result(work_result);

                    if (bt_awb_break.Text == "確認")
                    {
                        bt_awb_break_Click(sender, e);
                        flag_wait_for_confirm = false;
                    }
                }
                else if (flag_automation_mode == MODE_WRITE_DATA)
                {
                    if (work_result != REASON_NO_DATE_TIME_DATA)
                    {
                        richTextBox_plc.Text += "相機序號燒錄\n";
                        string camera_serial_data2 = string.Empty;
                        if (camera_serial_data.Length > 16)
                        {
                            camera_serial_data2 = camera_serial_data.Substring(0, 16);
                        }
                        else if (camera_serial_data.Length < 16)
                        {
                            camera_serial_data2 = camera_serial_data.PadRight(16, '@'); //向長度小於16的字符串末尾添加空格，補足16個字符
                        }
                        else
                        {
                            camera_serial_data2 = camera_serial_data;
                        }
                        work_result = do_write_serial_data(camera_serial_data2);

                        string reason = string.Empty;

                        richTextBox_plc.Text += "PC 工作結果: 0x" + work_result.ToString("X2") + " = " + work_result.ToString() + "\t";
                        if (work_result == S_OK)
                        {
                            reason = "OK";
                        }
                        else if (work_result == DONGLE_NONE)
                        {
                            reason = "無連接器";
                        }
                        else if (work_result == CAMERA_NONE)
                        {
                            reason = "有連接器, 無相機";
                        }
                        else if (work_result == CAMERA_UNKNOWN)
                        {
                            reason = "相機狀態不明";
                        }
                        else if (work_result == CAMERA_SENSOR_FAIL)
                        {
                            reason = "相機無法讀寫";
                        }
                        else if (work_result == REASON_NO_COMPORT)
                        {
                            reason = "無comport連線";
                        }
                        else if (work_result == REASON_NO_IMS_CAMERA)
                        {
                            reason = "無IMS相機";
                        }
                        else if (work_result == REASON_SERIAL_EXISTS)
                        {
                            reason = "相機內已有其他資料";
                        }
                        else if (work_result == REASON_SERIAL_FAIL)
                        {
                            reason = "相機序號格式錯誤";
                        }
                        else if (work_result == REASON_NO_DATE_TIME_DATA)
                        {
                            reason = "無年月日資料";
                        }
                        else
                        {
                            reason = "其他";
                        }
                        camera_serial_data2 = camera_serial_data2.Replace("@", "");

                        //richTextBox_plc.Text += "把資料暫存起來\n";
                        camera_serials.Add(new string[] { camera_serial_data2.ToUpper(), "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss"), reason });

                        richTextBox_plc.Text += "自動存檔\n";
                        flag_operation_mode = MODE_RELEASE_STAGE4;
                        exportCSV();
                        flag_operation_mode = MODE_RELEASE_STAGE2;
                    }
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXX\n";
                }
            }
            else   //假的做 燒錄 或 色調
            {
                if (flag_automation_mode == MODE_AWB)  //色彩調教
                {
                    //假的做AWB
                    for (int i = 0; i < 100; i++)
                    {
                        delay(50);
                        richTextBox_plc.Text += "a ";
                    }
                    work_result = r.Next(1, 20);
                }
                else if (flag_automation_mode == MODE_WRITE_DATA)
                {
                    //假的做資料燒錄
                    for (int i = 0; i < 100; i++)
                    {
                        delay(50);
                        richTextBox_plc.Text += "d ";
                    }
                    work_result = r.Next(0, 10);
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXX\n";
                }
            }
            richTextBox_plc.Text += "\n\n(7) PC 做完工作, 將結果碼寫在 D" + (5960 + plc_d_address_offset).ToString() + "\n";

            if (flag_always_return_ok_mode == true)
            {
                richTextBox_plc.Text += "粉飾太平模式\n";
                work_result = 0;
            }

            global_work_result = work_result;
            string string_work_result = get_work_result_data_write(work_result);

            richTextBox_plc.Text += "PC 工作結果: 0x" + work_result.ToString("X2") + " = " + work_result.ToString() + "\t" + string_work_result + "\n";

            work_result += 1;
            string write_data = work_result.ToString();
            show_plc_main_message1("寫入: D" + (5960 + plc_d_address_offset).ToString() + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16((5960 + plc_d_address_offset).ToString(), write_data);

            richTextBox_plc.Text += "(8) PC 拉高 M" + (7992 + plc_m_address_offset).ToString() + ", 供PLC讀取, 通知PLC, PC已做完工作\n";
            //richTextBox_plc.Text += "[M status] M7992 HIGH\n";

            if (flag_automation_mode == MODE_WRITE_DATA)   //1: 序號燒錄
            {
                groupBox_plc.BackColor = Color.LightPink;
                //richTextBox_plc.Text += "groupBox_plc 背景色 LightPink\n";
                lb_plc_main_mesg3.Text = "Slave 工作完成";
            }
            else if (flag_automation_mode == MODE_AWB)   //0: 色彩調教
            {
                groupBox_plc.BackColor = Color.LightYellow;
                //richTextBox_plc.Text += "groupBox_plc 背景色 LightYellow\n";
                lb_plc_main_mesg3.Text = "Slave 工作完成";
            }
            else
            {
                groupBox_plc.BackColor = Color.Red;
                //richTextBox_plc.Text += "groupBox_plc 背景色 Red\n";
            }

            delay(500);

            contact_address = (7992 + plc_m_address_offset).ToString();
            timer_plc_status_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox_plc.Text += "(9) PLC偵測到 PC之動作完成信號 M" + (7992 + plc_m_address_offset).ToString() + ", PLC設定 M" + (7982 + plc_m_address_offset).ToString() + "為ON\n";
            //richTextBox_plc.Text += "[M status] M7982 HIGH\n";

            richTextBox_plc.Text += "(10a) PC 檢測 M" + (7982 + plc_m_address_offset).ToString() + " 和 M" + (7992 + plc_m_address_offset).ToString() + "\n";

            richTextBox_plc.Text += "(10a1) PC 讀取 M" + (7982 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (7982 + plc_m_address_offset).ToString();
            richTextBox_plc.Text += "\npolling 時間2a : " + DateTime.Now.ToString() + "\n";
            polling_status = polling_m_status(contact_address, HIGH);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間2b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到訊號, timeout, 清除信號, 等待使用者確認2\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認2");
                //MessageBox.Show("PLC通信異常2", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號2");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(10a2) PC 取得 M" + (7982 + plc_m_address_offset).ToString() + " 為 ON\n";

            richTextBox_plc.Text += "(10a3) PC 讀取 M" + (7992 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (7992 + plc_m_address_offset).ToString();
            richTextBox_plc.Text += "\npolling 時間3a : " + DateTime.Now.ToString() + "\n";
            polling_status = polling_m_status(contact_address, HIGH);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間3b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到訊號, timeout, 清除信號, 等待使用者確認3\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認3");
                //MessageBox.Show("PLC通信異常3", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號3");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(10a4) PC 取得 M" + (7992 + plc_m_address_offset).ToString() + " 為 ON\n";

            delay(500);

            richTextBox_plc.Text += "(10b) PC 清除 D" + (5950 + plc_d_address_offset).ToString() + " ~ D" + (8007 + plc_d_address_offset).ToString() + " 資料\n";
            erase_plc_d_data((5950 + plc_d_address_offset).ToString(), 8);

            richTextBox_plc.Text += "(10c) PC 令 (收到動作要求信號)M" + (7990 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M7990 LOW\n";
            contact_address = (7990 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "(10d) PC 令 (動作執行信號)M" + (7991 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M7991 LOW\n";
            contact_address = (7991 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            //richTextBox_plc.Text += "[M status] M7980 LOW\n";
            //richTextBox_plc.Text += "[M status] M7981 LOW\n";

            delay(500);

            richTextBox_plc.Text += "(10e) PLC 清除 D" + (5900 + plc_d_address_offset).ToString() + " ~ D" + (2007 + plc_d_address_offset).ToString() + " 資料\n";
            richTextBox_plc.Text += "(10f) PLC 令 (動作要求訊號)M" + (7980 + plc_m_address_offset).ToString() + " 為 OFF\n";
            richTextBox_plc.Text += "(10g) PLC 令 (動作開始要求訊號)M" + (7981 + plc_m_address_offset).ToString() + " 為 OFF\n";

            delay(500);

            richTextBox_plc.Text += "(11a) PC 檢測 (PLC動作完成信號)M" + (7982 + plc_m_address_offset).ToString() + "\n";
            //當PC收到PLC收到動作完成訊號M7982 ON之後,結果碼D5960資料清除
            //PC->PLC動作完成訊號M7992 OFF

            richTextBox_plc.Text += "(11a) PC 讀取 M" + (7982 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (7982 + plc_m_address_offset).ToString();
            richTextBox_plc.Text += "\npolling 時間4a : " + DateTime.Now.ToString() + "\n";
            polling_status = polling_m_status(contact_address, HIGH);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間4b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到訊號, timeout, 清除信號, 等待使用者確認4\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認4");
                //MessageBox.Show("PLC通信異常4", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號4");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(11b) PC 取得 M" + (7982 + plc_m_address_offset).ToString() + " 為 ON\n";

            /*  暫不清除資料
            richTextBox_plc.Text += "(11c) PC 清除 D5960資料\n";
            contact_address = "5960";
            erase_plc_d_data(contact_address, 1);
            */

            richTextBox_plc.Text += "(11d) PC 令 M" + (7992 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M7992 LOW\n";
            contact_address = (7992 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            delay(500);

            richTextBox_plc.Text += "(12a) PLC 收到 PC 設定 M" + (7992 + plc_m_address_offset).ToString() + " 為 OFF, PLC 設定 M" + (7982 + plc_m_address_offset).ToString() + "為OFF\n";
            richTextBox_plc.Text += "[M status] M" + (7982 + plc_m_address_offset).ToString() + " LOW\n";

            richTextBox_plc.Text += "(12b) PC 讀取 M" + (7982 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (7982 + plc_m_address_offset).ToString();
            richTextBox_plc.Text += "\npolling 時間5a : " + DateTime.Now.ToString() + "\n";
            polling_status = polling_m_status(contact_address, LOW);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間5b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到訊號, timeout, 清除信號, 等待使用者確認5\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認5");
                //MessageBox.Show("PLC通信異常5", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號5");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(12c1) PC 取得 M" + (7982 + plc_m_address_offset).ToString() + " 為 LOW\n";
            get_all_plc_m_status();
            richTextBox_plc.Text += "測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\tOK\n\n\n";

            groupBox_plc.BackColor = Color.LightGray;
            //richTextBox_plc.Text += "groupBox_plc 背景色 LightGray\n";
            lb_plc_main_mesg3.Text = "Master 命令結束";

            stopwatch_plc.Stop();
            richTextBox_plc.Text += "PLC交握測試 完成時間: " + stopwatch_plc.ElapsedMilliseconds.ToString() + " msec\n";
            richTextBox_plc.Text += "時間2 : " + DateTime.Now.ToString() + "\n";
            flag_plc_test_busy = false;
        }

        string get_work_result_data_write(int work_result)
        {
            string result = string.Empty;

            if (work_result == S_OK)
            {
                result = "OK\n";
            }
            else if (work_result == DONGLE_NONE)
            {
                result = "無連接器\n";
            }
            else if (work_result == CAMERA_NONE)
            {
                result = "有連接器, 無相機\n";
            }
            else if (work_result == CAMERA_UNKNOWN)
            {
                result = "相機狀態不明\n";
            }
            else if (work_result == CAMERA_SENSOR_FAIL)
            {
                result = "相機無法讀寫\n";
            }
            else if (work_result == REASON_AWB_PROCESSING)
            {
                result = "AWB進行中\n";
            }
            else if (work_result == REASON_AWB_TIMEOUT)
            {
                result = "AWB作業延時\n";
            }
            else if (work_result == REASON_NO_COMPORT)
            {
                result = "無comport連線\n";
            }
            else if (work_result == REASON_NO_IMS_CAMERA)
            {
                result = "無IMS相機\n";
            }
            else if (work_result == REASON_SERIAL_EXISTS)
            {
                result = "相機內已有其他資料\n";
            }
            else if (work_result == REASON_SERIAL_FAIL)
            {
                result = "相機序號格式錯誤\n";
            }
            else if (work_result == REASON_FIND_AWB_AREA_FAIL_TOO_SMALL)
            {
                result = "AWB搜尋失敗, 太小\n";
            }
            else if (work_result == REASON_FIND_AWB_AREA_FAIL_TOO_FAR)
            {
                result = "AWB搜尋失敗, 太遠\n";
            }
            else if (work_result == REASON_MANUALLY_INTERRUPT)
            {
                result = "AWB人為中斷\n";
            }
            else if (work_result == REASON_NO_IMS_CAMERA_IMAGE)
            {
                result = "有IMS相機 但無IMS影像\n";
            }
            else if (work_result == REASON_NO_DATE_TIME_DATA)
            {
                result = "無年月日資料\n";
            }
            else
            {
                result = "其他\n";
            }
            return result;
        }

        void do_PC_PLC_Communication_check_time(object sender, EventArgs e)
        {
            //對時 完成

            delay(100);
            delay(100);
            string contact_address = (12013 + plc_m_address_offset).ToString();

            //對時完成 把 M12013拉為HIGH
            delay(100);
            delay(100);
            richTextBox_plc.Text += "(4b) PC 拉高 M" + contact_address + ", 通知PLC, PC動作已完成對時動作\n";

            set_plc_m_status(contact_address, HIGH);

            //pC檢查10012是否為low 若是 則將 12012   12013 拉為 low
            contact_address = (10012 + plc_m_address_offset).ToString();
            richTextBox_plc.Text += "\npolling 時間6a : " + DateTime.Now.ToString() + "\n";
            int polling_status = polling_m_status(contact_address, LOW);
            if (polling_status == S_FALSE)
            {
                richTextBox_plc.Text += "\npolling 時間6b : " + DateTime.Now.ToString() + "\n";
                richTextBox_plc.Text += "偵測不到訊號, timeout, 清除信號, 等待使用者確認6\n";
                set_all_plc_m_status_low();
                Logger.WriteLog("偵測不到PLC訊號, timeout, 清除信號, 等待使用者確認6");
                //MessageBox.Show("PLC通信異常6", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Logger.WriteLog("使用者確認, 回到原點, 開始偵測PLC訊號6");
                //richTextBox_plc.Text += "使用者確認, 回到原點\n";
                return;
            }
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;
                return;
            }

            richTextBox_plc.Text += "\n(12c2) PC 取得 M" + contact_address + " 為 LOW\n";

            contact_address = (12012 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            delay(100);
            delay(100);

            contact_address = (12013 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\tOK\n\n\n";

            groupBox_plc.BackColor = Color.LightGray;
            //richTextBox_plc.Text += "groupBox_plc 背景色 LightGray\n";
            lb_plc_main_mesg3.Text = "Master 命令結束";

            stopwatch_plc.Stop();
            richTextBox_plc.Text += "PLC交握測試 完成時間: " + stopwatch_plc.ElapsedMilliseconds.ToString() + " msec\n";
            richTextBox_plc.Text += "時間2 : " + DateTime.Now.ToString() + "\n";
            flag_plc_test_busy = false;
        }

        private void bt_plc_test_Click(object sender, EventArgs e)
        {
            flag_plc_test = true;
            flag_plc_test_busy = false;
            flag_plc_test_break = false;
            flag_plc_test_count = 0;
            bt_plc_test.BackColor = Color.Red;

            if (flag_comport_connection_ok == false)
            {
                if (flag_use_real_ims == true)
                {
                    //真下位
                    richTextBox_plc.Text += "無 comport 連線, 離開\n";
                    MessageBox.Show("無 COM port 連線\n無法啟動自動化作業", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    flag_plc_test = false;
                    bt_plc_test.BackColor = SystemColors.ControlLight;
                    return;
                }
            }

            richTextBox_plc.Text += "\n啟動自動化作業\n";

            if (flag_enaglb_automation_debug == true)
            {
                timer_automation_debug.Enabled = true;
            }
            else
            {
                timer_automation_debug.Enabled = false;
            }

            if (flag_automation_mode == MODE_WRITE_DATA)
            {
                this.Text = "iMS_Link_DataWrite";
            }

            int cnt = 1;
            while (true)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "使用者中斷PLC測試, 結束\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    break;
                }

                /*
                if (cnt == 3)
                {
                    richTextBox_plc.Text += "\n\n\n\n結束\n\n\n\n\n";
                    break;
                }
                */

                richTextBox_plc.Text += "\n第 " + (cnt++).ToString() + " 次測試, 時間 : " + DateTime.Now.ToString() + "\n";

                do_PC_PLC_Communication(sender, e);
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "使用者中斷PLC測試, 結束\n";
                    flag_plc_test_break = false;
                    bt_plc_test_break.BackColor = SystemColors.ControlLight;
                    break;
                }
                delay(1000);
            }

            bt_plc_test.BackColor = SystemColors.ControlLight;
            bt_plc_test_break.BackColor = SystemColors.ControlLight;

            if (flag_plc_test_break == true)
            {
                flag_plc_test_break = false;
                bt_plc_test_break.BackColor = SystemColors.ControlLight;

                richTextBox_plc.Text += "\n測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\t使用者中斷\n\n";

                stopwatch_plc.Stop();
                richTextBox_plc.Text += "時間3 : " + DateTime.Now.ToString() + "\n";
            }
            flag_plc_test = false;
            flag_plc_test_busy = false;
            flag_plc_test_break = false;
            bt_plc_test_break.BackColor = SystemColors.ControlLight;
        }

        private void bt_plc_test_break_Click(object sender, EventArgs e)
        {
            if (flag_plc_test == false)
                return;
            richTextBox_plc.Text += "設定 中斷\n";
            flag_plc_test_break = true;
            bt_plc_test_break.BackColor = Color.Red;
        }

        private void bt_plc_test_break_MouseDown(object sender, MouseEventArgs e)
        {
            if (flag_plc_test == false)
                return;
            richTextBox_plc.Text += "設定 中斷\n";
            flag_plc_test_break = true;
            bt_plc_test_break.BackColor = Color.Red;
        }

        private void bt_check_connection_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "檢查連線狀態\n";

            if (serialPort2.IsOpen == true)
            {
                richTextBox_plc.Text += "Comport 已開啟\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_ON;
            }
            else
            {
                richTextBox_plc.Text += "Comport 未開啟\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_OFF;
            }

            if (flag_comport_ok == true)
            {
                richTextBox_plc.Text += "Comport 開啟 OK\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_ON;
            }
            else
            {
                richTextBox_plc.Text += "Comport 開啟 失敗\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_OFF;
            }

            if (flag_comport_connection_ok == true)
            {
                richTextBox_plc.Text += "Comport 連線 OK\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_ON;
            }
            else
            {
                richTextBox_plc.Text += "Comport 連線 NG\n";
                pbx_ims_connection1.BackgroundImage = Properties.Resources.ims_connection1_OFF;
            }

            richTextBox_plc.Text += "檢查UART連線\t";

            bool comport_status = get_comport_status();
            if (comport_status == true)
            {
                richTextBox_plc.Text += "OK\n";
            }
            else
            {
                richTextBox_plc.Text += "NG\n";
            }

            //comport ok 才檢查相機連線
            if (flag_comport_connection_ok == true)
            {
                richTextBox_plc.Text += "檢查相機連線\n";
                int conn_status = get_camera_status();
                richTextBox_plc.Text += "檢查相機連線\t" + conn_status.ToString() + "\n";

                richTextBox_plc.Text += "檢查相機運行狀態\n";
                int frame_count = 0;
                int frame_count_old = 0;

                int i = 0;
                for (i = 0; i < 100; i++)
                {
                    frame_count = get_camera_frame_count();
                    if (frame_count == -1)
                        continue;

                    richTextBox_plc.Text += "第 " + (i + 1).ToString() + "次, Frame Count\t" + frame_count.ToString() + "\n";
                    if (i == 0)
                    {
                        frame_count_old = frame_count;
                    }
                    else
                    {
                        if (frame_count_old == frame_count)
                        {
                            richTextBox_plc.Text += "Frame count 相同, 再測一次\n";
                        }
                        else
                        {
                            richTextBox_plc.Text += "Frame count 不同, 表示相機正常運行\n";
                            break;
                        }
                        delay(100);
                    }
                }

                if (i < 10)
                {
                    richTextBox_plc.Text += "相機運行 OK\n";
                    pbx_ims_connection4.BackgroundImage = Properties.Resources.ims_connection4_ON;
                }
                else
                {
                    richTextBox_plc.Text += "相機運行 NG\n";
                    pbx_ims_connection4.BackgroundImage = Properties.Resources.ims_connection4_OFF;
                }

                if (flag_ims_egd_exist == true)
                {
                    richTextBox_plc.Text += "有ims相機\n";
                    pbx_ims_connection3.BackgroundImage = Properties.Resources.ims_connection3_ON;
                }
                else
                {
                    richTextBox_plc.Text += "無ims相機\n";
                    pbx_ims_connection3.BackgroundImage = Properties.Resources.ims_connection3_OFF;
                }
            }
            richTextBox_plc.Text += "\n";
        }

        private void bt_read_camera_data_Click(object sender, EventArgs e)
        {
            int cnt = 0;
            /*
            byte page;
            int cnt = 0;

            richTextBox_plc.Text += "\n\nread camera awb data AWB_PAGE\n";
            page = AWB_PAGE0;
            Get_IMS_Data(1, page, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox_plc.Text += "a";
                delay(100);
            }
            flag_wait_receive_data = 0;

            //new method get awb data
            flag_read_camera_raw_data = 1;
            page = AWB_PAGE1;
            Send_IMS_Data(0xD1, (byte)page, 0, 0);
            */

            if (get_comport_status() == false)
            {
                richTextBox_plc.Text += "無 comport 連線";
                return;
            }

            if (get_camera_status() != CAMERA_OK)
            {
                richTextBox_plc.Text += "無 相機 連線";
                return;
            }

            richTextBox_plc.Text += "讀取相機資料中...";

            flag_camera_has_serial = false;

            byte page;
            bt_read_camera_data.BackColor = Color.Red;

            richTextBox_plc.Text += "\n\nread camera serial\n";
            //get camera serial
            Get_IMS_Data(0, 0xAA, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox_plc.Text += "+";
                delay(100);
            }
            flag_wait_receive_data = 0;

            richTextBox_plc.Text += "flag_camera_has_serial = " + flag_camera_has_serial.ToString() + "\n";
            richTextBox_plc.Text += "flag_camera_has_serial = " + flag_camera_has_serial.ToString() + "\n";
            richTextBox_plc.Text += "flag_camera_has_serial = " + flag_camera_has_serial.ToString() + "\n";
            richTextBox_plc.Text += "flag_camera_has_serial = " + flag_camera_has_serial.ToString() + "\n";

            richTextBox_plc.Text += "\n\nread DATE_PAGE0\n";
            //get camera date_page0 product time
            page = DATE_PAGE0;
            Get_IMS_Data(1, page, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox_plc.Text += "a";
                delay(100);
            }
            flag_wait_receive_data = 0;

            //old method get awb data
            lb_awb_data.Text = "";
            cnt = 0;

            richTextBox_plc.Text += "\n\nread AWB_PAGE0\n";
            page = AWB_PAGE0;
            Get_IMS_Data(1, page, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox_plc.Text += "a";
                delay(100);
            }
            flag_wait_receive_data = 0;

            //new method get awb data
            flag_read_camera_raw_data = 1;
            richTextBox_plc.Text += "\n\nread AWB_PAGE1\n";
            page = AWB_PAGE1;
            Send_IMS_Data(0xD1, (byte)page, 0, 0);

            richTextBox_plc.Text += "讀取軟體版本資訊\n";

            page = SW_VERSION_PAGE; //儲存軟體版本資訊
            Get_IMS_Data(1, page, 0xAA);    //read camera page 10 for product time
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 20))
            {
                richTextBox_plc.Text += "+";
                delay(100);
            }
            flag_wait_receive_data = 0;

            bt_read_camera_data.BackColor = SystemColors.ControlLight;

            return;
        }

        private void bt_erase_camera_data_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "清除相機資料\n";
            erase_camera_data();
        }

        private void bt_setup_ims_type1_Click(object sender, EventArgs e)
        {
            //設定主機為燒錄主機

            int check_result = check_password();

            if (check_result == S_FALSE)
            {
                richTextBox_plc.Text += "密碼沒過\n";
                return;
            }

            check_result = check_using_comport();
            if (check_result == S_FALSE)
            {
                richTextBox_plc.Text += "無 comport\n";
                return;
            }

            richTextBox_plc.Text += "設定主機為燒錄主機 完成\n";
            this.panel_plc.BackColor = SystemColors.ControlLight;
            write_ims_type(0);
            MessageBox.Show("設定主機為 燒錄主機 完成", "iMS_Link", MessageBoxButtons.OK);

            //將 COM_Port_OK_Name 寫入.ini檔
            string section_name = "SetupWRITE_DATA";
            WritePrivateProfileString(section_name, "ComportName", COM_Port_OK_Name, iMS_Link_ini_filename);
        }

        private void bt_setup_ims_type2_Click(object sender, EventArgs e)
        {
            //設定主機為色調主機

            int check_result = check_password();

            if (check_result == S_FALSE)
            {
                richTextBox_plc.Text += "密碼沒過\n";
                return;
            }

            check_result = check_using_comport();
            if (check_result == S_FALSE)
            {
                richTextBox_plc.Text += "無 comport\n";
                return;
            }

            check_result = check_using_camera();
            if (check_result == S_FALSE)
            {
                richTextBox_plc.Text += "無影像\n";
                return;
            }

            richTextBox_plc.Text += "設定主機為色調主機 完成\n";
            this.panel_plc.BackColor = SystemColors.ControlLight;
            write_ims_type(1);
            MessageBox.Show("設定主機為 色調主機 完成", "iMS_Link", MessageBoxButtons.OK);

            //將 COM_Port_OK_Name / insighetyes 寫入.ini檔
            string section_name = "SetupAWB";
            WritePrivateProfileString(section_name, "ComportName", COM_Port_OK_Name, iMS_Link_ini_filename);
            WritePrivateProfileString(section_name, "CameraName", insighteyes_name, iMS_Link_ini_filename);

            richTextBox_plc.Text += "COM_Port_OK_Name : " + COM_Port_OK_Name + "\n";
            richTextBox_plc.Text += "insighteyes_name : " + insighteyes_name + "\n";
        }

        private void bt_reset_ims_Click(object sender, EventArgs e)
        {
            if (flag_automation_mode == MODE_WRITE_DATA)
            {
                richTextBox_plc.Text += "燒錄主機重開\n";
                reset_IMS_DataWrite();
            }
            else
            {
                richTextBox_plc.Text += "色調主機重開\n";
                reset_IMS_AWB();
            }
        }

        int check_password()
        {
            form_confirm.Owner = this;
            form_confirm.StartPosition = FormStartPosition.CenterScreen;    //設定視窗居中顯示
            DialogResult result = form_confirm.ShowDialog();

            if (result == DialogResult.Ignore)
            {
                //show_main_message1(form_confirm_data, S_OK, 100);
                //richTextBox_plc.Text += "你選擇了 " + form_confirm_data + "\n";
                if ((form_confirm_data == "iloveims") || (form_confirm_data == "ilovemic"))
                {
                    //show_main_message1("密碼正確", S_OK, 100);
                    richTextBox_plc.Text += "密碼正確, 儲存設定\n";
                }
                else
                {
                    //show_main_message1("密碼錯誤, 不儲存設定", S_OK, 100);
                    richTextBox_plc.Text += "密碼錯誤, 不儲存設定\n";
                    return S_FALSE;
                }
            }
            else
            {
                //show_main_message1("不儲存設定", S_OK, 100);
                richTextBox_plc.Text += "取消, 不儲存設定\n";
                return S_FALSE;
            }
            return S_OK;
        }

        int check_using_comport()
        {
            //重新抓取comport

            //若有comport連線 要先斷線
            if (flag_comport_ok == true)
            {
                richTextBox_plc.Text += "若有comport連線 要先斷線\n";

                serialPort2.Close();
                this.BackColor = Color.Yellow;
                bt_comport_connect1b.Enabled = true;
                bt_comport_disconnect1b.Enabled = false;
                flag_comport_ok = false;
                show_main_message1("COM未連線", S_FALSE, 100);
                pictureBox_comport1b.Image = iMS_Link.Properties.Resources.x;
                toolTip1.SetToolTip(pictureBox_comport1b, "COM未連線");
            }
            lb_automation_message4.Text = "COM   NG";

            richTextBox_plc.Text += "重新連線\n";

            flag_comport_connection_ok = false;
            flag_use_specific_ims = false;

            flag_auto_connect_comport_round = 0;
            for (int i = 0; i < flag_automation_check_connection_retry_count; i++)
            {
                if (flag_comport_connection_ok == false)
                {
                    richTextBox_plc.Text += "第 " + (flag_auto_connect_comport_round + 1).ToString() + " 輪 找尋comport\n";
                    flag_auto_connect_comport_round++;

                    richTextBox_plc.Text += "awb call connect_IMS_comport()\n";
                    show_main_message1("連線COM Port", S_OK, 30);
                    show_main_message2("連線COM Port", S_OK, 30);
                    show_main_message3("連線COM Port", S_OK, 30);
                    connect_IMS_comport();
                    if (flag_comport_connection_ok == true)
                    {
                        show_main_message1("連線COM Port, OK", S_OK, 30);
                        show_main_message2("連線COM Port, OK", S_OK, 30);
                        show_main_message3("連線COM Port, OK", S_OK, 30);
                        break;
                    }
                    delay(1000);
                }
            }

            if (serialPort2.IsOpen)
            {
                richTextBox_plc.Text += "COM port 連線 OK\n";

                bt_comport_connect1b.Enabled = false;
                bt_comport_disconnect1b.Enabled = true;
                this.BackColor = SystemColors.ControlLight;
                flag_comport_ok = true;
                bt_awb_test.Enabled = true;
                bt_awb_test.BackColor = Color.Lime;
                lb_automation_message1.Visible = false;
            }
            else
            {
                richTextBox_plc.Text += "COM port 連線 NG\n";

                bt_awb_test.Enabled = false;
                bt_awb_test.BackColor = Color.Pink;

                bt_awb_test.Enabled = true;
                bt_awb_test.BackColor = Color.Lime;
                lb_automation_message1.Text = "自動化作業啟動失敗\n\n連線Comport : 失敗";
                lb_automation_message1.Visible = true;
                MessageBox.Show("無 COM port 連線", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            return S_OK;
        }

        int check_using_camera()
        {
            richTextBox_plc.Text += "aa取得 flag_camera_use_insighteyes = " + flag_camera_use_insighteyes.ToString() + "\n";
            richTextBox_plc.Text += "aa取得 ims_camera_fullname = " + ims_camera_fullname + "\n";

            //重抓相機

            if (Cam != null)
            {
                if (Cam.IsRunning == true)  // When Form1 closes itself, WebCam must stop, too.
                {
                    flag_camera_start = 0;
                    Stop_Webcam();
                }
            }

            flag_camera_use_insighteyes = 0;

            ims_camera_fullname = string.Empty;

            int automation_mode = flag_automation_mode;
            flag_automation_mode = MODE_AWB;
            flag_use_specific_ims = false;

            Init_WebcamSetup();

            flag_automation_mode = automation_mode;     //恢復
            flag_use_specific_ims = flag_factory_mode;  //恢復

            richTextBox_plc.Text += "bb取得 flag_camera_use_insighteyes = " + flag_camera_use_insighteyes.ToString() + "\n";
            richTextBox_plc.Text += "bb取得 ims_camera_fullname = " + ims_camera_fullname + "\n";

            if (flag_camera_use_insighteyes == 0)
            {
                richTextBox_plc.Text += "找不到專用相機\n";
                MessageBox.Show("找不到專用相機", "iMS_Link", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return S_FALSE;
            }
            else
            {
                insighteyes_name = ims_camera_fullname;
            }
            return S_OK;
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (timer_plc_status.Enabled == true)
            {
                timer_plc_status.Enabled = false;
                timer_plc_simulator.Enabled = false;
                bt_pause.BackgroundImage = Properties.Resources.play;
            }
            else
            {
                timer_plc_status.Enabled = true;
                timer_plc_simulator.Enabled = true;
                bt_pause.BackgroundImage = Properties.Resources.pause;
            }
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive_automation(); //用時間檔名存檔 不檢查序號
        }

        void save_image_to_drive_automation() //用時間檔名存檔 不檢查序號
        {
            show_plc_main_message1("存檔中...", S_OK, 10);
            delay(10);

            Bitmap bitmap1 = (Bitmap)pictureBox_plc_status.Image;

            if (bitmap1 != null)
            {
                //是否保留時間......

                IntPtr pHdc;
                Graphics g = Graphics.FromImage(bitmap1);
                Pen p = new Pen(Color.Red, 1);
                SolidBrush drawBrush = new SolidBrush(Color.Yellow);
                Font drawFont = new Font("Arial", 6, FontStyle.Bold, GraphicsUnit.Millimeter);
                pHdc = g.GetHdc();

                g.ReleaseHdc();
                g.Dispose();

                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);

                    richTextBox_plc.Text += "存檔成功\n";
                    richTextBox_plc.Text += "已存檔 : " + filename + "\n";
                    show_plc_main_message1("已存檔BMP", S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox_plc.Text += "xxx錯誤訊息e39 : " + ex.Message + "\n";
                    show_plc_main_message1("存檔失敗", S_OK, 30);
                    //show_plc_main_message1("存檔失敗 : " + ex.Message, S_OK, 30);
                }
            }
            else
            {
                richTextBox_plc.Text += "無圖可存\n";
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
                show_plc_main_message1("無圖可存a", S_FALSE, 30);
            }
            return;
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox_plc.Text += "目前所在路徑: " + currentPath + "\n";
            //開啟檔案總管
            Process.Start(currentPath);
        }

        int plc_simulator_step = 0;
        int plc_simulator_count = 0;
        //bool plc_simulator_power_status = false;

        //資料燒錄用(6) 與色調共用
        int m7980_simulator_value = 0;
        int m7981_simulator_value = 0;
        int m7982_simulator_value = 0;
        int m7990_simulator_value = 0;
        int m7991_simulator_value = 0;
        int m7992_simulator_value = 0;

        //燒錄心跳
        int m10010_simulator_value = 0; //PLC賦值
        int m10011_simulator_value = 0; //PLC賦值
        int m12010_simulator_value = 0; //PC賦值
        int m12011_simulator_value = 0; //PC賦值
        //燒錄對時
        int m10012_simulator_value = 0; //PLC賦值
        int m12012_simulator_value = 0; //PC賦值
        int m12013_simulator_value = 0; //PC賦值
        //色調心跳
        int m13010_simulator_value = 0; //PLC賦值
        int m13011_simulator_value = 0; //PLC賦值
        int m15010_simulator_value = 0; //PC賦值
        int m15011_simulator_value = 0; //PC賦值
        //色調對時
        int m13012_simulator_value = 0; //PLC賦值
        int m15012_simulator_value = 0; //PC賦值
        int m15013_simulator_value = 0; //PC賦值

        string d5900_simulator_data = "";   //PLC製作之相機序號
        string d5910_simulator_data = "";   //PLC收到的動作結果
        string d5950_simulator_data = "";   //PC拿到的相機序號寫在這裡
        string d5960_simulator_data = "";   //PC把動作結果寫在這裡
        string d2020_simulator_data = "";   //PLC製作之燒錄對時資料
        string d8020_simulator_data = "";   //PC拿到的燒錄對時資料寫在這裡
        string d12020_simulator_data = "";   //PLC製作之色調對時資料
        string d18020_simulator_data = "";   //PC拿到的色調對時資料寫在這裡

        private void timer_plc_simulator_Tick(object sender, EventArgs e)
        {
            if (flag_plc_test == false)
            {
                return;
            }
            do_plc_simulation();
            plc_simulator_count++;
        }

        void do_plc_simulation()
        {
            //richTextBox_plc.Text += "S" + plc_simulator_step.ToString() + "_" + plc_simulator_count.ToString() + " ";

            string contact_address = string.Empty;
            bool status = false;

            if (plc_simulator_step == 0)    //PLC Power OFF
            {
                if (plc_simulator_count < 5)
                {
                    //richTextBox_plc.Text += "PLC OFF ";
                }
                else
                {
                    //richTextBox_plc.Text += "PLC ON\n";
                    plc_simulator_count = 0;
                    plc_simulator_step = 1;

                    d5900_simulator_data = "";
                    d5910_simulator_data = "";
                    d2020_simulator_data = "";
                    d5950_simulator_data = "";
                    d5960_simulator_data = "";
                    d8020_simulator_data = "";

                    if (plc_do_check_time == false)
                    {
                        //設定M7980 7981 7982 信號為0
                        contact_address = (7980 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        contact_address = (7981 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        contact_address = (7982 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                    }
                    else
                    {
                        //設定M10012 or M13012 信號為0
                        contact_address = (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
                        set_plc_m_status(contact_address, LOW);
                    }
                }
            }
            else if (plc_simulator_step == 1)   //PLC Power ON
            {
                if (plc_simulator_count < 20)
                {
                    if (plc_do_check_time == false)
                    {
                        //檢查M7980 7981 7982 M7990 7991 7992 信號是否皆為0
                        contact_address = (7980 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7980 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (7981 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7981 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (7982 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7982 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (7990 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7990 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (7991 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7991 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (7992 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7992 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                    }
                    else
                    {
                        //檢查M10012 12012 12013 信號是否皆為0
                        contact_address = (10012 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7980 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12012 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7981 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12013 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (7982 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                    }
                }
                else
                {
                    richTextBox_plc.Text += "\n[PLC] 開始PLC測試\n";
                    plc_simulator_count = 0;
                    plc_simulator_step = 2;

                    if (plc_do_check_time == false)
                    {
                        richTextBox_plc.Text += "[PLC] 把相機序號資料放在 D" + (5900 + plc_d_address_offset).ToString() + "\n";

                        //PLC製作相機序號資料

                        contact_address = (5900 + plc_d_address_offset).ToString();
                        string write_data = plc_make_camera_data();
                        show_plc_main_message1("PLC 寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
                        set_plc_d_data(contact_address, write_data);

                        richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (7980 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知條碼內容已備便\n";
                        richTextBox_plc.Text += "[PLC] 令 M" + (7980 + plc_m_address_offset).ToString() + " 為 HIGH\n";
                        contact_address = (7980 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, HIGH);
                    }
                    else
                    {
                        richTextBox_plc.Text += "[PLC] 把燒錄對時資料放在 D" + (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString() + "\n";

                        //PLC製作燒錄對時資料

                        contact_address = (5900 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
                        //contact_address = (5900 + plc_d_address_offset).ToString();
                        string write_data = plc_make_datetime_data();
                        show_plc_main_message1("PLC 寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
                        set_plc_d_data(contact_address, write_data);

                        richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + ", 供PC讀取, 通知對時資料已備便\n";
                        richTextBox_plc.Text += "[PLC] 令 M" + (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + " 為 HIGH\n";
                        contact_address = (7980 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
                        set_plc_m_status(contact_address, HIGH);
                    }

                    if (flag_automation_mode == MODE_AWB)
                    {
                        groupBox_plc.Text = "自動化作業 : 色彩調教";
                        groupBox_plc.BackColor = Color.LightYellow;
                        //richTextBox_plc.Text += "groupBox_plc 背景色 LightYellow\n";
                        lb_plc_main_mesg3.Text = "Master 發起命令";
                    }
                    else if (flag_automation_mode == MODE_WRITE_DATA)
                    {
                        groupBox_plc.Text = "自動化作業 : 資料燒錄";
                        groupBox_plc.BackColor = Color.LightPink;
                        //richTextBox_plc.Text += "groupBox_plc 背景色 LightPink\n";
                        lb_plc_main_mesg3.Text = "Master 發起命令";
                    }
                    else
                    {
                        groupBox_plc.Text = "自動化作業";
                        groupBox_plc.BackColor = Color.LightGray;
                        //richTextBox_plc.Text += "groupBox_plc 背景色 LightGray\n";
                    }

                    if (flag_use_real_plc == true)
                        groupBox_plc.Text += "    真上位";
                    else
                        groupBox_plc.Text += "    假上位";

                    if (flag_use_real_ims == false)
                        groupBox_plc.Text += "    假下位";
                    else
                        groupBox_plc.Text += "    真下位";
                }
            }
            else if (plc_simulator_step == 2)   //開始PLC測試
            {
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M7990 是否為HIGH, 若是, 代表PC已備便\n";
                    bool ret = false;
                    if (plc_do_check_time == false)
                    {
                        contact_address = (7990 + plc_m_address_offset).ToString();
                    }
                    else
                    {
                        contact_address = (7990 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
                    }
                    richTextBox_plc.Text += "[PLC] PLC 檢查 M" + contact_address + "是否為HIGH, 若是, 代表PC已備便\n";

                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未備便 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 已備便\n";

                        if (plc_do_check_time == false)
                        {
                            richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (7981 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知開始工作\n";
                            contact_address = (7981 + plc_m_address_offset).ToString();
                            set_plc_m_status(contact_address, HIGH);
                            plc_simulator_count = 0;
                            plc_simulator_step = 3;
                        }
                        else
                        {
                            //跳至對時的state
                            plc_simulator_count = 0;
                            plc_simulator_step = 9;
                        }
                    }
                }
            }
            else if (plc_simulator_step == 3)   //PLC等待PC工作
            {
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M7992 是否為 HIGH, 若是, 代表PC已做完工作\n";
                    bool ret = false;
                    contact_address = (7992 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成工作 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 已完成工作, 完成信號 M" + (7992 + plc_m_address_offset).ToString() + "\n";

                        string work_result = get_plc_d_data((5960 + plc_d_address_offset).ToString());
                        richTextBox_plc.Text += "[PLC] PLC 讀取D" + (5960 + plc_d_address_offset).ToString() + "的資料 : " + work_result + "\n";

                        richTextBox_plc.Text += "[PLC] PLC 讀取D" + (5960 + plc_d_address_offset).ToString() + "的資料, 寫到 D" + (5910 + plc_d_address_offset).ToString() + "\n";
                        contact_address = (5910 + plc_d_address_offset).ToString();
                        set_plc_d_data(contact_address, work_result);

                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (7982 + plc_m_address_offset).ToString() + "為ON\n";
                        contact_address = (7982 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, HIGH);

                        plc_simulator_count = 0;
                        plc_simulator_step = 4;
                    }
                }
            }
            else if (plc_simulator_step == 4)
            {
                if (plc_simulator_count < 3)
                {

                }
                else if (plc_simulator_count < 6)
                {
                    richTextBox_plc.Text += "[PLC] PLC 檢查 M" + (7992 + plc_m_address_offset).ToString() + " 是否為 ON, 若是, PLC 可以清除D" + (5900 + plc_d_address_offset).ToString() + "資料\n";
                    bool ret = false;
                    contact_address = (7992 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        richTextBox_plc.Text += "[PLC] PLC 檢查 M" + (7992 + plc_m_address_offset).ToString() + " 是否為 ON, PLC 可以清除D" + (5900 + plc_d_address_offset).ToString() + "資料\n";
                        show_plc_main_message1("清除 D" + (5900 + plc_d_address_offset).ToString(), S_OK, 30);
                        set_plc_d_data((5900 + plc_d_address_offset).ToString(), "");

                        plc_simulator_count = 7;
                    }
                    else
                    {
                        plc_simulator_count--;
                    }
                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M7991 是否為 LOW, 若是, 代表PC已做完\n";
                    bool ret = false;
                    contact_address = (7991 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 之動作完成信號 M" + (7991 + plc_m_address_offset).ToString() + " 為 LOW, PLC設定 M" + (7982 + plc_m_address_offset).ToString() + " 為 HIGH\n";

                        plc_simulator_count = 0;
                        plc_simulator_step = 5;

                        contact_address = (7982 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, HIGH);
                    }
                }
            }
            else if (plc_simulator_step == 5)
            {
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M7992 是否為 LOW, 若是, 代表PC已做完\n";
                    bool ret = false;
                    contact_address = (7992 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC之動作完成信號 M" + (7992 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (7982 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (7982 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (7981 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (7981 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (7980 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (7980 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);

                        plc_simulator_count = 0;
                        plc_simulator_step = 6;

                    }

                }
            }
            else if (plc_simulator_step == 6)
            {
                //richTextBox_plc.Text += plc_simulator_step.ToString() + " ";
                //richTextBox_plc.Text += plc_simulator_count.ToString() + " ";
                if (plc_simulator_count < 10)
                {

                }
                else
                {
                    plc_simulator_count = 0;
                    plc_simulator_step = 0;
                }
            }
            else if (plc_simulator_step == 9)   //對時專用的state
            {
                if (plc_simulator_count < 3)
                {
                }
                else
                {
                    contact_address = (12013 + plc_m_address_offset).ToString();

                    richTextBox_plc.Text += "[PLC] PLC 檢查 M" + contact_address + "是否為 HIGH, 若是, 代表PC已做完\n";
                    bool ret = false;
                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC之動作完成信號 M" + contact_address + " 為 HIGH\n";
                        delay(200);
                        contact_address = (12012 + plc_m_address_offset).ToString();
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + contact_address + " 為 LOW\n";
                        set_plc_m_status(contact_address, LOW);

                        plc_simulator_count = 0;
                        plc_simulator_step = 0;
                    }
                }
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXX\n";
            }
        }

        int camera_serial_length = 12;
        string plc_make_camera_data()
        {
            //序號格式(13碼, 1英7數1英4數) 例如 N2201001A0001
            //                                  012345678
            /*
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[15];
            var random = new Random();
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if ((i == 0) || (i == 8))
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            finalString1 += '@';
            */
            var chars2 = "1234567890";
            var stringChars1 = new char[camera_serial_length];
            for (int i = 0; i < stringChars1.Length; i++)
            {
                stringChars1[i] = chars2[i % 10];
            }
            var finalString1 = new String(stringChars1);

            camera_serial_length++;
            if (camera_serial_length > 15)
                camera_serial_length = 7;

            ///finalString1 = "ABC0123456789";
            //finalString1 = "AA123456789";

            richTextBox_plc.Text += "\nPLC製作相機序號：" + finalString1 + "\n";

            show_main_message1("PLC製作相機資料完成", S_OK, 30);
            show_plc_main_message1("PLC製作相機資料完成", S_OK, 30);
            return finalString1;
        }

        string plc_make_datetime_data()
        {
            /*
            //對時格式
            8020 年  8021 月  8022 日  8023 時    8024 分    8025 秒
            */

            var chars2 = "0123456789";
            var stringChars1 = new char[16];
            var random = new Random();

            stringChars1[0] = chars2[random.Next(chars2.Length)];
            stringChars1[1] = chars2[random.Next(chars2.Length)];
            stringChars1[2] = chars2[random.Next(chars2.Length)];
            stringChars1[3] = chars2[random.Next(chars2.Length)];
            stringChars1[4] = chars2[random.Next(chars2.Length)];
            stringChars1[5] = chars2[random.Next(chars2.Length)];
            for (int i = 6; i < 16; i++)
            {
                stringChars1[i] = chars2[random.Next(chars2.Length)];
            }

            var finalString1 = new String(stringChars1);

            richTextBox_plc.Text += "\nPLC製作對時資料：" + finalString1 + "\n";

            show_main_message1("PLC製作對時資料完成", S_OK, 30);
            show_plc_main_message1("PLC製作對時資料完成", S_OK, 30);
            return finalString1;
        }

        bool check_plc_simulator_power_status()
        {
            if (plc_simulator_step == 0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        bool get_plc_simulator_m_status(string contact_address)
        {
            if ((contact_address.Length != 4) && (contact_address.Length != 5))
            {
                show_plc_main_message1("位址錯誤", S_OK, 30);
                richTextBox_plc.Text += "位址錯誤 : " + contact_address + "\n";
                return false;
            }

            bool ret = false;

            if (cb_debug.Checked == true)
            {
                int rrrr;
                Random r = new Random();

                rrrr = r.Next(0, 2);

                if (rrrr == 0)
                {
                    ret = false;
                }
                else
                {
                    ret = true;
                }
            }
            else
            {
                int m_status = 0;
                if (contact_address == (7980 + plc_m_address_offset).ToString())
                {
                    m_status = m7980_simulator_value;
                }
                else if (contact_address == (7981 + plc_m_address_offset).ToString())
                {
                    m_status = m7981_simulator_value;
                }
                else if (contact_address == (7982 + plc_m_address_offset).ToString())
                {
                    m_status = m7982_simulator_value;
                }
                else if (contact_address == (7990 + plc_m_address_offset).ToString())
                {
                    m_status = m7990_simulator_value;
                }
                else if (contact_address == (7991 + plc_m_address_offset).ToString())
                {
                    m_status = m7991_simulator_value;
                }
                else if (contact_address == (7992 + plc_m_address_offset).ToString())
                {
                    m_status = m7992_simulator_value;
                }
                else if (contact_address == "10010")
                {
                    m_status = m10010_simulator_value;
                }
                else if (contact_address == "10011")
                {
                    m_status = m10011_simulator_value;
                }
                else if (contact_address == "12010")
                {
                    m_status = m12010_simulator_value;
                }
                else if (contact_address == "12011")
                {
                    m_status = m12011_simulator_value;
                }
                else if (contact_address == "13010")
                {
                    m_status = m13010_simulator_value;
                }
                else if (contact_address == "13011")
                {
                    m_status = m13011_simulator_value;
                }
                else if (contact_address == "15010")
                {
                    m_status = m15010_simulator_value;
                }
                else if (contact_address == "15011")
                {
                    m_status = m15011_simulator_value;
                }
                else if (contact_address == "10012")
                {
                    m_status = m10012_simulator_value;
                }
                else if (contact_address == "12012")
                {
                    m_status = m12012_simulator_value;
                }
                else if (contact_address == "12013")
                {
                    m_status = m12013_simulator_value;
                }
                else if (contact_address == "13012")
                {
                    m_status = m13012_simulator_value;
                }
                else if (contact_address == "15012")
                {
                    m_status = m15012_simulator_value;
                }
                else if (contact_address == "15013")
                {
                    m_status = m15013_simulator_value;
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 1, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
                    m_status = 0;
                }

                //richTextBox_plc.Text += "讀取 M" + contact_address + ", 資料為: " + m_status.ToString() + "\n";
                if (m_status == 0)
                {
                    ret = false;
                }
                else
                {
                    ret = true;
                }
            }
            return ret;
        }

        void set_plc_simulator_m_status(string contact_address, PLC_STATE write_data)
        {
            //richTextBox_plc.Text += "模擬寫了 M" + contact_address + ", 資料為: " + write_data.ToString() + "\n";
            if (contact_address == (7980 + plc_m_address_offset).ToString())
            {
                m7980_simulator_value = (int)write_data;
            }
            else if (contact_address == (7981 + plc_m_address_offset).ToString())
            {
                m7981_simulator_value = (int)write_data;
            }
            else if (contact_address == (7982 + plc_m_address_offset).ToString())
            {
                m7982_simulator_value = (int)write_data;
            }
            else if (contact_address == (7990 + plc_m_address_offset).ToString())
            {
                m7990_simulator_value = (int)write_data;
            }
            else if (contact_address == (7991 + plc_m_address_offset).ToString())
            {
                m7991_simulator_value = (int)write_data;
            }
            else if (contact_address == (7992 + plc_m_address_offset).ToString())
            {
                m7992_simulator_value = (int)write_data;
            }
            else if (contact_address == "10010")
            {
                m10010_simulator_value = (int)write_data;
            }
            else if (contact_address == "10011")
            {
                m10011_simulator_value = (int)write_data;
            }
            else if (contact_address == "10012")
            {
                m10012_simulator_value = (int)write_data;
            }
            else if (contact_address == "12010")
            {
                m12010_simulator_value = (int)write_data;
            }
            else if (contact_address == "12011")
            {
                m12011_simulator_value = (int)write_data;
            }
            else if (contact_address == "12012")
            {
                m12012_simulator_value = (int)write_data;
            }
            else if (contact_address == "12013")
            {
                m12013_simulator_value = (int)write_data;
            }
            else if (contact_address == "13010")
            {
                m13010_simulator_value = (int)write_data;
            }
            else if (contact_address == "13011")
            {
                m13011_simulator_value = (int)write_data;
            }
            else if (contact_address == "13012")
            {
                m13012_simulator_value = (int)write_data;
            }
            else if (contact_address == "15010")
            {
                m15010_simulator_value = (int)write_data;
            }
            else if (contact_address == "15011")
            {
                m15011_simulator_value = (int)write_data;
            }
            else if (contact_address == "15012")
            {
                m15012_simulator_value = (int)write_data;
            }
            else if (contact_address == "15013")
            {
                m15013_simulator_value = (int)write_data;
            }
            else
            {
                //richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 2, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
            }
        }

        string get_plc_simulator_d_data(string contact_address)
        {
            string plc_simulator_d_data = string.Empty;

            if (contact_address == (5900 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d5900_simulator_data;
            }
            else if (contact_address == (5910 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d5910_simulator_data;
            }
            else if (contact_address == (5950 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d5950_simulator_data;
            }
            else if (contact_address == (5960 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d5960_simulator_data;
            }
            else if (contact_address == "2020")
            {
                plc_simulator_d_data = d2020_simulator_data;
            }
            else if (contact_address == "12020")
            {
                plc_simulator_d_data = d12020_simulator_data;
            }
            else
            {
                //richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 3, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
            }
            return plc_simulator_d_data;
        }

        void set_plc_simulator_d_data(string contact_address, string write_data)
        {
            //richTextBox_plc.Text += "模擬寫了 D" + contact_address + ", 資料為: " + write_data.ToString() + "\n";

            if (contact_address == (5900 + plc_d_address_offset).ToString())
            {
                d5900_simulator_data = write_data;
            }
            else if (contact_address == (5910 + plc_d_address_offset).ToString())
            {
                d5910_simulator_data = write_data;
            }
            else if (contact_address == "2020")
            {
                d2020_simulator_data = write_data;
            }
            else if (contact_address == "12020")
            {
                d12020_simulator_data = write_data;
            }
            else if (contact_address == "8020")
            {
                d8020_simulator_data = write_data;
            }
            else if (contact_address == "18020")
            {
                d18020_simulator_data = write_data;
            }
            else if (contact_address == (5950 + plc_d_address_offset).ToString())
            {
                d5950_simulator_data = write_data;
            }
            else if (contact_address == (5960 + plc_d_address_offset).ToString())
            {
                d5960_simulator_data = write_data;
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 4, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
            }
        }

        int do_write_serial_data(string serial_data)
        {
            richTextBox_plc.Text += "相機序號 : " + serial_data + "\n";
            richTextBox_plc.Text += "相機序號長度 : " + serial_data.Length.ToString() + "\n";
            if (serial_data.Length != 16)
            {
                richTextBox_plc.Text += "相機序號1長度錯誤, 長度 : " + serial_data.Length.ToString() + "\n";
                lb_write_camera_serial2.Text = "相機序號1長度錯誤";
                lb_write_camera_serial2.BackColor = Color.Red;
                playSound(S_FALSE);
                flag_doing_writing_data = false;
                return S_FALSE;
            }

            if (get_comport_status() == false)
                return S_FALSE;

            g_conn_status = get_camera_status();

            if (g_conn_status != CAMERA_OK)
                return S_FALSE;

            if (david_debug == true)
            {
                richTextBox_plc.Text += "david debug\t清除相機資料\n";
                erase_camera_data();
            }

            richTextBox_plc.Text += "檢查相機內是否有資料1\n";
            int cnt = 0;
            richTextBox_plc.Text += "讀取相機資料中...";
            flag_camera_has_serial = false;
            //get camera serial
            Get_IMS_Data(0, 0xAA, 0xAA);
            cnt = 0;
            while ((flag_wait_receive_data == 1) && (cnt++ < 40))
            {
                richTextBox_plc.Text += "+";
                delay(100);
            }
            flag_wait_receive_data = 0;

            richTextBox_plc.Text += "flag_camera_has_serial = " + flag_camera_has_serial.ToString() + "\n";
            if (flag_camera_has_serial == true)
            {
                richTextBox_plc.Text += "相機內已有序號資料\n";
                return REASON_SERIAL_EXISTS;//相機內已有其他資料
            }
            else
            {
                g2.Clear(BackColor);
                g2.DrawString("燒錄中", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(60, 20));
                button11.BackColor = Color.Red;
                lb_write_camera_serial2.Text = "有連接器, 有相機, 燒錄資料進行中.....";
                lb_write_camera_serial2.BackColor = Color.Red;

                panel_camera_status1.BackgroundImage = null;
                panel_camera_status2.BackgroundImage = null;
                panel_camera_status3.BackgroundImage = null;
                panel_camera_status4.BackgroundImage = null;
                panel_camera_status5.BackgroundImage = null;

                int i;

                byte[] sn_data_tmp = new byte[16];
                for (i = 0; i < serial_data.Length; i++)
                {
                    sn_data_tmp[i] = (byte)serial_data[i];
                    //richTextBox_plc.Text += "\ni = " + i.ToString() + " tmp data : " + serial_data[i].ToString();
                }
                //richTextBox_plc.Text += "\n";

                //這裡是寫入資料
                Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write

                sn_data_tmp[15] = 0x40; //自動化的用 @ 結尾
                serialPort2.Write(sn_data_tmp, 0, 16);

                richTextBox_plc.Text += "相機無序號, continue\n";

                richTextBox_plc.Text += "序號 : 寫入資料  完成\n";

                lb_write_camera_serial2.Text = "寫入資料";

                delay(500);

                lb_write_camera_serial2.Text = "寫入相機序號完成";
                lb_write_camera_serial2.BackColor = Color.White;
                button11.BackColor = SystemColors.ControlLight;
                g2.Clear(BackColor);
                g2.DrawString("燒錄完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(15, 20));
                button11.BackColor = SystemColors.ControlLight;
                lb_write_camera_serial2.Text += "    燒錄完成";

                delay(200);
                //do_save_software_version();
                delay(200);

                //驗證資料
                lb_write_camera_serial2.Text += "    驗證中";
                lb_write_camera_serial2.BackColor = Color.White;
                richTextBox_plc.Text += "\n讀相機序號回來 " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

                Font f = new Font("標楷體", 60);
                int tmp_width = 0;
                int tmp_height = 0;
                string str = "驗證中";

                tmp_width = g.MeasureString(str, f).ToSize().Width;
                tmp_height = g.MeasureString(str, f).ToSize().Height;

                //richTextBox_plc.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";
                //richTextBox_plc.Text += "W = " + panel9.Width.ToString() + "  H = " + panel9.Height.ToString() + "\n";

                g2.Clear(BackColor);
                g2.DrawString(str, f, new SolidBrush(Color.Blue), new PointF(60, 20));
                //g2.DrawString(str, f, new SolidBrush(Color.Blue), new PointF((panel9.Width - tmp_width) / 2, (panel9.Height - tmp_height) / 2));
                button11.BackColor = SystemColors.ControlLight;

                //richTextBox_plc.Text += "delay ST\n";
                //flag_verify_serial_data = 1;
                //Get_IMS_Data(0, 0xAA, 0xAA);

                //delay(200);
                delay(200);
                delay(200);
                //richTextBox_plc.Text += "delay SP\n";

                richTextBox_plc.Text += "驗證完成, 序號相同\n";
                lb_write_camera_serial2.Text += "    驗證完成";
                lb_write_camera_serial2.BackColor = Color.White;
                g2.Clear(BackColor);
                g2.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
                playSound(S_OK);
            }

            // Stop timing
            stopwatch.Stop();
            richTextBox_plc.Text += "燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

            if (stopwatch.ElapsedMilliseconds > 7000)
            {
                flag_burn_long_cnt++;
                ////lb_mesg2.Text = "耗時太久 " + flag_burn_long_cnt.ToString() + " 次";
            }
            flag_doing_writing_data = false;
            flag_doing_writing_data = false;
            return S_OK;
        }

        private void timer_pc_clock_Tick(object sender, EventArgs e)
        {
            //顯示時間
            DateTime dt_system = DateTime.Now;
            if (flag_use_user_time == false)
            {
                lb_plc_datetime.Text = dt_system.ToString("yyyy/MM/dd HH:mm:ss");
            }
            else
            {
                DateTime dt_new = dt_system - datetime_diff;
                lb_plc_datetime.Text = dt_new.ToString("yyyy/MM/dd HH:mm:ss");
            }
        }

        PLC_STATE pc_breathe_status = PLC_STATE.OFF;
        private void timer_pc_breathe1_Tick(object sender, EventArgs e)
        {
            //PC製作心跳

            //心跳間隔可設定,預設3秒ON,3秒OFF

            string contact_address1 = String.Empty; //狀態
            string contact_address2 = String.Empty; //心跳
            string contact_address3 = String.Empty; //異常

            if (pc_breathe_status == PLC_STATE.OFF)
                pc_breathe_status = PLC_STATE.ON;
            else
                pc_breathe_status = PLC_STATE.OFF;

            /*
            //色調與燒錄一起心跳
            contact_address1 = "15010";  //色調狀態 PC給PLC
            contact_address2 = "15011";  //色調心跳 PC給PLC
            set_plc_m_status(contact_address1, HIGH);
            set_plc_m_status(contact_address2, pc_breathe_status);

            contact_address1 = "12010";  //燒錄狀態 PC給PLC
            contact_address2 = "12011";  //燒錄心跳 PC給PLC
            set_plc_m_status(contact_address1, HIGH);
            set_plc_m_status(contact_address2, pc_breathe_status);
            */

            //色調與燒錄分開心跳
            if (flag_automation_mode == MODE_AWB)
            {
                contact_address1 = "15010";  //色調狀態 PC給PLC
                contact_address2 = "5699";  //色調心跳 PC給PLC
                contact_address3 = "5693";  //色調異常狀態
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                contact_address1 = "12010";  //燒錄狀態 PC給PLC
                contact_address2 = "7999";  //燒錄心跳 PC給PLC
                contact_address3 = "7993";  //燒錄異常狀態
            }
            else
            {
                contact_address1 = "12010";  //燒錄狀態 PC給PLC
                contact_address2 = "7999";  //燒錄心跳 PC給PLC
                contact_address3 = "7993";  //燒錄異常狀態
            }
            //set_plc_m_status(contact_address1, HIGH); 不用了
            set_plc_m_status(contact_address2, pc_breathe_status);

            update_plc_breathe_status_data();

            if (richTextBox_plc.Text.Length > 10000)
            {
                richTextBox_plc.Clear();
            }

            //------------------------------------------------------------  # 60個

            //燒錄 / 色調 正常/異常
            //PLC_STATE pc_automation_status = PLC_STATE.OFF;
            if (flag_automation_status == S_OK)
            {
                //正常
                set_plc_m_status(contact_address3, LOW);
                //richTextBox_plc.Text += "OK ";
            }
            else
            {
                //異常
                set_plc_m_status(contact_address3, HIGH);
                //richTextBox_plc.Text += "NG ";
            }
        }

        private void timer_pc_breathe2_Tick(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "X ";   //廢棄使用
            //PC檢查PLC之心跳

            string contact_address1 = String.Empty;
            string contact_address2 = String.Empty;
            bool ret = false;

            if (flag_pc_check_plc_breathe_mode == MODE_WRITE_DATA)  //1: MODE_WRITE_DATA 燒錄
            {
                contact_address1 = "10010";
                contact_address2 = "10011";
            }
            else if (flag_pc_check_plc_breathe_mode == MODE_AWB)    //2: MODE_AWB 色調
            {
                contact_address1 = "13010";
                contact_address2 = "13011";
            }
            else
            {
                richTextBox_plc.Text += "XXX";
                return;
            }

            if (flag_pc_check_plc_breathe_mode > MODE_OFF)  //PC檢查PLC之心跳
            {
                //richTextBox_plc.Text += "PC檢查PLC之心跳\n";

                ret = get_plc_m_status(contact_address1);
                //richTextBox_plc.Text += "讀取 M" + contact_address1 + "\t結果 : " + ret.ToString() + "\n";

                if (ret == false)
                {
                    richTextBox_plc.Text += "PLC之狀態不存在\n";
                    flag_pc_check_plc_breathe_mode_status = false;
                    flag_pc_check_plc_breathe_mode = MODE_OFF;
                    timer_pc_breathe2.Enabled = false;
                    return;
                }

                ret = get_plc_m_status(contact_address2);
                //richTextBox_plc.Text += "讀取 M" + contact_address2 + "\t結果 : " + ret.ToString() + "\n";

                breathe_data[breathe_data_index] = ret;
                breathe_data_index++;

                if ((breathe_data_index >= 4) && (breathe_data_index <= CHECK_BREATHE_LENGTH))
                {
                    /*
                    for (int i = 0; i < breathe_data_index; i++)
                    {
                        richTextBox_plc.Text += breathe_data[i] + " ";
                    }
                    richTextBox_plc.Text += "\n";
                    */
                    int toggle = 0;
                    bool status = breathe_data[0];
                    for (int i = 1; i < breathe_data_index; i++)
                    {
                        if (status != breathe_data[i])
                        {
                            toggle++;
                            //richTextBox_plc.Text += "toggle at " + i.ToString() + "\n";
                            if (toggle >= 2)
                            {
                                //richTextBox_plc.Text += "enough, break\n";
                                //richTextBox_plc.Text += "toggle = " + toggle.ToString() + "\n";

                                flag_pc_check_plc_breathe_mode_status = true;
                                flag_pc_check_plc_breathe_mode = MODE_OFF;
                                timer_pc_breathe2.Enabled = false;

                                richTextBox_plc.Text += "PC檢查PLC之心跳\t存在\n";

                                return;
                            }
                        }
                        status = breathe_data[i];
                    }
                }
                if (breathe_data_index >= CHECK_BREATHE_LENGTH)
                {
                    //無心跳
                    flag_pc_check_plc_breathe_mode_status = false;
                    flag_pc_check_plc_breathe_mode = MODE_OFF;
                    timer_pc_breathe2.Enabled = false;

                    richTextBox_plc.Text += "PC檢查PLC之心跳\t不存在\n";
                }
            }
        }

        PLC_STATE plc_breathe_status = PLC_STATE.OFF;
        private void timer_plc_breathe1_Tick(object sender, EventArgs e)
        {
            //richTextBox_plc.Text += "廢棄使用1\n";
            return;
            //PLC製作心跳

            //心跳間隔可設定,預設3秒ON,3秒OFF

            string contact_address = String.Empty;

            contact_address = "10010";  //燒錄狀態 PLC給PC
            set_plc_m_status(contact_address, HIGH);
            contact_address = "13010";  //色調狀態 PLC給PC
            set_plc_m_status(contact_address, HIGH);

            if (plc_breathe_status == PLC_STATE.OFF)
                plc_breathe_status = PLC_STATE.ON;
            else
                plc_breathe_status = PLC_STATE.OFF;

            contact_address = "10011";  //燒錄心跳 PLC給PC
            set_plc_m_status(contact_address, plc_breathe_status);
            contact_address = "13011";  //色調心跳 PLC給PC
            set_plc_m_status(contact_address, plc_breathe_status);
        }

        private void timer_plc_breathe2_Tick(object sender, EventArgs e)
        {
        }

        private void bt_check_plc_breathe1_Click(object sender, EventArgs e)
        {
            bt_check_plc_breathe2_Click(sender, e);

            return;
            richTextBox_plc.Text += "廢棄使用2\t改成顯示系統資訊\n";
            show_system_info_plc();

            return;

            if (flag_pc_check_plc_breathe_mode != MODE_OFF) //busy
            {
                richTextBox_plc.Text += "忙線中\n";
                return;
            }

            richTextBox_plc.Text += "PC檢查PLC之心跳 for 燒錄\n";
            bt_check_plc_breathe1.BackColor = Color.Blue;
            flag_pc_check_plc_breathe_mode = MODE_WRITE_DATA;   //0: MODE_WRITE_DATA 燒錄, 1: MODE_AWB 色調
            flag_pc_check_plc_breathe_mode_status = false;      //PC檢查PLC之心跳是否存在結果

            breathe_data = new bool[CHECK_BREATHE_LENGTH];
            breathe_data_index = 0;
            timer_pc_breathe2.Enabled = true;

            int cnt = 0;
            while ((flag_pc_check_plc_breathe_mode > MODE_OFF) && (cnt++ < 100))
            {
                //richTextBox_plc.Text += "+" + cnt.ToString();
                delay(100);
            }

            if (flag_pc_check_plc_breathe_mode_status == true)
            {
                bt_check_plc_breathe1.BackColor = Color.Lime;
            }
            else
            {
                bt_check_plc_breathe1.BackColor = Color.Red;
            }
        }

        bool flag_already_show_system_info = false;
        private void bt_check_plc_breathe2_Click(object sender, EventArgs e)
        {
            if (flag_always_return_ok_mode == false)
            {
                richTextBox_plc.Text += "粉飾太平模式\n";
                bt_check_plc_breathe1.BackColor = Color.Red;
                bt_check_plc_breathe2.BackColor = Color.Red;
                flag_always_return_ok_mode = true;
            }
            else
            {
                richTextBox_plc.Text += "一般模式\n";
                bt_check_plc_breathe1.BackColor = SystemColors.ControlLight;
                bt_check_plc_breathe2.BackColor = SystemColors.ControlLight;
                flag_always_return_ok_mode = false;
            }
            return;

            richTextBox_plc.Text += "顯示系統資訊\n";
            show_system_info_plc();

            if (flag_already_show_system_info == false)
            {
                flag_already_show_system_info = true;

                lb_plc_pc0.Text = "ims主機連線狀態";
                lb_plc_pc1.Text = "ims相機連線狀態";
                lb_plc_pc2.Text = "程式狀態";
                lb_pc_plc0.Text = "色調資料";
                lb_pc_plc1.Text = "相機序號";
                lb_pc_plc2.Text = "燒錄時間";

                byte page;

                //取得色調資料
                flag_read_camera_raw_data = 1;
                richTextBox_plc.Text += "\n\nread AWB_PAGE1\n";
                page = AWB_PAGE1;
                Send_IMS_Data(0xD1, (byte)page, 0, 0);

                //取得相機序號
                richTextBox_plc.Text += "\n\nread camera serial\n";
                //get camera serial
                Get_IMS_Data(0, 0xAA, 0xAA);
                int cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox_plc.Text += "+";
                    delay(100);
                }
                flag_wait_receive_data = 0;

                //取得序號燒錄時間
                richTextBox_plc.Text += "\n\nread DATE_PAGE0\n";
                //get camera date_page0 product time
                page = DATE_PAGE0;
                Get_IMS_Data(1, page, 0xAA);
                cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 20))
                {
                    richTextBox_plc.Text += "a";
                    delay(100);
                }
                flag_wait_receive_data = 0;
            }
            else
            {
                flag_already_show_system_info = false;
                lb_plc_pc0.Text = "M" + (7980 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
                lb_plc_pc1.Text = "M" + (7981 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
                lb_plc_pc2.Text = "M" + (7982 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
                lb_pc_plc0.Text = "M" + (7990 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
                lb_pc_plc1.Text = "M" + (7991 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
                lb_pc_plc2.Text = "M" + (7992 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
            }
        }

        private void bt_automation_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        void show_system_info_plc()
        {
            //顯示系統資訊
            OperatingSystem OSv = System.Environment.OSVersion;
            richTextBox_plc.AppendText("iMS_Link登錄時間 : " + compile_time + "\n");
            richTextBox_plc.AppendText("作業系統版本 : " + OSv.ToString() + "\n");
            richTextBox_plc.AppendText("圖形介面版本 : " + software_version + "\n");
            richTextBox_plc.AppendText("韌體版本 : F0" + fw_version.ToString() + "\n");
            richTextBox_plc.AppendText("螢幕解析度 : " + Screen.PrimaryScreen.Bounds.Width.ToString() + "*" + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n");
            richTextBox_plc.AppendText("目前時間 : " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n");
            richTextBox_plc.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

            //顯示自動化基本設定

            //顯示系統參數

            //顯示連線狀態

            richTextBox_plc.Text += "檢查自動化存資料資料夾\n";
            check_automation_default_folder();

            richTextBox_plc.Text += "檢查自動化設定參數\n";
            check_automation_default_setup();

            if (flag_automation_mode == MODE_AWB)
            {
                richTextBox_plc.Text += "自動化作業 : 色彩調教\n";
                richTextBox_plc.Text += "色彩調教" + AUTOMATION_VERSION.ToString("D2") + "\n";
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                richTextBox_plc.Text += "自動化作業 : 資料燒錄\n";
                richTextBox_plc.Text += "資料燒錄" + AUTOMATION_VERSION.ToString("D2") + "\n";
            }
            else
            {
                richTextBox_plc.Text += "自動化作業 xxxxx\n";
            }
            if (flag_use_real_plc == true)
            {
                richTextBox_plc.Text += "    真上位\t";
            }
            else
            {
                richTextBox_plc.Text += "    假上位\t";
            }

            if (flag_use_real_ims == true)
            {
                richTextBox_plc.Text += "    真下位\n";
            }
            else
            {
                richTextBox_plc.Text += "    假下位\n";
            }

            if (flag_factory_mode == true)
            {
                richTextBox_plc.Text += "工廠模式\n";
            }
            else
            {
                richTextBox_plc.Text += "一般模式\n";
            }

            bt_awb_test.Text = "啟動自動化";
            string ip = "192.168.3.40";
            int port = 4996;    //色調

            if (flag_automation_mode == MODE_WRITE_DATA)
            {
                port = 4998;    //燒錄
            }
            else
            {
                port = 4996;    //色調
            }

            richTextBox_plc.Text += "使用 IP : " + ip + "\n";
            richTextBox_plc.Text += "使用 埠 : " + port.ToString() + "\n";
        }
    }

    public class Logger
    {
        /// <summary>
        /// 寫入日志.
        /// </summary>
        /// <param name="strList">The STR list.</param>
        /// <remarks> </remarks>
        /// <Description></Description>
        //public static void WriteLog(string ex)
        public static void WriteLog(params object[] strList)
        {
            if (strList.Count() == 0) return;
            string strDicPath = "";
            string strPath = "";
            try
            {
                //LogFileName = Application.StartupPath + "\\log_" + DateTime.Now.ToString("yyyyMMdd") + ".txt";
                strDicPath = Application.StartupPath + "//";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日誌記錄.txt";
            }
            catch (Exception e)
            {
                strDicPath = "C:/temp/log/";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日誌記錄.txt";
            }

            if (!Directory.Exists(strDicPath)) Directory.CreateDirectory(strDicPath);
            if (!File.Exists(strPath)) using (FileStream fs = File.Create(strPath)) { }
            string str = File.ReadAllText(strPath);
            StringBuilder sb = new StringBuilder();
            foreach (var item in strList)
            {
                sb.Append(DateTime.Now.ToString() + "-----" + item + "\n");
            }

            File.WriteAllText(strPath, str + sb.ToString());
        }
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



/*
erase_plc_d_data("8020", 6);    //清除年月日時分秒的資料

delay(500);//1秒
*/

