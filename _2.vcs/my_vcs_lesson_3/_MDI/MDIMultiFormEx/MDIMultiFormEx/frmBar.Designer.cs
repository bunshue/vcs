namespace MDIMutilFormEx
{
    partial class frmBar
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
            this.lblSum = new System.Windows.Forms.Label();
            this.nudQty = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.pic1 = new System.Windows.Forms.PictureBox();
            this.pic2 = new System.Windows.Forms.PictureBox();
            this.pic3 = new System.Windows.Forms.PictureBox();
            this.picBtn = new System.Windows.Forms.PictureBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.nudQty)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBtn)).BeginInit();
            this.SuspendLayout();
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblSum.Location = new System.Drawing.Point(86, 433);
            this.lblSum.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(62, 20);
            this.lblSum.TabIndex = 33;
            this.lblSum.Text = "lblSum";
            // 
            // nudQty
            // 
            this.nudQty.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nudQty.Location = new System.Drawing.Point(272, 427);
            this.nudQty.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.nudQty.Name = "nudQty";
            this.nudQty.Size = new System.Drawing.Size(77, 31);
            this.nudQty.TabIndex = 32;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(9, 433);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 20);
            this.label2.TabIndex = 31;
            this.label2.Text = "總數量";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(195, 433);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(69, 20);
            this.label1.TabIndex = 30;
            this.label1.Text = "投注量";
            // 
            // pic1
            // 
            this.pic1.Location = new System.Drawing.Point(13, 34);
            this.pic1.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.pic1.Name = "pic1";
            this.pic1.Size = new System.Drawing.Size(100, 95);
            this.pic1.TabIndex = 29;
            this.pic1.TabStop = false;
            // 
            // pic2
            // 
            this.pic2.Location = new System.Drawing.Point(129, 34);
            this.pic2.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.pic2.Name = "pic2";
            this.pic2.Size = new System.Drawing.Size(100, 95);
            this.pic2.TabIndex = 28;
            this.pic2.TabStop = false;
            // 
            // pic3
            // 
            this.pic3.Location = new System.Drawing.Point(249, 34);
            this.pic3.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.pic3.Name = "pic3";
            this.pic3.Size = new System.Drawing.Size(100, 95);
            this.pic3.TabIndex = 27;
            this.pic3.TabStop = false;
            // 
            // picBtn
            // 
            this.picBtn.Location = new System.Drawing.Point(277, 147);
            this.picBtn.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.picBtn.Name = "picBtn";
            this.picBtn.Size = new System.Drawing.Size(82, 204);
            this.picBtn.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picBtn.TabIndex = 26;
            this.picBtn.TabStop = false;
            this.picBtn.Click += new System.EventHandler(this.picBtn_Click);
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // frmBar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            //this.BackgroundImage = global::MDIMutilFormEx.Properties.Resources.拉霸背景;
            this.ClientSize = new System.Drawing.Size(361, 473);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.nudQty);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pic1);
            this.Controls.Add(this.pic2);
            this.Controls.Add(this.pic3);
            this.Controls.Add(this.picBtn);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "frmBar";
            this.Text = "拉霸遊戲";
            this.Load += new System.EventHandler(this.frmBar_Load);
            ((System.ComponentModel.ISupportInitialize)(this.nudQty)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picBtn)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.Label lblSum;
        internal System.Windows.Forms.NumericUpDown nudQty;
        internal System.Windows.Forms.Label label2;
        internal System.Windows.Forms.Label label1;
        internal System.Windows.Forms.PictureBox pic1;
        internal System.Windows.Forms.PictureBox pic2;
        internal System.Windows.Forms.PictureBox pic3;
        internal System.Windows.Forms.PictureBox picBtn;
        private System.Windows.Forms.Timer timer1;
    }
}