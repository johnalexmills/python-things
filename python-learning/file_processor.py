fn = "Darius-13-100m-fly.txt"


def split_filename(fn):
    return fn.removesuffix(".txt").split("-")


name, age, distance, stroke = split_filename(fn)

print(name, age, distance, stroke)
