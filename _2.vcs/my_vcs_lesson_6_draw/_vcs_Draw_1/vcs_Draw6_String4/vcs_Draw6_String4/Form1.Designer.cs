namespace vcs_Draw6_String4
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
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.bt_font_size_10 = new System.Windows.Forms.Button();
            this.cb_font_style3 = new System.Windows.Forms.CheckBox();
            this.bt_font_setup = new System.Windows.Forms.Button();
            this.bt_font_size_20 = new System.Windows.Forms.Button();
            this.cb_font_style2 = new System.Windows.Forms.CheckBox();
            this.bt_font_size_30 = new System.Windows.Forms.Button();
            this.bt_font_size_minus = new System.Windows.Forms.Button();
            this.bt_font_size_40 = new System.Windows.Forms.Button();
            this.cb_font_style1 = new System.Windows.Forms.CheckBox();
            this.bt_font_size_50 = new System.Windows.Forms.Button();
            this.bt_font_size_plus = new System.Windows.Forms.Button();
            this.bt_fontname1 = new System.Windows.Forms.Button();
            this.bt_fontname2 = new System.Windows.Forms.Button();
            this.bt_speed_minus = new System.Windows.Forms.Button();
            this.bt_speed_plus = new System.Windows.Forms.Button();
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_background_color = new System.Windows.Forms.Button();
            this.bt_open_picture = new System.Windows.Forms.Button();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox5.SuspendLayout();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 50;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Pink;
            this.pictureBox1.Location = new System.Drawing.Point(12, 240);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(800, 100);
            this.pictureBox1.TabIndex = 29;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.Location = new System.Drawing.Point(160, 20);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(640, 36);
            this.textBox1.TabIndex = 28;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 20);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(130, 49);
            this.button1.TabIndex = 27;
            this.button1.Text = "製作PNG檔";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 80);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(130, 49);
            this.button2.TabIndex = 26;
            this.button2.Text = "讀PNG 做成GIF";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 456);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(800, 171);
            this.richTextBox1.TabIndex = 30;
            this.richTextBox1.Text = "";
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.bt_font_size_10);
            this.groupBox5.Controls.Add(this.cb_font_style3);
            this.groupBox5.Controls.Add(this.bt_font_setup);
            this.groupBox5.Controls.Add(this.bt_font_size_20);
            this.groupBox5.Controls.Add(this.cb_font_style2);
            this.groupBox5.Controls.Add(this.bt_font_size_30);
            this.groupBox5.Controls.Add(this.bt_font_size_minus);
            this.groupBox5.Controls.Add(this.bt_font_size_40);
            this.groupBox5.Controls.Add(this.cb_font_style1);
            this.groupBox5.Controls.Add(this.bt_font_size_50);
            this.groupBox5.Controls.Add(this.bt_font_size_plus);
            this.groupBox5.Controls.Add(this.bt_fontname1);
            this.groupBox5.Controls.Add(this.bt_fontname2);
            this.groupBox5.Location = new System.Drawing.Point(160, 80);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(640, 140);
            this.groupBox5.TabIndex = 31;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "自型設定";
            // 
            // bt_font_size_10
            // 
            this.bt_font_size_10.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_10.Location = new System.Drawing.Point(19, 22);
            this.bt_font_size_10.Name = "bt_font_size_10";
            this.bt_font_size_10.Size = new System.Drawing.Size(41, 40);
            this.bt_font_size_10.TabIndex = 1;
            this.bt_font_size_10.Text = "10";
            this.bt_font_size_10.UseVisualStyleBackColor = true;
            this.bt_font_size_10.Click += new System.EventHandler(this.bt_font_size_10_Click);
            // 
            // cb_font_style3
            // 
            this.cb_font_style3.AutoSize = true;
            this.cb_font_style3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_font_style3.Location = new System.Drawing.Point(556, 33);
            this.cb_font_style3.Name = "cb_font_style3";
            this.cb_font_style3.Size = new System.Drawing.Size(66, 23);
            this.cb_font_style3.TabIndex = 10;
            this.cb_font_style3.Text = "底線";
            this.cb_font_style3.UseVisualStyleBackColor = true;
            this.cb_font_style3.CheckedChanged += new System.EventHandler(this.cb_font_style_CheckedChanged);
            // 
            // bt_font_setup
            // 
            this.bt_font_setup.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_setup.ForeColor = System.Drawing.Color.Red;
            this.bt_font_setup.Location = new System.Drawing.Point(298, 22);
            this.bt_font_setup.Name = "bt_font_setup";
            this.bt_font_setup.Size = new System.Drawing.Size(66, 40);
            this.bt_font_setup.TabIndex = 11;
            this.bt_font_setup.Text = "font";
            this.bt_font_setup.UseVisualStyleBackColor = true;
            this.bt_font_setup.Click += new System.EventHandler(this.bt_font_setup_Click);
            // 
            // bt_font_size_20
            // 
            this.bt_font_size_20.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_20.Location = new System.Drawing.Point(72, 22);
            this.bt_font_size_20.Name = "bt_font_size_20";
            this.bt_font_size_20.Size = new System.Drawing.Size(41, 40);
            this.bt_font_size_20.TabIndex = 2;
            this.bt_font_size_20.Text = "20";
            this.bt_font_size_20.UseVisualStyleBackColor = true;
            this.bt_font_size_20.Click += new System.EventHandler(this.bt_font_size_20_Click);
            // 
            // cb_font_style2
            // 
            this.cb_font_style2.AutoSize = true;
            this.cb_font_style2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_font_style2.Location = new System.Drawing.Point(475, 33);
            this.cb_font_style2.Name = "cb_font_style2";
            this.cb_font_style2.Size = new System.Drawing.Size(66, 23);
            this.cb_font_style2.TabIndex = 9;
            this.cb_font_style2.Text = "斜體";
            this.cb_font_style2.UseVisualStyleBackColor = true;
            this.cb_font_style2.CheckedChanged += new System.EventHandler(this.cb_font_style_CheckedChanged);
            // 
            // bt_font_size_30
            // 
            this.bt_font_size_30.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_30.Location = new System.Drawing.Point(128, 22);
            this.bt_font_size_30.Name = "bt_font_size_30";
            this.bt_font_size_30.Size = new System.Drawing.Size(41, 40);
            this.bt_font_size_30.TabIndex = 3;
            this.bt_font_size_30.Text = "30";
            this.bt_font_size_30.UseVisualStyleBackColor = true;
            this.bt_font_size_30.Click += new System.EventHandler(this.bt_font_size_30_Click);
            // 
            // bt_font_size_minus
            // 
            this.bt_font_size_minus.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_minus.Location = new System.Drawing.Point(19, 85);
            this.bt_font_size_minus.Name = "bt_font_size_minus";
            this.bt_font_size_minus.Size = new System.Drawing.Size(112, 40);
            this.bt_font_size_minus.TabIndex = 12;
            this.bt_font_size_minus.Text = "字體 -";
            this.bt_font_size_minus.UseVisualStyleBackColor = true;
            this.bt_font_size_minus.Click += new System.EventHandler(this.bt_font_size_minus_Click);
            // 
            // bt_font_size_40
            // 
            this.bt_font_size_40.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_40.Location = new System.Drawing.Point(181, 22);
            this.bt_font_size_40.Name = "bt_font_size_40";
            this.bt_font_size_40.Size = new System.Drawing.Size(41, 40);
            this.bt_font_size_40.TabIndex = 4;
            this.bt_font_size_40.Text = "40";
            this.bt_font_size_40.UseVisualStyleBackColor = true;
            this.bt_font_size_40.Click += new System.EventHandler(this.bt_font_size_40_Click);
            // 
            // cb_font_style1
            // 
            this.cb_font_style1.AutoSize = true;
            this.cb_font_style1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_font_style1.Location = new System.Drawing.Point(391, 33);
            this.cb_font_style1.Name = "cb_font_style1";
            this.cb_font_style1.Size = new System.Drawing.Size(66, 23);
            this.cb_font_style1.TabIndex = 8;
            this.cb_font_style1.Text = "粗體";
            this.cb_font_style1.UseVisualStyleBackColor = true;
            this.cb_font_style1.CheckedChanged += new System.EventHandler(this.cb_font_style_CheckedChanged);
            // 
            // bt_font_size_50
            // 
            this.bt_font_size_50.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_50.Location = new System.Drawing.Point(232, 22);
            this.bt_font_size_50.Name = "bt_font_size_50";
            this.bt_font_size_50.Size = new System.Drawing.Size(41, 40);
            this.bt_font_size_50.TabIndex = 5;
            this.bt_font_size_50.Text = "50";
            this.bt_font_size_50.UseVisualStyleBackColor = true;
            this.bt_font_size_50.Click += new System.EventHandler(this.bt_font_size_50_Click);
            // 
            // bt_font_size_plus
            // 
            this.bt_font_size_plus.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_font_size_plus.Location = new System.Drawing.Point(161, 85);
            this.bt_font_size_plus.Name = "bt_font_size_plus";
            this.bt_font_size_plus.Size = new System.Drawing.Size(112, 40);
            this.bt_font_size_plus.TabIndex = 14;
            this.bt_font_size_plus.Text = "字體 +";
            this.bt_font_size_plus.UseVisualStyleBackColor = true;
            this.bt_font_size_plus.Click += new System.EventHandler(this.bt_font_size_plus_Click);
            // 
            // bt_fontname1
            // 
            this.bt_fontname1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_fontname1.Location = new System.Drawing.Point(298, 85);
            this.bt_fontname1.Name = "bt_fontname1";
            this.bt_fontname1.Size = new System.Drawing.Size(112, 40);
            this.bt_fontname1.TabIndex = 6;
            this.bt_fontname1.Text = "標楷體";
            this.bt_fontname1.UseVisualStyleBackColor = true;
            this.bt_fontname1.Click += new System.EventHandler(this.bt_fontname1_Click);
            // 
            // bt_fontname2
            // 
            this.bt_fontname2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_fontname2.Location = new System.Drawing.Point(427, 85);
            this.bt_fontname2.Name = "bt_fontname2";
            this.bt_fontname2.Size = new System.Drawing.Size(112, 40);
            this.bt_fontname2.TabIndex = 7;
            this.bt_fontname2.Text = "新細明體";
            this.bt_fontname2.UseVisualStyleBackColor = true;
            this.bt_fontname2.Click += new System.EventHandler(this.bt_fontname2_Click);
            // 
            // bt_speed_minus
            // 
            this.bt_speed_minus.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_speed_minus.Location = new System.Drawing.Point(12, 409);
            this.bt_speed_minus.Name = "bt_speed_minus";
            this.bt_speed_minus.Size = new System.Drawing.Size(112, 40);
            this.bt_speed_minus.TabIndex = 15;
            this.bt_speed_minus.Text = "速度 -";
            this.bt_speed_minus.UseVisualStyleBackColor = true;
            this.bt_speed_minus.Click += new System.EventHandler(this.bt_speed_minus_Click);
            // 
            // bt_speed_plus
            // 
            this.bt_speed_plus.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_speed_plus.Location = new System.Drawing.Point(130, 410);
            this.bt_speed_plus.Name = "bt_speed_plus";
            this.bt_speed_plus.Size = new System.Drawing.Size(112, 40);
            this.bt_speed_plus.TabIndex = 15;
            this.bt_speed_plus.Text = "速度 +";
            this.bt_speed_plus.UseVisualStyleBackColor = true;
            this.bt_speed_plus.Click += new System.EventHandler(this.bt_speed_plus_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(752, 595);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 32;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_background_color
            // 
            this.bt_background_color.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_background_color.Location = new System.Drawing.Point(248, 410);
            this.bt_background_color.Name = "bt_background_color";
            this.bt_background_color.Size = new System.Drawing.Size(112, 40);
            this.bt_background_color.TabIndex = 33;
            this.bt_background_color.Text = "背景色";
            this.bt_background_color.UseVisualStyleBackColor = true;
            this.bt_background_color.Click += new System.EventHandler(this.bt_background_color_Click);
            // 
            // bt_open_picture
            // 
            this.bt_open_picture.BackgroundImage = global::vcs_Draw6_String4.Properties.Resources.Unification_Church_symbol_svg;
            this.bt_open_picture.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_picture.Location = new System.Drawing.Point(712, 350);
            this.bt_open_picture.Name = "bt_open_picture";
            this.bt_open_picture.Size = new System.Drawing.Size(100, 100);
            this.bt_open_picture.TabIndex = 249;
            this.bt_open_picture.UseVisualStyleBackColor = true;
            this.bt_open_picture.Click += new System.EventHandler(this.bt_open_picture_Click);
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Location = new System.Drawing.Point(367, 344);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(272, 106);
            this.groupBox_selection.TabIndex = 250;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "位置設定";
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(179, 65);
            this.nud_h.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_h.Name = "nud_h";
            this.nud_h.Size = new System.Drawing.Size(74, 33);
            this.nud_h.TabIndex = 16;
            this.nud_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_x_st
            // 
            this.lb_x_st.AutoSize = true;
            this.lb_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_x_st.Location = new System.Drawing.Point(13, 23);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(47, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x_st";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(179, 22);
            this.nud_w.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_w.Name = "nud_w";
            this.nud_w.Size = new System.Drawing.Size(74, 33);
            this.nud_w.TabIndex = 15;
            this.nud_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(155, 65);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(66, 65);
            this.nud_y_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_y_st.Name = "nud_y_st";
            this.nud_y_st.Size = new System.Drawing.Size(74, 33);
            this.nud_y_st.TabIndex = 14;
            this.nud_y_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // nud_x_st
            // 
            this.nud_x_st.Enabled = false;
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(66, 22);
            this.nud_x_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_x_st.Name = "nud_x_st";
            this.nud_x_st.Size = new System.Drawing.Size(74, 33);
            this.nud_x_st.TabIndex = 13;
            this.nud_x_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_y_st
            // 
            this.lb_y_st.AutoSize = true;
            this.lb_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y_st.Location = new System.Drawing.Point(13, 65);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(47, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y_st";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(152, 27);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(824, 639);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.bt_open_picture);
            this.Controls.Add(this.bt_background_color);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.bt_speed_plus);
            this.Controls.Add(this.bt_speed_minus);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.button2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Button bt_font_size_10;
        private System.Windows.Forms.CheckBox cb_font_style3;
        private System.Windows.Forms.Button bt_font_setup;
        private System.Windows.Forms.Button bt_font_size_20;
        private System.Windows.Forms.CheckBox cb_font_style2;
        private System.Windows.Forms.Button bt_font_size_30;
        private System.Windows.Forms.Button bt_font_size_minus;
        private System.Windows.Forms.Button bt_font_size_40;
        private System.Windows.Forms.CheckBox cb_font_style1;
        private System.Windows.Forms.Button bt_font_size_50;
        private System.Windows.Forms.Button bt_font_size_plus;
        private System.Windows.Forms.Button bt_fontname1;
        private System.Windows.Forms.Button bt_fontname2;
        private System.Windows.Forms.Button bt_speed_minus;
        private System.Windows.Forms.Button bt_speed_plus;
        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_background_color;
        private System.Windows.Forms.Button bt_open_picture;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
    }
}

