namespace WindowsFormsApplication1
{
    partial class testPictures
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(testPictures));
            this.ptbDisplay = new System.Windows.Forms.PictureBox();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnChange = new System.Windows.Forms.Button();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.ptbDisplay)).BeginInit();
            this.SuspendLayout();
            // 
            // ptbDisplay
            // 
            this.ptbDisplay.Image = ((System.Drawing.Image)(resources.GetObject("ptbDisplay.Image")));
            this.ptbDisplay.Location = new System.Drawing.Point(12, 12);
            this.ptbDisplay.Name = "ptbDisplay";
            this.ptbDisplay.Size = new System.Drawing.Size(200, 150);
            this.ptbDisplay.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.ptbDisplay.TabIndex = 0;
            this.ptbDisplay.TabStop = false;
            this.ptbDisplay.Click += new System.EventHandler(this.ptbDisplay_Click);
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(12, 177);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(97, 29);
            this.btnReset.TabIndex = 1;
            this.btnReset.Text = "顯示圖片";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // btnChange
            // 
            this.btnChange.Location = new System.Drawing.Point(115, 177);
            this.btnChange.Name = "btnChange";
            this.btnChange.Size = new System.Drawing.Size(97, 29);
            this.btnChange.TabIndex = 2;
            this.btnChange.Text = "變換圖片";
            this.btnChange.UseVisualStyleBackColor = true;
            this.btnChange.Click += new System.EventHandler(this.btnChange_Click);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "Chrysanthemum.jpg");
            this.imageList1.Images.SetKeyName(1, "Desert.jpg");
            this.imageList1.Images.SetKeyName(2, "Hydrangeas.jpg");
            this.imageList1.Images.SetKeyName(3, "Jellyfish.jpg");
            this.imageList1.Images.SetKeyName(4, "Koala.jpg");
            this.imageList1.Images.SetKeyName(5, "Lighthouse.jpg");
            this.imageList1.Images.SetKeyName(6, "Penguins.jpg");
            this.imageList1.Images.SetKeyName(7, "Tulips.jpg");
            this.imageList1.Images.SetKeyName(8, "Smile Time.jpg");
            // 
            // testPictures
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(224, 218);
            this.Controls.Add(this.btnChange);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.ptbDisplay);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "testPictures";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "圖片控制項";
            ((System.ComponentModel.ISupportInitialize)(this.ptbDisplay)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox ptbDisplay;
        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.Button btnChange;
        private System.Windows.Forms.ImageList imageList1;
    }
}