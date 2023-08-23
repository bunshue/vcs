using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports

namespace vcs_Comport5
{
    public partial class Form1 : Form
    {
        string[] COM_Ports_NameArr;
        string RxString1 = "";
        string RxString2 = "";

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        bool flag_comport_pc_ims_ok = false;

        private const int UART_BUF_LENGTH1 = 7;
        private const int UART_BUF_LENGTH2 = 5;

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
        private const int AWB_CHART_POINTS = 60;	    //AWB chart points
        bool flag_comport_ok = false;
        bool flag_comport_connection_ok = false;

        int g_conn_status = CAMERA_UNKNOWN;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            show_backcolor();
            Comport_Scan();

            /*
            //程式啟動完成後, 再開始檢查comport
            if (flag_comport_connection_ok == false)
            {
                richTextBox1.Text += "awb call connect_IMS_comport()\n";
                show_main_message0("連線COM Port", S_OK, 30);
                connect_IMS_comport();
                if (flag_comport_connection_ok == true)
                {
                    show_main_message0("連線COM Port, OK", S_OK, 30);
                }
            }

            if (serialPort2.IsOpen)
            {
                //bt_comport_connect1b.Enabled = false;
                //bt_comport_disconnect1b.Enabled = true;
                this.BackColor = SystemColors.ControlLight;
                flag_comport_ok = true;
                //bt_awb_test.Enabled = true;
                //bt_awb_test.BackColor = Color.Lime;
            }
            else
            {
                //bt_awb_test.Enabled = false;
                //bt_awb_test.BackColor = Color.Pink;

                //bt_awb_test.Enabled = true;
                //bt_awb_test.BackColor = Color.Lime;

            }
            */
        }

        int try_connect_comport()
        {
            int ret = S_FALSE;
            //if (flag_comport_ok == true)  always close any comport
            {
                serialPort2.Close();
                this.BackColor = Color.Yellow;
                //bt_comport_connect1b.Enabled = true;
                //button89.Enabled = true;
                //bt_comport_disconnect1b.Enabled = false;
                //button90.Enabled = false;
                flag_comport_ok = false;
            }

            comboBox_comport2.Items.Clear();    //Clear All items in Combobox
            richTextBox1.Text += "try_connect_comport ST\n";

            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "c共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox_comport2.Items.Add(port);
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
                comboBox_comport2.Text = COM_Ports_NameArr[0];
            }
            else
            {
                comboBox_comport2.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }

