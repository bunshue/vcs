namespace vcs_ModalMenuForm
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
            this.btnModalMenu = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnModalMenu
            // 
            this.btnModalMenu.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.btnModalMenu.Location = new System.Drawing.Point(130, 62);
            this.btnModalMenu.Name = "btnModalMenu";
            this.btnModalMenu.Size = new System.Drawing.Size(75, 23);
            this.btnModalMenu.TabIndex = 0;
            this.btnModalMenu.Text = "Modal Menu";
            this.btnModalMenu.UseVisualStyleBackColor = true;
            this.btnModalMenu.Click += new System.EventHandler(this.btnModalMenu_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnModalMenu;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LightGreen;
            this.ClientSize = new System.Drawing.Size(334, 146);
            this.Controls.Add(this.btnModalMenu);
            this.Name = "Form1";
            this.Text = "vcs_ModalMenuForm";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnModalMenu;
    }
}

