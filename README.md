# basics_py

Steps to Use the Script
	1.	Install Dependencies: Ensure you have the requests library installed.
  2.	Replace Proxy Details: Update the proxies dictionary with your proxy server information:
	     •	Replace username, password, proxyserver, and port with your actual proxy credentials.
	3.	Run the Script:
      Execute the script, and it will test your proxy and fetch data from httpbin.org.

Notes:
	•	Use http:// for proxies even if the target URL is https. The requests library handles the encryption.
	•	For SOCKS proxies, you can use socks5:// or socks5h:// and install the requests[socks] package:
