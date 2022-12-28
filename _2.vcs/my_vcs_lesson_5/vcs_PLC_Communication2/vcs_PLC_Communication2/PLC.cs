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

using vcs_PLC_Communication2.PLC_Communication;

namespace vcs_PLC_Communication2
{
    /// <summary>
    ///  PLC--按鈕狀態
    /// </summary>
    public enum Button_state
    {
        Off, ON
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
        bool flag_use_plc_simulator = false;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        private const Button_state HIGH = Button_state.ON;
        private const Button_state LOW = Button_state.Off;
        private const int BORDER = 10;
        private const int PLC_PANEL_WIDTH = 1380;
        private const int PLC_PANEL_HEIGHT = 720;
        private const int PLC_RTB_WIDTH = 350;
        private const int PLC_RTB_HEIGHT = PLC_PANEL_HEIGHT - BORDER * 2;
        private const int PLC_GBOX_WIDTH = PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER * 3;
        private const int PLC_GBOX_HEIGHT = PLC_PANEL_HEIGHT - BORDER * 2;
        private const int PLC_BTN_WIDTH = 50;
        private const int PLC_BTN_HEIGHT = 50;
        private const int DELAY_TIME = 5;

        //Panel PLC initial location
        private const int PANEL_PLC_DEFAULT_POSITION_X = BORDER;
        private const int PANEL_PLC_DEFAULT_POSITION_Y = BORDER;
        int panel_plc_position_x_old = PANEL_PLC_DEFAULT_POSITION_X;
        int panel_plc_position_y_old = PANEL_PLC_DEFAULT_POSITION_Y;

        Stopwatch stopwatch_plc = new Stopwatch();

        Panel panel_plc = new Panel();

        GroupBox groupBox_plc = new GroupBox();
        Button bt_plc_test = new Button();
        Button bt_plc_test_break = new Button();
        PictureBox pictureBox_plc = new PictureBox();
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

        Button bt_copy_to_clipboard = new Button();
        Button bt_plc_clear = new Button();
        RichTextBox richTextBox_plc = new RichTextBox();
        Label lb_plc_main_mesg1 = new Label();
        Label lb_plc_main_mesg2 = new Label();
        Timer timer_plc_status = new Timer();
        Timer timer_plc_display = new Timer();
        Timer timer_plc_simulator = new Timer();


        bool flag_plc_test = false;
        bool flag_plc_test_busy = false;
        bool flag_plc_test_break = false;
        int flag_plc_test_count = 0;

        void add_automation_controls()
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

            timer_plc_status.Enabled = true;
            timer_plc_status.Interval = 1000;
            timer_plc_status.Tick += new System.EventHandler(timer_plc_status_Tick);
            timer_plc_display.Tick += new System.EventHandler(timer_plc_display_Tick);

            if (flag_use_plc_simulator == true)
            {
                this.plC_Open_Time1.Enabled = false;
                this.plC_Open_Time1.Mitsubishi_Open = false;
                this.plC_Open_Time1.Stop();

                timer_plc_simulator.Enabled = true;
            }
            else
            {
                timer_plc_simulator.Enabled = false;
            }
            timer_plc_simulator.Interval = 1000;
            timer_plc_simulator.Tick += new System.EventHandler(timer_plc_simulator_Tick);

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
            this.panel_plc.Controls.Add(groupBox_plc);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test.Width = 90;
            bt_plc_test.Height = 70;
            bt_plc_test.Text = "PLC交握測試";
            bt_plc_test.Name = "bt_plc_test";
            bt_plc_test.Location = new Point(10, 20);
            // 加入按鈕事件
            //bt_plc_test.Click += new EventHandler(bt_plc_test_Click);   //same
            bt_plc_test.Click += bt_plc_test_Click;
            this.groupBox_plc.Controls.Add(bt_plc_test);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test_break.Width = 90;
            bt_plc_test_break.Height = 70;
            bt_plc_test_break.Text = "PLC交握測試 break";
            bt_plc_test_break.Name = "bt_plc_test_break";
            bt_plc_test_break.Location = new Point(110, 20);
            // 加入按鈕事件
            //bt_plc_test_break.Click += new EventHandler(bt_plc_test_break_Click);   //same
            bt_plc_test_break.Click += bt_plc_test_break_Click;
            bt_plc_test_break.MouseDown += bt_plc_test_break_MouseDown;
            this.groupBox_plc.Controls.Add(bt_plc_test_break);     // 將控件加入表單

