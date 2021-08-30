namespace DicomImageViewer
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
            this.bnOpen = new System.Windows.Forms.Button();
            this.bnSave = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
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
            this.windowLevelControl = new DicomImageViewer.WindowLevelGraphControl();
            this.imagePanelControl = new DicomImageViewer.ImagePanelControl();
            this.gbViewSettings.SuspendLayout();
            this.SuspendLayout();
            // 
            // bnOpen
            // 
            this.bnOpen.Location = new System.Drawing.Point(35, 12);
            this.bnOpen.Name = "bnOpen";
            this.bnOpen.Size = new System.Drawing.Size(117, 28);
            this.bnOpen.TabIndex = 0;
            this.bnOpen.Text = "Open DICOM Image";
            this.bnOpen.UseVisualStyleBackColor = true;
            this.bnOpen.Click += new System.EventHandler(this.bnOpen_Click);
            // 
            // bnSave
            // 
            this.bnSave.Location = new System.Drawing.Point(35, 74);
            this.bnSave.Name = "bnSave";
            this.bnSave.Size = new System.Drawing.Size(117, 28);
            this.bnSave.TabIndex = 2;
            this.bnSave.Text = "Save as PNG";
            this.bnSave.UseVisualStyleBackColor = true;
            this.bnSave.Click += new System.EventHandler(this.bnSave_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 225);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(73, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Image Size:";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 242);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(35, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "label2";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(12, 266);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(102, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Image Bit Depth:";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 283);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(35, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "label4";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // bnTags
            // 
            this.bnTags.Location = new System.Drawing.Point(35, 43);
            this.bnTags.Name = "bnTags";
            this.bnTags.Size = new System.Drawing.Size(117, 28);
            this.bnTags.TabIndex = 1;
            this.bnTags.Text = "View DICOM Tags";
            this.bnTags.UseVisualStyleBackColor = true;
            this.bnTags.Click += new System.EventHandler(this.bnTags_Click);
            // 
            // bnResetWL
            // 
            this.bnResetWL.Location = new System.Drawing.Point(35, 105);
            this.bnResetWL.Name = "bnResetWL";
            this.bnResetWL.Size = new System.Drawing.Size(117, 28);
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
            this.label5.Location = new System.Drawing.Point(19, 560);
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
            this.label6.Location = new System.Drawing.Point(22, 576);
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
            this.label7.Location = new System.Drawing.Point(19, 601);
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
            this.label8.Location = new System.Drawing.Point(19, 616);
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
            this.label9.Location = new System.Drawing.Point(19, 631);
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
            this.label10.Location = new System.Drawing.Point(19, 646);
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
            this.gbViewSettings.Location = new System.Drawing.Point(12, 143);
            this.gbViewSettings.Name = "gbViewSettings";
            this.gbViewSettings.Size = new System.Drawing.Size(145, 63);
            this.gbViewSettings.TabIndex = 5;
            this.gbViewSettings.TabStop = false;
            this.gbViewSettings.Text = "View Settings";
            // 
            // rbZoomfit
            // 
            this.rbZoomfit.AutoSize = true;
            this.rbZoomfit.Checked = true;
            this.rbZoomfit.Location = new System.Drawing.Point(16, 37);
            this.rbZoomfit.Name = "rbZoomfit";
            this.rbZoomfit.Size = new System.Drawing.Size(78, 17);
            this.rbZoomfit.TabIndex = 1;
            this.rbZoomfit.TabStop = true;
            this.rbZoomfit.Text = "Zoom to Fit";
            this.rbZoomfit.UseVisualStyleBackColor = true;
            this.rbZoomfit.CheckedChanged += new System.EventHandler(this.viewSettingsCheckedChanged);
            // 
            // rbZoom1_1
            // 
            this.rbZoom1_1.AutoSize = true;
            this.rbZoom1_1.Location = new System.Drawing.Point(16, 17);
            this.rbZoom1_1.Name = "rbZoom1_1";
            this.rbZoom1_1.Size = new System.Drawing.Size(40, 17);
            this.rbZoom1_1.TabIndex = 0;
            this.rbZoom1_1.Text = "1:1";
            this.rbZoom1_1.UseVisualStyleBackColor = true;
            this.rbZoom1_1.CheckedChanged += new System.EventHandler(this.viewSettingsCheckedChanged);
            // 
            // windowLevelControl
            // 
            this.windowLevelControl.Location = new System.Drawing.Point(10, 300);
            this.windowLevelControl.Name = "windowLevelControl";
            this.windowLevelControl.Size = new System.Drawing.Size(165, 235);
            this.windowLevelControl.TabIndex = 10;
            // 
            // imagePanelControl
            // 
            this.imagePanelControl.AutoValidate = System.Windows.Forms.AutoValidate.Disable;
            this.imagePanelControl.BackColor = System.Drawing.SystemColors.Control;
            this.imagePanelControl.CausesValidation = false;
            this.imagePanelControl.Location = new System.Drawing.Point(185, 9);
            this.imagePanelControl.Name = "imagePanelControl";
            this.imagePanelControl.Size = new System.Drawing.Size(800, 647);
            this.imagePanelControl.TabIndex = 1;
            this.imagePanelControl.TabStop = false;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(994, 668);
            this.Controls.Add(this.gbViewSettings);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.windowLevelControl);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.bnResetWL);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.bnSave);
            this.Controls.Add(this.bnTags);
            this.Controls.Add(this.imagePanelControl);
            this.Controls.Add(this.bnOpen);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "DICOM Image Viewer";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainForm_FormClosing);
            this.gbViewSettings.ResumeLayout(false);
            this.gbViewSettings.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bnOpen;
        private ImagePanelControl imagePanelControl;
        private System.Windows.Forms.Button bnSave;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
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

    }
}

