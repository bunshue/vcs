using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.IO.Ports;          //for serial ports

namespace vcs_Comport6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(800, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1050, 750);
            this.Text = "vcs_Comport6";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 115200;

            //serialPort1.Open(); //原本是這一行，改寫成以下。
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
                //button1.Enabled = false;
                //button2.Enabled = true;
                richTextBox1.Text += "已連上 COM4\n";
            }
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void button2_Click(object sender, EventArgs e)
        {
            //讀取
            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                if (BytesToRead > 0)
                {
                    if (BytesToRead > 2048)
                    {
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }
                    else if (BytesToRead > 0)
                    {
                        //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        serialPort1.Read(receive_buffer, 0, BytesToRead);

                        /*
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += (char)receive_buffer[i];
                        richTextBox1.Text += input + "\n";
                        */

                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += receive_buffer[i].ToString("X2") + " ";
                        richTextBox1.Text += input + "\n";

                        //richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";

                    }
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

        public bool Send_IMS_Data0(byte cc, byte xx, byte yy, byte zz)  //directly send data
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);
            //richTextBox1.Text += "Send data:\t" + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n";
            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
            return true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //寫入
            Send_IMS_Data0(0xFF, 0x11, 0x52, 0x00); //directly send uart command
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //關閉
            serialPort1.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Info
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

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


/*
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

WriteToSerialPort2(data, 0, data.Length)


void WriteToSerialPort2(byte[] data, int offset, int count)
{
            //serialPort2.Write(data, offset, count);
            try
            {   //可能會產生錯誤的程式區段
                serialPort2.Write(data, offset, count);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
}

        public bool Get_IMS_Data(byte xx, byte yy, byte zz)
        {
            if (get_comport_status() == false)
                return false;

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

//------------------------------------------------------------  # 60個

            richTextBox1.Text += "找出所有的COM port, ";

            // Get a list of serial port names.
            string[] ports = SerialPort.GetPortNames();

            richTextBox1.Text += " 共有 " + ports.Length + " 個COM port\n";
            // Display each port name to the console.
            foreach (string port in ports)
            {
                richTextBox1.Text += "\t" + port + "\n";
            }
            richTextBox1.Text += "\n";

//------------------------------------------------------------  # 60個

//是否是指名serial port讀取長度 未達目的決不罷休?
serial.Read(bytData, 0, bytData.Length, Timeout.Infinite);

//------------------------------------------------------------  # 60個

//c#中接收16進制串口數據(com), 在textbox顯示

static int buffersize = 18;   //十六進制數的大小（假設為6Byte）
byte[] buffer = new Byte[buffersize];   //創建緩沖區

private void button1_Click(object sender, EventArgs e)
{
    serialPort1.Read(buffer, 0, buffersize);
    string ss;
    ss = byteToHexStr(buffer); //用到函數byteToHexStr
    textBox2.Text = ss;
    serialPort1.Close();
    MessageBox.Show("數據接收成功！", "系統提示");
}

//字節數組轉16進制字符串
public static string byteToHexStr(byte[] bytes)
{
    string returnStr = "";
    if (bytes != null)
    {
        for (int i = 0; i < bytes.Length; i++)
        {
            returnStr += bytes[i].ToString("X2");
        }
    }
    return returnStr;
}

//------------------------------------------------------------  # 60個

//拜列轉字串(16進制)

	static int buffersize = 18;   //十六進制數的大小（假設為6Byte）
	byte[] buffer = new Byte[buffersize];   //創建緩沖區
	
	private void button1_Click(object sender, EventArgs e)
	{
	    serialPort1.Read(buffer, 0, buffersize);
	    string ss;
	    ss = byteToHexStr(buffer); //用到函數byteToHexStr
	    textBox2.Text = ss;
	    serialPort1.Close();
	    MessageBox.Show("數據接收成功！", "系統提示");
	}
	
	//字節數組轉16進制字符串
	public static string byteToHexStr(byte[] bytes)
	{
	    string returnStr = "";
	    if (bytes != null)
	    {
	        for (int i = 0; i < bytes.Length; i++)
	        {
	            returnStr += bytes[i].ToString("X2");
	        }
	    }
	    return returnStr;
	}
	
//------------------------------------------------------------  # 60個

            //comport訊息
            if (serialPort2.IsOpen)
            {
                richTextBox1.Text += "BaudRate = " + serialPort2.BaudRate.ToString() + "\n";
                richTextBox1.Text += "StopBits = " + serialPort2.StopBits.ToString() + "\n";
                richTextBox1.Text += "DataBits = " + serialPort2.DataBits.ToString() + "\n";
                richTextBox1.Text += "Parity = " + serialPort2.Parity.ToString() + "\n";
                richTextBox1.Text += "ReadTimeout = " + serialPort2.ReadTimeout.ToString() + "\n";
            }

//------------------------------------------------------------  # 60個

用WMI查serial port可否知道是ims的comport，
若可以知道，直接連線看看～～～

//------------------------------------------------------------  # 60個

        //串口號
        public static class Serial
        {
            public const SerialPort.Serial COM1 = (SerialPort.Serial)0;
            public const SerialPort.Serial COM2 = (SerialPort.Serial)1;
        }

        //串口波特率
        public static class BaudRate
        {
            public const SerialPort.BaudRate Baud4800 = (SerialPort.BaudRate)4800;
            public const SerialPort.BaudRate Baud9600 = (SerialPort.BaudRate)9600;
            public const SerialPort.BaudRate Baud19200 = (SerialPort.BaudRate)19200;
            public const SerialPort.BaudRate Baud38400 = (SerialPort.BaudRate)38400;
            public const SerialPort.BaudRate Baud57600 = (SerialPort.BaudRate)57600;
            public const SerialPort.BaudRate Baud115200 = (SerialPort.BaudRate)115200;
            public const SerialPort.BaudRate Baud230400 = (SerialPort.BaudRate)230400;
        }

*/

