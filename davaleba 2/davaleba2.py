samples = [
    [1,  2,  3,  0,  7],
    [4,  5,  6, 19,  1],
    [4,  5,  6, 23,  0],
    [7, 15,  6, 13,  1],
    [4,  5,  6,  2,  1],
    [1,  9,  8,  5, 41],
    [2,  6,  1,  8, 11]
]

sample_categories = [
    1,
    2,
    1,
    1,
    2,
    5,
    6
]

tests = [
    [1,  2,  3,  0,  7],
    [2,  6,  1,  8, 11],
    [7, 15,  6,  8, 11]
]


def knearest(k):
    predictions = []
    for test in tests:
        distances = []
        for index, sample in enumerate(samples):
            diff_sum = 0
            for i in range(len(sample)):
                diff_sum += abs(test[i] - sample[i])
            # ვინახავთ მანძილსაც და ინდექსსაც, რომ სორტირებაში არ დაგვეკარგოს
            distances.append((diff_sum, index))
        # ვსორტავთ მანძილის ზრდადობის მიხედვით
        # და ვიტოვებთ მხოლოდ პირველ k ცალ ელემენტს
        distances.sort()
        distances = distances[:k]
        # კატეგორიების სიხშირეების მეპი
        frequency = {}
        for category in sample_categories:
            frequency[category] = 0
        max_frequency = 0
        max_frequency_category = 0
        for _, index in distances:
            frequency[sample_categories[index]] += 1
            # მკაცრი მეტობა ნიშნავს, რომ ორი ერთი და იგივე
            # სიხშირის კატეგორიის არსებობის შემთხვევაში,
            # ავიღებთ ისეთს, რომელმაც პირველად მიაღწია ამ სიხშირეს
            # მანძილის ზრდადობით მოვლის დროს. ეს არ გვაძლევს გარანტიას
            # რომ ეს კატეგორია ჯამში უფრო ახლოა, მაგრამ კარგი მიახლოებაა
            if frequency[sample_categories[index]] > max_frequency:
                max_frequency = frequency[sample_categories[index]]
                max_frequency_category = sample_categories[index]
        predictions.append(max_frequency_category)
    return predictions


print(knearest(1))
print(knearest(3))
print(knearest(5))
print(knearest(6))
