try:
    file = open("hello.txt", "w")
    file.write("good")
    file.close
except FileNotFoundError as e:
    print(f"file nhi hai{e}")
