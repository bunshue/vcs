using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ImageViewer
{
    public partial class MainForm : Form
    {
        /// <summary>
        /// 開いた画像ファイル名
        /// </summary>
        private string _openedFileName;
        /// <summary>
        /// 画像データ
        /// </summary>
        private ImagingSolution.Imaging.ImageData _img;
        /// <summary>
        /// Bitmapクラス（表示用）
        /// </summary>
        private Bitmap _bmp;
        /// <summary>
        /// 表示する画像の領域
        /// </summary>
        private RectangleF _srcRect;
        /// <summary>
        /// 描画元を指定する３点の座標（左上、右上、左下の順）
        /// </summary>
        private PointF[] _srcPoints = new PointF[3];
        /// <summary>
        /// 描画用Graphicsオブジェクト
        /// </summary>
        private Graphics _gPicbox = null;
        /// <summary>
        /// マウスダウンフラグ
        /// </summary>
        private bool _mouseDownFlg = false;
        /// <summary>
        /// マウスをクリックした位置の保持用
        /// </summary>
        private PointF _oldPoint;
        /// <summary>
        /// アフィン変換行列
        /// </summary>
        private System.Drawing.Drawing2D.Matrix _matAffine;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            // ホイールイベントの追加
            this.picImage.MouseWheel
                += new System.Windows.Forms.MouseEventHandler(this.picImage_MouseWheel);

            picImage.AllowDrop = true;

            // リサイズイベントを強制的に実行（Graphicsオブジェクトの作成のため）
            MainForm_Resize(null, null);

            // Matrixクラスの確保（単位行列が代入される）
            _matAffine = new System.Drawing.Drawing2D.Matrix();

            // コマンドラインの確認
            var cmds = System.Environment.GetCommandLineArgs();
            if (cmds.Length > 1)
            {
                OpenImageFile(cmds[1]);
            }
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            // 解放
            if (_img != null)
            {
                _img.Dispose();
            }
            if (_bmp != null)
            {
                _bmp.Dispose();
            }
        }

        private void MainForm_Resize(object sender, EventArgs e)
        {
            if ((picImage.Width == 0) || (picImage.Height == 0)) return;

            // PictureBoxと同じ大きさのBitmapクラスを作成する。
            Bitmap bmpPicBox = new Bitmap(picImage.Width, picImage.Height);
            // 空のBitmapをPictureBoxのImageに指定する。
            picImage.Image = bmpPicBox;
            // Graphicsオブジェクトの作成(FromImageを使う)
            _gPicbox = Graphics.FromImage(picImage.Image);

            // 補間モードの設定（このサンプルではNearestNeighborに設定）
            _gPicbox.InterpolationMode
                = System.Drawing.Drawing2D.InterpolationMode.NearestNeighbor;
            // 画像の描画
            DrawImage();
        }

        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            // ファイルを開くダイアログの作成 
            OpenFileDialog dlg = new OpenFileDialog();
            // ファイルフィルタ 
            dlg.Filter = "画像ﾌｧｲﾙ(*.bmp,*.jpg,*.png,*.tif,*.ico)|*.bmp;*.jpg;*.png;*.tif;*.ico";
            // ダイアログの表示 （Cancelボタンがクリックされた場合は何もしない）
            if (dlg.ShowDialog() == System.Windows.Forms.DialogResult.Cancel) return;

            // 画像ファイルを開く
            OpenImageFile(dlg.FileName);
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            // 終了
            this.Close();
        }

        private void picImage_MouseDown(object sender, MouseEventArgs e)
        {
            // フォーカスの設定
            //（クリックしただけではMouseWheelイベントが有効にならない）
            picImage.Focus();
            // マウスをクリックした位置の記録
            _oldPoint.X = e.X;
            _oldPoint.Y = e.Y;
            // マウスダウンフラグ
            _mouseDownFlg = true;
        }

        private void picImage_MouseMove(object sender, MouseEventArgs e)
        {
            // マウスをクリックしながら移動中のとき
            if (_mouseDownFlg == true)
            {
                // 画像の移動
                _matAffine.Translate(e.X - _oldPoint.X, e.Y - _oldPoint.Y,
                    System.Drawing.Drawing2D.MatrixOrder.Append);
                // 画像の描画
                DrawImage();

                // ポインタ位置の保持
                _oldPoint.X = e.X;
                _oldPoint.Y = e.Y;
            }

            // マウスポインタの位置の輝度値表示
            DispPixelInfo(_matAffine, _img, e.Location);
        }

        private void picImage_MouseUp(object sender, MouseEventArgs e)
        {
            // マウスダウンフラグ
            _mouseDownFlg = false;
        }

        private void picImage_DragEnter(object sender, DragEventArgs e)
        {
            //コントロール内にドラッグされたとき実行される
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
                //ドラッグされたデータ形式を調べ、ファイルのときはコピーとする
                e.Effect = DragDropEffects.Copy;
            else
                //ファイル以外は受け付けない
                e.Effect = DragDropEffects.None;
        }

        private void picImage_DragDrop(object sender, DragEventArgs e)
        {
            //コントロール内にドロップされたとき実行される
            //ドロップされたすべてのファイル名を取得する
            var fileName =
                (string[])e.Data.GetData(DataFormats.FileDrop, false);
            //画像ファイルを開く
            OpenImageFile(fileName[0]);
        }

        // マウスホイールイベント
        private void picImage_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0)
            {
                // 拡大
                if (_matAffine.Elements[0] < 100)  // X方向の倍率を代表してチェック
                {
                    // ポインタの位置周りに拡大
                    ScaleAt(ref _matAffine, 1.5f, e.Location);
                }
            }
            else
            {
                // 縮小
                if (_matAffine.Elements[0] > 0.01)  // X方向の倍率を代表してチェック
                {
                    // ポインタの位置周りに縮小
                    ScaleAt(ref _matAffine, 1.0f / 1.5f, e.Location);
                }
            }
            // 画像の描画
            DrawImage();
        }

        private void picImage_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e)
        {
            if ((e.KeyCode == Keys.Right) || (e.KeyCode == Keys.Down))
            {
                // 次の画像ファイルを開く
                OpenNextFile(_openedFileName);
            }
            else if ((e.KeyCode == Keys.Left) || (e.KeyCode == Keys.Up))
            {
                // 前の画像ファイルを開く
                OpenPreviousFile(_openedFileName);
            }
        }

        private void picImage_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                // 画像全体を表示
                ZoomFit(ref _matAffine, _img, picImage);
            }
            if (e.Button == MouseButtons.Right)
            {
                // マウスポインタ周りに等倍表示
                ScaleAt(ref _matAffine, 1f / _matAffine.Elements[0], e.Location);
            }

            // 画像の描画
            DrawImage();
        }

        /// <summary>
        /// 画像ファイルを開く
        /// </summary>
        /// <param name="filename">画像ファイルのパス</param>
        private void OpenImageFile(string filename)
        {
            if (IsImageFile(filename) == false) return;

            // 画像データの確保
            if (_img != null)
            {
                _img.Dispose();
            }
            if (_bmp != null)
            {
                _bmp.Dispose();
            }
            _img = new ImagingSolution.Imaging.ImageData(filename);
            // 表示用
            _bmp = _img.ToBitmap();

            // 画像サイズ
            lblImageInfo.Text =
                _img.Width.ToString() + " x " +
                _img.Height.ToString() + " x " +
                _img.ImageBit.ToString() + "bit";

            // 表示する画像の領域
            _srcRect = new RectangleF(-0.5f, -0.5f, _img.Width, _img.Height);
            // 描画元を指定する３点の座標（左上、右上、左下の順）
            _srcPoints[0] = new PointF(_srcRect.Left, _srcRect.Top);
            _srcPoints[1] = new PointF(_srcRect.Right, _srcRect.Top);
            _srcPoints[2] = new PointF(_srcRect.Left, _srcRect.Bottom);

            // 画像全体を表示
            ZoomFit(ref _matAffine, _img, picImage);
            // 画像の描画
            DrawImage();

            _openedFileName = filename;

            this.Text = System.IO.Path.GetFileName(filename) + " - ImageViewer";
        }

        /// <summary>
        /// 画像の描画
        /// </summary>
        private void DrawImage()
        {
            if (_img == null) return;
            if (_bmp == null) return;

            // ピクチャボックスのクリア
            _gPicbox.Clear(picImage.BackColor);

            // 描画先の座標をアフィン変換で求める（左上、右上、左下の順）
            PointF[] destPoints = (PointF[])_srcPoints.Clone();
            // 描画先の座標をアフィン変換で求める（変換後の座標は上書きされる）
            _matAffine.TransformPoints(destPoints);

            // 描画
            _gPicbox.DrawImage(
                _bmp,
                destPoints,
                _srcRect,
                GraphicsUnit.Pixel
                );

            // 再描画
            picImage.Refresh();
        }

        /// <summary>
        /// 指定した点（point）周りの拡大縮小
        /// </summary>
        /// <param name="scale">倍率</param>
        /// <param name="point">基準点の座標</param>
        private void ScaleAt(
            ref System.Drawing.Drawing2D.Matrix mat,
            float scale,
            PointF point
            )
        {
            // 原点へ移動
            mat.Translate(-point.X, -point.Y,
                System.Drawing.Drawing2D.MatrixOrder.Append);
            // 拡大縮小
            mat.Scale(scale, scale,
                System.Drawing.Drawing2D.MatrixOrder.Append);
            // 元へ戻す
            mat.Translate(point.X, point.Y,
                System.Drawing.Drawing2D.MatrixOrder.Append);
        }

        /// <summary>
        /// 画像をピクチャボックスのサイズに合わせて全体に表示するアフィン変換行列を求める
        /// </summary>
        /// <param name="mat">アフィン変換行列</param>
        /// <param name="image">画像データ</param>
        /// <param name="dst">描画先のピクチャボックス</param>
        private void ZoomFit(
            ref System.Drawing.Drawing2D.Matrix mat,
            ImagingSolution.Imaging.ImageData image,
            PictureBox dst)
        {
            // アフィン変換行列の初期化（単位行列へ）
            mat.Reset();

            int srcWidth = image.Width;
            int srcHeight = image.Height;
            int dstWidth = dst.Width;
            int dstHeight = dst.Height;

            float scale;

            // 縦に合わせるか？横に合わせるか？
            if (srcHeight * dstWidth > dstHeight * srcWidth)
            {
                // ピクチャボックスの縦方法に画像表示を合わせる場合
                scale = dstHeight / (float)srcHeight;
                mat.Scale(scale, scale, System.Drawing.Drawing2D.MatrixOrder.Append);
                // 中央へ平行移動
                mat.Translate((dstWidth - srcWidth * scale) / 2f, 0f, System.Drawing.Drawing2D.MatrixOrder.Append);
            }
            else
            {
                // ピクチャボックスの横方法に画像表示を合わせる場合
                scale = dstWidth / (float)srcWidth;
                mat.Scale(scale, scale, System.Drawing.Drawing2D.MatrixOrder.Append);
                // 中央へ平行移動
                mat.Translate(0f, (dstHeight - srcHeight * scale) / 2f, System.Drawing.Drawing2D.MatrixOrder.Append);
            }
        }

        /// <summary>
        /// マウスポインタの位置の画像の輝度値を表示
        /// </summary>
        /// <param name="mat">画像を表示しているアフィン変換行列</param>
        /// <param name="image">表示している画像</param>
        /// <param name="pointPictureBox">表示先のピクチャボックス</param>
        private void DispPixelInfo(
            System.Drawing.Drawing2D.Matrix mat,
            ImagingSolution.Imaging.ImageData image,
            PointF pointPictureBox)
        {
            if (image == null) return;

            // ピクチャボックス→画像上の座標のアフィン変換行列
            var matInvert = mat.Clone();
            matInvert.Invert();

            // 画像上の座標
            var pointImage = new PointF[1];
            pointImage[0] = pointPictureBox;
            matInvert.TransformPoints(pointImage);

            int picX = (int)Math.Floor(pointImage[0].X + 0.5);
            int picY = (int)Math.Floor(pointImage[0].Y + 0.5);

            string bright = " = ";

            if (
                (picX >= 0) &&              // ポインタ座標が画像の範囲内の場合
                (picY >= 0) &&
                (picX < image.Width) &&
                (picY < image.Height) &&
                (image.ImageBit >= 24)    // カラー画像の場合
                )
            {
                bright += "(" +
                    image[picY, picX, 2].ToString() + ", " +    // R
                    image[picY, picX, 1].ToString() + ", " +    // G
                    image[picY, picX, 0].ToString() + ")";      // B
            }
            else
            {
                bright += image[picY, picX].ToString();
            }

            // 輝度値の表示（モノクロを除く）
            lblPixelInfo.Text =
                "(" +
                picX.ToString() + ", " +
                picY.ToString() + ")" +
                bright;
        }

        /// <summary>
        /// 指定したファイルが画像ファイルかどうか？調べる
        /// </summary>
        /// <param name="filename">調べるファイル名</param>
        /// <returns></returns>
        private bool IsImageFile(string filename)
        {
            if (System.IO.File.Exists(filename) == false) return false;

            // ファイル形式の確認
            string ext = System.IO.Path.GetExtension(filename).ToLower();
            if (
                (ext != ".bmp") &&
                (ext != ".jpg") &&
                (ext != ".png") &&
                (ext != ".tif") &&
                (ext != ".ico")
                ) return false;

            return true;
        }

        /// <summary>
        /// 一つ前の画像ファイルを開く
        /// </summary>
        /// <param name="filename">基準となるファイル名</param>
        private void OpenNextFile(string filename)
        {
            if (filename == "") return;

            // 指定したファイルのディレクトリ
            var directory = System.IO.Path.GetDirectoryName(filename);
            // ディレクトリ内のファイル一覧
            var files = System.IO.Directory.GetFiles(
                directory, "*", System.IO.SearchOption.TopDirectoryOnly);
            // 一覧からのIndex番号を取得
            int index = Array.IndexOf(files, filename);

            for (int i = index + 1; i < files.Length; i++)
            {
                if (IsImageFile(files[i]))
                {
                    OpenImageFile(files[i]);
                    break;
                }
            }
        }

        /// <summary>
        /// 一つ前の画像ファイルを開く
        /// </summary>
        /// <param name="filename">基準となるファイル名</param>
        private void OpenPreviousFile(string filename)
        {
            if (filename == "") return;

            // 指定したファイルのディレクトリ
            var directory = System.IO.Path.GetDirectoryName(filename);
            // ディレクトリ内のファイル一覧
            var files = System.IO.Directory.GetFiles(
                directory, "*", System.IO.SearchOption.TopDirectoryOnly);
            // 一覧からのIndex番号を取得
            int index = Array.IndexOf(files, filename);

            for (int i = index - 1; i >= 0; i--)
            {
                if (IsImageFile(files[i]))
                {
                    OpenImageFile(files[i]);
                    break;
                }
            }
        }
    }
}
