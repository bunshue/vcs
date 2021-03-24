using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

namespace vcs_Draw_XY
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        string title = "OV Exposure Plot";
        string xlabel = "x";
        string ylabel = "y";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);     // 設定畫筆為紅色、粗細為 2 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
        }

        void plotXY(int[] x, int[] y)
        {
            int border_x = 10;  //10% border X
            int border_y = 10;  //10% border Y

            int WW = pictureBox1.ClientSize.Width;
            int HH = pictureBox1.ClientSize.Height;

            int x_st = WW * border_x / 100;
            int y_st = HH * border_y / 100;

            richTextBox1.Text += "WW = " + WW.ToString() + "\n";
            richTextBox1.Text += "HH = " + HH.ToString() + "\n";

            int W = WW * (100 - border_x * 2) / 100;
            int H = HH * (100 - border_y * 2) / 100;

            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            int N1 = x.Length;
            int N2 = y.Length;
            int N = Math.Min(N1, N2);
            richTextBox1.Text += "x_len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "y_len = " + y.Length.ToString() + "\n";
            richTextBox1.Text += "N = " + N.ToString() + "\n";

            int y_max = y.Max();
            int y_min = y.Min();
            richTextBox1.Text += "y_max = " + y_max.ToString() + "\n";
            richTextBox1.Text += "y_min = " + y_min.ToString() + "\n";

            float x_ratio = W / (float)N;
            float y_ratio = H / (float)(y_max - y_min);

            richTextBox1.Text += "x_ratio = " + x_ratio.ToString() + "\n";
            richTextBox1.Text += "y_ratio = " + y_ratio.ToString() + "\n";

            g.Clear(Color.White);

            int i;
            Point[] curvePoints = new Point[N];    //一維陣列內有 N 個Point

            for (i = 0; i < N; i++)
            {
                curvePoints[i].X = x_st + (int)(x[i] * x_ratio);
                //curvePoints[i].Y = HH - (y_st + (int)(y[i] * y_ratio));
                curvePoints[i].Y = HH - (y_st + (int)((y[i] - y_min) * y_ratio));
                if (i == 0)
                {
                    richTextBox1.Text += curvePoints[i].ToString() + "\n";
                    richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
                }
            }
            g.DrawLines(p, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, W - 1, H - 1));


            Font f = new Font("標楷體", 24);
            int tmp_width = 0;
            int tmp_height = 0;
            tmp_width = g.MeasureString(title, f).ToSize().Width;
            tmp_height = g.MeasureString(title, f).ToSize().Height;
            richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";
            g.DrawString(title, f, new SolidBrush(Color.Blue), new PointF((WW - tmp_width) / 2, (y_st - tmp_height) / 2));



            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int N = 256;
            int[] data_x = new int[N];
            int[] data_y = new int[N];

            double gamma;
            gamma = 2.2;

            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                //data_y[i] = (int)(Math.Sin(i) * 100 + 100);
                data_y[i] = (int)(Math.Pow(((double)data_x[i]) / 255, 1 / gamma) * 255);
                //data_y[i] = i;

            }
            plotXY(data_x, data_y);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int N = 50;
            int i;
            int[] data_x = new int[N];
            int[] data_y = new int[N];

            Random r = new Random();
            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                //data_y[i] = (int)(100 * Math.Sin(i));
                data_y[i] = r.Next(50, 60000);

            }
            plotXY(data_x, data_y);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int N = 500;
            int i;
            int[] expo_data_in = new int[N];
            int[] expo_data_out = new int[N];

            expo_data_in[0] = 0; expo_data_out[0] = 70;

            expo_data_in[1] = 1; expo_data_out[1] = 71;

            expo_data_in[2] = 2; expo_data_out[2] = 71;

            expo_data_in[3] = 3; expo_data_out[3] = 71;

            expo_data_in[4] = 4; expo_data_out[4] = 71;

            expo_data_in[5] = 5; expo_data_out[5] = 71;

            expo_data_in[6] = 6; expo_data_out[6] = 71;

            expo_data_in[7] = 7; expo_data_out[7] = 71;

            expo_data_in[8] = 8; expo_data_out[8] = 71;

            expo_data_in[9] = 9; expo_data_out[9] = 72;

            expo_data_in[10] = 10; expo_data_out[10] = 72;

            expo_data_in[11] = 11; expo_data_out[11] = 72;

            expo_data_in[12] = 12; expo_data_out[12] = 72;

            expo_data_in[13] = 13; expo_data_out[13] = 72;

            expo_data_in[14] = 14; expo_data_out[14] = 72;

            expo_data_in[15] = 15; expo_data_out[15] = 72;

            expo_data_in[16] = 16; expo_data_out[16] = 72;

            expo_data_in[17] = 17; expo_data_out[17] = 73;

            expo_data_in[18] = 18; expo_data_out[18] = 73;

            expo_data_in[19] = 19; expo_data_out[19] = 73;

            expo_data_in[20] = 20; expo_data_out[20] = 73;

            expo_data_in[21] = 21; expo_data_out[21] = 73;

            expo_data_in[22] = 22; expo_data_out[22] = 73;

            expo_data_in[23] = 23; expo_data_out[23] = 73;

            expo_data_in[24] = 24; expo_data_out[24] = 73;

            expo_data_in[25] = 25; expo_data_out[25] = 74;

            expo_data_in[26] = 26; expo_data_out[26] = 74;

            expo_data_in[27] = 27; expo_data_out[27] = 74;

            expo_data_in[28] = 28; expo_data_out[28] = 74;

            expo_data_in[29] = 29; expo_data_out[29] = 74;

            expo_data_in[30] = 30; expo_data_out[30] = 74;

            expo_data_in[31] = 31; expo_data_out[31] = 74;

            expo_data_in[32] = 32; expo_data_out[32] = 75;

            expo_data_in[33] = 33; expo_data_out[33] = 75;

            expo_data_in[34] = 34; expo_data_out[34] = 75;

            expo_data_in[35] = 35; expo_data_out[35] = 75;

            expo_data_in[36] = 36; expo_data_out[36] = 75;

            expo_data_in[37] = 37; expo_data_out[37] = 75;

            expo_data_in[38] = 38; expo_data_out[38] = 75;

            expo_data_in[39] = 39; expo_data_out[39] = 75;

            expo_data_in[40] = 40; expo_data_out[40] = 76;

            expo_data_in[41] = 41; expo_data_out[41] = 76;

            expo_data_in[42] = 42; expo_data_out[42] = 76;

            expo_data_in[43] = 43; expo_data_out[43] = 76;

            expo_data_in[44] = 44; expo_data_out[44] = 76;

            expo_data_in[45] = 45; expo_data_out[45] = 76;

            expo_data_in[46] = 46; expo_data_out[46] = 76;

            expo_data_in[47] = 47; expo_data_out[47] = 76;

            expo_data_in[48] = 48; expo_data_out[48] = 77;

            expo_data_in[49] = 49; expo_data_out[49] = 77;

            expo_data_in[50] = 50; expo_data_out[50] = 77;

            expo_data_in[51] = 51; expo_data_out[51] = 77;

            expo_data_in[52] = 52; expo_data_out[52] = 77;

            expo_data_in[53] = 53; expo_data_out[53] = 77;

            expo_data_in[54] = 54; expo_data_out[54] = 77;

            expo_data_in[55] = 55; expo_data_out[55] = 77;

            expo_data_in[56] = 56; expo_data_out[56] = 78;

            expo_data_in[57] = 57; expo_data_out[57] = 78;

            expo_data_in[58] = 58; expo_data_out[58] = 78;

            expo_data_in[59] = 59; expo_data_out[59] = 78;

            expo_data_in[60] = 60; expo_data_out[60] = 78;

            expo_data_in[61] = 61; expo_data_out[61] = 78;

            expo_data_in[62] = 62; expo_data_out[62] = 78;

            expo_data_in[63] = 63; expo_data_out[63] = 78;

            expo_data_in[64] = 64; expo_data_out[64] = 78;

            expo_data_in[65] = 65; expo_data_out[65] = 79;

            expo_data_in[66] = 66; expo_data_out[66] = 79;

            expo_data_in[67] = 67; expo_data_out[67] = 79;

            expo_data_in[68] = 68; expo_data_out[68] = 79;

            expo_data_in[69] = 69; expo_data_out[69] = 79;

            expo_data_in[70] = 70; expo_data_out[70] = 79;

            expo_data_in[71] = 71; expo_data_out[71] = 79;

            expo_data_in[72] = 72; expo_data_out[72] = 79;

            expo_data_in[73] = 73; expo_data_out[73] = 80;

            expo_data_in[74] = 74; expo_data_out[74] = 80;

            expo_data_in[75] = 75; expo_data_out[75] = 79;

            expo_data_in[76] = 76; expo_data_out[76] = 79;

            expo_data_in[77] = 77; expo_data_out[77] = 80;

            expo_data_in[78] = 78; expo_data_out[78] = 80;

            expo_data_in[79] = 79; expo_data_out[79] = 80;

            expo_data_in[80] = 80; expo_data_out[80] = 80;

            expo_data_in[81] = 81; expo_data_out[81] = 80;

            expo_data_in[82] = 82; expo_data_out[82] = 80;

            expo_data_in[83] = 83; expo_data_out[83] = 80;

            expo_data_in[84] = 84; expo_data_out[84] = 80;

            expo_data_in[85] = 85; expo_data_out[85] = 80;

            expo_data_in[86] = 86; expo_data_out[86] = 81;

            expo_data_in[87] = 87; expo_data_out[87] = 81;

            expo_data_in[88] = 88; expo_data_out[88] = 81;

            expo_data_in[89] = 89; expo_data_out[89] = 81;

            expo_data_in[90] = 90; expo_data_out[90] = 81;

            expo_data_in[91] = 91; expo_data_out[91] = 81;

            expo_data_in[92] = 92; expo_data_out[92] = 81;

            expo_data_in[93] = 93; expo_data_out[93] = 81;

            expo_data_in[94] = 94; expo_data_out[94] = 81;

            expo_data_in[95] = 95; expo_data_out[95] = 82;

            expo_data_in[96] = 96; expo_data_out[96] = 82;

            expo_data_in[97] = 97; expo_data_out[97] = 82;

            expo_data_in[98] = 98; expo_data_out[98] = 82;

            expo_data_in[99] = 99; expo_data_out[99] = 82;

            expo_data_in[100] = 100; expo_data_out[100] = 82;

            expo_data_in[101] = 101; expo_data_out[101] = 82;

            expo_data_in[102] = 102; expo_data_out[102] = 82;

            expo_data_in[103] = 103; expo_data_out[103] = 82;

            expo_data_in[104] = 104; expo_data_out[104] = 83;

            expo_data_in[105] = 105; expo_data_out[105] = 83;

            expo_data_in[106] = 106; expo_data_out[106] = 83;

            expo_data_in[107] = 107; expo_data_out[107] = 83;

            expo_data_in[108] = 108; expo_data_out[108] = 83;

            expo_data_in[109] = 109; expo_data_out[109] = 83;

            expo_data_in[110] = 110; expo_data_out[110] = 83;

            expo_data_in[111] = 111; expo_data_out[111] = 83;

            expo_data_in[112] = 112; expo_data_out[112] = 83;

            expo_data_in[113] = 113; expo_data_out[113] = 83;

            expo_data_in[114] = 114; expo_data_out[114] = 84;

            expo_data_in[115] = 115; expo_data_out[115] = 84;

            expo_data_in[116] = 116; expo_data_out[116] = 84;

            expo_data_in[117] = 117; expo_data_out[117] = 84;

            expo_data_in[118] = 118; expo_data_out[118] = 84;

            expo_data_in[119] = 119; expo_data_out[119] = 84;

            expo_data_in[120] = 120; expo_data_out[120] = 84;

            expo_data_in[121] = 121; expo_data_out[121] = 84;

            expo_data_in[122] = 122; expo_data_out[122] = 84;

            expo_data_in[123] = 123; expo_data_out[123] = 85;

            expo_data_in[124] = 124; expo_data_out[124] = 85;

            expo_data_in[125] = 125; expo_data_out[125] = 85;

            expo_data_in[126] = 126; expo_data_out[126] = 85;

            expo_data_in[127] = 127; expo_data_out[127] = 85;

            expo_data_in[128] = 128; expo_data_out[128] = 85;

            expo_data_in[129] = 129; expo_data_out[129] = 85;

            expo_data_in[130] = 130; expo_data_out[130] = 85;

            expo_data_in[131] = 131; expo_data_out[131] = 85;

            expo_data_in[132] = 132; expo_data_out[132] = 86;

            expo_data_in[133] = 133; expo_data_out[133] = 86;

            expo_data_in[134] = 134; expo_data_out[134] = 86;

            expo_data_in[135] = 135; expo_data_out[135] = 86;

            expo_data_in[136] = 136; expo_data_out[136] = 86;

            expo_data_in[137] = 137; expo_data_out[137] = 86;

            expo_data_in[138] = 138; expo_data_out[138] = 86;

            expo_data_in[139] = 139; expo_data_out[139] = 86;

            expo_data_in[140] = 140; expo_data_out[140] = 86;

            expo_data_in[141] = 141; expo_data_out[141] = 86;

            expo_data_in[142] = 142; expo_data_out[142] = 86;

            expo_data_in[143] = 143; expo_data_out[143] = 87;

            expo_data_in[144] = 144; expo_data_out[144] = 87;

            expo_data_in[145] = 145; expo_data_out[145] = 87;

            expo_data_in[146] = 146; expo_data_out[146] = 87;

            expo_data_in[147] = 147; expo_data_out[147] = 87;

            expo_data_in[148] = 148; expo_data_out[148] = 87;

            expo_data_in[149] = 149; expo_data_out[149] = 87;

            expo_data_in[150] = 150; expo_data_out[150] = 87;

            expo_data_in[151] = 151; expo_data_out[151] = 87;

            expo_data_in[152] = 152; expo_data_out[152] = 87;

            expo_data_in[153] = 153; expo_data_out[153] = 88;

            expo_data_in[154] = 154; expo_data_out[154] = 88;

            expo_data_in[155] = 155; expo_data_out[155] = 88;

            expo_data_in[156] = 156; expo_data_out[156] = 88;

            expo_data_in[157] = 157; expo_data_out[157] = 88;

            expo_data_in[158] = 158; expo_data_out[158] = 88;

            expo_data_in[159] = 159; expo_data_out[159] = 88;

            expo_data_in[160] = 160; expo_data_out[160] = 88;

            expo_data_in[161] = 161; expo_data_out[161] = 88;

            expo_data_in[162] = 162; expo_data_out[162] = 88;

            expo_data_in[163] = 163; expo_data_out[163] = 89;

            expo_data_in[164] = 164; expo_data_out[164] = 89;

            expo_data_in[165] = 165; expo_data_out[165] = 89;

            expo_data_in[166] = 166; expo_data_out[166] = 89;

            expo_data_in[167] = 167; expo_data_out[167] = 89;

            expo_data_in[168] = 168; expo_data_out[168] = 89;

            expo_data_in[169] = 169; expo_data_out[169] = 89;

            expo_data_in[170] = 170; expo_data_out[170] = 89;

            expo_data_in[171] = 171; expo_data_out[171] = 89;

            expo_data_in[172] = 172; expo_data_out[172] = 89;

            expo_data_in[173] = 173; expo_data_out[173] = 89;

            expo_data_in[174] = 174; expo_data_out[174] = 90;

            expo_data_in[175] = 175; expo_data_out[175] = 90;

            expo_data_in[176] = 176; expo_data_out[176] = 90;

            expo_data_in[177] = 177; expo_data_out[177] = 90;

            expo_data_in[178] = 178; expo_data_out[178] = 90;

            expo_data_in[179] = 179; expo_data_out[179] = 90;

            expo_data_in[180] = 180; expo_data_out[180] = 90;

            expo_data_in[181] = 181; expo_data_out[181] = 90;

            expo_data_in[182] = 182; expo_data_out[182] = 90;

            expo_data_in[183] = 183; expo_data_out[183] = 90;

            expo_data_in[184] = 184; expo_data_out[184] = 90;

            expo_data_in[185] = 185; expo_data_out[185] = 91;

            expo_data_in[186] = 186; expo_data_out[186] = 91;

            expo_data_in[187] = 187; expo_data_out[187] = 91;

            expo_data_in[188] = 188; expo_data_out[188] = 91;

            expo_data_in[189] = 189; expo_data_out[189] = 91;

            expo_data_in[190] = 190; expo_data_out[190] = 91;

            expo_data_in[191] = 191; expo_data_out[191] = 91;

            expo_data_in[192] = 192; expo_data_out[192] = 91;

            expo_data_in[193] = 193; expo_data_out[193] = 91;

            expo_data_in[194] = 194; expo_data_out[194] = 91;

            expo_data_in[195] = 195; expo_data_out[195] = 92;

            expo_data_in[196] = 196; expo_data_out[196] = 92;

            expo_data_in[197] = 197; expo_data_out[197] = 92;

            expo_data_in[198] = 198; expo_data_out[198] = 92;

            expo_data_in[199] = 199; expo_data_out[199] = 92;

            expo_data_in[200] = 200; expo_data_out[200] = 92;

            expo_data_in[201] = 201; expo_data_out[201] = 92;

            expo_data_in[202] = 202; expo_data_out[202] = 92;

            expo_data_in[203] = 203; expo_data_out[203] = 92;

            expo_data_in[204] = 204; expo_data_out[204] = 92;

            expo_data_in[205] = 205; expo_data_out[205] = 92;

            expo_data_in[206] = 206; expo_data_out[206] = 93;

            expo_data_in[207] = 207; expo_data_out[207] = 93;

            expo_data_in[208] = 208; expo_data_out[208] = 93;

            expo_data_in[209] = 209; expo_data_out[209] = 93;

            expo_data_in[210] = 210; expo_data_out[210] = 93;

            expo_data_in[211] = 211; expo_data_out[211] = 93;

            expo_data_in[212] = 212; expo_data_out[212] = 93;

            expo_data_in[213] = 213; expo_data_out[213] = 92;

            expo_data_in[214] = 214; expo_data_out[214] = 92;

            expo_data_in[215] = 215; expo_data_out[215] = 92;

            expo_data_in[216] = 216; expo_data_out[216] = 92;

            expo_data_in[217] = 217; expo_data_out[217] = 93;

            expo_data_in[218] = 218; expo_data_out[218] = 93;

            expo_data_in[219] = 219; expo_data_out[219] = 93;

            expo_data_in[220] = 220; expo_data_out[220] = 93;

            expo_data_in[221] = 221; expo_data_out[221] = 93;

            expo_data_in[222] = 222; expo_data_out[222] = 93;

            expo_data_in[223] = 223; expo_data_out[223] = 93;

            expo_data_in[224] = 224; expo_data_out[224] = 93;

            expo_data_in[225] = 225; expo_data_out[225] = 93;

            expo_data_in[226] = 226; expo_data_out[226] = 93;

            expo_data_in[227] = 227; expo_data_out[227] = 94;

            expo_data_in[228] = 228; expo_data_out[228] = 94;

            expo_data_in[229] = 229; expo_data_out[229] = 94;

            expo_data_in[230] = 230; expo_data_out[230] = 94;

            expo_data_in[231] = 231; expo_data_out[231] = 94;

            expo_data_in[232] = 232; expo_data_out[232] = 94;

            expo_data_in[233] = 233; expo_data_out[233] = 94;

            expo_data_in[234] = 234; expo_data_out[234] = 94;

            expo_data_in[235] = 235; expo_data_out[235] = 95;

            expo_data_in[236] = 236; expo_data_out[236] = 95;

            expo_data_in[237] = 237; expo_data_out[237] = 95;

            expo_data_in[238] = 238; expo_data_out[238] = 95;

            expo_data_in[239] = 239; expo_data_out[239] = 95;

            expo_data_in[240] = 240; expo_data_out[240] = 95;

            expo_data_in[241] = 241; expo_data_out[241] = 95;

            expo_data_in[242] = 242; expo_data_out[242] = 95;

            expo_data_in[243] = 243; expo_data_out[243] = 95;

            expo_data_in[244] = 244; expo_data_out[244] = 95;

            expo_data_in[245] = 245; expo_data_out[245] = 95;

            expo_data_in[246] = 246; expo_data_out[246] = 95;

            expo_data_in[247] = 247; expo_data_out[247] = 96;

            expo_data_in[248] = 248; expo_data_out[248] = 96;

            expo_data_in[249] = 249; expo_data_out[249] = 96;

            expo_data_in[250] = 250; expo_data_out[250] = 96;

            expo_data_in[251] = 251; expo_data_out[251] = 96;

            expo_data_in[252] = 252; expo_data_out[252] = 45;

            expo_data_in[253] = 253; expo_data_out[253] = 45;

            expo_data_in[254] = 254; expo_data_out[254] = 45;

            expo_data_in[255] = 255; expo_data_out[255] = 45;

            expo_data_in[256] = 256; expo_data_out[256] = 70;

            expo_data_in[257] = 257; expo_data_out[257] = 70;

            expo_data_in[258] = 258; expo_data_out[258] = 70;

            expo_data_in[259] = 259; expo_data_out[259] = 71;

            expo_data_in[260] = 260; expo_data_out[260] = 71;

            expo_data_in[261] = 261; expo_data_out[261] = 71;

            expo_data_in[262] = 262; expo_data_out[262] = 71;

            expo_data_in[263] = 263; expo_data_out[263] = 71;

            expo_data_in[264] = 264; expo_data_out[264] = 71;

            expo_data_in[265] = 265; expo_data_out[265] = 71;

            expo_data_in[266] = 266; expo_data_out[266] = 71;

            expo_data_in[267] = 267; expo_data_out[267] = 72;

            expo_data_in[268] = 268; expo_data_out[268] = 72;

            expo_data_in[269] = 269; expo_data_out[269] = 72;

            expo_data_in[270] = 270; expo_data_out[270] = 72;

            expo_data_in[271] = 271; expo_data_out[271] = 72;

            expo_data_in[272] = 272; expo_data_out[272] = 72;

            expo_data_in[273] = 273; expo_data_out[273] = 72;

            expo_data_in[274] = 274; expo_data_out[274] = 73;

            expo_data_in[275] = 275; expo_data_out[275] = 73;

            expo_data_in[276] = 276; expo_data_out[276] = 73;

            expo_data_in[277] = 277; expo_data_out[277] = 73;

            expo_data_in[278] = 278; expo_data_out[278] = 73;

            expo_data_in[279] = 279; expo_data_out[279] = 73;

            expo_data_in[280] = 280; expo_data_out[280] = 73;

            expo_data_in[281] = 281; expo_data_out[281] = 73;

            expo_data_in[282] = 282; expo_data_out[282] = 74;

            expo_data_in[283] = 283; expo_data_out[283] = 74;

            expo_data_in[284] = 284; expo_data_out[284] = 74;

            expo_data_in[285] = 285; expo_data_out[285] = 74;

            expo_data_in[286] = 286; expo_data_out[286] = 74;

            expo_data_in[287] = 287; expo_data_out[287] = 74;

            expo_data_in[288] = 288; expo_data_out[288] = 74;

            expo_data_in[289] = 289; expo_data_out[289] = 74;

            expo_data_in[290] = 290; expo_data_out[290] = 75;

            expo_data_in[291] = 291; expo_data_out[291] = 75;

            expo_data_in[292] = 292; expo_data_out[292] = 75;

            expo_data_in[293] = 293; expo_data_out[293] = 75;

            expo_data_in[294] = 294; expo_data_out[294] = 75;

            expo_data_in[295] = 295; expo_data_out[295] = 75;

            expo_data_in[296] = 296; expo_data_out[296] = 75;

            expo_data_in[297] = 297; expo_data_out[297] = 75;

            expo_data_in[298] = 298; expo_data_out[298] = 76;

            expo_data_in[299] = 299; expo_data_out[299] = 76;

            expo_data_in[300] = 300; expo_data_out[300] = 76;

            expo_data_in[301] = 301; expo_data_out[301] = 76;

            expo_data_in[302] = 302; expo_data_out[302] = 76;

            expo_data_in[303] = 303; expo_data_out[303] = 76;

            expo_data_in[304] = 304; expo_data_out[304] = 76;

            expo_data_in[305] = 305; expo_data_out[305] = 76;

            expo_data_in[306] = 306; expo_data_out[306] = 77;

            expo_data_in[307] = 307; expo_data_out[307] = 77;

            expo_data_in[308] = 308; expo_data_out[308] = 77;

            expo_data_in[309] = 309; expo_data_out[309] = 77;

            expo_data_in[310] = 310; expo_data_out[310] = 77;

            expo_data_in[311] = 311; expo_data_out[311] = 77;

            expo_data_in[312] = 312; expo_data_out[312] = 77;

            expo_data_in[313] = 313; expo_data_out[313] = 77;

            expo_data_in[314] = 314; expo_data_out[314] = 78;

            expo_data_in[315] = 315; expo_data_out[315] = 78;

            expo_data_in[316] = 316; expo_data_out[316] = 78;

            expo_data_in[317] = 317; expo_data_out[317] = 78;

            expo_data_in[318] = 318; expo_data_out[318] = 78;

            expo_data_in[319] = 319; expo_data_out[319] = 78;

            expo_data_in[320] = 320; expo_data_out[320] = 78;

            expo_data_in[321] = 321; expo_data_out[321] = 78;

            expo_data_in[322] = 322; expo_data_out[322] = 78;

            expo_data_in[323] = 323; expo_data_out[323] = 79;

            expo_data_in[324] = 324; expo_data_out[324] = 79;

            expo_data_in[325] = 325; expo_data_out[325] = 79;

            expo_data_in[326] = 326; expo_data_out[326] = 79;

            expo_data_in[327] = 327; expo_data_out[327] = 79;

            expo_data_in[328] = 328; expo_data_out[328] = 79;

            expo_data_in[329] = 329; expo_data_out[329] = 79;

            expo_data_in[330] = 330; expo_data_out[330] = 79;

            expo_data_in[331] = 331; expo_data_out[331] = 80;

            expo_data_in[332] = 332; expo_data_out[332] = 80;

            expo_data_in[333] = 333; expo_data_out[333] = 80;

            expo_data_in[334] = 334; expo_data_out[334] = 80;

            expo_data_in[335] = 335; expo_data_out[335] = 80;

            expo_data_in[336] = 336; expo_data_out[336] = 80;

            expo_data_in[337] = 337; expo_data_out[337] = 80;

            expo_data_in[338] = 338; expo_data_out[338] = 80;

            expo_data_in[339] = 339; expo_data_out[339] = 80;

            expo_data_in[340] = 340; expo_data_out[340] = 80;

            expo_data_in[341] = 341; expo_data_out[341] = 81;

            expo_data_in[342] = 342; expo_data_out[342] = 81;

            expo_data_in[343] = 343; expo_data_out[343] = 81;

            expo_data_in[344] = 344; expo_data_out[344] = 81;

            expo_data_in[345] = 345; expo_data_out[345] = 81;

            expo_data_in[346] = 346; expo_data_out[346] = 81;

            expo_data_in[347] = 347; expo_data_out[347] = 81;

            expo_data_in[348] = 348; expo_data_out[348] = 81;

            expo_data_in[349] = 349; expo_data_out[349] = 81;

            expo_data_in[350] = 350; expo_data_out[350] = 82;

            expo_data_in[351] = 351; expo_data_out[351] = 81;

            expo_data_in[352] = 352; expo_data_out[352] = 81;

            expo_data_in[353] = 353; expo_data_out[353] = 81;

            expo_data_in[354] = 354; expo_data_out[354] = 82;

            expo_data_in[355] = 355; expo_data_out[355] = 82;

            expo_data_in[356] = 356; expo_data_out[356] = 82;

            expo_data_in[357] = 357; expo_data_out[357] = 82;

            expo_data_in[358] = 358; expo_data_out[358] = 82;

            expo_data_in[359] = 359; expo_data_out[359] = 82;

            expo_data_in[360] = 360; expo_data_out[360] = 82;

            expo_data_in[361] = 361; expo_data_out[361] = 82;

            expo_data_in[362] = 362; expo_data_out[362] = 82;

            expo_data_in[363] = 363; expo_data_out[363] = 83;

            expo_data_in[364] = 364; expo_data_out[364] = 83;

            expo_data_in[365] = 365; expo_data_out[365] = 83;

            expo_data_in[366] = 366; expo_data_out[366] = 83;

            expo_data_in[367] = 367; expo_data_out[367] = 83;

            expo_data_in[368] = 368; expo_data_out[368] = 83;

            expo_data_in[369] = 369; expo_data_out[369] = 83;

            expo_data_in[370] = 370; expo_data_out[370] = 83;

            expo_data_in[371] = 371; expo_data_out[371] = 83;

            expo_data_in[372] = 372; expo_data_out[372] = 83;

            expo_data_in[373] = 373; expo_data_out[373] = 84;

            expo_data_in[374] = 374; expo_data_out[374] = 84;

            expo_data_in[375] = 375; expo_data_out[375] = 84;

            expo_data_in[376] = 376; expo_data_out[376] = 84;

            expo_data_in[377] = 377; expo_data_out[377] = 84;

            expo_data_in[378] = 378; expo_data_out[378] = 84;

            expo_data_in[379] = 379; expo_data_out[379] = 84;

            expo_data_in[380] = 380; expo_data_out[380] = 84;

            expo_data_in[381] = 381; expo_data_out[381] = 84;

            expo_data_in[382] = 382; expo_data_out[382] = 85;

            expo_data_in[383] = 383; expo_data_out[383] = 85;

            expo_data_in[384] = 384; expo_data_out[384] = 85;

            expo_data_in[385] = 385; expo_data_out[385] = 85;

            expo_data_in[386] = 386; expo_data_out[386] = 85;

            expo_data_in[387] = 387; expo_data_out[387] = 85;

            expo_data_in[388] = 388; expo_data_out[388] = 85;

            expo_data_in[389] = 389; expo_data_out[389] = 85;

            expo_data_in[390] = 390; expo_data_out[390] = 85;

            expo_data_in[391] = 391; expo_data_out[391] = 85;

            expo_data_in[392] = 392; expo_data_out[392] = 86;

            expo_data_in[393] = 393; expo_data_out[393] = 86;

            expo_data_in[394] = 394; expo_data_out[394] = 86;

            expo_data_in[395] = 395; expo_data_out[395] = 86;

            expo_data_in[396] = 396; expo_data_out[396] = 86;

            expo_data_in[397] = 397; expo_data_out[397] = 86;

            expo_data_in[398] = 398; expo_data_out[398] = 86;

            expo_data_in[399] = 399; expo_data_out[399] = 86;

            expo_data_in[400] = 400; expo_data_out[400] = 86;

            expo_data_in[401] = 401; expo_data_out[401] = 86;

            expo_data_in[402] = 402; expo_data_out[402] = 87;

            expo_data_in[403] = 403; expo_data_out[403] = 87;

            expo_data_in[404] = 404; expo_data_out[404] = 87;

            expo_data_in[405] = 405; expo_data_out[405] = 87;

            expo_data_in[406] = 406; expo_data_out[406] = 87;

            expo_data_in[407] = 407; expo_data_out[407] = 87;

            expo_data_in[408] = 408; expo_data_out[408] = 87;

            expo_data_in[409] = 409; expo_data_out[409] = 87;

            expo_data_in[410] = 410; expo_data_out[410] = 87;

            expo_data_in[411] = 411; expo_data_out[411] = 87;

            expo_data_in[412] = 412; expo_data_out[412] = 88;

            expo_data_in[413] = 413; expo_data_out[413] = 88;

            expo_data_in[414] = 414; expo_data_out[414] = 88;

            expo_data_in[415] = 415; expo_data_out[415] = 88;

            expo_data_in[416] = 416; expo_data_out[416] = 88;

            expo_data_in[417] = 417; expo_data_out[417] = 88;

            expo_data_in[418] = 418; expo_data_out[418] = 88;

            expo_data_in[419] = 419; expo_data_out[419] = 88;

            expo_data_in[420] = 420; expo_data_out[420] = 88;

            expo_data_in[421] = 421; expo_data_out[421] = 88;

            expo_data_in[422] = 422; expo_data_out[422] = 88;

            expo_data_in[423] = 423; expo_data_out[423] = 89;

            expo_data_in[424] = 424; expo_data_out[424] = 89;

            expo_data_in[425] = 425; expo_data_out[425] = 89;

            expo_data_in[426] = 426; expo_data_out[426] = 89;

            expo_data_in[427] = 427; expo_data_out[427] = 89;

            expo_data_in[428] = 428; expo_data_out[428] = 89;

            expo_data_in[429] = 429; expo_data_out[429] = 89;

            expo_data_in[430] = 430; expo_data_out[430] = 89;

            expo_data_in[431] = 431; expo_data_out[431] = 89;

            expo_data_in[432] = 432; expo_data_out[432] = 89;

            expo_data_in[433] = 433; expo_data_out[433] = 90;

            expo_data_in[434] = 434; expo_data_out[434] = 90;

            expo_data_in[435] = 435; expo_data_out[435] = 90;

            expo_data_in[436] = 436; expo_data_out[436] = 90;

            expo_data_in[437] = 437; expo_data_out[437] = 90;

            expo_data_in[438] = 438; expo_data_out[438] = 90;

            expo_data_in[439] = 439; expo_data_out[439] = 90;

            expo_data_in[440] = 440; expo_data_out[440] = 90;

            expo_data_in[441] = 441; expo_data_out[441] = 90;

            expo_data_in[442] = 442; expo_data_out[442] = 90;

            expo_data_in[443] = 443; expo_data_out[443] = 91;

            expo_data_in[444] = 444; expo_data_out[444] = 91;

            expo_data_in[445] = 445; expo_data_out[445] = 91;

            expo_data_in[446] = 446; expo_data_out[446] = 91;

            expo_data_in[447] = 447; expo_data_out[447] = 91;

            expo_data_in[448] = 448; expo_data_out[448] = 91;

            expo_data_in[449] = 449; expo_data_out[449] = 91;

            expo_data_in[450] = 450; expo_data_out[450] = 91;

            expo_data_in[451] = 451; expo_data_out[451] = 91;

            expo_data_in[452] = 452; expo_data_out[452] = 91;

            expo_data_in[453] = 453; expo_data_out[453] = 91;

            expo_data_in[454] = 454; expo_data_out[454] = 91;

            expo_data_in[455] = 455; expo_data_out[455] = 92;

            expo_data_in[456] = 456; expo_data_out[456] = 92;

            expo_data_in[457] = 457; expo_data_out[457] = 92;

            expo_data_in[458] = 458; expo_data_out[458] = 92;

            expo_data_in[459] = 459; expo_data_out[459] = 92;

            expo_data_in[460] = 460; expo_data_out[460] = 92;

            expo_data_in[461] = 461; expo_data_out[461] = 92;

            expo_data_in[462] = 462; expo_data_out[462] = 92;

            expo_data_in[463] = 463; expo_data_out[463] = 92;

            expo_data_in[464] = 464; expo_data_out[464] = 92;

            expo_data_in[465] = 465; expo_data_out[465] = 92;

            expo_data_in[466] = 466; expo_data_out[466] = 92;

            expo_data_in[467] = 467; expo_data_out[467] = 92;

            expo_data_in[468] = 468; expo_data_out[468] = 92;

            expo_data_in[469] = 469; expo_data_out[469] = 93;

            expo_data_in[470] = 470; expo_data_out[470] = 93;

            expo_data_in[471] = 471; expo_data_out[471] = 93;

            expo_data_in[472] = 472; expo_data_out[472] = 93;

            expo_data_in[473] = 473; expo_data_out[473] = 93;

            expo_data_in[474] = 474; expo_data_out[474] = 93;

            expo_data_in[475] = 475; expo_data_out[475] = 93;

            expo_data_in[476] = 476; expo_data_out[476] = 93;

            expo_data_in[477] = 477; expo_data_out[477] = 93;

            expo_data_in[478] = 478; expo_data_out[478] = 93;

            expo_data_in[479] = 479; expo_data_out[479] = 93;

            expo_data_in[480] = 480; expo_data_out[480] = 93;

            expo_data_in[481] = 481; expo_data_out[481] = 94;

            expo_data_in[482] = 482; expo_data_out[482] = 94;

            expo_data_in[483] = 483; expo_data_out[483] = 94;

            expo_data_in[484] = 484; expo_data_out[484] = 94;

            expo_data_in[485] = 485; expo_data_out[485] = 94;

            expo_data_in[486] = 486; expo_data_out[486] = 94;

            expo_data_in[487] = 487; expo_data_out[487] = 94;

            expo_data_in[488] = 488; expo_data_out[488] = 94;

            expo_data_in[489] = 489; expo_data_out[489] = 94;

            expo_data_in[490] = 490; expo_data_out[490] = 94;

            expo_data_in[491] = 491; expo_data_out[491] = 94;

            expo_data_in[492] = 492; expo_data_out[492] = 95;

            expo_data_in[493] = 493; expo_data_out[493] = 95;

            expo_data_in[494] = 494; expo_data_out[494] = 95;

            expo_data_in[495] = 495; expo_data_out[495] = 95;

            expo_data_in[496] = 496; expo_data_out[496] = 95;

            expo_data_in[497] = 497; expo_data_out[497] = 95;

            expo_data_in[498] = 498; expo_data_out[498] = 95;

            expo_data_in[499] = 499; expo_data_out[499] = 95;


            plotXY(expo_data_in, expo_data_out);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            int i;
            int N = 20;
            int[] data_x = new int[N];
            int[] data_y = new int[N];

            for (i = 0; i < N; i++)
            {
                data_x[i] = i;
                data_y[i] = (int)(Math.Sin(i) * 100 + 100);
            }
            plotXY(data_x, data_y);
        }
    }
}
