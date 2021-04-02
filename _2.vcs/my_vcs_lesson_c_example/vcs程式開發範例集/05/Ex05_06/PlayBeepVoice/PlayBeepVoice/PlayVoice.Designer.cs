namespace PlayBeepVoice
{
    partial class PlayVoice
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
            this.playBeep = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.playExclamation = new System.Windows.Forms.Button();
            this.playQuestion = new System.Windows.Forms.Button();
            this.playAsterisk = new System.Windows.Forms.Button();
            this.playHand = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // playBeep
            // 
            this.playBeep.Location = new System.Drawing.Point(6, 63);
            this.playBeep.Name = "playBeep";
            this.playBeep.Size = new System.Drawing.Size(127, 23);
            this.playBeep.TabIndex = 0;
            this.playBeep.Text = "播放Beep事件";
            this.playBeep.UseVisualStyleBackColor = true;
            this.playBeep.Click += new System.EventHandler(this.playBeep_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.playExclamation);
            this.groupBox1.Controls.Add(this.playQuestion);
            this.groupBox1.Controls.Add(this.playAsterisk);
            this.groupBox1.Controls.Add(this.playHand);
            this.groupBox1.Controls.Add(this.playBeep);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(324, 242);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "音效類型";
            // 
            // playExclamation
            // 
            this.playExclamation.Location = new System.Drawing.Point(99, 109);
            this.playExclamation.Name = "playExclamation";
            this.playExclamation.Size = new System.Drawing.Size(127, 23);
            this.playExclamation.TabIndex = 2;
            this.playExclamation.Text = "播放Exclamation事件";
            this.playExclamation.UseVisualStyleBackColor = true;
            this.playExclamation.Click += new System.EventHandler(this.playExclamation_Click);
            // 
            // playQuestion
            // 
            this.playQuestion.Location = new System.Drawing.Point(191, 154);
            this.playQuestion.Name = "playQuestion";
            this.playQuestion.Size = new System.Drawing.Size(127, 23);
            this.playQuestion.TabIndex = 4;
            this.playQuestion.Text = "播放Question事件";
            this.playQuestion.UseVisualStyleBackColor = true;
            this.playQuestion.Click += new System.EventHandler(this.playQuestion_Click);
            // 
            // playAsterisk
            // 
            this.playAsterisk.Location = new System.Drawing.Point(191, 63);
            this.playAsterisk.Name = "playAsterisk";
            this.playAsterisk.Size = new System.Drawing.Size(127, 23);
            this.playAsterisk.TabIndex = 3;
            this.playAsterisk.Text = "播放Asterisk事件";
            this.playAsterisk.UseVisualStyleBackColor = true;
            this.playAsterisk.Click += new System.EventHandler(this.playAsterisk_Click);
            // 
            // playHand
            // 
            this.playHand.Location = new System.Drawing.Point(6, 154);
            this.playHand.Name = "playHand";
            this.playHand.Size = new System.Drawing.Size(127, 23);
            this.playHand.TabIndex = 1;
            this.playHand.Text = "播放Hand事件";
            this.playHand.UseVisualStyleBackColor = true;
            this.playHand.Click += new System.EventHandler(this.playHand_Click);
            // 
            // PlayVoice
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(348, 266);
            this.Controls.Add(this.groupBox1);
            this.Name = "PlayVoice";
            this.Text = "播放系統內建的事件聲音";
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button playBeep;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button playHand;
        private System.Windows.Forms.Button playExclamation;
        private System.Windows.Forms.Button playQuestion;
        private System.Windows.Forms.Button playAsterisk;
    }
}

