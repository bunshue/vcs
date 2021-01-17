namespace vcs_PictureCloseup2
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
            this.picHidden = new System.Windows.Forms.PictureBox();
            this.picMap = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picMap)).BeginInit();
            this.SuspendLayout();
            // 
            // picHidden
            // 
            this.picHidden.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picHidden.Image = global::vcs_PictureCloseup2.Properties.Resources.usmap;
            this.picHidden.Location = new System.Drawing.Point(222, 166);
            this.picHidden.Name = "picHidden";
            this.picHidden.Size = new System.Drawing.Size(1104, 708);
            this.picHidden.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHidden.TabIndex = 4;
            this.picHidden.TabStop = false;
            this.picHidden.Visible = false;
            // 
            // picMap
            // 
            this.picMap.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picMap.Cursor = System.Windows.Forms.Cursors.Cross;
            this.picMap.Image = global::vcs_PictureCloseup2.Properties.Resources.usmapsmall;
            this.picMap.Location = new System.Drawing.Point(11, 11);
            this.picMap.Name = "picMap";
            this.picMap.Size = new System.Drawing.Size(554, 356);
            this.picMap.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picMap.TabIndex = 5;
            this.picMap.TabStop = false;
            this.picMap.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picMap_MouseMove);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(743, 507);
            this.Controls.Add(this.picHidden);
            this.Controls.Add(this.picMap);
            this.Name = "Form1";
            this.Text = "vcs_PictureCloseup2";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picHidden)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picMap)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.PictureBox picHidden;
        internal System.Windows.Forms.PictureBox picMap;
    }
}

