namespace howto_hangman
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
            this.flpLetters = new System.Windows.Forms.FlowLayoutPanel();
            this.lblWon = new System.Windows.Forms.Label();
            this.lblLost = new System.Windows.Forms.Label();
            this.btnNewGame = new System.Windows.Forms.Button();
            this.button25 = new System.Windows.Forms.Button();
            this.button26 = new System.Windows.Forms.Button();
            this.button27 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.button19 = new System.Windows.Forms.Button();
            this.button20 = new System.Windows.Forms.Button();
            this.button21 = new System.Windows.Forms.Button();
            this.button22 = new System.Windows.Forms.Button();
            this.button23 = new System.Windows.Forms.Button();
            this.button8 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.btnY = new System.Windows.Forms.Button();
            this.btnT = new System.Windows.Forms.Button();
            this.btnR = new System.Windows.Forms.Button();
            this.btnE = new System.Windows.Forms.Button();
            this.btnW = new System.Windows.Forms.Button();
            this.btnQ = new System.Windows.Forms.Button();
            this.picSkeleton0 = new System.Windows.Forms.PictureBox();
            this.picSkeleton5 = new System.Windows.Forms.PictureBox();
            this.picSkeleton4 = new System.Windows.Forms.PictureBox();
            this.picSkeleton3 = new System.Windows.Forms.PictureBox();
            this.picSkeleton2 = new System.Windows.Forms.PictureBox();
            this.picSkeleton1 = new System.Windows.Forms.PictureBox();
            this.picSkeleton6 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton6)).BeginInit();
            this.SuspendLayout();
            // 
            // flpLetters
            // 
            this.flpLetters.Location = new System.Drawing.Point(281, 12);
            this.flpLetters.Name = "flpLetters";
            this.flpLetters.Size = new System.Drawing.Size(423, 70);
            this.flpLetters.TabIndex = 76;
            // 
            // lblWon
            // 
            this.lblWon.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblWon.ForeColor = System.Drawing.Color.Blue;
            this.lblWon.Location = new System.Drawing.Point(281, 85);
            this.lblWon.Name = "lblWon";
            this.lblWon.Size = new System.Drawing.Size(423, 46);
            this.lblWon.TabIndex = 75;
            this.lblWon.Text = "Congratulations, you won!";
            this.lblWon.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.lblWon.Visible = false;
            // 
            // lblLost
            // 
            this.lblLost.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLost.ForeColor = System.Drawing.Color.Red;
            this.lblLost.Location = new System.Drawing.Point(281, 85);
            this.lblLost.Name = "lblLost";
            this.lblLost.Size = new System.Drawing.Size(423, 46);
            this.lblLost.TabIndex = 74;
            this.lblLost.Text = "Sorry, you lost.";
            this.lblLost.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.lblLost.Visible = false;
            // 
            // btnNewGame
            // 
            this.btnNewGame.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnNewGame.Font = new System.Drawing.Font("Corbel", 14F, System.Drawing.FontStyle.Bold);
            this.btnNewGame.Location = new System.Drawing.Point(594, 286);
            this.btnNewGame.Name = "btnNewGame";
            this.btnNewGame.Size = new System.Drawing.Size(110, 32);
            this.btnNewGame.TabIndex = 73;
            this.btnNewGame.Text = "New Game";
            this.btnNewGame.UseVisualStyleBackColor = true;
            this.btnNewGame.Click += new System.EventHandler(this.btnNewGame_Click);
            // 
            // button25
            // 
            this.button25.Enabled = false;
            this.button25.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button25.Location = new System.Drawing.Point(646, 174);
            this.button25.Name = "button25";
            this.button25.Size = new System.Drawing.Size(37, 34);
            this.button25.TabIndex = 72;
            this.button25.TabStop = false;
            this.button25.Text = "L";
            this.button25.UseVisualStyleBackColor = true;
            // 
            // button26
            // 
            this.button26.Enabled = false;
            this.button26.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button26.Location = new System.Drawing.Point(668, 134);
            this.button26.Name = "button26";
            this.button26.Size = new System.Drawing.Size(37, 34);
            this.button26.TabIndex = 71;
            this.button26.TabStop = false;
            this.button26.Text = "P";
            this.button26.UseVisualStyleBackColor = true;
            // 
            // button27
            // 
            this.button27.Enabled = false;
            this.button27.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button27.Location = new System.Drawing.Point(625, 134);
            this.button27.Name = "button27";
            this.button27.Size = new System.Drawing.Size(37, 34);
            this.button27.TabIndex = 70;
            this.button27.TabStop = false;
            this.button27.Text = "O";
            this.button27.UseVisualStyleBackColor = true;
            // 
            // button17
            // 
            this.button17.Enabled = false;
            this.button17.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button17.Location = new System.Drawing.Point(582, 214);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(37, 34);
            this.button17.TabIndex = 69;
            this.button17.TabStop = false;
            this.button17.Text = "M";
            this.button17.UseVisualStyleBackColor = true;
            // 
            // button18
            // 
            this.button18.Enabled = false;
            this.button18.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button18.Location = new System.Drawing.Point(539, 214);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(37, 34);
            this.button18.TabIndex = 68;
            this.button18.TabStop = false;
            this.button18.Text = "N";
            this.button18.UseVisualStyleBackColor = true;
            // 
            // button19
            // 
            this.button19.Enabled = false;
            this.button19.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button19.Location = new System.Drawing.Point(496, 214);
            this.button19.Name = "button19";
            this.button19.Size = new System.Drawing.Size(37, 34);
            this.button19.TabIndex = 67;
            this.button19.TabStop = false;
            this.button19.Text = "B";
            this.button19.UseVisualStyleBackColor = true;
            // 
            // button20
            // 
            this.button20.Enabled = false;
            this.button20.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button20.Location = new System.Drawing.Point(453, 214);
            this.button20.Name = "button20";
            this.button20.Size = new System.Drawing.Size(37, 34);
            this.button20.TabIndex = 66;
            this.button20.TabStop = false;
            this.button20.Text = "V";
            this.button20.UseVisualStyleBackColor = true;
            // 
            // button21
            // 
            this.button21.Enabled = false;
            this.button21.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button21.Location = new System.Drawing.Point(410, 214);
            this.button21.Name = "button21";
            this.button21.Size = new System.Drawing.Size(37, 34);
            this.button21.TabIndex = 65;
            this.button21.TabStop = false;
            this.button21.Text = "C";
            this.button21.UseVisualStyleBackColor = true;
            // 
            // button22
            // 
            this.button22.Enabled = false;
            this.button22.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button22.Location = new System.Drawing.Point(367, 214);
            this.button22.Name = "button22";
            this.button22.Size = new System.Drawing.Size(37, 34);
            this.button22.TabIndex = 64;
            this.button22.TabStop = false;
            this.button22.Text = "X";
            this.button22.UseVisualStyleBackColor = true;
            // 
            // button23
            // 
            this.button23.Enabled = false;
            this.button23.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button23.Location = new System.Drawing.Point(324, 214);
            this.button23.Name = "button23";
            this.button23.Size = new System.Drawing.Size(37, 34);
            this.button23.TabIndex = 63;
            this.button23.TabStop = false;
            this.button23.Text = "Z";
            this.button23.UseVisualStyleBackColor = true;
            // 
            // button8
            // 
            this.button8.Enabled = false;
            this.button8.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button8.Location = new System.Drawing.Point(603, 174);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(37, 34);
            this.button8.TabIndex = 62;
            this.button8.TabStop = false;
            this.button8.Text = "K";
            this.button8.UseVisualStyleBackColor = true;
            // 
            // button9
            // 
            this.button9.Enabled = false;
            this.button9.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button9.Location = new System.Drawing.Point(560, 174);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(37, 34);
            this.button9.TabIndex = 61;
            this.button9.TabStop = false;
            this.button9.Text = "J";
            this.button9.UseVisualStyleBackColor = true;
            // 
            // button10
            // 
            this.button10.Enabled = false;
            this.button10.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button10.Location = new System.Drawing.Point(517, 174);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(37, 34);
            this.button10.TabIndex = 60;
            this.button10.TabStop = false;
            this.button10.Text = "H";
            this.button10.UseVisualStyleBackColor = true;
            // 
            // button11
            // 
            this.button11.Enabled = false;
            this.button11.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button11.Location = new System.Drawing.Point(474, 174);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(37, 34);
            this.button11.TabIndex = 59;
            this.button11.TabStop = false;
            this.button11.Text = "G";
            this.button11.UseVisualStyleBackColor = true;
            // 
            // button12
            // 
            this.button12.Enabled = false;
            this.button12.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button12.Location = new System.Drawing.Point(431, 174);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(37, 34);
            this.button12.TabIndex = 58;
            this.button12.TabStop = false;
            this.button12.Text = "F";
            this.button12.UseVisualStyleBackColor = true;
            // 
            // button13
            // 
            this.button13.Enabled = false;
            this.button13.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button13.Location = new System.Drawing.Point(388, 174);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(37, 34);
            this.button13.TabIndex = 57;
            this.button13.TabStop = false;
            this.button13.Text = "D";
            this.button13.UseVisualStyleBackColor = true;
            // 
            // button14
            // 
            this.button14.Enabled = false;
            this.button14.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button14.Location = new System.Drawing.Point(345, 174);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(37, 34);
            this.button14.TabIndex = 56;
            this.button14.TabStop = false;
            this.button14.Text = "S";
            this.button14.UseVisualStyleBackColor = true;
            // 
            // button15
            // 
            this.button15.Enabled = false;
            this.button15.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button15.Location = new System.Drawing.Point(302, 174);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(37, 34);
            this.button15.TabIndex = 55;
            this.button15.TabStop = false;
            this.button15.Text = "A";
            this.button15.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Enabled = false;
            this.button4.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button4.Location = new System.Drawing.Point(582, 134);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(37, 34);
            this.button4.TabIndex = 54;
            this.button4.TabStop = false;
            this.button4.Text = "I";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // button5
            // 
            this.button5.Enabled = false;
            this.button5.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.button5.Location = new System.Drawing.Point(539, 134);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(37, 34);
            this.button5.TabIndex = 53;
            this.button5.TabStop = false;
            this.button5.Text = "U";
            this.button5.UseVisualStyleBackColor = true;
            // 
            // btnY
            // 
            this.btnY.Enabled = false;
            this.btnY.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnY.Location = new System.Drawing.Point(496, 134);
            this.btnY.Name = "btnY";
            this.btnY.Size = new System.Drawing.Size(37, 34);
            this.btnY.TabIndex = 52;
            this.btnY.TabStop = false;
            this.btnY.Text = "Y";
            this.btnY.UseVisualStyleBackColor = true;
            // 
            // btnT
            // 
            this.btnT.Enabled = false;
            this.btnT.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnT.Location = new System.Drawing.Point(453, 134);
            this.btnT.Name = "btnT";
            this.btnT.Size = new System.Drawing.Size(37, 34);
            this.btnT.TabIndex = 51;
            this.btnT.TabStop = false;
            this.btnT.Text = "T";
            this.btnT.UseVisualStyleBackColor = true;
            // 
            // btnR
            // 
            this.btnR.Enabled = false;
            this.btnR.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnR.Location = new System.Drawing.Point(410, 134);
            this.btnR.Name = "btnR";
            this.btnR.Size = new System.Drawing.Size(37, 34);
            this.btnR.TabIndex = 50;
            this.btnR.TabStop = false;
            this.btnR.Text = "R";
            this.btnR.UseVisualStyleBackColor = true;
            // 
            // btnE
            // 
            this.btnE.Enabled = false;
            this.btnE.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnE.Location = new System.Drawing.Point(367, 134);
            this.btnE.Name = "btnE";
            this.btnE.Size = new System.Drawing.Size(37, 34);
            this.btnE.TabIndex = 49;
            this.btnE.TabStop = false;
            this.btnE.Text = "E";
            this.btnE.UseVisualStyleBackColor = true;
            // 
            // btnW
            // 
            this.btnW.Enabled = false;
            this.btnW.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnW.Location = new System.Drawing.Point(324, 134);
            this.btnW.Name = "btnW";
            this.btnW.Size = new System.Drawing.Size(37, 34);
            this.btnW.TabIndex = 48;
            this.btnW.TabStop = false;
            this.btnW.Text = "W";
            this.btnW.UseVisualStyleBackColor = true;
            // 
            // btnQ
            // 
            this.btnQ.Enabled = false;
            this.btnQ.Font = new System.Drawing.Font("Corbel", 20.25F, System.Drawing.FontStyle.Bold);
            this.btnQ.Location = new System.Drawing.Point(281, 134);
            this.btnQ.Name = "btnQ";
            this.btnQ.Size = new System.Drawing.Size(37, 34);
            this.btnQ.TabIndex = 47;
            this.btnQ.TabStop = false;
            this.btnQ.Text = "Q";
            this.btnQ.UseVisualStyleBackColor = true;
            // 
            // picSkeleton0
            // 
            this.picSkeleton0.BackColor = System.Drawing.Color.White;
            this.picSkeleton0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton0.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton0.Name = "picSkeleton0";
            this.picSkeleton0.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton0.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton0.TabIndex = 46;
            this.picSkeleton0.TabStop = false;
            // 
            // picSkeleton5
            // 
            this.picSkeleton5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton5.Image = global::howto_hangman.Properties.Resources.skeleton5;
            this.picSkeleton5.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton5.Name = "picSkeleton5";
            this.picSkeleton5.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton5.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton5.TabIndex = 45;
            this.picSkeleton5.TabStop = false;
            this.picSkeleton5.Visible = false;
            // 
            // picSkeleton4
            // 
            this.picSkeleton4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton4.Image = global::howto_hangman.Properties.Resources.skeleton4;
            this.picSkeleton4.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton4.Name = "picSkeleton4";
            this.picSkeleton4.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton4.TabIndex = 44;
            this.picSkeleton4.TabStop = false;
            this.picSkeleton4.Visible = false;
            // 
            // picSkeleton3
            // 
            this.picSkeleton3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton3.Image = global::howto_hangman.Properties.Resources.skeleton3;
            this.picSkeleton3.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton3.Name = "picSkeleton3";
            this.picSkeleton3.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton3.TabIndex = 43;
            this.picSkeleton3.TabStop = false;
            this.picSkeleton3.Visible = false;
            // 
            // picSkeleton2
            // 
            this.picSkeleton2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton2.Image = global::howto_hangman.Properties.Resources.skeleton2;
            this.picSkeleton2.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton2.Name = "picSkeleton2";
            this.picSkeleton2.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton2.TabIndex = 42;
            this.picSkeleton2.TabStop = false;
            this.picSkeleton2.Visible = false;
            // 
            // picSkeleton1
            // 
            this.picSkeleton1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton1.Image = global::howto_hangman.Properties.Resources.skeleton1;
            this.picSkeleton1.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton1.Name = "picSkeleton1";
            this.picSkeleton1.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton1.TabIndex = 41;
            this.picSkeleton1.TabStop = false;
            this.picSkeleton1.Visible = false;
            // 
            // picSkeleton6
            // 
            this.picSkeleton6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picSkeleton6.Image = global::howto_hangman.Properties.Resources.skeleton;
            this.picSkeleton6.Location = new System.Drawing.Point(11, 12);
            this.picSkeleton6.Name = "picSkeleton6";
            this.picSkeleton6.Size = new System.Drawing.Size(264, 306);
            this.picSkeleton6.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picSkeleton6.TabIndex = 40;
            this.picSkeleton6.TabStop = false;
            this.picSkeleton6.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(717, 330);
            this.Controls.Add(this.flpLetters);
            this.Controls.Add(this.lblWon);
            this.Controls.Add(this.lblLost);
            this.Controls.Add(this.btnNewGame);
            this.Controls.Add(this.button25);
            this.Controls.Add(this.button26);
            this.Controls.Add(this.button27);
            this.Controls.Add(this.button17);
            this.Controls.Add(this.button18);
            this.Controls.Add(this.button19);
            this.Controls.Add(this.button20);
            this.Controls.Add(this.button21);
            this.Controls.Add(this.button22);
            this.Controls.Add(this.button23);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.btnY);
            this.Controls.Add(this.btnT);
            this.Controls.Add(this.btnR);
            this.Controls.Add(this.btnE);
            this.Controls.Add(this.btnW);
            this.Controls.Add(this.btnQ);
            this.Controls.Add(this.picSkeleton0);
            this.Controls.Add(this.picSkeleton5);
            this.Controls.Add(this.picSkeleton4);
            this.Controls.Add(this.picSkeleton3);
            this.Controls.Add(this.picSkeleton2);
            this.Controls.Add(this.picSkeleton1);
            this.Controls.Add(this.picSkeleton6);
            this.Name = "Form1";
            this.Text = "howto_hangman";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picSkeleton6)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.FlowLayoutPanel flpLetters;
        private System.Windows.Forms.Label lblWon;
        private System.Windows.Forms.Label lblLost;
        private System.Windows.Forms.Button btnNewGame;
        private System.Windows.Forms.Button button25;
        private System.Windows.Forms.Button button26;
        private System.Windows.Forms.Button button27;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.Button button19;
        private System.Windows.Forms.Button button20;
        private System.Windows.Forms.Button button21;
        private System.Windows.Forms.Button button22;
        private System.Windows.Forms.Button button23;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button14;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button btnY;
        private System.Windows.Forms.Button btnT;
        private System.Windows.Forms.Button btnR;
        private System.Windows.Forms.Button btnE;
        private System.Windows.Forms.Button btnW;
        private System.Windows.Forms.Button btnQ;
        private System.Windows.Forms.PictureBox picSkeleton0;
        private System.Windows.Forms.PictureBox picSkeleton5;
        private System.Windows.Forms.PictureBox picSkeleton4;
        private System.Windows.Forms.PictureBox picSkeleton3;
        private System.Windows.Forms.PictureBox picSkeleton2;
        private System.Windows.Forms.PictureBox picSkeleton1;
        private System.Windows.Forms.PictureBox picSkeleton6;
    }
}

