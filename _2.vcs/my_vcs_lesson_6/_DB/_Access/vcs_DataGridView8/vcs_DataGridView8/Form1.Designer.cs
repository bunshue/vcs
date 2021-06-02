namespace vcs_DataGridView8
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
            this.dgContacts = new System.Windows.Forms.DataGrid();
            ((System.ComponentModel.ISupportInitialize)(this.dgContacts)).BeginInit();
            this.SuspendLayout();
            // 
            // dgContacts
            // 
            this.dgContacts.DataMember = "";
            this.dgContacts.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dgContacts.HeaderForeColor = System.Drawing.SystemColors.ControlText;
            this.dgContacts.Location = new System.Drawing.Point(0, 0);
            this.dgContacts.Name = "dgContacts";
            this.dgContacts.Size = new System.Drawing.Size(799, 491);
            this.dgContacts.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(799, 491);
            this.Controls.Add(this.dgContacts);
            this.Name = "Form1";
            this.Text = "vcs_DataGridView8";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgContacts)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.DataGrid dgContacts;
    }
}