            if (COM_Ports_NameArr.Length == 1)
            {
                richTextBox1.Text += "只有一個comport, try 一次\n";
                ret = connect_comport2(comboBox_comport2.Text);
            }
            else
            {
                richTextBox1.Text += "多個comport\n";

                int try_index;
                for (int i = 0; i < COM_Ports_NameArr.Length; i++)
                {
                    try_index = (i + COM_Ports_NameArr.Length - 2) % COM_Ports_NameArr.Length;  //從倒數第二個找起
                    //try_index = (i + COM_Ports_NameArr.Length - 1) % COM_Ports_NameArr.Length;  //從最後一個找起
                    //try_index = (0 + COM_Ports_NameArr.Length - 1) % COM_Ports_NameArr.Length;  //只找最後一個

                    //richTextBox1.Text += "try_index = " + try_index.ToString() + "\n";

                    comboBox_comport2.Text = COM_Ports_NameArr[try_index];

                    serialPort2.Close();
                    this.BackColor = Color.Yellow;
                    bt_comport_connect2.Enabled = true;
                    //button89.Enabled = true;
                    bt_comport_disconnect2.Enabled = false;
                    //button90.Enabled = false;
                    flag_comport_ok = false;

                    ret = connect_comport2(COM_Ports_NameArr[try_index]);
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
                //計算serialPort2中有多少位元組 
                BytesToRead = serialPort2.BytesToRead;

                if (BytesToRead > 0)
                {
                    //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                    serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                }
                return S_OK;
            }
            else
                return S_FALSE;
        }

        void connect_IMS_comport()
        {
            int ret;
            ret = try_connect_comport();    //是這個在耗時間 且不一定連得上
            if (ret == S_OK)
            {
                richTextBox1.Text += "已連上IMS EGD System\n";
                show_main_message0("COM已連線", S_OK, 30);
                //pictureBox_comport1b.Image = iMS_Link.Properties.Resources.comport;

                //計算serialPort2中有多少位元組 
                BytesToRead = serialPort2.BytesToRead;

                if (BytesToRead > 0)
                {
                    //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                    serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                }
            }
            else
            {
                richTextBox1.Text += "COM未連線\n";
                this.BackColor = Color.Pink;
                show_main_message0("COM未連線", S_FALSE, 100);
                //pictureBox_comport1b.Image = iMS_Link.Properties.Resources.x;
                //toolTip1.SetToolTip(pictureBox_comport1b, "COM未連線");

                serialPort2.Close();
                this.BackColor = Color.Yellow;
                //bt_comport_connect1b.Enabled = true;
                //button89.Enabled = true;
                //bt_comport_disconnect1b.Enabled = false;
                //button90.Enabled = false;
                flag_comport_ok = false;
            }
        }


        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            groupBox_comport2.Location = new Point(10 + 410 * 0, 10);
            groupBox_comport2.Size = new Size(400, 70);

            panel1.Location = new Point(660, 10);

            int W = 400;
            int H = 550;
            x_st = 10;
            y_st = 120;
            dx = W + 10;

            groupBox_pc.Location = new Point(x_st + dx * 0, y_st);
            groupBox_pc.Size = new Size(W, H);
            groupBox_pc.Enabled = false;

            //richTextBox1
            richTextBox1.Location = new Point(x_st + dx * 1, y_st);
            richTextBox1.Size = new Size(W * 5 / 4, H);

            lb_main_mesg0.Location = new Point(350, 80);
            lb_main_mesg2a.Location = new Point(20, 30);
            lb_main_mesg2b.Location = new Point(20, 60);

            lb_main_mesg0.Text = "";
            lb_main_mesg2a.Text = "";
            lb_main_mesg2b.Text = "";

            //button
            x_st = 12;
            y_st = 400;
            dx = 120;
            dy = 42;

            bt_pc_0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_pc_1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_pc_2.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            bt_pc_3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_pc_4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_pc_5.Location = new Point(x_st + dx * 1, y_st + dy * 2);

            bt_pc_6.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_pc_7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_pc_8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            groupBox_led.Location = new Point(10, 50);
            groupBox_led.Size = new Size(180, 250);
            groupBox_ae.Location = new Point(W / 2 + 10, 50);
            groupBox_ae.Size = new Size(180, 250);

            x_st = 30;
            y_st = 50;
            dx = 100;
            dy = 110;
            bt_led_off.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            //bt_led_on.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_ae_off.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_ae_on.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            bt_led_off.Size = new Size(120, 120);
            //bt_led_on.Size = new Size(120, 80);
            bt_ae_off.Size = new Size(120, 80);
            bt_ae_on.Size = new Size(120, 80);

            bt_led_off.Text = "LED";
            //bt_led_on.Text = "LED開啟";
            bt_ae_off.Text = "自動曝光關閉";
            bt_ae_on.Text = "自動曝光開啟";

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(950, 720);
            this.Location = new Point(10, 10);

            bt_pc_0.Visible = false;
            bt_pc_1.Visible = false;
            bt_pc_2.Visible = false;

            bt_pc_3.Visible = false;
            bt_pc_4.Visible = false;
            bt_pc_5.Visible = false;

            bt_pc_6.Visible = false;
            bt_pc_7.Visible = false;
            bt_pc_8.Visible = false;

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_backcolor()
        {
            if (flag_comport_pc_ims_ok == false)
            {
                this.BackColor = Color.Pink;
                groupBox_pc.Enabled = false;
            }
            else
            {
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                groupBox_pc.Enabled = true;
            }
        }

        private void DisplayText1(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString1);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void DisplayText2(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString2);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort2_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            /*
            //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了, putty mode
            RxString2 = serialPort2.ReadExisting();
            this.Invoke(new EventHandler(DisplayText2));
            */
        }

        private void Comport_Scan()
        {
            comboBox_comport2.Items.Clear();    //Clear All items in Combobox
            string[] comport_names = SerialPort.GetPortNames();
            Array.Sort(comport_names);
            Array.Resize(ref COM_Ports_NameArr, comport_names.Length);
            comport_names.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "a共抓到 " + comport_names.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox_comport2.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox_comport2.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                //comboBox_comport2.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
                comboBox_comport2.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 1];   //倒數第1個
            }

