# WRITE as many function as you want for clean code
def clean(words):
    newwords = []
    for word in words:
        word = word.lower()
        word = word.replace('.', '')
        word = word.replace('?', '')
        word = word.replace('!', '')
        word = word.replace(':', '')
        word = word.replace(';', '')
        word = word.replace('"', '')
        word = word.replace('[', '')
        word = word.replace(']', '')
        word = word.replace('(', '')
        word = word.replace('}', '')
        word = word.replace('{', '')
        word = word.replace(')', '')
        word = word.replace('<', '')
        word = word.replace('>', '')
        word = word.replace('0', '')
        word = word.replace('1', '')
        word = word.replace('2', '')
        word = word.replace('3', '')
        word = word.replace('4', '')
        word = word.replace('5', '')
        word = word.replace('6', '')
        word = word.replace('7', '')
        word = word.replace('8', '')
        word = word.replace('9', '')
        word = word.replace("'", '')
        newwords.append(word)
    newwords = list(set(newwords))
    return newwords

def levenshtein( word1, word2 ):
    columns = len(word1) + 1
    rows = len(word2) + 1

    # build first row
    currentRow = [0]
    for column in range( 1, columns ):
        currentRow.append( currentRow[column - 1] + 1 )

    for row in range( 1, rows ):
        previousRow = currentRow
        currentRow = [ previousRow[0] + 1 ]

        for column in range( 1, columns ):
        	# insert and delete costs are 1
            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1
            # replacement cost is 2
            if word1[column - 1] != word2[row - 1]:
                replaceCost = previousRow[ column - 1 ] + 2
            else:                
                replaceCost = previousRow[ column - 1 ]

            currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    return currentRow[-1]

def search(target, maxCost, newwords):
    results = []
    for word in newwords:
        cost = levenshtein( target, word )

        if cost <= maxCost:
            results.append( (word, cost) )

    return results


def autoCorrect(word):
    # we call this function in judge
    # Write your main code here and generate correct word as result.
    # please do not modify parameters or this function name
    MAX_COST = 20
    f = open('shakespeare.txt')
    data = f.read()
    old_words = data.split()
    newwords = clean(old_words)
    results = search( word, MAX_COST, newwords)
    results = list(set(results))

    min_distance = 10
    min_word = ''
    for word, dist in results:
        if dist <= min_distance:
            min_distance = dist
            min_word = word
        
    # WRITE YOUR CODE HERE
    return min_word

# this is how this code runs
# autoCorrect('flw') -> 'flow'