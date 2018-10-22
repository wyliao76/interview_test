

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
    memo = []
    freq = {}

    for url in urls:
        filename = url.split("/")[-1]
        files.append(filename)

    for file in files:
        if file not in memo:
            memo.append(file)
            freq[file] = 1
        else:
            freq[file] += 1

    for k, v in freq.items():
        print(k + ' ' + str(v))


question1()