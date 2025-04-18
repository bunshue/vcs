
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/132860.html



我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，我們可以根據這三者的共有特性提取出鳥類（Bird）做為父類，喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。

創建基類Bird如下，添加一個虛方法Eat():



/*
我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，
我們可以根據這三者的共有特性提取出鳥類（Bird1）做為父類，喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。
*/

//創建基類Bird1如下，添加一個虛方法Eat():
    /// <summary>
    /// 鳥類：父類
    /// </summary>
    public class Bird1
    {
        /// <summary>
        /// 吃：虛方法
        /// </summary>
        public virtual void Eat()
        {
            Console.WriteLine("我是一只小小鳥，我喜歡吃蟲子~");
        }
    }

//創建子類Magpie如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
    /// <summary>
    /// 喜鵲：子類
    /// </summary>
    public  class Magpie:Bird1
    {
        /// <summary>
        /// 重寫父類中Eat方法
        /// </summary>
        public override void Eat()
        {
            Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
        }
    }

//創建一個子類Eagle如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
    /// <summary>
    /// 老鷹：子類
    /// </summary>
    public  class Eagle:Bird1
    {
        /// <summary>
        /// 重寫父類中Eat方法
        /// </summary>
        public override void Eat()
        {
            Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
        }
    }

//創建一個子類Penguin如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
    /// <summary>
    /// 企鵝：子類
    /// </summary>
    public  class Penguin:Bird1
    {
        /// <summary>
        /// 重寫父類中Eat方法
        /// </summary>
        public override void Eat()
        {
            Console.WriteLine("我是一只小企鵝，我喜歡吃魚~");
        }
    }

到此，一個基類，三個子類已經創建完畢，接下來我們在主函數中來看下多態是怎樣體現的。

    static void Main(string[] args)
    {
        //創建一個Bird1基類數組，添加基類Bird1對象，Magpie對象，Eagle對象，Penguin對象
        Bird1[] birds = { 
                       new Bird1(),
                       new Magpie(),
                       new Eagle(),
                       new Penguin()
        };
        //遍歷一下birds數組
        foreach (Bird1 bird in birds)
        {
            bird.Eat();
        }
    }




Bird1






/*
我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，
我們可以根據這三者的共有特性提取出鳥類（Bird1）做為父類，喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。
*/

//創建基類Bird1如下，添加一個虛方法Eat():
/// <summary>
/// 鳥類：父類
/// </summary>
public class Bird1
{
/// <summary>
/// 吃：虛方法
/// </summary>
public virtual void Eat()
{
Console.WriteLine("我是一只小小鳥，我喜歡吃蟲子~");
}
}

//創建子類Magpie1如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
/// <summary>
/// 喜鵲：子類
/// </summary>
public  class Magpie1:Bird1
{
/// <summary>
/// 重寫父類中Eat方法
/// </summary>
public override void Eat()
{
Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
}
}

//創建一個子類Eagle1如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
/// <summary>
/// 老鷹：子類
/// </summary>
public  class Eagle1:Bird1
{
/// <summary>
/// 重寫父類中Eat方法
/// </summary>
public override void Eat()
{
Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
}
}

//創建一個子類Penguin1如下，繼承父類Bird1，重寫父類Bird1中的虛方法Eat()：
/// <summary>
/// 企鵝：子類
/// </summary>
public  class Penguin1:Bird1
{
/// <summary>
/// 重寫父類中Eat方法
/// </summary>
public override void Eat()
{
Console.WriteLine("我是一只小企鵝，我喜歡吃魚~");
}
}

    

//到此，一個基類，三個子類已經創建完畢，接下來我們在主函數中來看下多態是怎樣體現的。


    	//到此，一個基類，三個子類已經創建完畢，接下來我們在主函數中來看下多態是怎樣體現的。
        //創建一個Bird1基類數組，添加基類Bird1對象，Magpie1對象，Eagle1對象，Penguin1對象
        Bird1[] birds1 = { 
                       new Bird1(),
                       new Magpie1(),
                       new Eagle1(),
                       new Penguin1()
        };
        //遍歷一下birds數組
        foreach (Bird1 bird in birds1)
        {
            bird.Eat();
        }

//由此可見，子類Magpie，Eagle，Penguin對象可以賦值給父類對象，也就是說父類類型指針可以指向子類類型對象，這裡體現了裡氏替換原則。

//父類對象調用自己的Eat()方法，實際上顯示的是父類類型指針指向的子類類型對象重寫父類Eat後的方法。這就是多態。

		/*
		//我們再來看下利用抽象如何來實現多態
		
		還是剛才的例子，我們發現Bird這個父類，我們根本不需要使用它創建的對象，它存在的意義就是供子類來繼承。所以我們可以用抽象類來優化它。
		我們把Bird父類改成抽象類，Eat()方法改成抽象方法。代碼如下：
		*/

    /// <summary>
    /// 鳥類：基類
    /// </summary>
    public abstract class Bird
    {
        /// <summary>
        /// 吃：抽象方法
        /// </summary>
        public abstract void Eat();
    }


            //創建一個Bird基類數組，添加 Magpie對象，Eagle對象，Penguin對象
            Bird[] birds = { 
                           new Magpie(),
                           new Eagle(),
                           new Penguin()
            };
            //遍歷一下birds數組
            foreach (Bird bird in birds)
            {
                bird.Eat();
            }



						//添加一個接口IFlyable，代碼如下：
						
						/// <summary>
						/// 飛 接口
						/// </summary>
						public interface IFlyable
						{
						void Fly();
						}

