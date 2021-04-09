'''
        file = open('../data/'+ticker+'_'+period[0]+'_'+period[1]+'.txt','w')
		for i in range(n):
			line = ''
			for j in range(m):
				line += str(self.W[i][j])+' '
			line += '\n'
			file.write(line)
		file.close()
        '''