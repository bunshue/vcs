namespace UnhidePercent
{
    partial class UnhidePercent
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
            if (disposing && (components != null))
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
            this.progressBar1 = new System.Windows.Forms.ProgressBar();
            this.label1 = new System.Windows.Forms.Label();
            this.StartOrStop = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(12, 7);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(309, 45);
            this.progressBar1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(280, 74);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "label1";
            // 
            // StartOrStop
            // 
            this.StartOrStop.Font = new System.Drawing.Font("mingliu", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.StartOrStop.Location = new System.Drawing.Point(246, 103);
            this.StartOrStop.Name = "StartOrStop";
            this.StartOrStop.Size = new System.Drawing.Size(75, 34);
            this.StartOrStop.TabIndex = 3;
            this.StartOrStop.Text = "停止";
            this.StartOrStop.UseVisualStyleBackColor = true;
            this.StartOrStop.Click += new System.EventHandler(this.StartOrStop_Click);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // UnhidePercent
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(336, 147);
            this.Controls.Add(this.StartOrStop);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.progressBar1);
            this.Name = "UnhidePercent";
            this.Text = "在ProgressBar控制元件中顯示進度百分比";
            this.Load += new System.EventHandler(this.UnhidePercent_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button StartOrStop;
        private System.Windows.Forms.Timer timer1;
    }
}

