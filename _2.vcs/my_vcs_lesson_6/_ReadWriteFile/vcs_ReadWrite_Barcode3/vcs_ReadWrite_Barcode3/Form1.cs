using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_Barcode3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //製作一維條碼
            string aaaaa = "abcdefg";
            int h = 100;
            StringFormat s = new StringFormat();
            s = StringFormat.GenericDefault;
            Bitmap bitmap1 = GetCode39(aaaaa, h, s);
            pictureBox1.Image = bitmap1;

        }

        /// <summary>
        /// 生成條碼 Bitmap,自定義條碼高度,自定義文字對齊樣式
        /// </summary>
        /// <param name="sourceCode"></param>
        /// <param name="barCodeHeight"></param>
        /// <param name="sf"></param>
        /// <returns></returns>
        public Bitmap GetCode39(string sourceCode, int barCodeHeight, StringFormat sf)
        {
            string BarCodeText = sourceCode.ToUpper();
            int leftMargin = 5;
            int topMargin = 0;
            int thickLength = 2;
            int narrowLength = 1;
            int intSourceLength = sourceCode.Length;
            string strEncode = "010010100"; //添加起始碼“ *”.
            var font = new System.Drawing.Font("Segoe UI", 5);
            string AlphaBet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%*";
            string[] Code39 =
             {
                 /* 0 */ "000110100" , 
                 /* 1 */ "100100001" , 
                 /* 2 */ "001100001" , 
                 /* 3 */ "101100000" ,
                 /* 4 */ "000110001" , 
                 /* 5 */ "100110000" , 
                 /* 6 */ "001110000" , 
                 /* 7 */ "000100101" ,
                 /* 8 */ "100100100" , 
                 /* 9 */ "001100100" , 
                 /* A */ "100001001" , 
                 /* B */ "001001001" ,
                 /* C */ "101001000" , 
                 /* D */ "000011001" , 
                 /* E */ "100011000" , 
                 /* F */ "001011000" ,
                 /* G */ "000001101" , 
                 /* H */ "100001100" , 
                 /* I */ "001001100" , 
                 /* J */ "000011100" ,
                 /* K */ "100000011" , 
                 /* L */ "001000011" , 
                 /* M */ "101000010" , 
                 /* N */ "000010011" ,
                 /* O */ "100010010" , 
                 /* P */ "001010010" , 
                 /* Q */ "000000111" , 
                 /* R */ "100000110" ,
                 /* S */ "001000110" , 
                 /* T */ "000010110" , 
                 /* U */ "110000001" , 
                 /* V */ "011000001" ,
                 /* W */ "111000000" , 
                 /* X */ "010010001" , 
                 /* Y */ "110010000" , 
                 /* Z */ "011010000" ,
                 /* - */ "010000101" , 
                 /* . */ "110000100" , 
                 /*' '*/ "011000100" ,
                 /* $ */ "010101000" ,
                 /* / */ "010100010" , 
                 /* + */ "010001010" , 
                 /* % */ "000101010" , 
                 /* * */ "010010100"  
             };
            sourceCode = sourceCode.ToUpper();
            Bitmap objBitmap = new Bitmap(((thickLength * 3 + narrowLength * 7) * (intSourceLength + 2)) +
                                           (leftMargin * 2), barCodeHeight + (topMargin * 2));
            Graphics objGraphics = Graphics.FromImage(objBitmap);
            objGraphics.FillRectangle(Brushes.White, 0, 0, objBitmap.Width, objBitmap.Height);
            for (int i = 0; i < intSourceLength; i++)
            {
                //非法字符校驗
                if (AlphaBet.IndexOf(sourceCode[i]) == -1 || sourceCode[i] == '*')
                {
                    objGraphics.DrawString("Invalid Bar Code", SystemFonts.DefaultFont, Brushes.Red, leftMargin, topMargin);
                    return objBitmap;
                }
                //編碼
                strEncode = string.Format("{0}0{1}", strEncode,
                Code39[AlphaBet.IndexOf(sourceCode[i])]);
            }
            strEncode = string.Format("{0}0010010100", strEncode); //添加結束碼“*”
            int intEncodeLength = strEncode.Length;
            int intBarWidth;
            for (int i = 0; i < intEncodeLength; i++) //繪制 Code39 barcode
            {
                intBarWidth = strEncode[i] == '1' ? thickLength : narrowLength;
                objGraphics.FillRectangle(i % 2 == 0 ? Brushes.Black : Brushes.White, leftMargin, topMargin, intBarWidth, barCodeHeight);
                leftMargin += intBarWidth;
            }
            //繪制明碼         
            Font barCodeTextFont = new Font("黑體", 10F);
            RectangleF rect = new RectangleF(2, barCodeHeight - 20, objBitmap.Width - 4, 20);
            objGraphics.FillRectangle(Brushes.White, rect);
            //文本對齊
            objGraphics.DrawString(BarCodeText, barCodeTextFont, Brushes.Black, rect, sf);
            return objBitmap;
        }
    }
}
