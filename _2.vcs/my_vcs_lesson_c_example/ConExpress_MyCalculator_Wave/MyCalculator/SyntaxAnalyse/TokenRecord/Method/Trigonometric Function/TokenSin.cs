using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenSin : TokenTrigonometricFunction
    {
        public TokenSin(int Index, int Length)
            : base(Index, Length)
        { }

        public override void Execute()
        {
            this.CheckChildCount("sin����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Sin(TokenChild.ChangeTokenToDouble("sin�����Ĳ�������������") / 180 * Math.PI), 10);
        }
    }
}
