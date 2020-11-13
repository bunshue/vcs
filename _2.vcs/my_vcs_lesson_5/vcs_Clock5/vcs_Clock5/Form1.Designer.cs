namespace vcs_Clock5
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
            this.picClock = new System.Windows.Forms.PictureBox();
            this.tmrTick = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picClock)).BeginInit();
            this.SuspendLayout();
            // 
            // picClock
            // 
            this.picClock.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picClock.BackColor = System.Drawing.Color.White;
            this.picClock.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picClock.Location = new System.Drawing.Point(12, 11);
            this.picClock.Name = "picClock";
            this.picClock.Size = new System.Drawing.Size(653, 247);
            this.picClock.TabIndex = 0;
            this.picClock.TabStop = false;
            this.picClock.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            // 
            // tmrTick
            // 
            this.tmrTick.Enabled = true;
            this.tmrTick.Interval = 500;
            this.tmrTick.Tick += new System.EventHandler(this.tmrTick_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(677, 269);
            this.Controls.Add(this.picClock);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "Form1";
            this.Text = "vcs_Clock5";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picClock)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox picClock;
        private System.Windows.Forms.Timer tmrTick;
    }
}

