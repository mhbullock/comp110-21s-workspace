"""An exercise in remainders and boolean logic."""

__author__ = "730394070"


# Begin your solution here...

tar_heel: int = int(input("Enter an int: "))


if tar_heel % 2 == 0 and tar_heel % 7 == 0:
    print("TAR HEELS")
else: 
    if tar_heel % 2 == 0: 
        print("TAR")
    else:
        if tar_heel % 7 == 0:
            print("HEELS")
        else:
            if tar_heel % 2 != 0 and tar_heel % 7 != 0: 
                print("CAROLINA")