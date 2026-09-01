namespace WindowsFormsApplication1
{
    partial class MainForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.SerialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.SaveFileDlg_Log = new System.Windows.Forms.SaveFileDialog();
            this.StatusStrip = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.MainPage = new System.Windows.Forms.TabPage();
            this.gbKMLLogging = new System.Windows.Forms.GroupBox();
            this.label_Positions_Recorded = new System.Windows.Forms.Label();
            this.label21 = new System.Windows.Forms.Label();
            this.tbxLogInterval = new System.Windows.Forms.TextBox();
            this.label19 = new System.Windows.Forms.Label();
            this.label18 = new System.Windows.Forms.Label();
            this.btnFileName = new System.Windows.Forms.Button();
            this.label17 = new System.Windows.Forms.Label();
            this.tbxFilename = new System.Windows.Forms.TextBox();
            this.btnLogging = new System.Windows.Forms.Button();
            this.LinkLabel_BeyondLogicURL = new System.Windows.Forms.LinkLabel();
            this.gbLocalGPSTime = new System.Windows.Forms.GroupBox();
            this.label_LocalTime = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label_LocalDate = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.gbPosition = new System.Windows.Forms.GroupBox();
            this.LinkLabel_GoogleMaps = new System.Windows.Forms.LinkLabel();
            this.label14 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.LinkLabel_GoogleEarthPlacemark = new System.Windows.Forms.LinkLabel();
            this.label12 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label_Speedkmh = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label_Altitude = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label_Longitude = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label_Latitude = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.StatPage = new System.Windows.Forms.TabPage();
            this.gbStats = new System.Windows.Forms.GroupBox();
            this.label20 = new System.Windows.Forms.Label();
            this.label_FixStatus = new System.Windows.Forms.Label();
            this.label_VDOP = new System.Windows.Forms.Label();
            this.label_Satellites = new System.Windows.Forms.Label();
            this.label_HDOP1 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label_PDOP = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.gbSatellites = new System.Windows.Forms.GroupBox();
            this.label22 = new System.Windows.Forms.Label();
            this.pgCFG = new System.Windows.Forms.TabPage();
            this.gbLicence = new System.Windows.Forms.GroupBox();
            this.tbLicence = new System.Windows.Forms.TextBox();
            this.gbCOMPort = new System.Windows.Forms.GroupBox();
            this.cbBaudRate = new System.Windows.Forms.ComboBox();
            this.label11 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.btnOpenComPort = new System.Windows.Forms.Button();
            this.cbCOMPort = new System.Windows.Forms.ComboBox();
            this.Timer_LogInterval = new System.Windows.Forms.Timer(this.components);
            this.StatusStrip.SuspendLayout();
            this.tabControl1.SuspendLayout();
            this.MainPage.SuspendLayout();
            this.gbKMLLogging.SuspendLayout();
            this.gbLocalGPSTime.SuspendLayout();
            this.gbPosition.SuspendLayout();
            this.StatPage.SuspendLayout();
            this.gbStats.SuspendLayout();
            this.gbSatellites.SuspendLayout();
            this.pgCFG.SuspendLayout();
            this.gbLicence.SuspendLayout();
            this.gbCOMPort.SuspendLayout();
            this.SuspendLayout();
            // 
            // SerialPort1
            // 
            this.SerialPort1.PortName = "COM13";
            this.SerialPort1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // SaveFileDlg_Log
            // 
            this.SaveFileDlg_Log.InitialDirectory = "c:\\";
            // 
            // StatusStrip
            // 
            this.StatusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.StatusStrip.Location = new System.Drawing.Point(0, 463);
            this.StatusStrip.Name = "StatusStrip";
            this.StatusStrip.Size = new System.Drawing.Size(291, 22);
            this.StatusStrip.TabIndex = 42;
            this.StatusStrip.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(0, 17);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.MainPage);
            this.tabControl1.Controls.Add(this.StatPage);
            this.tabControl1.Controls.Add(this.pgCFG);
            this.tabControl1.Location = new System.Drawing.Point(0, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(294, 462);
            this.tabControl1.TabIndex = 43;
            // 
            // MainPage
            // 
            this.MainPage.Controls.Add(this.gbKMLLogging);
            this.MainPage.Controls.Add(this.LinkLabel_BeyondLogicURL);
            this.MainPage.Controls.Add(this.gbLocalGPSTime);
            this.MainPage.Controls.Add(this.gbPosition);
            this.MainPage.Location = new System.Drawing.Point(4, 22);
            this.MainPage.Name = "MainPage";
            this.MainPage.Padding = new System.Windows.Forms.Padding(3);
            this.MainPage.Size = new System.Drawing.Size(286, 436);
            this.MainPage.TabIndex = 0;
            this.MainPage.Text = "Main";
            this.MainPage.UseVisualStyleBackColor = true;
            // 
            // gbKMLLogging
            // 
            this.gbKMLLogging.Controls.Add(this.label_Positions_Recorded);
            this.gbKMLLogging.Controls.Add(this.label21);
            this.gbKMLLogging.Controls.Add(this.tbxLogInterval);
            this.gbKMLLogging.Controls.Add(this.label19);
            this.gbKMLLogging.Controls.Add(this.label18);
            this.gbKMLLogging.Controls.Add(this.btnFileName);
            this.gbKMLLogging.Controls.Add(this.label17);
            this.gbKMLLogging.Controls.Add(this.tbxFilename);
            this.gbKMLLogging.Controls.Add(this.btnLogging);
            this.gbKMLLogging.Location = new System.Drawing.Point(6, 289);
            this.gbKMLLogging.Name = "gbKMLLogging";
            this.gbKMLLogging.Size = new System.Drawing.Size(269, 124);
            this.gbKMLLogging.TabIndex = 28;
            this.gbKMLLogging.TabStop = false;
            this.gbKMLLogging.Text = "KML Logging";
            // 
            // label_Positions_Recorded
            // 
            this.label_Positions_Recorded.Location = new System.Drawing.Point(132, 97);
            this.label_Positions_Recorded.Name = "label_Positions_Recorded";
            this.label_Positions_Recorded.Size = new System.Drawing.Size(46, 18);
            this.label_Positions_Recorded.TabIndex = 8;
            this.label_Positions_Recorded.Text = "0";
            this.label_Positions_Recorded.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(214, 73);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(47, 13);
            this.label21.TabIndex = 7;
            this.label21.Text = "seconds";
            // 
            // tbxLogInterval
            // 
            this.tbxLogInterval.Location = new System.Drawing.Point(106, 69);
            this.tbxLogInterval.Name = "tbxLogInterval";
            this.tbxLogInterval.Size = new System.Drawing.Size(100, 20);
            this.tbxLogInterval.TabIndex = 6;
            this.tbxLogInterval.Text = "30";
            this.tbxLogInterval.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(10, 73);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(89, 13);
            this.label19.TabIndex = 5;
            this.label19.Text = "Logging Interval :";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(10, 100);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(125, 13);
            this.label18.TabIndex = 4;
            this.label18.Text = "No. Positions Recorded :";
            // 
            // btnFileName
            // 
            this.btnFileName.Location = new System.Drawing.Point(234, 38);
            this.btnFileName.Name = "btnFileName";
            this.btnFileName.Size = new System.Drawing.Size(27, 23);
            this.btnFileName.TabIndex = 3;
            this.btnFileName.Text = "...";
            this.btnFileName.UseVisualStyleBackColor = true;
            this.btnFileName.Click += new System.EventHandler(this.bttFileName_Click);
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(11, 22);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(55, 13);
            this.label17.TabIndex = 2;
            this.label17.Text = "Filename :";
            // 
            // tbxFilename
            // 
            this.tbxFilename.Location = new System.Drawing.Point(11, 40);
            this.tbxFilename.Name = "tbxFilename";
            this.tbxFilename.Size = new System.Drawing.Size(216, 20);
            this.tbxFilename.TabIndex = 1;
            // 
            // btnLogging
            // 
            this.btnLogging.Location = new System.Drawing.Point(188, 95);
            this.btnLogging.Name = "btnLogging";
            this.btnLogging.Size = new System.Drawing.Size(75, 23);
            this.btnLogging.TabIndex = 0;
            this.btnLogging.Text = "Start";
            this.btnLogging.UseVisualStyleBackColor = true;
            this.btnLogging.Click += new System.EventHandler(this.button_logging_Click);
            // 
            // LinkLabel_BeyondLogicURL
            // 
            this.LinkLabel_BeyondLogicURL.AutoSize = true;
            this.LinkLabel_BeyondLogicURL.Location = new System.Drawing.Point(172, 416);
            this.LinkLabel_BeyondLogicURL.Name = "LinkLabel_BeyondLogicURL";
            this.LinkLabel_BeyondLogicURL.Size = new System.Drawing.Size(109, 13);
            this.LinkLabel_BeyondLogicURL.TabIndex = 27;
            this.LinkLabel_BeyondLogicURL.TabStop = true;
            this.LinkLabel_BeyondLogicURL.Text = "www.beyondlogic.org";
            this.LinkLabel_BeyondLogicURL.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // gbLocalGPSTime
            // 
            this.gbLocalGPSTime.Controls.Add(this.label_LocalTime);
            this.gbLocalGPSTime.Controls.Add(this.label6);
            this.gbLocalGPSTime.Controls.Add(this.label_LocalDate);
            this.gbLocalGPSTime.Controls.Add(this.label7);
            this.gbLocalGPSTime.Location = new System.Drawing.Point(6, 218);
            this.gbLocalGPSTime.Name = "gbLocalGPSTime";
            this.gbLocalGPSTime.Size = new System.Drawing.Size(270, 65);
            this.gbLocalGPSTime.TabIndex = 26;
            this.gbLocalGPSTime.TabStop = false;
            this.gbLocalGPSTime.Text = "Local GPS Time";
            // 
            // label_LocalTime
            // 
            this.label_LocalTime.Location = new System.Drawing.Point(66, 20);
            this.label_LocalTime.Name = "label_LocalTime";
            this.label_LocalTime.Size = new System.Drawing.Size(189, 13);
            this.label_LocalTime.TabIndex = 18;
            this.label_LocalTime.Text = "[Local Time]";
            this.label_LocalTime.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(10, 20);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(39, 13);
            this.label6.TabIndex = 17;
            this.label6.Text = "Time  :";
            // 
            // label_LocalDate
            // 
            this.label_LocalDate.Location = new System.Drawing.Point(91, 39);
            this.label_LocalDate.Name = "label_LocalDate";
            this.label_LocalDate.Size = new System.Drawing.Size(164, 13);
            this.label_LocalDate.TabIndex = 16;
            this.label_LocalDate.Text = "[Date]";
            this.label_LocalDate.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(10, 39);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(36, 13);
            this.label7.TabIndex = 15;
            this.label7.Text = "Date :";
            // 
            // gbPosition
            // 
            this.gbPosition.Controls.Add(this.LinkLabel_GoogleMaps);
            this.gbPosition.Controls.Add(this.label14);
            this.gbPosition.Controls.Add(this.label13);
            this.gbPosition.Controls.Add(this.LinkLabel_GoogleEarthPlacemark);
            this.gbPosition.Controls.Add(this.label12);
            this.gbPosition.Controls.Add(this.label5);
            this.gbPosition.Controls.Add(this.label_Speedkmh);
            this.gbPosition.Controls.Add(this.label3);
            this.gbPosition.Controls.Add(this.label_Altitude);
            this.gbPosition.Controls.Add(this.label9);
            this.gbPosition.Controls.Add(this.label_Longitude);
            this.gbPosition.Controls.Add(this.label4);
            this.gbPosition.Controls.Add(this.label_Latitude);
            this.gbPosition.Controls.Add(this.label2);
            this.gbPosition.Location = new System.Drawing.Point(6, 6);
            this.gbPosition.Name = "gbPosition";
            this.gbPosition.Size = new System.Drawing.Size(270, 206);
            this.gbPosition.TabIndex = 25;
            this.gbPosition.TabStop = false;
            this.gbPosition.Text = "Position";
            // 
            // LinkLabel_GoogleMaps
            // 
            this.LinkLabel_GoogleMaps.AutoSize = true;
            this.LinkLabel_GoogleMaps.Location = new System.Drawing.Point(86, 151);
            this.LinkLabel_GoogleMaps.Name = "LinkLabel_GoogleMaps";
            this.LinkLabel_GoogleMaps.Size = new System.Drawing.Size(110, 13);
            this.LinkLabel_GoogleMaps.TabIndex = 28;
            this.LinkLabel_GoogleMaps.TabStop = true;
            this.LinkLabel_GoogleMaps.Text = "Open in Google Maps";
            this.LinkLabel_GoogleMaps.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel_GoogleMaps_LinkClicked);
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(228, 42);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(25, 13);
            this.label14.TabIndex = 27;
            this.label14.Text = "deg";
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(228, 23);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(25, 13);
            this.label13.TabIndex = 26;
            this.label13.Text = "deg";
            // 
            // LinkLabel_GoogleEarthPlacemark
            // 
            this.LinkLabel_GoogleEarthPlacemark.AutoSize = true;
            this.LinkLabel_GoogleEarthPlacemark.Location = new System.Drawing.Point(63, 126);
            this.LinkLabel_GoogleEarthPlacemark.Name = "LinkLabel_GoogleEarthPlacemark";
            this.LinkLabel_GoogleEarthPlacemark.Size = new System.Drawing.Size(156, 13);
            this.LinkLabel_GoogleEarthPlacemark.TabIndex = 25;
            this.LinkLabel_GoogleEarthPlacemark.TabStop = true;
            this.LinkLabel_GoogleEarthPlacemark.Text = "Create Google Earth Placemark";
            this.LinkLabel_GoogleEarthPlacemark.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel_GoogleEarthPlacemark_LinkClicked);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(228, 61);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(15, 13);
            this.label12.TabIndex = 24;
            this.label12.Text = "m";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(228, 80);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(32, 13);
            this.label5.TabIndex = 23;
            this.label5.Text = "km/h";
            // 
            // label_Speedkmh
            // 
            this.label_Speedkmh.Location = new System.Drawing.Point(150, 80);
            this.label_Speedkmh.Name = "label_Speedkmh";
            this.label_Speedkmh.Size = new System.Drawing.Size(77, 13);
            this.label_Speedkmh.TabIndex = 22;
            this.label_Speedkmh.Text = "[Speed kmh]";
            this.label_Speedkmh.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(10, 80);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(44, 13);
            this.label3.TabIndex = 21;
            this.label3.Text = "Speed :";
            // 
            // label_Altitude
            // 
            this.label_Altitude.Location = new System.Drawing.Point(154, 61);
            this.label_Altitude.Name = "label_Altitude";
            this.label_Altitude.Size = new System.Drawing.Size(73, 13);
            this.label_Altitude.TabIndex = 20;
            this.label_Altitude.Text = "[Altitude]";
            this.label_Altitude.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(10, 61);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(48, 13);
            this.label9.TabIndex = 19;
            this.label9.Text = "Altitude :";
            // 
            // label_Longitude
            // 
            this.label_Longitude.Location = new System.Drawing.Point(155, 42);
            this.label_Longitude.Name = "label_Longitude";
            this.label_Longitude.Size = new System.Drawing.Size(72, 13);
            this.label_Longitude.TabIndex = 10;
            this.label_Longitude.Text = "[Longitude]";
            this.label_Longitude.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(10, 42);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(60, 13);
            this.label4.TabIndex = 9;
            this.label4.Text = "Longitude :";
            // 
            // label_Latitude
            // 
            this.label_Latitude.Location = new System.Drawing.Point(156, 23);
            this.label_Latitude.Name = "label_Latitude";
            this.label_Latitude.Size = new System.Drawing.Size(70, 13);
            this.label_Latitude.TabIndex = 8;
            this.label_Latitude.Text = "[Latitude]";
            this.label_Latitude.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(10, 23);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 13);
            this.label2.TabIndex = 7;
            this.label2.Text = "Latitude :";
            // 
            // StatPage
            // 
            this.StatPage.Controls.Add(this.gbStats);
            this.StatPage.Controls.Add(this.gbSatellites);
            this.StatPage.Location = new System.Drawing.Point(4, 22);
            this.StatPage.Name = "StatPage";
            this.StatPage.Padding = new System.Windows.Forms.Padding(3);
            this.StatPage.Size = new System.Drawing.Size(286, 436);
            this.StatPage.TabIndex = 1;
            this.StatPage.Text = "Statistics";
            this.StatPage.UseVisualStyleBackColor = true;
            // 
            // gbStats
            // 
            this.gbStats.Controls.Add(this.label20);
            this.gbStats.Controls.Add(this.label_FixStatus);
            this.gbStats.Controls.Add(this.label_VDOP);
            this.gbStats.Controls.Add(this.label_Satellites);
            this.gbStats.Controls.Add(this.label_HDOP1);
            this.gbStats.Controls.Add(this.label8);
            this.gbStats.Controls.Add(this.label_PDOP);
            this.gbStats.Controls.Add(this.label1);
            this.gbStats.Controls.Add(this.label16);
            this.gbStats.Controls.Add(this.label15);
            this.gbStats.Location = new System.Drawing.Point(6, 5);
            this.gbStats.Name = "gbStats";
            this.gbStats.Size = new System.Drawing.Size(273, 113);
            this.gbStats.TabIndex = 38;
            this.gbStats.TabStop = false;
            this.gbStats.Text = "Stats";
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(17, 16);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(59, 13);
            this.label20.TabIndex = 46;
            this.label20.Text = "Fix Status :";
            // 
            // label_FixStatus
            // 
            this.label_FixStatus.Location = new System.Drawing.Point(192, 16);
            this.label_FixStatus.Name = "label_FixStatus";
            this.label_FixStatus.Size = new System.Drawing.Size(59, 13);
            this.label_FixStatus.TabIndex = 44;
            this.label_FixStatus.Text = "[Fix Status]";
            this.label_FixStatus.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label_VDOP
            // 
            this.label_VDOP.Location = new System.Drawing.Point(210, 92);
            this.label_VDOP.Name = "label_VDOP";
            this.label_VDOP.Size = new System.Drawing.Size(41, 13);
            this.label_VDOP.TabIndex = 43;
            this.label_VDOP.Text = "label19";
            this.label_VDOP.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label_Satellites
            // 
            this.label_Satellites.Location = new System.Drawing.Point(167, 35);
            this.label_Satellites.Name = "label_Satellites";
            this.label_Satellites.Size = new System.Drawing.Size(84, 13);
            this.label_Satellites.TabIndex = 26;
            this.label_Satellites.Text = "[No of Satellites]";
            this.label_Satellites.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label_HDOP1
            // 
            this.label_HDOP1.Location = new System.Drawing.Point(210, 73);
            this.label_HDOP1.Name = "label_HDOP1";
            this.label_HDOP1.Size = new System.Drawing.Size(41, 13);
            this.label_HDOP1.TabIndex = 42;
            this.label_HDOP1.Text = "label18";
            this.label_HDOP1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(17, 35);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(83, 13);
            this.label8.TabIndex = 25;
            this.label8.Text = "Satellites Used :";
            // 
            // label_PDOP
            // 
            this.label_PDOP.Location = new System.Drawing.Point(210, 54);
            this.label_PDOP.Name = "label_PDOP";
            this.label_PDOP.Size = new System.Drawing.Size(41, 13);
            this.label_PDOP.TabIndex = 41;
            this.label_PDOP.Text = "label17";
            this.label_PDOP.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(17, 54);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(146, 13);
            this.label1.TabIndex = 38;
            this.label1.Text = "Position Dilution of Precision :";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(17, 92);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(144, 13);
            this.label16.TabIndex = 40;
            this.label16.Text = "Vertical Dilution of Precision :";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(17, 73);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(156, 13);
            this.label15.TabIndex = 39;
            this.label15.Text = "Horizontal Dilution of Precision :";
            // 
            // gbSatellites
            // 
            this.gbSatellites.Controls.Add(this.label22);
            this.gbSatellites.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.gbSatellites.Location = new System.Drawing.Point(6, 121);
            this.gbSatellites.Name = "gbSatellites";
            this.gbSatellites.Size = new System.Drawing.Size(273, 306);
            this.gbSatellites.TabIndex = 37;
            this.gbSatellites.TabStop = false;
            this.gbSatellites.Text = "Satellites";
            // 
            // label22
            // 
            this.label22.AutoSize = true;
            this.label22.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label22.Location = new System.Drawing.Point(23, 284);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(228, 13);
            this.label22.TabIndex = 0;
            this.label22.Text = "Satellites shown in bold are used for position fix";
            // 
            // pgCFG
            // 
            this.pgCFG.Controls.Add(this.gbLicence);
            this.pgCFG.Controls.Add(this.gbCOMPort);
            this.pgCFG.Location = new System.Drawing.Point(4, 22);
            this.pgCFG.Name = "pgCFG";
            this.pgCFG.Size = new System.Drawing.Size(286, 436);
            this.pgCFG.TabIndex = 2;
            this.pgCFG.Text = "Config";
            this.pgCFG.UseVisualStyleBackColor = true;
            // 
            // gbLicence
            // 
            this.gbLicence.Controls.Add(this.tbLicence);
            this.gbLicence.Location = new System.Drawing.Point(8, 101);
            this.gbLicence.Name = "gbLicence";
            this.gbLicence.Size = new System.Drawing.Size(270, 321);
            this.gbLicence.TabIndex = 28;
            this.gbLicence.TabStop = false;
            this.gbLicence.Text = "Licence";
            // 
            // tbLicence
            // 
            this.tbLicence.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.tbLicence.Location = new System.Drawing.Point(6, 19);
            this.tbLicence.Multiline = true;
            this.tbLicence.Name = "tbLicence";
            this.tbLicence.ReadOnly = true;
            this.tbLicence.Size = new System.Drawing.Size(258, 296);
            this.tbLicence.TabIndex = 0;
            this.tbLicence.Text = resources.GetString("tbLicence.Text");
            // 
            // gbCOMPort
            // 
            this.gbCOMPort.Controls.Add(this.cbBaudRate);
            this.gbCOMPort.Controls.Add(this.label11);
            this.gbCOMPort.Controls.Add(this.label10);
            this.gbCOMPort.Controls.Add(this.btnOpenComPort);
            this.gbCOMPort.Controls.Add(this.cbCOMPort);
            this.gbCOMPort.Location = new System.Drawing.Point(3, 3);
            this.gbCOMPort.Name = "gbCOMPort";
            this.gbCOMPort.Size = new System.Drawing.Size(275, 92);
            this.gbCOMPort.TabIndex = 27;
            this.gbCOMPort.TabStop = false;
            this.gbCOMPort.Text = "Port";
            // 
            // cbBaudRate
            // 
            this.cbBaudRate.FormattingEnabled = true;
            this.cbBaudRate.Items.AddRange(new object[] {
            "2400",
            "4800",
            "7200",
            "9600",
            "14400",
            "19200",
            "38400",
            "57600",
            "115200"});
            this.cbBaudRate.Location = new System.Drawing.Point(76, 52);
            this.cbBaudRate.Name = "cbBaudRate";
            this.cbBaudRate.Size = new System.Drawing.Size(121, 21);
            this.cbBaudRate.TabIndex = 6;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(6, 55);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(64, 13);
            this.label11.TabIndex = 5;
            this.label11.Text = "Baud Rate :";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(6, 24);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(59, 13);
            this.label10.TabIndex = 4;
            this.label10.Text = "COM Port :";
            // 
            // btnOpenComPort
            // 
            this.btnOpenComPort.Location = new System.Drawing.Point(207, 19);
            this.btnOpenComPort.Name = "btnOpenComPort";
            this.btnOpenComPort.Size = new System.Drawing.Size(56, 24);
            this.btnOpenComPort.TabIndex = 3;
            this.btnOpenComPort.Text = "Open";
            this.btnOpenComPort.UseVisualStyleBackColor = true;
            this.btnOpenComPort.Click += new System.EventHandler(this.button1_Click_2);
            // 
            // cbCOMPort
            // 
            this.cbCOMPort.FormattingEnabled = true;
            this.cbCOMPort.Location = new System.Drawing.Point(76, 21);
            this.cbCOMPort.Name = "cbCOMPort";
            this.cbCOMPort.Size = new System.Drawing.Size(121, 21);
            this.cbCOMPort.TabIndex = 2;
            // 
            // Timer_LogInterval
            // 
            this.Timer_LogInterval.Tick += new System.EventHandler(this.Timer_LogInterval_Tick);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(291, 485);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.StatusStrip);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "MainForm";
            this.Text = "Beyond GPS";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.StatusStrip.ResumeLayout(false);
            this.StatusStrip.PerformLayout();
            this.tabControl1.ResumeLayout(false);
            this.MainPage.ResumeLayout(false);
            this.MainPage.PerformLayout();
            this.gbKMLLogging.ResumeLayout(false);
            this.gbKMLLogging.PerformLayout();
            this.gbLocalGPSTime.ResumeLayout(false);
            this.gbLocalGPSTime.PerformLayout();
            this.gbPosition.ResumeLayout(false);
            this.gbPosition.PerformLayout();
            this.StatPage.ResumeLayout(false);
            this.gbStats.ResumeLayout(false);
            this.gbStats.PerformLayout();
            this.gbSatellites.ResumeLayout(false);
            this.gbSatellites.PerformLayout();
            this.pgCFG.ResumeLayout(false);
            this.gbLicence.ResumeLayout(false);
            this.gbLicence.PerformLayout();
            this.gbCOMPort.ResumeLayout(false);
            this.gbCOMPort.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.IO.Ports.SerialPort SerialPort1;
        private System.Windows.Forms.SaveFileDialog SaveFileDlg_Log;
        private System.Windows.Forms.StatusStrip StatusStrip;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage MainPage;
        private System.Windows.Forms.GroupBox gbLocalGPSTime;
        private System.Windows.Forms.Label label_LocalTime;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label_LocalDate;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.GroupBox gbPosition;
        private System.Windows.Forms.LinkLabel LinkLabel_GoogleMaps;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.LinkLabel LinkLabel_GoogleEarthPlacemark;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label_Speedkmh;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label_Altitude;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label_Longitude;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label_Latitude;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TabPage StatPage;
        private System.Windows.Forms.GroupBox gbStats;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.Label label_FixStatus;
        private System.Windows.Forms.Label label_VDOP;
        private System.Windows.Forms.Label label_Satellites;
        private System.Windows.Forms.Label label_HDOP1;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label_PDOP;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.GroupBox gbSatellites;
        private System.Windows.Forms.TabPage pgCFG;
        private System.Windows.Forms.GroupBox gbCOMPort;
        private System.Windows.Forms.Button btnOpenComPort;
        private System.Windows.Forms.ComboBox cbCOMPort;
        private System.Windows.Forms.LinkLabel LinkLabel_BeyondLogicURL;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.ComboBox cbBaudRate;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.GroupBox gbKMLLogging;
        private System.Windows.Forms.Button btnFileName;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.TextBox tbxFilename;
        private System.Windows.Forms.Button btnLogging;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.TextBox tbxLogInterval;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.Timer Timer_LogInterval;
        private System.Windows.Forms.Label label_Positions_Recorded;
        private System.Windows.Forms.Label label22;
        private System.Windows.Forms.GroupBox gbLicence;
        private System.Windows.Forms.TextBox tbLicence;
    }
}

