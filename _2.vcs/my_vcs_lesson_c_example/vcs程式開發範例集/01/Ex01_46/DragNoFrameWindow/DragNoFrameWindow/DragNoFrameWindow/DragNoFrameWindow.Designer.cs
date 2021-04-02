namespace DragNoFrameWindow
{
    partial class DragNoFrameWindow
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
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.ExitContext = new System.Windows.Forms.ToolStripMenuItem();
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ExitContext});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(95,26);
            // 
            // ExitContext
            // 
            this.ExitContext.Name = "ExitContext";
            this.ExitContext.Size = new System.Drawing.Size(94,22);
            this.ExitContext.Text = "退出";
            this.ExitContext.Click += new System.EventHandler(this.ExitContext_Click);
            // 
            // DragNoFrameWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F,12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::DragNoFrameWindow.Properties.Resources._335;
            this.ClientSize = new System.Drawing.Size(292,266);
            this.ContextMenuStrip = this.contextMenuStrip1;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "DragNoFrameWindow";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "拖动无边框窗体";
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.DragNoFrameWindow_MouseDown);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem ExitContext;
    }
}

