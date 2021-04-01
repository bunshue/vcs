using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace InfraClient
{
  static class Program
  {
    /// <summary>
    /// The main entry point for the application.
    /// </summary>
    [MTAThread]
    static void Main()
    {
      Application.Run(new Form1());
    }
  }
}