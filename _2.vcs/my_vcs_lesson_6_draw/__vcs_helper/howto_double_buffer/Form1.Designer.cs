namespace howto_double_buffer
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
            this.chkDoubleBuffer = new System.Windows.Forms.CheckBox();
            this.btnRedraw = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // chkDoubleBuffer
            // 
            this.chkDoubleBuffer.AutoSize = true;
            this.chkDoubleBuffer.ForeColor = System.Drawing.Color.White;
            this.chkDoubleBuffer.Location = new System.Drawing.Point(12, 12);
            this.chkDoubleBuffer.Name = "chkDoubleBuffer";
            this.chkDoubleBuffer.Size = new System.Drawing.Size(91, 17);
            this.chkDoubleBuffer.TabIndex = 0;
            this.chkDoubleBuffer.Text = "Double Buffer";
            this.chkDoubleBuffer.UseVisualStyleBackColor = true;
            this.chkDoubleBuffer.CheckedChanged += new System.EventHandler(this.chkDoubleBuffer_CheckedChanged);
            // 
            // btnRedraw
            // 
            this.btnRedraw.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnRedraw.Location = new System.Drawing.Point(321, 12);
            this.btnRedraw.Name = "btnRedraw";
            this.btnRedraw.Size = new System.Drawing.Size(75, 23);
            this.btnRedraw.TabIndex = 1;
            this.btnRedraw.Text = "Redraw";
            this.btnRedraw.UseVisualStyleBackColor = true;
            this.btnRedraw.Click += new System.EventHandler(this.btnRedraw_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnRedraw;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(408, 341);
            this.Controls.Add(this.btnRedraw);
            this.Controls.Add(this.chkDoubleBuffer);
            this.Name = "Form1";
            this.Text = "howto_double_buffer";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox chkDoubleBuffer;
        private System.Windows.Forms.Button btnRedraw;

    }
}

