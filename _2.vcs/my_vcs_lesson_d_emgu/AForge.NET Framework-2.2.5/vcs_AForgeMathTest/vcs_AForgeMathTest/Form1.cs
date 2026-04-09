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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix3x3 matrix = Matrix3x3.CreateRotationY(radians);

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
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix3x3 matrix = Matrix3x3.CreateRotationX(radians);

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
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix3x3 matrix = Matrix3x3.CreateRotationZ(radians);

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

            Matrix3x3 inverse = matrix.Inverse();
            Matrix3x3 identity = matrix * inverse;

            //Assert.AreEqual<bool>( true, ApproximateEquals( identity, Matrix3x3.Identity ) );
        }

        public void AddMatricesTest()
        {
            Matrix3x3 expectedResult = new Matrix3x3();

            expectedResult.V00 = 3;
            expectedResult.V01 = 3;
            expectedResult.V02 = 6;

            expectedResult.V10 = 4;
            expectedResult.V11 = 5;
            expectedResult.V12 = 3;

            expectedResult.V20 = 4;
            expectedResult.V21 = 5;
            expectedResult.V22 = 3;

            Matrix3x3 result = a1 + a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
        }

        public void SubtractMatricesTest()
        {
            Matrix3x3 expectedResult = new Matrix3x3();

            expectedResult.V00 = -1;
            expectedResult.V01 = 1;
            expectedResult.V02 = 0;

            expectedResult.V10 = 2;
            expectedResult.V11 = -1;
            expectedResult.V12 = -1;

            expectedResult.V20 = -2;
            expectedResult.V21 = 1;
            expectedResult.V22 = 1;

            Matrix3x3 result = a1 - a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
        }

        public void MultiplyMatricesTest()
        {
            Matrix3x3 expectedResult = new Matrix3x3();

            expectedResult.V00 = 13;
            expectedResult.V01 = 13;
            expectedResult.V02 = 10;

            expectedResult.V10 = 11;
            expectedResult.V11 = 11;
            expectedResult.V12 = 14;

            expectedResult.V20 = 11;
            expectedResult.V21 = 14;
            expectedResult.V22 = 11;

            Matrix3x3 result = a1 * a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
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
            // TODO: better algorithm should be put into the framework actually
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
            UnmanagedImage uImage = UnmanagedImage.Create(10, 10, PixelFormat.Format8bppIndexed);

            for (int y = 0; y < 10; y++)
            {
                for (int x = 0; x < 10; x++)
                {
                    uImage.SetPixel(x, y, ((x + y) % 2 == 0) ? Color.FromArgb(0, 0, 0) : Color.FromArgb(1, 1, 1));
                }
            }


            integralImage = IntegralImage.FromBitmap(uImage);


            //pictureBox1.Image = integralImage;


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
            [Row( 1, 1, 45, 1.41421356f, -1, 2 )]
            [Row( -2, 2, 135, 2 * 1.41421356f, 1, 4 )]
            [Row( -0.5, -1.73205081f / 2, 240, 1, -1 / 1.73205081f, -2 / 1.73205081f )]
            [Row( 1, 0, 0, 1, float.NegativeInfinity, 1 )]
            [Row( 0, -1, 270, 1, 0, -1 )]
            */

            AForge.Point pt = new AForge.Point(x, y);

            // test Point-Theta factory
            Line line = Line.FromPointTheta(pt, theta);
            richTextBox1.Text += "aaaa " + line.Slope + "\n";
            richTextBox1.Text += "aaaa " + line.Intercept + "\n";

            // calculate radius
            float radius = pt.EuclideanNorm();
            richTextBox1.Text += "radius " + radius + "\n";

            // test R-Theta factory
            line = Line.FromRTheta(radius, theta);
            richTextBox1.Text += "bbbb " + line.Slope + "\n";
            richTextBox1.Text += "bbbb " + line.Intercept + "\n";


            //檢查一直線是否垂直
            int sx = 0;
            int sy = 0;
            int ex = 100;
            int ey = 100;

            line = Line.FromPoints(new AForge.Point(sx, sy), new AForge.Point(ex, ey));
            richTextBox1.Text += "cccc " + line.Slope + "\n";
            richTextBox1.Text += "cccc " + line.Intercept + "\n";
            richTextBox1.Text += "cccc " + line.IsVertical + "\n";
            richTextBox1.Text += "cccc " + line.IsHorizontal + "\n";

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

            sx2 = 100f;
            sy2 = 0f;
            ex2 = 200f;
            ey2 = 100f;

            Line line1 = Line.FromPoints(new AForge.Point(sx1, sy1), new AForge.Point(ex1, ey1));
            Line line2 = Line.FromPoints(new AForge.Point(sx2, sy2), new AForge.Point(ex2, ey2));

            AForge.Point? result = line1.GetIntersectionWith(line2);
            if (result == null)
                richTextBox1.Text += "無交叉點\n";
            else
                richTextBox1.Text += result.ToString() + "\n";

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
            Vector3 v3 = new Vector3(7);

            //在下面
        }

        public void ConstructorTest()
        {
            Vector3 v1 = new Vector3(1, 2, 3);
            Vector3 v2 = new Vector3(-1, -2, -3);
            Vector3 v3 = new Vector3(7);//X Y Z 都設為7

            // v1.X v1.Y v1.Z
            /*
            Assert.AreEqual<float>(v1.X, 1);
            Assert.AreEqual<float>(v1.Y, 2);
            Assert.AreEqual<float>(v1.Z, 3);

            Assert.AreEqual<float>(v2.X, -1);
            Assert.AreEqual<float>(v2.Y, -2);
            Assert.AreEqual<float>(v2.Z, -3);

            Assert.AreEqual<float>(v3.X, 7);
            Assert.AreEqual<float>(v3.Y, 7);
            Assert.AreEqual<float>(v3.Z, 7);
            */
        }

        /*
        [Row(0, 0, 0, 0, 0, 0, 0)]
        [Row(0, 7, 7, 0, 7, 0, 1)]
        [Row(0, 0, 7, 0, 7, 0, 2)]
        [Row(0, 7, 0, 0, 7, 0, 1)]
        [Row(7, 0, 7, 0, 7, 1, 0)]
        [Row(5, 7, 9, 5, 9, 0, 2)]
        [Row(5, 9, 7, 5, 9, 0, 1)]
        [Row(7, 5, 9, 5, 9, 1, 2)]
        [Row(7, 9, 5, 5, 9, 2, 1)]
        [Row(9, 5, 7, 5, 9, 1, 0)]
        [Row(9, 7, 5, 5, 9, 2, 0)]
        */
        public void MinMaxTest(float x, float y, float z, float expectedMin, float expectedMax,
            int expectedMinIndex, int expectedMaxIndex)
        {
            Vector3 vector = new Vector3(x, y, z);

            //取出
            //vector.Min
            //vector.Max
            //vector.MinIndex
            //vector.MaxIndex
        }

        /*
        [Row(0, 0, 0, 0)]
        [Row(1, 0, 0, 1)]
        [Row(0, 2, 0, 2)]
        [Row(0, 0, 3, 3)]
        [Row(3, 4, 0, 5)]
        [Row(-3, -4, 0, 5)]
        */
        public void NormTest(float x, float y, float z, float expectedNorm)
        {
            Vector3 vector = new Vector3(x, y, z);

            float norm = vector.Norm;

            //Assert.AreEqual<float>(norm, expectedNorm);
            //Assert.AreEqual<float>(norm * norm, vector.Square);
        }

        /*
        [Row(1, 2, 3, 1, 2, 3, true)]
        [Row(-1, -2, -3, -1, -2, -3, true)]
        [Row(-1, -2, -3, -1, -2, 3, false)]
        */
        public void EqualityTest(float x1, float y1, float z1, float x2, float y2, float z2, bool expected)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);

            /*
            Assert.AreEqual<bool>(vector1 == vector2, expected);
            Assert.AreEqual<bool>(vector1 != vector2, !expected);

            Assert.AreEqual<bool>(vector1.Equals(vector2), expected);
            Assert.AreEqual<bool>(vector1.Equals((object)vector2), expected);
            */
        }

        /*
        [Row(1, 2, 3, 4, 5, 6, 5, 7, 9)]
        [Row(1, 2, 3, -4, -5, -6, -3, -3, -3)]
        */
        public void AdditionTest(float x1, float y1, float z1, float x2, float y2, float z2,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector1 + vector2;
            Vector3 result2 = Vector3.Add(vector1, vector2);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 4, 5, 6, 7)]
        [Row(1, 2, 3, -4, -3, -2, -1)]
        */
        public void AdditionWithConstTest(float x, float y, float z, float value,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector + value;
            Vector3 result2 = Vector3.Add(vector, value);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 4, 5, 6, -3, -3, -3)]
        [Row(1, 2, 3, -4, -5, -6, 5, 7, 9)]
        */
        public void SubtractionTest(float x1, float y1, float z1, float x2, float y2, float z2,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector1 - vector2;
            Vector3 result2 = Vector3.Subtract(vector1, vector2);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 4, -3, -2, -1)]
        [Row(1, 2, 3, -4, 5, 6, 7)]
        */
        public void SubtractionWithConstTest(float x, float y, float z, float value,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector - value;
            Vector3 result2 = Vector3.Subtract(vector, value);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 4, 5, 6, 4, 10, 18)]
        [Row(1, 2, 3, -4, -5, -6, -4, -10, -18)]
        */
        public void MultiplicationTest(float x1, float y1, float z1, float x2, float y2, float z2,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector1 * vector2;
            Vector3 result2 = Vector3.Multiply(vector1, vector2);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 4, 4, 8, 12)]
        [Row(1, 2, 3, -4, -4, -8, -12)]
        */
        public void MultiplicationWithConstTest(float x, float y, float z, float value,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector * value;
            Vector3 result2 = Vector3.Multiply(vector, value);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 1, 4, 2, 1, 0.5, 1.5)]
        [Row(1, 2, 3, -1, -4, -2, -1, -0.5, -1.5)]
        */
        public void DivisionTest(float x1, float y1, float z1, float x2, float y2, float z2,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector1 / vector2;
            Vector3 result2 = Vector3.Divide(vector1, vector2);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 2, 3, 2, 0.5, 1, 1.5)]
        [Row(1, 2, 3, -2, -0.5, -1, -1.5)]
        */
        public void DivisionWithConstTest(float x, float y, float z, float value,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result1 = vector / value;
            Vector3 result2 = Vector3.Divide(vector, value);

            //Assert.AreEqual<bool>(expectedResult == result1, true);
            //Assert.AreEqual<bool>(expectedResult == result2, true);
        }

        /*
        [Row(1, 0, 0, 1, 0, 0)]
        [Row(0, 1, 0, 0, 1, 0)]
        [Row(0, 0, 1, 0, 0, 1)]
        [Row(3, 4, 0, 0.6, 0.8, 0)]
        [Row(3, 0, 4, 0.6, 0, 0.8)]
        */
        public void NormalizeTest(float x, float y, float z, float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            float norm1 = vector.Norm;
            float norm2 = vector.Normalize();

            //Assert.AreEqual<bool>(expectedResult == vector, true);
            //Assert.AreEqual<float>(norm1, norm2);
        }

        /*
        [Row(1, 0, 0, 1, 0, 0)]
        [Row(0, 0, 0, 0, 0, 0)]
        [Row(2, 4, 8, 0.5, 0.25, 0.125)]
        [Row(-2, -4, -8, -0.5, -0.25, -0.125)]
        [Row(0.5, 0.25, 0.125, 2, 4, 8)]
        */
        public void InverseTest(float x, float y, float z, float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector = new Vector3(x, y, z);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            Vector3 result = vector.Inverse();

            //Assert.AreEqual<bool>(expectedResult == result, true);
        }

        /*
        [Row(1, 2, 3, 0, 0, 0, 0)]
        [Row(1, 2, 3, 1, 1, 1, 6)]
        [Row(1, 2, 3, 3, 2, 1, 10)]
        [Row(1, 2, 3, -3, -2, -1, -10)]
        */
        public void DotTest(float x1, float y1, float z1, float x2, float y2, float z2, float expectedResult)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);

            //Assert.AreEqual<float>(Vector3.Dot(vector1, vector2), expectedResult);
        }

        /*
        [Row(1, 0, 0, 0, 1, 0, 0, 0, 1)]
        [Row(1, 1, 1, 1, 1, 1, 0, 0, 0)]
        [Row(1, 2, 3, 4, 5, 6, -3, 6, -3)]
        */
        public void CrossTest(float x1, float y1, float z1, float x2, float y2, float z2,
            float expectedX, float expectedY, float expectedZ)
        {
            Vector3 vector1 = new Vector3(x1, y1, z1);
            Vector3 vector2 = new Vector3(x2, y2, z2);
            Vector3 expectedResult = new Vector3(expectedX, expectedY, expectedZ);

            //Assert.AreEqual<bool>(Vector3.Cross(vector1, vector2) == expectedResult, true);
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            //在下面
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

            //Assert.Throws<ArgumentException>( ( ) => dist.GetDistance( p0, q4 ) );

            double result = dist.GetDistance(p0, q0);
            //Assert.AreApproximatelyEqual( result, .2, 0.00001 );

            result = dist.GetDistance(p1, q1);
            //Assert.AreApproximatelyEqual( result, 0.029857, 0.00001 );

            result = dist.GetDistance(p2, q2);
            //Assert.AreEqual( result, 1 );

            result = dist.GetDistance(p3, q3);
            //Assert.AreApproximatelyEqual( result, 0, 0.00001 );

            result = dist.GetDistance(p4, q4);
            //Assert.AreApproximatelyEqual( result, 0.039354, 0.00001 );

            result = dist.GetDistance(p5, q5);
            //Assert.AreApproximatelyEqual( result, 0.031026, 0.00001 );
        }

        public void CosineSimilarityTest()
        {
            CosineSimilarity sim = new CosineSimilarity();

            //Assert.Throws<ArgumentException>( ( ) => sim.GetSimilarityScore( p0, q4 ) );

            double result = sim.GetSimilarityScore(p0, q0);
            //Assert.AreApproximatelyEqual( result, .8, 0.00001 );

            result = sim.GetSimilarityScore(p1, q1);
            //Assert.AreApproximatelyEqual( result, 0.97014, 0.00001 );

            result = sim.GetSimilarityScore(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = sim.GetSimilarityScore(p3, q3);
            //Assert.AreApproximatelyEqual( result, 1, 0.00001 );

            result = sim.GetSimilarityScore(p4, q4);
            //Assert.AreApproximatelyEqual( result, 0.96065, 0.00001 );

            result = sim.GetSimilarityScore(p5, q5);
            //Assert.AreApproximatelyEqual( result, 0.96897, 0.00001 );
        }

        public void EuclideanDistanceTest()
        {
            EuclideanDistance dist = new EuclideanDistance();

            //Assert.Throws<ArgumentException>( ( ) => dist.GetDistance( p0, q4 ) );

            double result = dist.GetDistance(p0, q0);
            //Assert.AreApproximatelyEqual( result, .70711, 0.00001 );

            result = dist.GetDistance(p1, q1);
            //Assert.AreApproximatelyEqual( result, 1.11803, 0.00001 );

            result = dist.GetDistance(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p3, q3);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p4, q4);
            //Assert.AreApproximatelyEqual( result, 2.39792, 0.00001 );

            result = dist.GetDistance(p5, q5);
            //Assert.AreApproximatelyEqual( result, 4.24264, 0.00001 );
        }

        public void EuclideanSimilarityTest()
        {
            EuclideanSimilarity sim = new EuclideanSimilarity();

            //Assert.Throws<ArgumentException>( ( ) => sim.GetSimilarityScore( p0, q4 ) );

            double result = sim.GetSimilarityScore(p0, q0);
            //Assert.AreApproximatelyEqual( result, 0.58578, 0.00001 );

            result = sim.GetSimilarityScore(p1, q1);
            //Assert.AreApproximatelyEqual( result, 0.47213, 0.00001 );

            result = sim.GetSimilarityScore(p2, q2);
            //Assert.AreEqual( result, 1 );

            result = sim.GetSimilarityScore(p3, q3);
            //Assert.AreEqual( result, 1 );

            result = sim.GetSimilarityScore(p4, q4);
            //Assert.AreApproximatelyEqual( result, 0.2943, 0.00001 );

            result = sim.GetSimilarityScore(p5, q5);
            //Assert.AreApproximatelyEqual( result, 0.19074, 0.00001 );
        }

        public void HammingDistanceTest()
        {
            HammingDistance dist = new HammingDistance();

            //Assert.Throws<ArgumentException>( ( ) => dist.GetDistance( p0, q4 ) );

            double result = dist.GetDistance(p0, q0);
            //Assert.AreEqual( result, 2 );

            result = dist.GetDistance(p1, q1);
            //Assert.AreEqual( result, 2 );

            result = dist.GetDistance(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p3, q3);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p4, q4);
            //Assert.AreEqual( result, 4 );

            result = dist.GetDistance(p5, q5);
            //Assert.AreEqual( result, 9 );
        }

        public void JaccardDistanceTest()
        {
            JaccardDistance dist = new JaccardDistance();

            //Assert.Throws<ArgumentException>( ( ) => dist.GetDistance( p0, q4 ) );

            double result = dist.GetDistance(p0, q0);
            //Assert.AreEqual( result, 1 );

            result = dist.GetDistance(p1, q1);
            //Assert.AreEqual( result, 1 );

            result = dist.GetDistance(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p3, q3);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p4, q4);
            //Assert.AreApproximatelyEqual( result, 0.66666, 0.00001 );

            result = dist.GetDistance(p5, q5);
            //Assert.AreApproximatelyEqual( result, 0.9, 0.1 );
        }

        public void ManhattanDistanceTest()
        {
            ManhattanDistance dist = new ManhattanDistance();

            //Assert.Throws<ArgumentException>( ( ) => dist.GetDistance( p0, q4 ) );

            double result = dist.GetDistance(p0, q0);
            //Assert.AreEqual( result, 1 );

            result = dist.GetDistance(p1, q1);
            //Assert.AreEqual( result, 1.5 );

            result = dist.GetDistance(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p3, q3);
            //Assert.AreEqual( result, 0 );

            result = dist.GetDistance(p4, q4);
            //Assert.AreEqual( result, 4.5 );

            result = dist.GetDistance(p5, q5);
            //Assert.AreEqual( result, 12 );
        }

        public void PearsonCorrelationTest()
        {
            PearsonCorrelation sim = new PearsonCorrelation();

            //Assert.Throws<ArgumentException>( ( ) => sim.GetSimilarityScore( p0, q4 ) );

            double result = sim.GetSimilarityScore(p0, q0);
            //Assert.AreEqual( result, -1 );

            result = sim.GetSimilarityScore(p1, q1);
            //Assert.AreEqual( result, 1 );

            result = sim.GetSimilarityScore(p2, q2);
            //Assert.AreEqual( result, 0 );

            result = sim.GetSimilarityScore(p3, q3);
            //Assert.AreEqual( result, 0 );

            result = sim.GetSimilarityScore(p4, q4);
            //Assert.AreApproximatelyEqual( result, 0.396059, 0.00001 );

            result = sim.GetSimilarityScore(p5, q5);
            //Assert.AreApproximatelyEqual( result, 0.85470, 0.00001 );
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            //在下面

        }

        /*
        [Row( 0, 0, 10, 0, 100, 0, 0 )]
        [Row( 0, 0, 10, 10, 100, 100, 0 )]
        [Row( 0, 0, 10, 0, 0, 100, 90 )]
        [Row( 0, 0, 10, 0, 100, 100, 45 )]
        [Row( 0, 0, 10, 10, -100, 100, 90 )]
        [Row( 0, 0, 10, 0, -100, 100, 135 )]
        [Row( 0, 0, 10, 0, -100, 0, 180 )]
        [Row( 0, 0, 10, 0, -100, -100, 135 )]
        */
        public void GetAngleBetweenVectorsTest(int sx, int sy, int ex1, int ey1, int ex2, int ey2, float expectedAngle)
        {
            IntPoint startPoint = new IntPoint(sx, sy);
            IntPoint vector1end = new IntPoint(ex1, ey1);
            IntPoint vector2end = new IntPoint(ex2, ey2);

            float angle = GeometryTools.GetAngleBetweenVectors(startPoint, vector1end, vector2end);

            //Assert.AreApproximatelyEqual<float, float>( expectedAngle,  angle, 0.00001f );
        }

        /*
        [Row( 0, 0, 10, 0, 0, 10, 10, 10, 0 )]
        [Row( 0, 0, 10, 0, 0, 10, 0, 20, 90 )]
        [Row( 0, 0, 10, 0, 1, 1, 10, 10, 45 )]
        [Row( 0, 0, 10, 0, 1, 1, -8, 10, 45 )]
        [Row( 0, 0, 10, 10, 0, 0, -100, 100, 90 )]
        */
        public void GetAngleBetweenLinesTest(int sx1, int sy1, int ex1, int ey1, int sx2, int sy2, int ex2, int ey2, float expectedAngle)
        {
            IntPoint line1start = new IntPoint(sx1, sy1);
            IntPoint line1end = new IntPoint(ex1, ey1);
            IntPoint line2start = new IntPoint(sx2, sy2);
            IntPoint line2end = new IntPoint(ex2, ey2);

            float angle = GeometryTools.GetAngleBetweenLines(line1start, line1end, line2start, line2end);

            //Assert.AreApproximatelyEqual<float, float>( expectedAngle, angle, 0.00001f );
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
            //在下面
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

            //在下面
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
                idealCicle.Add(new IntPoint(
                    (int)(radius * System.Math.Cos(angle)),
                    (int)(radius * System.Math.Sin(angle))));

                // add a bit distortion for distorred cirlce
                double distorredRadius = radius + rand.Next(7) - 3;

                distorredCircle.Add(new IntPoint(
                    (int)(distorredRadius * System.Math.Cos(angle)),
                    (int)(distorredRadius * System.Math.Sin(angle))));
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
            //Assert.AreEqual( true, shapeChecker.IsCircle( idealCicle ) );
            //Assert.AreEqual( true, shapeChecker.IsCircle( distorredCircle ) );

            //Assert.AreEqual( false, shapeChecker.IsCircle( square1 ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( square2 ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( square3 ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( rectangle ) );

            //Assert.AreEqual( false, shapeChecker.IsCircle( triangle1 ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( equilateralTriangle ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( isoscelesTriangle ) );
            //Assert.AreEqual( false, shapeChecker.IsCircle( rectangledTriangle ) );
        }

        public void IsQuadrilateralTest()
        {
            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( square1 ) );
            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( square2 ) );
            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( square3 ) );
            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( rectangle ) );

            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( idealCicle ) );
            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( distorredCircle ) );

            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( triangle1 ) );
            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( equilateralTriangle ) );
            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( isoscelesTriangle ) );
            //Assert.AreEqual( false, shapeChecker.IsQuadrilateral( rectangledTriangle ) );
        }

        public void CheckQuadrilateralCornersTest()
        {
            List<IntPoint> corners;

            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( square1, out corners ) );
            //Assert.AreEqual( 4, corners.Count );
            //Assert.AreEqual( true, CompareShape( corners, square1Test ) );

            //Assert.AreEqual( true, shapeChecker.IsQuadrilateral( square2, out corners ) );
            //Assert.AreEqual( 4, corners.Count );
            //Assert.AreEqual( true, CompareShape( corners, square2Test ) );
        }

        public void IsTriangleTest()
        {
            //Assert.AreEqual( true, shapeChecker.IsTriangle( triangle1 ) );
            //Assert.AreEqual( true, shapeChecker.IsTriangle( equilateralTriangle ) );
            //Assert.AreEqual( true, shapeChecker.IsTriangle( isoscelesTriangle ) );
            //Assert.AreEqual( true, shapeChecker.IsTriangle( rectangledTriangle ) );

            //Assert.AreEqual( false, shapeChecker.IsTriangle( idealCicle ) );
            //Assert.AreEqual( false, shapeChecker.IsTriangle( distorredCircle ) );

            //Assert.AreEqual( false, shapeChecker.IsTriangle( square1 ) );
            //Assert.AreEqual( false, shapeChecker.IsTriangle( square2 ) );
            //Assert.AreEqual( false, shapeChecker.IsTriangle( square3 ) );
            //Assert.AreEqual( false, shapeChecker.IsTriangle( rectangle ) );
        }

        public void IsConvexPolygon()
        {
            List<IntPoint> corners;

            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( triangle1, out corners ) );
            //Assert.AreEqual( 3, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( equilateralTriangle, out corners ) );
            //Assert.AreEqual( 3, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( isoscelesTriangle, out corners ) );
            //Assert.AreEqual( 3, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( rectangledTriangle, out corners ) );
            //Assert.AreEqual( 3, corners.Count );

            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( square1, out corners ) );
            //Assert.AreEqual( 4, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( square2, out corners ) );
            //Assert.AreEqual( 4, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( square3, out corners ) );
            //Assert.AreEqual( 4, corners.Count );
            //Assert.AreEqual( true, shapeChecker.IsConvexPolygon( rectangle, out corners ) );
            //Assert.AreEqual( 4, corners.Count );

            //Assert.AreEqual( false, shapeChecker.IsConvexPolygon( idealCicle, out corners ) );
            //Assert.AreEqual( false, shapeChecker.IsConvexPolygon( distorredCircle, out corners ) );
        }

        public void CheckShapeTypeTest()
        {
            //Assert.AreEqual( ShapeType.Circle, shapeChecker.CheckShapeType( idealCicle ) );
            //Assert.AreEqual( ShapeType.Circle, shapeChecker.CheckShapeType( distorredCircle ) );

            //Assert.AreEqual( ShapeType.Quadrilateral, shapeChecker.CheckShapeType( square1 ) );
            //Assert.AreEqual( ShapeType.Quadrilateral, shapeChecker.CheckShapeType( square2 ) );
            //Assert.AreEqual( ShapeType.Quadrilateral, shapeChecker.CheckShapeType( square3 ) );
            //Assert.AreEqual( ShapeType.Quadrilateral, shapeChecker.CheckShapeType( rectangle ) );

            //Assert.AreEqual( ShapeType.Triangle, shapeChecker.CheckShapeType( triangle1 ) );
            //Assert.AreEqual( ShapeType.Triangle, shapeChecker.CheckShapeType( equilateralTriangle ) );
            //Assert.AreEqual( ShapeType.Triangle, shapeChecker.CheckShapeType( isoscelesTriangle ) );
            //Assert.AreEqual( ShapeType.Triangle, shapeChecker.CheckShapeType( rectangledTriangle ) );
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

            //在下面
        }


        /*
        [Row( 0, 0, 10, 0, 10 )]
        [Row( 0, 0, 0, 10, 10 )]
        [Row( 0, 0, 3, 4, 5 )]
        [Row( 0, 0, -3, 4, 5 )]
        [Row( 0, 0, -3, -4, 5 )]
        */
        public void LengthTest(float sx, float sy, float ex, float ey, float expectedResult)
        {
            LineSegment segment = new LineSegment(new AForge.Point(sx, sy), new AForge.Point(ex, ey));

            //Assert.AreEqual( expectedResult, segment.Length );
        }

        /*
        [Row( 0, 0, 5, 0, 8, 0, 5 )]
        [Row( 6, 2.5, 5, 0, 8, 0, 2.5 )]
        [Row( 2.5, 6, 0, 5, 0, 8, 2.5 )]
        [Row( 9, 0, 5, 0, 8, 0, 1 )]
        [Row( 3, 4, 0, 0, -10, 0, 5 )]
        */
        public void DistanceToPointTest(float x, float y, float x1, float y1, float x2, float y2, float expectedDistance)
        {
            AForge.Point pt = new AForge.Point(x, y);
            AForge.Point pt1 = new AForge.Point(x1, y1);
            AForge.Point pt2 = new AForge.Point(x2, y2);
            LineSegment segment = new LineSegment(pt1, pt2);

            //Assert.AreEqual( expectedDistance, segment.DistanceToPoint( pt ) );
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

            //在下面
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
//---------------  # 15個


/*  可搬出

*/