            pictureBox_plc.Location = new Point(210, 15);
            pictureBox_plc.Name = "pictureBox_plc";
            pictureBox_plc.Size = new Size(400, 75);
            this.groupBox_plc.Controls.Add(pictureBox_plc);     // 將控件加入表單

            cb_debug.Location = new Point(650, 80);
            cb_debug.Name = "cb_debug";
            cb_debug.Text = "Debug";
            cb_debug.Size = new Size(55, 16);
            this.groupBox_plc.Controls.Add(cb_debug);     // 將控件加入表單

            lb_plc_main_mesg1.AutoSize = true;
            lb_plc_main_mesg1.Name = "lb_plc_main_mesg1";
            lb_plc_main_mesg1.Text = "";
            lb_plc_main_mesg1.Font = new Font("Arial", 18.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            lb_plc_main_mesg1.ForeColor = Color.Red;
            lb_plc_main_mesg1.Size = new System.Drawing.Size(78, 24);
            lb_plc_main_mesg1.Location = new Point(groupBox_plc.Location.X + groupBox_plc.Width - 250, 10);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg1);     // 將控件加入表單

            lb_plc_main_mesg2.AutoSize = true;
            lb_plc_main_mesg2.Name = "lb_plc_main_mesg2";
            lb_plc_main_mesg2.Text = "";
            lb_plc_main_mesg2.Font = new Font("Arial", 18.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            lb_plc_main_mesg2.ForeColor = Color.Red;
            lb_plc_main_mesg2.Size = new System.Drawing.Size(138, 44);
            lb_plc_main_mesg2.Location = new Point(groupBox_plc.Location.X + groupBox_plc.Width - 250, 50 + 10);
            this.groupBox_plc.Controls.Add(lb_plc_main_mesg2);     // 將控件加入表單

            lb_plc_pc0.Text = "";
            lb_plc_pc0.Font = new Font("新細明體", 16);
            lb_plc_pc0.ForeColor = Color.Black;
            lb_plc_pc0.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc0);     // 將控件加入表單

            lb_plc_pc1.Text = "";
            lb_plc_pc1.Font = new Font("新細明體", 16);
            lb_plc_pc1.ForeColor = Color.Black;
            lb_plc_pc1.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc1);     // 將控件加入表單

