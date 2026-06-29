import datetime
import os

def generate_client_report(client_name, tasks_completed):
    """
    A simple automation script to generate a daily text report for a project.
    This doesn't require any external webhooks or API keys.
    """
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"{client_name}_update_{date_str}.txt"
    
    with open(filename, "w") as file:
        file.write(f"Project Update: {client_name}\n")
        file.write(f"Date: {date_str}\n")
        file.write("-" * 35 + "\n")
        file.write("Tasks Completed Successfully:\n")
        for task in tasks_completed:
            file.write(f"- {task}\n")
            
    print(f"Success: Report generated locally and saved as {filename}")

if __name__ == "__main__":
    # Dummy data for testing the automation
    tasks = [
        "Configured initial GitHub repository",
        "Tested local Python environment",
        "Compiled native Android client prototype"
    ]
    
    generate_client_report("Development", tasks)
