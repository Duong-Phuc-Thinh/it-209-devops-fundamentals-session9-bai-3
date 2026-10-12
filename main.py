import subprocess
import time
import urllib.request

def main():
    print("Building Docker image...")
    subprocess.run(["docker", "build", "-t", "my-html-app:v1", "."], check=True)

    print("Running Docker container...")
    subprocess.run(["docker", "run", "-d", "-p", "8081:80", "--name", "html-app", "my-html-app:v1"], check=True)

    time.sleep(2)
    try:
        print("Checking HTTP endpoint http://localhost:8081...")
        with urllib.request.urlopen("http://localhost:8081") as response:
            html = response.read().decode("utf-8")
            print("Response received:", html)
            assert "<h1>Hello Docker Session 09!</h1>" in html
            print("Test passed successfully!")
    finally:
        print("Cleaning up container...")
        subprocess.run(["docker", "rm", "-f", "html-app"], check=True)

if __name__ == "__main__":
    main()