using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Thread4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Start threads with different priorities.
        private void button1_Click(object sender, EventArgs e)
        {
            int num_low = 4;
            for (int i = 0; i < num_low; i++)
            {
                MakeThread("Low" + i.ToString(), ThreadPriority.BelowNormal);
            }

            int num_normal = 4;
            for (int i = 0; i < num_normal; i++)
            {
                MakeThread("Normal" + i.ToString(), ThreadPriority.Normal);
            }

            int num_high = 4;
            for (int i = 0; i < num_high; i++)
            {
                MakeThread("High" + i.ToString(), ThreadPriority.AboveNormal);
            }
        }

        // Make a thread with the indicated priority.
        private void MakeThread(string thread_name, ThreadPriority thread_priority)
        {
            richTextBox1.Text += "Make Thread " + thread_name + ", priority " + thread_priority.ToString() + "\n";
            Application.DoEvents();

            // Initialize the thread.
            Counter new_counter = new Counter(thread_name);
            Thread thread = new Thread(new_counter.Run);
            thread.Priority = thread_priority;
            thread.IsBackground = true;
            thread.Name = thread_name;

            // Start the thread.
            thread.Start();
        }

    }

    class Counter
    {
        // This counter's number.
        public string Name;

        // Initializing constructor.
        public Counter(string name)
        {
            Name = name;
        }

        // Count off 10 half second intervals in the Output window.
        public void Run()
        {
            for (int i = 1; i <= 10; i++)
            {
                // Display the next message.
                Console.WriteLine(Name + " " + i);

                // See when we should display the next message.
                DateTime next_time = DateTime.Now.AddSeconds(0.5);

                // Waste half a second. We don't sleep or call
                // DoEvents so we don't give up control of the CPU.
                while (DateTime.Now < next_time)
                {
                    // Wait a bit.
                }
            }
        }
    }

}
