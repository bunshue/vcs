namespace vcs_PictureDownload
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
            this.picApotd = new System.Windows.Forms.PictureBox();
            this.wbrApotd = new System.Windows.Forms.WebBrowser();
            ((System.ComponentModel.ISupportInitialize)(this.picApotd)).BeginInit();
            this.SuspendLayout();
            // 
            // picApotd
            // 
            this.picApotd.Dock = System.Windows.Forms.DockStyle.Fill;
            this.picApotd.Location = new System.Drawing.Point(0, 0);
            this.picApotd.Name = "picApotd";
            this.picApotd.Size = new System.Drawing.Size(477, 592);
            this.picApotd.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picApotd.TabIndex = 4;
            this.picApotd.TabStop = false;
            // 
            // wbrApotd
            // 
            this.wbrApotd.Location = new System.Drawing.Point(24, 24);
            this.wbrApotd.MinimumSize = new System.Drawing.Size(20, 18);
            this.wbrApotd.Name = "wbrApotd";
            this.wbrApotd.Size = new System.Drawing.Size(122, 96);
            this.wbrApotd.TabIndex = 5;
            this.wbrApotd.DocumentCompleted += new System.Windows.Forms.WebBrowserDocumentCompletedEventHandler(this.wbrApotd_DocumentCompleted);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(477, 592);
            this.Controls.Add(this.wbrApotd);
            this.Controls.Add(this.picApotd);
            this.Name = "Form1";
            this.Text = "vcs_PictureDownload";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picApotd)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox picApotd;
        private System.Windows.Forms.WebBrowser wbrApotd;
    }
}

