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
            this.Display_Cam2 = new System.Windows.Forms.PictureBox();
            this.RecordButton2 = new System.Windows.Forms.Button();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.MotionDetection1 = new System.Windows.Forms.CheckBox();
            this.BeepOnMotionCheck1 = new System.Windows.Forms.CheckBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.MotionDetection2 = new System.Windows.Forms.CheckBox();
            this.BeepOnMotionCheck2 = new System.Windows.Forms.CheckBox();
            this.AutoRecord2 = new System.Windows.Forms.CheckBox();
            this.groupBox7 = new System.Windows.Forms.GroupBox();
            this.MotionDetection3 = new System.Windows.Forms.CheckBox();
            this.BeepOnMotionCheck3 = new System.Windows.Forms.CheckBox();
            this.AutoRecord3 = new System.Windows.Forms.CheckBox();
            this.groupBox8 = new System.Windows.Forms.GroupBox();
            this.MotionDetection4 = new System.Windows.Forms.CheckBox();
            this.BeepOnMotionCheck4 = new System.Windows.Forms.CheckBox();
            this.AutoRecord4 = new System.Windows.Forms.CheckBox();
            this.groupBox9 = new System.Windows.Forms.GroupBox();
            this.ChangePathButton = new System.Windows.Forms.Button();
            this.RecordingPathInput = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.RecordButton1 = new System.Windows.Forms.Button();
            this.Display_Cam1 = new System.Windows.Forms.PictureBox();
            this.Display_Cam3 = new System.Windows.Forms.PictureBox();
            this.RecordButton3 = new System.Windows.Forms.Button();
            this.Display_Cam4 = new System.Windows.Forms.PictureBox();
            this.RecordButton4 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam2)).BeginInit();
            this.groupBox5.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.groupBox7.SuspendLayout();
            this.groupBox8.SuspendLayout();
            this.groupBox9.SuspendLayout();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam4)).BeginInit();
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
            // Display_Cam2
            // 
            this.Display_Cam2.BackColor = System.Drawing.Color.Black;
            this.Display_Cam2.Location = new System.Drawing.Point(494, 41);
            this.Display_Cam2.Name = "Display_Cam2";
            this.Display_Cam2.Size = new System.Drawing.Size(277, 186);
            this.Display_Cam2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.Display_Cam2.TabIndex = 0;
            this.Display_Cam2.TabStop = false;
            // 
            // RecordButton2
            // 
            this.RecordButton2.ImageIndex = 0;
            this.RecordButton2.Location = new System.Drawing.Point(494, 244);
            this.RecordButton2.Name = "RecordButton2";
            this.RecordButton2.Size = new System.Drawing.Size(231, 26);
            this.RecordButton2.TabIndex = 1;
            this.RecordButton2.Text = "Record";
            this.RecordButton2.UseVisualStyleBackColor = true;
            this.RecordButton2.Click += new System.EventHandler(this.RecordButton2_Click);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.MotionDetection1);
            this.groupBox5.Controls.Add(this.BeepOnMotionCheck1);
            this.groupBox5.Controls.Add(this.AutoRecord1);
            this.groupBox5.Location = new System.Drawing.Point(13, 12);
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
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.MotionDetection2);
            this.groupBox6.Controls.Add(this.BeepOnMotionCheck2);
            this.groupBox6.Controls.Add(this.AutoRecord2);
            this.groupBox6.Location = new System.Drawing.Point(13, 111);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(182, 93);
            this.groupBox6.TabIndex = 1;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "Camera 2";
            // 
            // MotionDetection2
            // 
            this.MotionDetection2.AutoSize = true;
            this.MotionDetection2.Location = new System.Drawing.Point(6, 18);
            this.MotionDetection2.Name = "MotionDetection2";
            this.MotionDetection2.Size = new System.Drawing.Size(105, 16);
            this.MotionDetection2.TabIndex = 4;
            this.MotionDetection2.Text = "Motion Detection";
            this.MotionDetection2.UseVisualStyleBackColor = true;
            this.MotionDetection2.CheckedChanged += new System.EventHandler(this.MotionDetection2_CheckedChanged);
            // 
            // BeepOnMotionCheck2
            // 
            this.BeepOnMotionCheck2.AutoSize = true;
            this.BeepOnMotionCheck2.Location = new System.Drawing.Point(6, 72);
            this.BeepOnMotionCheck2.Name = "BeepOnMotionCheck2";
            this.BeepOnMotionCheck2.Size = new System.Drawing.Size(102, 16);
            this.BeepOnMotionCheck2.TabIndex = 3;
            this.BeepOnMotionCheck2.Text = "Beep On Motion";
            this.BeepOnMotionCheck2.UseVisualStyleBackColor = true;
            this.BeepOnMotionCheck2.CheckedChanged += new System.EventHandler(this.BeepOnMotionCheck2_CheckedChanged);
            // 
            // AutoRecord2
            // 
            this.AutoRecord2.AutoSize = true;
            this.AutoRecord2.Location = new System.Drawing.Point(6, 39);
            this.AutoRecord2.Name = "AutoRecord2";
            this.AutoRecord2.Size = new System.Drawing.Size(121, 28);
            this.AutoRecord2.TabIndex = 2;
            this.AutoRecord2.Text = "Automaticly Record \r\nIf Motion Detected";
            this.AutoRecord2.UseVisualStyleBackColor = true;
            this.AutoRecord2.CheckedChanged += new System.EventHandler(this.AutoRecord2_CheckedChanged);
            // 
            // groupBox7
            // 
            this.groupBox7.Controls.Add(this.MotionDetection3);
            this.groupBox7.Controls.Add(this.BeepOnMotionCheck3);
            this.groupBox7.Controls.Add(this.AutoRecord3);
            this.groupBox7.Location = new System.Drawing.Point(13, 210);
            this.groupBox7.Name = "groupBox7";
            this.groupBox7.Size = new System.Drawing.Size(182, 93);
            this.groupBox7.TabIndex = 1;
            this.groupBox7.TabStop = false;
            this.groupBox7.Text = "Camera 3";
            // 
            // MotionDetection3
            // 
            this.MotionDetection3.AutoSize = true;
            this.MotionDetection3.Location = new System.Drawing.Point(6, 18);
            this.MotionDetection3.Name = "MotionDetection3";
            this.MotionDetection3.Size = new System.Drawing.Size(105, 16);
            this.MotionDetection3.TabIndex = 4;
            this.MotionDetection3.Text = "Motion Detection";
            this.MotionDetection3.UseVisualStyleBackColor = true;
            this.MotionDetection3.CheckedChanged += new System.EventHandler(this.MotionDetection3_CheckedChanged);
            // 
            // BeepOnMotionCheck3
            // 
            this.BeepOnMotionCheck3.AutoSize = true;
            this.BeepOnMotionCheck3.Location = new System.Drawing.Point(6, 72);
            this.BeepOnMotionCheck3.Name = "BeepOnMotionCheck3";
            this.BeepOnMotionCheck3.Size = new System.Drawing.Size(102, 16);
            this.BeepOnMotionCheck3.TabIndex = 3;
            this.BeepOnMotionCheck3.Text = "Beep On Motion";
            this.BeepOnMotionCheck3.UseVisualStyleBackColor = true;
            this.BeepOnMotionCheck3.CheckedChanged += new System.EventHandler(this.BeepOnMotionCheck3_CheckedChanged);
            // 
            // AutoRecord3
            // 
            this.AutoRecord3.AutoSize = true;
            this.AutoRecord3.Location = new System.Drawing.Point(6, 39);
            this.AutoRecord3.Name = "AutoRecord3";
            this.AutoRecord3.Size = new System.Drawing.Size(121, 28);
            this.AutoRecord3.TabIndex = 2;
            this.AutoRecord3.Text = "Automaticly Record \r\nIf Motion Detected";
            this.AutoRecord3.UseVisualStyleBackColor = true;
            this.AutoRecord3.CheckedChanged += new System.EventHandler(this.AutoRecord3_CheckedChanged);
            // 
            // groupBox8
            // 
            this.groupBox8.Controls.Add(this.MotionDetection4);
            this.groupBox8.Controls.Add(this.BeepOnMotionCheck4);
            this.groupBox8.Controls.Add(this.AutoRecord4);
            this.groupBox8.Location = new System.Drawing.Point(13, 308);
            this.groupBox8.Name = "groupBox8";
            this.groupBox8.Size = new System.Drawing.Size(182, 93);
            this.groupBox8.TabIndex = 1;
            this.groupBox8.TabStop = false;
            this.groupBox8.Text = "Camera 4";
            // 
            // MotionDetection4
            // 
            this.MotionDetection4.AutoSize = true;
            this.MotionDetection4.Location = new System.Drawing.Point(6, 18);
            this.MotionDetection4.Name = "MotionDetection4";
            this.MotionDetection4.Size = new System.Drawing.Size(105, 16);
            this.MotionDetection4.TabIndex = 4;
            this.MotionDetection4.Text = "Motion Detection";
            this.MotionDetection4.UseVisualStyleBackColor = true;
            this.MotionDetection4.CheckedChanged += new System.EventHandler(this.MotionDetection4_CheckedChanged);
            // 
            // BeepOnMotionCheck4
            // 
            this.BeepOnMotionCheck4.AutoSize = true;
            this.BeepOnMotionCheck4.Location = new System.Drawing.Point(6, 72);
            this.BeepOnMotionCheck4.Name = "BeepOnMotionCheck4";
            this.BeepOnMotionCheck4.Size = new System.Drawing.Size(102, 16);
            this.BeepOnMotionCheck4.TabIndex = 3;
            this.BeepOnMotionCheck4.Text = "Beep On Motion";
            this.BeepOnMotionCheck4.UseVisualStyleBackColor = true;
            this.BeepOnMotionCheck4.CheckedChanged += new System.EventHandler(this.BeepOnMotionCheck4_CheckedChanged);
            // 
            // AutoRecord4
            // 
            this.AutoRecord4.AutoSize = true;
            this.AutoRecord4.Location = new System.Drawing.Point(6, 39);
            this.AutoRecord4.Name = "AutoRecord4";
            this.AutoRecord4.Size = new System.Drawing.Size(121, 28);
            this.AutoRecord4.TabIndex = 2;
            this.AutoRecord4.Text = "Automaticly Record \r\nIf Motion Detected";
            this.AutoRecord4.UseVisualStyleBackColor = true;
            this.AutoRecord4.CheckedChanged += new System.EventHandler(this.AutoRecord4_CheckedChanged);
            // 
            // groupBox9
            // 
            this.groupBox9.Controls.Add(this.ChangePathButton);
            this.groupBox9.Controls.Add(this.RecordingPathInput);
            this.groupBox9.Location = new System.Drawing.Point(13, 407);
            this.groupBox9.Name = "groupBox9";
            this.groupBox9.Size = new System.Drawing.Size(181, 93);
            this.groupBox9.TabIndex = 2;
            this.groupBox9.TabStop = false;
            this.groupBox9.Text = "Records Path";
            // 
            // ChangePathButton
            // 
            this.ChangePathButton.Location = new System.Drawing.Point(6, 40);
            this.ChangePathButton.Name = "ChangePathButton";
            this.ChangePathButton.Size = new System.Drawing.Size(169, 21);
            this.ChangePathButton.TabIndex = 1;
            this.ChangePathButton.Text = "Change";
            this.ChangePathButton.UseVisualStyleBackColor = true;
            this.ChangePathButton.Click += new System.EventHandler(this.ChangeRecordingPath);
            // 
            // RecordingPathInput
            // 
            this.RecordingPathInput.Location = new System.Drawing.Point(6, 18);
            this.RecordingPathInput.Name = "RecordingPathInput";
            this.RecordingPathInput.ReadOnly = true;
            this.RecordingPathInput.Size = new System.Drawing.Size(169, 22);
            this.RecordingPathInput.TabIndex = 0;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.groupBox5);
            this.panel1.Controls.Add(this.groupBox6);
            this.panel1.Controls.Add(this.groupBox9);
            this.panel1.Controls.Add(this.groupBox7);
            this.panel1.Controls.Add(this.groupBox8);
            this.panel1.Location = new System.Drawing.Point(997, 29);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(213, 519);
            this.panel1.TabIndex = 4;
            // 
            // RecordButton1
            // 
            this.RecordButton1.ImageIndex = 0;
            this.RecordButton1.Location = new System.Drawing.Point(124, 248);
            this.RecordButton1.Name = "RecordButton1";
            this.RecordButton1.Size = new System.Drawing.Size(145, 26);
            this.RecordButton1.TabIndex = 1;
            this.RecordButton1.Text = "Record";
            this.RecordButton1.UseVisualStyleBackColor = true;
            this.RecordButton1.Click += new System.EventHandler(this.RecordButton1_Click);
            // 
            // Display_Cam1
            // 
            this.Display_Cam1.BackColor = System.Drawing.Color.Black;
            this.Display_Cam1.Location = new System.Drawing.Point(23, 12);
            this.Display_Cam1.Name = "Display_Cam1";
            this.Display_Cam1.Size = new System.Drawing.Size(339, 230);
            this.Display_Cam1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.Display_Cam1.TabIndex = 0;
            this.Display_Cam1.TabStop = false;
            // 
            // Display_Cam3
            // 
            this.Display_Cam3.BackColor = System.Drawing.Color.Black;
            this.Display_Cam3.Location = new System.Drawing.Point(36, 357);
            this.Display_Cam3.Name = "Display_Cam3";
            this.Display_Cam3.Size = new System.Drawing.Size(259, 191);
            this.Display_Cam3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.Display_Cam3.TabIndex = 0;
            this.Display_Cam3.TabStop = false;
            // 
            // RecordButton3
            // 
            this.RecordButton3.ImageIndex = 0;
            this.RecordButton3.Location = new System.Drawing.Point(36, 573);
            this.RecordButton3.Name = "RecordButton3";
            this.RecordButton3.Size = new System.Drawing.Size(232, 26);
            this.RecordButton3.TabIndex = 1;
            this.RecordButton3.Text = "Record";
            this.RecordButton3.UseVisualStyleBackColor = true;
            this.RecordButton3.Click += new System.EventHandler(this.RecordButton3_Click);
            // 
            // Display_Cam4
            // 
            this.Display_Cam4.BackColor = System.Drawing.Color.Black;
            this.Display_Cam4.Location = new System.Drawing.Point(494, 317);
            this.Display_Cam4.Name = "Display_Cam4";
            this.Display_Cam4.Size = new System.Drawing.Size(288, 184);
            this.Display_Cam4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.Display_Cam4.TabIndex = 0;
            this.Display_Cam4.TabStop = false;
            // 
            // RecordButton4
            // 
            this.RecordButton4.ImageIndex = 0;
            this.RecordButton4.Location = new System.Drawing.Point(494, 532);
            this.RecordButton4.Name = "RecordButton4";
            this.RecordButton4.Size = new System.Drawing.Size(206, 26);
            this.RecordButton4.TabIndex = 1;
            this.RecordButton4.Text = "Record";
            this.RecordButton4.UseVisualStyleBackColor = true;
            this.RecordButton4.Click += new System.EventHandler(this.RecordButton4_Click);
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
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.RecordButton4);
            this.Controls.Add(this.RecordButton2);
            this.Controls.Add(this.Display_Cam4);
            this.Controls.Add(this.Display_Cam2);
            this.Controls.Add(this.RecordButton3);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.Display_Cam3);
            this.Controls.Add(this.Display_Cam1);
            this.Controls.Add(this.RecordButton1);
            this.MinimumSize = new System.Drawing.Size(800, 557);
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.StopCameras);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam2)).EndInit();
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox6.ResumeLayout(false);
            this.groupBox6.PerformLayout();
            this.groupBox7.ResumeLayout(false);
            this.groupBox7.PerformLayout();
            this.groupBox8.ResumeLayout(false);
            this.groupBox8.PerformLayout();
            this.groupBox9.ResumeLayout(false);
            this.groupBox9.PerformLayout();
            this.panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Display_Cam4)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox Display_Cam2;
        private System.Windows.Forms.CheckBox AutoRecord1;
        private System.Windows.Forms.Button RecordButton2;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.CheckBox BeepOnMotionCheck1;
        private System.Windows.Forms.CheckBox MotionDetection1;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.CheckBox MotionDetection2;
        private System.Windows.Forms.CheckBox BeepOnMotionCheck2;
        private System.Windows.Forms.CheckBox AutoRecord2;
        private System.Windows.Forms.GroupBox groupBox7;
        private System.Windows.Forms.CheckBox MotionDetection3;
        private System.Windows.Forms.CheckBox BeepOnMotionCheck3;
        private System.Windows.Forms.CheckBox AutoRecord3;
        private System.Windows.Forms.GroupBox groupBox8;
        private System.Windows.Forms.CheckBox MotionDetection4;
        private System.Windows.Forms.CheckBox BeepOnMotionCheck4;
        private System.Windows.Forms.CheckBox AutoRecord4;
        private System.Windows.Forms.GroupBox groupBox9;
        private System.Windows.Forms.Button ChangePathButton;
        private System.Windows.Forms.TextBox RecordingPathInput;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button RecordButton1;
        private System.Windows.Forms.PictureBox Display_Cam1;
        private System.Windows.Forms.PictureBox Display_Cam3;
        private System.Windows.Forms.Button RecordButton3;
        private System.Windows.Forms.PictureBox Display_Cam4;
        private System.Windows.Forms.Button RecordButton4;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

