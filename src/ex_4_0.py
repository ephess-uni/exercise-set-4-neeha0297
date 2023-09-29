""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    number_of_shutdowns = list()
    
    with open(logfile, 'r') as file_lg:
        
        all_events = file_lg.read()
    
    all_logs_events = all_events.splitlines()
    
    for log in all_logs_events:
        
        if 'Shutdown initiated' in log :
            
            number_of_shutdowns.append(log)
        
    return number_of_shutdowns



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
