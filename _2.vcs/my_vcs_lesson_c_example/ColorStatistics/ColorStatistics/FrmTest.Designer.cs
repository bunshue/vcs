namespace ColorStatistics
{
    partial class FrmTest
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FrmTest));
            this.CmdOpen = new System.Windows.Forms.Button();
            this.PicR = new System.Windows.Forms.PictureBox();
            this.Thumb = new System.Windows.Forms.PictureBox();
            this.LblStatus = new System.Windows.Forms.Label();
            this.CmdDeal = new System.Windows.Forms.Button();
            this.Label = new System.Windows.Forms.Label();
            this.SliderColorAmount = new System.Windows.Forms.TrackBar();
            this.LblAmount = new System.Windows.Forms.Label();
            this.LblDelta = new System.Windows.Forms.Label();
            this.SliderDelta = new System.Windows.Forms.TrackBar();
            this.label2 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.PicR)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Thumb)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderColorAmount)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderDelta)).BeginInit();
            this.SuspendLayout();
            // 
            // CmdOpen
            // 
            this.CmdOpen.Location = new System.Drawing.Point(12, 12);
            this.CmdOpen.Name = "CmdOpen";
            this.CmdOpen.Size = new System.Drawing.Size(75, 23);
            this.CmdOpen.TabIndex = 1;
            this.CmdOpen.Text = "选择图像";
            this.CmdOpen.UseVisualStyleBackColor = true;
            this.CmdOpen.Click += new System.EventHandler(this.CmdOpen_Click);
            // 
            // PicR
            // 
            this.PicR.Location = new System.Drawing.Point(485, 12);
            this.PicR.Name = "PicR";
            this.PicR.Size = new System.Drawing.Size(519, 561);
            this.PicR.TabIndex = 2;
            this.PicR.TabStop = false;
            this.PicR.Click += new System.EventHandler(this.PicR_Click);
            this.PicR.Paint += new System.Windows.Forms.PaintEventHandler(this.PicR_Paint);
            // 
            // Thumb
            // 
            this.Thumb.Image = ((System.Drawing.Image)(resources.GetObject("Thumb.Image")));
            this.Thumb.Location = new System.Drawing.Point(12, 133);
            this.Thumb.Name = "Thumb";
            this.Thumb.Size = new System.Drawing.Size(453, 300);
            this.Thumb.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.Thumb.TabIndex = 3;
            this.Thumb.TabStop = false;
            // 
            // LblStatus
            // 
            this.LblStatus.AutoSize = true;
            this.LblStatus.Location = new System.Drawing.Point(200, 17);
            this.LblStatus.Name = "LblStatus";
            this.LblStatus.Size = new System.Drawing.Size(0, 12);
            this.LblStatus.TabIndex = 4;
            // 
            // CmdDeal
            // 
            this.CmdDeal.Location = new System.Drawing.Point(103, 12);
            this.CmdDeal.Name = "CmdDeal";
            this.CmdDeal.Size = new System.Drawing.Size(75, 23);
            this.CmdDeal.TabIndex = 5;
            this.CmdDeal.Text = "处理";
            this.CmdDeal.UseVisualStyleBackColor = true;
            this.CmdDeal.Click += new System.EventHandler(this.CmdDeal_Click);
            // 
            // Label
            // 
            this.Label.AutoSize = true;
            this.Label.Location = new System.Drawing.Point(12, 51);
            this.Label.Name = "Label";
            this.Label.Size = new System.Drawing.Size(89, 12);
            this.Label.TabIndex = 6;
            this.Label.Text = "主要颜色总数：";
            // 
            // SliderColorAmount
            // 
            this.SliderColorAmount.Location = new System.Drawing.Point(116, 46);
            this.SliderColorAmount.Maximum = 20;
            this.SliderColorAmount.Minimum = 1;
            this.SliderColorAmount.Name = "SliderColorAmount";
            this.SliderColorAmount.Size = new System.Drawing.Size(301, 45);
            this.SliderColorAmount.TabIndex = 7;
            this.SliderColorAmount.TickStyle = System.Windows.Forms.TickStyle.None;
            this.SliderColorAmount.Value = 20;
            this.SliderColorAmount.Scroll += new System.EventHandler(this.SliderColorAmount_Scroll);
            // 
            // LblAmount
            // 
            this.LblAmount.AutoSize = true;
            this.LblAmount.Location = new System.Drawing.Point(423, 51);
            this.LblAmount.Name = "LblAmount";
            this.LblAmount.Size = new System.Drawing.Size(17, 12);
            this.LblAmount.TabIndex = 8;
            this.LblAmount.Text = "20";
            // 
            // LblDelta
            // 
            this.LblDelta.AutoSize = true;
            this.LblDelta.Location = new System.Drawing.Point(423, 87);
            this.LblDelta.Name = "LblDelta";
            this.LblDelta.Size = new System.Drawing.Size(17, 12);
            this.LblDelta.TabIndex = 11;
            this.LblDelta.Text = "24";
            // 
            // SliderDelta
            // 
            this.SliderDelta.Location = new System.Drawing.Point(116, 82);
            this.SliderDelta.Maximum = 128;
            this.SliderDelta.Minimum = 1;
            this.SliderDelta.Name = "SliderDelta";
            this.SliderDelta.Size = new System.Drawing.Size(301, 45);
            this.SliderDelta.TabIndex = 10;
            this.SliderDelta.TickStyle = System.Windows.Forms.TickStyle.None;
            this.SliderDelta.Value = 24;
            this.SliderDelta.Scroll += new System.EventHandler(this.SliderDelta_Scroll);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 87);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 9;
            this.label2.Text = "Delta：";
            // 
            // FrmTest
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1080, 585);
            this.Controls.Add(this.LblDelta);
            this.Controls.Add(this.SliderDelta);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.LblAmount);
            this.Controls.Add(this.SliderColorAmount);
            this.Controls.Add(this.Label);
            this.Controls.Add(this.CmdDeal);
            this.Controls.Add(this.LblStatus);
            this.Controls.Add(this.Thumb);
            this.Controls.Add(this.PicR);
            this.Controls.Add(this.CmdOpen);
            this.MaximizeBox = false;
            this.Name = "FrmTest";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "测试窗口";
            this.Load += new System.EventHandler(this.FrmTest_Load);
            ((System.ComponentModel.ISupportInitialize)(this.PicR)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Thumb)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderColorAmount)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.SliderDelta)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button CmdOpen;
        private System.Windows.Forms.PictureBox PicR;
        private System.Windows.Forms.PictureBox Thumb;
        private System.Windows.Forms.Label LblStatus;
        private System.Windows.Forms.Button CmdDeal;
        private System.Windows.Forms.Label Label;
        private System.Windows.Forms.TrackBar SliderColorAmount;
        private System.Windows.Forms.Label LblAmount;
        private System.Windows.Forms.Label LblDelta;
        private System.Windows.Forms.TrackBar SliderDelta;
        private System.Windows.Forms.Label label2;
    }
}

