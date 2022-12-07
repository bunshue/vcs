namespace Bottom_Control
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
            this.components = new System.ComponentModel.Container();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button5 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.bt_generate = new System.Windows.Forms.Button();
            this.cb_random = new System.Windows.Forms.CheckBox();
            this.tb_contact_address = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.tb_data_read = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tb_data_to_write = new System.Windows.Forms.TextBox();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.tb_contact_point = new System.Windows.Forms.TextBox();
            this.tb_contact_address2 = new System.Windows.Forms.TextBox();
            this.tb_data = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.bt_read = new System.Windows.Forms.Button();
            this.bt_write = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_erase = new System.Windows.Forms.Button();
            this.daButton1 = new Bottom_Control.DAButton();
            this.plC_Open_Time1 = new Bottom_Control.设置控件.PLC_Open_Time();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_erase);
            this.groupBox1.Controls.Add(this.bt_write);
            this.groupBox1.Controls.Add(this.bt_read);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.tb_data);
            this.groupBox1.Controls.Add(this.tb_contact_address2);
            this.groupBox1.Controls.Add(this.tb_contact_point);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.lb_main_mesg1);
            this.groupBox1.Controls.Add(this.pictureBox1);
            this.groupBox1.Controls.Add(this.button5);
            this.groupBox1.Controls.Add(this.button4);
            this.groupBox1.Controls.Add(this.bt_generate);
            this.groupBox1.Controls.Add(this.cb_random);
            this.groupBox1.Controls.Add(this.tb_contact_address);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.tb_data_read);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.tb_data_to_write);
            this.groupBox1.Controls.Add(this.button3);
            this.groupBox1.Controls.Add(this.button2);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.daButton1);
            this.groupBox1.Location = new System.Drawing.Point(12, 21);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(838, 673);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "PC";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(24, 423);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(593, 232);
            this.pictureBox1.TabIndex = 14;
            this.pictureBox1.TabStop = false;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(569, 66);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(96, 42);
            this.button5.TabIndex = 13;
            this.button5.Text = "讀取 Y20";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(456, 66);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(96, 42);
            this.button4.TabIndex = 12;
            this.button4.Text = "Test";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // bt_generate
            // 
            this.bt_generate.Location = new System.Drawing.Point(554, 172);
            this.bt_generate.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.bt_generate.Name = "bt_generate";
            this.bt_generate.Size = new System.Drawing.Size(43, 43);
            this.bt_generate.TabIndex = 11;
            this.bt_generate.Text = "產生";
            this.bt_generate.UseVisualStyleBackColor = true;
            this.bt_generate.Click += new System.EventHandler(this.bt_generate_Click);
            // 
            // cb_random
            // 
            this.cb_random.AutoSize = true;
            this.cb_random.Location = new System.Drawing.Point(604, 185);
            this.cb_random.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.cb_random.Name = "cb_random";
            this.cb_random.Size = new System.Drawing.Size(48, 16);
            this.cb_random.TabIndex = 10;
            this.cb_random.Text = "亂數";
            this.cb_random.UseVisualStyleBackColor = true;
            // 
            // tb_contact_address
            // 
            this.tb_contact_address.Enabled = false;
            this.tb_contact_address.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_address.Location = new System.Drawing.Point(271, 142);
            this.tb_contact_address.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.tb_contact_address.Name = "tb_contact_address";
            this.tb_contact_address.Size = new System.Drawing.Size(275, 33);
            this.tb_contact_address.TabIndex = 9;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(121, 144);
            this.label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(115, 21);
            this.label3.TabIndex = 8;
            this.label3.Text = "讀寫之位址";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(121, 226);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(115, 21);
            this.label2.TabIndex = 7;
            this.label2.Text = "讀出之資料";
            // 
            // tb_data_read
            // 
            this.tb_data_read.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_data_read.Location = new System.Drawing.Point(271, 222);
            this.tb_data_read.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.tb_data_read.Name = "tb_data_read";
            this.tb_data_read.Size = new System.Drawing.Size(275, 33);
            this.tb_data_read.TabIndex = 6;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(121, 186);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(136, 21);
            this.label1.TabIndex = 5;
            this.label1.Text = "欲寫入之資料";
            // 
            // tb_data_to_write
            // 
            this.tb_data_to_write.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_data_to_write.Location = new System.Drawing.Point(271, 182);
            this.tb_data_to_write.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.tb_data_to_write.Name = "tb_data_to_write";
            this.tb_data_to_write.Size = new System.Drawing.Size(275, 33);
            this.tb_data_to_write.TabIndex = 4;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(349, 66);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(96, 42);
            this.button3.TabIndex = 3;
            this.button3.Text = "讀取 D8000";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(236, 66);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(96, 42);
            this.button2.TabIndex = 2;
            this.button2.Text = "寫入 D8000";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(123, 66);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(96, 42);
            this.button1.TabIndex = 1;
            this.button1.Text = "讀取 D2000";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(856, 37);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(352, 567);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(121, 25);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(78, 24);
            this.lb_main_mesg1.TabIndex = 135;
            this.lb_main_mesg1.Text = "mesg1";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(30, 301);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(52, 21);
            this.label4.TabIndex = 136;
            this.label4.Text = "觸點";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(30, 344);
            this.label5.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(52, 21);
            this.label5.TabIndex = 137;
            this.label5.Text = "位址";
            // 
            // tb_contact_point
            // 
            this.tb_contact_point.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_point.Location = new System.Drawing.Point(86, 297);
            this.tb_contact_point.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_point.Name = "tb_contact_point";
            this.tb_contact_point.Size = new System.Drawing.Size(198, 33);
            this.tb_contact_point.TabIndex = 138;
            this.tb_contact_point.Text = "D";
            // 
            // tb_contact_address2
            // 
            this.tb_contact_address2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_contact_address2.Location = new System.Drawing.Point(86, 339);
            this.tb_contact_address2.Margin = new System.Windows.Forms.Padding(2);
            this.tb_contact_address2.Name = "tb_contact_address2";
            this.tb_contact_address2.Size = new System.Drawing.Size(198, 33);
            this.tb_contact_address2.TabIndex = 139;
            this.tb_contact_address2.Text = "2000";
            // 
            // tb_data
            // 
            this.tb_data.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_data.Location = new System.Drawing.Point(86, 380);
            this.tb_data.Margin = new System.Windows.Forms.Padding(2);
            this.tb_data.Name = "tb_data";
            this.tb_data.Size = new System.Drawing.Size(198, 33);
            this.tb_data.TabIndex = 140;
            this.tb_data.Text = "0123456789";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(30, 383);
            this.label6.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(52, 21);
            this.label6.TabIndex = 141;
            this.label6.Text = "資料";
            // 
            // bt_read
            // 
            this.bt_read.Location = new System.Drawing.Point(320, 297);
            this.bt_read.Margin = new System.Windows.Forms.Padding(2);
            this.bt_read.Name = "bt_read";
            this.bt_read.Size = new System.Drawing.Size(50, 50);
            this.bt_read.TabIndex = 142;
            this.bt_read.Text = "讀取";
            this.bt_read.UseVisualStyleBackColor = true;
            this.bt_read.Click += new System.EventHandler(this.bt_read_Click);
            // 
            // bt_write
            // 
            this.bt_write.Location = new System.Drawing.Point(320, 363);
            this.bt_write.Margin = new System.Windows.Forms.Padding(2);
            this.bt_write.Name = "bt_write";
            this.bt_write.Size = new System.Drawing.Size(50, 50);
            this.bt_write.TabIndex = 143;
            this.bt_write.Text = "寫入";
            this.bt_write.UseVisualStyleBackColor = true;
            this.bt_write.Click += new System.EventHandler(this.bt_write_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1158, 576);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(50, 28);
            this.bt_clear.TabIndex = 136;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_erase
            // 
            this.bt_erase.Location = new System.Drawing.Point(283, 380);
            this.bt_erase.Margin = new System.Windows.Forms.Padding(2);
            this.bt_erase.Name = "bt_erase";
            this.bt_erase.Size = new System.Drawing.Size(33, 33);
            this.bt_erase.TabIndex = 144;
            this.bt_erase.Text = "X";
            this.bt_erase.UseVisualStyleBackColor = true;
            this.bt_erase.Click += new System.EventHandler(this.bt_erase_Click);
            // 
            // daButton1
            // 
            this.daButton1.BackColor = System.Drawing.Color.Transparent;
            this.daButton1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daButton1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daButton1.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.daButton1.DownBack = null;
            this.daButton1.Location = new System.Drawing.Point(24, 25);
            this.daButton1.MouseBack = null;
            this.daButton1.Name = "daButton1";
            this.daButton1.NormlBack = null;
            this.daButton1.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daButton1.PLC_Address = "20";
            this.daButton1.PLC_Contact = "Y";
            this.daButton1.PLC_Enable = true;
            this.daButton1.Size = new System.Drawing.Size(83, 77);
            this.daButton1.TabIndex = 0;
            this.daButton1.Text = "連接PLC";
            this.daButton1.UseVisualStyleBackColor = false;
            // 
            // plC_Open_Time1
            // 
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
            this.plC_Open_Time1.ModBusIP = "192.168.3.20";
            this.plC_Open_Time1.siemensPLCS = HslCommunication.Profinet.SiemensPLCS.S200Smart;
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1220, 706);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private 设置控件.PLC_Open_Time plC_Open_Time1;
        private DAButton daButton1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox tb_contact_address;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tb_data_read;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb_data_to_write;
        private System.Windows.Forms.Button bt_generate;
        private System.Windows.Forms.CheckBox cb_random;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Button bt_write;
        private System.Windows.Forms.Button bt_read;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox tb_data;
        private System.Windows.Forms.TextBox tb_contact_address2;
        private System.Windows.Forms.TextBox tb_contact_point;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_erase;
    }
}