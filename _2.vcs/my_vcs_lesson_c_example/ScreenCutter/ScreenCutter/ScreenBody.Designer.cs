namespace ScreenCutter
{
    partial class ScreenBody
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
            if (disposing && (components != null))
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
            this.components = new System.ComponentModel.Container();
            this.PositonTip = new System.Windows.Forms.ToolTip(this.components);
            this.SuspendLayout();
            // 
            // PositonTip
            // 
            this.PositonTip.ShowAlways = true;
            // 
            // ScreenBody
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 273);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "ScreenBody";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "ScreenBody";
            this.DoubleClick += new System.EventHandler(this.ScreenBody_DoubleClick);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.ScreenBody_MouseUp);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.ScreenBody_MouseMove);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.ScreenBody_MouseDown);
            this.Load += new System.EventHandler(this.ScreenBody_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ToolTip PositonTip;
    }
}