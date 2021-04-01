namespace VoIP
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
      this.chkGateway = new System.Windows.Forms.CheckBox();
      this.chkAuto = new System.Windows.Forms.CheckBox();
      this.chkSilence = new System.Windows.Forms.CheckBox();
      this.btnListen = new System.Windows.Forms.Button();
      this.btnHangup = new System.Windows.Forms.Button();
      this.txtGateway = new System.Windows.Forms.TextBox();
      this.txtHost = new System.Windows.Forms.TextBox();
      this.btnCall = new System.Windows.Forms.Button();
      this.label1 = new System.Windows.Forms.Label();
      this.cboOutput = new System.Windows.Forms.ComboBox();
      this.cboInput = new System.Windows.Forms.ComboBox();
      this.label2 = new System.Windows.Forms.Label();
      this.label3 = new System.Windows.Forms.Label();
      this.label4 = new System.Windows.Forms.Label();
      this.btnAnswer = new System.Windows.Forms.Button();
      this.SuspendLayout();
      // 
      // chkGateway
      // 
      this.chkGateway.Location = new System.Drawing.Point(201, 112);
      this.chkGateway.Name = "chkGateway";
      this.chkGateway.Size = new System.Drawing.Size(136, 28);
      this.chkGateway.TabIndex = 16;
      this.chkGateway.Text = "使用H.323閘道器";
      this.chkGateway.CheckedChanged += new System.EventHandler(this.chkGateway_CheckedChanged);
      // 
      // chkAuto
      // 
      this.chkAuto.Checked = true;
      this.chkAuto.CheckState = System.Windows.Forms.CheckState.Checked;
      this.chkAuto.Location = new System.Drawing.Point(201, 89);
      this.chkAuto.Name = "chkAuto";
      this.chkAuto.Size = new System.Drawing.Size(144, 28);
      this.chkAuto.TabIndex = 15;
      this.chkAuto.Text = "自動答話";
      this.chkAuto.CheckedChanged += new System.EventHandler(this.chkAuto_CheckedChanged);
      // 
      // chkSilence
      // 
      this.chkSilence.Checked = true;
      this.chkSilence.CheckState = System.Windows.Forms.CheckState.Checked;
      this.chkSilence.Location = new System.Drawing.Point(201, 68);
      this.chkSilence.Name = "chkSilence";
      this.chkSilence.Size = new System.Drawing.Size(144, 28);
      this.chkSilence.TabIndex = 14;
      this.chkSilence.Text = "靜音偵測";
      this.chkSilence.CheckedChanged += new System.EventHandler(this.chkSilence_CheckedChanged);
      // 
      // btnListen
      // 
      this.btnListen.Location = new System.Drawing.Point(14, 54);
      this.btnListen.Name = "btnListen";
      this.btnListen.Size = new System.Drawing.Size(77, 25);
      this.btnListen.TabIndex = 13;
      this.btnListen.Text = "Listen";
      this.btnListen.Click += new System.EventHandler(this.btnListen_Click);
      // 
      // btnHangup
      // 
      this.btnHangup.Location = new System.Drawing.Point(14, 117);
      this.btnHangup.Name = "btnHangup";
      this.btnHangup.Size = new System.Drawing.Size(77, 25);
      this.btnHangup.TabIndex = 12;
      this.btnHangup.Text = "Hang Up";
      this.btnHangup.Click += new System.EventHandler(this.btnHangup_Click);
      // 
      // txtGateway
      // 
      this.txtGateway.Enabled = false;
      this.txtGateway.Location = new System.Drawing.Point(274, 137);
      this.txtGateway.Name = "txtGateway";
      this.txtGateway.Size = new System.Drawing.Size(103, 22);
      this.txtGateway.TabIndex = 11;
      // 
      // txtHost
      // 
      this.txtHost.Location = new System.Drawing.Point(47, 12);
      this.txtHost.Name = "txtHost";
      this.txtHost.Size = new System.Drawing.Size(134, 22);
      this.txtHost.TabIndex = 10;
      // 
      // btnCall
      // 
      this.btnCall.Location = new System.Drawing.Point(14, 86);
      this.btnCall.Name = "btnCall";
      this.btnCall.Size = new System.Drawing.Size(77, 25);
      this.btnCall.TabIndex = 9;
      this.btnCall.Text = "Call";
      this.btnCall.Click += new System.EventHandler(this.btnCall_Click);
      // 
      // label1
      // 
      this.label1.AutoSize = true;
      this.label1.Location = new System.Drawing.Point(12, 15);
      this.label1.Name = "label1";
      this.label1.Size = new System.Drawing.Size(29, 12);
      this.label1.TabIndex = 17;
      this.label1.Text = "Host:";
      // 
      // cboOutput
      // 
      this.cboOutput.BackColor = System.Drawing.SystemColors.Window;
      this.cboOutput.Cursor = System.Windows.Forms.Cursors.Default;
      this.cboOutput.ForeColor = System.Drawing.SystemColors.WindowText;
      this.cboOutput.Location = new System.Drawing.Point(260, 38);
      this.cboOutput.Name = "cboOutput";
      this.cboOutput.RightToLeft = System.Windows.Forms.RightToLeft.No;
      this.cboOutput.Size = new System.Drawing.Size(160, 20);
      this.cboOutput.TabIndex = 18;
      this.cboOutput.SelectedIndexChanged += new System.EventHandler(this.cboOutput_SelectedIndexChanged);
      // 
      // cboInput
      // 
      this.cboInput.BackColor = System.Drawing.SystemColors.Window;
      this.cboInput.Cursor = System.Windows.Forms.Cursors.Default;
      this.cboInput.ForeColor = System.Drawing.SystemColors.WindowText;
      this.cboInput.Location = new System.Drawing.Point(260, 12);
      this.cboInput.Name = "cboInput";
      this.cboInput.RightToLeft = System.Windows.Forms.RightToLeft.No;
      this.cboInput.Size = new System.Drawing.Size(160, 20);
      this.cboInput.TabIndex = 19;
      this.cboInput.SelectedIndexChanged += new System.EventHandler(this.cboInput_SelectedIndexChanged);
      // 
      // label2
      // 
      this.label2.AutoSize = true;
      this.label2.Location = new System.Drawing.Point(224, 140);
      this.label2.Name = "label2";
      this.label2.Size = new System.Drawing.Size(44, 12);
      this.label2.TabIndex = 22;
      this.label2.Text = "閘道器:";
      // 
      // label3
      // 
      this.label3.AutoSize = true;
      this.label3.Location = new System.Drawing.Point(198, 43);
      this.label3.Name = "label3";
      this.label3.Size = new System.Drawing.Size(56, 12);
      this.label3.TabIndex = 23;
      this.label3.Text = "語音輸出:";
      // 
      // label4
      // 
      this.label4.AutoSize = true;
      this.label4.Location = new System.Drawing.Point(198, 15);
      this.label4.Name = "label4";
      this.label4.Size = new System.Drawing.Size(56, 12);
      this.label4.TabIndex = 24;
      this.label4.Text = "語音輸入:";
      // 
      // btnAnswer
      // 
      this.btnAnswer.BackColor = System.Drawing.SystemColors.Control;
      this.btnAnswer.Cursor = System.Windows.Forms.Cursors.Default;
      this.btnAnswer.ForeColor = System.Drawing.SystemColors.ControlText;
      this.btnAnswer.Location = new System.Drawing.Point(14, 148);
      this.btnAnswer.Name = "btnAnswer";
      this.btnAnswer.RightToLeft = System.Windows.Forms.RightToLeft.No;
      this.btnAnswer.Size = new System.Drawing.Size(77, 25);
      this.btnAnswer.TabIndex = 21;
      this.btnAnswer.Text = "Answer";
      this.btnAnswer.UseVisualStyleBackColor = false;
      this.btnAnswer.Click += new System.EventHandler(this.btnAnswer_Click);
      // 
      // Form1
      // 
      this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
      this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
      this.ClientSize = new System.Drawing.Size(432, 183);
      this.Controls.Add(this.txtGateway);
      this.Controls.Add(this.label4);
      this.Controls.Add(this.label3);
      this.Controls.Add(this.label2);
      this.Controls.Add(this.btnAnswer);
      this.Controls.Add(this.cboInput);
      this.Controls.Add(this.cboOutput);
      this.Controls.Add(this.label1);
      this.Controls.Add(this.chkGateway);
      this.Controls.Add(this.chkAuto);
      this.Controls.Add(this.chkSilence);
      this.Controls.Add(this.btnListen);
      this.Controls.Add(this.btnHangup);
      this.Controls.Add(this.txtHost);
      this.Controls.Add(this.btnCall);
      this.MaximizeBox = false;
      this.Name = "Form1";
      this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
      this.Text = "VoIP with H.323";
      this.Load += new System.EventHandler(this.Form1_Load);
      this.ResumeLayout(false);
      this.PerformLayout();

    }

    #endregion

    private System.Windows.Forms.CheckBox chkGateway;
    private System.Windows.Forms.CheckBox chkAuto;
    private System.Windows.Forms.CheckBox chkSilence;
    private System.Windows.Forms.Button btnListen;
    private System.Windows.Forms.Button btnHangup;
    private System.Windows.Forms.TextBox txtGateway;
    private System.Windows.Forms.TextBox txtHost;
    private System.Windows.Forms.Button btnCall;
    private System.Windows.Forms.Label label1;
    public System.Windows.Forms.ComboBox cboOutput;
    public System.Windows.Forms.ComboBox cboInput;
    private System.Windows.Forms.Label label2;
    private System.Windows.Forms.Label label3;
    private System.Windows.Forms.Label label4;
    public System.Windows.Forms.Button btnAnswer;


  }
}

