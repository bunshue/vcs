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

using AForge.Video;
using AForge.Video.DirectShow;

namespace imsLink
{
    public partial class Form1 : Form
    {
        private const bool SHOW_COMPORT_LOG = false;
        private const int UART_BUF_LENGTH = 5;
        private const int CAMERA_OK = 0;	//dongle + camera
        private const int CAMERA_NONE = 1;	//dongle only
        private const int DONGLE_NONE = 2;	//no dongle
        private const int CAMERA_UNKNOWN = 3;	//dongle camera unknown status
        private const int VIDEO_OK = 0;
        private const int VIDEO_FORBID_ALL = 1;
        private const int VIDEO_FORBID_DIFFERENT_CAMERA = 2;
        private const int VIDEO_FORBID_POWEROFF_LONG_1M = 3;
        private const int VIDEO_FORBID_POWEROFF_LONG_30M = 4;
        private const int VIDEO_FORBID_PULL_OUT_LONG_1M = 5;
        private const int VIDEO_FORBID_PULL_OUT_LONG_30M = 6;
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
        int flag_command_fail = 0;
        int flag_write_serial_to_camera = 0;
        int flag_write_serial_to_camera_old = 0;
        int flag_wait_receive_data = 0;
        int flag_receive_camera_serial = 0;
        int flag_receive_camera_flash_data = 0;
        int flag_request_item = 0;
        int flag_verify_serial_data = 0;
        int flag_need_confirm = 0;
        byte cnt1 = 0;
        int cnt2 = 0;
        int cnt3 = 0;
		int g_conn_status = CAMERA_UNKNOWN;
        int[] camera_serial_data = new int[16];
        byte[] sn_data_send2 = new byte[16];

        Stopwatch stopwatch = new Stopwatch();

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
            Reset_imsLink_Setting();

            tabControl1.SelectedIndex = 1;              //接跳到第1頁。
            textBox1.Text = trackBar6.Value.ToString();

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
        }

        private void Reset_imsLink_Setting()
        {

            tabControl1.SelectedIndex = 1;      //程式啟動時，直接跳到某一頁。

            this.Width = 960;
            show_comport_log = SHOW_COMPORT_LOG;

            Comport_Mode = 0;
            this.richTextBox1.Location = new System.Drawing.Point(958, 67);
            this.richTextBox1.Size = new System.Drawing.Size(382, 594);

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
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                button1.Enabled = true;
                button2.Enabled = false;
                richTextBox1.ReadOnly = true;
            }
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // If the port is closed, don't try to send a character.
            if (!serialPort1.IsOpen) return;

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
            richTextBox1.AppendText("[PC]: Reset imsLink\n");
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
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input ="";

