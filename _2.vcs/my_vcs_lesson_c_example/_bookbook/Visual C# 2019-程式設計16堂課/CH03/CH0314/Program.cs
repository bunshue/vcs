using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0314
{
    class Program
    {
        //宣告列舉型別
        enum EmployeTurnout : sbyte
        {
            unknown = -3, leave = -1, turnout = 0,
            fieldtrip = 2, dayoff = 4
        };

        static void Main(string[] args)
        {
            //宣告列舉成員
            EmployeTurnout Mary, Eric, Charles;
            sbyte state1, state2, state3;

            //存取列舉成員並輸出常數值
            Mary = EmployeTurnout.fieldtrip;
            state1 = (sbyte)Mary;
            WriteLine($"Mary   出外洽公({Mary} = {state1})");

            Eric = EmployeTurnout.leave;
            state2 = (sbyte)Eric;
            WriteLine($"Eric   休假中({Eric} = {state2})");

            Charles = EmployeTurnout.turnout;
            state3 = (sbyte)Charles;
            WriteLine($"Charles 出席({Charles} = {state3})");

            ReadKey();
        }
    }
}
