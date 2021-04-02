import tensorflow as tf
import numpy

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


img57 = x_train[57]
img61 = x_train[61]


def get_L1(img1, img2):
    L1 = 0
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            # abs-ის მაგივრად ვიყენებთ max - min, რადგან მოცემულ მატრიცაში
            # რიცხვები წერია uint8 ტიპით და პირდაპირი სხვაობის abs-ით
            # ზოგ ინდექსზე ხდება overflow, რაც გვაძლევს არასწორ პასუხს.
            # max - min ექვივალენტურია მოდულის
            L1 += max(img1[i][j], img2[i][j]) - min(img1[i][j], img2[i][j])
    return L1


print("Regular L1:", end=" ")
print(get_L1(img57, img61))

# ნორმალიზებული ([0-1] მნიშვნელობები [0-255]-ის მაგივრად) მატრიცისთვის
img57 = img57 / 255.0
img61 = img61 / 255.0

print("Normalized L1:", end=" ")
print(get_L1(img57, img61))
