namespace howto_stego_bytes
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
            this.picUsed = new System.Windows.Forms.PictureBox();
            this.label4 = new System.Windows.Forms.Label();
            this.picEncoded = new System.Windows.Forms.PictureBox();
            this.label3 = new System.Windows.Forms.Label();
            this.picOriginal = new System.Windows.Forms.PictureBox();
            this.label2 = new System.Windows.Forms.Label();
            this.btnDecode = new System.Windows.Forms.Button();
            this.btnEncode = new System.Windows.Forms.Button();
            this.txtMessage = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblResult = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.picUsed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picEncoded)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).BeginInit();
            this.SuspendLayout();
            // 
            // picUsed
            // 
            this.picUsed.Location = new System.Drawing.Point(436, 86);
            this.picUsed.Name = "picUsed";
            this.picUsed.Size = new System.Drawing.Size(206, 135);
            this.picUsed.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picUsed.TabIndex = 19;
            this.picUsed.TabStop = false;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(436, 71);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(58, 12);
            this.label4.TabIndex = 18;
            this.label4.Text = "Used Pixels";
            // 
            // picEncoded
            // 
            this.picEncoded.Location = new System.Drawing.Point(224, 86);
            this.picEncoded.Name = "picEncoded";
            this.picEncoded.Size = new System.Drawing.Size(206, 135);
            this.picEncoded.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picEncoded.TabIndex = 17;
            this.picEncoded.TabStop = false;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(224, 71);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(46, 12);
            this.label3.TabIndex = 16;
            this.label3.Text = "Encoded";
            // 
            // picOriginal
            // 
            this.picOriginal.Image = global::howto_stego_bytes.Properties.Resources.dog;
            this.picOriginal.Location = new System.Drawing.Point(12, 86);
            this.picOriginal.Name = "picOriginal";
            this.picOriginal.Size = new System.Drawing.Size(206, 135);
            this.picOriginal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picOriginal.TabIndex = 15;
            this.picOriginal.TabStop = false;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 71);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(43, 12);
            this.label2.TabIndex = 14;
            this.label2.Text = "Original";
            // 
            // btnDecode
            // 
            this.btnDecode.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnDecode.Enabled = false;
            this.btnDecode.Location = new System.Drawing.Point(566, 35);
            this.btnDecode.Name = "btnDecode";
            this.btnDecode.Size = new System.Drawing.Size(75, 21);
            this.btnDecode.TabIndex = 13;
            this.btnDecode.Text = "Decode";
            this.btnDecode.UseVisualStyleBackColor = true;
            this.btnDecode.Click += new System.EventHandler(this.btnDecode_Click);
            // 
            // btnEncode
            // 
            this.btnEncode.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.btnEncode.Location = new System.Drawing.Point(445, 35);
            this.btnEncode.Name = "btnEncode";
            this.btnEncode.Size = new System.Drawing.Size(75, 21);
            this.btnEncode.TabIndex = 12;
            this.btnEncode.Text = "Encode";
            this.btnEncode.UseVisualStyleBackColor = true;
            this.btnEncode.Click += new System.EventHandler(this.btnEncode_Click);
            // 
            // txtMessage
            // 
            this.txtMessage.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.txtMessage.Location = new System.Drawing.Point(71, 11);
            this.txtMessage.Name = "txtMessage";
            this.txtMessage.Size = new System.Drawing.Size(1004, 22);
            this.txtMessage.TabIndex = 11;
            this.txtMessage.Text = resources.GetString("txtMessage.Text");
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 12);
            this.label1.TabIndex = 10;
            this.label1.Text = "Message:";
            // 
            // lblResult
            // 
            this.lblResult.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.lblResult.AutoSize = true;
            this.lblResult.Location = new System.Drawing.Point(12, 497);
            this.lblResult.Name = "lblResult";
            this.lblResult.Size = new System.Drawing.Size(0, 12);
            this.lblResult.TabIndex = 20;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(664, 39);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(411, 470);
            this.richTextBox1.TabIndex = 21;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1087, 517);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lblResult);
            this.Controls.Add(this.picUsed);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.picEncoded);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.picOriginal);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnDecode);
            this.Controls.Add(this.btnEncode);
            this.Controls.Add(this.txtMessage);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_stego_bytes";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picUsed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picEncoded)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picOriginal)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picUsed;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.PictureBox picEncoded;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox picOriginal;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnDecode;
        private System.Windows.Forms.Button btnEncode;
        private System.Windows.Forms.TextBox txtMessage;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblResult;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

