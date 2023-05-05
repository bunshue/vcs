using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Drawing;   // 追加：「参照」でSystem.Drawingを追加すること
using ImagingSolution;  // ImagingSolution.Matクラス用

namespace ConsoleSample
{
    class Program
    {
        static void Main(string[] args)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_bmp\0.bmp";

            // 行列(matA)の設定例（二次元配列で行列を設定）
            var matA = new double[3, 3];
            matA[0, 0] = 1; matA[0, 1] = 2; matA[0, 2] = 3;
            matA[1, 0] = 4; matA[1, 1] = 5; matA[1, 2] = 6;
            matA[2, 0] = 7; matA[2, 1] = 8; matA[2, 2] = 9;

            matA.Print("matA =");　// コンソールへ行列の表示

            // 行列(matB)の設定例
            var matB = new double[,] {
                { 1, 4, 8 },
                { 6, 2, 5 },
                { 9, 7, 3 }
            };
            matB.Print("matB =");

            // 行列(matA)と行列(matA)の積
            var matMult = matA.Mult(matB);
            matMult.Print("matA matB =");

            // 行列(matA)と行列(matA)の加算
            var matAdd = matA.Add(matB);
            matAdd.Print("matA + matB =");

            // 行列(matA)と行列(matA)の減算
            var matSub = matA.Sub(matB);
            matSub.Print("matA - matB =");

            // 行列(matB)の逆行列
            var matInverse = matB.Inverse();
            matInverse.Print("(matB)-1 =");

            // 行列(matA)の転置
            var matTranspose = matA.Transpose();
            matTranspose.Print("(matA)T =");

            // 回転行列の取得
            var matRotate = Mat.RotateMat(10.0);
            matRotate.Print("RotateMat =");

            // 拡大行列の取得
            var matScale = Mat.ScaleMat(2.0, 5.0);
            matScale.Print("ScaleMat =");

            // 平行移動行列の取得
            var matTranslate = Mat.TranslateMat(-5.0, 12.0);
            matTranslate.Print("TranslateMat =");

            Bitmap bmp;
            // 画像ファイルを開く
            var imgMat = Mat.Imread(filename, out bmp);
            imgMat.Print("Image data =");

            // 画像の表示
            var window = bmp.Imshow("Image");

            // 配列(画像データ)をcsvファイルに保存
            string filename_csv = "data_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".csv";

            imgMat.SaveCsv(filename_csv);

            // キー入力待ち
            //Console.WriteLine("続行するには何かキーを押してください . . .");
            Console.WriteLine("Press any key to continue....");
            Console.ReadKey();
        }
    }
}

