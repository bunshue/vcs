using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Threading.Tasks;

namespace ImageViewer
{
    public partial class MainForm : Form
    {
        /// <summary>
        /// 開いた画像ファイル名
        /// </summary>
        private string image_filename;
        /// <summary>
        /// 画像データ
        /// </summary>
        private ImagingSolution.Imaging.ImageData image;
        /// <summary>
        /// Bitmapクラス（表示用）
        /// </summary>
        private Bitmap bitmap1;
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
        private Graphics g = null;
        /// <summary>
        /// マウスダウンフラグ
        /// </summary>
        private bool flag_mouse_down = false;
        /// <summary>
        /// マウスをクリックした位置の保持用
        /// </summary>
        private PointF point_old;
        /// <summary>
        /// アフィン変換行列
        /// </summary>
        private Matrix _matAffine;

        Label lb_pixel_info;
        Label lb_image_info;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            show_item_location();

            // ホイールイベントの追加
            this.pictureBox1.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseWheel);

            pictureBox1.AllowDrop = true;

            // リサイズイベントを強制的に実行（Graphicsオブジェクトの作成のため）
            MainForm_Resize(null, null);

            // Matrixクラスの確保（単位行列が代入される）
            _matAffine = new Matrix();

            // コマンドラインの確認
            var cmds = System.Environment.GetCommandLineArgs();
            if (cmds.Length > 1)
            {
                OpenImageFile(cmds[1]);
            }

