

def question1():
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]
    files = []
    freq = []

    for url in urls:
        filename = url.split("/")[-1]
        files.append(filename)

    for file in files:
        freq.append(files.count(file))

    print(files)
    print(freq)
    


question1()