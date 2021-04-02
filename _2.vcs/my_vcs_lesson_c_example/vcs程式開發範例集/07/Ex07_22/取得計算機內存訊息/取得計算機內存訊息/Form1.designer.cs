namespace 取得計算機內存訊息
{
    partial class Form1
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

        #region Windows 視窗設計器產生的程式碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.lblVuse = new System.Windows.Forms.Label();
            this.lblVinfo = new System.Windows.Forms.Label();
            this.pbVmemoryuse = new System.Windows.Forms.ProgressBar();
            this.pbVmemorysum = new System.Windows.Forms.ProgressBar();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.lblMuse = new System.Windows.Forms.Label();
            this.lblSum = new System.Windows.Forms.Label();
            this.pbMemoryUse = new System.Windows.Forms.ProgressBar();
            this.pbMemorySum = new System.Windows.Forms.ProgressBar();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.lblVuse);
            this.groupBox3.Controls.Add(this.lblVinfo);
            this.groupBox3.Controls.Add(this.pbVmemoryuse);
            this.groupBox3.Controls.Add(this.pbVmemorysum);
            this.groupBox3.Controls.Add(this.label5);
            this.groupBox3.Controls.Add(this.label6);
            this.groupBox3.Location = new System.Drawing.Point(12, 118);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(321, 100);
            this.groupBox3.TabIndex = 5;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "虛擬內存(K)";
            // 
            // lblVuse
            // 
            this.lblVuse.AutoSize = true;
            this.lblVuse.Location = new System.Drawing.Point(257, 61);
            this.lblVuse.Name = "lblVuse";
            this.lblVuse.Size = new System.Drawing.Size(0, 12);
            this.lblVuse.TabIndex = 9;
            // 
            // lblVinfo
            // 
            this.lblVinfo.AutoSize = true;
            this.lblVinfo.Location = new System.Drawing.Point(257, 38);
            this.lblVinfo.Name = "lblVinfo";
            this.lblVinfo.Size = new System.Drawing.Size(0, 12);
            this.lblVinfo.TabIndex = 8;
            // 
            // pbVmemoryuse
            // 
            this.pbVmemoryuse.Location = new System.Drawing.Point(69, 60);
            this.pbVmemoryuse.Name = "pbVmemoryuse";
            this.pbVmemoryuse.Size = new System.Drawing.Size(183, 13);
            this.pbVmemoryuse.TabIndex = 4;
            // 
            // pbVmemorysum
            // 
            this.pbVmemorysum.Location = new System.Drawing.Point(69, 38);
            this.pbVmemorysum.Name = "pbVmemorysum";
            this.pbVmemorysum.Size = new System.Drawing.Size(183, 13);
            this.pbVmemorysum.TabIndex = 3;
            this.pbVmemorysum.Click += new System.EventHandler(this.pbVmemorysum_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(19, 60);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(53, 12);
            this.label5.TabIndex = 1;
            this.label5.Text = "可用數：";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(31, 39);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(41, 12);
            this.label6.TabIndex = 0;
            this.label6.Text = "總數：";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.lblMuse);
            this.groupBox2.Controls.Add(this.lblSum);
            this.groupBox2.Controls.Add(this.pbMemoryUse);
            this.groupBox2.Controls.Add(this.pbMemorySum);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(12, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(321, 100);
            this.groupBox2.TabIndex = 4;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "物理內存(K)";
            // 
            // lblMuse
            // 
            this.lblMuse.AutoSize = true;
            this.lblMuse.Location = new System.Drawing.Point(257, 61);
            this.lblMuse.Name = "lblMuse";
            this.lblMuse.Size = new System.Drawing.Size(0, 12);
            this.lblMuse.TabIndex = 7;
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Location = new System.Drawing.Point(257, 39);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(0, 12);
            this.lblSum.TabIndex = 6;
            // 
            // pbMemoryUse
            // 
            this.pbMemoryUse.Location = new System.Drawing.Point(69, 61);
            this.pbMemoryUse.Name = "pbMemoryUse";
            this.pbMemoryUse.Size = new System.Drawing.Size(183, 13);
            this.pbMemoryUse.TabIndex = 4;
            // 
            // pbMemorySum
            // 
            this.pbMemorySum.Location = new System.Drawing.Point(69, 39);
            this.pbMemorySum.Name = "pbMemorySum";
            this.pbMemorySum.Size = new System.Drawing.Size(183, 13);
            this.pbMemorySum.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(19, 61);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "可用數：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(31, 40);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "總數：";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(349, 234);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "取得計算機內存訊息";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label lblVuse;
        private System.Windows.Forms.Label lblVinfo;
        private System.Windows.Forms.ProgressBar pbVmemoryuse;
        private System.Windows.Forms.ProgressBar pbVmemorysum;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label lblMuse;
        private System.Windows.Forms.Label lblSum;
        private System.Windows.Forms.ProgressBar pbMemoryUse;
        private System.Windows.Forms.ProgressBar pbMemorySum;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Timer timer1;
    }
}

