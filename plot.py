# -*- coding: utf-8 -*-
"""A plotting utility for conference stats
"""
# Author: Yue Zhao <yuezhao@cs.toronto.edu>
# License: BSD 2 clause


import numpy as np
import matplotlib.pyplot as plt

import matplotlib

# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

n_groups = 6

submitted_2016 = np.asarray([784, 370, 904, 701, 353, 368, 307])
accepted_2016 = np.asarray([142, 96, 178, 160, 100, 67, 91])
rejected_2016 = submitted_2016 - accepted_2016
accp_rate_2016 = np.rint((accepted_2016 / submitted_2016) * 100).astype(int)

submitted_2017 = np.asarray([748, 358, 778, 855, 364, 505, 458])
accepted_2017 = np.asarray([130, 93, 155, 171, 104, 80, 129])
rejected_2017 = submitted_2017 - accepted_2017
accp_rate_2017 = np.rint((accepted_2017 / submitted_2017) * 100).astype(int)

submitted_2018 = np.asarray([983, 374, 948, 826, 354, 514, 592])
accepted_2018 = np.asarray([181, 86, 188, 147, 94, 84, 164])
rejected_2018 = submitted_2018 - accepted_2018
accp_rate_2018 = np.rint((accepted_2018 / submitted_2018) * 100).astype(int)

fig, ax = plt.subplots()

fig.set_size_inches(12, 8)

index = np.arange(n_groups)
bar_width = 0.28

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects2016_rejected = ax.bar(index,
                            rejected_2016,
                            bar_width,
                            alpha=opacity,
                            color='darkred',
                            error_kw=error_config,
                            label='2016_rejected')

rects2016_accepted = ax.bar(index,
                            accepted_2016,
                            bar_width,
                            bottom=rejected_2016,
                            alpha=opacity,
                            color='red',
                            error_kw=error_config,
                            label='2016_accepted')

rects2016 = ax.bar(index,
                   submitted_2016,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2016'
                   )

rects2017_rejected = ax.bar(index + bar_width,
                            rejected_2017,
                            bar_width,
                            alpha=opacity,
                            color='darkgreen',
                            error_kw=error_config,
                            label='2017_rejected')

rects2017_accepted = ax.bar(index + bar_width,
                            accepted_2017,
                            bar_width,
                            bottom=rejected_2017,
                            alpha=opacity,
                            color='mediumseagreen',
                            error_kw=error_config,
                            label='2017_accepted')

rects2017 = ax.bar(index + bar_width,
                   submitted_2017,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2017'
                   )

rects2018_rejected = ax.bar(index + bar_width * 2,
                            rejected_2018,
                            bar_width,
                            alpha=opacity,
                            color='darkblue',
                            error_kw=error_config,
                            label='2018_rejected')

rects2018_accepted = ax.bar(index + bar_width * 2,
                            accepted_2018,
                            bar_width,
                            bottom=rejected_2018,
                            alpha=opacity,
                            color='slateblue',
                            error_kw=error_config,
                            label='2018_accepted')

rects2018 = ax.bar(index + bar_width * 2,
                   submitted_2018,
                   bar_width,
                   alpha=0.2,
                   color='white',
                   error_kw=error_config,
                   #                label='2018'
                   )

ax.set_xlabel('Major Data Minining Conferences', fontsize=15)
ax.set_ylabel('# Papers & Acceptance Rate', fontsize=15)
ax.set_title('Conference Statistics (2016-2018)', fontsize=18)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('KDD', 'SDM', 'ICDM', 'CIKM', 'PKDD', 'WSDM', 'PAKDD'))
ax.legend()


def autolabel(rects, accp_rates, accps, rejs):
    """
    Attach a text label above each bar displaying relevant information
    """
    for rect, accp_rate, accp, rej in zip(rects, accp_rates, accps, rejs):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 10,
                str(accp_rate) + '%',
                ha='center', va='bottom')
        ax.text(rect.get_x() + rect.get_width() / 2., 0.9 * height,
                '%d' % int(accp),
                ha='center', va='bottom')
        ax.text(rect.get_x() + rect.get_width() / 2., 0.4 * height,
                '%d' % int(rej),
                ha='center', va='bottom')


autolabel(rects2016, accp_rate_2016, accepted_2016, rejected_2016)
autolabel(rects2017, accp_rate_2017, accepted_2017, rejected_2017)
autolabel(rects2018, accp_rate_2018, accepted_2018, rejected_2018)
plt.savefig('conference_stats.png', dpi=330)
plt.show()
