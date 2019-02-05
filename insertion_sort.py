def IS(l):
	currentItem = 1
	while currentItem <= len(l) -1:
		currentDataItem = l[currentItem]
		comparison = 0
		comparisonItem = l[comparison]
		finished = False
		
		while comparison < currentItem and not finished:
			print("Current Item:\t\t %d (%d)" % (currentItem, currentDataItem))
			print("Comparison Item:\t %d (%d)" % (comparison, comparisonItem))
			if currentDataItem < comparisonItem:
				shuffleItem = currentItem
				while shuffleItem > comparison:
					l[shuffleItem] = l[shuffleItem - 1]
					shuffleItem -= 1
				l[comparison] = currentDataItem
				finished = True
			comparison += 1
			comparisonItem = l[comparison]
		currentItem += 1
		print(str(mylist) +'\n')

mylist = [2, 7, 8, 4, 3, 9, 1, 6, 5, 1]
IS(mylist)