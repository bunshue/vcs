using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenAtan2 : TokenTrigonometricFunction
    {
        public TokenAtan2(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 2;
        }

        public override void Execute()
        {
            this.CheckChildCount("Atan2����������Ԫ���������Ϸ�");

            TokenRecord TokenFirst = this.ChildList[0];
            TokenRecord TokenSecond = this.ChildList[1];
            TokenFirst.Execute();
            TokenSecond.Execute();

            this.TokenValue = Math.Round(Math.Atan2(TokenFirst.ChangeTokenToDouble("Atan2�����Ĳ�������������"), TokenSecond.ChangeTokenToDouble("Atan2�����Ĳ�������������")) * 180 / Math.PI, 10);
        }
    }
}
