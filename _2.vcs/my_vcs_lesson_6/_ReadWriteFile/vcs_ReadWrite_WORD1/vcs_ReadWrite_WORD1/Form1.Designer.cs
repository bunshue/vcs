namespace vcs_ReadWrite_WORD1
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
            this.txtFile = new System.Windows.Forms.TextBox();
            this.btnRemoveHyperlinks = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(25, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "File:";
            // 
            // txtFile
            // 
            this.txtFile.Location = new System.Drawing.Point(44, 11);
            this.txtFile.Name = "txtFile";
            this.txtFile.Size = new System.Drawing.Size(339, 22);
            this.txtFile.TabIndex = 1;
            // 
            // btnRemoveHyperlinks
            // 
            this.btnRemoveHyperlinks.Location = new System.Drawing.Point(44, 58);
            this.btnRemoveHyperlinks.Name = "btnRemoveHyperlinks";
            this.btnRemoveHyperlinks.Size = new System.Drawing.Size(166, 28);
            this.btnRemoveHyperlinks.TabIndex = 2;
            this.btnRemoveHyperlinks.Text = "移除WORD檔裡面的超連結";
            this.btnRemoveHyperlinks.UseVisualStyleBackColor = true;
            this.btnRemoveHyperlinks.Click += new System.EventHandler(this.btnRemoveHyperlinks_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(44, 116);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(613, 405);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnRemoveHyperlinks;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(693, 546);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnRemoveHyperlinks);
            this.Controls.Add(this.txtFile);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "vcs_ReadWrite_WORD1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtFile;
        private System.Windows.Forms.Button btnRemoveHyperlinks;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

