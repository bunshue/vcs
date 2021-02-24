namespace vcs_ImageProcessing8
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
            this.pictureBox0 = new System.Windows.Forms.PictureBox();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnLockBits = new System.Windows.Forms.Button();
            this.btnNoLockBits = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.btnQuarter = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox0
            // 
            this.pictureBox0.Location = new System.Drawing.Point(30, 67);
            this.pictureBox0.Name = "pictureBox0";
            this.pictureBox0.Size = new System.Drawing.Size(446, 577);
            this.pictureBox0.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox0.TabIndex = 1;
            this.pictureBox0.TabStop = false;
            this.pictureBox0.Visible = false;
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
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 39);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(446, 577);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
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
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(500, 11);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(292, 665);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(804, 688);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnQuarter);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnLockBits);
            this.Controls.Add(this.btnNoLockBits);
            this.Controls.Add(this.pictureBox0);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing8";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.PictureBox pictureBox0;
        internal System.Windows.Forms.Button btnReset;
        internal System.Windows.Forms.Button btnLockBits;
        internal System.Windows.Forms.Button btnNoLockBits;
        internal System.Windows.Forms.PictureBox pictureBox1;
        internal System.Windows.Forms.Button btnQuarter;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

