namespace SaveHTML
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
          this.SaveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
          this.btnSave = new System.Windows.Forms.Button();
          this.btnHTML = new System.Windows.Forms.Button();
          this.txtHTML = new System.Windows.Forms.TextBox();
          this.Label2 = new System.Windows.Forms.Label();
          this.txtURL = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.SuspendLayout();
          // 
          // SaveFileDialog1
          // 
          this.SaveFileDialog1.FileName = "doc1";
          // 
          // btnSave
          // 
          this.btnSave.Location = new System.Drawing.Point(141, 236);
          this.btnSave.Name = "btnSave";
          this.btnSave.Size = new System.Drawing.Size(72, 28);
          this.btnSave.TabIndex = 17;
          this.btnSave.Text = "Save";
          this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
          // 
          // btnHTML
          // 
          this.btnHTML.Location = new System.Drawing.Point(45, 236);
          this.btnHTML.Name = "btnHTML";
          this.btnHTML.Size = new System.Drawing.Size(72, 28);
          this.btnHTML.TabIndex = 16;
          this.btnHTML.Text = "HTML";
          this.btnHTML.Click += new System.EventHandler(this.btnHTML_Click);
          // 
          // txtHTML
          // 
          this.txtHTML.Location = new System.Drawing.Point(9, 56);
          this.txtHTML.Multiline = true;
          this.txtHTML.Name = "txtHTML";
          this.txtHTML.ScrollBars = System.Windows.Forms.ScrollBars.Both;
          this.txtHTML.Size = new System.Drawing.Size(241, 168);
          this.txtHTML.TabIndex = 15;
          // 
          // Label2
          // 
          this.Label2.Location = new System.Drawing.Point(9, 40);
          this.Label2.Name = "Label2";
          this.Label2.Size = new System.Drawing.Size(104, 16);
          this.Label2.TabIndex = 14;
          this.Label2.Text = "HTML:";
          // 
          // txtURL
          // 
          this.txtURL.Location = new System.Drawing.Point(49, 8);
          this.txtURL.Name = "txtURL";
          this.txtURL.Size = new System.Drawing.Size(201, 22);
          this.txtURL.TabIndex = 13;
          this.txtURL.Text = "www.yahoo.com";
          // 
          // Label1
          // 
          this.Label1.Location = new System.Drawing.Point(9, 12);
          this.Label1.Name = "Label1";
          this.Label1.Size = new System.Drawing.Size(44, 16);
          this.Label1.TabIndex = 12;
          this.Label1.Text = "URL:";
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(259, 273);
          this.Controls.Add(this.btnSave);
          this.Controls.Add(this.btnHTML);
          this.Controls.Add(this.txtHTML);
          this.Controls.Add(this.Label2);
          this.Controls.Add(this.txtURL);
          this.Controls.Add(this.Label1);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
          this.MaximizeBox = false;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "HTTP Response";
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.SaveFileDialog SaveFileDialog1;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnHTML;
        private System.Windows.Forms.TextBox txtHTML;
        private System.Windows.Forms.Label Label2;
        private System.Windows.Forms.TextBox txtURL;
        private System.Windows.Forms.Label Label1;
    }
}

