namespace vcs_MySmoothProgressBarDemo
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.smoothProgressBar1 = new vcs_MySmoothProgressBar.SmoothProgressBar();
            this.smoothProgressBar2 = new vcs_MySmoothProgressBar.SmoothProgressBar();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(27, 352);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(618, 200);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // smoothProgressBar1
            // 
            this.smoothProgressBar1.Location = new System.Drawing.Point(27, 21);
            this.smoothProgressBar1.Maximum = 100;
            this.smoothProgressBar1.Minimum = 0;
            this.smoothProgressBar1.Name = "smoothProgressBar1";
            this.smoothProgressBar1.ProgressBarColor = System.Drawing.Color.Blue;
            this.smoothProgressBar1.Size = new System.Drawing.Size(618, 115);
            this.smoothProgressBar1.TabIndex = 3;
            this.smoothProgressBar1.Value = 0;
            // 
            // smoothProgressBar2
            // 
            this.smoothProgressBar2.Location = new System.Drawing.Point(27, 168);
            this.smoothProgressBar2.Maximum = 100;
            this.smoothProgressBar2.Minimum = 0;
            this.smoothProgressBar2.Name = "smoothProgressBar2";
            this.smoothProgressBar2.ProgressBarColor = System.Drawing.Color.Blue;
            this.smoothProgressBar2.Size = new System.Drawing.Size(618, 115);
            this.smoothProgressBar2.TabIndex = 4;
            this.smoothProgressBar2.Value = 0;
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(665, 572);
            this.Controls.Add(this.smoothProgressBar2);
            this.Controls.Add(this.smoothProgressBar1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private vcs_MySmoothProgressBar.SmoothProgressBar smoothProgressBar1;
        private vcs_MySmoothProgressBar.SmoothProgressBar smoothProgressBar2;
        private System.Windows.Forms.Timer timer1;
    }
}

