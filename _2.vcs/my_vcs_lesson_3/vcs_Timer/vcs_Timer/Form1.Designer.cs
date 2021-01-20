namespace vcs_Timer
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
            this.timer_spin = new System.Windows.Forms.Timer(this.components);
            this.pictureBox_spin = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spin)).BeginInit();
            this.SuspendLayout();
            // 
            // timer_spin
            // 
            this.timer_spin.Enabled = true;
            this.timer_spin.Interval = 50;
            this.timer_spin.Tick += new System.EventHandler(this.timer_spin_Tick);
            // 
            // pictureBox_spin
            // 
            this.pictureBox_spin.Location = new System.Drawing.Point(12, 12);
            this.pictureBox_spin.Name = "pictureBox_spin";
            this.pictureBox_spin.Size = new System.Drawing.Size(50, 50);
            this.pictureBox_spin.TabIndex = 0;
            this.pictureBox_spin.TabStop = false;
            this.pictureBox_spin.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_spin_Paint);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(502, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(165, 564);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(679, 588);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox_spin);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_spin)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Timer timer_spin;
        private System.Windows.Forms.PictureBox pictureBox_spin;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

