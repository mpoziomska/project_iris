from .io import loader, save

from statistics import pstdev, mean, median

def make_stats(load_path, save_path):
	data = loader(load_path)

	fun = {'std': pstdev, 'mean': mean, 'median': median}

	results = [[""] + list(data.keys())]

	for f in fun:
		results.append([f] + [fun[f](map(float, data[k])) for k in data])

	save(save_path, results)

