using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAsin : TokenTrigonometricFunction
    {
        public TokenAsin(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("Asin����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Asin(TokenChild.ChangeTokenToDouble("Asin�����Ĳ�������������")) * 180 / Math.PI, 10);
        }
    }
}
