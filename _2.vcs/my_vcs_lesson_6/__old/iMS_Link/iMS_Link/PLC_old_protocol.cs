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

using iMS_Link.PLC_Communication;

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
        private const int MODE_OFF = 0;
        private const int MODE_WRITE_DATA = 1;
        private const int MODE_WRITE_DATA_CHECK_TIME = 2;
        private const int MODE_AWB = 3;
        private const int MODE_AWB_CHECK_TIME = 4;
        private const int OFFSET_M_WRITE_DATA = 0;
        private const int OFFSET_M_AWB = 3000;
        private const int OFFSET_M_CHECK_TIME = 12;
        private const int OFFSET_D_WRITE_DATA = 0;
        private const int OFFSET_D_AWB = 10000;
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
        private const int PLC_BTN_WIDTH1 = 80;
        private const int PLC_BTN_HEIGHT1 = 60;
        private const int PLC_BTN_WIDTH2 = 50;
        private const int PLC_BTN_HEIGHT2 = 50;
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
        Button bt_plc_test = new Button();
        Button bt_plc_test_break = new Button();
        Button bt_check_connection = new Button();
        Button bt_read_camera_data = new Button();
        Button bt_erase_camera_data = new Button();
        Button bt_check_plc_breathe1 = new Button();
        Button bt_check_plc_breathe2 = new Button();
        Button bt_automation_setup = new Button();
        Button bt_automation_exit = new Button();
        CheckBox cb_debug = new CheckBox();
        CheckBox cb_test_plc = new CheckBox();
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
        Button bt_open_folder = new Button();
        Button bt_save = new Button();
        Button bt_pause = new Button();
        PictureBox pbx_m10000 = new PictureBox();
        PictureBox pbx_m10001 = new PictureBox();
        PictureBox pbx_m10002 = new PictureBox();
        PictureBox pbx_m12000 = new PictureBox();
        PictureBox pbx_m12001 = new PictureBox();
        PictureBox pbx_m12002 = new PictureBox();
        PictureBox pbx_plc_status = new PictureBox();
        PictureBox pictureBox_plc_status = new PictureBox();
        PictureBox pbx_connection1 = new PictureBox();
        PictureBox pbx_connection2 = new PictureBox();
        PictureBox pbx_connection3 = new PictureBox();

        Button bt_copy_to_clipboard = new Button();
        Button bt_plc_clear = new Button();
        RichTextBox richTextBox_plc = new RichTextBox();
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
        int flag_plc_test_count = 0;

        Font f1 = new Font("新細明體", 14); //PLC m1XXXXX 暫存器內容
        Font f2 = new Font("Arial", 16.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0))); //main message
        Font f3 = new Font("標楷體", 15);
        Font f4 = new Font("Arial", 20.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0))); //main message

        bool flag_use_user_time = false;
        DateTime datetime_user = DateTime.Now;
        TimeSpan datetime_diff;

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
            richTextBox_plc.Location = new Point(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER, BORDER);
            richTextBox_plc.Size = new Size(PLC_RTB_WIDTH, PLC_RTB_HEIGHT);
            this.panel_plc.Controls.Add(richTextBox_plc);

            lb_plc_command_type.AutoSize = true;
            lb_plc_command_type.Name = "lb_plc_command_type";
            lb_plc_command_type.Text = "";
            lb_plc_command_type.Font = f2;
            lb_plc_command_type.ForeColor = Color.Red;
            lb_plc_command_type.Size = new System.Drawing.Size(78, 24);
            lb_plc_command_type.Location = new Point(PLC_PANEL_WIDTH - BORDER - 115, BORDER + 5);
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

            bt_copy_to_clipboard.Width = PLC_BTN_WIDTH2;
            bt_copy_to_clipboard.Height = PLC_BTN_HEIGHT2;
            bt_copy_to_clipboard.Text = "";
            bt_copy_to_clipboard.Name = "bt_copy_to_clipboard";
            bt_copy_to_clipboard.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_copy_to_clipboard.Size.Width * 2, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_copy_to_clipboard.Size.Height);
            // 加入按鈕事件
            //bt_copy_to_clipboard.Click += new EventHandler(bt_copy_to_clipboard_Click);   //same
            bt_copy_to_clipboard.Click += bt_copy_to_clipboard_Click;
            this.panel_plc.Controls.Add(bt_copy_to_clipboard);     // 將控件加入表單
            bt_copy_to_clipboard.BringToFront();

            // 實例化按鈕
            bt_plc_clear.Width = PLC_BTN_WIDTH2;
            bt_plc_clear.Height = PLC_BTN_HEIGHT2;
            bt_plc_clear.Text = "Clear";
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
            int dx = PLC_BTN_WIDTH1 + 3;

            // 實例化按鈕
            bt_plc_test.Width = PLC_BTN_WIDTH1;
            bt_plc_test.Height = PLC_BTN_HEIGHT1;
            bt_plc_test.Text = "啟動\n自動化作業";
            bt_plc_test.Name = "bt_plc_test";
            bt_plc_test.Location = new Point(x_st + dx * 0, y_st);
            // 加入按鈕事件
            //bt_plc_test.Click += new EventHandler(bt_plc_test_Click);   //same
            bt_plc_test.Click += bt_plc_test_Click;
            this.groupBox_plc.Controls.Add(bt_plc_test);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test_break.Width = PLC_BTN_WIDTH1;
            bt_plc_test_break.Height = PLC_BTN_HEIGHT1;
            bt_plc_test_break.Text = "關閉\n自動化作業";
            bt_plc_test_break.Name = "bt_plc_test_break";
            bt_plc_test_break.Location = new Point(x_st + dx * 1, y_st);
            // 加入按鈕事件
            //bt_plc_test_break.Click += new EventHandler(bt_plc_test_break_Click);   //same
            bt_plc_test_break.Click += bt_plc_test_break_Click;
            bt_plc_test_break.MouseDown += bt_plc_test_break_MouseDown;
            this.groupBox_plc.Controls.Add(bt_plc_test_break);     // 將控件加入表單

            // 實例化按鈕
            bt_check_connection.Width = PLC_BTN_WIDTH1;
            bt_check_connection.Height = PLC_BTN_HEIGHT1;
            bt_check_connection.Text = "檢查\n連線狀態";
            bt_check_connection.Name = "bt_check_connection";
            bt_check_connection.Location = new Point(x_st + dx * 2, y_st);
            // 加入按鈕事件
            //bt_check_connection.Click += new EventHandler(bt_check_connection_Click);   //same
            bt_check_connection.Click += bt_check_connection_Click;
            this.groupBox_plc.Controls.Add(bt_check_connection);     // 將控件加入表單

            // 實例化按鈕
            bt_read_camera_data.Width = PLC_BTN_WIDTH1;
            bt_read_camera_data.Height = PLC_BTN_HEIGHT1;
            bt_read_camera_data.Text = "讀取\n相機資料";
            bt_read_camera_data.Name = "bt_read_camera_data";
            bt_read_camera_data.Location = new Point(x_st + dx * 3, y_st);
            // 加入按鈕事件
            //bt_read_camera_data.Click += new EventHandler(bt_read_camera_data_Click);   //same
            bt_read_camera_data.Click += bt_read_camera_data_Click;
            this.groupBox_plc.Controls.Add(bt_read_camera_data);     // 將控件加入表單

            // 實例化按鈕
            bt_erase_camera_data.Width = PLC_BTN_WIDTH1;
            bt_erase_camera_data.Height = PLC_BTN_HEIGHT1;
            bt_erase_camera_data.Text = "清除\n相機資料";
            bt_erase_camera_data.Name = "bt_erase_camera_data";
            bt_erase_camera_data.Location = new Point(x_st + dx * 4, y_st);
            // 加入按鈕事件
            //bt_erase_camera_data.Click += new EventHandler(bt_erase_camera_data_Click);   //same
            bt_erase_camera_data.Click += bt_erase_camera_data_Click;
            this.groupBox_plc.Controls.Add(bt_erase_camera_data);     // 將控件加入表單

            if (flag_automation_mode == MODE_AWB)
            {
                // 實例化按鈕
                bt_check_plc_breathe2.Width = PLC_BTN_WIDTH2;
                bt_check_plc_breathe2.Height = PLC_BTN_HEIGHT2;
                bt_check_plc_breathe2.Text = "色調\n心跳";
                bt_check_plc_breathe2.Name = "bt_check_plc_breathe2";
                //bt_check_plc_breathe2.Location = new Point(x_st + dx * 5 - 2 + 48, y_st - 8);
                bt_check_plc_breathe2.Location = new Point(x_st + dx * 5 - 4, y_st - 8);
                // 加入按鈕事件
                //bt_check_plc_breathe2.Click += new EventHandler(bt_check_plc_breathe2_Click);   //same
                bt_check_plc_breathe2.Click += bt_check_plc_breathe2_Click;
                this.groupBox_plc.Controls.Add(bt_check_plc_breathe2);     // 將控件加入表單

            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                // 實例化按鈕
                bt_check_plc_breathe1.Width = PLC_BTN_WIDTH2;
                bt_check_plc_breathe1.Height = PLC_BTN_HEIGHT2;
                bt_check_plc_breathe1.Text = "燒錄\n心跳";
                bt_check_plc_breathe1.Name = "bt_check_plc_breathe1";
                bt_check_plc_breathe1.Location = new Point(x_st + dx * 5 - 4, y_st - 8);
                // 加入按鈕事件
                //bt_check_plc_breathe1.Click += new EventHandler(bt_check_plc_breathe1_Click);   //same
                bt_check_plc_breathe1.Click += bt_check_plc_breathe1_Click;
                this.groupBox_plc.Controls.Add(bt_check_plc_breathe1);     // 將控件加入表單
            }
            else
            {
            }

            // 實例化按鈕
            bt_automation_setup.Width = PLC_BTN_WIDTH2;
            bt_automation_setup.Height = PLC_BTN_HEIGHT2;
            bt_automation_setup.Text = "";
            bt_automation_setup.Name = "bt_automation_setup";
            bt_automation_setup.BackgroundImageLayout = ImageLayout.Zoom;
            bt_automation_setup.BackgroundImage = iMS_Link.Properties.Resources.setup;
            bt_automation_setup.Location = new Point(x_st + dx * 6 - 35, y_st - 8);
            // 加入按鈕事件
            //bt_automation_setup.Click += new EventHandler(bt_automation_setup_Click);   //same
            bt_automation_setup.Click += bt_automation_setup_Click;
            this.groupBox_plc.Controls.Add(bt_automation_setup);     // 將控件加入表單

            bt_automation_exit.Width = PLC_BTN_WIDTH2;
            bt_automation_exit.Height = PLC_BTN_HEIGHT2;
            bt_automation_exit.Text = "";
            bt_automation_exit.Name = "bt_automation_exit";
            bt_automation_exit.BackgroundImageLayout = ImageLayout.Zoom;
            bt_automation_exit.BackgroundImage = iMS_Link.Properties.Resources.power;
            bt_automation_exit.Location = new Point(x_st + dx * 6 + 18, y_st - 8);
            // 加入按鈕事件
            //bt_automation_exit.Click += new EventHandler(bt_automation_exit_Click);   //same
            bt_automation_exit.Click += bt_automation_exit_Click;
            this.groupBox_plc.Controls.Add(bt_automation_exit);     // 將控件加入表單

            cb_debug.Location = new Point(x_st + dx * 5, y_st + PLC_BTN_HEIGHT1 - 16);
            cb_debug.Name = "cb_debug";
            cb_debug.Text = "Debug";
            cb_debug.Size = new Size(55, 16);
            this.groupBox_plc.Controls.Add(cb_debug);     // 將控件加入表單

            cb_test_plc.Location = new Point(x_st + dx * 6 - 20, y_st + PLC_BTN_HEIGHT1 - 16);
            cb_test_plc.Name = "cb_test_plc";
            cb_test_plc.Text = "測試PLC";
            cb_test_plc.Size = new Size(80, 16);
            cb_test_plc.CheckedChanged += cb_test_plc_CheckedChanged;	// 加入事件
            this.groupBox_plc.Controls.Add(cb_test_plc);     // 將控件加入表單

            lb_plc_main_mesg1.AutoSize = true;
            lb_plc_main_mesg1.Name = "lb_plc_main_mesg1";
            lb_plc_main_mesg1.Text = "";
            lb_plc_main_mesg1.Font = f2;
            lb_plc_main_mesg1.ForeColor = Color.Red;
            lb_plc_main_mesg1.Size = new System.Drawing.Size(78, 24);
            lb_plc_main_mesg1.Location = new Point(x_st + dx * 6 + 15 + 55, y_st + 15);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg1);     // 將控件加入表單

            lb_plc_main_mesg2.AutoSize = true;
            lb_plc_main_mesg2.Name = "lb_plc_main_mesg2";
            lb_plc_main_mesg2.Text = "";
            lb_plc_main_mesg2.Font = f2;
            lb_plc_main_mesg2.ForeColor = Color.Red;
            lb_plc_main_mesg2.Size = new System.Drawing.Size(138, 44);
            lb_plc_main_mesg2.Location = new Point(x_st + dx * 6 + 15 + 55, y_st + 38);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg2);     // 將控件加入表單

            lb_plc_main_mesg3.AutoSize = true;
            lb_plc_main_mesg3.Name = "lb_plc_main_mesg3";
            lb_plc_main_mesg3.Text = "";
            lb_plc_main_mesg3.BackColor = Color.Silver;
            lb_plc_main_mesg3.Font = f2;
            lb_plc_main_mesg3.ForeColor = Color.Red;
            lb_plc_main_mesg3.Size = new System.Drawing.Size(160, 44);
            lb_plc_main_mesg3.Location = new Point(x_st + dx * 9 + 10, y_st + 68);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg3);     // 將控件加入表單
            lb_plc_main_mesg3.BringToFront();

            lb_plc_datetime.AutoSize = true;
            lb_plc_datetime.Name = "lb_plc_datetime";
            lb_plc_datetime.Text = "";
            lb_plc_datetime.BackColor = Color.Silver;
            lb_plc_datetime.Font = f4;
            lb_plc_datetime.ForeColor = Color.Yellow;
            lb_plc_datetime.Size = new System.Drawing.Size(160, 44);
            lb_plc_datetime.Location = new Point(x_st + dx * 9 - 36, y_st - 22);
            this.groupBox_plc.Controls.Add(lb_plc_datetime);     // 將控件加入表單
            lb_plc_datetime.BringToFront();

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
            bt_open_folder.Width = PLC_BTN_WIDTH2;
            bt_open_folder.Height = PLC_BTN_HEIGHT2;
            bt_open_folder.Text = "";
            bt_open_folder.Name = "bt_open_folder";
            // 加入按鈕事件
            //bt_open_folder.Click += new EventHandler(bt_open_folder_Click);   //same
            bt_open_folder.Click += bt_open_folder_Click;

            // 實例化按鈕
            bt_save.Width = PLC_BTN_WIDTH2;
            bt_save.Height = PLC_BTN_HEIGHT2;
            bt_save.Text = "";
            bt_save.Name = "bt_save";
            // 加入按鈕事件
            //bt_save.Click += new EventHandler(bt_save_Click);   //same
            bt_save.Click += bt_save_Click;

            // 實例化按鈕
            bt_pause.Width = PLC_BTN_WIDTH2;
            bt_pause.Height = PLC_BTN_HEIGHT2;
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
            pbx_m10000.Size = new Size(w, h);
            pbx_m10001.Size = new Size(w, h);
            pbx_m10002.Size = new Size(w, h);
            pbx_m12000.Size = new Size(w, h);
            pbx_m12001.Size = new Size(w, h);
            pbx_m12002.Size = new Size(w, h);
            pbx_m10000.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 5);
            pbx_m10001.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 5);
            pbx_m10002.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 5);
            pbx_m12000.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 5);
            pbx_m12001.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 5);
            pbx_m12002.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 5);
            pbx_m10000.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10001.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10002.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12000.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12001.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m12002.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
            pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;

            x_st = 40;
            lb_plc_pc0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_plc_pc1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_plc_pc2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_plc_pc3a.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_plc_pc4a.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_read_write_plc.Location = new Point(x_st + dx * 0 + 220, y_st + dy * 5 - 5);

            lb_plc_pc3b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 3);
            lb_plc_pc4b.Location = new Point(x_st + dx * 0 + 160, y_st + dy * 4);
            lb_pc_plc0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_pc_plc1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_pc_plc2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_pc_plc3a.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            lb_pc_plc4a.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            lb_pc_plc3b.Location = new Point(x_st + dx * 1 + 160, y_st + dy * 3);
            lb_pc_plc4b.Location = new Point(x_st + dx * 1 + 160, y_st + dy * 4);

            lb_plc_pc0.Text = "M" + (10000 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
            lb_plc_pc1.Text = "M" + (10001 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
            lb_plc_pc2.Text = "M" + (10002 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
            lb_pc_plc0.Text = "M" + (12000 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
            lb_pc_plc1.Text = "M" + (12001 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
            lb_pc_plc2.Text = "M" + (12002 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
            lb_plc_pc3a.Text = "ID資料    D" + (2000 + plc_d_address_offset).ToString();
            lb_plc_pc4a.Text = "收到結果D" + (2010 + plc_d_address_offset).ToString();
            lb_plc_pc3b.Text = "";
            lb_plc_pc4b.Text = "";
            lb_pc_plc3a.Text = "ID資料    D" + (8000 + plc_d_address_offset).ToString();
            lb_pc_plc4a.Text = "檢測結果D" + (8010 + plc_d_address_offset).ToString();
            lb_pc_plc3b.Text = "";
            lb_pc_plc4b.Text = "";
            lb_read_write_plc.Text = "";
            lb_plc_main_mesg3.Text = "Master 無動作";

            pbx_plc_status.Size = new Size(w * 3, h * 3);
            pbx_plc_status.Location = new Point(groupBox_plc.Location.X + groupBox_plc.Width - w * 4, h * 5);
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

            bt_copy_to_clipboard.BackgroundImage = Properties.Resources.clipboard;
            bt_copy_to_clipboard.BackgroundImageLayout = ImageLayout.Zoom;
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;
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
            this.groupBox_plc.Controls.Add(pbx_m10000);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m10001);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m10002);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m12000);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m12001);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_m12002);	// 將控件加入表單
            this.groupBox_plc.Controls.Add(pbx_plc_status);  // 將控件加入表單
            this.groupBox_plc.Controls.Add(pictureBox_plc_status);  // 將控件加入表單

            if (flag_automation_mode == MODE_AWB)
            {
                groupBox_plc.Text = "自動化作業 : 色彩調教";
                plc_m_address_offset = OFFSET_M_AWB;
                plc_d_address_offset = OFFSET_D_AWB;
                lb_plc_command_type.Text = "色彩調教";
                panel_plc.BackColor = Color.LightYellow;
                pbx_connection2.BackgroundImage = Properties.Resources.awb1;
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                groupBox_plc.Text = "自動化作業 : 資料燒錄";
                plc_m_address_offset = OFFSET_M_WRITE_DATA;
                plc_d_address_offset = OFFSET_D_WRITE_DATA;
                lb_plc_command_type.Text = "資料燒錄";
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

            richTextBox_plc.Text = groupBox_plc.Text;

            richTextBox_plc.Text += "\n按\"啟動自動化作業\"開始測試\n";
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
                    panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
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
                panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
            }
        }

        int timer_plc_display_show_main_mesg_count = 0;
        int timer_plc_display_show_main_mesg_count_target = 0;

        void show_plc_main_message1(string mesg, int number, int timeout)
        {
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
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
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
        int m10000_value = 0;
        int m10001_value = 0;
        int m10002_value = 0;
        int m12000_value = 0;
        int m12001_value = 0;
        int m12002_value = 0;

        int[] plc_test_status_data = new int[N];
        int[] m10000_data = new int[N];
        int[] m10001_data = new int[N];
        int[] m10002_data = new int[N];
        int[] m12000_data = new int[N];
        int[] m12001_data = new int[N];
        int[] m12002_data = new int[N];

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
                List<bool> data = mitsubishi.PLC_read_M_bit("M", "10000");//讀取狀態
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
            if (cb_test_plc.Checked == true)
            {
                do_test_plc();
                return;
            }

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

        void update_plc_data_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();
            bool status;

            string contact_address = string.Empty;

            //M10000
            contact_address = (10000 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10000_value = 1;
            }
            else
            {
                m10000_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10000_data[i] = m10000_data[i + 1];
            }
            m10000_data[N - 1] = m10000_value;

            if (m10000_value == 1)
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M10001
            contact_address = (10001 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10001_value = 1;
            }
            else
            {
                m10001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10001_data[i] = m10001_data[i + 1];
            }
            m10001_data[N - 1] = m10001_value;

            if (m10001_value == 1)
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M10002
            contact_address = (10002 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10002_value = 1;
            }
            else
            {
                m10002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10002_data[i] = m10002_data[i + 1];
            }
            m10002_data[N - 1] = m10002_value;

            if (m10002_value == 1)
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12000
            contact_address = (12000 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12000_value = 1;
            }
            else
            {
                m12000_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12000_data[i] = m12000_data[i + 1];
            }
            m12000_data[N - 1] = m12000_value;

            if (m12000_value == 1)
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12001
            contact_address = (12001 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12001_value = 1;
            }
            else
            {
                m12001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12001_data[i] = m12001_data[i + 1];
            }
            m12001_data[N - 1] = m12001_value;

            if (m12001_value == 1)
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12002
            contact_address = (12002 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12002_value = 1;
            }
            else
            {
                m12002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12002_data[i] = m12002_data[i + 1];
            }
            m12002_data[N - 1] = m12002_value;

            if (m12002_value == 1)
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            if ((flag_use_real_plc == true) || (plc_simulator_step != 0))
            {
                contact_address = (2000 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                string data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD2000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc3b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (2010 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (8000 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);

                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc3b.Text = data_read;
                delay(DELAY_TIME);

                contact_address = (8010 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc4b.Text = data_read;
            }
        }

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

            //畫 PLC status  畫直線, 灰色底線
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
            g.DrawString(flag_plc_test_count.ToString(), f3, new SolidBrush(Color.Red), new PointF(x_st - 10 - 10 * (flag_plc_test_count.ToString().Length), 20));

            int xx_st = x_st + step * 0;
            int xx_sp = x_st + step * (N - 1);
            int yy = 0;
            hh = h / 8;

            //畫直線, 灰色底線

            //畫M10000
            yy = H - y_st - 5 - hh * 5 - dd * 5;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M10001
            yy = H - y_st - 5 - hh * 4 - dd * 4;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M10002
            yy = H - y_st - 5 - hh * 3 - dd * 3;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M12000
            yy = H - y_st - 5 - hh * 2 - dd * 2;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M12001
            yy = H - y_st - 5 - hh * 1 - dd * 1;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            //畫M12002
            yy = H - y_st - 5 - hh * 0 - dd * 0;
            points.Clear();
            points.Add(new Point(xx_st, yy));
            points.Add(new Point(xx_sp, yy));
            g.DrawLines(grayPen, points.ToArray());  //畫直線, 灰色底線

            bool plc_power_status = check_plc_power_status();
            if (plc_power_status == true)
            {
                redPen = new Pen(Color.Red, 3);
            }
            else
            {
                redPen = new Pen(Color.Gray, 3);
            }

            //畫M10000
            points.Clear();
            pt_old = m10000_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m10000_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 5 - dd * 5;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m10000_data[i] - 5 - hh * 5 - dd * 5;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (10000 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 5 - dd * 5));

            //畫M10001
            points.Clear();
            pt_old = m10001_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m10001_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 4 - dd * 4;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m10001_data[i] - 5 - hh * 4 - dd * 4;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (10001 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 4 - dd * 4));

            //畫M10002
            points.Clear();
            pt_old = m10002_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m10002_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 3 - dd * 3;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m10002_data[i] - 5 - hh * 3 - dd * 3;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (10002 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 3 - dd * 3));

            //畫M12000
            points.Clear();
            pt_old = m12000_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m12000_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 2 - dd * 2;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m12000_data[i] - 5 - hh * 2 - dd * 2;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (12000 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 2 - dd * 2));

            //畫M12001
            points.Clear();
            pt_old = m12001_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m12001_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 1 - dd * 1;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m12001_data[i] - 5 - hh * 1 - dd * 1;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (12001 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 1 - dd * 1));

            //畫M12002
            points.Clear();
            pt_old = m12002_data[0];
            for (i = 0; i < N; i++)
            {
                if (i > 0)
                {
                    pt_new = m12002_data[i];
                    if (pt_new != pt_old)
                    {
                        x = x_st + step * i;
                        y = H - y_st - hh * pt_old - 5 - hh * 0 - dd * 0;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - hh * m12002_data[i] - 5 - hh * 0 - dd * 0;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M" + (12002 + plc_m_address_offset).ToString(), f3, new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - hh * 1 - 5 - hh * 0 - dd * 0));

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

        string get_plc_w_data(string contact_address)
        {
            string contact_point = "W";
            string data_read = "";

            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready)//PLC是否準備完成
            {
                //richTextBox_plc.Text += "三菱PLC ready 1\n";
                //richTextBox_plc.Text += "\n觸點 : " + contact_point + "\t位址 : " + contact_address + "\n";

                //List<bool> data = mitsubishi.PLC_read_M_bit(contact_point, contact_address);    //讀取狀態
                //richTextBox_plc.Text += "len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

                //if (data[0] == true)
                {
                    string dddd = mitsubishi.PLC_read_D_register(contact_point, contact_address, numerical_format.String_32_Bit);
                    data_read = dddd;
                }
                //else
                {
                    //data_read = "無資料";
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
                //richTextBox_plc.Text += "set " + contact_address + " as " + write_data + "\n";
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
            int i;
            bool ret = false;
            string get_signal = string.Empty;
            for (i = 0; i < 1000; i++)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    break;
                }

                //richTextBox_plc.Text += "contact_address1 = " + contact_address1 + "\n";
                //richTextBox_plc.Text += "contact_address2 = " + contact_address2 + "\n";
                ret = get_plc_m_status(contact_address1);
                if (ret == false)
                {
                    richTextBox_plc.Text += "OFF  ";
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
                    richTextBox_plc.Text += "ON  ";
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
                    richTextBox_plc.Text += "OFF  ";
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
                    richTextBox_plc.Text += "ON  ";
                    if (polling_status == HIGH)
                    {
                        get_signal = contact_address2;
                        break;
                    }
                    else
                        delay(500);
                }
            }
            return get_signal;
        }

        void polling_m_status(string contact_address, PLC_STATE polling_status)
        {
            int i;
            bool ret = false;
            for (i = 0; i < 1000; i++)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    break;
                }

                ret = get_plc_m_status(contact_address);
                if (ret == false)
                {
                    richTextBox_plc.Text += "OFF  ";
                    if (polling_status == HIGH)
                        delay(500);
                    else
                        break;
                }
                else
                {
                    richTextBox_plc.Text += "ON  ";
                    if (polling_status == HIGH)
                        break;
                    else
                        delay(500);
                }
            }
        }

        void get_all_plc_m_status()
        {
            string contact_address = String.Empty;
            bool ret = false;

            //richTextBox_plc.Text += "測試 get_plc_m_status()\n";

            contact_address = (10000 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (10001 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (10002 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (12000 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (12001 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = (12002 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
        }

        void set_all_plc_m_status_low()
        {
            string contact_address = String.Empty;

            if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
            {
                contact_address = "10000";
                set_plc_m_status(contact_address, LOW);
                contact_address = "10001";
                set_plc_m_status(contact_address, LOW);
                contact_address = "10002";
                set_plc_m_status(contact_address, LOW);
                contact_address = "12000";
                set_plc_m_status(contact_address, LOW);
                contact_address = "12001";
                set_plc_m_status(contact_address, LOW);
                contact_address = "12002";
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
                contact_address = "13000";
                set_plc_m_status(contact_address, LOW);
                contact_address = "13001";
                set_plc_m_status(contact_address, LOW);
                contact_address = "13002";
                set_plc_m_status(contact_address, LOW);
                contact_address = "15000";
                set_plc_m_status(contact_address, LOW);
                contact_address = "15001";
                set_plc_m_status(contact_address, LOW);
                contact_address = "15002";
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

            /* 不用檢查 M10000
            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;
            */

            contact_address = (10001 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (10002 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (12000 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (12001 + plc_m_address_offset).ToString();
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = (12002 + plc_m_address_offset).ToString();
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
                    lb_plc_pc3a.Text = "ID資料    D" + (2000 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (2010 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (8000 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (8010 + plc_d_address_offset).ToString();
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
                    lb_plc_pc3a.Text = "ID資料    D" + (2000 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (2010 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (8000 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (8010 + plc_d_address_offset).ToString();
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

                    lb_plc_pc0.Text = "M" + (10000 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M" + (10001 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M" + (10002 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M" + (12000 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M" + (12001 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M" + (12002 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (2000 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (2010 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (8000 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (8010 + plc_d_address_offset).ToString();
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
                    lb_plc_pc0.Text = "M" + (10000 + plc_m_address_offset).ToString() + " PLC -> PC 動作要求";
                    lb_plc_pc1.Text = "M" + (10001 + plc_m_address_offset).ToString() + " PLC -> PC 確認完成";
                    lb_plc_pc2.Text = "M" + (10002 + plc_m_address_offset).ToString() + " PLC -> PC 收到動作完成";
                    lb_pc_plc0.Text = "M" + (12000 + plc_m_address_offset).ToString() + " PC -> PLC 收到動作要求";
                    lb_pc_plc1.Text = "M" + (12001 + plc_m_address_offset).ToString() + " PC -> PLC 確認開始";
                    lb_pc_plc2.Text = "M" + (12002 + plc_m_address_offset).ToString() + " PC -> PLC 動作完成";
                    lb_plc_pc3a.Text = "ID資料    D" + (2000 + plc_d_address_offset).ToString();
                    lb_plc_pc4a.Text = "收到結果D" + (2010 + plc_d_address_offset).ToString();
                    lb_plc_pc3b.Text = "";
                    lb_plc_pc4b.Text = "";
                    lb_pc_plc3a.Text = "ID資料    D" + (8000 + plc_d_address_offset).ToString();
                    lb_pc_plc4a.Text = "檢測結果D" + (8010 + plc_d_address_offset).ToString();
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
                    return;
                }
                ret = check_plc_power_status();

                if (ret == true)
                {
                    richTextBox_plc.Text += "(0) 三菱PLC 已 Ready, 繼續\n";
                }
                else
                {
                    richTextBox_plc.Text += "(0) 三菱PLC 不 Ready, 等待\n";
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

            //richTextBox_plc.Text += "(0) PC 啟動完成, 偵測PLC之M10000信號 或 M13000信號\n";
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
            richTextBox_plc.Text += "\t(1b1) PLC 把相機序號資料放在 D" + (2000 + plc_d_address_offset).ToString() + "\n";
            richTextBox_plc.Text += "\t(1b2) PLC 拉高 M" + (10000 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知條碼內容已備便\n";
            richTextBox_plc.Text += "(1b) 若是要做燒錄/色調 對時\n";
            richTextBox_plc.Text += "\t(1c1) PLC 把對時資料放在 D" + (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString() + "\n";
            richTextBox_plc.Text += "\t(1c2) PLC 拉高 M" + (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + ", 供PC讀取, 通知對時資料已備便\n";

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

            string contact_address1 = (10000 + plc_m_address_offset).ToString();
            string contact_address2 = (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
            richTextBox_plc.Text += "PC 讀取 M" + contact_address1 + " 或 M" + contact_address2 + " 狀態\t=>\t";

            string get_signal = polling_2m_status(contact_address1, contact_address2, HIGH);

            richTextBox_plc.Text += "\n(3b) PC 取得 M" + get_signal + "為 ON\t=> ";

            if (get_signal == contact_address1)
            {
                /*
                //pc_work_type = MODE_WRITE_DATA;   //1: MODE_WRITE_DATA 燒錄
                groupBox_plc.BackColor = Color.DeepPink;
                //richTextBox_plc.Text += "groupBox_plc 背景色 DeepPink\n";
                richTextBox_plc.Text += "\n(3b) PC 取得 M10000 為 ON\t=> 序號燒錄\t";
                lb_plc_main_mesg3.Text = "Slave 接收命令";

                richTextBox_plc.Text += "序號燒錄\n";
                plc_m_address_offset = OFFSET_M_WRITE_DATA;
                plc_d_address_offset = OFFSET_D_WRITE_DATA;
                */

                if (flag_automation_mode == MODE_WRITE_DATA)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "燒錄\n";
                    lb_plc_command_type.Text = "資料燒錄";
                }
                else if (flag_automation_mode == MODE_AWB)    //0: MODE_OFF, 1: MODE_WRITE_DATA 燒錄, 2: MODE_AWB 色調
                {
                    richTextBox_plc.Text += "色調\n";
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
                contact_address = (2000 + plc_d_address_offset).ToString();
                richTextBox_plc.Text += "(3c1) PC 讀取 D" + contact_address + " 資料\n";
            }
            else
            {
                contact_address = (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
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

            delay(500);

            string data_to_write = string.Empty;
            string contact_address_to = string.Empty;
            if (plc_do_check_time == false)
            {
                //一般
                contact_address_to = (8000 + plc_d_address_offset).ToString();

                richTextBox_plc.Text += "(3d1) PC 將 從 D" + contact_address + " 取得的資料 寫到 D" + contact_address_to + "\n";

                data_to_write = camera_serial_data.Substring(0, 16);

                //richTextBox_plc.Text += "data_to_write : " + data_to_write + "\n";
                //richTextBox_plc.Text += "\nlen = " + data_to_write.Length.ToString() + "\n";

                show_plc_main_message1("寫入 D" + contact_address_to, S_OK, 30);
                set_plc_d_data(contact_address_to, data_to_write);

            }
            else
            {
                //對時
                contact_address = (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
                contact_address_to = (8000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();

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
                        string contact_address_r = (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME + offset).ToString();
                        string contact_address_w = (8000 + plc_d_address_offset + OFFSET_D_CHECK_TIME + offset).ToString();
                        string data = string.Empty;
                        data = get_plc_d_data_bcd16(contact_address_r);
                        //richTextBox_plc.Text += data + "\tlen = " + data.Length.ToString() + "\n";
                        if (data.Length > 0)
                        {
                            set_plc_d_data_bcd16(contact_address_w, data);

                            int vv = 0;
                            for (int i = 0; i < data.Length; i++)
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
                richTextBox1.Text += "system time = " + DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                richTextBox1.Text += "usertime    = " + datetime_user.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                richTextBox1.Text += "diff = " + datetime_diff.ToString() + "\n";
                */
            }

            delay(500);

            if (plc_do_check_time == false)
            {
                contact_address = (12000 + plc_m_address_offset).ToString();
            }
            else
            {
                contact_address = (12000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
            }

            richTextBox_plc.Text += "(4) PC 拉高 M" + contact_address + ", 通知PLC, PC動作已完成\n";
            //richTextBox_plc.Text += "[M status] M12000 HIGH\n";

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

            richTextBox_plc.Text += "(5a) PLC收到 PC訊號 M" + contact_address + " ON時,PLC確認資料一致\n";
            richTextBox_plc.Text += "(5b) PLC 拉高 M" + (10001 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知開始工作\n";
            //richTextBox_plc.Text += "[M status] M10001 HIGH\n";

            richTextBox_plc.Text += "(6a) PC 讀取 M" + (10001 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (10001 + plc_m_address_offset).ToString();
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(6b) PC 取得 M" + (10001 + plc_m_address_offset).ToString() + " 為 ON\n";

            richTextBox_plc.Text += "(6c) PC 拉高 M" + (12001 + plc_m_address_offset).ToString() + ", 供PLC讀取, 通知PC已開始工作\t";
            //richTextBox_plc.Text += "[M status] M12001 HIGH\n";

            lb_plc_main_mesg3.Text = "Slave 開始工作";

            contact_address = (12001 + plc_m_address_offset).ToString();
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

            richTextBox_plc.Text += "(未處理)相機序號 : \t" + camera_serial_data + "\n";
            richTextBox_plc.Text += "長度 : " + camera_serial_data.Length.ToString() + "\n";

            if (camera_serial_data.Length >= 16)
            {
                camera_serial_data = camera_serial_data.Substring(0, 15);
                camera_serial_data += "@";
            }
            else
            {
                camera_serial_data = camera_serial_data.PadRight(16, '@'); //向長度小於16的字符串末尾添加空格，補足16個字符
            }
            richTextBox_plc.Text += "(已處理)相機序號 : \t" + camera_serial_data + "\n";

            int work_result = 0xff;

            Random r = new Random();

            if (flag_use_real_ims == true)    //真的做 燒錄 或 色調
            {
                if (flag_automation_mode == MODE_AWB)  //色彩調教
                {
                    work_result = do_awb(sender, e);
                    check_awb_result(work_result);

                    if (bt_awb_break.Text == "確認")
                    {
                        bt_awb_break_Click(sender, e);
                        flag_wait_for_confirm = false;
                    }
                }
                else if (flag_automation_mode == MODE_WRITE_DATA)
                {
                    richTextBox_plc.Text += "相機序號燒錄\n";

                    work_result = do_write_serial_data(camera_serial_data);
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
            richTextBox_plc.Text += "\n\n(7) PC 做完工作, 將結果碼寫在 D" + (8010 + plc_d_address_offset).ToString() + "\n";

            //work_result = r.Next(1, 20);
            richTextBox_plc.Text += "PC 工作結果: 0x" + work_result.ToString("X2") + " = " + work_result.ToString() + "\n";

            string write_data = work_result.ToString();
            show_plc_main_message1("寫入: D" + (8010 + plc_d_address_offset).ToString() + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16((8010 + plc_d_address_offset).ToString(), write_data);

            richTextBox_plc.Text += "(8) PC 拉高 M" + (12002 + plc_m_address_offset).ToString() + ", 供PLC讀取, 通知PLC, PC已做完工作\n";
            //richTextBox_plc.Text += "[M status] M12002 HIGH\n";

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

            contact_address = (12002 + plc_m_address_offset).ToString();
            timer_plc_status_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox_plc.Text += "(9) PLC偵測到 PC之動作完成信號 M" + (12002 + plc_m_address_offset).ToString() + ", PLC設定 M" + (10002 + plc_m_address_offset).ToString() + "為ON\n";
            //richTextBox_plc.Text += "[M status] M10002 HIGH\n";

            richTextBox_plc.Text += "(10a) PC 檢測 M" + (10002 + plc_m_address_offset).ToString() + " 和 M" + (12002 + plc_m_address_offset).ToString() + "\n";

            richTextBox_plc.Text += "(10a1) PC 讀取 M" + (10002 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (10002 + plc_m_address_offset).ToString();
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(10a2) PC 取得 M" + (10002 + plc_m_address_offset).ToString() + " 為 ON\n";

            richTextBox_plc.Text += "(10a3) PC 讀取 M" + (12002 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (12002 + plc_m_address_offset).ToString();
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(10a4) PC 取得 M" + (12002 + plc_m_address_offset).ToString() + " 為 ON\n";

            delay(500);

            richTextBox_plc.Text += "(10b) PC 清除 D" + (8000 + plc_d_address_offset).ToString() + " ~ D" + (8007 + plc_d_address_offset).ToString() + " 資料\n";
            erase_plc_d_data((8000 + plc_d_address_offset).ToString(), 8);

            richTextBox_plc.Text += "(10c) PC 令 (收到動作要求信號)M" + (12000 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12000 LOW\n";
            contact_address = (12000 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "(10d) PC 令 (動作執行信號)M" + (12001 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12001 LOW\n";
            contact_address = (12001 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            //richTextBox_plc.Text += "[M status] M10000 LOW\n";
            //richTextBox_plc.Text += "[M status] M10001 LOW\n";

            delay(500);

            richTextBox_plc.Text += "(10e) PLC 清除 D" + (2000 + plc_d_address_offset).ToString() + " ~ D" + (2007 + plc_d_address_offset).ToString() + " 資料\n";
            richTextBox_plc.Text += "(10f) PLC 令 (動作要求訊號)M" + (10000 + plc_m_address_offset).ToString() + " 為 OFF\n";
            richTextBox_plc.Text += "(10g) PLC 令 (動作開始要求訊號)M" + (10001 + plc_m_address_offset).ToString() + " 為 OFF\n";

            delay(500);

            richTextBox_plc.Text += "(11a) PC 檢測 (PLC動作完成信號)M" + (10002 + plc_m_address_offset).ToString() + "\n";
            //當PC收到PLC收到動作完成訊號M10002 ON之後,結果碼D8010資料清除
            //PC->PLC動作完成訊號M12002 OFF

            richTextBox_plc.Text += "(11a) PC 讀取 M" + (10002 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (10002 + plc_m_address_offset).ToString();
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(11b) PC 取得 M" + (10002 + plc_m_address_offset).ToString() + " 為 ON\n";

            /*  暫不清除資料
            richTextBox_plc.Text += "(11c) PC 清除 D8010資料\n";
            contact_address = "8010";
            erase_plc_d_data(contact_address, 1);
            */

            richTextBox_plc.Text += "(11d) PC 令 M" + (12002 + plc_m_address_offset).ToString() + " 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12002 LOW\n";
            contact_address = (12002 + plc_m_address_offset).ToString();
            set_plc_m_status(contact_address, LOW);

            delay(500);

            richTextBox_plc.Text += "(12a) PLC 收到 PC 設定 M" + (12002 + plc_m_address_offset).ToString() + " 為 OFF, PLC 設定 M" + (10002 + plc_m_address_offset).ToString() + "為OFF\n";
            richTextBox_plc.Text += "[M status] M" + (10002 + plc_m_address_offset).ToString() + " LOW\n";

            richTextBox_plc.Text += "(12b) PC 讀取 M" + (10002 + plc_m_address_offset).ToString() + " 狀態\t=>\t";
            contact_address = (10002 + plc_m_address_offset).ToString();
            polling_m_status(contact_address, LOW);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(12c1) PC 取得 M" + (10002 + plc_m_address_offset).ToString() + " 為 LOW\n";
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
            polling_m_status(contact_address, LOW);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
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

            richTextBox_plc.Text += "\n啟動自動化作業\n";

            int cnt = 1;
            while (true)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "使用者中斷PLC測試, 結束\n";
                    break;
                }

                /*
                if (cnt == 3)
                {
                    richTextBox_plc.Text += "\n\n\n\n結束\n\n\n\n\n";
                    break;
                }
                */

                richTextBox_plc.Text += "\n第 " + (cnt++).ToString() + " 次測試\n";

                do_PC_PLC_Communication(sender, e);
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "使用者中斷PLC測試, 結束\n";
                    break;
                }
                delay(1000);
            }

            bt_plc_test.BackColor = Color.White;
            bt_plc_test_break.BackColor = Color.White;

            if (flag_plc_test_break == true)
            {
                flag_plc_test_break = false;

                richTextBox_plc.Text += "\n測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\t使用者中斷\n\n";

                stopwatch_plc.Stop();
                richTextBox_plc.Text += "時間3 : " + DateTime.Now.ToString() + "\n";
            }
            flag_plc_test = false;
            flag_plc_test_busy = false;
            flag_plc_test_break = false;
        }

        private void bt_plc_test_break_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "設定 中斷\n";
            bt_plc_test_break.BackColor = Color.Red;
            flag_plc_test_break = true;
        }

        private void bt_plc_test_break_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox_plc.Text += "設定 中斷\n";
            bt_plc_test_break.BackColor = Color.Red;
            flag_plc_test_break = true;
        }

        private void bt_check_connection_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "檢查連線狀態\n";

            if (serialPort2.IsOpen == true)
            {
                richTextBox_plc.Text += "Comport 已開啟\n";
            }
            else
            {
                richTextBox_plc.Text += "Comport 未開啟\n";
            }

            if (flag_comport_ok == true)
            {
                richTextBox_plc.Text += "Comport 開啟 OK\n";
            }
            else
            {
                richTextBox_plc.Text += "Comport 開啟 失敗\n";
            }

            if (flag_comport_connection_ok == true)
            {
                richTextBox_plc.Text += "Comport 連線 OK\n";
            }
            else
            {
                richTextBox_plc.Text += "Comport 連線 NG\n";
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
            }
            else
            {
                richTextBox_plc.Text += "相機運行 NG\n";
            }

            if (flag_ims_egd_exist == true)
            {
                richTextBox_plc.Text += "有ims相機\n";
            }
            else
            {
                richTextBox_plc.Text += "無ims相機\n";
            }




            richTextBox_plc.Text += "\n";
        }

        private void bt_read_camera_data_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "讀取相機資料中...";



            /*
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
            */

            return;
        }

        private void bt_erase_camera_data_Click(object sender, EventArgs e)
        {
            richTextBox_plc.Text += "清除相機資料\n";
            erase_camera_data();
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
        int m10000_simulator_value = 0;
        int m10001_simulator_value = 0;
        int m10002_simulator_value = 0;
        int m12000_simulator_value = 0;
        int m12001_simulator_value = 0;
        int m12002_simulator_value = 0;

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

        string d2000_simulator_data = "";   //PLC製作之相機序號
        string d2010_simulator_data = "";   //PLC收到的動作結果
        string d8000_simulator_data = "";   //PC拿到的相機序號寫在這裡
        string d8010_simulator_data = "";   //PC把動作結果寫在這裡
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

                    d2000_simulator_data = "";
                    d2010_simulator_data = "";
                    d2020_simulator_data = "";
                    d8000_simulator_data = "";
                    d8010_simulator_data = "";
                    d8020_simulator_data = "";

                    if (plc_do_check_time == false)
                    {
                        //設定M10000 10001 10002 信號為0
                        contact_address = (10000 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        contact_address = (10001 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        contact_address = (10002 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                    }
                    else
                    {
                        //設定M10012 or M13012 信號為0
                        contact_address = (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
                        set_plc_m_status(contact_address, LOW);
                    }

                    if (flag_automation_mode == MODE_WRITE_DATA)
                    {
                        if (flag_use_real_ims == true)
                        {
                            richTextBox_plc.Text += "相機序號燒錄\t清除相機資料\n";
                            erase_camera_data();
                        }
                    }
                }
            }
            else if (plc_simulator_step == 1)   //PLC Power ON
            {
                if (plc_simulator_count < 5)
                {
                    if (plc_do_check_time == false)
                    {

                        //檢查M10000 10001 10002 M12000 12001 12002 信號是否皆為0
                        contact_address = (10000 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (10000 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (10001 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (10001 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (10002 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (10002 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12000 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (12000 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12001 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (12001 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12002 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (12002 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
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
                            richTextBox_plc.Text += "M" + (10000 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12012 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (10001 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
                            plc_simulator_count = 0;
                        }
                        contact_address = (12013 + plc_m_address_offset).ToString();
                        status = get_plc_m_status(contact_address);
                        if (status == true)
                        {
                            richTextBox_plc.Text += "M" + (10002 + plc_m_address_offset).ToString() + " 不該為 HIGH\n";
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
                        richTextBox_plc.Text += "[PLC] 把相機序號資料放在 D" + (2000 + plc_d_address_offset).ToString() + "\n";

                        //PLC製作相機序號資料

                        contact_address = (2000 + plc_d_address_offset).ToString();
                        string write_data = plc_make_camera_data();
                        show_plc_main_message1("PLC 寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
                        set_plc_d_data(contact_address, write_data);

                        richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (10000 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知條碼內容已備便\n";
                        richTextBox_plc.Text += "[PLC] 令 M" + (10000 + plc_m_address_offset).ToString() + " 為 HIGH\n";
                        contact_address = (10000 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, HIGH);
                    }
                    else
                    {
                        richTextBox_plc.Text += "[PLC] 把燒錄對時資料放在 D" + (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString() + "\n";

                        //PLC製作燒錄對時資料

                        contact_address = (2000 + plc_d_address_offset + OFFSET_D_CHECK_TIME).ToString();
                        //contact_address = (2000 + plc_d_address_offset).ToString();
                        string write_data = plc_make_datetime_data();
                        show_plc_main_message1("PLC 寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
                        set_plc_d_data(contact_address, write_data);

                        richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + ", 供PC讀取, 通知對時資料已備便\n";
                        richTextBox_plc.Text += "[PLC] 令 M" + (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString() + " 為 HIGH\n";
                        contact_address = (10000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
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
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12000 是否為HIGH, 若是, 代表PC已備便\n";
                    bool ret = false;
                    if (plc_do_check_time == false)
                    {
                        contact_address = (12000 + plc_m_address_offset).ToString();
                    }
                    else
                    {
                        contact_address = (12000 + plc_m_address_offset + OFFSET_M_CHECK_TIME).ToString();
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
                            richTextBox_plc.Text += "[PLC] PLC 拉高 M" + (10001 + plc_m_address_offset).ToString() + ", 供PC讀取, 通知開始工作\n";
                            contact_address = (10001 + plc_m_address_offset).ToString();
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
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12002 是否為 HIGH, 若是, 代表PC已做完工作\n";
                    bool ret = false;
                    contact_address = (12002 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成工作 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 已完成工作, 完成信號 M" + (12002 + plc_m_address_offset).ToString() + "\n";

                        string work_result = get_plc_d_data((8010 + plc_d_address_offset).ToString());
                        richTextBox_plc.Text += "[PLC] PLC 讀取D" + (8010 + plc_d_address_offset).ToString() + "的資料 : " + work_result + "\n";

                        richTextBox_plc.Text += "[PLC] PLC 讀取D" + (8010 + plc_d_address_offset).ToString() + "的資料, 寫到 D" + (2010 + plc_d_address_offset).ToString() + "\n";
                        contact_address = (2010 + plc_d_address_offset).ToString();
                        set_plc_d_data(contact_address, work_result);

                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (10002 + plc_m_address_offset).ToString() + "為ON\n";
                        contact_address = (10002 + plc_m_address_offset).ToString();
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
                    richTextBox_plc.Text += "[PLC] PLC 檢查 M" + (12002 + plc_m_address_offset).ToString() + " 是否為 ON, 若是, PLC 可以清除D" + (2000 + plc_d_address_offset).ToString() + "資料\n";
                    bool ret = false;
                    contact_address = (12002 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        richTextBox_plc.Text += "[PLC] PLC 檢查 M" + (12002 + plc_m_address_offset).ToString() + " 是否為 ON, PLC 可以清除D" + (2000 + plc_d_address_offset).ToString() + "資料\n";
                        show_plc_main_message1("清除 D" + (2000 + plc_d_address_offset).ToString(), S_OK, 30);
                        set_plc_d_data((2000 + plc_d_address_offset).ToString(), "");

                        plc_simulator_count = 7;
                    }
                    else
                    {
                        plc_simulator_count--;
                    }
                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12001 是否為 LOW, 若是, 代表PC已做完\n";
                    bool ret = false;
                    contact_address = (12001 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 之動作完成信號 M" + (12001 + plc_m_address_offset).ToString() + " 為 LOW, PLC設定 M" + (10002 + plc_m_address_offset).ToString() + " 為 HIGH\n";

                        plc_simulator_count = 0;
                        plc_simulator_step = 5;

                        contact_address = (10002 + plc_m_address_offset).ToString();
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
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12002 是否為 LOW, 若是, 代表PC已做完\n";
                    bool ret = false;
                    contact_address = (12002 + plc_m_address_offset).ToString();
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC之動作完成信號 M" + (12002 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (10002 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (10002 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (10001 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (10001 + plc_m_address_offset).ToString();
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M" + (10000 + plc_m_address_offset).ToString() + " 為 LOW\n";
                        contact_address = (10000 + plc_m_address_offset).ToString();
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

        string plc_make_camera_data()
        {
            //序號格式(13碼, 1英7數1英4數) 例如 N2201001A0001
            //                                  012345678

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
                if (contact_address == (10000 + plc_m_address_offset).ToString())
                {
                    m_status = m10000_simulator_value;
                }
                else if (contact_address == (10001 + plc_m_address_offset).ToString())
                {
                    m_status = m10001_simulator_value;
                }
                else if (contact_address == (10002 + plc_m_address_offset).ToString())
                {
                    m_status = m10002_simulator_value;
                }
                else if (contact_address == (12000 + plc_m_address_offset).ToString())
                {
                    m_status = m12000_simulator_value;
                }
                else if (contact_address == (12001 + plc_m_address_offset).ToString())
                {
                    m_status = m12001_simulator_value;
                }
                else if (contact_address == (12002 + plc_m_address_offset).ToString())
                {
                    m_status = m12002_simulator_value;
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
            if (contact_address == (10000 + plc_m_address_offset).ToString())
            {
                m10000_simulator_value = (int)write_data;
            }
            else if (contact_address == (10001 + plc_m_address_offset).ToString())
            {
                m10001_simulator_value = (int)write_data;
            }
            else if (contact_address == (10002 + plc_m_address_offset).ToString())
            {
                m10002_simulator_value = (int)write_data;
            }
            else if (contact_address == (12000 + plc_m_address_offset).ToString())
            {
                m12000_simulator_value = (int)write_data;
            }
            else if (contact_address == (12001 + plc_m_address_offset).ToString())
            {
                m12001_simulator_value = (int)write_data;
            }
            else if (contact_address == (12002 + plc_m_address_offset).ToString())
            {
                m12002_simulator_value = (int)write_data;
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
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 2, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
            }
        }

        string get_plc_simulator_d_data(string contact_address)
        {
            string plc_simulator_d_data = string.Empty;

            if (contact_address == (2000 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d2000_simulator_data;
            }
            else if (contact_address == (2010 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d2010_simulator_data;
            }
            else if (contact_address == (8000 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d8000_simulator_data;
            }
            else if (contact_address == (8010 + plc_d_address_offset).ToString())
            {
                plc_simulator_d_data = d8010_simulator_data;
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
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 3, contact_address = " + contact_address + "\tplc_m_address_offset = " + plc_m_address_offset.ToString() + "\n";
            }
            return plc_simulator_d_data;
        }

        void set_plc_simulator_d_data(string contact_address, string write_data)
        {
            //richTextBox_plc.Text += "模擬寫了 D" + contact_address + ", 資料為: " + write_data.ToString() + "\n";

            if (contact_address == (2000 + plc_d_address_offset).ToString())
            {
                d2000_simulator_data = write_data;
            }
            else if (contact_address == (2010 + plc_d_address_offset).ToString())
            {
                d2010_simulator_data = write_data;
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
            else if (contact_address == (8000 + plc_d_address_offset).ToString())
            {
                d8000_simulator_data = write_data;
            }
            else if (contact_address == (8010 + plc_d_address_offset).ToString())
            {
                d8010_simulator_data = write_data;
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

            Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write

            serialPort2.Write(sn_data_tmp, 0, 16);

            /*      //不檢查相機內有無資料 直接寫入資料
            flag_camera_already_have_serial = 1;
            cnt = 0;
            int cnt_max = 50;
            while ((flag_camera_already_have_serial == 1) && (cnt < cnt_max))
            {
                cnt++;
                richTextBox_plc.Text += "s";
                //richTextBox_plc.Text += "e" + cnt.ToString() + " ";
                delay(10);
            }

            if (flag_camera_already_have_serial == 1)
            {
                richTextBox_plc.Text += "相機已有序號, break\n";
                lb_write_camera_serial2.Text = "相機已有序號, 中斷";

                g2.Clear(BackColor);
                g2.DrawString("燒錄失敗", new Font("標楷體", 60), new SolidBrush(Color.Red), new PointF(20, 20));
                bt_confirm.Visible = true;
                timer_stage4.Enabled = false;
                playSound(S_FALSE);
            }
            else
            */
            {
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

                //richTextBox_plc.Text += "把資料暫存起來\n";
                camera_serials.Add(new string[] { serial_data.ToUpper(), "", DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") });

                //if ((camera_serials.Count % 5) == 0)
                {
                    richTextBox_plc.Text += "自動存檔\n";
                    flag_operation_mode = MODE_RELEASE_STAGE4;
                    exportCSV();
                    flag_operation_mode = MODE_RELEASE_STAGE2;
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
            }
            flag_doing_writing_data = false;


            //在這裡檢查ims主機有無回傳錯誤碼


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
                contact_address2 = "15011";  //色調心跳 PC給PLC
            }
            else if (flag_automation_mode == MODE_WRITE_DATA)
            {
                contact_address1 = "12010";  //燒錄狀態 PC給PLC
                contact_address2 = "12011";  //燒錄心跳 PC給PLC
            }
            else
            {
                contact_address1 = "12010";  //燒錄狀態 PC給PLC
                contact_address2 = "12011";  //燒錄心跳 PC給PLC
            }
            set_plc_m_status(contact_address1, HIGH);
            set_plc_m_status(contact_address2, pc_breathe_status);
        }

        private void timer_pc_breathe2_Tick(object sender, EventArgs e)
        {
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

        private void bt_check_plc_breathe2_Click(object sender, EventArgs e)
        {
            if (flag_pc_check_plc_breathe_mode != MODE_OFF) //busy
            {
                richTextBox_plc.Text += "忙線中\n";
                return;
            }

            richTextBox_plc.Text += "PC檢查PLC之心跳 for 色調\n";
            bt_check_plc_breathe2.BackColor = Color.Blue;
            flag_pc_check_plc_breathe_mode = MODE_AWB;          //0: MODE_WRITE_DATA 燒錄, 1: MODE_AWB 色調
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
                bt_check_plc_breathe2.BackColor = Color.Lime;
            }
            else
            {
                bt_check_plc_breathe2.BackColor = Color.Red;
            }
        }

        private void bt_automation_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        private void bt_automation_exit_Click(object sender, EventArgs e)
        {
            exit_program();
        }

        void do_test_plc()
        {
            richTextBox_plc.Text += "檢查資料\n";
            int i;
            int rrrr;
            Random r = new Random();
            bool status;

            string contact_address = string.Empty;

            //M10000
            contact_address = (10000 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10000_value = 1;
            }
            else
            {
                m10000_value = 0;
            }
            richTextBox_plc.Text += "讀取: M" + contact_address + ", 結果 :" + status + "\n";

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10000_data[i] = m10000_data[i + 1];
            }
            m10000_data[N - 1] = m10000_value;

            if (m10000_value == 1)
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M10001
            contact_address = (10001 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10001_value = 1;
            }
            else
            {
                m10001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10001_data[i] = m10001_data[i + 1];
            }
            m10001_data[N - 1] = m10001_value;

            if (m10001_value == 1)
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M10002
            contact_address = (10002 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m10002_value = 1;
            }
            else
            {
                m10002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m10002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m10002_data[i] = m10002_data[i + 1];
            }
            m10002_data[N - 1] = m10002_value;

            if (m10002_value == 1)
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12000
            contact_address = (12000 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12000_value = 1;
            }
            else
            {
                m12000_value = 0;
            }
            richTextBox_plc.Text += "讀取: M" + contact_address + ", 結果 :" + status + "\n";

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12000_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12000_data[i] = m12000_data[i + 1];
            }
            m12000_data[N - 1] = m12000_value;

            if (m12000_value == 1)
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12001
            contact_address = (12001 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12001_value = 1;
            }
            else
            {
                m12001_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12001_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12001_data[i] = m12001_data[i + 1];
            }
            m12001_data[N - 1] = m12001_value;

            if (m12001_value == 1)
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            //M12002
            contact_address = (12002 + plc_m_address_offset).ToString();
            status = get_plc_m_status(contact_address);
            if (status == true)
            {
                m12002_value = 1;
            }
            else
            {
                m12002_value = 0;
            }

            if (cb_debug.Checked == true)
            {
                rrrr = r.Next(0, 2);
                m12002_value = rrrr;
            }

            for (i = 0; i < (N - 1); i++)
            {
                m12002_data[i] = m12002_data[i + 1];
            }
            m12002_data[N - 1] = m12002_value;

            if (m12002_value == 1)
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_green;
            }
            else
            {
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
            }
            delay(DELAY_TIME);

            if ((flag_use_real_plc == true) || (plc_simulator_step != 0))
            {
                contact_address = (2000 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                string data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD2000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc3b.Text = data_read;
                richTextBox_plc.Text += "讀取: D" + contact_address + ", 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                contact_address = (2010 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: D" + contact_address + ", 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                /*
                contact_address = (8000 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);

                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc3b.Text = data_read;
                richTextBox_plc.Text += "讀取: D" + contact_address + ", 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                contact_address = (8010 + plc_d_address_offset).ToString();
                show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
                data_read = get_plc_d_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_pc_plc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: D" + contact_address + ", 結果 :" + data_read + "\n";
                */

                contact_address = "1063";
                data_read = get_plc_w_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: W" + contact_address + "(時), 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                contact_address = "1064";
                data_read = get_plc_w_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: W" + contact_address + "(分), 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                contact_address = "1065";
                data_read = get_plc_w_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: W" + contact_address + "(秒), 結果 :" + data_read + "\n";
                delay(DELAY_TIME);

                contact_address = "1066";
                data_read = get_plc_w_data(contact_address);
                //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
                //richTextBox_plc.Text += "data : |" + data_read + "|\n";
                lb_plc_pc4b.Text = data_read;
                richTextBox_plc.Text += "讀取: W" + contact_address + "(設備狀態), 結果 :" + data_read + "\n";
                delay(DELAY_TIME);
            }
        }

        private void cb_test_plc_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_test_plc.Checked == true)
                timer_plc_status.Interval = 2000;
            else
                timer_plc_status.Interval = 1000;
        }
    }
}


/*

erase_plc_d_data("8020", 6);    //清除年月日時分秒的資料






*/