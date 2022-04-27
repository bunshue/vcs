namespace vcs_ImageProcessing6
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.picHidden = new System.Windows.Forms.PictureBox();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnLockBits = new System.Windows.Forms.Button();
            this.btnNoLockBits = new System.Windows.Forms.Button();
            this.picVisible = new System.Windows.Forms.PictureBox();
            this.lblElapsed = new System.Windows.Forms.Label();
            this.btnQuarter = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).BeginInit();
            this.SuspendLayout();
            // 
            // picHidden
            // 
            this.picHidden.Image = ((System.Drawing.Image)(resources.GetObject("picHidden.Image")));
            this.picHidden.Location = new System.Drawing.Point(184, 104);
            this.picHidden.Name = "picHidden";
            this.picHidden.Size = new System.Drawing.Size(305, 400);
            this.picHidden.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHidden.TabIndex = 1;
            this.picHidden.TabStop = false;
            this.picHidden.Visible = false;
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(12, 11);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(80, 22);
            this.btnReset.TabIndex = 3;
            this.btnReset.Text = "Reset";
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // btnLockBits
            // 
            this.btnLockBits.Location = new System.Drawing.Point(184, 11);
            this.btnLockBits.Name = "btnLockBits";
            this.btnLockBits.Size = new System.Drawing.Size(80, 22);
            this.btnLockBits.TabIndex = 5;
            this.btnLockBits.Text = "Lock Bits";
            this.btnLockBits.Click += new System.EventHandler(this.btnLockBits_Click);
            // 
            // btnNoLockBits
            // 
            this.btnNoLockBits.Location = new System.Drawing.Point(98, 11);
            this.btnNoLockBits.Name = "btnNoLockBits";
            this.btnNoLockBits.Size = new System.Drawing.Size(80, 22);
            this.btnNoLockBits.TabIndex = 4;
            this.btnNoLockBits.Text = "No Lock Bits";
            this.btnNoLockBits.Click += new System.EventHandler(this.btnNoLockBits_Click);
            // 
            // picVisible
            // 
            this.picVisible.Location = new System.Drawing.Point(12, 39);
            this.picVisible.Name = "picVisible";
            this.picVisible.Size = new System.Drawing.Size(446, 577);
            this.picVisible.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picVisible.TabIndex = 6;
            this.picVisible.TabStop = false;
            // 
            // lblElapsed
            // 
            this.lblElapsed.AutoSize = true;
            this.lblElapsed.Location = new System.Drawing.Point(12, 574);
            this.lblElapsed.Name = "lblElapsed";
            this.lblElapsed.Size = new System.Drawing.Size(0, 12);
            this.lblElapsed.TabIndex = 7;
            // 
            // btnQuarter
            // 
            this.btnQuarter.Location = new System.Drawing.Point(270, 11);
            this.btnQuarter.Name = "btnQuarter";
            this.btnQuarter.Size = new System.Drawing.Size(80, 22);
            this.btnQuarter.TabIndex = 8;
            this.btnQuarter.Text = "Quarter";
            this.btnQuarter.Click += new System.EventHandler(this.btnQuarter_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(471, 597);
            this.Controls.Add(this.btnQuarter);
            this.Controls.Add(this.lblElapsed);
            this.Controls.Add(this.picVisible);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnLockBits);
            this.Controls.Add(this.btnNoLockBits);
            this.Controls.Add(this.picHidden);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing6";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picVisible)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.PictureBox picHidden;
        internal System.Windows.Forms.Button btnReset;
        internal System.Windows.Forms.Button btnLockBits;
        internal System.Windows.Forms.Button btnNoLockBits;
        internal System.Windows.Forms.PictureBox picVisible;
        private System.Windows.Forms.Label lblElapsed;
        internal System.Windows.Forms.Button btnQuarter;
    }
}

