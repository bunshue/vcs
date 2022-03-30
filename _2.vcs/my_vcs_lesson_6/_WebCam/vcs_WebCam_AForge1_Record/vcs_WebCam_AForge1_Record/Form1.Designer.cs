namespace vcs_WebCam_AForge1_Record
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
            this.bt_record_start2 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(851, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(255, 585);
            this.richTextBox1.TabIndex = 8;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox1.Location = new System.Drawing.Point(180, 10);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(640, 480);
            this.pictureBox1.TabIndex = 19;
            this.pictureBox1.TabStop = false;
            // 
            // lb_fps
            // 
            this.lb_fps.AutoSize = true;
            this.lb_fps.Font = new System.Drawing.Font("Courier New", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_fps.Location = new System.Drawing.Point(1063, 12);
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
            this.bt_record_start.Location = new System.Drawing.Point(40, 511);
            this.bt_record_start.Name = "bt_record_start";
            this.bt_record_start.Size = new System.Drawing.Size(140, 50);
            this.bt_record_start.TabIndex = 21;
            this.bt_record_start.Text = "錄影 ST";
            this.bt_record_start.UseVisualStyleBackColor = true;
            this.bt_record_start.Click += new System.EventHandler(this.bt_record_start_Click);
            // 
            // bt_record_stop
            // 
            this.bt_record_stop.Location = new System.Drawing.Point(204, 511);
            this.bt_record_stop.Name = "bt_record_stop";
            this.bt_record_stop.Size = new System.Drawing.Size(140, 50);
            this.bt_record_stop.TabIndex = 22;
            this.bt_record_stop.Text = "錄影 SP";
            this.bt_record_stop.UseVisualStyleBackColor = true;
            this.bt_record_stop.Click += new System.EventHandler(this.bt_record_stop_Click);
            // 
            // bt_record_start2
            // 
            this.bt_record_start2.Location = new System.Drawing.Point(40, 567);
            this.bt_record_start2.Name = "bt_record_start2";
            this.bt_record_start2.Size = new System.Drawing.Size(140, 50);
            this.bt_record_start2.TabIndex = 23;
            this.bt_record_start2.Text = "錄影 3分鐘 ST";
            this.bt_record_start2.UseVisualStyleBackColor = true;
            this.bt_record_start2.Click += new System.EventHandler(this.bt_record_start2_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(977, 442);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(71, 30);
            this.bt_clear.TabIndex = 24;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1184, 661);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.bt_record_start2);
            this.Controls.Add(this.bt_record_stop);
            this.Controls.Add(this.bt_record_start);
            this.Controls.Add(this.lb_fps);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label lb_fps;
        private System.Windows.Forms.Timer timer_fps;
        private System.Windows.Forms.Button bt_record_start;
        private System.Windows.Forms.Button bt_record_stop;
        private System.Windows.Forms.Button bt_record_start2;
        private System.Windows.Forms.Button bt_clear;
    }
}

