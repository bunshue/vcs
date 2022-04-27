namespace vcs_ImageProcessing4
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.picToned = new System.Windows.Forms.PictureBox();
            this.picOriginal = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.picColor = new System.Windows.Forms.PictureBox();
            this.scrRed = new System.Windows.Forms.HScrollBar();
            this.scrGreen = new System.Windows.Forms.HScrollBar();
            this.label2 = new System.Windows.Forms.Label();
            this.scrBlue = new System.Windows.Forms.HScrollBar();
            this.label3 = new System.Windows.Forms.Label();
            this.scrBright = new System.Windows.Forms.HScrollBar();
            this.label4 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).BeginInit();
            this.SuspendLayout();
            // 
            // picToned
            // 
            this.picToned.Location = new System.Drawing.Point(318, 78);
            this.picToned.Name = "picToned";
            this.picToned.Size = new System.Drawing.Size(300, 400);
            this.picToned.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picToned.TabIndex = 4;
            this.picToned.TabStop = false;
            // 
            // picOriginal
            // 
            this.picOriginal.Image = ((System.Drawing.Image)(resources.GetObject("picOriginal.Image")));
            this.picOriginal.Location = new System.Drawing.Point(12, 78);
            this.picOriginal.Name = "picOriginal";
            this.picOriginal.Size = new System.Drawing.Size(305, 400);
            this.picOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picOriginal.TabIndex = 3;
            this.picOriginal.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 11);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(27, 12);
            this.label1.TabIndex = 5;
            this.label1.Text = "Red:";
            // 
            // picColor
            // 
            this.picColor.BackColor = System.Drawing.Color.LightBlue;
            this.picColor.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picColor.Cursor = System.Windows.Forms.Cursors.Hand;
            this.picColor.Location = new System.Drawing.Point(318, 11);
            this.picColor.Name = "picColor";
            this.picColor.Size = new System.Drawing.Size(68, 63);
            this.picColor.TabIndex = 6;
            this.picColor.TabStop = false;
            // 
            // scrRed
            // 
            this.scrRed.Location = new System.Drawing.Point(54, 11);
            this.scrRed.Maximum = 264;
            this.scrRed.Name = "scrRed";
            this.scrRed.Size = new System.Drawing.Size(258, 14);
            this.scrRed.TabIndex = 7;
            this.scrRed.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrColorComponent_Scroll);
            // 
            // scrGreen
            // 
            this.scrGreen.Location = new System.Drawing.Point(54, 29);
            this.scrGreen.Maximum = 264;
            this.scrGreen.Name = "scrGreen";
            this.scrGreen.Size = new System.Drawing.Size(258, 14);
            this.scrGreen.TabIndex = 9;
            this.scrGreen.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrColorComponent_Scroll);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 29);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(36, 12);
            this.label2.TabIndex = 8;
            this.label2.Text = "Green:";
            // 
            // scrBlue
            // 
            this.scrBlue.Location = new System.Drawing.Point(54, 46);
            this.scrBlue.Maximum = 264;
            this.scrBlue.Name = "scrBlue";
            this.scrBlue.Size = new System.Drawing.Size(258, 14);
            this.scrBlue.TabIndex = 11;
            this.scrBlue.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrColorComponent_Scroll);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 46);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(30, 12);
            this.label3.TabIndex = 10;
            this.label3.Text = "Blue:";
            // 
            // scrBright
            // 
            this.scrBright.Location = new System.Drawing.Point(54, 62);
            this.scrBright.Maximum = 264;
            this.scrBright.Name = "scrBright";
            this.scrBright.Size = new System.Drawing.Size(258, 14);
            this.scrBright.TabIndex = 13;
            this.scrBright.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrColorComponent_Scroll);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 62);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(38, 12);
            this.label4.TabIndex = 12;
            this.label4.Text = "Bright:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(716, 552);
            this.Controls.Add(this.scrBright);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.scrBlue);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.scrGreen);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.scrRed);
            this.Controls.Add(this.picColor);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picToned);
            this.Controls.Add(this.picOriginal);
            this.Name = "Form1";
            this.Text = "vcs_ImageProcessing4";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picToned)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picColor)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picToned;
        private System.Windows.Forms.PictureBox picOriginal;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox picColor;
        private System.Windows.Forms.HScrollBar scrRed;
        private System.Windows.Forms.HScrollBar scrGreen;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.HScrollBar scrBlue;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.HScrollBar scrBright;
        private System.Windows.Forms.Label label4;
    }
}

