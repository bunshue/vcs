namespace WindowsFormsApplication1
{
    partial class CallByRef
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
            this.lblBeforeSwap = new System.Windows.Forms.Label();
            this.lblAfterSwap = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblBeforeSwap
            // 
            this.lblBeforeSwap.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblBeforeSwap.Location = new System.Drawing.Point(20, 18);
            this.lblBeforeSwap.Name = "lblBeforeSwap";
            this.lblBeforeSwap.Size = new System.Drawing.Size(192, 27);
            this.lblBeforeSwap.TabIndex = 0;
            this.lblBeforeSwap.Text = "BeforeSwap";
            // 
            // lblAfterSwap
            // 
            this.lblAfterSwap.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblAfterSwap.Location = new System.Drawing.Point(20, 60);
            this.lblAfterSwap.Name = "lblAfterSwap";
            this.lblAfterSwap.Size = new System.Drawing.Size(192, 30);
            this.lblAfterSwap.TabIndex = 1;
            this.lblAfterSwap.Text = "AfterSwap";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(20, 102);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(85, 32);
            this.button1.TabIndex = 2;
            this.button1.Text = "傳值呼叫";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(127, 102);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(85, 32);
            this.button2.TabIndex = 3;
            this.button2.Text = "傳址呼叫";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // CallByRef
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(230, 147);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.lblAfterSwap);
            this.Controls.Add(this.lblBeforeSwap);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "CallByRef";
            this.Text = "兩數交換";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label lblBeforeSwap;
        private System.Windows.Forms.Label lblAfterSwap;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
    }
}