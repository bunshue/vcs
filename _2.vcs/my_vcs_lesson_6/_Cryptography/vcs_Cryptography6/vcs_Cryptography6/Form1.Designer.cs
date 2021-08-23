namespace vcs_Cryptography6
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
            this.tb_decrypted = new System.Windows.Forms.TextBox();
            this.tb_encrypted = new System.Windows.Forms.TextBox();
            this.tb_clear_code = new System.Windows.Forms.TextBox();
            this.Label4 = new System.Windows.Forms.Label();
            this.tb_password = new System.Windows.Forms.TextBox();
            this.Label3 = new System.Windows.Forms.Label();
            this.btnDecrypt = new System.Windows.Forms.Button();
            this.btnEncrypt = new System.Windows.Forms.Button();
            this.Label2 = new System.Windows.Forms.Label();
            this.Label1 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tb_decrypted
            // 
            this.tb_decrypted.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_decrypted.Location = new System.Drawing.Point(487, 80);
            this.tb_decrypted.Margin = new System.Windows.Forms.Padding(0, 2, 3, 3);
            this.tb_decrypted.Multiline = true;
            this.tb_decrypted.Name = "tb_decrypted";
            this.tb_decrypted.ReadOnly = true;
            this.tb_decrypted.Size = new System.Drawing.Size(200, 494);
            this.tb_decrypted.TabIndex = 91;
            // 
            // tb_encrypted
            // 
            this.tb_encrypted.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_encrypted.Location = new System.Drawing.Point(247, 80);
            this.tb_encrypted.Margin = new System.Windows.Forms.Padding(0, 2, 3, 3);
            this.tb_encrypted.Multiline = true;
            this.tb_encrypted.Name = "tb_encrypted";
            this.tb_encrypted.ReadOnly = true;
            this.tb_encrypted.Size = new System.Drawing.Size(200, 494);
            this.tb_encrypted.TabIndex = 90;
            // 
            // tb_clear_code
            // 
            this.tb_clear_code.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_clear_code.Location = new System.Drawing.Point(7, 80);
            this.tb_clear_code.Margin = new System.Windows.Forms.Padding(3, 2, 3, 3);
            this.tb_clear_code.Multiline = true;
            this.tb_clear_code.Name = "tb_clear_code";
            this.tb_clear_code.Size = new System.Drawing.Size(200, 494);
            this.tb_clear_code.TabIndex = 89;
            this.tb_clear_code.Text = "To encrypt data, attach a CryptoStream object to a stream. As you write data into" +
                " the CryptoStream, it encrypts or decrypts the data and sends it on to the outpu" +
                "t stream.";
            // 
            // Label4
            // 
            this.Label4.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label4.Location = new System.Drawing.Point(487, 55);
            this.Label4.Margin = new System.Windows.Forms.Padding(3, 3, 2, 1);
            this.Label4.Name = "Label4";
            this.Label4.Size = new System.Drawing.Size(200, 22);
            this.Label4.TabIndex = 87;
            this.Label4.Text = "編碼經使用密碼解密後";
            this.Label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tb_password
            // 
            this.tb_password.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_password.Location = new System.Drawing.Point(71, 18);
            this.tb_password.Name = "tb_password";
            this.tb_password.Size = new System.Drawing.Size(616, 30);
            this.tb_password.TabIndex = 86;
            this.tb_password.Text = "The quick brown fox jumps over the lazy dog";
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label3.Location = new System.Drawing.Point(20, 23);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(47, 19);
            this.Label3.TabIndex = 85;
            this.Label3.Text = "密碼";
            // 
            // btnDecrypt
            // 
            this.btnDecrypt.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnDecrypt.Location = new System.Drawing.Point(455, 85);
            this.btnDecrypt.Name = "btnDecrypt";
            this.btnDecrypt.Size = new System.Drawing.Size(25, 40);
            this.btnDecrypt.TabIndex = 84;
            this.btnDecrypt.TabStop = false;
            this.btnDecrypt.Text = ">";
            this.btnDecrypt.Click += new System.EventHandler(this.btnDecrypt_Click);
            // 
            // btnEncrypt
            // 
            this.btnEncrypt.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnEncrypt.Location = new System.Drawing.Point(215, 85);
            this.btnEncrypt.Margin = new System.Windows.Forms.Padding(3, 2, 1, 3);
            this.btnEncrypt.Name = "btnEncrypt";
            this.btnEncrypt.Size = new System.Drawing.Size(25, 40);
            this.btnEncrypt.TabIndex = 83;
            this.btnEncrypt.TabStop = false;
            this.btnEncrypt.Text = ">";
            this.btnEncrypt.Click += new System.EventHandler(this.btnEncrypt_Click);
            // 
            // Label2
            // 
            this.Label2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label2.Location = new System.Drawing.Point(247, 55);
            this.Label2.Margin = new System.Windows.Forms.Padding(3, 3, 2, 1);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(200, 22);
            this.Label2.TabIndex = 81;
            this.Label2.Text = "明碼經使用密碼加密後";
            this.Label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Label1
            // 
            this.Label1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Label1.Location = new System.Drawing.Point(7, 55);
            this.Label1.Margin = new System.Windows.Forms.Padding(3, 3, 2, 1);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(200, 22);
            this.Label1.TabIndex = 79;
            this.Label1.Text = "明碼";
            this.Label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(714, 78);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(676, 496);
            this.richTextBox1.TabIndex = 92;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(714, 14);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 37);
            this.button1.TabIndex = 93;
            this.button1.Text = "test";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1402, 591);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.tb_decrypted);
            this.Controls.Add(this.tb_encrypted);
            this.Controls.Add(this.tb_clear_code);
            this.Controls.Add(this.Label4);
            this.Controls.Add(this.tb_password);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.btnDecrypt);
            this.Controls.Add(this.btnEncrypt);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.Label1);
            this.Name = "Form1";
            this.Text = "vcs_Cryptography6";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.TextBox tb_decrypted;
        internal System.Windows.Forms.TextBox tb_encrypted;
        internal System.Windows.Forms.TextBox tb_clear_code;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.TextBox tb_password;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.Button btnDecrypt;
        internal System.Windows.Forms.Button btnEncrypt;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.Label Label1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;

    }
}

