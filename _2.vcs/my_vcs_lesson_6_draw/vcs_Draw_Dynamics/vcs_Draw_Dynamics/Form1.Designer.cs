﻿namespace vcs_Draw_Dynamics
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.button2 = new System.Windows.Forms.Button();
            this.trackBar1 = new System.Windows.Forms.TrackBar();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.lb_shoot_count = new System.Windows.Forms.Label();
            this.button4 = new System.Windows.Forms.Button();
            this.lb_energy_ek = new System.Windows.Forms.Label();
            this.progressBar_total_energy = new System.Windows.Forms.ProgressBar();
            this.groupBox_bird = new System.Windows.Forms.GroupBox();
            this.rb4 = new System.Windows.Forms.RadioButton();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.lb_total_energy = new System.Windows.Forms.Label();
            this.pictureBox_bird = new System.Windows.Forms.PictureBox();
            this.progressBar_this_energy = new System.Windows.Forms.ProgressBar();
            this.lb_this_energy = new System.Windows.Forms.Label();
            this.lb_initial_speed = new System.Windows.Forms.Label();
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.lb_velocity = new System.Windows.Forms.Label();
            this.lb_energy_ep = new System.Windows.Forms.Label();
            this.lb_energy_es = new System.Windows.Forms.Label();
            this.lb_energy_et = new System.Windows.Forms.Label();
            this.lb_pig_mesg = new System.Windows.Forms.Label();
            this.timer_pig = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).BeginInit();
            this.groupBox_bird.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_bird)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(324, 218);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1023, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(65, 65);
            this.button1.TabIndex = 1;
            this.button1.Text = "發射";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1023, 343);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(301, 269);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(1104, 12);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(65, 65);
            this.button2.TabIndex = 3;
            this.button2.Text = "暫停";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // trackBar1
            // 
            this.trackBar1.LargeChange = 1;
            this.trackBar1.Location = new System.Drawing.Point(1023, 292);
            this.trackBar1.Minimum = 1;
            this.trackBar1.Name = "trackBar1";
            this.trackBar1.Size = new System.Drawing.Size(335, 45);
            this.trackBar1.TabIndex = 4;
            this.trackBar1.Value = 1;
            this.trackBar1.Scroll += new System.EventHandler(this.trackBar1_Scroll);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1262, 589);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(62, 23);
            this.bt_clear.TabIndex = 5;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(1185, 12);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(65, 65);
            this.button3.TabIndex = 6;
            this.button3.Text = "Info";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // lb_shoot_count
            // 
            this.lb_shoot_count.AutoSize = true;
            this.lb_shoot_count.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_shoot_count.Location = new System.Drawing.Point(501, 431);
            this.lb_shoot_count.Name = "lb_shoot_count";
            this.lb_shoot_count.Size = new System.Drawing.Size(72, 16);
            this.lb_shoot_count.TabIndex = 7;
            this.lb_shoot_count.Text = "發射次數";
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(1266, 12);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(65, 65);
            this.button4.TabIndex = 8;
            this.button4.Text = "重玩";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // lb_energy_ek
            // 
            this.lb_energy_ek.AutoSize = true;
            this.lb_energy_ek.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_energy_ek.Location = new System.Drawing.Point(501, 71);
            this.lb_energy_ek.Name = "lb_energy_ek";
            this.lb_energy_ek.Size = new System.Drawing.Size(40, 16);
            this.lb_energy_ek.TabIndex = 9;
            this.lb_energy_ek.Text = "動能";
            // 
            // progressBar_total_energy
            // 
            this.progressBar_total_energy.Location = new System.Drawing.Point(1023, 218);
            this.progressBar_total_energy.Name = "progressBar_total_energy";
            this.progressBar_total_energy.Size = new System.Drawing.Size(100, 23);
            this.progressBar_total_energy.TabIndex = 10;
            this.progressBar_total_energy.Value = 100;
            // 
            // groupBox_bird
            // 
            this.groupBox_bird.Controls.Add(this.rb4);
            this.groupBox_bird.Controls.Add(this.rb3);
            this.groupBox_bird.Controls.Add(this.rb2);
            this.groupBox_bird.Controls.Add(this.rb1);
            this.groupBox_bird.Location = new System.Drawing.Point(12, 262);
            this.groupBox_bird.Name = "groupBox_bird";
            this.groupBox_bird.Size = new System.Drawing.Size(372, 65);
            this.groupBox_bird.TabIndex = 11;
            this.groupBox_bird.TabStop = false;
            this.groupBox_bird.Text = "Select";
            // 
            // rb4
            // 
            this.rb4.AutoSize = true;
            this.rb4.Location = new System.Drawing.Point(292, 30);
            this.rb4.Name = "rb4";
            this.rb4.Size = new System.Drawing.Size(59, 16);
            this.rb4.TabIndex = 3;
            this.rb4.Text = "炸彈鳥";
            this.rb4.UseVisualStyleBackColor = true;
            this.rb4.CheckedChanged += new System.EventHandler(this.rb_bird_CheckedChanged);
            // 
            // rb3
            // 
            this.rb3.AutoSize = true;
            this.rb3.Location = new System.Drawing.Point(201, 30);
            this.rb3.Name = "rb3";
            this.rb3.Size = new System.Drawing.Size(47, 16);
            this.rb3.TabIndex = 2;
            this.rb3.Text = "藍鳥";
            this.rb3.UseVisualStyleBackColor = true;
            this.rb3.CheckedChanged += new System.EventHandler(this.rb_bird_CheckedChanged);
            // 
            // rb2
            // 
            this.rb2.AutoSize = true;
            this.rb2.Location = new System.Drawing.Point(110, 30);
            this.rb2.Name = "rb2";
            this.rb2.Size = new System.Drawing.Size(47, 16);
            this.rb2.TabIndex = 1;
            this.rb2.Text = "黃鳥";
            this.rb2.UseVisualStyleBackColor = true;
            this.rb2.CheckedChanged += new System.EventHandler(this.rb_bird_CheckedChanged);
            // 
            // rb1
            // 
            this.rb1.AutoSize = true;
            this.rb1.Checked = true;
            this.rb1.Location = new System.Drawing.Point(19, 30);
            this.rb1.Name = "rb1";
            this.rb1.Size = new System.Drawing.Size(47, 16);
            this.rb1.TabIndex = 0;
            this.rb1.TabStop = true;
            this.rb1.Text = "紅鳥";
            this.rb1.UseVisualStyleBackColor = true;
            this.rb1.CheckedChanged += new System.EventHandler(this.rb_bird_CheckedChanged);
            // 
            // lb_total_energy
            // 
            this.lb_total_energy.AutoSize = true;
            this.lb_total_energy.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_total_energy.Location = new System.Drawing.Point(501, 174);
            this.lb_total_energy.Name = "lb_total_energy";
            this.lb_total_energy.Size = new System.Drawing.Size(56, 16);
            this.lb_total_energy.TabIndex = 12;
            this.lb_total_energy.Text = "總能量";
            // 
            // pictureBox_bird
            // 
            this.pictureBox_bird.Location = new System.Drawing.Point(1184, 86);
            this.pictureBox_bird.Name = "pictureBox_bird";
            this.pictureBox_bird.Size = new System.Drawing.Size(128, 117);
            this.pictureBox_bird.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_bird.TabIndex = 14;
            this.pictureBox_bird.TabStop = false;
            // 
            // progressBar_this_energy
            // 
            this.progressBar_this_energy.Location = new System.Drawing.Point(1023, 247);
            this.progressBar_this_energy.Name = "progressBar_this_energy";
            this.progressBar_this_energy.Size = new System.Drawing.Size(100, 23);
            this.progressBar_this_energy.TabIndex = 15;
            this.progressBar_this_energy.Value = 100;
            // 
            // lb_this_energy
            // 
            this.lb_this_energy.AutoSize = true;
            this.lb_this_energy.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_this_energy.Location = new System.Drawing.Point(501, 141);
            this.lb_this_energy.Name = "lb_this_energy";
            this.lb_this_energy.Size = new System.Drawing.Size(72, 16);
            this.lb_this_energy.TabIndex = 16;
            this.lb_this_energy.Text = "預計能量";
            // 
            // lb_initial_speed
            // 
            this.lb_initial_speed.AutoSize = true;
            this.lb_initial_speed.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_initial_speed.Location = new System.Drawing.Point(501, 218);
            this.lb_initial_speed.Name = "lb_initial_speed";
            this.lb_initial_speed.Size = new System.Drawing.Size(56, 16);
            this.lb_initial_speed.TabIndex = 17;
            this.lb_initial_speed.Text = "初速度";
            // 
            // timer2
            // 
            this.timer2.Enabled = true;
            this.timer2.Interval = 800;
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(496, 361);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(320, 48);
            this.lb_main_mesg.TabIndex = 18;
            this.lb_main_mesg.Text = "lb_main_mesg";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // lb_velocity
            // 
            this.lb_velocity.AutoSize = true;
            this.lb_velocity.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_velocity.Location = new System.Drawing.Point(501, 103);
            this.lb_velocity.Name = "lb_velocity";
            this.lb_velocity.Size = new System.Drawing.Size(48, 16);
            this.lb_velocity.TabIndex = 19;
            this.lb_velocity.Text = "vx = ";
            // 
            // lb_energy_ep
            // 
            this.lb_energy_ep.AutoSize = true;
            this.lb_energy_ep.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_energy_ep.Location = new System.Drawing.Point(501, 35);
            this.lb_energy_ep.Name = "lb_energy_ep";
            this.lb_energy_ep.Size = new System.Drawing.Size(40, 16);
            this.lb_energy_ep.TabIndex = 20;
            this.lb_energy_ep.Text = "位能";
            // 
            // lb_energy_es
            // 
            this.lb_energy_es.AutoSize = true;
            this.lb_energy_es.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_energy_es.Location = new System.Drawing.Point(636, 35);
            this.lb_energy_es.Name = "lb_energy_es";
            this.lb_energy_es.Size = new System.Drawing.Size(72, 16);
            this.lb_energy_es.TabIndex = 21;
            this.lb_energy_es.Text = "彈性位能";
            // 
            // lb_energy_et
            // 
            this.lb_energy_et.AutoSize = true;
            this.lb_energy_et.Font = new System.Drawing.Font("標楷體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_energy_et.Location = new System.Drawing.Point(636, 71);
            this.lb_energy_et.Name = "lb_energy_et";
            this.lb_energy_et.Size = new System.Drawing.Size(56, 16);
            this.lb_energy_et.TabIndex = 22;
            this.lb_energy_et.Text = "總能量";
            // 
            // lb_pig_mesg
            // 
            this.lb_pig_mesg.AutoSize = true;
            this.lb_pig_mesg.BackColor = System.Drawing.Color.White;
            this.lb_pig_mesg.Font = new System.Drawing.Font("標楷體", 27.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_pig_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_pig_mesg.Location = new System.Drawing.Point(496, 304);
            this.lb_pig_mesg.Name = "lb_pig_mesg";
            this.lb_pig_mesg.Size = new System.Drawing.Size(237, 37);
            this.lb_pig_mesg.TabIndex = 23;
            this.lb_pig_mesg.Text = "lb_pig_mesg";
            // 
            // timer_pig
            // 
            this.timer_pig.Enabled = true;
            this.timer_pig.Interval = 1000;
            this.timer_pig.Tick += new System.EventHandler(this.timer_pig_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1336, 627);
            this.Controls.Add(this.lb_pig_mesg);
            this.Controls.Add(this.lb_energy_et);
            this.Controls.Add(this.lb_energy_es);
            this.Controls.Add(this.lb_energy_ep);
            this.Controls.Add(this.lb_velocity);
            this.Controls.Add(this.lb_main_mesg);
            this.Controls.Add(this.lb_initial_speed);
            this.Controls.Add(this.lb_this_energy);
            this.Controls.Add(this.progressBar_this_energy);
            this.Controls.Add(this.pictureBox_bird);
            this.Controls.Add(this.lb_total_energy);
            this.Controls.Add(this.groupBox_bird);
            this.Controls.Add(this.progressBar_total_energy);
            this.Controls.Add(this.lb_energy_ek);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.lb_shoot_count);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.trackBar1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).EndInit();
            this.groupBox_bird.ResumeLayout(false);
            this.groupBox_bird.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_bird)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TrackBar trackBar1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label lb_shoot_count;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label lb_energy_ek;
        private System.Windows.Forms.ProgressBar progressBar_total_energy;
        private System.Windows.Forms.GroupBox groupBox_bird;
        private System.Windows.Forms.RadioButton rb4;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.Label lb_total_energy;
        private System.Windows.Forms.PictureBox pictureBox_bird;
        private System.Windows.Forms.ProgressBar progressBar_this_energy;
        private System.Windows.Forms.Label lb_this_energy;
        private System.Windows.Forms.Label lb_initial_speed;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.Label lb_main_mesg;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Label lb_velocity;
        private System.Windows.Forms.Label lb_energy_ep;
        private System.Windows.Forms.Label lb_energy_es;
        private System.Windows.Forms.Label lb_energy_et;
        private System.Windows.Forms.Label lb_pig_mesg;
        private System.Windows.Forms.Timer timer_pig;
    }
}

