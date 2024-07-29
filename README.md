This script generates a list of IP addresses within a specified range, saves them to a temporary file, and then runs `hakrevdns` and `httpx` tools on these IPs to perform reverse DNS lookups and HTTP probing.

## Requirements

- Python 3.x
- `hakrevdns` tool
- `httpx` tool

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Install `hakrevdns`:
   ```sh
   go install github.com/hakluke/hakrevdns@latest

    Install httpx:

    sh

    go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

Usage

    Run the script:



python3 script.py

Enter the start and end IP addresses when prompted:



    Enter the IP range to generate the list of IPs.
    Enter the start IP address: 192.168.1.1
    Enter the end IP address: 192.168.1.10

    The script will generate the list of IPs, save it to a temporary file, and run hakrevdns and httpx on the IP list. The output will be displayed in the console.

Example



$ python3 script.py
Enter the IP range to generate the list of IPs.
Enter the start IP address: 192.168.1.1
Enter the end IP address: 192.168.1.10
Generating IP list from 192.168.1.1 to 192.168.1.10...
IP list generated and saved to temporary file: /tmp/tmpabcdefg
Running hakrevdns and httpx on the IP list...
Shell command output:
192.168.1.1 [200 OK] [Title: Example Domain]
192.168.1.2 [200 OK] [Title: Another Domain]
...
Cleaning up temporary files...
Done.

Code Explanation
Function to List IPs in Range

The list_ips_in_range function generates a list of IP addresses within the specified range and writes them to a temporary file.
Main Script

    Prompts the user for the start and end IP addresses.
    Calls list_ips_in_range to generate the IP list.
    Creates a temporary shell script that runs hakrevdns and httpx on the IP list.
    Executes the shell script and captures the output.
    Cleans up temporary files.

Clean Up

The script removes the temporary files created during the process to ensure no leftover files remain.
