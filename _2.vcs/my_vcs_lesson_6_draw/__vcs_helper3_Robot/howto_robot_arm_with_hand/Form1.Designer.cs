namespace howto_robot_arm_with_hand
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
            this.scrHand = new System.Windows.Forms.HScrollBar();
            this.scrJoint3 = new System.Windows.Forms.HScrollBar();
            this.scrJoint2 = new System.Windows.Forms.HScrollBar();
            this.scrJoint1 = new System.Windows.Forms.HScrollBar();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // scrHand
            // 
            this.scrHand.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.scrHand.LargeChange = 1;
            this.scrHand.Location = new System.Drawing.Point(8, 71);
            this.scrHand.Maximum = 20;
            this.scrHand.Name = "scrHand";
            this.scrHand.Size = new System.Drawing.Size(369, 17);
            this.scrHand.TabIndex = 20;
            this.scrHand.Value = 10;
            this.scrHand.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrJoint_Scroll);
            // 
            // scrJoint3
            // 
            this.scrJoint3.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.scrJoint3.Location = new System.Drawing.Point(8, 50);
            this.scrJoint3.Maximum = 169;
            this.scrJoint3.Minimum = -160;
            this.scrJoint3.Name = "scrJoint3";
            this.scrJoint3.Size = new System.Drawing.Size(369, 17);
            this.scrJoint3.TabIndex = 19;
            this.scrJoint3.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrJoint_Scroll);
            // 
            // scrJoint2
            // 
            this.scrJoint2.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.scrJoint2.Location = new System.Drawing.Point(8, 29);
            this.scrJoint2.Maximum = 169;
            this.scrJoint2.Minimum = -160;
            this.scrJoint2.Name = "scrJoint2";
            this.scrJoint2.Size = new System.Drawing.Size(369, 17);
            this.scrJoint2.TabIndex = 18;
            this.scrJoint2.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrJoint_Scroll);
            // 
            // scrJoint1
            // 
            this.scrJoint1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.scrJoint1.Location = new System.Drawing.Point(8, 8);
            this.scrJoint1.Maximum = 169;
            this.scrJoint1.Minimum = -160;
            this.scrJoint1.Name = "scrJoint1";
            this.scrJoint1.Size = new System.Drawing.Size(369, 17);
            this.scrJoint1.TabIndex = 17;
            this.scrJoint1.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrJoint_Scroll);
            // 
            // picCanvas
            // 
            this.picCanvas.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(8, 91);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(370, 370);
            this.picCanvas.TabIndex = 16;
            this.picCanvas.TabStop = false;
            this.picCanvas.Paint += new System.Windows.Forms.PaintEventHandler(this.picCanvas_Paint);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(387, 469);
            this.Controls.Add(this.scrHand);
            this.Controls.Add(this.scrJoint3);
            this.Controls.Add(this.scrJoint2);
            this.Controls.Add(this.scrJoint1);
            this.Controls.Add(this.picCanvas);
            this.Name = "Form1";
            this.Text = "howto_robot_arm_with_hand";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.HScrollBar scrHand;
        private System.Windows.Forms.HScrollBar scrJoint3;
        private System.Windows.Forms.HScrollBar scrJoint2;
        private System.Windows.Forms.HScrollBar scrJoint1;
        internal System.Windows.Forms.PictureBox picCanvas;
    }
}

