namespace ScreenCutter
{
    partial class MainForm
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
            this.btnCutter = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCutter
            // 
            this.btnCutter.Location = new System.Drawing.Point(61, 12);
            this.btnCutter.Name = "btnCutter";
            this.btnCutter.Size = new System.Drawing.Size(75, 23);
            this.btnCutter.TabIndex = 0;
            this.btnCutter.Text = "Cutter";
            this.btnCutter.UseVisualStyleBackColor = true;
            this.btnCutter.Click += new System.EventHandler(this.btnCutter_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(200, 47);
            this.Controls.Add(this.btnCutter);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "ScreenCut";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCutter;
    }
}

