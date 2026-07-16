namespace VideoConference
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
      this.components = new System.ComponentModel.Container();
      this.picLocal = new System.Windows.Forms.PictureBox();
      this.label1 = new System.Windows.Forms.Label();
      this.label2 = new System.Windows.Forms.Label();
      this.picRemote = new System.Windows.Forms.PictureBox();
      this.btnSend = new System.Windows.Forms.Button();
      this.btnListen = new System.Windows.Forms.Button();
      this.btnStart = new System.Windows.Forms.Button();
      this.btnStop = new System.Windows.Forms.Button();
      this.txtHost = new System.Windows.Forms.TextBox();
      this.timer1 = new System.Windows.Forms.Timer(this.components);
      ((System.ComponentModel.ISupportInitialize)(this.picLocal)).BeginInit();
      ((System.ComponentModel.ISupportInitialize)(this.picRemote)).BeginInit();
      this.SuspendLayout();
      // 
      // picLocal
      // 
      this.picLocal.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
      this.picLocal.Location = new System.Drawing.Point(15, 41);
      this.picLocal.Name = "picLocal";
      this.picLocal.Size = new System.Drawing.Size(240, 180);
      this.picLocal.TabIndex = 21;
      this.picLocal.TabStop = false;
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.Location = new System.Drawing.Point(15, 16);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(58, 12);
      this.label1.TabIndex = 25;
      this.label1.Text = "Local Host:";
      // 
      // label2
      // 
      this.label2.AutoSize = true;
      this.label2.Location = new System.Drawing.Point(277, 16);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(68, 12);
      this.label2.TabIndex = 27;
      this.label2.Text = "Remote Host:";
      // 
      // picRemote
      // 
      this.picRemote.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
      this.picRemote.Location = new System.Drawing.Point(277, 41);
      this.picRemote.Name = "picRemote";
      this.picRemote.Size = new System.Drawing.Size(240, 180);
      this.picRemote.TabIndex = 26;
      this.picRemote.TabStop = false;
      // 
      // btnSend
      // 
      this.btnSend.FlatStyle = System.Windows.Forms.FlatStyle.System;
      this.btnSend.Location = new System.Drawing.Point(360, 232);
      this.btnSend.Name = "btnSend";
      this.btnSend.Size = new System.Drawing.Size(74, 28);
      this.btnSend.TabIndex = 31;
      this.btnSend.Text = "傳送";
      this.btnSend.UseVisualStyleBackColor = true;
      this.btnSend.Click += new System.EventHandler(this.btnSend_Click);
      // 
      // btnListen
      // 
      this.btnListen.FlatStyle = System.Windows.Forms.FlatStyle.System;
      this.btnListen.Location = new System.Drawing.Point(181, 232);
      this.btnListen.Name = "btnListen";
      this.btnListen.Size = new System.Drawing.Size(74, 28);
      this.btnListen.TabIndex = 30;
      this.btnListen.Text = "Listen";
      this.btnListen.UseVisualStyleBackColor = true;
      this.btnListen.Click += new System.EventHandler(this.btnListen_Click);
      // 
      // btnStart
      // 
      this.btnStart.Location = new System.Drawing.Point(17, 232);
      this.btnStart.Name = "btnStart";
      this.btnStart.Size = new System.Drawing.Size(74, 28);
      this.btnStart.TabIndex = 34;
      this.btnStart.Text = "錄影";
      this.btnStart.UseVisualStyleBackColor = true;
      this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
      // 
      // btnStop
      // 
      this.btnStop.Location = new System.Drawing.Point(99, 232);
      this.btnStop.Name = "btnStop";
      this.btnStop.Size = new System.Drawing.Size(74, 28);
      this.btnStop.TabIndex = 32;
      this.btnStop.Text = "停止";
      this.btnStop.UseVisualStyleBackColor = true;
      this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
      // 
      // txtHost
      // 
      this.txtHost.Location = new System.Drawing.Point(351, 12);
      this.txtHost.Name = "txtHost";
      this.txtHost.Size = new System.Drawing.Size(166, 22);
      this.txtHost.TabIndex = 35;
      // 
      // timer1
      // 
      this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(532, 273);
      this.Controls.Add(this.txtHost);
      this.Controls.Add(this.btnStart);
      this.Controls.Add(this.btnStop);
      this.Controls.Add(this.btnSend);
      this.Controls.Add(this.btnListen);
      this.Controls.Add(this.label2);
      this.Controls.Add(this.picRemote);
      this.Controls.Add(this.label1);
      this.Controls.Add(this.picLocal);
      this.MaximizeBox = false;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "Video Conference";
      this.Load += new System.EventHandler(this.Form1_Load);
      this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
      ((System.ComponentModel.ISupportInitialize)(this.picLocal)).EndInit();
      ((System.ComponentModel.ISupportInitialize)(this.picRemote)).EndInit();
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    internal System.Windows.Forms.PictureBox picLocal;
    private System.Windows.Forms.Label label1;
    private System.Windows.Forms.Label label2;
    internal System.Windows.Forms.PictureBox picRemote;
    private System.Windows.Forms.Button btnSend;
    private System.Windows.Forms.Button btnListen;
    internal System.Windows.Forms.Button btnStart;
    internal System.Windows.Forms.Button btnStop;
    private System.Windows.Forms.TextBox txtHost;
    private System.Windows.Forms.Timer timer1;
  }
}

