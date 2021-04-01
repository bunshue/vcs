namespace ServerSocket
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
            this.Button1 = new System.Windows.Forms.Button();
            this.ListBox1 = new System.Windows.Forms.ListBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Button1
            // 
            this.Button1.Location = new System.Drawing.Point(84, 196);
            this.Button1.Name = "Button1";
            this.Button1.Size = new System.Drawing.Size(88, 29);
            this.Button1.TabIndex = 1;
            this.Button1.Text = "Start";
            this.Button1.Click += new System.EventHandler(this.Button1_Click);
            // 
            // ListBox1
            // 
            this.ListBox1.ItemHeight = 12;
            this.ListBox1.Location = new System.Drawing.Point(12, 29);
            this.ListBox1.Name = "ListBox1";
            this.ListBox1.Size = new System.Drawing.Size(232, 148);
            this.ListBox1.TabIndex = 0;
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(12, 13);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(80, 16);
            this.Label1.TabIndex = 6;
            this.Label1.Text = "Server Log:";
            // 
            // Form1
            // 
            this.AcceptButton = this.Button1;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(256, 237);
            this.Controls.Add(this.Button1);
            this.Controls.Add(this.ListBox1);
            this.Controls.Add(this.Label1);
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Server";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Button1;
        public System.Windows.Forms.ListBox ListBox1;
        private System.Windows.Forms.Label Label1;
    }
}

