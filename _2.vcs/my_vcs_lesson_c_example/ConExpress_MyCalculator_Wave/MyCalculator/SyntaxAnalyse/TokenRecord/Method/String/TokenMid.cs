using System;
using System.Collections.Generic;
using System.Text;

namespace ConExpress.Calculator
{
    public class TokenMid : TokenStringMethod
    {
        public TokenMid(int Index, int Length)
            : base(Index, Length)
        { }

        /// <summary>
        /// ����¼�����
        /// </summary>
        /// <returns></returns>
        public new void CheckChildCount(string ErrorInformation)
        {
            if (!(this.ChildList.Count == 2 || this.ChildList.Count == 3))
            {
                //throw new ArgumentException(string.Format("�﷨������{0}��{1}��", this.Index.ToString(), ErrorInformation));
                throw new SyntaxException(this.Index, this.Length, ErrorInformation);
            }
        }

        public override void Execute()
        {
            this.CheckChildCount("mid������Ԫ���������Ϸ�");//check child token

            TokenRecord TokenSource = this.ChildList[0];
            TokenSource.Execute();
            string strSource = TokenSource.ChangeTokenToString();

            TokenRecord TokenStartIndex = this.ChildList[1];
            TokenStartIndex.Execute();
            int intStartIndex = Convert.ToInt32(TokenStartIndex.ChangeTokenToDouble("mid����ʼ��Ų��ǺϷ�����"));

            //�����ʼ��ŵĺϷ��ԣ���û��Խ����Χ
            if(intStartIndex < 0)
                throw new SyntaxException(this.Index, this.Length, "mid����ʼ���С��0");
            if(intStartIndex > strSource.Length)
                throw new SyntaxException(this.Index, this.Length, "mid����ʼ��Ŵ����ַ�������");

            if (this.ChildList.Count == 2)
            {
                this.TokenValue = strSource.Substring(intStartIndex);
            }
            else
            {
                TokenRecord TokenLength = this.ChildList[2];
                TokenLength.Execute();
                int intLength = Convert.ToInt32(TokenLength.ChangeTokenToDouble("mid�Ľ�����Ų��ǺϷ�����"));

                //��������ŵĺϷ��ԣ���û��Խ����Χ
                if (intLength < 0)
                    throw new SyntaxException(this.Index, this.Length, "mid�Ľ�ȡ����С��0");
                if(intLength > strSource.Length - intStartIndex)
                    throw new SyntaxException(this.Index, this.Length, "mid�Ľ�ȡ���ȳ�����Χ");

                this.TokenValue = strSource.Substring(intStartIndex, intLength);
            }
        }
    }
}
