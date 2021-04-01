namespace HTTPRequest
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
      this.txtRequest = new System.Windows.Forms.TextBox();
      this.txtURL = new System.Windows.Forms.TextBox();
      this.label1 = new System.Windows.Forms.Label();
      this.SuspendLayout();
      // 
      // txtRequest
      // 
      this.txtRequest.Location = new System.Drawing.Point(6, 45);
      this.txtRequest.Multiline = true;
      this.txtRequest.Name = "txtRequest";
      this.txtRequest.Size = new System.Drawing.Size(231, 245);
      this.txtRequest.TabIndex = 6;
      // 
      // txtURL
      // 
      this.txtURL.Location = new System.Drawing.Point(40, 9);
      this.txtURL.Name = "txtURL";
      this.txtURL.Size = new System.Drawing.Size(197, 30);
      this.txtURL.TabIndex = 5;
      this.txtURL.Text = "http://www.microsoft.com/taiwan";
      // 
      // label1
      // 
      this.label1.Location = new System.Drawing.Point(3, 9);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(42, 20);
      this.label1.Text = "URL:";
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(131F, 131F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
      this.AutoScroll = true;
      this.ClientSize = new System.Drawing.Size(240, 293);
      this.Controls.Add(this.txtRequest);
      this.Controls.Add(this.txtURL);
      this.Controls.Add(this.label1);
      this.KeyPreview = true;
      this.Name = "Form1";
      this.Text = "HTTP Request";
      this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
      this.ResumeLayout(false);

    }

    #endregion

    public System.Windows.Forms.TextBox txtRequest;
    private System.Windows.Forms.TextBox txtURL;
    private System.Windows.Forms.Label label1;
  }
}

