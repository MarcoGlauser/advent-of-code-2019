picture_size = (25, 6)
layer_size = picture_size[0] * picture_size[1]
result = (999999999, '0000')


def layers(layer_size):
    with open('input.txt', "r") as fp:
        chunk = fp.read(layer_size)
        while chunk:
            yield chunk
            chunk = fp.read(layer_size).strip()


for layer in layers(layer_size):
    number_of_zeroes = layer.count('0')
    if number_of_zeroes < result[0]:
        result = number_of_zeroes, layer

print(result[1].count('1') * result[1].count('2'))