        private void show_info(int item)
        {
            switch (flag_request_item)
            {
                case 0x9:
                case 0xb:
                case 0xd:
                case 0xf:
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


                        if (flag_request_item == 0x9)
                        {
                            lb_a.Text = "Product : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                        }
                        else if (flag_request_item == 0xb)
                        {
                            lb_b.Text = "1MIN : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                        }
                        else if (flag_request_item == 0xd)
                        {
                            lb_d.Text = "30MIN : " + month.ToString("00") + "/"
                                + mday.ToString("00") + "/"
                                + year.ToString("0000") + " "
                                + wday.ToString() + " "
                                + hour.ToString("00") + ":"
                                + minutes.ToString("00") + ":"
                                + seconds.ToString("00");
                        }
                        else if (flag_request_item == 0xf)
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
                            richTextBox1.Text += "unknown flag_request_item = " + flag_request_item.ToString() + "\n";
                        }




                    }
                    else
                    {
                        if (flag_request_item == 0xb)
                        {
                            lb_b.Text = "1MIN : ----------------------------------";
                        }
                        else if (flag_request_item == 0xd)
                        {
                            lb_d.Text = "30MIN : ----------------------------------";
                        }
                        else if (flag_request_item == 0xf)
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
                case 0xc:
                    int i;
                    int use_time;

                    for(i = 0; i < 0x10; i++)
                    {
	                    if((int)input[i] == 0x00)
	                    {
		                    break;
	                    }
                    }
                    if(i == 0)
                    {
	                    //xil_printf("use time : 0 minute\n\r");
	                    use_time = 0;
                    }
                    else
                    {
	                    if(i == 16)
		                    i = 15;
	                    if((int)input[i - 1] == 0x0A)
	                    {
		                    //xil_printf("use time : %d minutes\n\r", i * 2 -1);
		                    use_time = i * 2 -1;
	                    }
	                    else
	                    {
		                    //xil_printf("use time : %d minutes\n\r", i * 2);
		                    use_time = i * 2;
	                    }
                    }
                    lb_c.Text = "USE : " + use_time.ToString() + " minutes";

                    break;
                case 0xe:
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
                        case VIDEO_OK:                          lb_e.Text = "VIDEO_OK"; break;
                        case VIDEO_FORBID_ALL:                  lb_e.Text = "VIDEO_FORBID_ALL"; break;
                        case VIDEO_FORBID_DIFFERENT_CAMERA:     lb_e.Text = "VIDEO_FORBID_DIFFERENT_CAMERA"; break;
                        case VIDEO_FORBID_POWEROFF_LONG_1M:     lb_e.Text = "VIDEO_FORBID_POWEROFF_LONG_1M"; break;
                        case VIDEO_FORBID_POWEROFF_LONG_30M:    lb_e.Text = "VIDEO_FORBID_POWEROFF_LONG_30M"; break;
                        case VIDEO_FORBID_PULL_OUT_LONG_1M:     lb_e.Text = "VIDEO_FORBID_PULL_OUT_LONG_1M"; break;
                        case VIDEO_FORBID_PULL_OUT_LONG_30M:    lb_e.Text = "VIDEO_FORBID_PULL_OUT_LONG_30M"; break;
                        default:                                lb_e.Text = "unknown video status : " + flag_video_status.ToString(); break;
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
            if ((flag_write_serial_to_camera == 1) && (flag_write_serial_to_camera_old == 0))
            {
                label1.Text = "ST ";
                richTextBox1.Text += "ST: " + DateTime.Now.ToString() + "\n";
                flag_write_serial_to_camera_old = flag_write_serial_to_camera;
            }
            else if ((flag_write_serial_to_camera == 0) && (flag_write_serial_to_camera_old == 1))
            {
                label1.Text += " SP " + stopwatch.ElapsedMilliseconds.ToString() + " ms";
                richTextBox1.Text += "SP: " + DateTime.Now.ToString() + "\n";
                flag_write_serial_to_camera_old = flag_write_serial_to_camera;
            }




            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer, 0, BytesToRead);
                    if (Comport_Mode == 0)  //imsLink mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                            SpyMonitorRX();
                        else if (BytesToRead == 21) // 5 + 16
                        {
                            SpyMonitorRX();

                            input = "";
                            for (int i = 5; i < (16 + 5); i++)
                                input += (char)receive_buffer[i];

                            if (flag_receive_camera_serial == 1)
                            {
                                //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                                //if (BytesToRead == 21)
                                {
                                    //input = "";
                                    //for (int i = 5; i < (16 + 5); i++)
                                        //input += (char)receive_buffer[i];

                                    richTextBox1.AppendText("[S/N]: "
                                        + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2") + "-"
                                        + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2") + "-"
                                        + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2") + "-"
                                        + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n");
                                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                                    tb_sn1.Text = "[S/N]: " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");

                                    tb_info_a.Text = "[S/N]: " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
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
                                        groupBox10.BackColor = Color.Pink;
                                    }
                                    flag_write_serial_to_camera = 0;    //寫序號完成

                                    // Stop timing
                                    stopwatch.Stop();
                                    richTextBox1.Text += "燒錄驗證完成時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
                                }
                            }
                            else if (flag_receive_camera_flash_data == 1)
                            {
                                richTextBox1.Text += "tttBytesToRead = " + BytesToRead.ToString() + "\n";
                                //if (BytesToRead == 16)
                                {

                                    //input = "";
                                    //for (int i = 0; i < 16; i++)
                                        //input += (char)receive_buffer[i];

                                    richTextBox1.AppendText("[Data]: "
                                        + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2") + "-"
                                        + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2") + "-"
                                        + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2") + "-"
                                        + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2") + "\n");
                                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                                    textBox5.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                        + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                        + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                        + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");

                                    switch (flag_request_item)
                                    {
                                        case 0xb:
                                            tb_info_b.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case 0xc:
                                            tb_info_c.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case 0xd:
                                            tb_info_d.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case 0xe:
                                            tb_info_e.Text = "Data : " + ((int)input[0]).ToString("X2") + ((int)input[1]).ToString("X2") + "-" + ((int)input[2]).ToString("X2") + ((int)input[3]).ToString("X2")
                                                + "-" + ((int)input[4]).ToString("X2") + ((int)input[5]).ToString("X2") + "-" + ((int)input[6]).ToString("X2") + ((int)input[7]).ToString("X2")
                                                + "-" + ((int)input[8]).ToString("X2") + ((int)input[9]).ToString("X2") + "-" + ((int)input[10]).ToString("X2") + ((int)input[11]).ToString("X2")
                                                + "-" + ((int)input[12]).ToString("X2") + ((int)input[13]).ToString("X2") + "-" + ((int)input[14]).ToString("X2") + ((int)input[15]).ToString("X2");
                                            break;
                                        case 0xf:
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



                        }
                        else
                        {
                            /*
                            //for UART debug
                            lb_uart_debug.Text += BytesToRead.ToString();
                            lb_uart_debug.Text += ' ';
                            */

                            //資料不是5拜，打印出來。
                            input = "aa unknown data, len = " + BytesToRead.ToString() + ", data : ";
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
                            richTextBox1.AppendText("[UN]: ");
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
            richTextBox1.Text += "do SpyMonitorRX()\n";

            string message = "";
            //if (BytesToRead == 5)
            {
                input = "";
                for (int i = 0; i < UART_BUF_LENGTH; i++)
                    input += (char)receive_buffer[i];

                if (isCommandLog == 1)
                {
                    richTextBox1.AppendText("[RX]: " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " " + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "\n");
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
                        flag_command_fail = 1;
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
                    else if (input[1] == 0xFF)
                    {
                        g_conn_status = input[2];
                        if (g_conn_status == DONGLE_NONE)
                        {
                            textBox7.Text = "無連接器";
                            textBox7.BackColor = Color.Red;
                            panel3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                        }
                        else if (g_conn_status == CAMERA_NONE)
                        {
                            textBox7.Text = "有連接器, 無相機";
                            textBox7.BackColor = Color.Red;
                            panel3.BackgroundImage = imsLink.Properties.Resources.recorder_none;
                            panel4.BackgroundImage = imsLink.Properties.Resources.recorder_none;

                        }
                        else if (g_conn_status == CAMERA_OK)
                        {
                            textBox7.Text = "有連接器, 有相機";
                            textBox7.BackColor = Color.White;
                            panel3.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                            panel4.BackgroundImage = imsLink.Properties.Resources.recorder_ok;
                        }
                        else
                        {
                            textBox7.Text = "狀態不明, status = " + g_conn_status.ToString();
                            textBox7.BackColor = Color.Red;
                            panel3.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
                            panel4.BackgroundImage = imsLink.Properties.Resources.recorder_fail;
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
                    message += "[bb unknown data1]: ";
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
                message += "[cc unknown data2]: ";
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
            //Comport_Scan();
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
            //Comport_Scan();
            lb_a.Text = "";
            lb_b.Text = "";
            lb_c.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
            this.tb_sn2.Focus();
            bt_confirm.Visible = false;
            lb_warning.Text = "";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString();
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
        }

        bool show_comport_log = SHOW_COMPORT_LOG;
        private void button33_Click(object sender, EventArgs e)
        {
            if(show_comport_log == false)
            {
                show_comport_log = true;
                button33.BackgroundImage = imsLink.Properties.Resources.close_log;
                this.Width += 400;
            }
            else
            {
                show_comport_log = false;
                button33.BackgroundImage = imsLink.Properties.Resources.open_log;
                this.Width -= 400;
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
            string filename = "imsLink_Log." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            StreamWriter sw = File.CreateText(filename);
            sw.Write(richTextBox1.Text);
            sw.Close();
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
            richTextBox1.AppendText("[PC]: Putty mode\n");
            Comport_Mode = 1;
            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
        }

        private void button88_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: imsLink mode\n");
            Comport_Mode = 0;
            this.richTextBox1.Location = new System.Drawing.Point(958, 67);
            this.richTextBox1.Size = new System.Drawing.Size(382, 594);
        }

        private void button87_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: Hex mode\n");
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
                        if(Comport_Mode == 0)
                        {
                            Comport_Mode = 1;
                            richTextBox1.AppendText("[PC]: Putty mode\n");
                            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
                            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
                        }
                        else if (Comport_Mode == 1)
                        {
                            Comport_Mode = 2;
                            richTextBox1.AppendText("[PC]: Hex mode\n");
                            this.richTextBox1.Location = new System.Drawing.Point(4, 67);
                            this.richTextBox1.Size = new System.Drawing.Size(958 - 4 + 382 + 10, 594);
                        }
                        if (Comport_Mode == 2)
                        {
                            Comport_Mode = 0;
                            richTextBox1.AppendText("[PC]: imsLink mode\n");
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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

            richTextBox1.AppendText("[TX]: " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            if (serialPort1.IsOpen)
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

            richTextBox1.AppendText("[TX]: " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

            if (serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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

        private void button122_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("目前時間 : " + DateTime.Now.ToString() + "\n");
            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
        }

        private void button123_Click(object sender, EventArgs e)
        {
            if (comboBox5.SelectedIndex == 0)
            {
                if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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
            if (!serialPort1.IsOpen)
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

        private void textBox7_TextChanged(object sender, EventArgs e)
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
            if (!serialPort1.IsOpen)
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
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel3.BackgroundImage = null;
            panel4.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn1.BackColor = Color.Gray;
            tb_info_a.Clear();
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            while (g_conn_status == CAMERA_UNKNOWN)
            {
                richTextBox1.Text += "-";
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
                Get_IMS_Data(0, 0xAA, 0xAA);
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
        }

        private void button28_Click(object sender, EventArgs e)
        {
            textBox5.Clear();
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int page = Convert.ToInt32(textBox6.Text, 16);
            Send_IMS_Data(0xD1, (byte)page, 0, 0); 



        }

        private void button64_Click(object sender, EventArgs e)
        {
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel3.BackgroundImage = null;
            panel4.BackgroundImage = null;
            tb_sn1.Clear();
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_IMS_Data(0xFF, 0, 0, 0);

            this.tb_sn2.Focus();
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
            byte page;

            tb_sn2.Clear();
            tb_info_a.BackColor = Color.White;
            tb_info_a.Clear();
            tb_info_b.Clear();
            tb_info_c.Clear();
            tb_info_d.Clear();
            tb_info_e.Clear();
            tb_info_f.Clear();
            lb_a.Text = "";
            lb_b.Text = "";
            lb_c.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            tb_info_a2.BackColor = Color.White;
            tb_info_b2.BackColor = Color.White;
            tb_info_c2.BackColor = Color.White;
            tb_info_d2.BackColor = Color.White;
            tb_info_e2.BackColor = Color.White;
            tb_info_f2.BackColor = Color.White;
            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel3.BackgroundImage = null;
            panel4.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn1.BackColor = Color.Gray;
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            while (g_conn_status == CAMERA_UNKNOWN)
            {
                richTextBox1.Text += "-";
                delay(100);
            }
            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                tb_info_a.Text = "無連接器";
                tb_info_a.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                tb_info_a.Text = "有連接器, 無相機";
                tb_info_a.BackColor = Color.Red;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_sn1.Text = "有連接器, 有相機";
                tb_sn1.BackColor = Color.White;
                tb_info_a.Text = "有連接器, 有相機";
                tb_info_a.BackColor = Color.White;
                Get_IMS_Data(0, 0xAA, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0x9;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0xb;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0xc;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0xd;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0xe;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }

                page = 0xf;
                Get_IMS_Data(1, page, 0xAA);
                while (flag_wait_receive_data == 1)
                {
                    richTextBox1.Text += "+";
                    delay(100);
                }
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
            }
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tabControl1.SelectedIndex == 3)
            {
                USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
                if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
                {
                    button12.Enabled = true;
                    Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);
                    //Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                    Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                }
                else
                {
                    button12.Enabled = false;
                    richTextBox1.Text += "無影像裝置\n";
                }
            }
            else
            {
                if (Cam != null)
                {
                    if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                    {
                        Cam.Stop();   // WebCam stops capturing images.
                    }
                }

                this.tb_sn2.Focus();
            }
        }

        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (flag_need_confirm == 1)
            {
                lb_warning.Text = "請先解除鎖定";
                richTextBox1.Text += "請先解除鎖定\n";
                return;
            }

            lb_sn1.Text = "";
            lb_sn2.Text = "";
            lb_sn3.Text = "";
            groupBox10.BackColor = System.Drawing.SystemColors.ControlLightLight;

            textBox7.Clear();
            textBox7.BackColor = Color.Gray;
            panel3.BackgroundImage = null;
            panel4.BackgroundImage = null;
            tb_sn1.Clear();
            tb_sn1.BackColor = Color.Gray;
            tb_info_a.Clear();
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            g_conn_status = CAMERA_UNKNOWN;
            Send_IMS_Data(0xFF, 0, 0, 0);

            while (g_conn_status == CAMERA_UNKNOWN)
            {
                richTextBox1.Text += "-";
                delay(100);
            }

            if (g_conn_status == DONGLE_NONE)
            {
                tb_sn1.Text = "無連接器";
                tb_sn1.BackColor = Color.Red;
                flag_need_confirm = 1;
                bt_confirm.Visible = true;
            }
            else if (g_conn_status == CAMERA_NONE)
            {
                tb_sn1.Text = "有連接器, 無相機";
                tb_sn1.BackColor = Color.Red;
                flag_need_confirm = 1;
                bt_confirm.Visible = true;
            }
            else if (g_conn_status == CAMERA_OK)
            {
                tb_sn1.Text = "有連接器, 有相機";
                tb_sn1.BackColor = Color.White;
                if (flag_write_serial_to_camera == 0)
                {
                    if (tb_sn3.Text.Length > 0)
                        tb_sn2.Text = tb_sn3.Text;
                    else
                        tb_sn2.Text += "1234567890abcdef";
                }
                else
                    richTextBox1.Text += "正在寫序號中......., abort\n";
            }
            else
            {
                tb_sn1.Text = "狀態不明, status = " + g_conn_status.ToString();
                flag_need_confirm = 1;
                bt_confirm.Visible = true;
            }


            
            
        }

        private void scanner_timer_Tick(object sender, EventArgs e)
        {
            if((cnt3 % 1) == 0)
            {
                this.tb_sn2.Focus();
            }

            if (flag_need_confirm == 1)
            {
                return;
            }

            if (flag_write_serial_to_camera == 0)
            {
                if (tb_sn2.Text.Length > 0)
                {
                    int i;
                    if (cb_fix_length.Checked == true)
                    {

                        int valid_data_len = 0;
                        for (i = 0; i < tb_sn2.Text.Length; i++)
                        {
                            if (tb_sn2.Text[i] != '-')
                                valid_data_len++;
                        }
                        if (valid_data_len != int.Parse(tb_fix_length.Text))
                        {
                            richTextBox1.Text += "序號長度錯誤\n";
                            tb_sn2.Text = "";

                            tb_result.Text = "序號長度錯誤";
                            tb_result.ForeColor = Color.Black;
                            tb_result.BackColor = Color.Red;
                            groupBox10.BackColor = Color.Pink;

                            flag_need_confirm = 1;
                            bt_confirm.Visible = true;
                            return;
                        }
                    }

                    flag_write_serial_to_camera = 1;
                    tb_result.Text = "----";
                    tb_result.ForeColor = Color.White;
                    tb_result.BackColor = Color.Gray;

                    //開始計時
                    stopwatch.Reset();
                    stopwatch.Start();

                    lb_sn1.Text = "序號 : " + tb_sn2.Text + "       len = " + tb_sn2.Text.Length.ToString() + ",   寫入資料中.......";

                    //tb_sn2.Text = "0011-2233-4455-6677-8899-aabb-ccdd-eeff";
                    richTextBox1.Text += "tb_sn2 len = " + tb_sn2.Text.Length.ToString() + "\n";
                    int[] sn_data = new int[32];
                    int[] sn_data_send = new int[16];
                    int sn_data_length = 0;

                    for (i = 0; i < 32; i++)
                    {
                        sn_data[i] = 0;
                    }

                    for (i = 0; i < tb_sn2.Text.Length; i++)
                    {
                        // 限制 TextBox只能輸入十六進位碼、'-'
                        // e.KeyChar == (Char)0x30 ~ 0x39 -----> 0~9
                        // e.KeyChar == (Char)0x41 ~ 0x46 -----> A~F
                        // e.KeyChar == (Char)0x61 ~ 0x66 -----> a~f
                        // e.KeyChar == (Char)0x2D -----------> -
                        if (((tb_sn2.Text[i] >= (Char)0x30) && (tb_sn2.Text[i] <= (Char)0x39)) ||
                            ((tb_sn2.Text[i] >= (Char)0x41) && (tb_sn2.Text[i] <= (Char)0x46)) ||
                            ((tb_sn2.Text[i] >= (Char)0x61) && (tb_sn2.Text[i] <= (Char)0x66)))
                        {
                            sn_data[sn_data_length] = tb_sn2.Text[i];
                            sn_data_length++;
                            if (sn_data_length == 32)
                                break;
                        }
                        else if (tb_sn2.Text[i] == (Char)0x2D)
                        {
                            //skip -
                        }
                        else
                        {
                            richTextBox1.Text += "序號錯誤 僅允許0~9 A~F\n";
                            lb_sn1.Text = "序號 : " + tb_sn2.Text + "       len = " + tb_sn2.Text.Length.ToString() + ",   序號錯誤 僅允許0~9 A~F";

                            tb_sn2.Text = "";
                            tb_result.Text = "序號錯誤";
                            tb_result.ForeColor = Color.Black;
                            tb_result.BackColor = Color.Red;
                            groupBox10.BackColor = Color.Pink;
                            flag_write_serial_to_camera = 0;
                            flag_need_confirm = 1;
                            bt_confirm.Visible = true;
                            return;

                        }

                    }

                    richTextBox1.Text += "real serial data length = " + sn_data_length.ToString() + " data : ";
                    for (i = 0; i < 32; i++)
                    {
                        //richTextBox1.Text += sn_data[i].ToString();
                        richTextBox1.Text += sn_data[i].ToString("X2") + " ";
                    }
                    richTextBox1.Text += "\n";

                    int high = 0;
                    int low = 0;
                    for (i = 0; i < 16; i++)
                    {
                        high = 0;
                        low = 0;
                        if ((sn_data[i * 2] >= (Char)0x30) && (sn_data[i * 2] <= (Char)0x39))
                        {
                            high = sn_data[i * 2] - 0x30;
                        }
                        else if ((sn_data[i * 2] >= (Char)0x41) && (sn_data[i * 2] <= (Char)0x46))
                        {
                            high = sn_data[i * 2] - 0x41 + 10;
                        }
                        else if ((sn_data[i * 2] >= (Char)0x61) && (sn_data[i * 2] <= (Char)0x66))
                        {
                            high = sn_data[i * 2] - 0x61 + 10;
                        }
                        if ((sn_data[i * 2 + 1] >= (Char)0x30) && (sn_data[i * 2 + 1] <= (Char)0x39))
                        {
                            low = sn_data[i * 2 + 1] - 0x30;
                        }
                        else if ((sn_data[i * 2 + 1] >= (Char)0x41) && (sn_data[i * 2 + 1] <= (Char)0x46))
                        {
                            low = sn_data[i * 2 + 1] - 0x41 + 10;
                        }
                        else if ((sn_data[i * 2 + 1] >= (Char)0x61) && (sn_data[i * 2 + 1] <= (Char)0x66))
                        {
                            low = sn_data[i * 2 + 1] - 0x61 + 10;
                        }
                        sn_data_send[i] = (high << 4) + low;
                        //richTextBox1.Text += "high = " + high.ToString() + "\tlow = " + low.ToString() + " value = " + sn_data_send[i].ToString() + "\n";
                    }

                    //richTextBox1.Text += "\nresult : \n";
                    for (i = 0; i < 16; i++)
                    {
                        sn_data_send2[i] = (byte)sn_data_send[i];
                        //richTextBox1.Text += "i = " + i.ToString() + "\t" + sn_data_send[i].ToString("X2") + "\n";
                    }

                    Send_IMS_Data(0xC0, 0x12, 0x34, 0x56);   //camera serial write

                    serialPort1.Write(sn_data_send2, 0, 16);
                    flag_verify_serial_data = 1;

                    //richTextBox1.Text += "序號 : " + tb_sn2.Text + ",       len = " + tb_sn2.Text.Length.ToString() + ",   寫入資料中.......\n";
                    richTextBox1.Text += "序號 : " + tb_sn2.Text + ",       len = " + tb_sn2.Text.Length.ToString() + ",   寫入資料  完成\n";
                    //lb_sn1.Text = "序號 : " + tb_sn2.Text + ",       len = " + tb_sn2.Text.Length.ToString() + ",   寫入資料中.......";
                    lb_sn1.Text = "序號 : " + tb_sn2.Text + ",       len = " + tb_sn2.Text.Length.ToString() + ",   寫入資料  完成";

                    /*
                    lb_sn2.Text = "驗證中";
                    richTextBox1.Text += "讀相機序號回來\n";
                    Get_IMS_Data(0, 0xAA, 0xAA);
                     */
                }
            }
            else if ((flag_write_serial_to_camera == 1) && (flag_verify_serial_data == 1))
            {
                cnt2++;
                if (cnt2 == 6)
                {
                    label1.Text += "讀" + cnt2.ToString();

                    richTextBox1.Text += "驗證開始時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";


                    tb_sn2.Clear();
                    lb_sn2.Text = "驗證中";
                    richTextBox1.Text += "\n讀相機序號回來 " + DateTime.Now.ToString() + "\n";
                    //flag_verify_serial_data = 1;
                    Get_IMS_Data(0, 0xAA, 0xAA);
                }
                else if (cnt2 == 9)
                {
                    cnt2 = 0;
                    label1.Text += "y" + cnt2.ToString();
                }
                else
                    label1.Text += "z" + cnt2.ToString();
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
            tb_info_a.Clear();
            tb_info_b.Clear();
            tb_info_c.Clear();
            tb_info_d.Clear();
            tb_info_e.Clear();
            tb_info_f.Clear();
            lb_a.Text = "";
            lb_b.Text = "";
            lb_c.Text = "";
            lb_d.Text = "";
            lb_e.Text = "";
            lb_f.Text = "";
            tb_info_a2.BackColor = Color.White;
            tb_info_b2.BackColor = Color.White;
            tb_info_c2.BackColor = Color.White;
            tb_info_d2.BackColor = Color.White;
            tb_info_e2.BackColor = Color.White;
            tb_info_f2.BackColor = Color.White;

        }

        private void button12_Click(object sender, EventArgs e)
        {
            lb_warning.Text = "";
            lb_sn1.Text = "";
            tb_sn2.Text = "";
            tb_sn1.Text = "";
            tb_sn2.Text = "";
            tb_result.Text = "----";
            tb_result.ForeColor = System.Drawing.Color.MediumSpringGreen;
            tb_result.BackColor = Color.Green;
            groupBox10.BackColor = System.Drawing.SystemColors.ControlLightLight;
            flag_need_confirm = 0;
            bt_confirm.Visible = false;

        }

        int camera_start = 0;
        private void button12_Click_1(object sender, EventArgs e)
        {
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
                Cam.Stop();  // WebCam stops capturing images.
            }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                }
            }

        }


    }
}

