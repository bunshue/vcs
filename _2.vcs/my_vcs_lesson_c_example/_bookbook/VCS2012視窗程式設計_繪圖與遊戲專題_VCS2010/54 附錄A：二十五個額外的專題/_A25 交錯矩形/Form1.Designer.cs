namespace WindowsApplication1
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
        /// <param name="disposing">如果應該公開 Managed 資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.color1ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.color2ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.sizeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem3 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem4 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem5 = new System.Windows.Forms.ToolStripMenuItem();
            this.autoColorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.color1ToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.color2ToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.bothToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.contextMenuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // contextMenuStrip1
            // 
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.color1ToolStripMenuItem,
            this.color2ToolStripMenuItem,
            this.sizeToolStripMenuItem,
            this.autoColorToolStripMenuItem});
            this.contextMenuStrip1.Name = "contextMenuStrip1";
            this.contextMenuStrip1.Size = new System.Drawing.Size(124, 92);
            // 
            // color1ToolStripMenuItem
            // 
            this.color1ToolStripMenuItem.Name = "color1ToolStripMenuItem";
            this.color1ToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.color1ToolStripMenuItem.Text = "Color1";
            this.color1ToolStripMenuItem.Click += new System.EventHandler(this.color1ToolStripMenuItem_Click);
            // 
            // color2ToolStripMenuItem
            // 
            this.color2ToolStripMenuItem.Name = "color2ToolStripMenuItem";
            this.color2ToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.color2ToolStripMenuItem.Text = "Color2";
            this.color2ToolStripMenuItem.Click += new System.EventHandler(this.color2ToolStripMenuItem_Click);
            // 
            // sizeToolStripMenuItem
            // 
            this.sizeToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem2,
            this.toolStripMenuItem3,
            this.toolStripMenuItem4,
            this.toolStripMenuItem5});
            this.sizeToolStripMenuItem.Name = "sizeToolStripMenuItem";
            this.sizeToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.sizeToolStripMenuItem.Text = "Size";
            // 
            // toolStripMenuItem2
            // 
            this.toolStripMenuItem2.Name = "toolStripMenuItem2";
            this.toolStripMenuItem2.Size = new System.Drawing.Size(88, 22);
            this.toolStripMenuItem2.Text = "10";
            this.toolStripMenuItem2.Click += new System.EventHandler(this.toolStripMenuItem2_Click);
            // 
            // toolStripMenuItem3
            // 
            this.toolStripMenuItem3.Name = "toolStripMenuItem3";
            this.toolStripMenuItem3.Size = new System.Drawing.Size(88, 22);
            this.toolStripMenuItem3.Text = "20";
            this.toolStripMenuItem3.Click += new System.EventHandler(this.toolStripMenuItem3_Click);
            // 
            // toolStripMenuItem4
            // 
            this.toolStripMenuItem4.Name = "toolStripMenuItem4";
            this.toolStripMenuItem4.Size = new System.Drawing.Size(88, 22);
            this.toolStripMenuItem4.Text = "50";
            this.toolStripMenuItem4.Click += new System.EventHandler(this.toolStripMenuItem4_Click);
            // 
            // toolStripMenuItem5
            // 
            this.toolStripMenuItem5.Name = "toolStripMenuItem5";
            this.toolStripMenuItem5.Size = new System.Drawing.Size(88, 22);
            this.toolStripMenuItem5.Text = "100";
            this.toolStripMenuItem5.Click += new System.EventHandler(this.toolStripMenuItem5_Click);
            // 
            // autoColorToolStripMenuItem
            // 
            this.autoColorToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.color1ToolStripMenuItem1,
            this.color2ToolStripMenuItem1,
            this.bothToolStripMenuItem});
            this.autoColorToolStripMenuItem.Name = "autoColorToolStripMenuItem";
            this.autoColorToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.autoColorToolStripMenuItem.Text = "Auto Color";
            // 
            // color1ToolStripMenuItem1
            // 
            this.color1ToolStripMenuItem1.Name = "color1ToolStripMenuItem1";
            this.color1ToolStripMenuItem1.Size = new System.Drawing.Size(103, 22);
            this.color1ToolStripMenuItem1.Text = "Color1";
            this.color1ToolStripMenuItem1.Click += new System.EventHandler(this.color1ToolStripMenuItem1_Click);
            // 
            // color2ToolStripMenuItem1
            // 
            this.color2ToolStripMenuItem1.Name = "color2ToolStripMenuItem1";
            this.color2ToolStripMenuItem1.Size = new System.Drawing.Size(103, 22);
            this.color2ToolStripMenuItem1.Text = "Color2";
            this.color2ToolStripMenuItem1.Click += new System.EventHandler(this.color2ToolStripMenuItem1_Click);
            // 
            // bothToolStripMenuItem
            // 
            this.bothToolStripMenuItem.Name = "bothToolStripMenuItem";
            this.bothToolStripMenuItem.Size = new System.Drawing.Size(103, 22);
            this.bothToolStripMenuItem.Text = "Both";
            this.bothToolStripMenuItem.Click += new System.EventHandler(this.bothToolStripMenuItem_Click);
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // timer2
            // 
            this.timer2.Interval = 1000;
            this.timer2.Tick += new System.EventHandler(this.timer2_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 266);
            this.ContextMenuStrip = this.contextMenuStrip1;
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "交錯矩形 (滑鼠右鍵選單)";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.contextMenuStrip1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.Windows.Forms.ToolStripMenuItem color1ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem color2ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem sizeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem2;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem3;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem4;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem5;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.ToolStripMenuItem autoColorToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem color1ToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem color2ToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem bothToolStripMenuItem;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Timer timer2;
    }
}

