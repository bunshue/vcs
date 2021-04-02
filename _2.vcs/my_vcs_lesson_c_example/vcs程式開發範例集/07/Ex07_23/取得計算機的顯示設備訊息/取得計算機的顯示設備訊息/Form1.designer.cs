namespace 取得計算機的顯示設備訊息
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.lblname = new System.Windows.Forms.Label();
            this.lblpnp = new System.Windows.Forms.Label();
            this.lbldrivers = new System.Windows.Forms.Label();
            this.lblVersion = new System.Windows.Forms.Label();
            this.lblProcessor = new System.Windows.Forms.Label();
            this.lblMaxRefreshRate = new System.Windows.Forms.Label();
            this.lblMinRefreshRate = new System.Windows.Forms.Label();
            this.lblDescription = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lblDescription);
            this.groupBox1.Controls.Add(this.lblMinRefreshRate);
            this.groupBox1.Controls.Add(this.lblMaxRefreshRate);
            this.groupBox1.Controls.Add(this.lblProcessor);
            this.groupBox1.Controls.Add(this.lblVersion);
            this.groupBox1.Controls.Add(this.lbldrivers);
            this.groupBox1.Controls.Add(this.lblpnp);
            this.groupBox1.Controls.Add(this.lblname);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(497, 240);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "顯示設備訊息";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 27);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "顯示設備名稱：";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 52);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(131, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "顯示設備PNPDeviceID：";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 80);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(137, 12);
            this.label3.TabIndex = 3;
            this.label3.Text = "顯示設備驅動程序文件：";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 109);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(125, 12);
            this.label4.TabIndex = 4;
            this.label4.Text = "顯示設備驅動版本號：";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(6, 135);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(137, 12);
            this.label5.TabIndex = 5;
            this.label5.Text = "顯示設備的顯示處理器：";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(6, 190);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(137, 12);
            this.label6.TabIndex = 6;
            this.label6.Text = "顯示設備的最小更新率：";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(6, 215);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(137, 12);
            this.label8.TabIndex = 8;
            this.label8.Text = "顯示設備目前顯示模式：";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(6, 161);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(137, 12);
            this.label9.TabIndex = 9;
            this.label9.Text = "顯示設備的最大更新率：";
            // 
            // lblname
            // 
            this.lblname.AutoSize = true;
            this.lblname.Location = new System.Drawing.Point(101, 27);
            this.lblname.Name = "lblname";
            this.lblname.Size = new System.Drawing.Size(41, 12);
            this.lblname.TabIndex = 10;
            this.lblname.Text = "label7";
            // 
            // lblpnp
            // 
            this.lblpnp.AutoSize = true;
            this.lblpnp.Location = new System.Drawing.Point(143, 52);
            this.lblpnp.Name = "lblpnp";
            this.lblpnp.Size = new System.Drawing.Size(47, 12);
            this.lblpnp.TabIndex = 11;
            this.lblpnp.Text = "label10";
            // 
            // lbldrivers
            // 
            this.lbldrivers.AutoSize = true;
            this.lbldrivers.Location = new System.Drawing.Point(143, 80);
            this.lbldrivers.Name = "lbldrivers";
            this.lbldrivers.Size = new System.Drawing.Size(47, 12);
            this.lbldrivers.TabIndex = 12;
            this.lbldrivers.Text = "label11";
            // 
            // lblVersion
            // 
            this.lblVersion.AutoSize = true;
            this.lblVersion.Location = new System.Drawing.Point(137, 109);
            this.lblVersion.Name = "lblVersion";
            this.lblVersion.Size = new System.Drawing.Size(47, 12);
            this.lblVersion.TabIndex = 13;
            this.lblVersion.Text = "label12";
            // 
            // lblProcessor
            // 
            this.lblProcessor.AutoSize = true;
            this.lblProcessor.Location = new System.Drawing.Point(143, 135);
            this.lblProcessor.Name = "lblProcessor";
            this.lblProcessor.Size = new System.Drawing.Size(47, 12);
            this.lblProcessor.TabIndex = 14;
            this.lblProcessor.Text = "label13";
            // 
            // lblMaxRefreshRate
            // 
            this.lblMaxRefreshRate.AutoSize = true;
            this.lblMaxRefreshRate.Location = new System.Drawing.Point(149, 161);
            this.lblMaxRefreshRate.Name = "lblMaxRefreshRate";
            this.lblMaxRefreshRate.Size = new System.Drawing.Size(47, 12);
            this.lblMaxRefreshRate.TabIndex = 15;
            this.lblMaxRefreshRate.Text = "label14";
            // 
            // lblMinRefreshRate
            // 
            this.lblMinRefreshRate.AutoSize = true;
            this.lblMinRefreshRate.Location = new System.Drawing.Point(149, 190);
            this.lblMinRefreshRate.Name = "lblMinRefreshRate";
            this.lblMinRefreshRate.Size = new System.Drawing.Size(47, 12);
            this.lblMinRefreshRate.TabIndex = 16;
            this.lblMinRefreshRate.Text = "label15";
            // 
            // lblDescription
            // 
            this.lblDescription.AutoSize = true;
            this.lblDescription.Location = new System.Drawing.Point(149, 215);
            this.lblDescription.Name = "lblDescription";
            this.lblDescription.Size = new System.Drawing.Size(47, 12);
            this.lblDescription.TabIndex = 17;
            this.lblDescription.Text = "label16";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(521, 262);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "取得計算機的顯示設備訊息";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblDescription;
        private System.Windows.Forms.Label lblMinRefreshRate;
        private System.Windows.Forms.Label lblMaxRefreshRate;
        private System.Windows.Forms.Label lblProcessor;
        private System.Windows.Forms.Label lblVersion;
        private System.Windows.Forms.Label lbldrivers;
        private System.Windows.Forms.Label lblpnp;
        private System.Windows.Forms.Label lblname;
    }
}

