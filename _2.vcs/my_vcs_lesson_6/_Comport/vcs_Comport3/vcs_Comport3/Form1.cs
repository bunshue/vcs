using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports

namespace vcs_Comport3
{
    public partial class Form1 : Form
    {
        string[] COM_Ports_NameArr;
        string RxString1 = "";
        string RxString2 = "";

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        bool flag_comport_pc_plc_ok = false;
        bool flag_comport_pc_ims_ok = false;


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

        int g_conn_status = CAMERA_UNKNOWN;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.Yellow;
            show_item_location();
            Comport_Scan();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            groupBox_comport1.Location = new Point(10, 10);
            groupBox_comport1.Size = new Size(400, 70);

            groupBox_comport2.Location = new Point(10, 90);
            groupBox_comport2.Size = new Size(400, 70);

            groupBox_plc.Location = new Point(10, 170);
            groupBox_plc.Size = new Size(300, 500);

            groupBox_pc.Location = new Point(10+310, 170);
            groupBox_pc.Size = new Size(300, 500);

            groupBox_ims.Location = new Point(10 + 310+310, 170);
            groupBox_ims.Size = new Size(300, 500);

            //richTextBox1
            richTextBox1.Location = new Point(10 + 310+310+310, 170);
            richTextBox1.Size = new Size(400-120, 500);

            lb_main_mesg0.Location = new Point(450, 30);
            lb_main_mesg1a.Location = new Point(20, 30);
            lb_main_mesg2a.Location = new Point(20, 30);
            lb_main_mesg3a.Location = new Point(20, 30);
            lb_main_mesg1b.Location = new Point(20, 60);
            lb_main_mesg2b.Location = new Point(20, 60);
            lb_main_mesg3b.Location = new Point(20, 60);
            lb_main_mesg0.Text = "";
            lb_main_mesg1a.Text = "";
            lb_main_mesg2a.Text = "";
            lb_main_mesg3a.Text = "";
            lb_main_mesg1b.Text = "";
            lb_main_mesg2b.Text = "";
            lb_main_mesg3b.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";

            //button
            x_st = 12;
            y_st = 100;
            dx = 180;
            dy = 50;

            bt_plc_0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_plc_1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_plc_2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_plc_3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_plc_4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_plc_5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_plc_6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_plc_7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_plc_8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_plc_9.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            lb_sn1.Location = new Point(x_st + dx * 1 - 70, y_st + dy * 2);
            lb_sn2.Location = new Point(x_st + dx * 1 - 70, y_st + dy * 2+30);
            lb_sn3.Location = new Point(x_st + dx * 1 - 70, y_st + dy * 2+60);
            lb_sn.Location = new Point(x_st + dx * 1-70, y_st + dy * 4);
            tb_sn1.Location = new Point(x_st + dx * 1-70, y_st + dy * 5);
            tb_sn2.Location = new Point(x_st + dx * 1-70, y_st + dy * 6);
            bt_plc_generate_sn.Location = new Point(x_st + dx * 1+30, y_st + dy * 7);

