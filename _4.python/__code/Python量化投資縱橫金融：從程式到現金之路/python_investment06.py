"""
ch06a

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6.2  行业轮动理论及其投资策略

import itertools
from datetime import datetime
from dateutil.parser import parse
from scipy import stats as ss

sns.set_style('white')
     
1. 计算月度行业收益率

目前仅提供指数日线行情，故我们要将日线行情转化为月线行业。


def get_sw_ind_quotation():
    
    """
    返回申万一级行业指数所有历史行情
    Args:
        opt(bool):选择是否剔除综合行业，默认不剔除
    Returns:
        DataFrame: 申万一级行业指数日线行情

    Examples:
        >> df_daily_industry_unstack  = get_sw_ind_quotation()
    """
    
    # 拿取申万一级行业指数代码，一共28个
    index_symbol = DataAPI.IndustryGet(industryVersion=u"SW",industryVersionCD=u"",industryLevel=u"1",isNew=u"1",field=u"",pandas="1")['indexSymbol'].tolist() 

    index_symbol = [str(item) + '.ZICN' for item in index_symbol]  # 加上后缀，使得下面的行情API可以调用
    symbol_history_list = [] 
    for symbol in index_symbol: # 该API每次只能调用一个indexID
        df_daily_industry_symbol = DataAPI.MktIdxdGet(beginDate='2015-01-01', endDate='2018-01-23', ticker=symbol[:6], field=u"ticker,tradeDate,closeIndex")
        symbol_history_list.append(df_daily_industry_symbol)
        
    df_daily_industry_symbol = pd.concat(symbol_history_list,axis=0)  # 将获取的行业数据汇总
    df_daily_industry_unstack = df_daily_industry_symbol.set_index(['tradeDate','ticker']).unstack()['closeIndex'] # 将所有的行业行情数据转化为一张二维表
    return df_daily_industry_unstack
     

df_daily_industry_unstack = get_sw_ind_quotation() 
     

cc = df_daily_industry_unstack.head() # 如上我们便得到了申万一级行业至今的行情数据
print(cc)

接下来，我们要将日线的行情数据，转化为周线的行情数据，因为第一天的行情，有的行业存在缺失值，故我们将第一天的行情剔除。定义月行情为每月的第一个交易日到下一月的第一个交易日。

df_daily_industry_unstack = df_daily_industry_unstack.iloc[1:]  # 去掉第一期基期
df_daily_industry_unstack['tradeDate'] = df_daily_industry_unstack.index  # 加入tradeDate列，方便做map
     

def getMonthlyIndex(df_index):  # 得到月线行情
    df_index['tradeDate'] = df_index['tradeDate'].map(lambda x:parse(x)) # 将tradeDate列转化为时间格式
    df_index['year_month'] = df_index['tradeDate'].map(lambda x:(x.year,x.month)) # 得到（年，月）用于筛选
    return df_index.groupby(['year_month']).head(1) # 返回每个月的第一个交易日行情
     

df_monthly_industry_unstack = getMonthlyIndex(df_daily_industry_unstack[:])
df_monthly_industry_unstack = df_monthly_industry_unstack.sort_values(['tradeDate']) # 按tradeDate列排序
     

cc = df_monthly_industry_unstack.head(5) # 如上我们便得到了申万一级行业每个月第一个交易日的行情数据
print(cc)

接下来我们便要求月度收益率及其排名，调用Series的内置函数pct_change()可以很方便计算收益率；排名调用rank()函数按行做排序就就可以了，默认从小到大。

del df_monthly_industry_unstack['tradeDate'] # 删除tradeDate列和year_month列，方便后面调用后缀函数计算行业收益率
del df_monthly_industry_unstack['year_month']
     

df_monthly_industry_return = df_monthly_industry_unstack.pct_change(axis=0) # 调用pct_change()计算收益率
df_monthly_industry_return = df_monthly_industry_return.dropna(how='all') # 删除全是缺失值的第一行
df_monthly_industry_return_rank = df_monthly_industry_return.rank(axis=1) # 按行做排序
     

cc = df_monthly_industry_return_rank.head(5) # 如上我们便得到了申万一级行业每一期收益率的排名
print(cc)
     
cc = df_monthly_industry_return_rank.head()
print(cc)

2. 行业月度收益率相关性分析

将所有的行业月度收益率排序与行业的一阶滞后月度收益率排序做相关性分析。

# 拿取申万一级行业指数代码，一共28个
index_symbol = DataAPI.IndustryGet(industryVersion=u"SW",industryVersionCD=u"",industryLevel=u"1",isNew=u"1",field=u"",pandas="1")['indexSymbol'].tolist() 

     

def get_corr(ind1, ind2, df_ind):
    """
    返回行业1与行业2的1阶滞后的相关系数
    Args:
        ind1(str):行业指数代码
        ind2(str)：行业指数代码
        df_ind(DataFrame)：所有行业指数的月度收益表
    Returns:
        numpy.float64: 行业1与行业2的1阶滞后的相关系数

    Examples:
        >> ind_corr  = get_corr('801760','801150',df_monthly_industry_return_rank)
    """
    x = df_ind[ind1].iloc[0:-1].values
    y = df_ind[ind2].iloc[1:].values
    return np.corrcoef(x,y)[0][1]   #返回两组数据的皮尔森相关系数
     

predict_corr = {} 
for item in itertools.product(index_symbol,repeat=2):         #列表中的每个元素和剩余所有的元素进行配对
    predict_corr[item] = get_corr(item[0],item[1], df_monthly_industry_return_rank) # 得到行业收益率排名相关系数字典
predict_corr = pd.Series(predict_corr) # 将字典转化为序列
     

predict_corr.hist() # 做出相关系数的频数直方图

show()

可以看出行业与行业的一阶滞后的相关性并不高，大部分维持在0附近，我们要找出那些相关系数在统计上是显著的两个行业。相关系数不等于0的显著性检验量为：
查阅分布表,,反推出,即当

时,在99%置信水平是统计上显著的。故我们筛选出大于0.43或小于-0.43时的行业相关性。

filter_corr = predict_corr[(predict_corr>0.43) | (predict_corr<-0.43)]
tem = pd.DataFrame(filter_corr.sort_values(ascending=0)).reset_index()
tem.columns = ['ind1','ind2','corr']
print(tem)
     
def get_ind_name(tickers):
    """
    返回行业代码对应的行业名称
    Args:
        tickers(list):行业代码列表
    Returns:
        DataFrame: 一列行业代码一列行业名称组成的DataFrame

    Examples:
        >> symbol_name  = get_ind_name([801030,801120,801130,801170])
    """
    symbol_name = DataAPI.IndustryGet(industryVersion=u"SW",industryVersionCD=u"",industryLevel=u"1",isNew=u"1",
                                       field=u"indexSymbol,industryName",pandas="1")
    return symbol_name[symbol_name['indexSymbol'].isin(tickers)]
     

ind1_dict = get_ind_name(tem.ind1).set_index('indexSymbol').industryName.to_dict()    #一定注意是字符！！！
ind2_dict = get_ind_name(tem.ind2).set_index('indexSymbol').industryName.to_dict()    #一定注意是字符！！！
tem['ind1'] = tem.ind1.map(ind1_dict)
tem['ind2'] = tem.ind2.map(ind2_dict)
print(tem)
     
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6.8.1 有效边界

1 投资者偏好 马科维茨均值方差模型最早提出将数理统计的方法应用到投资组合选择上，并将资产的期望收益率的波动率定义为风险。这种定义下，我们使用收益率的均值（E(r)）和标准差（σ(r)）来刻画 “收益”和“风险”。 通常，我们认为人们是“风险厌恶”的，并构造如下形式的效用函数来代表投资者的投资偏好： U(r)=E(r)- 1/2 Aσ^2 (r) 其中E(r)表示投资组合的预期收益率，σ^2 (r)表示投资组合的方差；预期收益率越高，效用值越高，收益方差越大，效用值越小。这表明投资者喜欢更高的E(r)，而不喜欢高的σ^2 (r)。由于不同的投资者对于风险和收益有不同的偏好，因此效用函数中加入风险厌恶系数参数A表示投资者不同偏好，A越大，则投资者为追求更高的收益愿意承担更小的风险，或者说该投资者要求更高的收益补偿面临的风险。 下面的一段代码构造了不同的A对于投资者效用的影响，从输出的图形中可以看出，A越大投资者相同效用值的无差异曲线越陡峭，投资者为承担风险要求的收益补偿越大。

import matplotlib.pylab as pl

U = 0.3
sigmas = np.linspace(0., 1., 101)
As = [0., 1., 2., 3.]
indifference_curves = []
for A in As:
    Es = [U + 0.5 * A * sig*sig for sig in sigmas]
    indifference_curves.append(Es)

fig = pl.figure(figsize=(9, 6))
plots = []
for i, Es in enumerate(indifference_curves):
    plots.append(pl.plot(sigmas, Es, label="A = {}".format(As[i])))
pl.title("Indifference Curve with U = {}".format(U))
pl.xlabel("
")
pl.ylabel("
")
pl.legend(loc='best')
pl.show()
     

U同时是E和σ的函数，所以在σ-E图上，对于确定的A，不同的U表现为一组不相交的抛物线，这就是效用的无差异曲线，越往左上方的无差异曲线，代表越高的效用，因此投资者总是偏好位于左上方的无差异曲线上面的投资组合。下面一段代码绘制出了A = 2时的一组无差异曲线。

import matplotlib.pylab as pl

A = 2.
sigmas = np.linspace(0., 1., 101)
Us = [0.05, 0.1, 0.15, 0.2]
indifference_curves = []
for U in Us:
    Es = [U + 0.5 * A * sig*sig for sig in sigmas]
    indifference_curves.append(Es)

fig = pl.figure(figsize=(9, 6))
plots = []
for i, Es in enumerate(indifference_curves):
    plots.append(pl.plot(sigmas, Es, label="U = {}".format(Us[i])))
pl.title("Indifference Curve with A = {}".format(A))
pl.xlabel("
")
pl.ylabel("
")
pl.legend(loc='best')
pl.show()
     

2 资产组合 假设有两种资产E_1和E_2，其预期收益率和方差分别为r_1、σ_1^2和r_2、σ_2^2,收益率相关系数为ρ。另有，r_1<r_2、〖0<σ〗_1<σ_2。如果同时投资于两种资产，权重分别为w_1、1-w_1，则组合的期望收益率和方差可表示为： r=w_1 r_1+(1-w_1)r_2 σ^2= w_1^2 σ_1^2+〖(1-w_1)〗^2 σ_2^2+2w_1 (1-w_1)ρσ_1 σ_2 容易证明,当且仅当ρ=1时资产组合标准差与预期收益呈线性关系。由于ρ的取值范围在-1和1之间，因此通常情况下σ^2= w_1^2 σ_1^2+〖(1-w_1)〗^2 σ_1^2+2w_1 (1-w_1 )ρσ_1 σ_2<〖(w_1 σ_1+(1-w_1 )σ_2)〗^2，即组合标准差小于两种资产标准差的加权平均，收益-标准差点在两种资产收益-标准差点连线的左侧。甚至在大多数情况下，当把波动率更大的资产2开始引入组合时，其收益波动甚至比只投资于资产1时更小，当经过最小方差临界点时才会慢慢增大。这也体现了投资组合的重要性——通过分散投资以更小的组合风险获得更高的收益。如下代码显示了当投资产品只有两种时，不同相关系数对应的不同有效边界。

import matplotlib.pylab as pl

phos = [-1, -0.5, 0, 0.5, 1]
r1, sigma1 = 0.05, 0.05
r2, sigma2 = 0.10, 0.25

rs = [r1*t + r2*(1-t) for t in np.linspace(0., 1., 101)]
all_sigmas = []
for pho in phos:
    all_sigmas.append(np.sqrt([t*t*sigma1*sigma1 + (1-t)*(1-t)*sigma2*sigma2 + 2*pho*t*(1-t)*sigma1*sigma2 for t in np.linspace(0., 1., 101)]))

fig = pl.figure(figsize=(9, 6))
plots = []
for i, sigmas in enumerate(all_sigmas):
    plots.append(pl.plot(sigmas, rs, label="pho = {}".format(phos[i])))
pl.title("Convex Combinations of Two Risky Assets")
pl.xlabel("
")
pl.ylabel("
")
pl.legend(loc='best')
pl.show()
     

3 有效边界和投资组合选择 当投资者面临的可选资产大于2种时，标准差和收益的关系就不仅仅局限于一条曲线了，通过权重的选取，投资者可选的收益-标准差点构成一个有边界的面。人们趋利避险的心理决定了理性投资人在面临同样风险时，会选择预期收益率更高的组合；而在预期收益相同时，会选择风险较低的组合。在所有可选的预期收益-标准差点中，位于最左侧的部分构成了一条边界线，其中从最小方差点往上的部分构成了有效边界。在该边界线右下方的所有点是无效的投资组合，没有人会选择；在该边界线坐上的所有点是不可能达到的投资组合。 如下的代码中，我们给出了利用通联数据构造投资组合，并获取有效边界上几个特殊点的函数，以及相关的调用示例。其中，get_efficient_frontier()函数用于获取有效边界；draw_efficient_frontier()函数用于绘制有效边界图形；get_minimum_variance_portfolio()函数用于求解最小方差组合点； get_maximum_utility_portfolio()函数用于求解给定效用函数的效用最大化点；get_maximum_sharpe_portfolio()函数用于寻找最大夏普率点。

def describe(return_table, is_print=True):
    """
    输出收益率矩阵的描述性统计量，包括：
        年化收益率
        年化标准差
        相关系数矩阵
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        is_print (bool): 是否直接输出
    Returns:
        dict: 描述性统计量字典，键为"annualized_return", "annualized_volatility", "covariance_matrix"和"coefficient_matrix"
    Examples:
        >> describe(return_table)
        >> describe(return_table, is_print=True)
    """
    
    from scipy.stats.mstats import gmean
    
    output = {}
    output['annualized_return'] = pd.DataFrame(dict(zip(return_table.columns, gmean(return_table+1.)**252 - 1.)), index=[0], columns=return_table.columns)
    output['annualized_volatility'] = pd.DataFrame(return_table.std() * np.sqrt(250)).T
    output['covariance_matrix'] = return_table.cov() * 250.
    output['coefficient_matrix'] = return_table.corr()
        
    if is_print:
        for key, val in output.iteritems():
            print "{}:\n{}\n".format(key, val)
    
    return output

def get_efficient_frontier(return_table, allow_short=False, n_samples=25):
    """
    计算Efficient Frontier
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        n_samples (int): 用于计算Efficient Frontier的采样点数量
    Returns:
        DataFrame: Efficient Frontier的结果，列为"returns", "risks", "weights"
    """
    
    from cvxopt import matrix, solvers
    
    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        raise ValueError("There must be at least 2 assets to calculate the efficient frontier!")

    output = describe(return_table, is_print=False)
    covariance_matrix = matrix(output['covariance_matrix'].as_matrix())
    expected_return = output['annualized_return'].iloc[0, :].as_matrix()

    risks, returns, weights = [], [], []
    for level_return in np.linspace(min(expected_return), max(expected_return), n_samples):
        P = 2 * covariance_matrix
        q = matrix(np.zeros(n_asset))
        
        if allow_short:
            G = matrix(0., (n_asset, n_asset))
        else:
            G = matrix(np.diag(-1 * np.ones(n_asset)))
        
        h = matrix(0., (n_asset, 1))    
        A = matrix(np.row_stack((np.ones(n_asset), expected_return)))
        b = matrix([1.0, level_return])
        solvers.options['show_progress'] = False
        sol = solvers.qp(P, q, G, h, A, b)
        risks.append(np.sqrt(sol['primal objective']))
        returns.append(level_return)
        weights.append(dict(zip(assets, list(sol['x'].T))))
    
    output = {"returns": returns,
              "risks": risks,
              "weights": weights}
    output = pd.DataFrame(output)
    return output

def draw_efficient_frontier(effcient_frontier_output):
    """
    绘出Efficient Frontier
    
    Args:
        effcient_frontier_output: Efficient Frontier的计算结果，即get_efficient_frontier的输出
    """

    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(111)
    ax.plot(effcient_frontier_output['risks'], effcient_frontier_output['returns'])
    ax.set_title('Efficient Frontier')
    ax.set_xlabel('Standard Deviation')
    ax.set_ylabel('Expected Return')
    ax.tick_params(labelsize=12)
    show()

def get_minimum_variance_portfolio(return_table, allow_short=False, show_details=True):
    """
    计算最小方差组合
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节
    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    
    from cvxopt import matrix, solvers
    
    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        weights = np.array([1.])
        weights_dict = {assets[0]: 1.}
    else:
        output = describe(return_table, is_print=False)
        covariance_matrix = matrix(output['covariance_matrix'].as_matrix())
        expected_return = output['annualized_return'].iloc[0, :].as_matrix()

        P = 2 * covariance_matrix
        q = matrix(np.zeros(n_asset))

        if allow_short:
            G = matrix(0., (n_asset, n_asset))
        else:
            G = matrix(np.diag(-1 * np.ones(n_asset)))
        
        h = matrix(0., (n_asset, 1))
        A = matrix(np.ones(n_asset)).T
        b = matrix([1.0])
        solvers.options['show_progress'] = False
        sol = solvers.qp(P, q, G, h, A, b)
        weights = np.array(sol['x'].T)[0]
        weights_dict = dict(zip(assets, weights))

    r = np.dot(weights, output['annualized_return'].iloc[0, :].as_matrix())
    v = np.sqrt(np.dot(np.dot(weights, covariance_matrix), weights.T))

    if show_details:
        print """
Minimum Variance Portfolio:
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Weights: {}
""".format(allow_short, r, v, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict

def get_maximum_utility_portfolio(return_table, risk_aversion=3., allow_short=False, show_details=True):
    """
    计算最大效用组合，目标函数为：期望年化收益率 - 风险厌恶系数 * 期望年化方差
    
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        risk_aversion (float): 风险厌恶系数，越大表示对风险越厌恶，默认为3.0
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节

    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    
    from cvxopt import matrix, solvers

    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        weights = np.array([1.])
        weights_dict = {assets[0]: 1.}
    else:
        output = describe(return_table, is_print=False)
        covariance_matrix = matrix(output['covariance_matrix'].as_matrix())
        expected_return = output['annualized_return'].iloc[0, :].as_matrix()

        if abs(risk_aversion) < 0.01:
            max_ret = max(expected_return)
            weights = np.array([1. if expected_return[i] == max_ret else 0. for i in range(n_asset)])
            weights_dict = {asset: weights[i] for i, asset in enumerate(assets)}
        else:
            P = risk_aversion * covariance_matrix
            q = matrix(-expected_return.T)

            if allow_short:
                G = matrix(0., (n_asset, n_asset))
            else:
                G = matrix(np.diag(-1 * np.ones(n_asset)))

            h = matrix(0., (n_asset, 1))
            A = matrix(np.ones(n_asset)).T
            b = matrix([1.0])
            solvers.options['show_progress'] = False
            sol = solvers.qp(P, q, G, h, A, b)
            weights = np.array(sol['x'].T)[0]
            weights_dict = dict(zip(assets, weights))

    r = np.dot(weights, output['annualized_return'].iloc[0, :].as_matrix())
    v = np.sqrt(np.dot(np.dot(weights, covariance_matrix), weights.T))
    
    if show_details:
        print """
Maximum Utility Portfolio:
    Risk Aversion: {}
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Weights: {}
""".format(risk_aversion, allow_short, r, v, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict

def get_maximum_sharpe_portfolio(return_table, riskfree_rate=0., allow_short=False, show_details=True):
    """
    计算最大效用组合，目标函数为：（期望年化收益率 - 无风险收益率）/ 期望年化方差
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        riskfree_rate (float): 无风险收益率
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节
    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    
    from cvxopt import matrix, solvers

    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        output = describe(return_table, is_print=False)
        r = output['annualized_return'].iat[0, 0]
        v = output['annualized_volatility'].iat[0, 0]
        weights_dict = {assets[0]: 1.}
    else:
        efs = get_efficient_frontier(return_table, allow_short=allow_short, n_samples=100)
        i_star = max(range(100), key=lambda x: (efs.at[x, "returns"] - riskfree_rate) / efs.at[x, "risks"])
        r = efs.at[i_star, "returns"]
        v = efs.at[i_star, "risks"]
        weights_dict = efs.at[i_star, "weights"]

    s = (r - riskfree_rate) / v
    
    if show_details:
        print """
Maximum Sharpe Portfolio:
    Riskfree Rate: {}
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Sharpe: {}
    Portfolio Weights: {}
""".format(riskfree_rate, allow_short, r, v, s, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict
     

下面的代码利用上述理论和函数构造了一个简单的均值方差模型示例。

start = '20130101'
end = '20160630'
indices = ['000300.ZICN', '000905.ZICN', '399006.ZICN', '000012.ZICN','000013.ZICN']
df = DataAPI.MktIdxdGet(indexID=indices, beginDate=start, endDate=end, field="tradeDate,indexID,closeIndex")
df = df.pivot(index="tradeDate", columns="indexID", values="closeIndex")
for index in indices:
    df[index] = df[index] / df[index].shift() - 1.
return_table = df.dropna()

describe(return_table, is_print=True)
     

efficient_frontier = get_efficient_frontier(return_table, allow_short=False, n_samples=50)
efficient_frontier
     

draw_efficient_frontier(efficient_frontier)
     

get_minimum_variance_portfolio(return_table, allow_short=False, show_details=True)
     

get_maximum_utility_portfolio(return_table, risk_aversion=3, allow_short=False, show_details=True)
     

get_maximum_sharpe_portfolio(return_table, riskfree_rate=0.03, allow_short=True, show_details=True)
     


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 6.8.2 Black-Litterman模型



1 Black-Litterman模型概述 基于马科维茨均值-方差模型的资产组合分析需要获取各类资产预期收益和方差。通常有两种方法可以用来得到预期收益和收益率方差的估计，情景分析法和历史数据法。情景分析法主要根据当前行情和宏观经济环境等因素形成主观的预期，这种方法显然主观性、随意性过强。历史数据法则完全根据过去的历史收益率计算收益均值和方差，用来代替对未来的预期，这也是目前主流的做法。这种做法存在几个问题，一是历史数据往往由于历史的一些宏观环境或随机因素而存在比较大的波动性，这也意味着历史的收益率和方差在未来有可能由于宏观环境和随机因素的改变而不会重演；二是根据采取的历史数据的时间段不同，估算出的预期收益率和方差也会有较大差别，从而导致得出的最优资产配置比例也会有较大差别。高盛的Black F.和Litterman R.在其1991年的一篇论文中提到，在对全球债券投资组合的研究中，他们发现，当对德国债券预期报酬率做0.1%小幅修正后，该类资产的投资比例竟由原来的10.0%提高至55.0%。这也意味着马科维茨的均值-方差模型得到的投资组合对于输入的参数过于敏感。 Black和Litteraman在前述均值方差模型的基础上，通过历史数据估计基准预期和方差，导入投资者主观预期，把历史数据法和情景分析法结合起来，形成新的市场收益预期，从而解决了前述模型中预期收益和方差估计中存在的问题。 2 Black-Litterman模型简介 B-L模型在均衡收益基础上通过投资者观点修正了期望收益，使得均值方差组合优化中的期望收益更为合理，而且还将投资者观点融入进了模型，在一定程度上是对马科维茨均值方差组合理论的改进。 B-L模型假设各资产收益率R服从联合正态分布，R~N(μ,Σ)，其中μ和Σ是各资产预期收益率和协方差的估计值。现在假设估计向量μ本身也是随机的，且服从正态分布：μ~N(π,τΣ)，其中π为先验期望收益率的期望值，通常由历史平均收益率表示。模型引入投资者个人观点的方式是用线性方程组表示，每一个方程表示一个观点。例如，投资者认为未来第三种资产会比第一种资产收益率高2%，就可以表示为： -1×μ_1+0×μ_2+1×μ_3+⋯+0×μ_N=2% 投资者认为未来第二种资产收益率应该为5%，那么可以表示为： 0×μ_1+1×μ_2+0×μ_3+⋯+0×μ_N=5% 用P来表示该观点线性方程组的系数矩阵，观点方程组可表示为：Pμ = q。由于投资人观点也存在不确定性，因此在q的基础上还可以加上一个随机误差项：Pμ = q+ ϵ，其中ϵ~N(0, Ω)，因而Pμ~N(q, Ω)。这里，P被称为Pick Matrix，为K×N矩阵，表示对于N种资产的K个观点；q为K×1看法向量；Ω为看法向量误差项的K×K协方差矩阵，表示投资者观点的不确定程度。通常对于Ω，采用Ω=diag(τPΣP^T)的方式构造。 前面我们讨论过市场的看法：μ~N(π,τΣ)，用P调整后的市场看法可表示为：Pμ~N(Pπ,τPΣP^T)。 投资人观点和市场看法的差距服从分布：N(q-Pπ, Ω+τPΣP^T) 然后根据贝叶斯法则，结合先验信息和投资者观点，可以计算调整后的预期收益率和收益率方差分别为： Π ̂=Π+τΣP^T 〖(Ω+τPΣP^T)〗^(-1) (q-Pπ) M=τΣ-τΣP^T 〖(Ω+τPΣP^T)〗^(-1) PτΣ Σ_P=Σ+M 其中，Π为先验的期望收益，通过历史平均年化收益得到；Π ̂为个人观点调整后的期望收益；Σ为资产收益率之间的协方差矩阵；M为后验分布预期收益率的方差；Σ_P为调整后预期收益率方差；τ为均衡收益方差的刻度值，体现了对个人观点在总体估计中的权重，通常取值在0.025~0.05； P、q、Ω为观点矩阵。 得到调整后的期望收益率和方差后，就可以根据马科维茨均值方差模型计算最优权重。 3 Black-Litterman模型应用 在实践中应用该模型，简要来说主要有如下步骤： (1) 计算得到先验的期望收益； (2) 个人观点模型化，观点可以涉及单个资产，也可以有多个资产，最后按照一定的规则将所有观点构建成矩阵P、Q和Ω； (3) 计算调整后的预期收益率、调整后的收益率方差； (4) 根据调整后的期望收益，利用均值方差模型计算最优权重。 下面的代码提供了若干应用B-L模型进行优化的函数。其中get_BL_efficient_frontier()用于获取根据调整后的收益率期望和方差得到的有效边界；draw_efficient_frontier()用于绘制有效边界图形；get_BL_minimum_variance_portfolio()用于获取最小方差投资组合；get_BL_maximum_utility_portfolio()用于获取基于给定效用函数的最大化效用投资组合；get_maximum_sharpe_portfolio()用于获取最大夏普率投资组合。

def describe(return_table, is_print=True):
    """
    输出收益率矩阵的描述性统计量，包括：
        年化收益率
        年化标准差
        相关系数矩阵
    
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        is_print (bool): 是否直接输出

    Returns:
        dict: 描述性统计量字典，键为"annualized_return", "annualized_volatility", "covariance_matrix"和"coefficient_matrix"

    Examples:
        >> describe(return_table)
        >> describe(return_table, is_print=True)
    """
    from scipy.stats.mstats import gmean
    
    output = {}
    output['annualized_return'] = pd.DataFrame(dict(zip(return_table.columns, gmean(return_table+1.)**252 - 1.)), index=[0], columns=return_table.columns)
    output['annualized_volatility'] = pd.DataFrame(return_table.std() * np.sqrt(250)).T
    output['covariance_matrix'] = return_table.cov() * 250.
    output['coefficient_matrix'] = return_table.corr()
        
    if is_print:
        for key, val in output.iteritems():
            print "{}:\n{}\n".format(key, val)
    
    return output


def get_BL_efficient_frontier(return_table,tau=0.05,P=None,Q=None,Omega=None,allow_short=False, n_samples=25):
    """
    计算Efficient Frontier
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        n_samples (int): 用于计算Efficient Frontier的采样点数量
        P(np.array): 观点矩阵
        Q(np.array): 观点收益矩阵
        Omega(np.array): 观点置信度矩阵
        tau(float): 为均衡收益方差的刻度值，体现了对个人观点在总体估计中的权重
    Returns:
        DataFrame: Efficient Frontier的结果，列为"returns", "risks", "weights"
    """
    from cvxopt import matrix, solvers
    
    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        raise ValueError("There must be at least 2 assets to calculate the efficient frontier!")

    output = describe(return_table, is_print=False)
    covmat =(output['covariance_matrix'])
    expected_return = output['annualized_return'].iloc[0, :]
    
    # 求解调整后的期望收益、方差
    adjustedReturn = expected_return + tau*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+tau*(P.dot(covmat).dot(P.transpose())))).dot(Q - P.dot(expected_return))
    right = (tau)*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+P.dot(covmat).dot(P.transpose()))).dot(P.dot(tau*covmat))
    right = right.transpose()
    right = right.set_index(expected_return.index)
    M = tau*covmat - right
    Sigma_p = covmat + M
    adjustedReturn = adjustedReturn.as_matrix()
    Sigma_p = matrix(Sigma_p.as_matrix())
	
    risks, returns, weights = [], [], []
    for level_return in np.linspace(min(adjustedReturn), max(adjustedReturn), n_samples):
        P = 2 * Sigma_p
        q = matrix(np.zeros(n_asset))
        
        if allow_short:
            G = matrix(0., (n_asset, n_asset))
        else:
            G = matrix(np.diag(-1 * np.ones(n_asset)))
        
        h = matrix(0., (n_asset, 1))    
        A = matrix(np.row_stack((np.ones(n_asset), adjustedReturn)))
        b = matrix([1.0, level_return])
        solvers.options['show_progress'] = False
        sol = solvers.qp(P, q, G, h, A, b)
        risks.append(np.sqrt(sol['primal objective']))
        returns.append(level_return)
        weights.append(dict(zip(assets, list(sol['x'].T))))
    
    output = {"returns": returns,
              "risks": risks,
              "weights": weights}
    output = pd.DataFrame(output)
    return output

