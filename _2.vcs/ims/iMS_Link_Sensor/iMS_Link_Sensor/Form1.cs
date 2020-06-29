using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports

namespace iMS_Link_Sensor
{
    public partial class Form1 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int UART_BUF_LENGTH = 5;
        private const int CAMERA_OK = 0;	//dongle + camera
        private const int CAMERA_NONE = 1;	//dongle only
        private const int DONGLE_NONE = 2;	//no dongle
        private const int CAMERA_UNKNOWN = 3;	//dongle camera unknown status
        private const int CAMERA_SENSOR_FAIL = 6;	//dongle camera sensor fail
        bool flag_comport_ok = false;
        bool flag_comport_connection_ok = false;

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        string input = "";
        string[] COM_Ports_NameArr;
        int flag_need_to_merge_data = 0;
        int isCommandLog = 1;
        int Comport_Mode = 0;   //0: imsLink, 1: putty mode, 2: hex mode
        int g_conn_status = CAMERA_UNKNOWN;
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;
        
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (flag_comport_connection_ok == false)
            {
                richTextBox1.Text += "connect_IMS_comport()\n";
                connect_IMS_comport();
            }

            if (serialPort1.IsOpen)
            {
                button89.Enabled = false;
                button90.Enabled = true;
                this.BackColor = System.Drawing.SystemColors.ControlLight;
                flag_comport_ok = true;
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
                //pictureBox_comport.Image = imsLink.Properties.Resources.comport;
                //toolTip1.SetToolTip(pictureBox_comport, "COM已連線");

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
                //pictureBox_comport.Image = imsLink.Properties.Resources.x;
                //toolTip1.SetToolTip(pictureBox_comport, "COM未連線");

                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button89.Enabled = true;
                button90.Enabled = false;
                flag_comport_ok = false;
            }
        }

        int connect_comport(string comport)
        {
            flag_comport_ok = false;
            serialPort1.PortName = comport;

            try
            {
                serialPort1.BaudRate = int.Parse(comboBox6.Text);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                //MessageBox.Show("無法連上Comport, 請重新連線");
                richTextBox1.Text += "無法連上 " + comport + ", 請重新連線";
                button89.Enabled = true;
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
                            button89.Enabled = false;
                            button90.Enabled = true;
                            this.BackColor = System.Drawing.SystemColors.ControlLight;
                            flag_comport_ok = true;
                        }
                        else
                        {
                            button89.Enabled = true;
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

            if (flag_comport_ok == true)
                return S_OK;
            else
                return S_FALSE;
        }

        int try_connect_comport()
        {
            int ret = S_FALSE;
            //if (flag_comport_ok == true)  always close any comport
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                button89.Enabled = true;
                button90.Enabled = false;
                flag_comport_ok = false;
            }

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
                comboBox7.Text = COM_Ports_NameArr[0];
            }
            else
            {
                comboBox7.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }

            if (COM_Ports_NameArr.Length == 1)
            {
                richTextBox1.Text += "只有一個comport, try 一次\n";
                ret = connect_comport(comboBox7.Text);
            }
            else
            {
                richTextBox1.Text += "多個comport\n";

                int try_index;
                for (int i = 0; i < COM_Ports_NameArr.Length; i++)
                {
                    try_index = (i + COM_Ports_NameArr.Length - 2) % COM_Ports_NameArr.Length;  //從倒數第二個找起

                    //richTextBox1.Text += "try_index = " + try_index.ToString() + "\n";

                    comboBox7.Text = COM_Ports_NameArr[try_index];

                    serialPort1.Close();
                    this.BackColor = Color.Yellow;
                    button89.Enabled = true;
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


        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
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
                                    flag_no_camera_serial2 = false;
                                }
                            }

                            if (flag_no_camera_serial1 == true)
                            {
                            }
                            else
                            {
                            }
                            if (flag_no_camera_serial2 == true)
                            {
                            }
                            else
                            {
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
                    //if (flag_read_connection_again == false)
                      //  flag_read_connection_again = true;

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
                    }
                    else if ((input[1] == 0xEE) && (input[2] == 0xEE))
                    {
                        if (input[3] == 0x00)
                        {
                        }
                        else
                        {
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
                                if (input[2] == 0x03)
                                {
                                }
                                else if (input[2] == 0x04)
                                {
                                }
                                else if (input[2] == 0x19)
                                {
                                }
                            }
                            //richTextBox1.Text += "\n";
                        }
                        else if (input[1] == 0x58)
                        {
                            if (input[2] == 0x08)
                            {
                            }
                            //richTextBox1.Text += "ADDR : 0x" + ((int)input[1]).ToString("X2") + ((int)input[2]).ToString("X2") + ", value : 0x" + ((int)input[3]).ToString("X2") + "\n";
                        }
                    }
                    else if (input[1] == 0xA1)
                    {
                        //useless
                        int dd = (int)input[2];
                    }
                    else if (input[1] == 0xC1)
                    {
                    }
                    else if (input[1] == 0xD1)
                    {
                    }
                    else if (input[1] == 0xE1)
                    {
                    }
                    else if (input[1] == 0xF1)
                    {
                    }
                    else if (input[1] == 0xB1)
                    {
                    }
                    else if (input[1] == 0xFF)
                    {
                        g_conn_status = input[2];
                        if (g_conn_status == DONGLE_NONE)
                        {
                            show_main_message1("無連接器", S_OK, 30);
                            playSound(S_FALSE);
                        }
                        else if (g_conn_status == CAMERA_NONE)
                        {
                            show_main_message1("無相機", S_OK, 30);
                            playSound(S_FALSE);
                        }
                        else if (g_conn_status == CAMERA_OK)
                        {
                            show_main_message1("有相機", S_OK, 30);
                        }
                        else if (g_conn_status == CAMERA_SENSOR_FAIL)
                        {
                            show_main_message1("相機失效", S_OK, 30);

                        }
                        else
                        {
                            show_main_message1("相機狀態不明", S_OK, 30);
                            playSound(S_FALSE);
                        }
                        //flag_read_connection_again = true;
                    }
                    else if (input[1] == 0x99)
                    {
                        if ((input[2] == 0x00) && (input[3] == 0x00))
                        {
                        }
                        else if ((input[2] == 0x11) && (input[3] == 0x11))
                        {
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

        private void button86_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void Comport_Scan()
        {
            comboBox7.Items.Clear();
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox7.Items.Clear();    //Clear All items in Combobox

            richTextBox1.Text += "a共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox7.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox7.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                comboBox7.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }
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

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}
