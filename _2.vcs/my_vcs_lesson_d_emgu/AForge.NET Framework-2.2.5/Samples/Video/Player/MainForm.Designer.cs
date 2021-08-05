namespace Player
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose( bool disposing )
        {
            if ( disposing && ( components != null ) )
            {
                components.Dispose( );
            }
            base.Dispose( disposing );
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent( )
        {
            this.components = new System.ComponentModel.Container();
            this.statusStrip = new System.Windows.Forms.StatusStrip();
            this.fpsLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.vsp = new AForge.Controls.VideoSourcePlayer();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_exit = new System.Windows.Forms.Button();
            this.statusStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip
            // 
            this.statusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fpsLabel});
            this.statusStrip.Location = new System.Drawing.Point(0, 506);
            this.statusStrip.Name = "statusStrip";
            this.statusStrip.Size = new System.Drawing.Size(1276, 22);
            this.statusStrip.TabIndex = 1;
            this.statusStrip.Text = "statusStrip1";
            // 
            // fpsLabel
            // 
            this.fpsLabel.Name = "fpsLabel";
            this.fpsLabel.Size = new System.Drawing.Size(1261, 17);
            this.fpsLabel.Spring = true;
            this.fpsLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // vsp
            // 
            this.vsp.AutoSizeControl = true;
            this.vsp.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.vsp.ForeColor = System.Drawing.Color.White;
            this.vsp.Location = new System.Drawing.Point(477, 143);
            this.vsp.Name = "vsp";
            this.vsp.Size = new System.Drawing.Size(322, 242);
            this.vsp.TabIndex = 0;
            this.vsp.VideoSource = null;
            this.vsp.NewFrame += new AForge.Controls.VideoSourcePlayer.NewFrameHandler(this.vsp_NewFrame);
            // 
            // timer
            // 
            this.timer.Interval = 1000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1048, 37);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(216, 466);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 46);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(111, 47);
            this.button1.TabIndex = 3;
            this.button1.Text = "Local Video Capture Device";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(12, 114);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(111, 47);
            this.button2.TabIndex = 4;
            this.button2.Text = "Open video file (using DirectShow)";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(12, 183);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(111, 47);
            this.button3.TabIndex = 5;
            this.button3.Text = "Open JPEG URL";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(12, 254);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(111, 47);
            this.button4.TabIndex = 6;
            this.button4.Text = "Open MJPEG URL";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(12, 327);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(111, 47);
            this.button5.TabIndex = 7;
            this.button5.Text = "Capture 1st display";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_exit
            // 
            this.bt_exit.Location = new System.Drawing.Point(12, 441);
            this.bt_exit.Name = "bt_exit";
            this.bt_exit.Size = new System.Drawing.Size(111, 47);
            this.bt_exit.TabIndex = 8;
            this.bt_exit.Text = "Exit";
            this.bt_exit.UseVisualStyleBackColor = true;
            this.bt_exit.Click += new System.EventHandler(this.bt_exit_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1276, 528);
            this.Controls.Add(this.bt_exit);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.vsp);
            this.Controls.Add(this.statusStrip);
            this.Name = "MainForm";
            this.Text = "Simple Player";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.statusStrip.ResumeLayout(false);
            this.statusStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip;
        private AForge.Controls.VideoSourcePlayer vsp;
        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.ToolStripStatusLabel fpsLabel;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_exit;
    }
}