喜鵲Magpie實現IFlyable接口，代碼如下：

					    /// <summary>
					    /// 喜鵲：子類，實現IFlyable接口
					    /// </summary>
					    public  class Magpie:Bird,IFlyable
					    {
					        /// <summary>
					        /// 重寫父類Bird中Eat方法
					        /// </summary>
					        public override void Eat()
					        {
					            Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
					        }
					        /// <summary>
					        /// 實現 IFlyable接口方法
					        /// </summary>
					        public void Fly()
					        {
					            Console.WriteLine("我是一只喜鵲，我可以飛哦~~");
					        }
					    }

老鷹Eagle實現IFlyable接口，代碼如下：

			    /// <summary>
			    /// 老鷹：子類實現飛接口
			    /// </summary>
			    public  class Eagle2:Bird1,IFlyable
			    {
			        /// <summary>
			        /// 重寫父類Bird中Eat方法
			        /// </summary>
			        public override void Eat()
			        {
			            Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
			        }
			
			        /// <summary>
			        /// 實現 IFlyable接口方法
			        /// </summary>
			        public void Fly()
			        {
			            Console.WriteLine("我是一只老鷹，我可以飛哦~~");
			        }
			    }



			        //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象
			        IFlyable[] flys = { 
			                       new Magpie(),
			                       new Eagle()
			        };
			        //遍歷一下flys數組
			        foreach (IFlyable fly in flys)
			        {
			            fly.Fly();
			        }



	//飛機也能飛，繼承Bird不合適的問題，現在有了接口，這個問題也可以解決了。如下，我添加一個飛機Plane類，實現IFlyable接口，代碼如下：
	
	    /// <summary>
	    /// 飛機類，實現IFlyable接口
	    /// </summary>
	    public  class Plane:IFlyable
	    {
	        /// <summary>
	        /// 實現接口方法
	        /// </summary>
	        public void Fly()
	        {
	            Console.WriteLine("我是一架飛機，我也能飛~~");
	        }
	    }




在Main主函數中，接口IFlyable數組，添加Plane對象：

    class Program
    {
        static void Main(string[] args)
        {
				            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象，Plane對象
				            IFlyable[] flys = { 
				                           new Magpie(),
				                           new Eagle(),
				                           new Plane()
				            };
				            //遍歷一下flys數組
				            foreach (IFlyable fly in flys)
				            {
				                fly.Fly();
				            }
            Console.ReadKey();
        }
    }



/*
由此，可以看出用接口實現多態程序的擴展性得到了大大提升，以後不管是再擴展一個蝴蝶（Butterfly），還是鳥人（Birder）創建一個類，實現這個接口，在主函數中添加該對象就可以了。
也不需要查看源代碼是如何實現的，體現了開放封閉原則！

接口充分體現了多態的魅力~~
*/






以上通過一些小的事例，給大家介紹了面向對象中三種實現多態的方式，或許有人會問，在項目中怎麼使用多態呢？多態的魅力在項目中如何體現？
那麼接下來我做一個面向對象的簡單計算器，來Show一下多態在項目中使用吧！



//加減乘除運算，我們可以根據共性提取出一個計算類，裡面包含兩個屬性 Number1和Number2，還有一個抽象方法Compute();代碼如下：

/// <summary>
/// 計算父類
/// </summary>
public abstract class Calculate
{
public int Number1
{
get;
set;
}
public int Number2
{
get;
set;
}
public abstract int Compute();
}

//接下來，我們添加一個加法器，繼承計算Calculate父類：

/// <summary>
/// 加法器
/// </summary>
public class Addition : Calculate
{
/// <summary>
/// 實現父類計算方法
/// </summary>
/// <returns>加法計算結果</returns>
public override int Compute()
{
return Number1 + Number2;
}
}

//再添加一個減法器，繼承計算Calculate父類：

/// <summary>
/// 減法器
/// </summary>
public class Subtraction : Calculate
{
/// <summary>
/// 實現父類計算方法
/// </summary>
/// <returns>減法計算結果</returns>
public override int Compute()
{
return Number1 - Number2;
}
}




    private void btn_Compute_Click(object sender, EventArgs e)
    {
        //獲取兩個參數
        int number1 = 456;
        int number2 = 123;
        //獲取運算符
        string operation = "+";
        //通過運算符，返回父類類型
        Calculate calculate = GetCalculateResult(operation);
        calculate.Number1 = number1;
        calculate.Number2 = number2;
        //利用多態，返回運算結果
        string result = calculate.Compute().ToString();
        //result this.lab_Result.Text = result;
    }
    /// <summary>
    /// 通過運算符，返回父類類型
    /// </summary>
    /// <param name="operation"></param>
    /// <returns></returns>
    private Calculate GetCalculateResult(string operation)
    {
        Calculate calculate = null;
        switch (operation)
        {
            case "+":
                calculate = new Addition();
                break;
            case "-":
                calculate = new Subtraction();
                break;
        }
        return calculate;
    }
    
    
    


			        //獲取兩個參數
			        int number1 = 456;
			        int number2 = 123;
			        //獲取運算符
			        string operation = "+";
			        //通過運算符，返回父類類型
			        Calculate calculate = GetCalculateResult(operation);
			        calculate.Number1 = number1;
			        calculate.Number2 = number2;
			        //利用多態，返回運算結果
			        string result = calculate.Compute().ToString();
			        //result this.lab_Result.Text = result;



