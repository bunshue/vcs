using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenMethod : TokenRecord
    {
        public TokenMethod(int Index, int Length)
            : base(Index, Length)
        {
            this.TokenValueType = typeof(double);
        }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 2;
        }

        protected override void SetPriority()
        {
            this.m_Priority = 4;
        }

        public abstract override void Execute();
    }
}