namespace AlveoliClewWindow
{
    partial class AlveoliClewWindow
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
            if(disposing && (components != null))
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AlveoliClewWindow));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.closeButton = new System.Windows.Forms.Button();
            this.clewButton = new System.Windows.Forms.Button();
            this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.closeButton);
            this.groupBox1.Controls.Add(this.clewButton);
            this.groupBox1.Location = new System.Drawing.Point(38, 40);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(200, 115);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "操作類型";
            // 
            // closeButton
            // 
            this.closeButton.Location = new System.Drawing.Point(115, 42);
            this.closeButton.Name = "closeButton";
            this.closeButton.Size = new System.Drawing.Size(43, 23);
            this.closeButton.TabIndex = 1;
            this.closeButton.Text = "關閉";
            this.closeButton.UseVisualStyleBackColor = true;
            this.closeButton.Click += new System.EventHandler(this.closeButton_Click);
            // 
            // clewButton
            // 
            this.clewButton.Location = new System.Drawing.Point(38, 42);
            this.clewButton.Name = "clewButton";
            this.clewButton.Size = new System.Drawing.Size(43, 23);
            this.clewButton.TabIndex = 0;
            this.clewButton.Text = "提示";
            this.clewButton.UseVisualStyleBackColor = true;
            this.clewButton.Click += new System.EventHandler(this.clewButton_Click);
            // 
            // notifyIcon1
            // 
            this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject("notifyIcon1.Icon")));
            this.notifyIcon1.Text = "notifyIcon1";
            this.notifyIcon1.Visible = true;
            this.notifyIcon1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.notifyIcon1_MouseMove);
            // 
            // toolTip1
            // 
            this.toolTip1.AutomaticDelay = 100;
            this.toolTip1.IsBalloon = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(38, 190);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(461, 291);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // AlveoliClewWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(511, 493);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "AlveoliClewWindow";
            this.Text = "任務欄氣泡提示視窗";
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button closeButton;
        private System.Windows.Forms.Button clewButton;
        private System.Windows.Forms.NotifyIcon notifyIcon1;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

