namespace vcs_ReadWrite_DICOM
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
            this.bnOpen1 = new System.Windows.Forms.Button();
            this.bnSave = new System.Windows.Forms.Button();
            this.bnTags = new System.Windows.Forms.Button();
            this.bnResetWL = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.gbViewSettings = new System.Windows.Forms.GroupBox();
            this.rbZoomfit = new System.Windows.Forms.RadioButton();
            this.rbZoom1_1 = new System.Windows.Forms.RadioButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bnOpen2 = new System.Windows.Forms.Button();
            this.windowLevelControl = new vcs_ReadWrite_DICOM.WindowLevelGraphControl();
            this.imagePanelControl = new vcs_ReadWrite_DICOM.ImagePanelControl();
            this.bt_clear = new System.Windows.Forms.Button();
            this.gbViewSettings.SuspendLayout();
            this.SuspendLayout();
            // 
            // bnOpen1
            // 
            this.bnOpen1.Location = new System.Drawing.Point(24, 8);
            this.bnOpen1.Name = "bnOpen1";
            this.bnOpen1.Size = new System.Drawing.Size(150, 50);
            this.bnOpen1.TabIndex = 0;
            this.bnOpen1.Text = "Open DICOM Image 1";
            this.bnOpen1.UseVisualStyleBackColor = true;
            this.bnOpen1.Click += new System.EventHandler(this.bnOpen_Click);
            // 
            // bnSave
            // 
            this.bnSave.Location = new System.Drawing.Point(24, 174);
            this.bnSave.Name = "bnSave";
            this.bnSave.Size = new System.Drawing.Size(150, 50);
            this.bnSave.TabIndex = 2;
            this.bnSave.Text = "Save as PNG";
            this.bnSave.UseVisualStyleBackColor = true;
            this.bnSave.Click += new System.EventHandler(this.bnSave_Click);
            // 
            // bnTags
            // 
            this.bnTags.Location = new System.Drawing.Point(24, 118);
            this.bnTags.Name = "bnTags";
            this.bnTags.Size = new System.Drawing.Size(150, 50);
            this.bnTags.TabIndex = 1;
            this.bnTags.Text = "View DICOM Tags";
            this.bnTags.UseVisualStyleBackColor = true;
            this.bnTags.Click += new System.EventHandler(this.bnTags_Click);
            // 
            // bnResetWL
            // 
            this.bnResetWL.Location = new System.Drawing.Point(24, 231);
            this.bnResetWL.Name = "bnResetWL";
            this.bnResetWL.Size = new System.Drawing.Size(150, 50);
            this.bnResetWL.TabIndex = 3;
            this.bnResetWL.Text = "Reset Window/Level";
            this.bnResetWL.UseVisualStyleBackColor = true;
            this.bnResetWL.Click += new System.EventHandler(this.bnResetWL_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.ForeColor = System.Drawing.Color.DarkBlue;
            this.label5.Location = new System.Drawing.Point(19, 577);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(124, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Right Drag on Image";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.ForeColor = System.Drawing.Color.DarkBlue;
            this.label6.Location = new System.Drawing.Point(22, 592);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(108, 13);
            this.label6.TabIndex = 9;
            this.label6.Text = "to Window / Level";
            this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.ForeColor = System.Drawing.Color.DarkBlue;
            this.label7.Location = new System.Drawing.Point(19, 615);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(114, 13);
            this.label7.TabIndex = 11;
            this.label7.Text = "Up: Decrease Level";
            this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label8.ForeColor = System.Drawing.Color.DarkBlue;
            this.label8.Location = new System.Drawing.Point(19, 629);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(127, 13);
            this.label8.TabIndex = 12;
            this.label8.Text = "Down: Increase Level";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label9.ForeColor = System.Drawing.Color.DarkBlue;
            this.label9.Location = new System.Drawing.Point(19, 642);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(124, 13);
            this.label9.TabIndex = 13;
            this.label9.Text = "Left: Decrease Width";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label10.ForeColor = System.Drawing.Color.DarkBlue;
            this.label10.Location = new System.Drawing.Point(19, 656);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(129, 13);
            this.label10.TabIndex = 14;
            this.label10.Text = "Right: Increase Width";
            this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // gbViewSettings
            // 
            this.gbViewSettings.Controls.Add(this.rbZoomfit);
            this.gbViewSettings.Controls.Add(this.rbZoom1_1);
            this.gbViewSettings.Location = new System.Drawing.Point(24, 291);
            this.gbViewSettings.Name = "gbViewSettings";
            this.gbViewSettings.Size = new System.Drawing.Size(145, 58);
            this.gbViewSettings.TabIndex = 5;
            this.gbViewSettings.TabStop = false;
            this.gbViewSettings.Text = "View Settings";
            // 
            // rbZoomfit
            // 
            this.rbZoomfit.AutoSize = true;
            this.rbZoomfit.Checked = true;
            this.rbZoomfit.Location = new System.Drawing.Point(16, 34);
            this.rbZoomfit.Name = "rbZoomfit";
            this.rbZoomfit.Size = new System.Drawing.Size(78, 16);
            this.rbZoomfit.TabIndex = 1;
            this.rbZoomfit.TabStop = true;
            this.rbZoomfit.Text = "Zoom to Fit";
            this.rbZoomfit.UseVisualStyleBackColor = true;
            this.rbZoomfit.CheckedChanged += new System.EventHandler(this.viewSettingsCheckedChanged);
            // 
            // rbZoom1_1
            // 
            this.rbZoom1_1.AutoSize = true;
            this.rbZoom1_1.Location = new System.Drawing.Point(16, 16);
            this.rbZoom1_1.Name = "rbZoom1_1";
            this.rbZoom1_1.Size = new System.Drawing.Size(38, 16);
            this.rbZoom1_1.TabIndex = 0;
            this.rbZoom1_1.Text = "1:1";
            this.rbZoom1_1.UseVisualStyleBackColor = true;
            this.rbZoom1_1.CheckedChanged += new System.EventHandler(this.viewSettingsCheckedChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(1037, 8);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(254, 600);
            this.richTextBox1.TabIndex = 15;
            this.richTextBox1.Text = "";
            // 
            // bnOpen2
            // 
            this.bnOpen2.Location = new System.Drawing.Point(24, 63);
            this.bnOpen2.Name = "bnOpen2";
            this.bnOpen2.Size = new System.Drawing.Size(150, 50);
            this.bnOpen2.TabIndex = 16;
            this.bnOpen2.Text = "Open DICOM Image 2";
            this.bnOpen2.UseVisualStyleBackColor = true;
            this.bnOpen2.Click += new System.EventHandler(this.bnOpen2_Click);
            // 
            // windowLevelControl
            // 
            this.windowLevelControl.Location = new System.Drawing.Point(10, 355);
            this.windowLevelControl.Name = "windowLevelControl";
            this.windowLevelControl.Size = new System.Drawing.Size(165, 217);
            this.windowLevelControl.TabIndex = 10;
            // 
            // imagePanelControl
            // 
            this.imagePanelControl.AutoValidate = System.Windows.Forms.AutoValidate.Disable;
            this.imagePanelControl.BackColor = System.Drawing.SystemColors.Control;
            this.imagePanelControl.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.imagePanelControl.CausesValidation = false;
            this.imagePanelControl.Location = new System.Drawing.Point(205, 8);
            this.imagePanelControl.Name = "imagePanelControl";
            this.imagePanelControl.Size = new System.Drawing.Size(800, 600);
            this.imagePanelControl.TabIndex = 1;
            this.imagePanelControl.TabStop = false;
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1216, 565);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(75, 38);
            this.bt_clear.TabIndex = 17;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1303, 724);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.bnOpen2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.gbViewSettings);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.windowLevelControl);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.bnResetWL);
            this.Controls.Add(this.bnSave);
            this.Controls.Add(this.bnTags);
            this.Controls.Add(this.imagePanelControl);
            this.Controls.Add(this.bnOpen1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "DICOM Image Viewer";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.gbViewSettings.ResumeLayout(false);
            this.gbViewSettings.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bnOpen1;
        private ImagePanelControl imagePanelControl;
        private System.Windows.Forms.Button bnSave;
        private System.Windows.Forms.Button bnTags;
        private System.Windows.Forms.Button bnResetWL;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private WindowLevelGraphControl windowLevelControl;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.GroupBox gbViewSettings;
        private System.Windows.Forms.RadioButton rbZoomfit;
        private System.Windows.Forms.RadioButton rbZoom1_1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bnOpen2;
        private System.Windows.Forms.Button bt_clear;

    }
}

