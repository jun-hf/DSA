def test(fn, arr):
    if fn(arr, 67) != 18:
        raise Exception("should be 18")

    if fn(arr, 3) != 1:
        raise Exception("should be 1")

    if fn(arr, 89) != 23:
        raise Exception("should be 23")

    if fn(arr, 24) != -1:
        raise Exception("should be -1")
    
    print("Test passed")