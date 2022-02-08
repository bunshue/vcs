namespace vcs_RGB2YUV_HLS
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
            this.lb_b = new System.Windows.Forms.Label();
            this.lb_g = new System.Windows.Forms.Label();
            this.lb_r = new System.Windows.Forms.Label();
            this.textBox4 = new System.Windows.Forms.TextBox();
            this.textBox5 = new System.Windows.Forms.TextBox();
            this.textBox6 = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.lb_v = new System.Windows.Forms.Label();
            this.lb_u = new System.Windows.Forms.Label();
            this.lb_y = new System.Windows.Forms.Label();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtS = new System.Windows.Forms.TextBox();
            this.txtL = new System.Windows.Forms.TextBox();
            this.txtH = new System.Windows.Forms.TextBox();
            this.picSample = new System.Windows.Forms.PictureBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.nudB = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.nudG = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.nudR = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.textBox7 = new System.Windows.Forms.TextBox();
            this.textBox8 = new System.Windows.Forms.TextBox();
            this.textBox9 = new System.Windows.Forms.TextBox();
            this.txtB = new System.Windows.Forms.TextBox();
            this.txtG = new System.Windows.Forms.TextBox();
            this.txtR = new System.Windows.Forms.TextBox();
            this.scrS = new System.Windows.Forms.HScrollBar();
            this.label7 = new System.Windows.Forms.Label();
            this.scrL = new System.Windows.Forms.HScrollBar();
            this.label8 = new System.Windows.Forms.Label();
            this.scrH = new System.Windows.Forms.HScrollBar();
            this.label9 = new System.Windows.Forms.Label();
            this.scrB = new System.Windows.Forms.HScrollBar();
            this.label10 = new System.Windows.Forms.Label();
            this.scrG = new System.Windows.Forms.HScrollBar();
            this.label11 = new System.Windows.Forms.Label();
            this.scrR = new System.Windows.Forms.HScrollBar();
            this.label12 = new System.Windows.Forms.Label();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudB)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudG)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudR)).BeginInit();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // lb_b
            // 
            this.lb_b.AutoSize = true;
            this.lb_b.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_b.ForeColor = System.Drawing.Color.Blue;
            this.lb_b.Location = new System.Drawing.Point(332, 94);
            this.lb_b.Name = "lb_b";
            this.lb_b.Size = new System.Drawing.Size(58, 21);
            this.lb_b.TabIndex = 34;
            this.lb_b.Text = "label3";
            // 
            // lb_g
            // 
            this.lb_g.AutoSize = true;
            this.lb_g.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_g.ForeColor = System.Drawing.Color.Green;
            this.lb_g.Location = new System.Drawing.Point(332, 56);
            this.lb_g.Name = "lb_g";
            this.lb_g.Size = new System.Drawing.Size(58, 21);
            this.lb_g.TabIndex = 33;
            this.lb_g.Text = "label2";
            // 
            // lb_r
            // 
            this.lb_r.AutoSize = true;
            this.lb_r.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_r.ForeColor = System.Drawing.Color.Red;
            this.lb_r.Location = new System.Drawing.Point(332, 17);
            this.lb_r.Name = "lb_r";
            this.lb_r.Size = new System.Drawing.Size(58, 21);
            this.lb_r.TabIndex = 32;
            this.lb_r.Text = "label1";
            // 
            // textBox4
            // 
            this.textBox4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox4.ForeColor = System.Drawing.Color.Black;
            this.textBox4.Location = new System.Drawing.Point(241, 16);
            this.textBox4.Name = "textBox4";
            this.textBox4.Size = new System.Drawing.Size(75, 30);
            this.textBox4.TabIndex = 31;
            this.textBox4.Text = "0";
            this.textBox4.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox5
            // 
            this.textBox5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox5.ForeColor = System.Drawing.Color.Black;
            this.textBox5.Location = new System.Drawing.Point(241, 55);
            this.textBox5.Name = "textBox5";
            this.textBox5.Size = new System.Drawing.Size(75, 30);
            this.textBox5.TabIndex = 30;
            this.textBox5.Text = "0";
            this.textBox5.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox6
            // 
            this.textBox6.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox6.ForeColor = System.Drawing.Color.Black;
            this.textBox6.Location = new System.Drawing.Point(241, 94);
            this.textBox6.Name = "textBox6";
            this.textBox6.Size = new System.Drawing.Size(75, 30);
            this.textBox6.TabIndex = 29;
            this.textBox6.Text = "0";
            this.textBox6.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(274, 140);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 28;
            this.button2.Text = "YUV2RGB";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // lb_v
            // 
            this.lb_v.AutoSize = true;
            this.lb_v.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_v.Location = new System.Drawing.Point(103, 95);
            this.lb_v.Name = "lb_v";
            this.lb_v.Size = new System.Drawing.Size(58, 21);
            this.lb_v.TabIndex = 27;
            this.lb_v.Text = "label3";
            // 
            // lb_u
            // 
            this.lb_u.AutoSize = true;
            this.lb_u.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_u.Location = new System.Drawing.Point(103, 57);
            this.lb_u.Name = "lb_u";
            this.lb_u.Size = new System.Drawing.Size(58, 21);
            this.lb_u.TabIndex = 26;
            this.lb_u.Text = "label2";
            // 
            // lb_y
            // 
            this.lb_y.AutoSize = true;
            this.lb_y.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y.Location = new System.Drawing.Point(103, 18);
            this.lb_y.Name = "lb_y";
            this.lb_y.Size = new System.Drawing.Size(58, 21);
            this.lb_y.TabIndex = 25;
            this.lb_y.Text = "label1";
            // 
            // textBox3
            // 
            this.textBox3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox3.ForeColor = System.Drawing.Color.Blue;
            this.textBox3.Location = new System.Drawing.Point(12, 94);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(75, 30);
            this.textBox3.TabIndex = 24;
            this.textBox3.Text = "0";
            this.textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox2.ForeColor = System.Drawing.Color.Green;
            this.textBox2.Location = new System.Drawing.Point(12, 56);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(75, 30);
            this.textBox2.TabIndex = 23;
            this.textBox2.Text = "0";
            this.textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.textBox1.ForeColor = System.Drawing.Color.Red;
            this.textBox1.Location = new System.Drawing.Point(12, 17);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(75, 30);
            this.textBox1.TabIndex = 22;
            this.textBox1.Text = "0";
            this.textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(45, 140);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 21;
            this.button1.Text = "RGB2YUV";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 398);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(404, 124);
            this.richTextBox1.TabIndex = 35;
            this.richTextBox1.Text = "";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.txtS);
            this.groupBox1.Controls.Add(this.txtL);
            this.groupBox1.Controls.Add(this.txtH);
            this.groupBox1.Controls.Add(this.picSample);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.nudB);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.nudG);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.nudR);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 192);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(255, 183);
            this.groupBox1.TabIndex = 36;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "RGB HLS";
            // 
            // txtS
            // 
            this.txtS.Location = new System.Drawing.Point(172, 77);
            this.txtS.Name = "txtS";
            this.txtS.Size = new System.Drawing.Size(50, 22);
            this.txtS.TabIndex = 41;
            this.txtS.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtS.TextChanged += new System.EventHandler(this.txtHLS_TextChanged);
            // 
            // txtL
            // 
            this.txtL.Location = new System.Drawing.Point(172, 53);
            this.txtL.Name = "txtL";
            this.txtL.Size = new System.Drawing.Size(50, 22);
            this.txtL.TabIndex = 40;
            this.txtL.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtL.TextChanged += new System.EventHandler(this.txtHLS_TextChanged);
            // 
            // txtH
            // 
            this.txtH.Location = new System.Drawing.Point(172, 29);
            this.txtH.Name = "txtH";
            this.txtH.Size = new System.Drawing.Size(50, 22);
            this.txtH.TabIndex = 39;
            this.txtH.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtH.TextChanged += new System.EventHandler(this.txtHLS_TextChanged);
            // 
            // picSample
            // 
            this.picSample.Location = new System.Drawing.Point(31, 102);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(191, 66);
            this.picSample.TabIndex = 38;
            this.picSample.TabStop = false;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(148, 80);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(14, 12);
            this.label4.TabIndex = 37;
            this.label4.Text = "S:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(148, 56);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(15, 12);
            this.label5.TabIndex = 36;
            this.label5.Text = "L:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(148, 32);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(16, 12);
            this.label6.TabIndex = 35;
            this.label6.Text = "H:";
            // 
            // nudB
            // 
            this.nudB.Location = new System.Drawing.Point(55, 78);
            this.nudB.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.nudB.Name = "nudB";
            this.nudB.Size = new System.Drawing.Size(50, 22);
            this.nudB.TabIndex = 34;
            this.nudB.Value = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.nudB.ValueChanged += new System.EventHandler(this.nudRGB_ValueChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(31, 80);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(16, 12);
            this.label3.TabIndex = 33;
            this.label3.Text = "B:";
            // 
            // nudG
            // 
            this.nudG.Location = new System.Drawing.Point(55, 54);
            this.nudG.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.nudG.Name = "nudG";
            this.nudG.Size = new System.Drawing.Size(50, 22);
            this.nudG.TabIndex = 32;
            this.nudG.Value = new decimal(new int[] {
            128,
            0,
            0,
            0});
            this.nudG.ValueChanged += new System.EventHandler(this.nudRGB_ValueChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(31, 56);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(16, 12);
            this.label2.TabIndex = 31;
            this.label2.Text = "G:";
            // 
            // nudR
            // 
            this.nudR.Location = new System.Drawing.Point(55, 30);
            this.nudR.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.nudR.Name = "nudR";
            this.nudR.Size = new System.Drawing.Size(50, 22);
            this.nudR.TabIndex = 30;
            this.nudR.ValueChanged += new System.EventHandler(this.nudRGB_ValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(31, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(16, 12);
            this.label1.TabIndex = 29;
            this.label1.Text = "R:";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.pictureBox2);
            this.groupBox2.Controls.Add(this.textBox7);
            this.groupBox2.Controls.Add(this.textBox8);
            this.groupBox2.Controls.Add(this.textBox9);
            this.groupBox2.Controls.Add(this.txtB);
            this.groupBox2.Controls.Add(this.txtG);
            this.groupBox2.Controls.Add(this.txtR);
            this.groupBox2.Controls.Add(this.scrS);
            this.groupBox2.Controls.Add(this.label7);
            this.groupBox2.Controls.Add(this.scrL);
            this.groupBox2.Controls.Add(this.label8);
            this.groupBox2.Controls.Add(this.scrH);
            this.groupBox2.Controls.Add(this.label9);
            this.groupBox2.Controls.Add(this.scrB);
            this.groupBox2.Controls.Add(this.label10);
            this.groupBox2.Controls.Add(this.scrG);
            this.groupBox2.Controls.Add(this.label11);
            this.groupBox2.Controls.Add(this.scrR);
            this.groupBox2.Controls.Add(this.label12);
            this.groupBox2.Location = new System.Drawing.Point(274, 192);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(448, 209);
            this.groupBox2.TabIndex = 37;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "groupBox2";
            // 
            // textBox7
            // 
            this.textBox7.Location = new System.Drawing.Point(389, 124);
            this.textBox7.Name = "textBox7";
            this.textBox7.ReadOnly = true;
            this.textBox7.Size = new System.Drawing.Size(41, 22);
            this.textBox7.TabIndex = 82;
            this.textBox7.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // textBox8
            // 
            this.textBox8.Location = new System.Drawing.Point(389, 105);
            this.textBox8.Name = "textBox8";
            this.textBox8.ReadOnly = true;
            this.textBox8.Size = new System.Drawing.Size(41, 22);
            this.textBox8.TabIndex = 81;
            this.textBox8.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // textBox9
            // 
            this.textBox9.Location = new System.Drawing.Point(389, 84);
            this.textBox9.Name = "textBox9";
            this.textBox9.ReadOnly = true;
            this.textBox9.Size = new System.Drawing.Size(41, 22);
            this.textBox9.TabIndex = 80;
            this.textBox9.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtB
            // 
            this.txtB.Location = new System.Drawing.Point(389, 57);
            this.txtB.Name = "txtB";
            this.txtB.ReadOnly = true;
            this.txtB.Size = new System.Drawing.Size(41, 22);
            this.txtB.TabIndex = 79;
            this.txtB.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtG
            // 
            this.txtG.Location = new System.Drawing.Point(389, 37);
            this.txtG.Name = "txtG";
            this.txtG.ReadOnly = true;
            this.txtG.Size = new System.Drawing.Size(41, 22);
            this.txtG.TabIndex = 78;
            this.txtG.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtR
            // 
            this.txtR.Location = new System.Drawing.Point(389, 18);
            this.txtR.Name = "txtR";
            this.txtR.ReadOnly = true;
            this.txtR.Size = new System.Drawing.Size(41, 22);
            this.txtR.TabIndex = 77;
            this.txtR.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // scrS
            // 
            this.scrS.LargeChange = 100;
            this.scrS.Location = new System.Drawing.Point(62, 123);
            this.scrS.Maximum = 1099;
            this.scrS.Name = "scrS";
            this.scrS.Size = new System.Drawing.Size(324, 17);
            this.scrS.SmallChange = 10;
            this.scrS.TabIndex = 76;
            this.scrS.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrHLS_Scroll);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(41, 123);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(14, 12);
            this.label7.TabIndex = 75;
            this.label7.Text = "S:";
            // 
            // scrL
            // 
            this.scrL.LargeChange = 100;
            this.scrL.Location = new System.Drawing.Point(62, 104);
            this.scrL.Maximum = 1099;
            this.scrL.Name = "scrL";
            this.scrL.Size = new System.Drawing.Size(324, 17);
            this.scrL.SmallChange = 10;
            this.scrL.TabIndex = 74;
            this.scrL.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrHLS_Scroll);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(41, 104);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(15, 12);
            this.label8.TabIndex = 73;
            this.label8.Text = "L:";
            // 
            // scrH
            // 
            this.scrH.Location = new System.Drawing.Point(62, 84);
            this.scrH.Maximum = 369;
            this.scrH.Name = "scrH";
            this.scrH.Size = new System.Drawing.Size(324, 17);
            this.scrH.TabIndex = 72;
            this.scrH.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrHLS_Scroll);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(41, 84);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(16, 12);
            this.label9.TabIndex = 71;
            this.label9.Text = "H:";
            // 
            // scrB
            // 
            this.scrB.Location = new System.Drawing.Point(62, 57);
            this.scrB.Maximum = 264;
            this.scrB.Name = "scrB";
            this.scrB.Size = new System.Drawing.Size(324, 17);
            this.scrB.TabIndex = 70;
            this.scrB.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrRGB_Scroll);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(41, 57);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(16, 12);
            this.label10.TabIndex = 69;
            this.label10.Text = "B:";
            // 
            // scrG
            // 
            this.scrG.Location = new System.Drawing.Point(62, 37);
            this.scrG.Maximum = 264;
            this.scrG.Name = "scrG";
            this.scrG.Size = new System.Drawing.Size(324, 17);
            this.scrG.TabIndex = 68;
            this.scrG.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrRGB_Scroll);
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(41, 37);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(16, 12);
            this.label11.TabIndex = 67;
            this.label11.Text = "G:";
            // 
            // scrR
            // 
            this.scrR.Location = new System.Drawing.Point(62, 18);
            this.scrR.Maximum = 264;
            this.scrR.Name = "scrR";
            this.scrR.Size = new System.Drawing.Size(324, 17);
            this.scrR.TabIndex = 66;
            this.scrR.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrRGB_Scroll);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(41, 18);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(16, 12);
            this.label12.TabIndex = 65;
            this.label12.Text = "R:";
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(123, 143);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(191, 66);
            this.pictureBox2.TabIndex = 42;
            this.pictureBox2.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(734, 534);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lb_b);
            this.Controls.Add(this.lb_g);
            this.Controls.Add(this.lb_r);
            this.Controls.Add(this.textBox4);
            this.Controls.Add(this.textBox5);
            this.Controls.Add(this.textBox6);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.lb_v);
            this.Controls.Add(this.lb_u);
            this.Controls.Add(this.lb_y);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "各種色域轉換";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudB)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudG)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudR)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_b;
        private System.Windows.Forms.Label lb_g;
        private System.Windows.Forms.Label lb_r;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.TextBox textBox6;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label lb_v;
        private System.Windows.Forms.Label lb_u;
        private System.Windows.Forms.Label lb_y;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtS;
        private System.Windows.Forms.TextBox txtL;
        private System.Windows.Forms.TextBox txtH;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.NumericUpDown nudB;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown nudG;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.NumericUpDown nudR;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox textBox7;
        private System.Windows.Forms.TextBox textBox8;
        private System.Windows.Forms.TextBox textBox9;
        private System.Windows.Forms.TextBox txtB;
        private System.Windows.Forms.TextBox txtG;
        private System.Windows.Forms.TextBox txtR;
        private System.Windows.Forms.HScrollBar scrS;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.HScrollBar scrL;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.HScrollBar scrH;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.HScrollBar scrB;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.HScrollBar scrG;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.HScrollBar scrR;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.PictureBox pictureBox2;
    }
}

