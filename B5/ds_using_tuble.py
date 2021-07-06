zoo = ('python', 'elepant', 'penguin')
print('Number of enimal in the zoo is ', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('The number of cages in the new zoo is ', len(new_zoo))
print('All animal in the new zoo are: ', new_zoo)
print('Animal brought from old zoo is: ', new_zoo[2])
print('Last animal brought from old zoo is:', new_zoo[2][2])
print('The number in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))