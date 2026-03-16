namespace OperateCamera
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.Photograph = new System.Windows.Forms.Button();
            this.btnClose = new System.Windows.Forms.Button();
            this.tscbxCameras = new System.Windows.Forms.ComboBox();
            this.btnConnect = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.videoSourcePlayer = new AForge.Controls.VideoSourcePlayer();
            this.videoSourcePlayer1 = new AForge.Controls.VideoSourcePlayer();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // Photograph
            // 
            this.Photograph.Location = new System.Drawing.Point(402, 16);
            this.Photograph.Name = "Photograph";
            this.Photograph.Size = new System.Drawing.Size(75, 23);
            this.Photograph.TabIndex = 1;
            this.Photograph.Text = "拍照";
            this.Photograph.UseVisualStyleBackColor = true;
            this.Photograph.Click += new System.EventHandler(this.Photograph_Click);
            // 
            // btnClose
            // 
            this.btnClose.Location = new System.Drawing.Point(483, 16);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(75, 23);
            this.btnClose.TabIndex = 3;
            this.btnClose.Text = "关闭";
            this.btnClose.UseVisualStyleBackColor = true;
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // tscbxCameras
            // 
            this.tscbxCameras.FormattingEnabled = true;
            this.tscbxCameras.Location = new System.Drawing.Point(113, 19);
            this.tscbxCameras.Name = "tscbxCameras";
            this.tscbxCameras.Size = new System.Drawing.Size(121, 20);
            this.tscbxCameras.TabIndex = 7;
            // 
            // btnConnect
            // 
            this.btnConnect.Location = new System.Drawing.Point(240, 17);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(75, 23);
            this.btnConnect.TabIndex = 8;
            this.btnConnect.Text = "连接";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(18, 21);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 12);
            this.label1.TabIndex = 9;
            this.label1.Text = "视频输入设备：";
            // 
            // videoSourcePlayer
            // 
            this.videoSourcePlayer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.videoSourcePlayer.Location = new System.Drawing.Point(3, 17);
            this.videoSourcePlayer.Name = "videoSourcePlayer";
            this.videoSourcePlayer.Size = new System.Drawing.Size(256, 291);
            this.videoSourcePlayer.TabIndex = 10;
            this.videoSourcePlayer.Text = "videoSourcePlayer";
            this.videoSourcePlayer.VideoSource = null;
            this.videoSourcePlayer.NewFrame += new AForge.Controls.VideoSourcePlayer.NewFrameHandler(this.videoSourcePlayer_NewFrame);
            // 
            // videoSourcePlayer1
            // 
            this.videoSourcePlayer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.videoSourcePlayer1.Location = new System.Drawing.Point(3, 17);
            this.videoSourcePlayer1.Name = "videoSourcePlayer1";
            this.videoSourcePlayer1.Size = new System.Drawing.Size(256, 291);
            this.videoSourcePlayer1.TabIndex = 10;
            this.videoSourcePlayer1.Text = "videoSourcePlayer";
            this.videoSourcePlayer1.VideoSource = null;
            this.videoSourcePlayer1.NewFrame += new AForge.Controls.VideoSourcePlayer.NewFrameHandler(this.videoSourcePlayer1_NewFrame);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.videoSourcePlayer);
            this.groupBox1.Location = new System.Drawing.Point(11, 60);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(262, 311);
            this.groupBox1.TabIndex = 11;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "录像1";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.videoSourcePlayer1);
            this.groupBox2.Location = new System.Drawing.Point(294, 60);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(262, 311);
            this.groupBox2.TabIndex = 12;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "录像2";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(321, 17);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 13;
            this.button1.Text = "开始录像";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(570, 384);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnConnect);
            this.Controls.Add(this.tscbxCameras);
            this.Controls.Add(this.btnClose);
            this.Controls.Add(this.Photograph);
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "录像";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Photograph;
        private System.Windows.Forms.Button btnClose;
        private System.Windows.Forms.ComboBox tscbxCameras;
        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Label label1;
        private AForge.Controls.VideoSourcePlayer videoSourcePlayer;
        private AForge.Controls.VideoSourcePlayer videoSourcePlayer1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button1;
    }
}