def draw_efficient_frontier(effcient_frontier_output):
    """
    绘出Efficient Frontier
    Args:
        effcient_frontier_output: Efficient Frontier的计算结果，即get_efficient_frontier的输出
    """

    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(111)
    ax.plot(effcient_frontier_output['risks'], effcient_frontier_output['returns'])
    ax.set_title('Efficient Frontier')
    ax.set_xlabel('Standard Deviation')
    ax.set_ylabel('Expected Return')
    ax.tick_params(labelsize=12)
    show()

def get_BL_minimum_variance_portfolio(return_table,tau=0.05,P=None,Q=None,Omega=None, allow_short=False, show_details=True):
    """
    计算最小方差组合
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节
        P(np.array): 观点矩阵
        Q(np.array): 观点收益矩阵
        Omega(np.array): 观点置信度矩阵
        tau(float): 为均衡收益方差的刻度值，体现了对个人观点在总体估计中的权重
    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    
    from cvxopt import matrix, solvers
    
    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        weights = np.array([1.])
        weights_dict = {assets[0]: 1.}
    else:
        output = describe(return_table, is_print=False)
        covmat =(output['covariance_matrix'])
        expected_return = output['annualized_return'].iloc[0, :]
    
        # 求解调整后的期望收益、方差
        adjustedReturn = expected_return + tau*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+tau*(P.dot(covmat).dot(P.transpose())))).dot(Q - P.dot(expected_return))
        right = (tau)*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+P.dot(covmat).dot(P.transpose()))).dot(P.dot(tau*covmat))
        right = right.transpose()
        right = right.set_index(expected_return.index)
        M = tau*covmat - right
        Sigma_p = covmat + M
        adjustedReturn = adjustedReturn.as_matrix()
        Sigma_p = matrix(Sigma_p.as_matrix())

        P = 2 * Sigma_p
        q = matrix(np.zeros(n_asset))

        if allow_short:
            G = matrix(0., (n_asset, n_asset))
        else:
            G = matrix(np.diag(-1 * np.ones(n_asset)))
        
        h = matrix(0., (n_asset, 1))
        A = matrix(np.ones(n_asset)).T
        b = matrix([1.0])
        solvers.options['show_progress'] = False
        sol = solvers.qp(P, q, G, h, A, b)
        weights = np.array(sol['x'].T)[0]
        weights_dict = dict(zip(assets, weights))

    r = np.dot(weights, output['annualized_return'].iloc[0, :].as_matrix())
    v = np.sqrt(np.dot(np.dot(weights, Sigma_p), weights.T))

    if show_details:
        print """
