namespace howto_outline_graphics
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
            this.txtMinRadius = new System.Windows.Forms.TextBox();
            this.btnGo = new System.Windows.Forms.Button();
            this.txtMaxRadius = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.picGraphics = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picGraphics)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(140, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "Min Radius 字的近距 白色:";
            // 
            // txtMinRadius
            // 
            this.txtMinRadius.Location = new System.Drawing.Point(158, 13);
            this.txtMinRadius.Name = "txtMinRadius";
            this.txtMinRadius.Size = new System.Drawing.Size(61, 22);
            this.txtMinRadius.TabIndex = 0;
            this.txtMinRadius.Text = "5";
            this.txtMinRadius.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnGo
            // 
            this.btnGo.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnGo.Location = new System.Drawing.Point(235, 27);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(75, 25);
            this.btnGo.TabIndex = 2;
            this.btnGo.Text = "Go";
            this.btnGo.UseVisualStyleBackColor = true;
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // txtMaxRadius
            // 
            this.txtMaxRadius.Location = new System.Drawing.Point(158, 37);
            this.txtMaxRadius.Name = "txtMaxRadius";
            this.txtMaxRadius.Size = new System.Drawing.Size(61, 22);
            this.txtMaxRadius.TabIndex = 1;
            this.txtMaxRadius.Text = "10";
            this.txtMaxRadius.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 40);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(145, 12);
            this.label2.TabIndex = 4;
            this.label2.Text = "Max Radius 字的遠距 紅色::";
            // 
            // picGraphics
            // 
            this.picGraphics.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picGraphics.BackColor = System.Drawing.Color.White;
            this.picGraphics.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picGraphics.Location = new System.Drawing.Point(12, 61);
            this.picGraphics.Name = "picGraphics";
            this.picGraphics.Size = new System.Drawing.Size(534, 233);
            this.picGraphics.TabIndex = 0;
            this.picGraphics.TabStop = false;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGo;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(687, 432);
            this.Controls.Add(this.txtMaxRadius);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.txtMinRadius);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picGraphics);
            this.Name = "Form1";
            this.Text = "howto_outline_graphics";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picGraphics)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picGraphics;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtMinRadius;
        private System.Windows.Forms.Button btnGo;
        private System.Windows.Forms.TextBox txtMaxRadius;
        private System.Windows.Forms.Label label2;
    }
}

