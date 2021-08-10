using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ParallelTest2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int matrixSize = 250;
            int runs = 10;
            int tests = 5;

            double test1time = 0;
            double test2time = 0;

            richTextBox1.Text += "Starting test with " + AForge.Parallel.ThreadsCount + " threads" + "\n";

            richTextBox1.Text += "不使用平行運算" + "\t\t|\t\t" + "使用平行運算" + "\t\t|\n";

            Application.DoEvents();

            // allocate matrixes for all tests
            double[,] a = new double[matrixSize, matrixSize];
            double[,] b = new double[matrixSize, matrixSize];
            double[,] c1 = new double[matrixSize, matrixSize];
            double[,] c2 = new double[matrixSize, matrixSize];

            Random rand = new Random();

            // fill source matrixes with random numbers
            for (int i = 0; i < matrixSize; i++)
            {
                for (int j = 0; j < matrixSize; j++)
                {
                    a[i, j] = rand.NextDouble();
                    b[i, j] = rand.NextDouble();
                }
            }

            // run specified number of tests
            for (int test = 0; test < tests; test++)
            {
                // test 1
                DateTime start = DateTime.Now;

                for (int run = 0; run < runs; run++)
                {
                    Test1(a, b, c1);
                }

                DateTime end = DateTime.Now;
                TimeSpan span = end - start;

                richTextBox1.Text += span.TotalMilliseconds.ToString("F3") + "\t\t\t|\t\t";
                test1time += span.TotalMilliseconds;

                // test 2
                start = DateTime.Now;

                for (int run = 0; run < runs; run++)
                {
                    Test2(a, b, c2);
                }

                end = DateTime.Now;
                span = end - start;

                richTextBox1.Text += span.TotalMilliseconds.ToString("F3") + "\t\t\t|\t\t";
                test2time += span.TotalMilliseconds;

                richTextBox1.Text += "\n";
                Application.DoEvents();
            }

            // provide average performance
            test1time /= tests;
            test2time /= tests;

            richTextBox1.Text += "---------------------- AVG ----------------------\n";
            richTextBox1.Text += test1time.ToString("F3") + "\t\t\t|\t\t" + test2time.ToString("F3") + "\t\t\t|\n";
            richTextBox1.Text += "Done\n";
            Application.DoEvents();
        }

        // Test #1 - multiply 2 square matrixes without using parallel computations
        private static void Test1(double[,] a, double[,] b, double[,] c)
        {
            int s = a.GetLength(0);

            for (int i = 0; i < s; i++)
            {
                for (int j = 0; j < s; j++)
                {
                    double v = 0;

                    for (int k = 0; k < s; k++)
                    {
                        v += a[i, k] * b[k, j];
                    }
                    c[i, j] = v;
                }
            }
        }

        // Test #2 - multiply 2 square matrixes using parallel computations
        private static void Test2(double[,] a, double[,] b, double[,] c)
        {
            int s = a.GetLength(0);

            AForge.Parallel.For(0, s, delegate(int i)
            {
                for (int j = 0; j < s; j++)
                {
                    double v = 0;

                    for (int k = 0; k < s; k++)
                    {
                        v += a[i, k] * b[k, j];
                    }

                    c[i, j] = v;
                }
            }
            );
        }
    }
}

