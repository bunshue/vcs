namespace SnatchPlayTime
{
    partial class SnatchPlayTime
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
            this.filePath = new System.Windows.Forms.TextBox();
            this.playTime = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.snatch = new System.Windows.Forms.Button();
            this.unfold = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // filePath
            // 
            this.filePath.Location = new System.Drawing.Point(80, 25);
            this.filePath.Name = "filePath";
            this.filePath.ReadOnly = true;
            this.filePath.Size = new System.Drawing.Size(137, 22);
            this.filePath.TabIndex = 0;
            this.filePath.TextChanged += new System.EventHandler(this.filePath_TextChanged);
            // 
            // playTime
            // 
            this.playTime.Location = new System.Drawing.Point(80, 79);
            this.playTime.Name = "playTime";
            this.playTime.ReadOnly = true;
            this.playTime.Size = new System.Drawing.Size(137, 22);
            this.playTime.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(66, 12);
            this.label1.TabIndex = 2;
            this.label1.Text = "MP3 檔案：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(9, 82);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 3;
            this.label2.Text = "播放時間：";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.snatch);
            this.groupBox1.Controls.Add(this.unfold);
            this.groupBox1.Controls.Add(this.filePath);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.playTime);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(4, 5);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(284, 161);
            this.groupBox1.TabIndex = 4;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "操作類型";
            // 
            // snatch
            // 
            this.snatch.Enabled = false;
            this.snatch.Location = new System.Drawing.Point(225, 77);
            this.snatch.Name = "snatch";
            this.snatch.Size = new System.Drawing.Size(47, 23);
            this.snatch.TabIndex = 5;
            this.snatch.Text = "取得";
            this.snatch.UseVisualStyleBackColor = true;
            this.snatch.Click += new System.EventHandler(this.snatch_Click);
            // 
            // unfold
            // 
            this.unfold.Location = new System.Drawing.Point(225, 25);
            this.unfold.Name = "unfold";
            this.unfold.Size = new System.Drawing.Size(47, 23);
            this.unfold.TabIndex = 4;
            this.unfold.Text = "開啟";
            this.unfold.UseVisualStyleBackColor = true;
            this.unfold.Click += new System.EventHandler(this.unfold_Click);
            // 
            // SnatchPlayTime
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 171);
            this.Controls.Add(this.groupBox1);
            this.Name = "SnatchPlayTime";
            this.Text = "取得MP3播放時間";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TextBox filePath;
        private System.Windows.Forms.TextBox playTime;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button snatch;
        private System.Windows.Forms.Button unfold;
    }
}

