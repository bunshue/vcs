﻿namespace vcs_Spotlight1
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timer_spotlight1 = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_spotlight1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spotlight1)).BeginInit();
            this.SuspendLayout();
            // 
            // timer_spotlight1
            // 
            this.timer_spotlight1.Enabled = true;
            this.timer_spotlight1.Interval = 10;
            this.timer_spotlight1.Tick += new System.EventHandler(this.timer_spotlight1_Tick);
            // 
            // pictureBox_spotlight1
            // 
            this.pictureBox_spotlight1.Location = new System.Drawing.Point(377, 77);
            this.pictureBox_spotlight1.Name = "pictureBox_spotlight1";
            this.pictureBox_spotlight1.Size = new System.Drawing.Size(219, 206);
            this.pictureBox_spotlight1.TabIndex = 0;
            this.pictureBox_spotlight1.TabStop = false;
            this.pictureBox_spotlight1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_spotlight1_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1061, 769);
            this.Controls.Add(this.pictureBox_spotlight1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "探照燈";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spotlight1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Timer timer_spotlight1;
        private System.Windows.Forms.PictureBox pictureBox_spotlight1;
    }
}

