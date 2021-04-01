namespace ButtonApplication
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
            this.Button2 = new System.Windows.Forms.Button();
            this.Button1 = new System.Windows.Forms.Button();
            this.TextBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // Button2
            // 
            this.Button2.Location = new System.Drawing.Point(42, 88);
            this.Button2.Name = "Button2";
            this.Button2.Size = new System.Drawing.Size(108, 28);
            this.Button2.TabIndex = 2;
            this.Button2.Text = "Button2";
            this.Button2.Click += new System.EventHandler(this.Button2_Click);
            this.Button2.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Button2_MouseDown);
            this.Button2.MouseHover += new System.EventHandler(this.Button2_MouseHover);
            // 
            // Button1
            // 
            this.Button1.Location = new System.Drawing.Point(42, 52);
            this.Button1.Name = "Button1";
            this.Button1.Size = new System.Drawing.Size(108, 28);
            this.Button1.TabIndex = 1;
            this.Button1.Text = "Button1";
            this.Button1.Click += new System.EventHandler(this.Button1_Click);
            this.Button1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Button1_MouseDown);
            this.Button1.MouseHover += new System.EventHandler(this.Button1_MouseHover);
            // 
            // TextBox1
            // 
            this.TextBox1.Location = new System.Drawing.Point(20, 16);
            this.TextBox1.Name = "TextBox1";
            this.TextBox1.Size = new System.Drawing.Size(152, 22);
            this.TextBox1.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(192, 133);
            this.Controls.Add(this.Button2);
            this.Controls.Add(this.Button1);
            this.Controls.Add(this.TextBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Button Application";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Button Button2;
        internal System.Windows.Forms.Button Button1;
        internal System.Windows.Forms.TextBox TextBox1;
    }
}

