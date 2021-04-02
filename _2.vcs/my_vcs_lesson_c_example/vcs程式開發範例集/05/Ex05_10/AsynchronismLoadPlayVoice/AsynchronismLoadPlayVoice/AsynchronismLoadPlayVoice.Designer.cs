namespace AsynchronismLoadPlayVoice
{
    partial class AsynchronismLoadPlayVoice
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
            if(disposing && (components != null))
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.play = new System.Windows.Forms.Button();
            this.path = new System.Windows.Forms.TextBox();
            this.unfold = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.play);
            this.groupBox1.Controls.Add(this.path);
            this.groupBox1.Controls.Add(this.unfold);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(228, 148);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "播放選項";
            // 
            // play
            // 
            this.play.Enabled = false;
            this.play.Location = new System.Drawing.Point(174, 90);
            this.play.Name = "play";
            this.play.Size = new System.Drawing.Size(48, 23);
            this.play.TabIndex = 2;
            this.play.Text = "播放";
            this.play.UseVisualStyleBackColor = true;
            this.play.Click += new System.EventHandler(this.play_Click);
            // 
            // path
            // 
            this.path.Location = new System.Drawing.Point(61, 36);
            this.path.Name = "path";
            this.path.ReadOnly = true;
            this.path.Size = new System.Drawing.Size(161, 22);
            this.path.TabIndex = 1;
            this.path.TextChanged += new System.EventHandler(this.path_TextChanged);
            // 
            // unfold
            // 
            this.unfold.Location = new System.Drawing.Point(6, 35);
            this.unfold.Name = "unfold";
            this.unfold.Size = new System.Drawing.Size(48, 23);
            this.unfold.TabIndex = 0;
            this.unfold.Text = "開啟";
            this.unfold.UseVisualStyleBackColor = true;
            this.unfold.Click += new System.EventHandler(this.unfold_Click);
            // 
            // AsynchronismLoadPlayVoice
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(252, 172);
            this.Controls.Add(this.groupBox1);
            this.Name = "AsynchronismLoadPlayVoice";
            this.Text = "非同步載入並播放音效檔案";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button play;
        private System.Windows.Forms.TextBox path;
        private System.Windows.Forms.Button unfold;
    }
}

