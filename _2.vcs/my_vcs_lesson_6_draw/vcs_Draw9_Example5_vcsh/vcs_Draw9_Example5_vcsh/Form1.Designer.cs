namespace vcs_Draw9_Example5_vcsh
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
            this.bt_save = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
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
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.chkOutline = new System.Windows.Forms.CheckBox();
            this.btnDraw = new System.Windows.Forms.Button();
            this.txtNumTriangles = new System.Windows.Forms.TextBox();
            this.chkFill = new System.Windows.Forms.CheckBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.txtDt = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.txtH = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.txtB = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.txtA = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.timer_epitrochoid = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
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
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(1030, 12);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(63, 40);
            this.bt_save.TabIndex = 58;
            this.bt_save.Text = "Save";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1018, 374);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(63, 40);
            this.bt_clear.TabIndex = 57;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(856, 172);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(237, 297);
            this.richTextBox1.TabIndex = 59;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Navy;
            this.pictureBox1.Location = new System.Drawing.Point(133, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 60;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
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
            this.pictureBox3.Location = new System.Drawing.Point(12, 129);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3.TabIndex = 62;
            this.pictureBox3.TabStop = false;
            // 
            // pictureBox4
            // 
            this.pictureBox4.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox4.Location = new System.Drawing.Point(136, 129);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 100);
            this.pictureBox4.TabIndex = 63;
            this.pictureBox4.TabStop = false;
            // 
            // pictureBox5
            // 
            this.pictureBox5.BackColor = System.Drawing.SystemColors.ControlLight;
            this.pictureBox5.Location = new System.Drawing.Point(258, 129);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(100, 100);
            this.pictureBox5.TabIndex = 68;
            this.pictureBox5.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb6);
            this.groupBox1.Controls.Add(this.rb5);
            this.groupBox1.Controls.Add(this.rb4);
            this.groupBox1.Controls.Add(this.rb3);
            this.groupBox1.Controls.Add(this.rb2);
            this.groupBox1.Controls.Add(this.rb1);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Location = new System.Drawing.Point(12, 294);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(309, 56);
            this.groupBox1.TabIndex = 69;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "萬花筒";
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
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.chkRectangles);
            this.groupBox2.Controls.Add(this.chkTrueSpiral);
            this.groupBox2.Controls.Add(this.chkSquareSpiral);
            this.groupBox2.Controls.Add(this.chkCircularSpiral);
            this.groupBox2.Location = new System.Drawing.Point(355, 294);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(379, 56);
            this.groupBox2.TabIndex = 70;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Phi Spiral";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.chkOutline);
            this.groupBox3.Controls.Add(this.btnDraw);
            this.groupBox3.Controls.Add(this.txtNumTriangles);
            this.groupBox3.Controls.Add(this.chkFill);
            this.groupBox3.Controls.Add(this.label1);
            this.groupBox3.Location = new System.Drawing.Point(12, 402);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(309, 67);
            this.groupBox3.TabIndex = 70;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "spiral_of_theodorus";
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
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.txtDt);
            this.groupBox4.Controls.Add(this.label4);
            this.groupBox4.Controls.Add(this.button2);
            this.groupBox4.Controls.Add(this.txtH);
            this.groupBox4.Controls.Add(this.label3);
            this.groupBox4.Controls.Add(this.txtB);
            this.groupBox4.Controls.Add(this.label2);
            this.groupBox4.Controls.Add(this.txtA);
            this.groupBox4.Controls.Add(this.label5);
            this.groupBox4.Location = new System.Drawing.Point(379, 444);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(448, 57);
            this.groupBox4.TabIndex = 74;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Epitrochoid";
            // 
            // txtDt
            // 
            this.txtDt.Location = new System.Drawing.Point(301, 22);
            this.txtDt.Name = "txtDt";
            this.txtDt.Size = new System.Drawing.Size(44, 22);
            this.txtDt.TabIndex = 25;
            this.txtDt.Text = "0.05";
            this.txtDt.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(276, 25);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(17, 12);
            this.label4.TabIndex = 30;
            this.label4.Text = "dt:";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(360, 20);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 21);
            this.button2.TabIndex = 26;
            this.button2.Text = "Draw";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // txtH
            // 
            this.txtH.Location = new System.Drawing.Point(210, 22);
            this.txtH.Name = "txtH";
            this.txtH.Size = new System.Drawing.Size(44, 22);
            this.txtH.TabIndex = 24;
            this.txtH.Text = "4";
            this.txtH.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(188, 25);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(14, 12);
            this.label3.TabIndex = 29;
            this.label3.Text = "h:";
            // 
            // txtB
            // 
            this.txtB.Location = new System.Drawing.Point(122, 22);
            this.txtB.Name = "txtB";
            this.txtB.Size = new System.Drawing.Size(44, 22);
            this.txtB.TabIndex = 23;
            this.txtB.Text = "3";
            this.txtB.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(100, 25);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(14, 12);
            this.label2.TabIndex = 28;
            this.label2.Text = "b:";
            // 
            // txtA
            // 
            this.txtA.Location = new System.Drawing.Point(34, 22);
            this.txtA.Name = "txtA";
            this.txtA.Size = new System.Drawing.Size(44, 22);
            this.txtA.TabIndex = 22;
            this.txtA.Text = "5";
            this.txtA.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 25);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(13, 12);
            this.label5.TabIndex = 27;
            this.label5.Text = "a:";
            // 
            // timer_epitrochoid
            // 
            this.timer_epitrochoid.Interval = 10;
            this.timer_epitrochoid.Tick += new System.EventHandler(this.timer_epitrochoid_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1105, 594);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.pictureBox5);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.bt_save);
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
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox0;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.PictureBox pictureBox5;
        private System.Windows.Forms.GroupBox groupBox1;
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
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.CheckBox chkOutline;
        private System.Windows.Forms.Button btnDraw;
        private System.Windows.Forms.TextBox txtNumTriangles;
        private System.Windows.Forms.CheckBox chkFill;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.TextBox txtDt;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox txtH;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtB;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtA;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Timer timer_epitrochoid;
    }
}

