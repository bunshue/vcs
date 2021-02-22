namespace vcs_Draw9_Example3
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
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_save = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.timer_battery1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lblStatus = new System.Windows.Forms.Label();
            this.picHBattery2 = new System.Windows.Forms.PictureBox();
            this.picVBattery2 = new System.Windows.Forms.PictureBox();
            this.picHBattery1 = new System.Windows.Forms.PictureBox();
            this.picVBattery1 = new System.Windows.Forms.PictureBox();
            this.picSamples = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picHBattery2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVBattery2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHBattery1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVBattery1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSamples)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(706, 479);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(548, 140);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(0, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(704, 418);
            this.pictureBox1.TabIndex = 15;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(875, 428);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(100, 40);
            this.bt_save.TabIndex = 56;
            this.bt_save.Text = "Save";
            this.bt_save.UseVisualStyleBackColor = true;
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(1153, 579);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(63, 40);
            this.bt_clear.TabIndex = 55;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // timer_battery1
            // 
            this.timer_battery1.Enabled = true;
            this.timer_battery1.Interval = 500;
            this.timer_battery1.Tick += new System.EventHandler(this.timer_battery1_Tick);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lblStatus);
            this.groupBox1.Controls.Add(this.picHBattery2);
            this.groupBox1.Controls.Add(this.picVBattery2);
            this.groupBox1.Controls.Add(this.picHBattery1);
            this.groupBox1.Controls.Add(this.picVBattery1);
            this.groupBox1.Location = new System.Drawing.Point(12, 439);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(346, 162);
            this.groupBox1.TabIndex = 75;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Battery";
            // 
            // lblStatus
            // 
            this.lblStatus.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.lblStatus.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblStatus.Location = new System.Drawing.Point(17, 40);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(173, 37);
            this.lblStatus.TabIndex = 10;
            this.lblStatus.Text = "Offline";
            this.lblStatus.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // picHBattery2
            // 
            this.picHBattery2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picHBattery2.Location = new System.Drawing.Point(108, 96);
            this.picHBattery2.Name = "picHBattery2";
            this.picHBattery2.Size = new System.Drawing.Size(80, 37);
            this.picHBattery2.TabIndex = 9;
            this.picHBattery2.TabStop = false;
            // 
            // picVBattery2
            // 
            this.picVBattery2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picVBattery2.Location = new System.Drawing.Point(272, 59);
            this.picVBattery2.Name = "picVBattery2";
            this.picVBattery2.Size = new System.Drawing.Size(40, 74);
            this.picVBattery2.TabIndex = 8;
            this.picVBattery2.TabStop = false;
            // 
            // picHBattery1
            // 
            this.picHBattery1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picHBattery1.Location = new System.Drawing.Point(22, 96);
            this.picHBattery1.Name = "picHBattery1";
            this.picHBattery1.Size = new System.Drawing.Size(80, 37);
            this.picHBattery1.TabIndex = 7;
            this.picHBattery1.TabStop = false;
            // 
            // picVBattery1
            // 
            this.picVBattery1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picVBattery1.Location = new System.Drawing.Point(226, 59);
            this.picVBattery1.Name = "picVBattery1";
            this.picVBattery1.Size = new System.Drawing.Size(40, 74);
            this.picVBattery1.TabIndex = 6;
            this.picVBattery1.TabStop = false;
            // 
            // picSamples
            // 
            this.picSamples.BackColor = System.Drawing.Color.Pink;
            this.picSamples.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSamples.Location = new System.Drawing.Point(376, 439);
            this.picSamples.Name = "picSamples";
            this.picSamples.Size = new System.Drawing.Size(243, 127);
            this.picSamples.TabIndex = 76;
            this.picSamples.TabStop = false;
            this.picSamples.Paint += new System.Windows.Forms.PaintEventHandler(this.picSamples_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1389, 688);
            this.Controls.Add(this.picSamples);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.bt_save);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.picHBattery2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVBattery2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHBattery1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVBattery1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSamples)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Timer timer_battery1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.PictureBox picHBattery2;
        private System.Windows.Forms.PictureBox picVBattery2;
        private System.Windows.Forms.PictureBox picHBattery1;
        private System.Windows.Forms.PictureBox picVBattery1;
        private System.Windows.Forms.PictureBox picSamples;
    }
}

