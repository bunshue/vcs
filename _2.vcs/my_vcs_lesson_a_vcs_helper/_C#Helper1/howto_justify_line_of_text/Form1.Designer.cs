namespace howto_justify_line_of_text
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
            this.pictureBox_justify1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_justify1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox_justify1
            // 
            this.pictureBox_justify1.BackColor = System.Drawing.Color.White;
            this.pictureBox_justify1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_justify1.Location = new System.Drawing.Point(12, 11);
            this.pictureBox_justify1.Name = "pictureBox_justify1";
            this.pictureBox_justify1.Size = new System.Drawing.Size(450, 140);
            this.pictureBox_justify1.TabIndex = 1;
            this.pictureBox_justify1.TabStop = false;
            this.pictureBox_justify1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_justify1_Paint);
            this.pictureBox_justify1.Resize += new System.EventHandler(this.pictureBox_justify1_Resize);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(573, 229);
            this.Controls.Add(this.pictureBox_justify1);
            this.Name = "Form1";
            this.Text = "howto_justify_line_of_text";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_justify1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox_justify1;
    }
}

