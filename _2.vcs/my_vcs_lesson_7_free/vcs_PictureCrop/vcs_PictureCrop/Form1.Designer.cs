namespace vcs_PictureCrop
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.cb_overwrite = new System.Windows.Forms.CheckBox();
            this.rb_filetype2 = new System.Windows.Forms.RadioButton();
            this.bt_open_folder = new System.Windows.Forms.Button();
            this.rb_filetype1 = new System.Windows.Forms.RadioButton();
            this.button6 = new System.Windows.Forms.Button();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.button3 = new System.Windows.Forms.Button();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.button0 = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox_resize = new System.Windows.Forms.GroupBox();
            this.rb_resize_type4 = new System.Windows.Forms.RadioButton();
            this.rb_resize_type1 = new System.Windows.Forms.RadioButton();
            this.rb_resize_type2 = new System.Windows.Forms.RadioButton();
            this.rb_resize_type3 = new System.Windows.Forms.RadioButton();
            this.rb_resize_type0 = new System.Windows.Forms.RadioButton();
            this.cb_keep_ratio = new System.Windows.Forms.CheckBox();
            this.bt_restore = new System.Windows.Forms.Button();
            this.tb_h = new System.Windows.Forms.TextBox();
            this.tb_w = new System.Windows.Forms.TextBox();
            this.lb_w2 = new System.Windows.Forms.Label();
            this.lb_h2 = new System.Windows.Forms.Label();
            this.bt_save2 = new System.Windows.Forms.Button();
            this.trackBar_h = new System.Windows.Forms.TrackBar();
            this.trackBar_w = new System.Windows.Forms.TrackBar();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.groupBox_resize.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_w)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(131, 118);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.cb_overwrite);
            this.groupBox_selection.Controls.Add(this.rb_filetype2);
            this.groupBox_selection.Controls.Add(this.bt_open_folder);
            this.groupBox_selection.Controls.Add(this.rb_filetype1);
            this.groupBox_selection.Controls.Add(this.button6);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Controls.Add(this.button3);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Location = new System.Drawing.Point(237, 12);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(300, 200);
            this.groupBox_selection.TabIndex = 17;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // cb_overwrite
            // 
            this.cb_overwrite.AutoSize = true;
            this.cb_overwrite.Location = new System.Drawing.Point(180, 180);
            this.cb_overwrite.Name = "cb_overwrite";
            this.cb_overwrite.Size = new System.Drawing.Size(72, 16);
            this.cb_overwrite.TabIndex = 22;
            this.cb_overwrite.Text = "覆蓋原檔";
            this.cb_overwrite.UseVisualStyleBackColor = true;
            // 
            // rb_filetype2
            // 
            this.rb_filetype2.AutoSize = true;
            this.rb_filetype2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype2.Location = new System.Drawing.Point(180, 155);
            this.rb_filetype2.Name = "rb_filetype2";
            this.rb_filetype2.Size = new System.Drawing.Size(54, 20);
            this.rb_filetype2.TabIndex = 21;
            this.rb_filetype2.Text = "bmp";
            this.rb_filetype2.UseVisualStyleBackColor = true;
            // 
            // bt_open_folder
            // 
            this.bt_open_folder.Location = new System.Drawing.Point(235, 126);
            this.bt_open_folder.Name = "bt_open_folder";
            this.bt_open_folder.Size = new System.Drawing.Size(40, 40);
            this.bt_open_folder.TabIndex = 20;
            this.bt_open_folder.UseVisualStyleBackColor = true;
            this.bt_open_folder.Click += new System.EventHandler(this.bt_open_folder_Click);
            // 
            // rb_filetype1
            // 
            this.rb_filetype1.AutoSize = true;
            this.rb_filetype1.Checked = true;
            this.rb_filetype1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype1.Location = new System.Drawing.Point(180, 130);
            this.rb_filetype1.Name = "rb_filetype1";
            this.rb_filetype1.Size = new System.Drawing.Size(46, 20);
            this.rb_filetype1.TabIndex = 20;
            this.rb_filetype1.TabStop = true;
            this.rb_filetype1.Text = "jpg";
            this.rb_filetype1.UseVisualStyleBackColor = true;
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(185, 80);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(90, 40);
            this.button6.TabIndex = 6;
            this.button6.Text = "save";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
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
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(185, 26);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(90, 40);
            this.button3.TabIndex = 5;
            this.button3.Text = "Info";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
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
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(162, 183);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 18;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(131, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.pictureBox2.TabIndex = 19;
            this.pictureBox2.TabStop = false;
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(12, 229);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(90, 40);
            this.button0.TabIndex = 20;
            this.button0.Text = "test";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // panel1
            // 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel1.Location = new System.Drawing.Point(12, 122);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(100, 100);
            this.panel1.TabIndex = 21;
            // 
            // groupBox_resize
            // 
            this.groupBox_resize.Controls.Add(this.rb_resize_type4);
            this.groupBox_resize.Controls.Add(this.rb_resize_type1);
            this.groupBox_resize.Controls.Add(this.rb_resize_type2);
            this.groupBox_resize.Controls.Add(this.rb_resize_type3);
            this.groupBox_resize.Controls.Add(this.rb_resize_type0);
            this.groupBox_resize.Controls.Add(this.cb_keep_ratio);
            this.groupBox_resize.Controls.Add(this.bt_restore);
            this.groupBox_resize.Controls.Add(this.tb_h);
            this.groupBox_resize.Controls.Add(this.tb_w);
            this.groupBox_resize.Controls.Add(this.lb_w2);
            this.groupBox_resize.Controls.Add(this.lb_h2);
            this.groupBox_resize.Controls.Add(this.bt_save2);
            this.groupBox_resize.Controls.Add(this.trackBar_h);
            this.groupBox_resize.Controls.Add(this.trackBar_w);
            this.groupBox_resize.Location = new System.Drawing.Point(237, 229);
            this.groupBox_resize.Name = "groupBox_resize";
            this.groupBox_resize.Size = new System.Drawing.Size(300, 200);
            this.groupBox_resize.TabIndex = 23;
            this.groupBox_resize.TabStop = false;
            this.groupBox_resize.Text = "縮放大小";
            // 
            // rb_resize_type4
            // 
            this.rb_resize_type4.AutoSize = true;
            this.rb_resize_type4.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_resize_type4.Location = new System.Drawing.Point(156, 161);
            this.rb_resize_type4.Name = "rb_resize_type4";
            this.rb_resize_type4.Size = new System.Drawing.Size(90, 20);
            this.rb_resize_type4.TabIndex = 27;
            this.rb_resize_type4.Text = "四分之一";
            this.rb_resize_type4.UseVisualStyleBackColor = true;
            // 
            // rb_resize_type1
            // 
            this.rb_resize_type1.AutoSize = true;
            this.rb_resize_type1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_resize_type1.Location = new System.Drawing.Point(158, 130);
            this.rb_resize_type1.Name = "rb_resize_type1";
            this.rb_resize_type1.Size = new System.Drawing.Size(66, 20);
            this.rb_resize_type1.TabIndex = 26;
            this.rb_resize_type1.Text = "1080p";
            this.rb_resize_type1.UseVisualStyleBackColor = true;
            // 
            // rb_resize_type2
            // 
            this.rb_resize_type2.AutoSize = true;
            this.rb_resize_type2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_resize_type2.Location = new System.Drawing.Point(22, 161);
            this.rb_resize_type2.Name = "rb_resize_type2";
            this.rb_resize_type2.Size = new System.Drawing.Size(58, 20);
            this.rb_resize_type2.TabIndex = 26;
            this.rb_resize_type2.Text = "720p";
            this.rb_resize_type2.UseVisualStyleBackColor = true;
            // 
            // rb_resize_type3
            // 
            this.rb_resize_type3.AutoSize = true;
            this.rb_resize_type3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_resize_type3.Location = new System.Drawing.Point(92, 161);
            this.rb_resize_type3.Name = "rb_resize_type3";
            this.rb_resize_type3.Size = new System.Drawing.Size(58, 20);
            this.rb_resize_type3.TabIndex = 23;
            this.rb_resize_type3.Text = "一半";
            this.rb_resize_type3.UseVisualStyleBackColor = true;
            // 
            // rb_resize_type0
            // 
            this.rb_resize_type0.AutoSize = true;
            this.rb_resize_type0.Checked = true;
            this.rb_resize_type0.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_resize_type0.Location = new System.Drawing.Point(88, 130);
            this.rb_resize_type0.Name = "rb_resize_type0";
            this.rb_resize_type0.Size = new System.Drawing.Size(58, 20);
            this.rb_resize_type0.TabIndex = 23;
            this.rb_resize_type0.TabStop = true;
            this.rb_resize_type0.Text = "自訂";
            this.rb_resize_type0.UseVisualStyleBackColor = true;
            // 
            // cb_keep_ratio
            // 
            this.cb_keep_ratio.AutoSize = true;
            this.cb_keep_ratio.Checked = true;
            this.cb_keep_ratio.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_keep_ratio.Location = new System.Drawing.Point(19, 133);
            this.cb_keep_ratio.Name = "cb_keep_ratio";
            this.cb_keep_ratio.Size = new System.Drawing.Size(72, 16);
            this.cb_keep_ratio.TabIndex = 22;
            this.cb_keep_ratio.Text = "保持比例";
            this.cb_keep_ratio.UseVisualStyleBackColor = true;
            // 
            // bt_restore
            // 
            this.bt_restore.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_restore.Location = new System.Drawing.Point(149, 53);
            this.bt_restore.Name = "bt_restore";
            this.bt_restore.Size = new System.Drawing.Size(80, 30);
            this.bt_restore.TabIndex = 28;
            this.bt_restore.Text = "恢復";
            this.bt_restore.UseVisualStyleBackColor = true;
            this.bt_restore.Click += new System.EventHandler(this.bt_restore_Click);
            // 
            // tb_h
            // 
            this.tb_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_h.Location = new System.Drawing.Point(48, 89);
            this.tb_h.Name = "tb_h";
            this.tb_h.Size = new System.Drawing.Size(70, 33);
            this.tb_h.TabIndex = 24;
            this.tb_h.Text = "100";
            this.tb_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_w
            // 
            this.tb_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_w.Location = new System.Drawing.Point(48, 53);
            this.tb_w.Name = "tb_w";
            this.tb_w.Size = new System.Drawing.Size(70, 33);
            this.tb_w.TabIndex = 23;
            this.tb_w.Text = "100";
            this.tb_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_w2
            // 
            this.lb_w2.AutoSize = true;
            this.lb_w2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w2.Location = new System.Drawing.Point(15, 54);
            this.lb_w2.Name = "lb_w2";
            this.lb_w2.Size = new System.Drawing.Size(131, 24);
            this.lb_w2.TabIndex = 6;
            this.lb_w2.Text = "寬             %";
            // 
            // lb_h2
            // 
            this.lb_h2.AutoSize = true;
            this.lb_h2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h2.Location = new System.Drawing.Point(15, 93);
            this.lb_h2.Name = "lb_h2";
            this.lb_h2.Size = new System.Drawing.Size(131, 24);
            this.lb_h2.TabIndex = 8;
            this.lb_h2.Text = "高             %";
            // 
            // bt_save2
            // 
            this.bt_save2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save2.Location = new System.Drawing.Point(149, 92);
            this.bt_save2.Name = "bt_save2";
            this.bt_save2.Size = new System.Drawing.Size(80, 30);
            this.bt_save2.TabIndex = 23;
            this.bt_save2.Text = "save";
            this.bt_save2.UseVisualStyleBackColor = true;
            this.bt_save2.Click += new System.EventHandler(this.bt_save2_Click);
            // 
            // trackBar_h
            // 
            this.trackBar_h.Location = new System.Drawing.Point(235, 47);
            this.trackBar_h.Maximum = 120;
            this.trackBar_h.Minimum = 1;
            this.trackBar_h.Name = "trackBar_h";
            this.trackBar_h.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.trackBar_h.Size = new System.Drawing.Size(45, 129);
            this.trackBar_h.TabIndex = 24;
            this.trackBar_h.Value = 100;
            this.trackBar_h.Scroll += new System.EventHandler(this.trackBar_h_Scroll);
            this.trackBar_h.MouseDown += new System.Windows.Forms.MouseEventHandler(this.trackBar_h_MouseDown);
            this.trackBar_h.MouseUp += new System.Windows.Forms.MouseEventHandler(this.trackBar_h_MouseUp);
            // 
            // trackBar_w
            // 
            this.trackBar_w.Location = new System.Drawing.Point(19, 18);
            this.trackBar_w.Maximum = 120;
            this.trackBar_w.Minimum = 1;
            this.trackBar_w.Name = "trackBar_w";
            this.trackBar_w.Size = new System.Drawing.Size(264, 45);
            this.trackBar_w.TabIndex = 25;
            this.trackBar_w.Value = 100;
            this.trackBar_w.Scroll += new System.EventHandler(this.trackBar_w_Scroll);
            this.trackBar_w.MouseDown += new System.Windows.Forms.MouseEventHandler(this.trackBar_w_MouseDown);
            this.trackBar_w.MouseUp += new System.Windows.Forms.MouseEventHandler(this.trackBar_w_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(656, 523);
            this.Controls.Add(this.groupBox_resize);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.groupBox_resize.ResumeLayout(false);
            this.groupBox_resize.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_w)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button bt_open_folder;
        private System.Windows.Forms.RadioButton rb_filetype2;
        private System.Windows.Forms.RadioButton rb_filetype1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.CheckBox cb_overwrite;
        private System.Windows.Forms.GroupBox groupBox_resize;
        private System.Windows.Forms.Label lb_w2;
        private System.Windows.Forms.Label lb_h2;
        private System.Windows.Forms.TrackBar trackBar_h;
        private System.Windows.Forms.TrackBar trackBar_w;
        private System.Windows.Forms.TextBox tb_h;
        private System.Windows.Forms.TextBox tb_w;
        private System.Windows.Forms.CheckBox cb_keep_ratio;
        private System.Windows.Forms.Button bt_save2;
        private System.Windows.Forms.Button bt_restore;
        private System.Windows.Forms.RadioButton rb_resize_type4;
        private System.Windows.Forms.RadioButton rb_resize_type1;
        private System.Windows.Forms.RadioButton rb_resize_type2;
        private System.Windows.Forms.RadioButton rb_resize_type3;
        private System.Windows.Forms.RadioButton rb_resize_type0;
    }
}

