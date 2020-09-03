namespace vcs_KeyDown1
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.picTank = new System.Windows.Forms.PictureBox();
            this.picTankU = new System.Windows.Forms.PictureBox();
            this.picTankL = new System.Windows.Forms.PictureBox();
            this.picTankR = new System.Windows.Forms.PictureBox();
            this.picTankD = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.picTank)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankU)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankL)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankR)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankD)).BeginInit();
            this.SuspendLayout();
            // 
            // picTank
            // 
            this.picTank.Location = new System.Drawing.Point(227, 192);
            this.picTank.Name = "picTank";
            this.picTank.Size = new System.Drawing.Size(100, 95);
            this.picTank.TabIndex = 0;
            this.picTank.TabStop = false;
            // 
            // picTankU
            // 
            this.picTankU.Image = global::vcs_KeyDown1.Properties.Resources.tankU;
            this.picTankU.Location = new System.Drawing.Point(227, 60);
            this.picTankU.Name = "picTankU";
            this.picTankU.Size = new System.Drawing.Size(66, 73);
            this.picTankU.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picTankU.TabIndex = 1;
            this.picTankU.TabStop = false;
            // 
            // picTankL
            // 
            this.picTankL.Image = global::vcs_KeyDown1.Properties.Resources.tankL;
            this.picTankL.Location = new System.Drawing.Point(69, 192);
            this.picTankL.Name = "picTankL";
            this.picTankL.Size = new System.Drawing.Size(100, 95);
            this.picTankL.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picTankL.TabIndex = 2;
            this.picTankL.TabStop = false;
            // 
            // picTankR
            // 
            this.picTankR.Image = global::vcs_KeyDown1.Properties.Resources.tankR;
            this.picTankR.Location = new System.Drawing.Point(404, 192);
            this.picTankR.Name = "picTankR";
            this.picTankR.Size = new System.Drawing.Size(71, 67);
            this.picTankR.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picTankR.TabIndex = 3;
            this.picTankR.TabStop = false;
            // 
            // picTankD
            // 
            this.picTankD.Image = global::vcs_KeyDown1.Properties.Resources.tankD;
            this.picTankD.Location = new System.Drawing.Point(227, 346);
            this.picTankD.Name = "picTankD";
            this.picTankD.Size = new System.Drawing.Size(65, 71);
            this.picTankD.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picTankD.TabIndex = 4;
            this.picTankD.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(402, 479);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(33, 12);
            this.label1.TabIndex = 5;
            this.label1.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(588, 521);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picTankD);
            this.Controls.Add(this.picTankR);
            this.Controls.Add(this.picTankL);
            this.Controls.Add(this.picTankU);
            this.Controls.Add(this.picTank);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.picTank)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankU)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankL)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankR)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picTankD)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picTank;
        private System.Windows.Forms.PictureBox picTankU;
        private System.Windows.Forms.PictureBox picTankL;
        private System.Windows.Forms.PictureBox picTankR;
        private System.Windows.Forms.PictureBox picTankD;
        private System.Windows.Forms.Label label1;
    }
}

