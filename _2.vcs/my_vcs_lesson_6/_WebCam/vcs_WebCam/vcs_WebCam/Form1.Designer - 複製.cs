namespace vcs_WebCam
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.lb_rgb_r = new System.Windows.Forms.Label();
            this.lb_rgb_g = new System.Windows.Forms.Label();
            this.lb_rgb_b = new System.Windows.Forms.Label();
            this.lb_yuv_y = new System.Windows.Forms.Label();
            this.lb_yuv_u = new System.Windows.Forms.Label();
            this.lb_yuv_v = new System.Windows.Forms.Label();
            this.lb_fps = new System.Windows.Forms.Label();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.bt_cellphone = new System.Windows.Forms.Button();
            this.cb_rgb = new System.Windows.Forms.CheckBox();
            this.bt_open_folder = new System.Windows.Forms.Button();
            this.bt_motion_detection = new System.Windows.Forms.Button();
            this.bt_record = new System.Windows.Forms.Button();
            this.rb_5X5 = new System.Windows.Forms.RadioButton();
            this.rb_4X4 = new System.Windows.Forms.RadioButton();
            this.rb_3X3 = new System.Windows.Forms.RadioButton();
            this.cb_show_grid = new System.Windows.Forms.CheckBox();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.bt_help = new System.Windows.Forms.Button();
            this.cb_image_processing = new System.Windows.Forms.CheckBox();
            this.cb_auto_save = new System.Windows.Forms.CheckBox();
            this.bt_fullscreen = new System.Windows.Forms.Button();
            this.cb_show_time = new System.Windows.Forms.CheckBox();
            this.bt_start = new System.Windows.Forms.Button();
            this.bt_info = new System.Windows.Forms.Button();
            this.bt_pause = new System.Windows.Forms.Button();
            this.bt_stop = new System.Windows.Forms.Button();
            this.bt_exit = new System.Windows.Forms.Button();
            this.bt_refresh = new System.Windows.Forms.Button();
            this.bt_snapshot = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.comboBox3 = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.checkBox3 = new System.Windows.Forms.CheckBox();
            this.checkBox2 = new System.Windows.Forms.CheckBox();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.timer_clock = new System.Windows.Forms.Timer(this.components);
            this.timer_auto_save = new System.Windows.Forms.Timer(this.components);
            this.timer_qr_code = new System.Windows.Forms.Timer(this.components);
            this.timer_rgb = new System.Windows.Forms.Timer(this.components);
            this.groupBox1.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.groupBox5);
            this.groupBox1.Controls.Add(this.groupBox4);
            this.groupBox1.Controls.Add(this.groupBox3);
            this.groupBox1.Controls.Add(this.groupBox2);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(1270, 272);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.panel1);
            this.groupBox5.Controls.Add(this.lb_rgb_r);
            this.groupBox5.Controls.Add(this.lb_rgb_g);
            this.groupBox5.Controls.Add(this.lb_rgb_b);
            this.groupBox5.Controls.Add(this.lb_yuv_y);
            this.groupBox5.Controls.Add(this.lb_yuv_u);
            this.groupBox5.Controls.Add(this.lb_yuv_v);
            this.groupBox5.Controls.Add(this.lb_fps);
            this.groupBox5.Controls.Add(this.lb_main_mesg);
            this.groupBox5.Location = new System.Drawing.Point(958, 37);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(254, 212);
            this.groupBox5.TabIndex = 17;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Message";
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(143, 74);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(90, 60);
            this.panel1.TabIndex = 203;
            // 
            // lb_rgb_r
            // 
            this.lb_rgb_r.AutoSize = true;
            this.lb_rgb_r.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_r.ForeColor = System.Drawing.Color.Red;
            this.lb_rgb_r.Location = new System.Drawing.Point(68, 164);
            this.lb_rgb_r.Name = "lb_rgb_r";
            this.lb_rgb_r.Size = new System.Drawing.Size(25, 28);
            this.lb_rgb_r.TabIndex = 197;
            this.lb_rgb_r.Text = "R";
            // 
            // lb_rgb_g
            // 
            this.lb_rgb_g.AutoSize = true;
            this.lb_rgb_g.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_g.ForeColor = System.Drawing.Color.Green;
            this.lb_rgb_g.Location = new System.Drawing.Point(85, 164);
            this.lb_rgb_g.Name = "lb_rgb_g";
            this.lb_rgb_g.Size = new System.Drawing.Size(25, 28);
            this.lb_rgb_g.TabIndex = 198;
            this.lb_rgb_g.Text = "G";
            // 
            // lb_rgb_b
            // 
            this.lb_rgb_b.AutoSize = true;
            this.lb_rgb_b.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_b.ForeColor = System.Drawing.Color.Blue;
            this.lb_rgb_b.Location = new System.Drawing.Point(103, 164);
            this.lb_rgb_b.Name = "lb_rgb_b";
            this.lb_rgb_b.Size = new System.Drawing.Size(25, 28);
            this.lb_rgb_b.TabIndex = 199;
            this.lb_rgb_b.Text = "B";
            // 
            // lb_yuv_y
            // 
            this.lb_yuv_y.AutoSize = true;
            this.lb_yuv_y.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_y.ForeColor = System.Drawing.Color.Gold;
            this.lb_yuv_y.Location = new System.Drawing.Point(138, 164);
            this.lb_yuv_y.Name = "lb_yuv_y";
            this.lb_yuv_y.Size = new System.Drawing.Size(25, 28);
            this.lb_yuv_y.TabIndex = 200;
            this.lb_yuv_y.Text = "Y";
            // 
            // lb_yuv_u
            // 
            this.lb_yuv_u.AutoSize = true;
            this.lb_yuv_u.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_u.ForeColor = System.Drawing.Color.Blue;
            this.lb_yuv_u.Location = new System.Drawing.Point(159, 164);
            this.lb_yuv_u.Name = "lb_yuv_u";
            this.lb_yuv_u.Size = new System.Drawing.Size(25, 28);
            this.lb_yuv_u.TabIndex = 201;
            this.lb_yuv_u.Text = "U";
            // 
            // lb_yuv_v
            // 
            this.lb_yuv_v.AutoSize = true;
            this.lb_yuv_v.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_v.ForeColor = System.Drawing.Color.Red;
            this.lb_yuv_v.Location = new System.Drawing.Point(190, 164);
            this.lb_yuv_v.Name = "lb_yuv_v";
            this.lb_yuv_v.Size = new System.Drawing.Size(25, 28);
            this.lb_yuv_v.TabIndex = 202;
            this.lb_yuv_v.Text = "V";
            // 
            // lb_fps
            // 
            this.lb_fps.AutoSize = true;
            this.lb_fps.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_fps.Location = new System.Drawing.Point(24, 100);
            this.lb_fps.Name = "lb_fps";
            this.lb_fps.Size = new System.Drawing.Size(35, 21);
            this.lb_fps.TabIndex = 11;
            this.lb_fps.Text = "fps";
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(24, 39);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(154, 24);
            this.lb_main_mesg.TabIndex = 16;
            this.lb_main_mesg.Text = "lb_main_mesg";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.bt_cellphone);
            this.groupBox4.Controls.Add(this.cb_rgb);
            this.groupBox4.Controls.Add(this.bt_open_folder);
            this.groupBox4.Controls.Add(this.bt_motion_detection);
            this.groupBox4.Controls.Add(this.bt_record);
            this.groupBox4.Controls.Add(this.rb_5X5);
            this.groupBox4.Controls.Add(this.rb_4X4);
            this.groupBox4.Controls.Add(this.rb_3X3);
            this.groupBox4.Controls.Add(this.cb_show_grid);
            this.groupBox4.Controls.Add(this.rb3);
            this.groupBox4.Controls.Add(this.rb2);
            this.groupBox4.Controls.Add(this.rb1);
            this.groupBox4.Controls.Add(this.bt_help);
            this.groupBox4.Controls.Add(this.cb_image_processing);
            this.groupBox4.Controls.Add(this.cb_auto_save);
            this.groupBox4.Controls.Add(this.bt_fullscreen);
            this.groupBox4.Controls.Add(this.cb_show_time);
            this.groupBox4.Controls.Add(this.bt_start);
            this.groupBox4.Controls.Add(this.bt_info);
            this.groupBox4.Controls.Add(this.bt_pause);
            this.groupBox4.Controls.Add(this.bt_stop);
            this.groupBox4.Controls.Add(this.bt_exit);
            this.groupBox4.Controls.Add(this.bt_refresh);
            this.groupBox4.Controls.Add(this.bt_snapshot);
            this.groupBox4.Location = new System.Drawing.Point(496, 30);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(384, 215);
            this.groupBox4.TabIndex = 1;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Operation";
            // 
            // bt_cellphone
            // 
            this.bt_cellphone.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_cellphone.Location = new System.Drawing.Point(184, 122);
            this.bt_cellphone.Name = "bt_cellphone";
            this.bt_cellphone.Size = new System.Drawing.Size(75, 30);
            this.bt_cellphone.TabIndex = 61;
            this.bt_cellphone.Text = "手機啟動";
            this.bt_cellphone.UseVisualStyleBackColor = true;
            this.bt_cellphone.Click += new System.EventHandler(this.bt_cellphone_Click);
            // 
            // cb_rgb
            // 
            this.cb_rgb.AutoSize = true;
            this.cb_rgb.Checked = true;
            this.cb_rgb.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_rgb.Location = new System.Drawing.Point(18, 193);
            this.cb_rgb.Name = "cb_rgb";
            this.cb_rgb.Size = new System.Drawing.Size(48, 16);
            this.cb_rgb.TabIndex = 60;
            this.cb_rgb.Text = "RGB";
            this.cb_rgb.UseVisualStyleBackColor = true;
            this.cb_rgb.CheckedChanged += new System.EventHandler(this.cb_rgb_CheckedChanged);
            // 
            // bt_open_folder
            // 
            this.bt_open_folder.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_folder.Location = new System.Drawing.Point(319, 150);
            this.bt_open_folder.Name = "bt_open_folder";
            this.bt_open_folder.Size = new System.Drawing.Size(55, 55);
            this.bt_open_folder.TabIndex = 59;
            this.bt_open_folder.UseVisualStyleBackColor = true;
            this.bt_open_folder.Click += new System.EventHandler(this.bt_open_folder_Click);
            // 
            // bt_motion_detection
            // 
            this.bt_motion_detection.Font = new System.Drawing.Font("新細明體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_motion_detection.Location = new System.Drawing.Point(188, 80);
            this.bt_motion_detection.Name = "bt_motion_detection";
            this.bt_motion_detection.Size = new System.Drawing.Size(75, 30);
            this.bt_motion_detection.TabIndex = 24;
            this.bt_motion_detection.Text = "移動偵測";
            this.bt_motion_detection.UseVisualStyleBackColor = true;
            this.bt_motion_detection.Click += new System.EventHandler(this.bt_motion_detection_Click);
            // 
            // bt_record
            // 
            this.bt_record.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_record.Location = new System.Drawing.Point(269, 38);
            this.bt_record.Name = "bt_record";
            this.bt_record.Size = new System.Drawing.Size(75, 30);
            this.bt_record.TabIndex = 23;
            this.bt_record.Text = "錄影";
            this.bt_record.UseVisualStyleBackColor = true;
            this.bt_record.Click += new System.EventHandler(this.bt_record_Click);
            // 
            // rb_5X5
            // 
            this.rb_5X5.AutoSize = true;
            this.rb_5X5.Location = new System.Drawing.Point(319, 144);
            this.rb_5X5.Name = "rb_5X5";
            this.rb_5X5.Size = new System.Drawing.Size(43, 16);
            this.rb_5X5.TabIndex = 22;
            this.rb_5X5.Text = "5X5";
            this.rb_5X5.UseVisualStyleBackColor = true;
            // 
            // rb_4X4
            // 
            this.rb_4X4.AutoSize = true;
            this.rb_4X4.Checked = true;
            this.rb_4X4.Location = new System.Drawing.Point(319, 122);
            this.rb_4X4.Name = "rb_4X4";
            this.rb_4X4.Size = new System.Drawing.Size(43, 16);
            this.rb_4X4.TabIndex = 21;
            this.rb_4X4.TabStop = true;
            this.rb_4X4.Text = "4X4";
            this.rb_4X4.UseVisualStyleBackColor = true;
            // 
            // rb_3X3
            // 
            this.rb_3X3.AutoSize = true;
            this.rb_3X3.Location = new System.Drawing.Point(319, 100);
            this.rb_3X3.Name = "rb_3X3";
            this.rb_3X3.Size = new System.Drawing.Size(43, 16);
            this.rb_3X3.TabIndex = 20;
            this.rb_3X3.Text = "3X3";
            this.rb_3X3.UseVisualStyleBackColor = true;
            // 
            // cb_show_grid
            // 
            this.cb_show_grid.AutoSize = true;
            this.cb_show_grid.Location = new System.Drawing.Point(242, 193);
            this.cb_show_grid.Name = "cb_show_grid";
            this.cb_show_grid.Size = new System.Drawing.Size(48, 16);
            this.cb_show_grid.TabIndex = 19;
            this.cb_show_grid.Text = "格線";
            this.cb_show_grid.UseVisualStyleBackColor = true;
            this.cb_show_grid.CheckedChanged += new System.EventHandler(this.cb_show_grid_CheckedChanged);
            // 
            // rb3
            // 
            this.rb3.AutoSize = true;
            this.rb3.Location = new System.Drawing.Point(210, 193);
            this.rb3.Name = "rb3";
            this.rb3.Size = new System.Drawing.Size(29, 16);
            this.rb3.TabIndex = 18;
            this.rb3.Text = "3";
            this.rb3.UseVisualStyleBackColor = true;
            this.rb3.CheckedChanged += new System.EventHandler(this.rb_processing_CheckedChanged);
            // 
            // rb2
            // 
            this.rb2.AutoSize = true;
            this.rb2.Location = new System.Drawing.Point(175, 193);
            this.rb2.Name = "rb2";
            this.rb2.Size = new System.Drawing.Size(29, 16);
            this.rb2.TabIndex = 17;
            this.rb2.Text = "2";
            this.rb2.UseVisualStyleBackColor = true;
            this.rb2.CheckedChanged += new System.EventHandler(this.rb_processing_CheckedChanged);
            // 
            // rb1
            // 
            this.rb1.AutoSize = true;
            this.rb1.Checked = true;
            this.rb1.Location = new System.Drawing.Point(150, 194);
            this.rb1.Name = "rb1";
            this.rb1.Size = new System.Drawing.Size(29, 16);
            this.rb1.TabIndex = 5;
            this.rb1.TabStop = true;
            this.rb1.Text = "1";
            this.rb1.UseVisualStyleBackColor = true;
            this.rb1.CheckedChanged += new System.EventHandler(this.rb_processing_CheckedChanged);
            // 
            // bt_help
            // 
            this.bt_help.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_help.Location = new System.Drawing.Point(247, 122);
            this.bt_help.Name = "bt_help";
            this.bt_help.Size = new System.Drawing.Size(75, 30);
            this.bt_help.TabIndex = 16;
            this.bt_help.Text = "Help";
            this.bt_help.UseVisualStyleBackColor = true;
            this.bt_help.Click += new System.EventHandler(this.bt_help_Click);
            // 
            // cb_image_processing
            // 
            this.cb_image_processing.AutoSize = true;
            this.cb_image_processing.Location = new System.Drawing.Point(103, 174);
            this.cb_image_processing.Name = "cb_image_processing";
            this.cb_image_processing.Size = new System.Drawing.Size(48, 16);
            this.cb_image_processing.TabIndex = 15;
            this.cb_image_processing.Text = "處裡";
            this.cb_image_processing.UseVisualStyleBackColor = true;
            // 
            // cb_auto_save
            // 
            this.cb_auto_save.AutoSize = true;
            this.cb_auto_save.Location = new System.Drawing.Point(218, 173);
            this.cb_auto_save.Name = "cb_auto_save";
            this.cb_auto_save.Size = new System.Drawing.Size(72, 16);
            this.cb_auto_save.TabIndex = 14;
            this.cb_auto_save.Text = "自動存檔";
            this.cb_auto_save.UseVisualStyleBackColor = true;
            this.cb_auto_save.CheckedChanged += new System.EventHandler(this.cb_auto_save_CheckedChanged);
            // 
            // bt_fullscreen
            // 
            this.bt_fullscreen.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_fullscreen.Location = new System.Drawing.Point(103, 122);
            this.bt_fullscreen.Name = "bt_fullscreen";
            this.bt_fullscreen.Size = new System.Drawing.Size(75, 30);
            this.bt_fullscreen.TabIndex = 13;
            this.bt_fullscreen.Text = "全螢幕";
            this.bt_fullscreen.UseVisualStyleBackColor = true;
            this.bt_fullscreen.Click += new System.EventHandler(this.bt_fullscreen_Click);
            // 
            // cb_show_time
            // 
            this.cb_show_time.AutoSize = true;
            this.cb_show_time.Checked = true;
            this.cb_show_time.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_show_time.Location = new System.Drawing.Point(18, 173);
            this.cb_show_time.Name = "cb_show_time";
            this.cb_show_time.Size = new System.Drawing.Size(72, 16);
            this.cb_show_time.TabIndex = 5;
            this.cb_show_time.Text = "顯示時間";
            this.cb_show_time.UseVisualStyleBackColor = true;
            // 
            // bt_start
            // 
            this.bt_start.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_start.Location = new System.Drawing.Point(18, 38);
            this.bt_start.Name = "bt_start";
            this.bt_start.Size = new System.Drawing.Size(75, 30);
            this.bt_start.TabIndex = 5;
            this.bt_start.Text = "啟動";
            this.bt_start.UseVisualStyleBackColor = true;
            this.bt_start.Click += new System.EventHandler(this.bt_start_Click);
            // 
            // bt_info
            // 
            this.bt_info.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_info.Location = new System.Drawing.Point(18, 122);
            this.bt_info.Name = "bt_info";
            this.bt_info.Size = new System.Drawing.Size(75, 30);
            this.bt_info.TabIndex = 12;
            this.bt_info.Text = "Info";
            this.bt_info.UseVisualStyleBackColor = true;
            this.bt_info.Click += new System.EventHandler(this.bt_info_Click);
            // 
            // bt_pause
            // 
            this.bt_pause.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_pause.Location = new System.Drawing.Point(103, 38);
            this.bt_pause.Name = "bt_pause";
            this.bt_pause.Size = new System.Drawing.Size(75, 30);
            this.bt_pause.TabIndex = 6;
            this.bt_pause.Text = "暫停";
            this.bt_pause.UseVisualStyleBackColor = true;
            this.bt_pause.Click += new System.EventHandler(this.bt_pause_Click);
            // 
            // bt_stop
            // 
            this.bt_stop.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_stop.Location = new System.Drawing.Point(188, 38);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(75, 30);
            this.bt_stop.TabIndex = 7;
            this.bt_stop.Text = "停止";
            this.bt_stop.UseVisualStyleBackColor = true;
            this.bt_stop.Click += new System.EventHandler(this.bt_stop_Click);
            // 
            // bt_exit
            // 
            this.bt_exit.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_exit.Location = new System.Drawing.Point(269, 70);
            this.bt_exit.Name = "bt_exit";
            this.bt_exit.Size = new System.Drawing.Size(75, 30);
            this.bt_exit.TabIndex = 10;
            this.bt_exit.Text = "離開";
            this.bt_exit.UseVisualStyleBackColor = true;
            this.bt_exit.Click += new System.EventHandler(this.bt_exit_Click);
            // 
            // bt_refresh
            // 
            this.bt_refresh.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_refresh.Location = new System.Drawing.Point(18, 80);
            this.bt_refresh.Name = "bt_refresh";
            this.bt_refresh.Size = new System.Drawing.Size(75, 30);
            this.bt_refresh.TabIndex = 8;
            this.bt_refresh.Text = "重抓";
            this.bt_refresh.UseVisualStyleBackColor = true;
            this.bt_refresh.Click += new System.EventHandler(this.bt_refresh_Click);
            // 
            // bt_snapshot
            // 
            this.bt_snapshot.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_snapshot.Location = new System.Drawing.Point(103, 80);
            this.bt_snapshot.Name = "bt_snapshot";
            this.bt_snapshot.Size = new System.Drawing.Size(75, 30);
            this.bt_snapshot.TabIndex = 9;
            this.bt_snapshot.Text = "截圖";
            this.bt_snapshot.UseVisualStyleBackColor = true;
            this.bt_snapshot.Click += new System.EventHandler(this.bt_snapshot_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.label3);
            this.groupBox3.Controls.Add(this.comboBox3);
            this.groupBox3.Controls.Add(this.label2);
            this.groupBox3.Controls.Add(this.comboBox1);
            this.groupBox3.Controls.Add(this.comboBox2);
            this.groupBox3.Controls.Add(this.label1);
            this.groupBox3.Location = new System.Drawing.Point(233, 30);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(257, 219);
            this.groupBox3.TabIndex = 1;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "WebCam";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(26, 147);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 19);
            this.label3.TabIndex = 14;
            this.label3.Text = "方向";
            // 
            // comboBox3
            // 
            this.comboBox3.FormattingEnabled = true;
            this.comboBox3.Items.AddRange(new object[] {
            "不鏡射也不旋轉",
            "水平鏡射",
            "垂直鏡射",
            "水平 & 垂直鏡射",
            "90°旋轉",
            "90°旋轉 + 水平鏡射",
            "90°旋轉 + 垂直鏡射",
            "90°旋轉 + 水平 & 垂直鏡射",
            "180°旋轉",
            "180°旋轉 + 水平鏡射",
            "180°旋轉 + 垂直鏡射",
            "180°旋轉 + 水平 & 垂直鏡射",
            "270°旋轉",
            "270°旋轉 + 水平鏡射",
            "270°旋轉 + 垂直鏡射",
            "270°旋轉 + 水平 & 垂直鏡射"});
            this.comboBox3.Location = new System.Drawing.Point(29, 173);
            this.comboBox3.Name = "comboBox3";
            this.comboBox3.Size = new System.Drawing.Size(192, 20);
            this.comboBox3.TabIndex = 3;
            this.comboBox3.SelectedIndexChanged += new System.EventHandler(this.comboBox3_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(26, 81);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(66, 19);
            this.label2.TabIndex = 13;
            this.label2.Text = "解析度";
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(29, 57);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(192, 20);
            this.comboBox1.TabIndex = 1;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Location = new System.Drawing.Point(29, 114);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(192, 20);
            this.comboBox2.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(25, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 19);
            this.label1.TabIndex = 4;
            this.label1.Text = "相機";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.checkBox3);
            this.groupBox2.Controls.Add(this.checkBox2);
            this.groupBox2.Controls.Add(this.checkBox1);
            this.groupBox2.Controls.Add(this.radioButton2);
            this.groupBox2.Controls.Add(this.radioButton1);
            this.groupBox2.Location = new System.Drawing.Point(17, 30);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(157, 215);
            this.groupBox2.TabIndex = 0;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Method";
            // 
            // checkBox3
            // 
            this.checkBox3.AutoSize = true;
            this.checkBox3.Checked = true;
            this.checkBox3.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox3.Location = new System.Drawing.Point(18, 183);
            this.checkBox3.Name = "checkBox3";
            this.checkBox3.Size = new System.Drawing.Size(55, 16);
            this.checkBox3.TabIndex = 4;
            this.checkBox3.Text = "Debug";
            this.checkBox3.UseVisualStyleBackColor = true;
            this.checkBox3.CheckedChanged += new System.EventHandler(this.checkBox3_CheckedChanged);
            // 
            // checkBox2
            // 
            this.checkBox2.AutoSize = true;
            this.checkBox2.Location = new System.Drawing.Point(18, 72);
            this.checkBox2.Name = "checkBox2";
            this.checkBox2.Size = new System.Drawing.Size(57, 16);
            this.checkBox2.TabIndex = 3;
            this.checkBox2.Text = "EMGU";
            this.checkBox2.UseVisualStyleBackColor = true;
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Checked = true;
            this.checkBox1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox1.Location = new System.Drawing.Point(18, 32);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(59, 16);
            this.checkBox1.TabIndex = 2;
            this.checkBox1.Text = "AForge";
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(80, 143);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(41, 16);
            this.radioButton2.TabIndex = 1;
            this.radioButton2.Text = "x64";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Checked = true;
            this.radioButton1.Location = new System.Drawing.Point(80, 105);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(41, 16);
            this.radioButton1.TabIndex = 0;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "x86";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(570, 301);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(421, 273);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Pink;
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 301);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(464, 248);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDoubleClick);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(916, 538);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(75, 36);
            this.bt_clear.TabIndex = 15;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // timer_clock
            // 
            this.timer_clock.Enabled = true;
            this.timer_clock.Interval = 1000;
            this.timer_clock.Tick += new System.EventHandler(this.timer_clock_Tick);
            // 
            // timer_auto_save
            // 
            this.timer_auto_save.Interval = 3000;
            this.timer_auto_save.Tick += new System.EventHandler(this.timer_auto_save_Tick);
            // 
            // timer_qr_code
            // 
            this.timer_qr_code.Interval = 1000;
            this.timer_qr_code.Tick += new System.EventHandler(this.timer_qr_code_Tick);
            // 
            // timer_rgb
            // 
            this.timer_rgb.Enabled = true;
            this.timer_rgb.Tick += new System.EventHandler(this.timer_rgb_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1244, 761);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "WebCam";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_exit;
        private System.Windows.Forms.Button bt_snapshot;
        private System.Windows.Forms.Button bt_refresh;
        private System.Windows.Forms.Button bt_stop;
        private System.Windows.Forms.Button bt_pause;
        private System.Windows.Forms.Button bt_start;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox comboBox3;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.CheckBox checkBox3;
        private System.Windows.Forms.CheckBox checkBox2;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.Label lb_fps;
        private System.Windows.Forms.Button bt_info;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.CheckBox cb_show_time;
        private System.Windows.Forms.Button bt_fullscreen;
        private System.Windows.Forms.CheckBox cb_auto_save;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.CheckBox cb_image_processing;
        private System.Windows.Forms.Timer timer_clock;
        private System.Windows.Forms.Timer timer_auto_save;
        private System.Windows.Forms.Button bt_help;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.Timer timer_qr_code;
        private System.Windows.Forms.CheckBox cb_show_grid;
        private System.Windows.Forms.RadioButton rb_5X5;
        private System.Windows.Forms.RadioButton rb_4X4;
        private System.Windows.Forms.RadioButton rb_3X3;
        private System.Windows.Forms.Button bt_record;
        private System.Windows.Forms.Button bt_motion_detection;
        private System.Windows.Forms.Button bt_open_folder;
        private System.Windows.Forms.CheckBox cb_rgb;
        private System.Windows.Forms.Timer timer_rgb;
        private System.Windows.Forms.Label lb_rgb_r;
        private System.Windows.Forms.Label lb_rgb_g;
        private System.Windows.Forms.Label lb_rgb_b;
        private System.Windows.Forms.Label lb_yuv_y;
        private System.Windows.Forms.Label lb_yuv_u;
        private System.Windows.Forms.Label lb_yuv_v;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button bt_cellphone;
    }
}

