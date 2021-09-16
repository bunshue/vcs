namespace WebcamSecurity
{
    partial class MainForm
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
            this.AutoRecord1 = new System.Windows.Forms.CheckBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.MotionDetection1 = new System.Windows.Forms.CheckBox();
            this.BeepOnMotionCheck1 = new System.Windows.Forms.CheckBox();
            this.RecordingPathInput = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // AutoRecord1
            // 
            this.AutoRecord1.AutoSize = true;
            this.AutoRecord1.Location = new System.Drawing.Point(6, 39);
            this.AutoRecord1.Name = "AutoRecord1";
            this.AutoRecord1.Size = new System.Drawing.Size(121, 28);
            this.AutoRecord1.TabIndex = 2;
            this.AutoRecord1.Text = "Automaticly Record \r\nIf Motion Detected";
            this.AutoRecord1.UseVisualStyleBackColor = true;
            this.AutoRecord1.CheckedChanged += new System.EventHandler(this.AutoRecord1_CheckedChanged);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.MotionDetection1);
            this.groupBox5.Controls.Add(this.BeepOnMotionCheck1);
            this.groupBox5.Controls.Add(this.AutoRecord1);
            this.groupBox5.Location = new System.Drawing.Point(756, 33);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(182, 93);
            this.groupBox5.TabIndex = 1;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Camera 1";
            // 
            // MotionDetection1
            // 
            this.MotionDetection1.AutoSize = true;
            this.MotionDetection1.Location = new System.Drawing.Point(6, 18);
            this.MotionDetection1.Name = "MotionDetection1";
            this.MotionDetection1.Size = new System.Drawing.Size(105, 16);
            this.MotionDetection1.TabIndex = 4;
            this.MotionDetection1.Text = "Motion Detection";
            this.MotionDetection1.UseVisualStyleBackColor = true;
            this.MotionDetection1.CheckedChanged += new System.EventHandler(this.MotionDetection1_CheckedChanged);
            // 
            // BeepOnMotionCheck1
            // 
            this.BeepOnMotionCheck1.AutoSize = true;
            this.BeepOnMotionCheck1.Location = new System.Drawing.Point(6, 72);
            this.BeepOnMotionCheck1.Name = "BeepOnMotionCheck1";
            this.BeepOnMotionCheck1.Size = new System.Drawing.Size(102, 16);
            this.BeepOnMotionCheck1.TabIndex = 3;
            this.BeepOnMotionCheck1.Text = "Beep On Motion";
            this.BeepOnMotionCheck1.UseVisualStyleBackColor = true;
            this.BeepOnMotionCheck1.CheckedChanged += new System.EventHandler(this.BeepOnMotionCheck1_CheckedChanged);
            // 
            // RecordingPathInput
            // 
            this.RecordingPathInput.Location = new System.Drawing.Point(762, 143);
            this.RecordingPathInput.Name = "RecordingPathInput";
            this.RecordingPathInput.ReadOnly = true;
            this.RecordingPathInput.Size = new System.Drawing.Size(169, 22);
            this.RecordingPathInput.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.ImageIndex = 0;
            this.button1.Location = new System.Drawing.Point(113, 471);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(145, 26);
            this.button1.TabIndex = 1;
            this.button1.Text = "Record";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Black;
            this.pictureBox1.Location = new System.Drawing.Point(23, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(339, 230);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(997, 573);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(188, 119);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1206, 717);
            this.Controls.Add(this.RecordingPathInput);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.button1);
            this.MinimumSize = new System.Drawing.Size(800, 557);
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox AutoRecord1;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.CheckBox BeepOnMotionCheck1;
        private System.Windows.Forms.CheckBox MotionDetection1;
        private System.Windows.Forms.TextBox RecordingPathInput;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

