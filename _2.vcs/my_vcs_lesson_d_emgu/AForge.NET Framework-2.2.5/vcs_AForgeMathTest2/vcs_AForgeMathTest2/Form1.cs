using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Math;

namespace vcs_AForgeMathTest2
{
    public partial class Form1 : Form
    {
        private const float Epsilon = 0.000001f;
        private Matrix4x4 a1 = new Matrix4x4();
        private Matrix4x4 a2 = new Matrix4x4();

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
            
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(800, 750);
            this.Text = "vcs_AForgeMathTest2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public void Matrix4x4Test()
        {
            // prepare 1st argument
            a1.V00 = 1;
            a1.V01 = 2;
            a1.V02 = 3;
            a1.V03 = 4;

            a1.V10 = 4;
            a1.V11 = 3;
            a1.V12 = 2;
            a1.V13 = 1;

            a1.V20 = 3;
            a1.V21 = 1;
            a1.V22 = 4;
            a1.V23 = 2;

            a1.V30 = 2;
            a1.V31 = 4;
            a1.V32 = 1;
            a1.V33 = 3;

            // prepare 2nd argument
            a2.V00 = 2;
            a2.V01 = 1;
            a2.V02 = 4;
            a2.V03 = 3;

            a2.V10 = 4;
            a2.V11 = 2;
            a2.V12 = 3;
            a2.V13 = 1;

            a2.V20 = 3;
            a2.V21 = 4;
            a2.V22 = 1;
            a2.V23 = 2;

            a2.V30 = 1;
            a2.V31 = 3;
            a2.V32 = 2;
            a2.V33 = 4;
        }

        public void ToArrayTest()
        {
            Matrix4x4 matrix = new Matrix4x4();

            matrix.V00 = 1;
            matrix.V01 = 2;
            matrix.V02 = 3;
            matrix.V03 = 4;

            matrix.V10 = 5;
            matrix.V11 = 6;
            matrix.V12 = 7;
            matrix.V13 = 8;

            matrix.V20 = 9;
            matrix.V21 = 10;
            matrix.V22 = 11;
            matrix.V23 = 12;

            matrix.V30 = 13;
            matrix.V31 = 14;
            matrix.V32 = 15;
            matrix.V33 = 16;

            float[] array = matrix.ToArray();

            for (int i = 0; i < 16; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }
        }

        public void CreateFromRowsTest()
        {
            Vector4 row0 = new Vector4(1, 2, 3, 4);
            Vector4 row1 = new Vector4(5, 6, 7, 8);
            Vector4 row2 = new Vector4(9, 10, 11, 12);
            Vector4 row3 = new Vector4(13, 14, 15, 16);
            Matrix4x4 matrix = Matrix4x4.CreateFromRows(row0, row1, row2, row3);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 16; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }

            //Assert.AreEqual<Vector4>( row0, matrix.GetRow( 0 ) );
            //Assert.AreEqual<Vector4>( row1, matrix.GetRow( 1 ) );
            //Assert.AreEqual<Vector4>( row2, matrix.GetRow( 2 ) );
            //Assert.AreEqual<Vector4>( row3, matrix.GetRow( 3 ) );

            matrix.GetRow(-1);
            matrix.GetRow(4);
        }

        public void CreateFromColumnsTest()
        {
            Vector4 column0 = new Vector4(1, 5, 9, 13);
            Vector4 column1 = new Vector4(2, 6, 10, 14);
            Vector4 column2 = new Vector4(3, 7, 11, 15);
            Vector4 column3 = new Vector4(4, 8, 12, 16);
            Matrix4x4 matrix = Matrix4x4.CreateFromColumns(column0, column1, column2, column3);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 16; i++)
            {
                //Assert.AreEqual<float>( array[i], (float) ( i + 1 ) );
            }

            //Assert.AreEqual<Vector4>( column0, matrix.GetColumn( 0 ) );
            //Assert.AreEqual<Vector4>( column1, matrix.GetColumn( 1 ) );
            //Assert.AreEqual<Vector4>( column2, matrix.GetColumn( 2 ) );
            //Assert.AreEqual<Vector4>( column3, matrix.GetColumn( 3 ) );

