using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMin : TokenArithmeticMethod
    {
        public TokenMin(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// ����¼�����
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (this.ChildList.Count < 2)
            {
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        private const string c_IsNotNumber = "Min�����Ĳ�������������";
        public override void Execute()
        {
            this.CheckChildCount("Min����������Ԫ���������Ϸ�");

            List<double> myList = new List<double>();
            foreach (TokenRecord item in this.ChildList)
            {
                item.Execute();
                myList.Add(item.ChangeTokenToDouble(c_IsNotNumber));
            }
            myList.Sort();

            this.TokenValue = myList[0];
        }
    }
}