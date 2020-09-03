using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

/*
DLL檔案必須與執行檔同層目錄，

假設該DLL名為TargetDLL.dll

在C#程式中引用方式如下 ↓

// 首先
using System.Runtime.InteropServices;

// 在class中加入下方
[DllImport("TargrtDLL.dll")]
private static extern bool function1(int args1, int args2);

其中傳入傳出參數型別依照需求可自訂，

每個函式前方都必須加入[DllImport(“TargrtDLL.dll”)]，

如此一來就能在該專案中使用該DLL中之函式。
*/


namespace 使用unmanaged_DLL
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
    }
}
