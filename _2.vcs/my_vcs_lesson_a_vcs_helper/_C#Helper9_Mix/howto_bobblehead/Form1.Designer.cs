namespace howto_bobblehead
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
            this.picBobble = new System.Windows.Forms.PictureBox();
            this.picHead = new System.Windows.Forms.PictureBox();
            this.picBody = new System.Windows.Forms.PictureBox();
            this.tmrBobble = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picBobble)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHead)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBody)).BeginInit();
            this.SuspendLayout();
            // 
            // picBobble
            // 
            this.picBobble.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.picBobble.Location = new System.Drawing.Point(12, 12);
            this.picBobble.Name = "picBobble";
            this.picBobble.Size = new System.Drawing.Size(183, 270);
            this.picBobble.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picBobble.TabIndex = 2;
            this.picBobble.TabStop = false;
            this.picBobble.Click += new System.EventHandler(this.picBobble_Click);
            // 
            // picHead
            // 
            this.picHead.Image = global::howto_bobblehead.Properties.Resources.Donald_Trump_Head;
            this.picHead.Location = new System.Drawing.Point(201, 12);
            this.picHead.Name = "picHead";
            this.picHead.Size = new System.Drawing.Size(161, 202);
            this.picHead.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picHead.TabIndex = 1;
            this.picHead.TabStop = false;
            this.picHead.Visible = false;
            // 
            // picBody
            // 
            this.picBody.Image = global::howto_bobblehead.Properties.Resources.Donald_Trump;
            this.picBody.Location = new System.Drawing.Point(84, 39);
            this.picBody.Name = "picBody";
            this.picBody.Size = new System.Drawing.Size(517, 600);
            this.picBody.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picBody.TabIndex = 0;
            this.picBody.TabStop = false;
            this.picBody.Visible = false;
            // 
            // tmrBobble
            // 
            this.tmrBobble.Interval = 50;
            this.tmrBobble.Tick += new System.EventHandler(this.tmrBobble_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.picHead);
            this.Controls.Add(this.picBody);
            this.Controls.Add(this.picBobble);
            this.Name = "Form1";
            this.Text = "howto_bobblehead";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picBobble)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picHead)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBody)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picBody;
        private System.Windows.Forms.PictureBox picHead;
        private System.Windows.Forms.PictureBox picBobble;
        private System.Windows.Forms.Timer tmrBobble;
    }
}

