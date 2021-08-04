namespace vcs_Draw_Dynamics3
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
            this.button1 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.trackBar1 = new System.Windows.Forms.TrackBar();
            this.button2 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.groupBox_bird = new System.Windows.Forms.GroupBox();
            this.rb4 = new System.Windows.Forms.RadioButton();
            this.rb3 = new System.Windows.Forms.RadioButton();
            this.rb2 = new System.Windows.Forms.RadioButton();
            this.rb1 = new System.Windows.Forms.RadioButton();
            this.pictureBox_bird = new System.Windows.Forms.PictureBox();
            this.lb_interval = new System.Windows.Forms.Label();
            this.button4 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).BeginInit();
            this.groupBox_bird.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_bird)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(817, 14);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "自由落體";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.Location = new System.Drawing.Point(12, 14);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(250, 500);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(817, 262);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(374, 376);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // trackBar1
            // 
            this.trackBar1.LargeChange = 1;
            this.trackBar1.Location = new System.Drawing.Point(817, 153);
            this.trackBar1.Minimum = 1;
            this.trackBar1.Name = "trackBar1";
            this.trackBar1.Size = new System.Drawing.Size(236, 45);
            this.trackBar1.TabIndex = 3;
            this.trackBar1.Value = 2;
            this.trackBar1.Scroll += new System.EventHandler(this.trackBar1_Scroll);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(1002, 14);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 4;
            this.button2.Text = "Reset";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(880, 564);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(67, 36);
            this.bt_clear.TabIndex = 56;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(1093, 14);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 57;
            this.button3.Text = "Info";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // groupBox_bird
            // 
            this.groupBox_bird.Controls.Add(this.rb4);
            this.groupBox_bird.Controls.Add(this.rb3);
            this.groupBox_bird.Controls.Add(this.rb2);
            this.groupBox_bird.Controls.Add(this.rb1);
            this.groupBox_bird.Location = new System.Drawing.Point(817, 55);
            this.groupBox_bird.Name = "groupBox_bird";
            this.groupBox_bird.Size = new System.Drawing.Size(372, 65);
            this.groupBox_bird.TabIndex = 58;
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
            // pictureBox_bird
            // 
            this.pictureBox_bird.Location = new System.Drawing.Point(1063, 135);
            this.pictureBox_bird.Name = "pictureBox_bird";
            this.pictureBox_bird.Size = new System.Drawing.Size(128, 117);
            this.pictureBox_bird.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_bird.TabIndex = 59;
            this.pictureBox_bird.TabStop = false;
            // 
            // lb_interval
            // 
            this.lb_interval.AutoSize = true;
            this.lb_interval.Location = new System.Drawing.Point(817, 205);
            this.lb_interval.Name = "lb_interval";
            this.lb_interval.Size = new System.Drawing.Size(29, 12);
            this.lb_interval.TabIndex = 60;
            this.lb_interval.Text = "間隔";
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(909, 14);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 61;
            this.button4.Text = "橫拋";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1203, 599);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.lb_interval);
            this.Controls.Add(this.pictureBox_bird);
            this.Controls.Add(this.groupBox_bird);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.trackBar1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "自由落體 ( Freely Falling Body )";
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

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.TrackBar trackBar1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.GroupBox groupBox_bird;
        private System.Windows.Forms.RadioButton rb4;
        private System.Windows.Forms.RadioButton rb3;
        private System.Windows.Forms.RadioButton rb2;
        private System.Windows.Forms.RadioButton rb1;
        private System.Windows.Forms.PictureBox pictureBox_bird;
        private System.Windows.Forms.Label lb_interval;
        private System.Windows.Forms.Button button4;
    }
}

