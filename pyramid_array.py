def pyramid(n):
    pyramid = [];
    subpyramid = [];
    for i in range(n + 1):
        for i1 in range(i):
            subpyramid.append(1);
        pyramid.append(subpyramid);
        subpyramid = [];
    pyramid = pyramid[1::];
    return pyramid;