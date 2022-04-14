using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenLessThan : TokenCompare
    {
        public TokenLessThan(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "С�������Ԫ���������Ϸ�";
        }

        public override void Execute()
        {
            base.Execute();
            this.TokenValue = (base.Compare() < 0);
        }
    }
}
