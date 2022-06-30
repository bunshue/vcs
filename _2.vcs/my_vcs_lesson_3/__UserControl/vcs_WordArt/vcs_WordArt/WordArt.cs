using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;
using System.Drawing.Drawing2D;

//这是一个艺术字的控件
namespace vcs_WordArt
{
    public partial class WordArt : UserControl
    {
        //文本属性
        private string _text = "艺术字的控件";
        public string Caption
        {
            get { return _text; }
            set { _text = value; }
        }
        //字体以及大小
        private Font _WordArtFont = new Font("標楷體", 24);
        public Font WordArtFont
        {
            get { return _WordArtFont; }
            set { _WordArtFont = value; }
        }
        //颜色
        private Color _WordArtForeColor = Color.BlueViolet;
        public Color WordArtForeColor
        {
            get { return _WordArtForeColor; }
            set { _WordArtForeColor = value; }
        }
        //阴影的颜色
        private Color _WordArtBackColor = Color.Gray;
        public Color WordArtBackColor
        {
            set { _WordArtBackColor = value; }
            get { return _WordArtBackColor; }
        }
        //文本输出质量：呈现模式和平滑效果
        private TextRenderingHint _TextRenderingHint = TextRenderingHint.ClearTypeGridFit;
        public TextRenderingHint WordArtTextRenderingHint
        {
            get { return _TextRenderingHint; }
            set { _TextRenderingHint = value; }
        }

        public SmoothingMode _SmoothingMode = SmoothingMode.AntiAlias;
        public SmoothingMode WordArtSmoothingMode
        {
            get { return _SmoothingMode; }
            set { _SmoothingMode = value; }
        }

