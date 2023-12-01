import subprocess
import schedule
import time
import platform
import logging

# Configure logging
logging.basicConfig(filename='patch_management.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def check_updates():
    """Check for available updates using apt."""
    if platform.system() == "Linux" and platform.linux_distribution()[0].lower() == "ubuntu":
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            result = subprocess.run(["sudo", "apt", "list", "--upgradeable"], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Error checking updates: {e}")
            return None
    else:
        logging.warning("Unsupported platform or distribution.")
        return None

def install_updates():
    """Install available updates using apt."""
    if platform.system() == "Linux" and platform.linux_distribution()[0].lower() == "ubuntu":
        try:
            subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
            return "Updates installed successfully."
        except subprocess.CalledProcessError as e:
            logging.error(f"Error installing updates: {e}")
            return "Error installing updates."
    else:
        logging.warning("Unsupported platform or distribution.")
        return "Unsupported platform or distribution."

def job():
    logging.info("Checking for available updates...")
    updates_info = check_updates()

    if updates_info:
        logging.info("Available updates:\n%s", updates_info)
        
        install_result = install_updates()
        logging.info(install_result)
    else:
        logging.warning("Failed to check updates.")

def main():
    # Set the scheduled time for daily updates check to 5 am
    check_time = "05:00"

    try:
        # Schedule the job to run every day at 5 am
        schedule.every().day.at(check_time).do(job)
        logging.info(f"Daily updates check scheduled for {check_time}")

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")

if __name__ == "__main__":
    main()
