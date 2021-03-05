using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;          //for serial ports

namespace vcs_Comport
{
    public partial class Form1 : Form
    {
        string[] COM_Ports_NameArr;
        string RxString;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            groupBox_comport.Location = new Point(0, 0);
            groupBox_comport.Size = new Size(397, 58);



        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_comport_scan_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void Comport_Scan()
        {
            comboBox_comport.Items.Clear();    //Clear All items in Combobox
            string[] tempString = SerialPort.GetPortNames();
            Array.Sort(tempString);
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            richTextBox1.Text += "a共抓到 " + tempString.Length.ToString() + " 個 comport :\t";
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
                comboBox_comport.Text = COM_Ports_NameArr[COM_Ports_NameArr.Length - 2];   //倒數第2個
            }
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
            serialPort1.Close();
            this.BackColor = Color.Yellow;
            //pictureBox_comport.Image = iMS_Link.Properties.Resources.x;
            //SerialPortTimer100ms.Enabled = false;

        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public Byte[] receive_buffer_tmp = new Byte[20];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";
        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            //計算serialPort1中有多少位元組 
            BytesToRead = serialPort1.BytesToRead;
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
                input += "\n";

                richTextBox1.AppendText(input);     //打印一般文字訊息
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

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
