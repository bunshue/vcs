namespace HideToolBar
{
    partial class HideToolBar
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
            this.Counter = new System.Windows.Forms.Timer(this.components);
            this.Tip = new System.Windows.Forms.Label();
            this.JudgeWinMouPosition = new System.Windows.Forms.Timer(this.components);
            this.HideWindow = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // progressBar1
            // 
            this.progressBar1.Location = new System.Drawing.Point(44, 149);
            this.progressBar1.Name = "progressBar1";
            this.progressBar1.Size = new System.Drawing.Size(126, 19);
            this.progressBar1.Style = System.Windows.Forms.ProgressBarStyle.Marquee;
            this.progressBar1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(63, 184);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "正在登錄中……";
            // 
            // Counter
            // 
            this.Counter.Interval = 3000;
            this.Counter.Tick += new System.EventHandler(this.Counter_Tick);
            // 
            // Tip
            // 
            this.Tip.AutoSize = true;
            this.Tip.BackColor = System.Drawing.Color.Transparent;
            this.Tip.Font = new System.Drawing.Font("細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.Tip.Location = new System.Drawing.Point(37, 252);
            this.Tip.Name = "Tip";
            this.Tip.Size = new System.Drawing.Size(152, 16);
            this.Tip.TabIndex = 201;
            this.Tip.Text = "祝賀你！登錄成功！";
            // 
            // JudgeWinMouPosition
            // 
            this.JudgeWinMouPosition.Interval = 1;
            this.JudgeWinMouPosition.Tick += new System.EventHandler(this.JudgeWinMouPosition_Tick);
            // 
            // HideWindow
            // 
            this.HideWindow.Interval = 1;
            this.HideWindow.Tick += new System.EventHandler(this.HideWindow_Tick);
            // 
            // HideToolBar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(542, 566);
            this.Controls.Add(this.Tip);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.progressBar1);
            this.Name = "HideToolBar";
            this.Text = "隱藏式表單";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.HideToolBar_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ProgressBar progressBar1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Timer Counter;
        private System.Windows.Forms.Label Tip;
        private System.Windows.Forms.Timer JudgeWinMouPosition;
        private System.Windows.Forms.Timer HideWindow;
    }
}

