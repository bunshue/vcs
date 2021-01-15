namespace howto_spiral_of_theodorus
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
            this.label1 = new System.Windows.Forms.Label();
            this.chkFill = new System.Windows.Forms.CheckBox();
            this.txtNumTriangles = new System.Windows.Forms.TextBox();
            this.btnDraw = new System.Windows.Forms.Button();
            this.picSpiral = new System.Windows.Forms.PictureBox();
            this.chkOutline = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.picSpiral)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(63, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "# Triangles:";
            // 
            // chkFill
            // 
            this.chkFill.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.chkFill.Checked = true;
            this.chkFill.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkFill.Location = new System.Drawing.Point(15, 61);
            this.chkFill.Name = "chkFill";
            this.chkFill.Size = new System.Drawing.Size(83, 17);
            this.chkFill.TabIndex = 2;
            this.chkFill.Text = "Fill";
            this.chkFill.UseVisualStyleBackColor = true;
            // 
            // txtNumTriangles
            // 
            this.txtNumTriangles.Location = new System.Drawing.Point(81, 12);
            this.txtNumTriangles.Name = "txtNumTriangles";
            this.txtNumTriangles.Size = new System.Drawing.Size(49, 20);
            this.txtNumTriangles.TabIndex = 0;
            this.txtNumTriangles.Text = "16";
            this.txtNumTriangles.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnDraw
            // 
            this.btnDraw.Location = new System.Drawing.Point(29, 95);
            this.btnDraw.Name = "btnDraw";
            this.btnDraw.Size = new System.Drawing.Size(75, 23);
            this.btnDraw.TabIndex = 3;
            this.btnDraw.Text = "Draw";
            this.btnDraw.UseVisualStyleBackColor = true;
            this.btnDraw.Click += new System.EventHandler(this.btnDraw_Click);
            // 
            // picSpiral
            // 
            this.picSpiral.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picSpiral.BackColor = System.Drawing.Color.White;
            this.picSpiral.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSpiral.Location = new System.Drawing.Point(136, 12);
            this.picSpiral.Name = "picSpiral";
            this.picSpiral.Size = new System.Drawing.Size(237, 237);
            this.picSpiral.TabIndex = 4;
            this.picSpiral.TabStop = false;
            // 
            // chkOutline
            // 
            this.chkOutline.CheckAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.chkOutline.Checked = true;
            this.chkOutline.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkOutline.Location = new System.Drawing.Point(15, 38);
            this.chkOutline.Name = "chkOutline";
            this.chkOutline.Size = new System.Drawing.Size(83, 17);
            this.chkOutline.TabIndex = 1;
            this.chkOutline.Text = "Outline";
            this.chkOutline.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnDraw;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(385, 261);
            this.Controls.Add(this.chkOutline);
            this.Controls.Add(this.picSpiral);
            this.Controls.Add(this.btnDraw);
            this.Controls.Add(this.txtNumTriangles);
            this.Controls.Add(this.chkFill);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_spiral_of_theodorus";
            ((System.ComponentModel.ISupportInitialize)(this.picSpiral)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.CheckBox chkFill;
        private System.Windows.Forms.TextBox txtNumTriangles;
        private System.Windows.Forms.Button btnDraw;
        private System.Windows.Forms.PictureBox picSpiral;
        private System.Windows.Forms.CheckBox chkOutline;
    }
}

