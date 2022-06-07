namespace vcs_FFMPEG
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
            this.bt_open_file = new System.Windows.Forms.Button();
            this.bt_save_file = new System.Windows.Forms.Button();
            this.bt_play_pause = new System.Windows.Forms.Button();
            this.bt_stop = new System.Windows.Forms.Button();
            this.lb_st = new System.Windows.Forms.Label();
            this.lb_sp = new System.Windows.Forms.Label();
            this.lb_total = new System.Windows.Forms.Label();
            this.lb_cut = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_ffmpeg1 = new System.Windows.Forms.Button();
            this.bt_ffmpeg2 = new System.Windows.Forms.Button();
            this.bt_ffmpeg0 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button14 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.tb_filename = new System.Windows.Forms.TextBox();
            this.lb_time = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.bt_plus = new System.Windows.Forms.Button();
            this.bt_minus = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 283);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(924, 206);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // bt_open_file
            // 
            this.bt_open_file.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_open_file.BackgroundImage")));
            this.bt_open_file.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_file.Location = new System.Drawing.Point(26, 204);
            this.bt_open_file.Name = "bt_open_file";
            this.bt_open_file.Size = new System.Drawing.Size(64, 64);
            this.bt_open_file.TabIndex = 45;
            this.bt_open_file.UseVisualStyleBackColor = true;
            this.bt_open_file.Click += new System.EventHandler(this.bt_open_file_Click);
            // 
            // bt_save_file
            // 
            this.bt_save_file.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_save_file.BackgroundImage")));
            this.bt_save_file.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_save_file.Location = new System.Drawing.Point(107, 204);
            this.bt_save_file.Name = "bt_save_file";
            this.bt_save_file.Size = new System.Drawing.Size(64, 64);
            this.bt_save_file.TabIndex = 46;
            this.bt_save_file.UseVisualStyleBackColor = true;
            this.bt_save_file.Click += new System.EventHandler(this.bt_save_file_Click);
            // 
            // bt_play_pause
            // 
            this.bt_play_pause.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_play_pause.BackgroundImage")));
            this.bt_play_pause.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_play_pause.Location = new System.Drawing.Point(192, 204);
            this.bt_play_pause.Name = "bt_play_pause";
            this.bt_play_pause.Size = new System.Drawing.Size(64, 64);
            this.bt_play_pause.TabIndex = 47;
            this.bt_play_pause.UseVisualStyleBackColor = true;
            this.bt_play_pause.Click += new System.EventHandler(this.bt_play_pause_Click);
            // 
            // bt_stop
            // 
            this.bt_stop.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_stop.BackgroundImage")));
            this.bt_stop.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_stop.Location = new System.Drawing.Point(360, 204);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(64, 64);
            this.bt_stop.TabIndex = 48;
            this.bt_stop.UseVisualStyleBackColor = true;
            this.bt_stop.Click += new System.EventHandler(this.bt_stop_Click);
            // 
            // lb_st
            // 
            this.lb_st.AutoSize = true;
            this.lb_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_st.Location = new System.Drawing.Point(711, 35);
            this.lb_st.Name = "lb_st";
            this.lb_st.Size = new System.Drawing.Size(58, 21);
            this.lb_st.TabIndex = 49;
            this.lb_st.Text = "label1";
            // 
            // lb_sp
            // 
            this.lb_sp.AutoSize = true;
            this.lb_sp.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_sp.Location = new System.Drawing.Point(711, 66);
            this.lb_sp.Name = "lb_sp";
            this.lb_sp.Size = new System.Drawing.Size(58, 21);
            this.lb_sp.TabIndex = 50;
            this.lb_sp.Text = "label2";
            // 
            // lb_total
            // 
            this.lb_total.AutoSize = true;
            this.lb_total.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_total.Location = new System.Drawing.Point(711, 6);
            this.lb_total.Name = "lb_total";
            this.lb_total.Size = new System.Drawing.Size(58, 21);
            this.lb_total.TabIndex = 51;
            this.lb_total.Text = "label1";
            // 
            // lb_cut
            // 
            this.lb_cut.AutoSize = true;
            this.lb_cut.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_cut.Location = new System.Drawing.Point(711, 99);
            this.lb_cut.Name = "lb_cut";
            this.lb_cut.Size = new System.Drawing.Size(58, 21);
            this.lb_cut.TabIndex = 52;
            this.lb_cut.Text = "label2";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(587, 448);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 53;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(6, 21);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(100, 40);
            this.button5.TabIndex = 54;
            this.button5.Text = "test 1";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(112, 21);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(100, 40);
            this.button6.TabIndex = 55;
            this.button6.Text = "test 2 影片轉mp3";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(218, 21);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(100, 40);
            this.button7.TabIndex = 56;
            this.button7.Text = "test 3";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(324, 21);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(100, 40);
            this.button8.TabIndex = 57;
            this.button8.Text = "test 4 視頻截圖";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_ffmpeg1);
            this.groupBox1.Controls.Add(this.bt_ffmpeg2);
            this.groupBox1.Controls.Add(this.bt_ffmpeg0);
            this.groupBox1.Location = new System.Drawing.Point(771, 495);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(165, 167);
            this.groupBox1.TabIndex = 58;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ffmpeg";
            // 
            // bt_ffmpeg1
            // 
            this.bt_ffmpeg1.Location = new System.Drawing.Point(17, 68);
            this.bt_ffmpeg1.Name = "bt_ffmpeg1";
            this.bt_ffmpeg1.Size = new System.Drawing.Size(128, 40);
            this.bt_ffmpeg1.TabIndex = 6;
            this.bt_ffmpeg1.Text = "獲取視頻時長";
            this.bt_ffmpeg1.UseVisualStyleBackColor = true;
            this.bt_ffmpeg1.Click += new System.EventHandler(this.bt_ffmpeg1_Click);
            // 
            // bt_ffmpeg2
            // 
            this.bt_ffmpeg2.Location = new System.Drawing.Point(17, 115);
            this.bt_ffmpeg2.Name = "bt_ffmpeg2";
            this.bt_ffmpeg2.Size = new System.Drawing.Size(128, 40);
            this.bt_ffmpeg2.TabIndex = 5;
            this.bt_ffmpeg2.Text = "獲取視頻第一秒圖片";
            this.bt_ffmpeg2.UseVisualStyleBackColor = true;
            this.bt_ffmpeg2.Click += new System.EventHandler(this.bt_ffmpeg2_Click);
            // 
            // bt_ffmpeg0
            // 
            this.bt_ffmpeg0.Location = new System.Drawing.Point(17, 21);
            this.bt_ffmpeg0.Name = "bt_ffmpeg0";
            this.bt_ffmpeg0.Size = new System.Drawing.Size(128, 40);
            this.bt_ffmpeg0.TabIndex = 4;
            this.bt_ffmpeg0.Text = "取得影片的寬高";
            this.bt_ffmpeg0.UseVisualStyleBackColor = true;
            this.bt_ffmpeg0.Click += new System.EventHandler(this.bt_ffmpeg0_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button14);
            this.groupBox2.Controls.Add(this.button13);
            this.groupBox2.Controls.Add(this.button12);
            this.groupBox2.Controls.Add(this.button11);
            this.groupBox2.Controls.Add(this.button10);
            this.groupBox2.Controls.Add(this.button9);
            this.groupBox2.Controls.Add(this.button5);
            this.groupBox2.Controls.Add(this.button6);
            this.groupBox2.Controls.Add(this.button8);
            this.groupBox2.Controls.Add(this.button7);
            this.groupBox2.Location = new System.Drawing.Point(12, 509);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(551, 126);
            this.groupBox2.TabIndex = 59;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "new";
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(430, 67);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(100, 40);
            this.button14.TabIndex = 63;
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(324, 67);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(100, 40);
            this.button13.TabIndex = 62;
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(218, 67);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(100, 40);
            this.button12.TabIndex = 61;
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(112, 67);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(100, 40);
            this.button11.TabIndex = 60;
            this.button11.Text = "切割mp3範例";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(6, 67);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(100, 40);
            this.button10.TabIndex = 59;
            this.button10.Text = "取得mp3音樂長度";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(430, 21);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(100, 40);
            this.button9.TabIndex = 58;
            this.button9.Text = "info";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // tb_filename
            // 
            this.tb_filename.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_filename.Location = new System.Drawing.Point(12, 134);
            this.tb_filename.Multiline = true;
            this.tb_filename.Name = "tb_filename";
            this.tb_filename.Size = new System.Drawing.Size(924, 61);
            this.tb_filename.TabIndex = 61;
            // 
            // lb_time
            // 
            this.lb_time.AutoSize = true;
            this.lb_time.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_time.Location = new System.Drawing.Point(273, 223);
            this.lb_time.Name = "lb_time";
            this.lb_time.Size = new System.Drawing.Size(58, 21);
            this.lb_time.TabIndex = 62;
            this.lb_time.Text = "label2";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // bt_plus
            // 
            this.bt_plus.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_plus.BackgroundImage")));
            this.bt_plus.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_plus.Location = new System.Drawing.Point(442, 199);
            this.bt_plus.Name = "bt_plus";
            this.bt_plus.Size = new System.Drawing.Size(40, 40);
            this.bt_plus.TabIndex = 63;
            this.bt_plus.UseVisualStyleBackColor = true;
            this.bt_plus.Click += new System.EventHandler(this.bt_plus_Click);
            // 
            // bt_minus
            // 
            this.bt_minus.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_minus.BackgroundImage")));
            this.bt_minus.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_minus.Location = new System.Drawing.Point(442, 241);
            this.bt_minus.Name = "bt_minus";
            this.bt_minus.Size = new System.Drawing.Size(40, 40);
            this.bt_minus.TabIndex = 64;
            this.bt_minus.UseVisualStyleBackColor = true;
            this.bt_minus.Click += new System.EventHandler(this.bt_minus_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(948, 666);
            this.Controls.Add(this.bt_minus);
            this.Controls.Add(this.bt_plus);
            this.Controls.Add(this.lb_time);
            this.Controls.Add(this.tb_filename);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.lb_cut);
            this.Controls.Add(this.lb_total);
            this.Controls.Add(this.lb_sp);
            this.Controls.Add(this.lb_st);
            this.Controls.Add(this.bt_stop);
            this.Controls.Add(this.bt_play_pause);
            this.Controls.Add(this.bt_save_file);
            this.Controls.Add(this.bt_open_file);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_open_file;
        private System.Windows.Forms.Button bt_save_file;
        private System.Windows.Forms.Button bt_play_pause;
        private System.Windows.Forms.Button bt_stop;
        private System.Windows.Forms.Label lb_st;
        private System.Windows.Forms.Label lb_sp;
        private System.Windows.Forms.Label lb_total;
        private System.Windows.Forms.Label lb_cut;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_ffmpeg1;
        private System.Windows.Forms.Button bt_ffmpeg2;
        private System.Windows.Forms.Button bt_ffmpeg0;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.TextBox tb_filename;
        private System.Windows.Forms.Label lb_time;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button bt_plus;
        private System.Windows.Forms.Button bt_minus;
    }
}

