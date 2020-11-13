namespace vcs_Compass
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.picCompass = new System.Windows.Forms.PictureBox();
            this.hbarDegrees = new System.Windows.Forms.HScrollBar();
            this.lblDegrees = new System.Windows.Forms.Label();
            this.picHeading = new System.Windows.Forms.PictureBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picCompass)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHeading)).BeginInit();
            this.SuspendLayout();
            // 
            // picCompass
            // 
            this.picCompass.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCompass.BackColor = System.Drawing.Color.White;
            this.picCompass.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCompass.Location = new System.Drawing.Point(12, 272);
            this.picCompass.Name = "picCompass";
            this.picCompass.Size = new System.Drawing.Size(260, 74);
            this.picCompass.TabIndex = 0;
            this.picCompass.TabStop = false;
            this.picCompass.Paint += new System.Windows.Forms.PaintEventHandler(this.picCompass_Paint);
            // 
            // hbarDegrees
            // 
            this.hbarDegrees.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.hbarDegrees.Location = new System.Drawing.Point(12, 8);
            this.hbarDegrees.Maximum = 360;
            this.hbarDegrees.Name = "hbarDegrees";
            this.hbarDegrees.Size = new System.Drawing.Size(214, 17);
            this.hbarDegrees.TabIndex = 1;
            this.hbarDegrees.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hbarDegrees_Scroll);
            // 
            // lblDegrees
            // 
            this.lblDegrees.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.lblDegrees.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblDegrees.Location = new System.Drawing.Point(229, 8);
            this.lblDegrees.Name = "lblDegrees";
            this.lblDegrees.Size = new System.Drawing.Size(43, 16);
            this.lblDegrees.TabIndex = 2;
            this.lblDegrees.Text = "0";
            this.lblDegrees.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // picHeading
            // 
            this.picHeading.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.picHeading.BackColor = System.Drawing.Color.White;
            this.picHeading.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picHeading.Location = new System.Drawing.Point(12, 27);
            this.picHeading.Name = "picHeading";
            this.picHeading.Size = new System.Drawing.Size(260, 240);
            this.picHeading.TabIndex = 3;
            this.picHeading.TabStop = false;
            this.picHeading.Paint += new System.Windows.Forms.PaintEventHandler(this.picHeading_Paint);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 250;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 351);
            this.Controls.Add(this.picHeading);
            this.Controls.Add(this.lblDegrees);
            this.Controls.Add(this.hbarDegrees);
            this.Controls.Add(this.picCompass);
            this.Name = "Form1";
            this.Text = "vcs_Compass";
            ((System.ComponentModel.ISupportInitialize)(this.picCompass)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHeading)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox picCompass;
        private System.Windows.Forms.HScrollBar hbarDegrees;
        private System.Windows.Forms.Label lblDegrees;
        private System.Windows.Forms.PictureBox picHeading;
        private System.Windows.Forms.Timer timer1;
    }
}

