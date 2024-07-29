import ipaddress

import tempfile

import subprocess

import os



def list_ips_in_range(start_ip, end_ip):

    try:

        start = ipaddress.IPv4Address(start_ip)

        end = ipaddress.IPv4Address(end_ip)

    except ipaddress.AddressValueError:

        print("Invalid IP address format")

        return None

    

    if start > end:

        print("Start IP should be less than or equal to end IP")

        return None

    

    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:

        for ip_int in range(int(start), int(end) + 1):

            ip_str = str(ipaddress.IPv4Address(ip_int))

            temp_file.write(ip_str + '\n')

        

        temp_filename = temp_file.name



    return temp_filename



if __name__ == "__main__":

    print("Enter the IP range to generate the list of IPs.")

    start_ip = input("Enter the start IP address: ")

    end_ip = input("Enter the end IP address: ")



    print(f"Generating IP list from {start_ip} to {end_ip}...")

    temp_filename = list_ips_in_range(start_ip, end_ip)

    

    if temp_filename:

        print(f"IP list generated and saved to temporary file: {temp_filename}")

        print("Running hakrevdns and httpx on the IP list...")



        # Create a temporary shell script file

        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.sh') as script_file:

            script_file.write(f"""

            while read -r ip; do

                echo "$ip" | hakrevdns -d | httpx -silent -title -rl 5 -status-code -td -mc 200,201,202,203,204,206,301,302,303,307,308 -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

            done < {temp_filename}

            """)

            script_filename = script_file.name



        # Make the script executable

        os.chmod(script_filename, 0o755)



        # Run the shell script

        result = subprocess.run(script_filename, shell=True, capture_output=True, text=True)



        print("Shell command output:")

        print(result.stdout)

        print(result.stderr)

        

        # Clean up the temporary files

        print("Cleaning up temporary files...")

        os.remove(temp_filename)

        os.remove(script_filename)

        print("Done.")

    else:

        print("Failed to generate IP list.")

