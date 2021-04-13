using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ImagingSolution
{
    /// <summary>
    /// 行列演算クラスライブラリ
    /// </summary>
    public static class Mat
    {
        /// <summary>
        /// 角度の度数（°）からラジアンへ変更
        /// </summary>
        /// <param name="degree">角度（°）を指定します。</param>
        /// <returns>ラジアン単位の角度</returns>
        public static double Radians(this double degree)
        {
            return Math.PI * degree / 180.0;
        }

        private static dynamic Radians<T>(this T degree) where T : struct
        {
            return Math.PI * (dynamic)degree / 180.0;
        }

        /// <summary>
        /// 角度のラジアンから度へ変更
        /// </summary>
        /// <param name="radian">角度（radian）を指定します。</param>
        /// <returns>度数（°）単位の角度</returns>
        public static double Degrees(this double radian)
        {
            return radian * 180.0 / Math.PI;
        }

        private static dynamic Degrees<T>(this T radian) where T : struct
        {
            return (dynamic)radian * 180.0 / Math.PI;
        }

        /// <summary>
        /// 単位行列を取得します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="size">行列のサイズを指定します。</param>
        /// <returns>単位行列</returns>
        public static T[,] Identity<T>(int size) where T : struct
        {
            var ret = new T[size, size];

            var val = (dynamic)1;

            for (int k = 0; k < size; k++)
            {
                ret[k, k] = val;
            }
            return ret;
        }

        /// <summary>
        /// 行列の要素ごとに加算します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="matA">行列（二次元配列）を指定します。</param>
        /// <param name="matB">行列（二次元配列）を指定します。</param>
        /// <returns></returns>
        public static T[,] Add<T>(this T[,] matA, T[,] matB) where T : struct
        {
            if ((matA == null) || (matB == null)) ThrowException("Add", "matA != null && matB != null");

            if ((matA.GetLength(0) != matB.GetLength(0)) || (matA.GetLength(1) != matB.GetLength(1)))
            {
                ThrowException("Add",  "(matA.Rows == matB.Rows) && (matA.columns == matB.columns)");
            }

            var rows = matA.GetLength(0);
            var columns = matA.GetLength(1);

            var ret = new T[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = matA[row, col] + (dynamic)matB[row, col];
                }
            });
            return ret;
        }

        /// <summary>
        /// 行列の各要素にスカラ値を加算します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="value">加算する値を指定します。</param>
        /// <returns>行列の各要素にスカラ値が加算された行列</returns>
        public static T[,] AddS<T>(this T[,] mat, T value) where T : struct
        {
            if (mat == null) ThrowException("AddS", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var ret = new T[rows, columns];

            var val = (dynamic)value;

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = mat[row, col] + val;
                }
            });
            return ret;
        }

        /// <summary>
        /// 行列の要素ごとに減算します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="matA">行列（二次元配列）を指定します。</param>
        /// <param name="matB">行列（二次元配列）を指定します。</param>
        /// <returns>行列の各要素にスカラ値が減算された行列</returns>
        public static T[,] Sub<T>(this T[,] matA, T[,] matB) where T : struct
        {
            if ((matA == null) || (matB == null)) ThrowException("Sub", "matA != null && matB != null");

            if ((matA.GetLength(0) != matB.GetLength(0)) || (matA.GetLength(1) != matB.GetLength(1)))
            {
                ThrowException("Sub", "(matA.Rows == matB.Rows) && (matA.columns == matB.columns)");
            }

            var rows = matA.GetLength(0);
            var columns = matA.GetLength(1);

            var ret = new T[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = matA[row, col] - (dynamic)matB[row, col];
                }
            });
            return ret;
        }

        /// <summary>
        /// 行列の各要素にスカラ値を減算します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="value">行列の各要素にスカラ値が減算された行列</param>
        /// <returns></returns>
        public static T[,] SubS<T>(this T[,] mat, T value) where T : struct
        {
            if (mat == null) ThrowException("SubS", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var ret = new T[rows, columns];

            var val = (dynamic)value;

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = mat[row, col] - val;
                }
            });
            return ret;
        }

        /// <summary>
        /// 行列の積
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="matA">行列（二次元配列）を指定します。</param>
        /// <param name="matB">行列（二次元配列）を指定します。</param>
        /// <returns>行列の積</returns>
        public static T[,] Mult<T>(this T[,] matA, T[,] matB) where T : struct
        {
            if ((matA == null) || (matB == null)) ThrowException("Mult", "matA != null && matB != null");

            if (matA.GetLength(1) != matB.GetLength(0)) ThrowException("Mult", "matA.Columns == matB.Rows");

            var rows = matA.GetLength(0);
            var columns = matB.GetLength(1);

            var acolumns = matA.GetLength(1);

            var ret = new T[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {

                    dynamic sum = 0;

                    for (int k = 0; k < acolumns; k++)
                    {
                        sum += matA[row, k] * (dynamic)matB[k, col];
                    }
                    ret[row, col] = sum;
                }
            });
            return ret;
        }

        /// <summary>
        /// アダマール積（行列の各要素ごとの積）
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="matA">行列（二次元配列）を指定します。</param>
        /// <param name="matB">行列（二次元配列）を指定します。</param>
        /// <returns>アダマール積</returns>
        public static T[,] Hadam<T>(this T[,] matA, T[,] matB) where T : struct
        {
            if ((matA == null) || (matB == null)) ThrowException("Hadam", "matA != null && matB != null");

            if ((matA.GetLength(0) != matB.GetLength(0)) || (matA.GetLength(1) != matB.GetLength(1))) ThrowException("Hadam", "(matA.Rows == matB.Rows) && (matA.Columns == matB.Columns)"); 

            var rows = matA.GetLength(0);
            var columns = matA.GetLength(1);

            var ret = new T[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = matA[row, col] * (dynamic)matB[row, col];
                }
            });
            return ret;
        }

        /// <summary>
        /// 外積
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="matA">行列（二次元配列[3行1列]）を指定します。</param>
        /// <param name="matB">行列（二次元配列[3行1列]）を指定します。</param>
        /// <returns>外積の値</returns>
        public static T[,] Cross<T>(this T[,] matA, T[,] matB) where T : struct
        {
            if ((matA == null) || (matB == null)) ThrowException("Cross", "matA != null && matB != null");

            if (
                (matA.GetLength(0) != 3) ||
                (matA.GetLength(1) != 1) ||
                (matB.GetLength(0) != 3) ||
                (matB.GetLength(1) != 1)
                )
            {
                ThrowException("Cross", "(Rows == 3) && (columns == 1)");
            }

            var rows = matA.GetLength(0);
            var columns = matB.GetLength(1);

            var ret = new T[3, 1];

            ret[0, 0] = matA[1, 0] * (dynamic)matB[2, 0] - matA[2, 0] * (dynamic)matB[1, 0];
            ret[1, 0] = matA[2, 0] * (dynamic)matB[0, 0] - matA[0, 0] * (dynamic)matB[2, 0];
            ret[2, 0] = matA[0, 0] * (dynamic)matB[1, 0] - matA[1, 0] * (dynamic)matB[0, 0];

            return ret;
        }


        /// <summary>
        /// 転置行列
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <returns>転置行列</returns>
        public static T[,] Transpose<T>(this T[,] mat) where T : struct
        {
            if (mat == null) ThrowException("Transpose", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var ret = new T[columns, rows];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[col, row] = mat[row, col];
                }
            });

            return ret;
        }

        /// <summary>
        /// クローンの作成
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <returns>matがコピーされた行列</returns>
        public static T[,] CloneMat<T>(this T[,] mat) where T : struct
        {
            if (mat == null) ThrowException("Clone", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var ret = new T[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = mat[row, col];
                }
            });
            return ret;
        }

        /// <summary>
        /// 行列のrow1行とrow2行の要素を交換する
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="row1">交換する行番号(0,1,2...)</param>
        /// <param name="row2">交換する行番号(0,1,2...)</param>
        public static void SwapRows<T>(this T[,] mat, int row1, int row2) where T : struct
        {
            var columns = mat.GetLength(1);

            Parallel.For(0, columns, col =>
            {
                var temp = mat[row1, col];
                mat[row1, col] = mat[row2, col];
                mat[row2, col] = temp;
            });
        }

        /// <summary>
        /// LU分解
        /// </summary>
        /// <param name="mat"></param>
        /// <param name="ip"></param>
        /// <returns></returns>
        private static double LuDecomposition(ref double[,] mat, ref int[] ip)
        {
            double det = 0;

            if (mat == null) ThrowException("LuDecomposition", "mat != null");
            if (mat.GetLength(0) != mat.GetLength(1)) ThrowException("LuDecomposition", "mat.Rows == mat.Columns");

            int size = mat.GetLength(0);

            int i, j, k, ii, ik;
            double t, u;

            double[] weight = new double[size];

            for (k = 0; k < size; k++)
            {
                ip[k] = k;
                u = 0;

                for (j = 0; j < size; j++)
                {
                    t = Math.Abs(mat[j, k]);
                    if (t > u)
                    {
                        u = t;
                    }
                }
                if (u == 0)
                {
                    ThrowException("LuDecomposition", "Unable to compute inverse");
                }
                weight[k] = 1 / u;
            }

            j = size - 1;
            det = 1.0;
            for (k = 0; k < size; k++)
            {
                u = -1;
                for (i = k; i < size; i++)
                {
                    ii = ip[i];

                    t = Math.Abs(mat[k, ii]) * weight[ii];

                    if (t > u)
                    {
                        u = t;
                        j = i;
                    }
                }

                ik = ip[j];
                if (j != k)
                {
                    ip[j] = ip[k];
                    ip[k] = ik;
                    det = -det;
                }

                u = mat[k, ik];
                det *= u;
                if (u == 0)
                {
                    ThrowException("LuDecomposition", "Unable to compute inverse");
                }

                for (i = k + 1; i < size; i++)
                {
                    ii = ip[i];
                    t = (mat[k, ii] /= u);

                    for (j = k + 1; j < size; j++)
                    {
                        mat[j, ii] -= t * mat[j, ik];
                    }
                }
            }
            return det;
        }

        /// <summary>
        /// 逆行列を求めます。
        /// </summary>
        /// <param name="mat">行列（正方行列、二次元配列）を指定します。</param>
        /// <returns>逆行列</returns>
        public static double[,] Inverse(this double[,] mat)
        {
            if (mat == null) ThrowException("Inverse", "mat != null");

            int size = mat.GetLength(0);

            var m = mat.CloneMat();
            var m_inv = new double[size, size];

            double det;

            if (size == 1)
            {
                ThrowException("Inverse", "Unable to compute inverse");
            }
            else if (size == 2)
            {
                det = mat[0, 0] * mat[1, 1] - mat[0, 1] * mat[1, 0];

                if (det == 0) ThrowException("Inverse", "Unable to compute inverse");

                m_inv[0, 0] = m[1, 1] / det; m_inv[0, 1] = -m[0, 1] / det;
                m_inv[1, 0] = -m[1, 0] / det; m_inv[1, 1] = m[0, 0] / det;
            }
            else if (size == 3)
            {
                det = m[0, 0] * m[1, 1] * m[2, 2] 
                    + m[1, 0] * m[2, 1] * m[0, 2] 
                    + m[2, 0] * m[0, 1] * m[1, 2] 
                    - m[0, 0] * m[2, 1] * m[1, 2] 
                    - m[2, 0] * m[1, 1] * m[0, 2] 
                    - m[1, 0] * m[0, 1] * m[2, 2];

                if (det == 0) ThrowException("Inverse", "Unable to compute inverse");

                m_inv[0, 0] = (m[1, 1] * m[2, 2] - m[1, 2] * m[2, 1]) / det;
                m_inv[0, 1] = (m[0, 2] * m[2, 1] - m[0, 1] * m[2, 2]) / det;
                m_inv[0, 2] = (m[0, 1] * m[1, 2] - m[0, 2] * m[1, 1]) / det;

                m_inv[1, 0] = (m[1, 2] * m[2, 0] - m[1, 0] * m[2, 2]) / det;
                m_inv[1, 1] = (m[0, 0] * m[2, 2] - m[0, 2] * m[2, 0]) / det;
                m_inv[1, 2] = (m[0, 2] * m[1, 0] - m[0, 0] * m[1, 2]) / det;

                m_inv[2, 0] = (m[1, 0] * m[2, 1] - m[1, 1] * m[2, 0]) / det;
                m_inv[2, 1] = (m[0, 1] * m[2, 0] - m[0, 0] * m[2, 1]) / det;
                m_inv[2, 2] = (m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]) / det;
            }
            else
            {
                int[] ip = new int[size];
                // LU分解
                det = LuDecomposition(ref m, ref ip);

                if (det == 0) ThrowException("Inverse", "Unable to compute inverse");

                Parallel.For(0, size, k =>
                {
                    int i, j, ii;
                    double t;

                    for (i = 0; i < size; i++)
                    {
                        ii = ip[i];

                        if (ii == k)
                        {
                            t = 1;
                        }
                        else
                        {
                            t = 0;
                        }

                        for (j = 0; j < i; j++)
                        {
                            t -= m[j, ii] * m_inv[k, j];
                        }
                        m_inv[k, i] = t;
                    }

                    for (i = size - 1; i >= 0; i--)
                    {
                        t = m_inv[k, i];
                        ii = ip[i];

                        for (j = i + 1; j < size; j++)
                        {
                            t -= m[j, ii] * m_inv[k, j];
                        }
                        m_inv[k, i] = t / m[i, ii];
                    }
                }
                );
            }
            return m_inv;
        }

        /// <summary>
        /// 逆行列を求めます。
        /// </summary>
        /// <param name="mat">行列（正方行列、二次元配列）を指定します。</param>
        /// <returns>逆行列</returns>
        public static float[,] Inverse(this float[,] mat)
        {
            var matD = Cast<float, double>(mat);

            var matInv = Inverse(matD);

            return Cast<double, float>(matInv);
        }

        /// <summary>
        /// 擬似逆行列を求めます。
        /// </summary>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <returns>擬似逆行列</returns>
        public static float[,] PseudoInverse(this float[,] mat)
        {
            var matd = Cast<float, double>(mat);

            var matd_pi = Mult(Inverse(Mult(Transpose(matd), matd)), Transpose(matd));

            return Cast<double, float>(matd_pi);
        }

        /// <summary>
        /// 擬似逆行列を求めます。
        /// </summary>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <returns>擬似逆行列</returns>
        public static double[,] PseudoInverse(this double[,] mat)
        {
            return Mult(Inverse(Mult(Transpose(mat), mat)), Transpose(mat));
        }

        /// <summary>
        /// 行列のサイズ（行数、列数）を変更します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="rows">変更後の行数（-1を指定すると自動調整）</param>
        /// <param name="columns">変更後の列数（-1を指定すると自動調整）</param>
        /// <returns>サイズが変更された行列</returns>
        public static T[,] Reshape<T>(this T[,] mat, int rows, int columns) where T : struct
        {
            if (mat == null) ThrowException("Reshape", "mat != null");

            var srcRows = mat.GetLength(0);
            var srcColumns = mat.GetLength(1);

            if (rows == -1)
            {
                rows = srcRows * srcColumns / columns;
            }

            if (columns == -1)
            {
                columns = srcRows * srcColumns / rows;
            }

            if (srcRows * srcColumns != rows * columns) ThrowException("Reshape", "mat.rows * mat.columns == rows * columns");

            var ret = new T[rows, columns];

            int index = 0;
            int row, col;

            for (int srcRow = 0; srcRow < srcRows; srcRow++)
            {
                for (int srcCol = 0; srcCol < srcColumns; srcCol++)
                {
                    row = index / columns;
                    col = index % columns;

                    ret[row, col] = mat[srcRow, srcCol];
                    index++;
                }
            }
            return ret;
        }

        /// <summary>
        /// 行列（二次元配列）をN行１列の行列に変換します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <returns>N行１列の行列</returns>
        public static T[,] Flatten<T>(this T[,] mat) where T : struct
        {
            return Reshape(mat, -1, 1);
        }

        /// <summary>
        /// 数値型行列（二次元配列）を別の型へ変換します。
        /// </summary>
        /// <typeparam name="T1">元の数値型</typeparam>
        /// <typeparam name="T2">変換後の数値型</typeparam>
        /// <param name="mat">変換後の行列</param>
        /// <returns>型が変更された行列</returns>
        public static T2[,] Cast<T1, T2>(this T1[,] mat) where T1 : struct where T2 : struct
        {
            if (mat == null) ThrowException("Cast", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var ret = new T2[rows, columns];

            Parallel.For(0, rows, row =>
            {
                for (int col = 0; col < columns; col++)
                {
                    ret[row, col] = (T2)(dynamic)mat[row, col];
                }
            });
            return ret;
        }

        ////////////////////////////////////////////////////////////////
        // ユーティリティ
        ////////////////////////////////////////////////////////////////

        /// <summary>
        /// 画像ファイル名を指定して画像データの行列（Byte型の二次元配列）を取得します。
        /// カラーの場合、B,G,R,B,G,R...の順で格納されます。
        /// </summary>
        /// <param name="filename">画像のファイル名を指定します。</param>
        /// <param name="bmp">開いた画像のBitmapクラスオブジェクトが格納されます。</param>
        /// <returns>画像データが可能された行列</returns>
        public static Byte[,] Imread(string filename, out System.Drawing.Bitmap bmp)
        {
            if (System.IO.File.Exists(filename) == false) ThrowException("Imread", "File not exist({filename})");

            bmp = new System.Drawing.Bitmap(filename);
            var channel = System.Drawing.Bitmap.GetPixelFormatSize(bmp.PixelFormat) / 8;

            var width = bmp.Width;
            var height = bmp.Height;

            // Bitmapをロック
            var bmpData = bmp.LockBits(
                    new System.Drawing.Rectangle(0, 0, width, height),
                    System.Drawing.Imaging.ImageLockMode.ReadWrite,
                    bmp.PixelFormat
                );

            // メモリの幅のバイト数を取得
            var stride = Math.Abs(bmpData.Stride);

            // 画像データ格納用配列
            var data = new byte[stride * height];

            // Bitmapデータを配列へコピー
            System.Runtime.InteropServices.Marshal.Copy(
                bmpData.Scan0,
                data,
                0,
                stride * bmpData.Height
                );

            // アンロック
            bmp.UnlockBits(bmpData);

            var matRows = height;
            var matcolumns = width * channel;

            var ret = new Byte[matRows, matcolumns];

            // 画像データの右端の部分を無視して行ごとにコピーする
            for (int y = 0; y < height; y++)
            {
                Buffer.BlockCopy(data, y * stride, ret, y * matcolumns, matcolumns * sizeof(byte));
            }

            return ret;
        }

        /// <summary>
        /// 画像ファイル名を指定して画像データの行列（Byte型の二次元配列）を取得します。
        /// カラーの場合、B,G,R,B,G,R...の順で格納されます。
        /// </summary>
        /// <param name="filename">画像のファイル名を指定します。</param>
        /// <returns>画像データが可能された行列</returns>
        public static Byte[,] Imread(string filename)
        {
            System.Drawing.Bitmap bmp;
            var data = Imread(filename, out bmp);
            bmp.Dispose();

            return data;
        }

        /// <summary>
        /// 画像ファイル名を指定して画像データのプレーン分離された行列（Byte型の二次元配列の配列）を取得します。
        /// カラーの場合、[B][,], [G][,], [R][,]の順で格納されます。
        /// </summary>
        /// <param name="filename">画像のファイル名を指定します。</param>
        /// <param name="bmp">開いた画像のBitmapクラスオブジェクトが格納されます。</param>
        /// <returns>プレーン分離された画像データが可能された行列</returns>
        public static Byte[][,] ImreadPlane(string filename, out System.Drawing.Bitmap bmp)
        {
            var data = Imread(filename, out bmp);

            var width = bmp.Width;
            var height = bmp.Height;
            var channel = System.Drawing.Bitmap.GetPixelFormatSize(bmp.PixelFormat) / 8;

            var planeData = new Byte[channel][,];

            for (int c = 0; c < channel; c++)
            {
                planeData[c] = new Byte[height, width];
                for (int row = 0; row < height; row++)
                {
                    for (int col = 0; col < width; col++)
                    {
                        planeData[c][row, col] = data[row, c + col * channel];
                    }
                }
            }
            return planeData;
        }

        /// <summary>
        /// 画像ファイル名を指定して画像データのプレーン分離された行列（Byte型の二次元配列の配列）を取得します。
        /// カラーの場合、[B][,], [G][,], [R][,]の順で格納されます。
        /// </summary>
        /// <param name="filename">画像のファイル名を指定します。</param>
        /// <returns>プレーン分離された画像データが可能された行列</returns>
        public static Byte[][,] ImreadPlane(string filename)
        {
            System.Drawing.Bitmap bmp;
            var data = ImreadPlane(filename, out bmp);
            bmp.Dispose();

            return data;
        }

        /// <summary>
        /// 行列をCSVファイルに保存します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="filename">CSVファイル名（*.csv）を指定します。</param>
        public static void SaveCsv<T>(this T[,] mat, string filename) where T : struct
        {
            if (mat == null) ThrowException("SaveCsv", "mat != null");

            var rows = mat.GetLength(0);
            var columns = mat.GetLength(1);

            var encode = System.Text.Encoding.GetEncoding("SHIFT_JIS");

            using (var wt = new System.IO.StreamWriter(filename, false, encode))
            {
                for (int row = 0; row < rows; row++)
                {
                    for (int col = 0; col < columns -1; col++)
                    {
                        wt.Write("{mat[row, col]}, ");
                    }
                    wt.WriteLine("{mat[row, columns - 1]}");
                }
            }
        }

        /// <summary>
        /// 行列の内容をコンソールへ表示
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="title">行列表示の先頭行に表示する文字列を指定します。</param>
        /// <param name="omission">10行より大きい行列のとき、中略表示する場合はtrue</param>
        public static void Print<T>(this T[,] mat, string title = "", bool omission = true)
        {
            if (title.Length > 0)
            {
                Console.WriteLine(title);
            }

            if (mat == null)
            {
                Console.WriteLine("mat == null");
                return;
            }

            var matRows = mat.GetLength(0);
            var matcolumns = mat.GetLength(1);

            int maxLength = 0;
            string text;

            // 数値文字の最大の長さを取得
            for (int row = 0; row < matRows; row++)
            {
                for (int col = 0; col < matcolumns - 1; col++)
                {
                    text = mat[row, col].ToString();
                    if (maxLength < text.Length) maxLength = text.Length;
                }
            }

            text = mat.ToString();
            Console.WriteLine("{text.Substring(0, text.Length - 3)}[{matRows},{matcolumns}]");

            if ((matRows <= 10) || (omission == false))
            {
                for (int row = 0; row < matRows; row++)
                {
                    for (int col = 0; col < matcolumns - 1; col++)
                    {
                        Console.Write(mat[row, col].ToString().PadLeft(maxLength) + ",");

                    }
                    Console.WriteLine(mat[row, matcolumns - 1].ToString().PadLeft(maxLength));
                }
                Console.WriteLine("");
            }
            else
            {
                // 前半の5行分の表示

                for (int row = 0; row < 5; row++)
                {
                    for (int col = 0; col < matcolumns - 1; col++)
                    {
                        Console.Write(mat[row, col].ToString().PadLeft(maxLength) + ", ");

                    }
                    Console.WriteLine(mat[row, matcolumns - 1].ToString().PadLeft(maxLength));
                }
                Console.WriteLine("...........");

                // 後半の５行分
                for (int row = matRows - 6; row < matRows; row++)
                {
                    for (int col = 0; col < matcolumns - 1; col++)
                    {
                        Console.Write(mat[row, col].ToString().PadLeft(maxLength) + ", ");

                    }
                    Console.WriteLine(mat[row, matcolumns - 1].ToString().PadLeft(maxLength));
                }
                Console.WriteLine("");
            }
        }

        /// <summary>
        /// 行列の内容をコンソールへ表示
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="mat">行列（二次元配列）を指定します。</param>
        /// <param name="omission">大きい行列のとき、中略表示する場合はtrue</param>
        public static void Print<T>(this T[,] mat, bool omission)
        {
            mat.Print(omission);
        }


        /// <summary>
        /// 画像表示ウィンドウクラス
        /// </summary>
        public class NamedWindow
        {
            System.Windows.Forms.PictureBox _pictureBox;
            System.Windows.Forms.Form _form;

            /// <summary>
            /// 画像表示ウィンドウクラスのコンストラクタ
            /// </summary>
            /// <param name="winname"></param>
            public NamedWindow(string winname = "")
            {
                _form = new System.Windows.Forms.Form();

                _pictureBox = new System.Windows.Forms.PictureBox();
                _pictureBox.Dock = System.Windows.Forms.DockStyle.Fill;
                // 
                // Form
                // 
                _form.AutoSize = true;
                //_form.ClientSize = new System.Drawing.Size(100, 100);
                _form.Controls.Add(_pictureBox);
                _form.Text = winname;
                _form.MinimizeBox = false;
                _form.MaximizeBox = false;
            }

            /// <summary>
            /// 画像を表示します。
            /// </summary>
            /// <param name="bmp">表示するBitmapクラスオブジェクト</param>
            public void Imshow(System.Drawing.Bitmap bmp)
            {
                _pictureBox.Image = bmp;
                _pictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;

                _form.Show();
                System.Windows.Forms.Application.DoEvents();    // コンソールアプリから呼ぶ場合用
            }
        }

        /// <summary>
        /// 画像をウィンドウに表示します。
        /// </summary>
        /// <param name="bmp">表示するBitmapクラスオブジェクトを指定します。</param>
        /// <param name="winname">ウィンドウタイトルを指定します。</param>
        /// <returns>表示されたウィンドウオブジェクト</returns>
        public static NamedWindow Imshow(this System.Drawing.Bitmap bmp, string winname)
        {
            var window = new NamedWindow(winname);
            window.Imshow(bmp);

            return window;
        }

        /// <summary>
        /// 画像をウィンドウに表示します。
        /// </summary>
        /// <param name="bmp">表示するBitmapクラスオブジェクトを指定します。</param>
        /// <param name="window">表示先のウィンドウオブジェクトを指定します。</param>
        /// <returns>表示したウィンドウオブジェクト</returns>
        public static NamedWindow Imshow(this System.Drawing.Bitmap bmp, NamedWindow window = null)
        {
            if (window == null)
            {
                window = new NamedWindow();
            }
            window.Imshow(bmp);

            return window;
        }

        ////////////////////////////////////////////////////////////////
        // アフィン変換用(float, doubleのみ対応)
        ////////////////////////////////////////////////////////////////

        /// <summary>
        /// 回転行列（同次座標系）を取得します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>回転行列（同次座標系）</returns>
        private static T[,] RotateMat<T>(T deg) where T : struct
        {
            // 3x3の単位行列
            var ret = Identity<T>(3);

            var rad = deg.Radians();

            var sin = (T)Math.Sin(rad);
            var msin = (T)Math.Sin(-rad);
            var cos = (T)Math.Cos(rad);

            ret[0, 0] = cos; ret[0, 1] = msin;
            ret[1, 0] = sin; ret[1, 1] = cos;

            return ret;
        }

        /// <summary>
        /// 回転行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>回転行列（同次座標系）</returns>
        public static float[,] RotateMat(float deg)
        {
            return RotateMat<float>(deg);
        }

        /// <summary>
        /// 回転行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>回転行列（同次座標系）</returns>
        public static double[,] RotateMat(double deg)
        {
            return RotateMat<double>(deg);
        }

        /// <summary>
        /// 指定座標（cX, cY）周りの回転行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <param name="cX">回転中心のX座標を指定します。</param>
        /// <param name="cY">回転中心のY座標を指定します。</param>
        /// <returns>回転行列（同次座標系）</returns>
        public static float[,] RotateAtMat(float deg, float cX, float cY)
        {
            var ret = TranslateMat(-cX, -cY);       // 原点へ移動
            ret = Mult(RotateMat(deg), ret);        // 原点まわりに回転
            ret = Mult(TranslateMat(cX, cY), ret);  // 元の位置へ戻す

            return ret;
        }

        /// <summary>
        /// 指定座標（cX, cY）周りの回転行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <param name="cX">回転中心のX座標を指定します。</param>
        /// <param name="cY">回転中心のY座標を指定します。</param>
        /// <returns>回転行列（同次座標系）</returns>
        public static double[,] RotateAtMat(double deg, double cX, double cY)
        {
            var ret = TranslateMat(-cX, -cY);       // 原点へ移動
            ret = Mult(RotateMat(deg), ret);        // 原点まわりに回転
            ret = Mult(TranslateMat(cX, cY), ret);  // 元の位置へ戻す

            return ret;
        }

        /// <summary>
        /// 拡大行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <returns>拡大行列（同次座標系）</returns>
        public static float[,] ScaleMat(float sX, float sY)
        {
            var ret = Identity<float>(3);

            ret[0, 0] = sX;
            ret[1, 1] = sY;

            return ret;
        }

        /// <summary>
        /// 拡大行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <returns>拡大行列（同次座標系）</returns>
        public static double[,] ScaleMat(double sX, double sY)
        {
            var ret = Identity<double>(3);

            ret[0, 0] = sX;
            ret[1, 1] = sY;

            return ret;
        }

        /// <summary>
        /// 指定座標（cX, cY）を基点とした拡大行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <param name="cX">拡大の基点となるX座標を指定します。</param>
        /// <param name="cY">拡大の基点となるY座標を指定します。</param>
        /// <returns>拡大行列（同次座標系）</returns>
        public static float[,] ScaleAtMat(float sX, float sY, float cX, float cY)
        {
            var ret = TranslateMat(-cX, -cY);       // 原点へ移動
            ret = Mult(ScaleMat(sX, sY), ret);      // 原点まわりに拡大縮小
            ret = Mult(TranslateMat(cX, cY), ret);  // 元の位置へ戻す

            return ret;
        }

        /// <summary>
        /// 指定座標（cX, cY）を基点とした拡大行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <param name="cX">拡大の基点となるX座標を指定します。</param>
        /// <param name="cY">拡大の基点となるY座標を指定します。</param>
        /// <returns>拡大行列（同次座標系）</returns>
        public static double[,] ScaleAtMat(double sX, double sY, double cX, double cY)
        {
            var ret = TranslateMat(-cX, -cY);       // 原点へ移動
            ret = Mult(ScaleMat(sX, sY), ret);      // 原点まわりに拡大縮小
            ret = Mult(TranslateMat(cX, cY), ret);  // 元の位置へ戻す

            return ret;
        }

        /// <summary>
        /// 平行移動行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="tX">X軸方向の移動量を指定します。</param>
        /// <param name="tY">Y軸方向の移動量を指定します。</param>
        /// <returns>平行移動行列（同次座標系）</returns>
        public static float[,] TranslateMat(float tX, float tY)
        {
            var ret = Identity<float>(3);

            ret[0, 2] = tX;
            ret[1, 2] = tY;

            return ret;
        }

        /// <summary>
        /// 平行移動行列（同次座標系）を取得します。
        /// </summary>
        /// <param name="tX">X軸方向の移動量を指定します。</param>
        /// <param name="tY">Y軸方向の移動量を指定します。</param>
        /// <returns>平行移動行列（同次座標系）</returns>
        public static double[,] TranslateMat(double tX, double tY)
        {
            var ret = Identity<double>(3);

            ret[0, 2] = tX;
            ret[1, 2] = tY;

            return ret;
        }

        // 三次元座標

        private static T[,] RotateXMat<T>(T deg) where T : struct
        {
            // 4x4の単位行列
            var ret = Identity<T>(4);

            var rad = deg.Radians();

            var sin = (T)Math.Sin(rad);
            var msin = (T)Math.Sin(-rad);
            var cos = (T)Math.Cos(rad);

            ret[1, 1] = cos; ret[1, 2] = msin;
            ret[2, 1] = sin; ret[2, 2] = cos;

            return ret;
        }

        /// <summary>
        /// X軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>X軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static float[,] RotateXMat(float deg)
        {
            return RotateXMat(deg);
        }

        /// <summary>
        /// X軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>X軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static double[,] RotateXMat(double deg)
        {
            return RotateXMat(deg);
        }

        private static T[,] RotateYMat<T>(T deg) where T : struct
        {
            // 4x4の単位行列
            var ret = Identity<T>(4);

            var rad = deg.Radians();

            var sin = (T)Math.Sin(rad);
            var msin = (T)Math.Sin(-rad);
            var cos = (T)Math.Cos(rad);

            ret[0, 0] = cos; ret[0, 2] = sin;
            ret[2, 0] = msin; ret[2, 2] = cos;

            return ret;
        }

        /// <summary>
        /// Y軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>Y軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static float[,] RotateYMat(float deg)
        {
            return RotateYMat(deg);
        }

        /// <summary>
        /// Y軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>Y軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static double[,] RotateYMat(double deg)
        {
            return RotateYMat(deg);
        }

        private static T[,] RotateZMat<T>(T deg) where T : struct
        {
            // 4x4の単位行列
            var ret = Identity<T>(4);

            var rad = deg.Radians();

            var sin = (T)Math.Sin(rad);
            var msin = (T)Math.Sin(-rad);
            var cos = (T)Math.Cos(rad);

            ret[0, 0] = cos; ret[0, 1] = msin;
            ret[1, 0] = sin; ret[1, 1] = cos;

            return ret;
        }

        /// <summary>
        /// Z軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>Z軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static float[,] RotateZMat(float deg)
        {
            return RotateZMat(deg);
        }

        /// <summary>
        /// Z軸周りの回転行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="deg">回転角度を度数単位（°）で指定します。</param>
        /// <returns>Z軸周りの回転行列（同次座標系、三次元座標）</returns>
        public static double[,] RotateZMat(double deg)
        {
            return RotateZMat(deg);
        }

        /// <summary>
        /// 拡大行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <param name="sZ">Z軸方向の倍率を指定します。</param>
        /// <returns>拡大行列（同次座標系、三次元座標）</returns>
        public static float[,] ScaleMat(float sX, float sY, float sZ)
        {
            var ret = Identity<float>(4);

            ret[0, 0] = sX;
            ret[1, 1] = sY;
            ret[2, 2] = sZ;

            return ret;
        }

        /// <summary>
        /// 拡大行列（三次元座標）を取得します。
        /// </summary>
        /// <param name="sX">X軸方向の倍率を指定します。</param>
        /// <param name="sY">Y軸方向の倍率を指定します。</param>
        /// <param name="sZ">Z軸方向の倍率を指定します。</param>
        /// <returns>拡大行列（同次座標系、三次元座標）</returns>
        public static double[,] ScaleMat(double sX, double sY, double sZ)
        {
            var ret = Identity<double>(4);

            ret[0, 0] = sX;
            ret[1, 1] = sY;
            ret[2, 2] = sZ;

            return ret;
        }

        /// <summary>
        /// 平行移動行列（同次座標系、三次元座標）を取得します。
        /// </summary>
        /// <param name="tX">X軸方向の移動量を指定します。</param>
        /// <param name="tY">Y軸方向の移動量を指定します。</param>
        /// <param name="tZ">Z軸方向の移動量を指定します。</param>
        /// <returns>平行移動行列（同次座標系、三次元座標）</returns>
        public static float[,] TranslateMat(float tX, float tY, float tZ)
        {
            var ret = Identity<float>(4);

            ret[0, 3] = tX;
            ret[1, 3] = tY;
            ret[2, 3] = tZ;

            return ret;
        }

        /// <summary>
        /// 平行移動行列（同次座標系、三次元座標）を取得します。
        /// </summary>
        /// <param name="tX">X軸方向の移動量を指定します。</param>
        /// <param name="tY">Y軸方向の移動量を指定します。</param>
        /// <param name="tZ">Z軸方向の移動量を指定します。</param>
        /// <returns>平行移動行列（同次座標系、三次元座標）</returns>
        public static double[,] TranslateMat(double tX, double tY, double tZ)
        {
            var ret = Identity<double>(4);

            ret[0, 3] = tX;
            ret[1, 3] = tY;
            ret[2, 3] = tZ;

            return ret;
        }

        /// <summary>
        /// System.Drawing.Pointから同次座標系の行列（3行1列）へ変換します。
        /// </summary>
        /// <param name="p">System.Drawing.Pointの座標</param>
        /// <returns>同次座標系の行列（3行1列）</returns>
        public static int[,] PointToMat(this System.Drawing.Point p)
        {
            if (p == null) ThrowException("PointToMat", "p != null");

            var mat = new int[3, 1];
            mat[0, 0] = p.X;
            mat[1, 0] = p.Y;
            mat[2, 0] = 1;

            return mat;
        }

        /// <summary>
        /// System.Drawing.PointFから同次座標系の行列（3行1列）へ変換します。
        /// </summary>
        /// <param name="p">System.Drawing.PointFの座標</param>
        /// <returns>同次座標系の行列（3行1列）</returns>
        public static float[,] PointToMat(this System.Drawing.PointF p)
        {
            if (p == null) ThrowException("PointToMat", "p != null");

            var mat = new float[3, 1];
            mat[0, 0] = p.X;
            mat[1, 0] = p.Y;
            mat[2, 0] = 1;

            return mat;
        }

        /// <summary>
        /// System.Drawing.Pointの配列から同次座標系の行列（3行N列）へ変換します。
        /// </summary>
        /// <param name="p">System.Drawing.Point[]の座標配列</param>
        /// <returns>同次座標系の行列（3行N列）</returns>
        public static int[,] PointToMat(this System.Drawing.Point[] p)
        {
            if (p == null) ThrowException("PointToMat", "p != null");

            int count = p.Length;

            var mat = new int[3, count];
            for (int i = 0; i < count; i++) {
                mat[0, 0] = p[i].X;
                mat[1, 0] = p[i].Y;
                mat[2, 0] = 1;
            }

            return mat;
        }

        /// <summary>
        /// System.Drawing.PointFの配列から同次座標系の行列（3行N列）へ変換します。
        /// </summary>
        /// <param name="p">System.Drawing.PointF[]の座標配列</param>
        /// <returns>同次座標系の行列（3行N列）</returns>
        public static float[,] PointToMat(this System.Drawing.PointF[] p)
        {
            if (p == null) ThrowException("PointToMat", "p != null");

            int count = p.Length;

            var mat = new float[3, count];
            for (int i = 0; i < count; i++)
            {
                mat[0, 0] = p[i].X;
                mat[1, 0] = p[i].Y;
                mat[2, 0] = 1;
            }
            return mat;
        }

        /// <summary>
        /// 一次元配列から行列（N行1列の二次元配列）へ変換します。
        /// </summary>
        /// <typeparam name="T">数値型を指定します。</typeparam>
        /// <param name="array">一次元配列</param>
        /// <returns>行列（N行1列の二次元配列）</returns>
        public static T[,] ArrayToMat<T>(this T[] array) where T : struct
        {
            if (array == null) ThrowException("ArrayToMat", "array != null");

            int count = array.Length;

            var mat = new T[count, 1];

            Parallel.For(0, count, i =>
            {
                mat[i, 0] = array[i];
            });
            return mat;
        }

        /// <summary>
        /// エラーの例外を投げます。
        /// </summary>
        /// <param name="functionName"></param>
        /// <param name="message"></param>
        private static void ThrowException(string functionName, string message)
        {
            var errorMessage = "error: " + message + " in function '{functionName}'";

            Console.WriteLine(errorMessage);
            throw new Exception(message + " in function '{functionName}'");
        }



    }
}
