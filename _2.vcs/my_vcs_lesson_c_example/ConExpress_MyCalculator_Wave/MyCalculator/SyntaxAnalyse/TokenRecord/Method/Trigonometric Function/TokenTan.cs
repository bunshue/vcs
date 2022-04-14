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
            this.CheckChildCount("tan����������Ԫ���������Ϸ�");

            TokenRecord TokenChild = this.ChildList[0];
            TokenChild.Execute();

            this.TokenValue = Math.Round(Math.Tan(TokenChild.ChangeTokenToDouble("tan�����Ĳ�������������") / 180 * Math.PI), 10);
        }
    }
}
