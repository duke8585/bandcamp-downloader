from datetime import datetime
from dateutil.relativedelta import relativedelta

def generate_bandcamp_commands(start_month, num_months, username="duke8585"):
    try:
        current_date = datetime.strptime(f"{start_month}-01", "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid start_month format: {start_month}. Use YYYY-MM")
    
    commands = []
    
    for i in range(num_months):
        month_start = current_date.strftime("%Y-%m-%d")
        next_month = current_date + relativedelta(months=1)
        month_end = next_month.strftime("%Y-%m-%d")
        directory = current_date.strftime("%Y-%m")
        
        command = (f"./bandcamp-downloader.py {username} "
                  f"--browser brave "
                  f"--format aiff-lossless "
                  f"--parallel-downloads 6 "
                  f"--directory loaded/{directory} "
                  f"--extract "
                  f"--download-since {month_start} "
                  f"--download-until {month_end}")
        
        commands.append(command)
        current_date = next_month
    
    return commands

if __name__ == "__main__":
    # Example usage
    start_month = "2025-08"
    num_months = 12
    commands = generate_bandcamp_commands(start_month, num_months)
    
    for cmd in commands:
        print(cmd)