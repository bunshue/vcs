namespace vcs_Draw3A
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.timer_rotate = new System.Windows.Forms.Timer(this.components);
            this.bt_clear = new System.Windows.Forms.Button();
            this.timer_random_rectangle = new System.Windows.Forms.Timer(this.components);
            this.picSample = new System.Windows.Forms.PictureBox();
            this.picRainbow = new System.Windows.Forms.PictureBox();
            this.timer_rainbow = new System.Windows.Forms.Timer(this.components);
            this.label1 = new System.Windows.Forms.Label();
            this.timer_battery = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_battery = new System.Windows.Forms.PictureBox();
            this.pictureBox_gear = new System.Windows.Forms.PictureBox();
            this.timer_gear = new System.Windows.Forms.Timer(this.components);
            this.trackBar1 = new System.Windows.Forms.TrackBar();
            this.lb_fps = new System.Windows.Forms.Label();
            this.pictureBox_atom = new System.Windows.Forms.PictureBox();
            this.timer_atom = new System.Windows.Forms.Timer(this.components);
            this.timer_card = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_card = new System.Windows.Forms.PictureBox();
            this.timer_card2 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_card2 = new System.Windows.Forms.PictureBox();
            this.timer_atom2 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_random = new System.Windows.Forms.PictureBox();
            this.timer_random = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_stock = new System.Windows.Forms.PictureBox();
            this.tipData = new System.Windows.Forms.ToolTip(this.components);
            this.timer_stock = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_rotate = new System.Windows.Forms.PictureBox();
            this.panel_radar = new System.Windows.Forms.Panel();
            this.pictureBox_radar = new System.Windows.Forms.PictureBox();
            this.timer_radar = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_hex = new System.Windows.Forms.PictureBox();
            this.timer_hex = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_random_color = new System.Windows.Forms.PictureBox();
            this.timer_random_color = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_battery2 = new System.Windows.Forms.PictureBox();
            this.lb_title00 = new System.Windows.Forms.Label();
            this.lb_title03 = new System.Windows.Forms.Label();
            this.lb_title02 = new System.Windows.Forms.Label();
            this.lb_title01 = new System.Windows.Forms.Label();
            this.lb_title_rotate = new System.Windows.Forms.Label();
            this.lb_title_hex = new System.Windows.Forms.Label();
            this.groupBox_rainbow = new System.Windows.Forms.GroupBox();
            this.groupBox_gear = new System.Windows.Forms.GroupBox();
            this.groupBox_random_color = new System.Windows.Forms.GroupBox();
            this.groupBox_battery = new System.Windows.Forms.GroupBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRainbow)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_battery)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gear)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_atom)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_card)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_card2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_stock)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_rotate)).BeginInit();
            this.panel_radar.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_radar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_hex)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random_color)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_battery2)).BeginInit();
            this.groupBox_rainbow.SuspendLayout();
            this.groupBox_gear.SuspendLayout();
            this.groupBox_random_color.SuspendLayout();
            this.groupBox_battery.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(985, 118);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.LightGreen;
            this.pictureBox1.Location = new System.Drawing.Point(985, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 15;
            this.pictureBox1.TabStop = false;
            // 
            // timer_rotate
            // 
            this.timer_rotate.Enabled = true;
            this.timer_rotate.Tick += new System.EventHandler(this.timer_rotate_Tick);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(999, 148);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(70, 30);
            this.bt_clear.TabIndex = 52;
            this.bt_clear.Text = "clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // timer_random_rectangle
            // 
            this.timer_random_rectangle.Tick += new System.EventHandler(this.timer_random_rectangle_Tick);
            // 
            // picSample
            // 
            this.picSample.Location = new System.Drawing.Point(20, 71);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(100, 50);
            this.picSample.TabIndex = 54;
            this.picSample.TabStop = false;
            this.picSample.Paint += new System.Windows.Forms.PaintEventHandler(this.picSample_Paint);
            this.picSample.Resize += new System.EventHandler(this.picSample_Resize);
            // 
            // picRainbow
            // 
            this.picRainbow.Location = new System.Drawing.Point(20, 30);
            this.picRainbow.Name = "picRainbow";
            this.picRainbow.Size = new System.Drawing.Size(500, 30);
            this.picRainbow.TabIndex = 53;
            this.picRainbow.TabStop = false;
            this.picRainbow.Paint += new System.Windows.Forms.PaintEventHandler(this.picRainbow_Paint);
            this.picRainbow.Resize += new System.EventHandler(this.picRainbow_Resize);
            // 
            // timer_rainbow
            // 
            this.timer_rainbow.Enabled = true;
            this.timer_rainbow.Tick += new System.EventHandler(this.timer_rainbow_Tick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(126, 85);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 19);
            this.label1.TabIndex = 55;
            this.label1.Text = "label1";
            // 
            // timer_battery
            // 
            this.timer_battery.Enabled = true;
            this.timer_battery.Tick += new System.EventHandler(this.timer_battery_Tick);
            // 
            // pictureBox_battery
            // 
            this.pictureBox_battery.Location = new System.Drawing.Point(27, 26);
            this.pictureBox_battery.Name = "pictureBox_battery";
            this.pictureBox_battery.Size = new System.Drawing.Size(50, 50);
            this.pictureBox_battery.TabIndex = 56;
            this.pictureBox_battery.TabStop = false;
            // 
            // pictureBox_gear
            // 
            this.pictureBox_gear.Location = new System.Drawing.Point(25, 55);
            this.pictureBox_gear.Name = "pictureBox_gear";
            this.pictureBox_gear.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_gear.TabIndex = 57;
            this.pictureBox_gear.TabStop = false;
            // 
            // timer_gear
            // 
            this.timer_gear.Enabled = true;
            this.timer_gear.Interval = 20;
            this.timer_gear.Tick += new System.EventHandler(this.timer_gear_Tick);
            // 
            // trackBar1
            // 
            this.trackBar1.Location = new System.Drawing.Point(10, 21);
            this.trackBar1.Maximum = 100;
            this.trackBar1.Minimum = 1;
            this.trackBar1.Name = "trackBar1";
            this.trackBar1.Size = new System.Drawing.Size(255, 45);
            this.trackBar1.TabIndex = 58;
            this.trackBar1.Value = 50;
            this.trackBar1.Scroll += new System.EventHandler(this.trackBar1_Scroll);
            // 
            // lb_fps
            // 
            this.lb_fps.AutoSize = true;
            this.lb_fps.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_fps.Location = new System.Drawing.Point(145, 69);
            this.lb_fps.Name = "lb_fps";
            this.lb_fps.Size = new System.Drawing.Size(31, 19);
            this.lb_fps.TabIndex = 59;
            this.lb_fps.Text = "fps";
            // 
            // pictureBox_atom
            // 
            this.pictureBox_atom.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_atom.Location = new System.Drawing.Point(473, 41);
            this.pictureBox_atom.Name = "pictureBox_atom";
            this.pictureBox_atom.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_atom.TabIndex = 60;
            this.pictureBox_atom.TabStop = false;
            // 
            // timer_atom
            // 
            this.timer_atom.Interval = 20;
            this.timer_atom.Tick += new System.EventHandler(this.timer_atom_Tick);
            // 
            // timer_card
            // 
            this.timer_card.Enabled = true;
            this.timer_card.Interval = 1000;
            this.timer_card.Tick += new System.EventHandler(this.timer_card_Tick);
            // 
            // pictureBox_card
            // 
            this.pictureBox_card.Location = new System.Drawing.Point(162, 669);
            this.pictureBox_card.Name = "pictureBox_card";
            this.pictureBox_card.Size = new System.Drawing.Size(102, 128);
            this.pictureBox_card.TabIndex = 63;
            this.pictureBox_card.TabStop = false;
            // 
            // timer_card2
            // 
            this.timer_card2.Enabled = true;
            this.timer_card2.Interval = 1000;
            this.timer_card2.Tick += new System.EventHandler(this.timer_card2_Tick);
            // 
            // pictureBox_card2
            // 
            this.pictureBox_card2.Location = new System.Drawing.Point(290, 669);
            this.pictureBox_card2.Name = "pictureBox_card2";
            this.pictureBox_card2.Size = new System.Drawing.Size(102, 128);
            this.pictureBox_card2.TabIndex = 64;
            this.pictureBox_card2.TabStop = false;
            // 
            // timer_atom2
            // 
            this.timer_atom2.Enabled = true;
            this.timer_atom2.Tick += new System.EventHandler(this.timer_atom2_Tick);
            // 
            // pictureBox_random
            // 
            this.pictureBox_random.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_random.Location = new System.Drawing.Point(243, 41);
            this.pictureBox_random.Name = "pictureBox_random";
            this.pictureBox_random.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_random.TabIndex = 65;
            this.pictureBox_random.TabStop = false;
            // 
            // timer_random
            // 
            this.timer_random.Enabled = true;
            this.timer_random.Interval = 5;
            this.timer_random.Tick += new System.EventHandler(this.timer_random_Tick);
            // 
            // pictureBox_stock
            // 
            this.pictureBox_stock.BackColor = System.Drawing.Color.LightPink;
            this.pictureBox_stock.Location = new System.Drawing.Point(1102, 12);
            this.pictureBox_stock.Name = "pictureBox_stock";
            this.pictureBox_stock.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_stock.TabIndex = 68;
            this.pictureBox_stock.TabStop = false;
            this.pictureBox_stock.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_stock_Paint);
            this.pictureBox_stock.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox_stock_MouseMove);
            // 
            // timer_stock
            // 
            this.timer_stock.Enabled = true;
            this.timer_stock.Interval = 500;
            this.timer_stock.Tick += new System.EventHandler(this.timer_stock_Tick);
            // 
            // pictureBox_rotate
            // 
            this.pictureBox_rotate.BackColor = System.Drawing.Color.Linen;
            this.pictureBox_rotate.Location = new System.Drawing.Point(414, 700);
            this.pictureBox_rotate.Name = "pictureBox_rotate";
            this.pictureBox_rotate.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_rotate.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_rotate.TabIndex = 72;
            this.pictureBox_rotate.TabStop = false;
            // 
            // panel_radar
            // 
            this.panel_radar.Controls.Add(this.pictureBox_radar);
            this.panel_radar.Location = new System.Drawing.Point(12, 53);
            this.panel_radar.Name = "panel_radar";
            this.panel_radar.Size = new System.Drawing.Size(183, 192);
            this.panel_radar.TabIndex = 73;
            // 
            // pictureBox_radar
            // 
            this.pictureBox_radar.Location = new System.Drawing.Point(17, 17);
            this.pictureBox_radar.Name = "pictureBox_radar";
            this.pictureBox_radar.Size = new System.Drawing.Size(154, 148);
            this.pictureBox_radar.TabIndex = 0;
            this.pictureBox_radar.TabStop = false;
            // 
            // timer_radar
            // 
            this.timer_radar.Enabled = true;
            this.timer_radar.Interval = 5;
            this.timer_radar.Tick += new System.EventHandler(this.timer_radar_Tick);
            // 
            // pictureBox_hex
            // 
            this.pictureBox_hex.Location = new System.Drawing.Point(12, 713);
            this.pictureBox_hex.Name = "pictureBox_hex";
            this.pictureBox_hex.Size = new System.Drawing.Size(70, 78);
            this.pictureBox_hex.TabIndex = 75;
            this.pictureBox_hex.TabStop = false;
            // 
            // timer_hex
            // 
            this.timer_hex.Enabled = true;
            this.timer_hex.Interval = 50;
            this.timer_hex.Tick += new System.EventHandler(this.timer_hex_Tick);
            // 
            // pictureBox_random_color
            // 
            this.pictureBox_random_color.Location = new System.Drawing.Point(24, 46);
            this.pictureBox_random_color.Name = "pictureBox_random_color";
            this.pictureBox_random_color.Size = new System.Drawing.Size(100, 100);
            this.pictureBox_random_color.TabIndex = 76;
            this.pictureBox_random_color.TabStop = false;
            this.pictureBox_random_color.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_random_color_Paint);
            // 
            // timer_random_color
            // 
            this.timer_random_color.Enabled = true;
            this.timer_random_color.Interval = 1000;
            this.timer_random_color.Tick += new System.EventHandler(this.timer_random_color_Tick);
            // 
            // pictureBox_battery2
            // 
            this.pictureBox_battery2.Location = new System.Drawing.Point(54, 46);
            this.pictureBox_battery2.Name = "pictureBox_battery2";
            this.pictureBox_battery2.Size = new System.Drawing.Size(50, 50);
            this.pictureBox_battery2.TabIndex = 77;
            this.pictureBox_battery2.TabStop = false;
            // 
            // lb_title00
            // 
            this.lb_title00.AutoSize = true;
            this.lb_title00.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title00.Location = new System.Drawing.Point(12, 16);
            this.lb_title00.Name = "lb_title00";
            this.lb_title00.Size = new System.Drawing.Size(104, 19);
            this.lb_title00.TabIndex = 225;
            this.lb_title00.Text = "雷達掃瞄圖";
            // 
            // lb_title03
            // 
            this.lb_title03.AutoSize = true;
            this.lb_title03.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title03.Location = new System.Drawing.Point(654, 9);
            this.lb_title03.Name = "lb_title03";
            this.lb_title03.Size = new System.Drawing.Size(135, 19);
            this.lb_title03.TabIndex = 227;
            this.lb_title03.Text = "pictureBox_color";
            // 
            // lb_title02
            // 
            this.lb_title02.AutoSize = true;
            this.lb_title02.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title02.Location = new System.Drawing.Point(474, 9);
            this.lb_title02.Name = "lb_title02";
            this.lb_title02.Size = new System.Drawing.Size(134, 19);
            this.lb_title02.TabIndex = 228;
            this.lb_title02.Text = "pictureBox_atom";
            // 
            // lb_title01
            // 
            this.lb_title01.AutoSize = true;
            this.lb_title01.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title01.Location = new System.Drawing.Point(239, 16);
            this.lb_title01.Name = "lb_title01";
            this.lb_title01.Size = new System.Drawing.Size(153, 19);
            this.lb_title01.TabIndex = 229;
            this.lb_title01.Text = "pictureBox_random";
            // 
            // lb_title_rotate
            // 
            this.lb_title_rotate.AutoSize = true;
            this.lb_title_rotate.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title_rotate.Location = new System.Drawing.Point(410, 678);
            this.lb_title_rotate.Name = "lb_title_rotate";
            this.lb_title_rotate.Size = new System.Drawing.Size(139, 19);
            this.lb_title_rotate.TabIndex = 233;
            this.lb_title_rotate.Text = "pictureBox_rotate";
            // 
            // lb_title_hex
            // 
            this.lb_title_hex.AutoSize = true;
            this.lb_title_hex.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_title_hex.Location = new System.Drawing.Point(8, 691);
            this.lb_title_hex.Name = "lb_title_hex";
            this.lb_title_hex.Size = new System.Drawing.Size(124, 19);
            this.lb_title_hex.TabIndex = 234;
            this.lb_title_hex.Text = "pictureBox_hex";
            // 
            // groupBox_rainbow
            // 
            this.groupBox_rainbow.Controls.Add(this.picRainbow);
            this.groupBox_rainbow.Controls.Add(this.picSample);
            this.groupBox_rainbow.Controls.Add(this.label1);
            this.groupBox_rainbow.Location = new System.Drawing.Point(836, 304);
            this.groupBox_rainbow.Name = "groupBox_rainbow";
            this.groupBox_rainbow.Size = new System.Drawing.Size(100, 100);
            this.groupBox_rainbow.TabIndex = 235;
            this.groupBox_rainbow.TabStop = false;
            this.groupBox_rainbow.Text = "Rainbow";
            // 
            // groupBox_gear
            // 
            this.groupBox_gear.Controls.Add(this.pictureBox_gear);
            this.groupBox_gear.Controls.Add(this.trackBar1);
            this.groupBox_gear.Controls.Add(this.lb_fps);
            this.groupBox_gear.Location = new System.Drawing.Point(12, 295);
            this.groupBox_gear.Name = "groupBox_gear";
            this.groupBox_gear.Size = new System.Drawing.Size(247, 201);
            this.groupBox_gear.TabIndex = 236;
            this.groupBox_gear.TabStop = false;
            this.groupBox_gear.Text = "Gear";
            // 
            // groupBox_random_color
            // 
            this.groupBox_random_color.Controls.Add(this.pictureBox_random_color);
            this.groupBox_random_color.Location = new System.Drawing.Point(290, 304);
            this.groupBox_random_color.Name = "groupBox_random_color";
            this.groupBox_random_color.Size = new System.Drawing.Size(200, 192);
            this.groupBox_random_color.TabIndex = 237;
            this.groupBox_random_color.TabStop = false;
            this.groupBox_random_color.Text = "Random Color";
            // 
            // groupBox_battery
            // 
            this.groupBox_battery.Controls.Add(this.pictureBox_battery);
            this.groupBox_battery.Controls.Add(this.pictureBox_battery2);
            this.groupBox_battery.Location = new System.Drawing.Point(519, 304);
            this.groupBox_battery.Name = "groupBox_battery";
            this.groupBox_battery.Size = new System.Drawing.Size(100, 100);
            this.groupBox_battery.TabIndex = 238;
            this.groupBox_battery.TabStop = false;
            this.groupBox_battery.Text = "Battery";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1262, 807);
            this.Controls.Add(this.groupBox_battery);
            this.Controls.Add(this.groupBox_random_color);
            this.Controls.Add(this.groupBox_gear);
            this.Controls.Add(this.groupBox_rainbow);
            this.Controls.Add(this.lb_title_hex);
            this.Controls.Add(this.lb_title_rotate);
            this.Controls.Add(this.lb_title01);
            this.Controls.Add(this.lb_title02);
            this.Controls.Add(this.lb_title03);
            this.Controls.Add(this.lb_title00);
            this.Controls.Add(this.pictureBox_hex);
            this.Controls.Add(this.panel_radar);
            this.Controls.Add(this.pictureBox_rotate);
            this.Controls.Add(this.pictureBox_stock);
            this.Controls.Add(this.pictureBox_random);
            this.Controls.Add(this.pictureBox_card2);
            this.Controls.Add(this.pictureBox_card);
            this.Controls.Add(this.pictureBox_atom);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRainbow)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_battery)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_gear)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_atom)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_card)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_card2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_stock)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_rotate)).EndInit();
            this.panel_radar.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_radar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_hex)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_random_color)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_battery2)).EndInit();
            this.groupBox_rainbow.ResumeLayout(false);
            this.groupBox_rainbow.PerformLayout();
            this.groupBox_gear.ResumeLayout(false);
            this.groupBox_gear.PerformLayout();
            this.groupBox_random_color.ResumeLayout(false);
            this.groupBox_battery.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer timer_rotate;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer timer_random_rectangle;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.PictureBox picRainbow;
        private System.Windows.Forms.Timer timer_rainbow;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Timer timer_battery;
        private System.Windows.Forms.PictureBox pictureBox_battery;
        private System.Windows.Forms.PictureBox pictureBox_gear;
        private System.Windows.Forms.Timer timer_gear;
        private System.Windows.Forms.TrackBar trackBar1;
        private System.Windows.Forms.Label lb_fps;
        private System.Windows.Forms.PictureBox pictureBox_atom;
        private System.Windows.Forms.Timer timer_atom;
        private System.Windows.Forms.Timer timer_card;
        private System.Windows.Forms.PictureBox pictureBox_card;
        private System.Windows.Forms.Timer timer_card2;
        private System.Windows.Forms.PictureBox pictureBox_card2;
        internal System.Windows.Forms.Timer timer_atom2;
        private System.Windows.Forms.PictureBox pictureBox_random;
        private System.Windows.Forms.Timer timer_random;
        private System.Windows.Forms.PictureBox pictureBox_stock;
        private System.Windows.Forms.ToolTip tipData;
        private System.Windows.Forms.Timer timer_stock;
        private System.Windows.Forms.PictureBox pictureBox_rotate;
        private System.Windows.Forms.Panel panel_radar;
        private System.Windows.Forms.PictureBox pictureBox_radar;
        private System.Windows.Forms.Timer timer_radar;
        private System.Windows.Forms.PictureBox pictureBox_hex;
        private System.Windows.Forms.Timer timer_hex;
        private System.Windows.Forms.PictureBox pictureBox_random_color;
        private System.Windows.Forms.Timer timer_random_color;
        private System.Windows.Forms.PictureBox pictureBox_battery2;
        private System.Windows.Forms.Label lb_title00;
        private System.Windows.Forms.Label lb_title03;
        private System.Windows.Forms.Label lb_title02;
        private System.Windows.Forms.Label lb_title01;
        private System.Windows.Forms.Label lb_title_rotate;
        private System.Windows.Forms.Label lb_title_hex;
        private System.Windows.Forms.GroupBox groupBox_rainbow;
        private System.Windows.Forms.GroupBox groupBox_gear;
        private System.Windows.Forms.GroupBox groupBox_random_color;
        private System.Windows.Forms.GroupBox groupBox_battery;
    }
}

