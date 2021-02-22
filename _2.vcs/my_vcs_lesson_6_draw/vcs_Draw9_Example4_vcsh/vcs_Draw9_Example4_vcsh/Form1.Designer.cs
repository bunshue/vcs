namespace vcs_Draw9_Example4_vcsh
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_exit = new System.Windows.Forms.Button();
            this.bt_save = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_hit_curve = new System.Windows.Forms.PictureBox();
            this.pictureBox_color_curve = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnGo = new System.Windows.Forms.Button();
            this.picHidden = new System.Windows.Forms.PictureBox();
            this.label21 = new System.Windows.Forms.Label();
            this.label22 = new System.Windows.Forms.Label();
            this.label23 = new System.Windows.Forms.Label();
            this.label24 = new System.Windows.Forms.Label();
            this.label25 = new System.Windows.Forms.Label();
            this.label26 = new System.Windows.Forms.Label();
            this.label27 = new System.Windows.Forms.Label();
            this.label28 = new System.Windows.Forms.Label();
            this.label29 = new System.Windows.Forms.Label();
            this.label30 = new System.Windows.Forms.Label();
            this.label31 = new System.Windows.Forms.Label();
            this.label32 = new System.Windows.Forms.Label();
            this.label33 = new System.Windows.Forms.Label();
            this.label34 = new System.Windows.Forms.Label();
            this.label35 = new System.Windows.Forms.Label();
            this.label36 = new System.Windows.Forms.Label();
            this.label37 = new System.Windows.Forms.Label();
            this.label38 = new System.Windows.Forms.Label();
            this.label39 = new System.Windows.Forms.Label();
            this.label40 = new System.Windows.Forms.Label();
            this.picColors = new System.Windows.Forms.PictureBox();
            this.picVisible = new System.Windows.Forms.PictureBox();
            this.label11 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.label18 = new System.Windows.Forms.Label();
            this.label19 = new System.Windows.Forms.Label();
            this.label20 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tmrSmallLabels = new System.Windows.Forms.Timer(this.components);
            this.tmrLabels = new System.Windows.Forms.Timer(this.components);
            this.tmrColoredLabels = new System.Windows.Forms.Timer(this.components);
            this.tmrColorBar = new System.Windows.Forms.Timer(this.components);
            this.tmrPicture = new System.Windows.Forms.Timer(this.components);
            this.label41 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_hit_curve)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_color_curve)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picColors)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(706, 479);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(548, 140);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.Location = new System.Drawing.Point(0, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(685, 418);
            this.pictureBox1.TabIndex = 15;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // bt_exit
            // 
            this.bt_exit.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_exit.Location = new System.Drawing.Point(994, 428);
            this.bt_exit.Name = "bt_exit";
            this.bt_exit.Size = new System.Drawing.Size(100, 40);
            this.bt_exit.TabIndex = 57;
            this.bt_exit.Text = "Exit";
            this.bt_exit.UseVisualStyleBackColor = true;
            this.bt_exit.Click += new System.EventHandler(this.bt_exit_Click);
            // 
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(875, 428);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(100, 40);
            this.bt_save.TabIndex = 56;
            this.bt_save.Text = "Save";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1153, 579);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(63, 40);
            this.bt_clear.TabIndex = 55;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // pictureBox_hit_curve
            // 
            this.pictureBox_hit_curve.BackColor = System.Drawing.Color.LightGreen;
            this.pictureBox_hit_curve.Location = new System.Drawing.Point(431, 438);
            this.pictureBox_hit_curve.Name = "pictureBox_hit_curve";
            this.pictureBox_hit_curve.Size = new System.Drawing.Size(254, 238);
            this.pictureBox_hit_curve.TabIndex = 75;
            this.pictureBox_hit_curve.TabStop = false;
            this.pictureBox_hit_curve.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_hit_curve_Paint);
            this.pictureBox_hit_curve.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox_hit_curve_MouseClick);
            this.pictureBox_hit_curve.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox_hit_curve_MouseMove);
            // 
            // pictureBox_color_curve
            // 
            this.pictureBox_color_curve.BackColor = System.Drawing.Color.LightGreen;
            this.pictureBox_color_curve.Location = new System.Drawing.Point(171, 438);
            this.pictureBox_color_curve.Name = "pictureBox_color_curve";
            this.pictureBox_color_curve.Size = new System.Drawing.Size(254, 238);
            this.pictureBox_color_curve.TabIndex = 76;
            this.pictureBox_color_curve.TabStop = false;
            this.pictureBox_color_curve.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_color_curve_Paint);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnGo);
            this.groupBox1.Controls.Add(this.picHidden);
            this.groupBox1.Controls.Add(this.label21);
            this.groupBox1.Controls.Add(this.label22);
            this.groupBox1.Controls.Add(this.label23);
            this.groupBox1.Controls.Add(this.label24);
            this.groupBox1.Controls.Add(this.label25);
            this.groupBox1.Controls.Add(this.label26);
            this.groupBox1.Controls.Add(this.label27);
            this.groupBox1.Controls.Add(this.label28);
            this.groupBox1.Controls.Add(this.label29);
            this.groupBox1.Controls.Add(this.label30);
            this.groupBox1.Controls.Add(this.label31);
            this.groupBox1.Controls.Add(this.label32);
            this.groupBox1.Controls.Add(this.label33);
            this.groupBox1.Controls.Add(this.label34);
            this.groupBox1.Controls.Add(this.label35);
            this.groupBox1.Controls.Add(this.label36);
            this.groupBox1.Controls.Add(this.label37);
            this.groupBox1.Controls.Add(this.label38);
            this.groupBox1.Controls.Add(this.label39);
            this.groupBox1.Controls.Add(this.label40);
            this.groupBox1.Controls.Add(this.picColors);
            this.groupBox1.Controls.Add(this.picVisible);
            this.groupBox1.Controls.Add(this.label11);
            this.groupBox1.Controls.Add(this.label12);
            this.groupBox1.Controls.Add(this.label13);
            this.groupBox1.Controls.Add(this.label14);
            this.groupBox1.Controls.Add(this.label15);
            this.groupBox1.Controls.Add(this.label16);
            this.groupBox1.Controls.Add(this.label17);
            this.groupBox1.Controls.Add(this.label18);
            this.groupBox1.Controls.Add(this.label19);
            this.groupBox1.Controls.Add(this.label20);
            this.groupBox1.Controls.Add(this.label10);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(495, 393);
            this.groupBox1.TabIndex = 77;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "unique progressbar";
            // 
            // btnGo
            // 
            this.btnGo.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnGo.Location = new System.Drawing.Point(414, 21);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(75, 21);
            this.btnGo.TabIndex = 87;
            this.btnGo.Text = "Go";
            this.btnGo.UseVisualStyleBackColor = true;
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // picHidden
            // 
            this.picHidden.Image = ((System.Drawing.Image)(resources.GetObject("picHidden.Image")));
            this.picHidden.Location = new System.Drawing.Point(20, 272);
            this.picHidden.Name = "picHidden";
            this.picHidden.Size = new System.Drawing.Size(367, 87);
            this.picHidden.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picHidden.TabIndex = 86;
            this.picHidden.TabStop = false;
            this.picHidden.Visible = false;
            // 
            // label21
            // 
            this.label21.BackColor = System.Drawing.Color.Gray;
            this.label21.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label21.Location = new System.Drawing.Point(20, 87);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(6, 6);
            this.label21.TabIndex = 85;
            // 
            // label22
            // 
            this.label22.BackColor = System.Drawing.Color.Gray;
            this.label22.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label22.Location = new System.Drawing.Point(33, 97);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(6, 6);
            this.label22.TabIndex = 84;
            // 
            // label23
            // 
            this.label23.BackColor = System.Drawing.Color.Gray;
            this.label23.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label23.Location = new System.Drawing.Point(46, 89);
            this.label23.Name = "label23";
            this.label23.Size = new System.Drawing.Size(6, 6);
            this.label23.TabIndex = 83;
            // 
            // label24
            // 
            this.label24.BackColor = System.Drawing.Color.Gray;
            this.label24.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label24.Location = new System.Drawing.Point(59, 97);
            this.label24.Name = "label24";
            this.label24.Size = new System.Drawing.Size(6, 6);
            this.label24.TabIndex = 82;
            // 
            // label25
            // 
            this.label25.BackColor = System.Drawing.Color.Gray;
            this.label25.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label25.Location = new System.Drawing.Point(72, 104);
            this.label25.Name = "label25";
            this.label25.Size = new System.Drawing.Size(6, 6);
            this.label25.TabIndex = 81;
            // 
            // label26
            // 
            this.label26.BackColor = System.Drawing.Color.Gray;
            this.label26.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label26.Location = new System.Drawing.Point(85, 87);
            this.label26.Name = "label26";
            this.label26.Size = new System.Drawing.Size(6, 6);
            this.label26.TabIndex = 80;
            // 
            // label27
            // 
            this.label27.BackColor = System.Drawing.Color.Gray;
            this.label27.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label27.Location = new System.Drawing.Point(98, 97);
            this.label27.Name = "label27";
            this.label27.Size = new System.Drawing.Size(6, 6);
            this.label27.TabIndex = 79;
            // 
            // label28
            // 
            this.label28.BackColor = System.Drawing.Color.Gray;
            this.label28.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label28.Location = new System.Drawing.Point(111, 93);
            this.label28.Name = "label28";
            this.label28.Size = new System.Drawing.Size(6, 6);
            this.label28.TabIndex = 78;
            // 
            // label29
            // 
            this.label29.BackColor = System.Drawing.Color.Gray;
            this.label29.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label29.Location = new System.Drawing.Point(124, 97);
            this.label29.Name = "label29";
            this.label29.Size = new System.Drawing.Size(6, 6);
            this.label29.TabIndex = 77;
            // 
            // label30
            // 
            this.label30.BackColor = System.Drawing.Color.Gray;
            this.label30.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label30.Location = new System.Drawing.Point(137, 107);
            this.label30.Name = "label30";
            this.label30.Size = new System.Drawing.Size(6, 6);
            this.label30.TabIndex = 76;
            // 
            // label31
            // 
            this.label31.BackColor = System.Drawing.Color.Gray;
            this.label31.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label31.Location = new System.Drawing.Point(150, 92);
            this.label31.Name = "label31";
            this.label31.Size = new System.Drawing.Size(6, 6);
            this.label31.TabIndex = 75;
            // 
            // label32
            // 
            this.label32.BackColor = System.Drawing.Color.Gray;
            this.label32.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label32.Location = new System.Drawing.Point(163, 99);
            this.label32.Name = "label32";
            this.label32.Size = new System.Drawing.Size(6, 6);
            this.label32.TabIndex = 74;
            // 
            // label33
            // 
            this.label33.BackColor = System.Drawing.Color.Gray;
            this.label33.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label33.Location = new System.Drawing.Point(176, 87);
            this.label33.Name = "label33";
            this.label33.Size = new System.Drawing.Size(6, 6);
            this.label33.TabIndex = 73;
            // 
            // label34
            // 
            this.label34.BackColor = System.Drawing.Color.Gray;
            this.label34.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label34.Location = new System.Drawing.Point(189, 87);
            this.label34.Name = "label34";
            this.label34.Size = new System.Drawing.Size(6, 6);
            this.label34.TabIndex = 72;
            // 
            // label35
            // 
            this.label35.BackColor = System.Drawing.Color.Gray;
            this.label35.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label35.Location = new System.Drawing.Point(202, 97);
            this.label35.Name = "label35";
            this.label35.Size = new System.Drawing.Size(6, 6);
            this.label35.TabIndex = 71;
            // 
            // label36
            // 
            this.label36.BackColor = System.Drawing.Color.Gray;
            this.label36.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label36.Location = new System.Drawing.Point(215, 97);
            this.label36.Name = "label36";
            this.label36.Size = new System.Drawing.Size(6, 6);
            this.label36.TabIndex = 70;
            // 
            // label37
            // 
            this.label37.BackColor = System.Drawing.Color.Gray;
            this.label37.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label37.Location = new System.Drawing.Point(228, 108);
            this.label37.Name = "label37";
            this.label37.Size = new System.Drawing.Size(6, 6);
            this.label37.TabIndex = 69;
            // 
            // label38
            // 
            this.label38.BackColor = System.Drawing.Color.Gray;
            this.label38.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label38.Location = new System.Drawing.Point(241, 91);
            this.label38.Name = "label38";
            this.label38.Size = new System.Drawing.Size(6, 6);
            this.label38.TabIndex = 68;
            // 
            // label39
            // 
            this.label39.BackColor = System.Drawing.Color.Gray;
            this.label39.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label39.Location = new System.Drawing.Point(254, 97);
            this.label39.Name = "label39";
            this.label39.Size = new System.Drawing.Size(6, 6);
            this.label39.TabIndex = 67;
            // 
            // label40
            // 
            this.label40.BackColor = System.Drawing.Color.Gray;
            this.label40.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label40.Location = new System.Drawing.Point(267, 93);
            this.label40.Name = "label40";
            this.label40.Size = new System.Drawing.Size(6, 6);
            this.label40.TabIndex = 66;
            // 
            // picColors
            // 
            this.picColors.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picColors.Location = new System.Drawing.Point(20, 127);
            this.picColors.Name = "picColors";
            this.picColors.Size = new System.Drawing.Size(253, 22);
            this.picColors.TabIndex = 65;
            this.picColors.TabStop = false;
            this.picColors.Visible = false;
            // 
            // picVisible
            // 
            this.picVisible.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picVisible.Location = new System.Drawing.Point(20, 168);
            this.picVisible.Name = "picVisible";
            this.picVisible.Size = new System.Drawing.Size(253, 87);
            this.picVisible.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picVisible.TabIndex = 64;
            this.picVisible.TabStop = false;
            this.picVisible.Visible = false;
            // 
            // label11
            // 
            this.label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label11.Location = new System.Drawing.Point(20, 49);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(20, 18);
            this.label11.TabIndex = 63;
            // 
            // label12
            // 
            this.label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label12.Location = new System.Drawing.Point(46, 49);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(20, 18);
            this.label12.TabIndex = 62;
            // 
            // label13
            // 
            this.label13.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label13.Location = new System.Drawing.Point(72, 49);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(20, 18);
            this.label13.TabIndex = 61;
            // 
            // label14
            // 
            this.label14.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label14.Location = new System.Drawing.Point(98, 49);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(20, 18);
            this.label14.TabIndex = 60;
            // 
            // label15
            // 
            this.label15.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label15.Location = new System.Drawing.Point(124, 49);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(20, 18);
            this.label15.TabIndex = 59;
            // 
            // label16
            // 
            this.label16.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label16.Location = new System.Drawing.Point(150, 49);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(20, 18);
            this.label16.TabIndex = 58;
            // 
            // label17
            // 
            this.label17.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label17.Location = new System.Drawing.Point(176, 49);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(20, 18);
            this.label17.TabIndex = 57;
            // 
            // label18
            // 
            this.label18.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label18.Location = new System.Drawing.Point(202, 49);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(20, 18);
            this.label18.TabIndex = 56;
            // 
            // label19
            // 
            this.label19.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label19.Location = new System.Drawing.Point(228, 49);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(20, 18);
            this.label19.TabIndex = 55;
            // 
            // label20
            // 
            this.label20.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label20.Location = new System.Drawing.Point(254, 49);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(20, 18);
            this.label20.TabIndex = 54;
            // 
            // label10
            // 
            this.label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label10.Location = new System.Drawing.Point(254, 19);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(20, 18);
            this.label10.TabIndex = 53;
            // 
            // label9
            // 
            this.label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label9.Location = new System.Drawing.Point(228, 19);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(20, 18);
            this.label9.TabIndex = 52;
            // 
            // label8
            // 
            this.label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label8.Location = new System.Drawing.Point(202, 19);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(20, 18);
            this.label8.TabIndex = 51;
            // 
            // label7
            // 
            this.label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label7.Location = new System.Drawing.Point(176, 19);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(20, 18);
            this.label7.TabIndex = 50;
            // 
            // label6
            // 
            this.label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label6.Location = new System.Drawing.Point(150, 19);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(20, 18);
            this.label6.TabIndex = 49;
            // 
            // label5
            // 
            this.label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label5.Location = new System.Drawing.Point(124, 19);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(20, 18);
            this.label5.TabIndex = 48;
            // 
            // label4
            // 
            this.label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label4.Location = new System.Drawing.Point(98, 19);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(20, 18);
            this.label4.TabIndex = 47;
            // 
            // label3
            // 
            this.label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label3.Location = new System.Drawing.Point(72, 19);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 18);
            this.label3.TabIndex = 46;
            // 
            // label2
            // 
            this.label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label2.Location = new System.Drawing.Point(46, 19);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(20, 18);
            this.label2.TabIndex = 45;
            // 
            // label1
            // 
            this.label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label1.Location = new System.Drawing.Point(20, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(20, 18);
            this.label1.TabIndex = 44;
            // 
            // tmrSmallLabels
            // 
            this.tmrSmallLabels.Interval = 150;
            this.tmrSmallLabels.Tick += new System.EventHandler(this.tmrSmallLabels_Tick);
            // 
            // tmrLabels
            // 
            this.tmrLabels.Interval = 300;
            this.tmrLabels.Tick += new System.EventHandler(this.tmrLabels_Tick);
            // 
            // tmrColoredLabels
            // 
            this.tmrColoredLabels.Interval = 300;
            this.tmrColoredLabels.Tick += new System.EventHandler(this.tmrColoredLabels_Tick);
            // 
            // tmrColorBar
            // 
            this.tmrColorBar.Interval = 150;
            this.tmrColorBar.Tick += new System.EventHandler(this.tmrColorBar_Tick);
            // 
            // tmrPicture
            // 
            this.tmrPicture.Interval = 150;
            this.tmrPicture.Tick += new System.EventHandler(this.tmrPicture_Tick);
            // 
            // label41
            // 
            this.label41.AutoSize = true;
            this.label41.Location = new System.Drawing.Point(704, 438);
            this.label41.Name = "label41";
            this.label41.Size = new System.Drawing.Size(113, 12);
            this.label41.TabIndex = 78;
            this.label41.Text = "檢查有沒有點在線上";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1370, 688);
            this.Controls.Add(this.label41);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox_color_curve);
            this.Controls.Add(this.pictureBox_hit_curve);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_exit);
            this.Controls.Add(this.bt_save);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_hit_curve)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_color_curve)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picColors)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_exit;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.PictureBox pictureBox_hit_curve;
        private System.Windows.Forms.PictureBox pictureBox_color_curve;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.PictureBox picHidden;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.Label label22;
        private System.Windows.Forms.Label label23;
        private System.Windows.Forms.Label label24;
        private System.Windows.Forms.Label label25;
        private System.Windows.Forms.Label label26;
        private System.Windows.Forms.Label label27;
        private System.Windows.Forms.Label label28;
        private System.Windows.Forms.Label label29;
        private System.Windows.Forms.Label label30;
        private System.Windows.Forms.Label label31;
        private System.Windows.Forms.Label label32;
        private System.Windows.Forms.Label label33;
        private System.Windows.Forms.Label label34;
        private System.Windows.Forms.Label label35;
        private System.Windows.Forms.Label label36;
        private System.Windows.Forms.Label label37;
        private System.Windows.Forms.Label label38;
        private System.Windows.Forms.Label label39;
        private System.Windows.Forms.Label label40;
        private System.Windows.Forms.PictureBox picColors;
        private System.Windows.Forms.PictureBox picVisible;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnGo;
        private System.Windows.Forms.Timer tmrSmallLabels;
        private System.Windows.Forms.Timer tmrLabels;
        private System.Windows.Forms.Timer tmrColoredLabels;
        private System.Windows.Forms.Timer tmrColorBar;
        private System.Windows.Forms.Timer tmrPicture;
        private System.Windows.Forms.Label label41;
    }
}

