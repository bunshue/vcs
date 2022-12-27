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

    public partial class Form2 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        private const Button_state HIGH = Button_state.ON;
        private const Button_state LOW = Button_state.Off;

        Stopwatch stopwatch = new Stopwatch();

        Panel panel_plc = new Panel();

        GroupBox groupBox_plc = new GroupBox();
        Button bt_plc_test = new Button();
        Button bt_plc_test_break = new Button();
        PictureBox pictureBox_plc = new PictureBox();
        CheckBox cb_debug = new CheckBox();

        GroupBox groupBox_plc_status = new GroupBox();
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
        RichTextBox richTextBox1 = new RichTextBox();

        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Enabled = true;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.Start();

            add_automation_controls();

            show_item_location();
        }

        void add_automation_controls()
        {
            // 實例化控件
            panel_plc.BackColor = Color.LightYellow;
            panel_plc.Size = new Size(1500, 650);
            panel_plc.Location = new Point(10, 10);
            this.Controls.Add(panel_plc);     // 將控件加入表單

            groupBox_plc.Text = "";
            groupBox_plc.Size = new Size(800, 100);
            groupBox_plc.Location = new Point(10, 10);
            this.panel_plc.Controls.Add(groupBox_plc);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test.Width = 50;
            bt_plc_test.Height = 50;
            bt_plc_test.Text = "PLC交握測試";
            bt_plc_test.Name = "bt_plc_test";
            bt_plc_test.Location = new Point(17, 29);
            // 加入按鈕事件
            //bt_plc_test.Click += new EventHandler(bt_plc_test_Click);   //same
            bt_plc_test.Click += bt_plc_test_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_plc_test;
            this.groupBox_plc.Controls.Add(bt_plc_test);     // 將控件加入表單

            // 實例化按鈕
            bt_plc_test_break.Width = 50;
            bt_plc_test_break.Height = 50;
            bt_plc_test_break.Text = "PLC交握測試 break";
            bt_plc_test_break.Name = "bt_plc_test_break";
            bt_plc_test_break.Location = new Point(119, 29);
            // 加入按鈕事件
            //bt_plc_test_break.Click += new EventHandler(bt_plc_test_break_Click);   //same
            bt_plc_test_break.Click += bt_plc_test_break_Click;
            bt_plc_test_break.MouseDown += bt_plc_test_break_MouseDown;
            // 將按鈕加入表單
            //this.AcceptButton = bt_plc_test_break;
            this.groupBox_plc.Controls.Add(bt_plc_test_break);     // 將控件加入表單

            pictureBox_plc.Location = new Point(230, 29);
            pictureBox_plc.Name = "pictureBox_plc";
            pictureBox_plc.Size = new Size(100, 50);
            this.groupBox_plc.Controls.Add(pictureBox_plc);     // 將控件加入表單

            //cb_debug.AutoSize = true;
            cb_debug.Location = new Point(groupBox_plc.Width - 60, groupBox_plc.Height - 30);
            cb_debug.Name = "cb_debug";
            cb_debug.Text = "Debug";
            cb_debug.Size = new Size(55, 16);
            this.groupBox_plc.Controls.Add(cb_debug);     // 將控件加入表單

            richTextBox1.Text = "";
            richTextBox1.Name = "richTextBox1";
            richTextBox1.Location = new Point(1100, 10);
            richTextBox1.Size = new Size(380, 600);
            this.panel_plc.Controls.Add(richTextBox1);

            // 實例化按鈕
            bt_copy_to_clipboard.Width = 50;
            bt_copy_to_clipboard.Height = 50;
            bt_copy_to_clipboard.Text = "";
            bt_copy_to_clipboard.Name = "bt_copy_to_clipboard";
            bt_copy_to_clipboard.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_copy_to_clipboard.Size.Width * 2, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_copy_to_clipboard.Size.Height);
            // 加入按鈕事件
            //bt_copy_to_clipboard.Click += new EventHandler(bt_copy_to_clipboard_Click);   //same
            bt_copy_to_clipboard.Click += bt_copy_to_clipboard_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_copy_to_clipboard;
            this.panel_plc.Controls.Add(bt_copy_to_clipboard);     // 將控件加入表單
            bt_copy_to_clipboard.BringToFront();

            // 實例化按鈕
            bt_clear.Width = 50;
            bt_clear.Height = 50;
            bt_clear.Text = "Clear";
            bt_clear.Name = "bt_clear";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            // 加入按鈕事件
            //bt_clear.Click += new EventHandler(bt_clear_Click);   //same
            bt_clear.Click += bt_clear_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_clear;
            this.panel_plc.Controls.Add(bt_clear);     // 將控件加入表單
            bt_clear.BringToFront();

            groupBox_plc_status.Text = "";
            groupBox_plc_status.Size = new Size(980, 505);
            groupBox_plc_status.Location = new Point(10, 120);
            this.panel_plc.Controls.Add(groupBox_plc_status);     // 將控件加入表單

            lb_plc_pc0.Text = "";
            lb_plc_pc0.Font = new Font("新細明體", 16);
            lb_plc_pc0.ForeColor = Color.Black;
            lb_plc_pc0.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc0);     // 將控件加入表單

            lb_plc_pc1.Text = "";
            lb_plc_pc1.Font = new Font("新細明體", 16);
            lb_plc_pc1.ForeColor = Color.Black;
            lb_plc_pc1.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc1);     // 將控件加入表單

            lb_plc_pc2.Text = "";
            lb_plc_pc2.Font = new Font("新細明體", 16);
            lb_plc_pc2.ForeColor = Color.Black;
            lb_plc_pc2.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc2);     // 將控件加入表單

            lb_plc_pc3a.Text = "";
            lb_plc_pc3a.Font = new Font("新細明體", 16);
            lb_plc_pc3a.ForeColor = Color.Black;
            lb_plc_pc3a.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc3a);     // 將控件加入表單

            lb_plc_pc4a.Text = "";
            lb_plc_pc4a.Font = new Font("新細明體", 16);
            lb_plc_pc4a.ForeColor = Color.Black;
            lb_plc_pc4a.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc4a);     // 將控件加入表單

            lb_plc_pc3b.Text = "";
            lb_plc_pc3b.Font = new Font("新細明體", 16);
            lb_plc_pc3b.ForeColor = Color.Blue;
            lb_plc_pc3b.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc3b);     // 將控件加入表單

            lb_plc_pc4b.Text = "";
            lb_plc_pc4b.Font = new Font("新細明體", 16);
            lb_plc_pc4b.ForeColor = Color.Blue;
            lb_plc_pc4b.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_plc_pc4b);     // 將控件加入表單

            // 實例化控件
            lb_pc_plc0.Text = "";
            lb_pc_plc0.Font = new Font("新細明體", 16);
            lb_pc_plc0.ForeColor = Color.Black;
            lb_pc_plc0.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc0);     // 將控件加入表單

            lb_pc_plc1.Text = "";
            lb_pc_plc1.Font = new Font("新細明體", 16);
            lb_pc_plc1.ForeColor = Color.Black;
            lb_pc_plc1.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc1);     // 將控件加入表單

            lb_pc_plc2.Text = "";
            lb_pc_plc2.Font = new Font("新細明體", 16);
            lb_pc_plc2.ForeColor = Color.Black;
            lb_pc_plc2.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc2);     // 將控件加入表單

            lb_pc_plc3a.Text = "";
            lb_pc_plc3a.Font = new Font("新細明體", 16);
            lb_pc_plc3a.ForeColor = Color.Black;
            lb_pc_plc3a.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc3a);     // 將控件加入表單

            lb_pc_plc4a.Text = "";
            lb_pc_plc4a.Font = new Font("新細明體", 16);
            lb_pc_plc4a.ForeColor = Color.Black;
            lb_pc_plc4a.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc4a);     // 將控件加入表單

            lb_pc_plc3b.Text = "";
            lb_pc_plc3b.Font = new Font("新細明體", 16);
            lb_pc_plc3b.ForeColor = Color.Blue;
            lb_pc_plc3b.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc3b);     // 將控件加入表單

            lb_pc_plc4b.Text = "";
            lb_pc_plc4b.Font = new Font("新細明體", 16);
            lb_pc_plc4b.ForeColor = Color.Blue;
            lb_pc_plc4b.AutoSize = true;
            this.groupBox_plc_status.Controls.Add(lb_pc_plc4b);     // 將控件加入表單

            lb_read_write_plc.Text = "";
            lb_read_write_plc.Font = new Font("新細明體", 16);
            lb_read_write_plc.ForeColor = Color.Black;
            lb_read_write_plc.AutoSize = true;

            // 實例化按鈕
            bt_open_folder.Width = 50;
            bt_open_folder.Height = 50;
            bt_open_folder.Text = "";
            bt_open_folder.Name = "bt_save";
            // 加入按鈕事件
            //bt_open_folder.Click += new EventHandler(bt_open_folder_Click);   //same
            bt_open_folder.Click += bt_open_folder_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_open_folder;

            // 實例化按鈕
            bt_save.Width = 50;
            bt_save.Height = 50;
            bt_save.Text = "";
            bt_save.Name = "bt_save";
            // 加入按鈕事件
            //bt_save.Click += new EventHandler(bt_save_Click);   //same
            bt_save.Click += bt_save_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_save;

            // 實例化按鈕
            bt_pause.Width = 50;
            bt_pause.Height = 50;
            bt_pause.Text = "";
            bt_pause.Name = "bt_save";
            // 加入按鈕事件
            //bt_pause.Click += new EventHandler(bt_pause_Click);   //same
            bt_pause.Click += bt_pause_Click;
            // 將按鈕加入表單
            //this.AcceptButton = bt_pause;

            this.groupBox_plc_status.Controls.Add(lb_read_write_plc);   // 將控件加入表單
            this.groupBox_plc_status.Controls.Add(bt_open_folder);      // 將控件加入表單
            this.groupBox_plc_status.Controls.Add(bt_save);     // 將控件加入表單
            this.groupBox_plc_status.Controls.Add(bt_pause);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m10000);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m10001);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m10002);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m12000);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m12001);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_m12002);	// 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pbx_plc_status);  // 將控件加入表單
            this.groupBox_plc_status.Controls.Add(pictureBox_plc_status);  // 將控件加入表單
        }

        void show_item_location()
        {
            this.Size = new Size(1600, 980);

            groupBox1.Location = new Point(10, 700);
            lb_main_mesg1.Visible = true;
            lb_main_mesg1.Text = "";
            bt_copy_to_clipboard.BackgroundImage = Properties.Resources.clipboard;
            bt_copy_to_clipboard.BackgroundImageLayout = ImageLayout.Zoom;
            bt_save.BackgroundImage = Properties.Resources.save;
            bt_save.BackgroundImageLayout = ImageLayout.Zoom;
            bt_open_folder.BackgroundImage = Properties.Resources.open_folder;
            bt_open_folder.BackgroundImageLayout = ImageLayout.Zoom;

            lb_main_mesg1.Location = new Point(450, 182);

            cb_random.Checked = true;

            lb_plc_mesg.Location = new Point(groupBox_plc_status.Location.X + 200, groupBox_plc_status.Location.Y + 155);

            int x_st = 10;
            int y_st = 15;
            int dx = 470;
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
            pbx_plc_status.Size = new Size(w * 3, h * 3);
            pbx_plc_status.Location = new Point(x_st + dx * 2 - 80, y_st + dy * 3 - 70);
            pbx_plc_status.BackgroundImageLayout = ImageLayout.Zoom;
            pbx_plc_status.BackgroundImage = Properties.Resources.ball_gray;
            pictureBox_plc_status.Location = new Point(10, 192);
            pictureBox_plc_status.Size = new Size(960, 300);

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

            bt_open_folder.Location = new Point(904, 294);
            bt_save.Location = new Point(904, 348);
            bt_pause.Location = new Point(904, 402);

            x_st = 230;
            y_st = 20;
            pictureBox_plc.Location = new Point(x_st, y_st);
            pictureBox_plc.Size = new Size(330, groupBox_plc.Height - 30);
            //pictureBox_plc.BackColor = Color.Pink;

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
            lb_plc_mesg.Text = "";
            lb_read_write_plc.Text = "";

            bt_pause.BackgroundImageLayout = ImageLayout.Zoom;
            if (timer1.Enabled == true)
            {
                bt_pause.BackgroundImage = Properties.Resources.pause;
            }
            else
            {
                bt_pause.BackgroundImage = Properties.Resources.play;
            }

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(10, 10);

            // C# 設定視窗載入位置 
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

        }
        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {


        }
        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
        {
            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();
        }

        private void bt_generate_Click(object sender, EventArgs e)
        {
            string random_data = string.Empty;
            if (cb_random.Checked == true)
            {
                random_data = make_random_data();
            }
            else
            {
                random_data = "A1234567B1234";
            }
            richTextBox1.Text += "相機序號：" + random_data + "\n";
            tb_data_d.Text = random_data;
        }

        string make_random_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            string random_data = string.Empty;
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[13];
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
            random_data = new String(stringChars1);
            return random_data;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試 get_plc_m_status()\n";

            string contact_address = "10000";
            bool ret = false;

            contact_address = "10000";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10001";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "10002";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12000";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12001";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "12002";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8000";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8001";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8002";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8012";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            contact_address = "8013";
            ret = get_plc_m_status(contact_address);
            richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            string data_read;
            contact_address = "8013";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8014";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8015";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8016";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8017";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8018";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";

            contact_address = "8019";
            data_read = get_plc_d_data(contact_address);
            richTextBox1.Text += "讀取 D" + contact_address + "\t結果 : " + data_read + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            get_all_plc_m_status();
        }

        private void timer1_Tick(object sender, EventArgs e)
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
                lb_plc_mesg.Text = "三菱PLC 不 Ready";
                lb_plc_mesg.Visible = true;
                groupBox_plc_status.Enabled = false;
                pictureBox_plc_status.Enabled = false;
                return;
            }
            else
            {
                lb_plc_mesg.Text = "";
                lb_plc_mesg.Visible = false;
                groupBox_plc_status.Enabled = true;
                pictureBox_plc_status.Enabled = true;
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
            //讀取 PLC狀態
            IPLC_interface mitsubishi = new Mitsubishi_realize();//實例化接口--實現三菱在線訪問
            if (mitsubishi.PLC_ready == true)   //PLC是否準備完成
            {
                plc_power_status = true;
                /* 目前無法判斷 PLC_read_M_bit 是讀不到資料 還是資料為True/False
                richTextBox1.Text += "check_plc_power_status\n";
                //richTextBox1.Text += "三菱PLC ready 3\n";
                List<bool> data = mitsubishi.PLC_read_M_bit("M", "10000");//讀取狀態
                richTextBox1.Text += "aaaa len = " + data.Count.ToString() + ", data = " + data[0].ToString() + "\n";

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

            //richTextBox1.Text += "step  = " + step.ToString() + " ";

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

            contact_address = "2000";
            show_main_message1("讀取: D" + contact_address, S_OK, 30);
            string data_read = get_plc_d_data(contact_address);
            //richTextBox1.Text += "\nD2000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_plc_pc3b.Text = data_read;

            contact_address = "2010";
            show_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_plc_pc4b.Text = data_read;

            contact_address = "8000";
            show_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
            lb_pc_plc3b.Text = data_read;

            contact_address = "8010";
            show_main_message1("讀取: D" + contact_address, S_OK, 30);
            data_read = get_plc_d_data(contact_address);
            //richTextBox1.Text += "\nD8000 len = " + data_read.Length.ToString() + "\n";
            //richTextBox1.Text += "data : |" + data_read + "|\n";
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

            //richTextBox1.Text += "step  = " + step.ToString() + " ";

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

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_copy_to_clipboard_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_erase_d_Click(object sender, EventArgs e)
        {
            tb_data_d.Text = "";
        }

        private void bt_read_d_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_d.Text;

            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("讀取: M" + contact_address, S_OK, 30);

            string data_read = get_plc_d_data(contact_address);
            tb_data_d.Text = data_read;
        }

        private void bt_write_d_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_d.Text;
            string write_data = tb_data_d.Text;
            tb_data_d.Text = "";

            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }
            if (write_data.Length <= 0)
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }
            if (write_data == "無寫入資料")
            {
                show_main_message1("無資料", S_OK, 30);
                return;
            }

            show_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);

            set_plc_d_data(contact_address, write_data);
        }

        private void bt_erase_m_Click(object sender, EventArgs e)
        {
            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;
        }

        private void bt_read_m_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_m.Text;

            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("讀取: M" + contact_address, S_OK, 30);

            bool ret = get_plc_m_status(contact_address);
            //richTextBox1.Text += "讀取 M" + contact_address + "\t結果 : " + ret.ToString() + "\n";

            if (ret == true)
            {
                tb_data_m.BackColor = Color.Lime;
                tb_data_m.Text = "High";
            }
            else
            {
                tb_data_m.BackColor = Color.Gray;
                tb_data_m.Text = "Low";
            }
        }

        private void bt_write_m_Click(object sender, EventArgs e)
        {
            string contact_address = tb_contact_address_m.Text;

            Button_state button_State;
            if (rb_high.Checked == true)
            {
                button_State = Button_state.ON;
            }
            else
            {
                button_State = Button_state.Off;
            }

            tb_data_m.Text = "";
            tb_data_m.BackColor = Color.White;

            if (contact_address.Length <= 0)
            {
                show_main_message1("無位址", S_OK, 30);
                return;
            }

            show_main_message1("寫入: M" + contact_address + ", 資料: " + button_State, S_OK, 30);

            set_plc_m_status(contact_address, button_State);
        }

        bool flag_plc_test = false;
        bool flag_plc_test_busy = false;
        bool flag_plc_test_break = false;
        int flag_plc_test_count = 0;

        void do_PC_PLC_Communication(object sender, EventArgs e)
        {
            int i;
            string contact_address = String.Empty;
            bool ret = false;

            flag_plc_test_busy = false;
            richTextBox1.Text += "測試PLC作業流程 ST\t" + DateTime.Now.ToString() + "\n";

            richTextBox1.Text += "(0) PC 啟動完成, 檢查PLC是否已開機\n";

            while (ret == false)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    return;
                }
                ret = check_plc_power_status();

                if (ret == true)
                {
                    richTextBox1.Text += "(0) 三菱PLC 已 Ready, 繼續\n";
                }
                else
                {
                    richTextBox1.Text += "(0) 三菱PLC 不 Ready, 等待\n";
                    delay(500);
                }
            }

            richTextBox1.Text += "(0) PC 啟動完成, 檢查所有 M1XXXX 信號 是否皆為 LOW\n";

            while (ret == false)
            {
                if (flag_plc_test_break == true)
                {
                    richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                    return;
                }
                ret = check_all_plc_m_status_low();
                if (ret == true)
                {
                    richTextBox1.Text += "(0) 所有 M1XXXX 信號 皆為 LOW, 繼續\n";
                }
                else
                {
                    richTextBox1.Text += "(0) 有 M1XXXX 信號 不為 LOW, 等待\n";
                    delay(500);
                }
            }

            richTextBox1.Text += "(0) PC 啟動完成, 偵測PLC之M10000信號\n";
            richTextBox1.Text += "(1) PLC 把資料放在 D2000\n";
            richTextBox1.Text += "(2a) PLC 拉高 M10000, 供PC讀取, 通知條碼內容已備便\n";
            //richTextBox1.Text += "[M status] M10000 HIGH\n";

            richTextBox1.Text += "(3a) PC 讀取 M10000 狀態\t=>\t";
            contact_address = "10000";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }
            richTextBox1.Text += "\n(3b) PC 取得 M10000 為 ON\n";
            flag_plc_test_busy = true;
            flag_plc_test_count++;

            //開始計時
            richTextBox1.Text += "時間1 : " + DateTime.Now.ToString() + "\n";
            stopwatch = new Stopwatch();
            stopwatch.Start();

            richTextBox1.Text += "(3c) PC 讀取 D2000 資料\n";

            show_main_message1("讀取 D2000", S_OK, 30);
            contact_address = "2000";
            string data_read = string.Empty;

            while (data_read.Length <= 0)
            {
                data_read = get_plc_d_data(contact_address);
            }

            richTextBox1.Text += "取得 D2000 資料 : " + data_read + "\n";
            //richTextBox1.Text += "\nlen = " + data_read.Length.ToString() + "\n";

            delay(500);

            richTextBox1.Text += "\n(3d) PC 將 從 D2000 取得的資料 寫到 D8000\n";

            string data_to_write = data_read.Substring(0, 16);

            //richTextBox1.Text += "欲寫入 D8000 資料 : " + data_to_write + ", len = " + data_to_write.Length.ToString() + "\n";

            show_main_message1("寫入 D8000", S_OK, 30);
            contact_address = "8000";
            set_plc_d_data(contact_address, data_to_write);

            delay(500);

            richTextBox1.Text += "(4) PC 拉高 M12000, 通知PLC, PC動作已完成\n";
            //richTextBox1.Text += "[M status] M12000 HIGH\n";

            contact_address = "12000";
            timer1_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox1.Text += "(5a) PLC收到 PC訊號 M12000 ON時,PLC確認資料一致\n";
            richTextBox1.Text += "(5b) PLC 拉高 M10001, 供PC讀取, 通知開始做色調\n";
            //richTextBox1.Text += "[M status] M10001 HIGH\n";

            richTextBox1.Text += "(6a) PC 讀取 M10001 狀態\t=>\t";
            contact_address = "10001";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox1.Text += "\n(6b) PC 取得 M10001 為 ON\n";

            richTextBox1.Text += "(6c) PC 拉高 M12001, 供PLC讀取, 通知PC已開始做色調\n";
            //richTextBox1.Text += "[M status] M12001 HIGH\n";

            contact_address = "12001";
            set_plc_m_status(contact_address, HIGH);

            richTextBox1.Text += "\nPC開始做色調........";
            for (i = 0; i < 30; i++)
            {
                delay(50);
                richTextBox1.Text += ". ";
            }
            richTextBox1.Text += "\n\n(7) PC 做完色調, 將結果碼寫在 D8010\t";

            Random r = new Random();
            int color_result = r.Next(1, 20);
            richTextBox1.Text += "色調結果: 0x" + color_result.ToString("X2") + " = " + color_result.ToString() + "\n";
            contact_address = "8010";
            string write_data = color_result.ToString();
            show_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16(contact_address, write_data);

            richTextBox1.Text += "(8) PC 拉高 M12002, 供PLC讀取, 通知PC已做完色調\n";
            //richTextBox1.Text += "[M status] M12002 HIGH\n";

            delay(500);

            contact_address = "12002";
            timer1_Tick(sender, e);
            set_plc_m_status(contact_address, HIGH);

            delay(200);

            richTextBox1.Text += "(9) PLC偵測到 PC之動作完成信號 M12002, PLC設定 M10002為ON\n";
            //richTextBox1.Text += "[M status] M10002 HIGH\n";

            richTextBox1.Text += "(10a) PC 檢測 M10002 和 M12002\n";

            richTextBox1.Text += "(10a1) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox1.Text += "\n(10a2) PC 取得 M10002 為 ON\n";

            richTextBox1.Text += "(10a3) PC 讀取 M12002 狀態\t=>\t";
            contact_address = "12002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox1.Text += "\n(10a4) PC 取得 M12002 為 ON\n";

            delay(500);

            richTextBox1.Text += "(10b) PC 清除 D8000 ~ D8007 資料\n";
            erase_plc_d_data(contact_address, 8);

            richTextBox1.Text += "(10c) PC 令 (收到動作要求信號)M12000 為 OFF\n";
            //richTextBox1.Text += "[M status] M12000 LOW\n";
            contact_address = "12000";
            set_plc_m_status(contact_address, LOW);

            richTextBox1.Text += "(10d) PC 令 (動作執行信號)M12001 為 OFF\n";
            //richTextBox1.Text += "[M status] M12001 LOW\n";
            contact_address = "12001";
            set_plc_m_status(contact_address, LOW);

            //richTextBox1.Text += "[M status] M10000 LOW\n";
            //richTextBox1.Text += "[M status] M10001 LOW\n";

            delay(500);

            richTextBox1.Text += "(10e) PLC 清除 D2000 ~ D2006 資料\n";
            richTextBox1.Text += "(10f) PC 令 (動作要求訊號)M10000 為 OFF\n";
            richTextBox1.Text += "(10g) PC 令 (動作開始要求訊號)M10001 為 OFF\n";

            delay(500);

            richTextBox1.Text += "(11a) PC 檢測 (PLC動作完成信號)M10002\n";
            //當PC收到PLC收到動作完成訊號M10002 ON之後,結果碼D8010資料清除
            //PC->PLC動作完成訊號M12002 OFF

            richTextBox1.Text += "(11a) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, HIGH);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox1.Text += "\n(11b) PC 取得 M10002 為 ON\n";

            richTextBox1.Text += "(11c) PC 清除 D8010資料\n";
            //contact_address = "8010";
            //erase_plc_d_data(contact_address, 1);

            richTextBox1.Text += "(11d) PC 令 M12002 為 OFF\n";
            //richTextBox1.Text += "[M status] M12002 LOW\n";
            contact_address = "12002";
            set_plc_m_status(contact_address, LOW);

            delay(500);

            get_all_plc_m_status();

            richTextBox1.Text += "(12a) PLC 收到 PC 設定 M12002 為 OFF, PLC 設定 M10002為OFF\n";
            richTextBox1.Text += "[M status] M10002 LOW\n";

            richTextBox1.Text += "(12b) PC 讀取 M10002 狀態\t=>\t";
            contact_address = "10002";
            polling_m_status(contact_address, LOW);
            if (flag_plc_test_break == true)
            {
                richTextBox1.Text += "PLC測試中斷 PLC測試中斷 PLC測試中斷\n";
                return;
            }

            richTextBox1.Text += "\n(12b) PC 取得 M10002 為 LOW\n";

            richTextBox1.Text += "測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\tOK\n\n\n";

            stopwatch.Stop();
            richTextBox1.Text += "PLC交握測試 完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            richTextBox1.Text += "時間2 : " + DateTime.Now.ToString() + "\n";
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
                    richTextBox1.Text += "使用者中斷PLC測試, 結束\n";
                    break;
                }
                richTextBox1.Text += "第 " + (cnt++).ToString() + " 次測試\n";
                do_PC_PLC_Communication(sender, e);
                if (flag_plc_test_break == true)
                {
                    richTextBox1.Text += "使用者中斷PLC測試, 結束\n";
                    break;
                }
                delay(1000);
            }

            bt_plc_test.BackColor = Color.White;
            bt_plc_test_break.BackColor = Color.White;

            if (flag_plc_test_break == true)
            {
                flag_plc_test_break = false;

                richTextBox1.Text += "\n測試PLC作業流程 SP\t" + DateTime.Now.ToString() + "\t使用者中斷\n\n";

                stopwatch.Stop();
                richTextBox1.Text += "時間3 : " + DateTime.Now.ToString() + "\n";
            }
            flag_plc_test = false;
            flag_plc_test_busy = false;
            flag_plc_test_break = false;
        }

        private void bt_plc_test_break_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            bt_plc_test_break.BackColor = Color.Red;
            flag_plc_test_break = true;
        }

        private void bt_plc_test_break_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "設定 中斷\n";
            bt_plc_test_break.BackColor = Color.Red;
            flag_plc_test_break = true;
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == true)
            {
                timer1.Enabled = false;
                bt_pause.BackgroundImage = Properties.Resources.play;
            }
            else
            {
                timer1.Enabled = true;
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
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
            //開啟檔案總管
            Process.Start(currentPath);
        }
        void save_image_to_drive() //用時間檔名存檔 不檢查序號
        {
            show_main_message1("存檔中...", S_OK, 10);
            delay(10);

            Bitmap bitmap1 = (Bitmap)pictureBox_plc_status.Image;

            if (bitmap1 != null)
            {
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

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    show_main_message1("已存檔BMP", S_OK, 30);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "xxx錯誤訊息e39 : " + ex.Message + "\n";
                    show_main_message1("存檔失敗", S_OK, 30);
                    //show_main_message1("存檔失敗 : " + ex.Message, S_OK, 30);
                }
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
                show_main_message1("無圖可存a", S_FALSE, 30);
                show_main_message1("無圖可存a", S_FALSE, 30);
            }
            return;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string contact_address = string.Empty;

            richTextBox1.Text += "[M status] M12000 LOW\n";
            contact_address = "12000";
            set_plc_m_status(contact_address, LOW);

            richTextBox1.Text += "[M status] M12001 LOW\n";
            contact_address = "12001";
            set_plc_m_status(contact_address, LOW);

            richTextBox1.Text += "[M status] M12002 LOW\n";
            contact_address = "12002";
            set_plc_m_status(contact_address, LOW);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string contact_address = "8010";
            int length = 1;
            erase_plc_d_data(contact_address, length);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Print D2000
            string contact_address = "2000";
            print_plc_d_data(contact_address);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n\n(7) PC 做完色調, 將結果碼寫在 D8010\t";

            Random r = new Random();
            int color_result = r.Next(0, 20);
            richTextBox1.Text += "色調結果: 0x" + color_result.ToString("X2") + " = " + color_result.ToString() + "\n";
            string contact_address = "8010";
            string write_data = color_result.ToString();
            show_main_message1("寫入: D" + contact_address + ", 資料: " + write_data, S_OK, 30);
            set_plc_d_data_bcd16(contact_address, write_data);
        }
    }
}
