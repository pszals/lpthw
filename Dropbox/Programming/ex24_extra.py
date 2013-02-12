def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 2000
jb, j, c = secret_formula(start_point)

print "%d jb, %d j, and %d c" % (jb, j, c)