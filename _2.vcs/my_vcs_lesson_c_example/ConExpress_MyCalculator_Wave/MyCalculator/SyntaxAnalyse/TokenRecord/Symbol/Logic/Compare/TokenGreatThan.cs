using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenGreatThan : TokenCompare
    {
        public TokenGreatThan(int Index, int Length)
            : base(Index, Length)
        {
        }

        protected override void SetChildCountError()
        {
            this.m_ChildCountErrorInformation = "大于运算的元素数量不合法";
        }

        public override void Execute()
        {
            base.Execute();
            this.TokenValue = (base.Compare() > 0);
        }

    }
}
