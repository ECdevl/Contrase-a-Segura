# 🔐 ContraseñaMaestra (Password Master)

A secure password generator and manager built with Python Flet. Generate strong, customizable passwords and store them locally with associated service names for easy retrieval.

## ✨ Features

- **Secure Password Generation**: Create strong passwords with customizable length (up to 50 characters)
- **Service Organization**: Store passwords with associated service names (Google, GitHub, Steam, etc.)
- **Local Storage**: All passwords stored securely on your device using Flet's client storage
- **Easy Management**: View, copy, and delete stored passwords
- **Clean Dark UI**: Modern interface with gradient design
- **Cross-platform**: Works on Windows and Linux

## 🖼️ Screenshots

<img width="1251" height="657" alt="Screenshot_1" src="https://github.com/user-attachments/assets/519a2469-39cd-461c-b213-a043d0f386ef" />
*Password generation interface with length slider*

<img width="1248" height="662" alt="Screenshot_2" src="https://github.com/user-attachments/assets/bb1d76f5-64dd-4d1b-9d08-c43e7360e41b" />
*View and manage your stored passwords by service*

## 🛠️ Built With

- **Python** - Core programming language
- **Flet** - Cross-platform UI framework
- **Flet Client Storage** - Secure local data persistence

## 📥 Installation

### Windows
1. Download the latest release from [Releases](https://github.com/ECdevl/contrase-a-Segura/releases)
2. Extract the ZIP file
3. Run `ContraseñaMaestra.exe`

### Linux
1. Download the Linux build from [Releases](https://github.com/ECdevl/contrase-a-Segura/releases)
2. Make it executable: `chmod +x ContraseñaMaestra`
3. Run: `./ContraseñaMaestra`

## 🚀 Usage

### Generating a Password
1. Enter a service name (e.g., "Google", "GitHub", "Steam")
2. Adjust the password length using the slider (default: 50 characters)
3. Click "Crear Contraseña segura" to generate
4. Your password will be automatically saved and displayed

### Managing Passwords
- **View**: All saved passwords are displayed in cards organized by service
- **Copy**: Click on the password text to copy it to clipboard
- **Delete**: Click the trash icon to remove a stored password

## 💻 Running from Source

```bash
# Clone the repository
git clone https://github.com/ECdevl/contrase-a-Segura.git

# Navigate to project directory
cd contrase-a-Segura

# Install dependencies
pip install flet

# Run the application
flet run main.py
```

## 🔧 Technical Highlights

- **Random Password Generation**: Uses Python's `random` module with comprehensive character sets
- **Character Diversity**: Passwords include uppercase, lowercase, numbers, and special characters
- **No External Database**: All data stored locally using Flet's client storage
- **Lightweight**: Minimal dependencies for fast performance

## 🔒 Security Notes

- All passwords are stored locally on your device
- No data is transmitted over the internet
- The application does not have cloud sync capabilities
- For maximum security, ensure your device is encrypted and password-protected

## 📝 Future Improvements

- [ ] Password strength indicator
- [ ] Custom character set selection (exclude special chars, etc.)
- [ ] Export/Import password database
- [ ] Master password protection
- [ ] Password expiration reminders
- [ ] Search and filter functionality
- [ ] Multi-language support

## 👤 Author

**ECdevl**
- GitHub: [@ECdevl](https://github.com/ECdevl)
- LinkedIn: [Your LinkedIn Profile]

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project useful, please consider giving it a star!

## ⚠️ Disclaimer

This tool is provided for personal use. While it generates strong passwords, users are responsible for maintaining the security of their devices and stored passwords.
