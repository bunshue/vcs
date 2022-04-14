using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenPow : TokenArithmeticMethod
    {
        public TokenPow(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("幂运算的操作数数量不合法");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = Math.Pow(TokenFirst.ChangeTokenToDouble("幂运算的运算元素不是数值"), TokenSecond.ChangeTokenToDouble("幂运算的运算元素不是数值"));
        }
    }
}
