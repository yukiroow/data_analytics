# Dominguez, Harry Jr
# Lapig, Cazandra Jae
# 9463 - IT 322
# Prelim Activity 2

import pandas as panda

stocks = class_data = panda.read_csv("prelimact2/stocks.csv")

# Google - ggl, Microsoft - mcsft
ggl_stocks = stocks["Stock Price Google"]
mcsft_stocks = stocks["Stock Price Microsoft"]

# Mean
ggl_mean = ggl_stocks.mean()
mcsft_mean = mcsft_stocks.mean()

# Median
ggl_median = ggl_stocks.median()
mcsft_median = mcsft_stocks.median()

# Mode
ggl_mode = (
    None
    if ggl_stocks.size == ggl_stocks.mode().size
    else ggl_stocks.mode()
)
mcsft_mode = (
    None
    if mcsft_stocks.size == mcsft_stocks.mode().size
    else mcsft_stocks.mode()
)

# Quartiles
# .25 - 1st Quartile, .75 - 2nd Quartile
ggl_quartiles = ggl_stocks.quantile([0.25, 0.75])
mcsft_quartiles = mcsft_stocks.quantile([0.25, 0.75])

# Percentiles
# .05 - 5th Percentile, .95 - 95th Percentile
ggl_percentiles = ggl_stocks.quantile([0.05, 0.95])
mcsft_percentiles = mcsft_stocks.quantile([0.05, 0.95])

# Variance
ggl_var = ggl_stocks.var(ddof = 0)
mcsft_var = mcsft_stocks.var(ddof = 0)

# Standard Deviation
ggl_std = ggl_stocks.std(ddof = 0)
mcsft_std = mcsft_stocks.std(ddof = 0)

# Coefficient of Variation
ggl_coeffvar = ggl_std / ggl_mean
mcsft_coeffvar = mcsft_std / mcsft_mean
