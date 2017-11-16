def box(height,width,length):
    if length != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
try:
    box(2,2,1)
except Exception as err:
    print("An exception ahppend")