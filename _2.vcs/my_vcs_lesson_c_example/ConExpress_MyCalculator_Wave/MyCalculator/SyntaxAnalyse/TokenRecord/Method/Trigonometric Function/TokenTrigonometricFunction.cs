using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public abstract class TokenTrigonometricFunction : TokenMethod
    {
        public TokenTrigonometricFunction(int Index, int Length)
            : base(Index, Length)
        { }

        protected override void SetChildCount()
        {
            this.m_ChildCount = 1;
        }

        public abstract override void Execute();
    }
}
