namespace URL
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
      this.Label1 = new System.Windows.Forms.Label();
      this.txtURL = new System.Windows.Forms.TextBox();
      this.txtResult = new System.Windows.Forms.TextBox();
      this.Label2 = new System.Windows.Forms.Label();
      this.Button1 = new System.Windows.Forms.Button();
      this.SuspendLayout();
      // 
      // Label1
      // 
      this.Label1.Location = new System.Drawing.Point(12, 42);
      this.Label1.Name = "Label1";
      this.Label1.Size = new System.Drawing.Size(64, 20);
      this.Label1.TabIndex = 21;
      this.Label1.Text = "Properties:";
      // 
      // txtURL
      // 
      this.txtURL.Location = new System.Drawing.Point(55, 12);
      this.txtURL.Name = "txtURL";
      this.txtURL.Size = new System.Drawing.Size(274, 22);
      this.txtURL.TabIndex = 17;
      // 
      // txtResult
      // 
      this.txtResult.Location = new System.Drawing.Point(12, 62);
      this.txtResult.Multiline = true;
      this.txtResult.Name = "txtResult";
      this.txtResult.ScrollBars = System.Windows.Forms.ScrollBars.Both;
      this.txtResult.Size = new System.Drawing.Size(317, 188);
      this.txtResult.TabIndex = 18;
      // 
      // Label2
      // 
      this.Label2.Location = new System.Drawing.Point(11, 12);
      this.Label2.Name = "Label2";
      this.Label2.Size = new System.Drawing.Size(64, 20);
      this.Label2.TabIndex = 20;
      this.Label2.Text = "URL:";
      // 
      // Button1
      // 
      this.Button1.Location = new System.Drawing.Point(124, 266);
      this.Button1.Name = "Button1";
      this.Button1.Size = new System.Drawing.Size(94, 28);
      this.Button1.TabIndex = 19;
      this.Button1.Text = "Properties";
      this.Button1.Click += new System.EventHandler(this.Button1_Click);
      // 
      // Form1
      // 
      this.AcceptButton = this.Button1;
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(342, 308);
      this.Controls.Add(this.Label1);
      this.Controls.Add(this.txtURL);
      this.Controls.Add(this.txtResult);
      this.Controls.Add(this.Label2);
      this.Controls.Add(this.Button1);
      this.MaximizeBox = false;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "URL";
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.Label Label1;
    private System.Windows.Forms.TextBox txtURL;
    private System.Windows.Forms.TextBox txtResult;
    private System.Windows.Forms.Label Label2;
    private System.Windows.Forms.Button Button1;
  }
}

