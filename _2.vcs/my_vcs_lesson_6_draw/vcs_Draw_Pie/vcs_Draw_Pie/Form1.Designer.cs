namespace vcs_Draw_Pie
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
            this.components = new System.ComponentModel.Container();
            this.btnExplode = new System.Windows.Forms.Button();
            this.tmrExplode = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // btnExplode
            // 
            this.btnExplode.Location = new System.Drawing.Point(2, 2);
            this.btnExplode.Name = "btnExplode";
            this.btnExplode.Size = new System.Drawing.Size(75, 21);
            this.btnExplode.TabIndex = 2;
            this.btnExplode.Text = "Explode";
            this.btnExplode.UseVisualStyleBackColor = true;
            this.btnExplode.Click += new System.EventHandler(this.btnExplode_Click);
            // 
            // tmrExplode
            // 
            this.tmrExplode.Interval = 20;
            this.tmrExplode.Tick += new System.EventHandler(this.tmrExplode_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(673, 532);
            this.Controls.Add(this.btnExplode);
            this.Name = "Form1";
            this.Text = "vcs_Draw_Pie";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnExplode;
        private System.Windows.Forms.Timer tmrExplode;
    }
}

