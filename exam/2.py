# -*- coding:utf-8 -*-

# 人口普查是一项重要的国情调查，对于国家管理、制定各项方针政策具有重要的意义，中国最早的一次人口普查在西汉汉平帝元始二年进行，
# 而自中华人民共和国建国以来分别在1953、1964、1982、1990、2000和2010年进行了共六次人口普查，
# 其中第六次人口普查分别涉及到了人口增长、家庭户人口、性别构成、年龄构成、民族构成、受教育程度、城乡人口、人口流动性等八方面。
# 现有关于《各地区分性别的16岁及以上人口的就业状况》的数据，现定义
#
# 成年人比率=16岁及以上人口/总人口，就业率=就业人口/经济活动人口，失业率=失业人口/经济活动人口，
# 以北京为例其成年人比率=1672749/1849475=0.9044，就业率=977387/1020455=0.9578，失业率=43068/1020455=0.0422，请利用Python代码完成如下问题：

# 1）以各地区数据为代表，计算成年人比率均值的置信区间，置信水平为90%，假设成年人比率符合正态分布

# 2）以各地区数据为代表，计算就业率与失业率的方差比的置信区间，置信水平为90%，假设就业率与失业率辆样本相互独立，且各自符合正态分布


import numpy as np
from scipy.stats import norm
from scipy.stats import f

class Solution():
	def solve(self):
		list_over16 = ['1672749', '992504', '5759327', '2810549', '1948123', '3713575', '2209254', '3000940', '2040875', '6482159', '4611756', '4211557', '2880394', '3242397', '7688407', '7124733', '4391940', '4920101', '7852679', '3301266', '640690', '2107266', '6598501', '2404526', '3438510', '195270', '3012481', '2077912', '411514', '467146', '1608023']
		list_total = ['1849475', '1127589', '7037620', '3477805', '2310941', '4252076', '2551123', '3465051', '2253525', '7577122', '5400348', '5312628', '3477491', '4251692', '9272503', '9224288', '5226904', '6096586', '9676589', '4362551', '826560', '2609882', '8161604', '3332265', '4467537', '265904', '3614887', '2623094', '535412', '611957', '2086576']
		alpha = 0.1
		n = len(list_total)
		list_aul = []
		for i in range(n):
			list_aul.append(float(list_over16[i])*100/float(list_total[i]))
		average = np.mean(list_aul)
		std = np.std(list_aul)
		test = norm.ppf(1 - alpha / 2)
		aver_lower = average - std / np.sqrt(n) * test
		aver_higher = average + std / np.sqrt(n) * test

		list_inwork = ['977387', '550787', '4004477', '1729275', '1285021', '2345361', '1429001', '1868107', '1251461', '4486706', '3280387', '2897236', '1950006', '2251205', '5694220', '5006277', '3035863', '3389354', '5525078', '2447946', '426823', '1374581', '4688003', '1676240', '2668421', '147821', '1996061', '1414319', '290469', '327094', '1133002']
		list_worktotal = ['1020455', '581836', '4094886', '1801393', '1321004', '2437622', '1480029', '1940036', '1308691', '4591588', '3385618', '2962251', '2005135', '2305307', '5803432', '5153619', '3126385', '3499264', '5740925', '2530754', '450576', '1424331', '4801677', '1723117', '2710172', '149281', '2058807', '1462388', '296990', '334932', '1163800']
		list_workrate = []
		for i in range(n):
			list_workrate.append(float(list_inwork[i]) / float(list_worktotal[i]))

		list_outwork = ['43068', '31049', '90409', '72118', '35983', '92261', '51028', '71929', '57230', '104882', '105231', '65015', '55129', '54102', '109212', '147342', '90522', '109910', '215847', '82808', '23753', '49750', '113674', '46877', '41751', '1460', '62746', '48069', '6521', '7838', '30798']
		list_outworkrate = []
		for i in range(n):
			list_outworkrate.append(float(list_outwork[i]) / float(list_worktotal[i]))

		var_lower = np.var(list_workrate) / np.var(list_outworkrate) / f.ppf(1 - alpha / 2, n-1, n-1)
		var_higher = np.var(list_workrate) / np.var(list_outworkrate) / f.ppf(alpha / 2, n-1, n-1)
		return [[aver_lower, aver_higher], [var_lower, var_higher]]

if __name__ == '__main__':
	S = Solution()
	print(S.solve())