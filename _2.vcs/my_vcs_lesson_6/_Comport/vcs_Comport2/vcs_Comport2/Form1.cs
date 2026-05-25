using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports
using System.Windows.Forms.DataVisualization.Charting;  //for Series,   參考/加入參考/.NET/System.Windows.Forms.DataVisualization

using Microsoft.Win32;//for RegistryKey

namespace vcs_Comport2
{
    public partial class Form1 : Form
    {
        private const int UART_BUF_LENGTH = 5;
        string[] COM_Ports_NameArr;
        string RxString = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            this.BackColor = Color.Yellow;
            Comport_Scan();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            //button
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

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_Comport2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'^';
                data[1] = (byte)'^';
                data[2] = (byte)'^';
                data[3] = (byte)'^';
                data[4] = (byte)'^';

                serialPort1.Write(data, 0, 5);
                richTextBox1.Text += "send message ok\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'a';
                data[1] = (byte)'b';
                data[2] = (byte)'c';
                data[3] = (byte)'d';
                data[4] = (byte)'e';
                data[5] = (byte)'f';
                data[6] = (byte)'g';

                serialPort1.Write(data, 0, 7);
                richTextBox1.Text += "send message ok\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int BytesToRead = 0;							//緩衝區內可接收資料數

            if (serialPort1.IsOpen == true)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";
                richTextBox1.Text += "ReadBufferSize = " + serialPort1.ReadBufferSize.ToString() + "\n";

                if (BytesToRead > 0)
                {
                    //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                    Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區

                    if (BytesToRead <= 2048)
                    {
                        //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        serialPort1.Read(receive_buffer, 0, BytesToRead);
                    }
                    else
                    {
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }

                    string input = "";
                    for (int i = 0; i < BytesToRead; i++)
                    {
                        input += (char)receive_buffer[i];
                    }
                    richTextBox1.Text += input + "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                richTextBox1.Text += "丟棄UART buffer內的資料\n";
                serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
            }
        }

        private void DisplayText(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                //有什麼印什麼~~~~~~, 這樣就只能單純顯示訊息了, putty mode
                RxString = serialPort1.ReadExisting();
                this.Invoke(new EventHandler(DisplayText));
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

        byte dir = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                dir++;
                if (dir > 3)
                    dir = 0;

                if (dir == 0)
                    richTextBox1.Text += "原圖\n";
                else if (dir == 1)
                    richTextBox1.Text += "左右\n";
                else if (dir == 2)
                    richTextBox1.Text += "上下\n";
                else if (dir == 3)
                    richTextBox1.Text += "左右+上下\n";
                else
                    richTextBox1.Text += "XXXXX\n";

                byte DongleAddr_h;
                byte DongleAddr_l;
                byte DongleData;
                DongleAddr_h = 0x38;
                DongleAddr_l = 0x20;
                DongleData = (byte)(0x10 | (dir << 2));
                Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
            }
            else
            {
                richTextBox1.Text += "無連線\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                if (textBox1.TextLength > 0)
                {
                    richTextBox1.Text += "len = " + textBox1.TextLength.ToString() + "\n";

                    // Convert a C# string to a byte array  
                    byte[] data1 = Encoding.ASCII.GetBytes(textBox1.Text);   //字串 轉 拜列

                    byte[] data2 = Encoding.Default.GetBytes(textBox1.Text);

                    //string str = Encoding.ASCII.GetString(data1); //拜列 轉 字串
                    //richTextBox1.Text += "str = " + str + "\n";

                    foreach (byte b in data1)
                    {
                        //richTextBox1.Text += b.ToString("X2") + "\n";
                    }

                    //serialPort1.Write(data1, 0, textBox1.TextLength);

                    serialPort1.Write(data2, 0, data2.Length);

                    richTextBox1.Text += "send message ok\n";
                }
                else
                {
                    richTextBox1.Text += "無資料可傳\n";
                }
            }
            else
            {
                richTextBox1.Text += "無連線\n";
            }
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

            }
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            //richTextBox1.Text += "a";
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
                input += "aaaaaa\n";

                richTextBox1.Text += "bbbbbbbb ";
                richTextBox1.AppendText(input);     //打印一般文字訊息
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
                //SerialPortTimer100ms.Enabled = true;
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
            //SerialPortTimer100ms.Enabled = false;
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

        private void button1_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            //write 1
            string cmd = "systeminfo";
            serialPort1.Write(cmd);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            //write 2
            string cmd = "systeminfo";
            serialPort1.WriteLine(cmd);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            //write 3
        }

        private void button10_Click(object sender, EventArgs e)
        {
            RegistryKey key = Registry.LocalMachine.OpenSubKey(@"Hardware\DeviceMap\SerialComm");

            if (key != null)
            {
                //讀取所有串列通訊的名稱
                String[] names = key.GetValueNames();
                foreach (String s in names)
                {
                    richTextBox1.Text += "抓到 : " + key.GetValue(s) + "\t在 : " + s + "\n";
                }
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == false)
            {
                richTextBox1.Text += "無連線\n";
                return;
            }

            serialPort1.Write("^");
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



