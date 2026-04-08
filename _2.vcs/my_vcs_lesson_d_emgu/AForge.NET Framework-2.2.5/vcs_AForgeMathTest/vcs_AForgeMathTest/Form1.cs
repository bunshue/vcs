using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using AForge.Math;

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
            this.Text = "vcs_AForgeMathTest";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button0_Click(object sender, EventArgs e)
        {
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

            /*
            Vector3 row0 = new Vector3(1, 2, 3);
            Vector3 row1 = new Vector3(4, 5, 6);
            Vector3 row2 = new Vector3(7, 8, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromRows(row0, row1, row2);
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試 ToArray()\n";

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
                richTextBox1.Text += array[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //CreateFromRowsTest
            Vector3 row0 = new Vector3(1, 2, 3);
            Vector3 row1 = new Vector3(4, 5, 6);
            Vector3 row2 = new Vector3(7, 8, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromRows(row0, row1, row2);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {

            }

            //Assert.AreEqual<Vector3>(row0, matrix.GetRow(0));
            //Assert.AreEqual<Vector3>(row1, matrix.GetRow(1));
            //Assert.AreEqual<Vector3>(row2, matrix.GetRow(2));

            //matrix.GetRow(-1);

            //matrix.GetRow(3);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //CreateFromColumnsTest
            Vector3 column0 = new Vector3(1, 4, 7);
            Vector3 column1 = new Vector3(2, 5, 8);
            Vector3 column2 = new Vector3(3, 6, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromColumns(column0, column1, column2);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
            }

            //Assert.AreEqual<Vector3>(column0, matrix.GetColumn(0));
            //Assert.AreEqual<Vector3>(column1, matrix.GetColumn(1));
            //Assert.AreEqual<Vector3>(column2, matrix.GetColumn(2));

            //matrix.GetColumn(-1);
            //matrix.GetColumn(3);
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
