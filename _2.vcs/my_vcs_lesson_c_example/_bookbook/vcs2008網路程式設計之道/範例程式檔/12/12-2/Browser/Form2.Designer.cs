namespace Browser
{
    partial class Form2
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
          this.btnOK = new System.Windows.Forms.Button();
          this.txtSource = new System.Windows.Forms.TextBox();
          this.SuspendLayout();
          // 
          // btnOK
          // 
          this.btnOK.DialogResult = System.Windows.Forms.DialogResult.OK;
          this.btnOK.Location = new System.Drawing.Point(133, 283);
          this.btnOK.Name = "btnOK";
          this.btnOK.Size = new System.Drawing.Size(81, 29);
          this.btnOK.TabIndex = 0;
          this.btnOK.Text = "&OK";
          this.btnOK.UseVisualStyleBackColor = true;
          this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
          // 
          // txtSource
          // 
          this.txtSource.Font = new System.Drawing.Font("PMingLiU", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
          this.txtSource.Location = new System.Drawing.Point(3, 3);
          this.txtSource.Multiline = true;
          this.txtSource.Name = "txtSource";
          this.txtSource.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
          this.txtSource.Size = new System.Drawing.Size(341, 269);
          this.txtSource.TabIndex = 1;
          // 
          // Form2
          // 
          this.AcceptButton = this.btnOK;
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(346, 321);
          this.Controls.Add(this.txtSource);
          this.Controls.Add(this.btnOK);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
          this.MaximizeBox = false;
          this.Name = "Form2";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
          this.Text = "Source Code";
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.TextBox txtSource;
        public System.Windows.Forms.Button btnOK;
    }
}