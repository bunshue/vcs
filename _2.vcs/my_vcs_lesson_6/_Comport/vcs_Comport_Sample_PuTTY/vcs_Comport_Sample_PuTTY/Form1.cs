using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports

namespace vcs_Comport_Sample_PuTTY
{
    public partial class Form1 : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int UART_BUF_LENGTH = 5;

        string[] COM_Ports_NameArr;
        bool flag_comport_ok = false;

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        public int BytesToRead_tmp = 0;							//緩衝區內可接收資料數
        string input = "";
        int flag_need_to_merge_data = 0;
        bool flag_read_connection_again = true;
        bool flag_show_cpu_temperature = false;

        string RxString;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.Yellow;
            Comport_Scan();

        }

        private void Comport_Scan()
        {
            comboBox_comport.Items.Clear();
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox_comport.Items.Clear();    //Clear All items in Combobox

            richTextBox1.Text += "共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
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
                comboBox_comport.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 1];   //倒數第1個
            }
        }

        private void bt_comport_scan_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void bt_comport_connect_Click(object sender, EventArgs e)
        {
            this.BackColor = Color.Yellow;
            bt_comport_connect.Enabled = true;
            bt_comport_disconnect.Enabled = false;
            flag_comport_ok = false;

            serialPort1.PortName = comboBox_comport.Text;
            serialPort1.BaudRate = 115200;

            //serialPort1.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                richTextBox1.Text += "try to open " + serialPort1.PortName + "\n";
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "fail to open " + serialPort1.PortName + ", reason : " + ex.Message + "\n";
                //MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                {
                    richTextBox1.Text += "已連上\n";

                    //pictureBox_comport.Image = vcs_Comport_Sample_Temperature.Properties.Resources.comport;
                    this.BackColor = SystemColors.ControlLight;

                    serialPort1.DtrEnable = true;   //白話地說就是通知儀器說我(電腦)這邊已經準備好了
                    //MessageBox.Show("已經連上" + serialPort1.PortName);

                    flag_comport_ok = true;
                    //flag_comport_connection_ok = false;

                    Application.DoEvents();

                    /*
                    //計算serialPort1中有多少位元組 
                    BytesToRead = serialPort1.BytesToRead;

                    if (BytesToRead > 0)
                    {
                        //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }
                    */
                    delay(50);
                    serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    //SerialPortTimer100ms2.Stop();
                    //SerialPortTimer100ms2.Start();
                    Application.DoEvents();
                    delay(100);

                    //計算serialPort1中有多少位元組 
                    BytesToRead = serialPort1.BytesToRead;

                    if (BytesToRead > 0)
                    {
                        richTextBox1.Text += "XXXXXX BytesToRead = " + BytesToRead.ToString() + "\n";
                    }

                    Application.DoEvents();


                    if (serialPort1.IsOpen)
                    {
                        bt_comport_connect.Enabled = false;
                        bt_comport_disconnect.Enabled = true;
                        this.BackColor = SystemColors.ControlLight;
                        flag_comport_ok = true;
                    }
                    else
                    {
                        bt_comport_connect.Enabled = true;
                        bt_comport_disconnect.Enabled = false;
                        this.BackColor = Color.Pink;
                        flag_comport_ok = false;
                    }
                }
                else
                {
                    //MessageBox.Show("無法連上Comport, 請重新連線");
                    richTextBox1.Text += "無法連上 " + serialPort1.PortName + ", 請重新連線";
                }
            }

            //計算serialPort1中有多少位元組 
            BytesToRead = serialPort1.BytesToRead;

            if (BytesToRead > 0)
            {
                //開啟程式時, 把所有serialPort的資料讀出來, 並丟棄之
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
            }
        }

        private void bt_comport_disconnect_Click(object sender, EventArgs e)
        {
            if (flag_comport_ok == true)
            {
                serialPort1.Close();
                this.BackColor = Color.Yellow;
                bt_comport_connect.Enabled = true;
                bt_comport_disconnect.Enabled = false;
                flag_comport_ok = false;
                //show_main_message1("COM未連線", S_FALSE, 100);
                //pictureBox_comport.Image = vcs_Comport_Sample_Temperature.Properties.Resources.x;
                //toolTip1.SetToolTip(pictureBox_comport1b, "COM未連線");
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
            RxString = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(DisplayText));
        }
    }
}
