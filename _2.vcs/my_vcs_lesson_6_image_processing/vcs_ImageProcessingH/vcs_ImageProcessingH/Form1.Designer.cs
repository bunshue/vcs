namespace vcs_ImageProcessingH
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
            this.pictureBox0 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.scrBright = new System.Windows.Forms.HScrollBar();
            this.lb_bright = new System.Windows.Forms.Label();
            this.scrBlue = new System.Windows.Forms.HScrollBar();
            this.lb_blue = new System.Windows.Forms.Label();
            this.scrGreen = new System.Windows.Forms.HScrollBar();
            this.lb_green = new System.Windows.Forms.Label();
            this.scrRed = new System.Windows.Forms.HScrollBar();
            this.picColor = new System.Windows.Forms.PictureBox();
            this.lb_red = new System.Windows.Forms.Label();
            this.picToned = new System.Windows.Forms.PictureBox();
            this.picOriginal = new System.Windows.Forms.PictureBox();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.trackBar_gamma1 = new System.Windows.Forms.TrackBar();
            this.trackBar_gamma2 = new System.Windows.Forms.TrackBar();
            this.trackBar_brightness = new System.Windows.Forms.TrackBar();
            this.trackBar_threshold = new System.Windows.Forms.TrackBar();
            this.trackBar_binary = new System.Windows.Forms.TrackBar();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label0 = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.bt_auto = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gamma1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gamma2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_brightness)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_threshold)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_binary)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(118, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox0
            // 
            this.pictureBox0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox0.Location = new System.Drawing.Point(12, 12);
            this.pictureBox0.Name = "pictureBox0";
            this.pictureBox0.Size = new System.Drawing.Size(100, 100);
            this.pictureBox0.TabIndex = 3;
            this.pictureBox0.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(224, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 4;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox3
            // 
            this.pictureBox3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3.Location = new System.Drawing.Point(330, 12);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3.TabIndex = 5;
            this.pictureBox3.TabStop = false;
            // 
            // pictureBox4
            // 
            this.pictureBox4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox4.Location = new System.Drawing.Point(436, 12);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 100);
            this.pictureBox4.TabIndex = 6;
            this.pictureBox4.TabStop = false;
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.scrBright);
            this.groupBox1.Controls.Add(this.lb_bright);
            this.groupBox1.Controls.Add(this.scrBlue);
            this.groupBox1.Controls.Add(this.lb_blue);
            this.groupBox1.Controls.Add(this.scrGreen);
            this.groupBox1.Controls.Add(this.lb_green);
            this.groupBox1.Controls.Add(this.scrRed);
            this.groupBox1.Controls.Add(this.picColor);
            this.groupBox1.Controls.Add(this.lb_red);
            this.groupBox1.Controls.Add(this.picToned);
            this.groupBox1.Controls.Add(this.picOriginal);
            this.groupBox1.Location = new System.Drawing.Point(12, 118);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(644, 512);
            this.groupBox1.TabIndex = 21;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "改變色調";
            // 
            // scrBright
            // 
            this.scrBright.Location = new System.Drawing.Point(62, 81);
            this.scrBright.Maximum = 264;
            this.scrBright.Name = "scrBright";
            this.scrBright.Size = new System.Drawing.Size(258, 14);
            this.scrBright.TabIndex = 24;
            // 
            // lb_bright
            // 
            this.lb_bright.AutoSize = true;
            this.lb_bright.Location = new System.Drawing.Point(20, 81);
            this.lb_bright.Name = "lb_bright";
            this.lb_bright.Size = new System.Drawing.Size(38, 12);
            this.lb_bright.TabIndex = 23;
            this.lb_bright.Text = "Bright:";
            // 
            // scrBlue
            // 
            this.scrBlue.Location = new System.Drawing.Point(62, 65);
            this.scrBlue.Maximum = 264;
            this.scrBlue.Name = "scrBlue";
            this.scrBlue.Size = new System.Drawing.Size(258, 14);
            this.scrBlue.TabIndex = 22;
            // 
            // lb_blue
            // 
            this.lb_blue.AutoSize = true;
            this.lb_blue.Location = new System.Drawing.Point(20, 65);
            this.lb_blue.Name = "lb_blue";
            this.lb_blue.Size = new System.Drawing.Size(30, 12);
            this.lb_blue.TabIndex = 21;
            this.lb_blue.Text = "Blue:";
            // 
            // scrGreen
            // 
            this.scrGreen.Location = new System.Drawing.Point(62, 48);
            this.scrGreen.Maximum = 264;
            this.scrGreen.Name = "scrGreen";
            this.scrGreen.Size = new System.Drawing.Size(258, 14);
            this.scrGreen.TabIndex = 20;
            // 
            // lb_green
            // 
            this.lb_green.AutoSize = true;
            this.lb_green.Location = new System.Drawing.Point(20, 48);
            this.lb_green.Name = "lb_green";
            this.lb_green.Size = new System.Drawing.Size(36, 12);
            this.lb_green.TabIndex = 19;
            this.lb_green.Text = "Green:";
            // 
            // scrRed
            // 
            this.scrRed.Location = new System.Drawing.Point(62, 30);
            this.scrRed.Maximum = 264;
            this.scrRed.Name = "scrRed";
            this.scrRed.Size = new System.Drawing.Size(258, 14);
            this.scrRed.TabIndex = 18;
            // 
            // picColor
            // 
            this.picColor.BackColor = System.Drawing.Color.LightBlue;
            this.picColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.picColor.Location = new System.Drawing.Point(326, 30);
            this.picColor.Name = "picColor";
            this.picColor.Size = new System.Drawing.Size(68, 63);
            this.picColor.TabIndex = 17;
            this.picColor.TabStop = false;
            // 
            // lb_red
            // 
            this.lb_red.AutoSize = true;
            this.lb_red.Location = new System.Drawing.Point(20, 30);
            this.lb_red.Name = "lb_red";
            this.lb_red.Size = new System.Drawing.Size(27, 12);
            this.lb_red.TabIndex = 16;
            this.lb_red.Text = "Red:";
            // 
            // picToned
            // 
            this.picToned.Location = new System.Drawing.Point(326, 97);
            this.picToned.Name = "picToned";
            this.picToned.Size = new System.Drawing.Size(300, 400);
            this.picToned.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picToned.TabIndex = 15;
            this.picToned.TabStop = false;
            // 
            // picOriginal
            // 
            this.picOriginal.Image = ((System.Drawing.Image)(resources.GetObject("picOriginal.Image")));
            this.picOriginal.Location = new System.Drawing.Point(20, 97);
            this.picOriginal.Name = "picOriginal";
            this.picOriginal.Size = new System.Drawing.Size(305, 400);
            this.picOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picOriginal.TabIndex = 14;
            this.picOriginal.TabStop = false;
            // 
            // pictureBox5
            // 
            this.pictureBox5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox5.Location = new System.Drawing.Point(544, 12);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(100, 100);
            this.pictureBox5.TabIndex = 22;
            this.pictureBox5.TabStop = false;
            // 
            // trackBar_gamma1
            // 
            this.trackBar_gamma1.Location = new System.Drawing.Point(666, 152);
            this.trackBar_gamma1.Maximum = 25;
            this.trackBar_gamma1.Name = "trackBar_gamma1";
            this.trackBar_gamma1.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.trackBar_gamma1.Size = new System.Drawing.Size(300, 45);
            this.trackBar_gamma1.TabIndex = 24;
            // 
            // trackBar_gamma2
            // 
            this.trackBar_gamma2.Location = new System.Drawing.Point(666, 193);
            this.trackBar_gamma2.Maximum = 25;
            this.trackBar_gamma2.Name = "trackBar_gamma2";
            this.trackBar_gamma2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.trackBar_gamma2.Size = new System.Drawing.Size(300, 45);
            this.trackBar_gamma2.TabIndex = 25;
            // 
            // trackBar_brightness
            // 
            this.trackBar_brightness.Location = new System.Drawing.Point(666, 233);
            this.trackBar_brightness.Maximum = 25;
            this.trackBar_brightness.Name = "trackBar_brightness";
            this.trackBar_brightness.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.trackBar_brightness.Size = new System.Drawing.Size(300, 45);
            this.trackBar_brightness.TabIndex = 26;
            // 
            // trackBar_threshold
            // 
            this.trackBar_threshold.Location = new System.Drawing.Point(666, 273);
            this.trackBar_threshold.Maximum = 100;
            this.trackBar_threshold.Name = "trackBar_threshold";
            this.trackBar_threshold.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.trackBar_threshold.Size = new System.Drawing.Size(300, 45);
            this.trackBar_threshold.TabIndex = 27;
            // 
            // trackBar_binary
            // 
            this.trackBar_binary.Location = new System.Drawing.Point(666, 314);
            this.trackBar_binary.Maximum = 255;
            this.trackBar_binary.Name = "trackBar_binary";
            this.trackBar_binary.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.trackBar_binary.Size = new System.Drawing.Size(300, 45);
            this.trackBar_binary.TabIndex = 28;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(650, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 29;
            this.richTextBox1.Text = "";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(756, 33);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 21);
            this.label1.TabIndex = 30;
            this.label1.Text = "label1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(756, 54);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 21);
            this.label2.TabIndex = 31;
            this.label2.Text = "label2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(756, 75);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(58, 21);
            this.label3.TabIndex = 32;
            this.label3.Text = "label3";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(756, 96);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(58, 21);
            this.label4.TabIndex = 33;
            this.label4.Text = "label4";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(756, 117);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(58, 21);
            this.label5.TabIndex = 34;
            this.label5.Text = "label5";
            // 
            // label0
            // 
            this.label0.AutoSize = true;
            this.label0.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label0.Location = new System.Drawing.Point(756, 12);
            this.label0.Name = "label0";
            this.label0.Size = new System.Drawing.Size(58, 21);
            this.label0.TabIndex = 35;
            this.label0.Text = "label0";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(666, 70);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 36;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // bt_auto
            // 
            this.bt_auto.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_auto.Location = new System.Drawing.Point(820, 12);
            this.bt_auto.Name = "bt_auto";
            this.bt_auto.Size = new System.Drawing.Size(60, 32);
            this.bt_auto.TabIndex = 37;
            this.bt_auto.Text = "自動";
            this.bt_auto.UseVisualStyleBackColor = true;
            this.bt_auto.Click += new System.EventHandler(this.bt_auto_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(984, 661);
            this.Controls.Add(this.bt_auto);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.label0);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.trackBar_binary);
            this.Controls.Add(this.trackBar_threshold);
            this.Controls.Add(this.trackBar_brightness);
            this.Controls.Add(this.trackBar_gamma2);
            this.Controls.Add(this.trackBar_gamma1);
            this.Controls.Add(this.pictureBox5);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox0);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gamma1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_gamma2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_brightness)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_threshold)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_binary)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox0;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.HScrollBar scrBright;
        private System.Windows.Forms.Label lb_bright;
        private System.Windows.Forms.HScrollBar scrBlue;
        private System.Windows.Forms.Label lb_blue;
        private System.Windows.Forms.HScrollBar scrGreen;
        private System.Windows.Forms.Label lb_green;
        private System.Windows.Forms.HScrollBar scrRed;
        private System.Windows.Forms.PictureBox picColor;
        private System.Windows.Forms.Label lb_red;
        private System.Windows.Forms.PictureBox picToned;
        private System.Windows.Forms.PictureBox picOriginal;
        private System.Windows.Forms.PictureBox pictureBox5;
        private System.Windows.Forms.TrackBar trackBar_gamma1;
        private System.Windows.Forms.TrackBar trackBar_gamma2;
        private System.Windows.Forms.TrackBar trackBar_brightness;
        private System.Windows.Forms.TrackBar trackBar_threshold;
        private System.Windows.Forms.TrackBar trackBar_binary;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label0;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button bt_auto;
    }
}

