namespace vcs_Draw9_Example5a_vcsh
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
            this.pictureBox0 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.rb6 = new System.Windows.Forms.RadioButton();
            this.rb5 = new System.Windows.Forms.RadioButton();
            this.rb4 = new System.Windows.Forms.RadioButton();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.button1 = new System.Windows.Forms.Button();
            this.chkTrueSpiral = new System.Windows.Forms.CheckBox();
            this.chkCircularSpiral = new System.Windows.Forms.CheckBox();
            this.chkSquareSpiral = new System.Windows.Forms.CheckBox();
            this.chkRectangles = new System.Windows.Forms.CheckBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.chkOutline = new System.Windows.Forms.CheckBox();
            this.btnDraw = new System.Windows.Forms.Button();
            this.txtNumTriangles = new System.Windows.Forms.TextBox();
            this.chkFill = new System.Windows.Forms.CheckBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.txtZ0 = new System.Windows.Forms.TextBox();
            this.btnStart = new System.Windows.Forms.Button();
            this.label9 = new System.Windows.Forms.Label();
            this.txtY0 = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.txtX0 = new System.Windows.Forms.TextBox();
            this.label11 = new System.Windows.Forms.Label();
            this.txtE = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.txtD = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.txtC = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.txtB = new System.Windows.Forms.TextBox();
            this.label12 = new System.Windows.Forms.Label();
            this.txtA = new System.Windows.Forms.TextBox();
            this.label13 = new System.Windows.Forms.Label();
            this.lblForeColor = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.cboPlane = new System.Windows.Forms.ComboBox();
            this.label16 = new System.Windows.Forms.Label();
            this.lblBackColor = new System.Windows.Forms.Label();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.pictureBox6 = new System.Windows.Forms.PictureBox();
            this.pictureBox7 = new System.Windows.Forms.PictureBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.scrSpeed = new System.Windows.Forms.HScrollBar();
            this.lblWalkNum2 = new System.Windows.Forms.Label();
            this.lblWalkNum = new System.Windows.Forms.Label();
            this.trkWalk = new System.Windows.Forms.TrackBar();
            this.lblResults = new System.Windows.Forms.Label();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.txtHeight = new System.Windows.Forms.TextBox();
            this.label21 = new System.Windows.Forms.Label();
            this.txtWidth = new System.Windows.Forms.TextBox();
            this.label22 = new System.Windows.Forms.Label();
            this.tmrShowWalk = new System.Windows.Forms.Timer(this.components);
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            this.groupBox0.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox6)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox7)).BeginInit();
            this.groupBox6.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trkWalk)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox0
            // 
            this.pictureBox0.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox0.Location = new System.Drawing.Point(12, 12);
            this.pictureBox0.Name = "pictureBox0";
            this.pictureBox0.Size = new System.Drawing.Size(100, 100);
            this.pictureBox0.TabIndex = 16;
            this.pictureBox0.TabStop = false;
            this.pictureBox0.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox0_Paint);
            this.pictureBox0.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox0_MouseDown);
            this.pictureBox0.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox0_MouseMove);
            this.pictureBox0.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox0_MouseUp);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Navy;
            this.pictureBox1.Location = new System.Drawing.Point(133, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 60;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox2.Location = new System.Drawing.Point(258, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 61;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox3
            // 
            this.pictureBox3.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox3.Location = new System.Drawing.Point(381, 12);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3.TabIndex = 62;
            this.pictureBox3.TabStop = false;
            // 
            // pictureBox4
            // 
            this.pictureBox4.BackColor = System.Drawing.Color.Red;
            this.pictureBox4.Location = new System.Drawing.Point(12, 129);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 100);
            this.pictureBox4.TabIndex = 63;
            this.pictureBox4.TabStop = false;
            this.pictureBox4.Resize += new System.EventHandler(this.pictureBox4_Resize);
            // 
            // pictureBox5
            // 
            this.pictureBox5.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox5.Location = new System.Drawing.Point(133, 129);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(100, 100);
            this.pictureBox5.TabIndex = 68;
            this.pictureBox5.TabStop = false;
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.rb6);
            this.groupBox0.Controls.Add(this.rb5);
            this.groupBox0.Controls.Add(this.rb4);
            this.groupBox0.Controls.Add(this.rb3);
            this.groupBox0.Controls.Add(this.rb2);
            this.groupBox0.Controls.Add(this.rb1);
            this.groupBox0.Controls.Add(this.button1);
            this.groupBox0.Location = new System.Drawing.Point(416, 532);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(309, 56);
            this.groupBox0.TabIndex = 69;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "萬花筒";
            // 
            // rb6
            // 
            this.rb6.AutoSize = true;
            this.rb6.Location = new System.Drawing.Point(246, 24);
            this.rb6.Name = "rb6";
            this.rb6.Size = new System.Drawing.Size(29, 16);
            this.rb6.TabIndex = 6;
            this.rb6.Text = "8";
            this.rb6.UseVisualStyleBackColor = true;
            // 
            // rb5
            // 
            this.rb5.AutoSize = true;
            this.rb5.Location = new System.Drawing.Point(214, 24);
            this.rb5.Name = "rb5";
            this.rb5.Size = new System.Drawing.Size(29, 16);
            this.rb5.TabIndex = 5;
            this.rb5.Text = "4";
            this.rb5.UseVisualStyleBackColor = true;
            // 
            // rb4
            // 
            this.rb4.AutoSize = true;
            this.rb4.Location = new System.Drawing.Point(177, 24);
            this.rb4.Name = "rb4";
            this.rb4.Size = new System.Drawing.Size(29, 16);
            this.rb4.TabIndex = 4;
            this.rb4.Text = "2";
            this.rb4.UseVisualStyleBackColor = true;
            // 
            // rb3
            // 
            this.rb3.AutoSize = true;
            this.rb3.Location = new System.Drawing.Point(140, 24);
            this.rb3.Name = "rb3";
            this.rb3.Size = new System.Drawing.Size(39, 16);
            this.rb3.TabIndex = 3;
            this.rb3.Text = "XY";
            this.rb3.UseVisualStyleBackColor = true;
            // 
            // rb2
            // 
            this.rb2.AutoSize = true;
            this.rb2.Location = new System.Drawing.Point(115, 24);
            this.rb2.Name = "rb2";
            this.rb2.Size = new System.Drawing.Size(31, 16);
            this.rb2.TabIndex = 2;
            this.rb2.Text = "Y";
            this.rb2.UseVisualStyleBackColor = true;
            // 
            // rb1
            // 
            this.rb1.AutoSize = true;
            this.rb1.Checked = true;
            this.rb1.Location = new System.Drawing.Point(78, 24);
            this.rb1.Name = "rb1";
            this.rb1.Size = new System.Drawing.Size(31, 16);
            this.rb1.TabIndex = 1;
            this.rb1.TabStop = true;
            this.rb1.Text = "X";
            this.rb1.UseVisualStyleBackColor = true;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(15, 21);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(54, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "Reset";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // chkTrueSpiral
            // 
            this.chkTrueSpiral.AutoSize = true;
            this.chkTrueSpiral.Checked = true;
            this.chkTrueSpiral.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkTrueSpiral.ForeColor = System.Drawing.Color.Blue;
            this.chkTrueSpiral.Location = new System.Drawing.Point(295, 24);
            this.chkTrueSpiral.Name = "chkTrueSpiral";
            this.chkTrueSpiral.Size = new System.Drawing.Size(76, 16);
            this.chkTrueSpiral.TabIndex = 73;
            this.chkTrueSpiral.Text = "True Spiral";
            this.chkTrueSpiral.UseVisualStyleBackColor = true;
            this.chkTrueSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkCircularSpiral
            // 
            this.chkCircularSpiral.AutoSize = true;
            this.chkCircularSpiral.ForeColor = System.Drawing.Color.Red;
            this.chkCircularSpiral.Location = new System.Drawing.Point(195, 24);
            this.chkCircularSpiral.Name = "chkCircularSpiral";
            this.chkCircularSpiral.Size = new System.Drawing.Size(92, 16);
            this.chkCircularSpiral.TabIndex = 72;
            this.chkCircularSpiral.Text = "Circular Spiral";
            this.chkCircularSpiral.UseVisualStyleBackColor = true;
            this.chkCircularSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkSquareSpiral
            // 
            this.chkSquareSpiral.AutoSize = true;
            this.chkSquareSpiral.ForeColor = System.Drawing.Color.Green;
            this.chkSquareSpiral.Location = new System.Drawing.Point(96, 24);
            this.chkSquareSpiral.Name = "chkSquareSpiral";
            this.chkSquareSpiral.Size = new System.Drawing.Size(86, 16);
            this.chkSquareSpiral.TabIndex = 71;
            this.chkSquareSpiral.Text = "Square Spiral";
            this.chkSquareSpiral.UseVisualStyleBackColor = true;
            this.chkSquareSpiral.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // chkRectangles
            // 
            this.chkRectangles.AutoSize = true;
            this.chkRectangles.Checked = true;
            this.chkRectangles.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkRectangles.Location = new System.Drawing.Point(6, 24);
            this.chkRectangles.Name = "chkRectangles";
            this.chkRectangles.Size = new System.Drawing.Size(74, 16);
            this.chkRectangles.TabIndex = 70;
            this.chkRectangles.Text = "Rectangles";
            this.chkRectangles.UseVisualStyleBackColor = true;
            this.chkRectangles.CheckedChanged += new System.EventHandler(this.Options_CheckedChanged);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.chkRectangles);
            this.groupBox3.Controls.Add(this.chkTrueSpiral);
            this.groupBox3.Controls.Add(this.chkSquareSpiral);
            this.groupBox3.Controls.Add(this.chkCircularSpiral);
            this.groupBox3.Location = new System.Drawing.Point(12, 532);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(379, 56);
            this.groupBox3.TabIndex = 70;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Phi Spiral";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.chkOutline);
            this.groupBox2.Controls.Add(this.btnDraw);
            this.groupBox2.Controls.Add(this.txtNumTriangles);
            this.groupBox2.Controls.Add(this.chkFill);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(12, 459);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(309, 67);
            this.groupBox2.TabIndex = 70;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "spiral_of_theodorus";
            // 
            // chkOutline
            // 
            this.chkOutline.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.chkOutline.Checked = true;
            this.chkOutline.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkOutline.Location = new System.Drawing.Point(138, 21);
            this.chkOutline.Name = "chkOutline";
            this.chkOutline.Size = new System.Drawing.Size(83, 16);
            this.chkOutline.TabIndex = 6;
            this.chkOutline.Text = "Outline";
            this.chkOutline.UseVisualStyleBackColor = true;
            // 
            // btnDraw
            // 
            this.btnDraw.Location = new System.Drawing.Point(227, 23);
            this.btnDraw.Name = "btnDraw";
            this.btnDraw.Size = new System.Drawing.Size(75, 21);
            this.btnDraw.TabIndex = 8;
            this.btnDraw.Text = "Draw";
            this.btnDraw.UseVisualStyleBackColor = true;
            this.btnDraw.Click += new System.EventHandler(this.btnDraw_Click);
            // 
            // txtNumTriangles
            // 
            this.txtNumTriangles.Location = new System.Drawing.Point(78, 24);
            this.txtNumTriangles.Name = "txtNumTriangles";
            this.txtNumTriangles.Size = new System.Drawing.Size(49, 22);
            this.txtNumTriangles.TabIndex = 5;
            this.txtNumTriangles.Text = "16";
            this.txtNumTriangles.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // chkFill
            // 
            this.chkFill.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.chkFill.Checked = true;
            this.chkFill.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkFill.Location = new System.Drawing.Point(138, 42);
            this.chkFill.Name = "chkFill";
            this.chkFill.Size = new System.Drawing.Size(83, 16);
            this.chkFill.TabIndex = 7;
            this.chkFill.Text = "Fill";
            this.chkFill.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(60, 12);
            this.label1.TabIndex = 4;
            this.label1.Text = "# Triangles:";
            // 
            // groupBox1
            // 
            this.groupBox1.Location = new System.Drawing.Point(12, 385);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(448, 57);
            this.groupBox1.TabIndex = 74;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Epitrochoid";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.txtZ0);
            this.groupBox4.Controls.Add(this.btnStart);
            this.groupBox4.Controls.Add(this.label9);
            this.groupBox4.Controls.Add(this.txtY0);
            this.groupBox4.Controls.Add(this.label10);
            this.groupBox4.Controls.Add(this.txtX0);
            this.groupBox4.Controls.Add(this.label11);
            this.groupBox4.Controls.Add(this.txtE);
            this.groupBox4.Controls.Add(this.label8);
            this.groupBox4.Controls.Add(this.txtD);
            this.groupBox4.Controls.Add(this.label7);
            this.groupBox4.Controls.Add(this.txtC);
            this.groupBox4.Controls.Add(this.label6);
            this.groupBox4.Controls.Add(this.txtB);
            this.groupBox4.Controls.Add(this.label12);
            this.groupBox4.Controls.Add(this.txtA);
            this.groupBox4.Controls.Add(this.label13);
            this.groupBox4.Controls.Add(this.lblForeColor);
            this.groupBox4.Controls.Add(this.label14);
            this.groupBox4.Controls.Add(this.label15);
            this.groupBox4.Controls.Add(this.cboPlane);
            this.groupBox4.Controls.Add(this.label16);
            this.groupBox4.Controls.Add(this.lblBackColor);
            this.groupBox4.Location = new System.Drawing.Point(487, 12);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(468, 100);
            this.groupBox4.TabIndex = 74;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "pickover_attractor";
            // 
            // txtZ0
            // 
            this.txtZ0.Location = new System.Drawing.Point(284, 42);
            this.txtZ0.Name = "txtZ0";
            this.txtZ0.Size = new System.Drawing.Size(33, 22);
            this.txtZ0.TabIndex = 38;
            this.txtZ0.Text = "0";
            this.txtZ0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(228, 69);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(75, 21);
            this.btnStart.TabIndex = 40;
            this.btnStart.Text = "Start";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(263, 45);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(18, 12);
            this.label9.TabIndex = 47;
            this.label9.Text = "Z0";
            // 
            // txtY0
            // 
            this.txtY0.Location = new System.Drawing.Point(214, 42);
            this.txtY0.Name = "txtY0";
            this.txtY0.Size = new System.Drawing.Size(33, 22);
            this.txtY0.TabIndex = 37;
            this.txtY0.Text = "0";
            this.txtY0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(194, 45);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(19, 12);
            this.label10.TabIndex = 46;
            this.label10.Text = "Y0";
            // 
            // txtX0
            // 
            this.txtX0.Location = new System.Drawing.Point(144, 42);
            this.txtX0.Name = "txtX0";
            this.txtX0.Size = new System.Drawing.Size(33, 22);
            this.txtX0.TabIndex = 35;
            this.txtX0.Text = "0";
            this.txtX0.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(124, 45);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(19, 12);
            this.label11.TabIndex = 45;
            this.label11.Text = "X0";
            // 
            // txtE
            // 
            this.txtE.Location = new System.Drawing.Point(424, 18);
            this.txtE.Name = "txtE";
            this.txtE.Size = new System.Drawing.Size(33, 22);
            this.txtE.TabIndex = 34;
            this.txtE.Text = "1.0";
            this.txtE.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(403, 21);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(12, 12);
            this.label8.TabIndex = 44;
            this.label8.Text = "E";
            // 
            // txtD
            // 
            this.txtD.Location = new System.Drawing.Point(354, 18);
            this.txtD.Name = "txtD";
            this.txtD.Size = new System.Drawing.Size(33, 22);
            this.txtD.TabIndex = 31;
            this.txtD.Text = "-2.5";
            this.txtD.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(333, 21);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(13, 12);
            this.label7.TabIndex = 43;
            this.label7.Text = "D";
            // 
            // txtC
            // 
            this.txtC.Location = new System.Drawing.Point(284, 18);
            this.txtC.Name = "txtC";
            this.txtC.Size = new System.Drawing.Size(33, 22);
            this.txtC.TabIndex = 30;
            this.txtC.Text = "-0.6";
            this.txtC.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(263, 21);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(13, 12);
            this.label6.TabIndex = 42;
            this.label6.Text = "C";
            // 
            // txtB
            // 
            this.txtB.Location = new System.Drawing.Point(214, 18);
            this.txtB.Name = "txtB";
            this.txtB.Size = new System.Drawing.Size(33, 22);
            this.txtB.TabIndex = 28;
            this.txtB.Text = "0.5";
            this.txtB.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(194, 21);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(13, 12);
            this.label12.TabIndex = 41;
            this.label12.Text = "B";
            // 
            // txtA
            // 
            this.txtA.Location = new System.Drawing.Point(144, 18);
            this.txtA.Name = "txtA";
            this.txtA.Size = new System.Drawing.Size(33, 22);
            this.txtA.TabIndex = 26;
            this.txtA.Text = "2.0";
            this.txtA.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(124, 21);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(13, 12);
            this.label13.TabIndex = 39;
            this.label13.Text = "A";
            // 
            // lblForeColor
            // 
            this.lblForeColor.BackColor = System.Drawing.Color.Blue;
            this.lblForeColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblForeColor.Location = new System.Drawing.Point(72, 20);
            this.lblForeColor.Name = "lblForeColor";
            this.lblForeColor.Size = new System.Drawing.Size(20, 19);
            this.lblForeColor.TabIndex = 29;
            this.lblForeColor.Click += new System.EventHandler(this.ColorSample_Click);
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(5, 69);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(30, 12);
            this.label14.TabIndex = 36;
            this.label14.Text = "Plane";
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(5, 21);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(60, 12);
            this.label15.TabIndex = 27;
            this.label15.Text = "Foreground";
            // 
            // cboPlane
            // 
            this.cboPlane.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboPlane.FormattingEnabled = true;
            this.cboPlane.Items.AddRange(new object[] {
            "XY",
            "YZ",
            "XZ"});
            this.cboPlane.Location = new System.Drawing.Point(72, 66);
            this.cboPlane.Name = "cboPlane";
            this.cboPlane.Size = new System.Drawing.Size(41, 20);
            this.cboPlane.TabIndex = 25;
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(5, 45);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(63, 12);
            this.label16.TabIndex = 32;
            this.label16.Text = "Background";
            // 
            // lblBackColor
            // 
            this.lblBackColor.BackColor = System.Drawing.Color.Black;
            this.lblBackColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblBackColor.Location = new System.Drawing.Point(72, 44);
            this.lblBackColor.Name = "lblBackColor";
            this.lblBackColor.Size = new System.Drawing.Size(20, 19);
            this.lblBackColor.TabIndex = 33;
            this.lblBackColor.Click += new System.EventHandler(this.ColorSample_Click);
            // 
            // pictureBox6
            // 
            this.pictureBox6.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox6.Location = new System.Drawing.Point(258, 129);
            this.pictureBox6.Name = "pictureBox6";
            this.pictureBox6.Size = new System.Drawing.Size(100, 100);
            this.pictureBox6.TabIndex = 75;
            this.pictureBox6.TabStop = false;
            // 
            // pictureBox7
            // 
            this.pictureBox7.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox7.Location = new System.Drawing.Point(381, 129);
            this.pictureBox7.Name = "pictureBox7";
            this.pictureBox7.Size = new System.Drawing.Size(100, 100);
            this.pictureBox7.TabIndex = 76;
            this.pictureBox7.TabStop = false;
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.scrSpeed);
            this.groupBox6.Controls.Add(this.lblWalkNum2);
            this.groupBox6.Controls.Add(this.lblWalkNum);
            this.groupBox6.Controls.Add(this.trkWalk);
            this.groupBox6.Controls.Add(this.lblResults);
            this.groupBox6.Controls.Add(this.btnGenerate);
            this.groupBox6.Controls.Add(this.txtHeight);
            this.groupBox6.Controls.Add(this.label21);
            this.groupBox6.Controls.Add(this.txtWidth);
            this.groupBox6.Controls.Add(this.label22);
            this.groupBox6.Location = new System.Drawing.Point(12, 251);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(960, 114);
            this.groupBox6.TabIndex = 75;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "self_avoiding_corner_walk";
            // 
            // scrSpeed
            // 
            this.scrSpeed.LargeChange = 1;
            this.scrSpeed.Location = new System.Drawing.Point(453, 65);
            this.scrSpeed.Minimum = 1;
            this.scrSpeed.Name = "scrSpeed";
            this.scrSpeed.Size = new System.Drawing.Size(248, 21);
            this.scrSpeed.TabIndex = 32;
            this.scrSpeed.Value = 2;
            this.scrSpeed.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrSpeed_Scroll);
            // 
            // lblWalkNum2
            // 
            this.lblWalkNum2.AutoSize = true;
            this.lblWalkNum2.Location = new System.Drawing.Point(451, 26);
            this.lblWalkNum2.Name = "lblWalkNum2";
            this.lblWalkNum2.Size = new System.Drawing.Size(45, 12);
            this.lblWalkNum2.TabIndex = 33;
            this.lblWalkNum2.Text = "XXXXX";
            // 
            // lblWalkNum
            // 
            this.lblWalkNum.AutoSize = true;
            this.lblWalkNum.Location = new System.Drawing.Point(205, 97);
            this.lblWalkNum.Name = "lblWalkNum";
            this.lblWalkNum.Size = new System.Drawing.Size(0, 12);
            this.lblWalkNum.TabIndex = 25;
            // 
            // trkWalk
            // 
            this.trkWalk.Location = new System.Drawing.Point(205, 62);
            this.trkWalk.Name = "trkWalk";
            this.trkWalk.Size = new System.Drawing.Size(210, 45);
            this.trkWalk.TabIndex = 24;
            this.trkWalk.Visible = false;
            this.trkWalk.Scroll += new System.EventHandler(this.trkWalk_Scroll);
            // 
            // lblResults
            // 
            this.lblResults.AutoSize = true;
            this.lblResults.Location = new System.Drawing.Point(214, 24);
            this.lblResults.Name = "lblResults";
            this.lblResults.Size = new System.Drawing.Size(45, 12);
            this.lblResults.TabIndex = 23;
            this.lblResults.Text = "XXXXX";
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(58, 50);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(75, 21);
            this.btnGenerate.TabIndex = 22;
            this.btnGenerate.Text = "Generate";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // txtHeight
            // 
            this.txtHeight.Location = new System.Drawing.Point(147, 26);
            this.txtHeight.Name = "txtHeight";
            this.txtHeight.Size = new System.Drawing.Size(42, 22);
            this.txtHeight.TabIndex = 21;
            this.txtHeight.Text = "4";
            this.txtHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(103, 28);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(39, 12);
            this.label21.TabIndex = 20;
            this.label21.Text = "Height:";
            // 
            // txtWidth
            // 
            this.txtWidth.Location = new System.Drawing.Point(51, 26);
            this.txtWidth.Name = "txtWidth";
            this.txtWidth.Size = new System.Drawing.Size(42, 22);
            this.txtWidth.TabIndex = 19;
            this.txtWidth.Text = "4";
            this.txtWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label22
            // 
            this.label22.AutoSize = true;
            this.label22.Location = new System.Drawing.Point(11, 28);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(37, 12);
            this.label22.TabIndex = 18;
            this.label22.Text = "Width:";
            // 
            // tmrShowWalk
            // 
            this.tmrShowWalk.Interval = 500;
            this.tmrShowWalk.Tick += new System.EventHandler(this.tmrShowWalk_Tick);
            // 
            // groupBox5
            // 
            this.groupBox5.Location = new System.Drawing.Point(487, 118);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(303, 74);
            this.groupBox5.TabIndex = 74;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "queue_breadth_first_tree";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1105, 594);
            this.Controls.Add(this.groupBox6);
            this.Controls.Add(this.pictureBox7);
            this.Controls.Add(this.pictureBox6);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.pictureBox5);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.pictureBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).EndInit();
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox6)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox7)).EndInit();
            this.groupBox6.ResumeLayout(false);
            this.groupBox6.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trkWalk)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox0;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.PictureBox pictureBox5;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.RadioButton rb6;
        private System.Windows.Forms.RadioButton rb5;
        private System.Windows.Forms.RadioButton rb4;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.CheckBox chkTrueSpiral;
        private System.Windows.Forms.CheckBox chkCircularSpiral;
        private System.Windows.Forms.CheckBox chkSquareSpiral;
        private System.Windows.Forms.CheckBox chkRectangles;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.CheckBox chkOutline;
        private System.Windows.Forms.Button btnDraw;
        private System.Windows.Forms.TextBox txtNumTriangles;
        private System.Windows.Forms.CheckBox chkFill;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.TextBox txtZ0;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox txtY0;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.TextBox txtX0;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox txtE;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox txtD;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox txtC;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox txtB;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox txtA;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label lblForeColor;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.ComboBox cboPlane;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label lblBackColor;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.PictureBox pictureBox6;
        private System.Windows.Forms.PictureBox pictureBox7;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.Label lblWalkNum;
        private System.Windows.Forms.TrackBar trkWalk;
        private System.Windows.Forms.Label lblResults;
        private System.Windows.Forms.Button btnGenerate;
        private System.Windows.Forms.TextBox txtHeight;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.TextBox txtWidth;
        private System.Windows.Forms.Label label22;
        private System.Windows.Forms.HScrollBar scrSpeed;
        private System.Windows.Forms.Label lblWalkNum2;
        private System.Windows.Forms.Timer tmrShowWalk;
        private System.Windows.Forms.GroupBox groupBox5;
    }
}

