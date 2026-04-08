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

            pictureBox1.Size = new Size(500, 300);
            pictureBox1.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.Size = new Size(500, 690-310);
            richTextBox1.Location = new System.Drawing.Point(x_st + dx * 2, y_st + dy * 0+310);
            bt_clear.Location = new System.Drawing.Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(960, 750);
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

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}
