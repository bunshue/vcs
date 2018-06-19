namespace vcs_BLDC
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
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button14 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.button10 = new System.Windows.Forms.Button();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.comboBox_dashtype = new System.Windows.Forms.ComboBox();
            this.comboBox_jointype = new System.Windows.Forms.ComboBox();
            this.comboBox_drawtype = new System.Windows.Forms.ComboBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tb_h = new System.Windows.Forms.TextBox();
            this.tb_w = new System.Windows.Forms.TextBox();
            this.tb_y = new System.Windows.Forms.TextBox();
            this.tb_x = new System.Windows.Forms.TextBox();
            this.numericUpDown_linewidth = new System.Windows.Forms.NumericUpDown();
            this.bt_color = new System.Windows.Forms.Button();
            this.button26 = new System.Windows.Forms.Button();
            this.button27 = new System.Windows.Forms.Button();
            this.button25 = new System.Windows.Forms.Button();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.button23 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button13 = new System.Windows.Forms.Button();
            this.button20 = new System.Windows.Forms.Button();
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.button21 = new System.Windows.Forms.Button();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.comboBox3 = new System.Windows.Forms.ComboBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tb_radius = new System.Windows.Forms.TextBox();
            this.tb_center_y = new System.Windows.Forms.TextBox();
            this.tb_center_x = new System.Windows.Forms.TextBox();
            this.numericUpDown_linewidth2 = new System.Windows.Forms.NumericUpDown();
            this.button22 = new System.Windows.Forms.Button();
            this.button24 = new System.Windows.Forms.Button();
            this.button28 = new System.Windows.Forms.Button();
            this.button29 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_linewidth)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_linewidth2)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button14);
            this.groupBox2.Controls.Add(this.button15);
            this.groupBox2.Controls.Add(this.button16);
            this.groupBox2.Controls.Add(this.button17);
            this.groupBox2.Controls.Add(this.button18);
            this.groupBox2.Location = new System.Drawing.Point(837, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(173, 173);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Fill";
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(7, 135);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(160, 23);
            this.button14.TabIndex = 4;
            this.button14.Text = "Path";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(7, 106);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(160, 23);
            this.button15.TabIndex = 3;
            this.button15.Text = "Polygon";
            this.button15.UseVisualStyleBackColor = true;
            this.button15.Click += new System.EventHandler(this.button15_Click);
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(6, 79);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(160, 23);
            this.button16.TabIndex = 2;
            this.button16.Text = "Pie deg(0~180)";
            this.button16.UseVisualStyleBackColor = true;
            this.button16.Click += new System.EventHandler(this.button16_Click);
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(6, 50);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(160, 23);
            this.button17.TabIndex = 1;
            this.button17.Text = "Ellipse";
            this.button17.UseVisualStyleBackColor = true;
            this.button17.Click += new System.EventHandler(this.button17_Click);
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(6, 21);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(160, 23);
            this.button18.TabIndex = 0;
            this.button18.Text = "Rectangle";
            this.button18.UseVisualStyleBackColor = true;
            this.button18.Click += new System.EventHandler(this.button18_Click);
            // 
            // button19
            // 
            this.button19.Location = new System.Drawing.Point(951, 469);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(53, 23);
            this.button19.TabIndex = 9;
            this.button19.Text = "clear";
            this.button19.UseVisualStyleBackColor = true;
            this.button19.Click += new System.EventHandler(this.button19_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.DefaultExt = "Image File (*.gif, *.bmp, *.jpg, *.jpeg, *.png)";
            this.openFileDialog1.FileName = "openFileDialog1";
            this.openFileDialog1.Filter = "Image File (*.gif, *.bmp, *.jpg, *.jpeg, *.png)|*.gif;*.bmp;*.jpg;*.jpeg;*.png";
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(7, 21);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(75, 23);
            this.button10.TabIndex = 10;
            this.button10.Text = "Pen Style";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.comboBox_dashtype);
            this.groupBox4.Controls.Add(this.comboBox_jointype);
            this.groupBox4.Controls.Add(this.comboBox_drawtype);
            this.groupBox4.Controls.Add(this.groupBox5);
            this.groupBox4.Controls.Add(this.numericUpDown_linewidth);
            this.groupBox4.Controls.Add(this.bt_color);
            this.groupBox4.Controls.Add(this.button26);
            this.groupBox4.Controls.Add(this.button27);
            this.groupBox4.Controls.Add(this.button25);
            this.groupBox4.Controls.Add(this.button10);
            this.groupBox4.Location = new System.Drawing.Point(658, 331);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(352, 132);
            this.groupBox4.TabIndex = 11;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "xxx";
            // 
            // comboBox_dashtype
            // 
            this.comboBox_dashtype.FormattingEnabled = true;
            this.comboBox_dashtype.Items.AddRange(new object[] {
            "Custom",
            "Dash",
            "DashDot",
            "DashDotDot",
            "Dot",
            "Solid"});
            this.comboBox_dashtype.Location = new System.Drawing.Point(228, 100);
            this.comboBox_dashtype.Name = "comboBox_dashtype";
            this.comboBox_dashtype.Size = new System.Drawing.Size(80, 20);
            this.comboBox_dashtype.TabIndex = 19;
            this.comboBox_dashtype.Text = "Custom";
            // 
            // comboBox_jointype
            // 
            this.comboBox_jointype.FormattingEnabled = true;
            this.comboBox_jointype.Items.AddRange(new object[] {
            "Bevel",
            "Miter",
            "MiterClipped",
            "Round"});
            this.comboBox_jointype.Location = new System.Drawing.Point(140, 100);
            this.comboBox_jointype.Name = "comboBox_jointype";
            this.comboBox_jointype.Size = new System.Drawing.Size(82, 20);
            this.comboBox_jointype.TabIndex = 18;
            this.comboBox_jointype.Text = "Bevel";
            // 
            // comboBox_drawtype
            // 
            this.comboBox_drawtype.FormattingEnabled = true;
            this.comboBox_drawtype.Items.AddRange(new object[] {
            "Rectangle",
            "Ellipse",
            "Pie",
            "Arc",
            "String"});
            this.comboBox_drawtype.Location = new System.Drawing.Point(228, 68);
            this.comboBox_drawtype.Name = "comboBox_drawtype";
            this.comboBox_drawtype.Size = new System.Drawing.Size(80, 20);
            this.comboBox_drawtype.TabIndex = 17;
            this.comboBox_drawtype.Text = "Rectangle";
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.label1);
            this.groupBox5.Controls.Add(this.tb_h);
            this.groupBox5.Controls.Add(this.tb_w);
            this.groupBox5.Controls.Add(this.tb_y);
            this.groupBox5.Controls.Add(this.tb_x);
            this.groupBox5.Location = new System.Drawing.Point(7, 53);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(127, 73);
            this.groupBox5.TabIndex = 16;
            this.groupBox5.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 36);
            this.label1.TabIndex = 4;
            this.label1.Text = "位置\r\n\r\n大小";
            // 
            // tb_h
            // 
            this.tb_h.Location = new System.Drawing.Point(77, 45);
            this.tb_h.Name = "tb_h";
            this.tb_h.Size = new System.Drawing.Size(40, 22);
            this.tb_h.TabIndex = 3;
            this.tb_h.Text = "200";
            this.tb_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_w
            // 
            this.tb_w.Location = new System.Drawing.Point(31, 45);
            this.tb_w.Name = "tb_w";
            this.tb_w.Size = new System.Drawing.Size(40, 22);
            this.tb_w.TabIndex = 2;
            this.tb_w.Text = "200";
            this.tb_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_y
            // 
            this.tb_y.Location = new System.Drawing.Point(77, 17);
            this.tb_y.Name = "tb_y";
            this.tb_y.Size = new System.Drawing.Size(40, 22);
            this.tb_y.TabIndex = 1;
            this.tb_y.Text = "100";
            this.tb_y.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_x
            // 
            this.tb_x.Location = new System.Drawing.Point(31, 17);
            this.tb_x.Name = "tb_x";
            this.tb_x.Size = new System.Drawing.Size(40, 22);
            this.tb_x.TabIndex = 0;
            this.tb_x.Text = "100";
            this.tb_x.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // numericUpDown_linewidth
            // 
            this.numericUpDown_linewidth.Location = new System.Drawing.Point(182, 68);
            this.numericUpDown_linewidth.Maximum = new decimal(new int[] {
            20,
            0,
            0,
            0});
            this.numericUpDown_linewidth.Name = "numericUpDown_linewidth";
            this.numericUpDown_linewidth.Size = new System.Drawing.Size(40, 22);
            this.numericUpDown_linewidth.TabIndex = 15;
            this.numericUpDown_linewidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown_linewidth.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            // 
            // bt_color
            // 
            this.bt_color.BackColor = System.Drawing.Color.Red;
            this.bt_color.Location = new System.Drawing.Point(140, 68);
            this.bt_color.Name = "bt_color";
            this.bt_color.Size = new System.Drawing.Size(36, 23);
            this.bt_color.TabIndex = 14;
            this.bt_color.UseVisualStyleBackColor = false;
            this.bt_color.Click += new System.EventHandler(this.button22_Click);
            // 
            // button26
            // 
            this.button26.Location = new System.Drawing.Point(270, 21);
            this.button26.Name = "button26";
            this.button26.Size = new System.Drawing.Size(75, 23);
            this.button26.TabIndex = 13;
            this.button26.Text = "畫X軸刻度";
            this.button26.UseVisualStyleBackColor = true;
            this.button26.Click += new System.EventHandler(this.button26_Click);
            // 
            // button27
            // 
            this.button27.Location = new System.Drawing.Point(186, 21);
            this.button27.Name = "button27";
            this.button27.Size = new System.Drawing.Size(75, 23);
            this.button27.TabIndex = 12;
            this.button27.Text = "畫X軸線";
            this.button27.UseVisualStyleBackColor = true;
            this.button27.Click += new System.EventHandler(this.button27_Click);
            // 
            // button25
            // 
            this.button25.Location = new System.Drawing.Point(91, 21);
            this.button25.Name = "button25";
            this.button25.Size = new System.Drawing.Size(75, 23);
            this.button25.TabIndex = 11;
            this.button25.Text = "畫XY軸";
            this.button25.UseVisualStyleBackColor = true;
            this.button25.Click += new System.EventHandler(this.button25_Click);
            // 
            // button23
            // 
            this.button23.Location = new System.Drawing.Point(972, 398);
            this.button23.Name = "button23";
            this.button23.Size = new System.Drawing.Size(32, 53);
            this.button23.TabIndex = 20;
            this.button23.Text = "畫";
            this.button23.UseVisualStyleBackColor = true;
            this.button23.Click += new System.EventHandler(this.button23_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.button2);
            this.groupBox1.Controls.Add(this.button3);
            this.groupBox1.Controls.Add(this.button4);
            this.groupBox1.Controls.Add(this.button5);
            this.groupBox1.Location = new System.Drawing.Point(661, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(173, 173);
            this.groupBox1.TabIndex = 10;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "BLDC";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(7, 135);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(160, 23);
            this.button1.TabIndex = 4;
            this.button1.Text = "Path";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(7, 106);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(160, 23);
            this.button2.TabIndex = 3;
            this.button2.Text = "Polygon";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(6, 79);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(160, 23);
            this.button3.TabIndex = 2;
            this.button3.Text = "Pie deg(0~180)";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(6, 50);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(160, 23);
            this.button4.TabIndex = 1;
            this.button4.Text = "Ellipse";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(6, 21);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(160, 23);
            this.button5.TabIndex = 0;
            this.button5.Text = "Hall";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click_1);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(670, 191);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(84, 23);
            this.button6.TabIndex = 5;
            this.button6.Text = "CW";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click_1);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(670, 229);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(84, 23);
            this.button7.TabIndex = 21;
            this.button7.Text = "CCW";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click_1);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(760, 229);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(84, 23);
            this.button8.TabIndex = 23;
            this.button8.Text = "SP";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click_1);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(760, 191);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(84, 23);
            this.button9.TabIndex = 22;
            this.button9.Text = "ST";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click_1);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(850, 229);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(84, 23);
            this.button11.TabIndex = 25;
            this.button11.Text = "DOWN";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click_1);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(850, 191);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(84, 23);
            this.button12.TabIndex = 24;
            this.button12.Text = "UP";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(850, 267);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(84, 22);
            this.textBox1.TabIndex = 26;
            this.textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1017, 23);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(219, 468);
            this.richTextBox1.TabIndex = 27;
            this.richTextBox1.Text = "";
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(670, 267);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(84, 23);
            this.button13.TabIndex = 28;
            this.button13.Text = "canon";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click_1);
            // 
            // button20
            // 
            this.button20.Location = new System.Drawing.Point(760, 267);
            this.button20.Name = "button20";
            this.button20.Size = new System.Drawing.Size(84, 23);
            this.button20.TabIndex = 29;
            this.button20.Text = "canon ST";
            this.button20.UseVisualStyleBackColor = true;
            // 
            // timer2
            // 
            this.timer2.Interval = 1000;
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // button21
            // 
            this.button21.Location = new System.Drawing.Point(760, 296);
            this.button21.Name = "button21";
            this.button21.Size = new System.Drawing.Size(84, 23);
            this.button21.TabIndex = 30;
            this.button21.Text = "canon SP";
            this.button21.UseVisualStyleBackColor = true;
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "Custom",
            "Dash",
            "DashDot",
            "DashDotDot",
            "Dot",
            "Solid"});
            this.comboBox1.Location = new System.Drawing.Point(886, 549);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(80, 20);
            this.comboBox1.TabIndex = 36;
            this.comboBox1.Text = "Custom";
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Items.AddRange(new object[] {
            "Bevel",
            "Miter",
            "MiterClipped",
            "Round"});
            this.comboBox2.Location = new System.Drawing.Point(798, 549);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(82, 20);
            this.comboBox2.TabIndex = 35;
            this.comboBox2.Text = "Bevel";
            // 
            // comboBox3
            // 
            this.comboBox3.FormattingEnabled = true;
            this.comboBox3.Items.AddRange(new object[] {
            "Ellipse"});
            this.comboBox3.Location = new System.Drawing.Point(886, 517);
            this.comboBox3.Name = "comboBox3";
            this.comboBox3.Size = new System.Drawing.Size(80, 20);
            this.comboBox3.TabIndex = 34;
            this.comboBox3.Text = "Eclipse";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.label2);
            this.groupBox3.Controls.Add(this.tb_radius);
            this.groupBox3.Controls.Add(this.tb_center_y);
            this.groupBox3.Controls.Add(this.tb_center_x);
            this.groupBox3.Location = new System.Drawing.Point(665, 502);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(127, 73);
            this.groupBox3.TabIndex = 33;
            this.groupBox3.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(3, 24);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 36);
            this.label2.TabIndex = 4;
            this.label2.Text = "圓心\r\n\r\n半徑";
            // 
            // tb_radius
            // 
            this.tb_radius.Location = new System.Drawing.Point(49, 45);
            this.tb_radius.Name = "tb_radius";
            this.tb_radius.Size = new System.Drawing.Size(40, 22);
            this.tb_radius.TabIndex = 2;
            this.tb_radius.Text = "200";
            this.tb_radius.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_center_y
            // 
            this.tb_center_y.Location = new System.Drawing.Point(77, 17);
            this.tb_center_y.Name = "tb_center_y";
            this.tb_center_y.Size = new System.Drawing.Size(40, 22);
            this.tb_center_y.TabIndex = 1;
            this.tb_center_y.Text = "100";
            this.tb_center_y.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tb_center_x
            // 
            this.tb_center_x.Location = new System.Drawing.Point(31, 17);
            this.tb_center_x.Name = "tb_center_x";
            this.tb_center_x.Size = new System.Drawing.Size(40, 22);
            this.tb_center_x.TabIndex = 0;
            this.tb_center_x.Text = "100";
            this.tb_center_x.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // numericUpDown_linewidth2
            // 
            this.numericUpDown_linewidth2.Location = new System.Drawing.Point(840, 517);
            this.numericUpDown_linewidth2.Maximum = new decimal(new int[] {
            20,
            0,
            0,
            0});
            this.numericUpDown_linewidth2.Name = "numericUpDown_linewidth2";
            this.numericUpDown_linewidth2.Size = new System.Drawing.Size(40, 22);
            this.numericUpDown_linewidth2.TabIndex = 32;
            this.numericUpDown_linewidth2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.numericUpDown_linewidth2.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            // 
            // button22
            // 
            this.button22.BackColor = System.Drawing.Color.Red;
            this.button22.Location = new System.Drawing.Point(798, 517);
            this.button22.Name = "button22";
            this.button22.Size = new System.Drawing.Size(36, 23);
            this.button22.TabIndex = 31;
            this.button22.UseVisualStyleBackColor = false;
            // 
            // button24
            // 
            this.button24.Location = new System.Drawing.Point(972, 516);
            this.button24.Name = "button24";
            this.button24.Size = new System.Drawing.Size(32, 53);
            this.button24.TabIndex = 37;
            this.button24.Text = "畫";
            this.button24.UseVisualStyleBackColor = true;
            this.button24.Click += new System.EventHandler(this.button24_Click);
            // 
            // button28
            // 
            this.button28.Location = new System.Drawing.Point(665, 582);
            this.button28.Name = "button28";
            this.button28.Size = new System.Drawing.Size(32, 53);
            this.button28.TabIndex = 38;
            this.button28.Text = "畫";
            this.button28.UseVisualStyleBackColor = true;
            this.button28.Click += new System.EventHandler(this.button28_Click);
            // 
            // button29
            // 
            this.button29.Location = new System.Drawing.Point(722, 582);
            this.button29.Name = "button29";
            this.button29.Size = new System.Drawing.Size(32, 53);
            this.button29.TabIndex = 39;
            this.button29.Text = "畫一圓";
            this.button29.UseVisualStyleBackColor = true;
            this.button29.Click += new System.EventHandler(this.button29_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1248, 647);
            this.Controls.Add(this.button29);
            this.Controls.Add(this.button28);
            this.Controls.Add(this.button24);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox3);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.numericUpDown_linewidth2);
            this.Controls.Add(this.button22);
            this.Controls.Add(this.button21);
            this.Controls.Add(this.button20);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button23);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Draw";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_linewidth)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_linewidth2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Button button19;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.Button button26;
        private System.Windows.Forms.Button button27;
        private System.Windows.Forms.Button button25;
        private System.Windows.Forms.Button bt_color;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.ComboBox comboBox_dashtype;
        private System.Windows.Forms.ComboBox comboBox_jointype;
        private System.Windows.Forms.ComboBox comboBox_drawtype;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_h;
        private System.Windows.Forms.TextBox tb_w;
        private System.Windows.Forms.TextBox tb_y;
        private System.Windows.Forms.TextBox tb_x;
        private System.Windows.Forms.NumericUpDown numericUpDown_linewidth;
        private System.Windows.Forms.Button button23;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button20;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.Button button21;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.ComboBox comboBox3;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tb_radius;
        private System.Windows.Forms.TextBox tb_center_y;
        private System.Windows.Forms.TextBox tb_center_x;
        private System.Windows.Forms.NumericUpDown numericUpDown_linewidth2;
        private System.Windows.Forms.Button button22;
        private System.Windows.Forms.Button button24;
        private System.Windows.Forms.Button button28;
        private System.Windows.Forms.Button button29;
    }
}

