namespace FacialMouseControl
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
            ReleaseData();
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
            this.components = new System.ComponentModel.Container();
            this.flipHorizontalButton = new System.Windows.Forms.Button();
            this.imageBox1 = new Emgu.CV.UI.ImageBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // flipHorizontalButton
            // 
            this.flipHorizontalButton.Location = new System.Drawing.Point(670, 12);
            this.flipHorizontalButton.Name = "flipHorizontalButton";
            this.flipHorizontalButton.Size = new System.Drawing.Size(130, 21);
            this.flipHorizontalButton.TabIndex = 0;
            this.flipHorizontalButton.Text = "Flip Horizontal";
            this.flipHorizontalButton.UseVisualStyleBackColor = true;
            this.flipHorizontalButton.Click += new System.EventHandler(this.flipHorizontalButton_Click);
            // 
            // imageBox1
            // 
            this.imageBox1.Location = new System.Drawing.Point(12, 12);
            this.imageBox1.Name = "imageBox1";
            this.imageBox1.Size = new System.Drawing.Size(640, 480);
            this.imageBox1.TabIndex = 1;
            this.imageBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(670, 50);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(256, 442);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(938, 512);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.flipHorizontalButton);
            this.Controls.Add(this.imageBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.imageBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button flipHorizontalButton;
        private Emgu.CV.UI.ImageBox imageBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

