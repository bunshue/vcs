using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;  // for PixelFormat

using AForge;
using AForge.Math;
using AForge.Math.Geometry;
using AForge.Math.Metrics;
using AForge.Imaging;

namespace vcs_AForgeMathTest
{
    public partial class Form1 : Form
    {
        private const float Epsilon = 0.000001f;
        private Matrix3x3 a1 = new Matrix3x3();
        private Matrix3x3 a2 = new Matrix3x3();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            button0.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new System.Drawing.Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new System.Drawing.Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox1.Size = new Size(500, 300);
            pictureBox1.Location = new System.Drawing.Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Size = new Size(500, 690 - 310);
            richTextBox1.Location = new System.Drawing.Point(x_st + dx * 3, y_st + dy * 0 + 310);
            bt_clear.Location = new System.Drawing.Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1170, 750);
            this.Text = "vcs_AForgeMathTest";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public void print_matrix3(Matrix3x3 matrix)
        {
            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
                richTextBox1.Text += array[i];
                if ((i % 3) == 2)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += "\t";
            }
        }

        public void Matrix3x3Test()
        {
            // prepare 1st argument
            a1.V00 = 1;
            a1.V01 = 2;
            a1.V02 = 3;

            a1.V10 = 3;
            a1.V11 = 2;
            a1.V12 = 1;

            a1.V20 = 1;
            a1.V21 = 3;
            a1.V22 = 2;

            // prepare 2nd argument
            a2.V00 = 2;
            a2.V01 = 1;
            a2.V02 = 3;

            a2.V10 = 1;
            a2.V11 = 3;
            a2.V12 = 2;

            a2.V20 = 3;
            a2.V21 = 2;
            a2.V22 = 1;
        }

        public void ToArrayTest()
        {
            Matrix3x3 matrix = new Matrix3x3();

            matrix.V00 = 1;
            matrix.V01 = 2;
            matrix.V02 = 3;

            matrix.V10 = 4;
            matrix.V11 = 5;
            matrix.V12 = 6;

            matrix.V20 = 7;
            matrix.V21 = 8;
            matrix.V22 = 9;

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }
        }

        public void CreateFromRowsTest()
        {
            Vector3 row0 = new Vector3(1, 2, 3);
            Vector3 row1 = new Vector3(4, 5, 6);
            Vector3 row2 = new Vector3(7, 8, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromRows(row0, row1, row2);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }

            //Assert.AreEqual<Vector3>( row0, matrix.GetRow( 0 ) );
            //Assert.AreEqual<Vector3>( row1, matrix.GetRow( 1 ) );
            //Assert.AreEqual<Vector3>( row2, matrix.GetRow( 2 ) );

            //matrix.GetRow(-1);

            //matrix.GetRow(3);
        }

        public void CreateFromColumnsTest()
        {
            Vector3 column0 = new Vector3(1, 4, 7);
            Vector3 column1 = new Vector3(2, 5, 8);
            Vector3 column2 = new Vector3(3, 6, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromColumns(column0, column1, column2);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }

            //Assert.AreEqual<Vector3>( column0, matrix.GetColumn( 0 ) );
            //Assert.AreEqual<Vector3>( column1, matrix.GetColumn( 1 ) );
            //Assert.AreEqual<Vector3>( column2, matrix.GetColumn( 2 ) );

            //matrix.GetColumn( -1 );
            //matrix.GetColumn( 3 );
        }

        public void CreateRotationYTest(float angle)
        {
            richTextBox1.Text = "CreateRotationYTest, angle = " + angle + "\n";

            float radians = (float)(angle * System.Math.PI / 180);

            Matrix3x3 matrix = new Matrix3x3();
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            matrix = Matrix3x3.CreateRotationY(radians);
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[9]
            {
                cos, 0, sin, 0, 1, 0, -sin, 0, cos
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateRotationXTest(float angle)
        {
            richTextBox1.Text = "CreateRotationXTest, angle = " + angle + "\n";

            float radians = (float)(angle * System.Math.PI / 180);

            Matrix3x3 matrix = new Matrix3x3();
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            matrix = Matrix3x3.CreateRotationX(radians);
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[9]
            {
                1, 0, 0, 0, cos, -sin, 0, sin, cos
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateRotationZTest(float angle)
        {
            richTextBox1.Text = "CreateRotationZTest, angle = " + angle + "\n";

            float radians = (float)(angle * System.Math.PI / 180);

            Matrix3x3 matrix = new Matrix3x3();
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            matrix = Matrix3x3.CreateRotationZ(radians);
            richTextBox1.Text += "matrix :\n";
            print_matrix3(matrix);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[9]
            {
                cos, -sin, 0, sin, cos, 0, 0, 0, 1
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateFromYawPitchRollTest(float yaw, float pitch, float roll)
        {
            float radiansYaw = (float)(yaw * System.Math.PI / 180);
            float radiansPitch = (float)(pitch * System.Math.PI / 180);
            float radiansRoll = (float)(roll * System.Math.PI / 180);

            Matrix3x3 matrix = Matrix3x3.CreateFromYawPitchRoll(radiansYaw, radiansPitch, radiansRoll);

            Matrix3x3 xMatrix = Matrix3x3.CreateRotationX(radiansPitch);
            Matrix3x3 yMatrix = Matrix3x3.CreateRotationY(radiansYaw);
            Matrix3x3 zMatrix = Matrix3x3.CreateRotationZ(radiansRoll);

            Matrix3x3 rotationMatrix = (yMatrix * xMatrix) * zMatrix;

            CompareMatrixWithArray(matrix, rotationMatrix.ToArray());
        }

        public void ExtractYawPitchRollTest(float yaw, float pitch, float roll)
        {
            float radiansYaw = (float)(yaw * System.Math.PI / 180);
            float radiansPitch = (float)(pitch * System.Math.PI / 180);
            float radiansRoll = (float)(roll * System.Math.PI / 180);

            Matrix3x3 matrix = Matrix3x3.CreateFromYawPitchRoll(radiansYaw, radiansPitch, radiansRoll);

            float extractedYaw;
            float extractedPitch;
            float extractedRoll;

            matrix.ExtractYawPitchRoll(out extractedYaw, out extractedPitch, out extractedRoll);

            //Assert.AreApproximatelyEqual<float, float>( radiansYaw,   extractedYaw,   Epsilon );
            //Assert.AreApproximatelyEqual<float, float>( radiansPitch, extractedPitch, Epsilon );
            //Assert.AreApproximatelyEqual<float, float>( radiansRoll,  extractedRoll,  Epsilon );
        }

        public void CreateDiagonalTest(float v00, float v11, float v22)
        {
            Vector3 diagonal = new Vector3(v00, v11, v22);
            Matrix3x3 matrix = Matrix3x3.CreateDiagonal(diagonal);

            float[] expectedArray = new float[9] { v00, 0, 0, 0, v11, 0, 0, 0, v22 };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void DeterminantTest(float expectedDeterminant,
            float v00, float v01, float v02,
            float v10, float v11, float v12,
            float v20, float v21, float v22)
        {
            Matrix3x3 matrix = new Matrix3x3();

            matrix.V00 = v00;
            matrix.V01 = v01;
            matrix.V02 = v02;

            matrix.V10 = v10;
            matrix.V11 = v11;
            matrix.V12 = v12;

            matrix.V20 = v20;
            matrix.V21 = v21;
            matrix.V22 = v22;

            //Assert.AreEqual<float>( expectedDeterminant, matrix.Determinant );
        }

        public void InverseTest(float v00, float v01, float v02, float v10, float v11, float v12, float v20, float v21, float v22)
        {
            Matrix3x3 matrix = new Matrix3x3();

            matrix.V00 = v00;
            matrix.V01 = v01;
            matrix.V02 = v02;

            matrix.V10 = v10;
            matrix.V11 = v11;
            matrix.V12 = v12;

            matrix.V20 = v20;
            matrix.V21 = v21;
            matrix.V22 = v22;

            Matrix3x3 inverse = matrix.Inverse();  // 反矩陣
            Matrix3x3 identity = matrix * inverse;  // 矩陣 * 反矩陣

            //Matrix3x3.Identity  // 單一矩陣

            //Assert.AreEqual<bool>( true, ApproximateEquals( identity, Matrix3x3.Identity ) );
        }

        private void CompareMatrixWithArray(Matrix3x3 matrix, float[] array)
        {
            float[] matrixArray = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
                //Assert.AreEqual<float>( matrixArray[i], array[i] );
            }
        }

        private bool ApproximateEquals(Matrix3x3 matrix1, Matrix3x3 matrix2)
        {
            //兩個矩陣的每個元素是否都很接近

            return (
                (System.Math.Abs(matrix1.V00 - matrix2.V00) <= Epsilon) &&
                (System.Math.Abs(matrix1.V01 - matrix2.V01) <= Epsilon) &&
                (System.Math.Abs(matrix1.V02 - matrix2.V02) <= Epsilon) &&
                (System.Math.Abs(matrix1.V10 - matrix2.V10) <= Epsilon) &&
                (System.Math.Abs(matrix1.V11 - matrix2.V11) <= Epsilon) &&
                (System.Math.Abs(matrix1.V12 - matrix2.V12) <= Epsilon) &&
                (System.Math.Abs(matrix1.V20 - matrix2.V20) <= Epsilon) &&
                (System.Math.Abs(matrix1.V21 - matrix2.V21) <= Epsilon) &&
                (System.Math.Abs(matrix1.V22 - matrix2.V22) <= Epsilon)
            );
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Matrix3x3Test();
            ToArrayTest();

            CreateFromRowsTest();
            CreateFromColumnsTest();

            float angle = 45f;

            CreateRotationXTest(angle);

            CreateRotationYTest(angle);
            
            CreateRotationZTest(angle);

            //第一张是绕x轴旋转pitch， 上下點頭
            //第二张绕y轴旋转yaw，左右搖頭
            //第三张是绕z轴旋转roll。
            //绕三个轴的旋转值pitch，yaw，roll来自航空界的叫法，翻译为俯仰角，偏航角，翻滚角，非常形象
            //roll:是卷；滚动，转动；辗的意思；
            //yaw是（火箭、飞机、宇宙飞船等）偏航的意思；
            //pitch是倾斜；投掷；搭帐篷；坠落的意思；

            float yaw = -30;
            float pitch = -60;
            float roll = -90;
            CreateFromYawPitchRollTest(yaw, pitch, roll);
            ExtractYawPitchRollTest(yaw, pitch, roll);

            float v00 = -1;
            float v11 = -2;
            float v22 = -3;
            CreateDiagonalTest(v00, v11, v22);

            //matrix.Determinant 3X3矩陣的determinant

            //反矩陣 matrix.Inverse()
            //Matrix3x3 inverse = matrix.Inverse();

            //單一矩陣
            //Matrix3x3 identity = matrix * inverse;
            //Matrix3x3.Identity

            //矩陣相加/減/乘

            //矩陣+矩陣
            Matrix3x3 result1 = a1 + a2;

            //矩陣-矩陣
            Matrix3x3 result2 = a1 - a2;

            //矩陣X矩陣
            Matrix3x3 result3 = a1 * a2;

            //矩陣與陣列比較
            //CompareMatrixWithArray( Matrix3x3 matrix, float[] array )

            //矩陣之大約相等
            //ApproximateEquals( Matrix3x3 matrix1, Matrix3x3 matrix2 )
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //不知道 mode是什麼意思, 也不是眾數

            int[] values = new int[] { 1, 2, 2, 3, 3, 3 };
            int mode = Statistics.Mode(values);
            //Assert.AreEqual(3, mode);
            richTextBox1.Text += "mode = " + mode.ToString() + "\n";

            values = new int[] { 1, 1, 1, 2, 2, 2 };
            mode = Statistics.Mode(values);
            //Assert.AreEqual(3, mode);
            richTextBox1.Text += "mode = " + mode.ToString() + "\n";

            values = new int[] { 2, 2, 2, 1, 1, 1 };
            mode = Statistics.Mode(values);
            //Assert.AreEqual(0, mode);
            richTextBox1.Text += "mode = " + mode.ToString() + "\n";

            values = new int[] { 0, 0, 0, 0, 0, 0 };
            mode = Statistics.Mode(values);
            //Assert.AreEqual(0, mode);
            richTextBox1.Text += "mode = " + mode.ToString() + "\n";

            values = new int[] { 1, 1, 2, 3, 6, 8, 11, 12, 7, 3 };
            mode = Statistics.Mode(values);
            //Assert.AreEqual(7, mode);
            richTextBox1.Text += "mode = " + mode.ToString() + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //歐基里德距離 就是 sqrt(x^2+y^2)
            IntPoint point = new IntPoint(3, 4);
            float cc = point.EuclideanNorm();
            richTextBox1.Text += cc.ToString() + "\n";
        }

        private IntegralImage integralImage = null;
        private void button12_Click(object sender, EventArgs e)
        {
            UnmanagedImage uImage = UnmanagedImage.Create(100, 100, PixelFormat.Format8bppIndexed);

            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    uImage.SetPixel(x, y, ((x + y) % 2 == 0) ? Color.FromArgb(0, 0, 0) : Color.FromArgb(1, 1, 1));
                }
            }

            integralImage = IntegralImage.FromBitmap(uImage);

            Bitmap bmp = uImage.ToManagedImage();

            pictureBox1.Image = bmp;

            int x1 = 0;
            int y1 = 0;
            int x2 = 5;
            int y2 = 5;

            uint sum = integralImage.GetRectangleSum(x1, y1, x2, y2);
            richTextBox1.Text += "sum = " + sum.ToString() + "\n";

            int xx = 3;
            int yy = 3;
            int radius = 2;
            sum = integralImage.GetRectangleSum(xx, yy, radius);

            richTextBox1.Text += "sum = " + sum.ToString() + "\n";

            float mean = integralImage.GetRectangleMean(x1, y1, x2, y2);
            richTextBox1.Text += "mean = " + mean.ToString() + "\n";

            int valueX = integralImage.GetHaarXWavelet(xx, yy, radius);
            richTextBox1.Text += "valueX = " + valueX.ToString() + "\n";

            int valueY = integralImage.GetHaarYWavelet(xx, yy, radius);
            richTextBox1.Text += "valueY = " + valueY.ToString() + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //LineTest

            float x;
            float y;
            float theta;
            x = 1;
            y = 1;
            theta = 45f;
            /*
            [Row(  1,                  1,  45, 1.41421356f, -1, 2 )]
            [Row( -2,                  2, 135, 2 * 1.41421356f, 1, 4 )]
            [Row( -0.5, -1.73205081f / 2, 240, 1, -1 / 1.73205081f, -2 / 1.73205081f )]
            [Row(  1,                  0,   0, 1, float.NegativeInfinity, 1 )]
            [Row(  0,                 -1, 270, 1, 0, -1 )]
            */

            AForge.Point pt = new AForge.Point(x, y);

            // test Point-Theta factory
            Line line = Line.FromPointTheta(pt, theta);
            richTextBox1.Text += "Slope :\t" + line.Slope + "\n";
            richTextBox1.Text += "Intercept :\t" + line.Intercept + "\n";
            richTextBox1.Text += "IsHorizontal :\t" + line.IsHorizontal + "\n";
            richTextBox1.Text += "IsVertical :\t" + line.IsVertical + "\n";

            richTextBox1.Text += "---------------\n";  // 15個

            // calculate radius
            float radius = pt.EuclideanNorm();
            richTextBox1.Text += "radius " + radius + "\n";

            richTextBox1.Text += "---------------\n";  // 15個

            // test R-Theta factory
            line = Line.FromRTheta(radius, theta);
            richTextBox1.Text += "Slope :\t" + line.Slope + "\n";
            richTextBox1.Text += "Intercept :\t" + line.Intercept + "\n";
            richTextBox1.Text += "IsHorizontal :\t" + line.IsHorizontal + "\n";
            richTextBox1.Text += "IsVertical :\t" + line.IsVertical + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //檢查一直線是否垂直
            int sx = 0;
            int sy = 0;
            int ex = 100;
            int ey = 100;

            line = Line.FromPoints(new AForge.Point(sx, sy), new AForge.Point(ex, ey));
            richTextBox1.Text += "Slope :\t" + line.Slope + "\n";
            richTextBox1.Text += "Intercept :\t" + line.Intercept + "\n";
            richTextBox1.Text += "IsHorizontal :\t" + line.IsHorizontal + "\n";
            richTextBox1.Text += "IsVertical :\t" + line.IsVertical + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //兩直線的夾角
            int sx1 = 0;
            int sy1 = 0;
            int ex1 = 100;
            int ey1 = 0;
            int sx2 = 0;
            int sy2 = 0;
            int ex2 = 0;
            int ey2 = 100;

            Line line1 = Line.FromPoints(new AForge.Point(sx1, sy1), new AForge.Point(ex1, ey1));
            Line line2 = Line.FromPoints(new AForge.Point(sx2, sy2), new AForge.Point(ex2, ey2));

            float angle = line1.GetAngleBetweenLines(line2);
            richTextBox1.Text += "夾角 : " + angle + " 度\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //求兩直線的交叉點座標
            //GetIntersectionPointTest
            float sx1 = 0f;
            float sy1 = 0f;
            float ex1 = 100f;
            float ey1 = 100f;
            float sx2 = 100f;
            float sy2 = 0f;
            float ex2 = 0f;
            float ey2 = 100f;
            /*
            sx2 = 100f;
            sy2 = 0f;
            ex2 = 200f;
            ey2 = 100f;
            */
            Line line1 = Line.FromPoints(new AForge.Point(sx1, sy1), new AForge.Point(ex1, ey1));
            Line line2 = Line.FromPoints(new AForge.Point(sx2, sy2), new AForge.Point(ex2, ey2));

            AForge.Point? result = line1.GetIntersectionWith(line2);
            if (result == null)
            {
                richTextBox1.Text += "無交叉點\n";
            }
            else
            {
                richTextBox1.Text += "交叉點 : " + result.ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //點到線的距離
            int x = 0;
            int y = 0;
            int x1 = 100;
            int y1 = 0;
            int x2 = 0;
            int y2 = 100;
            AForge.Point pt = new AForge.Point(x, y);
            AForge.Point pt1 = new AForge.Point(x1, y1);
            AForge.Point pt2 = new AForge.Point(x2, y2);
            Line line = Line.FromPoints(pt1, pt2);
            float distance = line.DistanceToPoint(pt);
            richTextBox1.Text += "點到線的距離 : " + distance + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Vector3 v1 = new Vector3(1, 2, 3);
            Vector3 v2 = new Vector3(-1, -2, -3);
            Vector3 v3 = new Vector3(7);  // X Y Z 都設為7
            // v1.X  v1.Y  v1.Z
            // v2.X  v2.Y  v2.Z
            // v3.X  v3.Y  v3.Z

            float x = 7;
            float y = 2;
            float z = 8;
            Vector3 vector = new Vector3(x, y, z);

            richTextBox1.Text += "最大 :\t" + vector.Max + "\n";
            richTextBox1.Text += "最大位置 :\t" + vector.MaxIndex + "\n";
            richTextBox1.Text += "最小 :\t" + vector.Min + "\n";
            richTextBox1.Text += "最小位置 :\t" + vector.MinIndex + "\n";

            richTextBox1.Text += "Norm :\t" + vector.Norm + "\n";//float
            richTextBox1.Text += "Square :\t" + vector.Square + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //向量加法

            float x1 = 1;
            float y1 = 2;
            float z1 = 3;
            float x2 = 4;
            float y2 = 5;
            float z2 = 6;

            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);

            Vector3 result1 = vector1 + vector2;
            Vector3 result2 = Vector3.Add(vector1, vector2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //加上常數
            float value = 5;
            vector = new Vector3(x, y, z);

            result1 = vector + value;
            result2 = Vector3.Add(vector, value);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //向量減法
            vector1 = new Vector3(x1, y1, z1);
            vector2 = new Vector3(x2, y2, z2);

            result1 = vector1 - vector2;
            result2 = Vector3.Subtract(vector1, vector2);

            //減去常數
            vector = new Vector3(x, y, z);
            result1 = vector - value;
            result2 = Vector3.Subtract(vector, value);

            //向量相乘
            x1 = 1;
            y1 = 2;
            z1 = 3;
            x2 = -4;
            y2 = -5;
            z2 = -6;

            vector1 = new Vector3(x1, y1, z1);
            vector2 = new Vector3(x2, y2, z2);

            result1 = vector1 * vector2;
            result2 = Vector3.Multiply(vector1, vector2);

            richTextBox1.Text += "result1 :\t" + result1 + "\n";
            richTextBox1.Text += "result2 :\t" + result2 + "\n";

            //乘上常數
            x = 1;
            y = 2;
            z = 3;
            value = -4;

            vector = new Vector3(x, y, z);
            result1 = vector * value;
            result2 = Vector3.Multiply(vector, value);
            richTextBox1.Text += "result1 :\t" + result1 + "\n";
            richTextBox1.Text += "result2 :\t" + result2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //除法測試

            x1 = 1;
            y1 = 2;
            z1 = 3;
            x2 = -1;
            y2 = -4;
            z2 = -2;

            vector1 = new Vector3(x1, y1, z1);
            vector2 = new Vector3(x2, y2, z2);

            result1 = vector1 / vector2;
            result2 = Vector3.Divide(vector1, vector2);

            richTextBox1.Text += "result1 :\t" + result1 + "\n";
            richTextBox1.Text += "result2 :\t" + result2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //除以常數

            x = 1;
            y = 2;
            z = 3;
            value = -2;
            vector = new Vector3(x, y, z);
            result1 = vector / value;
            result2 = Vector3.Divide(vector, value);
            richTextBox1.Text += "result1 :\t" + result1 + "\n";
            richTextBox1.Text += "result2 :\t" + result2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //正規化 Normalize

            x = 3;
            y = 4;
            z = 0;

            vector = new Vector3(x, y, z);

            float norm1 = vector.Norm;
            float norm2 = vector.Normalize();
            richTextBox1.Text += "正規化 :\t" + norm1 + "\n";
            richTextBox1.Text += "正規化 :\t" + norm2 + "\n";

            //反向測試 Inverse

            x = 2;
            y = 4;
            z = 8;

            vector = new Vector3(x, y, z);
            Vector3 result = vector.Inverse();
            richTextBox1.Text += "倒數/反向測試 :\t" + result + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //內積測試

            x1 = 1;
            y1 = 2;
            z1 = 3;
            x2 = -3;
            y2 = -2;
            z2 = -1;

            vector1 = new Vector3(x1, y1, z1);
            vector2 = new Vector3(x2, y2, z2);

            float cc = Vector3.Dot(vector1, vector2);
            richTextBox1.Text += "內積測試 : " + cc + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //外積測試

            x1 = 1;
            y1 = 2;
            z1 = 3;
            x2 = 4;
            y2 = 5;
            z2 = 6;
            vector1 = new Vector3(x1, y1, z1);
            vector2 = new Vector3(x2, y2, z2);

            var ccc = Vector3.Cross(vector1, vector2);
            richTextBox1.Text += "外積測試 : " + ccc + "\n";

        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "CosineDistanceTest()\n";
            CosineDistanceTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "CosineSimilarityTest()\n";
            CosineSimilarityTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "EuclideanDistanceTest()\n";
            EuclideanDistanceTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "EuclideanSimilarityTest()\n";
            EuclideanSimilarityTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "HammingDistanceTest()\n";
            HammingDistanceTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "JaccardDistanceTest()\n";
            JaccardDistanceTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "ManhattanDistanceTest()\n";
            ManhattanDistanceTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "PearsonCorrelationTest()\n";
            PearsonCorrelationTest();
        }

        // test data
        private double[] p0 = new double[] { 1, 0.5 };
        private double[] q0 = new double[] { 0.5, 1 };

        private double[] p1 = new double[] { 4.5, 1 };
        private double[] q1 = new double[] { 4, 2 };

        private double[] p2 = new double[] { 0, 0, 0 };
        private double[] q2 = new double[] { 0, 0, 0 };

        private double[] p3 = new double[] { 1, 1, 1 };
        private double[] q3 = new double[] { 1, 1, 1 };

        private double[] p4 = new double[] { 2.5, 3.5, 3.0, 3.5, 2.5, 3.0 };
        private double[] q4 = new double[] { 3.0, 3.5, 1.5, 5.0, 3.5, 3.0 };

        private double[] p5 = new double[] { 1, 3, 5, 6, 8, 9, 6, 4, 3, 2 };
        private double[] q5 = new double[] { 2, 5, 6, 6, 7, 7, 5, 3, 1, 1 };


        public void CosineDistanceTest()
        {
            CosineDistance dist = new CosineDistance();

            double result = dist.GetDistance(p0, q0);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p1, q1);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p2, q2);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p3, q3);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p4, q4);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p5, q5);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";
        }

        public void CosineSimilarityTest()
        {
            CosineSimilarity sim = new CosineSimilarity();

            double result = sim.GetSimilarityScore(p0, q0);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p1, q1);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p2, q2);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p3, q3);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p4, q4);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p5, q5);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";
        }

        public void EuclideanDistanceTest()
        {
            EuclideanDistance dist = new EuclideanDistance();

            double result = dist.GetDistance(p0, q0);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p1, q1);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p2, q2);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p3, q3);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p4, q4);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p5, q5);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";
        }

        public void EuclideanSimilarityTest()
        {
            EuclideanSimilarity sim = new EuclideanSimilarity();

            double result = sim.GetSimilarityScore(p0, q0);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p1, q1);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p2, q2);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p3, q3);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p4, q4);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p5, q5);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";
        }

        public void HammingDistanceTest()
        {
            HammingDistance dist = new HammingDistance();

            double result = dist.GetDistance(p0, q0);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p1, q1);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p2, q2);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p3, q3);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p4, q4);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p5, q5);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";
        }

        public void JaccardDistanceTest()
        {
            JaccardDistance dist = new JaccardDistance();

            double result = dist.GetDistance(p0, q0);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p1, q1);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p2, q2);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p3, q3);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p4, q4);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p5, q5);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";
        }

        public void ManhattanDistanceTest()
        {
            ManhattanDistance dist = new ManhattanDistance();

            double result = dist.GetDistance(p0, q0);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p1, q1);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p2, q2);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p3, q3);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p4, q4);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";

            result = dist.GetDistance(p5, q5);
            richTextBox1.Text += "GetDistance :\t" + result + "\n";
        }

        public void PearsonCorrelationTest()
        {
            PearsonCorrelation sim = new PearsonCorrelation();

            double result = sim.GetSimilarityScore(p0, q0);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p1, q1);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p2, q2);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p3, q3);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p4, q4);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";

            result = sim.GetSimilarityScore(p5, q5);
            richTextBox1.Text += "GetSimilarityScore :\t" + result + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            int sx = 0;
            int sy = 0;
            int ex1 = 10;
            int ey1 = 0;
            int ex2 = -100;
            int ey2 = 100;

            IntPoint startPoint = new IntPoint(sx, sy);
            IntPoint vector1end = new IntPoint(ex1, ey1);
            IntPoint vector2end = new IntPoint(ex2, ey2);

            float angle = GeometryTools.GetAngleBetweenVectors(startPoint, vector1end, vector2end);

            richTextBox1.Text += "取得角度 : " + angle + " 度\n";

            //3030

            int sx1 = 0;
            int sy1 = 0;
            ex1 = 10;
            ey1 = 10;
            int sx2 = 0;
            int sy2 = 0;
            ex2 = -100;
            ey2 = 100;

            IntPoint line1start = new IntPoint(sx1, sy1);
            IntPoint line1end = new IntPoint(ex1, ey1);
            IntPoint line2start = new IntPoint(sx2, sy2);
            IntPoint line2end = new IntPoint(ex2, ey2);

            angle = GeometryTools.GetAngleBetweenLines(line1start, line1end, line2start, line2end);
            richTextBox1.Text += "取得角度 : " + angle + " 度\n";
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "GrahamConvexHullTest()\n";
            GrahamConvexHullTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "FindHullTest()\n";
            FindHullTest();
        }

        private List<IntPoint> pointsList0 = new List<IntPoint>();
        private List<IntPoint> pointsList1 = new List<IntPoint>();
        private List<IntPoint> pointsList2 = new List<IntPoint>();
        private List<IntPoint> pointsList3 = new List<IntPoint>();
        private List<IntPoint> pointsList4 = new List<IntPoint>();
        private List<IntPoint> pointsList5 = new List<IntPoint>();
        private List<IntPoint> pointsList6 = new List<IntPoint>();

        private List<IntPoint> pointsList7 = new List<IntPoint>();
        private List<IntPoint> pointsList8 = new List<IntPoint>();
        private List<IntPoint> pointsList9 = new List<IntPoint>();

        private List<IntPoint> expectedHull8 = new List<IntPoint>();

        private List<List<IntPoint>> pointsLists = new List<List<IntPoint>>();
        private List<List<IntPoint>> expectedHulls = new List<List<IntPoint>>();

        public void GrahamConvexHullTest()
        {
            // prepare 0st list
            pointsList0.Add(new IntPoint(0, 0));

            // prepare 1st list
            pointsList1.Add(new IntPoint(0, 0));
            pointsList1.Add(new IntPoint(100, 0));

            // prepare 2nd list
            pointsList2.AddRange(pointsList1);
            pointsList2.Add(new IntPoint(100, 100));

            // prepare 3rd list
            pointsList3.AddRange(pointsList2);
            pointsList3.Add(new IntPoint(0, 100));

            // prepare 4th list
            pointsList4.AddRange(pointsList2);
            pointsList4.Add(new IntPoint(60, 40));

            // prepare 5th list
            pointsList5.AddRange(pointsList3);
            pointsList5.Add(new IntPoint(50, 50));

            // prepare 6th list
            pointsList6.AddRange(pointsList3);
            pointsList6.Add(new IntPoint(0, 0));

            // prepare 7th list
            pointsList7.AddRange(pointsList3);
            pointsList7.AddRange(pointsList3);

            // prepare 8th list
            pointsList8.AddRange(pointsList3);
            pointsList8.Add(new IntPoint(50, -10));
            pointsList8.Add(new IntPoint(110, 50));
            pointsList8.Add(new IntPoint(50, 110));

            expectedHull8.AddRange(pointsList3);
            expectedHull8.Insert(1, new IntPoint(50, -10));
            expectedHull8.Insert(3, new IntPoint(110, 50));
            expectedHull8.Insert(5, new IntPoint(50, 110));

            // prepare 9th list
            pointsList9.AddRange(pointsList8);
            pointsList9.Add(new IntPoint(50, 10));
            pointsList9.Add(new IntPoint(90, 50));
            pointsList9.Add(new IntPoint(50, 90));
            pointsList9.Add(new IntPoint(10, 50));

            // now prepare list of tests
            pointsLists.Add(pointsList0);
            pointsLists.Add(pointsList1);
            pointsLists.Add(pointsList2);
            pointsLists.Add(pointsList3);

            expectedHulls.AddRange(pointsLists);

            pointsLists.Add(pointsList4);
            expectedHulls.Add(pointsList2);

            pointsLists.Add(pointsList5);
            expectedHulls.Add(pointsList3);

            pointsLists.Add(pointsList6);
            expectedHulls.Add(pointsList3);

            pointsLists.Add(pointsList7);
            expectedHulls.Add(pointsList3);

            pointsLists.Add(pointsList8);
            expectedHulls.Add(expectedHull8);

            pointsLists.Add(pointsList9);
            expectedHulls.Add(expectedHull8);
        }

        public void FindHullTest()
        {
            GrahamConvexHull grahamHull = new GrahamConvexHull();

            for (int i = 0, n = pointsLists.Count; i < n; i++)
            {
                ComparePointsLists(grahamHull.FindHull(pointsLists[i]), expectedHulls[i]);
            }
        }

        private void ComparePointsLists(List<IntPoint> list1, List<IntPoint> list2)
        {
            //Assert.AreEqual<int>( list1.Count, list2.Count );

            if (list1.Count == list2.Count)
            {
                for (int i = 0, n = list1.Count; i < n; i++)
                {
                    //Assert.AreEqual<IntPoint>( list2[i], list1[i] );
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
            //SimpleShapeChecker

            richTextBox1.Text += "SimpleShapeCheckerTest()\n";
            SimpleShapeCheckerTest();
            /*
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "IsCircleTest()\n";
            IsCircleTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "IsQuadrilateralTest()\n";
            IsQuadrilateralTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "CheckQuadrilateralCornersTest()\n";
            CheckQuadrilateralCornersTest();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "IsTriangleTest()\n";
            IsTriangleTest();
            */
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "IsConvexPolygon()\n";
            IsConvexPolygon();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "CheckShapeTypeTest()\n";
            CheckShapeTypeTest();
        }

        private SimpleShapeChecker shapeChecker = new SimpleShapeChecker();

        private List<IntPoint> idealCicle = new List<IntPoint>();
        private List<IntPoint> distorredCircle = new List<IntPoint>();

        private List<IntPoint> square1 = new List<IntPoint>();
        private List<IntPoint> square1Test = new List<IntPoint>();
        private List<IntPoint> square2 = new List<IntPoint>();
        private List<IntPoint> square2Test = new List<IntPoint>();
        private List<IntPoint> square3 = new List<IntPoint>();
        private List<IntPoint> rectangle = new List<IntPoint>();

        private List<IntPoint> triangle1 = new List<IntPoint>();
        private List<IntPoint> isoscelesTriangle = new List<IntPoint>();
        private List<IntPoint> equilateralTriangle = new List<IntPoint>();
        private List<IntPoint> rectangledTriangle = new List<IntPoint>();

        public void SimpleShapeCheckerTest()
        {
            System.Random rand = new System.Random();

            // generate sample circles
            double radius = 100;

            for (int i = 0; i < 360; i += 10)
            {
                double angle = (double)i / 180 * System.Math.PI;

                // add point to ideal circle
                idealCicle.Add(new IntPoint((int)(radius * System.Math.Cos(angle)), (int)(radius * System.Math.Sin(angle))));

                // add a bit distortion for distorred cirlce
                double distorredRadius = radius + rand.Next(7) - 3;

                distorredCircle.Add(new IntPoint((int)(distorredRadius * System.Math.Cos(angle)), (int)(distorredRadius * System.Math.Sin(angle))));
            }

            // generate sample squares
            square1.Add(new IntPoint(0, 0));
            square1.Add(new IntPoint(50, 0));
            square1.Add(new IntPoint(100, 0));
            square1.Add(new IntPoint(100, 50));
            square1.Add(new IntPoint(100, 100));
            square1.Add(new IntPoint(50, 100));
            square1.Add(new IntPoint(0, 100));
            square1.Add(new IntPoint(0, 50));

            square2.Add(new IntPoint(50, 0));
            square2.Add(new IntPoint(75, 25));
            square2.Add(new IntPoint(100, 50));
            square2.Add(new IntPoint(75, 75));
            square2.Add(new IntPoint(50, 100));
            square2.Add(new IntPoint(25, 75));
            square2.Add(new IntPoint(0, 50));
            square2.Add(new IntPoint(25, 25));

            // these should be obtained as corners
            square1Test.Add(new IntPoint(0, 0));
            square1Test.Add(new IntPoint(100, 0));
            square1Test.Add(new IntPoint(100, 100));
            square1Test.Add(new IntPoint(0, 100));

            square2Test.Add(new IntPoint(50, 0));
            square2Test.Add(new IntPoint(100, 50));
            square2Test.Add(new IntPoint(50, 100));
            square2Test.Add(new IntPoint(0, 50));

            // special square, which may look like circle, but should be recognized as circle
            square3.Add(new IntPoint(50, 0));
            square3.Add(new IntPoint(100, 50));
            square3.Add(new IntPoint(50, 100));
            square3.Add(new IntPoint(0, 50));

            // generate sample rectangle
            rectangle.Add(new IntPoint(0, 0));
            rectangle.Add(new IntPoint(50, 0));
            rectangle.Add(new IntPoint(100, 0));
            rectangle.Add(new IntPoint(100, 20));
            rectangle.Add(new IntPoint(100, 40));
            rectangle.Add(new IntPoint(50, 40));
            rectangle.Add(new IntPoint(0, 40));
            rectangle.Add(new IntPoint(0, 20));

            // generate some triangles
            triangle1.Add(new IntPoint(0, 0));
            triangle1.Add(new IntPoint(50, 10));
            triangle1.Add(new IntPoint(100, 20));
            triangle1.Add(new IntPoint(90, 50));
            triangle1.Add(new IntPoint(80, 80));
            triangle1.Add(new IntPoint(40, 40));

            isoscelesTriangle.Add(new IntPoint(0, 0));
            isoscelesTriangle.Add(new IntPoint(50, 0));
            isoscelesTriangle.Add(new IntPoint(100, 0));
            isoscelesTriangle.Add(new IntPoint(75, 20));
            isoscelesTriangle.Add(new IntPoint(50, 40));
            isoscelesTriangle.Add(new IntPoint(25, 20));

            equilateralTriangle.Add(new IntPoint(0, 0));
            equilateralTriangle.Add(new IntPoint(50, 0));
            equilateralTriangle.Add(new IntPoint(100, 0));
            equilateralTriangle.Add(new IntPoint(75, 43));
            equilateralTriangle.Add(new IntPoint(50, 86));
            equilateralTriangle.Add(new IntPoint(25, 43));

            rectangledTriangle.Add(new IntPoint(0, 0));
            rectangledTriangle.Add(new IntPoint(20, 0));
            rectangledTriangle.Add(new IntPoint(40, 0));
            rectangledTriangle.Add(new IntPoint(20, 50));
            rectangledTriangle.Add(new IntPoint(0, 100));
            rectangledTriangle.Add(new IntPoint(0, 50));
        }

        public void IsCircleTest()
        {
            bool result;
            result = shapeChecker.IsCircle(idealCicle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(distorredCircle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(square1);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(square2);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(square3);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(rectangle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(triangle1);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(equilateralTriangle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(isoscelesTriangle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
            result = shapeChecker.IsCircle(rectangledTriangle);
            richTextBox1.Text += "是否為圓 :\t" + result + "\n";
        }

        public void IsQuadrilateralTest()
        {
            bool result;
            result = shapeChecker.IsQuadrilateral(square1);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(square2);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(square3);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(rectangle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(idealCicle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(distorredCircle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(triangle1);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(equilateralTriangle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(isoscelesTriangle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            result = shapeChecker.IsQuadrilateral(rectangledTriangle);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
        }

        public void CheckQuadrilateralCornersTest()
        {
            List<IntPoint> corners;

            bool result;
            result = shapeChecker.IsQuadrilateral(square1, out corners);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = CompareShape(corners, square1Test);
            richTextBox1.Text += "是否OK :\t" + result + "\n";


            result = shapeChecker.IsQuadrilateral(square2, out corners);
            richTextBox1.Text += "是否為四邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = CompareShape(corners, square2Test);
            richTextBox1.Text += "是否OK :\t" + result + "\n";
        }

        public void IsTriangleTest()
        {
            bool result;
            result = shapeChecker.IsTriangle(triangle1);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(equilateralTriangle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(isoscelesTriangle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(rectangledTriangle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";

            result = shapeChecker.IsTriangle(idealCicle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(distorredCircle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";

            result = shapeChecker.IsTriangle(square1);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(square2);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(square3);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
            result = shapeChecker.IsTriangle(rectangle);
            richTextBox1.Text += "是否為三角形 :\t" + result + "\n";
        }

        public void IsConvexPolygon()
        {
            bool result;

            List<IntPoint> corners;

            result = shapeChecker.IsConvexPolygon(triangle1, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(equilateralTriangle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(isoscelesTriangle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(rectangledTriangle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";

            result = shapeChecker.IsConvexPolygon(square1, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(square2, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(square3, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";
            result = shapeChecker.IsConvexPolygon(rectangle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
            richTextBox1.Text += "Count :\t" + corners.Count + "\n";

            result = shapeChecker.IsConvexPolygon(idealCicle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";

            result = shapeChecker.IsConvexPolygon(distorredCircle, out corners);
            richTextBox1.Text += "是否為凸多邊形 :\t" + result + "\n";
        }

        public void CheckShapeTypeTest()
        {
            richTextBox1.Text += "測試 CheckShapeType\n";

            richTextBox1.Text += "ShapeType.Circle :\t" + ShapeType.Circle + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(idealCicle) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(distorredCircle) + "\n";

            richTextBox1.Text += "ShapeType.Quadrilateral :\t" + ShapeType.Quadrilateral + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(square1) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(square2) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(square3) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(rectangle) + "\n";

            richTextBox1.Text += "ShapeType.Triangle :\t" + ShapeType.Triangle + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(triangle1) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(equilateralTriangle) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(isoscelesTriangle) + "\n";
            richTextBox1.Text += "取得形狀 :\t" + shapeChecker.CheckShapeType(rectangledTriangle) + "\n";
        }

        private bool CompareShape(List<IntPoint> shape1, List<IntPoint> shape2)
        {
            if (shape1.Count != shape2.Count)
                return false;
            if (shape1.Count == 0)
                return true;

            int index = shape1.IndexOf(shape2[0]);

            if (index == -1)
                return false;

            index++;

            for (int i = 1; i < shape2.Count; i++, index++)
            {
                if (index >= shape1.Count)
                    index = 0;

                if (!shape1[index].Equals(shape2[i]))
                    return false;
            }

            return true;
        }

        /*
        [Row( PolygonSubType.Unknown, new int[] { 0, 0, 100, 0, 90, 10 } )]     // just a triangle
        [Row( PolygonSubType.IsoscelesTriangle, new int[] { 0, 0, 100, 0, 50, 10 } )]
        [Row( PolygonSubType.IsoscelesTriangle, new int[] { 0, 0, 100, 0, 50, 200 } )]
        [Row( PolygonSubType.EquilateralTriangle, new int[] { 0, 0, 100, 0, 50, 86 } )]
        [Row( PolygonSubType.RectangledIsoscelesTriangle, new int[] { 0, 0, 100, 0, 50, 50 } )]
        [Row( PolygonSubType.RectangledIsoscelesTriangle, new int[] { 0, 0, 100, 0, 0, 100 } )]
        [Row( PolygonSubType.RectangledTriangle, new int[] { 0, 0, 100, 0, 0, 50 } )]
        [Row( PolygonSubType.Unknown, new int[] { 0, 0, 100, 0, 90, 50, 10, 70 } )]     // just a quadrilateral
        [Row( PolygonSubType.Trapezoid, new int[] { 0, 0, 100, 0, 90, 50, 10, 50 } )]
        [Row( PolygonSubType.Trapezoid, new int[] { 0, 0, 100, 0, 90, 50, 0, 50 } )]
        [Row( PolygonSubType.Trapezoid, new int[] { 0, 0, 100, 0, 90, 50, 0, 53 } )]    // a bit disformed
        [Row( PolygonSubType.Parallelogram, new int[] { 0, 0, 100, 0, 120, 50, 20, 50 } )]
        [Row( PolygonSubType.Parallelogram, new int[] { 0, 0, 100, 0, 70, 50, -30, 50 } )]
        [Row( PolygonSubType.Rectangle, new int[] { 0, 0, 100, 0, 100, 50, 0, 50 } )]
        [Row( PolygonSubType.Rectangle, new int[] { 0, 0, 100, 0, 100, 52, -3, 50 } )]   // a bit disformed
        [Row( PolygonSubType.Square, new int[] { 0, 0, 100, 0, 100, 100, 0, 100 } )]
        [Row( PolygonSubType.Square, new int[] { 50, 0, 100, 50, 50, 100, 0, 50 } )]
        [Row( PolygonSubType.Square, new int[] { 51, 0, 100, 49, 50, 101, 1, 50 } )]    // a bit disformed
        [Row( PolygonSubType.Rhombus, new int[] { 30, 0, 60, 50, 30, 100, 0, 50 } )]
        [Row( PolygonSubType.Rhombus, new int[] { 0, 0, 100, 0, 130, 95, 30, 95 } )]
        [Row( PolygonSubType.Unknown, new int[] { 0, 0, 100, 0, 90, 50, 40, 70, 10, 40 } )]     // unknown if 5 corners or more
        */
        public void CheckPolygonSubTypeTest(PolygonSubType expectedSubType, int[] corners)
        {
            //還沒測
            //Assert.AreEqual( expectedSubType, shapeChecker.CheckPolygonSubType( GetListOfPointFromArray( corners ) ) );
        }

        private List<IntPoint> GetListOfPointFromArray(int[] points)
        {
            List<IntPoint> list = new List<IntPoint>();

            for (int i = 0, n = points.Length; i < n; i += 2)
            {
                list.Add(new IntPoint(points[i], points[i + 1]));
            }

            return list;
        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {
            //LineSegmentTest

            float sx = 0;
            float sy = 0;
            float ex = -3;
            float ey = -4;
            LineSegment segment = new LineSegment(new AForge.Point(sx, sy), new AForge.Point(ex, ey));
            richTextBox1.Text += "長度 : " + segment.Length + "\n";

            //3030
            float x = 2.5f;
            float y = 6;
            float x1 = 0;
            float y1 = 5;
            float x2 = 0;
            float y2 = 8;

            AForge.Point pt = new AForge.Point(x, y);
            AForge.Point pt1 = new AForge.Point(x1, y1);
            AForge.Point pt2 = new AForge.Point(x2, y2);
            segment = new LineSegment(pt1, pt2);

            richTextBox1.Text += "長度 : " + segment.DistanceToPoint(pt) + "\n";

            /*
            [Row( 0, 0, 5, 0, 8, 0, 5 )]
            [Row( 6, 2.5, 5, 0, 8, 0, 2.5 )]
            [Row( 2.5, 6, 0, 5, 0, 8, 2.5 )]
            [Row( 9, 0, 5, 0, 8, 0, 1 )]
            [Row( 3, 4, 0, 0, -10, 0, 5 )]
            */

            //3030


        }

        // Denotes which versions of the test are supposed to return non-null values:
        // SegmentA means that the segment A1-A2 intersects with the line B1-B2, but not
        // with the segment B1-B2.
        public enum IntersectionType { None, LinesOnly, SegmentA, SegmentB, AllFour };

        /*
        [Row( 0, 0, 4, 4, 0, 4, 4, 0, 2, 2, IntersectionType.AllFour )]
        [Row( 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, IntersectionType.AllFour )]
        [Row( 0, 0, 4, 4, 4, 8, 8, 4, 6, 6, IntersectionType.SegmentB )]
        [Row( -4, -4, 0, 0, 4, 0, 8, -4, 2, 2, IntersectionType.LinesOnly )]
        [Row( 0, 0, 6, 0, 5, 1, 5, 5, 5, 0, IntersectionType.SegmentA )]
        [Row( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, IntersectionType.LinesOnly, ExpectedException = typeof( ArgumentException ), ExpectedExceptionMessage = "Start point of the line cannot be the same as its end point." )]
        [Row( 0, 0, 0, 5, 1, 0, 1, 5, 0, 0, IntersectionType.None)]
        */
        public void IntersectionPointTest(float ax1, float ay1, float ax2, float ay2, float bx1, float by1, float bx2, float by2, float ix, float iy, IntersectionType type)
        {
            LineSegment segA = new LineSegment(new AForge.Point(ax1, ay1), new AForge.Point(ax2, ay2));
            LineSegment segB = new LineSegment(new AForge.Point(bx1, by1), new AForge.Point(bx2, by2));
            AForge.Point expectedIntersection = new AForge.Point(ix, iy);
            /*
            Assert.DoesNotThrow(() =>
            {
                AForge.Point? segSeg = segA.GetIntersectionWith(segB);
                AForge.Point? segLine = segA.GetIntersectionWith((Line)segB);
                AForge.Point? lineSeg = ((Line)segA).GetIntersectionWith(segB);

                if (type == IntersectionType.AllFour)
                {
                    //Assert.AreEqual( expectedIntersection, segSeg );
                }
                else
                {
                    //Assert.AreEqual( null, segSeg );
                }

                if ((type == IntersectionType.AllFour) || (type == IntersectionType.SegmentA))
                {
                    //Assert.AreEqual( expectedIntersection, segLine );
                }
                else
                {
                    //Assert.AreEqual( null, segLine );
                }

                if ((type == IntersectionType.AllFour) || (type == IntersectionType.SegmentB))
                {
                    //Assert.AreEqual( expectedIntersection, lineSeg );
                }
                else
                {
                    //Assert.AreEqual( null, lineSeg );
                }
            });
            */

            AForge.Point? lineLine = ((Line)segA).GetIntersectionWith((Line)segB);

            if (type != IntersectionType.None)
            {
                //Assert.AreEqual( expectedIntersection, lineLine );
            }
            else
            {
                //Assert.AreEqual( null, lineLine );
            }
        }

        /*
        [Row( 0, 0, 0, 1, 1, 1, 1, 2 )]
        [Row( 0, 0, 4, 4, 3, -1, 7, 3 )]
        [Row( 0, 0, 1, 0, 1, 1, 2, 1 )]
        */
        public void ParallelIntersectionPointTest(float ax1, float ay1, float ax2, float ay2, float bx1, float by1, float bx2, float by2)
        {
            LineSegment segA = new LineSegment(new AForge.Point(ax1, ay1), new AForge.Point(ax2, ay2));
            LineSegment segB = new LineSegment(new AForge.Point(bx1, by1), new AForge.Point(bx2, by2));

            // are we really parallel?
            //Assert.AreEqual( null, ( (Line) segA ).GetIntersectionWith( (Line) segB ) );

            //Assert.AreEqual( null, segA.GetIntersectionWith( (Line) segB ) );
            //Assert.AreEqual( null, ( (Line) segA ).GetIntersectionWith( segB ) );
            //Assert.AreEqual( null, segB.GetIntersectionWith( (Line) segA ) );
            //Assert.AreEqual( null, ( (Line) segB ).GetIntersectionWith( segA ) );
            //Assert.AreEqual( null, segB.GetIntersectionWith( segA ) );
            //Assert.AreEqual( null, segA.GetIntersectionWith( segB ) );
        }

        /*
        [Row( 0, 0, 1, 1, 2, 2, 3, 3 )]
        [Row( 0, 1, 0, 2, 0, 3, 0, 4 )]
        [Row( 0, 0, -1, 1, -2, 2, -3, 3, -4, 4 )]
        [Row( 1, 0, 2, 0, 3, 0, 4, 0 )]
        [Row(0, 0, 0, 1, 0, 2, 0, 3 )]
        */
        public void CollinearIntersectionPointTest(float ax1, float ay1, float ax2, float ay2, float bx1, float by1, float bx2, float by2)
        {
            LineSegment segA = new LineSegment(new AForge.Point(ax1, ay1), new AForge.Point(ax2, ay2));
            LineSegment segB = new LineSegment(new AForge.Point(bx1, by1), new AForge.Point(bx2, by2));

            // are we really collinear?
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( (Line) segB ) );

            //Assert.Throws<InvalidOperationException>( ( ) => segA.GetIntersectionWith( (Line) segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => segB.GetIntersectionWith( (Line) segA ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segB ).GetIntersectionWith( segA ) );
            //Assert.AreEqual( null, segB.GetIntersectionWith( segA ) );
            //Assert.AreEqual( null, segA.GetIntersectionWith( segB ) );
        }

        /*
        [Row( 0, 0, 1, 1, 1, 1, 3, 3, 1, 1 )]
        [Row( 0, 0, 1, 1, 3, 3, 1, 1, 1, 1 )]
        [Row( 0, 0, 1, 1, 0, 0, -3, -3, 0, 0 )]
        [Row( 0, 0, 1, 1, -1, -1, 0, 0, 0, 0 )]
        [Row( 0, 1, 0, 2, 0, 1, 0, 0, 0, 1 )]
        [Row( 0, 1, 0, 2, 0, 2, 0, 4, 0, 2 )]
        [Row( 0, 1, 0, 2, 0, 0, 0, 1, 0, 1 )]
        [Row( 0, 1, 0, 2, 0, 3, 0, 2, 0, 2 )]
        */
        public void CommonIntersectionPointTest(float ax1, float ay1, float ax2, float ay2, float bx1, float by1, float bx2, float by2, float ix, float iy)
        {
            LineSegment segA = new LineSegment(new AForge.Point(ax1, ay1), new AForge.Point(ax2, ay2));
            LineSegment segB = new LineSegment(new AForge.Point(bx1, by1), new AForge.Point(bx2, by2));
            AForge.Point expectedIntersection = new AForge.Point(ix, iy);

            // are we really collinear?
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( (Line) segB ) );

            //Assert.Throws<InvalidOperationException>( ( ) => segA.GetIntersectionWith( (Line) segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => segB.GetIntersectionWith( (Line) segA ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segB ).GetIntersectionWith( segA ) );
            //Assert.AreEqual( expectedIntersection, segB.GetIntersectionWith( segA ) );
            //Assert.AreEqual( expectedIntersection, segA.GetIntersectionWith( segB ) );
        }

        /*
        [Row( 0, 0, 0, 2, 0, 1, 0, 3 )]
        [Row( 1, 2, 3, 4, 2, 3, 4, 5 )]
        [Row( 0, 0, 2, 0, 3, 0, 1, 0 )]
        */
        public void OverlappingSegmentIntersectionPointTest(float ax1, float ay1, float ax2, float ay2, float bx1, float by1, float bx2, float by2)
        {
            LineSegment segA = new LineSegment(new AForge.Point(ax1, ay1), new AForge.Point(ax2, ay2));
            LineSegment segB = new LineSegment(new AForge.Point(bx1, by1), new AForge.Point(bx2, by2));

            // are we really collinear?
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( (Line) segB ) );

            //Assert.Throws<InvalidOperationException>( ( ) => segA.GetIntersectionWith( (Line) segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segA ).GetIntersectionWith( segB ) );
            //Assert.Throws<InvalidOperationException>( ( ) => segB.GetIntersectionWith( (Line) segA ) );
            //Assert.Throws<InvalidOperationException>( ( ) => ( (Line) segB ).GetIntersectionWith( segA ) );
            //Assert.Throws<InvalidOperationException>( ( ) => segB.GetIntersectionWith( segA ) );
            //Assert.Throws<InvalidOperationException>( ( ) => segA.GetIntersectionWith( segB ) );
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
            //UnmanagedImageTest

            Collect8bppPixelValuesTest_Grayscale();
            Collect8bppPixelValuesTest_RGB();
            CollectActivePixelsTest();

            //還有

        }

        public void Collect8bppPixelValuesTest_Grayscale()
        {
            // create grayscale image
            UnmanagedImage image = UnmanagedImage.Create(320, 240, PixelFormat.Format8bppIndexed);

            // draw vertical and horizontal lines
            Drawing.Line(image, new IntPoint(10, 10), new IntPoint(20, 10), Color.FromArgb(128, 128, 128));
            Drawing.Line(image, new IntPoint(20, 20), new IntPoint(20, 30), Color.FromArgb(64, 64, 64));

            // prepare lists with coordinates
            List<IntPoint> horizontal = new List<IntPoint>();
            List<IntPoint> horizontalU = new List<IntPoint>();
            List<IntPoint> horizontalD = new List<IntPoint>();

            for (int x = 10; x <= 20; x++)
            {
                horizontal.Add(new IntPoint(x, 10));  // on the line
                horizontalU.Add(new IntPoint(x, 9));  // above
                horizontalD.Add(new IntPoint(x, 11)); // below
            }

            List<IntPoint> vertical = new List<IntPoint>();
            List<IntPoint> verticalL = new List<IntPoint>();
            List<IntPoint> verticalR = new List<IntPoint>();

            for (int y = 20; y <= 30; y++)
            {
                vertical.Add(new IntPoint(20, y));    // on the line
                verticalL.Add(new IntPoint(19, y));   // left
                verticalR.Add(new IntPoint(21, y));   // right
            }

            // collect all pixel's values
            byte[] horizontalValues = image.Collect8bppPixelValues(horizontal);
            byte[] horizontalUValues = image.Collect8bppPixelValues(horizontalU);
            byte[] horizontalDValues = image.Collect8bppPixelValues(horizontalD);
            byte[] verticalValues = image.Collect8bppPixelValues(vertical);
            byte[] verticalLValues = image.Collect8bppPixelValues(verticalL);
            byte[] verticalRValues = image.Collect8bppPixelValues(verticalR);

            //Assert.AreEqual( horizontal.Count, horizontalValues.Length );
            //Assert.AreEqual( vertical.Count, verticalValues.Length );

            // check all pixel values
            for (int i = 0, n = horizontalValues.Length; i < n; i++)
            {
                //Assert.AreEqual<byte>( 128, horizontalValues[i] );
                //Assert.AreEqual<byte>( 0, horizontalUValues[i] );
                //Assert.AreEqual<byte>( 0, horizontalDValues[i] );
            }

            for (int i = 0, n = verticalValues.Length; i < n; i++)
            {
                //Assert.AreEqual<byte>( 64, verticalValues[i] );
                //Assert.AreEqual<byte>( 0, verticalLValues[i] );
                //Assert.AreEqual<byte>( 0, verticalRValues[i] );
            }
        }

        public void Collect8bppPixelValuesTest_RGB()
        {
            // create grayscale image
            UnmanagedImage image = UnmanagedImage.Create(320, 240, PixelFormat.Format24bppRgb);

            // draw vertical and horizontal lines
            Drawing.Line(image, new IntPoint(10, 10), new IntPoint(20, 10), Color.FromArgb(128, 129, 130));
            Drawing.Line(image, new IntPoint(20, 20), new IntPoint(20, 30), Color.FromArgb(64, 65, 66));

            // prepare lists with coordinates
            List<IntPoint> horizontal = new List<IntPoint>();
            List<IntPoint> horizontalU = new List<IntPoint>();
            List<IntPoint> horizontalD = new List<IntPoint>();

            for (int x = 10; x <= 20; x++)
            {
                horizontal.Add(new IntPoint(x, 10));  // on the line
                horizontalU.Add(new IntPoint(x, 9));  // above
                horizontalD.Add(new IntPoint(x, 11)); // below
            }

            List<IntPoint> vertical = new List<IntPoint>();
            List<IntPoint> verticalL = new List<IntPoint>();
            List<IntPoint> verticalR = new List<IntPoint>();

            for (int y = 20; y <= 30; y++)
            {
                vertical.Add(new IntPoint(20, y));    // on the line
                verticalL.Add(new IntPoint(19, y));   // left
                verticalR.Add(new IntPoint(21, y));   // right
            }

            // collect all pixel's values
            byte[] horizontalValues = image.Collect8bppPixelValues(horizontal);
            byte[] horizontalUValues = image.Collect8bppPixelValues(horizontalU);
            byte[] horizontalDValues = image.Collect8bppPixelValues(horizontalD);
            byte[] verticalValues = image.Collect8bppPixelValues(vertical);
            byte[] verticalLValues = image.Collect8bppPixelValues(verticalL);
            byte[] verticalRValues = image.Collect8bppPixelValues(verticalR);

            //Assert.AreEqual( horizontal.Count * 3, horizontalValues.Length );
            //Assert.AreEqual( vertical.Count * 3, verticalValues.Length );

            // check all pixel values
            for (int i = 0, n = horizontalValues.Length; i < n; i += 3)
            {
                //Assert.AreEqual<byte>( 128, horizontalValues[i] );
                //Assert.AreEqual<byte>( 129, horizontalValues[i + 1] );
                //Assert.AreEqual<byte>( 130, horizontalValues[i + 2] );

                //Assert.AreEqual<byte>( 0, horizontalUValues[i] );
                //Assert.AreEqual<byte>( 0, horizontalUValues[i + 1] );
                //Assert.AreEqual<byte>( 0, horizontalUValues[i + 2] );

                //Assert.AreEqual<byte>( 0, horizontalDValues[i] );
                //Assert.AreEqual<byte>( 0, horizontalDValues[i + 1] );
                //Assert.AreEqual<byte>( 0, horizontalDValues[i + 2] );
            }

            for (int i = 0, n = verticalValues.Length; i < n; i += 3)
            {
                //Assert.AreEqual<byte>( 64, verticalValues[i] );
                //Assert.AreEqual<byte>( 65, verticalValues[i + 1] );
                //Assert.AreEqual<byte>( 66, verticalValues[i + 2] );

                //Assert.AreEqual<byte>( 0, verticalLValues[i] );
                //Assert.AreEqual<byte>( 0, verticalLValues[i + 1] );
                //Assert.AreEqual<byte>( 0, verticalLValues[i + 2] );

                //Assert.AreEqual<byte>( 0, verticalRValues[i] );
                //Assert.AreEqual<byte>( 0, verticalRValues[i + 1] );
                //Assert.AreEqual<byte>( 0, verticalRValues[i + 2] );
            }
        }

        public void CollectActivePixelsTest()
        {
            // create grayscale image
            UnmanagedImage image24 = UnmanagedImage.Create(7, 7, PixelFormat.Format24bppRgb);
            UnmanagedImage image8 = UnmanagedImage.Create(7, 7, PixelFormat.Format8bppIndexed);

            Drawing.FillRectangle(image24, new Rectangle(1, 1, 5, 5), Color.FromArgb(255, 255, 255));
            Drawing.FillRectangle(image24, new Rectangle(2, 2, 3, 3), Color.FromArgb(1, 1, 1));
            Drawing.FillRectangle(image24, new Rectangle(3, 3, 1, 1), Color.FromArgb(0, 0, 0));

            Drawing.FillRectangle(image8, new Rectangle(1, 1, 5, 5), Color.FromArgb(255, 255, 255));
            Drawing.FillRectangle(image8, new Rectangle(2, 2, 3, 3), Color.FromArgb(1, 1, 1));
            Drawing.FillRectangle(image8, new Rectangle(3, 3, 1, 1), Color.FromArgb(0, 0, 0));

            List<IntPoint> pixels24 = image24.CollectActivePixels();
            List<IntPoint> pixels8 = image8.CollectActivePixels();

            //Assert.AreEqual<int>( pixels24.Count, 24 );
            //Assert.AreEqual<int>( pixels8.Count, 24 );

            for (int i = 1; i < 6; i++)
            {
                for (int j = 1; j < 6; j++)
                {
                    if ((i == 3) && (j == 3))
                        continue;

                    //Assert.IsTrue( pixels24.Contains( new IntPoint( j, i ) ) );
                    //Assert.IsTrue( pixels8.Contains( new IntPoint( j, i ) ) );
                }
            }

            pixels24 = image24.CollectActivePixels(new Rectangle(1, 0, 5, 4));
            pixels8 = image8.CollectActivePixels(new Rectangle(1, 0, 5, 4));

            //Assert.AreEqual<int>( pixels24.Count, 14 );
            //Assert.AreEqual<int>( pixels8.Count, 14 );

            for (int i = 1; i < 4; i++)
            {
                for (int j = 1; j < 6; j++)
                {
                    if ((i == 3) && (j == 3))
                        continue;

                    //Assert.IsTrue( pixels24.Contains( new IntPoint( j, i ) ) );
                    //Assert.IsTrue( pixels8.Contains( new IntPoint( j, i ) ) );
                }
            }
        }

        /*
        [Row( PixelFormat.Format8bppIndexed )]
        [Row( PixelFormat.Format24bppRgb )]
        [Row( PixelFormat.Format32bppArgb)]
        [Row( PixelFormat.Format32bppRgb )]
        [Row( PixelFormat.Format16bppGrayScale )]
        [Row( PixelFormat.Format48bppRgb )]
        [Row( PixelFormat.Format64bppArgb )]
        [Row( PixelFormat.Format32bppPArgb, ExpectedException = typeof( UnsupportedImageFormatException ) )]
        */
        public void SetPixelTest(PixelFormat pixelFormat)
        {
            UnmanagedImage image = UnmanagedImage.Create(320, 240, pixelFormat);
            Color color = Color.White;
            byte value = 255;

            image.SetPixel(0, 0, color);
            image.SetPixel(319, 0, color);
            image.SetPixel(0, 239, color);
            image.SetPixel(319, 239, value);
            image.SetPixel(160, 120, value);

            image.SetPixel(-1, -1, color);
            image.SetPixel(320, 0, color);
            image.SetPixel(0, 240, value);
            image.SetPixel(320, 240, value);

            List<IntPoint> pixels = image.CollectActivePixels();

            //Assert.AreEqual<int>( 5, pixels.Count );

            //Assert.IsTrue( pixels.Contains( new IntPoint( 0, 0 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 319, 0 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 0, 239 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 319, 239 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 160, 120 ) ) );
        }

        public void SetGetPixelGrayscale()
        {
            UnmanagedImage image = UnmanagedImage.Create(320, 240, PixelFormat.Format8bppIndexed);

            image.SetPixel(0, 0, 255);
            image.SetPixel(319, 0, 127);
            image.SetPixel(0, 239, Color.FromArgb(64, 64, 64));

            Color color1 = image.GetPixel(0, 0);
            Color color2 = image.GetPixel(319, 0);
            Color color3 = image.GetPixel(0, 239);

            //Assert.AreEqual<int>( 255, color1.R );
            //Assert.AreEqual<int>( 255, color1.G );
            //Assert.AreEqual<int>( 255, color1.B );

            //Assert.AreEqual<int>( 127, color2.R );
            //Assert.AreEqual<int>( 127, color2.G );
            //Assert.AreEqual<int>( 127, color2.B );

            //Assert.AreEqual<int>( 64, color3.R );
            //Assert.AreEqual<int>( 64, color3.G );
            //Assert.AreEqual<int>( 64, color3.B );
        }

        /*
        [Row( PixelFormat.Format24bppRgb )]
        [Row( PixelFormat.Format32bppArgb )]
        [Row( PixelFormat.Format32bppRgb )]
        */
        public void SetGetPixelColor(PixelFormat pixelFormat)
        {
            UnmanagedImage image = UnmanagedImage.Create(320, 240, pixelFormat);

            image.SetPixel(0, 0, Color.FromArgb(255, 10, 20, 30));
            image.SetPixel(319, 0, Color.FromArgb(127, 110, 120, 130));
            image.SetPixel(0, 239, Color.FromArgb(64, 210, 220, 230));

            Color color1 = image.GetPixel(0, 0);
            Color color2 = image.GetPixel(319, 0);
            Color color3 = image.GetPixel(0, 239);

            //Assert.AreEqual<int>( 10, color1.R );
            //Assert.AreEqual<int>( 20, color1.G );
            //Assert.AreEqual<int>( 30, color1.B );

            //Assert.AreEqual<int>( 110, color2.R );
            //Assert.AreEqual<int>( 120, color2.G );
            //Assert.AreEqual<int>( 130, color2.B );

            //Assert.AreEqual<int>( 210, color3.R );
            //Assert.AreEqual<int>( 220, color3.G );
            //Assert.AreEqual<int>( 230, color3.B );

            if (pixelFormat == PixelFormat.Format32bppArgb)
            {
                //Assert.AreEqual<int>( 255, color1.A );
                //Assert.AreEqual<int>( 127, color2.A );
                //Assert.AreEqual<int>( 64, color3.A );
            }
        }

        /*
        [Row( PixelFormat.Format8bppIndexed )]
        [Row( PixelFormat.Format24bppRgb )]
        [Row( PixelFormat.Format32bppArgb )]
        [Row( PixelFormat.Format32bppRgb )]
        [Row( PixelFormat.Format16bppGrayScale )]
        [Row( PixelFormat.Format48bppRgb )]
        [Row( PixelFormat.Format64bppArgb )]
        [Row( PixelFormat.Format32bppPArgb, ExpectedException = typeof( UnsupportedImageFormatException ) )]
        */
        public void SetPixelsTest(PixelFormat pixelFormat)
        {
            UnmanagedImage image = UnmanagedImage.Create(320, 240, pixelFormat);
            Color color = Color.White;
            List<IntPoint> points = new List<IntPoint>();

            points.Add(new IntPoint(0, 0));
            points.Add(new IntPoint(319, 0));
            points.Add(new IntPoint(0, 239));
            points.Add(new IntPoint(319, 239));
            points.Add(new IntPoint(160, 120));

            points.Add(new IntPoint(-1, -1));
            points.Add(new IntPoint(320, 0));
            points.Add(new IntPoint(0, 240));
            points.Add(new IntPoint(320, 240));

            image.SetPixels(points, color);

            List<IntPoint> pixels = image.CollectActivePixels();

            //Assert.AreEqual<int>( 5, pixels.Count );

            //Assert.IsTrue( pixels.Contains( new IntPoint( 0, 0 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 319, 0 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 0, 239 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 319, 239 ) ) );
            //Assert.IsTrue( pixels.Contains( new IntPoint( 160, 120 ) ) );
        }

        /*
        [Row( PixelFormat.Format24bppRgb,   1,   1, 240,   0,   0 )]
        [Row( PixelFormat.Format24bppRgb, 318,   1,   0, 240,   0 )]
        [Row( PixelFormat.Format24bppRgb, 318, 238, 240, 240,   0 )]
        [Row( PixelFormat.Format24bppRgb,   1, 238,   0,   0, 240 )]
        [Row( PixelFormat.Format24bppRgb, 160, 120, 240, 240, 240 )]

        [Row( PixelFormat.Format32bppArgb,   1,   1, 240,   0,   0 )]
        [Row( PixelFormat.Format32bppArgb, 318,   1,   0, 240,   0 )]
        [Row( PixelFormat.Format32bppArgb, 318, 238, 240, 240,   0 )]
        [Row( PixelFormat.Format32bppArgb,   1, 238,   0,   0, 240 )]
        [Row( PixelFormat.Format32bppArgb, 160, 120, 240, 240, 240 )]

        [Row( PixelFormat.Format32bppRgb,   1,   1, 240,   0,   0 )]
        [Row( PixelFormat.Format32bppRgb, 318,   1,   0, 240,   0 )]
        [Row( PixelFormat.Format32bppRgb, 318, 238, 240, 240,   0 )]
        [Row( PixelFormat.Format32bppRgb,   1, 238,   0,   0, 240 )]
        [Row( PixelFormat.Format32bppRgb, 160, 120, 240, 240, 240 )]

        [Row( PixelFormat.Format8bppIndexed,   1,   1, 128, 128, 128 )]
        [Row( PixelFormat.Format8bppIndexed, 318,   1,  96,  96,  96 )]
        [Row( PixelFormat.Format8bppIndexed, 318, 238, 192, 192, 192 )]
        [Row( PixelFormat.Format8bppIndexed,   1, 238,  32,  32,  32 )]
        [Row( PixelFormat.Format8bppIndexed, 160, 120, 255, 255, 255 )]
        */
        public void ToManagedImageTest(PixelFormat pixelFormat, int x, int y, byte red, byte green, byte blue)
        {
            UnmanagedImage image = UnmanagedImage.Create(320, 240, pixelFormat);

            image.SetPixel(new IntPoint(x, y), Color.FromArgb(255, red, green, blue));

            Bitmap bitmap = image.ToManagedImage();

            // check colors of pixels
            //Assert.AreEqual<Color>( Color.FromArgb( 255, red, green, blue ), bitmap.GetPixel( x, y ) );

            // make sure there are only 1 pixel
            UnmanagedImage temp = UnmanagedImage.FromManagedImage(bitmap);

            List<IntPoint> pixels = temp.CollectActivePixels();
            //Assert.AreEqual<int>( 1, pixels.Count );

            image.Dispose();
            bitmap.Dispose();
            temp.Dispose();
        }

        //------------------------------------------------------------  # 60個


        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//richTextBox1.Text += "---------------\n";  // 15個
//---------------  # 15個


/*  可搬出

*/

