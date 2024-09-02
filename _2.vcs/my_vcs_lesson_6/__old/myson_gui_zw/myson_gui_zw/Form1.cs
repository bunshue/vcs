using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;          //for serial ports
using System.Diagnostics;       //for Process

namespace myson_gui_zw
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;
        int IsRunning;
        int Updata_System_Status = 0;

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
            label_speed.Text = 0.ToString();
            label_speed2.Text = 0.ToString();
            label_rpm.Text = 0.ToString();
            label_rpm.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = 0.ToString();
            label_target_speed.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = "---";
            label_target_speed2.Text = 0.ToString();
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            label_target_speed2.Text = "---";
            label_rpm.Text = "---";
            label_speed.Text = "-";
            label_speed2.Text = "-";
            tb_ADCA.Text = "---";
            tb_ADCA_mV.Text = "---";
            tb_ADCB.Text = "---";
            tb_ADCB_mV.Text = "---";
            tb_VR.Text = "---";
            tb_VR_mV.Text = "---";
            tb_VR2.Text = "---";
            tb_VR_mV2.Text = "---";
            tb_Hall2.Text = "---";
            tb_svpwm_m.Text = "---";
            tb_VAC.Text = "---";
            tb_Hall.Text = "---";
            tb_Hall.ForeColor = Color.Gray;
            status_motor.Text = "";
            status_power.Text = "";
            progressBar1.Value = 0;
            progressBar2.Value = 0;
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

        private void button9_Click(object sender, EventArgs e)
        {
            Send_Reset_Demo_Board_Cmd();
            richTextBox1.AppendText("[PC]: Reset ZW Board\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
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
            label_speed.Text = 0.ToString();
            label_speed2.Text = 0.ToString();
            label_rpm.Text = 0.ToString();
            label_rpm.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = 0.ToString();
            label_target_speed.ForeColor = System.Drawing.Color.Red;
            label_target_speed2.Text = 0.ToString();
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            trackBar1.Value = 1;
            numericUpDown1.Value = 1;
            numericUpDown2.Value = 0;
            numericUpDown3.Value = 0;
            button_update_status.Text = "更新狀態";
            button_update_status.ForeColor = Color.Green;
            Updata_System_Status = 0;
            label_target_speed.Text = "---";
            label_target_speed2.Text = "---";
            label_rpm.Text = "---";
            label_speed.Text = "-";
            label_speed2.Text = "-";
            tb_ADCA.Text = "---";
            tb_ADCA_mV.Text = "---";
            tb_ADCB.Text = "---";
            tb_ADCB_mV.Text = "---";
            tb_VR.Text = "---";
            tb_VR_mV.Text = "---";
            tb_VR2.Text = "---";
            tb_VR_mV2.Text = "---";
            tb_Hall2.Text = "---";
            tb_svpwm_m.Text = "---";
            tb_VAC.Text = "---";
            tb_Hall.Text = "---";
            tb_Hall.ForeColor = Color.Gray;
            status_motor.Text = "";
            status_power.Text = "";
            progressBar1.Value = 0;
            progressBar2.Value = 0;
            //richTextBox1.Clear();
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
        int motor_status = 0;
        int power_status = 0;
        int fw_version = 0;
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
                    if (real_speed_L > 0)
                    {
                        real_speed = (((int)input[1]) << 8) + real_speed_L;
                        label_rpm.Text = real_speed.ToString();
                        real_speed = 0;
                        if (real_speed == 0)
                            label_rpm.ForeColor = System.Drawing.Color.Red;
                        else
                            label_rpm.ForeColor = System.Drawing.Color.Green;
                        real_speed_L = 0;
                    }
                    else if (real_speed_L == 0)
                    {
                        if (input[1] == 0)
                        {
                            real_speed = 0;
                            label_rpm.Text = real_speed.ToString();
                            label_rpm.ForeColor = System.Drawing.Color.Red;
                            real_speed_L = 0;
                        }
                    }
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
                    if (target_speed_L > 0)
                    {
                        target_speed = (((int)input[1]) << 8) + target_speed_L;
                        label_target_speed.Text = target_speed.ToString();
                        target_speed = 0;
                        if (target_speed == 0)
                            label_target_speed.ForeColor = System.Drawing.Color.Red;
                        else
                            label_target_speed.ForeColor = System.Drawing.Color.Green;
                        target_speed_L = 0;
                    }
                    else if (target_speed_L == 0)
                    {
                        if (input[1] == 0)
                        {
                            target_speed = 0;
                            label_target_speed.Text = target_speed.ToString();
                            label_target_speed.ForeColor = System.Drawing.Color.Red;
                            target_speed_L = 0;
                        }
                    }

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
                    label_speed.Text = Convert.ToString(input[1], 10);
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC9)
                {
                    progressBar2.Value = 100;
                    if (input[1] == 16)
                    {
                        status_motor.Text = "RESET";
                        status_motor.ForeColor = Color.Green;
                    }
                    else
                    {
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
                        switch ((input[1] >> 2) & 0x03)
                        {
                            case 0:
                                status_power.Text = "電壓正常";
                                status_power.ForeColor = Color.Green;
                                break;
                            case 1:
                                status_power.Text = "電壓欠壓";
                                status_power.ForeColor = Color.Red;
                                break;
                            case 2:
                                status_power.Text = "電壓過壓";
                                status_power.ForeColor = Color.Red;
                                break;
                            default:
                                status_power.Text = "電壓不詳";
                                status_power.ForeColor = Color.Red;
                                break;
                        }
                        motor_status = input[1] & 0x03;
                        power_status = (input[1] >> 2) & 0x03;
                        fw_version = (input[1] >> 5) & 0x07;
                    }
                    Application.DoEvents();         //執行某一事件，以達到延遲效果。
                    for (int j = 0; j < 10; j++)
                        System.Threading.Thread.Sleep(1);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xCA)
                {
                    if (tabControl1.SelectedIndex == 0)
                    {
                        switch (input[1] & 0x07)
                        {
                            case 0:
                                tb_Hall.Text = "錯 000";
                                tb_Hall.ForeColor = Color.Red;
                                break;
                            case 1:
                                tb_Hall.Text = "一 001";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 2:
                                tb_Hall.Text = "二 010";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 3:
                                tb_Hall.Text = "三 011";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 4:
                                tb_Hall.Text = "四 100";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 5:
                                tb_Hall.Text = "五 101";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 6:
                                tb_Hall.Text = "六 110";
                                tb_Hall.ForeColor = Color.Green;
                                break;
                            case 7:
                                tb_Hall.Text = "錯 111";
                                tb_Hall.ForeColor = Color.Red;
                                break;
                            default:
                                tb_Hall.Text = "錯錯錯";
                                tb_Hall.ForeColor = Color.Red;
                                break;
                        }
                    }
                    else if (tabControl1.SelectedIndex == 1)
                    {
                        switch (input[1] & 0x07)
                        {
                            case 0:
                                tb_Hall2.Text = "錯 000";
                                tb_Hall2.ForeColor = Color.Red;
                                break;
                            case 1:
                                tb_Hall2.Text = "一 001";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 2:
                                tb_Hall2.Text = "二 010";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 3:
                                tb_Hall2.Text = "三 011";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 4:
                                tb_Hall2.Text = "四 100";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 5:
                                tb_Hall2.Text = "五 101";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 6:
                                tb_Hall2.Text = "六 110";
                                tb_Hall2.ForeColor = Color.Green;
                                break;
                            case 7:
                                tb_Hall2.Text = "錯 111";
                                tb_Hall2.ForeColor = Color.Red;
                                break;
                            default:
                                tb_Hall2.Text = "錯錯錯";
                                tb_Hall2.ForeColor = Color.Red;
                                break;
                        }
                    }
                }
                else if (input[0] == 0xCB)
                {
                    if (tabControl1.SelectedIndex == 0)
                    {
                        progressBar2.Value = 100;
                        tb_VR.Text = Convert.ToString(input[1], 16);
                        tb_VR_mV.Text = Convert.ToString((input[1] << 4) * 5000 / 4096);
                        Application.DoEvents();         //執行某一事件，以達到延遲效果。
                        for (int j = 0; j < 10; j++)
                            System.Threading.Thread.Sleep(1);
                        progressBar2.Value = 0;
                    }
                    else if (tabControl1.SelectedIndex == 1)
                    {
                        progressBar2.Value = 100;
                        tb_VR2.Text = Convert.ToString(input[1], 16);
                        tb_VR_mV2.Text = Convert.ToString((input[1] << 4) * 5000 / 4096);
                        Application.DoEvents();         //執行某一事件，以達到延遲效果。
                        for (int j = 0; j < 10; j++)
                            System.Threading.Thread.Sleep(1);
                        progressBar2.Value = 0;
                    }
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
            Process.Start(@"D:\_data1\Release-cs8967A\Release\eZISP-Plus V3.0.7.exe");
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
            //radioButton1.Enabled = false;
            radioButton2.Checked = true;
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

            label_speed2.Text = numericUpDown1.Value.ToString();

            if (numericUpDown1.Value == 0)
                label_target_speed2.Text = "0";
            else
                label_target_speed2.Text = (300 + 50 * (numericUpDown1.Value - 1)).ToString();

            if (numericUpDown1.Value == 0)
                label_target_speed2.ForeColor = System.Drawing.Color.Black;
            else
                label_target_speed2.ForeColor = System.Drawing.Color.Black;
           
            Send_Speed_Cmd(1);
        }

        private void button_Run_Click(object sender, EventArgs e)
        {
            button_Run.Enabled = false;
            button_Stop.Enabled = true;

            richTextBox1.AppendText("[PC]: 啟動, 速度 = " + numericUpDown1.Value.ToString() + " 檔 = " + (300 + 50 * (numericUpDown1.Value - 1)).ToString());
            if (button_Swing.Enabled == true)
                richTextBox1.AppendText(" RPM, 停止搖頭\n");
            else
                richTextBox1.AppendText(" RPM, 搖頭\n");

            label_speed2.Text = numericUpDown1.Value.ToString();

            if (numericUpDown1.Value == 0)
                label_target_speed2.Text = "0";
            else
                label_target_speed2.Text = (300 + 50 * (numericUpDown1.Value - 1)).ToString();

            if (numericUpDown1.Value == 0)
                label_target_speed2.ForeColor = System.Drawing.Color.Black;
            else
                label_target_speed2.ForeColor = System.Drawing.Color.Black;

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

        public bool Send_Update_System_Status_Cmd(int on_off)
        {
            byte[] data = new byte[3];
            data[0] = 0xD1;
            if(on_off  == 1)
                data[1] = 0xfa;
            else
                data[1] = 0xf5;
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

        public bool Send_Print_Test_Data_Cmd()
        {
            byte[] data = new byte[3];
            data[0] = 0xD1;
            data[1] = 0xfc;
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

        private void button3_Click(object sender, EventArgs e)
        {
            if (Updata_System_Status == 1)
            {
                Send_Update_System_Status_Cmd(0);
                button_update_status.Text = "更新狀態";
                button_update_status.ForeColor = Color.Green;
                Updata_System_Status = 0;
                label_target_speed2.Text = "---";
                label_speed2.Text = "-";
                label_target_speed.Text = "---";
                label_rpm.Text = "---";
                label_speed.Text = "-";
                tb_ADCA.Text = "---";
                tb_ADCA_mV.Text = "---";
                tb_ADCB.Text = "---";
                tb_ADCB_mV.Text = "---";
                tb_VR.Text = "---";
                tb_VR_mV.Text = "---";
                tb_VR2.Text = "---";
                tb_VR_mV2.Text = "---";
                tb_Hall2.Text = "---";
                tb_svpwm_m.Text = "---";
                tb_VAC.Text = "---";
            }
            else
            {
                Send_Update_System_Status_Cmd(1);
                button_update_status.Text = "不更新狀態";
                button_update_status.ForeColor = Color.Red;
                Updata_System_Status = 1;
            }
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            Send_Print_Test_Data_Cmd();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            OperatingSystem OSv = System.Environment.OSVersion;
            richTextBox1.AppendText("作業系統版本 : " + OSv.ToString() + "\n");
            richTextBox1.AppendText("圖形介面版本 : A02\n");
            richTextBox1.AppendText("韌體版本 : F0" + fw_version.ToString() + "\n");
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("螢幕解析度 : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");
            richTextBox1.AppendText("目前時間 : " + DateTime.Now.ToString() + "\n");

            richTextBox1.AppendText("目標轉速 : " + target_speed.ToString() + " rpm\n");
            richTextBox1.AppendText("實際轉速 : " + real_speed.ToString() + " rpm\n");
            richTextBox1.AppendText("馬達狀態 : ");
            switch (motor_status)
            {
                case 0:
                    richTextBox1.AppendText("START\n");
                    break;
                case 1:
                    richTextBox1.AppendText("STOP\n");
                    break;
                default:
                    richTextBox1.AppendText("UNKNOWN\n");
                    break;
            }
            richTextBox1.AppendText("電源狀態 : ");
            switch (power_status)
            {
                case 0:
                    richTextBox1.AppendText("電壓正常\n");
                    break;
                case 1:
                    richTextBox1.AppendText("電壓欠壓\n");
                    break;
                case 2:
                    richTextBox1.AppendText("電壓過壓\n");
                    break;
                default:
                    richTextBox1.AppendText("電壓不詳\n");
                    break;
            }

            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        public bool Send_SVPWM_Phase_Cmd(int svpwm_phase)
        {
            byte[] data = new byte[3];

            data[0] = 0xD2;

            data[1] = (byte)(svpwm_phase);
            data[2] = CalcCheckSum(data, 2);

            //richTextBox1.AppendText("[PC]: bbbb設定, SVPWM相位 = " + data[1].ToString() + "\n");
            //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

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

        private void bt_svpwm_phase_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: 設定, SVPWM相位 = " + numericUpDown2.Value.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_SVPWM_Phase_Cmd((Int32)numericUpDown2.Value);
        }

        public bool Send_Get_Status_Cmd(int get_status)
        {
            byte[] data = new byte[3];

            data[0] = 0xD3;

            data[1] = (byte)(get_status);
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

        public bool Send_SVPWM_M_Cmd(int uart_status)
        {
            byte[] data = new byte[3];

            data[0] = 0xD7;

            data[1] = (byte)(uart_status);
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

        public bool Send_UART_Test_Cmd(int uart_status)
        {
            byte[] data = new byte[3];

            data[0] = 0xD8;

            data[1] = (byte)(uart_status);
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

        public bool Send_SVPWM_Test_Cmd(int enable_svpwm)
        {
            byte[] data = new byte[3];
            byte phase;
            int value;

            phase = (byte)numericUpDown3.Value;

            data[0] = 0xD4;

            if (enable_svpwm == 2)
                data[1] = 0xff;
            else
            {
                value = (phase & 0x3f) | (byte)enable_svpwm << 6;
                data[1] = (byte)value;
            }

            data[2] = CalcCheckSum(data, 2);

            //MessageBox.Show("phase = " + phase.ToString() + ", data1 = " + data[1].ToString());

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

        private void button5_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(1); //Get hall status
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(1); //Get hall status
        }

        private void button12_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(1);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(0);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            int mode = 0;
            int VTH = 0;
            int mV = 0;
            string message = "";

            mode = (radioButton1.Checked == true) ? 0 : 1;

            MessageBox.Show("CMP數值 = " + tb_cmp_data.Text.ToString());
            MessageBox.Show("CMP電壓 = " + tb_cmp_mV.Text.ToString());

            if (mode == 0)
            {
                if (tb_cmp_data.Text.Length <= 0)
                {
                    MessageBox.Show("未輸入資料");
                    return;
                }
                else
                {
                    VTH = (int)hex2dec(tb_cmp_data.Text);

                    if (VTH > 255)
                        MessageBox.Show("輸入資料錯誤，最大值為0xff。");
                    else if (VTH < 0)
                        MessageBox.Show("輸入資料錯誤，最小值為0。");
                    else
                    {
                        MessageBox.Show("輸入資料正確。 VTH = " + VTH);
                    }
                }
            }
            else
            {
                if (tb_cmp_mV.Text.Length <= 0)
                {
                    MessageBox.Show("您還沒有設定CMP電壓值");
                    return;
                }
                else
                {
                    mV = int.Parse(tb_cmp_mV.Text);
                    if ((mV > 1800) || (mV < 0))
                        MessageBox.Show("不合法的CMP電壓值");
                    else
                    {
                        VTH = (int)((double)mV * 255 / 1800);
                        MessageBox.Show("輸入資料正確。 CMP電壓 = " + tb_cmp_mV.Text + " mV, VTH = " + VTH);
                        //MessageBox.Show("mV = " + mV + ", VTH = " + VTH);
                    }
                }
            }

            //Send_Initial_CMP_Cmd(comboBox_comparator.SelectedIndex, VTH);

            if (mode == 0)
            {
                message += ", mode = 0 , setup data = ";
                message += VTH.ToString();
                message += "\n";
            }
            else
            {
                message += ", mode = 1 , setup voltage = ";
                message += mV.ToString();
                message += " mV, VTH = ";
                message += VTH;
                message += "\n";
            }

            richTextBox1.AppendText(message);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

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

        private void tb_cmp_data_MouseClick(object sender, MouseEventArgs e)
        {
            radioButton1.Checked = true;
            radioButton2.Checked = false;
        }

        private void tb_cmp_mV_MouseClick(object sender, MouseEventArgs e)
        {
            radioButton1.Checked = false;
            radioButton2.Checked = true;
        }

        private void tb_cmp_data_KeyPress(object sender, KeyPressEventArgs e)
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

        private void tb_cmp_mV_KeyPress(object sender, KeyPressEventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(2);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(2); //Continuously get hall status
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Send_UART_Test_Cmd(1);  //UART test START
        }

        private void button16_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(0); //Stop getting hall status

        }

        private void button17_Click(object sender, EventArgs e)
        {
            Send_UART_Test_Cmd(0);  //UART test STOP
        }

        private void tb_m_value_KeyPress(object sender, KeyPressEventArgs e)
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

        private void button18_Click(object sender, EventArgs e)
        {
            int m_value = 0;
            string message = "";

            if (tb_m_value.Text.Length <= 0)
            {
                MessageBox.Show("未輸入資料");
                return;
            }
            else
            {
                m_value = int.Parse(tb_m_value.Text);

                if (m_value > 100)
                    MessageBox.Show("輸入資料錯誤，最大值為100。");
                else if (m_value < 1)
                    MessageBox.Show("輸入資料錯誤，最小值為1。");
                else
                {
                    MessageBox.Show("輸入資料正確。 m_value = " + m_value);

                    Send_SVPWM_M_Cmd(m_value);

                    message += "[PC] Setup m_value =  ";
                    message += m_value.ToString();
                    message += "\n";

                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行


              
                
                
                }
            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(3); //Stop getting VR status
        }

        private void button23_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(4); //Get VR status
        }

        private void button22_Click(object sender, EventArgs e)
        {
            Send_Get_Status_Cmd(5); //Continuously get VR status
        }

    
    }
}
