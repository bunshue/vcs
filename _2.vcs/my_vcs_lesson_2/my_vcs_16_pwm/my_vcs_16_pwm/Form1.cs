using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;          //for serial ports

namespace my_vcs_16_pwm
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;

        public Form1()
        {
            InitializeComponent();
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

            this.tabPage1_ADC.Parent = this.tabControl1;
            this.tabPage2_DAC.Parent = this.tabControl1;
            this.tabPage3_CMP.Parent = this.tabControl1;
            this.tabPage4_PWM.Parent = this.tabControl1;
            this.tabPage5_Timer.Parent = this.tabControl1;
        
        
        }

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

                    if (BytesToRead == 10)
                        SpyMonitorRX();
                    else
                    {
                        //資料不是10拜，打印出來。
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += (char)receive_buffer[i];

                        richTextBox1.AppendText(input);
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
                }
            }
        }

        private void SpyMonitorRX()
        {
            if (BytesToRead == 10)
            {
                input = "";
                for (int i = 0; i < BytesToRead; i++)
                    input += (char)receive_buffer[i];

                if ((input[0] == 0x55) && (input[1] == 0x20) && (input[2] == 0x01))
                {
                    textBox3.Text = Convert.ToString(input[3], 16) + " " + Convert.ToString(input[4], 16);
                    textBox4.Text = Convert.ToString((input[3] << 8 | input[4]) * 5000 / 4096);
                }
            }
            else
            {
                //資料是10拜，但是解不出所要的資訊。
                /*
                richTextBox1.AppendText(input);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                */
            }
        }

        /*  ZW
        private void SpyMonitorRX()
        {
            if (BytesToRead == 3)
                {
                input = "";
                for (int i = 0; i < BytesToRead; i++)
                    input += (char)receive_buffer[i];

                if (input[0] == 0x55)
                {
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
                }
            }
            else
            {
                //資料是3拜，但是解不出所要的資訊。
                //richTextBox1.AppendText(input);
                //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
        }
        */

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show("PWM測試\n" + "韌體：CS8963_Sample_Codeg_vcs3\n");
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
            //tabControl1.SelectedIndex = 1;      //程式啟動時，直接跳到DAC那頁。
            tabControl1.SelectedIndex = 3;      //程式啟動時，直接跳到PWM那頁。
            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox5.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            /* for ZW
            tabControl1.SelectedIndex = 7;      //程式啟動時，直接跳到ZW那頁。
            this.tabPage1_ADC.Parent = null;
            this.tabPage2_DAC.Parent = null;
            this.tabPage3_CMP.Parent = null;
            this.tabPage4_PWM.Parent = null;
            this.tabPage5_Timer.Parent = null;
            */
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (comboBox3.SelectedIndex != -1)
            {
                richTextBox1.AppendText("[PC]: Send_Initial_DAC_Cmd\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                Send_Initial_DAC_Cmd(comboBox3.SelectedIndex);
            }
            else
                MessageBox.Show("您還沒有選擇DAC輸出埠");
        }

        private void button12_Click(object sender, EventArgs e)
        {
            if (comboBox3.SelectedIndex != -1)
            {
                richTextBox1.AppendText("[PC]: Send_Disable_DAC_Cmd\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
                output = hex2dec(textBox1.Text);

                if (output > 1023)
                    MessageBox.Show("輸入資料錯誤，最大值為0x3ff。");
            else
                {
                    //MessageBox.Show("輸入資料正確。");
                    Send_DAC_Data_Cmd(comboBox3.SelectedIndex, ((int)output >> 8) & 0x3, (int)output & 0xff);
                    richTextBox1.AppendText("[PC]: Send_DAC_Data_Cmd data = ");
                    richTextBox1.AppendText(output.ToString());
                    richTextBox1.AppendText("\n");
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
                    richTextBox1.AppendText("[PC]: Send_DAC_Voltage_Cmd, voltage = ");
                    richTextBox1.AppendText(textBox5.Text);
                    richTextBox1.AppendText("\n");
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
            Send_DAC_Demo_Mode_Cmd(1);
            richTextBox1.AppendText("[PC]: Send_DAC_Demo_Mode_Cmd\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://www.myson.com.tw/");
        }

        private void tb_pwm_period_point_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Return)    //TextBox中輸完資料按enter的事件
            {
                tb_pwm_freq_hz.Text = (16000000 / (2 * int.Parse(tb_pwm_period_point.Text))).ToString();
                tb_pwm_period_us.Text = ((2 * int.Parse(tb_pwm_period_point.Text)) / 16).ToString();
            }
        }

        private void tb_pwm_period_us_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Return)   //TextBox中輸完資料按enter的事件
            {
                tb_pwm_period_point.Text = (8 * int.Parse(tb_pwm_period_us.Text)).ToString();
                tb_pwm_freq_hz.Text = (1000000 / (int.Parse(tb_pwm_period_us.Text))).ToString();
            }
        }

        private void tb_pwm_freq_hz_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Return)   //TextBox中輸完資料按enter的事件
            {
                tb_pwm_period_us.Text = (1000000 / (int.Parse(tb_pwm_freq_hz.Text))).ToString();
                tb_pwm_period_point.Text = (8 * 1000000 / (int.Parse(tb_pwm_freq_hz.Text))).ToString();
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: PWM初始化\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Initial_PWM_Cmd();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            int pwm_period = int.Parse(tb_pwm_period_point.Text);
            int pwm_duty = (int)numericUpDown_duty.Value;
            int pwm_deadtime = (int)numericUpDown_dt.Value;

            int pwm_p_invert = (comboBox_p_invert.SelectedIndex == 0) ? 0 : 1;
            int pwm_n_invert = (comboBox_n_invert.SelectedIndex == 0) ? 0 : 1;
            int pwm_invert = pwm_n_invert * 2 + pwm_p_invert;

            if ((pwm_period < 0) || (pwm_period > 50000))
            {
                MessageBox.Show("Illegal parameters. pwm_period = " + pwm_period.ToString());
                return;
            }
            else if ((pwm_duty < 0) || (pwm_duty > 100))
            {
                MessageBox.Show("Illegal parameters. pwm_duty = " + pwm_duty.ToString());
                return;
            }
            else if ((pwm_deadtime < 0) || (pwm_deadtime > 31))
            {
                MessageBox.Show("Illegal parameters. pwm_deadtime = " + pwm_deadtime.ToString());
                return;
            }

            Send_PWM_Parameter_Cmd((pwm_period >> 8) & 0xff, pwm_period & 0xff, pwm_duty, pwm_deadtime, pwm_invert);
            richTextBox1.AppendText("[PC]: Send PWM Parameter\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

            for (int i = 0; i < 500000; i++)
                Application.DoEvents();         //執行某一事件，以達到延遲效果

            int port_on = 0;

            if (cb_AP.Checked == true)
                port_on |= 1<<5;
            if (cb_AN.Checked == true)
                port_on |= 1<<4;
            if (cb_BP.Checked == true)
                port_on |= 1<<3;
            if (cb_BN.Checked == true)
                port_on |= 1<<2;
            if (cb_CP.Checked == true)
                port_on |= 1<<1;
            if (cb_CN.Checked == true)
                port_on |= 1<<0;

            Send_PWM_ON_OFF_Cmd(port_on);
            richTextBox1.AppendText("[PC]: 設定PWM開關, port_on = " + port_on.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        public bool Send_Initial_PWM_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x03;
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
        public bool Send_Disable_PWM_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x03;
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
        public bool Send_PWM_Parameter_Cmd(int prdh, int prdl, int duty, int deadtime, int invert)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x03;
            data[3] = 0x02;
            data[4] = (byte)prdh;
            data[5] = (byte)prdl;
            data[6] = (byte)duty;
            data[7] = (byte)deadtime;
            data[8] = (byte)invert;
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

        public bool Send_PWM_ON_OFF_Cmd(int port_on)
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x03;
            data[3] = 0x03;
            data[4] = (byte)port_on;
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

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: 關閉PWM\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Disable_PWM_Cmd();
            cb_AP.Checked = false;
            cb_AN.Checked = false;
            cb_BP.Checked = false;
            cb_BN.Checked = false;
            cb_CP.Checked = false;
            cb_CN.Checked = false;
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
    }
}