            bt_pc_0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_pc_1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_pc_2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_pc_3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_pc_4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_pc_5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_pc_6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_pc_7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_pc_8.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_ims_0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_ims_1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_ims_2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_ims_3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_ims_4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_ims_5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1135+120, 725);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void DisplayText1(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString1);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            /*
            //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了, putty mode
            RxString1 = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(DisplayText1));
            */
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
            comboBox_comport1.Items.Clear();    //Clear All items in Combobox
            comboBox_comport2.Items.Clear();    //Clear All items in Combobox
            string[] comport_names = SerialPort.GetPortNames();
            Array.Sort(comport_names);
            Array.Resize(ref COM_Ports_NameArr, comport_names.Length);
            comport_names.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "a共抓到 " + comport_names.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox_comport1.Items.Add(port);
                comboBox_comport2.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox_comport1.Text = COM_Ports_NameArr[0];
                comboBox_comport2.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                //comboBox_comport1.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
                comboBox_comport1.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 1];   //倒數第1個

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
                show_main_message0("PC-IMS 未連線", S_FALSE, 30);
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

        private void SpyMonitorRX1()
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

            richTextBox1.AppendText("[RX] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + "\n");

            if (input[0] == 0xAA)
            {
            }
            else if (input[0] == 0xBB)
            {
            }
            else if (input[0] == 0xFF)
            {
                if ((input[1] == 0xAA) && (input[2] == 0xBB) && (input[3] == 0xCC))
                {
                    richTextBox1.Text += "PLC -> PC : START\n";
                    do_plc_command(5);
                }
                else if ((input[1] == 0xCC) && (input[2] == 0xBB) && (input[3] == 0xAA))
                {
                    richTextBox1.Text += "PLC -> PC : LED\n";
                    do_plc_command(6);
                }
                else if ((input[1] == 0xAA) && (input[2] == 0xBB) && (input[3] == 0x10))
                {
                    richTextBox1.Text += "PLC -> PC : IMS影像存檔\n";
                    do_plc_command(8);
                }
                else if ((input[1] == 0xAA) && (input[2] == 0xBB) && (input[3] == 0x55))
                {
                    richTextBox1.Text += "PLC -> PC : AWB START\n";
                    do_plc_command(2);
                }
                else if ((input[1] == 0xAA) && (input[2] == 0xBB) && (input[3] == 0xAA))
                {
                    richTextBox1.Text += "PLC -> PC : AWB STOP\n";
                }
                else if ((input[1] == 0xAA) && (input[2] == 0xBB) && (input[3] == 0x00))
                {
                    richTextBox1.Text += "PLC -> PC : AWB Result\n";
                    do_plc_command(3);
                }
            }
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void SerialPortTimer100ms1_Tick(object sender, EventArgs e)
        {
            if (flag_comport_pc_plc_ok == true)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                if (BytesToRead > 0)
                    richTextBox1.Text += "len = " + BytesToRead.ToString() + "\n";

                if ((BytesToRead > 0) && (BytesToRead < 21) && (BytesToRead != UART_BUF_LENGTH) && (flag_need_to_merge_data == 0))
                {
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer_tmp, 0, BytesToRead);
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
                            //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                            serialPort1.Read(receive_buffer, 0, BytesToRead);
                        }
                        else
                        {
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

                    richTextBox1.Text += "a";

                    if (Comport_Mode == 0)  //iMS_Link mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                        {
                            SpyMonitorRX1();
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

                            SpyMonitorRX1();

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
                                    lb_sn1.Text = "xxxx[S/N] : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
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

                            SpyMonitorRX1();

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
                            lb_sn1.Text = "[S/N] : ";
                            lb_sn2.Text = "[S/N] : ";

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
                                        lb_sn1.Text += (char)input[i];
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
                                        lb_sn1.Text += (char)input[i];
                                        flag_no_camera_serial1 = false;
                                    }
                                }
                            }

                            for (i = 16; i < (16 + 11); i++)
                            {
                                //richTextBox1.Text += ((int)input[i]).ToString("X2") + "  ";
                                if ((i > 16) && (((int)input[i] < '0') || ((int)input[i] > '9')))
                                {
                                    flag_no_camera_serial2 = true;
                                    break;
                                }
                                else
                                {
                                    lb_sn2.Text += (char)input[i];
                                    flag_no_camera_serial2 = false;
                                }
                            }

                            if (flag_no_camera_serial1 == true)
                            {
                                lb_sn1.Text = "[S/N] : 無相機序號資料1";
                            }
                            else
                            {
                            }
                            if (flag_no_camera_serial2 == true)
                            {
                                lb_sn2.Text = "[S/N] : 無相機序號資料2";
                            }
                            else
                            {
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

                            SpyMonitorRX1();

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
                            serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                        }
                    }
                }
            }
        }

        private void bt_comport_scan1_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void bt_comport_connect1_Click(object sender, EventArgs e)
        {
            if ((COM_Ports_NameArr == null) || (COM_Ports_NameArr.Length == 0))
            {
                richTextBox1.Text += "沒有comport\n";
                return;
            }

            serialPort1.Close();
            this.BackColor = Color.Yellow;
            connect_comport1(comboBox_comport1.Text);
        }

        int connect_comport1(string comport)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }

            serialPort1.PortName = comport;

            try
            {
                serialPort1.BaudRate = int.Parse(comboBox_baud_rate1.Text);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                richTextBox1.Text += "無法連上 " + comport + ", 請重新連線";
                this.BackColor = Color.Pink;
            }

            //serialPort1.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + comport + "\n";
                serialPort1.Open();
                richTextBox1.Text += "已連線\n";
                //SerialPortTimer100ms1.Enabled = true;
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + comport + ", reason : " + ex.Message + "\n";
            }
            finally
            {
                serialPort1.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                //MessageBox.Show("已經連上" + serialPort1.PortName);

                this.BackColor = System.Drawing.SystemColors.ControlLight;

                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                SerialPortTimer100ms1.Stop();
                SerialPortTimer100ms1.Start();
                Application.DoEvents();
                flag_comport_pc_plc_ok = true;
            }
            return 1;
        }

        private void bt_comport_disconnect1_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }
            richTextBox1.Text += "已離線\n";

            this.BackColor = Color.Yellow;
            //pictureBox_comport1.Image = iMS_Link.Properties.Resources.x;
            //SerialPortTimer100ms1.Enabled = false;
            flag_comport_pc_plc_ok = false;
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

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


        /*
        private void button1_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Yellow;

            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }
            if (serialPort2.IsOpen == true)
            {
                serialPort2.Close();
            }

            serialPort1.PortName = "COM4";
            serialPort2.PortName = "COM6";
            serialPort1.BaudRate = 115200;
            serialPort2.BaudRate = 115200;

            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + serialPort1.PortName + "\n";
                serialPort1.Open();
                richTextBox1.Text += "已連線\n";
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + serialPort1.PortName + ", reason : " + ex.Message + "\n";
            }
            finally
            {
                serialPort1.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                SerialPortTimer100ms1.Stop();
                SerialPortTimer100ms1.Start();
                Application.DoEvents();
            }

            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + serialPort2.PortName + "\n";
                serialPort2.Open();
                richTextBox1.Text += "已連線\n";
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + serialPort2.PortName + ", reason : " + ex.Message + "\n";
            }
            finally
            {
                serialPort2.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                SerialPortTimer100ms2.Stop();
                SerialPortTimer100ms2.Start();
                Application.DoEvents();
            }
        }
        */

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
            this.BackColor = Color.Yellow;
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
                this.BackColor = Color.Pink;
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

                this.BackColor = System.Drawing.SystemColors.ControlLight;

                serialPort2.DiscardInBuffer();  //丟棄UART buffer內的資料
                SerialPortTimer100ms2.Stop();
                SerialPortTimer100ms2.Start();
                Application.DoEvents();
                flag_comport_pc_ims_ok = true;
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

            this.BackColor = Color.Yellow;
            //pictureBox_comport2.Image = iMS_Link.Properties.Resources.x;
            //SerialPortTimer100ms2.Enabled = false;
            flag_comport_pc_ims_ok = false;
        }

        int timer_display_show_main_mesg0_count = 0;
        int timer_display_show_main_mesg0_count_target = 0;
        int timer_display_show_main_mesg1_count = 0;
        int timer_display_show_main_mesg1_count_target = 0;
        int timer_display_show_main_mesg2_count = 0;
        int timer_display_show_main_mesg2_count_target = 0;
        int timer_display_show_main_mesg3_count = 0;
        int timer_display_show_main_mesg3_count_target = 0;

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

        void show_main_message1a(string mesg, int number, int timeout)
        {
            lb_main_mesg1a.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg1_count = 0;
            timer_display_show_main_mesg1_count_target = timeout;   //timeout in 0.1 sec
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

        void show_main_message3a(string mesg, int number, int timeout)
        {
            lb_main_mesg3a.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg3_count = 0;
            timer_display_show_main_mesg3_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message1b(string mesg, int number, int timeout)
        {
            lb_main_mesg1b.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg1_count = 0;
            timer_display_show_main_mesg1_count_target = timeout;   //timeout in 0.1 sec
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

        void show_main_message3b(string mesg, int number, int timeout)
        {
            lb_main_mesg3b.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg3_count = 0;
            timer_display_show_main_mesg3_count_target = timeout;   //timeout in 0.1 sec
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

            if (timer_display_show_main_mesg1_count < timer_display_show_main_mesg1_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg1_count++;
                if (timer_display_show_main_mesg1_count >= timer_display_show_main_mesg1_count_target)
                {
                    lb_main_mesg1a.Text = "";
                    lb_main_mesg1b.Text = "";
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

            if (timer_display_show_main_mesg3_count < timer_display_show_main_mesg3_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg3_count++;
                if (timer_display_show_main_mesg3_count >= timer_display_show_main_mesg3_count_target)
                {
                    lb_main_mesg3a.Text = "";
                    lb_main_mesg3b.Text = "";
                }
            }
        }

        public bool Send_Data_PLC_PC(byte cc, byte xx, byte yy, byte zz)
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            string cmd = "[RX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2");
            show_main_message2a(cmd, S_FALSE, 30);

            if ((xx == 0xAA) && (yy == 0xBB) && (zz == 0xCC))
            {
                show_main_message2b("START", S_FALSE, 30);
            }
            else if ((xx == 0xCC) && (yy == 0xBB) && (zz == 0xAA))
            {
                show_main_message2b("LED", S_FALSE, 30);
            }
            else if ((cc == 0xFF) && (xx == 0x00) && (yy == 0x00) && (zz == 0x00))
            {
                show_main_message2b("讀取連線狀態", S_FALSE, 30);
            }
            else if ((cc == 0xC1) && (xx == 0x00) && (yy == 0x00) && (zz == 0x00))
            {
                show_main_message2b("讀取相機序號", S_FALSE, 30);
            }
            else if ((cc == 0xC0) && (xx == 0x12) && (yy == 0x34) && (zz == 0x56))
            {
                show_main_message2b("寫入相機序號", S_FALSE, 30);
            }
            else if ((cc == 0xFF) && (xx == 0xAA) && (yy == 0xBB) && (zz == 0x55))
            {
                show_main_message2b("啟動色彩校正", S_FALSE, 30);
                //TBD
                return true;
            }
            else if ((cc == 0xFF) && (xx == 0xAA) && (yy == 0xBB) && (zz == 0x00))
            {
                show_main_message2b("讀取色彩校正結果", S_FALSE, 30);
                //TBD
                return true;
            }
            else if ((cc == 0xFF) && (xx == 0xAA) && (yy == 0xBB) && (zz == 0x10))
            {
                show_main_message2b("命令ims影像存檔", S_FALSE, 30);
                //TBD
                return true;
            }
            else if ((xx == 0x33) && (yy == 0x88) && (zz == 0x77))  //故意發一個錯誤命令
            {
                data[4] = CalcCheckSum(data, 2);
                cmd = "[RX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2");

                richTextBox1.Text += cmd + "\n";

                show_main_message2a(cmd, S_FALSE, 30);
                show_main_message2b("校驗和錯誤", S_FALSE, 30);

                return false;
            }
            else
            {
                show_main_message2b("未定義", S_FALSE, 30);
            }

            richTextBox1.Text += cmd + "\n";

            show_main_message2a(cmd, S_FALSE, 30);

            Send_Data_PC_IMS(cc, xx, yy, zz);

            return true;
        }

        public bool Send_Data_PC_PLC(byte cc, byte xx, byte yy, byte zz)
        {
            if (flag_comport_pc_plc_ok == false)
            {
                show_main_message0("PC-PLC未連線", S_FALSE, 30);
                return false;
            }

            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            string cmd = "[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2");

            show_main_message2b(cmd, S_FALSE, 30);

            //serialPort1.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
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

        void do_plc_command(int item)
        {
            if (item == 0)
            {
                Send_Data_PLC_PC(0xFF, 0x00, 0x00, 0x00);   //讀取連線狀態
            }
            else if (item == 1)
            {
                show_main_message1a("還沒做好", S_FALSE, 30);
                return;

                lb_sn1.Text = "相機序號1 讀取中...";
                lb_sn2.Text = "相機序號2 讀取中...";
                lb_sn3.Text = "";

                //Send_Data_PLC_PC(0xC1, 0x00, 0x00, 0x00);   //讀取相機序號

                //讀取相機序號
                Get_IMS_Data(0, 0xAA, 0xAA);    //camera serial read

                int cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 50))
                {
                    richTextBox1.Text += "+" + cnt.ToString();
                    delay(100);
                }
                flag_wait_receive_data = 0;

            }
            else if (item == 2)
            {
                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x55);   //啟動色彩校正

                //通知imsLink做色彩校正就好 不用下命令給ims主機

            }
            else if (item == 3)
            {
                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x00);   //讀取色彩校正結果

            }
            else if (item == 4)
            {
                show_main_message1a("還沒做好", S_FALSE, 30);
                return;
            }
            else if (item == 5)
            {

                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0xCC);

            }
            else if (item == 6)
            {

                Send_Data_PLC_PC(0xFF, 0xCC, 0xBB, 0xAA);

            }
            else if (item == 7)
            {

                Send_Data_PLC_PC(0xFF, 0x33, 0x88, 0x77);

            }
            else if (item == 8)
            {

                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x10);

            }
            else if (item == 9)
            {
                if ((tb_sn1.Text.Length != 10) || (tb_sn2.Text.Length != 12))
                {
                    make_camera_data();
                }

                Send_Data_PLC_PC(0xC0, 0x12, 0x34, 0x56);   //寫入相機序號

                show_main_message2b("寫入相機序號", S_FALSE, 30);

                richTextBox1.Text += "相機序號1長度 : " + tb_sn1.Text.Length.ToString() + "\n";
                richTextBox1.Text += "相機序號2長度 : " + tb_sn2.Text.Length.ToString() + "\n";

                int i;

                byte[] sn_data_tmp = new byte[22];
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
                    //richTextBox1.Text += "i = " + i.ToString() + " tmp data : " + tb_sn2.Text[i - 10].ToString() + "\n";
                }

                //richTextBox1.Text += "\n";

                //Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write    ols

                if (flag_comport_pc_ims_ok == false)
                {
                    show_main_message0("PC-IMS 未連線", S_FALSE, 30);
                    return;
                }
                serialPort2.Write(sn_data_tmp, 0, 22);

            }

            return;
        }

        void do_plc_command(object sender, EventArgs e, int item)
        {
            if (item == 0)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);
                Send_Data_PLC_PC(0xFF, 0x00, 0x00, 0x00);   //讀取連線狀態
            }
            else if (item == 1)
            {
                show_main_message1a("還沒做好", S_FALSE, 30);
                return;

                lb_sn1.Text = "相機序號1 讀取中...";
                lb_sn2.Text = "相機序號2 讀取中...";
                lb_sn3.Text = "";

                show_main_message1a(((Button)sender).Text, S_FALSE, 30);
                //Send_Data_PLC_PC(0xC1, 0x00, 0x00, 0x00);   //讀取相機序號

                //讀取相機序號
                Get_IMS_Data(0, 0xAA, 0xAA);    //camera serial read

                int cnt = 0;
                while ((flag_wait_receive_data == 1) && (cnt++ < 50))
                {
                    richTextBox1.Text += "+" + cnt.ToString();
                    delay(100);
                }
                flag_wait_receive_data = 0;

            }
            else if (item == 2)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x55);   //啟動色彩校正

                //通知imsLink做色彩校正就好 不用下命令給ims主機

            }
            else if (item == 3)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);
                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x00);   //讀取色彩校正結果

            }
            else if (item == 4)
            {
                show_main_message1a("還沒做好", S_FALSE, 30);
                return;

                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

            }
            else if (item == 5)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0xCC);

            }
            else if (item == 6)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

                Send_Data_PLC_PC(0xFF, 0xCC, 0xBB, 0xAA);

            }
            else if (item == 7)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

                Send_Data_PLC_PC(0xFF, 0x33, 0x88, 0x77);

            }
            else if (item == 8)
            {
                show_main_message1a(((Button)sender).Text, S_FALSE, 30);

                Send_Data_PLC_PC(0xFF, 0xAA, 0xBB, 0x10);

            }
            else if (item == 9)
            {
                if ((tb_sn1.Text.Length != 10) || (tb_sn2.Text.Length != 12))
                {
                    make_camera_data();
                }

                Send_Data_PLC_PC(0xC0, 0x12, 0x34, 0x56);   //寫入相機序號

                show_main_message2b("寫入相機序號", S_FALSE, 30);

                richTextBox1.Text += "相機序號1長度 : " + tb_sn1.Text.Length.ToString() + "\n";
                richTextBox1.Text += "相機序號2長度 : " + tb_sn2.Text.Length.ToString() + "\n";

                int i;

                byte[] sn_data_tmp = new byte[22];
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
                    //richTextBox1.Text += "i = " + i.ToString() + " tmp data : " + tb_sn2.Text[i - 10].ToString() + "\n";
                }

                //richTextBox1.Text += "\n";

                //Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write    ols

                if (flag_comport_pc_ims_ok == false)
                {
                    show_main_message0("PC-IMS 未連線", S_FALSE, 30);
                    return;
                }
                serialPort2.Write(sn_data_tmp, 0, 22);

            }

            return;
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

        private void bt_plc_0_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 0);
        }

        private void bt_plc_1_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 1);
        }

        private void bt_plc_2_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 2);
        }

        private void bt_plc_3_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 3);
        }

        private void bt_plc_4_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 4);
        }

        private void bt_plc_5_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 5);
        }

        private void bt_plc_6_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 6);
        }

        private void bt_plc_7_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 7);
        }

        private void bt_plc_8_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 8);
        }

        private void bt_plc_9_Click(object sender, EventArgs e)
        {
            do_plc_command(sender, e, 9);
        }

        private void bt_pc_0_Click(object sender, EventArgs e)
        {
            //發送系統連線狀態給PLC
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

            richTextBox1.Text += "發送系統連線狀態給PLC(任意)\n";

            Random r = new Random();
            int connection0 = r.Next(2);    //PLC-PC
            int connection1 = r.Next(2);    //PC-IMS
            int connection2 = r.Next(2);    //IMS-Camera
            int connection3 = r.Next(2);    //Camera Video
            int connection4 = r.Next(2);    //dongle

            //richTextBox1.Text += connection0.ToString() + " " + connection1.ToString() + " " + connection2.ToString() + " " + connection3.ToString() + " " + connection4.ToString() + "\n";

            int connection = 0;
            if (connection0 == 0)
            {
                richTextBox1.Text += "PLC-PC 未連線\n";
            }
            else
            {
                richTextBox1.Text += "PLC-PC 已連線\n";
                connection |= 1 << 0;
            }
            if (connection1 == 0)
            {
                richTextBox1.Text += "PC-IMS 未連線\n";
            }
            else
            {
                richTextBox1.Text += "PC-IMS 已連線\n";
                connection |= 1 << 1;
            }

            if (connection2 == 0)
            {
                richTextBox1.Text += "IMS-Camera 未連線\n";
            }
            else
            {
                richTextBox1.Text += "IMS-Camera 已連線\n";
                connection |= 1 << 2;
            }

            if (connection3 == 0)
            {
                richTextBox1.Text += "Camera Video 未連線\n";
            }
            else
            {
                richTextBox1.Text += "Camera Video 已連線\n";
                connection |= 1 << 3;
            }

            if (connection4 == 0)
            {
                richTextBox1.Text += "dongle 未連線\n";
            }
            else
            {
                richTextBox1.Text += "dongle 已連線\n";
                connection |= 1 << 4;
            }

            byte xx = 0xFF;
            byte yy = (byte)connection;
            byte zz = 0;

            Send_Data_PC_PLC(0xFF, xx, yy, zz);
        }

        private void bt_pc_1_Click(object sender, EventArgs e)
        {
            //發送命令給PLC
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);
            richTextBox1.Text += "發送命令給PLC\n";

            Random r = new Random();
            byte xx = (byte)r.Next(256);
            byte yy = (byte)r.Next(256);
            byte zz = (byte)r.Next(256);

            Send_Data_PC_PLC(0xFF, xx, yy, zz);
        }

        private void bt_pc_2_Click(object sender, EventArgs e)
        {
            //回傳色彩校正結果
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

            Random r = new Random();
            byte xx = 0xAA;
            byte yy = (byte)r.Next(14);
            byte zz = 0;

            Send_Data_PC_PLC(0xFF, xx, yy, zz);

            richTextBox1.Text += "回傳色彩校正結果, " + yy.ToString() + "\n";

            switch (yy)
            {
                case S_OK: richTextBox1.Text += "OK\n"; break;
                case CAMERA_NONE: richTextBox1.Text += "dongle only, 有連接器, 無相機\n"; break;
                case DONGLE_NONE: richTextBox1.Text += "no dongle, 無連接器\n"; break;
                case CAMERA_UNKNOWN: richTextBox1.Text += "dongle camera unknown status, 相機狀態不明\n"; break;
                case CAMERA_SENSOR_FAIL: richTextBox1.Text += "dongle camera sensor fail, 相機無法讀寫\n"; break;
                case REASON_AWB_PROCESSING: richTextBox1.Text += "AWB進行中\n"; break;
                case REASON_AWB_TIMEOUT: richTextBox1.Text += "AWB作業延時\n"; break;
                case REASON_NO_COMPORT: richTextBox1.Text += "無comport連線\n"; break;
                case REASON_NO_IMS_CAMERA: richTextBox1.Text += "無IMS相機\n"; break;
                case REASON_FIND_AWB_AREA_FAIL_TOO_SMALL: richTextBox1.Text += "AWB搜尋失敗, 太小\n"; break;
                case REASON_FIND_AWB_AREA_FAIL_TOO_FAR: richTextBox1.Text += "AWB搜尋失敗, 太遠\n"; break;
                case REASON_MANUALLY_INTERRUPT: richTextBox1.Text += "AWB人為中斷\n"; break;
                default: richTextBox1.Text += "其他原因, "+yy.ToString()+"\n"; break;
            }
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

        }

        private void bt_pc_7_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_pc_8_Click(object sender, EventArgs e)
        {
            show_main_message2a(((Button)sender).Text, S_FALSE, 30);

        }


        private void bt_ims_0_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_ims_1_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_ims_2_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_ims_3_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_ims_4_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_ims_5_Click(object sender, EventArgs e)
        {
            show_main_message3a(((Button)sender).Text, S_FALSE, 30);

        }

        private void bt_plc_generate_sn_Click(object sender, EventArgs e)
        {
            make_camera_data();
        }

        void make_camera_data()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[10];
            var stringChars2 = new char[12];
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

            stringChars2[0] = chars1[random.Next(chars1.Length)];
            for (int i = 1; i < stringChars2.Length; i++)
            {
                stringChars2[i] = chars2[random.Next(chars2.Length)];
            }
            var finalString2 = new String(stringChars2);
            richTextBox1.Text += "相機序號2：" + finalString2 + "\n";

            tb_sn1.Text = finalString1;
            tb_sn2.Text = finalString2;

            show_main_message1a("製作相機資料完成", S_OK, 30);

            richTextBox1.Text += "len1 = " + tb_sn1.Text.Length.ToString() + "\n";
            richTextBox1.Text += "len2 = " + tb_sn2.Text.Length.ToString() + "\n";
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

                if ((BytesToRead > 0) && (BytesToRead < 21) && (BytesToRead != UART_BUF_LENGTH) && (flag_need_to_merge_data == 0))
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
                        if (BytesToRead == UART_BUF_LENGTH)
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
                                    lb_sn1.Text = "xxxx[S/N] : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
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

                            bool flag_no_camera_serial1 = true;
                            bool flag_no_camera_serial2 = true;
                            lb_sn1.Text = "[S/N] : ";
                            lb_sn2.Text = "[S/N] : ";

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
                                        lb_sn1.Text += (char)input[i];
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
                                        lb_sn1.Text += (char)input[i];
                                        flag_no_camera_serial1 = false;
                                    }
                                }
                            }

                            for (i = 16; i < (16 + 11); i++)
                            {
                                //richTextBox1.Text += ((int)input[i]).ToString("X2") + "  ";
                                if ((i > 16) && (((int)input[i] < '0') || ((int)input[i] > '9')))
                                {
                                    flag_no_camera_serial2 = true;
                                    break;
                                }
                                else
                                {
                                    lb_sn2.Text += (char)input[i];
                                    flag_no_camera_serial2 = false;
                                }
                            }

                            if (flag_no_camera_serial1 == true)
                            {
                                lb_sn1.Text = "[S/N] : 無相機序號資料1";
                            }
                            else
                            {
                            }
                            if (flag_no_camera_serial2 == true)
                            {
                                lb_sn2.Text = "[S/N] : 無相機序號資料2";
                            }
                            else
                            {
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




        //22222
        private void SpyMonitorRX2()
        {
            richTextBox1.Text += "do SpyMonitorRX() len = " + BytesToRead.ToString() + "\n";

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







    }
}

