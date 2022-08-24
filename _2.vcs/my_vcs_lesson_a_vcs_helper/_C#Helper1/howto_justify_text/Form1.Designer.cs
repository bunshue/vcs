namespace howto_justify_text
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.pictureBox_justify2 = new System.Windows.Forms.PictureBox();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.chkLeft = new System.Windows.Forms.ToolStripButton();
            this.chkCenter = new System.Windows.Forms.ToolStripButton();
            this.chkRight = new System.Windows.Forms.ToolStripButton();
            this.chkFull = new System.Windows.Forms.ToolStripButton();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_justify2)).BeginInit();
            this.toolStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox_justify2
            // 
            this.pictureBox_justify2.BackColor = System.Drawing.Color.White;
            this.pictureBox_justify2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox_justify2.Location = new System.Drawing.Point(12, 26);
            this.pictureBox_justify2.Name = "pictureBox_justify2";
            this.pictureBox_justify2.Size = new System.Drawing.Size(450, 448);
            this.pictureBox_justify2.TabIndex = 0;
            this.pictureBox_justify2.TabStop = false;
            this.pictureBox_justify2.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox_justify2_Paint);
            this.pictureBox_justify2.Resize += new System.EventHandler(this.pictureBox_justify2_Resize);
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.chkLeft,
            this.chkCenter,
            this.chkRight,
            this.chkFull});
            this.toolStrip1.Location = new System.Drawing.Point(0, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(706, 25);
            this.toolStrip1.TabIndex = 1;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // chkLeft
            // 
            this.chkLeft.Checked = true;
            this.chkLeft.CheckOnClick = true;
            this.chkLeft.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkLeft.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.chkLeft.Image = ((System.Drawing.Image)(resources.GetObject("chkLeft.Image")));
            this.chkLeft.ImageTransparentColor = System.Drawing.Color.Red;
            this.chkLeft.Name = "chkLeft";
            this.chkLeft.Size = new System.Drawing.Size(23, 22);
            this.chkLeft.Text = "toolStripButton1";
            this.chkLeft.Click += new System.EventHandler(this.chkAlignment_Click);
            // 
            // chkCenter
            // 
            this.chkCenter.CheckOnClick = true;
            this.chkCenter.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.chkCenter.Image = ((System.Drawing.Image)(resources.GetObject("chkCenter.Image")));
            this.chkCenter.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.chkCenter.Name = "chkCenter";
            this.chkCenter.Size = new System.Drawing.Size(23, 22);
            this.chkCenter.Text = "toolStripButton2";
            this.chkCenter.Click += new System.EventHandler(this.chkAlignment_Click);
            // 
            // chkRight
            // 
            this.chkRight.CheckOnClick = true;
            this.chkRight.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.chkRight.Image = ((System.Drawing.Image)(resources.GetObject("chkRight.Image")));
            this.chkRight.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.chkRight.Name = "chkRight";
            this.chkRight.Size = new System.Drawing.Size(23, 22);
            this.chkRight.Text = "toolStripButton3";
            this.chkRight.Click += new System.EventHandler(this.chkAlignment_Click);
            // 
            // chkFull
            // 
            this.chkFull.CheckOnClick = true;
            this.chkFull.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.chkFull.Image = ((System.Drawing.Image)(resources.GetObject("chkFull.Image")));
            this.chkFull.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.chkFull.Name = "chkFull";
            this.chkFull.Size = new System.Drawing.Size(23, 22);
            this.chkFull.Text = "toolStripButton4";
            this.chkFull.Click += new System.EventHandler(this.chkAlignment_Click);
            // 
            // button1
            // 
            this.button1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button1.BackgroundImage")));
            this.button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.button1.Location = new System.Drawing.Point(513, 67);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(23, 22);
            this.button1.TabIndex = 2;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.Button_Alignment_Click);
            // 
            // button2
            // 
            this.button2.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button2.BackgroundImage")));
            this.button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.button2.Location = new System.Drawing.Point(542, 67);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(23, 22);
            this.button2.TabIndex = 3;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.Button_Alignment_Click);
            // 
            // button3
            // 
            this.button3.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button3.BackgroundImage")));
            this.button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.button3.Location = new System.Drawing.Point(571, 67);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(23, 22);
            this.button3.TabIndex = 4;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.Button_Alignment_Click);
            // 
            // button4
            // 
            this.button4.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("button4.BackgroundImage")));
            this.button4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            this.button4.Location = new System.Drawing.Point(600, 67);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(23, 22);
            this.button4.TabIndex = 5;
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.Button_Alignment_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(706, 562);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.pictureBox_justify2);
            this.Name = "Form1";
            this.Text = "howto_justify_text";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_justify2)).EndInit();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox_justify2;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton chkLeft;
        private System.Windows.Forms.ToolStripButton chkCenter;
        private System.Windows.Forms.ToolStripButton chkRight;
        private System.Windows.Forms.ToolStripButton chkFull;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
    }
}

