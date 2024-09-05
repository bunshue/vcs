namespace vcs_WebCam_AForge2_Record2
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.lb_fps = new System.Windows.Forms.Label();
            this.timer_fps = new System.Windows.Forms.Timer(this.components);
            this.bt_record_start = new System.Windows.Forms.Button();
            this.bt_record_stop = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lb_main_mesg = new System.Windows.Forms.Label();
            this.bt_refresh = new System.Windows.Forms.Button();
            this.bt_exit = new System.Windows.Forms.Button();
            this.bt_stop = new System.Windows.Forms.Button();
            this.bt_snapshot = new System.Windows.Forms.Button();
            this.bt_start = new System.Windows.Forms.Button();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(130, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 19;
            this.pictureBox1.TabStop = false;
            // 
            // lb_fps
            // 
            this.lb_fps.AutoSize = true;
            this.lb_fps.Font = new System.Drawing.Font("Courier New", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_fps.Location = new System.Drawing.Point(6, 101);
            this.lb_fps.Name = "lb_fps";
            this.lb_fps.Size = new System.Drawing.Size(43, 21);
            this.lb_fps.TabIndex = 20;
            this.lb_fps.Text = "fps";
            // 
            // timer_fps
            // 
            this.timer_fps.Enabled = true;
            this.timer_fps.Interval = 1000;
            this.timer_fps.Tick += new System.EventHandler(this.timer_fps_Tick);
            // 
            // bt_record_start
            // 
            this.bt_record_start.Location = new System.Drawing.Point(82, 63);
            this.bt_record_start.Name = "bt_record_start";
            this.bt_record_start.Size = new System.Drawing.Size(70, 30);
            this.bt_record_start.TabIndex = 21;
            this.bt_record_start.Text = "錄影 開始";
            this.bt_record_start.UseVisualStyleBackColor = true;
            this.bt_record_start.Click += new System.EventHandler(this.bt_record_start_Click);
            // 
            // bt_record_stop
            // 
            this.bt_record_stop.Location = new System.Drawing.Point(153, 64);
            this.bt_record_stop.Name = "bt_record_stop";
            this.bt_record_stop.Size = new System.Drawing.Size(70, 30);
            this.bt_record_stop.TabIndex = 22;
            this.bt_record_stop.Text = "錄影 停止";
            this.bt_record_stop.UseVisualStyleBackColor = true;
            this.bt_record_stop.Click += new System.EventHandler(this.bt_record_stop_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(159, 82);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(71, 30);
            this.bt_clear.TabIndex = 24;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lb_main_mesg);
            this.groupBox1.Controls.Add(this.bt_refresh);
            this.groupBox1.Controls.Add(this.bt_exit);
            this.groupBox1.Controls.Add(this.bt_stop);
            this.groupBox1.Controls.Add(this.lb_fps);
            this.groupBox1.Controls.Add(this.bt_snapshot);
            this.groupBox1.Controls.Add(this.bt_start);
            this.groupBox1.Controls.Add(this.bt_record_stop);
            this.groupBox1.Controls.Add(this.bt_record_start);
            this.groupBox1.Location = new System.Drawing.Point(4, 116);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(512, 141);
            this.groupBox1.TabIndex = 25;
            this.groupBox1.TabStop = false;
            // 
            // lb_main_mesg
            // 
            this.lb_main_mesg.AutoSize = true;
            this.lb_main_mesg.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg.Location = new System.Drawing.Point(55, 101);
            this.lb_main_mesg.Name = "lb_main_mesg";
            this.lb_main_mesg.Size = new System.Drawing.Size(154, 24);
            this.lb_main_mesg.TabIndex = 27;
            this.lb_main_mesg.Text = "lb_main_mesg";
            // 
            // bt_refresh
            // 
            this.bt_refresh.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_refresh.Location = new System.Drawing.Point(153, 21);
            this.bt_refresh.Name = "bt_refresh";
            this.bt_refresh.Size = new System.Drawing.Size(70, 30);
            this.bt_refresh.TabIndex = 31;
            this.bt_refresh.Text = "重抓";
            this.bt_refresh.UseVisualStyleBackColor = true;
            this.bt_refresh.Click += new System.EventHandler(this.bt_refresh_Click);
            // 
            // bt_exit
            // 
            this.bt_exit.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_exit.Location = new System.Drawing.Point(229, 22);
            this.bt_exit.Name = "bt_exit";
            this.bt_exit.Size = new System.Drawing.Size(70, 30);
            this.bt_exit.TabIndex = 30;
            this.bt_exit.Text = "離開";
            this.bt_exit.UseVisualStyleBackColor = true;
            this.bt_exit.Click += new System.EventHandler(this.bt_exit_Click);
            // 
            // bt_stop
            // 
            this.bt_stop.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_stop.Location = new System.Drawing.Point(82, 21);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(70, 30);
            this.bt_stop.TabIndex = 28;
            this.bt_stop.Text = "停止";
            this.bt_stop.UseVisualStyleBackColor = true;
            this.bt_stop.Click += new System.EventHandler(this.bt_stop_Click);
            // 
            // bt_snapshot
            // 
            this.bt_snapshot.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_snapshot.Location = new System.Drawing.Point(6, 62);
            this.bt_snapshot.Name = "bt_snapshot";
            this.bt_snapshot.Size = new System.Drawing.Size(70, 30);
            this.bt_snapshot.TabIndex = 29;
            this.bt_snapshot.Text = "截圖";
            this.bt_snapshot.UseVisualStyleBackColor = true;
            this.bt_snapshot.Click += new System.EventHandler(this.bt_snapshot_Click);
            // 
            // bt_start
            // 
            this.bt_start.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_start.Location = new System.Drawing.Point(6, 20);
            this.bt_start.Name = "bt_start";
            this.bt_start.Size = new System.Drawing.Size(70, 30);
            this.bt_start.TabIndex = 27;
            this.bt_start.Text = "啟動";
            this.bt_start.UseVisualStyleBackColor = true;
            this.bt_start.Click += new System.EventHandler(this.bt_start_Click);
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(533, 261);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "imsCamera";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lb_fps;
        private System.Windows.Forms.Timer timer_fps;
        private System.Windows.Forms.Button bt_record_start;
        private System.Windows.Forms.Button bt_record_stop;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_refresh;
        private System.Windows.Forms.Button bt_exit;
        private System.Windows.Forms.Button bt_stop;
        private System.Windows.Forms.Button bt_snapshot;
        private System.Windows.Forms.Button bt_start;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Label lb_main_mesg;
    }
}

