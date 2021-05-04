namespace HTTPRequest
{
  partial class Form1
  {
    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;
    private System.Windows.Forms.MainMenu mainMenu1;

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
      this.mainMenu1 = new System.Windows.Forms.MainMenu();
      this.menuItem1 = new System.Windows.Forms.MenuItem();
      this.mnuExit = new System.Windows.Forms.MenuItem();
      this.btnOK = new System.Windows.Forms.Button();
      this.txtRequest = new System.Windows.Forms.TextBox();
      this.txtURL = new System.Windows.Forms.TextBox();
      this.label1 = new System.Windows.Forms.Label();
      this.SuspendLayout();
      // 
      // mainMenu1
      // 
      this.mainMenu1.MenuItems.Add(this.menuItem1);
      // 
      // menuItem1
      // 
      this.menuItem1.MenuItems.Add(this.mnuExit);
      this.menuItem1.Text = "File";
      // 
      // mnuExit
      // 
      this.mnuExit.Text = "Exit";
      this.mnuExit.Click += new System.EventHandler(this.mnuExit_Click);
      // 
      // btnOK
      // 
      this.btnOK.Location = new System.Drawing.Point(80, 228);
      this.btnOK.Name = "btnOK";
      this.btnOK.Size = new System.Drawing.Size(81, 30);
      this.btnOK.TabIndex = 7;
      this.btnOK.Text = "OK";
      this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
      // 
      // txtRequest
      // 
      this.txtRequest.Location = new System.Drawing.Point(6, 45);
      this.txtRequest.Multiline = true;
      this.txtRequest.Name = "txtRequest";
      this.txtRequest.ScrollBars = System.Windows.Forms.ScrollBars.Both;
      this.txtRequest.Size = new System.Drawing.Size(228, 177);
      this.txtRequest.TabIndex = 6;
      // 
      // txtURL
      // 
      this.txtURL.Location = new System.Drawing.Point(36, 10);
      this.txtURL.Name = "txtURL";
      this.txtURL.Size = new System.Drawing.Size(201, 21);
      this.txtURL.TabIndex = 5;
      this.txtURL.Text = "http://www.microsoft.com/taiwan";
      // 
      // label1
      // 
      this.label1.Location = new System.Drawing.Point(3, 10);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(42, 20);
      this.label1.Text = "URL:";
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(96F, 96F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
      this.AutoScroll = true;
      this.ClientSize = new System.Drawing.Size(240, 268);
      this.Controls.Add(this.btnOK);
      this.Controls.Add(this.txtRequest);
      this.Controls.Add(this.txtURL);
      this.Controls.Add(this.label1);
      this.Menu = this.mainMenu1;
      this.Name = "Form1";
      this.Text = "HTTP Request";
      this.ResumeLayout(false);

    }

    #endregion

    private System.Windows.Forms.MenuItem menuItem1;
    private System.Windows.Forms.MenuItem mnuExit;
    private System.Windows.Forms.Button btnOK;
    public System.Windows.Forms.TextBox txtRequest;
    private System.Windows.Forms.TextBox txtURL;
    private System.Windows.Forms.Label label1;
  }
}

