# XSSLoad

XSSLoad is a tool designed for detecting and exploiting Cross-Site Scripting (XSS) vulnerabilities on target web applications. It includes options for custom payload generation, web crawling, and flexible scanning methods.

## Features
- Crawl target websites to discover potential XSS vulnerabilities.
- Use custom or generated payloads for testing.
- Supports both GET and POST request methods.
- Proxy support for anonymous scanning.
- Configurable user-agent for requests.

## Requirements
- Python 3.8+

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/xssload.git
   cd xssload
   ```

2. Run the tool:
   ```bash
   python xssload.py
   ```

## Usage
XSSLoad provides both interactive and command-line usage modes.

### Interactive Mode
Simply run the tool and follow the on-screen instructions:
```bash
python xssload.py
```
You will be presented with the ASCII art logo and an interactive menu to select options such as scanning a URL, setting custom payloads, or viewing tool information.

### Command-Line Mode
You can also provide arguments directly via the command line:

#### Basic Scan
```bash
python xssload.py -u http://testphp.vulnweb.com
```

#### Single Scan
```bash
python xssload.py --single http://example.com
```

#### Custom Payload
```bash
python xssload.py -u http://testphp.vulnweb.com --payload "<script>alert('XSS')</script>"
```

#### Set Payload Level
```bash
python xssload.py -u http://testphp.vulnweb.com --payload-level 5
```

#### Proxy Support
```bash
python xssload.py -u http://testphp.vulnweb.com --proxy "{'https':'https://10.10.1.10:1080'}"
```

#### Set User-Agent
```bash
python xssload.py -u http://testphp.vulnweb.com --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
```

## Options
| Argument           | Description                                                                                           | Default                          |
|--------------------|-------------------------------------------------------------------------------------------------------|----------------------------------|
| `-u`              | Target URL to scan.                                                                                   | None                             |
| `--single`         | Single URL scan without crawling.                                                                     | None                             |
| `--depth`          | Depth of web page crawling.                                                                           | 2                                |
| `--payload-level`  | Level for payload generation (1-6) or 7 for custom payload.                                           | 6                                |
| `--payload`        | Directly load a custom payload.                                                                       | None                             |
| `--method`         | HTTP method: 0 for GET, 1 for POST, 2 for both.                                                       | 2                                |
| `--proxy`          | Proxy settings (e.g., `{'https':'https://10.10.1.10:1080'}`).                                         | None                             |
| `--user-agent`     | Set a custom User-Agent for HTTP requests.                                                            | Default user-agent               |
| `--cookie`         | Set a cookie for requests (e.g., `{'ID':'1094200543'}`).                                              | `{"ID":"1094200543"}`        |
| `--about`          | Display information about the tool.                                                                   | None                             |
| `--help`           | Show usage and help parameters.                                                                       | None                             |

## Example
Here is an example of a typical XSSLoad run:
```bash
python xssload.py -u http://testphp.vulnweb.com --depth 3 --payload-level 6 --proxy "{'https':'https://127.0.0.1:8080'}"
```

## Disclaimer
**Use this tool responsibly.**

This tool is intended for educational and ethical testing purposes only. The developers are not responsible for any misuse or damage caused by this tool. Always obtain permission before scanning or testing any website or system.

---

### Author
Created by [Umut Kaya](https://github.com/umutkayash)

Feel free to contribute or report issues on the [GitHub repository](https://github.com/umutkayash/xssload).