            lb_plc_pc2.Text = "";
            lb_plc_pc2.Font = new Font("新細明體", 16);
            lb_plc_pc2.ForeColor = Color.Black;
            lb_plc_pc2.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc2);     // 將控件加入表單

            lb_plc_pc3a.Text = "";
            lb_plc_pc3a.Font = new Font("新細明體", 16);
            lb_plc_pc3a.ForeColor = Color.Black;
            lb_plc_pc3a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc3a);     // 將控件加入表單

            lb_plc_pc4a.Text = "";
            lb_plc_pc4a.Font = new Font("新細明體", 16);
            lb_plc_pc4a.ForeColor = Color.Black;
            lb_plc_pc4a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc4a);     // 將控件加入表單

            lb_plc_pc3b.Text = "";
            lb_plc_pc3b.Font = new Font("新細明體", 16);
            lb_plc_pc3b.ForeColor = Color.Blue;
            lb_plc_pc3b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc3b);     // 將控件加入表單

            lb_plc_pc4b.Text = "";
            lb_plc_pc4b.Font = new Font("新細明體", 16);
            lb_plc_pc4b.ForeColor = Color.Blue;
            lb_plc_pc4b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_plc_pc4b);     // 將控件加入表單

            // 實例化控件
            lb_pc_plc0.Text = "";
            lb_pc_plc0.Font = new Font("新細明體", 16);
            lb_pc_plc0.ForeColor = Color.Black;
            lb_pc_plc0.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc0);     // 將控件加入表單

            lb_pc_plc1.Text = "";
            lb_pc_plc1.Font = new Font("新細明體", 16);
            lb_pc_plc1.ForeColor = Color.Black;
            lb_pc_plc1.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc1);     // 將控件加入表單

            lb_pc_plc2.Text = "";
            lb_pc_plc2.Font = new Font("新細明體", 16);
            lb_pc_plc2.ForeColor = Color.Black;
            lb_pc_plc2.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc2);     // 將控件加入表單

            lb_pc_plc3a.Text = "";
            lb_pc_plc3a.Font = new Font("新細明體", 16);
            lb_pc_plc3a.ForeColor = Color.Black;
            lb_pc_plc3a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc3a);     // 將控件加入表單

            lb_pc_plc4a.Text = "";
            lb_pc_plc4a.Font = new Font("新細明體", 16);
            lb_pc_plc4a.ForeColor = Color.Black;
            lb_pc_plc4a.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc4a);     // 將控件加入表單

            lb_pc_plc3b.Text = "";
            lb_pc_plc3b.Font = new Font("新細明體", 16);
            lb_pc_plc3b.ForeColor = Color.Blue;
            lb_pc_plc3b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc3b);     // 將控件加入表單

            lb_pc_plc4b.Text = "";
            lb_pc_plc4b.Font = new Font("新細明體", 16);
            lb_pc_plc4b.ForeColor = Color.Blue;
            lb_pc_plc4b.AutoSize = true;
            this.groupBox_plc.Controls.Add(lb_pc_plc4b);     // 將控件加入表單

            lb_read_write_plc.Text = "";
            lb_read_write_plc.Font = new Font("新細明體", 16);
            lb_read_write_plc.ForeColor = Color.Black;
            lb_read_write_plc.AutoSize = true;

            // 實例化按鈕
            bt_open_folder.Width = PLC_BTN_WIDTH;
            bt_open_folder.Height = PLC_BTN_HEIGHT;
            bt_open_folder.Text = "";
            bt_open_folder.Name = "bt_save";
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
            bt_pause.Name = "bt_save";
            // 加入按鈕事件
            //bt_pause.Click += new EventHandler(bt_pause_Click);   //same
            bt_pause.Click += bt_pause_Click;

            int x_st = 10;
            int y_st = 110;
            int dx = PLC_GBOX_WIDTH * 45 / 100;
            int dy = 30;
            int w = 30;
            int h = 30;
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

            lb_plc_pc0.Text = "M10000 PLC -> PC 動作要求";
            lb_plc_pc1.Text = "M10001 PLC -> PC 確認完成";
            lb_plc_pc2.Text = "M10002 PLC -> PC 收到動作完成";
            lb_pc_plc0.Text = "M12000 PC -> PLC 收到動作要求";
            lb_pc_plc1.Text = "M12001 PC -> PLC 確認開始";
            lb_pc_plc2.Text = "M12002 PC -> PLC 動作完成";
            lb_plc_pc3a.Text = "ID資料    D2000";
            lb_plc_pc4a.Text = "收到結果D2010";
            lb_plc_pc3b.Text = "";
            lb_plc_pc4b.Text = "";
            lb_pc_plc3a.Text = "ID資料    D8000";
            lb_pc_plc4a.Text = "檢測結果D8010";
            lb_pc_plc3b.Text = "";
            lb_pc_plc4b.Text = "";
            lb_read_write_plc.Text = "";

            pbx_plc_status.Size = new Size(w * 3, h * 3);
            pbx_plc_status.Location = new Point(groupBox_plc.Location.X + groupBox_plc.Width - w * 4, h * 5);
            pbx_plc_status.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_plc_status.BackgroundImage = Properties.Resources.ball_gray;
            pictureBox_plc_status.Location = new Point(BORDER, y_st + dy * 5);
            pictureBox_plc_status.Size = new Size(PLC_PANEL_WIDTH - PLC_RTB_WIDTH - BORDER * 5, PLC_GBOX_HEIGHT - pictureBox_plc_status.Location.Y - BORDER);

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
                panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
            }
        }
        private void Panel_plc_MouseUp(object sender, MouseEventArgs e)
        {
            flag_panel_plc_mouse_down = false;
            //richTextBox_plc.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - panel_plc_position_x_old;
            int dy = e.Y - panel_plc_position_y_old;

            //richTextBox_plc.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            panel_plc.Location = new Point(panel_plc.Location.X + dx, panel_plc.Location.Y + dy);
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
            if (flag_plc_test == true)
            {
                pictureBox_plc.BackColor = Color.White;
            }
            else
            {
                pictureBox_plc.BackColor = SystemColors.ControlLight;
            }
            update_plc_test_status_data();
            draw_plc_test_status();

            bool plc_power_status = check_plc_power_status();

            if (cb_debug.Checked == true)
            {
                plc_power_status = true;
            }

            if (plc_power_status == false)
            {
                lb_plc_pc3b.Text = "";
                lb_plc_pc4b.Text = "";
                lb_pc_plc3b.Text = "";
                lb_pc_plc4b.Text = "";
                pbx_m10000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m10002.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12000.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12001.BackgroundImage = Properties.Resources.ball_gray;
                pbx_m12002.BackgroundImage = Properties.Resources.ball_gray;
                pbx_plc_status.BackgroundImage = Properties.Resources.ball_gray;
                lb_plc_main_mesg2.Text = "三菱PLC 不 Ready";
                lb_plc_main_mesg2.Visible = true;
                //groupBox_plc.Enabled = false;
                //pictureBox_plc_status.Enabled = false;
                return;
            }
            else
            {
                lb_plc_main_mesg2.Text = "";
                lb_plc_main_mesg2.Visible = false;
                //groupBox_plc.Enabled = true;
                //pictureBox_plc_status.Enabled = true;
                pbx_plc_status.BackgroundImage = Properties.Resources.ball_green2;
            }

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

            if (flag_use_plc_simulator == true)
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

        void draw_plc_test_status()
        {
            int W = pictureBox_plc.Width;
            int H = pictureBox_plc.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            if (flag_plc_test == false)
            {
                g.Clear(SystemColors.ControlLight);
            }
            else
            {
                g.Clear(Color.White);
            }

            //畫X軸 Y軸
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x_st = W * 10 / 100;
            int x_sp = W * 90 / 100;
            int y_st = H * 10 / 100;
            int y_sp = H * 90 / 100;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            int hh = h * 5 / 10;
            int step = w / (N - 1);

            //richTextBox_plc.Text += "step  = " + step.ToString() + " ";

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            //Pen grayPen = new Pen(Color.Gray, 9);
            List<Point> points = new List<Point>();

            int i;
            int x;
            int y;
            int pt_new = 0;
            int pt_old = 0;

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
                        y = H - y_st - hh * pt_old;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }

                x = x_st + step * i;
                y = H - y_st - hh * plc_test_status_data[i];
                //y = H - y_st - (h / 2) * plc_test_status_data[i] - 5 - (h / 7) * 5 - dd * 5;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString(flag_plc_test_count.ToString(), new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 20, H - 50));

            pictureBox_plc.Image = bitmap1;

            g.Dispose();
        }

        void update_plc_data_status_data()
        {
            int i;
            int rrrr;
            Random r = new Random();
            bool status;

            string contact_address = "10000";

            //M10000
            contact_address = "10000";
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
            contact_address = "10001";
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
            contact_address = "10002";
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
            contact_address = "12000";
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
            contact_address = "12001";
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
            contact_address = "12002";
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

            contact_address = "2000";
            show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
            string data_read = get_plc_d_data(contact_address);
            //richTextBox_plc.Text += "\nD2000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox_plc.Text += "data : |" + data_read + "|\n";
            lb_plc_pc3b.Text = data_read;
            delay(DELAY_TIME);

            contact_address = "2010";
            show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox_plc.Text += "data : |" + data_read + "|\n";
            lb_plc_pc4b.Text = data_read;
            delay(DELAY_TIME);

            contact_address = "8000";
            show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox_plc.Text += "data : |" + data_read + "|\n";
            lb_pc_plc3b.Text = data_read;
            delay(DELAY_TIME);

            contact_address = "8010";
            show_plc_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox_plc.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox_plc.Text += "data : |" + data_read + "|\n";
            lb_pc_plc4b.Text = data_read;
        }

        void draw_status()
        {
            int W = pictureBox_plc_status.Width;
            int H = pictureBox_plc_status.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            //畫X軸 Y軸
            Point px1 = new Point(W * 10 / 100, H * 90 / 100);
            Point px2 = new Point(W * 90 / 100, H * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            Point py1 = new Point(W * 10 / 100, H * 90 / 100);
            Point py2 = new Point(W * 10 / 100, H * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);

            int x_st = W * 10 / 100;
            int x_sp = W * 90 / 100;
            int y_st = H * 10 / 100;
            int y_sp = H * 90 / 100;
            int w = x_sp - x_st;
            int h = y_sp - y_st;
            int step = w / (N - 1);

            //richTextBox_plc.Text += "step  = " + step.ToString() + " ";

            // Create pens.
            Pen redPen = new Pen(Color.Red, 3);
            //Pen grayPen = new Pen(Color.Gray, 9);
            List<Point> points = new List<Point>();

            int i;
            int x;
            int y;
            int dd = 8;
            int pt_new = 0;
            int pt_old = 0;

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 5 - dd * 5;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m10000_data[i] - 5 - (h / 7) * 5 - dd * 5;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M10000", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 5 - dd * 5));

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 4 - dd * 4;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m10001_data[i] - 5 - (h / 7) * 4 - dd * 4;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M10001", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 4 - dd * 4));

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 3 - dd * 3;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m10002_data[i] - 5 - (h / 7) * 3 - dd * 3;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M10002", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 3 - dd * 3));

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 2 - dd * 2;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m12000_data[i] - 5 - (h / 7) * 2 - dd * 2;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M12000", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 2 - dd * 2));

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 1 - dd * 1;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m12001_data[i] - 5 - (h / 7) * 1 - dd * 1;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M12001", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 1 - dd * 1));

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
                        y = H - y_st - (h / 7) * pt_old - 5 - (h / 7) * 0 - dd * 0;
                        points.Add(new Point(x, y));
                        pt_old = pt_new;
                    }
                }
                x = x_st + step * i;
                y = H - y_st - (h / 7) * m12002_data[i] - 5 - (h / 7) * 0 - dd * 0;
                points.Add(new Point(x, y));
            }
            g.DrawLines(redPen, points.ToArray());  //畫直線
            g.DrawString("M12002", new Font("標楷體", 15), new SolidBrush(Color.Green), new PointF(x_st - 70, H - y_st - (h / 7) * 1 - 5 - (h / 7) * 0 - dd * 0));

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
            if (flag_use_plc_simulator == true)
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

        void set_plc_d_data(string contact_address, string write_data)
        {
            if (flag_use_plc_simulator == true)
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

        void set_plc_d_data_bcd16(string contact_address, string write_data)
        {
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
            if (flag_use_plc_simulator == true)
            {
                return get_plc_simulator_m_status(contact_address);
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

        void set_plc_m_status(string contact_address, Button_state write_data)
        {
            if (flag_use_plc_simulator == true)
            {
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

        void polling_m_status(string contact_address, Button_state polling_status)
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

            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12002";
            ret = get_plc_m_status(contact_address);
            richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
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

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            //richTextBox_plc.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";
            if (ret == true)
                all_plc_m_status = false;

            contact_address = "12002";
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
            int i;
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

            richTextBox_plc.Text += "(0) PC 啟動完成, 偵測PLC之M10000信號\n";
            richTextBox_plc.Text += "(1) PLC 把相機序號資料放在 D2000\n";
            richTextBox_plc.Text += "(2a) PLC 拉高 M10000, 供PC讀取, 通知條碼內容已備便\n";
            //richTextBox_plc.Text += "[M status] M10000 HIGH\n";

            richTextBox_plc.Text += "(3a) PC 讀取 M10000 狀態\t=>\t";
            contact_address = "10000";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }
            richTextBox_plc.Text += "\n(3b) PC 取得 M10000 為 ON\n";
            flag_plc_test_busy = true;
            flag_plc_test_count++;

            //開始計時
            richTextBox_plc.Text += "時間1 : " + DateTime.Now.ToString() + "\n";
            stopwatch_plc = new Stopwatch();
            stopwatch_plc.Start();

            richTextBox_plc.Text += "(3c) PC 讀取 D2000 資料\n";

            show_plc_main_message1("讀取 D2000", S_OK, 30);
            contact_address = "2000";
            string data_read = string.Empty;

            while (data_read.Length <= 0)
            {
                data_read = get_plc_d_data(contact_address);
            }

            richTextBox_plc.Text += "取得 D2000 資料 : " + data_read + "\n";
            //richTextBox_plc.Text += "\nlen = " + data_read.Length.ToString() + "\n";

            delay(500);

            richTextBox_plc.Text += "\n(3d) PC 將 從 D2000 取得的資料 寫到 D8000\n";

            string data_to_write = data_read.Substring(0, 16);

            //richTextBox_plc.Text += "欲寫入 D8000 資料 : " + data_to_write + ", len = " + data_to_write.Length.ToString() + "\n";

            show_plc_main_message1("寫入 D8000", S_OK, 30);
            contact_address = "8000";
            set_plc_d_data(contact_address, data_to_write);

            delay(500);

            richTextBox_plc.Text += "(4) PC 拉高 M12000, 通知PLC, PC動作已完成\n";
            //richTextBox_plc.Text += "[M status] M12000 HIGH\n";

            contact_address = "12000";
            timer_plc_status_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox_plc.Text += "(5a) PLC收到 PC訊號 M12000 ON時,PLC確認資料一致\n";
            richTextBox_plc.Text += "(5b) PLC 拉高 M10001, 供PC讀取, 通知開始做色調\n";
            //richTextBox_plc.Text += "[M status] M10001 HIGH\n";

            richTextBox_plc.Text += "(6a) PC 讀取 M10001 狀態\t=>\t";
            contact_address = "10001";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(6b) PC 取得 M10001 為 ON\n";

            richTextBox_plc.Text += "(6c) PC 拉高 M12001, 供PLC讀取, 通知PC已開始做色調\n";
            //richTextBox_plc.Text += "[M status] M12001 HIGH\n";

            contact_address = "12001";
            set_plc_m_status(contact_address, HIGH);

            richTextBox_plc.Text += "\nPC開始做色調........";
            for (i = 0; i < 30; i++)
            {
                delay(50);
                richTextBox_plc.Text += ". ";
            }
            richTextBox_plc.Text += "\n\n(7) PC 做完色調, 將結果碼寫在 D8010\t";

            Random r = new Random();
            int color_result = r.Next(1, 20);
            richTextBox_plc.Text += "色調結果: 0x" + color_result.ToString("X2") + " = " + color_result.ToString() + "\n";
            contact_address = "8010";
            string write_data = color_result.ToString();
            show_plc_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16(contact_address, write_data);

            richTextBox_plc.Text += "(8) PC 拉高 M12002, 供PLC讀取, 通知PC已做完色調\n";
            //richTextBox_plc.Text += "[M status] M12002 HIGH\n";

            delay(500);

            contact_address = "12002";
            timer_plc_status_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox_plc.Text += "(9) PLC偵測到 PC之動作完成信號 M12002, PLC設定 M10002為ON\n";
            //richTextBox_plc.Text += "[M status] M10002 HIGH\n";

            richTextBox_plc.Text += "(10a) PC 檢測 M10002 和 M12002\n";

            richTextBox_plc.Text += "(10a1) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(10a2) PC 取得 M10002 為 ON\n";

            richTextBox_plc.Text += "(10a3) PC 讀取 M12002 狀態\t=>\t";
            contact_address = "12002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(10a4) PC 取得 M12002 為 ON\n";

            delay(500);

            richTextBox_plc.Text += "(10b) PC 清除 D8000 ~ D8007 資料\n";
            erase_plc_d_data(contact_address, 8);

            richTextBox_plc.Text += "(10c) PC 令 (收到動作要求信號)M12000 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12000 LOW\n";
            contact_address = "12000";
            set_plc_m_status(contact_address, LOW);

            richTextBox_plc.Text += "(10d) PC 令 (動作執行信號)M12001 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12001 LOW\n";
            contact_address = "12001";
            set_plc_m_status(contact_address, LOW);

            //richTextBox_plc.Text += "[M status] M10000 LOW\n";
            //richTextBox_plc.Text += "[M status] M10001 LOW\n";

            delay(500);

            richTextBox_plc.Text += "(10e) PLC 清除 D2000 ~ D2006 資料\n";
            richTextBox_plc.Text += "(10f) PLC 令 (動作要求訊號)M10000 為 OFF\n";
            richTextBox_plc.Text += "(10g) PLC 令 (動作開始要求訊號)M10001 為 OFF\n";

            delay(500);

            richTextBox_plc.Text += "(11a) PC 檢測 (PLC動作完成信號)M10002\n";
            //當PC收到PLC收到動作完成訊號M10002 ON之後,結果碼D8010資料清除
            //PC->PLC動作完成訊號M12002 OFF

            richTextBox_plc.Text += "(11a) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(11b) PC 取得 M10002 為 ON\n";

            richTextBox_plc.Text += "(11c) PC 清除 D8010資料\n";
            //contact_address = "8010";
            //erase_plc_d_data(contact_address, 1);

            richTextBox_plc.Text += "(11d) PC 令 M12002 為 OFF\n";
            //richTextBox_plc.Text += "[M status] M12002 LOW\n";
            contact_address = "12002";
            set_plc_m_status(contact_address, LOW);

            delay(500);

            richTextBox_plc.Text += "(12a) PLC 收到 PC 設定 M12002 為 OFF, PLC 設定 M10002為OFF\n";
            richTextBox_plc.Text += "[M status] M10002 LOW\n";

            richTextBox_plc.Text += "(12b) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, LOW);
            if (flag_plc_test_break == true)
            {
                richTextBox_plc.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox_plc.Text += "\n(12c) PC 取得 M10002 為 LOW\n";
            get_all_plc_m_status();
            richTextBox_plc.Text += "測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\tOK\n\n\n";

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

            int cnt = 1;
            while (true)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox_plc.Text += "使用者中斷PLC測試, 結束\n";
                    break;
                }
                richTextBox_plc.Text += "第 " + (cnt++).ToString() + " 次測試\n";
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

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (timer_plc_status.Enabled == true)
            {
                timer_plc_status.Enabled = false;
                bt_pause.BackgroundImage = Properties.Resources.play;
            }
            else
            {
                timer_plc_status.Enabled = true;
                bt_pause.BackgroundImage = Properties.Resources.pause;
            }
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive(); //用時間檔名存檔 不檢查序號
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
        bool plc_simulator_power_status = false;
        int m10000_simulator_value = 0;
        int m10001_simulator_value = 0;
        int m10002_simulator_value = 0;
        int m12000_simulator_value = 0;
        int m12001_simulator_value = 0;
        int m12002_simulator_value = 0;
        string d2000_simulator_data = "D2000-DATAD2000-DATA";
        string d2010_simulator_data = "D2010-DATAD2010-DATA";
        string d8000_simulator_data = "D8000-DATAD8000-DATA";
        string d8010_simulator_data = "D8010-DATAD8010-DATA";

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

                    //設定M10000 10001 10002 信號為0
                    contact_address = "10000";
                    set_plc_m_status(contact_address, LOW);
                    contact_address = "10001";
                    set_plc_m_status(contact_address, LOW);
                    contact_address = "10002";
                    set_plc_m_status(contact_address, LOW);
                }
            }
            else if (plc_simulator_step == 1)   //PLC Power ON
            {
                if (plc_simulator_count < 5)
                {
                    //檢查M10000 10001 10002 M12000 12001 12002 信號是否皆為0
                    contact_address = "10000";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M10000 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                    contact_address = "10001";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M10001 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                    contact_address = "10002";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M10002 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                    contact_address = "12000";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M12000 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                    contact_address = "12001";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M12001 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                    contact_address = "12002";
                    status = get_plc_m_status(contact_address);
                    if (status == true)
                    {
                        richTextBox_plc.Text += "M12002 不該為 HIGH\n";
                        plc_simulator_count = 0;
                    }
                }
                else
                {
                    richTextBox_plc.Text += "\n[PLC] 開始PLC測試\n";
                    plc_simulator_count = 0;
                    plc_simulator_step = 2;

                    richTextBox_plc.Text += "[PLC] 把相機序號資料放在 D2000\n";

                    contact_address = "2000";
                    string write_data = "A123456789B1234";
                    show_plc_main_message1("PLC 寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
                    set_plc_d_data_bcd16(contact_address, write_data);

                    richTextBox_plc.Text += "[PLC] PLC 拉高 M10000, 供PC讀取, 通知條碼內容已備便\n";
                    richTextBox_plc.Text += "[PLC] 令 M10000 為 HIGH\n";
                    contact_address = "10000";
                    set_plc_m_status(contact_address, HIGH);
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
                    contact_address = "12000";
                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未備便 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 已備便\n";
                        richTextBox_plc.Text += "[PLC] PLC 拉高 M10001, 供PC讀取, 通知開始做色調\n";

                        plc_simulator_count = 0;
                        plc_simulator_step = 3;

                        contact_address = "10001";
                        set_plc_m_status(contact_address, HIGH);
                    }
                }
            }
            else if (plc_simulator_step == 3)   //PLC等待PC做色調
            {
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12002 是否為 HIGH, 若是, 代表PC已做完色調\n";
                    bool ret = false;
                    contact_address = "12002";
                    ret = get_plc_m_status(contact_address);
                    if (ret == false)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成色調 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 已完成色調完成信號 M12002, PLC設定 M10002為ON\n";

                        plc_simulator_count = 0;
                        plc_simulator_step = 4;

                        contact_address = "10002";
                        set_plc_m_status(contact_address, HIGH);
                    }
                }
            }
            else if (plc_simulator_step == 4)
            {
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                    //richTextBox_plc.Text += "[PLC] PLC 檢查 M12001 是否為 LOW, 若是, 代表PC已做完\n";
                    bool ret = false;
                    contact_address = "12001";
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC 之動作完成信號 M12001 為 LOW, PLC設定 M10002 為 HIGH\n";

                        plc_simulator_count = 0;
                        plc_simulator_step = 5;

                        contact_address = "10002";
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
                    contact_address = "12002";
                    ret = get_plc_m_status(contact_address);
                    if (ret == true)
                    {
                        //richTextBox_plc.Text += "[PLC] PLC 檢查 PC 未完成 ";
                        return;
                    }
                    else
                    {
                        richTextBox_plc.Text += "\n[PLC] PLC 檢查 PC之動作完成信號 M12002 為 LOW\n";
                        richTextBox_plc.Text += "[PLC] PLC設定 M10002 為 LOW\n";
                        contact_address = "10002";
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M10001 為 LOW\n";
                        contact_address = "10001";
                        set_plc_m_status(contact_address, LOW);
                        richTextBox_plc.Text += "[PLC] PLC設定 M10000 為 LOW\n";
                        contact_address = "10000";
                        set_plc_m_status(contact_address, LOW);

                        plc_simulator_count = 0;
                        plc_simulator_step = 6;

                    }

                }
            }
            else if (plc_simulator_step == 6)
            {
                richTextBox_plc.Text += plc_simulator_step.ToString() + " ";
                get_all_plc_m_status();
                //收尾

                if (plc_simulator_count < 3)
                {

                }
                else
                {
                }
            }
            else if (plc_simulator_step == 7)
            {
                richTextBox_plc.Text += plc_simulator_step.ToString() + " ";
                if (plc_simulator_count < 3)
                {

                }
                else
                {
                }
            }
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
                if (contact_address == "10000")
                {
                    m_status = m10000_simulator_value;
                }
                else if (contact_address == "10001")
                {
                    m_status = m10001_simulator_value;
                }
                else if (contact_address == "10002")
                {
                    m_status = m10002_simulator_value;
                }
                else if (contact_address == "12000")
                {
                    m_status = m12000_simulator_value;
                }
                else if (contact_address == "12001")
                {
                    m_status = m12001_simulator_value;
                }
                else if (contact_address == "12002")
                {
                    m_status = m12002_simulator_value;
                }
                else
                {
                    richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 1\n";
                }
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

        void set_plc_simulator_m_status(string contact_address, Button_state write_data)
        {
            //richTextBox_plc.Text += "模擬寫了 M" + contact_address + ", 資料為: " + write_data.ToString() + "\n";
            if (contact_address == "10000")
            {
                m10000_simulator_value = (int)write_data;
            }
            else if (contact_address == "10001")
            {
                m10001_simulator_value = (int)write_data;
            }
            else if (contact_address == "10002")
            {
                m10002_simulator_value = (int)write_data;
            }
            else if (contact_address == "12000")
            {
                m12000_simulator_value = (int)write_data;
            }
            else if (contact_address == "12001")
            {
                m12001_simulator_value = (int)write_data;
            }
            else if (contact_address == "12002")
            {
                m12002_simulator_value = (int)write_data;
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 2\n";
            }
        }

        string get_plc_simulator_d_data(string contact_address)
        {
            string plc_simulator_d_data = string.Empty;

            if (contact_address == "2000")
            {
                plc_simulator_d_data = d2000_simulator_data;
            }
            else if (contact_address == "2010")
            {
                plc_simulator_d_data = d2010_simulator_data;
            }
            else if (contact_address == "8000")
            {
                plc_simulator_d_data = d8000_simulator_data;
            }
            else if (contact_address == "8010")
            {
                plc_simulator_d_data = d8010_simulator_data;
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 3\n";
            }
            return plc_simulator_d_data;
        }

        void set_plc_simulator_d_data(string contact_address, string write_data)
        {
            //richTextBox_plc.Text += "模擬寫了 D" + contact_address + ", 資料為: " + write_data.ToString() + "\n";

            if (contact_address == "2000")
            {
                d2000_simulator_data = write_data;
            }
            else if (contact_address == "2010")
            {
                d2010_simulator_data = write_data;
            }
            else if (contact_address == "8000")
            {
                d8000_simulator_data = write_data;
            }
            else if (contact_address == "8010")
            {
                d8010_simulator_data = write_data;
            }
            else
            {
                richTextBox_plc.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 4\n";
            }
        }
    }
}
