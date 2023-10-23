"""scopetest: 可視範圍測試模組"""
v = 6
def f(x):
    """f: scope test function"""
    print("global: ", list(globals().keys()))
    print("進入 local:", locals())
    y = x
    w = v
    print("離開 local:", locals().keys())