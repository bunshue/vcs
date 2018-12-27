using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;          //for serial ports

namespace my_vcs_15_zw
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;
        int IsRunning;

        public Form1()
        {
            InitializeComponent();
            button_Run.Enabled = true;
            button_Stop.Enabled = false;
            button_Swing.Enabled = true;
            button_NoSwing.Enabled = false;
            btn_error1.Enabled = false;
            btn_error2.Enabled = false;
            btn_error3.Enabled = false;
            btn_error4.Enabled = false;
            btn_error5.Enabled = false;
            btn_error6.Enabled = false;
            btn_error7.Enabled = false;
            btn_error8.Enabled = false;
            IsRunning = 0;
            label_rpm.Text = 0.ToString();
            label_rpm.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = 0.ToString();
            label_target_speed.ForeColor = System.Drawing.Color.Red;
        }

        private void button1_Click(object sender, EventArgs e)
        {
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
                    MessageBox.Show("連結Comport失敗");
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

        private void button3_Click(object sender, EventArgs e)
        {
            Send_Initial_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Initial ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Send_Disable_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Disable ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Send_Read_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Read ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Send_Disable_Read_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Disable Read ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Send_Reset_Demo_Board_Cmd();
            richTextBox1.AppendText("[PC]: Reset Demo Board\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        /*
        public bool Send_Reset_Demo_Board_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x00;
            data[3] = 0x00;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }
        */
        public bool Send_Initial_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x00;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }
        public bool Send_Disable_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x01;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Read_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x02;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Disable_Read_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x03;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
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
        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer, 0, BytesToRead);
                   
                    if (BytesToRead == 3)
                    	SpyMonitorRX();
            else
            {
                        //資料不是3拜，打印出來。
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += (char)receive_buffer[i];

                richTextBox1.AppendText(input);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
        }
            }
        }

        int real_speed = 0;
        int target_speed = 0;
        int real_speed_L = 0;
        int target_speed_L = 0;
        private void SpyMonitorRX()
        {
            if (BytesToRead == 3)
            {
                input = "";
                for (int i = 0; i < BytesToRead; i++)
                    input += (char)receive_buffer[i];

                if (input[0] == 0xDD)
                {
                    //MessageBox.Show("PC got ack");
                    progressBar1.Value = 0;
                }
                else if (input[0] == 0xEE)
                {
                    //MessageBox.Show("ZZZZZZ, value = " + Convert.ToString(input[1], 10));
                    progressBar2.Value = 100;

                    if(input[1] == 0)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if(input[1]==1)
                    {
                        btn_error1.Enabled = true;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 2)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = true;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 3)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = true;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 4)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = true;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 5)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = true;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 6)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = true;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 7)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = true;
                        btn_error8.Enabled = false;
                    }
                    else if (input[1] == 8)
                    {
                        btn_error1.Enabled = false;
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                        btn_error4.Enabled = false;
                        btn_error5.Enabled = false;
                        btn_error6.Enabled = false;
                        btn_error7.Enabled = false;
                        btn_error8.Enabled = true;
                    }
                    else if (input[1] == 15)
                    {
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                    }
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC1)
                {
                    progressBar2.Value = 100;
                    real_speed_L = (int)input[1];
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC2)
                {
                    progressBar2.Value = 100;
                    real_speed = (((int)input[1]) << 8) + real_speed_L;
                    label_rpm.Text = real_speed.ToString();
                    real_speed = 0;
                    if (real_speed == 0)
                        label_rpm.ForeColor = System.Drawing.Color.Red;
                    else
                        label_rpm.ForeColor = System.Drawing.Color.Green;
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC3)
                {
                    progressBar2.Value = 100;
                    target_speed_L = (int)input[1];
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC4)
                {
                    progressBar2.Value = 100;
                    target_speed = (((int)input[1]) << 8) + target_speed_L;
                    label_target_speed.Text = target_speed.ToString();
                    target_speed = 0;
                    if (target_speed == 0)
                        label_rpm.ForeColor = System.Drawing.Color.Red;
                    else
                        label_rpm.ForeColor = System.Drawing.Color.Green;
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC5)
                {
                    progressBar2.Value = 100;
                    tb_ADCB.Text = Convert.ToString(input[1], 16);
                    tb_ADCB_mV.Text = Convert.ToString((input[1] << 4) * 5000 / 4096);
                    tb_VAC.Text = Convert.ToString((input[1] << 4) * 5000 / 4096 *(2000+20)/20/1414);
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC6)
                {
                    progressBar2.Value = 100;
                    tb_ADCA.Text = Convert.ToString(input[1], 16);
                    tb_ADCA_mV.Text = Convert.ToString((input[1] << 4) * 5000 / 4096);
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC7)
                {
                    progressBar2.Value = 100;
                    tb_svpwm_m.Text = Convert.ToString(input[1], 10);
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC8)
                {
                    progressBar2.Value = 100;
                    switch (input[1] & 0x03)
                    { 
                        case 0:
                            status_motor.Text = "START";
                            status_motor.ForeColor = Color.Green;
                            break;
                        case 1:
                            status_motor.Text = "STOP";
                            status_motor.ForeColor = Color.Red;
                            break;
                        default:
                            status_motor.Text = "UNKNOWN";
                            status_motor.ForeColor = Color.Red;
                            break;
                    }
                    switch ((input[1]>>2) & 0x03)
                    { 
                        case 0:
                            status_power.Text = "POWER_NORMAL";
                            status_power.ForeColor = Color.Green;
                            break;
                        case 1:
                            status_power.Text = "POWER_LOW";
                            status_power.ForeColor = Color.Red;
                            break;
                        case 2:
                            status_power.Text = "POWER_HIGH";
                            status_power.ForeColor = Color.Red;
                            break;
                        default:
                            status_power.Text = "UNKNOWN";
                            status_power.ForeColor = Color.Red;
                            break;
                    }
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
            }
            else
            {
                //資料是3拜，但是解不出所要的資訊。
                /*
                richTextBox1.AppendText(input);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                */
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show("ZW專用\n" + "韌體：CS8963_Sample_Codeg_vcs2_zw\n" + "增加了About頁");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            Comport_Scan();
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
            Comport_Scan();
            tabControl1.SelectedIndex = 7;      //程式啟動時，直接跳到ZW那頁。
            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox5.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (comboBox3.SelectedIndex != -1)
            {
                richTextBox1.Text += "[PC]: Send_Initial_DAC_Cmd\n";
                Send_Initial_DAC_Cmd(comboBox3.SelectedIndex);
            }
            else
                MessageBox.Show("您還沒有選擇DAC輸出埠");
        }

        private void button12_Click(object sender, EventArgs e)
        {
            if (comboBox3.SelectedIndex != -1)
            {
                richTextBox1.Text += "[PC]: Send_Disable_DAC_Cmd\n";
                Send_Disable_DAC_Cmd(comboBox3.SelectedIndex);
            }
            else
                MessageBox.Show("您還沒有選擇DAC輸出埠");
        }

        public bool Send_Initial_DAC_Cmd(int pin)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x02;
            data[3] = 0x00;
            data[4] = (byte)pin;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Disable_DAC_Cmd(int pin)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x02;
            data[3] = 0x01;
            data[4] = (byte)pin;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            double output = 0;
            if (textBox1.Text.Length <= 0)
            {
                MessageBox.Show("未輸入資料");
        }
            else
            {
                string input = textBox1.Text; ;
                byte value = 0;
                for (int i = 0; i < input.Length; i++)
                {
                    if ((input[i] >= (Char)48 && input[i] <= (Char)57))
                    {
                        value = (byte)(input[i] - 48);

                    }
                    else if ((input[i] >= 'A') && (input[i] <= 'F'))
        {
                        value = (byte)(input[i] - 'A' + 10);
                    }
                    else if ((input[i] >= 'a') && (input[i] <= 'f'))
                    {
                        value = (byte)(input[i] - 'a' + 10);
                    }
                    output = output * 16 + value;
                    //MessageBox.Show("data : " + input[i] + " value : " + value);
                }
                if (output > 1023)
                    MessageBox.Show("輸入資料錯誤，最大值為0x3ff。");
            else
                {
                    //MessageBox.Show("輸入資料正確。");
                    Send_DAC_Data_Cmd(comboBox3.SelectedIndex, ((int)output >> 8) & 0x3, (int)output & 0xff);
                    richTextBox1.Text += "[PC]: Send_DAC_Data_Cmd data = ";
                    richTextBox1.Text += output;
                    richTextBox1.Text += "\n";

                }
            }

        }
        public bool Send_DAC_Data_Cmd(int pin, int dach, int dacl)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x02;
            data[3] = 0x02;
            data[4] = (byte)pin;
            data[5] = (byte)(dach);
            data[6] = (byte)(dacl);
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }


        private void button14_Click(object sender, EventArgs e)
        {
            if (textBox5.Text.Length <= 0)
                MessageBox.Show("您還沒有設定DAC電壓值");
            else
            {
                if ((int.Parse(textBox5.Text) > 5000) || (int.Parse(textBox5.Text) < 0))
                    MessageBox.Show("不合法的DAC電壓值");
                else
                {
                    richTextBox1.Text += "[PC]: Send_DAC_Voltage_Cmd, voltage = ";
                    richTextBox1.Text += textBox5.Text;
                    richTextBox1.Text += "\n";
                    Send_DAC_Voltage_Cmd(comboBox3.SelectedIndex, int.Parse(textBox5.Text));
                }
            }
        }

        public bool Send_DAC_Voltage_Cmd(int pin, int mV)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x02;
            data[3] = 0x03;
            data[4] = (byte)pin;
            data[5] = (byte)((mV >> 8) & 0xff);
            data[6] = (byte)(mV & 0xff);
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "[PC]: Send_DAC_Demo_Mode_Cmd\n";
            Send_DAC_Demo_Mode_Cmd(1);
        }

        public bool Send_DAC_Demo_Mode_Cmd(int on_off)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x02;
            data[3] = 0x04;
            data[4] = (byte)on_off;
            data[5] = 0x000;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十六進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || ((e.KeyChar >= 'A') && (e.KeyChar <= 'F')) || ((e.KeyChar >= 'a') && (e.KeyChar <= 'f')) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)13) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            numericUpDown1.Value = trackBar1.Value;
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            trackBar1.Value = (Int32)numericUpDown1.Value;
        }

        private void button_Set_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: 設定, 速度 = " + numericUpDown1.Value.ToString() + " 檔 = " + (300 + 50 * (numericUpDown1.Value-1)).ToString());

            if (button_Swing.Enabled == true)
                richTextBox1.AppendText(" RPM, 停止搖頭\n");
            else
                richTextBox1.AppendText(" RPM, 搖頭\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Speed_Cmd(1);
        }

        private void button_Run_Click(object sender, EventArgs e)
        {
            button_Run.Enabled = false;
            button_Stop.Enabled = true;

            richTextBox1.AppendText("[PC]: 啟動, 速度 = " + numericUpDown1.Value.ToString());
            if (button_Swing.Enabled == true)
                richTextBox1.AppendText(" 檔, 停止搖頭\n");
            else
                richTextBox1.AppendText(" 檔, 搖頭\n");

            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Speed_Cmd(1);
        }

        private void button_Stop_Click(object sender, EventArgs e)
        {
            button_Run.Enabled = true;
            button_Stop.Enabled = false;

            richTextBox1.AppendText("[PC]: 停止\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Speed_Cmd(0);
        }

        private void button_Swing_Click(object sender, EventArgs e)
        {
            //if (IsRunning == 0)
            {
                button_Swing.Enabled = false;
                button_NoSwing.Enabled = true;

                richTextBox1.AppendText("[PC]: 搖頭\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                Send_Speed_Cmd(1);
            }
        }

        private void button_NoSwing_Click(object sender, EventArgs e)
        {
            //if (IsRunning == 0)
            {
                button_Swing.Enabled = true;
                button_NoSwing.Enabled = false;

                richTextBox1.AppendText("[PC]: 停止搖頭\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                Send_Speed_Cmd(1);
            }
        }

        public bool Send_Speed_Cmd(int on_off)
        {
            byte[] data = new byte[3];
            byte speed;
            int swing;
            int value;

            speed = (byte)trackBar1.Value;
            swing = (button_NoSwing.Enabled == true)?1:0;

            if (on_off == 0)
                speed = 0;

            IsRunning = (speed ==0)?0:1;

            if (IsRunning == 0)
            {
                button_Run.Enabled = true;
                button_Stop.Enabled = false;
            }
            else
            {
                button_Run.Enabled = false;
                button_Stop.Enabled = true;
            }
            data[0] = 0xD1;

            value = (speed & 0x1f) | (byte)swing << 6;
            data[1] = (byte)value;

            data[2] = CalcCheckSum(data, 2);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                return false;
            }
            return true;
        }
        public bool Send_Reset_Demo_Board_Cmd()
        {
            byte[] data = new byte[3];
            data[0] = 0xD1;
            data[1] = 0xff;
            data[2] = CalcCheckSum(data, 2);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://www.myson.com.tw/");
        }
    }
}
