namespace vcs_Radar
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
            this.pictureBox_radar = new System.Windows.Forms.PictureBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.panel_radar = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_radar)).BeginInit();
            this.panel_radar.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox_radar
            // 
            this.pictureBox_radar.Location = new System.Drawing.Point(19, 34);
            this.pictureBox_radar.Name = "pictureBox_radar";
            this.pictureBox_radar.Size = new System.Drawing.Size(316, 317);
            this.pictureBox_radar.TabIndex = 0;
            this.pictureBox_radar.TabStop = false;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 5;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // panel_radar
            // 
            this.panel_radar.Controls.Add(this.pictureBox_radar);
            this.panel_radar.Location = new System.Drawing.Point(60, 78);
            this.panel_radar.Name = "panel_radar";
            this.panel_radar.Size = new System.Drawing.Size(349, 373);
            this.panel_radar.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(791, 521);
            this.Controls.Add(this.panel_radar);
            this.Name = "Form1";
            this.Text = "Radar";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_radar)).EndInit();
            this.panel_radar.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox_radar;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Panel panel_radar;
    }
}