        public WordArt()
        {
            InitializeComponent();
        }
        //艺术字的形式:阴影,浮雕……
        private WordArtEffectStyle _WordArtEffect = WordArtEffectStyle.projection;//投影为默认形式;
        public WordArtEffectStyle WordArtEffect
        {
            get { return _WordArtEffect; }
            set { _WordArtEffect = value; }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            Graphics g = this.CreateGraphics();
            Brush backBrush = new SolidBrush(this.WordArtBackColor);
            Brush foreBrush = new SolidBrush(this.WordArtForeColor);

            SizeF size = g.MeasureString(this.Caption, this.WordArtFont);
            Single posX = (this.Width - Convert.ToInt16(size.Width)) / 2;
            Single posY = (this.Height - Convert.ToInt16(size.Height)) / 2;

            switch (this.WordArtEffect)
            {
                case WordArtEffectStyle.projection://投影效果
                    //设置文本输出质量
                    g.TextRenderingHint = this.WordArtTextRenderingHint;
                    g.SmoothingMode = this.WordArtSmoothingMode;
                    Matrix matrix = new Matrix();
                    //投射
                    matrix.Shear(-1.5f, 0.0f);
                    //缩放
                    matrix.Scale(1, 0.5f);
                    //平移
                    matrix.Translate(120, 75);
                    //对绘图平面坐标实施变换
                    g.Transform = matrix;
                    //绘制阴影
                    SolidBrush grayBrush = new SolidBrush(this.WordArtBackColor);
                    SolidBrush colorBrush = new SolidBrush(this.WordArtForeColor);
                    g.DrawString(this.Caption, this.WordArtFont, grayBrush, new PointF(0, 20));
                    g.ResetTransform();
                    //绘制前景
                    g.DrawString(this.Caption, this.WordArtFont, colorBrush, new PointF(0, 20));
                    break;
                case WordArtEffectStyle.embossment://浮雕效果
                    backBrush = Brushes.Black;
                    foreBrush = Brushes.White;

                    g.DrawString(this.Caption, this.WordArtFont, backBrush, posX + 1, posY + 1);
                    g.DrawString(this.Caption, this.WordArtFont, foreBrush, posX, posY);
                    break;
                case WordArtEffectStyle.forme://印版效果
                    int i = 0;
                    backBrush = new SolidBrush(this.WordArtBackColor);
                    foreBrush = new SolidBrush(this.WordArtForeColor);
                    while (i < 20)
                    {
                        g.DrawString(this.Caption, this.WordArtFont, backBrush, posX - i, posY + i);
                        i = i + 1;
                    }
                    g.DrawString(this.Caption, this.WordArtFont, foreBrush, posX, posY);
                    break;
                case WordArtEffectStyle.Reflection://倒影效果
                    backBrush = new SolidBrush(this.WordArtBackColor);
                    foreBrush = new SolidBrush(this.WordArtForeColor);

                    g.TranslateTransform(posX, posY);

                    int ascent = this.WordArtFont.FontFamily.GetCellAscent(this.WordArtFont.Style);
                    int spacing = this.WordArtFont.FontFamily.GetLineSpacing(this.WordArtFont.Style);
                    int lineHeight = System.Convert.ToInt16(this.WordArtFont.GetHeight(g));
                    int height = lineHeight * ascent / spacing;

                    GraphicsState state = g.Save();
                    g.ScaleTransform(1, -1.0f);
                    g.DrawString(this.Caption, this.WordArtFont, backBrush, 0, -height);
                    g.Restore(state);
                    g.DrawString(this.Caption, this.WordArtFont, foreBrush, 0, -height);
                    break;
                case WordArtEffectStyle.shadow://阴影效果
                    Brush shadowBrush = Brushes.Gray;
                    foreBrush = new SolidBrush(this.WordArtBackColor);
                    posX = (this.Width - Convert.ToInt16(size.Width)) / 4;
                    posY = (this.Height - Convert.ToInt16(size.Height)) / 3;
                    g.DrawString(this.Caption, this.WordArtFont, shadowBrush, posX + 20, posY + 20);
                    g.DrawString(this.Caption, this.WordArtFont, foreBrush, posX, posY);
                    break;
                case WordArtEffectStyle.grain://纹理的效果

                    break;

                case WordArtEffectStyle.slope://倾斜
                    g.TranslateTransform(posX, posY);
                    Matrix transform = g.Transform;
                    //右倾斜文字
                    //float shearX = -0.230F;
                    //左倾斜文字
                    float shearX = 0.550F;
                    float shearY = 0.10F;
                    transform.Shear(shearX, shearY);
                    g.Transform = transform;
                    g.DrawString(this.Caption, this.WordArtFont, foreBrush, 0, 0);
                    break;
                case WordArtEffectStyle.shadeLines://渐变
                    Brush ShadowBrush = Brushes.Gray;
                    PointF point = new PointF(0, 0);
                    RectangleF rectangle = new RectangleF(point, size);
                    Brush brush = new LinearGradientBrush(rectangle, Color.Red, Color.Green, LinearGradientMode.Horizontal);
                    int xwidth = (this.Width - Convert.ToInt16(size.Width)) / 2;
                    int xheight = (this.Height - Convert.ToInt16(size.Height)) / 2;
                    g.DrawString(this.Caption, this.WordArtFont, brush, xwidth, xheight);
                    break;
                case WordArtEffectStyle.circumgyrate://旋转
                    for (int n = 0; n <= 360; n += 30)
                    {
                        //平移到对象中心
                        g.TranslateTransform(this.Width / 2, this.Height / 2);
                        //设置Graphics对象的输出角度
                        g.RotateTransform(n);
                        //设置文字填充颜色
                        g.DrawString(this.Caption, this.WordArtFont, foreBrush, 0, 0);
                        //恢复全局变换矩阵
                        g.ResetTransform();
                    }
                    break;
            }
        }
    }
    public enum WordArtEffectStyle
    {
        //投影，浮雕，印版，倒影，阴影，纹理， 倾斜，渐变，旋转
        projection, embossment, forme, Reflection, shadow, grain, slope, shadeLines, circumgyrate
    }
}

