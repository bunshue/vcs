namespace howto_use_property_grid
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
            this.lstPeople = new System.Windows.Forms.ListBox();
            this.pgdPeople = new System.Windows.Forms.PropertyGrid();
            this.SuspendLayout();
            // 
            // lstPeople
            // 
            this.lstPeople.Dock = System.Windows.Forms.DockStyle.Left;
            this.lstPeople.FormattingEnabled = true;
            this.lstPeople.ItemHeight = 12;
            this.lstPeople.Location = new System.Drawing.Point(0, 0);
            this.lstPeople.Name = "lstPeople";
            this.lstPeople.Size = new System.Drawing.Size(136, 307);
            this.lstPeople.TabIndex = 0;
            this.lstPeople.SelectedIndexChanged += new System.EventHandler(this.lstPeople_SelectedIndexChanged);
            // 
            // pgdPeople
            // 
            this.pgdPeople.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pgdPeople.Location = new System.Drawing.Point(136, 0);
            this.pgdPeople.Name = "pgdPeople";
            this.pgdPeople.Size = new System.Drawing.Size(348, 307);
            this.pgdPeople.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(484, 307);
            this.Controls.Add(this.pgdPeople);
            this.Controls.Add(this.lstPeople);
            this.Name = "Form1";
            this.Text = "howto_use_property_grid";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lstPeople;
        private System.Windows.Forms.PropertyGrid pgdPeople;
    }
}

