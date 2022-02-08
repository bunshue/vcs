namespace vcs_ColorPalette3
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.Label1 = new System.Windows.Forms.Label();
            this.lblAlpha = new System.Windows.Forms.Label();
            this.picAlpha = new System.Windows.Forms.PictureBox();
            this.tkbAlpha = new System.Windows.Forms.TrackBar();
            this.picBlue = new System.Windows.Forms.PictureBox();
            this.picGreen = new System.Windows.Forms.PictureBox();
            this.picRed = new System.Windows.Forms.PictureBox();
            this.tkbBlue = new System.Windows.Forms.TrackBar();
            this.tkbGreen = new System.Windows.Forms.TrackBar();
            this.tkbRed = new System.Windows.Forms.TrackBar();
            this.lblPaint = new System.Windows.Forms.Label();
            this.lblBlue = new System.Windows.Forms.Label();
            this.lblGreen = new System.Windows.Forms.Label();
            this.lblRed = new System.Windows.Forms.Label();
            this.picPaint = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picAlpha)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbAlpha)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBlue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGreen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbBlue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbGreen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbRed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picPaint)).BeginInit();
            this.SuspendLayout();
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label1.Location = new System.Drawing.Point(251, 10);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(66, 19);
            this.Label1.TabIndex = 142;
            this.Label1.Text = "調色盤";
            // 
            // lblAlpha
            // 
            this.lblAlpha.AutoSize = true;
            this.lblAlpha.Location = new System.Drawing.Point(54, 185);
            this.lblAlpha.Name = "lblAlpha";
            this.lblAlpha.Size = new System.Drawing.Size(19, 12);
            this.lblAlpha.TabIndex = 141;
            this.lblAlpha.Text = "A=";
            // 
            // picAlpha
            // 
            this.picAlpha.Location = new System.Drawing.Point(154, 202);
            this.picAlpha.Name = "picAlpha";
            this.picAlpha.Size = new System.Drawing.Size(25, 25);
            this.picAlpha.TabIndex = 140;
            this.picAlpha.TabStop = false;
            // 
            // tkbAlpha
            // 
            this.tkbAlpha.LargeChange = 20;
            this.tkbAlpha.Location = new System.Drawing.Point(14, 202);
            this.tkbAlpha.Maximum = 255;
            this.tkbAlpha.Name = "tkbAlpha";
            this.tkbAlpha.Size = new System.Drawing.Size(134, 45);
            this.tkbAlpha.TabIndex = 139;
            this.tkbAlpha.TickFrequency = 10;
            // 
            // picBlue
            // 
            this.picBlue.Location = new System.Drawing.Point(154, 144);
            this.picBlue.Name = "picBlue";
            this.picBlue.Size = new System.Drawing.Size(25, 25);
            this.picBlue.TabIndex = 138;
            this.picBlue.TabStop = false;
            // 
            // picGreen
            // 
            this.picGreen.Location = new System.Drawing.Point(154, 81);
            this.picGreen.Name = "picGreen";
            this.picGreen.Size = new System.Drawing.Size(25, 25);
            this.picGreen.TabIndex = 137;
            this.picGreen.TabStop = false;
            // 
            // picRed
            // 
            this.picRed.Location = new System.Drawing.Point(155, 21);
            this.picRed.Name = "picRed";
            this.picRed.Size = new System.Drawing.Size(25, 25);
            this.picRed.TabIndex = 136;
            this.picRed.TabStop = false;
            // 
            // tkbBlue
            // 
            this.tkbBlue.LargeChange = 20;
            this.tkbBlue.Location = new System.Drawing.Point(14, 144);
            this.tkbBlue.Maximum = 255;
            this.tkbBlue.Name = "tkbBlue";
            this.tkbBlue.Size = new System.Drawing.Size(134, 45);
            this.tkbBlue.TabIndex = 135;
            this.tkbBlue.TickFrequency = 10;
            // 
            // tkbGreen
            // 
            this.tkbGreen.LargeChange = 20;
            this.tkbGreen.Location = new System.Drawing.Point(12, 81);
            this.tkbGreen.Maximum = 255;
            this.tkbGreen.Name = "tkbGreen";
            this.tkbGreen.Size = new System.Drawing.Size(136, 45);
            this.tkbGreen.TabIndex = 134;
            this.tkbGreen.TickFrequency = 10;
            // 
            // tkbRed
            // 
            this.tkbRed.LargeChange = 20;
            this.tkbRed.Location = new System.Drawing.Point(12, 21);
            this.tkbRed.Maximum = 255;
            this.tkbRed.Name = "tkbRed";
            this.tkbRed.Size = new System.Drawing.Size(136, 45);
            this.tkbRed.TabIndex = 133;
            this.tkbRed.TickFrequency = 10;
            // 
            // lblPaint
            // 
            this.lblPaint.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPaint.Font = new System.Drawing.Font("新細明體", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblPaint.Location = new System.Drawing.Point(210, 187);
            this.lblPaint.Name = "lblPaint";
            this.lblPaint.Size = new System.Drawing.Size(167, 40);
            this.lblPaint.TabIndex = 132;
            this.lblPaint.Text = "目前顏色設定值：";
            // 
            // lblBlue
            // 
            this.lblBlue.AutoSize = true;
            this.lblBlue.Font = new System.Drawing.Font("新細明體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblBlue.Location = new System.Drawing.Point(54, 129);
            this.lblBlue.Name = "lblBlue";
            this.lblBlue.Size = new System.Drawing.Size(25, 12);
            this.lblBlue.TabIndex = 131;
            this.lblBlue.Text = "B = ";
            // 
            // lblGreen
            // 
            this.lblGreen.AutoSize = true;
            this.lblGreen.Font = new System.Drawing.Font("新細明體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblGreen.Location = new System.Drawing.Point(54, 69);
            this.lblGreen.Name = "lblGreen";
            this.lblGreen.Size = new System.Drawing.Size(22, 12);
            this.lblGreen.TabIndex = 130;
            this.lblGreen.Text = "G =";
            // 
            // lblRed
            // 
            this.lblRed.AutoSize = true;
            this.lblRed.Font = new System.Drawing.Font("新細明體", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblRed.Location = new System.Drawing.Point(54, 10);
            this.lblRed.Name = "lblRed";
            this.lblRed.Size = new System.Drawing.Size(19, 12);
            this.lblRed.TabIndex = 129;
            this.lblRed.Text = "R=";
            // 
            // picPaint
            // 
            this.picPaint.BackColor = System.Drawing.SystemColors.Control;
            this.picPaint.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.picPaint.Location = new System.Drawing.Point(225, 40);
            this.picPaint.Name = "picPaint";
            this.picPaint.Size = new System.Drawing.Size(152, 137);
            this.picPaint.TabIndex = 128;
            this.picPaint.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(399, 252);
            this.Controls.Add(this.Label1);
            this.Controls.Add(this.lblAlpha);
            this.Controls.Add(this.picAlpha);
            this.Controls.Add(this.tkbAlpha);
            this.Controls.Add(this.picBlue);
            this.Controls.Add(this.picGreen);
            this.Controls.Add(this.picRed);
            this.Controls.Add(this.tkbBlue);
            this.Controls.Add(this.tkbGreen);
            this.Controls.Add(this.tkbRed);
            this.Controls.Add(this.lblPaint);
            this.Controls.Add(this.lblBlue);
            this.Controls.Add(this.lblGreen);
            this.Controls.Add(this.lblRed);
            this.Controls.Add(this.picPaint);
            this.Name = "Form1";
            this.Text = "調色盤";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picAlpha)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbAlpha)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBlue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picGreen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbBlue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbGreen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tkbRed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picPaint)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label Label1;
        internal System.Windows.Forms.Label lblAlpha;
        internal System.Windows.Forms.PictureBox picAlpha;
        internal System.Windows.Forms.TrackBar tkbAlpha;
        internal System.Windows.Forms.PictureBox picBlue;
        internal System.Windows.Forms.PictureBox picGreen;
        internal System.Windows.Forms.PictureBox picRed;
        internal System.Windows.Forms.TrackBar tkbBlue;
        internal System.Windows.Forms.TrackBar tkbGreen;
        internal System.Windows.Forms.TrackBar tkbRed;
        internal System.Windows.Forms.Label lblPaint;
        internal System.Windows.Forms.Label lblBlue;
        internal System.Windows.Forms.Label lblGreen;
        internal System.Windows.Forms.Label lblRed;
        internal System.Windows.Forms.PictureBox picPaint;
    }
}

