namespace Main
{
    partial class aboutForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(aboutForm));
            this.lbAbout = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.lbContact = new System.Windows.Forms.LinkLabel();
            this.SuspendLayout();
            // 
            // lbAbout
            // 
            this.lbAbout.AutoSize = true;
            this.lbAbout.Location = new System.Drawing.Point(12, 24);
            this.lbAbout.Name = "lbAbout";
            this.lbAbout.Size = new System.Drawing.Size(41, 12);
            this.lbAbout.TabIndex = 0;
            this.lbAbout.Text = "label1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(242, 81);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(59, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "Coded By:";
            // 
            // lbContact
            // 
            this.lbContact.AutoSize = true;
            this.lbContact.Location = new System.Drawing.Point(308, 81);
            this.lbContact.Name = "lbContact";
            this.lbContact.Size = new System.Drawing.Size(41, 12);
            this.lbContact.TabIndex = 2;
            this.lbContact.TabStop = true;
            this.lbContact.Text = "Lawson";
            this.lbContact.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.lbContact_LinkClicked);
            // 
            // aboutForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(404, 103);
            this.Controls.Add(this.lbContact);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lbAbout);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "aboutForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "¹ØÓÚ";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.aboutForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lbAbout;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.LinkLabel lbContact;

    }
}