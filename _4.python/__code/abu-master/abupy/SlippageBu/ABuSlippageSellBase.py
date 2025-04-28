# -*- encoding:utf-8 -*-
"""
    日内滑点卖出价格决策基础模块：暂时迁移简单实现方式，符合回测需求，如迁移实盘模块
    需添加日内择时策略，通过日内分钟k线，实现日内分钟k线择时，更微观的
    实现日内择时滑点功能，不考虑大资金的冲击成本及系统外的大幅滑点
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from abc import ABCMeta, abstractmethod
import functools

import numpy as np

from ..CoreBu.ABuFixes import six

__author__ = '阿布'
__weixin__ = 'abu_quant'


class AbuSlippageSellBase(six.with_metaclass(ABCMeta, object)):
    """非高频日内滑点卖出决策抽象基类"""

    def __init__(self, kl_pd_sell, factor_name):
        """
        :param kl_pd_sell: 交易当日的交易数据
        :param factor_name: ABuFactorSellBase实例对象的factor_name
        """
        self.sell_price = np.inf
        self.kl_pd_sell = kl_pd_sell
        self.factor_name = factor_name

    def fit(self):
        """做基础验证比如今天是否停盘后调用fit_price"""
        if self.kl_pd_sell.empty or self.kl_pd_sell.volume == 0:
            # 卖出时负无穷为放弃单子
            return -np.inf

        return self.fit_price()

    @abstractmethod
    def fit_price(self):
        """
        子类主要需要实现的函数，决策交易当日的最终卖出价格
        :return: 最终决策的当前交易卖出价格
        """
        pass

"""是否开启跌停板滑点卖出价格特殊处理，默认关闭，外部修改如：abupy.slippage.ssb.g_enable_limit_down = True"""
g_enable_limit_down = False
"""
    初始设定跌停板卖出成交概率100%，这里也可以在计算完一次概率后，再使用成交量做二次概率计算，
    外部修改如：abupy.slippage.ssb.g_limit_down_deal_chance = 0.5，即修改为50%成功卖出概率
"""
g_limit_down_deal_chance = 1
"""在集合竞价阶段价格已达成跌停的情况下卖出成功的概率，默认0.2, 即20%成功概率"""
g_pre_limit_down_rate = 0.2


def slippage_limit_down(func):
    """
        针对a股跌停板卖出价格决策的装饰器，子类可选择装饰与不装饰在fit_price上
        如果是实盘策略中，使用分钟k线，及日内择时策略子策略，即不需特别处理。
        回测中需要特别处理，处理卖出成功概率，根据概率决定是否能卖出，
        及跌停下的卖出价格决策，跌停下卖出价格模型为，越靠近跌停板价格
        卖出成交概率越大, 即在跌停下预期以靠近跌停价格卖出，缺点是使用了随机数，
        导致回测结果将出现不一致的情况
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if g_enable_limit_down and self.kl_pd_sell.p_change <= -10 and self.kl_pd_sell.low == self.kl_pd_sell.close:
            """
                跌停板命中后需要根据跌停板买入成交概率(g_limit_down_deal_chance)来作为
                二项式分布的概率值计算卖出成功概率
            """

            if self.kl_pd_sell.high == self.kl_pd_sell.low:
                # 10个点，且最高＝最低，即a股在集合竞价阶段达成跌停，卖出成功概率降低到g_limit_down_deal_chance * 0.2
                # TODO 这个概率最好使用成交量当日来计算出来
                limit_down_deal_chance = g_limit_down_deal_chance * g_pre_limit_down_rate
            else:
                limit_down_deal_chance = g_limit_down_deal_chance

            deal = np.random.binomial(1, limit_down_deal_chance)
            if deal:
                # 卖出成功后需要进一步决策价位，首选arange出一个从高到跌停价格的序列，间隔-0.01
                if self.kl_pd_sell.high == self.kl_pd_sell.low:
                    return self.kl_pd_sell.low

                price_hl = np.arange(self.kl_pd_sell.high, self.kl_pd_sell.low, -0.01)
                hl_chance = np.linspace(0, 1, len(price_hl))
                # noinspection PyUnresolvedReferences
                p = hl_chance / hl_chance.sum()
                # 最后使用随机加权概率抽取，选中一个卖出价格
                return np.random.choice(price_hl, 1, p=p)[0]
            # 没能成交返回负无穷
            return -np.inf
        else:
            return func(self, *args, **kwargs)
    return wrapper
