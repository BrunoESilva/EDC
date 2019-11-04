from lxml import etree;

def listMovies():
    tree = etree.parse("film.xml")
    list = []
    for v in tree.xpath("//Movies/movie/title"):
        list.append(v.text)
    return list

def info(este):
    tree = etree.parse("film.xml")
    dict = {'year': tree.xpath("//Movies/movie[title/text()='"+este+"']/year")[0].text,
            'lenght': tree.xpath("//Movies/movie[title/text()='"+este+"']/length")[0].text,
            'subject': tree.xpath("//Movies/movie[title/text()='"+este+"']/subject")[0].text,
            'actor': tree.xpath("//Movies/movie[title/text()='"+este+"']/actor")[0].text,
            'actress': tree.xpath("//Movies/movie[title/text()='"+este+"']/actress")[0].text,
            'director' : tree.xpath("//Movies/movie[title/text()='"+este+"']/director")[0].text,
            'popularity': tree.xpath("//Movies/movie[title/text()='"+este+"']/popularity")[0].text}
    return dict