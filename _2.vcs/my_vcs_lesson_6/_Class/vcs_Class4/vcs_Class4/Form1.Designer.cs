namespace vcs_Class4
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.trackBar_color2b = new System.Windows.Forms.TrackBar();
            this.trackBar_color2g = new System.Windows.Forms.TrackBar();
            this.trackBar_color2r = new System.Windows.Forms.TrackBar();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.trackBar_color1b = new System.Windows.Forms.TrackBar();
            this.trackBar_color1g = new System.Windows.Forms.TrackBar();
            this.trackBar_color1r = new System.Windows.Forms.TrackBar();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2b)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2g)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2r)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1b)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1g)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1r)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(385, 14);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(402, 31);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 9;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.trackBar_color2b);
            this.groupBox2.Controls.Add(this.trackBar_color2g);
            this.groupBox2.Controls.Add(this.trackBar_color2r);
            this.groupBox2.Location = new System.Drawing.Point(164, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(136, 168);
            this.groupBox2.TabIndex = 11;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "顏色二";
            // 
            // trackBar_color2b
            // 
            this.trackBar_color2b.Location = new System.Drawing.Point(6, 117);
            this.trackBar_color2b.Maximum = 255;
            this.trackBar_color2b.Name = "trackBar_color2b";
            this.trackBar_color2b.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color2b.TabIndex = 2;
            this.trackBar_color2b.Scroll += new System.EventHandler(this.trackBar_color2_Scroll);
            // 
            // trackBar_color2g
            // 
            this.trackBar_color2g.Location = new System.Drawing.Point(6, 69);
            this.trackBar_color2g.Maximum = 255;
            this.trackBar_color2g.Name = "trackBar_color2g";
            this.trackBar_color2g.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color2g.TabIndex = 1;
            this.trackBar_color2g.Scroll += new System.EventHandler(this.trackBar_color2_Scroll);
            // 
            // trackBar_color2r
            // 
            this.trackBar_color2r.Location = new System.Drawing.Point(6, 21);
            this.trackBar_color2r.Maximum = 255;
            this.trackBar_color2r.Name = "trackBar_color2r";
            this.trackBar_color2r.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color2r.TabIndex = 0;
            this.trackBar_color2r.Scroll += new System.EventHandler(this.trackBar_color2_Scroll);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.trackBar_color1b);
            this.groupBox1.Controls.Add(this.trackBar_color1g);
            this.groupBox1.Controls.Add(this.trackBar_color1r);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(136, 168);
            this.groupBox1.TabIndex = 10;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "顏色一";
            // 
            // trackBar_color1b
            // 
            this.trackBar_color1b.Location = new System.Drawing.Point(6, 117);
            this.trackBar_color1b.Maximum = 255;
            this.trackBar_color1b.Name = "trackBar_color1b";
            this.trackBar_color1b.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color1b.TabIndex = 2;
            this.trackBar_color1b.Scroll += new System.EventHandler(this.trackBar_color1_Scroll);
            // 
            // trackBar_color1g
            // 
            this.trackBar_color1g.Location = new System.Drawing.Point(6, 69);
            this.trackBar_color1g.Maximum = 255;
            this.trackBar_color1g.Name = "trackBar_color1g";
            this.trackBar_color1g.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color1g.TabIndex = 1;
            this.trackBar_color1g.Scroll += new System.EventHandler(this.trackBar_color1_Scroll);
            // 
            // trackBar_color1r
            // 
            this.trackBar_color1r.Location = new System.Drawing.Point(6, 21);
            this.trackBar_color1r.Maximum = 255;
            this.trackBar_color1r.Name = "trackBar_color1r";
            this.trackBar_color1r.Size = new System.Drawing.Size(124, 45);
            this.trackBar_color1r.TabIndex = 0;
            this.trackBar_color1r.Scroll += new System.EventHandler(this.trackBar_color1_Scroll);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(660, 575);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "類別示範, 可用滑鼠移動圓球";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseDown);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseMove);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseUp);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2b)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2g)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color2r)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1b)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1g)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar_color1r)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TrackBar trackBar_color2b;
        private System.Windows.Forms.TrackBar trackBar_color2g;
        private System.Windows.Forms.TrackBar trackBar_color2r;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TrackBar trackBar_color1b;
        private System.Windows.Forms.TrackBar trackBar_color1g;
        private System.Windows.Forms.TrackBar trackBar_color1r;
    }
}

