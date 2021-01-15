namespace howto_timed_self_avoiding_walks
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
            this.lblWalkNum = new System.Windows.Forms.Label();
            this.scrSpeed = new System.Windows.Forms.HScrollBar();
            this.btnGenerate = new System.Windows.Forms.Button();
            this.txtHeight = new System.Windows.Forms.TextBox();
            this.tmrShowWalk = new System.Windows.Forms.Timer(this.components);
            this.label2 = new System.Windows.Forms.Label();
            this.txtWidth = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // lblWalkNum
            // 
            this.lblWalkNum.AutoSize = true;
            this.lblWalkNum.Location = new System.Drawing.Point(15, 80);
            this.lblWalkNum.Name = "lblWalkNum";
            this.lblWalkNum.Size = new System.Drawing.Size(0, 13);
            this.lblWalkNum.TabIndex = 31;
            // 
            // scrSpeed
            // 
            this.scrSpeed.LargeChange = 1;
            this.scrSpeed.Location = new System.Drawing.Point(12, 216);
            this.scrSpeed.Minimum = 1;
            this.scrSpeed.Name = "scrSpeed";
            this.scrSpeed.Size = new System.Drawing.Size(210, 17);
            this.scrSpeed.TabIndex = 30;
            this.scrSpeed.Value = 2;
            this.scrSpeed.Scroll += new System.Windows.Forms.ScrollEventHandler(this.scrSpeed_Scroll);
            // 
            // btnGenerate
            // 
            this.btnGenerate.Location = new System.Drawing.Point(69, 33);
            this.btnGenerate.Name = "btnGenerate";
            this.btnGenerate.Size = new System.Drawing.Size(75, 23);
            this.btnGenerate.TabIndex = 29;
            this.btnGenerate.Text = "Generate";
            this.btnGenerate.UseVisualStyleBackColor = true;
            this.btnGenerate.Click += new System.EventHandler(this.btnGenerate_Click);
            // 
            // txtHeight
            // 
            this.txtHeight.Location = new System.Drawing.Point(164, 7);
            this.txtHeight.Name = "txtHeight";
            this.txtHeight.Size = new System.Drawing.Size(42, 20);
            this.txtHeight.TabIndex = 28;
            this.txtHeight.Text = "4";
            this.txtHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // tmrShowWalk
            // 
            this.tmrShowWalk.Interval = 500;
            this.tmrShowWalk.Tick += new System.EventHandler(this.tmrShowWalk_Tick);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(120, 10);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 13);
            this.label2.TabIndex = 27;
            this.label2.Text = "Height:";
            // 
            // txtWidth
            // 
            this.txtWidth.Location = new System.Drawing.Point(53, 7);
            this.txtWidth.Name = "txtWidth";
            this.txtWidth.Size = new System.Drawing.Size(42, 20);
            this.txtWidth.TabIndex = 26;
            this.txtWidth.Text = "4";
            this.txtWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 10);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 13);
            this.label1.TabIndex = 25;
            this.label1.Text = "Width:";
            // 
            // picCanvas
            // 
            this.picCanvas.BackColor = System.Drawing.Color.White;
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(225, 13);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(220, 220);
            this.picCanvas.TabIndex = 24;
            this.picCanvas.TabStop = false;
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGenerate;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(454, 241);
            this.Controls.Add(this.lblWalkNum);
            this.Controls.Add(this.scrSpeed);
            this.Controls.Add(this.btnGenerate);
            this.Controls.Add(this.txtHeight);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtWidth);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.picCanvas);
            this.Name = "Form1";
            this.Text = "howto_timed_self_avoiding_walks";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblWalkNum;
        private System.Windows.Forms.HScrollBar scrSpeed;
        private System.Windows.Forms.Button btnGenerate;
        private System.Windows.Forms.TextBox txtHeight;
        private System.Windows.Forms.Timer tmrShowWalk;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtWidth;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox picCanvas;
    }
}

