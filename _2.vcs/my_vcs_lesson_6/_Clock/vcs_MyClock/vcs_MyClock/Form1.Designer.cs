namespace vcs_MyClock
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
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown2 = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown3 = new System.Windows.Forms.NumericUpDown();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.lb_mesg = new System.Windows.Forms.Label();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.radioButton4 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.button12 = new System.Windows.Forms.Button();
            this.numericUpDown4 = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown5 = new System.Windows.Forms.NumericUpDown();
            this.button15 = new System.Windows.Forms.Button();
            this.numericUpDown6 = new System.Windows.Forms.NumericUpDown();
            this.button16 = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.lb_ww = new System.Windows.Forms.Panel();
            this.lb_yy = new System.Windows.Forms.Label();
            this.lb_weekday = new System.Windows.Forms.Label();
            this.lb_dd2 = new System.Windows.Forms.Label();
            this.lb_mm2 = new System.Windows.Forms.Label();
            this.lb_dd1 = new System.Windows.Forms.Label();
            this.lb_mm1 = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.lb_alarm_target = new System.Windows.Forms.Label();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.button4 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.button5 = new System.Windows.Forms.Button();
            this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown3)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown6)).BeginInit();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.lb_ww.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.tabPage4.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 78;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown1.Location = new System.Drawing.Point(6, 21);
            this.numericUpDown1.Maximum = new decimal(new int[] {
            24,
            0,
            0,
            0});
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown1.TabIndex = 1;
            this.numericUpDown1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // numericUpDown2
            // 
            this.numericUpDown2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown2.Location = new System.Drawing.Point(72, 21);
            this.numericUpDown2.Maximum = new decimal(new int[] {
            60,
            0,
            0,
            0});
            this.numericUpDown2.Name = "numericUpDown2";
            this.numericUpDown2.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown2.TabIndex = 2;
            this.numericUpDown2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown2.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // numericUpDown3
            // 
            this.numericUpDown3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown3.Location = new System.Drawing.Point(138, 21);
            this.numericUpDown3.Maximum = new decimal(new int[] {
            60,
            0,
            0,
            0});
            this.numericUpDown3.Name = "numericUpDown3";
            this.numericUpDown3.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown3.TabIndex = 3;
            this.numericUpDown3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(0, 334);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(462, 127);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // lb_mesg
            // 
            this.lb_mesg.AutoSize = true;
            this.lb_mesg.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_mesg.Location = new System.Drawing.Point(10, 294);
            this.lb_mesg.Name = "lb_mesg";
            this.lb_mesg.Size = new System.Drawing.Size(103, 21);
            this.lb_mesg.TabIndex = 9;
            this.lb_mesg.Text = "lb_message";
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Checked = true;
            this.radioButton1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radioButton1.Location = new System.Drawing.Point(8, 10);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(14, 13);
            this.radioButton1.TabIndex = 10;
            this.radioButton1.TabStop = true;
            this.radioButton1.UseVisualStyleBackColor = true;
            this.radioButton1.CheckedChanged += new System.EventHandler(this.radioButton1_CheckedChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioButton4);
            this.groupBox1.Controls.Add(this.radioButton3);
            this.groupBox1.Controls.Add(this.radioButton2);
            this.groupBox1.Controls.Add(this.radioButton1);
            this.groupBox1.Location = new System.Drawing.Point(432, -2);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(30, 80);
            this.groupBox1.TabIndex = 11;
            this.groupBox1.TabStop = false;
            // 
            // radioButton4
            // 
            this.radioButton4.AutoSize = true;
            this.radioButton4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radioButton4.Location = new System.Drawing.Point(8, 63);
            this.radioButton4.Name = "radioButton4";
            this.radioButton4.Size = new System.Drawing.Size(14, 13);
            this.radioButton4.TabIndex = 13;
            this.radioButton4.UseVisualStyleBackColor = true;
            this.radioButton4.CheckedChanged += new System.EventHandler(this.radioButton4_CheckedChanged);
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radioButton3.Location = new System.Drawing.Point(8, 46);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(14, 13);
            this.radioButton3.TabIndex = 12;
            this.radioButton3.UseVisualStyleBackColor = true;
            this.radioButton3.CheckedChanged += new System.EventHandler(this.radioButton3_CheckedChanged);
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.radioButton2.Location = new System.Drawing.Point(8, 28);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(14, 13);
            this.radioButton2.TabIndex = 11;
            this.radioButton2.UseVisualStyleBackColor = true;
            this.radioButton2.CheckedChanged += new System.EventHandler(this.radioButton2_CheckedChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button1);
            this.groupBox2.Controls.Add(this.button18);
            this.groupBox2.Controls.Add(this.button17);
            this.groupBox2.Location = new System.Drawing.Point(8, 27);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(230, 102);
            this.groupBox2.TabIndex = 12;
            this.groupBox2.TabStop = false;
            // 
            // button1
            // 
            this.button1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button1.BackgroundImage")));
            this.button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(154, 25);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(60, 60);
            this.button1.TabIndex = 21;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button18
            // 
            this.button18.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button18.BackgroundImage")));
            this.button18.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button18.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button18.Location = new System.Drawing.Point(81, 25);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(60, 60);
            this.button18.TabIndex = 20;
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // button17
            // 
            this.button17.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button17.BackgroundImage")));
            this.button17.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button17.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button17.Location = new System.Drawing.Point(9, 25);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(60, 60);
            this.button17.TabIndex = 17;
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.button3);
            this.groupBox3.Controls.Add(this.button2);
            this.groupBox3.Controls.Add(this.numericUpDown1);
            this.groupBox3.Controls.Add(this.numericUpDown2);
            this.groupBox3.Controls.Add(this.numericUpDown3);
            this.groupBox3.Location = new System.Drawing.Point(21, 16);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(206, 134);
            this.groupBox3.TabIndex = 17;
            this.groupBox3.TabStop = false;
            // 
            // button3
            // 
            this.button3.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button3.BackgroundImage")));
            this.button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button3.Location = new System.Drawing.Point(30, 66);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(60, 60);
            this.button3.TabIndex = 21;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button2.BackgroundImage")));
            this.button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button2.Location = new System.Drawing.Point(115, 66);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(60, 60);
            this.button2.TabIndex = 22;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.button12);
            this.groupBox4.Controls.Add(this.numericUpDown4);
            this.groupBox4.Controls.Add(this.numericUpDown5);
            this.groupBox4.Controls.Add(this.button15);
            this.groupBox4.Controls.Add(this.numericUpDown6);
            this.groupBox4.Location = new System.Drawing.Point(13, 45);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(227, 103);
            this.groupBox4.TabIndex = 18;
            this.groupBox4.TabStop = false;
            // 
            // button12
            // 
            this.button12.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button12.Location = new System.Drawing.Point(126, 63);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(60, 30);
            this.button12.TabIndex = 16;
            this.button12.Text = "停止";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // numericUpDown4
            // 
            this.numericUpDown4.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown4.Location = new System.Drawing.Point(25, 21);
            this.numericUpDown4.Maximum = new decimal(new int[] {
            23,
            0,
            0,
            0});
            this.numericUpDown4.Name = "numericUpDown4";
            this.numericUpDown4.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown4.TabIndex = 1;
            this.numericUpDown4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // numericUpDown5
            // 
            this.numericUpDown5.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown5.Location = new System.Drawing.Point(91, 21);
            this.numericUpDown5.Maximum = new decimal(new int[] {
            59,
            0,
            0,
            0});
            this.numericUpDown5.Name = "numericUpDown5";
            this.numericUpDown5.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown5.TabIndex = 2;
            this.numericUpDown5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown5.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // button15
            // 
            this.button15.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button15.Location = new System.Drawing.Point(38, 63);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(60, 30);
            this.button15.TabIndex = 13;
            this.button15.Text = "開始";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // numericUpDown6
            // 
            this.numericUpDown6.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.numericUpDown6.Location = new System.Drawing.Point(157, 22);
            this.numericUpDown6.Maximum = new decimal(new int[] {
            59,
            0,
            0,
            0});
            this.numericUpDown6.Name = "numericUpDown6";
            this.numericUpDown6.Size = new System.Drawing.Size(60, 36);
            this.numericUpDown6.TabIndex = 3;
            this.numericUpDown6.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button16
            // 
            this.button16.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button16.Location = new System.Drawing.Point(389, 343);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(50, 30);
            this.button16.TabIndex = 19;
            this.button16.Text = "Clear";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Location = new System.Drawing.Point(8, 104);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(259, 186);
            this.tabControl1.TabIndex = 20;
            this.tabControl1.SelectedIndexChanged += new System.EventHandler(this.tabControl1_SelectedIndexChanged);
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.lb_ww);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(251, 160);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "時鐘";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // lb_ww
            // 
            this.lb_ww.BackColor = System.Drawing.Color.White;
            this.lb_ww.Controls.Add(this.lb_yy);
            this.lb_ww.Controls.Add(this.lb_weekday);
            this.lb_ww.Controls.Add(this.lb_dd2);
            this.lb_ww.Controls.Add(this.lb_mm2);
            this.lb_ww.Controls.Add(this.lb_dd1);
            this.lb_ww.Controls.Add(this.lb_mm1);
            this.lb_ww.Location = new System.Drawing.Point(29, 19);
            this.lb_ww.Name = "lb_ww";
            this.lb_ww.Size = new System.Drawing.Size(175, 135);
            this.lb_ww.TabIndex = 27;
            // 
            // lb_yy
            // 
            this.lb_yy.AutoSize = true;
            this.lb_yy.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_yy.Location = new System.Drawing.Point(119, 13);
            this.lb_yy.Name = "lb_yy";
            this.lb_yy.Size = new System.Drawing.Size(54, 24);
            this.lb_yy.TabIndex = 26;
            this.lb_yy.Text = "2019";
            // 
            // lb_weekday
            // 
            this.lb_weekday.AutoSize = true;
            this.lb_weekday.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_weekday.Location = new System.Drawing.Point(49, 99);
            this.lb_weekday.Name = "lb_weekday";
            this.lb_weekday.Size = new System.Drawing.Size(82, 24);
            this.lb_weekday.TabIndex = 31;
            this.lb_weekday.Text = "星期一";
            // 
            // lb_dd2
            // 
            this.lb_dd2.AutoSize = true;
            this.lb_dd2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dd2.ForeColor = System.Drawing.Color.Red;
            this.lb_dd2.Location = new System.Drawing.Point(15, 59);
            this.lb_dd2.Name = "lb_dd2";
            this.lb_dd2.Size = new System.Drawing.Size(21, 24);
            this.lb_dd2.TabIndex = 30;
            this.lb_dd2.Text = "1";
            // 
            // lb_mm2
            // 
            this.lb_mm2.AutoSize = true;
            this.lb_mm2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_mm2.Location = new System.Drawing.Point(6, 25);
            this.lb_mm2.Name = "lb_mm2";
            this.lb_mm2.Size = new System.Drawing.Size(45, 24);
            this.lb_mm2.TabIndex = 29;
            this.lb_mm2.Text = "1月";
            // 
            // lb_dd1
            // 
            this.lb_dd1.AutoSize = true;
            this.lb_dd1.Font = new System.Drawing.Font("新細明體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_dd1.ForeColor = System.Drawing.Color.Red;
            this.lb_dd1.Location = new System.Drawing.Point(65, 32);
            this.lb_dd1.Name = "lb_dd1";
            this.lb_dd1.Size = new System.Drawing.Size(43, 48);
            this.lb_dd1.TabIndex = 28;
            this.lb_dd1.Text = "1";
            // 
            // lb_mm1
            // 
            this.lb_mm1.AutoSize = true;
            this.lb_mm1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_mm1.Location = new System.Drawing.Point(127, 43);
            this.lb_mm1.Name = "lb_mm1";
            this.lb_mm1.Size = new System.Drawing.Size(45, 24);
            this.lb_mm1.TabIndex = 27;
            this.lb_mm1.Text = "1月";
            // 
            // tabPage2
            // 
            this.tabPage2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.tabPage2.Controls.Add(this.groupBox2);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(251, 160);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "碼表";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.groupBox3);
            this.tabPage3.Location = new System.Drawing.Point(4, 22);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Size = new System.Drawing.Size(251, 160);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "倒數";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // tabPage4
            // 
            this.tabPage4.Controls.Add(this.lb_alarm_target);
            this.tabPage4.Controls.Add(this.groupBox4);
            this.tabPage4.Location = new System.Drawing.Point(4, 22);
            this.tabPage4.Name = "tabPage4";
            this.tabPage4.Size = new System.Drawing.Size(251, 160);
            this.tabPage4.TabIndex = 3;
            this.tabPage4.Text = "鬧鐘";
            this.tabPage4.UseVisualStyleBackColor = true;
            // 
            // lb_alarm_target
            // 
            this.lb_alarm_target.AutoSize = true;
            this.lb_alarm_target.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_alarm_target.ForeColor = System.Drawing.Color.Red;
            this.lb_alarm_target.Location = new System.Drawing.Point(14, 16);
            this.lb_alarm_target.Name = "lb_alarm_target";
            this.lb_alarm_target.Size = new System.Drawing.Size(135, 21);
            this.lb_alarm_target.TabIndex = 26;
            this.lb_alarm_target.Text = "lb_alarm_target";
            // 
            // tabPage5
            // 
            this.tabPage5.Location = new System.Drawing.Point(4, 22);
            this.tabPage5.Name = "tabPage5";
            this.tabPage5.Size = new System.Drawing.Size(251, 160);
            this.tabPage5.TabIndex = 4;
            this.tabPage5.Text = "About";
            this.tabPage5.UseVisualStyleBackColor = true;
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 464);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(466, 22);
            this.statusStrip1.TabIndex = 21;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(128, 17);
            this.toolStripStatusLabel1.Text = "toolStripStatusLabel1";
            // 
            // button4
            // 
            this.button4.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button4.BackgroundImage")));
            this.button4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button4.Location = new System.Drawing.Point(432, 79);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(30, 20);
            this.button4.TabIndex = 23;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(291, 125);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(164, 164);
            this.pictureBox1.TabIndex = 24;
            this.pictureBox1.TabStop = false;
            // 
            // timer2
            // 
            this.timer2.Enabled = true;
            this.timer2.Interval = 1000;
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // button5
            // 
            this.button5.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button5.BackgroundImage")));
            this.button5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.button5.Location = new System.Drawing.Point(432, 296);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(30, 20);
            this.button5.TabIndex = 25;
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // digitalDisplayControl1
            // 
            this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.digitalDisplayControl1.DigitColor = System.Drawing.Color.Purple;
            this.digitalDisplayControl1.DigitText = "88:88:88.88";
            this.digitalDisplayControl1.Location = new System.Drawing.Point(0, 0);
            this.digitalDisplayControl1.Name = "digitalDisplayControl1";
            this.digitalDisplayControl1.Size = new System.Drawing.Size(429, 99);
            this.digitalDisplayControl1.TabIndex = 0;
            this.digitalDisplayControl1.DoubleClick += new System.EventHandler(this.digitalDisplayControl1_DoubleClick);
            this.digitalDisplayControl1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.digitalDisplayControl1_MouseDown);
            this.digitalDisplayControl1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.digitalDisplayControl1_MouseMove);
            this.digitalDisplayControl1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.digitalDisplayControl1_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlLight;
            this.ClientSize = new System.Drawing.Size(466, 486);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.button16);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.lb_mesg);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.digitalDisplayControl1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "ims_Clock";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown3)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown6)).EndInit();
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.lb_ww.ResumeLayout(false);
            this.lb_ww.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage3.ResumeLayout(false);
            this.tabPage4.ResumeLayout(false);
            this.tabPage4.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.NumericUpDown numericUpDown1;
        private System.Windows.Forms.NumericUpDown numericUpDown2;
        private System.Windows.Forms.NumericUpDown numericUpDown3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label lb_mesg;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton radioButton4;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.NumericUpDown numericUpDown4;
        private System.Windows.Forms.NumericUpDown numericUpDown5;
        private System.Windows.Forms.NumericUpDown numericUpDown6;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.TabPage tabPage4;
        private System.Windows.Forms.TabPage tabPage5;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Label lb_alarm_target;
        private System.Windows.Forms.Panel lb_ww;
        private System.Windows.Forms.Label lb_dd2;
        private System.Windows.Forms.Label lb_mm2;
        private System.Windows.Forms.Label lb_dd1;
        private System.Windows.Forms.Label lb_mm1;
        private System.Windows.Forms.Label lb_weekday;
        private System.Windows.Forms.Label lb_yy;
    }
}

