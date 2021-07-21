namespace EstablishAndExpunctionM3U
{
    partial class EstablishAndExpunctionM3U
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
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.writeIn = new System.Windows.Forms.Button();
            this.openMusic = new System.Windows.Forms.Button();
            this.musicPath = new System.Windows.Forms.TextBox();
            this.musicName = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.M3UPath = new System.Windows.Forms.TextBox();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(9, 22);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "檔案名稱：";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 56);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 2;
            this.label3.Text = "檔案路徑：";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.writeIn);
            this.groupBox2.Controls.Add(this.openMusic);
            this.groupBox2.Controls.Add(this.M3UPath);
            this.groupBox2.Controls.Add(this.musicPath);
            this.groupBox2.Controls.Add(this.musicName);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Location = new System.Drawing.Point(12, 23);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(642, 152);
            this.groupBox2.TabIndex = 5;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "寫入";
            // 
            // writeIn
            // 
            this.writeIn.Location = new System.Drawing.Point(552, 80);
            this.writeIn.Name = "writeIn";
            this.writeIn.Size = new System.Drawing.Size(84, 23);
            this.writeIn.TabIndex = 8;
            this.writeIn.Text = "寫入m3u";
            this.writeIn.UseVisualStyleBackColor = true;
            this.writeIn.Click += new System.EventHandler(this.writeIn_Click);
            // 
            // openMusic
            // 
            this.openMusic.Location = new System.Drawing.Point(552, 34);
            this.openMusic.Name = "openMusic";
            this.openMusic.Size = new System.Drawing.Size(84, 23);
            this.openMusic.TabIndex = 7;
            this.openMusic.Text = "開啟mp3";
            this.openMusic.UseVisualStyleBackColor = true;
            this.openMusic.Click += new System.EventHandler(this.openMusic_Click);
            // 
            // musicPath
            // 
            this.musicPath.Location = new System.Drawing.Point(78, 53);
            this.musicPath.Name = "musicPath";
            this.musicPath.ReadOnly = true;
            this.musicPath.Size = new System.Drawing.Size(468, 22);
            this.musicPath.TabIndex = 5;
            // 
            // musicName
            // 
            this.musicName.Location = new System.Drawing.Point(78, 19);
            this.musicName.Name = "musicName";
            this.musicName.ReadOnly = true;
            this.musicName.Size = new System.Drawing.Size(468, 22);
            this.musicName.TabIndex = 4;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 192);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(642, 422);
            this.richTextBox1.TabIndex = 6;
            this.richTextBox1.Text = "";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(9, 91);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(68, 12);
            this.label4.TabIndex = 3;
            this.label4.Text = "M3U 路徑：";
            // 
            // M3UPath
            // 
            this.M3UPath.Location = new System.Drawing.Point(78, 88);
            this.M3UPath.Name = "M3UPath";
            this.M3UPath.ReadOnly = true;
            this.M3UPath.Size = new System.Drawing.Size(468, 22);
            this.M3UPath.TabIndex = 6;
            // 
            // EstablishAndExpunctionM3U
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(670, 626);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox2);
            this.Name = "EstablishAndExpunctionM3U";
            this.Text = "建立M3U檔案";
            this.Load += new System.EventHandler(this.EstablishAndExpunctionM3U_Load);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button writeIn;
        private System.Windows.Forms.Button openMusic;
        private System.Windows.Forms.TextBox musicPath;
        private System.Windows.Forms.TextBox musicName;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox M3UPath;
    }
}

