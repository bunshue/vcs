namespace Cookie
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
      this.txtCookie = new System.Windows.Forms.TextBox();
      this.Label2 = new System.Windows.Forms.Label();
      this.Button1 = new System.Windows.Forms.Button();
      this.SuspendLayout();
      // 
      // txtCookie
      // 
      this.txtCookie.Location = new System.Drawing.Point(12, 31);
      this.txtCookie.Multiline = true;
      this.txtCookie.Name = "txtCookie";
      this.txtCookie.ScrollBars = System.Windows.Forms.ScrollBars.Both;
      this.txtCookie.Size = new System.Drawing.Size(243, 156);
      this.txtCookie.TabIndex = 12;
      // 
      // Label2
      // 
      this.Label2.Location = new System.Drawing.Point(13, 11);
      this.Label2.Name = "Label2";
      this.Label2.Size = new System.Drawing.Size(64, 20);
      this.Label2.TabIndex = 14;
      this.Label2.Text = "Cookie:";
      // 
      // Button1
      // 
      this.Button1.Location = new System.Drawing.Point(91, 203);
      this.Button1.Name = "Button1";
      this.Button1.Size = new System.Drawing.Size(84, 28);
      this.Button1.TabIndex = 13;
      this.Button1.Text = "OK";
      this.Button1.Click += new System.EventHandler(this.Button1_Click);
      // 
      // Form1
      // 
      this.AcceptButton = this.Button1;
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(267, 246);
      this.Controls.Add(this.txtCookie);
      this.Controls.Add(this.Label2);
      this.Controls.Add(this.Button1);
      this.MaximizeBox = false;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "Cookie";
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.TextBox txtCookie;
    private System.Windows.Forms.Label Label2;
    private System.Windows.Forms.Button Button1;
  }
}

