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
using System.Diagnostics;       //for Process

namespace imsLink
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;
        int IsRunning = 0;
        int IsCCW = 0;
        int IsVRRecording = 0;
        int IsDutyRecording = 0;
        int IsRpmRecording = 0;
        int IsPhaseComp = 0;
        int isCommandLog = 0;
        int Comport_Mode = 0;   //0: imsLink, 1: putty mode, 2: hex mode
        int Demo_Mode = 0;
        
        String imslink_setup_filename = "imslink.ini";
        String imslink_log_filename = "imslink.log";
        string ezisp_path = "";
        int SelectedLanguage = 0;
        static int ProtectionFunction_default = 0x5f;          //default setting
        int ProtectionFunction = ProtectionFunction_default;
        private const int UART_BUF_LENGTH = 5;
        private const int _ALL = 63;
        private const int _CONTROL = 0;
        private const int _DIRECTION = 1;
        private const int _REAL_SPEED = 2;
        private const int _TARGET_SPEED = 3;
        private const int _MAX_SPEED = 4;
        private const int _MIN_SPEED = 5;
        private const int _DUTY = 6;
        private const int _SVPWM_M = 7;
        private const int _PWM_FREQUENCY = 8;
        private const int _POLE_PAIR = 9;
        private const int _TOLERANCE = 10;
        private const int _ACCELERATION = 11;
        private const int _HALL = 12;
        private const int _PROTECTION = 13;
        private const int _ERROR = 14;
        private const int _RUN_STATUS = 15;
        private const int _PHASE_COMP = 16;
        private const int _START_DUTY = 17;
        private const int _PCA_DUTY = 18;
        private const int _GPIO = 19;

        private const int _TIMER0 = 20;
        private const int _TIMER1 = 21;
        private const int _TIMER2 = 22;
        private const int _TIMER3 = 23;
        private const int _TIMER4 = 24;
        private const int _TIMER5 = 25;
        private const int _ADC1 = 26;
        private const int _ADC2 = 27;
        private const int _ADC3 = 28;
        private const int _ADC4 = 29;
        private const int _CMPA = 30;
        private const int _CMPB = 31;
        private const int _CMPC = 32;
        private const int _CMPD = 33;
        private const int _CMPVTH0 = 34;
        private const int _CMPVTH1 = 35;
        private const int _VDC = 40;
        private const int _IS = 41;
        private const int _VR = 42;
        private const int _DEADTIME = 43;

        private const int _ALIVE = 63;

        private const int _NONE = 0; 
        private const int _STOP = 0;
        private const int _ONCE = 1;
        private const int _CONTINUOUS = 2;
        private const int _START = 1;
        private const int _TEST = 2;

        private const int NORMAL_MODE = 0;
        private const int VR_MODE = 1;
        private const int AUTO_MODE = 2;
        private const int TEST_MODE = 3;

        private const int _TEST_NONE = 0;
        private const int _TEST_PWM = 1;
        private const int _TEST_SVPWM = 2;
        private const int _TEST_SENSORLESS = 3;
        private const int _TEST_UART = 4;
        private const int _TEST_UVW = 5;

        private const int N = 15;

        private const int _PROTECTION_OCA = 0;
        private const int _PROTECTION_OCC = 1;
        private const int _PROTECTION_OCX = 2;
        private const int _PROTECTION_LOCK = 3;
        private const int _PROTECTION_HALL = 4;
        private const int _PROTECTION_VDC = 5;
        private const int _PROTECTION_WD = 6;

	    private const int HALL_SENSOR_MODE = 0;
	    private const int SENSORLESS_MODE = 1;
        private const int PCA_MODE = 2;

        int direction = 0;
        int real_speed = 0;
        int target_speed = 0;
        int max_speed = 0;
        int min_speed = 0;
        int duty = 0;
        int tolerance = 0;
        int acceleration = 0;
        int pwm_frequency_point = 0;
        int pwm_frequency = 0;
        int start_duty = 0;
        int pca_duty = 0;
        int timer0_th_tl = 0;
        int timer1_th_tl = 0;
        int timer2_th_tl = 0;
        int adc_vdc = 0;
        int adc_is = 0;
        int adc_vr = 0;
        int adc_vr_mv = 0;
        int hall_status = 0;

        int motor_status = 0;
        int power_status = 0;
        int fw_version = 0;
        int error_code = 0;
        int flag_error_1 = 0;
        int flag_error_2 = 0;
        int flag_error_3 = 0;
        int flag_error_4 = 0;
        int flag_error_5 = 0;
        int flag_error_6 = 0;
        int flag_error_7 = 0;
        int flag_error_8 = 0;
        int flag_error_9 = 0;
        int flag_error_10 = 0;
        int flag_error_11 = 0;

        int flag_get_duty = 0;
        int flag_get_target_speed = 0;
        int flag_get_max_speed = 0;
        int flag_get_min_speed = 0;
        int flag_get_acceleration = 0;
        int flag_get_tolerance = 0;
        int flag_get_pole_pair = 0;
        int flag_get_pwm_freq = 0;
        int flag_get_direction = 0;
        int flag_get_start_duty = 0;
        int flag_sensor_type = HALL_SENSOR_MODE;

        int control_1 = 0;	//CW/CCW
        int control_2 = 0;	//duty/rpm
        int control_3 = 0;	//sensor/sensorless
        //int control_4 = 0;	//PWM/SVPWM
        //int control_5 = 0;	//NNMOS/PNMOS
        //int control_6 = 2;	//CM2209A/CM2209B/CM2209C/CM2209D/CM2209_others
        int control_7 = 1;	//real hall/sensorless hall
        int target_vr = 0;
        int real_vr = 0;

        string[,] language1 = new string[3, 8] { 
        { "搖頭", "搖頭", "更新  狀態", "不更新  狀態", "打印  訊息", "系統  資訊", "計算機", "計時器"}, 
        { "摇头", "不摇头", "更新  状态", "不更新  状态", "打印  讯息", "系统  资讯", "计算机", "计时器"},
        { "Swing", "No Swing", "Update", "No Update", "Mess- age", "System Info", "Calc", "Timer"} 
        };

        string[,] language2 = new string[3, 10] { 
        { "參數錯誤", "過壓", "欠壓", "堵轉", "霍爾錯誤", "過流 A", "過流 C", "過流 X", "缺相", "電機短路" }, 
        { "参数错误", "过压", "欠压", "堵转", "霍尔错误", "过流 A", "过流 C", "过流 X", "缺相", "电机短路" }, 
        { "Para Error", "OV", "UV", "Lock", "Hall", "OC A", "OC C", "OC X", "Phase", "Short" } 
        };

        string[,] language3 = new string[3, 8] { 
        { "確定", "過流保護", "堵轉保護", "過壓欠壓保護", "相序保護", "過流", "缺相", "電機短路" }, 
        { "确定", "过流保护", "堵转保护", "过压欠压保护", "相序保护", "过流", "缺相", "电机短路" }, 
        { "Apply", "OC Protection", "Lock Protection", "Voltage Protection", "Hall Protection", "OC", "Phase", "Short" } 
        };

        string[,] language4 = new string[3, 5] { 
        { "電源狀態 : ", "電壓正常", "電壓欠壓", "電壓過壓", "電壓不詳"}, 
        { "电源状态 : ", "电压正常", "电压欠压", "电压过压", "电压不详"},
        { "Power Status : ", "Power Normal", "Power UV", "Power OV", "Power Unknown"} 
        };

        string[,] language5 = new string[3, 11] { 
        { "確定", "連續", "啟用", "停止",  "停用", "設定CMP", "設定ADC", "設定DAC", "設定VDC", "數值", "電壓"}, 
        { "确定", "连续", "启用", "停止",  "停用", "设定CMP", "设定ADC", "设定DAC", "设定VDC", "数值", "电压"},
        { "Apply", "Cont.", "Start", "Stop", "Disable", "Setup CMP", "Setup ADC", "Setup DAC", "Setup VDC","Value", "Voltage"} 
        };

        string[,] language6 = new string[3, 5] { 
        { "確定", "啟動", "停止",  "加速", "减速"}, 
        { "确定", "启动", "停止",  "加速", "减速"},
        { "Apply","Start", "Stop", "UP", "DOWN"} 
        };

        string[,] language7 = new string[3, 7] { 
        { "過流保護A", "過流保護C", "過流保護X", "堵轉保護", "相序保護", "過壓欠壓保護", "WatchDog"}, 
        { "过流保护A", "过流保护C", "过流保护X", "堵转保护", "相序保护", "过压欠压保护", "WatchDog"}, 
        { "OC ProtectionA", "OC ProtectionC", "OC ProtectionX", "Lock Protection", "Hall Protection", "Voltage Protection", "WatchDog" } 
        };

        string[,] language8 = new string[3, 1] { 
        {"六 U0V-W+\r\n四 U-V0W+\r\n五 U-V+W0\r\n一 U0V+W-\r\n三 U+V0W-\r\n二 U+V-W0"},
        {"六 U0V-W+\r\n四 U-V0W+\r\n五 U-V+W0\r\n一 U0V+W-\r\n三 U+V0W-\r\n二 U+V-W0"},
        {"Ⅵ U0V-W+\r\nⅣ U-V0W+\r\nⅤ U-V+W0\r\nⅠ U0V+W-\r\nⅢ U+V0W-\r\nⅡ U+V-W0"}
        };

        string[,] language9 = new string[3, 5] {
        {"請連線Comport", "連結Comport失敗", "加速度", "允許值", "相位補償"},
        {"请连线Comport", "连结Comport失败", "加速度", "允许值", "相位补偿"},
        {"Please Connect Comport", "Connect Comport Fail", "Speed", "Tolerance", "Phase Compensation"}
        };

        public void Update_Language(int idx)
        {
            button_Swing.Text = language1[idx, 0];
            button_NoSwing.Text = language1[idx, 1];
            button3.Text = language1[idx, 4];
            button4.Text = language1[idx, 5];
            button27.Text = language1[idx, 6];
            //button30.Text = language1[idx, 7];

            btn_error1.Text = language2[idx, 0];
            btn_error2.Text = language2[idx, 1];
            btn_error3.Text = language2[idx, 2];
            btn_error4.Text = language2[idx, 3];
            btn_error5.Text = language2[idx, 4];
            btn_error6.Text = language2[idx, 5];
            btn_error7.Text = language2[idx, 6];
            btn_error8.Text = language2[idx, 7];
            btn_error9.Text = language2[idx, 8];
            btn_error10.Text = language2[idx, 9];

            button24.Text = language3[idx, 0];
            cb_protection0.Text = language3[idx, 1];
            cb_protection1.Text = language3[idx, 2];
            cb_protection2.Text = language3[idx, 3];
            cb_protection3.Text = language3[idx, 4];

            status_power.Text = language4[idx, 1];

            button24.Text = language5[idx, 0];
            button22.Text = language5[idx, 1];
            button14.Text = language5[idx, 1];
            button19.Text = language5[idx, 2];
            button16.Text = language5[idx, 3];
            button21.Text = language5[idx, 3];
            button20.Text = language5[idx, 4];
            groupBox4.Text = language5[idx, 5];

            groupBox18.Text = language5[idx, 6];
            groupBox15.Text = language5[idx, 5];
            groupBox16.Text = language5[idx, 7];
            groupBox19.Text = language5[idx, 8];

            button80.Text = language5[idx, 2];
            button77.Text = language5[idx, 2];
            button75.Text = language5[idx, 2];
            button82.Text = language5[idx, 2];

            button81.Text = language5[idx, 4];
            button78.Text = language5[idx, 4];
            button76.Text = language5[idx, 4];
            button83.Text = language5[idx, 4];

            button49.Text = language6[idx, 0]; 
            button_st.Text = language6[idx, 1];
            button_sp.Text = language6[idx, 2];
            button_speed_up.Text = language6[idx, 3];
            button_speed_down.Text = language6[idx, 4];
            button_speed_up3.Text = language6[idx, 3];
            button_speed_down3.Text = language6[idx, 4];
            button_st2.Text = language6[idx, 1];
            button_sp2.Text = language6[idx, 2];
            button_speed_up2.Text = language6[idx, 3];
            button_speed_down2.Text = language6[idx, 4];

            cb_protection_00.Text = language7[idx, 0];
            cb_protection_01.Text = language7[idx, 1];
            cb_protection_02.Text = language7[idx, 2];
            cb_protection_03.Text = language7[idx, 3];
            cb_protection_04.Text = language7[idx, 4];
            cb_protection_05.Text = language7[idx, 5];
            cb_protection_06.Text = language7[idx, 6];

            label26.Text = language8[idx, 0];

            button31.Text = language5[idx, 0];
            button32.Text = language5[idx, 0];
            button79.Text = language5[idx, 0];
            button71.Text = language5[idx, 0];
            button68.Text = language5[idx, 0];

            button40.Text = language5[idx, 1];
            bt_drive_conti_1.Text = language5[idx, 1];
            bt_drive_conti_2.Text = language5[idx, 1];
            bt_drive_conti_3.Text = language5[idx, 1];
            bt_drive_conti_4.Text = language5[idx, 1];
            bt_drive_conti_5.Text = language5[idx, 1];
            bt_drive_conti_6.Text = language5[idx, 1];

            button_phase_comp_st.Text = language6[idx, 1];
            button_phase_comp_sp.Text = language6[idx, 2];

            button_sensorless_start.Text = language6[idx, 1];
            button_sensorless_stop.Text = language6[idx, 2];

            if (idx == 0)
            {
                label9.Text = "世紀民生科技股份有限公司";
                label10.Text = "電話:   (03) 5784866";
                label11.Text = "傳真:   (03) 5785002";
                label12.Text = "地址:   新竹市科學園區工業東四路24-2號2樓";
                label13.Text = "信箱:   sales@myson.com.tw";

                label36.Text = "電壓：               (0~5000mV)";
                label37.Text = "數值：               (0~4095)";
                label34.Text = "電壓：               (0~5000mV)";
                label35.Text = "數值：               (0~1023)";
                label38.Text = "過壓保護             VAC";
                label39.Text = "過壓恢復             VAC";
                label40.Text = "欠壓恢復             VAC";
                label41.Text = "欠壓保護             VAC";
            }
            else if (idx == 1)
            {
                label9.Text = "世纪民生科技股份有限公司";
                label10.Text = "电话:   (03) 5784866";
                label11.Text = "传真:   (03) 5785002";
                label12.Text = "地址:   新竹市科学园区工业东四路24-2号2楼";
                label13.Text = "信箱:   sales@myson.com.tw";

                label36.Text = "电压：               (0~5000mV)";
                label37.Text = "数值：               (0~4095)";
                label34.Text = "电压：               (0~5000mV)";
                label35.Text = "数值：               (0~1023)";
                label38.Text = "过压保护             VAC";
                label39.Text = "过压恢复             VAC";
                label40.Text = "欠压恢复             VAC";
                label41.Text = "欠压保护             VAC";
            }
            else
            {
                label9.Text = "MYSON CENTURY,INC.";
                label10.Text = "TEL:  (886)3-5784866";
                label11.Text = "FAX:  (886)3-5785002";
                label12.Text = "ADD:  2F., No.24-2, Gongye E. 4th Rd., East Dist., \n           Hsinchu City 300, Taiwan (R.O.C.)";
                label13.Text = "E-mail: sales@myson.com.tw";
                label36.Text = "Voltage:               (0~5000mV)";
                label37.Text = "Value:                 (0~4095)";
                label34.Text = "Voltage:               (0~5000mV)";
                label35.Text = "Value:                 (0~1023)";
                label38.Text = "OV high                VAC";
                label39.Text = "OV low                 VAC";
                label40.Text = "UV high                VAC";
                label41.Text = "UV low                 VAC";
            }
            if (!serialPort1.IsOpen)
            {
                tb_target.Text = language9[idx, 0];
                tb_target2.Text = language9[idx, 0];
                if (idx == 2)  //English
                {
                    tb_target.Font = new Font("Courier New", 12);
                    tb_target2.Font = new Font("Courier New", 12);
                }
                else
                {
                    tb_target.Font = new Font("Courier New", 18);
                    tb_target2.Font = new Font("Courier New", 18);
                }
            }
            label22.Text = language9[idx, 2];
            label23.Text = language9[idx, 3];
            button39.Text = language5[idx, 3];
            bt_drive_stop.Text = language5[idx, 3];
            groupBox14.Text = language9[idx, 4];

        }

        int log_file_tmp_length = 0;
        string log_file_tmp_data = "";
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

        void Read_Setup_File()
        {
            int i;
            if (System.IO.File.Exists(imslink_setup_filename) == false)
            {
                //MessageBox.Show("檔案 " + imslink_setup_filename + " 不存在，製作一個。");
                StreamWriter sw = File.CreateText(imslink_setup_filename);
                string content = "";
                content += SelectedLanguage.ToString();
                content += "\n";
                content += ezisp_path;
                content += "\n";

                sw.WriteLine(content);
                sw.Close();

                comboBox3.SelectedIndex = 0;
            }
            else
            {
                //MessageBox.Show("檔案 " + imslink_setup_filename + " 存在, 開啟，並讀入設定");

                String line;
                StreamReader sr = new StreamReader(imslink_setup_filename);
                for (i = 0; i < 2; i++)
                {
                    line = sr.ReadLine();
                    //MessageBox.Show(line);
                    if (i == 0)
                    {
                        SelectedLanguage = int.Parse(line);
                        comboBox3.SelectedIndex = SelectedLanguage;
                        Update_Language(SelectedLanguage);
                    }
                    if (i == 1)
                        ezisp_path = line;
                }
                sr.Close();
            }
        }

        public Form1()
        {
            InitializeComponent();
            Reset_imsLink_Setting();
            Read_Setup_File();
            panel1.BackColor = System.Drawing.Color.OrangeRed;
            panel5.BackColor = System.Drawing.Color.OrangeRed;


            /*
            tabControl1.TabPages.Remove(this.tabPage1_Phase);
            tabControl1.TabPages.Remove(this.tabPage1_protection);
            tabControl1.TabPages.Remove(this.tabPage1_PWM);
            tabControl1.TabPages.Remove(this.tabPage1_Record);
            tabControl1.TabPages.Remove(this.tabPage1_Sensorless);
            tabControl1.TabPages.Remove(this.tabPage1_Servo);
            tabControl1.TabPages.Remove(this.tabPage5_Tools);
            tabControl1.TabPages.Remove(this.tabPage7_About);
            tabControl1.TabPages.Remove(this.tabPage8_SVPWM);
            tabControl1.TabPages.Remove(this.tabPage1_main);
            */
            tabControl1.SelectedIndex = 10;              //接跳到第10頁。
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
                    MessageBox.Show(language9[SelectedLanguage, 1]);
            }

            if (serialPort1.IsOpen)
            {
                panel1.BackColor = System.Drawing.Color.Yellow;
                panel5.BackColor = System.Drawing.Color.Yellow;
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
                if (control_2 == 0)
                {
                    tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                    tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                }
                else
                {
                    tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                    tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                }
            }

        }

        private void Refresh_Protection_Setting()
        {
            if (((ProtectionFunction >> 0) & 0x01) == 0x01) //OCA
            {
                cb_protection_00.Checked = true;
                numericUpDown_adc_data.ForeColor = System.Drawing.Color.Black;
                tb_adc_mV.ForeColor = System.Drawing.Color.Black;
            }
            else
            {
                cb_protection_00.Checked = false;
                numericUpDown_adc_data.ForeColor = System.Drawing.Color.Red;
                tb_adc_mV.ForeColor = System.Drawing.Color.Red;
            }
            if (((ProtectionFunction >> 1) & 0x01) == 0x01) //OCC
            {
                cb_protection_01.Checked = true;
                numericUpDown_cmp2_data1.ForeColor = System.Drawing.Color.Black;
                numericUpDown_cmp2_data2.ForeColor = System.Drawing.Color.Black;
                tb_cmp_mV.ForeColor = System.Drawing.Color.Black;
            }
            else
            {
                cb_protection_01.Checked = false;
                numericUpDown_cmp2_data1.ForeColor = System.Drawing.Color.Red;
                numericUpDown_cmp2_data2.ForeColor = System.Drawing.Color.Red;
                tb_cmp_mV.ForeColor = System.Drawing.Color.Red;
            }
            if (((ProtectionFunction >> 2) & 0x01) == 0x01) //OCX
            {
                cb_protection_02.Checked = true;
            }
            else
            {
                cb_protection_02.Checked = false;
            }
            if (((ProtectionFunction >> 3) & 0x01) == 0x01) //Lock-Rotor
            {
                cb_protection_03.Checked = true;
            }
            else
            {
                cb_protection_03.Checked = false;
            }
            if (((ProtectionFunction >> 4) & 0x01) == 0x01) //Hall
            {
                cb_protection_04.Checked = true;
            }
            else
            {
                cb_protection_04.Checked = false;
            }
            if (((ProtectionFunction >> 5) & 0x01) == 0x01)     //VDC
            {
                cb_protection_05.Checked = true;
                tb_v1.ForeColor = System.Drawing.Color.Black;
                tb_v2.ForeColor = System.Drawing.Color.Black;
                tb_v3.ForeColor = System.Drawing.Color.Black;
                tb_v4.ForeColor = System.Drawing.Color.Black;
            }
            else
            {
                cb_protection_05.Checked = false;
                tb_v1.ForeColor = System.Drawing.Color.Red;
                tb_v2.ForeColor = System.Drawing.Color.Red;
                tb_v3.ForeColor = System.Drawing.Color.Red;
                tb_v4.ForeColor = System.Drawing.Color.Red;
            }
            if (((ProtectionFunction >> 6) & 0x01) == 0x01)     //WatchDog
            {
                cb_protection_06.Checked = true;
            }
            else
            {
                cb_protection_06.Checked = false;
            }

            //cb_protection_05.Enabled = false;
        }

        private void Reset_imsLink_Setting()
        {
            //trackBar2.Visible = false;
            //textBox_timer2.Visible = false;
            //numericUpDown5.Visible = false;
            //trackBar_3.Visible = false;
            //trackBar_2.Visible = false;
            //trackBar_1.Visible = false;
            //trackBar_0.Visible = false;

            tabControl1.SelectedIndex = 0;      //程式啟動時，直接跳到main那頁。
            //button_Run.Enabled = true;
            //button_Stop.Enabled = false;
            //button_st.Enabled = true;
            //button_sp.Enabled = false;
            //button_st2.Enabled = true;
            //button_sp2.Enabled = false;
            //button_phase_comp_st.Enabled = true;
            //button_phase_comp_sp.Enabled = false;
            //button_Swing.Enabled = true;
            //button_NoSwing.Enabled = false;
            btn_error1.Enabled = false;
            btn_error2.Enabled = false;
            btn_error3.Enabled = false;
            btn_error4.Enabled = false;
            btn_error5.Enabled = false;
            btn_error6.Enabled = false;
            btn_error7.Enabled = false;
            btn_error8.Enabled = false;
            btn_error9.Enabled = false;
            btn_error10.Enabled = false;
            IsRunning = 0;
            IsCCW = 0;
            label_speed.Text = 0.ToString();
            label_speed2.Text = 0.ToString();
            label_rpm.Text = 0.ToString();
            label_rpm.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = 0.ToString();
            label_target_speed.ForeColor = System.Drawing.Color.Red;
            label_target_speed.Text = "---";
            label_target_speed2.Text = 0.ToString();
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            numericUpDown4.Value = 15;
            trackBar1.Value = 1;
            numericUpDown1.Value = 1;
            numericUpDown2.Value = 0;
            numericUpDown2.ForeColor = System.Drawing.Color.Black;
            numericUpDown3.Value = 0;
            numericUpDown6.Value = 25;
            numericUpDown7.Value = 1;
            //button_update_status.Text = "不更新狀態";
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
            tb_Hall3.Text = "---";
            tb_svpwm_m.Text = "---";
            tb_VAC.Text = "---";
            tb_Hall.Text = "---";
            tb_Hall.ForeColor = Color.Gray;
            status_motor.Text = "";
            status_power.Text = "";
            progressBar1.Value = 0;
            progressBar2.Value = 0;
            //richTextBox1.Clear();
            cb_protection0.Checked = true;
            cb_protection1.Checked = true;
            cb_protection2.Checked = true;
            cb_protection3.Checked = true;
            tb_m_value.Text = "20";
            tb_duty_value.Text = "20";
            numericUpDown_cmp_data1.Value = 240;
            numericUpDown_cmp_data2.Value = 200;
            lb_uart_debug.Text = "";
            label_speed2.ForeColor = System.Drawing.Color.Black;
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            numericUpDown1.ForeColor = System.Drawing.Color.Black;
            numericUpDown4.ForeColor = System.Drawing.Color.Black;
            numericUpDown_cmp_data1.ForeColor = System.Drawing.Color.Black;
            numericUpDown_cmp_data2.ForeColor = System.Drawing.Color.Black;
            numericUpDown3.ForeColor = System.Drawing.Color.Black;
            comboBox4.SelectedIndex = 1;
            button36.Enabled = true;
            button37.Enabled = false;
            button33.BackgroundImage = imsLink.Properties.Resources.open_log;

            tb_main_duty.Text = "20";
            tb_main_target_speed.Text = "1000";
            tb_main_max_speed.Text = "3000";
            max_speed = int.Parse(tb_main_max_speed.Text);
            tb_main_min_speed.Text = "500";
            tb_main_tolerance.Text = "50";
            tb_main_acceleration.Text = "100";
            tb_main_pole_pair.Text = "4";
            tb_main_frequency.Text = "20";
            tb_main_start_duty.Text = "20";
            trackBar5.Value = 60;
            tb_direction.Text = "CW";
            tb_direction2.Text = "CW";
            tb_direction3.Text = "CW";
            pictureBox3.Image = imsLink.Properties.Resources.CW;
            pictureBox4.Image = imsLink.Properties.Resources.CW;
            pictureBox5.Image = imsLink.Properties.Resources.CW;

            if (control_2 == 0) //open-loop
            {
                trackBar3.Maximum = 100;
                trackBar3.Minimum = 0;
                trackBar3.Value = 20;
                trackBar3.TickFrequency = 5;
                tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                tb_main_duty.Enabled = true;
                tb_main_target_speed.Enabled = false;
                tb_main_max_speed.Enabled = true;
                tb_main_min_speed.Enabled = false;
                tb_main_tolerance.Enabled = false;
                tb_main_acceleration.Enabled = false;
            }
            else                  //close loop
            {
                trackBar3.Maximum = 3000;
                trackBar3.Minimum = 0;
                trackBar3.Value = 500;
                trackBar3.TickFrequency = 300;
                tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                tb_main_duty.Enabled = false;
                tb_main_target_speed.Enabled = true;
                tb_main_max_speed.Enabled = true;
                tb_main_min_speed.Enabled = true;
                tb_main_tolerance.Enabled = true;
                tb_main_acceleration.Enabled = true;
            }

            if (!serialPort1.IsOpen)
            {
                tb_target.Text = language9[SelectedLanguage, 0];
                tb_target2.Text = language9[SelectedLanguage, 0];

                if (SelectedLanguage == 2)  //English
                {
                    tb_target.Font = new Font("Courier New", 12);
                    tb_target2.Font = new Font("Courier New", 12);
                }
                else
                {
                    tb_target.Font = new Font("Courier New", 18);
                    tb_target2.Font = new Font("Courier New", 18);
                }

                panel1.BackColor = System.Drawing.Color.OrangeRed;
                panel5.BackColor = System.Drawing.Color.OrangeRed;
            }
            else
            {
                panel1.BackColor = System.Drawing.Color.Yellow;
                panel5.BackColor = System.Drawing.Color.Yellow;
            }

            Graphics g = panel4.CreateGraphics();
            //g.Clear(BackColor);
            g.Clear(Color.White);
            DrawXY();
            //DrawXLine();
            //DrawYLine();
            g.Dispose();

            string timer2_value = "";
            int timer2_start_point = 0;

            timer2_value += Convert.ToString(trackBar_3.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_2.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_1.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_0.Value, 16).ToUpper();
            textBox_timer2.Text = timer2_value;
            timer2_start_point = trackBar_3.Value * 4096 + trackBar_2.Value * 256 + trackBar_1.Value * 16 + trackBar_0.Value;
            trackBar2.Value = timer2_start_point;

            this.Width = 960;
            show_comport_log = 0;

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
            comboBox_adc.SelectedIndex = 0;
            comboBox_cmp.SelectedIndex = 1;
            comboBox_dac.SelectedIndex = 0;
            comboBox_adc.Enabled = false;
            comboBox_cmp.Enabled = false;
            comboBox_dac.Enabled = false;

            tb_main_control_1.Text = "----";
            tb_main_control_2.Text = "----";
            tb_main_control_3.Text = "----";
            tb_main_control_4.Text = "----";
            tb_main_control_5.Text = "----";
            tb_main_control_6.Text = "----";
            tb_ac_control2.Text = "----";
            tb_ac_control3.Text = "----";
            gb_main_1.Enabled = false;
            gb_main_2.Enabled = false;
            gb_main_3.Enabled = false;
            gb_main_4.Enabled = false;
            gb_main_5.Enabled = false;
            gb_main_6.Enabled = false;
            gb_ac2.Enabled = false;
            gb_ac3.Enabled = false;
            tb_main_duty5.Text = "---";
            tb_main_pca_duty5.Text = "---";
            tb_target_pca_duty.Text = "---";
            tb_real_pca_duty.Text = "---";
            tb_hall_diff.Text = "---";
            tb_hall_diff_ms.Text = "---";
            tb_hall_diff_timer1.Text = "---";

            trackBar_3.Value = 8;
            trackBar_2.Value = 9;
            trackBar_1.Value = 6;
            trackBar_0.Value = 3;

            textBox_timer2.Text = "8000";
            textBox_timer2.ForeColor = System.Drawing.Color.Black;
            tb_rpm.ForeColor = System.Drawing.Color.Black;
            tb_msec.ForeColor = System.Drawing.Color.Black;
            tb_msec2.ForeColor = System.Drawing.Color.Black;

            numericUpDown5.Value = 3;
            numericUpDown5.ForeColor = System.Drawing.Color.Black;

            numericUpDown6.Value = 25;
            numericUpDown6.ForeColor = System.Drawing.Color.Black;

            numericUpDown7.Value = 1;
            numericUpDown7.ForeColor = System.Drawing.Color.Black;

            tb_target_pca_duty.Text = "---";
            tb_real_pca_duty.Text = "---";

            tb_target_pca_duty.ForeColor = System.Drawing.Color.Black;
            tb_real_pca_duty.ForeColor = System.Drawing.Color.Black;

            ProtectionFunction = ProtectionFunction_default;
            Refresh_Protection_Setting();
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
                    MessageBox.Show(language9[SelectedLanguage, 1]);
            }
            
            if (serialPort1.IsOpen)
            {
                panel1.BackColor = System.Drawing.Color.Yellow;
                panel5.BackColor = System.Drawing.Color.Yellow;
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
                if (control_2 == 0)
                {
                    tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                    tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                }
                else
                {
                    tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                    tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                }
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
                tb_target.Text = "請連線Comport";
                tb_target2.Text = "請連線Comport";
                panel1.BackColor = System.Drawing.Color.OrangeRed;
                panel5.BackColor = System.Drawing.Color.OrangeRed;
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
            Send_Control_Cmd(0xff, 0, 0);
            richTextBox1.AppendText("[PC]: Reset imsLink\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Reset_imsLink_Setting();
            refresh_meter();
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
            lb_uart_debug.Text = "";
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
                    if (Comport_Mode == 0)  //imsLink mode
                    {
                        if (BytesToRead == UART_BUF_LENGTH)
                            SpyMonitorRX();
                        else
                        {
                            /*
                            //for UART debug
                            lb_uart_debug.Text += BytesToRead.ToString();
                            lb_uart_debug.Text += ' ';
                            */

                            //資料不是5拜，打印出來。
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
                            richTextBox1.AppendText("[UN]: ");
                            for (int i = 0; i < BytesToRead; i++)
                            { 
                                richTextBox1.AppendText(((int)input[i]).ToString("X2") + " ");
                            }
                            richTextBox1.AppendText("\n");
                            */
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

        private void DrawXY()//画X轴Y轴
        {
            Graphics g = this.panel4.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.panel4.Width * 90 / 100, this.panel4.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.panel4.Width * 10 / 100, this.panel4.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawXLine()    //画X轴平行线
        {
            Graphics g = this.panel4.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point px1 = new System.Drawing.Point(0, this.panel4.Height - i * 50);
                System.Drawing.Point px2 = new System.Drawing.Point(this.panel4.Width, this.panel4.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            g.Dispose();
        }
        private void DrawYLine()    //画X轴刻度
        {
            Graphics g = this.panel4.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.panel4.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.panel4.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }

        int y1_value = 0;
        int y2_value = 0;
        int y3_value = 0;
        int[] y1_data = new int[15];
        int[] y2_data = new int[15];
        int[] y3_data = new int[15];
        int x_st = 0;
        int x_step = 0;
        int h_st = 0;
        int ratio_vr = 0;
        int ratio_duty = 0;
        int ratio_rpm = 0;
        int control_data2 = 0;
        int control_data3 = 0;
        int board_number = 0;
        int loop = 0;
        int loop_old = -1;

        private void SpyMonitorRX()
        {
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
                    //MessageBox.Show("PC got ack");

                    if (flag_get_duty == 1)
                    {
                        if (tb_main_duty.Text != "----")
                        {
                            flag_get_duty = 0;
                            tb_main_duty.BackColor = System.Drawing.SystemColors.Window;
                            trackBar3.Value = duty;
                        }
                    }
                    else if (flag_get_target_speed == 1)
                    {
                        if (tb_main_target_speed.Text != "----")
                        {
                            flag_get_target_speed = 0;
                            tb_main_target_speed.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_max_speed == 1)
                    {
                        if (tb_main_max_speed.Text != "----")
                        {
                            flag_get_max_speed = 0;
                            tb_main_max_speed.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_min_speed == 1)
                    {
                        if (tb_main_min_speed.Text != "----")
                        {
                            flag_get_min_speed = 0;
                            tb_main_min_speed.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_acceleration == 1)
                    {
                        if (tb_main_acceleration.Text != "----")
                        {
                            flag_get_acceleration = 0;
                            tb_main_acceleration.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_tolerance == 1)
                    {
                        if (tb_main_tolerance.Text != "----")
                        {
                            flag_get_tolerance = 0;
                            tb_main_tolerance.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_pole_pair == 1)
                    {
                        if (tb_main_pole_pair.Text != "----")
                        {
                            flag_get_pole_pair = 0;
                            tb_main_pole_pair.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_pwm_freq == 1)
                    {
                        if (tb_main_frequency.Text != "----")
                        {
                            flag_get_pwm_freq = 0;
                            tb_main_frequency.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (flag_get_direction == 1)
                    {
                        if (tb_direction.Text != "----")
                        {
                            flag_get_direction = 0;
                            tb_direction.BackColor = Color.Green;
                            tb_direction2.BackColor = Color.Green;
                            tb_direction3.BackColor = Color.Green;
                        }
                    }
                    else if (flag_get_start_duty == 1)
                    {
                        //if (tb_main_start_duty.Text != "----")
                        {
                            flag_get_start_duty = 0;
                            tb_main_start_duty.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    progressBar1.Value = 0;
                }
                else if (input[0] == 0xEE)
                {
                    progressBar2.Value = 100;

                    error_code = (int)input[2] * 256 + (int)input[3];
                    //richTextBox1.AppendText("[PC]: error_code = " + error_code.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                    flag_error_1 = error_code & 0x01;           //parameter   btn_error1
                    flag_error_2 = (error_code & 0x02) >> 1;    //ov          btn_error2
                    flag_error_3 = (error_code & 0x04) >> 2;    //uv          btn_error3
                    flag_error_4 = (error_code & 0x08) >> 3;    //lock        btn_error4
                    flag_error_5 = (error_code & 0x10) >> 4;    //hall        btn_error5
                    flag_error_6 = (error_code & 0x20) >> 5;    //oca         btn_error6
                    flag_error_7 = (error_code & 0x40) >> 6;    //occ         btn_error7
                    flag_error_8 = (error_code & 0x80) >> 7;    //ocx         btn_error8
                    flag_error_9 = (error_code & 0x100) >> 8;   //uvw         btn_error9
                    flag_error_10 = (error_code & 0x200) >> 9;  //short       btn_error10
                    flag_error_11 = (error_code & 0x400) >> 10; //recover from ov uv, disable btn_error2 btn_error3

                    if(flag_error_1 == 1)
                        btn_error1.Enabled = true;
                    else
                        btn_error1.Enabled = false;
                    if (flag_error_2 == 1)
                        btn_error2.Enabled = true;
                    else
                        btn_error2.Enabled = false;
                    if (flag_error_3 == 1)
                        btn_error3.Enabled = true;
                    else
                        btn_error3.Enabled = false;
                    if (flag_error_4 == 1)
                        btn_error4.Enabled = true;
                    else
                        btn_error4.Enabled = false;
                    if (flag_error_5 == 1)
                        btn_error5.Enabled = true;
                    else
                        btn_error5.Enabled = false;
                    if (flag_error_6 == 1)
                        btn_error6.Enabled = true;
                    else
                        btn_error6.Enabled = false;
                    if (flag_error_7 == 1)
                        btn_error7.Enabled = true;
                    else
                        btn_error7.Enabled = false;
                    if (flag_error_8 == 1)
                        btn_error8.Enabled = true;
                    else
                        btn_error8.Enabled = false;
                    if (flag_error_9 == 1)
                        btn_error9.Enabled = true;
                    else
                        btn_error9.Enabled = false;
                    if (flag_error_10 == 1)
                        btn_error10.Enabled = true;
                    else
                        btn_error10.Enabled = false;
                    if (flag_error_11 == 1)
                    {
                        btn_error2.Enabled = false;
                        btn_error3.Enabled = false;
                    }
                    delay(10);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC1)          //0xC1: 收到下位發送的馬達參數命令
                {
                    progressBar2.Value = 100;

                    if (input[1] == _ALIVE)
                    {
                        panel1.BackColor = System.Drawing.SystemColors.ControlLightLight;
                        panel5.BackColor = System.Drawing.SystemColors.ControlLightLight;
                        if (input[2] == VR_MODE)
                        {
                            if (input[3] == _START)
                            {
                                //button_Run.Enabled = true;
                                //button_Stop.Enabled = false;
                                //button_st.Enabled = false;
                                //button_sp.Enabled = true;
                                //button_st2.Enabled = false;
                                //button_sp2.Enabled = true;
                                IsRunning = 1;
                                if (control_2 == 0)
                                {
                                    tb_target.Text = "Target: " + aGauge_duty.Value.ToString() + " %";
                                    tb_target2.Text = "Target: " + aGauge_duty2.Value.ToString() + " %";
                                }
                                else
                                {
                                    tb_target.Text = "Target: " + aGauge_rpm.Value.ToString() + " rpm";
                                    tb_target2.Text = "Target: " + aGauge_rpm.Value.ToString() + " rpm";
                                }
                            }
                            else if (input[3] == _STOP)
                            {
                                //button_Run.Enabled = false;
                                //button_Stop.Enabled = true;
                                //button_st.Enabled = true;
                                //button_sp.Enabled = false;
                                //button_st2.Enabled = true;
                                //button_sp2.Enabled = false;
                                IsRunning = 0;
                                aGauge_duty.Value = 0;
                                aGauge_duty2.Value = 0;
                                if (control_2 == 0)
                                {
                                    tb_target.Text = "Target: 0 %";
                                    tb_target2.Text = "Target: 0 %";
                                }
                                else
                                {
                                    tb_target.Text = "Target: 0 rpm";
                                    tb_target2.Text = "Target: 0 rpm";
                                }
                            }
                        }
                    }
                    else if (input[1] == _CONTROL)
                    {
                        control_data2 = input[2];
                        control_data3 = input[3];
                        board_number = control_data3;

                        if (((control_data2 >> 7) & 0x01) == 0)
                        {
                            tb_main_control_1.Text = "CW";
                            control_1 = 0;
                            IsCCW = 0;
                            pictureBox3.Image = imsLink.Properties.Resources.CW;
                            pictureBox4.Image = imsLink.Properties.Resources.CW;
                            pictureBox5.Image = imsLink.Properties.Resources.CW;
                            tb_direction.Text = "CW";
                            tb_direction2.Text = "CW";
                            tb_direction3.Text = "CW";
                        }
                        else
                        {
                            tb_main_control_1.Text = "CCW";
                            control_1 = 1;
                            IsCCW = 1;
                            pictureBox3.Image = imsLink.Properties.Resources.CCW;
                            pictureBox4.Image = imsLink.Properties.Resources.CCW;
                            pictureBox5.Image = imsLink.Properties.Resources.CCW;
                            tb_direction.Text = "CCW";
                            tb_direction2.Text = "CCW";
                            tb_direction3.Text = "CCW";
                        }
                        if (((control_data2 >> 6) & 0x01) == 0)
                        {
                            tb_main_control_2.Text = "duty";
                            control_2 = 0;
                            loop = (control_data2 >> 6) & 0x01;
                            if (loop != loop_old)
                            {
                                loop_old = loop;
                                trackBar3.Maximum = 100;
                                trackBar3.Minimum = 0;
                                trackBar3.Value = 20;
                                trackBar3.TickFrequency = 5;
                                tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                                tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                                tb_main_duty.Enabled = true;
                                tb_main_target_speed.Enabled = false;
                                tb_main_max_speed.Enabled = true;
                                tb_main_min_speed.Enabled = false;
                                tb_main_tolerance.Enabled = false;
                                tb_main_acceleration.Enabled = false;
                            }
                        }
                        else
                        {
                            tb_main_control_2.Text = "rpm";
                            control_2 = 1;
                            loop = (control_data2 >> 6) & 0x01;
                            if (loop != loop_old)
                            {
                                loop_old = loop;
                                trackBar3.Maximum = 3000;
                                trackBar3.Minimum = 0;
                                trackBar3.Value = 500;
                                trackBar3.TickFrequency = 300;
                                tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                                tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                                tb_main_duty.Enabled = false;
                                tb_main_target_speed.Enabled = true;
                                tb_main_max_speed.Enabled = true;
                                tb_main_min_speed.Enabled = true;
                                tb_main_tolerance.Enabled = true;
                                tb_main_acceleration.Enabled = true;
                            }
                        }
                        if (((control_data2 >> 4) & 0x03) == 0)
                        {
                            control_3 = 0;
                            tb_main_control_3.Text = "Sensor";
                            tb_ac_control2.Text = "Sensor";
                            flag_sensor_type = HALL_SENSOR_MODE;
                            tb_main_pca_duty5.Text = "---";
                        }
                        else if (((control_data2 >> 4) & 0x03) == 0x01)
                        {
                            control_3 = 1;
                            tb_main_control_3.Text = "Sensorless";
                            tb_ac_control2.Text = "Sensorless";
                            flag_sensor_type = SENSORLESS_MODE;
                            tb_main_pca_duty5.Text = "---";
                        }
                        else if (((control_data2 >> 4) & 0x03) == 0x02)
                        {
                            control_3 = 2;
                            tb_main_control_3.Text = "PCA";
                            tb_ac_control2.Text = "PCA";
                            flag_sensor_type = PCA_MODE;
                        }
                        else if (((control_data2 >> 4) & 0x03) == 0x03)
                        {
                            //reserved
                        }
                        if (((control_data2 >> 2) & 0x03) == 0)
                        {
                            tb_main_control_4.Text = "PWM";
                        }
                        else if (((control_data2 >> 2) & 0x03) == 1)
                        {
                            tb_main_control_4.Text = "KPWM";
                        }
                        else if (((control_data2 >> 2) & 0x03) == 2)
                        {
                            tb_main_control_4.Text = "SVPWM";
                        }
                        else
                        {
                            tb_main_control_4.Text = "XXX";
                        }
                        if (((control_data2 >> 1) & 0x01) == 0)
                        {
                            tb_main_control_5.Text = "NNMOS";
                        }
                        else
                        {
                            tb_main_control_5.Text = "PNMOS";
                        }
                        if (((control_data2 >> 0) & 0x01) == 1)
                        {
                            control_7 = 1;
                            tb_ac_control3.Text = "真Hall";
                        }
                        else
                        {
                            control_7 = 0;
                            tb_ac_control3.Text = "無Hall";
                        }
                        switch (board_number)
                        {
                            case 1: tb_main_control_6.Text = "CM2209A"; break;
                            case 2: tb_main_control_6.Text = "CM2209B"; break;
                            case 3: tb_main_control_6.Text = "CM2209C"; break;
                            case 4: tb_main_control_6.Text = "CM2209D"; break;
                            default: tb_main_control_6.Text = "Unknown"; break;
                        }
                        gb_main_1.Enabled = true;
                        gb_main_2.Enabled = true;
                        gb_main_3.Enabled = true;
                        gb_main_4.Enabled = true;
                        gb_main_5.Enabled = true;
                        gb_main_6.Enabled = true;
                        gb_ac2.Enabled = true;
                        gb_ac3.Enabled = true;
                    }
                    else if (input[1] == _DIRECTION)
                    {
                        direction = (int)input[3];
                        if (IsRunning == 0)
                        {
                            if (direction == 0)
                            {
                                IsCCW = 0;
                                pictureBox3.Image = imsLink.Properties.Resources.CW;
                                pictureBox4.Image = imsLink.Properties.Resources.CW;
                                pictureBox5.Image = imsLink.Properties.Resources.CW;
                                tb_direction.Text = "CW";
                                tb_direction2.Text = "CW";
                                tb_direction3.Text = "CW";
                            }
                            else
                            {
                                IsCCW = 1;
                                pictureBox3.Image = imsLink.Properties.Resources.CCW;
                                pictureBox4.Image = imsLink.Properties.Resources.CCW;
                                pictureBox5.Image = imsLink.Properties.Resources.CCW;
                                tb_direction.Text = "CCW";
                                tb_direction2.Text = "CCW";
                                tb_direction3.Text = "CCW";
                            }
                        }
                    }
                    else if (input[1] == _REAL_SPEED)
                    {
                        //real_speed = (int)input[2] << 8 + (int)input[3];
                        real_speed = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: real_speed = " + real_speed.ToString() + "\n");richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        aGauge_rpm.Value = real_speed;
                        tb_main_rpm.Text = real_speed.ToString();
                        aGauge_rpm2.Value = real_speed;
                        tb_main_rpm2.Text = real_speed.ToString();
                        tb_main_rpm3.Text = real_speed.ToString();
                        tb_main_rpm5.Text = real_speed.ToString();
                        label_rpm.Text = real_speed.ToString();
                        if (real_speed == 0)
                            label_rpm.ForeColor = System.Drawing.Color.Red;
                        else
                            label_rpm.ForeColor = System.Drawing.Color.Green;
                    }
                    else if (input[1] == _TARGET_SPEED)
                    {
                        target_speed = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: target_speed = " + target_speed.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        label_target_speed.Text = target_speed.ToString();
                        if (target_speed == 0)
                            label_target_speed.ForeColor = System.Drawing.Color.Red;
                        else
                            label_target_speed.ForeColor = System.Drawing.Color.Green;
                        tb_main_target_speed.Text = target_speed.ToString();
                    }
                    else if (input[1] == _MAX_SPEED)
                    {
                        max_speed = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: max_speed = " + max_speed.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_main_max_speed.Text = max_speed.ToString();
                    }
                    else if (input[1] == _MIN_SPEED)
                    {
                        min_speed = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: min_speed = " + min_speed.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_main_min_speed.Text = min_speed.ToString();
                    }
                    else if (input[1] == _DUTY)
                    {
                        duty = (int)input[3];
                        tb_duty_value.Text = Convert.ToString(duty, 10);
                        tb_svpwm_m.Text = Convert.ToString(duty, 10);
                        //richTextBox1.AppendText("[PC]: duty = " + duty.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        aGauge_duty.Value = duty;
                        tb_main_duty2.Text = duty.ToString();
                        tb_main_duty4.Text = duty.ToString();
                        tb_main_duty5.Text = duty.ToString();
                        aGauge_duty2.Value = duty;
                        tb_main_duty3.Text = duty.ToString();
                        if (flag_get_duty == 1)
                        {
                            flag_get_duty = 0;
                            tb_main_duty.Text = duty.ToString();
                            tb_main_duty.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (input[1] == _TOLERANCE)
                    {
                        tolerance = (int)input[3];
                        //richTextBox1.AppendText("[PC]: tolerance = " + tolerance.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_main_tolerance.Text = tolerance.ToString();
                    }
                    else if (input[1] == _ACCELERATION)
                    {
                        acceleration = (int)input[3];
                        //richTextBox1.AppendText("[PC]: acceleration = " + acceleration.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_main_acceleration.Text = acceleration.ToString();
                    }
                    else if (input[1] == _PWM_FREQUENCY)
                    {
                        pwm_frequency_point = (int)input[2] * 256 + (int)input[3];
                        pwm_frequency = 16000000 / pwm_frequency_point / 2 / 1000;
                        tb_main_frequency.Text = pwm_frequency.ToString();
                    }
                    else if (input[1] == _START_DUTY)
                    {
                        start_duty = (int)input[3];
                        //tb_main_start_duty.Text = Convert.ToString(start_duty, 10);
                        if (flag_get_start_duty == 1)
                        {
                            flag_get_start_duty = 0;
                            tb_main_start_duty.Text = start_duty.ToString();
                            tb_main_start_duty.BackColor = System.Drawing.SystemColors.Window;
                        }
                    }
                    else if (input[1] == _PCA_DUTY)
                    {
                        pca_duty = (int)input[3];
                        duty = pca_duty * 100 / 255;
                        if (pca_duty > 0)
                        {
                            tb_main_pca_duty5.Text = pca_duty.ToString();
                            tb_main_duty5.Text = duty.ToString() + " %";
                            tb_real_pca_duty.Text = pca_duty.ToString() + " (" + duty.ToString() + " %)";
                        }
                        else
                        {
                            tb_main_pca_duty5.Text = "---";
                            tb_main_duty5.Text = "---";
                            tb_real_pca_duty.Text = "---";
                        }

                        aGauge_duty.Value = duty;
                        tb_main_duty2.Text = duty.ToString();
                        tb_main_duty4.Text = duty.ToString();
                        aGauge_duty2.Value = duty;
                        tb_main_duty3.Text = duty.ToString();
                    }
                    else if (input[1] == _TIMER0)
                    {
                        timer0_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer0 TH TL = " + Convert.ToString(timer0_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        if(control_7 == 1)  //use real hall
                        {
                            if (timer0_th_tl > 0)
                            {
                                tb_hall_diff.Text = "0x " + Convert.ToString(timer0_th_tl, 16).ToUpper();
                                //tb_hall_diff_ms.Text = (timer0_th_tl * 12 * 100000 / 16000000).ToString() + " msec";
                                tb_hall_diff_ms.Text = ((float)timer0_th_tl * 12 / 16000).ToString() + " msec";
                                tb_hall_diff_timer1.Text = "0x " + Convert.ToString((65536 - timer0_th_tl), 16).ToUpper();
                            }
                            else
                            {
                                tb_hall_diff.Text = "---";
                                tb_hall_diff_ms.Text = "---";
                                tb_hall_diff_timer1.Text = "---";
                            }
                        }
                    }
                    else if (input[1] == _TIMER1)
                    {
                        timer1_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer1 TH TL = " + Convert.ToString(timer1_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
                    else if (input[1] == _TIMER2)
                    {
                        timer2_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer2 TH TL = " + Convert.ToString(timer2_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        textBox_timer2.Text = Convert.ToString(timer2_th_tl, 16).ToString();
                    }
                    else if (input[1] == _VDC)
                    {
                        adc_vdc = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: adc_vdc = " + adc_vdc.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_ADCB.Text = Convert.ToString(adc_vdc, 16);
                        tb_ADCB_mV.Text = Convert.ToString(adc_vdc * 5000 / 4096);
                        tb_VAC.Text = Convert.ToString(adc_vdc * 5000 / 4096 * (2000 + 20) / 20 / 1414);
                    }
                    else if (input[1] == _IS)
                    {
                        adc_is = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: adc_is = " + adc_is.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        tb_ADCA.Text = Convert.ToString(adc_is, 16);
                        tb_ADCA_mV.Text = Convert.ToString(adc_is * 5000 / 4096);
                    }
                    else if (input[1] == _VR)
                    {
                        adc_vr = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: adc_vr = " + adc_vr.ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                        //if (tabControl1.SelectedIndex == 0)
                        {
                            progressBar2.Value = 100;
                            adc_vr_mv = adc_vr * 5000 / 4096;
                            tb_main_vr.Text = Convert.ToString(adc_vr_mv) + " mV";
                            progressBar_vr.Value = adc_vr_mv;
                            delay(10);
                            progressBar2.Value = 0;
                        }
                        //else if (tabControl1.SelectedIndex == 1)
                        {
                            progressBar2.Value = 100;
                            tb_VR.Text = Convert.ToString(adc_vr, 16);
                            tb_VR_mV.Text = Convert.ToString(adc_vr * 5000 / 4096);
                            delay(10);
                            progressBar2.Value = 0;
                        }
                        //else if (tabControl1.SelectedIndex == 2)
                        {
                            progressBar2.Value = 100;
                            tb_VR2.Text = Convert.ToString(adc_vr, 16);
                            tb_VR_mV2.Text = Convert.ToString(adc_vr * 5000 / 4096);
                            delay(10);
                            progressBar2.Value = 0;
                        }

                        if ((IsVRRecording == 1) || (IsDutyRecording == 1) || (IsRpmRecording == 1))
                        {
                            Graphics g = panel4.CreateGraphics();
                            //g.Clear(BackColor);
                            g.Clear(Color.White);
                            DrawXY();
                            //DrawXLine();
                            //DrawYLine();
                            g.Dispose();
                        }

                        x_st = panel4.Width * 10 / 100;
                        x_step = panel4.Width * 80 / 100 / (N - 1);
                        h_st = panel4.Height * 90 / 100;

                        if (IsVRRecording == 1)
                        {
                            ratio_vr = 4096 / (panel4.Height * 80 / 100) +2;

                            adc_vr_mv = adc_vr * 5000 / 4096;

                            //y1_value = (adc_vr_mv) / 13;
                            y1_value = (adc_vr_mv) / ratio_vr;

                            for (int i = 0; i < (N-1); i++)
                            {
                                y1_data[i] = y1_data[i + 1];
                            }
                            y1_data[N-1] = y1_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen redPen = new Pen(Color.Red, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y1_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y1_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y1_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y1_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y1_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y1_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y1_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y1_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y1_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y1_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y1_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y1_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y1_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y1_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y1_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(redPen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(redPen, curvePoints); //畫曲線
                            g.Dispose();
                        }

                        if (IsDutyRecording == 1)
                        {
                            ratio_duty = (panel4.Height * 80 / 100)/100;

                            //y2_value = duty*4;
                            y2_value = duty * ratio_duty;

                            for (int i = 0; i < 14; i++)
                            {
                                y2_data[i] = y2_data[i + 1];
                            }
                            y2_data[14] = y2_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen greenPen = new Pen(Color.Green, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y2_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y2_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y2_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y2_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y2_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y2_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y2_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y2_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y2_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y2_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y2_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y2_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y2_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y2_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y2_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(greenPen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(greenPen, curvePoints); //畫曲線

                            g.Dispose();
                        }
                        if (IsRpmRecording == 1)
                        {
                            ratio_rpm = max_speed / (panel4.Height * 80 / 100) + 1;

                            y3_value = (int)(real_speed/ratio_rpm);

                            for (int i = 0; i < 14; i++)
                            {
                                y3_data[i] = y3_data[i + 1];
                            }
                            y3_data[14] = y3_value;

                            Graphics g = panel4.CreateGraphics();
                            // Create pens.
                            Pen bluePen = new Pen(Color.Blue, 3);

                            // Create points that define curve.
                            Point point0 = new Point(x_st + x_step * 0, h_st - y3_data[0]);
                            Point point1 = new Point(x_st + x_step * 1, h_st - y3_data[1]);
                            Point point2 = new Point(x_st + x_step * 2, h_st - y3_data[2]);
                            Point point3 = new Point(x_st + x_step * 3, h_st - y3_data[3]);
                            Point point4 = new Point(x_st + x_step * 4, h_st - y3_data[4]);
                            Point point5 = new Point(x_st + x_step * 5, h_st - y3_data[5]);
                            Point point6 = new Point(x_st + x_step * 6, h_st - y3_data[6]);
                            Point point7 = new Point(x_st + x_step * 7, h_st - y3_data[7]);
                            Point point8 = new Point(x_st + x_step * 8, h_st - y3_data[8]);
                            Point point9 = new Point(x_st + x_step * 9, h_st - y3_data[9]);
                            Point point10 = new Point(x_st + x_step * 10, h_st - y3_data[10]);
                            Point point11 = new Point(x_st + x_step * 11, h_st - y3_data[11]);
                            Point point12 = new Point(x_st + x_step * 12, h_st - y3_data[12]);
                            Point point13 = new Point(x_st + x_step * 13, h_st - y3_data[13]);
                            Point point14 = new Point(x_st + x_step * 14, h_st - y3_data[14]);

                            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                            // Draw lines between original points to screen.
                            //g.DrawLines(bluePen, curvePoints);   //畫直線

                            // Draw curve to screen.
                            g.DrawCurve(bluePen, curvePoints); //畫曲線

                            g.Dispose();
                        }



                    }
                    else if (input[1] == _HALL)
                    {
                        hall_status = input[3] & 0x07;
                        //MessageBox.Show("got hall status = " + hall_status.ToString());
                        //if (tabControl1.SelectedIndex == 1)
                        {
                            switch (hall_status)
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
                        //else if (tabControl1.SelectedIndex == 2)
                        {
                            switch (hall_status)
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
                        //else if (tabControl1.SelectedIndex == 3)
                        {
                            switch (hall_status)
                            {
                                case 0:
                                    tb_Hall3.Text = "錯 000";
                                    tb_Hall3.ForeColor = Color.Red;
                                    break;
                                case 1:
                                    tb_Hall3.Text = "一 001";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 2:
                                    tb_Hall3.Text = "二 010";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 3:
                                    tb_Hall3.Text = "三 011";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 4:
                                    tb_Hall3.Text = "四 100";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 5:
                                    tb_Hall3.Text = "五 101";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 6:
                                    tb_Hall3.Text = "六 110";
                                    tb_Hall3.ForeColor = Color.Green;
                                    break;
                                case 7:
                                    tb_Hall3.Text = "錯 111";
                                    tb_Hall3.ForeColor = Color.Red;
                                    break;
                                default:
                                    tb_Hall3.Text = "錯錯錯";
                                    tb_Hall3.ForeColor = Color.Red;
                                    break;
                            }
                        }
                    }
                    else if (input[1] == _POLE_PAIR)
                    {
                        tb_main_pole_pair.Text = ((int)input[3]).ToString();
                        tb_main_pole_pair.BackColor = System.Drawing.SystemColors.Window;
                    }
                    delay(10);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xC2)          //0xC2: 收到下位發送的目前系統狀態命令
                {
                    progressBar2.Value = 100;
                    if (((input[1] >> 4) & 0x01) == 1)  //XX[4] = 1, reset
                    {
                        status_motor.Text = "RESET";
                        status_motor.ForeColor = Color.Green;
                    }
                    else
                    {
                        switch (input[1] & 0x1)
                        {
                            case 0:
                                status_motor.Text = "STOP";
                                status_motor.ForeColor = Color.Red;
                                break;
                            case 1:
                                status_motor.Text = "START";
                                status_motor.ForeColor = Color.Green;
                                break;
                            default:
                                status_motor.Text = "UNKNOWN";
                                status_motor.ForeColor = Color.Black;
                                break;
                        }
                        switch ((input[1] >> 1) & 0x07)
                        {
                            case 0:
                                status_power.Text = "電壓過壓";
                                status_power.ForeColor = Color.Red;
                                break;
                            case 1:
                                status_power.Text = "高壓警告";
                                status_power.ForeColor = Color.Orange;
                                break;
                            case 2:
                                status_power.Text = "電壓正常";
                                status_power.ForeColor = Color.Green;
                                break;
                            case 3:
                                status_power.Text = "欠壓警告";
                                status_power.ForeColor = Color.Orange;
                                break;
                            case 4:
                                status_power.Text = "電壓欠壓";
                                status_power.ForeColor = Color.Red;
                                break;
                            default:
                                status_power.Text = "電壓不詳";
                                status_power.ForeColor = Color.Black;
                                break;
                        }
                        motor_status = input[1] & 0x01;
                        power_status = (input[1] >> 1) & 0x07;
                        fw_version = (input[1] >> 4) & 0x07;
                        richTextBox1.AppendText("[PC]: fw_version = " + Convert.ToString(fw_version, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
                    delay(10);
                    progressBar2.Value = 0;
                }
                else if (input[0] == 0xCC)          //0xCC: Servo專用命令
                {
                    progressBar_servo.Value = 100;
                    target_vr = input[1];
                    real_vr = input[2];
                    trackBar_target_vr.Value = target_vr;
                    trackBar_real_vr.Value = real_vr;
                    tb_target_vr.Text = target_vr.ToString();
                    tb_real_vr.Text = real_vr.ToString();
                    delay(10);
                    progressBar_servo.Value = 0;
                }
                else if (input[0] == 0xCE)          //0xCE: Servo專用命令
                {
                    message += "[CE data]: ";
                    for (int i = 0; i < 5; i++)
                    {
                        message += ((int)input[i]).ToString("X2") + " ";
                    }
                    message += Environment.NewLine;
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行


                    int pulse_tolerance = 0;
                    int vr_variation = 0;
                    int vr_diff_tolerance = 0;
                    progressBar_servo.Value = 100;

                    pulse_tolerance = input[1];
                    vr_variation = input[2];
                    vr_diff_tolerance = input[3];

                    tb_pulse_tolerance.Text = pulse_tolerance.ToString();
                    tb_vr_variation.Text = vr_variation.ToString();
                    tb_vr_diff_tolerance.Text = vr_diff_tolerance.ToString();

                    delay(10);
                    progressBar_servo.Value = 0;
                }
                else
                {
                    //資料是5拜，但是解不出所要的資訊。
                    message += "[unknown data1]: ";
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
                message += "[unknown data2]: ";
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

        private void button8_Click(object sender, EventArgs e)
        {
            if (System.IO.File.Exists(ezisp_path) == false)
            {
                MessageBox.Show("找不到eZISP+檔案, 選取一個eZISP+檔");

                OpenFileDialog oFD = new OpenFileDialog();
                oFD.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //oFD.Filter = "exe files (*.exe)|*.exe|All files (*.*)|*.*";     //限定檔案格式
                oFD.Title = "選擇 eZISP+ 程式";

                if (oFD.ShowDialog() == DialogResult.OK)
                {
                    ezisp_path = oFD.FileName;
                    //MessageBox.Show("OPEN FILE OK, 檔名：" + oFD.FileName);
                    Process.Start(@oFD.FileName);

                    string context = string.Empty;
                    FileStream filestream = File.Open(imslink_setup_filename, FileMode.Create);
                    StreamWriter str_writer = new StreamWriter(filestream);

                    context += comboBox3.SelectedIndex.ToString();
                    context += "\n";
                    context += ezisp_path;
                    context += "\n";
                    str_writer.WriteLine(context);
                    // Dispose StreamWriter
                    str_writer.Dispose();
                    // Close FileStream
                    filestream.Close();
                    //MessageBox.Show("儲存資料完畢111，檔案：" + imslink_setup_filename);
                }
                else
                {
                    //MessageBox.Show("OPEN FILE FAIL");
                }
            }
            else
            {
                //MessageBox.Show("檔案 " + ezisp_path + " 存在, 開啟之。");
                Process.Start(@ezisp_path);
            }
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
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            numericUpDown1.Value = trackBar1.Value;

            label_speed2.Text = trackBar1.Value.ToString();

            if (trackBar1.Value == 0)
                label_target_speed2.Text = "0";
            else
                label_target_speed2.Text = (300 + 50 * (trackBar1.Value - 1)).ToString();

            label_speed2.ForeColor = System.Drawing.Color.Red;
            label_target_speed2.ForeColor = System.Drawing.Color.Red;
            numericUpDown1.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            trackBar1.Value = (Int32)numericUpDown1.Value;

            label_speed2.Text = trackBar1.Value.ToString();

            if (trackBar1.Value == 0)
                label_target_speed2.Text = "0";
            else
                label_target_speed2.Text = (300 + 50 * (trackBar1.Value - 1)).ToString();

            label_speed2.ForeColor = System.Drawing.Color.Red;
            label_target_speed2.ForeColor = System.Drawing.Color.Red;
            numericUpDown1.ForeColor = System.Drawing.Color.Red;
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

            label_speed2.ForeColor = System.Drawing.Color.Black; 
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            numericUpDown1.ForeColor = System.Drawing.Color.Black;
           
            Send_Speed_Cmd(1);
        }

        private void button_Run_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //button_Run.Enabled = false;
            //button_Stop.Enabled = true;
            //button_st.Enabled = false;
            //button_sp.Enabled = true;
            //button_st2.Enabled = false;
            //button_sp2.Enabled = true;
            IsRunning = 1;

            /*
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
            */
            label_speed2.ForeColor = System.Drawing.Color.Black;
            label_target_speed2.ForeColor = System.Drawing.Color.Black;
            numericUpDown1.ForeColor = System.Drawing.Color.Black;

            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Speed_Cmd(1);
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
            }
            else
            {
                tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
            }
            tb_target.ForeColor = System.Drawing.Color.MediumSpringGreen;
            tb_target2.ForeColor = System.Drawing.Color.MediumSpringGreen;

            if (flag_sensor_type == PCA_MODE)
            {
                Send_Parameter_Cmd(_GPIO, 3, 0);
            }
        }

        private void button_Stop_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //button_Run.Enabled = true;
            //button_Stop.Enabled = false;
            //button_st.Enabled = true;
            //button_sp.Enabled = false;
            //button_st2.Enabled = true;
            //button_sp2.Enabled = false;
            IsRunning = 0;

            /*
            label_speed2.ForeColor = System.Drawing.Color.Red;
            label_target_speed2.ForeColor = System.Drawing.Color.Red;
            numericUpDown1.ForeColor = System.Drawing.Color.Red;
             */

            richTextBox1.AppendText("[PC]: 停止\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_Speed_Cmd(0);
            tb_main_duty.Text = "20";
            tb_main_target_speed.Text = "1000";
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                tb_main_duty.Enabled = true;
                tb_main_target_speed.Enabled = false;
            }
            else
            {
                tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                tb_main_duty.Enabled = false;
                tb_main_target_speed.Enabled = true;
            }
            tb_target.ForeColor = System.Drawing.Color.OrangeRed;
            tb_target2.ForeColor = System.Drawing.Color.OrangeRed;
            if (flag_sensor_type == PCA_MODE)
            {
                Send_Parameter_Cmd(_GPIO, 3, 1);
            }
            tb_target_pca_duty.Text = "---";
            tb_real_pca_duty.Text = "---";
            tb_hall_diff.Text = "---";
            tb_hall_diff_ms.Text = "---";
            tb_hall_diff_timer1.Text = "---";
        }

        private void button_Swing_Click(object sender, EventArgs e)
        {
            if (IsRunning == 0)
            {
                //button_Swing.Enabled = false;
                //button_NoSwing.Enabled = true;

                label_speed2.ForeColor = System.Drawing.Color.Black;
                label_target_speed2.ForeColor = System.Drawing.Color.Black;
                numericUpDown1.ForeColor = System.Drawing.Color.Black;

                richTextBox1.AppendText("[PC]: 搖頭\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                Send_Speed_Cmd(1);
            }
        }

        private void button_NoSwing_Click(object sender, EventArgs e)
        {
            if (IsRunning == 0)
            {
                //button_Swing.Enabled = true;
                //button_NoSwing.Enabled = false;

                label_speed2.ForeColor = System.Drawing.Color.Black;
                label_target_speed2.ForeColor = System.Drawing.Color.Black;
                numericUpDown1.ForeColor = System.Drawing.Color.Black;

                richTextBox1.AppendText("[PC]: 停止搖頭\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                Send_Speed_Cmd(1);
            }
        }

        public bool Send_Speed_Cmd(int speed)
        {
            byte[] data = new byte[5];

            if (IsRunning == 0)
            {
                //button_Run.Enabled = true;
                //button_Stop.Enabled = false;
            }
            else
            {
                //button_Run.Enabled = false;
                //button_Stop.Enabled = true;
            }
            data[0] = 0xD3;

            data[1] = (byte)speed;

            data[4] = CalcCheckSum(data, 4);

            if (isCommandLog == 1)
            {
                richTextBox1.AppendText("[TX]: " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool Send_Control_Cmd(int control1, int control2, int control3)
        {
            byte[] data = new byte[5];

            data[0] = 0xD1;

            data[1] = (byte)control1;
            data[2] = (byte)control2;
            data[3] = (byte)control3;

            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool Send_Parameter_Cmd(int xx, int yy, int zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xD2;
            data[1] = (byte)xx;
            data[2] = (byte)yy;
            data[3] = (byte)zz;
            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool Send_Ask_Cmd(int item, int continus)
        {
            byte[] data = new byte[5];
            int send_data = 0;
            send_data = continus * 64 + item;

            data[0] = 0xD4;
            data[1] = (byte)send_data;
            data[2] = 0;
            data[3] = 0;
            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool Send_Test_Cmd(int xx, int yy, int zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xD7;
            data[1] = (byte)xx;
            data[2] = (byte)yy;
            data[3] = (byte)zz;
            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool Send_SVPWM_Mode_Cmd(int svpwm_mode)
        {
            byte[] data = new byte[5];
            data[0] = 0xD1;
            if(svpwm_mode == 1)
                data[1] = 0xfe;
            else
                data[1] = 0xfd;
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_Update_System_Status_Cmd(int on_off)
        {
            byte[] data = new byte[5];
            data[0] = 0xD5;
            if(on_off  == 1)
                data[1] = 0xfa;
            else
                data[1] = 0xf5;
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_Print_Test_Data_Cmd()
        {
            byte[] data = new byte[5];
            data[0] = 0xD1;
            data[1] = 0xfc;
            data[4] = CalcCheckSum(data, 4);

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

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://www.myson.com.tw/");
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            Send_Print_Test_Data_Cmd();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (Demo_Mode == 1)
            {
                DateTime dt = new DateTime(2016, 5, 20, 13, 14, 15, 16);
                toolStripStatusLabel1.Text = dt.ToString();
            }
            else
                toolStripStatusLabel1.Text = DateTime.Now.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
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
            byte[] data = new byte[5];

            data[0] = 0xD2;

            data[1] = (byte)(svpwm_phase);
            data[4] = CalcCheckSum(data, 4);

            //richTextBox1.AppendText("[PC]: bbbb設定, SVPWM相位 = " + data[1].ToString() + "\n");
            //richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

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

        private void bt_svpwm_phase_Click(object sender, EventArgs e)
        {
            richTextBox1.AppendText("[PC]: 設定, SVPWM相位 = " + numericUpDown2.Value.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_SVPWM_Phase_Cmd((Int32)numericUpDown2.Value);
            numericUpDown2.ForeColor = System.Drawing.Color.Black;
        }

        public bool Send_SVPWM_M_Cmd(int uart_status)
        {
            byte[] data = new byte[5];

            data[0] = 0xD8;

            data[1] = (byte)(uart_status);
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_SVPWM_Test_Cmd(int enable_svpwm)
        {
            byte[] data = new byte[5];
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

            data[4] = CalcCheckSum(data, 4);

            //MessageBox.Show("phase = " + phase.ToString() + ", data1 = " + data[1].ToString());

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _ONCE);    //Get hall status
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _ONCE);    //Get hall status
        }

        private void button12_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(1);
            numericUpDown3.ForeColor = System.Drawing.Color.Black;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(0);
            numericUpDown3.ForeColor = System.Drawing.Color.Red;
        }

        public bool Send_CMP_Enable_Cmd(byte enable, byte vth0, byte vth1)
        {
            byte[] data = new byte[5];

            data[0] = 0xD9;

            if (enable == 1)
            {
                data[1] = 0xc0 | _CMPA;
            }
            else
                data[1] = _CMPA;

            data[2] = vth0;
            data[3] = vth1;
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_DAC_Enable_Cmd(byte enable, byte dac_h, byte dac_l)
        {
            byte[] data = new byte[5];

            data[0] = 0xDA;

            if (enable == 1)
            {
                data[1] = 0xF0 | 1;
            }
            else
                data[1] = 1;

            data[2] = dac_h;
            data[3] = dac_l;
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_CMP_VTH1_Cmd(int VTH)
        {
            byte[] data = new byte[5];

            data[0] = 0xD6;

            data[1] = (byte)(VTH);
            data[4] = CalcCheckSum(data, 4);

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

        public bool Send_CMP_VTH2_Cmd(int VTH)
        {
            byte[] data = new byte[5];

            data[0] = 0xD7;

            data[1] = (byte)(VTH);
            data[4] = CalcCheckSum(data, 4);

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

        private void button19_Click(object sender, EventArgs e)
        {
            /*      old
            int VTH1 = 0;
            int VTH2 = 0;

            numericUpDown_cmp_data1.ForeColor = System.Drawing.Color.Black;
            numericUpDown_cmp_data2.ForeColor = System.Drawing.Color.Black;

            VTH1 = (Int32)numericUpDown_cmp_data1.Value;
            VTH2 = (Int32)numericUpDown_cmp_data2.Value;

            if (VTH1 > 255)
                MessageBox.Show("輸入資料錯誤，VTH1最大值為255。");
            else if (VTH1 < 0)
                MessageBox.Show("輸入資料錯誤，VTH1最小值為0。");
            else if (VTH2 > 255)
                MessageBox.Show("輸入資料錯誤，VTH2最大值為255。");
            else if (VTH2 < 0)
                MessageBox.Show("輸入資料錯誤，VTH2最小值為0。");
            else
            {
                //MessageBox.Show("輸入資料正確。 VTH1 = " + VTH1);
                //MessageBox.Show("輸入資料正確。 VTH2 = " + VTH2);
            }

            Send_CMP_VTH1_Cmd(VTH1);      //Setup Comparator VTH1

            delay(10);

            Send_CMP_VTH2_Cmd(VTH2);      //Setup Comparator VTH2

            delay(10);

            Send_CMP_Enable_Cmd(1);     //Enable Comparator

            richTextBox1.AppendText("[PC]: 設定Comparator, VTH1 = " + VTH1.ToString() + ", VTH2 = " + VTH2.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
             */
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

        private void button6_Click(object sender, EventArgs e)
        {
            Send_SVPWM_Test_Cmd(2);
            numericUpDown3.ForeColor = System.Drawing.Color.Black;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _CONTINUOUS);    //Continuously get hall status
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UART, _START, _NONE);  //UART test START
        }

        private void button16_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _STOP);    //Stop getting hall status
        }

        private void button17_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UART, _STOP, _NONE);  //UART test STOP
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
                    //MessageBox.Show("輸入資料正確。 m_value = " + m_value);

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
            Send_Ask_Cmd(_VR, _STOP);    //Stop getting VR status
        }

        private void button23_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_VR, _ONCE);    //Get VR status
        }

        private void button22_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_VR, _CONTINUOUS);    //Continuously get VR status
        }

        private void button20_Click(object sender, EventArgs e)
        {
            /*  old
            Send_CMP_Enable_Cmd(0);     //Disable Comparator
            numericUpDown_cmp_data1.ForeColor = System.Drawing.Color.Red;
            numericUpDown_cmp_data2.ForeColor = System.Drawing.Color.Red;
             */
        }

        private void button24_Click(object sender, EventArgs e)
        {
            int protection = 0;

            if (cb_protection0.Checked == true)
                protection |= 1<<0;
            if (cb_protection1.Checked == true)
                protection |= 1 << 1;
            if (cb_protection2.Checked == true)
                protection |= 1 << 2;
            if (cb_protection3.Checked == true)
                protection |= 1 << 3;

            Send_Parameter_Cmd(_PROTECTION, 0, protection);
            richTextBox1.AppendText("[PC]: 設定保護功能, protection = " + protection.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UVW, _START, _NONE);  //UVW test START
        }

        private void button25_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UVW, _STOP, _NONE);  //UVW test STOP
        }

        private void button27_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\WINDOWS\system32\calc.exe");
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            SelectedLanguage = comboBox3.SelectedIndex;
            Update_Language(SelectedLanguage);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            string context = string.Empty;
            FileStream filestream = File.Open(imslink_setup_filename, FileMode.Create);
            StreamWriter str_writer = new StreamWriter(filestream);

            context += comboBox3.SelectedIndex.ToString();
            context += "\n";
            context += ezisp_path;
            context += "\n";
            str_writer.WriteLine(context);
            // Dispose StreamWriter
            str_writer.Dispose();
            // Close FileStream
            filestream.Close();
            //MessageBox.Show("儲存資料完畢222，檔案：" + imslink_setup_filename);
        }

        private void button28_Click(object sender, EventArgs e)
        {
            OpenFileDialog oFD = new OpenFileDialog();
            oFD.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //oFD.Filter = "exe files (*.exe)|*.exe|All files (*.*)|*.*";     //限定檔案格式
            //oFD.Title = "限定選擇可執行檔，從目前目錄開始尋找檔案";
            oFD.Title = "選擇 eZISP+ 程式";

            if (oFD.ShowDialog() == DialogResult.OK)
            {
                ezisp_path = oFD.FileName;
                //MessageBox.Show("OPEN FILE OK, 檔名：" + oFD.FileName);
                Process.Start(@oFD.FileName);

                string context = string.Empty;
                FileStream filestream = File.Open(imslink_setup_filename, FileMode.Open);
                StreamWriter str_writer = new StreamWriter(filestream);

                context += comboBox3.SelectedIndex.ToString();
                context += "\n";
                context += ezisp_path;
                context += "\n";
                context += ezisp_path;
                context += "\n";
                context += ezisp_path;
                context += "\n";
                str_writer.WriteLine(context);
                // Dispose StreamWriter
                str_writer.Dispose();
                // Close FileStream
                filestream.Close();
                //MessageBox.Show("儲存資料完畢111，檔案：" + imslink_setup_filename + "路径：" + ezisp_path);

            }
            else
            {
                //MessageBox.Show("OPEN FILE FAIL");
            }

        }

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            lb_uart_debug.Text = "";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //Process.Start(@"TimerClock.exe");
            //開啟Form2表單
            Form2 Form_Timer = new Form2();
            Form_Timer.Show();
        }

        private void button31_Click(object sender, EventArgs e)
        {
            int SelectedAcceleration = 0;
            int acceleration = 0;
            SelectedAcceleration = comboBox4.SelectedIndex;
            switch (SelectedAcceleration)
            {
                case 0:
                    acceleration = 200;
                    break;
                case 1:
                    acceleration = 150;
                    break;
                case 2:
                    acceleration = 100;
                    break;
                case 3:
                    acceleration = 50;
                    break;
                case 4:
                    acceleration = 35;
                    break;
                default:
                    acceleration = 200;
                    break;
            }
            richTextBox1.AppendText("[PC]: 設定加速度 = " + SelectedAcceleration.ToString() + "accleration = " + acceleration.ToString() + "\n");
            Send_Parameter_Cmd(_ACCELERATION, 0, acceleration);
        }

        private void numericUpDown4_ValueChanged(object sender, EventArgs e)
        {
            numericUpDown4.ForeColor = System.Drawing.Color.Red;
        }

        public bool Send_RPM_Tolerance_Cmd(int rpm)
        {
            byte[] data = new byte[5];

            data[0] = 0xDC;

            data[1] = (byte)(rpm);
            data[4] = CalcCheckSum(data, 4);

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

        private void button32_Click(object sender, EventArgs e)
        {
            numericUpDown4.ForeColor = System.Drawing.Color.Black;
            richTextBox1.AppendText("[PC]: 設定允許值 = " + numericUpDown4.Value.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_RPM_Tolerance_Cmd((int)numericUpDown4.Value);
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            numericUpDown2.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown_cmp_data1_ValueChanged(object sender, EventArgs e)
        {
            numericUpDown_cmp_data1.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown_cmp_data2_ValueChanged(object sender, EventArgs e)
        {
            int VTH1 = 0;
            int VTH1_mV = 0;
            numericUpDown_cmp2_data2.ForeColor = System.Drawing.Color.Red;

            VTH1 = (Int32)numericUpDown_cmp2_data2.Value;
            VTH1_mV = VTH1 * 1800 / 255;
            tb_cmp_mV.Text = VTH1_mV.ToString();
            tb_cmp_mV.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown3_ValueChanged(object sender, EventArgs e)
        {
            numericUpDown3.ForeColor = System.Drawing.Color.Red;
        }

        private void trackBar_timer1_Scroll(object sender, EventArgs e)
        {
            string timer2_value = "";
            byte timer2_3_value = 0;
            byte timer2_2_value = 0;
            byte timer2_1_value = 0;
            byte timer2_0_value = 0;
            int timer2_start_point = 0;
            double msec = 0;
            int pair = int.Parse(tb_pair2.Text);
            if ((pair < 1) || (pair > 10))
                return;
            int rpm = 0;

            //??????? useless

            timer2_value += Convert.ToString(trackBar_3.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_2.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_1.Value, 16).ToUpper();
            timer2_value += Convert.ToString(trackBar_0.Value, 16).ToUpper();
            textBox_timer2.Text = timer2_value;

            timer2_3_value = (byte)(trackBar_3.Value);
            timer2_2_value = (byte)(trackBar_2.Value);
            timer2_1_value = (byte)(trackBar_1.Value);
            timer2_0_value = (byte)(trackBar_0.Value);

            timer2_start_point = trackBar_3.Value * 4096 + trackBar_2.Value * 256 + trackBar_1.Value * 16 + trackBar_0.Value;
            trackBar2.Value = timer2_start_point;

            msec = (65536 - timer2_start_point) * ((double)1 / 16000000 * 12) * 1000;
            if (msec < 0.001)
            {
                tb_msec.Text = "";
                return;
            }
            tb_msec.Text = msec.ToString("#00.02");     //格式化，小數點前2位，小數點後留2位四捨五入
            tb_msec2.Text = (msec*6).ToString("#00.02");     //格式化，小數點前2位，小數點後留2位四捨五入

            rpm = (int)(1 / (msec / 1000 * 6 * pair) * 60);
            if (rpm > 99999)
            {
                tb_rpm.Text = "";
                return;
            }
            tb_rpm.Text = rpm.ToString();
            textBox_timer2.ForeColor = System.Drawing.Color.Red;
            tb_rpm.ForeColor = System.Drawing.Color.Red;
            tb_msec.ForeColor = System.Drawing.Color.Red;
            tb_msec2.ForeColor = System.Drawing.Color.Red;
        }

        private void trackBar_timer1a_Scroll(object sender, EventArgs e)
        {
            string timer2_value = "";
            byte timer2_3_value = 0;
            byte timer2_2_value = 0;
            byte timer2_1_value = 0;
            byte timer2_0_value = 0;

            timer2_value += Convert.ToString(trackBar2.Value, 16).ToUpper();
            textBox_timer2.Text = timer2_value;

            timer2_3_value = (byte)((trackBar2.Value >> 12) & 0x0f);
            timer2_2_value = (byte)((trackBar2.Value >> 8) & 0x0f);
            timer2_1_value = (byte)((trackBar2.Value >> 4) & 0x0f);
            timer2_0_value = (byte)((trackBar2.Value >> 0) & 0x0f);

            trackBar_3.Value = timer2_3_value;
            trackBar_2.Value = timer2_2_value;
            trackBar_1.Value = timer2_1_value;
            trackBar_0.Value = timer2_0_value;

            textBox_timer2.ForeColor = System.Drawing.Color.Red;
            tb_rpm.ForeColor = System.Drawing.Color.Red;
            tb_msec.ForeColor = System.Drawing.Color.Red;
            tb_msec2.ForeColor = System.Drawing.Color.Red;
        }

        private void button36_Click(object sender, EventArgs e)
        {
            button36.Enabled = false;
            button37.Enabled = true;
            richTextBox1.AppendText("[PC]: 切換成 PWM 模式\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_SVPWM_Mode_Cmd(0);
        }

        private void button37_Click(object sender, EventArgs e)
        {
            button36.Enabled = true;
            button37.Enabled = false;
            richTextBox1.AppendText("[PC]: 切換成 SVPWM 模式\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            Send_SVPWM_Mode_Cmd(1);
        }

        private void button38_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _ONCE);    //Get hall status
        }

        private void button39_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _CONTINUOUS);    //Continuously get hall status
        }

        private void button40_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _STOP);    //Stop getting hall status
        }

        private void button41_Click(object sender, EventArgs e)
        {
            int duty = 0;
            string message = "";

            if (tb_duty_value.Text.Length <= 0)
            {
                MessageBox.Show("未輸入資料");
                return;
            }
            else
            {
                duty = int.Parse(tb_duty_value.Text);
                if (duty > 100)
                    MessageBox.Show("輸入資料錯誤，duty最大值為100。");
                else if (duty < 1)
                    MessageBox.Show("輸入資料錯誤，duty最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 duty = " + duty);
                    Send_Parameter_Cmd(_DUTY, 0, duty);
                    message += "[PC] Send duty =  ";
                    message += duty.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }
        }

        private void bt_drive_pulse_6_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 6, _NONE);
        }

        private void bt_drive_pulse_4_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 4, _NONE);
        }

        private void bt_drive_pulse_5_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 5, _NONE);
        }

        private void bt_drive_pulse_1_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 1, _NONE);
        }

        private void bt_drive_pulse_3_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 3, _NONE);
        }

        private void bt_drive_pulse_2_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 2, _NONE);
        }

        private void bt_drive_conti_6_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 16, _NONE);
        }

        private void bt_drive_conti_4_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 14, _NONE);
        }

        private void bt_drive_conti_5_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 15, _NONE);
        }

        private void bt_drive_conti_1_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 11, _NONE);
        }

        private void bt_drive_conti_3_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 13, _NONE);
        }

        private void bt_drive_conti_2_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 12, _NONE);
        }

        private void bt_drive_stop_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 0, _NONE);
        }

        private void button38_Click_1(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button42_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _ONCE);    //Get hall status
        }

        private void button40_Click_1(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _CONTINUOUS);    //Continuously get hall status
        }

        private void button39_Click_1(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_HALL, _STOP);    //Stop getting hall status
        }

        private void button43_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UVW, _START, _NONE);  //UVW test START
        }

        private void button44_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_UVW, _STOP, _NONE);  //UVW test STOP
        }

        private void button45_Click(object sender, EventArgs e)
        {
            int duty = 0;
            string message = "";

            if (tb_duty_value.Text.Length <= 0)
            {
                MessageBox.Show("未輸入資料");
                return;
            }
            else
            {
                duty = int.Parse(tb_duty_value.Text);
                if (duty > 100)
                    MessageBox.Show("輸入資料錯誤，duty最大值為100。");
                else if (duty < 1)
                    MessageBox.Show("輸入資料錯誤，duty最小值為1。");
                else
                {
                    duty += 1;
                    if (duty > 100)
                        duty = 100;
                    else if (duty < 1)
                        duty = 1;
                    //MessageBox.Show("輸入資料正確。 duty = " + duty);
                    Send_Parameter_Cmd(_DUTY, 0, duty);
                    message += "[PC] Send duty =  ";
                    message += duty.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }
        }

        private void button46_Click(object sender, EventArgs e)
        {
            int duty = 0;
            string message = "";

            if (tb_duty_value.Text.Length <= 0)
            {
                MessageBox.Show("未輸入資料");
                return;
            }
            else
            {
                duty = int.Parse(tb_duty_value.Text);
                if (duty > 100)
                    MessageBox.Show("輸入資料錯誤，duty最大值為100。");
                else if (duty < 1)
                    MessageBox.Show("輸入資料錯誤，duty最小值為1。");
                else
                {
                    duty -= 1;
                    if (duty > 100)
                        duty = 100;
                    else if (duty < 1)
                        duty = 1;
                    //MessageBox.Show("輸入資料正確。 duty = " + duty);
                    Send_Parameter_Cmd(_DUTY, 0, duty);
                    message += "[PC] Send duty =  ";
                    message += duty.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }
        }

        private void button47_Click(object sender, EventArgs e)
        {
            Send_Ask_Cmd(_DUTY, _ONCE);    //Get PWM duty status
        }

        private void button_speed_up_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //依目前儀表版的顯示加速。
            int setup = 0;
            int step = 0;
            if (control_2 == 0)
            {
                if (tb_main_duty2.Text.Length > 0)
                    setup = int.Parse(tb_main_duty2.Text);
                else
                    setup = int.Parse(tb_main_duty.Text);
                setup++;
                if (setup > 100)
                    setup = 100;
                tb_main_duty.Text = setup.ToString();
                tb_target.Text = "Target: " + setup.ToString() + " %";
                tb_target2.Text = "Target: " + setup.ToString() + " %";
                tb_main_duty.Text = setup.ToString();
                Send_Parameter_Cmd(_DUTY, 0, setup);
            }
            else
            {
                if (tb_main_rpm.Text.Length > 0)
                    setup = int.Parse(tb_main_rpm.Text);
                else
                    setup = int.Parse(tb_main_target_speed.Text);
                step = (int.Parse(tb_main_max_speed.Text) - int.Parse(tb_main_min_speed.Text)) / (100 - int.Parse(tb_main_duty.Text));
                setup += step;
                if (setup > int.Parse(tb_main_max_speed.Text))
                    setup = int.Parse(tb_main_max_speed.Text);
                tb_target.Text = "Target: " + setup.ToString() + " rpm";
                tb_target2.Text = "Target: " + setup.ToString() + " rpm";
                tb_main_target_speed.Text = setup.ToString();
                Send_Parameter_Cmd(_TARGET_SPEED, (setup >> 8) & 0xff, setup & 0xff);
            }
        }

        private void button_speed_down_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int setup = 0;
            int step = 0;
            if (control_2 == 0)
            {
                setup = int.Parse(tb_main_duty.Text);
                setup--;
                if (setup < 0)
                    setup = 0;
                tb_main_duty.Text = setup.ToString();
                tb_target.Text = "Target: " + setup.ToString() + " %";
                tb_target2.Text = "Target: " + setup.ToString() + " %";
                tb_main_duty.Text = setup.ToString();
                Send_Parameter_Cmd(_DUTY, 0, setup);
            }
            else
            {
                setup = int.Parse(tb_main_target_speed.Text);
                step = (int.Parse(tb_main_max_speed.Text) - int.Parse(tb_main_min_speed.Text)) / (100 - int.Parse(tb_main_duty.Text));
                setup -= step;
                if (setup < int.Parse(tb_main_min_speed.Text))
                    setup = int.Parse(tb_main_min_speed.Text);
                tb_target.Text = "Target: " + setup.ToString() + " rpm";
                tb_target2.Text = "Target: " + setup.ToString() + " rpm";
                tb_main_target_speed.Text = setup.ToString();
                Send_Parameter_Cmd(_TARGET_SPEED, (setup >> 8) & 0xff, setup & 0xff);
            }
        }

        private void tb_check_decimal_value_KeyPress(object sender, KeyPressEventArgs e)
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

        private void button35_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int duty = 0;
            string message = "";
            if (tb_main_duty.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                duty = int.Parse(tb_main_duty.Text);
                if (duty > 100)
                    MessageBox.Show("輸入資料錯誤，duty最大值為100。");
                else if (duty < 1)
                    MessageBox.Show("輸入資料錯誤，duty最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 duty = " + duty);
                    trackBar3.Value = duty;
                    Send_Parameter_Cmd(_DUTY, 0, duty);
                    flag_get_duty = 1;
                    tb_main_duty.BackColor = Color.Red;
                    message += "[PC] Send duty =  ";
                    message += duty.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    if (control_2 == 0)
                    {
                        tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                        tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                    }
                    else
                    {
                        tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                        tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                    }
                    tb_target.ForeColor = System.Drawing.Color.OrangeRed;
                    tb_target2.ForeColor = System.Drawing.Color.OrangeRed;
                }
            }
        }

        private void trackBar3_Scroll(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + trackBar3.Value.ToString() + " %";
                tb_target2.Text = "Target: " + trackBar3.Value.ToString() + " %";
            }
            else
            {
                tb_target.Text = "Target: " + trackBar3.Value.ToString() + " rpm";
                tb_target2.Text = "Target: " + trackBar3.Value.ToString() + " rpm";
            }
            tb_target.ForeColor = System.Drawing.Color.OrangeRed;
            tb_target2.ForeColor = System.Drawing.Color.OrangeRed;
        }

        private void button49_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            string message = "";
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + trackBar3.Value.ToString() + " %";
                tb_target2.Text = "Target: " + trackBar3.Value.ToString() + " %";
                Send_Parameter_Cmd(_DUTY, 0, trackBar3.Value);
                message += "[PC] Send duty =  ";
                message += trackBar3.Value.ToString();
                message += "\n";
                richTextBox1.AppendText(message);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                tb_main_duty.Text = trackBar3.Value.ToString();
            }
            else
            {
                tb_target.Text = "Target: " + trackBar3.Value.ToString() + " rpm";
                tb_target2.Text = "Target: " + trackBar3.Value.ToString() + " rpm";
                Send_Parameter_Cmd(_TARGET_SPEED, (trackBar3.Value >> 8) & 0xff, trackBar3.Value & 0xff);
                message += "[PC] Send target =  ";
                message += trackBar3.Value.ToString();
                message += "\n";
                richTextBox1.AppendText(message);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                tb_main_target_speed.Text = trackBar3.Value.ToString();
            }
            tb_target.ForeColor = System.Drawing.Color.MediumSpringGreen;
            tb_target2.ForeColor = System.Drawing.Color.MediumSpringGreen;
        }

        private void button50_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int target = 0;
            string message = "";
            if (tb_main_target_speed.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                int max = 0;
                int min = 0;
                max = int.Parse(tb_main_max_speed.Text);
                min = int.Parse(tb_main_min_speed.Text);
                target = int.Parse(tb_main_target_speed.Text);
                if (target > 100000)
                    MessageBox.Show("Error, maximum target speed is 100000.");
                else if (target < 0)
                    MessageBox.Show("Error, minimum target speed is 0.");
                else if ((target > max) || (target < min))
                    MessageBox.Show("Error, target speed must be between max and min.");
                else
                {
                    //MessageBox.Show("輸入資料正確。 target = " + target);
                    Send_Parameter_Cmd(_TARGET_SPEED, (target >> 8) & 0xff, target & 0xff);
                    flag_get_target_speed = 1;
                    tb_main_target_speed.BackColor = Color.Red;
                    message += "[PC] Send target =  ";
                    message += target.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    if (control_2 == 0)
                    {
                        tb_target.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                        tb_target2.Text = "Target: " + int.Parse(tb_main_duty.Text).ToString() + " %";
                    }
                    else
                    {
                        tb_target.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                        tb_target2.Text = "Target: " + int.Parse(tb_main_target_speed.Text).ToString() + " rpm";
                    }
                    tb_target.ForeColor = System.Drawing.Color.OrangeRed;
                    tb_target2.ForeColor = System.Drawing.Color.OrangeRed;
                }
            }
        }

        private void button52_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int max = 0;
            string message = "";
            if (tb_main_max_speed.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                max = int.Parse(tb_main_max_speed.Text);
                if (max > 100000)
                    MessageBox.Show("Error, maximum max_speed is 100000.");
                else if (max < 0)
                    MessageBox.Show("Error, minimum max_speed is 100000.");
                else
                {
                    //MessageBox.Show("輸入資料正確。 max = " + max);
                    Send_Parameter_Cmd(_MAX_SPEED, (max >> 8) & 0xff, max & 0xff);
                    flag_get_max_speed = 1;
                    tb_main_max_speed.BackColor = Color.Red;
                    message += "[PC] Send max =  ";
                    message += max.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                    max = int.Parse(tb_main_max_speed.Text);

                    int range1_st = 0;
                    int range1_sp = max * 60 / 100;
                    int range2_st = max * 60 / 100;
                    int range2_sp = max * 80 / 100;
                    int range3_st = max * 80 / 100;
                    int range3_sp = max;
                    int step = 0;

                    step = ((max+999)/1000)*100;

                    aGauge_rpm.MaxValue = max;

                    aGauge_rpm.RangesEndValue = new float[] {
        range1_sp,
        range2_sp,
        range3_sp,
        0F,
        0F};
                    aGauge_rpm.RangesStartValue = new float[] {
        range1_st,
        range2_st,
        range3_st,
        0F,
        0F};

                    aGauge_rpm.ScaleLinesMajorStepValue = step;     //這一行是必要的
                    aGauge_rpm2.MaxValue = max;

                    aGauge_rpm2.RangesEndValue = new float[] {
        range1_sp,
        range2_sp,
        range3_sp,
        0F,
        0F};
                    aGauge_rpm2.RangesStartValue = new float[] {
        range1_st,
        range2_st,
        range3_st,
        0F,
        0F};

                    aGauge_rpm2.ScaleLinesMajorStepValue = step;     //這一行是必要的
                }
            }
        }

        private void button54_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int min = 0;
            string message = "";
            if (tb_main_min_speed.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                min = int.Parse(tb_main_min_speed.Text);
                if (min > 100000)
                    MessageBox.Show("Error, maximum min_speed is 100000.");
                else if (min < 0)
                    MessageBox.Show("Error, minimum min_speed is 0.");
                else
                {
                    //MessageBox.Show("輸入資料正確。 min = " + min);
                    Send_Parameter_Cmd(_MIN_SPEED, (min >> 8) & 0xff, min & 0xff);
                    flag_get_min_speed = 1;
                    tb_main_min_speed.BackColor = Color.Red;
                    message += "[PC] Send min =  ";
                    message += min.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

            }

        }

        private void button62_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int tolerance = 0;
            string message = "";
            if (tb_main_tolerance.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                tolerance = int.Parse(tb_main_tolerance.Text);
                if (tolerance > 250)
                    MessageBox.Show("輸入資料錯誤，tolerance最大值為250。");
                else if (tolerance < 1)
                    MessageBox.Show("輸入資料錯誤，tolerance最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 tolerance = " + tolerance);
                    Send_Parameter_Cmd(_TOLERANCE, 0, tolerance);
                    flag_get_tolerance = 1;
                    tb_main_tolerance.BackColor = Color.Red;
                    message += "[PC] Send tolerance =  ";
                    message += tolerance.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

            }

        }

        private void button60_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int acceleration = 0;
            string message = "";
            if (tb_main_acceleration.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                acceleration = int.Parse(tb_main_acceleration.Text);
                if (acceleration > 250)
                    MessageBox.Show("輸入資料錯誤，acceleration最大值為250。");
                else if (acceleration < 1)
                    MessageBox.Show("輸入資料錯誤，acceleration最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 acceleration = " + acceleration);
                    Send_Parameter_Cmd(_ACCELERATION, 0, acceleration);
                    flag_get_acceleration = 1;
                    tb_main_acceleration.BackColor = Color.Red;
                    message += "[PC] Send acceleration =  ";
                    message += acceleration.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

            }

        }

        private void button58_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pole_pair = 0;
            string message = "";
            if (tb_main_pole_pair.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                pole_pair = int.Parse(tb_main_pole_pair.Text);
                if (pole_pair > 20)
                    MessageBox.Show("輸入資料錯誤，pole_pair最大值為20。");
                else if (pole_pair < 1)
                    MessageBox.Show("輸入資料錯誤，pole_pair最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 pole_pair = " + pole_pair);
                    Send_Parameter_Cmd(_POLE_PAIR, 0, pole_pair);
                    flag_get_pole_pair = 1;
                    tb_main_pole_pair.BackColor = Color.Red;
                    message += "[PC] Send pole_pair =  ";
                    message += pole_pair.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }

            }

        }

        private void button56_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int frequency = 0;
            int pwm_setup = 0;
            string message = "";

            if (tb_main_frequency.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                frequency = int.Parse(tb_main_frequency.Text);
                if (frequency > 100)
                    MessageBox.Show("輸入資料錯誤，frequency最大值為100。");
                else if (frequency < 1)
                    MessageBox.Show("輸入資料錯誤，frequency最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 frequency = " + frequency);
                    pwm_setup = 16000 / frequency / 2;
                    Send_Parameter_Cmd(_PWM_FREQUENCY, (pwm_setup >> 8) & 0xff, pwm_setup & 0xff);
                    flag_get_pwm_freq = 1;
                    tb_main_frequency.BackColor = Color.Red;
                    message += "[PC] Send frequency =  ";
                    message += frequency.ToString();
                    message += " kHz, point = ";
                    message += pwm_setup.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }

        }

        private void button29_Click_1(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_DUTY, _ONCE);
            flag_get_duty = 1;
            tb_main_duty.Text = "----";
            tb_main_duty.BackColor = Color.Red;
        }

        private void button51_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_TARGET_SPEED, _ONCE);
            flag_get_target_speed = 1;
            tb_main_target_speed.Text = "----";
            tb_main_target_speed.BackColor = Color.Red;
        }

        private void button53_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_MAX_SPEED, _ONCE);
            flag_get_max_speed = 1;
            tb_main_max_speed.Text = "----";
            tb_main_max_speed.BackColor = Color.Red;
        }

        private void button55_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_MIN_SPEED, _ONCE);
            flag_get_min_speed = 1;
            tb_main_min_speed.Text = "----";
            tb_main_min_speed.BackColor = Color.Red;
        }

        private void button63_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_TOLERANCE, _ONCE);
            flag_get_tolerance = 1;
            tb_main_tolerance.Text = "----";
            tb_main_tolerance.BackColor = Color.Red;
        }

        private void button61_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_ACCELERATION, _ONCE);
            flag_get_acceleration = 1;
            tb_main_acceleration.Text = "----";
            tb_main_acceleration.BackColor = Color.Red;
        }

        private void button59_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_POLE_PAIR, _ONCE);
            flag_get_pole_pair = 1;
            tb_main_pole_pair.Text = "----";
            tb_main_pole_pair.BackColor = Color.Red;
        }

        private void button57_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_PWM_FREQUENCY, _ONCE);
            flag_get_pwm_freq = 1;
            tb_main_frequency.Text = "----";
            tb_main_frequency.BackColor = Color.Red;
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (IsRunning == 0)
            {
                if (IsCCW == 1)
                {
                    IsCCW = 0;
                    pictureBox3.Image = imsLink.Properties.Resources.CW;
                    pictureBox4.Image = imsLink.Properties.Resources.CW;
                    pictureBox5.Image = imsLink.Properties.Resources.CW;
                    tb_direction.Text = "CW";
                    tb_direction2.Text = "CW";
                    tb_direction3.Text = "CW";
                }
                else
                {
                    IsCCW = 1;
                    pictureBox3.Image = imsLink.Properties.Resources.CCW;
                    pictureBox4.Image = imsLink.Properties.Resources.CCW;
                    pictureBox5.Image = imsLink.Properties.Resources.CCW;
                    tb_direction.Text = "CCW";
                    tb_direction2.Text = "CCW";
                    tb_direction3.Text = "CCW";
                }
                Send_Parameter_Cmd(_DIRECTION, 0, IsCCW);
                flag_get_direction = 1;
                tb_direction.BackColor = Color.Red;
                tb_direction2.BackColor = Color.Red;
                tb_direction3.BackColor = Color.Red;
                if (flag_sensor_type == PCA_MODE)
                {
                    Send_Parameter_Cmd(_GPIO, 4, 1-IsCCW);
                }

            }
        }

        private void tb_main_max_speed_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button52_Click(sender, e);
            }
        }

        private void tb_main_duty_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button35_Click(sender, e);
            }
        }

        private void tb_main_target_speed_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button50_Click(sender, e);
            }
        }

        private void tb_main_min_speed_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button54_Click(sender, e);
            }
        }

        private void tb_main_tolerance_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button62_Click(sender, e);
            }
        }

        private void tb_main_acceleration_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button60_Click(sender, e);
            }
        }

        private void tb_main_pole_pair_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button58_Click(sender, e);
            }
        }

        private void tb_main_frequency_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                button56_Click(sender, e);
            }
        }

        private void button64_Click(object sender, EventArgs e)
        {
            if (IsVRRecording == 1)
                IsVRRecording = 0;
            else
                IsVRRecording = 1;
        }

        private void button65_Click(object sender, EventArgs e)
        {
            if (IsDutyRecording == 1)
                IsDutyRecording = 0;
            else
                IsDutyRecording = 1;
        }

        private void button66_Click(object sender, EventArgs e)
        {
            if (IsRpmRecording == 1)
                IsRpmRecording = 0;
            else
                IsRpmRecording = 1;
        }

        private void button67_Click(object sender, EventArgs e)
        {
            Graphics g = panel4.CreateGraphics();
            g.Clear(Color.White);
            //順道清掉舊資料
            for (int i = 0; i < (N); i++)
            {
                y1_data[i] = 0;
                y2_data[i] = 0;
                y3_data[i] = 0;
            }
        }

        private void trackBar4_Scroll(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + trackBar4.Value.ToString() + " %";
                tb_target2.Text = "Target: " + trackBar4.Value.ToString() + " %";
            }
            else
            {
                tb_target.Text = "Target: " + trackBar4.Value.ToString() + " rpm";
                tb_target2.Text = "Target: " + trackBar4.Value.ToString() + " rpm";
            }
            tb_target.ForeColor = System.Drawing.Color.OrangeRed;
            tb_target2.ForeColor = System.Drawing.Color.OrangeRed;

        }

        private void button68_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            string message = "";
            if (control_2 == 0)
            {
                tb_target.Text = "Target: " + trackBar4.Value.ToString() + " %";
                tb_target2.Text = "Target: " + trackBar4.Value.ToString() + " %";
                Send_Parameter_Cmd(_DUTY, 0, trackBar4.Value);
                message += "[PC] Send duty =  ";
                message += trackBar4.Value.ToString();
                message += "\n";
                richTextBox1.AppendText(message);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                tb_main_duty.Text = trackBar4.Value.ToString();
            }
            else
            {
                tb_target.Text = "Target: " + trackBar4.Value.ToString() + " rpm";
                tb_target2.Text = "Target: " + trackBar4.Value.ToString() + " rpm";
                Send_Parameter_Cmd(_TARGET_SPEED, (trackBar4.Value >> 8) & 0xff, trackBar4.Value & 0xff);
                message += "[PC] Send target =  ";
                message += trackBar4.Value.ToString();
                message += "\n";
                richTextBox1.AppendText(message);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                tb_main_target_speed.Text = trackBar4.Value.ToString();
            }
            tb_target.ForeColor = System.Drawing.Color.MediumSpringGreen;
            tb_target2.ForeColor = System.Drawing.Color.MediumSpringGreen;
        }

        private void button_phase_comp_st_Click(object sender, EventArgs e)
        {
            int phase_comp_angle = 0;
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //button_phase_comp_st.Enabled = false;
            //button_phase_comp_sp.Enabled = true;
            IsPhaseComp = 1;

            if (tb_phase_comp.Text.Length > 0)
            {
                phase_comp_angle = int.Parse(tb_phase_comp.Text);
                Send_Parameter_Cmd(_PHASE_COMP, _START, phase_comp_angle);
                richTextBox1.AppendText("[PC]: 開啟相位補償功能, phase = " + phase_comp_angle.ToString() + "\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
            else
            {
                MessageBox.Show("Phase angle setup error!", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }

        private void button_phase_comp_sp_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //button_phase_comp_st.Enabled = true;
            //button_phase_comp_sp.Enabled = false;
            IsPhaseComp = 0;

            Send_Parameter_Cmd(_PHASE_COMP, _STOP, _NONE);
            richTextBox1.AppendText("[PC]: 關閉相位補償功能\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void trackBar5_Scroll(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            tb_phase_comp.Text = trackBar5.Value.ToString();
            tb_phase_comp.ForeColor = System.Drawing.Color.OrangeRed;
        }

        private void button71_Click(object sender, EventArgs e)
        {
            int phase_comp_angle = 0;
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (IsPhaseComp == 0)
            {
                MessageBox.Show("尚未開啟相位補償功能", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (tb_phase_comp.Text.Length > 0)
            {
                phase_comp_angle = int.Parse(tb_phase_comp.Text);
                Send_Parameter_Cmd(_PHASE_COMP, _START, phase_comp_angle);
                richTextBox1.AppendText("[PC]: 設定相位補償相角, phase = " + phase_comp_angle.ToString() + "\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
            else
            {
                MessageBox.Show("Phase angle setup error!", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            tb_phase_comp.ForeColor = System.Drawing.Color.MediumSpringGreen;
        }

        public bool Send_AC_Motor_Cmd(int xx, int yy, int zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xD8;
            data[1] = (byte)xx;
            data[2] = (byte)yy;
            data[3] = (byte)zz;
            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        int show_comport_log = 0;
        private void button33_Click(object sender, EventArgs e)
        {
            if(show_comport_log == 0)
            {
                show_comport_log = 1;
                button33.BackgroundImage = imsLink.Properties.Resources.close_log;
                this.Width += 400;
            }
            else
            {
                show_comport_log = 0;
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

        private void button75_Click(object sender, EventArgs e)
        {
            int VTH0 = 0;
            int VTH1 = 0;

            numericUpDown_cmp2_data1.ForeColor = System.Drawing.Color.Black;
            numericUpDown_cmp2_data2.ForeColor = System.Drawing.Color.Black;

            VTH0 = (Int32)numericUpDown_cmp2_data1.Value;
            VTH1 = (Int32)numericUpDown_cmp2_data2.Value;

            if (VTH0 > 255)
                MessageBox.Show("輸入資料錯誤，VTH0最大值為255。");
            else if (VTH0 < 0)
                MessageBox.Show("輸入資料錯誤，VTH0最小值為0。");
            else if (VTH1 > 255)
                MessageBox.Show("輸入資料錯誤，VTH1最大值為255。");
            else if (VTH1 < 0)
                MessageBox.Show("輸入資料錯誤，VTH1最小值為0。");
            else
            {
                //MessageBox.Show("輸入資料正確。 VTH0 = " + VTH0);
                //MessageBox.Show("輸入資料正確。 VTH1 = " + VTH1);
            }

            Send_CMP_Enable_Cmd(1, (byte)VTH0, (byte)VTH1);     //Enable Comparator

            richTextBox1.AppendText("[PC]: 設定Comparator, VTH0 = " + VTH0.ToString() + ", VTH1 = " + VTH1.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

            ProtectionFunction |= 1 << _PROTECTION_OCC;
            Refresh_Protection_Setting();

        }

        private void button76_Click(object sender, EventArgs e)
        {
            Send_CMP_Enable_Cmd(0, 0, 0);     //Disable Comparator
            numericUpDown_cmp2_data1.ForeColor = System.Drawing.Color.Red;
            numericUpDown_cmp2_data2.ForeColor = System.Drawing.Color.Red;
            ProtectionFunction &= 0xfc;
            Refresh_Protection_Setting();
        }

        private void bt_drive_auto_Click(object sender, EventArgs e)
        {
            Send_Test_Cmd(_TEST_PWM, 0x55, _NONE);
        }

        private void button77_Click(object sender, EventArgs e)
        {
            int dac_data = 0;
            int dac_mV = 0;

            numericUpDown_dac_data.ForeColor = System.Drawing.Color.Black;
            tb_dac_mV.ForeColor = System.Drawing.Color.Black;

            dac_data = (Int32)numericUpDown_dac_data.Value;
            dac_mV = int.Parse(tb_dac_mV.Text);

            if (dac_data > 1023)
                MessageBox.Show("輸入資料錯誤，DAC_DATA最大值為1023。");
            else if (dac_data < 0)
                MessageBox.Show("輸入資料錯誤，DAC_DATA最小值為0。");
            else if (dac_mV > 5000)
                MessageBox.Show("輸入資料錯誤，DAC_mV最大值為5000。");
            else if (dac_mV < 0)
                MessageBox.Show("輸入資料錯誤，DAC_mV最小值為0。");
            else
            {
                //MessageBox.Show("輸入資料正確。 dac_data = " + dac_data);
                //MessageBox.Show("輸入資料正確。 dac_mV = " + dac_mV);
                Send_DAC_Enable_Cmd(1, (byte)(dac_data >> 8), (byte)(dac_data & 0xff));     //Enable DAC
                richTextBox1.AppendText("[PC]: 設定DAC, data = " + dac_data.ToString() + " = " + dac_mV.ToString() + " mV\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }
        }

        private void button78_Click(object sender, EventArgs e)
        {

            Send_DAC_Enable_Cmd(0, 0, 0);     //Disable DAC
            numericUpDown_dac_data.ForeColor = System.Drawing.Color.Red;
            tb_dac_mV.ForeColor = System.Drawing.Color.Red;

        }

        private void numericUpDown_dac_data_ValueChanged(object sender, EventArgs e)
        {
            int dac_data = 0;
            int dac_mV = 0;

            dac_data = (Int32)numericUpDown_dac_data.Value;
            dac_mV = dac_data *5000 / 1023;

            numericUpDown_dac_data.ForeColor = System.Drawing.Color.Red;
            tb_dac_mV.ForeColor = System.Drawing.Color.Red;
            tb_dac_mV.Text = dac_mV.ToString();
        }

        public bool check_dac_mV()
        {
            int dac_data = 0;
            int dac_mV = 0;
            if (tb_dac_mV.Text.Length == 0)
            {
                MessageBox.Show("Error, no DAC mV value.");
                return false;
            }
            else
                dac_mV = int.Parse(tb_dac_mV.Text);
            if (dac_mV > 5000)
            {
                MessageBox.Show("Error, maximum DAC mV is 5000.");
                return false;
            }
            else if (dac_mV < 0)
            {
                MessageBox.Show("Error, minimum DAC mV is 0.");
                return false;
            }
            else
            {
                //MessageBox.Show("輸入資料正確。 dac_mV = " + dac_mV.ToString());
                dac_data = dac_mV*1023/5000;
                numericUpDown_dac_data.Value = dac_data;
                return true;
            }
        }

        public bool check_adc_mV()
        {
            int adc_data = 0;
            int adc_mV = 0;
            if (tb_adc_mV.Text.Length == 0)
            {
                MessageBox.Show("Error, no ADC mV value.");
                return false;
            }
            else
                adc_mV = int.Parse(tb_adc_mV.Text);
            if (adc_mV > 5000)
            {
                MessageBox.Show("Error, maximum ADC mV is 5000.");
                return false;
            }
            else if (adc_mV < 0)
            {
                MessageBox.Show("Error, minimum ADC mV is 0.");
                return false;
            }
            else
            {
                //MessageBox.Show("輸入資料正確。 adc_mV = " + adc_mV.ToString());
                adc_data = adc_mV*4095/5000;
                numericUpDown_adc_data.Value = adc_data;
                return true;
            }
        }

        private void tb_dac_mV_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                check_dac_mV();
            }
            else
            {
                e.Handled = true;
            }
        }

        private void button79_Click(object sender, EventArgs e)
        {
            int protection = 0;

            if (cb_protection_00.Checked == true)
                protection |= 1 << 0;
            if (cb_protection_01.Checked == true)
                protection |= 1 << 1;
            if (cb_protection_02.Checked == true)
                protection |= 1 << 2;
            if (cb_protection_03.Checked == true)
                protection |= 1 << 3;
            if (cb_protection_04.Checked == true)
                protection |= 1 << 4;
            if (cb_protection_05.Checked == true)
                protection |= 1 << 5;
            if (cb_protection_06.Checked == true)
                protection |= 1 << 6;

            ProtectionFunction = protection;
            Refresh_Protection_Setting();

            Send_Protection_Cmd(0xff, 0, protection);
            richTextBox1.AppendText("[PC]: 設定保護功能, protection = " + protection.ToString() + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        public bool Send_Protection_Cmd(int xx, int yy, int zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xDB;
            data[1] = (byte)xx;
            data[2] = (byte)yy;
            data[3] = (byte)zz;
            data[4] = CalcCheckSum(data, 4);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        private void button82_Click(object sender, EventArgs e)
        {
            int v1 = 0;
            int v2 = 0;
            int v3 = 0;
            int v4 = 0;
            v1 = int.Parse(tb_v1.Text);
            v2 = int.Parse(tb_v2.Text);
            v3 = int.Parse(tb_v3.Text);
            v4 = int.Parse(tb_v4.Text);

            if ((v1 <= 0) || (v2 <= 0) || (v3 <= 0) || (v4 <= 0))
                MessageBox.Show("輸入資料錯誤，保護電壓值錯誤。");
            else if ((v1 >= 500) || (v2 >= 500) || (v3 >= 500) || (v4 >= 500))
                MessageBox.Show("輸入資料錯誤，保護電壓值錯誤，最多500V。");
            else
            {
                richTextBox1.AppendText("[PC]: 過壓保護 = " + v1.ToString() + "V\n");
                richTextBox1.AppendText("[PC]: 過壓恢復 = " + v2.ToString() + "V\n");
                richTextBox1.AppendText("[PC]: 欠壓恢復 = " + v3.ToString() + "V\n");
                richTextBox1.AppendText("[PC]: 欠壓保護 = " + v4.ToString() + "V\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

                ProtectionFunction |= 1 << _PROTECTION_VDC;
                Refresh_Protection_Setting();

                Send_Protection_Cmd(_PROTECTION_VDC << 4 | 0x0f, (1 << 4) | ((v1 >> 8) & 0xff), v1 & 0xff);
                delay(10);
                Send_Protection_Cmd(_PROTECTION_VDC << 4 | 0x0f, (2 << 4) | ((v2 >> 8) & 0xff), v2 & 0xff);
                delay(10);
                Send_Protection_Cmd(_PROTECTION_VDC << 4 | 0x0f, (3 << 4) | ((v3 >> 8) & 0xff), v3 & 0xff);
                delay(10);
                Send_Protection_Cmd(_PROTECTION_VDC << 4 | 0x0f, (4 << 4) | ((v4 >> 8) & 0xff), v4 & 0xff);

                tb_v1.ForeColor = System.Drawing.Color.Black;
                tb_v2.ForeColor = System.Drawing.Color.Black;
                tb_v3.ForeColor = System.Drawing.Color.Black;
                tb_v4.ForeColor = System.Drawing.Color.Black;
            }
        }

        private void button83_Click(object sender, EventArgs e)
        {
            Send_Protection_Cmd(_PROTECTION_VDC << 4 | 0x00, 0, 0);

            ProtectionFunction &= 0xdf;
            Refresh_Protection_Setting();

            tb_v1.ForeColor = System.Drawing.Color.Red;
            tb_v2.ForeColor = System.Drawing.Color.Red;
            tb_v3.ForeColor = System.Drawing.Color.Red;
            tb_v4.ForeColor = System.Drawing.Color.Red;
        }

        private void button80_Click(object sender, EventArgs e)
        {
            int adc_data = 0;
            int adc_mV = 0;

            numericUpDown_adc_data.ForeColor = System.Drawing.Color.Black;
            tb_adc_mV.ForeColor = System.Drawing.Color.Black;

            adc_data = (Int32)numericUpDown_adc_data.Value;
            adc_mV = int.Parse(tb_adc_mV.Text);

            if (adc_data > 4095)
                MessageBox.Show("輸入資料錯誤，ADC_DATA最大值為4095。");
            else if (adc_data < 0)
                MessageBox.Show("輸入資料錯誤，ADC_DATA最小值為0。");
            else if (adc_mV > 5000)
                MessageBox.Show("輸入資料錯誤，ADC_mV最大值為5000。");
            else if (adc_mV < 0)
                MessageBox.Show("輸入資料錯誤，ADC_mV最小值為0。");
            else
            {
                //MessageBox.Show("輸入資料正確。 adc_data = " + adc_data);
                //MessageBox.Show("輸入資料正確。 adc_mV = " + adc_mV);
                Send_Protection_Cmd(_PROTECTION_OCA << 4 | 0x0f, (byte)(adc_data >> 8), (byte)(adc_data & 0xff));     //Setup ADC data
                richTextBox1.AppendText("[PC]: 設定ADC, data = " + adc_data.ToString() + " = " + adc_mV.ToString() + " mV\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                ProtectionFunction |= 1 << _PROTECTION_OCA;
                Refresh_Protection_Setting();
            }
        }

        private void tb_adc_mV_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                check_adc_mV();
            }
            else
            {
                e.Handled = true;
            }
        }

        private void numericUpDown_adc_data_ValueChanged(object sender, EventArgs e)
        {
            int adc_data = 0;
            int adc_mV = 0;

            adc_data = (Int32)numericUpDown_adc_data.Value;
            adc_mV = adc_data * 5000 / 4095;

            numericUpDown_adc_data.ForeColor = System.Drawing.Color.Red;
            tb_adc_mV.ForeColor = System.Drawing.Color.Red;
            tb_adc_mV.Text = adc_mV.ToString();

        }

        private void button81_Click(object sender, EventArgs e)
        {
            Send_Protection_Cmd(_PROTECTION_OCA << 4 | 0x00, 0, 0);
            ProtectionFunction &= 0xfe;
            Refresh_Protection_Setting();
            numericUpDown_adc_data.ForeColor = System.Drawing.Color.Red;
            tb_adc_mV.ForeColor = System.Drawing.Color.Red;
        }

        private void button_speed_up3_Click(object sender, EventArgs e)
        {
            Send_Speed_Up_Cmd(1);
        }

        private void button_speed_down3_Click(object sender, EventArgs e)
        {
            Send_Speed_Up_Cmd(0);
        }

        public bool Send_Speed_Up_Cmd(int up)
        {
            byte[] data = new byte[5];

            data[0] = 0xD3;
            data[1] = 0;
            data[2] = 0;
            if (up == 1)
                data[3] = 0xAA;
            else
                data[3] = 0x55;
            data[4] = CalcCheckSum(data, 4);

            if (isCommandLog == 1)
            {
                richTextBox1.AppendText("[TX]: " + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n");
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
            }

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        public bool check_cmp_mV()
        {
            int cmp_data = 0;
            int cmp_mV = 0;
            if (tb_cmp_mV.Text.Length == 0)
            {
                MessageBox.Show("Error, no CMP mV value.");
                return false;
            }
            else
                cmp_mV = int.Parse(tb_cmp_mV.Text);
            if (cmp_mV > 1800)
            {
                MessageBox.Show("Error, maximum CMP mV is 1800.");
                return false;
            }
            else if (cmp_mV < 0)
            {
                MessageBox.Show("Error, minimum CMP mV is 0.");
                return false;
            }
            else
            {
                //MessageBox.Show("輸入資料正確。 cmp_mV = " + cmp_mV.ToString());
                cmp_data = cmp_mV * 255 / 1800;
                numericUpDown_cmp2_data2.Value = cmp_data;
                return true;
            }
        }

        private void tb_cmp_mV_KeyPress(object sender, KeyPressEventArgs e)
        {
            // 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                check_cmp_mV();
            }
            else
            {
                e.Handled = true;
            }

        }

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
                System.Threading.Thread.Sleep(1);
        }

        private void refresh_meter()
        {
            int i = 0;

            for (i = 0; i <= aGauge_rpm.MaxValue; i += 100)
            {
                aGauge_rpm.Value = i;
                delay(1);
            }
            aGauge_rpm.Value = aGauge_rpm.MaxValue;
            for (i = 0; i <= aGauge_rpm.MaxValue; i += 100)
            {
                aGauge_rpm.Value = aGauge_rpm.MaxValue - i;
                delay(1);
            }

        }

        private void button85_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            Send_Ask_Cmd(_START_DUTY, _ONCE);
            flag_get_start_duty = 1;
            tb_main_start_duty.Text = "----";
            tb_main_start_duty.BackColor = Color.Red;
            richTextBox1.Text += "send get start duty command\n";
        }

        private void button84_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int start_duty = 0;
            string message = "";
            if (tb_main_start_duty.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                start_duty = int.Parse(tb_main_start_duty.Text);
                if (start_duty > 100)
                    MessageBox.Show("輸入資料錯誤，start duty最大值為100。");
                else if (start_duty < 1)
                    MessageBox.Show("輸入資料錯誤，start duty最小值為1。");
                else
                {
                    //MessageBox.Show("輸入資料正確。 start_duty = " + start_duty);
                    Send_Parameter_Cmd(_START_DUTY, 0, start_duty);
                    flag_get_start_duty = 1;
                    tb_main_start_duty.BackColor = Color.Red;
                    message += "[PC] Send start_duty =  ";
                    message += start_duty.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }

        }

        private void button69_Click(object sender, EventArgs e)
        {
            panel1.BackColor = System.Drawing.SystemColors.ControlLightLight;
            panel5.BackColor = System.Drawing.SystemColors.ControlLightLight;
            tb_target.Text = "Target: " + 36.ToString() + " %";
            tb_target2.Text = "Target: " + 36.ToString() + " %";
            aGauge_rpm.Value = 1688;
            tb_main_rpm.Text = 1688.ToString();
            aGauge_duty.Value = 36;
            trackBar3.Value = 36;
            tb_main_duty2.Text = 36.ToString();
            tb_main_vr.Text = 3456.ToString() +" mV";
            progressBar_vr.Value = 3456;
            //button_st.Enabled = false;
            //button_sp.Enabled = true;

            timer_demo.Enabled = true;
            Demo_Mode = 1;
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

        private void button93_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int duty = 0;
            int timer_start_point = 0;

            duty = (int)numericUpDown5.Value;

            //richTextBox1.Text += "trackBar_3 = " + trackBar_3.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_2 = " + trackBar_2.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_1 = " + trackBar_1.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_0 = " + trackBar_0.Value.ToString() + "\n";
            
            //timer_start_point = trackBar_3.Value << 12 + trackBar_2.Value << 8 + trackBar_1.Value << 4 + trackBar_0.Value;
            timer_start_point = trackBar_3.Value * 4096 + trackBar_2.Value * 256 + trackBar_1.Value * 16 + trackBar_0.Value;

            //richTextBox1.Text += "T1 value = " + timer_start_point.ToString() + "\n";

            Send_AC_Motor_Cmd(duty, (timer_start_point >> 8) & 0xff, timer_start_point & 0xff);
            textBox_timer2.ForeColor = System.Drawing.Color.Black;
            tb_rpm.ForeColor = System.Drawing.Color.Black;
            tb_msec.ForeColor = System.Drawing.Color.Black;
            tb_msec2.ForeColor = System.Drawing.Color.Black;
            numericUpDown5.ForeColor = System.Drawing.Color.Black;
        }

        int demo_duty = 36;
        int demo_rpm = 1688;
        int demo_vr = 1234;
        private void timer_demo_Tick(object sender, EventArgs e)
        {
            demo_duty++;
            demo_rpm += 123;
            demo_vr += 237;
            if(demo_duty >=100)
                demo_duty = 36;
            if(demo_rpm >= aGauge_rpm.MaxValue)
                demo_rpm = 688;
            if(demo_vr >= 4000)
                demo_vr = 234;

            tb_target.Text = "Target: " + demo_duty.ToString() + " %";
            tb_target2.Text = "Target: " + demo_duty.ToString() + " %";
            aGauge_rpm.Value = demo_rpm;
            tb_main_rpm.Text = demo_rpm.ToString();
            aGauge_duty.Value = demo_duty;
            trackBar3.Value = demo_duty;
            tb_main_duty2.Text = demo_duty.ToString();
            tb_main_vr.Text = demo_vr.ToString() + " mV";
            progressBar_vr.Value = demo_vr;

            Graphics g = panel4.CreateGraphics();
            //g.Clear(BackColor);
            g.Clear(Color.White);
            DrawXY();
            //DrawXLine();
            //DrawYLine();
            g.Dispose();

            demo_record_function();
        }

        void demo_record_function()
        {

            x_st = panel4.Width * 10 / 100;
            x_step = panel4.Width * 80 / 100 / (N - 1);
            h_st = panel4.Height * 90 / 100;

            if (IsVRRecording == 1)
            {
                ratio_vr = 4096 / (panel4.Height * 80 / 100) + 2;

                adc_vr_mv = demo_vr * 5000 / 4096;

                //y1_value = (adc_vr_mv) / 13;
                y1_value = (adc_vr_mv) / ratio_vr;

                for (int i = 0; i < (N - 1); i++)
                {
                    y1_data[i] = y1_data[i + 1];
                }
                y1_data[N - 1] = y1_value;

                Graphics g = panel4.CreateGraphics();
                // Create pens.
                Pen redPen = new Pen(Color.Red, 3);

                // Create points that define curve.
                Point point0 = new Point(x_st + x_step * 0, h_st - y1_data[0]);
                Point point1 = new Point(x_st + x_step * 1, h_st - y1_data[1]);
                Point point2 = new Point(x_st + x_step * 2, h_st - y1_data[2]);
                Point point3 = new Point(x_st + x_step * 3, h_st - y1_data[3]);
                Point point4 = new Point(x_st + x_step * 4, h_st - y1_data[4]);
                Point point5 = new Point(x_st + x_step * 5, h_st - y1_data[5]);
                Point point6 = new Point(x_st + x_step * 6, h_st - y1_data[6]);
                Point point7 = new Point(x_st + x_step * 7, h_st - y1_data[7]);
                Point point8 = new Point(x_st + x_step * 8, h_st - y1_data[8]);
                Point point9 = new Point(x_st + x_step * 9, h_st - y1_data[9]);
                Point point10 = new Point(x_st + x_step * 10, h_st - y1_data[10]);
                Point point11 = new Point(x_st + x_step * 11, h_st - y1_data[11]);
                Point point12 = new Point(x_st + x_step * 12, h_st - y1_data[12]);
                Point point13 = new Point(x_st + x_step * 13, h_st - y1_data[13]);
                Point point14 = new Point(x_st + x_step * 14, h_st - y1_data[14]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                // Draw lines between original points to screen.
                //g.DrawLines(redPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(redPen, curvePoints); //畫曲線
                g.Dispose();
            }

            if (IsDutyRecording == 1)
            {
                ratio_duty = (panel4.Height * 80 / 100) / 100;

                //y2_value = duty*4;
                y2_value = demo_duty * ratio_duty;

                for (int i = 0; i < 14; i++)
                {
                    y2_data[i] = y2_data[i + 1];
                }
                y2_data[14] = y2_value;

                Graphics g = panel4.CreateGraphics();
                // Create pens.
                Pen greenPen = new Pen(Color.Green, 3);

                // Create points that define curve.
                Point point0 = new Point(x_st + x_step * 0, h_st - y2_data[0]);
                Point point1 = new Point(x_st + x_step * 1, h_st - y2_data[1]);
                Point point2 = new Point(x_st + x_step * 2, h_st - y2_data[2]);
                Point point3 = new Point(x_st + x_step * 3, h_st - y2_data[3]);
                Point point4 = new Point(x_st + x_step * 4, h_st - y2_data[4]);
                Point point5 = new Point(x_st + x_step * 5, h_st - y2_data[5]);
                Point point6 = new Point(x_st + x_step * 6, h_st - y2_data[6]);
                Point point7 = new Point(x_st + x_step * 7, h_st - y2_data[7]);
                Point point8 = new Point(x_st + x_step * 8, h_st - y2_data[8]);
                Point point9 = new Point(x_st + x_step * 9, h_st - y2_data[9]);
                Point point10 = new Point(x_st + x_step * 10, h_st - y2_data[10]);
                Point point11 = new Point(x_st + x_step * 11, h_st - y2_data[11]);
                Point point12 = new Point(x_st + x_step * 12, h_st - y2_data[12]);
                Point point13 = new Point(x_st + x_step * 13, h_st - y2_data[13]);
                Point point14 = new Point(x_st + x_step * 14, h_st - y2_data[14]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                // Draw lines between original points to screen.
                //g.DrawLines(greenPen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(greenPen, curvePoints); //畫曲線

                g.Dispose();
            }
            if (IsRpmRecording == 1)
            {
                ratio_rpm = max_speed / (panel4.Height * 80 / 100) + 1;

                y3_value = (int)(demo_rpm / ratio_rpm);

                for (int i = 0; i < 14; i++)
                {
                    y3_data[i] = y3_data[i + 1];
                }
                y3_data[14] = y3_value;

                Graphics g = panel4.CreateGraphics();
                // Create pens.
                Pen bluePen = new Pen(Color.Blue, 3);

                // Create points that define curve.
                Point point0 = new Point(x_st + x_step * 0, h_st - y3_data[0]);
                Point point1 = new Point(x_st + x_step * 1, h_st - y3_data[1]);
                Point point2 = new Point(x_st + x_step * 2, h_st - y3_data[2]);
                Point point3 = new Point(x_st + x_step * 3, h_st - y3_data[3]);
                Point point4 = new Point(x_st + x_step * 4, h_st - y3_data[4]);
                Point point5 = new Point(x_st + x_step * 5, h_st - y3_data[5]);
                Point point6 = new Point(x_st + x_step * 6, h_st - y3_data[6]);
                Point point7 = new Point(x_st + x_step * 7, h_st - y3_data[7]);
                Point point8 = new Point(x_st + x_step * 8, h_st - y3_data[8]);
                Point point9 = new Point(x_st + x_step * 9, h_st - y3_data[9]);
                Point point10 = new Point(x_st + x_step * 10, h_st - y3_data[10]);
                Point point11 = new Point(x_st + x_step * 11, h_st - y3_data[11]);
                Point point12 = new Point(x_st + x_step * 12, h_st - y3_data[12]);
                Point point13 = new Point(x_st + x_step * 13, h_st - y3_data[13]);
                Point point14 = new Point(x_st + x_step * 14, h_st - y3_data[14]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14 };

                // Draw lines between original points to screen.
                //g.DrawLines(bluePen, curvePoints);   //畫直線

                // Draw curve to screen.
                g.DrawCurve(bluePen, curvePoints); //畫曲線

                g.Dispose();
            }
        }

        private void button38_Click_2(object sender, EventArgs e)
        {
            control_1 = 0;
            set_and_wait_response();
        }

        private void button48_Click(object sender, EventArgs e)
        {
            control_1 = 1;
            set_and_wait_response();
        }

        private void button90_Click(object sender, EventArgs e)
        {
            trackBar3.Maximum = 100;
            trackBar3.Minimum = 0;
            trackBar3.Value = 20;
            trackBar3.TickFrequency = 5;
            tb_main_duty.Enabled = true;
            tb_main_target_speed.Enabled = false;
            tb_main_max_speed.Enabled = true;
            tb_main_min_speed.Enabled = false;
            tb_main_tolerance.Enabled = false;
            tb_main_acceleration.Enabled = false;
            control_2 = 0;
            set_and_wait_response();
        }

        private void button91_Click(object sender, EventArgs e)
        {
            trackBar3.Maximum = max_speed;
            trackBar3.Minimum = 0;
            trackBar3.Value = target_speed;
            trackBar3.TickFrequency = max_speed/20;
            tb_main_duty.Enabled = false;
            tb_main_target_speed.Enabled = true;
            tb_main_max_speed.Enabled = true;
            tb_main_min_speed.Enabled = true;
            tb_main_tolerance.Enabled = true;
            tb_main_acceleration.Enabled = true;
            control_2 = 1;
            set_and_wait_response();
        }

        private void button92_Click(object sender, EventArgs e)
        {
            control_3 = 0;
            set_and_wait_response();
        }

        private void button93_Click_1(object sender, EventArgs e)
        {
            control_3 = 1;
            set_and_wait_response();
        }
        void set_and_wait_response()
        {
            int yy = 0;
            int zz = 2; //CM2209B
            gb_main_1.Enabled = false;
            gb_main_2.Enabled = false;
            gb_main_3.Enabled = false;
            gb_main_4.Enabled = false;
            gb_main_5.Enabled = false;
            gb_main_6.Enabled = false;
            gb_ac2.Enabled = false;
            gb_ac3.Enabled = false;
            yy = (control_1 << 7) | (control_2 << 6) | (control_3 << 4) | (control_7 << 0);
            Send_Control_Cmd(0, yy, zz);
        }

        private void button102_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int duty = 0;
            duty = (int)numericUpDown5.Value;
            Send_Parameter_Cmd(_DUTY, 0, duty);
            numericUpDown5.ForeColor = System.Drawing.Color.Black;
        }

        private void button103_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            int timer_start_point = 0;

            //richTextBox1.Text += "trackBar_3 = " + trackBar_3.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_2 = " + trackBar_2.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_1 = " + trackBar_1.Value.ToString() + "\n";
            //richTextBox1.Text += "trackBar_0 = " + trackBar_0.Value.ToString() + "\n";

            //timer_start_point = trackBar_3.Value << 12 + trackBar_2.Value << 8 + trackBar_1.Value << 4 + trackBar_0.Value;
            timer_start_point = trackBar_3.Value * 4096 + trackBar_2.Value * 256 + trackBar_1.Value * 16 + trackBar_0.Value;

            //richTextBox1.Text += "T1 value = " + timer_start_point.ToString() + "\n";

            Send_Parameter_Cmd(_TIMER2, (timer_start_point >> 8) & 0xff, timer_start_point & 0xff);
            textBox_timer2.ForeColor = System.Drawing.Color.Black;
            tb_rpm.ForeColor = System.Drawing.Color.Black;
            tb_msec.ForeColor = System.Drawing.Color.Black;
            tb_msec2.ForeColor = System.Drawing.Color.Black;
        }

        private void button104_Click(object sender, EventArgs e)
        {
            control_3 = 3;          //PCA mode
            set_and_wait_response();
        }

        private void button106_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pca_duty = 0;
            pca_duty = (int)numericUpDown6.Value;
            Send_Parameter_Cmd(_PCA_DUTY, 0, pca_duty);
            tb_target_pca_duty.Text = pca_duty.ToString() + " (" + (pca_duty * 100 / 255).ToString() + " %)";
            tb_target_pca_duty.ForeColor = System.Drawing.Color.Black;
            numericUpDown6.ForeColor = System.Drawing.Color.Black;
        }

        private void button108_Click(object sender, EventArgs e)
        {
            control_7 = 1;          //use real hall
            set_and_wait_response();
        }

        private void button109_Click(object sender, EventArgs e)
        {
            control_7 = 0;          //use sensorless hall
            set_and_wait_response();
        }

        private void button105_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pca_duty = 0;
            int speed = 0;
            speed = (int)numericUpDown7.Value;
            if (speed < 10)
                pca_duty = 25 * speed;
            else if (speed == 10)
                pca_duty = 255;
            else
            {
                richTextBox1.Text += "數字不合法，abort....\n";
                return;
            }
            Send_Parameter_Cmd(_PCA_DUTY, 0, pca_duty);
            numericUpDown6.Value = pca_duty;
            tb_target_pca_duty.Text = pca_duty.ToString() + " (" + (pca_duty * 100 / 255).ToString() + " %)";
            tb_target_pca_duty.ForeColor = System.Drawing.Color.Black;
            numericUpDown7.ForeColor = System.Drawing.Color.Black;
        }

        private void numericUpDown6_ValueChanged(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pca_duty = 0;
            pca_duty = (int)numericUpDown6.Value;
            tb_target_pca_duty.Text = pca_duty.ToString() + " (" + (pca_duty * 100 / 255).ToString() + " %)";
            numericUpDown6.ForeColor = System.Drawing.Color.Red;
            numericUpDown7.ForeColor = System.Drawing.Color.Red;
            numericUpDown7.Value = pca_duty/25;
            tb_target_pca_duty.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown7_ValueChanged(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pca_duty = 0;
            int speed = 0;
            speed = (int)numericUpDown7.Value;
            if (speed < 10)
                pca_duty = 25 * speed;
            else if (speed == 10)
                pca_duty = 255;
            else
            {
                richTextBox1.Text += "數字不合法，abort....\n";
                return;
            }
            numericUpDown6.ForeColor = System.Drawing.Color.Red;
            numericUpDown7.ForeColor = System.Drawing.Color.Red;
            numericUpDown6.Value = pca_duty;
            tb_target_pca_duty.Text = pca_duty.ToString() + " (" + (pca_duty * 100 / 255).ToString() + " %)";
            tb_target_pca_duty.ForeColor = System.Drawing.Color.Red;
        }

        private void numericUpDown5_ValueChanged(object sender, EventArgs e)
        {
            numericUpDown5.ForeColor = System.Drawing.Color.Red;
        }

        public bool Send_Servo_Parameter_Cmd(int xx, int yy, int zz)
        {
            byte[] data = new byte[5];

            data[0] = 0xCD;
            data[1] = (byte)xx;
            data[2] = (byte)yy;
            data[3] = (byte)zz;
            //data[4] = CalcCheckSum(data, 4);
            data[4] = 0x0d;

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
                progressBar1.Value = 100;
            }
            else
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return false;
            }
            return true;
        }

        private void button89_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            int pulse_tolerance = 0;
            int vr_variation = 0;
            int vr_diff_tolerance = 0;
            string message = "";
            if (tb_pulse_tolerance.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else if (tb_vr_variation.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else if (tb_vr_diff_tolerance.Text.Length <= 0)
            {
                MessageBox.Show("資料不完整");
                return;
            }
            else
            {
                pulse_tolerance = int.Parse(tb_pulse_tolerance.Text);
                vr_variation = int.Parse(tb_vr_variation.Text);
                vr_diff_tolerance = int.Parse(tb_vr_diff_tolerance.Text);
                if (pulse_tolerance > 10)
                    MessageBox.Show("輸入資料錯誤，pulse_tolerance最大值為10。");
                else if (pulse_tolerance < 0)
                    MessageBox.Show("輸入資料錯誤，pulse_tolerance最小值為0。");
                else if (vr_variation > 10)
                    MessageBox.Show("輸入資料錯誤，vr_variation最大值為10。");
                else if (vr_variation < 0)
                    MessageBox.Show("輸入資料錯誤，vr_variation最小值為0。");
                else if (vr_diff_tolerance > 10)
                    MessageBox.Show("輸入資料錯誤，vr_diff_tolerance最大值為10。");
                else if (vr_diff_tolerance < 0)
                    MessageBox.Show("輸入資料錯誤，vr_diff_tolerance最小值為0。");
                else
                {
                    Send_Servo_Parameter_Cmd(pulse_tolerance, vr_variation, vr_diff_tolerance);
                    message += "[PC] Send data =  ";
                    message += pulse_tolerance.ToString() + " ";
                    message += vr_variation.ToString() + " ";
                    message += vr_diff_tolerance.ToString();
                    message += "\n";
                    richTextBox1.AppendText(message);
                    richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                }
            }

        }

        private void button107_Click(object sender, EventArgs e)
        {
            Send_Servo_Parameter_Cmd(0xff, 0, 0);
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

        private void button110_Click(object sender, EventArgs e)
        {
            //開啟Form3表單
            Form3 Form_AnalogClock = new Form3();
            Form_AnalogClock.Show();
        }

        private void button113_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 start command
            Send_Parameter_Cmd(_TIMER2 | 0xE0, 0, 0);
        }

        private void button114_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 stop command
            Send_Parameter_Cmd(_TIMER2 | 0x80, 0, 0);
        }

        private void button111_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 +0x10
            Send_Parameter_Cmd(_TIMER2 | 0xC0, 0, 0);
        }

        private void button112_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 -0x10
            Send_Parameter_Cmd(_TIMER2 | 0xA0, 0, 0);
        }

        private void button115_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 +0x01
            Send_Parameter_Cmd(_TIMER2 | 0x60, 0, 0);
        }

        private void button116_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            //Send Timer2 -0x01
            Send_Parameter_Cmd(_TIMER2 | 0x40, 0, 0);
        }

        byte cnt = 0;
        byte DongleAddr_h;
        byte DongleAddr_l;
        byte DongleData;
        byte xx;
        byte yy;
        byte zz;

        private void button118_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 1;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
        }

        private void button117_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 0;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt << 2));
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


        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt++;
            cnt %= 4;
            
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;

            DongleData = (byte)(0x10 | (cnt << 2));

            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 
            



        }

        private void button119_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 2;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt << 2));
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData); 

        }

        private void button120_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 3;
            DongleAddr_h = 0x38;
            DongleAddr_l = 0x20;
            DongleData = (byte)(0x10 | (cnt << 2));
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
                cnt = 0;
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
            cnt = 1;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button127_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 2;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);

        }

        private void button126_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 3;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button125_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 4;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt + 128);
            Send_IMS_Data(0xA0, DongleAddr_h, DongleAddr_l, DongleData);
        }

        private void button129_Click(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                MessageBox.Show("No Comport", "imsLink", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            cnt = 0;
            DongleAddr_h = 0x50;
            DongleAddr_l = 0x80;
            DongleData = (byte)(cnt + 0);
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


    }
}

