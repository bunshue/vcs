import network

def collect_gc():
    import gc
    gc.collect()
    gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

wlan = network.WLAN(network.STA_IF)
wlan.disconnect()
collect_gc()
