# Patch Management Automation Script

Automate the process of checking and installing system updates on Ubuntu systems using this Python script. The script employs the `schedule` library to run daily checks at 5 am, ensuring that your systems are regularly updated with the latest security patches.

## Features

- **Automated Updates:** The script leverages system commands to check for and install available updates using `apt` on Ubuntu systems.

- **Scheduled Execution:** Updates are checked and installed automatically every day at 5 am, reducing the risk of vulnerabilities due to outdated software.

- **Logging:** All script activities are logged in the `patch_management.log` file, providing a detailed record of update checks and installations.

## Prerequisites

- This script is designed for Linux systems, specifically Ubuntu.

- Ensure that the script is executed with the necessary privileges to run system commands with `sudo`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/patch-management-automation.git

## Installation

1. **Navigate to the project directory:**

    ```bash
    cd patch-management-automation
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- **Run the script:**

    ```bash
    python patch_management.py
    ```

- Follow the on-screen instructions to check for available updates and install them.

## Configuration

- You can configure the scheduled time for daily updates by modifying the `check_time` variable in the `main` function of the script.

## Logging

- Script activities and potential errors are logged in the `patch_management.log` file, aiding in monitoring and troubleshooting.

## Security Considerations

- The script uses `sudo` for privileged operations, ensuring that only authorized users can execute these commands.

- User input for the scheduled time is validated to prevent potential security vulnerabilities.

- Exception handling is implemented to provide informative error messages and enhance script robustness.

## Important Notes

- Ensure that the system's time zone is correctly set, as the schedule is based on the system time.

- Customize the script as needed for your specific environment and requirements.
