namespace vcs_ComboBox2
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
            this.lstTimeZones = new System.Windows.Forms.ListBox();
            this.cboTimeZones = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // lstTimeZones
            // 
            this.lstTimeZones.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.lstTimeZones.FormattingEnabled = true;
            this.lstTimeZones.IntegralHeight = false;
            this.lstTimeZones.Location = new System.Drawing.Point(12, 39);
            this.lstTimeZones.Name = "lstTimeZones";
            this.lstTimeZones.Size = new System.Drawing.Size(308, 118);
            this.lstTimeZones.TabIndex = 0;
            // 
            // cboTimeZones
            // 
            this.cboTimeZones.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.cboTimeZones.FormattingEnabled = true;
            this.cboTimeZones.Location = new System.Drawing.Point(12, 12);
            this.cboTimeZones.Name = "cboTimeZones";
            this.cboTimeZones.Size = new System.Drawing.Size(309, 21);
            this.cboTimeZones.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(333, 169);
            this.Controls.Add(this.cboTimeZones);
            this.Controls.Add(this.lstTimeZones);
            this.Name = "Form1";
            this.Text = "vcs_ComboBox2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lstTimeZones;
        private System.Windows.Forms.ComboBox cboTimeZones;
    }
}

