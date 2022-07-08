data1 = ['Desktop', 'Notes', 'Commands', 'WorkSpace', 'React', 'Angular', 'Veu', 'Public', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['desktop', 'notes', 'commands', 'workspace', 'react', 'angular', 'veu', 'public', 'general', 'downloads', 'wordFile', 'excelFile']

print (str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())


data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data2).replace(' ','').lower()
print(data2)


assert data1 == data2