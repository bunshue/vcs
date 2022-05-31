namespace vcs_PictureCrop4
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
            this.picSource = new System.Windows.Forms.PictureBox();
            this.picArea = new System.Windows.Forms.PictureBox();
            this.picWithoutArea = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWithoutArea)).BeginInit();
            this.SuspendLayout();
            // 
            // picSource
            // 
            this.picSource.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSource.Location = new System.Drawing.Point(12, 41);
            this.picSource.Name = "picSource";
            this.picSource.Size = new System.Drawing.Size(100, 100);
            this.picSource.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSource.TabIndex = 10;
            this.picSource.TabStop = false;
            this.picSource.Visible = false;
            this.picSource.Paint += new System.Windows.Forms.PaintEventHandler(this.picSource_Paint);
            this.picSource.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseDown);
            this.picSource.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseMove);
            this.picSource.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picSource_MouseUp);
            // 
            // picArea
            // 
            this.picArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picArea.Location = new System.Drawing.Point(118, 41);
            this.picArea.Name = "picArea";
            this.picArea.Size = new System.Drawing.Size(100, 100);
            this.picArea.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picArea.TabIndex = 12;
            this.picArea.TabStop = false;
            this.picArea.Visible = false;
            // 
            // picWithoutArea
            // 
            this.picWithoutArea.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picWithoutArea.Location = new System.Drawing.Point(224, 41);
            this.picWithoutArea.Name = "picWithoutArea";
            this.picWithoutArea.Size = new System.Drawing.Size(100, 100);
            this.picWithoutArea.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picWithoutArea.TabIndex = 13;
            this.picWithoutArea.TabStop = false;
            this.picWithoutArea.Visible = false;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(79, 23);
            this.button1.TabIndex = 14;
            this.button1.Text = "Open";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(109, 12);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(79, 23);
            this.button2.TabIndex = 15;
            this.button2.Text = "Save";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(935, 571);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.picWithoutArea);
            this.Controls.Add(this.picArea);
            this.Controls.Add(this.picSource);
            this.Name = "Form1";
            this.Text = "vcs_PictureCrop4";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picWithoutArea)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picSource;
        private System.Windows.Forms.PictureBox picArea;
        private System.Windows.Forms.PictureBox picWithoutArea;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
    }
}

