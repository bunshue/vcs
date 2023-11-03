namespace CH1303
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
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.tsslMsg = new System.Windows.Forms.ToolStripStatusLabel();
            this.tsspShow = new System.Windows.Forms.ToolStripProgressBar();
            this.picSample = new System.Windows.Forms.PictureBox();
            this.tmrAuto = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).BeginInit();
            this.SuspendLayout();
            // 
            // statusStrip1
            // 
            this.statusStrip1.ImageScalingSize = new System.Drawing.Size(22, 22);
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsslMsg,
            this.tsspShow});
            this.statusStrip1.Location = new System.Drawing.Point(0, 165);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Padding = new System.Windows.Forms.Padding(1, 0, 19, 0);
            this.statusStrip1.Size = new System.Drawing.Size(328, 30);
            this.statusStrip1.TabIndex = 2;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // tsslMsg
            // 
            this.tsslMsg.AutoSize = false;
            this.tsslMsg.Name = "tsslMsg";
            this.tsslMsg.Size = new System.Drawing.Size(120, 25);
            this.tsslMsg.Text = "請按我";
            this.tsslMsg.Click += new System.EventHandler(this.tsslMsg_Click);
            // 
            // tsspShow
            // 
            this.tsspShow.Maximum = 200;
            this.tsspShow.Name = "tsspShow";
            this.tsspShow.Size = new System.Drawing.Size(180, 24);
            // 
            // picSample
            // 
            this.picSample.Image = global::CH1303.Properties.Resources._026;
            this.picSample.Location = new System.Drawing.Point(0, 7);
            this.picSample.Name = "picSample";
            this.picSample.Size = new System.Drawing.Size(103, 104);
            this.picSample.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picSample.TabIndex = 3;
            this.picSample.TabStop = false;
            // 
            // tmrAuto
            // 
            this.tmrAuto.Tick += new System.EventHandler(this.tmrAuto_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(328, 195);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.picSample);
            this.Name = "Form1";
            this.Text = "CH1303";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picSample)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel tsslMsg;
        private System.Windows.Forms.ToolStripProgressBar tsspShow;
        private System.Windows.Forms.PictureBox picSample;
        private System.Windows.Forms.Timer tmrAuto;
    }
}

