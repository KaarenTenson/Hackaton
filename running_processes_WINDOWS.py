import psutil
import os

def get_running_processes():
    # Get a list of running processes
    running_processes = psutil.process_iter(['pid', 'name', 'exe'])

    # Extract process names without the file extension
    process_names = set()
    for process in running_processes:
        if process.info['exe'] is not None:
            base_name = os.path.splitext(os.path.basename(process.info['exe']))[0]
            process_names.add(base_name)

    return process_names

if __name__ == "__main__":
    running_process_names = get_running_processes()
    print("Currently running process names:")
    for process_name in running_process_names:
        print(process_name)