            matrix.GetColumn(-1);
            matrix.GetColumn(4);
        }

        public void CreateRotationYTest(float angle)
        {
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix4x4 matrix = Matrix4x4.CreateRotationY(radians);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[16]
            {
                cos, 0, sin, 0,
                0, 1, 0, 0,
                -sin, 0, cos, 0,
                0, 0, 0, 1
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateRotationXTest(float angle)
        {
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix4x4 matrix = Matrix4x4.CreateRotationX(radians);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[16]
            {
                1, 0, 0, 0,
                0, cos, -sin, 0,
                0, sin, cos, 0,
                0, 0, 0, 1
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateRotationZTest(float angle)
        {
            float radians = (float)(angle * System.Math.PI / 180);
            Matrix4x4 matrix = Matrix4x4.CreateRotationZ(radians);

            float sin = (float)System.Math.Sin(radians);
            float cos = (float)System.Math.Cos(radians);

            float[] expectedArray = new float[16]
            {
                cos, -sin, 0, 0,
                sin, cos, 0, 0,
                0, 0, 1, 0,
                0, 0, 0, 1,
            };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void CreateFromYawPitchRollTest(float yaw, float pitch, float roll)
        {
            float radiansYaw = (float)(yaw * System.Math.PI / 180);
            float radiansPitch = (float)(pitch * System.Math.PI / 180);
            float radiansRoll = (float)(roll * System.Math.PI / 180);

            Matrix4x4 matrix = Matrix4x4.CreateFromYawPitchRoll(radiansYaw, radiansPitch, radiansRoll);

            Matrix4x4 xMatrix = Matrix4x4.CreateRotationX(radiansPitch);
            Matrix4x4 yMatrix = Matrix4x4.CreateRotationY(radiansYaw);
            Matrix4x4 zMatrix = Matrix4x4.CreateRotationZ(radiansRoll);

            Matrix4x4 rotationMatrix = (yMatrix * xMatrix) * zMatrix;

            CompareMatrixWithArray(matrix, rotationMatrix.ToArray());
        }

        public void ExtractYawPitchRollTest(float yaw, float pitch, float roll)
        {
            float radiansYaw = (float)(yaw * System.Math.PI / 180);
            float radiansPitch = (float)(pitch * System.Math.PI / 180);
            float radiansRoll = (float)(roll * System.Math.PI / 180);

            Matrix4x4 matrix = Matrix4x4.CreateFromYawPitchRoll(radiansYaw, radiansPitch, radiansRoll);

            float extractedYaw;
            float extractedPitch;
            float extractedRoll;

            matrix.ExtractYawPitchRoll(out extractedYaw, out extractedPitch, out extractedRoll);

            //Assert.AreApproximatelyEqual<float, float>( radiansYaw,   extractedYaw,   Epsilon );
            //Assert.AreApproximatelyEqual<float, float>( radiansPitch, extractedPitch, Epsilon );
            //Assert.AreApproximatelyEqual<float, float>( radiansRoll,  extractedRoll,  Epsilon );
        }

        public void CreateDiagonalTest(float v00, float v11, float v22, float v33)
        {
            Vector4 diagonal = new Vector4(v00, v11, v22, v33);
            Matrix4x4 matrix = Matrix4x4.CreateDiagonal(diagonal);

            float[] expectedArray = new float[16] { v00, 0, 0, 0, 0, v11, 0, 0, 0, 0, v22, 0, 0, 0, 0, v33 };

            CompareMatrixWithArray(matrix, expectedArray);
        }

        public void AddMatricesTest()
        {
            Matrix4x4 expectedResult = new Matrix4x4();

            expectedResult.V00 = 3;
            expectedResult.V01 = 3;
            expectedResult.V02 = 7;
            expectedResult.V03 = 7;

            expectedResult.V10 = 8;
            expectedResult.V11 = 5;
            expectedResult.V12 = 5;
            expectedResult.V13 = 2;

            expectedResult.V20 = 6;
            expectedResult.V21 = 5;
            expectedResult.V22 = 5;
            expectedResult.V23 = 4;

            expectedResult.V30 = 3;
            expectedResult.V31 = 7;
            expectedResult.V32 = 3;
            expectedResult.V33 = 7;

            Matrix4x4 result = a1 + a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
        }

        public void SubtractMatricesTest()
        {
            Matrix4x4 expectedResult = new Matrix4x4();

            expectedResult.V00 = -1;
            expectedResult.V01 = 1;
            expectedResult.V02 = -1;
            expectedResult.V03 = 1;

            expectedResult.V10 = 0;
            expectedResult.V11 = 1;
            expectedResult.V12 = -1;
            expectedResult.V13 = 0;

            expectedResult.V20 = 0;
            expectedResult.V21 = -3;
            expectedResult.V22 = 3;
            expectedResult.V23 = 0;

            expectedResult.V30 = 1;
            expectedResult.V31 = 1;
            expectedResult.V32 = -1;
            expectedResult.V33 = -1;

            Matrix4x4 result = a1 - a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
        }

        public void MultiplyMatricesTest()
        {
            Matrix4x4 expectedResult = new Matrix4x4();

            expectedResult.V00 = 23;
            expectedResult.V01 = 29;
            expectedResult.V02 = 21;
            expectedResult.V03 = 27;

            expectedResult.V10 = 27;
            expectedResult.V11 = 21;
            expectedResult.V12 = 29;
            expectedResult.V13 = 23;

            expectedResult.V20 = 24;
            expectedResult.V21 = 27;
            expectedResult.V22 = 23;
            expectedResult.V23 = 26;

            expectedResult.V30 = 26;
            expectedResult.V31 = 23;
            expectedResult.V32 = 27;
            expectedResult.V33 = 24;

            Matrix4x4 result = a1 * a2;

            //Assert.AreEqual<bool>( true, ApproximateEquals( result, expectedResult ) );
        }

        private void CompareMatrixWithArray(Matrix4x4 matrix, float[] array)
        {
            float[] matrixArray = matrix.ToArray();

            for (int i = 0; i < 16; i++)
            {
                //Assert.AreEqual<float>( matrixArray[i], array[i] );
            }
        }

        private bool ApproximateEquals(Matrix4x4 matrix1, Matrix4x4 matrix2)
        {
            // TODO: better algorithm should be put into the framework actually
            return (
                (System.Math.Abs(matrix1.V00 - matrix2.V00) <= Epsilon) &&
                (System.Math.Abs(matrix1.V01 - matrix2.V01) <= Epsilon) &&
                (System.Math.Abs(matrix1.V02 - matrix2.V02) <= Epsilon) &&
                (System.Math.Abs(matrix1.V03 - matrix2.V03) <= Epsilon) &&

                (System.Math.Abs(matrix1.V10 - matrix2.V10) <= Epsilon) &&
                (System.Math.Abs(matrix1.V11 - matrix2.V11) <= Epsilon) &&
                (System.Math.Abs(matrix1.V12 - matrix2.V12) <= Epsilon) &&
                (System.Math.Abs(matrix1.V13 - matrix2.V13) <= Epsilon) &&

                (System.Math.Abs(matrix1.V20 - matrix2.V20) <= Epsilon) &&
                (System.Math.Abs(matrix1.V21 - matrix2.V21) <= Epsilon) &&
                (System.Math.Abs(matrix1.V22 - matrix2.V22) <= Epsilon) &&
                (System.Math.Abs(matrix1.V23 - matrix2.V23) <= Epsilon) &&

                (System.Math.Abs(matrix1.V30 - matrix2.V30) <= Epsilon) &&
                (System.Math.Abs(matrix1.V31 - matrix2.V31) <= Epsilon) &&
                (System.Math.Abs(matrix1.V32 - matrix2.V32) <= Epsilon) &&
                (System.Math.Abs(matrix1.V33 - matrix2.V33) <= Epsilon)
            );
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Matrix4x4Test();
            ToArrayTest();

            CreateFromRowsTest();
            CreateFromColumnsTest();

            float angle = 30f;

            CreateRotationXTest(angle);
            CreateRotationYTest(angle);
            CreateRotationZTest(angle);

            float yaw = -30;
            float pitch = -60;
            float roll = -90;
            CreateFromYawPitchRollTest(yaw, pitch, roll);
            ExtractYawPitchRollTest(yaw, pitch, roll);

            float v00 = -1;
            float v11 = -2;
            float v22 = -3;
            float v33 = -4;
            CreateDiagonalTest(v00, v11, v22, v33);

            //matrix.Determinant 3X3矩陣的determinant

            //反矩陣 matrix.Inverse()
            //Matrix3x3 inverse = matrix.Inverse();

            //單一矩陣
            //Matrix3x3 identity = matrix * inverse;
            //Matrix3x3.Identity


            //矩陣相加/減/乘
            AddMatricesTest();
            SubtractMatricesTest();
            MultiplyMatricesTest();


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
    }
}
