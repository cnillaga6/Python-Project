# Project 5 - Image Modifier
# Name: Cesar Nillaga
# Instructor: Dr. S. Einakian
# Section: 15

def main():
    var_infile = input("Please enter input PPM file name: ")
    var_outfile = input("Pleas enter output PPM file name: ")
    var_mod = input("Please enter the modification to execute: ")

    process_header(var_infile, var_outfile)
    process_body(var_infile, var_outfile, var_mod)


# purpose: writes the first three lines of the input image to the output image
# signature: file file -> None
def process_header(infile, outfile):
    readfile = open(infile, 'r')
    lines = readfile.readline()
    list1 = []
    while True:
        line2 = readfile.readline()
        if line2 == '':
            break
        aline = line2.split()
        for sub_comp in aline:
            list1.append(int(sub_comp))
    header = list1[0:3]
    writefile = open(outfile, 'w')
    writefile.write('P3\n')
    writefile.write('{0} {1}\n'.format(header[0], header[1]))
    writefile.write('{0}\n'.format(header[2]))
    writefile.close()
    readfile.close()


# purpose: modifies input image based on user specified modification and then outputs modified image
# signature: file file str -> None
def process_body(infile, outfile, modification):
    readfile = open(infile, 'r')
    lines = readfile.readline()
    list1 = []
    while True:
        line2 = readfile.readline()
        if line2 == '':
            break
        aline = line2.split()
        for sub_comp in aline:
            list1.append(int(sub_comp))
    writefile = open(outfile, 'a+')
    del list1[0:3]
    groups = groups_of_3(list1)
    if modification == 'negate':
        negate(groups)
        for pixels in groups:
            for pixel in pixels:
                writefile.write('{0:d}\n'.format(pixel))

    elif modification == 'high contrast':
        high_contrast(groups)
        for pixels in groups:
            for pixel in pixels:
                writefile.write('{0:d}\n'.format(pixel))

    elif modification == 'gray scale':
        gray_scale(groups)
        for pixels in groups:
            for pixel in pixels:
                writefile.write('{0:d}\n'.format(pixel))

    elif modification == 'remove red':
        remove_color(groups, modification, outfile)

    elif modification == 'remove green':
        remove_color(groups, modification, outfile)

    elif modification == 'remove blue':
        remove_color(groups, modification, outfile)

    writefile.close()
    readfile.close()


# purpose: takes a group of 3 pixels and returns updated negated pixels
# signature: list -> list
def negate(groups):
    for pixels in groups:
        pixels[0] = abs(pixels[0] - 255)
        pixels[1] = abs(pixels[1] - 255)
        pixels[2] = abs(pixels[2] - 255)
    return groups


# purpose: takes a group of 3 pixels and returns updated high contrast pixels
# signature: list -> list
def high_contrast(groups):
    for pixels in groups:
        if pixels[0 - 2] > 127:
            pixels[0] = 255
            pixels[1] = 255
            pixels[2] = 255
        else:
            pixels[0] = 0
            pixels[1] = 0
            pixels[2] = 0
    return groups


# purpose: takes a group of 3 pixels and returns updated gray scale pixels
# signature: list -> list
def gray_scale(groups):
    for pixels in groups:
        pixel_avg = int((pixels[0] + pixels[1] + pixels[2]) / 3)
        pixels[0] = pixel_avg
        pixels[1] = pixel_avg
        pixels[2] = pixel_avg
    return groups


# purpose: takes a group of 3 pixels and removes pixels based on what color needs to be removed
# signature: list str file -> None
def remove_color(groups, str, outfile):
    if str == 'remove red':
        for pixels in groups:
            pixels[0] = 0
    elif str == 'remove green':
        for pixels in groups:
            pixels[1] = 0
    elif str == 'remove blue':
        for pixels in groups:
            pixels[2] = 0
    writefile = open(outfile, 'a+')
    for pixels in groups:
        for pixel in pixels:
            writefile.write('{0:d}\n'.format(pixel))
    writefile.close()


# purpose: takes a list of values and returns list of sub list of groups of 3
# signature: list -> list
def groups_of_3(list):
    result = [list[i:i + 3] for i in range(0, len(list), 3)]
    return result


if __name__ == '__main__':
    main()
