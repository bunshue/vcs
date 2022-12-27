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

using vcs_PLC_Communication1.PLC_Communication;

namespace vcs_PLC_Communication1
{
    public partial class Form2 : Form
    {
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
        Button bt_clear = new Button();
        RichTextBox richTextBox_plc = new RichTextBox();
        Label lb_plc_main_mesg1 = new Label();
        Label lb_plc_main_mesg2 = new Label();
        Timer timer_plc_status = new Timer();
        Timer timer_plc_display = new Timer();


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

            bt_copy_to_clipboard.Width = PLC_BTN_WIDTH;
            bt_copy_to_clipboard.Height = PLC_BTN_HEIGHT;
            bt_copy_to_clipboard.Text = "";
            bt_copy_to_clipboard.Name = "bt_copy_to_clipboard";
            bt_copy_to_clipboard.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_copy_to_clipboard.Size.Width * 2, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_copy_to_clipboard.Size.Height);
            // 加入按鈕事件
            //bt_copy_to_clipboard.Click += new EventHandler(bt_copy_to_clipboard_Click);   //same
            bt_copy_to_clipboard.Click += bt_copy_to_clipboard_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_copy_to_clipboard;
            this.panel_plc.Controls.Add(bt_copy_to_clipboard);     // 將控件加入表單
            bt_copy_to_clipboard.BringToFront();

            // 實例化按鈕
            bt_clear.Width = PLC_BTN_WIDTH;
            bt_clear.Height = PLC_BTN_HEIGHT;
            bt_clear.Text = "Clear";
            bt_clear.Name = "bt_clear";
            bt_clear.Location = new Point(richTextBox_plc.Location.X + richTextBox_plc.Size.Width - bt_clear.Size.Width, richTextBox_plc.Location.Y + richTextBox_plc.Size.Height - bt_clear.Size.Height);
            // 加入按鈕事件
            //bt_clear.Click += new EventHandler(bt_clear_Click);   //same
            bt_clear.Click += bt_clear_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_clear;
            this.panel_plc.Controls.Add(bt_clear);     // 將控件加入表單
            bt_clear.BringToFront();

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
            // 將按鈕加入表單
            //this.AcceptButton = bt_plc_test;
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


        string get_plc_d_data(string contact_address)
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
            string contact_point = "M";

            if ((contact_address.Length != 4) && (contact_address.Length != 5))
            {
                show_main_message1("位址錯誤", S_OK, 30);
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
    }
}
