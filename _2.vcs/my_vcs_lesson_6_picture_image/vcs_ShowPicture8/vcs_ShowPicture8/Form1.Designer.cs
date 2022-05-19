namespace vcs_ShowPicture8
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
            this.pictureBox_FadeInFadeOut = new System.Windows.Forms.PictureBox();
            this.timer_FadeInFadeOut = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_FadeInFadeOut)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox_FadeInFadeOut
            // 
            this.pictureBox_FadeInFadeOut.Location = new System.Drawing.Point(30, 30);
            this.pictureBox_FadeInFadeOut.Name = "pictureBox_FadeInFadeOut";
            this.pictureBox_FadeInFadeOut.Size = new System.Drawing.Size(249, 254);
            this.pictureBox_FadeInFadeOut.TabIndex = 0;
            this.pictureBox_FadeInFadeOut.TabStop = false;
            this.pictureBox_FadeInFadeOut.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_FadeInFadeOut_Paint);
            // 
            // timer_FadeInFadeOut
            // 
            this.timer_FadeInFadeOut.Enabled = true;
            this.timer_FadeInFadeOut.Tick += new System.EventHandler(this.timer_FadeInFadeOut_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1019, 709);
            this.Controls.Add(this.pictureBox_FadeInFadeOut);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_FadeInFadeOut)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox_FadeInFadeOut;
        private System.Windows.Forms.Timer timer_FadeInFadeOut;
    }
}

