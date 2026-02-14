namespace SmoothProgressBar
{
    partial class SmoothProgressBar
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if(disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.smoothProgressBar1 = new WindowsFormsControlLibrary.SmoothProgressBar();
            this.smoothProgressBar2 = new WindowsFormsControlLibrary.SmoothProgressBar();
            this.StartOrStop = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // smoothProgressBar1
            // 
            this.smoothProgressBar1.BackColor = System.Drawing.Color.MistyRose;
            this.smoothProgressBar1.ForeColor = System.Drawing.SystemColors.ControlText;
            this.smoothProgressBar1.Location = new System.Drawing.Point(46, 25);
            this.smoothProgressBar1.Maximum = 100;
            this.smoothProgressBar1.Minimum = 0;
            this.smoothProgressBar1.Name = "smoothProgressBar1";
            this.smoothProgressBar1.ProgressBarColor = System.Drawing.Color.Blue;
            this.smoothProgressBar1.Size = new System.Drawing.Size(150, 30);
            this.smoothProgressBar1.TabIndex = 4;
            this.smoothProgressBar1.Value = 0;
            // 
            // smoothProgressBar2
            // 
            this.smoothProgressBar2.BackColor = System.Drawing.Color.Blue;
            this.smoothProgressBar2.Location = new System.Drawing.Point(46, 85);
            this.smoothProgressBar2.Maximum = 100;
            this.smoothProgressBar2.Minimum = 0;
            this.smoothProgressBar2.Name = "smoothProgressBar2";
            this.smoothProgressBar2.ProgressBarColor = System.Drawing.Color.MediumSpringGreen;
            this.smoothProgressBar2.Size = new System.Drawing.Size(150, 30);
            this.smoothProgressBar2.TabIndex = 3;
            this.smoothProgressBar2.Value = 0;
            // 
            // StartOrStop
            // 
            this.StartOrStop.Location = new System.Drawing.Point(85, 147);
            this.StartOrStop.Name = "StartOrStop";
            this.StartOrStop.Size = new System.Drawing.Size(75, 28);
            this.StartOrStop.TabIndex = 2;
            this.StartOrStop.Text = "開始";
            this.StartOrStop.UseVisualStyleBackColor = true;
            this.StartOrStop.Click += new System.EventHandler(this.StartOrStop_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // SmoothProgressBar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(488, 431);
            this.Controls.Add(this.StartOrStop);
            this.Controls.Add(this.smoothProgressBar2);
            this.Controls.Add(this.smoothProgressBar1);
            this.Name = "SmoothProgressBar";
            this.Text = "自製平滑進度列控制元件";
            this.Load += new System.EventHandler(this.SmoothProgressBar_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private WindowsFormsControlLibrary.SmoothProgressBar smoothProgressBar1;
        private WindowsFormsControlLibrary.SmoothProgressBar smoothProgressBar2;
        private System.Windows.Forms.Button StartOrStop;
        private System.Windows.Forms.Timer timer1;
    }
}

