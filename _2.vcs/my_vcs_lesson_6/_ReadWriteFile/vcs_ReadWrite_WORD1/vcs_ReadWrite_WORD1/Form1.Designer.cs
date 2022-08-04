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
            this.btnRemoveHyperlinks = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.btnGo = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnRemoveHyperlinks
            // 
            this.btnRemoveHyperlinks.Location = new System.Drawing.Point(12, 12);
            this.btnRemoveHyperlinks.Name = "btnRemoveHyperlinks";
            this.btnRemoveHyperlinks.Size = new System.Drawing.Size(166, 28);
            this.btnRemoveHyperlinks.TabIndex = 2;
            this.btnRemoveHyperlinks.Text = "移除WORD檔裡面的超連結";
            this.btnRemoveHyperlinks.UseVisualStyleBackColor = true;
            this.btnRemoveHyperlinks.Click += new System.EventHandler(this.btnRemoveHyperlinks_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 46);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(613, 429);
            this.richTextBox1.TabIndex = 3;
            this.richTextBox1.Text = "";
            // 
            // btnGo
            // 
            this.btnGo.Location = new System.Drawing.Point(193, 12);
            this.btnGo.Name = "btnGo";
            this.btnGo.Size = new System.Drawing.Size(158, 28);
            this.btnGo.TabIndex = 7;
            this.btnGo.Text = "建立一Word檔案";
            this.btnGo.UseVisualStyleBackColor = true;
            this.btnGo.Click += new System.EventHandler(this.btnGo_Click);
            // 
            // Form1
            // 
            this.AcceptButton = this.btnRemoveHyperlinks;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(635, 485);
            this.Controls.Add(this.btnGo);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.btnRemoveHyperlinks);
            this.Name = "Form1";
            this.Text = "vcs_ReadWrite_WORD1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnRemoveHyperlinks;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button btnGo;
    }
}

