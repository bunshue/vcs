namespace howto_round_scaled_ellipses
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
            this.label1 = new System.Windows.Forms.Label();
            this.picNormal = new System.Windows.Forms.PictureBox();
            this.picRound = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.picThinPen = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picNormal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRound)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picThinPen)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 8);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Scaled:";
            // 
            // picNormal
            // 
            this.picNormal.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.picNormal.BackColor = System.Drawing.Color.White;
            this.picNormal.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picNormal.Location = new System.Drawing.Point(12, 23);
            this.picNormal.Name = "picNormal";
            this.picNormal.Size = new System.Drawing.Size(229, 553);
            this.picNormal.TabIndex = 1;
            this.picNormal.TabStop = false;
            this.picNormal.Paint += new System.Windows.Forms.PaintEventHandler(this.picNormal_Paint);
            this.picNormal.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pic_MouseClick);
            // 
            // picRound
            // 
            this.picRound.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.picRound.BackColor = System.Drawing.Color.White;
            this.picRound.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picRound.Location = new System.Drawing.Point(595, 23);
            this.picRound.Name = "picRound";
            this.picRound.Size = new System.Drawing.Size(229, 553);
            this.picRound.TabIndex = 3;
            this.picRound.TabStop = false;
            this.picRound.Paint += new System.Windows.Forms.PaintEventHandler(this.picRound_Paint);
            this.picRound.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pic_MouseClick);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(597, 8);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(40, 12);
            this.label2.TabIndex = 2;
            this.label2.Text = "Round:";
            // 
            // picThinPen
            // 
            this.picThinPen.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)));
            this.picThinPen.BackColor = System.Drawing.Color.White;
            this.picThinPen.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picThinPen.Location = new System.Drawing.Point(300, 23);
            this.picThinPen.Name = "picThinPen";
            this.picThinPen.Size = new System.Drawing.Size(229, 553);
            this.picThinPen.TabIndex = 5;
            this.picThinPen.TabStop = false;
            this.picThinPen.Paint += new System.Windows.Forms.PaintEventHandler(this.picThinPen_Paint);
            this.picThinPen.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pic_MouseClick);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(301, 8);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(50, 12);
            this.label3.TabIndex = 4;
            this.label3.Text = "Thin Pen:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(836, 587);
            this.Controls.Add(this.picThinPen);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.picRound);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.picNormal);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_round_scaled_ellipses";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picNormal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picRound)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picThinPen)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox picNormal;
        private System.Windows.Forms.PictureBox picRound;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox picThinPen;
        private System.Windows.Forms.Label label3;
    }
}

