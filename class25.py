try:
    with open("hello.txt", "r+") as f:
        content = f.read()
        f.seek(2)
        f.write("aryan" + content[2:])
        f.close()

except FileNotFoundError as e:
    print(f"file nhi hai{e}")
