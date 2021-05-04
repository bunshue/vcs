namespace WebCam
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
      this.btnStart = new System.Windows.Forms.Button();
      this.btnSave = new System.Windows.Forms.Button();
      this.btnStop = new System.Windows.Forms.Button();
      this.picCapture = new System.Windows.Forms.PictureBox();
      ((System.ComponentModel.ISupportInitialize)(this.picCapture)).BeginInit();
      this.SuspendLayout();
      // 
      // btnStart
      // 
      this.btnStart.Location = new System.Drawing.Point(14, 267);
      this.btnStart.Name = "btnStart";
      this.btnStart.Size = new System.Drawing.Size(80, 30);
      this.btnStart.TabIndex = 20;
      this.btnStart.Text = "錄影";
      this.btnStart.UseVisualStyleBackColor = true;
      this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
      // 
      // btnSave
      // 
      this.btnSave.Location = new System.Drawing.Point(131, 267);
      this.btnSave.Name = "btnSave";
      this.btnSave.Size = new System.Drawing.Size(80, 30);
      this.btnSave.TabIndex = 19;
      this.btnSave.Text = "儲存";
      this.btnSave.UseVisualStyleBackColor = true;
      this.btnSave.Click += new System.EventHandler(this.btnSave_Click);
      // 
      // btnStop
      // 
      this.btnStop.Location = new System.Drawing.Point(248, 267);
      this.btnStop.Name = "btnStop";
      this.btnStop.Size = new System.Drawing.Size(80, 30);
      this.btnStop.TabIndex = 16;
      this.btnStop.Text = "停止";
      this.btnStop.UseVisualStyleBackColor = true;
      this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
      // 
      // picCapture
      // 
      this.picCapture.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
      this.picCapture.Location = new System.Drawing.Point(11, 12);
      this.picCapture.Name = "picCapture";
      this.picCapture.Size = new System.Drawing.Size(320, 240);
      this.picCapture.TabIndex = 15;
      this.picCapture.TabStop = false;
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(342, 308);
      this.Controls.Add(this.btnStart);
      this.Controls.Add(this.btnSave);
      this.Controls.Add(this.btnStop);
      this.Controls.Add(this.picCapture);
      this.MaximizeBox = false;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "WebCam";
      this.Load += new System.EventHandler(this.Form1_Load);
      ((System.ComponentModel.ISupportInitialize)(this.picCapture)).EndInit();
      this.ResumeLayout(false);

    }

    #endregion

    internal System.Windows.Forms.Button btnStart;
    internal System.Windows.Forms.Button btnSave;
    internal System.Windows.Forms.Button btnStop;
    internal System.Windows.Forms.PictureBox picCapture;
  }
}

