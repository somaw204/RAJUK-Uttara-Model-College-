# Login Credential Checker

A Python script that tests multiple login credentials against the Rajuk College portal to verify their validity.

## Features

- **Bulk credential testing** from a text file
- **CSRF token extraction** for secure authentication
- **Real-time progress tracking** with status updates
- **Clean output format** without HTML responses
- **Comprehensive summary** of results
- **Error handling** for malformed credentials
- **Rate limiting** to avoid server overload

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Create a `user.txt` file with credentials in the following format:
   ```
   username1:password1
   username2:password2
   admin:admin123
   test@email.com:password
   ```

2. Run the script:
   ```bash
   python login_checker.py
   ```

## File Format

The `user.txt` file should contain one credential per line in the format:
```
username:password
```

- Each line represents one credential pair
- Use colon `:` as separator between username and password
- Empty lines are automatically skipped
- Passwords can contain colons (only first colon is used as separator)

## Output

The script provides:

- **Progress tracking**: Shows current credential being tested
- **Real-time results**: ✅ for valid, ❌ for invalid credentials
- **Final summary**: Total tested, valid count, invalid count
- **Valid credentials list**: All working credentials found

### Sample Output
```
Found 5 credential(s) to check...
==================================================
Testing [1/5] Username: admin
❌ INVALID - admin:admin
------------------------------
Testing [2/5] Username: user123
✅ SUCCESS - user123:password123
------------------------------
==================================================
FINAL SUMMARY:
Total tested: 5
Valid credentials: 1
Invalid credentials: 4

✅ VALID CREDENTIALS FOUND:
  user123:password123
```

## Error Handling

The script handles various error scenarios:

- **Missing file**: Alerts if `user.txt` doesn't exist
- **Empty file**: Warns if no credentials found
- **Invalid format**: Skips malformed lines
- **Network issues**: Continues with next credential if CSRF token fails
- **Server errors**: Graceful handling of connection problems

## Rate Limiting

The script includes a 1-second delay between requests to:
- Avoid overwhelming the target server
- Prevent potential IP blocking
- Ensure stable connection handling

## Security Notes

- This tool is for **educational purposes** and **authorized testing** only
- Ensure you have **proper permission** before testing any system
- Use responsibly and in compliance with applicable laws
- Consider the **ethical implications** of credential testing

## Troubleshooting

**Script doesn't start:**
- Verify `user.txt` exists in the same directory
- Check Python and requests library installation

**No results shown:**
- Ensure credentials are in correct `username:password` format
- Check network connectivity
- Verify target website is accessible

**All credentials show as invalid:**
- Confirm the target URL is correct
- Check if the website structure has changed
- Verify credentials are actually valid

## License

This project is provided as-is for educational purposes. Use responsibly and at your own risk.
