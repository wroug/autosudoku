# AutoSudoku

A sudoku solver that solves a sudoku on your screen autonomously.

## Overview

AutoSudoku is an automated sudoku solving tool that:
- Captures sudoku grids from your screen
- Recognizes numbers using OCR (Optical Character Recognition)
- Solves the puzzle intelligently
- Automatically inputs the solution back into the sudoku game

## Features

- **Screen Recognition**: Captures and analyzes sudoku grids from any screen position
- **OCR Integration**: Uses advanced OCR (ddddocr) to read sudoku numbers
- **Intelligent Solving**: Uses the Hodoku solver for complex sudoku puzzles
- **3 Input speeds**: 
  - **Instant**: Immediate input (fastest)
  - **Fast**: Quick but inhumane movements (~4000 pixels/sec)
  - **Humane**: Natural mouse movement patterns (looks realistic)
- **Progress Tracking**: Real-time progress bar during solving and input

## Installation

### Option 1: Download Pre-built Binary (Recommended)

1. Go to [Releases](https://github.com/wroug/autosudoku/releases)
2. Download the latest `autosudoku` executable for your platform
3. Make it executable (Linux/Mac):
   ```bash
   chmod +x autosudoku
   ```
4. Run it:
   ```bash
   ./autosudoku
   ```

### Option 2: Run from Source

Requirements:
- Python 3.7+
- Java

```bash
git clone https://github.com/wroug/autosudoku.git
cd autosudoku
pip install -r requirements.txt
python menu.py
```

### System Requirements

- **Java**: Required for the Hodoku solver  
  If not installed, download from [adoptium.net](https://adoptium.net/)

### Supported Platforms

- Linux (x86_64)

### PLatforms Not Fully Tested Yet

- Windows (x86_64)
- macOS (Intel/Apple Silicon)

## Usage

### Basic Usage

Launch the application:
```bash
./autosudoku
```

### Workflow

1. **Launch the Menu**
   - Click "Start"

2. **Set Grid Boundaries**
   - Hover over the TOP-LEFT corner of your sudoku grid and press ENTER
   - Hover over the BOTTOM-RIGHT corner and press ENTER

3. **Choose Input Speed**
   - **Instant**: No delay between moves
   - **Fast**: ~4000 pixels/sec movement speed
   - **Humane**: Realistic human-like mouse movement

4. **Sit Back and Watch**
   - The solver will recognize the grid, solve it, and fill in all the answers automatically

## How It Works

1. **Capture**: Takes a screenshot of the specified sudoku area
2. **Recognize**: Uses OCR to read each cell's number
3. **Solve**: Passes the puzzle to Hodoku solver via Java
4. **Input**: Simulates mouse movements and keyboard input to fill in answers

## Dependencies

- **pyautogui** - Screen automation and mouse control
- **Pillow (PIL)** - Image processing
- **ddddocr** - OCR for number recognition
- **tqdm** - Progress bars
- **windmouse** - Natural mouse movement simulation

See `requirements.txt` for complete list.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

This project uses **HoDoKu** by Bernhard Hobiger, which is also licensed under GPL-3.0. See [ATTRIBUTION.md](ATTRIBUTION.md) for full credits.

## Attribution

- **Hodoku Sudoku Solver** - Bernhard Hobiger (http://hodoku.sourceforge.net/)

For detailed attribution and library licenses, see [ATTRIBUTION.md](ATTRIBUTION.md).

## Troubleshooting

### "Java not found" error
- Ensure Java is installed and added to your system PATH
- Test with: `java -version`
- Download from [adoptium.net](https://adoptium.net/) if needed

### OCR not recognizing numbers
- Ensure the sudoku grid is clearly visible on screen
- Try adjusting lighting or screen position
- Make sure numbers are in standard format

### Mouse input not working
- Ensure no other applications are capturing mouse events
- Try "Fast" or "Instant" modes instead of "Humane"
- Check that you have appropriate permissions to control mouse/keyboard

### Solver taking too long
- This is normal for difficult sudoku puzzles
- Progress bar will show the recognition process

## Future Improvements

- [ ] Support for more sudoku variants
- [ ] Cleaner UI

## Known Limitations

- Requires Java to be installed
- Works best with standard digital sudoku displays
- May struggle with low-quality; pixelated grids, or too colorful grids
- Requires proper boundary setup for accurate recognition

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## Author

**wroug** - [GitHub Profile](https://github.com/wroug)

## Disclaimer

This tool is for educational purposes and personal use. Use responsibly and respect the terms of service of any online sudoku platforms you use with this tool.

---

**Last Updated**: March 2026