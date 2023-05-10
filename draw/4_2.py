from pyecharts import options as opts
from pyecharts.charts import Geo
import pandas as pd
import numpy as np

lf_loc = pd.read_csv('data/lf_loc.csv')

def block_map(title) -> Geo:
    geo = Geo()
    geo.add_schema(maptype="廊坊")
    for i in lf_loc.itertuples():
        geo.add_coordinate(getattr(i, 'name'), getattr(i, 'x'), getattr(i, 'y'))
    geo.add(
        title, [tuple(z) for z in zip(lf_loc['name'], lf_loc['avg'])],
        # type_=ChartType.EFFECT_SCATTER,
        label_opts=opts.LabelOpts(is_show=False))
    geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=np.max(list(lf_loc['avg']))),
                     title_opts=opts.TitleOpts(title="廊坊市各板块租房单位面积均价"))
    return geo


block_map('单位面积租价(元)').render('assets/lf_block.html')


