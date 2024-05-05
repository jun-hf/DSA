def test(fn):
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if fn(arr, 67) != 18:
        raise Exception("should be 18")

    if fn(arr, 3) != 1:
        raise Exception("should be 1")

    if fn(arr, 89) != 23:
        raise Exception("should be 23")

    if fn(arr, 24) != -1:
        raise Exception("should be -1")
    
    print("Test passed")