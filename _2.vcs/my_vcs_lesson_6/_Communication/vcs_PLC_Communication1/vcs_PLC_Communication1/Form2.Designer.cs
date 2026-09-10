namespace vcs_PLC_Communication1
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.rb_low = new System.Windows.Forms.RadioButton();
            this.rb_high = new System.Windows.Forms.RadioButton();
            this.label7 = new System.Windows.Forms.Label();
            this.bt_erase_m = new System.Windows.Forms.Button();
            this.label8 = new System.Windows.Forms.Label();
            this.bt_write_m = new System.Windows.Forms.Button();
            this.tb_contact_point_m = new System.Windows.Forms.TextBox();
            this.bt_read_m = new System.Windows.Forms.Button();
            this.tb_contact_address_m = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.tb_data_m = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.cb_random = new System.Windows.Forms.CheckBox();
            this.label4 = new System.Windows.Forms.Label();
            this.bt_erase_d = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.bt_write_d = new System.Windows.Forms.Button();
            this.tb_contact_point_d = new System.Windows.Forms.TextBox();
            this.bt_read_d = new System.Windows.Forms.Button();
            this.tb_contact_address_d = new System.Windows.Forms.TextBox();
            this.bt_generate = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.tb_data_d = new System.Windows.Forms.TextBox();
            this.plC_Open_Time1 = new vcs_PLC_Communication1.SetupControls.PLC_Open_Time();
            this.groupBox1.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.groupBox6);
            this.groupBox1.Controls.Add(this.groupBox3);
            this.groupBox1.Controls.Add(this.groupBox2);
            this.groupBox1.Location = new System.Drawing.Point(21, 22);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(950, 180);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.button3);
            this.groupBox6.Controls.Add(this.button4);
            this.groupBox6.Controls.Add(this.button2);
            this.groupBox6.Controls.Add(this.button1);
            this.groupBox6.Controls.Add(this.button8);
            this.groupBox6.Controls.Add(this.button5);
            this.groupBox6.Location = new System.Drawing.Point(730, 10);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(210, 160);
            this.groupBox6.TabIndex = 151;
            this.groupBox6.TabStop = false;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(10, 65);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(90, 40);
            this.button3.TabIndex = 152;
            this.button3.Text = "寫D8010";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(110, 20);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(90, 40);
            this.button2.TabIndex = 151;
            this.button2.Text = "Print D2000";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(10, 20);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(90, 40);
            this.button1.TabIndex = 150;
            this.button1.Text = "Erase";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(110, 110);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(90, 40);
            this.button8.TabIndex = 149;
            this.button8.Text = "Rest M1200X";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(110, 65);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(90, 40);
            this.button4.TabIndex = 12;
            this.button4.Text = "測試m_status";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(10, 110);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(90, 40);
            this.button5.TabIndex = 13;
            this.button5.Text = "Get M1X00X status";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.groupBox4);
            this.groupBox3.Controls.Add(this.label7);
            this.groupBox3.Controls.Add(this.bt_erase_m);
            this.groupBox3.Controls.Add(this.label8);
            this.groupBox3.Controls.Add(this.bt_write_m);
            this.groupBox3.Controls.Add(this.tb_contact_point_m);
            this.groupBox3.Controls.Add(this.bt_read_m);
            this.groupBox3.Controls.Add(this.tb_contact_address_m);
            this.groupBox3.Controls.Add(this.label9);
            this.groupBox3.Controls.Add(this.tb_data_m);
            this.groupBox3.Location = new System.Drawing.Point(370, 10);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(350, 160);
            this.groupBox3.TabIndex = 146;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "讀寫 M bit";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.rb_low);
            this.groupBox4.Controls.Add(this.rb_high);
            this.groupBox4.Location = new System.Drawing.Point(256, 79);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(81, 74);
            this.groupBox4.TabIndex = 145;
            this.groupBox4.TabStop = false;
            // 
            // rb_low
            // 
            this.rb_low.AutoSize = true;
            this.rb_low.Location = new System.Drawing.Point(17, 43);
            this.rb_low.Name = "rb_low";
            this.rb_low.Size = new System.Drawing.Size(44, 16);
            this.rb_low.TabIndex = 1;
            this.rb_low.Text = "Low";
            this.rb_low.UseVisualStyleBackColor = true;
            // 
            // rb_high
            // 
            this.rb_high.AutoSize = true;
            this.rb_high.Checked = true;
            this.rb_high.Location = new System.Drawing.Point(17, 21);
            this.rb_high.Name = "rb_high";
            this.rb_high.Size = new System.Drawing.Size(46, 16);
            this.rb_high.TabIndex = 0;
            this.rb_high.TabStop = true;
            this.rb_high.Text = "High";
            this.rb_high.UseVisualStyleBackColor = true;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(10, 30);
            this.label7.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(52, 21);
            this.label7.TabIndex = 136;
            this.label7.Text = "觸點";
            // 
            // bt_erase_m
            // 
            this.bt_erase_m.Location = new System.Drawing.Point(218, 109);
            this.bt_erase_m.Margin = new System.Windows.Forms.Padding(2);
            this.bt_erase_m.Name = "bt_erase_m";
            this.bt_erase_m.Size = new System.Drawing.Size(33, 33);
            this.bt_erase_m.TabIndex = 144;
            this.bt_erase_m.Text = "X";
            this.bt_erase_m.UseVisualStyleBackColor = true;
            this.bt_erase_m.Click += new System.EventHandler(this.bt_erase_m_Click);
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label8.Location = new System.Drawing.Point(10, 73);
            this.label8.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(52, 21);
            this.label8.TabIndex = 137;
            this.label8.Text = "位址";
            // 
            // bt_write_m
            // 
            this.bt_write_m.Location = new System.Drawing.Point(287, 26);
            this.bt_write_m.Margin = new System.Windows.Forms.Padding(2);
            this.bt_write_m.Name = "bt_write_m";
            this.bt_write_m.Size = new System.Drawing.Size(50, 50);
            this.bt_write_m.TabIndex = 143;
            this.bt_write_m.Text = "寫入";
            this.bt_write_m.UseVisualStyleBackColor = true;
            this.bt_write_m.Click += new System.EventHandler(this.bt_write_m_Click);
            // 
            // tb_contact_point_m
            // 
            this.tb_contact_point_m.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_point_m.Location = new System.Drawing.Point(66, 26);
            this.tb_contact_point_m.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_point_m.Name = "tb_contact_point_m";
            this.tb_contact_point_m.Size = new System.Drawing.Size(150, 33);
            this.tb_contact_point_m.TabIndex = 138;
            this.tb_contact_point_m.Text = "M";
            // 
            // bt_read_m
            // 
            this.bt_read_m.Location = new System.Drawing.Point(233, 26);
            this.bt_read_m.Margin = new System.Windows.Forms.Padding(2);
            this.bt_read_m.Name = "bt_read_m";
            this.bt_read_m.Size = new System.Drawing.Size(50, 50);
            this.bt_read_m.TabIndex = 142;
            this.bt_read_m.Text = "讀取";
            this.bt_read_m.UseVisualStyleBackColor = true;
            this.bt_read_m.Click += new System.EventHandler(this.bt_read_m_Click);
            // 
            // tb_contact_address_m
            // 
            this.tb_contact_address_m.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_address_m.Location = new System.Drawing.Point(66, 68);
            this.tb_contact_address_m.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_address_m.Name = "tb_contact_address_m";
            this.tb_contact_address_m.Size = new System.Drawing.Size(150, 33);
            this.tb_contact_address_m.TabIndex = 139;
            this.tb_contact_address_m.Text = "10000";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.Location = new System.Drawing.Point(10, 112);
            this.label9.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(52, 21);
            this.label9.TabIndex = 141;
            this.label9.Text = "資料";
            // 
            // tb_data_m
            // 
            this.tb_data_m.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_data_m.Location = new System.Drawing.Point(66, 109);
            this.tb_data_m.Margin = new System.Windows.Forms.Padding(2);
            this.tb_data_m.Name = "tb_data_m";
            this.tb_data_m.Size = new System.Drawing.Size(150, 33);
            this.tb_data_m.TabIndex = 140;
            this.tb_data_m.Text = "Low";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.cb_random);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.bt_erase_d);
            this.groupBox2.Controls.Add(this.label5);
            this.groupBox2.Controls.Add(this.bt_write_d);
            this.groupBox2.Controls.Add(this.tb_contact_point_d);
            this.groupBox2.Controls.Add(this.bt_read_d);
            this.groupBox2.Controls.Add(this.tb_contact_address_d);
            this.groupBox2.Controls.Add(this.bt_generate);
            this.groupBox2.Controls.Add(this.label6);
            this.groupBox2.Controls.Add(this.tb_data_d);
            this.groupBox2.Location = new System.Drawing.Point(10, 10);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(350, 160);
            this.groupBox2.TabIndex = 145;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "讀寫 D register";
            // 
            // cb_random
            // 
            this.cb_random.AutoSize = true;
            this.cb_random.Location = new System.Drawing.Point(250, 138);
            this.cb_random.Margin = new System.Windows.Forms.Padding(2);
            this.cb_random.Name = "cb_random";
            this.cb_random.Size = new System.Drawing.Size(48, 16);
            this.cb_random.TabIndex = 10;
            this.cb_random.Text = "亂數";
            this.cb_random.UseVisualStyleBackColor = true;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(6, 30);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(52, 21);
            this.label4.TabIndex = 136;
            this.label4.Text = "觸點";
            // 
            // bt_erase_d
            // 
            this.bt_erase_d.Location = new System.Drawing.Point(214, 109);
            this.bt_erase_d.Margin = new System.Windows.Forms.Padding(2);
            this.bt_erase_d.Name = "bt_erase_d";
            this.bt_erase_d.Size = new System.Drawing.Size(33, 33);
            this.bt_erase_d.TabIndex = 144;
            this.bt_erase_d.Text = "X";
            this.bt_erase_d.UseVisualStyleBackColor = true;
            this.bt_erase_d.Click += new System.EventHandler(this.bt_erase_d_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(6, 73);
            this.label5.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(52, 21);
            this.label5.TabIndex = 137;
            this.label5.Text = "位址";
            // 
            // bt_write_d
            // 
            this.bt_write_d.Location = new System.Drawing.Point(294, 93);
            this.bt_write_d.Margin = new System.Windows.Forms.Padding(2);
            this.bt_write_d.Name = "bt_write_d";
            this.bt_write_d.Size = new System.Drawing.Size(50, 50);
            this.bt_write_d.TabIndex = 143;
            this.bt_write_d.Text = "寫入";
            this.bt_write_d.UseVisualStyleBackColor = true;
            this.bt_write_d.Click += new System.EventHandler(this.bt_write_d_Click);
            // 
            // tb_contact_point_d
            // 
            this.tb_contact_point_d.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_point_d.Location = new System.Drawing.Point(62, 26);
            this.tb_contact_point_d.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_point_d.Name = "tb_contact_point_d";
            this.tb_contact_point_d.Size = new System.Drawing.Size(150, 33);
            this.tb_contact_point_d.TabIndex = 138;
            this.tb_contact_point_d.Text = "D";
            // 
            // bt_read_d
            // 
            this.bt_read_d.Location = new System.Drawing.Point(294, 26);
            this.bt_read_d.Margin = new System.Windows.Forms.Padding(2);
            this.bt_read_d.Name = "bt_read_d";
            this.bt_read_d.Size = new System.Drawing.Size(50, 50);
            this.bt_read_d.TabIndex = 142;
            this.bt_read_d.Text = "讀取";
            this.bt_read_d.UseVisualStyleBackColor = true;
            this.bt_read_d.Click += new System.EventHandler(this.bt_read_d_Click);
            // 
            // tb_contact_address_d
            // 
            this.tb_contact_address_d.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_address_d.Location = new System.Drawing.Point(62, 68);
            this.tb_contact_address_d.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_address_d.Name = "tb_contact_address_d";
            this.tb_contact_address_d.Size = new System.Drawing.Size(150, 33);
            this.tb_contact_address_d.TabIndex = 139;
            this.tb_contact_address_d.Text = "2000";
            // 
            // bt_generate
            // 
            this.bt_generate.Location = new System.Drawing.Point(248, 89);
            this.bt_generate.Margin = new System.Windows.Forms.Padding(2);
            this.bt_generate.Name = "bt_generate";
            this.bt_generate.Size = new System.Drawing.Size(43, 43);
            this.bt_generate.TabIndex = 11;
            this.bt_generate.Text = "產生";
            this.bt_generate.UseVisualStyleBackColor = true;
            this.bt_generate.Click += new System.EventHandler(this.bt_generate_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(6, 112);
            this.label6.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(52, 21);
            this.label6.TabIndex = 141;
            this.label6.Text = "資料";
            // 
            // tb_data_d
            // 
            this.tb_data_d.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_data_d.Location = new System.Drawing.Point(62, 109);
            this.tb_data_d.Margin = new System.Windows.Forms.Padding(2);
            this.tb_data_d.Name = "tb_data_d";
            this.tb_data_d.Size = new System.Drawing.Size(150, 33);
            this.tb_data_d.TabIndex = 140;
            this.tb_data_d.Text = "0123456789";
            // 
            // plC_Open_Time1
            // 
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1468, 862);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form2";
            this.Text = "PC Console";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form2_FormClosing);
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form2_FormClosed);
            this.Load += new System.EventHandler(this.Form2_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox6.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private SetupControls.PLC_Open_Time plC_Open_Time1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_generate;
        private System.Windows.Forms.CheckBox cb_random;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_write_d;
        private System.Windows.Forms.Button bt_read_d;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox tb_data_d;
        private System.Windows.Forms.TextBox tb_contact_address_d;
        private System.Windows.Forms.TextBox tb_contact_point_d;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button bt_erase_d;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Button bt_erase_m;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button bt_write_m;
        private System.Windows.Forms.TextBox tb_contact_point_m;
        private System.Windows.Forms.Button bt_read_m;
        private System.Windows.Forms.TextBox tb_contact_address_m;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox tb_data_m;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.RadioButton rb_low;
        private System.Windows.Forms.RadioButton rb_high;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
    }
}