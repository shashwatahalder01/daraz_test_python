
def writetxt(filename,productlist):
    
    with open(filename, 'w', encoding="utf-8") as f:
        for row in productlist:
            f.write(row + '\n')