Minimum Variance Portfolio:
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Weights: {}
""".format(allow_short, r, v, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict

def get_BL_maximum_utility_portfolio(return_table,tau=0.05,P=None,Q=None,Omega=None, risk_aversion=3., allow_short=False, show_details=True):
    """
    计算最大效用组合，目标函数为：期望年化收益率 - 风险厌恶系数 * 期望年化方差
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        risk_aversion (float): 风险厌恶系数，越大表示对风险越厌恶，默认为3.0
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节
        P(np.array): 观点矩阵
        Q(np.array): 观点收益矩阵
        Omega(np.array): 观点置信度矩阵
        tau(float): 为均衡收益方差的刻度值，体现了对个人观点在总体估计中的权重

    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    from cvxopt import matrix, solvers

    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        weights = np.array([1.])
        weights_dict = {assets[0]: 1.}
    else:
        output = describe(return_table, is_print=False)
        covmat =(output['covariance_matrix'])
        expected_return = output['annualized_return'].iloc[0, :]
    
        # 求解调整后的期望收益、方差
        adjustedReturn = expected_return + tau*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+tau*(P.dot(covmat).dot(P.transpose())))).dot(Q - P.dot(expected_return))
        right = (tau)*covmat.dot(P.transpose()).dot(np.linalg.inv(Omega+P.dot(covmat).dot(P.transpose()))).dot(P.dot(tau*covmat))
        right = right.transpose()
        right = right.set_index(expected_return.index)
        M = tau*covmat - right
        Sigma_p = covmat + M
        adjustedReturn = adjustedReturn.as_matrix()
        Sigma_p = matrix(Sigma_p.as_matrix())

        if abs(risk_aversion) < 0.01:
            max_ret = max(adjustedReturn)
            weights = np.array([1. if adjustedReturn[i] == max_ret else 0. for i in range(n_asset)])
            weights_dict = {asset: weights[i] for i, asset in enumerate(assets)}
        else:
            P = risk_aversion * Sigma_p
            q = matrix(-adjustedReturn.T)

            if allow_short:
                G = matrix(0., (n_asset, n_asset))
            else:
                G = matrix(np.diag(-1 * np.ones(n_asset)))

            h = matrix(0., (n_asset, 1))
            A = matrix(np.ones(n_asset)).T
            b = matrix([1.0])
            solvers.options['show_progress'] = False
            sol = solvers.qp(P, q, G, h, A, b)
            weights = np.array(sol['x'].T)[0]
            weights_dict = dict(zip(assets, weights))

    r = np.dot(weights, output['annualized_return'].iloc[0, :].as_matrix())
    v = np.sqrt(np.dot(np.dot(weights, Sigma_p), weights.T))
    
    if show_details:
        print """
Maximum Utility Portfolio:
    Risk Aversion: {}
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Weights: {}
""".format(risk_aversion, allow_short, r, v, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict

def get_maximum_sharpe_portfolio(return_table, riskfree_rate=0.,tau=0.05,P=None,Q=None,Omega=None,allow_short=False, show_details=True):
    """
    计算最大效用组合，目标函数为：（期望年化收益率 - 无风险收益率）/ 期望年化方差
    Args:
        return_table (DataFrame): 收益率矩阵，列为资产，值为按日期升序排列的收益率
        riskfree_rate (float): 无风险收益率
        allow_short (bool): 是否允许卖空
        show_details (bool): 是否显示细节
        P(np.array): 观点矩阵
        Q(np.array): 观点收益矩阵
        Omega(np.array): 观点置信度矩阵
        tau(float): 为均衡收益方差的刻度值，体现了对个人观点在总体估计中的权重

    Returns:
        dict: 最小方差组合的权重信息，键为资产名，值为权重
    """
    from cvxopt import matrix, solvers

    assets = return_table.columns
    n_asset = len(assets)
    if n_asset < 2:
        output = describe(return_table, is_print=False)
        r = output['annualized_return'].iat[0, 0]
        v = output['annualized_volatility'].iat[0, 0]
        weights_dict = {assets[0]: 1.}
    else:
        efs = get_BL_efficient_frontier(return_table,tau,P=P,Q=Q,Omega=Omega,allow_short=allow_short, n_samples=100)
        i_star = max(range(100), key=lambda x: (efs.at[x, "returns"] - riskfree_rate) / efs.at[x, "risks"])
        r = efs.at[i_star, "returns"]
        v = efs.at[i_star, "risks"]
        weights_dict = efs.at[i_star, "weights"]

    s = (r - riskfree_rate) / v
    
    if show_details:
        print """
Maximum Sharpe Portfolio:
    Riskfree Rate: {}
    Short Allowed: {}
    Portfolio Return: {}
    Portfolio Volatility: {}
    Portfolio Sharpe: {}
    Portfolio Weights: {}
""".format(riskfree_rate, allow_short, r, v, s, "\n\t{}".format("\n\t".join("{}: {:.1%}".format(k, v) for k, v in weights_dict.items()))).strip()
    
    return weights_dict

     

下面，我们利用沪深300指数、中证500指数、创业板指、国债指数、企业债指数构造一个利用B-L模型的简单示例。

from cvxopt import matrix, solvers

start = '20130101'
end = '20160630'
indices = ['000300.ZICN', '000905.ZICN', '399006.ZICN', '000012.ZICN','000013.ZICN']
df = DataAPI.MktIdxdGet(indexID=indices, beginDate=start, endDate=end, field="tradeDate,indexID,closeIndex")
df = df.pivot(index="tradeDate", columns="indexID", values="closeIndex")
for index in indices:
    df[index] = df[index] / df[index].shift() - 1.
return_table = df.dropna()

describe(return_table, is_print=False)
     

# - 生成观点矩阵P、Q、Omega，我们知道历史数据由于包含了14-15牛市，历史平均收益偏高，尤其创业板，对于刚经历3轮股灾的现在，显然要调整股市的期望收益。给出下面3个观点：
# 	- 观点1： 中证500的收益率超过沪深300收益5%(相比原来差距的近20%显著下调)
# 	- 观点2： HS300的收益率高于国债1%，（相对原来差距微调）
# 	- 观点3：创业板指收益比企业债指数高5%（相比原来差距近33%显著下调）
output = describe(return_table, is_print=False)
covariance_matrix = output['covariance_matrix']
expected_return = output['annualized_return'].iloc[0, :]
tau = 0.05 

P = np.array([[-1,1,0,0,0],[1,0,0,-1,0],[0,0,1,0,-1]])
print "P:",P
Q = np.array([0.05,0.01,0.05])
print "Q:",Q
Omega = tau*(P.dot(covariance_matrix).dot(P.transpose()))
Omega = np.diag(np.diag(Omega,k=0))
print "Omega:",Omega
     

efficient_frontier = get_BL_efficient_frontier(return_table,tau,P=P,Q=Q,Omega=Omega,allow_short=False, n_samples=50)
draw_efficient_frontier(efficient_frontier)
efficient_frontier.head()
     

get_BL_minimum_variance_portfolio(return_table,tau=0.05,P=P,Q=Q,Omega=Omega, allow_short=False, show_details=True)
     

get_BL_maximum_utility_portfolio(return_table,tau=0.05,P=P,Q=Q,Omega=Omega, risk_aversion=3., allow_short=False, show_details=True)
     

get_maximum_sharpe_portfolio(return_table, riskfree_rate=0.,tau=0.05,P=P,Q=Q,Omega=Omega,allow_short=True, show_details=True)
     

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6.8.3 风险平价模型

from datetime import datetime as dt
from CAL.PyCAL import font
from scipy.optimize import minimize

sns.set_style('whitegrid')


def get_smart_weight(cov_mat, method='min variance', wts_adjusted=False):
    """
    功能：输入协方差矩阵，得到不同优化方法下的权重配置
    输入：
        cov_mat  pd.DataFrame,协方差矩阵，index和column均为资产名称
        method  优化方法，可选的有min variance、risk parity、max diversification、equal weight
    输出：
        pd.Series  index为资产名，values为weight
    PS:
        依赖scipy package
    """
    
    if not isinstance(cov_mat, pd.DataFrame):
        raise ValueError('cov_mat should be pandas DataFrame！')
        
    omega = np.matrix(cov_mat.values)  # 协方差矩阵
    
    # 定义目标函数
    def fun1(x):
        return np.matrix(x) * omega * np.matrix(x).T
    
    def fun2(x):
        tmp = (omega * np.matrix(x).T).A1
        risk = x * tmp
        delta_risk = [sum((i - risk)**2) for i in risk]
        return sum(delta_risk)
    
    def fun3(x):
        den = x * omega.diagonal().T
        num = np.sqrt(np.matrix(x) * omega * np.matrix(x).T)
        return num/den
    
    # 初始值 + 约束条件 
    x0 = np.ones(omega.shape[0]) / omega.shape[0]  
    bnds = tuple((0,None) for x in x0)
    cons = ({'type':'eq', 'fun': lambda x: sum(x) - 1})
    options={'disp':False, 'maxiter':1000, 'ftol':1e-20}
        
    if method == 'min variance':   
        res = minimize(fun1, x0, bounds=bnds, constraints=cons, method='SLSQP', options=options) 
    elif method == 'risk parity':
        res = minimize(fun2, x0, bounds=bnds, constraints=cons, method='SLSQP', options=options)
    elif method == 'max diversification':
        res = minimize(fun3, x0, bounds=bnds, constraints=cons, method='SLSQP', options=options)
    elif method == 'equal weight':
        return pd.Series(index=cov_mat.index, data=1.0 / cov_mat.shape[0])
    else:
        raise ValueError('method should be min variance/risk parity/max diversification/equal weight！！！')
        
    # 权重调整
    if res['success'] == False:
        # print res['message']
        pass
    wts = pd.Series(index=cov_mat.index, data=res['x'])
    if wts_adjusted == True:
        wts = wts[wts >= 0.0001]
        return wts / wts.sum() * 1.0
    elif wts_adjusted == False:
        return wts
    else:
        raise ValueError('wts_adjusted should be True/False！')
        
def get_dates(start_date, end_date, frequency='daily'):
    """
    功能：输入起始日期和频率，即可获得日期列表（daily包括起始日，其余的都是位于起始日中间的）
    输入参数：
       start_date，开始日期，'xxxxxxxx'形式
       end_date，截止日期，'xxxxxxxx'形式
       frequency，频率，daily为所有交易日，daily1为所有自然日，weekly为每周最后一个交易日，weekly2为每隔两周，monthly为每月最后一个交易日，quarterly为每季最后一个交易日
    输出参数：
       获得list型日期列表，以'xxxxxxxx'形式存储
    PS:
        要用到DataAPI.TradeCalGet！！！
    """
    
    data = DataAPI.TradeCalGet(exchangeCD=u"XSHG",beginDate=start_date,endDate=end_date,field=u"calendarDate,isOpen,isWeekEnd,isMonthEnd,isQuarterEnd",pandas="1")
    if frequency == 'daily':
        data = data[data['isOpen'] == 1]
    elif frequency == 'daily1':
        pass
    elif frequency == 'weekly':
        data = data[data['isWeekEnd'] == 1]
    elif frequency == 'weekly2':
        data = data[data['isWeekEnd'] == 1]
        data = data[0:data.shape[0]:2]
    elif frequency == 'monthly':
        data = data[data['isMonthEnd'] == 1]
    elif frequency == 'quarterly':
        data = data[data['isQuarterEnd'] == 1]
    else:
        raise ValueError('调仓频率必须为daily/daily1/weekly/weekly2/monthly/quarterly！！！')
    # date_list = map(lambda x: x[0:4]+x[5:7]+x[8:10], data['calendarDate'].values.tolist())
    date_list = data['calendarDate'].values.tolist()
    return date_list


def shift_date(date, n, direction='back'): 
    """
    功能：给定date，获取该日期前/后n个交易日对应的交易日
    输入：
        date  'yyyymmdd'类型字符串
        n  非负整数，取值区间（0,720）
        direction  方向，取值为back/forward
    PS：
        get_dates()
    """
    
    last_two_year = str(int(date[:4])-3) + '0101'
    forward_two_year = str(int(date[:4])+3) + '1231'
    if direction == 'back':
        date_list = get_dates(last_two_year, date, 'daily')
        return date_list[len(date_list)-1-n]
    elif direction == 'forward':
        date_list = get_dates(date, forward_two_year, 'daily')
        return date_list[n]
    else:
        raise ValueError('direction should be back/forward！！！')


def cal_maxdrawdown(data):
    """
    功能：给定净值数据（list, np.array, pd.Series, pd.DataFrame），返回最大回撤
    输入：
        data, list/np.array/pd.Series/pd.DataFrame，净值曲线，初始金为1
    输出：
        list/np.array/pd.Series返回float
        pd.DataFrame返回pd.DataFrame，index为DataFrame.columns
    """
    
    if isinstance(data, list):
        data = np.array(data)
    if isinstance(data, pd.Series):
        data = data.values
        
    def get_mdd(values): # values为np.array的净值曲线，初始资金为1
        dd = [values[i:].min() / values[i] - 1 for i in range(len(values))]
        return abs(min(dd))
    
    if not isinstance(data, pd.DataFrame):
        return get_mdd(data)
    else:
        return data.apply(get_mdd)
    
    
def cal_indicators(df_daily_return):
    """
    功能：给定daily return，计算各组合的评价指标，包括：年化收益率、年化标准差、夏普值、最大回撤
    输入：
        df_daily_return  pd.DataFrame，index为升序排列的日期，columns为各组合名称，value为daily_return
    """
    
    df_cum_value = (df_daily_return + 1).cumprod()
    res = pd.DataFrame(index=['年化收益率','年化标准差','夏普值','最大回撤'], columns=df_daily_return.columns, data=0.0)
    res.loc['年化收益率'] = (df_daily_return.mean() * 250).apply(lambda x: '%.2f%%' % (x*100))
    res.loc['年化标准差'] = (df_daily_return.std() * np.sqrt(250)).apply(lambda x: '%.2f%%' % (x*100))
    res.loc['夏普值'] = (df_daily_return.mean() / df_daily_return.std() * np.sqrt(250)).apply(lambda x: np.round(x, 2))
    res.loc['最大回撤'] = cal_maxdrawdown(df_cum_value).apply(lambda x: '%.2f%%' % (x*100))
    return res
     

start_date = '20130913'
end_date = '20171215'

data = DataAPI.TradeCalGet(exchangeCD=u"XSHG",beginDate=start_date,endDate=end_date,field=u"calendarDate,isOpen,isWeekEnd,isMonthEnd,isQuarterEnd",pandas="1")

start_date = '2007-01-01'
end_date = '2016-11-02'
idx = ['000300', '399005', 'HSI', 'SPX', '000012']  # 沪深300、中小板指、恒生指数、标普500、国债
data1 = DataAPI.MktIdxdGet(ticker=idx, beginDate=start_date, endDate=end_date, field=u"secShortName,tradeDate,CHGPct", pandas="1")
total_daily_return = data1.pivot(index='tradeDate', columns='secShortName', values='CHGPct').dropna(how='all').fillna(0.0)
# total_daily_return.index = map(lambda x: x.replace('-',''), total_daily_return.index)
total_daily_return.head()
     

# backtest
selected_daily_return = total_daily_return[['沪深300', '中小板指', '恒生指数', '标普500', '上证国债']]
Ndays = 500   # 用多少天估算协方差矩阵
starts = shift_date(selected_daily_return.index[0], Ndays, 'forward')
ends = selected_daily_return.index[-1]
portfolio_cum_value = pd.DataFrame(index=selected_daily_return.loc[starts:ends].index, columns=['min variance', 'risk parity', 'max diversification','equal weight'], data=0.0)  # 记录组合累计净值
portfolio_positions = {}  # 记录组合各资产持仓 
allocation_methods = {'min variance', 'risk parity', 'max diversification','equal weight'}
for k in allocation_methods:
    portfolio_positions[k] = pd.DataFrame(index=portfolio_cum_value.index, columns=selected_daily_return.columns, data=0.0)
date_list = sorted(get_dates(starts, ends, 'quarterly')+[starts, ends])
for i in range(len(date_list)-1):
    current_period = date_list[i]
    next_period = date_list[i+1]
    tmp_date = shift_date(current_period, Ndays)
    cov_mat = selected_daily_return.loc[tmp_date:current_period].cov()*250
    # 权重优化
    for j in allocation_methods:
        wts = get_smart_weight(cov_mat, method=j, wts_adjusted=False)
        daily_rtn = selected_daily_return.loc[current_period:next_period]
        daily_rtn.ix[0] = 0.0
        assets_positions = (daily_rtn + 1).cumprod() * wts
        portfolio_positions[j].loc[assets_positions.index,:] = (assets_positions.T / assets_positions.sum(axis=1)).T
        cum_value = assets_positions.sum(axis=1)
        if i == 0:
            portfolio_cum_value.loc[cum_value.index, j] = cum_value * 1.0
        else:
            portfolio_cum_value.loc[cum_value.index, j] = cum_value * portfolio_cum_value.loc[cum_value.index[0],j]
            
assets_cum_value = (total_daily_return.loc[starts:ends] + 1).cumprod()
assets_cum_value['date'] = map(lambda x: dt.strptime(x, '%Y-%m-%d'), assets_cum_value.index)

fig = plt.figure(figsize=(15,6))
ax = fig.add_subplot(111)
font.set_size(12)
colors = ['royalblue','orange','powderblue','sage','gray','dimgray']
columns = ['沪深300', '中小板指', '恒生指数', '标普500', '上证国债']
for i in range(len(columns)):
    ax.plot(assets_cum_value['date'].values, assets_cum_value[columns[i]].values, color=colors[i])
ax.plot(assets_cum_value['date'].values, portfolio_cum_value['risk parity'].values, color='r')
ax.legend([i.decode('utf8') for i in columns] + ['risk parity'], prop=font, loc='best')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.grid(True)     

assets_indicators = cal_indicators(selected_daily_return.loc[starts:ends])
portfolio_indicators = cal_indicators(portfolio_cum_value.pct_change().dropna())
assets_indicators['risk parity'] = portfolio_indicators['risk parity']
assets_indicators     

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6.9 时间序列分析

from scipy import stats
import statsmodels.api as sm 

IndexData = pd.read_csv('data/01pct.csv')
IndexData = IndexData.set_index(IndexData['tradeDate'])
IndexData['colseIndexDiff_1'] = IndexData['closeIndex'].diff(1)  # 1阶差分处理
IndexData['closeIndexDiff_2'] = IndexData['colseIndexDiff_1'].diff(1)  # 2阶差分处理
IndexData.plot(subplots=True,figsize=(18,12))

show()

a = pd.Series([9,8,7,5,4,2])
b = a - a.mean() # 去均值
plt.figure(figsize=(10,4))
a.plot(label='a')
b.plot(label='mean removed a')
plt.legend()

show()

data = IndexData['closeIndex'] # 上证指数
m = 10 # 我们检验10个自相关系数

acf,q,p = sm.tsa.acf(data,nlags=m,qstat=True)  ## 计算自相关系数 及p-value
out = np.c_[range(1,11), acf[1:], q, p]
output=pd.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')
print(output)

data2 = IndexData['CHGPct'] # 上证指数日涨跌
m = 10 # 我们检验10个自相关系数

acf,q,p = sm.tsa.acf(data2,nlags=m,qstat=True)  ## 计算自相关系数 及p-value
out = np.c_[range(1,11), acf[1:], q, p]
output=pd.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')
print(output)

temp = np.array(data2) # 载入收益率序列
model = sm.tsa.AR(temp)  
results_AR = model.fit()  
plt.figure(figsize=(10,4))
plt.plot(temp,'b',label='CHGPct')
plt.plot(results_AR.fittedvalues, 'r',label='AR model')
plt.legend()

show()

print(len(results_AR.roots))

17

pi,sin,cos = np.pi,np.sin,np.cos
r1 = 1
theta = np.linspace(0,2*pi,360)
x1 = r1*cos(theta)
y1 = r1*sin(theta)
plt.figure(figsize=(6,6))
plt.plot(x1,y1,'k')  # 画单位圆
roots = 1/results_AR.roots  # 注意，这里results_AR.roots 是计算的特征方程的解，特征根应该取倒数
for i in range(len(roots)):
    plt.plot(roots[i].real,roots[i].imag,'.r',markersize=8)  #画特征根
show()

fig = plt.figure(figsize=(20,5))
ax1=fig.add_subplot(111)
fig = sm.graphics.tsa.plot_pacf(temp,ax=ax1)

aicList = []
bicList = []
hqicList = []
for i in range(1,11):  #从1阶开始算
    order = (i,0)  # 这里使用了ARMA模型，order 代表了模型的(p,q)值，我们令q始终为0，就只考虑了AR情况。
    tempModel = sm.tsa.ARMA(temp,order).fit()
    aicList.append(tempModel.aic)
    bicList.append(tempModel.bic)
    hqicList.append(tempModel.hqic)

plt.figure(figsize=(15,6))
plt.plot(aicList,'r',label='aic value')
plt.plot(bicList,'b',label='bic value')
plt.plot(hqicList,'k',label='hqic value')
plt.legend(loc=0)

show()

delta = results_AR.fittedvalues  - temp[17:]  # 残差
plt.figure(figsize=(10,6))

plt.plot(delta,'r',label=' residual error')
plt.legend(loc=0)

show()

acf,q,p = sm.tsa.acf(delta,nlags=10,qstat=True)  ## 计算自相关系数 及p-value
out = np.c_[range(1,11), acf[1:], q, p]
output=pd.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')
print(output)

score = 1 - delta.var()/temp[17:].var()
print(score)

0.0405231650285

train = temp[:-10]
test = temp[-10:]
output = sm.tsa.AR(train).fit()  
cc = output.predict()
print(cc)

predicts = output.predict(355, 364, dynamic=True)
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = temp[-10:]
comp['predict'] = predicts
print(comp)

data = np.array(IndexData['CHGPct']) # 上证指数日涨跌
IndexData['CHGPct'].plot(figsize=(15,5))

show()

fig = plt.figure(figsize=(20,5))
ax1=fig.add_subplot(111)
fig = sm.graphics.tsa.plot_acf(data,ax=ax1)

order = (0,10)
train = data[:-10]
test = data[-10:]
tempModel = sm.tsa.ARMA(train,order).fit()

delta = tempModel.fittedvalues - train
score = 1 - delta.var()/train.var()
print(score)

0.0278739998881

predicts = tempModel.predict(371, 380, dynamic=True)
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = test
comp['predict'] = predicts
comp.plot()

10

show()

data = np.array(IndexData['CHGPct']) # 上证指数日涨跌

fig = plt.figure(figsize=(20,10))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(data,lags=30,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(data,lags=30,ax=ax2)

print("AIC", sm.tsa.arma_order_select_ic(data,max_ar=6,max_ma=4,ic='aic')['aic_min_order'])  # AIC
print("BIC", sm.tsa.arma_order_select_ic(data,max_ar=6,max_ma=4,ic='bic')['bic_min_order'])  # BIC
print("HQIC", sm.tsa.arma_order_select_ic(data,max_ar=6,max_ma=4,ic='hqic')['hqic_min_order']) # HQIC

AIC (3, 3)

BIC (0, 0)

HQIC (0, 0)

order = (3,2)
train = data[:-10]
test = data[-10:]
tempModel = sm.tsa.ARMA(train,order).fit()

delta = tempModel.fittedvalues - train
score = 1 - delta.var()/train.var()
print(score)

0.0055187509265

predicts = tempModel.predict(371, 380, dynamic=True)
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = test
comp['predict'] = predicts
comp.plot()

10

show()

data2 = IndexData['closeIndex'] # 上证指数
data2.plot(figsize=(15,5))

show()

temp = np.array(data2)
t = sm.tsa.stattools.adfuller(temp)  # ADF检验
output=pd.DataFrame(index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used","Critical Value(1%)","Critical Value(5%)","Critical Value(10%)"],columns=['value'])
output['value']['Test Statistic Value'] = t[0]
output['value']['p-value'] = t[1]
output['value']['Lags Used'] = t[2]
output['value']['Number of Observations Used'] = t[3]
output['value']['Critical Value(1%)'] = t[4]['1%']
output['value']['Critical Value(5%)'] = t[4]['5%']
output['value']['Critical Value(10%)'] = t[4]['10%']
output

	value
Test Statistic Value 	-2.30472
p-value 	0.170449
Lags Used 	1
Number of Observations Used 	379
Critical Value(1%) 	-3.44772
Critical Value(5%) 	-2.8692
Critical Value(10%) 	-2.57085

data2Diff = data2.diff()  # 差分
data2Diff.plot(figsize=(15,5))

show()

temp = np.array(data2Diff)[1:] # 差分后第一个值为NaN,舍去
t = sm.tsa.stattools.adfuller(temp)  # ADF检验
print("p-value:   ",t[1])

p-value:    2.31245750144e-30

temp = np.array(data2Diff)[1:] # 差分后第一个值为NaN,舍去
fig = plt.figure(figsize=(20,10))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(temp,lags=30,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(temp,lags=30,ax=ax2)

sm.tsa.arma_order_select_ic(temp,max_ar=6,max_ma=4,ic='aic')['aic_min_order']  # AIC

(2, 2)

order = (2,2)
data = np.array(data2Diff)[1:] # 差分后，第一个值为NaN
rawdata = np.array(data2)
train = data[:-10]
test = data[-10:]
model = sm.tsa.ARMA(train,order).fit()

plt.figure(figsize=(15,5))
plt.plot(model.fittedvalues,label='fitted value')
plt.plot(train[1:],label='real value')
plt.legend(loc=0)

show()

delta = model.fittedvalues - train
score = 1 - delta.var()/train[1:].var()
print(score)

0.0397490021589

predicts = model.predict(10,381, dynamic=True)[-10:]
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = test
comp['predict'] = predicts
comp.plot(figsize=(8,5))

10

show()

rec = [rawdata[-11]]
pre = model.predict(371, 380, dynamic=True) # 差分序列的预测
for i in range(10):
    rec.append(rec[i]+pre[i])
plt.figure(figsize=(10,5))
plt.plot(rec[-10:],'r',label='predict value')
plt.plot(rawdata[-10:],'blue',label='real value')    
plt.legend(loc=0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6.10 优矿组合优化器使用文档


目录

    简介
    API
    示例

1. 简介

在多因子选股模型当中，常见的组合构建的方式为排序法和筛选法。排序法选出第几分位组的股票，然后进行简单的等权或者市值加权，筛选法会先对股票进行分层，在每一层里选出对应的第几分位组的股票。然而这两种方法在组合风险的控制上并不够精细，因此需要使用组合优化的算法来给出个股的权重。优矿的优化器正是为了实现这一功能而推出的。 优化器的模型大概可以用下面的数学式子进行表示：

我们做了些修改，将原先目标函数的二次项放在约束当中，省去了对风险厌恶系数的估计

上面的公式给了七个约束：

    个股权重约束:这是一个很明显的约束，因为A股市场不允许做空，所以我们个股的权重必须要控制在0到1之间
    权重之和约束:这个约束是强制的，它会使得我们组合最终的权重之和为1，即全额投资
    换手率约束:我们对换手率进行控制，换手率的计算公式为：

    ，注意这个约束带绝对值，求解起来要用特殊的方法
    风格因子约束：我们要控制组合在某些风格因子上的暴露
    行业因子约束：我们要控制组合在行业上的暴露
    风险约束：二次约束，用以约束组合的风险
    跟踪误差约束：二次约束，用以控制组合的跟踪误差，与风险约束的区别在于这里使用的是主动权重

2. API

创建一个优化器对象 UqerOptimizer(signal, construct_date, risk_model='short', benchmark_str='ZZ500', **kwargs) 释义：创建一个优化器对象 参数：

    signal(Series，dict，list，numpy.ndarray)：信号，可以是预期收益率。如果为Series，那么索引为str格式的secID，值为该期信号值；如果为dict，那么键为str格式的secID，值为该期信号值
    construct_date(str)：组合构建的日期，合理的格式为'YYYYMMDD'
    risk_model(str)：风险模型预测周期，可选的参数为'day'，'short'，'long'，默认为'short'
    benchmark_str(str)：指定基准，默认为中证500指数，允许的值包括，'ZZ500', 'HS300', 'SH50', 'SH180', 'SZZS'
    assets(Series，dict或者list)：用来导入上期的持仓权重，主要用于换手率约束当中。如果为Series，那么索引为股票名称，值为上期权重；如果为dict，那么键为股票名称，值为上期权重；

UqerOptimizer的相关属性

    assets(DataFrame)：一个index为股票代码，列为'init_weights','min','max'的DataFrame，用来记录初始权重，和权重上下限约束。
    optimal(bool)：记录组合优化的状态，默认为False，优化成功则为True
    construct_date：记录组合构建的日期
    risk_model_type(str)：用来记录风险模型存储的类型
    custom_constraints(dict)：用来记录用户传入的自定义约束，如果不传，则为None

UqerOptimizer的相关方法 add_constraints(name, **kwargs) 释义：添加约束 由于后面是可变参数，我们大概介绍该函数支持的添加约束的方式

    添加换手率约束：add_constraint(turnover_target)
        turnover_target(float)：指定组合的换手率上限
    添加个股权重约束：add_constraint(min_weights, max_weights, default_min_weight, default_max_weight)
        min_weights(pd.Series， dict)：如果为Series，index为股票，值为权重，如果为dict，键为str格式的ticker，值为权重，用来指定index所包含的股票的权重下限，可不输。
        max_weights(pd.Series， dict)：如果为Series，index为股票，值为权重，如果为dict，键为str格式的ticker，值为权重，用来指定index所包含的股票的权重上限，可不输。
        default_min_weight(float)：用来指定组合个股默认的权重下限，优先级低于min_weight
        default_max_weight(float)：用来指定组合个股默认的权重上限，优先级低于max_weight
    添加风格因子主动暴露约束：add_constraint(spec_style)
        style_value(dict): 用来设置风格因子约束，键为风格因子的名称，值为目标的主动暴露值(基准在创建优化器对象时指定)。风格因子只支持风险模型当中的风格因子：BETA， MOMENTUM， SIZE， EARNYILD， RESVOL， GROWTH， BTOP， LEVERAGE， LIQUIDTY， SIZENL。风格约束的值合理的值应在-3到3之间，具体要看universe。
    添加行业中性约束：add_constraint(is_industry_neutralize)
        is_industry_neutralize(bool):是否行业中性
    自定义行业约束：add_constraint(spec_indu)
        spec_indu(Series, dict):允许用户自己传入行业配置方案，键值为行业名称，value为用户自己配置的行业权重, 如果为字典，则index为secID。注意行业为申万一级行业分类，名称为中文，可以通过DataAPI中的行业分类获得
    添加风险约束：add_constraint(risk)
        risk(float):合理的值应大于0
    添加跟踪误差约束：add_constraint(tracking_error)
        tracking_error(float):合理的值应大于0
    添加自定义约束：add_constraint(custom_constraints)
        custom_constraints(dict):字典，包括三个键，
            'data'，表示传入的约束矩阵，不允许有缺失值，而且应该确保signal当中每个股票都有值，格式为DataFrame或Series，其中，index为股票的secID
            'upper'，list，np.array，记录约束的上限，长度与data的列长一致，注意，即使自定义约束只有一个，也烦请写在列表当中
            'lower'，list，np.array，记录约束的上限，其他同'upper'

另一种方式:add_constraint(is_industry_neutralize, turnover_target, max_weights, min_weights, default_max_weight, default_min_weight, spec_style, spec_industry, tracking_error, risk, custom_constraints)。 注意：两种方式必须输入参数名

solve() 释义：求解优化问题 会在assets属性当中加'optimal_weights'一列，如果求解成功，则该列为优化后的权重，否则，仍然返回上期权重。
3. 示例

这里，我们具体给出一个例子，用来介绍我们优化器的具体的用法
例：

import quartz_extensions.Optimizer.optimize as opt

# 获取信号
date = '20160930'
data = DataAPI.MktStockFactorsOneDayProGet(tradeDate=date,
                                        secID=set_universe('HS300', date),
                                        field=u"secID,tradeDate,OperatingProfitPS", pandas="1")
signal = (data.pivot(index='tradeDate', columns='secID', values='OperatingProfitPS').dropna(axis=1)).iloc[0, :]
signal = standardize(neutralize(winsorize(signal), date)).dropna()

# 创建优化器对象
pspec = opt.UqerOptimizer(signal, date, benchmark_str='HS300')
# 添加约束
# 个股上下限约束
pspec.add_constraint(default_min_weight=0., default_max_weight=0.05)
# 行业中性
pspec.add_constraint(is_industry_neutralize=True)

# 风格约束
pspec.add_constraint(spec_style={'SIZE':-0.05})
pspec.solve()
pspec.optimal
     

True

或者可以这样

# 创建优化器对象
pspec = opt.UqerOptimizer(signal, date, benchmark_str='HS300')
pspec.add_constraint(default_min_weight=0., default_max_weight=0.05, is_industry_neutralize=True, spec_style={'SIZE':-0.05})
pspec.solve()
pspec.optimal
     

True

优化后的结果

优化后的结果存在assets这个属性当中，我们可以大体上地看一部分股票的结果

weights = pspec.assets[pspec.assets.optimal_weights > 0.00001]
weights.head()
     
	init_weights 	max 	min 	optimal_weights
secID 				
000002.XSHE 	0.003333 	0.05 	0.0 	0.011507
000009.XSHE 	0.003333 	0.05 	0.0 	0.006025
000039.XSHE 	0.003333 	0.05 	0.0 	0.022808
000538.XSHE 	0.003333 	0.05 	0.0 	0.004430
000651.XSHE 	0.003333 	0.05 	0.0 	0.031614

这里，我们没有传入上一期权重，所以初始化了一个等权组合，如果要添加换手率约束，那么我们还需要在创建优化器对象时传入上一期的权重。
权重分布图

这里展示了权重大于0.00001的股票的权重的分布

from CAL.PyCAL import *
sns.set_style('white')
fig = plt.figure(figsize=(16,5))
ax = fig.add_subplot(111)
ax = weights.optimal_weights.plot(kind='bar', ax=ax)
ax.set_title(u'部分股票权重分布', fontproperties=font)
ax.set_xlabel(u'股票代码', fontproperties=font)
ax.set_ylabel(u'权重', fontproperties=font)
ax.grid()
     
行业分布比较

这里我们做的是行业中性，所以优化后组合的行业权重应与基准的行业权重一致

# 获得基准成分股行业分类
equ_indu = DataAPI.EquIndustryGet(industryVersionCD=u"010303", secID=set_universe('HS300', '20160930'), intoDate='20160930', field=u"secID,industryName1", pandas="1")
benchmark_equ_weight = DataAPI.IdxCloseWeightGet(ticker='000300', beginDate='20160930', endDate='20160930', field=u"consID,weight",pandas="1")
benchmark_equ_weight.rename(columns={'consID': 'secID', 'weight':u'基准行业权重'}, inplace=True)

# 获得基准行业权重
benchmark_indu_weight =equ_indu.merge(benchmark_equ_weight, on='secID', how='inner').groupby(by='industryName1').sum()/100
     

equ_indu_ = DataAPI.EquIndustryGet(industryVersionCD=u"010303", secID=list(pspec.assets.index), intoDate='20160930', field=u"secID,industryName1", pandas="1")
pspec_indu_weight=equ_indu_.merge(pspec.assets[['optimal_weights']], left_on='secID', right_index=True, how='inner').groupby(by='industryName1').sum()
pspec_indu_weight.rename(columns={'optimal_weights':u'组合行业权重'}, inplace=True)
     

data = pspec_indu_weight.merge(benchmark_indu_weight, left_index=True, right_index=True, how='inner')
fig = plt.figure(figsize=(16,5))
ax = fig.add_subplot(111)
ax = data.plot(kind='bar', ax=ax)
labels = [label.decode("utf-8") for label in data.index.values] 
ax.set_xticklabels(labels, fontproperties=font)
ax.legend(prop=font, loc='best')
ax.set_xlabel(u'行业名称', fontproperties=font)
ax.set_ylabel(u'权重', fontproperties=font)
ax.grid()
     

可以看到，添加行业中性约束后，优化器能够将组合的行业权重和基准的行业权重的分布变得基本一样。
版本历史

V1.0，2017-06-15，文章上线 V1.1，2017-12-26，增加跟踪误差约束 V1.2，2018-02-26，调整指数成份股接口为 DataAPI.IdxCloseWeightGet

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 6.11 Greeks和隐含波动率微笑



在本文中，我们将通过优矿提供的数据，计算上证50ETF期权的隐含波动率微笑。
目录

    数据准备
    Greeks和隐含波动率计算
    隐含波动率微笑


from CAL.PyCAL import *
from matplotlib import rc
rc('mathtext', default='regular')
sns.set_style('white')
from scipy import interpolate
from scipy.stats import mstats
from pandas import Series, DataFrame, concat
from matplotlib import dates
     
1. 数据准备

上海银行间同业拆借利率SHIBOR，用来作为无风险利率参考。

## 银行间质押式回购利率
def getHistDayInterestRateInterbankRepo(date):
    cal = Calendar('China.SSE')
    period = Period('-10B')
    begin = cal.advanceDate(date, period)
    begin_str = begin.toISO().replace('-', '')
    date_str = date.toISO().replace('-', '')
    # 以下的indicID分别对应的银行间质押式回购利率周期为：
    # 1D, 7D, 14D, 21D, 1M, 3M, 4M, 6M, 9M, 1Y
    indicID = [u"1090000566", u"1090000567", u"1090000568", u"1090000569", u"1090000570", 
               u"1090000571", u"1090000572", u"1090000573", u"1090000574", u"1090000575"]
    
    period = np.asarray([1.0, 7.0, 14.0, 21.0, 30.0, 90.0, 120.0, 180.0, 270.0, 360.0]) / 360.0
    period_matrix = pd.DataFrame(index=indicID, data=period, columns=['period'])
    field = [u"indicID",u"publishDate",u"periodDate",u"dataValue"]
    interbank_repo = DataAPI.EcoDataProGet(indicID, begin_str, date_str)
    interbank_repo = interbank_repo.groupby('indicID').first()
    interbank_repo.index = [str(i) for i in interbank_repo.index]
    interbank_repo = concat([interbank_repo, period_matrix], axis=1, join='inner').sort_index()
    return interbank_repo

## 银行间同业拆借利率
def getHistDaySHIBOR(date):
    date_str = date.toISO().replace('-', '')
    # 以下的indicID分别对应的SHIBOR周期为：
    # 1D, 7D, 14D, 1M, 3M, 6M, 9M, 1Y
    indicID = [u'1090000537',u'1090000538',u'1090000539',u'1090000540',
               u'1090000541',u'1090000542',u'1090000543',u'1090000544']
    period = np.asarray([1.0, 7.0, 14.0, 30.0, 90.0, 180.0, 270.0, 360.0]) / 360.0
    period_matrix = pd.DataFrame(index=indicID, data=period, columns=['period'])
    field = [u"indicID",u"publishDate",u"periodDate",u"dataValue"]
    interest_shibor = DataAPI.EcoDataProGet(indicID, beginDate=date_str, endDate=date_str)[field]
    interest_shibor = interest_shibor.set_index('indicID')
    interest_shibor.index = [str(i) for i in interest_shibor.index]
    interest_shibor = concat([interest_shibor, period_matrix], axis=1, join='inner').sort_index()
    return interest_shibor

## 插值得到给定的周期的无风险利率
def periodsSplineRiskFreeInterestRate(date, periods):
    # 此处使用SHIBOR来插值
    init_shibor = getHistDaySHIBOR(date)
    
    shibor = {}
    min_period = min(init_shibor.period.values)
    min_period = 25.0/360.0
    max_period = max(init_shibor.period.values)
    for p in periods.keys():
        tmp = periods[p]
        if periods[p] > max_period:
            tmp = max_period * 0.99999
        elif periods[p] < min_period:
            tmp = min_period * 1.00001
        sh = interpolate.spline(init_shibor.period.values, init_shibor.dataValue.values, [tmp], order=3)
        shibor[p] = sh[0]/100.0
    return shibor
     
2. Greeks和隐含波动率计算

本文中计算的Greeks包括：

    delta 期权价格关于标的价格的一阶导数
    gamma 期权价格关于标的价格的二阶导数
    rho 期权价格关于无风险利率的一阶导数
    theta 期权价格关于到期时间的一阶导数
    vega 期权价格关于波动率的一阶导数

注意：

    计算隐含波动率，我们采用Black-Scholes-Merton模型，此模型在平台Python包CAL中已有实现
    无风险利率使用SHIBOR
    期权的时间价值为负时(此种情况在50ETF期权里时有发生)，没法通过BSM模型计算隐含波动率，故此时将期权隐含波动率设为0.0，实际上，此时的隐含波动率和各风险指标并无实际参考价值


## 使用DataAPI.OptGet, DataAPI.MktOptdGet拿到计算所需数据
def getOptDayData(opt_var_sec, date):
    date_str = date.toISO().replace('-', '')

    #使用DataAPI.OptGet，拿到已退市和上市的所有期权的基本信息
    info_fields = [u'optID', u'varSecID', u'varShortName', u'varTicker', u'varExchangeCD', u'varType', 
                   u'contractType', u'strikePrice', u'contMultNum', u'contractStatus', u'listDate', 
                   u'expYear', u'expMonth', u'expDate', u'lastTradeDate', u'exerDate', u'deliDate', 
                   u'delistDate']
    opt_info = DataAPI.OptGet(optID='', contractStatus=[u"DE",u"L"], field=info_fields, pandas="1")

    #使用DataAPI.MktOptdGet，拿到历史上某一天的期权成交信息
    mkt_fields = [u'ticker', u'optID', u'secShortName', u'exchangeCD', u'tradeDate', u'preSettlePrice', 
                  u'preClosePrice', u'openPrice', u'highestPrice', u'lowestPrice', u'closePrice', 
                  u'settlPrice', u'turnoverVol', u'turnoverValue', u'openInt']
    opt_mkt = DataAPI.MktOptdGet(tradeDate=date_str, field=mkt_fields, pandas = "1")

    opt_info = opt_info.set_index(u"optID")
    opt_mkt = opt_mkt.set_index(u"optID")
    opt = concat([opt_info, opt_mkt], axis=1, join='inner').sort_index()
    return opt
    
## 分析历史某一日的期权收盘价信息，得到隐含波动率微笑和期权风险指标
def getOptDayAnalysis(opt_var_sec, date):
    opt = getOptDayData(opt_var_sec, date)
    
    #使用DataAPI.MktFunddGet拿到期权标的的日行情
    date_str = date.toISO().replace('-', '')
    opt_var_mkt = DataAPI.MktFunddGet(secID=opt_var_sec,tradeDate=date_str,beginDate=u"",endDate=u"",field=u"",pandas="1")
    #opt_var_mkt = DataAPI.MktFunddAdjGet(secID=opt_var_sec,beginDate=date_str,endDate=date_str,field=u"",pandas="1")

    # 计算shibor
    exp_dates_str = opt.expDate.unique()
    periods = {}
    for date_str in exp_dates_str:
        exp_date = Date.parseISO(date_str)
        periods[exp_date] = (exp_date - date)/360.0
    shibor = periodsSplineRiskFreeInterestRate(date, periods)
    
    settle = opt.settlPrice.values         # 期权 settle price
    close = opt.closePrice.values          # 期权 close price
    strike = opt.strikePrice.values        # 期权 strike price
    option_type = opt.contractType.values  # 期权类型
    exp_date_str = opt.expDate.values      # 期权行权日期
    eval_date_str = opt.tradeDate.values   # 期权交易日期

    mat_dates = []
    eval_dates = []
    spot = []
    for epd, evd in zip(exp_date_str, eval_date_str):
        mat_dates.append(Date.parseISO(epd))
        eval_dates.append(Date.parseISO(evd))
        spot.append(opt_var_mkt.closePrice[0])
    time_to_maturity = [float(mat - eva + 1.0)/365.0 for (mat, eva) in zip(mat_dates, eval_dates)]

    risk_free = []  # 无风险利率
    for s, mat, time in zip(spot, mat_dates, time_to_maturity):
        #rf = math.log(forward_price[mat] / s) / time
        rf = shibor[mat]
        risk_free.append(rf)

    opt_types = []   # 期权类型
    for t in option_type:
        if t == 'CO':
            opt_types.append(1)
        else:
            opt_types.append(-1)
    
    # 使用通联CAL包中 BSMImpliedVolatity 计算隐含波动率
    calculated_vol = BSMImpliedVolatity(opt_types, strike, spot, risk_free, 0.0, time_to_maturity, settle)
    calculated_vol = calculated_vol.fillna(0.0)

    # 使用通联CAL包中 BSMPrice 计算期权风险指标
    greeks = BSMPrice(opt_types, strike, spot, risk_free, 0.0, calculated_vol.vol.values, time_to_maturity)
    greeks.vega = greeks.vega #/ 100.0
    greeks.rho = greeks.rho #/ 100.0
    greeks.theta = greeks.theta #* 365.0 / 252.0 #/ 365.0
    
    opt['strike'] = strike
    opt['optType'] = option_type
    opt['expDate'] = exp_date_str
    opt['spotPrice'] = spot
    opt['riskFree'] = risk_free
    opt['timeToMaturity'] = np.around(time_to_maturity, decimals=4)
    opt['settle'] = np.around(greeks.price.values.astype(np.double), decimals=4)
    opt['iv'] = np.around(calculated_vol.vol.values.astype(np.double), decimals=4)
    opt['delta'] = np.around(greeks.delta.values.astype(np.double), decimals=4)
    opt['vega'] = np.around(greeks.vega.values.astype(np.double), decimals=4)
    opt['gamma'] = np.around(greeks.gamma.values.astype(np.double), decimals=4)
    opt['theta'] = np.around(greeks.theta.values.astype(np.double), decimals=4)
    opt['rho'] = np.around(greeks.rho.values.astype(np.double), decimals=4)
    
    fields = [u'ticker', u'contractType', u'strikePrice', u'expDate', u'tradeDate', 
              u'closePrice', u'settlPrice', 'spotPrice', u'iv', 
              u'delta', u'vega', u'gamma', u'theta',  u'rho']
    opt = opt[fields].reset_index().set_index('ticker').sort_index()
    #opt['iv'] = opt.iv.replace(to_replace=0.0, value=np.nan)
    return opt

     

尝试用getOptDayAnalysis计算2015-09-24这一天的风险指标

# Uqer 计算期权的风险数据
opt_var_sec = u"510050.XSHG"    # 期权标的
date = Date(2015, 9, 24)

option_risk = getOptDayAnalysis(opt_var_sec, date)
option_risk.head(2)
     
	optID 	contractType 	strikePrice 	expDate 	tradeDate 	closePrice 	settlPrice 	spotPrice 	iv 	delta 	vega 	gamma 	theta 	rho
ticker 														
510050C1510M01850 	10000405 	CO 	1.85 	2015-10-28 	2015-09-24 	0.3268 	0.3555 	2.187 	0.4317 	0.9101 	0.1099 	0.5550 	-0.2992 	0.1568
510050C1510M01900 	10000406 	CO 	1.90 	2015-10-28 	2015-09-24 	0.2791 	0.3102 	2.187 	0.4161 	0.8810 	0.1347 	0.7058 	-0.3435 	0.1550

getOptDayAnalysis函数计算结果展示

# 本文计算结果 option_risk 

near_exp = np.sort(option_risk.expDate.unique())[0]    # 近月期权行权日

opt_call_uqer = option_risk[option_risk.expDate==near_exp][option_risk.contractType=='CO'].set_index('strikePrice')
opt_put_uqer = option_risk[option_risk.expDate==near_exp][option_risk.contractType=='PO'].set_index('strikePrice')

## ----------------------------------------------
## 风险指标
fig = plt.figure(figsize=(10,12))
fig.set_tight_layout(True)

# ------ Delta ------
ax = fig.add_subplot(321)
ax.plot(opt_call_uqer.index, opt_call_uqer['delta'], '-o')
ax.plot(opt_put_uqer.index, opt_put_uqer['delta'], '-o')
ax.legend(['call-uqer', 'put-uqer'])
ax.grid()
ax.set_xlabel(u"strikePrice")
ax.set_ylabel(r"Delta")
plt.title('Delta Comparison')

# ------ Theta ------
ax = fig.add_subplot(322)
ax.plot(opt_call_uqer.index, opt_call_uqer['theta'], '-o')
ax.plot(opt_put_uqer.index, opt_put_uqer['theta'], '-o')
ax.legend(['call-uqer', 'put-uqer'])
ax.grid()
ax.set_xlabel(u"strikePrice")
ax.set_ylabel(r"Theta")
plt.title('Theta Comparison')

# ------ Gamma ------
ax = fig.add_subplot(323)
ax.plot(opt_call_uqer.index, opt_call_uqer['gamma'], '-o')
ax.plot(opt_put_uqer.index, opt_put_uqer['gamma'], '-o')
ax.legend(['call-uqer', 'put-uqer'], loc=0)
ax.grid()
ax.set_xlabel(u"strikePrice")
ax.set_ylabel(r"Gamma")
plt.title('Gamma Comparison')

# # ------ Vega ------
ax = fig.add_subplot(324)
ax.plot(opt_call_uqer.index, opt_call_uqer['vega'], '-o')
ax.plot(opt_put_uqer.index, opt_put_uqer['vega'], '-o')
ax.legend(['call-uqer',  'put-uqer'], loc=4)
ax.grid()
ax.set_xlabel(u"strikePrice")
ax.set_ylabel(r"Vega")
plt.title('Vega Comparison')

# ------ Rho ------
ax = fig.add_subplot(325)
ax.plot(opt_call_uqer.index, opt_call_uqer['rho'], '-o')
ax.plot(opt_put_uqer.index, opt_put_uqer['rho'], '-o')
ax.legend(['call-uqer', 'put-uqer'], loc=3)
ax.grid()
ax.set_xlabel(u"strikePrice")
ax.set_ylabel(r"Rho")
plt.title('Rho Comparison')
     
show()

上述五张图中，对于近月期权，我们分别对比了五个Greeks风险指标：Delta，Theta，Gamma，Vega，Rho：

    每张图中，Call和Put分开比较，横轴为行权价
    可以看出，本文中的计算结果和上交所的参考数值符合的比较好
    在接下来的50ETF期权分析中，我们将使用本文中的计算方法来计算期权隐含波动率和Greeks风险指标

把上面的数据整理整理，格式更简洁一点

# 每日期权分析数据整理
def getOptDayGreeksIV(date):
    # Uqer 计算期权的风险数据
    opt_var_sec = u"510050.XSHG"    # 期权标的
    opt = getOptDayAnalysis(opt_var_sec, date)
    
    # 整理数据部分
    opt.index = [index[-10:] for index in opt.index]
    opt = opt[['contractType','strikePrice','expDate','closePrice','iv','delta','theta','gamma','vega','rho']]
    opt_call = opt[opt.contractType=='CO']
    opt_put = opt[opt.contractType=='PO']
    opt_call.columns = pd.MultiIndex.from_tuples([('Call', c) for c in opt_call.columns])
    opt_call[('Call-Put', 'strikePrice')] = opt_call[('Call', 'strikePrice')]
    opt_put.columns = pd.MultiIndex.from_tuples([('Put', c) for c in opt_put.columns])
    opt = concat([opt_call, opt_put], axis=1, join='inner').sort_index()
    opt = opt.set_index(('Call','expDate')).sort_index()
    opt = opt.drop([('Call','contractType'), ('Call','strikePrice')], axis=1)
    opt = opt.drop([('Put','expDate'), ('Put','contractType'), ('Put','strikePrice')], axis=1)
    opt.index.name = 'expDate'
    ## 以上得到完整的历史某日数据，格式简洁明了
    return opt
     

date = Date(2015, 9, 24)

option_risk = getOptDayGreeksIV(date)
option_risk.head(10)
     
	Call 	Call-Put 	Put
	closePrice 	iv 	delta 	theta 	gamma 	vega 	rho 	strikePrice 	closePrice 	iv 	delta 	theta 	gamma 	vega 	rho
expDate 															
2015-10-28 	0.3268 	0.4317 	0.9101 	-0.2992 	0.5550 	0.1099 	0.1568 	1.85 	0.0129 	0.4319 	-0.0900 	-0.2410 	0.5551 	0.1100 	-0.0201
2015-10-28 	0.2791 	0.4161 	0.8810 	-0.3435 	0.7058 	0.1347 	0.1550 	1.90 	0.0176 	0.4174 	-0.1197 	-0.2854 	0.7063 	0.1352 	-0.0268
2015-10-28 	0.2360 	0.3990 	0.8449 	-0.3862 	0.8823 	0.1615 	0.1517 	1.95 	0.0232 	0.3992 	-0.1552 	-0.3247 	0.8822 	0.1615 	-0.0348
2015-10-28 	0.1955 	0.1811 	0.9532 	-0.1225 	0.7980 	0.0663 	0.1811 	2.00 	0.0345 	0.4020 	-0.2105 	-0.3940 	1.0601 	0.1954 	-0.0474
2015-10-28 	0.1599 	0.2453 	0.8237 	-0.2764 	1.5588 	0.1754 	0.1574 	2.05 	0.0474 	0.3975 	-0.2703 	-0.4441 	1.2290 	0.2241 	-0.0612
2015-10-28 	0.1275 	0.2698 	0.7137 	-0.3696 	1.8625 	0.2304 	0.1374 	2.10 	0.0643 	0.3952 	-0.3381 	-0.4847 	1.3660 	0.2476 	-0.0771
2015-10-28 	0.0990 	0.2814 	0.6081 	-0.4208 	2.0162 	0.2602 	0.1180 	2.15 	0.0869 	0.4013 	-0.4114 	-0.5200 	1.4317 	0.2635 	-0.0946
2015-10-28 	0.0768 	0.2955 	0.5057 	-0.4489 	1.9934 	0.2701 	0.0987 	2.20 	0.1146 	0.4121 	-0.4836 	-0.5428 	1.4284 	0.2699 	-0.1124
2015-10-28 	0.0584 	0.3068 	0.4132 	-0.4487 	1.8746 	0.2637 	0.0810 	2.25 	0.1450 	0.4200 	-0.5517 	-0.5438 	1.3908 	0.2679 	-0.1296
2015-10-28 	0.0470 	0.3264 	0.3381 	-0.4434 	1.6538 	0.2476 	0.0664 	2.30 	0.1826 	0.4426 	-0.6091 	-0.5520 	1.2809 	0.2600 	-0.1452
3. 隐含波动率微笑

利用上一小节的代码，给出隐含波动率微笑结构

隐含波动率微笑

# 做图展示某一天的隐含波动率微笑
def plotSmileVolatility(date):
    # Uqer 计算期权的风险数据
    opt = getOptDayGreeksIV(date)
    
    # 下面展示波动率微笑
    exp_dates = np.sort(opt.index.unique())
    ## ----------------------------------------------
    fig = plt.figure(figsize=(10,8))
    fig.set_tight_layout(True)
    
    for i in range(exp_dates.shape[0]):
        date = exp_dates[i]
        ax = fig.add_subplot(2,2,i+1)
        opt_date = opt[opt.index==date].set_index(('Call-Put', 'strikePrice'))
        opt_date.index.name = 'strikePrice'
        
        ax.plot(opt_date.index, opt_date[('Call', 'iv')], '-o')
        ax.plot(opt_date.index, opt_date[('Put', 'iv')], '-s')
        ax.legend(['call', 'put'], loc=0)
        ax.grid()
        ax.set_xlabel(u"strikePrice")
        ax.set_ylabel(r"Implied Volatility")
        plt.title(exp_dates[i])
    
     

plotSmileVolatility(Date(2015,9,24))
     

行权价和行权日期两个方向上的隐含波动率微笑

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# 做图展示某一天的隐含波动率结构
def plotSmileVolatilitySurface(date):
    # Uqer 计算期权的风险数据
    opt = getOptDayGreeksIV(date)
    
    # 下面展示波动率结构
    exp_dates = np.sort(opt.index.unique())
    strikes = np.sort(opt[('Call-Put', 'strikePrice')].unique())
    risk_mt = {'Call': pd.DataFrame(index=strikes),
               'Put': pd.DataFrame(index=strikes) }
    
    # 将数据整理成Call和Put分开来，分别的结构为：
    # 行为行权价，列为剩余到期天数（以自然天数计算）
    for epd in exp_dates:
        exp_days = Date.parseISO(epd) - date
        opt_date = opt[opt.index==epd].set_index(('Call-Put', 'strikePrice'))
        opt_date.index.name = 'strikePrice'
        for cp in risk_mt.keys():
            risk_mt[cp][exp_days] = opt_date[(cp, 'iv')]
    for cp in risk_mt.keys():
        for strike in risk_mt[cp].index:
            if np.sum(np.isnan(risk_mt[cp].ix[strike])) > 0:
                risk_mt[cp] = risk_mt[cp].drop(strike)
                
    # Call和Put分开显示，行index为行权价，列index为剩余到期天数
    #print risk_mt
    
    # 画图
    for cp in ['Call', 'Put']:
        opt = risk_mt[cp]
        x = []
        y = []
        z = []
        for xx in opt.index:
            for yy in opt.columns:
                x.append(xx)
                y.append(yy)
                z.append(opt[yy][xx])        
        fig = plt.figure(figsize=(10,8))
        fig.suptitle(cp)
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
    return risk_mt
     

画出某一天的波动率微笑曲面结构

opt = plotSmileVolatilitySurface(Date(2015,9,24))
opt  # Call和Put分开显示，行index为行权价，列index为剩余到期天数
     

{'Call':          34      62      90      181
 2.10  0.2698  0.2817  0.2823  0.3042
 2.15  0.2814  0.2888  0.2916  0.3063
 2.20  0.2955  0.3008  0.2922  0.3237
 2.25  0.3068  0.3067  0.3093  0.3157
 2.30  0.3264  0.3155  0.3128  0.3172,
 'Put':          34      62      90      181
 2.10  0.3952  0.4403  0.4740  0.4449
 2.15  0.4013  0.4442  0.4794  0.4632
 2.20  0.4121  0.4498  0.4802  0.4451
 2.25  0.4200  0.4581  0.4863  0.4547
 2.30  0.4426  0.4673  0.4893  0.4691}

波动率曲面结构图中：

    上图为Call，下图为Put，此处没有进行任何插值处理，所以略显粗糙
    Put的隐含波动率明显大于Call
    期限结构来说，波动率呈现远高近低的特征

版本历史

V1.0，2016-10-15，文章上线

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

ddddddddddddddddddddddddddd


