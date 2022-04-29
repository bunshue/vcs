namespace vcs_MP3Cutter
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.button1 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.trackBar_st = new System.Windows.Forms.TrackBar();
            this.trackBar_sp = new System.Windows.Forms.TrackBar();
            this.bt_open_file = new System.Windows.Forms.Button();
            this.bt_save_file = new System.Windows.Forms.Button();
            this.bt_play_pause = new System.Windows.Forms.Button();
            this.bt_stop = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_sp)).BeginInit();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 143);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(127, 52);
            this.button1.TabIndex = 0;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 201);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(1129, 206);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(295, 143);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(127, 52);
            this.button2.TabIndex = 2;
            this.button2.Text = "取得mp3音樂長度";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(438, 143);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(127, 52);
            this.button3.TabIndex = 2;
            this.button3.Text = "button2";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(583, 143);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(127, 52);
            this.button4.TabIndex = 3;
            this.button4.Text = "button4";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // trackBar_st
            // 
            this.trackBar_st.LargeChange = 1;
            this.trackBar_st.Location = new System.Drawing.Point(12, 12);
            this.trackBar_st.Maximum = 100;
            this.trackBar_st.Name = "trackBar_st";
            this.trackBar_st.Size = new System.Drawing.Size(693, 45);
            this.trackBar_st.TabIndex = 43;
            // 
            // trackBar_sp
            // 
            this.trackBar_sp.LargeChange = 1;
            this.trackBar_sp.Location = new System.Drawing.Point(12, 63);
            this.trackBar_sp.Maximum = 100;
            this.trackBar_sp.Name = "trackBar_sp";
            this.trackBar_sp.Size = new System.Drawing.Size(693, 45);
            this.trackBar_sp.TabIndex = 44;
            // 
            // bt_open_file
            // 
            this.bt_open_file.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_open_file.BackgroundImage")));
            this.bt_open_file.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_file.Location = new System.Drawing.Point(770, 25);
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
            this.bt_save_file.Location = new System.Drawing.Point(858, 25);
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
            this.bt_play_pause.Location = new System.Drawing.Point(770, 114);
            this.bt_play_pause.Name = "bt_play_pause";
            this.bt_play_pause.Size = new System.Drawing.Size(64, 64);
            this.bt_play_pause.TabIndex = 47;
            this.bt_play_pause.UseVisualStyleBackColor = true;
            // 
            // bt_stop
            // 
            this.bt_stop.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_stop.BackgroundImage")));
            this.bt_stop.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_stop.Location = new System.Drawing.Point(858, 114);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(64, 64);
            this.bt_stop.TabIndex = 48;
            this.bt_stop.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1153, 419);
            this.Controls.Add(this.bt_stop);
            this.Controls.Add(this.bt_play_pause);
            this.Controls.Add(this.bt_save_file);
            this.Controls.Add(this.bt_open_file);
            this.Controls.Add(this.trackBar_sp);
            this.Controls.Add(this.trackBar_st);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_sp)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.TrackBar trackBar_st;
        private System.Windows.Forms.TrackBar trackBar_sp;
        private System.Windows.Forms.Button bt_open_file;
        private System.Windows.Forms.Button bt_save_file;
        private System.Windows.Forms.Button bt_play_pause;
        private System.Windows.Forms.Button bt_stop;
    }
}

