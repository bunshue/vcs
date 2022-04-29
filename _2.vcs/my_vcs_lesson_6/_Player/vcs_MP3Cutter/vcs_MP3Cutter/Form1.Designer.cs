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
            this.lb_st = new System.Windows.Forms.Label();
            this.lb_sp = new System.Windows.Forms.Label();
            this.lb_total = new System.Windows.Forms.Label();
            this.lb_diff = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
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
            this.button1.Text = "切割mp3範例";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(26, 201);
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
            this.trackBar_st.Location = new System.Drawing.Point(12, 18);
            this.trackBar_st.Maximum = 100;
            this.trackBar_st.Name = "trackBar_st";
            this.trackBar_st.Size = new System.Drawing.Size(693, 45);
            this.trackBar_st.TabIndex = 43;
            this.trackBar_st.Scroll += new System.EventHandler(this.trackBar_st_Scroll);
            // 
            // trackBar_sp
            // 
            this.trackBar_sp.LargeChange = 1;
            this.trackBar_sp.Location = new System.Drawing.Point(12, 63);
            this.trackBar_sp.Maximum = 100;
            this.trackBar_sp.Name = "trackBar_sp";
            this.trackBar_sp.Size = new System.Drawing.Size(693, 45);
            this.trackBar_sp.TabIndex = 44;
            this.trackBar_sp.Scroll += new System.EventHandler(this.trackBar_sp_Scroll);
            // 
            // bt_open_file
            // 
            this.bt_open_file.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_open_file.BackgroundImage")));
            this.bt_open_file.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_file.Location = new System.Drawing.Point(924, 23);
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
            this.bt_save_file.Location = new System.Drawing.Point(995, 23);
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
            this.bt_play_pause.Location = new System.Drawing.Point(924, 112);
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
            this.bt_stop.Location = new System.Drawing.Point(995, 112);
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
            // lb_diff
            // 
            this.lb_diff.AutoSize = true;
            this.lb_diff.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_diff.Location = new System.Drawing.Point(711, 99);
            this.lb_diff.Name = "lb_diff";
            this.lb_diff.Size = new System.Drawing.Size(58, 21);
            this.lb_diff.TabIndex = 52;
            this.lb_diff.Text = "label2";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1072, 375);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 53;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1169, 419);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.lb_diff);
            this.Controls.Add(this.lb_total);
            this.Controls.Add(this.trackBar_sp);
            this.Controls.Add(this.lb_sp);
            this.Controls.Add(this.lb_st);
            this.Controls.Add(this.bt_stop);
            this.Controls.Add(this.bt_play_pause);
            this.Controls.Add(this.bt_save_file);
            this.Controls.Add(this.bt_open_file);
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
        private System.Windows.Forms.Label lb_st;
        private System.Windows.Forms.Label lb_sp;
        private System.Windows.Forms.Label lb_total;
        private System.Windows.Forms.Label lb_diff;
        private System.Windows.Forms.Button bt_clear;
    }
}

