
namespace Bottom_Control
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.daConduit1 = new Bottom_Control.基本控件.DAConduit();
            this.daBottle1 = new Bottom_Control.基本控件.DABottle();
            this.daPond1 = new Bottom_Control.基本控件.DAPond();
            this.daConveyor1 = new Bottom_Control.基本控件.DAConveyor();
            this.daAnalogMeter1 = new Bottom_Control.基本控件.DAAnalogMeter();
            this.daProcessWave1 = new Bottom_Control.基本控件.DAProcessWave();
            this.daMeter1 = new Bottom_Control.基本控件.DAMeter();
            this.daSwitch1 = new Bottom_Control.基本控件.DASwitch();
            this.daProcessEllipse1 = new Bottom_Control.基本控件.DAProcessEllipse();
            this.daSignalLamp1 = new Bottom_Control.基本控件.DASignalLamp();
            this.daThermometer1 = new Bottom_Control.基本控件.DAThermometer();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.daRotor1 = new Bottom_Control.基本控件.DARotor();
            this.daAlarmLamp1 = new Bottom_Control.基本控件.DAAlarmLamp();
            this.daLedBulb1 = new Bottom_Control.基本控件.DALedBulb();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(1096, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(199, 680);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 200;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Location = new System.Drawing.Point(10, 10);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(1078, 668);
            this.tabControl1.TabIndex = 12;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.daLedBulb1);
            this.tabPage1.Controls.Add(this.daAlarmLamp1);
            this.tabPage1.Controls.Add(this.daConduit1);
            this.tabPage1.Controls.Add(this.daBottle1);
            this.tabPage1.Controls.Add(this.daPond1);
            this.tabPage1.Controls.Add(this.daConveyor1);
            this.tabPage1.Controls.Add(this.daAnalogMeter1);
            this.tabPage1.Controls.Add(this.daProcessWave1);
            this.tabPage1.Controls.Add(this.daMeter1);
            this.tabPage1.Controls.Add(this.daSwitch1);
            this.tabPage1.Controls.Add(this.daProcessEllipse1);
            this.tabPage1.Controls.Add(this.daSignalLamp1);
            this.tabPage1.Controls.Add(this.daThermometer1);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(1070, 642);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "控件使用";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // daConduit1
            // 
            this.daConduit1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daConduit1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daConduit1.ConduitColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daConduit1.ConduitStyle = HZH_Controls.Controls.ConduitStyle.Horizontal_None_None;
            this.daConduit1.ConduitWidth = 50;
            this.daConduit1.LiquidColor = System.Drawing.Color.FromArgb(((int)(((byte)(3)))), ((int)(((byte)(169)))), ((int)(((byte)(243)))));
            this.daConduit1.LiquidDirection = HZH_Controls.Controls.LiquidDirection.Forward;
            this.daConduit1.LiquidSpeed = 100;
            this.daConduit1.Location = new System.Drawing.Point(18, 173);
            this.daConduit1.Name = "daConduit1";
            this.daConduit1.Pattern = Bottom_Control.Button_pattern.Regression;
            this.daConduit1.PLC_Address = "0";
            this.daConduit1.PLC_Contact = "X";
            this.daConduit1.PLC_Enable = false;
            this.daConduit1.Size = new System.Drawing.Size(300, 50);
            this.daConduit1.TabIndex = 14;
            // 
            // daBottle1
            // 
            this.daBottle1.BottleColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daBottle1.BottleMouthColor = System.Drawing.Color.FromArgb(((int)(((byte)(105)))), ((int)(((byte)(105)))), ((int)(((byte)(105)))));
            this.daBottle1.Control_Text = "50";
            this.daBottle1.Direction = HZH_Controls.Controls.Direction.Down;
            this.daBottle1.LiquidColor = System.Drawing.Color.FromArgb(((int)(((byte)(3)))), ((int)(((byte)(169)))), ((int)(((byte)(243)))));
            this.daBottle1.Location = new System.Drawing.Point(218, 418);
            this.daBottle1.MaxValue = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.daBottle1.Name = "daBottle1";
            this.daBottle1.NO = null;
            this.daBottle1.PLC_Address = "0";
            this.daBottle1.PLC_Contact = "D";
            this.daBottle1.PLC_Enable = false;
            this.daBottle1.Size = new System.Drawing.Size(100, 150);
            this.daBottle1.TabIndex = 13;
            this.daBottle1.Title = "瓶子1";
            this.daBottle1.Value = new decimal(new int[] {
            50,
            0,
            0,
            0});
            // 
            // daPond1
            // 
            this.daPond1.Control_Text = "0";
            this.daPond1.LiquidColor = System.Drawing.Color.FromArgb(((int)(((byte)(3)))), ((int)(((byte)(169)))), ((int)(((byte)(243)))));
            this.daPond1.Location = new System.Drawing.Point(18, 472);
            this.daPond1.MaxValue = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.daPond1.Name = "daPond1";
            this.daPond1.PLC_Address = "0";
            this.daPond1.PLC_Contact = "D";
            this.daPond1.PLC_Enable = false;
            this.daPond1.Size = new System.Drawing.Size(150, 50);
            this.daPond1.TabIndex = 12;
            this.daPond1.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
            this.daPond1.WallColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daPond1.WallWidth = 2;
            // 
            // daConveyor1
            // 
            this.daConveyor1.ConveyorColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daConveyor1.ConveyorDirection = HZH_Controls.Controls.ConveyorDirection.Forward;
            this.daConveyor1.ConveyorHeight = 50;
            this.daConveyor1.ConveyorSpeed = 100;
            this.daConveyor1.Inclination = 0D;
            this.daConveyor1.Location = new System.Drawing.Point(18, 98);
            this.daConveyor1.Name = "daConveyor1";
            this.daConveyor1.Size = new System.Drawing.Size(300, 50);
            this.daConveyor1.TabIndex = 5;
            // 
            // daAnalogMeter1
            // 
            this.daAnalogMeter1.BackColor = System.Drawing.Color.White;
            this.daAnalogMeter1.BodyColor = System.Drawing.Color.Silver;
            this.daAnalogMeter1.Control_Text = "0";
            this.daAnalogMeter1.Font = new System.Drawing.Font("微软雅黑", 12F);
            this.daAnalogMeter1.ForeColor = System.Drawing.Color.White;
            this.daAnalogMeter1.Location = new System.Drawing.Point(493, 34);
            this.daAnalogMeter1.MaxValue = 100D;
            this.daAnalogMeter1.MinValue = 0D;
            this.daAnalogMeter1.Name = "daAnalogMeter1";
            this.daAnalogMeter1.NeedleColor = System.Drawing.Color.YellowGreen;
            this.daAnalogMeter1.PLC_Address = "0";
            this.daAnalogMeter1.PLC_Contact = "D";
            this.daAnalogMeter1.PLC_Enable = false;
            this.daAnalogMeter1.Renderer = null;
            this.daAnalogMeter1.ScaleColor = System.Drawing.Color.Black;
            this.daAnalogMeter1.Size = new System.Drawing.Size(180, 180);
            this.daAnalogMeter1.Style = Sunny.UI.UIStyle.Custom;
            this.daAnalogMeter1.TabIndex = 11;
            this.daAnalogMeter1.Text = "daAnalogMeter1";
            this.daAnalogMeter1.Value = 0D;
            // 
            // daProcessWave1
            // 
            this.daProcessWave1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(228)))), ((int)(((byte)(231)))), ((int)(((byte)(237)))));
            this.daProcessWave1.ConerRadius = 0;
            this.daProcessWave1.Control_Text = "0";
            this.daProcessWave1.FillColor = System.Drawing.Color.Empty;
            this.daProcessWave1.Font = new System.Drawing.Font("微软雅黑", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Pixel);
            this.daProcessWave1.ForeColor = System.Drawing.Color.White;
            this.daProcessWave1.IsRadius = false;
            this.daProcessWave1.IsRectangle = false;
            this.daProcessWave1.IsShowRect = false;
            this.daProcessWave1.Location = new System.Drawing.Point(18, 246);
            this.daProcessWave1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.daProcessWave1.MaxValue = 100;
            this.daProcessWave1.Name = "daProcessWave1";
            this.daProcessWave1.PLC_Address = "0";
            this.daProcessWave1.PLC_Contact = "D";
            this.daProcessWave1.PLC_Enable = false;
            this.daProcessWave1.RectColor = System.Drawing.Color.White;
            this.daProcessWave1.RectWidth = 4;
            this.daProcessWave1.Size = new System.Drawing.Size(150, 150);
            this.daProcessWave1.TabIndex = 4;
            this.daProcessWave1.Value = 0;
            this.daProcessWave1.ValueColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            // 
            // daMeter1
            // 
            this.daMeter1.BoundaryLineColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.Control_Text = "0";
            this.daMeter1.ExternalRoundColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.FixedText = null;
            this.daMeter1.InsideRoundColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.Location = new System.Drawing.Point(371, 250);
            this.daMeter1.MaxValue = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.daMeter1.MeterDegrees = 150;
            this.daMeter1.MinValue = new decimal(new int[] {
            0,
            0,
            0,
            0});
            this.daMeter1.Name = "daMeter1";
            this.daMeter1.PLC_Address = "0";
            this.daMeter1.PLC_Contact = "D";
            this.daMeter1.PLC_Enable = false;
            this.daMeter1.PointerColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.ScaleColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.ScaleValueColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.Size = new System.Drawing.Size(350, 200);
            this.daMeter1.SplitCount = 10;
            this.daMeter1.TabIndex = 6;
            this.daMeter1.TextColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daMeter1.TextFont = new System.Drawing.Font("新細明體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.daMeter1.TextLocation = HZH_Controls.Controls.MeterTextLocation.None;
            this.daMeter1.Value = new decimal(new int[] {
            0,
            0,
            0,
            0});
            // 
            // daSwitch1
            // 
            this.daSwitch1.BackColor = System.Drawing.Color.Transparent;
            this.daSwitch1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daSwitch1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daSwitch1.Checked = false;
            this.daSwitch1.FalseColor = System.Drawing.Color.FromArgb(((int)(((byte)(189)))), ((int)(((byte)(189)))), ((int)(((byte)(189)))));
            this.daSwitch1.FalseTextColr = System.Drawing.Color.White;
            this.daSwitch1.Location = new System.Drawing.Point(247, 48);
            this.daSwitch1.Name = "daSwitch1";
            this.daSwitch1.Pattern = Bottom_Control.Button_pattern.Regression;
            this.daSwitch1.PLC_Address = "0";
            this.daSwitch1.PLC_Contact = "X";
            this.daSwitch1.PLC_Enable = false;
            this.daSwitch1.Size = new System.Drawing.Size(83, 31);
            this.daSwitch1.SwitchType = HZH_Controls.Controls.SwitchType.Ellipse;
            this.daSwitch1.TabIndex = 10;
            this.daSwitch1.Texts = null;
            this.daSwitch1.TrueColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daSwitch1.TrueTextColr = System.Drawing.Color.White;
            // 
            // daProcessEllipse1
            // 
            this.daProcessEllipse1.BackEllipseColor = System.Drawing.Color.FromArgb(((int)(((byte)(228)))), ((int)(((byte)(231)))), ((int)(((byte)(237)))));
            this.daProcessEllipse1.Control_Text = "0";
            this.daProcessEllipse1.CoreEllipseColor = System.Drawing.Color.FromArgb(((int)(((byte)(228)))), ((int)(((byte)(231)))), ((int)(((byte)(237)))));
            this.daProcessEllipse1.Font = new System.Drawing.Font("Arial Unicode MS", 20F);
            this.daProcessEllipse1.ForeColor = System.Drawing.Color.White;
            this.daProcessEllipse1.IsShowCoreEllipseBorder = true;
            this.daProcessEllipse1.Location = new System.Drawing.Point(200, 246);
            this.daProcessEllipse1.MaxValue = 100;
            this.daProcessEllipse1.Name = "daProcessEllipse1";
            this.daProcessEllipse1.PLC_Address = "0";
            this.daProcessEllipse1.PLC_Contact = "D";
            this.daProcessEllipse1.PLC_Enable = false;
            this.daProcessEllipse1.ShowType = HZH_Controls.Controls.ShowType.Ring;
            this.daProcessEllipse1.Size = new System.Drawing.Size(150, 150);
            this.daProcessEllipse1.TabIndex = 7;
            this.daProcessEllipse1.Value = 0;
            this.daProcessEllipse1.ValueColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daProcessEllipse1.ValueMargin = 5;
            this.daProcessEllipse1.ValueType = HZH_Controls.Controls.ValueType.Percent;
            this.daProcessEllipse1.ValueWidth = 30;
            // 
            // daSignalLamp1
            // 
            this.daSignalLamp1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daSignalLamp1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daSignalLamp1.Button_select = false;
            this.daSignalLamp1.Command = false;
            this.daSignalLamp1.I_FlickerColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daSignalLamp1.I_FlickerTime = 1000;
            this.daSignalLamp1.IsHighlight = true;
            this.daSignalLamp1.IsShowBorder = false;
            this.daSignalLamp1.LampColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daSignalLamp1.Location = new System.Drawing.Point(18, 29);
            this.daSignalLamp1.Name = "daSignalLamp1";
            this.daSignalLamp1.O_FlickerColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daSignalLamp1.O_FlickerTime = 1000;
            this.daSignalLamp1.Pattern = Bottom_Control.Button_pattern.Regression;
            this.daSignalLamp1.PLC_Address = "0";
            this.daSignalLamp1.PLC_Contact = "X";
            this.daSignalLamp1.PLC_Enable = false;
            this.daSignalLamp1.Size = new System.Drawing.Size(50, 50);
            this.daSignalLamp1.TabIndex = 9;
            this.daSignalLamp1.Text_OFF = "OFF";
            this.daSignalLamp1.Text_ON = "ON";
            this.daSignalLamp1.TwinkleSpeed = 0;
            // 
            // daThermometer1
            // 
            this.daThermometer1.Control_Text = "10";
            this.daThermometer1.GlassTubeColor = System.Drawing.Color.FromArgb(((int)(((byte)(211)))), ((int)(((byte)(211)))), ((int)(((byte)(211)))));
            this.daThermometer1.LeftTemperatureUnit = HZH_Controls.Controls.TemperatureUnit.C;
            this.daThermometer1.Location = new System.Drawing.Point(371, 34);
            this.daThermometer1.MaxValue = new decimal(new int[] {
            100,
            0,
            0,
            0});
            this.daThermometer1.MercuryColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))));
            this.daThermometer1.MinValue = new decimal(new int[] {
            0,
            0,
            0,
            0});
            this.daThermometer1.Name = "daThermometer1";
            this.daThermometer1.PLC_Address = "0";
            this.daThermometer1.PLC_Contact = "D";
            this.daThermometer1.PLC_Enable = false;
            this.daThermometer1.RightTemperatureUnit = HZH_Controls.Controls.TemperatureUnit.C;
            this.daThermometer1.Size = new System.Drawing.Size(70, 200);
            this.daThermometer1.SplitCount = 1;
            this.daThermometer1.TabIndex = 8;
            this.daThermometer1.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.daRotor1);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(1070, 642);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "新進測試";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // daRotor1
            // 
            this.daRotor1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daRotor1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daRotor1.Location = new System.Drawing.Point(882, 34);
            this.daRotor1.Name = "daRotor1";
            this.daRotor1.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daRotor1.PLC_Address = "0";
            this.daRotor1.PLC_Contact = "X";
            this.daRotor1.PLC_Enable = false;
            this.daRotor1.RotorAround = HZH_Controls.Controls.RotorAround.None;
            this.daRotor1.RotorColor = System.Drawing.Color.Black;
            this.daRotor1.Size = new System.Drawing.Size(150, 150);
            this.daRotor1.Speed = 100;
            this.daRotor1.TabIndex = 1;
            // 
            // daAlarmLamp1
            // 
            this.daAlarmLamp1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daAlarmLamp1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daAlarmLamp1.Button_select = false;
            this.daAlarmLamp1.Command = false;
            this.daAlarmLamp1.I_FlickerColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daAlarmLamp1.I_FlickerTime = 1000;
            this.daAlarmLamp1.LampColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daAlarmLamp1.Lampstand = System.Drawing.Color.FromArgb(((int)(((byte)(105)))), ((int)(((byte)(105)))), ((int)(((byte)(105)))));
            this.daAlarmLamp1.Location = new System.Drawing.Point(167, 29);
            this.daAlarmLamp1.Name = "daAlarmLamp1";
            this.daAlarmLamp1.O_FlickerColor = new System.Drawing.Color[] {
        System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(77)))), ((int)(((byte)(59)))))};
            this.daAlarmLamp1.O_FlickerTime = 1000;
            this.daAlarmLamp1.Pattern = Bottom_Control.Button_pattern.Regression;
            this.daAlarmLamp1.PLC_Address = "0";
            this.daAlarmLamp1.PLC_Contact = "X";
            this.daAlarmLamp1.PLC_Enable = false;
            this.daAlarmLamp1.Size = new System.Drawing.Size(50, 50);
            this.daAlarmLamp1.TabIndex = 15;
            this.daAlarmLamp1.Text_OFF = "OFF";
            this.daAlarmLamp1.Text_ON = "ON";
            this.daAlarmLamp1.TwinkleSpeed = 0;
            // 
            // daLedBulb1
            // 
            this.daLedBulb1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daLedBulb1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daLedBulb1.Location = new System.Drawing.Point(95, 34);
            this.daLedBulb1.Name = "daLedBulb1";
            this.daLedBulb1.Pattern = Bottom_Control.Button_pattern.Regression;
            this.daLedBulb1.PLC_Address = "0";
            this.daLedBulb1.PLC_Contact = "X";
            this.daLedBulb1.PLC_Enable = false;
            this.daLedBulb1.Size = new System.Drawing.Size(32, 32);
            this.daLedBulb1.TabIndex = 16;
            this.daLedBulb1.Text = "daLedBulb1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1295, 680);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer1;
        private 基本控件.DAProcessWave daProcessWave1;
        private 基本控件.DAConveyor daConveyor1;
        private 基本控件.DAMeter daMeter1;
        private 基本控件.DAProcessEllipse daProcessEllipse1;
        private 基本控件.DAThermometer daThermometer1;
        private 基本控件.DASignalLamp daSignalLamp1;
        private 基本控件.DASwitch daSwitch1;
        private 基本控件.DAAnalogMeter daAnalogMeter1;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private 基本控件.DARotor daRotor1;
        private 基本控件.DABottle daBottle1;
        private 基本控件.DAPond daPond1;
        private 基本控件.DAConduit daConduit1;
        private 基本控件.DALedBulb daLedBulb1;
        private 基本控件.DAAlarmLamp daAlarmLamp1;
    }
}