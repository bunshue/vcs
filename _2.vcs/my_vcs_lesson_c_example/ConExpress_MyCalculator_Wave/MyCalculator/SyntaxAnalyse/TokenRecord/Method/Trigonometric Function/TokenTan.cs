using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenTan : TokenTrigonometricFunction
    {
        public TokenTan(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("tan方法的运算元素数量不合法");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Tan(TokenChild.ChangeTokenToDouble("tan方法的操作数不是数字") / 180 * Math.PI), 10);
        }
    }
}
