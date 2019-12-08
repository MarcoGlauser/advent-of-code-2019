picture_size = (25, 6)
layer_size = picture_size[0] * picture_size[1]
final_layer = ['2'] * layer_size
color_map = {
    '0': u"\u25A0",
    '1': u"\u25A1"
}


def layers(layer_size):
    with open('input.txt', "r") as fp:
        chunk = fp.read(layer_size)
        while chunk:
            yield chunk
            chunk = fp.read(layer_size).strip()


for layer in layers(layer_size):
    for i, pixel in enumerate(layer):
        if final_layer[i] == '2':
            final_layer[i] = pixel

for i, pixel in enumerate(final_layer, 1):
    print(color_map[pixel], end=' ')
    if i % picture_size[0] == 0:
        print()

