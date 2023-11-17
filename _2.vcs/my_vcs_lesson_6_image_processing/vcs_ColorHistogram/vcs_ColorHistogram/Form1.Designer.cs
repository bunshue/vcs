namespace vcs_ColorHistogram
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox0 = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.bt_open_picture = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.rb_selection3 = new System.Windows.Forms.RadioButton();
            this.rb_selection2 = new System.Windows.Forms.RadioButton();
            this.rb_selection1 = new System.Windows.Forms.RadioButton();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.tb_filename = new System.Windows.Forms.TextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox_control = new System.Windows.Forms.GroupBox();
            this.bt_save_picture = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.lb_rgb_r = new System.Windows.Forms.Label();
            this.lb_rgb_g = new System.Windows.Forms.Label();
            this.lb_rgb_b = new System.Windows.Forms.Label();
            this.lb_yuv_y = new System.Windows.Forms.Label();
            this.lb_yuv_u = new System.Windows.Forms.Label();
            this.lb_yuv_v = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox_color = new System.Windows.Forms.GroupBox();
            this.timer_rgb = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            this.groupBox_control.SuspendLayout();
            this.groupBox_color.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(118, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 25;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox0
            // 
            this.pictureBox0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox0.Location = new System.Drawing.Point(12, 12);
            this.pictureBox0.Name = "pictureBox0";
            this.pictureBox0.Size = new System.Drawing.Size(100, 100);
            this.pictureBox0.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox0.TabIndex = 24;
            this.pictureBox0.TabStop = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(92, 20);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(80, 40);
            this.button1.TabIndex = 28;
            this.button1.Text = "亮度量測";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(25, 190);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 30;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 135);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 29;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(178, 20);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(80, 40);
            this.button2.TabIndex = 31;
            this.button2.Text = "Channel 交換";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(6, 68);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(80, 40);
            this.button3.TabIndex = 32;
            this.button3.Text = "統計";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(6, 20);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(80, 40);
            this.button0.TabIndex = 33;
            this.button0.Text = "灰階";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // bt_open_picture
            // 
            this.bt_open_picture.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_picture.Location = new System.Drawing.Point(264, 20);
            this.bt_open_picture.Name = "bt_open_picture";
            this.bt_open_picture.Size = new System.Drawing.Size(60, 60);
            this.bt_open_picture.TabIndex = 249;
            this.bt_open_picture.UseVisualStyleBackColor = true;
            this.bt_open_picture.Click += new System.EventHandler(this.bt_open_picture_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(92, 68);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(80, 40);
            this.button4.TabIndex = 250;
            this.button4.Text = "停止統計";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(178, 66);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(80, 40);
            this.button5.TabIndex = 251;
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(6, 121);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(80, 40);
            this.button6.TabIndex = 252;
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(92, 121);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(80, 40);
            this.button7.TabIndex = 253;
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.rb_selection3);
            this.groupBox_selection.Controls.Add(this.rb_selection2);
            this.groupBox_selection.Controls.Add(this.rb_selection1);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Location = new System.Drawing.Point(224, 190);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(238, 193);
            this.groupBox_selection.TabIndex = 254;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // rb_selection3
            // 
            this.rb_selection3.AutoSize = true;
            this.rb_selection3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_selection3.Location = new System.Drawing.Point(179, 75);
            this.rb_selection3.Name = "rb_selection3";
            this.rb_selection3.Size = new System.Drawing.Size(42, 20);
            this.rb_selection3.TabIndex = 22;
            this.rb_selection3.Text = "小";
            this.rb_selection3.UseVisualStyleBackColor = true;
            // 
            // rb_selection2
            // 
            this.rb_selection2.AutoSize = true;
            this.rb_selection2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_selection2.Location = new System.Drawing.Point(179, 49);
            this.rb_selection2.Name = "rb_selection2";
            this.rb_selection2.Size = new System.Drawing.Size(42, 20);
            this.rb_selection2.TabIndex = 21;
            this.rb_selection2.Text = "中";
            this.rb_selection2.UseVisualStyleBackColor = true;
            // 
            // rb_selection1
            // 
            this.rb_selection1.AutoSize = true;
            this.rb_selection1.Checked = true;
            this.rb_selection1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_selection1.Location = new System.Drawing.Point(179, 27);
            this.rb_selection1.Name = "rb_selection1";
            this.rb_selection1.Size = new System.Drawing.Size(42, 20);
            this.rb_selection1.TabIndex = 20;
            this.rb_selection1.TabStop = true;
            this.rb_selection1.Text = "大";
            this.rb_selection1.UseVisualStyleBackColor = true;
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(83, 152);
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
            this.lb_x_st.Location = new System.Drawing.Point(30, 27);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(47, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x_st";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(83, 110);
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
            this.lb_h.Location = new System.Drawing.Point(42, 153);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(83, 69);
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
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(83, 26);
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
            this.lb_y_st.Location = new System.Drawing.Point(30, 69);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(47, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y_st";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(42, 111);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // tb_filename
            // 
            this.tb_filename.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_filename.Location = new System.Drawing.Point(118, 135);
            this.tb_filename.Name = "tb_filename";
            this.tb_filename.Size = new System.Drawing.Size(100, 30);
            this.tb_filename.TabIndex = 255;
            // 
            // timer1
            // 
            this.timer1.Interval = 3000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // groupBox_control
            // 
            this.groupBox_control.Controls.Add(this.bt_save_picture);
            this.groupBox_control.Controls.Add(this.button8);
            this.groupBox_control.Controls.Add(this.bt_open_picture);
            this.groupBox_control.Controls.Add(this.button0);
            this.groupBox_control.Controls.Add(this.button1);
            this.groupBox_control.Controls.Add(this.button7);
            this.groupBox_control.Controls.Add(this.button2);
            this.groupBox_control.Controls.Add(this.button6);
            this.groupBox_control.Controls.Add(this.button3);
            this.groupBox_control.Controls.Add(this.button5);
            this.groupBox_control.Controls.Add(this.button4);
            this.groupBox_control.Location = new System.Drawing.Point(224, 12);
            this.groupBox_control.Name = "groupBox_control";
            this.groupBox_control.Size = new System.Drawing.Size(346, 172);
            this.groupBox_control.TabIndex = 256;
            this.groupBox_control.TabStop = false;
            this.groupBox_control.Text = "功能";
            // 
            // bt_save_picture
            // 
            this.bt_save_picture.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_save_picture.Location = new System.Drawing.Point(264, 93);
            this.bt_save_picture.Name = "bt_save_picture";
            this.bt_save_picture.Size = new System.Drawing.Size(60, 60);
            this.bt_save_picture.TabIndex = 255;
            this.bt_save_picture.UseVisualStyleBackColor = true;
            this.bt_save_picture.Click += new System.EventHandler(this.bt_save_picture_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(178, 121);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(80, 40);
            this.button8.TabIndex = 254;
            this.button8.Text = "Clear";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // lb_rgb_r
            // 
            this.lb_rgb_r.AutoSize = true;
            this.lb_rgb_r.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_r.ForeColor = System.Drawing.Color.Red;
            this.lb_rgb_r.Location = new System.Drawing.Point(18, 18);
            this.lb_rgb_r.Name = "lb_rgb_r";
            this.lb_rgb_r.Size = new System.Drawing.Size(30, 32);
            this.lb_rgb_r.TabIndex = 257;
            this.lb_rgb_r.Text = "R";
            // 
            // lb_rgb_g
            // 
            this.lb_rgb_g.AutoSize = true;
            this.lb_rgb_g.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_g.ForeColor = System.Drawing.Color.Green;
            this.lb_rgb_g.Location = new System.Drawing.Point(35, 18);
            this.lb_rgb_g.Name = "lb_rgb_g";
            this.lb_rgb_g.Size = new System.Drawing.Size(30, 32);
            this.lb_rgb_g.TabIndex = 258;
            this.lb_rgb_g.Text = "G";
            // 
            // lb_rgb_b
            // 
            this.lb_rgb_b.AutoSize = true;
            this.lb_rgb_b.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_rgb_b.ForeColor = System.Drawing.Color.Blue;
            this.lb_rgb_b.Location = new System.Drawing.Point(53, 18);
            this.lb_rgb_b.Name = "lb_rgb_b";
            this.lb_rgb_b.Size = new System.Drawing.Size(30, 32);
            this.lb_rgb_b.TabIndex = 259;
            this.lb_rgb_b.Text = "B";
            // 
            // lb_yuv_y
            // 
            this.lb_yuv_y.AutoSize = true;
            this.lb_yuv_y.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_y.ForeColor = System.Drawing.Color.Gold;
            this.lb_yuv_y.Location = new System.Drawing.Point(88, 18);
            this.lb_yuv_y.Name = "lb_yuv_y";
            this.lb_yuv_y.Size = new System.Drawing.Size(30, 32);
            this.lb_yuv_y.TabIndex = 260;
            this.lb_yuv_y.Text = "Y";
            // 
            // lb_yuv_u
            // 
            this.lb_yuv_u.AutoSize = true;
            this.lb_yuv_u.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_u.ForeColor = System.Drawing.Color.Blue;
            this.lb_yuv_u.Location = new System.Drawing.Point(109, 18);
            this.lb_yuv_u.Name = "lb_yuv_u";
            this.lb_yuv_u.Size = new System.Drawing.Size(30, 32);
            this.lb_yuv_u.TabIndex = 261;
            this.lb_yuv_u.Text = "U";
            // 
            // lb_yuv_v
            // 
            this.lb_yuv_v.AutoSize = true;
            this.lb_yuv_v.Font = new System.Drawing.Font("Consolas", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_yuv_v.ForeColor = System.Drawing.Color.Red;
            this.lb_yuv_v.Location = new System.Drawing.Point(140, 18);
            this.lb_yuv_v.Name = "lb_yuv_v";
            this.lb_yuv_v.Size = new System.Drawing.Size(30, 32);
            this.lb_yuv_v.TabIndex = 262;
            this.lb_yuv_v.Text = "V";
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(23, 49);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(90, 60);
            this.panel1.TabIndex = 263;
            // 
            // groupBox_color
            // 
            this.groupBox_color.Controls.Add(this.lb_rgb_r);
            this.groupBox_color.Controls.Add(this.panel1);
            this.groupBox_color.Controls.Add(this.lb_yuv_v);
            this.groupBox_color.Controls.Add(this.lb_yuv_u);
            this.groupBox_color.Controls.Add(this.lb_rgb_g);
            this.groupBox_color.Controls.Add(this.lb_yuv_y);
            this.groupBox_color.Controls.Add(this.lb_rgb_b);
            this.groupBox_color.Location = new System.Drawing.Point(18, 250);
            this.groupBox_color.Name = "groupBox_color";
            this.groupBox_color.Size = new System.Drawing.Size(200, 117);
            this.groupBox_color.TabIndex = 264;
            this.groupBox_color.TabStop = false;
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
            this.ClientSize = new System.Drawing.Size(763, 481);
            this.Controls.Add(this.groupBox_color);
            this.Controls.Add(this.groupBox_control);
            this.Controls.Add(this.tb_filename);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.pictureBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).EndInit();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            this.groupBox_control.ResumeLayout(false);
            this.groupBox_color.ResumeLayout(false);
            this.groupBox_color.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox0;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button bt_open_picture;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.RadioButton rb_selection2;
        private System.Windows.Forms.RadioButton rb_selection1;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.TextBox tb_filename;
        private System.Windows.Forms.RadioButton rb_selection3;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.GroupBox groupBox_control;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button bt_save_picture;
        private System.Windows.Forms.Label lb_rgb_r;
        private System.Windows.Forms.Label lb_rgb_g;
        private System.Windows.Forms.Label lb_rgb_b;
        private System.Windows.Forms.Label lb_yuv_y;
        private System.Windows.Forms.Label lb_yuv_u;
        private System.Windows.Forms.Label lb_yuv_v;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.GroupBox groupBox_color;
        private System.Windows.Forms.Timer timer_rgb;
    }
}

