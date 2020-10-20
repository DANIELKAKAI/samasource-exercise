import json
import sys


def read_file(file_name):
	with open(file_name) as json_file:
		data = json.load(json_file)
		return data


def get_shape_types(data):
	shape_types = []
	for item in data:
		for image in item['taggable image']:
			shape_types.append(image['type'])
	return set(shape_types)


def get_labels(data):
	labels = []
	for item in data:
		for image in item['taggable image']:
			labels.append(image['tags']['label'])
	return set(labels)


def calculate_frequency(data):
	frequencies = {}
	labels = get_labels(data)
	shape_types = get_shape_types(data)
	for shape in shape_types:
		for label in labels:
			for item in data:
				for image in item['taggable image']:
					if image['tags']['label'] == label and image['type'] == shape:
						if frequencies.get("{}-{}".format(shape,label)):
							frequencies["{}-{}".format(shape,label)] += 1
						else:
							frequencies["{}-{}".format(shape,label)] = 1
	return frequencies





if __name__=='__main__':
	file_name = sys.argv[1]
	data = read_file(file_name)
	print(get_shape_types(data))
	print(get_labels(data))
	print(calculate_frequency(data))