            open_image_file();
        }

        void show_item_location()
        {
            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);

            this.Size = new Size(1920 * 9 / 10, 900);

            pictureBox1.Size = new Size(1920 * 7 / 10, 500);

            int x_st = this.Width - 250;
            int y_st = 50;

            lb_pixel_info = new Label();
            lb_pixel_info.Location = new Point(x_st, y_st + 0);
            lb_pixel_info.Text = "PixelInfo";
            lb_pixel_info.Size = new Size(150, 50);
            this.Controls.Add(lb_pixel_info);

            lb_image_info = new Label();
            lb_image_info.Location = new Point(x_st, y_st + 40);
            lb_image_info.Text = "ImageInfo";
            lb_image_info.Size = new Size(150, 50);
            this.Controls.Add(lb_image_info);

            richTextBox1.Size = new Size(300, 700);
            richTextBox1.Location = new Point(x_st-70, y_st + 80);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (image != null)
            {
                image.Dispose();
            }
            if (bitmap1 != null)
            {
                bitmap1.Dispose();
            }
        }

        private void MainForm_Resize(object sender, EventArgs e)
        {
            if ((pictureBox1.Width == 0) || (pictureBox1.Height == 0))
            {
                return;
            }

            // PictureBoxと同じ大きさのBitmapクラスを作成する。
            Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            // 空のBitmapをPictureBoxのImageに指定する。
            pictureBox1.Image = bmp;
            // Graphicsオブジェクトの作成(FromImageを使う)
            g = Graphics.FromImage(pictureBox1.Image);

            // 補間モードの設定（このサンプルではNearestNeighborに設定）
            g.InterpolationMode = InterpolationMode.NearestNeighbor;
            // 画像の描画
            DrawImage();
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // フォーカスの設定
            //（クリックしただけではMouseWheelイベントが有効にならない）
            pictureBox1.Focus();
            // マウスをクリックした位置の記録
            point_old.X = e.X;
            point_old.Y = e.Y;
            // マウスダウンフラグ
            flag_mouse_down = true;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // マウスをクリックしながら移動中のとき
            if (flag_mouse_down == true)
            {
                // 画像の移動
                _matAffine.Translate(e.X - point_old.X, e.Y - point_old.Y, MatrixOrder.Append);
                // 画像の描画
                DrawImage();

                // ポインタ位置の保持
                point_old.X = e.X;
                point_old.Y = e.Y;
            }

            // マウスポインタの位置の輝度値表示
            DispPixelInfo(_matAffine, image, e.Location);
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // マウスダウンフラグ
            flag_mouse_down = false;
        }

        private void pictureBox1_DragEnter(object sender, DragEventArgs e)
        {
            //コントロール内にドラッグされたとき実行される
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                //ドラッグされたデータ形式を調べ、ファイルのときはコピーとする
                e.Effect = DragDropEffects.Copy;
            }
            else
            {
                //ファイル以外は受け付けない
                e.Effect = DragDropEffects.None;
            }
        }

        private void pictureBox1_DragDrop(object sender, DragEventArgs e)
        {
            //コントロール内にドロップされたとき実行される
            //ドロップされたすべてのファイル名を取得する
            var fileName = (string[])e.Data.GetData(DataFormats.FileDrop, false);
            //画像ファイルを開く
            OpenImageFile(fileName[0]);
        }

        // マウスホイールイベント
        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (image == null)
            {
                return;
            }

            if (e.Delta > 0)
            {
                if (_matAffine.Elements[0] < 100)  // X方向の倍率を代表してチェック
                {
                    richTextBox1.Text += "放大 在 " + e.Location.ToString() + "\tr=" + _matAffine.Elements[0].ToString() + "\n";
                    ScaleAt(ref _matAffine, 1.5f, e.Location);
                }
            }
            else
            {
                if (_matAffine.Elements[0] > 0.01)  // X方向の倍率を代表してチェック
                {
                    richTextBox1.Text += "縮小 在 " + e.Location.ToString() + "\tr=" + _matAffine.Elements[0].ToString() + "\n";
                    ScaleAt(ref _matAffine, 1.0f / 1.5f, e.Location);
                }
            }
            // 画像の描画
            DrawImage();
        }

        private void pictureBox1_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e)
        {
            richTextBox1.Text += "pictureBox1_PreviewKeyDown\n";
            if ((e.KeyCode == Keys.Right) || (e.KeyCode == Keys.Down) || (e.KeyCode == Keys.PageDown))
            {
                // 次の画像ファイルを開く
                richTextBox1.Text += "pictureBox1_PreviewKeyDown 右 下\n";
                OpenNextFile(image_filename);
            }
            else if ((e.KeyCode == Keys.Left) || (e.KeyCode == Keys.Up) || (e.KeyCode == Keys.PageUp))
            {
                // 前の画像ファイルを開く
                richTextBox1.Text += "pictureBox1_PreviewKeyDown 左 上\n";
                OpenPreviousFile(image_filename);
            }
        }

        private void pictureBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                richTextBox1.Text += "全螢幕顯示圖片\n";
                // 画像全体を表示
                ZoomFit(ref _matAffine, image, pictureBox1);
            }

            if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "原始比例顯示圖片\n";
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
            if (IsImageFile(filename) == false)
            {
                return;
            }

            // 画像データの確保
            if (image != null)
            {
                image.Dispose();
            }
            if (bitmap1 != null)
            {
                bitmap1.Dispose();
            }

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";
            //richTextBox1.Text += "開啟檔案 : " + Path.GetFileName(filename) + "\n";   簡檔名

            image = new ImagingSolution.Imaging.ImageData(filename);
            // 表示用
            bitmap1 = image.ToBitmap();

            // 画像サイズ
            lb_image_info.Text = image.Width.ToString() + " x " + image.Height.ToString() + " x " + image.ImageBit.ToString() + "bit";

            // 表示する画像の領域
            _srcRect = new RectangleF(-0.5f, -0.5f, image.Width, image.Height);
            // 描画元を指定する３点の座標（左上、右上、左下の順）
            _srcPoints[0] = new PointF(_srcRect.Left, _srcRect.Top);
            _srcPoints[1] = new PointF(_srcRect.Right, _srcRect.Top);
            _srcPoints[2] = new PointF(_srcRect.Left, _srcRect.Bottom);

            // 画像全体を表示
            ZoomFit(ref _matAffine, image, pictureBox1);

            // 画像の描画
            DrawImage();

            image_filename = filename;
        }

        /// <summary>
        /// 画像の描画
        /// </summary>
        private void DrawImage()
        {
            if (image == null)
            {
                return;
            }

            if (bitmap1 == null)
            {
                return;
            }

            // pictureBoxのクリア
            g.Clear(pictureBox1.BackColor);

            // 描画先の座標をアフィン変換で求める（左上、右上、左下の順）
            PointF[] destPoints = (PointF[])_srcPoints.Clone();
            // 描画先の座標をアフィン変換で求める（変換後の座標は上書きされる）
            _matAffine.TransformPoints(destPoints);

            // 描画
            g.DrawImage(bitmap1, destPoints, _srcRect, GraphicsUnit.Pixel);

            // 再描画
            pictureBox1.Refresh();
        }

        /// <summary>
        /// 指定した点（point）周りの拡大縮小
        /// </summary>
        /// <param name="scale">倍率</param>
        /// <param name="point">基準点の座標</param>
        private void ScaleAt(ref Matrix mat, float scale, PointF point)
        {
            // 原点へ移動
            mat.Translate(-point.X, -point.Y, MatrixOrder.Append);
            // 拡大縮小
            mat.Scale(scale, scale, MatrixOrder.Append);
            // 元へ戻す
            mat.Translate(point.X, point.Y, MatrixOrder.Append);
        }

        /// <summary>
        /// 画像をpictureBoxのサイズに合わせて全体に表示するアフィン変換行列を求める
        /// </summary>
        /// <param name="mat">アフィン変換行列</param>
        /// <param name="image">画像データ</param>
        /// <param name="dst">描画先のpictureBox</param>
        private void ZoomFit(ref Matrix mat, ImagingSolution.Imaging.ImageData image, PictureBox dst)
        {
            // アフィン変換行列の初期化（単位行列へ）
            mat.Reset();

            int srcWidth = image.Width;
            int srcHeight = image.Height;
            int dstWidth = dst.Width;
            int dstHeight = dst.Height;

            float scale;

            //richTextBox1.Text += "source W = " + srcWidth.ToString() + ", H = " + srcHeight.ToString() + "\n";
            //richTextBox1.Text += "destination W = " + dstWidth.ToString() + ", H = " + dstHeight.ToString() + "\n";

            // 縦に合わせるか？横に合わせるか？
            if (srcHeight * dstWidth > dstHeight * srcWidth)
            {
                // pictureBoxの縦方法に画像表示を合わせる場合
                scale = dstHeight / (float)srcHeight;
                //richTextBox1.Text += "a scale = " + scale.ToString() + "\n";
                mat.Scale(scale, scale, MatrixOrder.Append);
                // 中央へ平行移動
                mat.Translate((dstWidth - srcWidth * scale) / 2f, 0f, MatrixOrder.Append);
            }
            else
            {
                // pictureBoxの横方法に画像表示を合わせる場合
                scale = dstWidth / (float)srcWidth;
                //richTextBox1.Text += "b scale = " + scale.ToString() + "\n";
                mat.Scale(scale, scale, MatrixOrder.Append);
                // 中央へ平行移動
                mat.Translate(0f, (dstHeight - srcHeight * scale) / 2f, MatrixOrder.Append);
            }
        }

        /// <summary>
        /// マウスポインタの位置の画像の輝度値を表示
        /// </summary>
        /// <param name="mat">画像を表示しているアフィン変換行列</param>
        /// <param name="image">表示している画像</param>
        /// <param name="pointPictureBox">表示先のpictureBox</param>
        private void DispPixelInfo(Matrix mat, ImagingSolution.Imaging.ImageData image, PointF pointPictureBox)
        {
            if (image == null)
            {
                return;
            }

            // pictureBox→画像上の座標のアフィン変換行列
            var matInvert = mat.Clone();
            matInvert.Invert();

            // 画像上の座標
            var pointImage = new PointF[1];
            pointImage[0] = pointPictureBox;
            matInvert.TransformPoints(pointImage);

            int picX = (int)Math.Floor(pointImage[0].X + 0.5);
            int picY = (int)Math.Floor(pointImage[0].Y + 0.5);

            string bright = " = ";

            // ポインタ座標が画像の範囲内の場合                                                    カラー画像の場合
            if ((picX >= 0) && (picY >= 0) && (picX < image.Width) && (picY < image.Height) && (image.ImageBit >= 24))
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
            lb_pixel_info.Text = "(" + picX.ToString() + ", " + picY.ToString() + ")" + bright;
        }

        /// <summary>
        /// 指定したファイルが画像ファイルかどうか？調べる
        /// </summary>
        /// <param name="filename">調べるファイル名</param>
        /// <returns></returns>
        private bool IsImageFile(string filename)
        {
            if (File.Exists(filename) == false)
            {
                return false;
            }

            // ファイル形式の確認
            string ext = Path.GetExtension(filename).ToLower();
            if ((ext != ".bmp") && (ext != ".jpg") && (ext != ".png") && (ext != ".tif") && (ext != ".ico"))
            {
                return false;
            }
            return true;
        }

        /// <summary>
        /// 一つ前の画像ファイルを開く
        /// </summary>
        /// <param name="filename">基準となるファイル名</param>
        private void OpenNextFile(string filename)
        {
            if (filename == "")
            {
                return;
            }
            richTextBox1.Text += "OpenNextFile, filename = " + filename + "\n";

            // 指定したファイルのディレクトリ
            var directory = Path.GetDirectoryName(filename);
            // ディレクトリ内のファイル一覧
            var files = Directory.GetFiles(directory, "*", SearchOption.TopDirectoryOnly);
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
            if (filename == "")
            {
                return;
            }
            richTextBox1.Text += "OpenPreviousFile, filename = " + filename + "\n";

            // 指定したファイルのディレクトリ
            var directory = Path.GetDirectoryName(filename);
            // ディレクトリ内のファイル一覧
            var files = Directory.GetFiles(directory, "*", SearchOption.TopDirectoryOnly);
            // 一覧からのIndex番号を取得
            int index = Array.IndexOf(files, filename);

            for (int i = index - 1; i >= 0; i--)
            {
                if (IsImageFile(files[i]))
                {
                    richTextBox1.Text += "old index = " + index.ToString() + "\ti = " + i.ToString() + "\tfilename = " + files[i] + "\n";
                    OpenImageFile(files[i]);
                    break;
                }
            }
        }

        void open_image_file()
        {
            string filename = @"C:\______test_files1\ims01.bmp";
            OpenImageFile(filename);

            /*
            // ファイルを開くダイアログの作成 
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.InitialDirectory = @"C:\______test_files1\";
            // ファイルフィルタ 
            openFileDialog1.Filter = "画像ﾌｧｲﾙ(*.bmp,*.jpg,*.png,*.tif,*.ico)|*.bmp;*.jpg;*.png;*.tif;*.ico";
            // ダイアログの表示 （Cancelボタンがクリックされた場合は何もしない）

            openFileDialog1.FileName = "ims_image.bmp";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                // 画像ファイルを開く
                OpenImageFile(openFileDialog1.FileName);
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
            */
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Focus();
        }
    }
}
