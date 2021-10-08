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
        private const int UART_BUF_LENGTH = 5;
        string[] COM_Ports_NameArr;
        string RxString1 = "";
        string RxString2 = "";

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

            //button
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 48;

            groupBox_comport.Location = new Point(10, 10);
            groupBox_comport.Size = new Size(397, 58);

            /*
            //button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            */

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
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
            {
                //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了, putty mode
                RxString1 = serialPort1.ReadExisting();
                this.Invoke(new EventHandler(DisplayText1));
            }
        }

        private void DisplayText2(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString2);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort2_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            {
                //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了, putty mode
                RxString2 = serialPort2.ReadExisting();
                this.Invoke(new EventHandler(DisplayText2));
            }
        }



        private void Comport_Scan()
        {
            comboBox_comport.Items.Clear();    //Clear All items in Combobox
            string[] comport_names = SerialPort.GetPortNames();
            Array.Sort(comport_names);
            Array.Resize(ref COM_Ports_NameArr, comport_names.Length);
            comport_names.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "a共抓到 " + comport_names.Length.ToString() + " 個 comport :\t";
            foreach (string port in COM_Ports_NameArr)
            {
                richTextBox1.Text += port + "\t";
                comboBox_comport.Items.Add(port);
            }
            richTextBox1.Text += "\n";

            if (COM_Ports_NameArr.Length > 0)
            {
                comboBox_comport.Text = COM_Ports_NameArr[0];
            }

            if (COM_Ports_NameArr.Length >= 2)
            {
                //comboBox_comport.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
                comboBox_comport.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 1];   //倒數第1個
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

        public bool Send_IMS_Data(byte cc, byte xx, byte yy, byte zz)
        {

            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[TX] : " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");

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

        private void SpyMonitorRX()
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

            /*
            richTextBox1.AppendText("[RX] : " + ((int)input[0]).ToString("X2") + " " + ((int)input[1]).ToString("X2") + " " + ((int)input[2]).ToString("X2") + " "
                + ((int)input[3]).ToString("X2") + " " + ((int)input[4]).ToString("X2") + "  chk: " + ((int)data[4]).ToString("X2") + "\n");
            */

            if (input[0] == 0xA1)
            {
                if (input[1] == 0xCD)
                {
                }
            }
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void SerialPortTimer100ms1_Tick(object sender, EventArgs e)
        {
            {
                richTextBox1.Text += "a";
                return;
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;



                //richTextBox1.Text += BytesToRead.ToString() + " ";
                if (BytesToRead > 0)
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
                    input += "444444\n";
                    richTextBox1.AppendText(input);     //打印一般文字訊息
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }
        }

        private void bt_comport_scan_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void bt_comport_connect_Click(object sender, EventArgs e)
        {
            if ((COM_Ports_NameArr == null) || (COM_Ports_NameArr.Length == 0))
            {
                richTextBox1.Text += "沒有comport\n";
                return;
            }

            serialPort1.Close();
            this.BackColor = Color.Yellow;
            connect_comport(comboBox_comport.Text);
        }

        int connect_comport(string comport)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }

            serialPort1.PortName = comport;

            try
            {
                serialPort1.BaudRate = int.Parse(comboBox_baud_rate.Text);
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
            }
            return 1;
        }

        private void bt_comport_disconnect_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }
            richTextBox1.Text += "已離線\n";

            this.BackColor = Color.Yellow;
            //pictureBox_comport.Image = iMS_Link.Properties.Resources.x;
            //SerialPortTimer100ms1.Enabled = false;
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

        private void SerialPortTimer100ms2_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += "6";
        }

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

    }
}

