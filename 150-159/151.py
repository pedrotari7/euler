batchs = []

def break_down(current):
	if current == 'A5':
		return []
	elif current == 'A4':
		return ['A5']
	elif current == 'A3':
		return ['A4','A5']
	elif current == 'A2':
		return ['A3','A4','A5']
	elif current == 'A1':
		return ['A2','A3','A4','A5']


def next_batch(previous_batch,current_batch):

	if current_batch == ['A5']:
		batchs.append(previous_batch)
		return



	for sheet in current_batch:
		index = current_batch.index(sheet)
		next_current  = current_batch[:index] + current_batch[index+1:] + break_down(sheet)
		next_batch(previous_batch+[current_batch],next_current)		




next_batch([],['A1'])


