# THIS IS A FUNCTION WHICH WILL FIND THE CUBES UPTO A GIVEN NUMBER STARTING FROM 1.

def cube_finder(num):
    cubes = {}
    for cube in range(1,num+1):
        cubes[cube] = cube**3
        # print(f"{cube}:{cubes}")
    return cubes

number = int(input("Enter a number to find the cubes upto that number: "))
print(cube_finder(number))

