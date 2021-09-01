namespace howto_address_maps
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
            this.cboGoogle = new System.Windows.Forms.ComboBox();
            this.btnGoogle = new System.Windows.Forms.Button();
            this.txtAddress = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // cboGoogle
            // 
            this.cboGoogle.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.cboGoogle.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cboGoogle.FormattingEnabled = true;
            this.cboGoogle.Items.AddRange(new object[] {
            "Map",
            "Satellite",
            "Hybrid",
            "Terrain",
            "Google Earth"});
            this.cboGoogle.Location = new System.Drawing.Point(87, 70);
            this.cboGoogle.Name = "cboGoogle";
            this.cboGoogle.Size = new System.Drawing.Size(115, 20);
            this.cboGoogle.TabIndex = 15;
            // 
            // btnGoogle
            // 
            this.btnGoogle.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.btnGoogle.Location = new System.Drawing.Point(208, 64);
            this.btnGoogle.Name = "btnGoogle";
            this.btnGoogle.Size = new System.Drawing.Size(88, 30);
            this.btnGoogle.TabIndex = 14;
            this.btnGoogle.Text = "Google";
            this.btnGoogle.UseVisualStyleBackColor = true;
            this.btnGoogle.Click += new System.EventHandler(this.btnGoogle_Click);
            // 
            // txtAddress
            // 
            this.txtAddress.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtAddress.Location = new System.Drawing.Point(66, 11);
            this.txtAddress.Name = "txtAddress";
            this.txtAddress.Size = new System.Drawing.Size(369, 22);
            this.txtAddress.TabIndex = 13;
            this.txtAddress.Text = "1600 Pennsylvania Avenue; NW Washington, D.C. 20500";
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(12, 14);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(45, 12);
            this.Label1.TabIndex = 12;
            this.Label1.Text = "Address:";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(14, 125);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(421, 433);
            this.richTextBox1.TabIndex = 16;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGoogle;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(447, 570);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.cboGoogle);
            this.Controls.Add(this.btnGoogle);
            this.Controls.Add(this.txtAddress);
            this.Controls.Add(this.Label1);
            this.Name = "Form1";
            this.Text = "howto_address_maps";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.ComboBox cboGoogle;
        internal System.Windows.Forms.Button btnGoogle;
        internal System.Windows.Forms.TextBox txtAddress;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

