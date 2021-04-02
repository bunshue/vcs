namespace SnatchDisplayDeviceListMode
{
    partial class SnatchDisplayDeviceListMode
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
            if(disposing && (components != null))
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.snatch = new System.Windows.Forms.Button();
            this.unhideMode = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.snatch);
            this.groupBox1.Controls.Add(this.unhideMode);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(268, 137);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "操作類型";
            // 
            // snatch
            // 
            this.snatch.Location = new System.Drawing.Point(206, 85);
            this.snatch.Name = "snatch";
            this.snatch.Size = new System.Drawing.Size(50, 23);
            this.snatch.TabIndex = 2;
            this.snatch.Text = "取得";
            this.snatch.UseVisualStyleBackColor = true;
            this.snatch.Click += new System.EventHandler(this.snatch_Click);
            // 
            // unhideMode
            // 
            this.unhideMode.Location = new System.Drawing.Point(77, 37);
            this.unhideMode.Name = "unhideMode";
            this.unhideMode.ReadOnly = true;
            this.unhideMode.Size = new System.Drawing.Size(179, 22);
            this.unhideMode.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 44);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "顯示模式：";
            // 
            // SnatchDisplayDeviceListMode
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 165);
            this.Controls.Add(this.groupBox1);
            this.Name = "SnatchDisplayDeviceListMode";
            this.Text = "取得顯示設備的目前顯示模式";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox unhideMode;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button snatch;
    }
}

