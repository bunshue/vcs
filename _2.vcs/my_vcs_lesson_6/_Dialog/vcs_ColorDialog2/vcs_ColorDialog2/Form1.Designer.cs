namespace vcs_ColorDialog2
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
            this.btnFgColor = new System.Windows.Forms.Button();
            this.btnBgColor = new System.Windows.Forms.Button();
            this.dlgBgColor = new System.Windows.Forms.ColorDialog();
            this.dlgFgColor = new System.Windows.Forms.ColorDialog();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnFgColor
            // 
            this.btnFgColor.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnFgColor.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnFgColor.Location = new System.Drawing.Point(156, 12);
            this.btnFgColor.Name = "btnFgColor";
            this.btnFgColor.Size = new System.Drawing.Size(108, 23);
            this.btnFgColor.TabIndex = 1;
            this.btnFgColor.Text = "Foreground Color";
            this.btnFgColor.UseVisualStyleBackColor = true;
            this.btnFgColor.Click += new System.EventHandler(this.btnFgColor_Click);
            // 
            // btnBgColor
            // 
            this.btnBgColor.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnBgColor.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnBgColor.Location = new System.Drawing.Point(21, 12);
            this.btnBgColor.Name = "btnBgColor";
            this.btnBgColor.Size = new System.Drawing.Size(108, 23);
            this.btnBgColor.TabIndex = 0;
            this.btnBgColor.Text = "Background Color";
            this.btnBgColor.UseVisualStyleBackColor = true;
            this.btnBgColor.Click += new System.EventHandler(this.btnBgColor_Click);
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(18, 56);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(246, 79);
            this.label1.TabIndex = 2;
            this.label1.Text = "This example displays foreground and background color dialogs that contain custom" +
                " colors.";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 144);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnBgColor);
            this.Controls.Add(this.btnFgColor);
            this.Name = "Form1";
            this.Text = "vcs_ColorDialog2";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnFgColor;
        private System.Windows.Forms.Button btnBgColor;
        private System.Windows.Forms.ColorDialog dlgBgColor;
        private System.Windows.Forms.ColorDialog dlgFgColor;
        private System.Windows.Forms.Label label1;
    }
}

