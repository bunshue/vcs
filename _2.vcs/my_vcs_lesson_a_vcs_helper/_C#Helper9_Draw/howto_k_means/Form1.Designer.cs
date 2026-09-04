namespace howto_k_means
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
            this.picItems = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.txtNumClusters = new System.Windows.Forms.TextBox();
            this.btnMakeClusters = new System.Windows.Forms.Button();
            this.btnMakePoints = new System.Windows.Forms.Button();
            this.txtNumPoints = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tmrUpdate = new System.Windows.Forms.Timer(this.components);
            this.btnClear = new System.Windows.Forms.Button();
            this.hscrFps = new System.Windows.Forms.HScrollBar();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.lb_fps = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picItems)).BeginInit();
            this.SuspendLayout();
            // 
            // picItems
            // 
            this.picItems.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.picItems.BackColor = System.Drawing.Color.White;
            this.picItems.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picItems.Location = new System.Drawing.Point(12, 85);
            this.picItems.Name = "picItems";
            this.picItems.Size = new System.Drawing.Size(795, 549);
            this.picItems.TabIndex = 0;
            this.picItems.TabStop = false;
            this.picItems.Paint += new System.Windows.Forms.PaintEventHandler(this.picItems_Paint);
            this.picItems.MouseClick += new System.Windows.Forms.MouseEventHandler(this.picItems_MouseClick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(12, 49);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(87, 19);
            this.label1.TabIndex = 1;
            this.label1.Text = "# Clusters:";
            // 
            // txtNumClusters
            // 
            this.txtNumClusters.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.txtNumClusters.Location = new System.Drawing.Point(104, 46);
            this.txtNumClusters.Name = "txtNumClusters";
            this.txtNumClusters.Size = new System.Drawing.Size(45, 30);
            this.txtNumClusters.TabIndex = 2;
            this.txtNumClusters.Text = "3";
            this.txtNumClusters.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // btnMakeClusters
            // 
            this.btnMakeClusters.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnMakeClusters.Location = new System.Drawing.Point(211, 44);
            this.btnMakeClusters.Name = "btnMakeClusters";
            this.btnMakeClusters.Size = new System.Drawing.Size(140, 36);
            this.btnMakeClusters.TabIndex = 3;
            this.btnMakeClusters.Text = "Make Clusters";
            this.btnMakeClusters.UseVisualStyleBackColor = true;
            this.btnMakeClusters.Click += new System.EventHandler(this.btnMakeClusters_Click);
            // 
            // btnMakePoints
            // 
            this.btnMakePoints.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnMakePoints.Location = new System.Drawing.Point(211, 4);
            this.btnMakePoints.Name = "btnMakePoints";
            this.btnMakePoints.Size = new System.Drawing.Size(140, 36);
            this.btnMakePoints.TabIndex = 1;
            this.btnMakePoints.Text = "Make Points";
            this.btnMakePoints.UseVisualStyleBackColor = true;
            this.btnMakePoints.Click += new System.EventHandler(this.btnMakePoints_Click);
            // 
            // txtNumPoints
            // 
            this.txtNumPoints.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.txtNumPoints.Location = new System.Drawing.Point(104, 6);
            this.txtNumPoints.Name = "txtNumPoints";
            this.txtNumPoints.Size = new System.Drawing.Size(45, 30);
            this.txtNumPoints.TabIndex = 0;
            this.txtNumPoints.Text = "200";
            this.txtNumPoints.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(12, 10);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(73, 19);
            this.label2.TabIndex = 4;
            this.label2.Text = "# Points:";
            // 
            // tmrUpdate
            // 
            this.tmrUpdate.Interval = 500;
            this.tmrUpdate.Tick += new System.EventHandler(this.tmrUpdate_Tick);
            // 
            // btnClear
            // 
            this.btnClear.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnClear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnClear.Location = new System.Drawing.Point(364, 4);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(140, 36);
            this.btnClear.TabIndex = 6;
            this.btnClear.Text = "Clear";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // hscrFps
            // 
            this.hscrFps.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.hscrFps.Location = new System.Drawing.Point(104, 650);
            this.hscrFps.Maximum = 209;
            this.hscrFps.Minimum = 1;
            this.hscrFps.Name = "hscrFps";
            this.hscrFps.Size = new System.Drawing.Size(703, 17);
            this.hscrFps.TabIndex = 7;
            this.hscrFps.Value = 20;
            this.hscrFps.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hscrFps_Scroll);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(813, 85);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(275, 549);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            // 
            // lb_fps
            // 
            this.lb_fps.AutoSize = true;
            this.lb_fps.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_fps.Location = new System.Drawing.Point(21, 648);
            this.lb_fps.Name = "lb_fps";
            this.lb_fps.Size = new System.Drawing.Size(31, 19);
            this.lb_fps.TabIndex = 11;
            this.lb_fps.Text = "fps";
            this.lb_fps.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnMakePoints;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1115, 683);
            this.Controls.Add(this.lb_fps);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.hscrFps);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.btnMakePoints);
            this.Controls.Add(this.txtNumPoints);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnMakeClusters);
            this.Controls.Add(this.txtNumClusters);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picItems);
            this.Name = "Form1";
            this.Text = "howto_k_means";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picItems)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picItems;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtNumClusters;
        private System.Windows.Forms.Button btnMakeClusters;
        private System.Windows.Forms.Button btnMakePoints;
        private System.Windows.Forms.TextBox txtNumPoints;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Timer tmrUpdate;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.HScrollBar hscrFps;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label lb_fps;
    }
}

