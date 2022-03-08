namespace my_vcs_16_pwm
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.button3 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.button7 = new System.Windows.Forms.Button();
            this.SerialPortTimer100ms = new System.Windows.Forms.Timer(this.components);
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.button10 = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1_ADC = new System.Windows.Forms.TabPage();
            this.tabPage2_DAC = new System.Windows.Forms.TabPage();
            this.button15 = new System.Windows.Forms.Button();
            this.textBox5 = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button14 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.button12 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.comboBox3 = new System.Windows.Forms.ComboBox();
            this.tabPage3_CMP = new System.Windows.Forms.TabPage();
            this.tabPage4_PWM = new System.Windows.Forms.TabPage();
            this.label19 = new System.Windows.Forms.Label();
            this.comboBox_n_invert = new System.Windows.Forms.ComboBox();
            this.label18 = new System.Windows.Forms.Label();
            this.button18 = new System.Windows.Forms.Button();
            this.comboBox_p_invert = new System.Windows.Forms.ComboBox();
            this.label17 = new System.Windows.Forms.Label();
            this.numericUpDown_dt = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown_duty = new System.Windows.Forms.NumericUpDown();
            this.tb_pwm_freq_hz = new System.Windows.Forms.TextBox();
            this.tb_pwm_period_us = new System.Windows.Forms.TextBox();
            this.tb_pwm_period_point = new System.Windows.Forms.TextBox();
            this.button17 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.label16 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.cb_CN = new System.Windows.Forms.CheckBox();
            this.cb_CP = new System.Windows.Forms.CheckBox();
            this.cb_BN = new System.Windows.Forms.CheckBox();
            this.cb_BP = new System.Windows.Forms.CheckBox();
            this.cb_AN = new System.Windows.Forms.CheckBox();
            this.cb_AP = new System.Windows.Forms.CheckBox();
            this.tabPage5_Timer = new System.Windows.Forms.TabPage();
            this.tabPage8_PCA = new System.Windows.Forms.TabPage();
            this.tabPage9_GPIO = new System.Windows.Forms.TabPage();
            this.tabPage7_About = new System.Windows.Forms.TabPage();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.label13 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.tabControl1.SuspendLayout();
            this.tabPage1_ADC.SuspendLayout();
            this.tabPage2_DAC.SuspendLayout();
            this.tabPage4_PWM.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_dt)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_duty)).BeginInit();
            this.tabPage7_About.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(369, 29);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(81, 33);
            this.button1.TabIndex = 0;
            this.button1.Text = "Connect";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(467, 28);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(81, 33);
            this.button2.TabIndex = 1;
            this.button2.Text = "Disconnect";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.Color.Black;
            this.richTextBox1.Font = new System.Drawing.Font("Courier New", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextBox1.ForeColor = System.Drawing.Color.White;
            this.richTextBox1.Location = new System.Drawing.Point(12, 299);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(777, 473);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            this.richTextBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.richTextBox1_KeyPress);
            // 
            // serialPort1
            // 
            this.serialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // button3
            // 
            this.button3.BackColor = System.Drawing.Color.Black;
            this.button3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.ForeColor = System.Drawing.Color.White;
            this.button3.Location = new System.Drawing.Point(11, 21);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(109, 33);
            this.button3.TabIndex = 4;
            this.button3.Text = "Initial ADC";
            this.button3.UseVisualStyleBackColor = false;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(27, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(80, 21);
            this.label1.TabIndex = 6;
            this.label1.Text = "Comport";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(171, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 21);
            this.label2.TabIndex = 7;
            this.label2.Text = "Baud";
            // 
            // button4
            // 
            this.button4.BackColor = System.Drawing.Color.Black;
            this.button4.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button4.ForeColor = System.Drawing.Color.White;
            this.button4.Location = new System.Drawing.Point(142, 21);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(109, 33);
            this.button4.TabIndex = 8;
            this.button4.Text = "Disable ADC";
            this.button4.UseVisualStyleBackColor = false;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.BackColor = System.Drawing.Color.Black;
            this.button5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button5.ForeColor = System.Drawing.Color.White;
            this.button5.Location = new System.Drawing.Point(266, 21);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(109, 33);
            this.button5.TabIndex = 9;
            this.button5.Text = "Read";
            this.button5.UseVisualStyleBackColor = false;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.BackColor = System.Drawing.Color.Black;
            this.button6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.ForeColor = System.Drawing.Color.White;
            this.button6.Location = new System.Drawing.Point(400, 21);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(109, 33);
            this.button6.TabIndex = 10;
            this.button6.Text = "Stop";
            this.button6.UseVisualStyleBackColor = false;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // textBox3
            // 
            this.textBox3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox3.Location = new System.Drawing.Point(142, 94);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(109, 30);
            this.textBox3.TabIndex = 11;
            this.textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox4
            // 
            this.textBox4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox4.Location = new System.Drawing.Point(400, 94);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(112, 30);
            this.textBox4.TabIndex = 12;
            this.textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(76, 97);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 19);
            this.label3.TabIndex = 13;
            this.label3.Text = "ADC";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(328, 97);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(66, 19);
            this.label4.TabIndex = 14;
            this.label4.Text = "Voltage";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(518, 97);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(36, 19);
            this.label5.TabIndex = 15;
            this.label5.Text = "mV";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(708, 270);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(75, 23);
            this.button7.TabIndex = 16;
            this.button7.Text = "clear";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // SerialPortTimer100ms
            // 
            this.SerialPortTimer100ms.Enabled = true;
            this.SerialPortTimer100ms.Tick += new System.EventHandler(this.SerialPortTimer100ms_Tick);
            // 
            // button8
            // 
            this.button8.BackColor = System.Drawing.Color.Red;
            this.button8.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button8.Location = new System.Drawing.Point(674, 29);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(109, 33);
            this.button8.TabIndex = 17;
            this.button8.Text = "說明";
            this.button8.UseVisualStyleBackColor = false;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button9
            // 
            this.button9.BackColor = System.Drawing.Color.Black;
            this.button9.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button9.ForeColor = System.Drawing.Color.White;
            this.button9.Location = new System.Drawing.Point(572, 29);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(81, 33);
            this.button9.TabIndex = 18;
            this.button9.Text = "Reset";
            this.button9.UseVisualStyleBackColor = false;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // comboBox1
            // 
            this.comboBox1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(15, 33);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(109, 24);
            this.comboBox1.TabIndex = 19;
            // 
            // comboBox2
            // 
            this.comboBox2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Items.AddRange(new object[] {
            "9600",
            "19600",
            "115200"});
            this.comboBox2.Location = new System.Drawing.Point(146, 33);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(109, 24);
            this.comboBox2.TabIndex = 20;
            this.comboBox2.Text = "9600";
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(272, 29);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(81, 33);
            this.button10.TabIndex = 21;
            this.button10.Text = "COM Scan";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1_ADC);
            this.tabControl1.Controls.Add(this.tabPage2_DAC);
            this.tabControl1.Controls.Add(this.tabPage3_CMP);
            this.tabControl1.Controls.Add(this.tabPage4_PWM);
            this.tabControl1.Controls.Add(this.tabPage5_Timer);
            this.tabControl1.Controls.Add(this.tabPage8_PCA);
            this.tabControl1.Controls.Add(this.tabPage9_GPIO);
            this.tabControl1.Controls.Add(this.tabPage7_About);
            this.tabControl1.Location = new System.Drawing.Point(15, 67);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(774, 197);
            this.tabControl1.TabIndex = 22;
            // 
            // tabPage1_ADC
            // 
            this.tabPage1_ADC.Controls.Add(this.button4);
            this.tabPage1_ADC.Controls.Add(this.button3);
            this.tabPage1_ADC.Controls.Add(this.button5);
            this.tabPage1_ADC.Controls.Add(this.button6);
            this.tabPage1_ADC.Controls.Add(this.textBox3);
            this.tabPage1_ADC.Controls.Add(this.textBox4);
            this.tabPage1_ADC.Controls.Add(this.label3);
            this.tabPage1_ADC.Controls.Add(this.label5);
            this.tabPage1_ADC.Controls.Add(this.label4);
            this.tabPage1_ADC.Location = new System.Drawing.Point(4, 22);
            this.tabPage1_ADC.Name = "tabPage1_ADC";
            this.tabPage1_ADC.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1_ADC.Size = new System.Drawing.Size(766, 171);
            this.tabPage1_ADC.TabIndex = 0;
            this.tabPage1_ADC.Text = "ADC";
            this.tabPage1_ADC.UseVisualStyleBackColor = true;
            // 
            // tabPage2_DAC
            // 
            this.tabPage2_DAC.Controls.Add(this.button15);
            this.tabPage2_DAC.Controls.Add(this.textBox5);
            this.tabPage2_DAC.Controls.Add(this.textBox1);
            this.tabPage2_DAC.Controls.Add(this.button14);
            this.tabPage2_DAC.Controls.Add(this.button13);
            this.tabPage2_DAC.Controls.Add(this.label8);
            this.tabPage2_DAC.Controls.Add(this.label7);
            this.tabPage2_DAC.Controls.Add(this.button12);
            this.tabPage2_DAC.Controls.Add(this.button11);
            this.tabPage2_DAC.Controls.Add(this.label6);
            this.tabPage2_DAC.Controls.Add(this.comboBox3);
            this.tabPage2_DAC.Location = new System.Drawing.Point(4, 22);
            this.tabPage2_DAC.Name = "tabPage2_DAC";
            this.tabPage2_DAC.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2_DAC.Size = new System.Drawing.Size(766, 171);
            this.tabPage2_DAC.TabIndex = 1;
            this.tabPage2_DAC.Text = "DAC";
            this.tabPage2_DAC.UseVisualStyleBackColor = true;
            // 
            // button15
            // 
            this.button15.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button15.Location = new System.Drawing.Point(662, 15);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(84, 34);
            this.button15.TabIndex = 11;
            this.button15.Text = "展示";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // textBox5
            // 
            this.textBox5.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox5.Location = new System.Drawing.Point(225, 124);
            this.textBox5.MaxLength = 4;
            this.textBox5.Name = "textBox5";
            this.textBox5.Size = new System.Drawing.Size(89, 36);
            this.textBox5.TabIndex = 10;
            this.textBox5.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.textBox5.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox5_KeyPress);
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(225, 65);
            this.textBox1.MaxLength = 3;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(89, 36);
            this.textBox1.TabIndex = 8;
            this.textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.textBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
            // 
            // button14
            // 
            this.button14.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button14.Location = new System.Drawing.Point(443, 122);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(84, 34);
            this.button14.TabIndex = 7;
            this.button14.Text = "確定";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button13
            // 
            this.button13.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button13.Location = new System.Drawing.Point(443, 67);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(84, 34);
            this.button13.TabIndex = 6;
            this.button13.Text = "確定";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(33, 129);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(405, 21);
            this.label8.TabIndex = 5;
            this.label8.Text = "設定DAC電壓：                            mV (0~5000)";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(33, 70);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(355, 21);
            this.label7.TabIndex = 4;
            this.label7.Text = "設定DAC數值： 0x                       (0~3ff)";
            // 
            // button12
            // 
            this.button12.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button12.Location = new System.Drawing.Point(553, 15);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(84, 34);
            this.button12.TabIndex = 3;
            this.button12.Text = "停用";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button11
            // 
            this.button11.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button11.Location = new System.Drawing.Point(443, 15);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(84, 34);
            this.button11.TabIndex = 2;
            this.button11.Text = "啟用";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(30, 15);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(198, 21);
            this.label6.TabIndex = 1;
            this.label6.Text = "選取DAC輸出接腳：";
            // 
            // comboBox3
            // 
            this.comboBox3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox3.FormattingEnabled = true;
            this.comboBox3.Items.AddRange(new object[] {
            "pin01_P1.7",
            "pin23_P3.2",
            "pin29_P2.2"});
            this.comboBox3.Location = new System.Drawing.Point(225, 13);
            this.comboBox3.Name = "comboBox3";
            this.comboBox3.Size = new System.Drawing.Size(204, 32);
            this.comboBox3.TabIndex = 0;
            // 
            // tabPage3_CMP
            // 
            this.tabPage3_CMP.Location = new System.Drawing.Point(4, 22);
            this.tabPage3_CMP.Name = "tabPage3_CMP";
            this.tabPage3_CMP.Size = new System.Drawing.Size(766, 171);
            this.tabPage3_CMP.TabIndex = 2;
            this.tabPage3_CMP.Text = "CMP";
            this.tabPage3_CMP.UseVisualStyleBackColor = true;
            // 
            // tabPage4_PWM
            // 
            this.tabPage4_PWM.Controls.Add(this.label19);
            this.tabPage4_PWM.Controls.Add(this.comboBox_n_invert);
            this.tabPage4_PWM.Controls.Add(this.label18);
            this.tabPage4_PWM.Controls.Add(this.button18);
            this.tabPage4_PWM.Controls.Add(this.comboBox_p_invert);
            this.tabPage4_PWM.Controls.Add(this.label17);
            this.tabPage4_PWM.Controls.Add(this.numericUpDown_dt);
            this.tabPage4_PWM.Controls.Add(this.numericUpDown_duty);
            this.tabPage4_PWM.Controls.Add(this.tb_pwm_freq_hz);
            this.tabPage4_PWM.Controls.Add(this.tb_pwm_period_us);
            this.tabPage4_PWM.Controls.Add(this.tb_pwm_period_point);
            this.tabPage4_PWM.Controls.Add(this.button17);
            this.tabPage4_PWM.Controls.Add(this.button16);
            this.tabPage4_PWM.Controls.Add(this.label16);
            this.tabPage4_PWM.Controls.Add(this.label15);
            this.tabPage4_PWM.Controls.Add(this.label14);
            this.tabPage4_PWM.Controls.Add(this.cb_CN);
            this.tabPage4_PWM.Controls.Add(this.cb_CP);
            this.tabPage4_PWM.Controls.Add(this.cb_BN);
            this.tabPage4_PWM.Controls.Add(this.cb_BP);
            this.tabPage4_PWM.Controls.Add(this.cb_AN);
            this.tabPage4_PWM.Controls.Add(this.cb_AP);
            this.tabPage4_PWM.Location = new System.Drawing.Point(4, 22);
            this.tabPage4_PWM.Name = "tabPage4_PWM";
            this.tabPage4_PWM.Size = new System.Drawing.Size(766, 171);
            this.tabPage4_PWM.TabIndex = 3;
            this.tabPage4_PWM.Text = "PWM";
            this.tabPage4_PWM.UseVisualStyleBackColor = true;
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label19.Location = new System.Drawing.Point(484, 132);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(32, 19);
            this.label19.TabIndex = 35;
            this.label19.Text = "N :";
            // 
            // comboBox_n_invert
            // 
            this.comboBox_n_invert.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_n_invert.FormattingEnabled = true;
            this.comboBox_n_invert.Items.AddRange(new object[] {
            "不反相",
            "反相"});
            this.comboBox_n_invert.Location = new System.Drawing.Point(519, 125);
            this.comboBox_n_invert.Name = "comboBox_n_invert";
            this.comboBox_n_invert.Size = new System.Drawing.Size(103, 32);
            this.comboBox_n_invert.TabIndex = 34;
            this.comboBox_n_invert.Text = "不反相";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label18.Location = new System.Drawing.Point(484, 79);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(29, 19);
            this.label18.TabIndex = 33;
            this.label18.Text = "P :";
            // 
            // button18
            // 
            this.button18.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button18.Location = new System.Drawing.Point(644, 78);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(108, 33);
            this.button18.TabIndex = 32;
            this.button18.Text = "關閉";
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // comboBox_p_invert
            // 
            this.comboBox_p_invert.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.comboBox_p_invert.FormattingEnabled = true;
            this.comboBox_p_invert.Items.AddRange(new object[] {
            "不反相",
            "反相"});
            this.comboBox_p_invert.Location = new System.Drawing.Point(519, 72);
            this.comboBox_p_invert.Name = "comboBox_p_invert";
            this.comboBox_p_invert.Size = new System.Drawing.Size(103, 32);
            this.comboBox_p_invert.TabIndex = 31;
            this.comboBox_p_invert.Text = "不反相";
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label17.Location = new System.Drawing.Point(458, 20);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(91, 19);
            this.label17.TabIndex = 30;
            this.label17.Text = "PWM DT :";
            // 
            // numericUpDown_dt
            // 
            this.numericUpDown_dt.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown_dt.Location = new System.Drawing.Point(555, 12);
            this.numericUpDown_dt.Maximum = new decimal(new int[] {
            31,
            0,
            0,
            0});
            this.numericUpDown_dt.Name = "numericUpDown_dt";
            this.numericUpDown_dt.Size = new System.Drawing.Size(67, 36);
            this.numericUpDown_dt.TabIndex = 29;
            this.numericUpDown_dt.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDown_dt.Value = new decimal(new int[] {
            8,
            0,
            0,
            0});
            // 
            // numericUpDown_duty
            // 
            this.numericUpDown_duty.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown_duty.Location = new System.Drawing.Point(265, 128);
            this.numericUpDown_duty.Name = "numericUpDown_duty";
            this.numericUpDown_duty.Size = new System.Drawing.Size(67, 36);
            this.numericUpDown_duty.TabIndex = 28;
            this.numericUpDown_duty.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDown_duty.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            // 
            // tb_pwm_freq_hz
            // 
            this.tb_pwm_freq_hz.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_pwm_freq_hz.Location = new System.Drawing.Point(264, 15);
            this.tb_pwm_freq_hz.Name = "tb_pwm_freq_hz";
            this.tb_pwm_freq_hz.Size = new System.Drawing.Size(81, 33);
            this.tb_pwm_freq_hz.TabIndex = 27;
            this.tb_pwm_freq_hz.Text = "20000";
            this.tb_pwm_freq_hz.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.tb_pwm_freq_hz.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tb_pwm_freq_hz_KeyDown);
            // 
            // tb_pwm_period_us
            // 
            this.tb_pwm_period_us.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_pwm_period_us.Location = new System.Drawing.Point(362, 71);
            this.tb_pwm_period_us.Name = "tb_pwm_period_us";
            this.tb_pwm_period_us.Size = new System.Drawing.Size(81, 33);
            this.tb_pwm_period_us.TabIndex = 26;
            this.tb_pwm_period_us.Text = "50";
            this.tb_pwm_period_us.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.tb_pwm_period_us.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tb_pwm_period_us_KeyDown);
            // 
            // tb_pwm_period_point
            // 
            this.tb_pwm_period_point.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_pwm_period_point.Location = new System.Drawing.Point(264, 71);
            this.tb_pwm_period_point.Name = "tb_pwm_period_point";
            this.tb_pwm_period_point.Size = new System.Drawing.Size(81, 33);
            this.tb_pwm_period_point.TabIndex = 25;
            this.tb_pwm_period_point.Text = "400";
            this.tb_pwm_period_point.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.tb_pwm_period_point.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tb_pwm_period_point_KeyDown);
            // 
            // button17
            // 
            this.button17.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button17.Location = new System.Drawing.Point(644, 32);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(108, 33);
            this.button17.TabIndex = 24;
            this.button17.Text = "初始化";
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // button16
            // 
            this.button16.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button16.Location = new System.Drawing.Point(644, 125);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(108, 33);
            this.button16.TabIndex = 23;
            this.button16.Text = "套用";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label16.Location = new System.Drawing.Point(148, 133);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(103, 19);
            this.label16.TabIndex = 8;
            this.label16.Text = "PWM Duty :";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label15.Location = new System.Drawing.Point(148, 78);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(320, 19);
            this.label15.TabIndex = 7;
            this.label15.Text = "PWM Period :                  =                  us";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label14.Location = new System.Drawing.Point(148, 20);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(231, 19);
            this.label14.TabIndex = 6;
            this.label14.Text = "PWM Freq :                      Hz";
            // 
            // cb_CN
            // 
            this.cb_CN.AutoSize = true;
            this.cb_CN.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_CN.Location = new System.Drawing.Point(39, 145);
            this.cb_CN.Name = "cb_CN";
            this.cb_CN.Size = new System.Drawing.Size(96, 23);
            this.cb_CN.TabIndex = 5;
            this.cb_CN.Text = "PWMCN";
            this.cb_CN.UseVisualStyleBackColor = true;
            // 
            // cb_CP
            // 
            this.cb_CP.AutoSize = true;
            this.cb_CP.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_CP.Location = new System.Drawing.Point(39, 119);
            this.cb_CP.Name = "cb_CP";
            this.cb_CP.Size = new System.Drawing.Size(93, 23);
            this.cb_CP.TabIndex = 4;
            this.cb_CP.Text = "PWMCP";
            this.cb_CP.UseVisualStyleBackColor = true;
            // 
            // cb_BN
            // 
            this.cb_BN.AutoSize = true;
            this.cb_BN.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_BN.Location = new System.Drawing.Point(39, 90);
            this.cb_BN.Name = "cb_BN";
            this.cb_BN.Size = new System.Drawing.Size(96, 23);
            this.cb_BN.TabIndex = 3;
            this.cb_BN.Text = "PWMBN";
            this.cb_BN.UseVisualStyleBackColor = true;
            // 
            // cb_BP
            // 
            this.cb_BP.AutoSize = true;
            this.cb_BP.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_BP.Location = new System.Drawing.Point(39, 61);
            this.cb_BP.Name = "cb_BP";
            this.cb_BP.Size = new System.Drawing.Size(93, 23);
            this.cb_BP.TabIndex = 2;
            this.cb_BP.Text = "PWMBP";
            this.cb_BP.UseVisualStyleBackColor = true;
            // 
            // cb_AN
            // 
            this.cb_AN.AutoSize = true;
            this.cb_AN.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_AN.Location = new System.Drawing.Point(39, 32);
            this.cb_AN.Name = "cb_AN";
            this.cb_AN.Size = new System.Drawing.Size(97, 23);
            this.cb_AN.TabIndex = 1;
            this.cb_AN.Text = "PWMAN";
            this.cb_AN.UseVisualStyleBackColor = true;
            // 
            // cb_AP
            // 
            this.cb_AP.AutoSize = true;
            this.cb_AP.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_AP.Location = new System.Drawing.Point(39, 3);
            this.cb_AP.Name = "cb_AP";
            this.cb_AP.Size = new System.Drawing.Size(94, 23);
            this.cb_AP.TabIndex = 0;
            this.cb_AP.Text = "PWMAP";
            this.cb_AP.UseVisualStyleBackColor = true;
            // 
            // tabPage5_Timer
            // 
            this.tabPage5_Timer.Location = new System.Drawing.Point(4, 22);
            this.tabPage5_Timer.Name = "tabPage5_Timer";
            this.tabPage5_Timer.Size = new System.Drawing.Size(766, 171);
            this.tabPage5_Timer.TabIndex = 4;
            this.tabPage5_Timer.Text = "Timer";
            this.tabPage5_Timer.UseVisualStyleBackColor = true;
            // 
            // tabPage8_PCA
            // 
            this.tabPage8_PCA.Location = new System.Drawing.Point(4, 22);
            this.tabPage8_PCA.Name = "tabPage8_PCA";
            this.tabPage8_PCA.Size = new System.Drawing.Size(766, 171);
            this.tabPage8_PCA.TabIndex = 7;
            this.tabPage8_PCA.Text = "PCA";
            this.tabPage8_PCA.UseVisualStyleBackColor = true;
            // 
            // tabPage9_GPIO
            // 
            this.tabPage9_GPIO.Location = new System.Drawing.Point(4, 22);
            this.tabPage9_GPIO.Name = "tabPage9_GPIO";
            this.tabPage9_GPIO.Size = new System.Drawing.Size(766, 171);
            this.tabPage9_GPIO.TabIndex = 8;
            this.tabPage9_GPIO.Text = "GPIO";
            this.tabPage9_GPIO.UseVisualStyleBackColor = true;
            // 
            // tabPage7_About
            // 
            this.tabPage7_About.Controls.Add(this.linkLabel1);
            this.tabPage7_About.Controls.Add(this.label13);
            this.tabPage7_About.Controls.Add(this.label12);
            this.tabPage7_About.Controls.Add(this.label11);
            this.tabPage7_About.Controls.Add(this.label10);
            this.tabPage7_About.Controls.Add(this.label9);
            this.tabPage7_About.Controls.Add(this.pictureBox1);
            this.tabPage7_About.Location = new System.Drawing.Point(4, 22);
            this.tabPage7_About.Name = "tabPage7_About";
            this.tabPage7_About.Size = new System.Drawing.Size(766, 171);
            this.tabPage7_About.TabIndex = 6;
            this.tabPage7_About.Text = "About";
            this.tabPage7_About.UseVisualStyleBackColor = true;
            // 
            // linkLabel1
            // 
            this.linkLabel1.AutoSize = true;
            this.linkLabel1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.linkLabel1.LinkArea = new System.Windows.Forms.LinkArea(6, 24);
            this.linkLabel1.Location = new System.Drawing.Point(351, 144);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(296, 31);
            this.linkLabel1.TabIndex = 6;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Text = "網址:   http://www.myson.com.tw/";
            this.linkLabel1.UseCompatibleTextRendering = true;
            this.linkLabel1.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label13.Location = new System.Drawing.Point(351, 117);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(245, 21);
            this.label13.TabIndex = 5;
            this.label13.Text = "信箱:   sales@myson.com.tw";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label12.Location = new System.Drawing.Point(351, 90);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(413, 21);
            this.label12.TabIndex = 4;
            this.label12.Text = "地址:   新竹市科學園區工業東四路24-2號2樓";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label11.Location = new System.Drawing.Point(351, 65);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(181, 21);
            this.label11.TabIndex = 3;
            this.label11.Text = "傳真:   (03) 5785002";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label10.Location = new System.Drawing.Point(351, 38);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(181, 21);
            this.label10.TabIndex = 2;
            this.label10.Text = "電話:   (03) 5784866";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("微軟正黑體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.ForeColor = System.Drawing.Color.Navy;
            this.label9.Location = new System.Drawing.Point(348, 6);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(302, 31);
            this.label9.TabIndex = 1;
            this.label9.Text = "世紀民生科技股份有限公司";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(13, 45);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(334, 112);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(795, 742);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1_ADC.ResumeLayout(false);
            this.tabPage1_ADC.PerformLayout();
            this.tabPage2_DAC.ResumeLayout(false);
            this.tabPage2_DAC.PerformLayout();
            this.tabPage4_PWM.ResumeLayout(false);
            this.tabPage4_PWM.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_dt)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_duty)).EndInit();
            this.tabPage7_About.ResumeLayout(false);
            this.tabPage7_About.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Timer SerialPortTimer100ms;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1_ADC;
        private System.Windows.Forms.TabPage tabPage2_DAC;
        private System.Windows.Forms.TabPage tabPage3_CMP;
        private System.Windows.Forms.TabPage tabPage4_PWM;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.ComboBox comboBox3;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.TabPage tabPage5_Timer;
        private System.Windows.Forms.TabPage tabPage7_About;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.LinkLabel linkLabel1;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TabPage tabPage8_PCA;
        private System.Windows.Forms.TabPage tabPage9_GPIO;
        private System.Windows.Forms.NumericUpDown numericUpDown_duty;
        private System.Windows.Forms.TextBox tb_pwm_freq_hz;
        private System.Windows.Forms.TextBox tb_pwm_period_us;
        private System.Windows.Forms.TextBox tb_pwm_period_point;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.CheckBox cb_CN;
        private System.Windows.Forms.CheckBox cb_CP;
        private System.Windows.Forms.CheckBox cb_BN;
        private System.Windows.Forms.CheckBox cb_BP;
        private System.Windows.Forms.CheckBox cb_AN;
        private System.Windows.Forms.CheckBox cb_AP;
        private System.Windows.Forms.ComboBox comboBox_p_invert;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.NumericUpDown numericUpDown_dt;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.ComboBox comboBox_n_invert;
        private System.Windows.Forms.Label label18;
    }
}

