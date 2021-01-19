namespace howto_fill_shape_with_random_lines
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
            this.chkAntiAlias = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // chkAntiAlias
            // 
            this.chkAntiAlias.AutoSize = true;
            this.chkAntiAlias.Location = new System.Drawing.Point(0, 0);
            this.chkAntiAlias.Name = "chkAntiAlias";
            this.chkAntiAlias.Size = new System.Drawing.Size(70, 16);
            this.chkAntiAlias.TabIndex = 0;
            this.chkAntiAlias.Text = "Anti Alias";
            this.chkAntiAlias.UseVisualStyleBackColor = true;
            this.chkAntiAlias.CheckedChanged += new System.EventHandler(this.chkAntiAlias_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(815, 472);
            this.Controls.Add(this.chkAntiAlias);
            this.Name = "Form1";
            this.Text = "howto_fill_shape_with_random_lines";
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseDown);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseMove);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseUp);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkAntiAlias;
    }
}

