
看
TwistImage

 

 程式師世界 >> 編程語言 >> .NET網頁編程 >> ASP.NET >> ASP.NET基礎 >> 隨機圖片生成器制作方法分享
隨機圖片生成器制作方法分享
日期：2017/1/9 17:39:23      編輯：ASP.NET基礎

復制代碼 代碼如下:
/// <summary>
    /// PicHandler1 的摘要說明
    /// </summary>
    public class PicHandler1 : IHttpHandler, IRequiresSessionState
    {
        private string mCheckNo = string.Empty;
        protected ImgBuilder _ImgBuilder = new ImgBuilder();
        protected VryImgGen _ImgBuilderNew = new VryImgGen();
        private string _text = string.Empty;
        private string _font = "宋體";
        private int _fontSize = 8;
        private int _padding = 2;
        public void ProcessRequest(HttpContext context)
        {
            mCheckNo = DisCheckNo();
            context.Session["CheckCode"] = mCheckNo;
            this._ImgBuilder.FontSize = this._fontSize;
            this._ImgBuilder.Padding = this._padding;

            if (!string.IsNullOrEmpty(this._font))
            {
                this._ImgBuilder.Fonts = new string[] { this._font };
            }
            this._ImgBuilderNew.ChaosWight = 40;
            this._ImgBuilderNew.FontSize = 25;

            this._ImgBuilderNew.Padding = 3;
            System.Drawing.Bitmap image =
             this._ImgBuilderNew.CreateImage(mCheckNo);
            System.IO.MemoryStream ms = new System.IO.MemoryStream();
            image.Save(ms, System.Drawing.Imaging.ImageFormat.Jpeg);
            context.Response.ClearContent();
            context.Response.ContentType = "image/Jpeg";
            context.Response.BinaryWrite(ms.ToArray());
            context.Session["CheckCode"] = mCheckNo.ToString(); //如果沒有實現IRequiresSessionState，則這裡會出錯，也無法生成圖片
            context.Response.End();
        }

        //驗證碼生成
        protected string DisCheckNo()
        {
            string hash = HashCode.GetNext();
            string CheckNo = string.Empty;
            Random rd = new Random(DateTime.Now.Millisecond);
            for (int i = 0; i < 6; i++)
            {
                CheckNo += hash.Substring(rd.Next(1, hash.Length - 1), 1);
            }
            CheckNo = CheckNo.Replace("0", rd.Next(1, 9).ToString());
            CheckNo = CheckNo.Replace("o", rd.Next(1, 9).ToString());
            CheckNo = CheckNo.Replace("O", rd.Next(1, 9).ToString());
            return CheckNo;
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }


調用的類

復制代碼 代碼如下:
using System;
using System.Drawing;
using System.Text;

/// <summary>
/// VryImgGen 的摘要說明
/// </summary>
public class VryImgGen
{
    public static string ChineseChars = String.Empty;

    /// <summary>
    /// 英文與數字串
    /// </summary>
    protected static readonly string EnglishOrNumChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public VryImgGen()
    {
        rnd = new Random(unchecked((int)DateTime.Now.Ticks));
    }

    /// <summary>
    /// 全局隨機數生成器
    /// </summary>
    private Random rnd;

    int length = 5;
    /// <summary>
    /// 驗證碼長度(默認6個驗證碼的長度)
    /// </summary>
    public int Length
    {
        get { return length; }
        set { length = value; }
    }

    int fontSize = 20;
    /// <summary>
    /// 驗證碼字體大小(為了顯示扭曲效果，默認30像素，可以自行修改)
    /// </summary>
    public int FontSize
    {
        get { return fontSize; }
        set { fontSize = value; }
    }

    int padding = 4;
    /// <summary>
    /// 邊框補(默認4像素)
    /// </summary>
    public int Padding
    {
        get { return padding; }
        set { padding = value; }
    }

    bool chaos = true;
    /// <summary>
    /// 是否輸出燥點(默認輸出)
    /// </summary>
    public bool Chaos
    {
        get { return chaos; }
        set { chaos = value; }
    }

    Color chaosColor = Color.LightGray;
    /// <summary>
    /// 輸出燥點的顏色(默認灰色)
    /// </summary>
    public Color ChaosColor
    {
        get { return chaosColor; }
        set { chaosColor = value; }
    }

    int chaosWight = 1;
    /// <summary>
    /// 輸出燥點的濃度
    /// </summary>
    public int ChaosWight
    {
        get { return chaosWight; }
        set { chaosWight = value; }
    }

    Color backgroundColor = Color.White;
    /// <summary>
    /// 自定義背景色(默認白色)
    /// </summary>
    public Color BackgroundColor
    {
        get { return backgroundColor; }
        set { backgroundColor = value; }
    }

    Color[] colors = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
    /// <summary>
    /// 自定義隨機顏色數組
    /// </summary>
    public Color[] Colors
    {
        get { return colors; }
        set { colors = value; }
    }

    string[] fonts = { "Arial", "Georgia" };
    /// <summary>
    /// 自定義字體數組
    /// </summary>
    public string[] Fonts
    {
        get { return fonts; }
        set { fonts = value; }
    }

    #region 產生波形濾鏡效果

    private const double PI = 3.1415926535897932384626433832795;
    private const double PI2 = 6.283185307179586476925286766559;

								    /// <summary>
								    /// 正弦曲線Wave扭曲圖片（Edit By 51aspx.com）
								    /// </summary>
								    /// <param name="srcBmp">圖片路徑</param>
								    /// <param name="bXDir">如果扭曲則選擇為True</param>
								    /// <param name="nMultValue">波形的幅度倍數，越大扭曲的程度越高，一般為3</param>
								    /// <param name="dPhase">波形的起始相位，取值區間[0-2*PI)</param>
								    /// <returns></returns>
								    public System.Drawing.Bitmap TwistImage(Bitmap srcBmp, bool bXDir, double dMultValue, double dPhase)
								    {
								        System.Drawing.Bitmap destBmp = new Bitmap(srcBmp.Width, srcBmp.Height);
								
								        // 將位圖背景填充為白色
								        System.Drawing.Graphics graph = System.Drawing.Graphics.FromImage(destBmp);
								        graph.FillRectangle(new SolidBrush(System.Drawing.Color.White), 0, 0, destBmp.Width, destBmp.Height);
								        graph.Dispose();
								
								        double dBaseAxisLen = bXDir ? (double)destBmp.Height : (double)destBmp.Width;
								
								        for (int i = 0; i < destBmp.Width; i++)
								        {
								            for (int j = 0; j < destBmp.Height; j++)
								            {
								                double dx = 0;
								                dx = bXDir ? (PI2 * (double)j) / dBaseAxisLen : (PI2 * (double)i) / dBaseAxisLen;
								                dx += dPhase;
								                double dy = Math.Sin(dx);
								
								                // 取得當前點的顏色
								                int nOldX = 0, nOldY = 0;
								                nOldX = bXDir ? i + (int)(dy * dMultValue) : i;
								                nOldY = bXDir ? j : j + (int)(dy * dMultValue);
								
								                System.Drawing.Color color = srcBmp.GetPixel(i, j);
								                if (nOldX >= 0 && nOldX < destBmp.Width
								                 && nOldY >= 0 && nOldY < destBmp.Height)
								                {
								                    destBmp.SetPixel(nOldX, nOldY, color);
								                }
								            }
								        }
								
								        return destBmp;
								    }
								
								 
								
								    #endregion

    /// <summary>
    /// 生成校驗碼圖片
    /// </summary>
    /// <param name="code">驗證碼</param>
    /// <returns></returns>
    public Bitmap CreateImage(string code)
    {
        int fSize = FontSize;
        int fWidth = fSize + Padding;

        int imageWidth = (int)(code.Length * fWidth) + 4 + Padding * 2;
        int imageHeight = fSize * 2 + Padding * 2;

        System.Drawing.Bitmap image = new System.Drawing.Bitmap(imageWidth - 10, imageHeight - 10);

        Graphics g = Graphics.FromImage(image);

        g.Clear(BackgroundColor);

        //給背景添加隨機生成的燥點
        if (this.Chaos)
        {

            Pen pen = new Pen(ChaosColor, 0);
            int c = ChaosWight * 10;

            for (int i = 0; i < c; i++)
            {
                int x = rnd.Next(image.Width);
                int y = rnd.Next(image.Height);

                g.DrawRectangle(pen, x, y, 1, 1);
            }
        }

        int left = 0, top = 0, top1 = 1, top2 = 1;

        int n1 = (imageHeight - FontSize - Padding * 2);
        int n2 = n1 / 4;
        top1 = n2;
        top2 = n2 * 2;

        Font f;
        Brush b;

        int cindex, findex;

        //隨機字體和顏色的驗證碼字符
        for (int i = 0; i < code.Length; i++)
        {
            cindex = rnd.Next(Colors.Length - 1);
            findex = rnd.Next(Fonts.Length - 1);

            f = new System.Drawing.Font(Fonts[findex], fSize, System.Drawing.FontStyle.Bold);
            b = new System.Drawing.SolidBrush(Colors[cindex]);

            if (i % 2 == 1)
            {
                top = top2;
            }
            else
            {
                top = top1;
            }

            left = i * fWidth;

            g.DrawString(code.Substring(i, 1), f, b, left, top);
        }

        //畫一個邊框 邊框顏色為Color.Gainsboro
        g.DrawRectangle(new Pen(Color.Gainsboro, 0), 0, 0, image.Width - 1, image.Height - 1);
        g.Dispose();

        //產生波形（Add By 51aspx.com）
        image = TwistImage(image, true, 8, 4);

        return image;
    }

    /// <summary>
    /// 生成隨機字符碼
    /// </summary>
    /// <param name="codeLen">字符串長度</param>
    /// <param name="zhCharsCount">中文字符數</param>
    /// <returns></returns>
    public string CreateVerifyCode(int codeLen, int zhCharsCount)
    {
        char[] chs = new char[codeLen];

        int index;
        for (int i = 0; i < zhCharsCount; i++)
        {
            index = rnd.Next(0, codeLen);
            if (chs[index] == '\0')
                chs[index] = CreateZhChar();
            else
                --i;
        }
        for (int i = 0; i < codeLen; i++)
        {
            if (chs[i] == '\0')
                chs[i] = CreateEnOrNumChar();
        }

        return new string(chs, 0, chs.Length);
    }

    /// <summary>
    /// 生成默認長度5的隨機字符碼
    /// </summary>
    /// <returns></returns>
    public string CreateVerifyCode()
    {
        return CreateVerifyCode(Length, 0);
    }

    /// <summary>
    /// 生成英文或數字字符
    /// </summary>
    /// <returns></returns>
    protected char CreateEnOrNumChar()
    {
        return EnglishOrNumChars[rnd.Next(0, EnglishOrNumChars.Length)];
    }

    /// <summary>
    /// 生成漢字字符
    /// </summary>
    /// <returns></returns>
    protected char CreateZhChar()
    {
        //若提供了漢字集，查詢漢字集選取漢字
        if (ChineseChars.Length > 0)
        {
            return ChineseChars[rnd.Next(0, ChineseChars.Length)];
        }
        //若沒有提供漢字集，則根據《GB2312簡體中文編碼表》編碼規則構造漢字
        else
        {
            byte[] bytes = new byte[2];

            //第一個字節值在0xb0, 0xf7之間
            bytes[0] = (byte)rnd.Next(0xb0, 0xf8);
            //第二個字節值在0xa1, 0xfe之間
            bytes[1] = (byte)rnd.Next(0xa1, 0xff);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str1 = Encoding.GetEncoding("gb2312").GetString(bytes);

            return str1[0];
        }
    }

}

    上一頁:淺談.net平台下深拷貝和淺拷貝
    下一頁:asp.net 參數不同共用一個頁面的實現方法

ASP.NET基礎
ASP.NET Table 表格控件的使用方法

一個Table對象包含多個行TableRow，每一行又包含T
ASP.NET MVC5網站開發之登錄、驗證和注銷管理員篇1（六）

上次業務邏輯和展示層的架構都寫了，可以開始進行具體功能的實現
Asp.Net 和 AJAX.Net 的區別第1/2頁

原文：http://www.microsoft.com/ch
.Net Compact Framework開發小技巧 推薦

1. 獲取應用程序當前的路徑 復制代碼 代碼如下:Syste
MVC+EasyUI+三層架構簡單權限管理系統

閒來無事把以前做的一個項目整理了一下，今天拿出來跟大家分享，
.NET裝飾模式講解

裝飾模式的定義：裝飾模式是在不必改變原類文件和使用繼承的情況
相關文章

    使用富文本編輯器上傳圖片實例詳解
    jsp中點擊圖片彈出文件上傳界面及實現預覽實例詳解
    用JSP實現數據庫圖片的存儲與顯示實例
    圖片-一道ACM試題，求大神解答，如果有代碼就更好了
    C#無損壓縮圖片，
    C#無損壓縮圖片，
    使用富文本編輯器上傳圖片實例詳解，文本編輯器上傳圖片
    jsp中點擊圖片彈出文件上傳界面及實現預覽實例詳解，jsp文件上傳
    img的src地址是一個請求的方式來顯示圖片方法，src顯示圖片
    C#批量生成隨機密碼，必須包含數字和字母，並用加密算法加密

閱讀排行榜
asp.net 權限管理分析
asp.net中Repeart選中整行操作實例
頁面爬蟲(獲取其他頁面HTML)加載到自己頁面示例
用CSS實現圖片傾斜 只支持IE
ASP.NET中Request.Form中文亂碼的解決方法
ASP.NET Web Pages 文件夾
spring mvc整合freemarker基於注解方式
如何實現ListView高效分頁代碼
解決.net項目中上傳的圖片或者文件太大無法上傳問題
asp.net(C#)使用QRCode生成圖片中心加Logo或圖像的二維碼實例
實現onmouseover和onmouseout應用於RadioButtonList或CheckBoxList控件上
熱門圖文
ASP.net Server Application Unavailable
C++中的函數重載
Aspfso檢測文件、磁盤、文件夾是否存在代碼
android-小白 在做Android新聞端 用json獲取網頁數據 出現如下圖的報錯 不知道怎麼改
JSP獲取服務器時間以倒計時的形式在頁面顯示
關於strcpy，strncpy以及memcpy的學習
用InstallShield6.22制作帶ODBC安裝軟件
php similar_text()函數的定義和用法
欄目導航
ASP.NET基礎
關於ASP.NET
Copyright © 程式師世界 All Rights Reserved
