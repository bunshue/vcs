namespace howto_plot_level_curves
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
            this.radF4 = new System.Windows.Forms.RadioButton();
            this.radF3 = new System.Windows.Forms.RadioButton();
            this.radF2 = new System.Windows.Forms.RadioButton();
            this.radF1 = new System.Windows.Forms.RadioButton();
            this.picGraph = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).BeginInit();
            this.SuspendLayout();
            // 
            // radF4
            // 
            this.radF4.AutoSize = true;
            this.radF4.Location = new System.Drawing.Point(12, 81);
            this.radF4.Name = "radF4";
            this.radF4.Size = new System.Drawing.Size(185, 17);
            this.radF4.TabIndex = 17;
            this.radF4.TabStop = true;
            this.radF4.Text = "Hemisphere: Sqrt(25 - (x^2 + y^2))";
            this.radF4.UseVisualStyleBackColor = true;
            this.radF4.Click += new System.EventHandler(this.radF4_Click);
            // 
            // radF3
            // 
            this.radF3.AutoSize = true;
            this.radF3.Location = new System.Drawing.Point(12, 58);
            this.radF3.Name = "radF3";
            this.radF3.Size = new System.Drawing.Size(146, 17);
            this.radF3.TabIndex = 16;
            this.radF3.TabStop = true;
            this.radF3.Text = "Crossed trough: x^2 * y^2";
            this.radF3.UseVisualStyleBackColor = true;
            this.radF3.Click += new System.EventHandler(this.radF3_Click);
            // 
            // radF2
            // 
            this.radF2.AutoSize = true;
            this.radF2.Location = new System.Drawing.Point(12, 35);
            this.radF2.Name = "radF2";
            this.radF2.Size = new System.Drawing.Size(183, 17);
            this.radF2.TabIndex = 15;
            this.radF2.TabStop = true;
            this.radF2.Text = "Monkey saddle: x * (x^2 - 3 * y^2)";
            this.radF2.UseVisualStyleBackColor = true;
            this.radF2.Click += new System.EventHandler(this.radF2_Click);
            // 
            // radF1
            // 
            this.radF1.AutoSize = true;
            this.radF1.Location = new System.Drawing.Point(12, 12);
            this.radF1.Name = "radF1";
            this.radF1.Size = new System.Drawing.Size(154, 17);
            this.radF1.TabIndex = 14;
            this.radF1.TabStop = true;
            this.radF1.Text = "Bowl: z = x^2 + (y*2)^2 - 75";
            this.radF1.UseVisualStyleBackColor = true;
            this.radF1.Click += new System.EventHandler(this.radF1_Click);
            // 
            // picGraph
            // 
            this.picGraph.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraph.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraph.Location = new System.Drawing.Point(219, 12);
            this.picGraph.Name = "picGraph";
            this.picGraph.Size = new System.Drawing.Size(260, 260);
            this.picGraph.TabIndex = 13;
            this.picGraph.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(491, 284);
            this.Controls.Add(this.radF4);
            this.Controls.Add(this.radF3);
            this.Controls.Add(this.radF2);
            this.Controls.Add(this.radF1);
            this.Controls.Add(this.picGraph);
            this.Name = "Form1";
            this.Text = "howto_plot_level_curves";
            ((System.ComponentModel.ISupportInitialize)(this.picGraph)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton radF4;
        private System.Windows.Forms.RadioButton radF3;
        private System.Windows.Forms.RadioButton radF2;
        private System.Windows.Forms.RadioButton radF1;
        private System.Windows.Forms.PictureBox picGraph;

    }
}

