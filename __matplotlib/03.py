import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# 日期列表
events = [
    datetime.date(2015, 1, 23),
    datetime.date(2015, 1, 28),
    datetime.date(2015, 2, 3),
    datetime.date(2015, 2, 21),
    datetime.date(2015, 3, 15),
    datetime.date(2015, 3, 24),
    datetime.date(2015, 4, 8),
    datetime.date(2015, 4, 24),
]

# 阅读量
readings = [12, 22, 25, 20, 18, 15, 17, 14]

# 需要引入matplotlib.dates模块
months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%Y-%m')

fig, ax = plt.subplots()

# 生成图形，默认情况下生成的图形日期可读性非常差（挤在一块）
plt.plot(events, readings)

# X轴将只显示"年-月"
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)

# 显示图形
plt.show()