            if (COM_Ports_NameArr.Length > 0)
            {
                for (int i = 0; i < COM_Ports_NameArr.Length; i++)
                {
                    richTextBox1.Text += "COM_Ports_NameArr[" + i.ToString() + "] = " + COM_Ports_NameArr[i] + "\n";
                }
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

        public bool Send_Data_PC_IMS(byte cc, byte xx, byte yy, byte zz)
        {
            if (flag_comport_pc_ims_ok == false)
            {
                //show_main_message0("PC-IMS 未連線", S_FALSE, 30);
                return false;
            }

            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, 0, data.Length);
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

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
        }

        private void bt_comport_scan2_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void bt_comport_connect2_Click(object sender, EventArgs e)
        {
            if ((COM_Ports_NameArr == null) || (COM_Ports_NameArr.Length == 0))
            {
                richTextBox1.Text += "沒有comport\n";
                return;
            }

            serialPort2.Close();

            flag_comport_pc_ims_ok = false;
            show_backcolor();
            groupBox_ae.BackColor = Color.Lime;

            connect_comport2(comboBox_comport2.Text);
        }

        int connect_comport2(string comport)
        {
            if (serialPort2.IsOpen == true)
            {
                serialPort2.Close();
            }

            serialPort2.PortName = comport;

            try
            {
                serialPort2.BaudRate = int.Parse(comboBox_baud_rate2.Text);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                richTextBox1.Text += "無法連上 " + comport + ", 請重新連線";
            }

            //serialPort2.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + comport + "\n";
                serialPort2.Open();
                richTextBox1.Text += "已連線\n";
                //SerialPortTimer100ms2.Enabled = true;
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + comport + ", reason : " + ex.Message + "\n";
            }
            finally
            {
                serialPort2.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                //MessageBox.Show("已經連上" + serialPort2.PortName);

                serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                SerialPortTimer100ms2.Stop();
                SerialPortTimer100ms2.Start();
                Application.DoEvents();
                flag_comport_pc_ims_ok = true;
                show_backcolor();
            }
            return 1;
        }

        private void bt_comport_disconnect2_Click(object sender, EventArgs e)
        {
            if (serialPort2.IsOpen == true)
            {
                serialPort2.Close();
            }
            richTextBox1.Text += "已離線\n";

            //pictureBox_comport2.Image = iMS_Link.Properties.Resources.x;
            //SerialPortTimer100ms2.Enabled = false;
            flag_comport_pc_ims_ok = false;
            show_backcolor();
        }

        int timer_display_show_main_mesg0_count = 0;
        int timer_display_show_main_mesg0_count_target = 0;
        int timer_display_show_main_mesg2_count = 0;
        int timer_display_show_main_mesg2_count_target = 0;

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

        void show_main_message0(string mesg, int number, int timeout)
        {
            lb_main_mesg0.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg0_count = 0;
            timer_display_show_main_mesg0_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message2a(string mesg, int number, int timeout)
        {
            lb_main_mesg2a.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg2_count = 0;
            timer_display_show_main_mesg2_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message2b(string mesg, int number, int timeout)
        {
            lb_main_mesg2b.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg2_count = 0;
            timer_display_show_main_mesg2_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg0_count < timer_display_show_main_mesg0_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg0_count++;
                if (timer_display_show_main_mesg0_count >= timer_display_show_main_mesg0_count_target)
                {
                    lb_main_mesg0.Text = "";
                }
            }

            if (timer_display_show_main_mesg2_count < timer_display_show_main_mesg2_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg2_count++;
                if (timer_display_show_main_mesg2_count >= timer_display_show_main_mesg2_count_target)
                {
                    lb_main_mesg2a.Text = "";
                    lb_main_mesg2b.Text = "";
                }
            }
        }

        public bool Send_Cmd_PC_IMS(byte d0, byte d1, byte d2, byte d3)
        {
            if (flag_comport_pc_ims_ok == false)
            {
                show_main_message0("PC-IMS未連線", S_FALSE, 30);
                return false;
            }

            byte[] data = new byte[5];

            data[0] = d0;
            data[1] = d1;
            data[2] = d2;
            data[3] = d3;
            data[4] = CalcCheckSum(data, 4);

            string mesg = "[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " "
                + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2");

            show_main_message2b(mesg, S_FALSE, 30);

            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, 0, data.Length);
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
            if (flag_comport_pc_ims_ok == false)
            {
                show_main_message0("PC-IMS 未連線", S_FALSE, 30);
                return false;
            }

            byte[] data = new byte[5];

            data[0] = 0xAA;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            serialPort2.Write(data, 0, data.Length);
            flag_wait_receive_data = 1;

            return true;
        }

        private void bt_pc_0_Click(object sender, EventArgs e)
        {
        }

        private void bt_pc_1_Click(object sender, EventArgs e)
        {
        }

        private void bt_pc_2_Click(object sender, EventArgs e)
        {
        }

        private void bt_pc_3_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);
        }

        private void bt_pc_4_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);
        }

        private void bt_pc_5_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);
        }

        private void bt_pc_6_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

            Send_Cmd_PC_IMS(0xFF, 0xAA, 0xBB, 0xCC);
        }

        private void bt_pc_7_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

            Send_Cmd_PC_IMS(0xFF, 0xCC, 0xBB, 0xAA);
        }

        private void bt_pc_8_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

            //清除相機資料
            erase_camera_data();
        }

        void erase_camera_data()
        {
            richTextBox1.Text += "erase all camera flash data\n";

            Send_Cmd_PC_IMS(0xEE, 0xFF, 0xEE, 0xFF);   //erase all camera flash data
            show_main_message2b("清除相機資料完成", S_OK, 30);
            return;
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

        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        int flag_need_to_merge_data = 0;
        int flag_receive_camera_serial = 0;
        int flag_read_camera_raw_data = 0;
        int flag_wait_receive_data = 0;
        //int flag_receive_camera_serial = 0;
        int flag_receive_camera_flash_data = 0;
        int flag_request_item = 0;
        bool flag_read_connection_again = true;

        int Comport_Mode = 0;   //0: iMS_Link, 1: putty mode, 2: hex mode

        private void SerialPortTimer100ms2_Tick(object sender, EventArgs e)
        {
            if (flag_comport_pc_ims_ok == true)
            {
                //計算serialPort2中有多少位元組 
                BytesToRead = serialPort2.BytesToRead;
                if (BytesToRead > 0)
                    richTextBox1.Text += "len = " + BytesToRead.ToString() + "\n";

                if ((BytesToRead > 0) && (BytesToRead < 21) && (BytesToRead != UART_BUF_LENGTH2) && (flag_need_to_merge_data == 0))
                {
                    //serialPort2.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort2.Read(receive_buffer_tmp, 0, BytesToRead);
                    BytesToRead_tmp = BytesToRead;
                    flag_need_to_merge_data = 1;
                    //groupBox10.BackColor = Color.Red;
                    //richTextBox1.Text += "\n";
                    return;
                }
                else if (BytesToRead > 0)
                {
                    richTextBox1.Text += "a";
                    if (flag_need_to_merge_data == 1)
                    {
                        flag_need_to_merge_data = 0;
                        if (BytesToRead == 21)
                        {
                            //directly use new data.....
                            //richTextBox1.Text += "[debug] BytesToRead = " + BytesToRead.ToString() + ", use new data\n";
                            //serialPort2.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                            serialPort2.Read(receive_buffer, 0, BytesToRead);
                        }
                        else
                        {
                            //serialPort2.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                            serialPort2.Read(receive_buffer, BytesToRead_tmp, BytesToRead);
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
                        //serialPort2.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        if (BytesToRead <= 2048)
                            serialPort2.Read(receive_buffer, 0, BytesToRead);
                        else
                        {
                            serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                        }
                    }

                    richTextBox1.Text += "a";

                    if (Comport_Mode == 0)  //iMS_Link mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH2)
                        {
                            SpyMonitorRX2();
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

                            SpyMonitorRX2();

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
                                }
                                flag_receive_camera_serial = 0;
                                flag_wait_receive_data = 0;
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
                                    /*
                                    textBox5.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                    */
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

                                    /*
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
                                            richTextBox1.Text += "c unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                                            break;

                                    }
                                    show_info(flag_request_item);
                                    */
                                }
                                flag_receive_camera_flash_data = 0;
                                flag_wait_receive_data = 0;
                            }
                        }
                        else if (BytesToRead == 37) // 5 + 16 + 16
                        {
                            int i;
                            richTextBox1.Text += "\nBytesToRead = 37 Bytes, data\t";
                            for (i = 0; i < BytesToRead; i++)
                            {
                                richTextBox1.Text += receive_buffer[i].ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";

                            SpyMonitorRX2();

                            input = "";
                            for (i = 5; i < (32 + 5); i++)
                                input += (char)receive_buffer[i];

                            richTextBox1.Text += "input data \n";
                            for (i = 0; i < 32; i++)
                            {
                                richTextBox1.Text += ((int)input[i]).ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";
                        }
                        else if (BytesToRead == 55) // 5 + 50
                        {
                            richTextBox1.Text += "BytesToRead = 55 Bytes, data\t";
                            for (int i = 0; i < BytesToRead; i++)
                            {
                                richTextBox1.Text += receive_buffer[i].ToString("X2") + " ";
                            }
                            richTextBox1.Text += "\n";

                            SpyMonitorRX2();

                            richTextBox1.Text += "check received data.............\n";

                            input = "";
                            for (int i = 5; i < (50 + 5); i++)
                                input += (char)receive_buffer[i];
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
                            serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                        }
                    }
                }
            }
        }

        private void SpyMonitorRX2()
        {
            richTextBox1.Text += "do SpyMonitorRX2() len = " + BytesToRead.ToString() + "\n";

            string message = "";
            //if (BytesToRead == 5)
            {
                input = "";
                for (int i = 0; i < UART_BUF_LENGTH2; i++)
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

                //if (isCommandLog == 1)
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
                    /*
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
                    */
                    else if ((input[1] == 0x11) && (input[2] == 0x52) && (input[3] == 0x00))
                    {
                        //richTextBox1.Text += "get uart response from aries egd system.\n";
                        //flag_comport_connection_ok = true;
                    }
                    else if (input[1] <= 0x58)  //ims send camera sensor data
                    {
                        //讀取相機暫存器值 先一律顯示在固定位置 再依指令放到變數裏

                        int dd = (int)input[3];
                        /*
                        tb_3.Text = dd.ToString("X2");
                        tb_4.Text = dd.ToString();
                        tb_3a.Text = dd.ToString("X2");
                        tb_4a.Text = dd.ToString();
                        tb_3m.Text = dd.ToString("X2");
                        tb_4m.Text = dd.ToString();
                        */
                        //richTextBox1.Text += "cmd : " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + "\n";

                        if ((input[1] == 0x35) || (input[1] == 0x52) || (input[1] == 0x3A))
                        {
                            if (input[1] == 0x35)
                            {
                                if (input[2] == 0x01)
                                {
                                }
                                else if (input[2] == 0x02)
                                {
                                }
                                else if (input[2] == 0x0A)
                                {
                                }
                                else if (input[2] == 0x0B)
                                {
                                }
                            }
                            else if (input[1] == 0x52)
                            {
                                if (input[2] == 0x1A)
                                {
                                }
                                else if (input[2] == 0x1B)
                                {
                                }
                                else if (input[2] == 0x1C)
                                {
                                }
                                else if (input[2] == 0x1D)
                                {
                                }
                                else if (input[2] == 0x1E)
                                {
                                }
                                else if (input[2] == 0x1F)
                                {
                                }
                            }
                            else if (input[1] == 0x3A)
                            {
                            }
                            //richTextBox1.Text += "\n";
                        }
                        else if (input[1] == 0x58)
                        {
                        }
                        else if (input[1] == 0x56)  // Color Matrix
                        {
                        }
                    }
                    else if (input[1] == 0xA1)
                    {
                        //useless
                        int dd = (int)input[2];
                        /*
                        tb_3.Text = dd.ToString("X2");
                        tb_4.Text = dd.ToString();
                        tb_3a.Text = dd.ToString("X2");
                        tb_4a.Text = dd.ToString();
                        tb_3m.Text = dd.ToString("X2");
                        tb_4m.Text = dd.ToString();
                        */
                    }
                    else if (input[1] == 0xC1)
                    {
                        flag_receive_camera_serial = 1;
                        richTextBox1.Text += "let flag_receive_camera_serial = 1\n";
                    }
                    else if (input[1] == 0xCC)
                    {
                        richTextBox1.Text += "CC";
                    }
                    else if (input[1] == 0xCD)
                    {
                        /*
                        if (flag_show_cpu_temperature == true)
                        {
                            //溫度偵測顯示
                            temperature_data = input[2] * 256 + input[3];
                            //richTextBox1.Text += temperature_data.ToString("X4") + "  ";
                            float temperature = ((((float)(temperature_data) / 65536.0f) / 0.00198421639f) - 273.15f);
                            //richTextBox1.Text += temperature.ToString()+" C ";

                            if (temperature > 70)
                                lb_temperature.ForeColor = Color.Red;
                            else
                                lb_temperature.ForeColor = Color.Blue;

                            lb_temperature.Text = temperature.ToString("#0.000") + " C ";
                        */
                        /*
                        #define XAdcPs_RawToTemperature(AdcData)				\
                        ((((float)(AdcData)/65536.0f)/0.00198421639f ) - 273.15f)
                        */
                        /*
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
                        */
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
                    }
                    else if (input[1] == 0xB1)
                    {
                        flag_request_item = input[2];
                    }
                    else if (input[1] == 0xFF)
                    {
                        g_conn_status = input[2];
                        /*
                        if (g_conn_status == DONGLE_NONE)
                        {
                            show_main_message1("無連接器", S_OK, 30);
                            textBox7.Text = "無連接器";
                            textBox7.BackColor = Color.Red;
                            playSound(S_FALSE);
                            panel_camera_status1.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status5.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                        }
                        else if (g_conn_status == CAMERA_NONE)
                        {
                            show_main_message1("無相機", S_OK, 30);
                            textBox7.Text = "有連接器, 無相機";
                            textBox7.BackColor = Color.Red;
                            playSound(S_FALSE);
                            panel_camera_status1.BackgroundImage = iMS_Link.Properties.Resources.recorder_none;
                            panel_camera_status2.BackgroundImage = iMS_Link.Properties.Resources.recorder_none;
                            panel_camera_status3.BackgroundImage = iMS_Link.Properties.Resources.recorder_none;
                            panel_camera_status4.BackgroundImage = iMS_Link.Properties.Resources.recorder_none;
                            panel_camera_status5.BackgroundImage = iMS_Link.Properties.Resources.recorder_none;
                        }
                        else if (g_conn_status == CAMERA_OK)
                        {
                            show_main_message1("有相機", S_OK, 30);
                            textBox7.Text = "有連接器, 有相機";
                            textBox7.BackColor = Color.White;
                            panel_camera_status1.BackgroundImage = iMS_Link.Properties.Resources.recorder_ok;
                            panel_camera_status2.BackgroundImage = iMS_Link.Properties.Resources.recorder_ok;
                            panel_camera_status3.BackgroundImage = iMS_Link.Properties.Resources.recorder_ok;
                            panel_camera_status4.BackgroundImage = iMS_Link.Properties.Resources.recorder_ok;
                            panel_camera_status5.BackgroundImage = iMS_Link.Properties.Resources.recorder_ok;
                        }
                        else if (g_conn_status == CAMERA_SENSOR_FAIL)
                        {
                            show_main_message1("相機失效", S_OK, 30);
                            textBox7.Text = "有連接器, 有相機, 但是相機無法讀寫";
                            textBox7.BackColor = Color.White;
                            panel_camera_status1.BackgroundImage = iMS_Link.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status2.BackgroundImage = iMS_Link.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status3.BackgroundImage = iMS_Link.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status4.BackgroundImage = iMS_Link.Properties.Resources.recorder_sensor_fail;
                            panel_camera_status5.BackgroundImage = iMS_Link.Properties.Resources.recorder_sensor_fail;

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
                            panel_camera_status1.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status2.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status3.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status4.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                            panel_camera_status5.BackgroundImage = iMS_Link.Properties.Resources.recorder_fail;
                        }
                        flag_read_connection_again = true;
                        progressBar1.Value = 100;
                        */
                    }
                    else if (input[1] == 0x99)
                    {
                        /*
                        if ((input[2] == 0x00) && (input[3] == 0x00))
                        {
                            button36.BackgroundImage = iMS_Link.Properties.Resources.console;
                            button36.BackColor = SystemColors.ControlLight;
                            button37.BackColor = SystemColors.ControlLight;
                        }
                        else if ((input[2] == 0x11) && (input[3] == 0x11))
                        {
                            button36.BackgroundImage = iMS_Link.Properties.Resources.ims3;
                            button35.BackColor = SystemColors.ControlLight;
                            button36.BackColor = SystemColors.ControlLight;
                            button37.BackColor = SystemColors.ControlLight;
                        }
                        else
                        {
                            richTextBox1.Text += "unknown status\n";
                        }
                        */
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

        private void bt_led_off_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "LED關閉\n";
            Send_Data_PC_IMS(0xFF, 0xCC, 0xBB, 0xAA);
        }

        private void bt_ae_off_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "自動曝光關閉\n";
            byte DongleAddr_h = 0x35;
            byte DongleAddr_l = 0x03;
            byte DongleData = 0x03;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            groupBox_ae.BackColor = Color.Gray;
        }

        private void bt_ae_on_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "自動曝光開啟\n";
            byte DongleAddr_h = 0x35;
            byte DongleAddr_l = 0x03;
            byte DongleData = 0x00;
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            groupBox_ae.BackColor = Color.Lime;
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

            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, 0, data.Length);
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

    }
}
