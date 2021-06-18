import numpy as np

x = np.array([
    [[1.,  1.,  0.], [6.,  4., 10.], [7., 10.,  6.], [10.,  8.,  4.], [9.,  6.,  6.], [
        4.,  4., 10.], [6.,  1.,  1.], [2.,  3.,  1.], [10.,  9.,  3.], [3.,  6.,  7.]],
    [[7.,  0.,  9.], [2.,  2.,  6.], [8.,  7.,  6.], [5.,  0.,  3.], [8.,  2., 10.], [
        1.,  9.,  6.], [4.,  0.,  7.], [4.,  1.,  9.], [0.,  9.,  3.], [6.,  3.,  3.]],
    [[1.,  8.,  7.], [3.,  9.,  2.], [9.,  8.,  7.], [1.,  6.,  8.], [0.,  5.,  4.], [
        6.,  9.,  7.], [0.,  1.,  6.], [5.,  5.,  0.], [1.,  4.,  6.], [4.,  8.,  6.]],
    [[7.,  4.,  9.], [1.,  9.,  2.], [6.,  1., 10.], [5.,  7.,  9.], [1.,  8.,  9.], [
        0.,  5.,  4.], [3.,  1.,  3.], [5.,  8.,  0.], [1.,  0.,  6.], [5.,  7.,  3.]],
    [[10., 10.,  8.], [6.,  6.,  3.], [2.,  2.,  8.], [6.,  1.,  5.], [3.,  9.,  6.], [
        6.,  7.,  1.], [1.,  2.,  3.], [3.,  0.,  8.], [8.,  2.,  4.], [5.,  8.,  4.]],
    [[1.,  6.,  7.], [9.,  1.,  7.], [7.,  0.,  4.], [0.,  3.,  6.], [9.,  9.,  2.], [
        4.,  7.,  4.], [7.,  0.,  4.], [2.,  0.,  6.], [7.,  9.,  7.], [9.,  7.,  8.]],
    [[7.,  0.,  6.], [8.,  2.,  2.], [2.,  9.,  7.], [4.,  4.,  8.], [5.,  5.,  3.], [
        2.,  5.,  5.], [6.,  5.,  6.], [7.,  5.,  3.], [3.,  9.,  7.], [8.,  7.,  1.]],
    [[9.,  5.,  9.], [2.,  0.,  4.], [3.,  7.,  3.], [1.,  1.,  7.], [1.,  5.,  7.], [
        2.,  4.,  4.], [1.,  8.,  8.], [1.,  7.,  1.], [4.,  8., 10.], [9.,  7.,  1.]],
    [[1., 10.,  8.], [8.,  6.,  5.], [2.,  5.,  4.], [1.,  9.,  2.], [9.,  9.,  1.], [
        8.,  5.,  5.], [8.,  4.,  6.], [8.,  4.,  7.], [7.,  1.,  3.], [1.,  1.,  8.]],
    [[1.,  2.,  1.], [10.,  9.,  6.], [3.,  8.,  0.], [6.,  8.,  7.], [0.,  2.,  7.], [
        6.,  4.,  6.], [5.,  6.,  4.], [10.,  5.,  2.], [9.,  8.,  6.], [2.,  4.,  5.]]
])

f_w = np.array([
    [[9.,  8.,  4.], [7.,  6.,  8.], [3.,  8.,  1.], [2.,  1.,  5.], [3.,  0.,  6.]],
    [[7.,  9.,  7.], [10.,  4.,  3.], [3.,  2.,  9.],
     [6.,  2.,  4.], [4.,  9.,  0.]],
    [[6.,  2.,  2.], [2.,  2.,  5.], [1.,  9.,  5.],
     [4.,  3.,  4.], [3.,  9.,  2.]],
    [[1.,  3.,  6.], [3.,  7.,  9.], [5.,  2.,  7.],
     [4.,  3.,  3.], [8.,  0.,  2.]],
    [[8.,  6.,  7.], [2.,  2.,  4.], [8.,  4.,  9.], [1.,  6.,  1.], [8.,  8.,  2.]]
])

f_b = 2

stride = 1


def relu(x):
    return max(0, x)


result = []

# სიღრმეში ყველა მატრიცისთვის (ამ შემთხვევაში 3, ხშირად rgb ფერის აღმნიშვნელი)
# ვითვლით ფილტრის შესაბამისი სიღრმის კერნელის მოდების შედეგს
# და ბოლოს ვკრებთ ამ მატრიცებს საბოლოო შედეგის მისაღებად
for color in range(len(x[0][0])):
    # შედეგი 6x6x1 მატრიცა color სიღმისთვის
    colorResult = []

    # იგივე რაც წინა დავალებაში
    for xrow in range(0, len(x), stride):
        # ვჩერდებით, თუ ფილტრი დაბლა ჩაცდა მოცემულ მატრიცს
        if xrow + len(f_w) > len(x):
            break

        resultRow = []
        for xcol in range(0, len(x[0]), stride):
            # ვჩერდებით, თუ ფილტრი გაცდა მარჯვნივ მოცემულ მატრიცს
            if xcol + len(f_w[0]) > len(x[0]):
                break

            sumwx = 0
            # გადავყვებით ფილტრში ყველა წონას
            for frow in range(len(f_w)):
                for fcol in range(len(f_w[0])):
                    # ვითვლით სკალარულ ნამრავლს xrow, xcol-დან დაწყებული 5x5 ფანჯრისთვის
                    sumwx += f_w[frow][fcol][color] * \
                        x[frow + xrow][fcol + xcol][color]

            # ვუმატებთ bias-ს და ვატარებთ აქტივაციის ფუნქციაში
            output = relu(sumwx + f_b)

            # შედეგი რიცხვი ჩაჯდება პასუხის შესაბამის ინდექსზე
            resultRow.append(output)

        # შედეგი რიგი ჩაჯდება შესაბამის ინდექსზე
        colorResult.append(resultRow)

    # თუ პირველ სიღრმეზე ვართ მივანიჭოთ შედეგს, თუ არა დავუმატოთ შესაბამის ადგილებში მნიშვნელობები
    if len(result) == 0:
        result = colorResult
    else:
        for i in range(len(result)):
            for j in range(len(result)):
                result[i][j] += colorResult[i][j]


print(result)

# result
# [[1828.0, 2011.0, 1861.0, 1606.0, 1556.0, 1487.0],
# [1836.0, 1826.0, 1658.0, 1558.0, 1516.0, 1519.0],
# [1865.0, 1753.0, 1743.0, 1575.0, 1452.0, 1616.0],
# [1784.0, 1635.0, 1642.0, 1418.0, 1599.0, 1639.0],
# [1847.0, 1669.0, 1432.0, 1629.0, 1809.0, 1719.0],
# [1583.0, 1628.0, 1668.0, 1821.0, 1852.0, 1787.0]]
