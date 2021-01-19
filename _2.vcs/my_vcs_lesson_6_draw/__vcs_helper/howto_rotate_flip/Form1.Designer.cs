namespace howto_rotate_flip
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.rad180FlipNone = new System.Windows.Forms.RadioButton();
            this.rad180FlipX = new System.Windows.Forms.RadioButton();
            this.rad180FlipY = new System.Windows.Forms.RadioButton();
            this.rad180FlipXY = new System.Windows.Forms.RadioButton();
            this.rad270FlipY = new System.Windows.Forms.RadioButton();
            this.rad270FlipXY = new System.Windows.Forms.RadioButton();
            this.rad270FlipX = new System.Windows.Forms.RadioButton();
            this.rad270FlipNone = new System.Windows.Forms.RadioButton();
            this.radNoneFlipY = new System.Windows.Forms.RadioButton();
            this.radNoneFlipXY = new System.Windows.Forms.RadioButton();
            this.radNoneFlipX = new System.Windows.Forms.RadioButton();
            this.radNoneFlipNone = new System.Windows.Forms.RadioButton();
            this.rad90FlipY = new System.Windows.Forms.RadioButton();
            this.rad90FlipXY = new System.Windows.Forms.RadioButton();
            this.rad90FlipX = new System.Windows.Forms.RadioButton();
            this.rad90FlipNone = new System.Windows.Forms.RadioButton();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::howto_rotate_flip.Properties.Resources.picture1;
            this.pictureBox1.Location = new System.Drawing.Point(143, 11);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(305, 400);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(449, 11);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 50);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 1;
            this.pictureBox2.TabStop = false;
            // 
            // rad180FlipNone
            // 
            this.rad180FlipNone.AutoSize = true;
            this.rad180FlipNone.Location = new System.Drawing.Point(12, 11);
            this.rad180FlipNone.Name = "rad180FlipNone";
            this.rad180FlipNone.Size = new System.Drawing.Size(114, 16);
            this.rad180FlipNone.TabIndex = 2;
            this.rad180FlipNone.TabStop = true;
            this.rad180FlipNone.Text = "Rotate180FlipNone";
            this.rad180FlipNone.UseVisualStyleBackColor = true;
            this.rad180FlipNone.CheckedChanged += new System.EventHandler(this.rad180FlipNone_CheckedChanged);
            // 
            // rad180FlipX
            // 
            this.rad180FlipX.AutoSize = true;
            this.rad180FlipX.Location = new System.Drawing.Point(12, 32);
            this.rad180FlipX.Name = "rad180FlipX";
            this.rad180FlipX.Size = new System.Drawing.Size(97, 16);
            this.rad180FlipX.TabIndex = 3;
            this.rad180FlipX.TabStop = true;
            this.rad180FlipX.Text = "Rotate180FlipX";
            this.rad180FlipX.UseVisualStyleBackColor = true;
            this.rad180FlipX.CheckedChanged += new System.EventHandler(this.rad180FlipX_CheckedChanged);
            // 
            // rad180FlipY
            // 
            this.rad180FlipY.AutoSize = true;
            this.rad180FlipY.Location = new System.Drawing.Point(12, 75);
            this.rad180FlipY.Name = "rad180FlipY";
            this.rad180FlipY.Size = new System.Drawing.Size(97, 16);
            this.rad180FlipY.TabIndex = 5;
            this.rad180FlipY.TabStop = true;
            this.rad180FlipY.Text = "Rotate180FlipY";
            this.rad180FlipY.UseVisualStyleBackColor = true;
            this.rad180FlipY.CheckedChanged += new System.EventHandler(this.rad180FlipY_CheckedChanged);
            // 
            // rad180FlipXY
            // 
            this.rad180FlipXY.AutoSize = true;
            this.rad180FlipXY.Location = new System.Drawing.Point(12, 54);
            this.rad180FlipXY.Name = "rad180FlipXY";
            this.rad180FlipXY.Size = new System.Drawing.Size(105, 16);
            this.rad180FlipXY.TabIndex = 4;
            this.rad180FlipXY.TabStop = true;
            this.rad180FlipXY.Text = "Rotate180FlipXY";
            this.rad180FlipXY.UseVisualStyleBackColor = true;
            this.rad180FlipXY.CheckedChanged += new System.EventHandler(this.rad180FlipXY_CheckedChanged);
            // 
            // rad270FlipY
            // 
            this.rad270FlipY.AutoSize = true;
            this.rad270FlipY.Location = new System.Drawing.Point(12, 160);
            this.rad270FlipY.Name = "rad270FlipY";
            this.rad270FlipY.Size = new System.Drawing.Size(97, 16);
            this.rad270FlipY.TabIndex = 9;
            this.rad270FlipY.TabStop = true;
            this.rad270FlipY.Text = "Rotate270FlipY";
            this.rad270FlipY.UseVisualStyleBackColor = true;
            this.rad270FlipY.CheckedChanged += new System.EventHandler(this.rad270FlipY_CheckedChanged);
            // 
            // rad270FlipXY
            // 
            this.rad270FlipXY.AutoSize = true;
            this.rad270FlipXY.Location = new System.Drawing.Point(12, 138);
            this.rad270FlipXY.Name = "rad270FlipXY";
            this.rad270FlipXY.Size = new System.Drawing.Size(105, 16);
            this.rad270FlipXY.TabIndex = 8;
            this.rad270FlipXY.TabStop = true;
            this.rad270FlipXY.Text = "Rotate270FlipXY";
            this.rad270FlipXY.UseVisualStyleBackColor = true;
            this.rad270FlipXY.CheckedChanged += new System.EventHandler(this.rad270FlipXY_CheckedChanged);
            // 
            // rad270FlipX
            // 
            this.rad270FlipX.AutoSize = true;
            this.rad270FlipX.Location = new System.Drawing.Point(12, 117);
            this.rad270FlipX.Name = "rad270FlipX";
            this.rad270FlipX.Size = new System.Drawing.Size(97, 16);
            this.rad270FlipX.TabIndex = 7;
            this.rad270FlipX.TabStop = true;
            this.rad270FlipX.Text = "Rotate270FlipX";
            this.rad270FlipX.UseVisualStyleBackColor = true;
            this.rad270FlipX.CheckedChanged += new System.EventHandler(this.rad270FlipX_CheckedChanged);
            // 
            // rad270FlipNone
            // 
            this.rad270FlipNone.AutoSize = true;
            this.rad270FlipNone.Location = new System.Drawing.Point(12, 96);
            this.rad270FlipNone.Name = "rad270FlipNone";
            this.rad270FlipNone.Size = new System.Drawing.Size(114, 16);
            this.rad270FlipNone.TabIndex = 6;
            this.rad270FlipNone.TabStop = true;
            this.rad270FlipNone.Text = "Rotate270FlipNone";
            this.rad270FlipNone.UseVisualStyleBackColor = true;
            this.rad270FlipNone.CheckedChanged += new System.EventHandler(this.rad270FlipNone_CheckedChanged);
            // 
            // radNoneFlipY
            // 
            this.radNoneFlipY.AutoSize = true;
            this.radNoneFlipY.Location = new System.Drawing.Point(12, 330);
            this.radNoneFlipY.Name = "radNoneFlipY";
            this.radNoneFlipY.Size = new System.Drawing.Size(104, 16);
            this.radNoneFlipY.TabIndex = 17;
            this.radNoneFlipY.TabStop = true;
            this.radNoneFlipY.Text = "RotateNoneFlipY";
            this.radNoneFlipY.UseVisualStyleBackColor = true;
            this.radNoneFlipY.CheckedChanged += new System.EventHandler(this.radNoneFlipY_CheckedChanged);
            // 
            // radNoneFlipXY
            // 
            this.radNoneFlipXY.AutoSize = true;
            this.radNoneFlipXY.Location = new System.Drawing.Point(12, 308);
            this.radNoneFlipXY.Name = "radNoneFlipXY";
            this.radNoneFlipXY.Size = new System.Drawing.Size(112, 16);
            this.radNoneFlipXY.TabIndex = 16;
            this.radNoneFlipXY.TabStop = true;
            this.radNoneFlipXY.Text = "RotateNoneFlipXY";
            this.radNoneFlipXY.UseVisualStyleBackColor = true;
            this.radNoneFlipXY.CheckedChanged += new System.EventHandler(this.radNoneFlipXY_CheckedChanged);
            // 
            // radNoneFlipX
            // 
            this.radNoneFlipX.AutoSize = true;
            this.radNoneFlipX.Location = new System.Drawing.Point(12, 287);
            this.radNoneFlipX.Name = "radNoneFlipX";
            this.radNoneFlipX.Size = new System.Drawing.Size(104, 16);
            this.radNoneFlipX.TabIndex = 15;
            this.radNoneFlipX.TabStop = true;
            this.radNoneFlipX.Text = "RotateNoneFlipX";
            this.radNoneFlipX.UseVisualStyleBackColor = true;
            this.radNoneFlipX.CheckedChanged += new System.EventHandler(this.radNoneFlipX_CheckedChanged);
            // 
            // radNoneFlipNone
            // 
            this.radNoneFlipNone.AutoSize = true;
            this.radNoneFlipNone.Location = new System.Drawing.Point(12, 266);
            this.radNoneFlipNone.Name = "radNoneFlipNone";
            this.radNoneFlipNone.Size = new System.Drawing.Size(121, 16);
            this.radNoneFlipNone.TabIndex = 14;
            this.radNoneFlipNone.TabStop = true;
            this.radNoneFlipNone.Text = "RotateNoneFlipNone";
            this.radNoneFlipNone.UseVisualStyleBackColor = true;
            this.radNoneFlipNone.CheckedChanged += new System.EventHandler(this.radNoneFlipNone_CheckedChanged);
            // 
            // rad90FlipY
            // 
            this.rad90FlipY.AutoSize = true;
            this.rad90FlipY.Location = new System.Drawing.Point(12, 245);
            this.rad90FlipY.Name = "rad90FlipY";
            this.rad90FlipY.Size = new System.Drawing.Size(91, 16);
            this.rad90FlipY.TabIndex = 13;
            this.rad90FlipY.TabStop = true;
            this.rad90FlipY.Text = "Rotate90FlipY";
            this.rad90FlipY.UseVisualStyleBackColor = true;
            this.rad90FlipY.CheckedChanged += new System.EventHandler(this.rad90FlipY_CheckedChanged);
            // 
            // rad90FlipXY
            // 
            this.rad90FlipXY.AutoSize = true;
            this.rad90FlipXY.Location = new System.Drawing.Point(12, 223);
            this.rad90FlipXY.Name = "rad90FlipXY";
            this.rad90FlipXY.Size = new System.Drawing.Size(99, 16);
            this.rad90FlipXY.TabIndex = 12;
            this.rad90FlipXY.TabStop = true;
            this.rad90FlipXY.Text = "Rotate90FlipXY";
            this.rad90FlipXY.UseVisualStyleBackColor = true;
            this.rad90FlipXY.CheckedChanged += new System.EventHandler(this.rad90FlipXY_CheckedChanged);
            // 
            // rad90FlipX
            // 
            this.rad90FlipX.AutoSize = true;
            this.rad90FlipX.Location = new System.Drawing.Point(12, 202);
            this.rad90FlipX.Name = "rad90FlipX";
            this.rad90FlipX.Size = new System.Drawing.Size(91, 16);
            this.rad90FlipX.TabIndex = 11;
            this.rad90FlipX.TabStop = true;
            this.rad90FlipX.Text = "Rotate90FlipX";
            this.rad90FlipX.UseVisualStyleBackColor = true;
            this.rad90FlipX.CheckedChanged += new System.EventHandler(this.rad90FlipX_CheckedChanged);
            // 
            // rad90FlipNone
            // 
            this.rad90FlipNone.AutoSize = true;
            this.rad90FlipNone.Location = new System.Drawing.Point(12, 181);
            this.rad90FlipNone.Name = "rad90FlipNone";
            this.rad90FlipNone.Size = new System.Drawing.Size(108, 16);
            this.rad90FlipNone.TabIndex = 10;
            this.rad90FlipNone.TabStop = true;
            this.rad90FlipNone.Text = "Rotate90FlipNone";
            this.rad90FlipNone.UseVisualStyleBackColor = true;
            this.rad90FlipNone.CheckedChanged += new System.EventHandler(this.rad90FlipNone_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1009, 538);
            this.Controls.Add(this.radNoneFlipY);
            this.Controls.Add(this.radNoneFlipXY);
            this.Controls.Add(this.radNoneFlipX);
            this.Controls.Add(this.radNoneFlipNone);
            this.Controls.Add(this.rad90FlipY);
            this.Controls.Add(this.rad90FlipXY);
            this.Controls.Add(this.rad90FlipX);
            this.Controls.Add(this.rad90FlipNone);
            this.Controls.Add(this.rad270FlipY);
            this.Controls.Add(this.rad270FlipXY);
            this.Controls.Add(this.rad270FlipX);
            this.Controls.Add(this.rad270FlipNone);
            this.Controls.Add(this.rad180FlipY);
            this.Controls.Add(this.rad180FlipXY);
            this.Controls.Add(this.rad180FlipX);
            this.Controls.Add(this.rad180FlipNone);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "howto_rotate_flip";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.RadioButton rad180FlipNone;
        private System.Windows.Forms.RadioButton rad180FlipX;
        private System.Windows.Forms.RadioButton rad180FlipY;
        private System.Windows.Forms.RadioButton rad180FlipXY;
        private System.Windows.Forms.RadioButton rad270FlipY;
        private System.Windows.Forms.RadioButton rad270FlipXY;
        private System.Windows.Forms.RadioButton rad270FlipX;
        private System.Windows.Forms.RadioButton rad270FlipNone;
        private System.Windows.Forms.RadioButton radNoneFlipY;
        private System.Windows.Forms.RadioButton radNoneFlipXY;
        private System.Windows.Forms.RadioButton radNoneFlipX;
        private System.Windows.Forms.RadioButton radNoneFlipNone;
        private System.Windows.Forms.RadioButton rad90FlipY;
        private System.Windows.Forms.RadioButton rad90FlipXY;
        private System.Windows.Forms.RadioButton rad90FlipX;
        private System.Windows.Forms.RadioButton rad90FlipNone;
    }
}

