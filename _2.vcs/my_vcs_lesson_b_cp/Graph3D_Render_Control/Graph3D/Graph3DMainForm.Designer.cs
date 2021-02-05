namespace Plot3D
{
    partial class Graph3DMainForm
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
            this.trackRho = new System.Windows.Forms.TrackBar();
            this.trackTheta = new System.Windows.Forms.TrackBar();
            this.trackPhi = new System.Windows.Forms.TrackBar();
            this.lblPolygons = new System.Windows.Forms.Label();
            this.comboColors = new System.Windows.Forms.ComboBox();
            this.checkAutoFitScreen = new System.Windows.Forms.CheckBox();
            this.comboDataSrc = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.comboRaster = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.graph3D = new Plot3D.Graph3D();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.trackRho)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackTheta)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackPhi)).BeginInit();
            this.SuspendLayout();
            // 
            // trackRho
            // 
            this.trackRho.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.trackRho.Location = new System.Drawing.Point(9, 182);
            this.trackRho.Name = "trackRho";
            this.trackRho.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.trackRho.Size = new System.Drawing.Size(45, 510);
            this.trackRho.TabIndex = 0;
            this.trackRho.TickFrequency = 20;
            this.trackRho.TickStyle = System.Windows.Forms.TickStyle.None;
            // 
            // trackTheta
            // 
            this.trackTheta.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.trackTheta.Location = new System.Drawing.Point(53, 182);
            this.trackTheta.Name = "trackTheta";
            this.trackTheta.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.trackTheta.Size = new System.Drawing.Size(45, 510);
            this.trackTheta.TabIndex = 1;
            this.trackTheta.TickFrequency = 20;
            this.trackTheta.TickStyle = System.Windows.Forms.TickStyle.None;
            // 
            // trackPhi
            // 
            this.trackPhi.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.trackPhi.Location = new System.Drawing.Point(98, 182);
            this.trackPhi.Name = "trackPhi";
            this.trackPhi.Orientation = System.Windows.Forms.Orientation.Vertical;
            this.trackPhi.Size = new System.Drawing.Size(45, 510);
            this.trackPhi.TabIndex = 2;
            this.trackPhi.TickFrequency = 20;
            this.trackPhi.TickStyle = System.Windows.Forms.TickStyle.None;
            // 
            // lblPolygons
            // 
            this.lblPolygons.AutoSize = true;
            this.lblPolygons.Location = new System.Drawing.Point(8, 158);
            this.lblPolygons.Name = "lblPolygons";
            this.lblPolygons.Size = new System.Drawing.Size(53, 13);
            this.lblPolygons.TabIndex = 9;
            this.lblPolygons.Text = "Polygons:";
            // 
            // comboColors
            // 
            this.comboColors.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboColors.FormattingEnabled = true;
            this.comboColors.Location = new System.Drawing.Point(9, 66);
            this.comboColors.MaxDropDownItems = 30;
            this.comboColors.Name = "comboColors";
            this.comboColors.Size = new System.Drawing.Size(121, 21);
            this.comboColors.TabIndex = 10;
            this.comboColors.SelectedIndexChanged += new System.EventHandler(this.comboColors_SelectedIndexChanged);
            // 
            // checkAutoFitScreen
            // 
            this.checkAutoFitScreen.AutoSize = true;
            this.checkAutoFitScreen.Location = new System.Drawing.Point(10, 134);
            this.checkAutoFitScreen.Name = "checkAutoFitScreen";
            this.checkAutoFitScreen.Size = new System.Drawing.Size(99, 17);
            this.checkAutoFitScreen.TabIndex = 11;
            this.checkAutoFitScreen.Text = "Auto Fit Screen";
            this.checkAutoFitScreen.UseVisualStyleBackColor = true;
            this.checkAutoFitScreen.CheckedChanged += new System.EventHandler(this.checkFitScreen_CheckedChanged);
            // 
            // comboDataSrc
            // 
            this.comboDataSrc.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboDataSrc.FormattingEnabled = true;
            this.comboDataSrc.Items.AddRange(new object[] {
            "Callback",
            "Formula",
            "Fix Values"});
            this.comboDataSrc.Location = new System.Drawing.Point(9, 26);
            this.comboDataSrc.MaxDropDownItems = 30;
            this.comboDataSrc.Name = "comboDataSrc";
            this.comboDataSrc.Size = new System.Drawing.Size(121, 21);
            this.comboDataSrc.TabIndex = 12;
            this.comboDataSrc.SelectedIndexChanged += new System.EventHandler(this.comboDataSrc_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.ForeColor = System.Drawing.Color.Blue;
            this.label1.Location = new System.Drawing.Point(137, 696);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(514, 13);
            this.label1.TabIndex = 13;
            this.label1.Text = "Left mouse button : Elevate,  Right mouse: Rotate,  Left mouse + SHIFT: Move,  Le" +
    "ft mouse + CTRL: Zoom";
            // 
            // comboRaster
            // 
            this.comboRaster.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboRaster.FormattingEnabled = true;
            this.comboRaster.Location = new System.Drawing.Point(9, 105);
            this.comboRaster.MaxDropDownItems = 30;
            this.comboRaster.Name = "comboRaster";
            this.comboRaster.Size = new System.Drawing.Size(121, 21);
            this.comboRaster.TabIndex = 14;
            this.comboRaster.SelectedIndexChanged += new System.EventHandler(this.comboRaster_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(7, 11);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(70, 13);
            this.label2.TabIndex = 15;
            this.label2.Text = "Data Source:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(7, 50);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(76, 13);
            this.label3.TabIndex = 16;
            this.label3.Text = "Color Scheme:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(7, 90);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(98, 13);
            this.label4.TabIndex = 17;
            this.label4.Text = "Coordinate System:";
            // 
            // graph3D
            // 
            this.graph3D.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.graph3D.BackColor = System.Drawing.Color.White;
            this.graph3D.Cursor = System.Windows.Forms.Cursors.Default;
            this.graph3D.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.graph3D.Location = new System.Drawing.Point(139, 11);
            this.graph3D.Name = "graph3D";
            this.graph3D.Size = new System.Drawing.Size(656, 682);
            this.graph3D.TabIndex = 6;
            // 
            // label5
            // 
            this.label5.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(7, 696);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(27, 13);
            this.label5.TabIndex = 18;
            this.label5.Text = "Rho";
            // 
            // label6
            // 
            this.label6.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(49, 696);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(35, 13);
            this.label6.TabIndex = 19;
            this.label6.Text = "Theta";
            // 
            // label7
            // 
            this.label7.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(99, 696);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(22, 13);
            this.label7.TabIndex = 20;
            this.label7.Text = "Phi";
            // 
            // Graph3DMainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(807, 715);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.comboRaster);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.comboDataSrc);
            this.Controls.Add(this.checkAutoFitScreen);
            this.Controls.Add(this.comboColors);
            this.Controls.Add(this.lblPolygons);
            this.Controls.Add(this.graph3D);
            this.Controls.Add(this.trackPhi);
            this.Controls.Add(this.trackTheta);
            this.Controls.Add(this.trackRho);
            this.MinimumSize = new System.Drawing.Size(400, 400);
            this.Name = "Graph3DMainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Graph3D Demo";
            ((System.ComponentModel.ISupportInitialize)(this.trackRho)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackTheta)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackPhi)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TrackBar trackRho;
        private System.Windows.Forms.TrackBar trackTheta;
        private System.Windows.Forms.TrackBar trackPhi;
        private Plot3D.Graph3D graph3D;
        private System.Windows.Forms.Label lblPolygons;
        private System.Windows.Forms.ComboBox comboColors;
        private System.Windows.Forms.CheckBox checkAutoFitScreen;
        private System.Windows.Forms.ComboBox comboDataSrc;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox comboRaster;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;

    }
}

