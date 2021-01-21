namespace vcs_PictureCloseup
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
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.label1 = new System.Windows.Forms.Label();
            this.panCloseup = new System.Windows.Forms.Panel();
            this.picCloseup = new System.Windows.Forms.PictureBox();
            this.picWhole = new System.Windows.Forms.PictureBox();
            this.panCloseup.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picCloseup)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWhole)).BeginInit();
            this.SuspendLayout();
            // 
            // linkLabel1
            // 
            this.linkLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkLabel1.LinkArea = new System.Windows.Forms.LinkArea(110, 28);
            this.linkLabel1.LinkBehavior = System.Windows.Forms.LinkBehavior.AlwaysUnderline;
            this.linkLabel1.Location = new System.Drawing.Point(12, 325);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(532, 42);
            this.linkLabel1.TabIndex = 2;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Text = "This is a picture of Saturn\'s moon Encaledus taken by the Casinni spacecraft. For" +
                " more information, visit the Astronomy Picture of the Day web site.";
            this.linkLabel1.UseCompatibleTextRendering = true;
            this.linkLabel1.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 293);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(394, 17);
            this.label1.TabIndex = 3;
            this.label1.Text = "Move the mouse over the picture on the left to see a closeup.";
            // 
            // panCloseup
            // 
            this.panCloseup.Controls.Add(this.picCloseup);
            this.panCloseup.Location = new System.Drawing.Point(268, 12);
            this.panCloseup.Name = "panCloseup";
            this.panCloseup.Size = new System.Drawing.Size(250, 250);
            this.panCloseup.TabIndex = 4;
            this.panCloseup.Visible = false;
            // 
            // picCloseup
            // 
            this.picCloseup.Location = new System.Drawing.Point(3, 3);
            this.picCloseup.Name = "picCloseup";
            this.picCloseup.Size = new System.Drawing.Size(189, 196);
            this.picCloseup.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picCloseup.TabIndex = 1;
            this.picCloseup.TabStop = false;
            // 
            // picWhole
            // 
            this.picWhole.Image = global::vcs_PictureCloseup.Properties.Resources.enceladus_cassini;
            this.picWhole.Location = new System.Drawing.Point(12, 12);
            this.picWhole.Name = "picWhole";
            this.picWhole.Size = new System.Drawing.Size(250, 250);
            this.picWhole.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.picWhole.TabIndex = 0;
            this.picWhole.TabStop = false;
            this.picWhole.MouseLeave += new System.EventHandler(this.picWhole_MouseLeave);
            this.picWhole.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picWhole_MouseMove);
            this.picWhole.Paint += new System.Windows.Forms.PaintEventHandler(this.picWhole_Paint);
            this.picWhole.MouseEnter += new System.EventHandler(this.picWhole_MouseEnter);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(558, 374);
            this.Controls.Add(this.panCloseup);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.linkLabel1);
            this.Controls.Add(this.picWhole);
            this.Name = "Form1";
            this.Text = "vcs_PictureCloseup";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panCloseup.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.picCloseup)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWhole)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picWhole;
        private System.Windows.Forms.PictureBox picCloseup;
        private System.Windows.Forms.LinkLabel linkLabel1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panCloseup;
    }
}

